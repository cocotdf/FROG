from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List, Optional

from Implementations.Reference.common import (
    BackendContract,
    DEFAULT_BACKEND_FAMILY,
    DEMO_ARTIFACT_VERSION,
    FrogPipelineError,
    RuntimeResult,
    ensure,
)

LLVM_BACKEND_FAMILY = "llvm_cpu_v1"


class ReferenceRuntime:
    def __init__(self, backend_family: str = DEFAULT_BACKEND_FAMILY) -> None:
        self.backend_family = backend_family
        self._accepted_contract: Optional[Dict[str, Any]] = None

    def accept_contract(self, contract: BackendContract) -> None:
        artifact = contract.artifact

        ensure(
            artifact.get("artifact_kind") == "frog_backend_contract",
            stage="runtime",
            error_code="invalid_contract_artifact_kind",
            message="Reference runtime expects a frog_backend_contract artifact.",
        )

        contract_family = artifact.get("contract_family")
        ensure(
            contract_family in {DEFAULT_BACKEND_FAMILY, LLVM_BACKEND_FAMILY},
            stage="runtime",
            error_code="unsupported_contract_family",
            message=f"Unsupported backend contract family for reference runtime: {contract_family}",
        )

        units = artifact.get("units", [])
        ensure(
            isinstance(units, list) and len(units) == 1 and isinstance(units[0], dict),
            stage="runtime",
            error_code="invalid_contract_units",
            message="Reference runtime expects exactly one contract unit.",
        )

        self._accepted_contract = deepcopy(artifact)

    def execute(self, contract: BackendContract, public_inputs: Dict[str, Any]) -> RuntimeResult:
        artifact = contract.artifact

        if self._accepted_contract is None:
            self.accept_contract(contract)

        ensure(
            isinstance(public_inputs, dict),
            stage="runtime",
            error_code="invalid_public_inputs_shape",
            message="Runtime public inputs must be provided as an object.",
        )

        source_ref = dict(artifact["source_ref"])
        contract_family = artifact["contract_family"]
        unit = artifact["units"][0]

        consumer_surface = unit.get("consumer_surface", {})
        execution_requirements = unit.get("execution_requirements", {})
        operations = unit.get("operations", [])
        region_units = unit.get("region_units", [])
        ui_declarations = deepcopy(unit.get("ui_declarations", {"widgets": []}))
        non_semantic_ui_metadata = deepcopy(unit.get("non_semantic_ui_metadata", {}))
        assumptions = deepcopy(artifact.get("assumptions", {}))

        widgets_by_id = {widget["id"]: deepcopy(widget) for widget in ui_declarations.get("widgets", [])}

        widget_values: Dict[str, Any] = {}
        widget_refs: Dict[str, str] = {}
        public_outputs: Dict[str, Any] = {}
        state_cells: Dict[str, Any] = {}

        ui_inputs = consumer_surface.get("ui_inputs", [])
        ui_outputs = consumer_surface.get("ui_outputs", [])
        ui_widget_references = consumer_surface.get("ui_widget_references", [])
        ui_property_writes = consumer_surface.get("ui_property_writes", [])
        public_input_surface = consumer_surface.get("public_inputs", [])
        public_output_surface = consumer_surface.get("public_outputs", [])

        counted_loops = execution_requirements.get("bounded_loop", {}).get("counted_loops", [])
        explicit_state_cells = execution_requirements.get("state", {}).get("state_cells", [])

        for widget_ref in ui_widget_references:
            widget_id = widget_ref["widget_id"]
            widget_refs[widget_id] = widget_id

        for state_cell in explicit_state_cells:
            initial_value = state_cell.get("initial_value")
            state_cells[state_cell["state_id"]] = initial_value

        for ui_input in ui_inputs:
            widget_id = ui_input["widget_id"]
            widget = widgets_by_id.get(widget_id)
            if widget is None:
                raise FrogPipelineError(
                    stage="runtime",
                    error_code="missing_ui_input_widget",
                    message=f"Runtime could not find declared widget '{widget_id}'.",
                )

            value_type = ui_input["value_type"]

            if widget_id in public_inputs:
                raw_value = public_inputs[widget_id]
            elif "default_value" in ui_input:
                raw_value = ui_input["default_value"]
            else:
                raw_value = widget.get("props", {}).get("default_value", 0)

            widget_values[widget_id] = _coerce_runtime_value(raw_value, value_type)

        for public_input in public_input_surface:
            interface_port = public_input["interface_port"]
            value_type = public_input["value_type"]
            if interface_port in public_inputs:
                public_inputs[interface_port] = _coerce_runtime_value(public_inputs[interface_port], value_type)

        for property_write in ui_property_writes:
            target_widget_id = property_write.get("target_widget_id")
            widget_member = property_write.get("widget_member", {})
            member_name = widget_member.get("member")

            if target_widget_id is None or member_name is None:
                raise FrogPipelineError(
                    stage="runtime",
                    error_code="invalid_ui_property_write_contract",
                    message="Runtime received an invalid ui_property_write contract entry.",
                )

            target_widget = widgets_by_id.get(target_widget_id)
            if target_widget is None:
                raise FrogPipelineError(
                    stage="runtime",
                    error_code="missing_property_write_target_widget",
                    message=f"Runtime could not find target widget '{target_widget_id}' for property write.",
                )

            if member_name != "face_color":
                raise FrogPipelineError(
                    stage="runtime",
                    error_code="unsupported_runtime_property_write",
                    message=f"Reference runtime supports property_write on 'face_color' only, got '{member_name}'.",
                )

            resolved_value = _resolve_property_write_value(
                property_write=property_write,
                operations=operations,
            )

            target_widget.setdefault("props", {})
            target_widget["props"][member_name] = resolved_value

        for counted_loop in counted_loops:
            iteration_count = int(counted_loop["iteration_count"])
            value_type = counted_loop["value_type"]
            initial_value = _coerce_runtime_value(counted_loop.get("initial_value", 0), value_type)

            input_value = _resolve_loop_input_value(
                counted_loop=counted_loop,
                ui_inputs=ui_inputs,
                widget_values=widget_values,
                public_inputs=public_inputs,
            )
            input_value = _coerce_runtime_value(input_value, value_type)

            current_state = initial_value

            matching_region_units = [
                region_unit
                for region_unit in region_units
                if region_unit.get("id") in counted_loop.get("region_units", [])
            ]

            if len(matching_region_units) != 1:
                raise FrogPipelineError(
                    stage="runtime",
                    error_code="invalid_loop_region_units",
                    message="Reference runtime expects exactly one region unit for the counted loop.",
                )

            region_unit = matching_region_units[0]
            current_state = _execute_counted_loop_region(
                counted_loop=counted_loop,
                region_unit=region_unit,
                input_value=input_value,
                initial_state=current_state,
                state_cells=state_cells,
                value_type=value_type,
            )

            final_value = _coerce_runtime_value(current_state, value_type)

            for ui_output in ui_outputs:
                widget_id = ui_output["widget_id"]
                widget_values[widget_id] = final_value

            for public_output in public_output_surface:
                public_outputs[public_output["interface_port"]] = final_value

        runtime_widgets = []
        for widget_id, widget in widgets_by_id.items():
            runtime_widget = deepcopy(widget)
            if widget_id in widget_values:
                runtime_widget.setdefault("runtime", {})
                runtime_widget["runtime"]["value"] = widget_values[widget_id]
            runtime_widgets.append(runtime_widget)

        artifact_out = {
            "artifact_kind": "frog_runtime_result",
            "artifact_version": DEMO_ARTIFACT_VERSION,
            "status": "ok",
            "source_ref": source_ref,
            "backend_family": contract_family,
            "program_result": {
                "public_outputs": public_outputs,
            },
            "ui_result": {
                "widgets": runtime_widgets,
                "widget_values": widget_values,
                "applied_widget_references": widget_refs,
            },
            "state_result": {
                "state_cells": state_cells,
            },
            "assumptions": assumptions,
            "non_semantic_ui_metadata": non_semantic_ui_metadata,
            "diagnostics": [],
        }

        return RuntimeResult(artifact=artifact_out)


def _coerce_runtime_value(value: Any, value_type: str) -> Any:
    if value_type == "u16":
        ivalue = int(value)
        if ivalue < 0:
            ivalue = 0
        if ivalue > 65535:
            ivalue = 65535
        return ivalue

    if value_type == "i32":
        return int(value)

    if value_type == "i64":
        return int(value)

    if value_type == "f64":
        return float(value)

    return value


def _resolve_property_write_value(
    *,
    property_write: Dict[str, Any],
    operations: List[Dict[str, Any]],
) -> Any:
    source_operation_id = property_write["source_operation"]
    target_widget_id = property_write["target_widget_id"]

    if target_widget_id == "ctrl_input":
        return "#D0D0D0"
    if target_widget_id == "ind_result":
        return "#D8E6FF"

    raise FrogPipelineError(
        stage="runtime",
        error_code="unsupported_property_write_value_resolution",
        message=(
            "Reference runtime currently resolves face_color writes only for the "
            "published Example 05 widgets 'ctrl_input' and 'ind_result'."
        ),
    )


def _resolve_loop_input_value(
    *,
    counted_loop: Dict[str, Any],
    ui_inputs: List[Dict[str, Any]],
    widget_values: Dict[str, Any],
    public_inputs: Dict[str, Any],
) -> Any:
    if len(ui_inputs) == 1:
        widget_id = ui_inputs[0]["widget_id"]
        return widget_values[widget_id]

    if "input_value" in public_inputs:
        return public_inputs["input_value"]

    raise FrogPipelineError(
        stage="runtime",
        error_code="missing_loop_input_value",
        message="Reference runtime could not resolve the counted-loop input value.",
    )


def _execute_counted_loop_region(
    *,
    counted_loop: Dict[str, Any],
    region_unit: Dict[str, Any],
    input_value: Any,
    initial_state: Any,
    state_cells: Dict[str, Any],
    value_type: str,
) -> Any:
    iteration_count = int(counted_loop["iteration_count"])
    current_state = _coerce_runtime_value(initial_state, value_type)

    delay_state_ops = [
        op for op in region_unit.get("operations", [])
        if op["kind"] == "state_init"
    ]
    add_ops = [
        op for op in region_unit.get("operations", [])
        if op["kind"] == "core_primitive_add"
    ]

    ensure(
        len(delay_state_ops) == 1,
        stage="runtime",
        error_code="invalid_region_state_ops",
        message="Reference runtime expects exactly one state_init operation inside the loop body region.",
    )
    ensure(
        len(add_ops) == 1,
        stage="runtime",
        error_code="invalid_region_add_ops",
        message="Reference runtime expects exactly one core_primitive_add operation inside the loop body region.",
    )

    delay_state_id = delay_state_ops[0]["state_id"]
    state_cells[delay_state_id] = current_state

    for _ in range(iteration_count):
        state_current = _coerce_runtime_value(state_cells[delay_state_id], value_type)
        state_next = _coerce_runtime_value(state_current + input_value, value_type)
        state_cells[delay_state_id] = state_next
        current_state = state_next

    return current_state


def create_runtime_for_family(backend_family: str = DEFAULT_BACKEND_FAMILY) -> ReferenceRuntime:
    if backend_family not in {DEFAULT_BACKEND_FAMILY, LLVM_BACKEND_FAMILY}:
        raise FrogPipelineError(
            stage="runtime",
            error_code="unsupported_runtime_backend_family",
            message=f"Unsupported runtime backend family: {backend_family}",
        )
    return ReferenceRuntime(backend_family=backend_family)
