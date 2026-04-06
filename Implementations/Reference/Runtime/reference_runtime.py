from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List, Optional, Tuple

from Implementations.Reference.common import (
    DEFAULT_BACKEND_FAMILY,
    DEMO_ARTIFACT_VERSION,
    BackendContract,
    FrogPipelineError,
    RuntimeResult,
    ensure,
)


def _coerce_runtime_value(raw_value: Any, value_type: str, *, stage: str, label: str) -> Any:
    if value_type == "f64":
        try:
            return float(raw_value)
        except (TypeError, ValueError) as exc:
            raise FrogPipelineError(
                stage=stage,
                error_code="invalid_runtime_value",
                message=f"{label} must be numeric for type f64.",
            ) from exc

    if value_type == "u16":
        try:
            value = int(raw_value)
        except (TypeError, ValueError) as exc:
            raise FrogPipelineError(
                stage=stage,
                error_code="invalid_runtime_value",
                message=f"{label} must be an integer-compatible value for type u16.",
            ) from exc

        if value < 0 or value > 65535:
            raise FrogPipelineError(
                stage=stage,
                error_code="invalid_runtime_value_range",
                message=f"{label} must be within u16 range [0, 65535].",
            )

        return value

    if value_type == "i32":
        try:
            value = int(raw_value)
        except (TypeError, ValueError) as exc:
            raise FrogPipelineError(
                stage=stage,
                error_code="invalid_runtime_value",
                message=f"{label} must be an integer-compatible value for type i32.",
            ) from exc

        if value < -(2**31) or value > (2**31 - 1):
            raise FrogPipelineError(
                stage=stage,
                error_code="invalid_runtime_value_range",
                message=f"{label} must be within i32 range.",
            )

        return value

    if value_type == "string":
        if isinstance(raw_value, str):
            return raw_value
        if raw_value is None:
            raise FrogPipelineError(
                stage=stage,
                error_code="invalid_runtime_value",
                message=f"{label} must be a string.",
            )
        return str(raw_value)

    if value_type == "frog.ui.color":
        if not isinstance(raw_value, str):
            raise FrogPipelineError(
                stage=stage,
                error_code="invalid_runtime_value",
                message=f"{label} must be a string for type frog.ui.color.",
            )
        return raw_value

    raise FrogPipelineError(
        stage=stage,
        error_code="unsupported_runtime_type",
        message=f"Unsupported runtime type in reference slice: {value_type}",
    )


def _add_typed_values(a: Any, b: Any, value_type: str) -> Any:
    if value_type == "f64":
        return float(a) + float(b)

    if value_type == "u16":
        total = int(a) + int(b)
        if total < 0:
            total = 0
        if total > 65535:
            total = 65535
        return total

    if value_type == "i32":
        total = int(a) + int(b)
        if total < -(2**31):
            total = -(2**31)
        if total > (2**31 - 1):
            total = 2**31 - 1
        return total

    raise FrogPipelineError(
        stage="run",
        error_code="unsupported_add_type",
        message=f"Unsupported add type for runtime execution: {value_type}",
    )


class ReferenceHostRuntime:
    def __init__(self, backend_family: str = DEFAULT_BACKEND_FAMILY):
        ensure(
            backend_family == DEFAULT_BACKEND_FAMILY,
            stage="runtime-create",
            error_code="unsupported_backend_family",
            message=f"Unsupported runtime family: {backend_family}",
        )
        self.backend_family = backend_family

    def accept_contract(self, contract: BackendContract) -> Dict[str, Any]:
        artifact = contract.artifact

        ensure(
            artifact["artifact_kind"] == "frog_backend_contract",
            stage="runtime-accept",
            error_code="invalid_contract_kind",
            message="Runtime expected a frog_backend_contract artifact.",
        )
        ensure(
            artifact["backend_family"] == self.backend_family,
            stage="runtime-accept",
            error_code="backend_family_mismatch",
            message="Runtime backend family mismatch.",
        )
        ensure(
            len(artifact["units"]) == 1,
            stage="runtime-accept",
            error_code="unsupported_unit_count",
            message="Reference runtime expects exactly one contract unit.",
        )

        unit = artifact["units"][0]
        ensure(
            unit.get("role") == "entry_unit",
            stage="runtime-accept",
            error_code="unsupported_unit_role",
            message="Reference runtime expects one entry_unit.",
        )

        payload = unit.get("implementation_payload")
        ensure(
            isinstance(payload, dict) and payload.get("kind") == "demo_dataflow_plan",
            stage="runtime-accept",
            error_code="missing_demo_payload",
            message="Reference runtime requires a demo_dataflow_plan payload.",
        )

        return {
            "status": "ok",
            "unit_ids": [unit["id"]],
        }

    def execute(self, contract: BackendContract, public_inputs: Dict[str, Any]) -> RuntimeResult:
        unit = contract.artifact["units"][0]
        payload = unit["implementation_payload"]

        operations = payload["operations"]
        connections = payload["connections"]
        ui_declarations = payload.get("ui_declarations", {"widgets": []})
        ui_widgets = {widget["id"]: deepcopy(widget) for widget in ui_declarations.get("widgets", [])}

        values: Dict[Tuple[str, str], Any] = {}
        executed_ops = set()
        ui_effects: List[Dict[str, Any]] = []
        state_values: Dict[str, Any] = {}

        input_boundaries = [b for b in unit.get("boundaries", []) if b["kind"] == "public_input"]
        for boundary in input_boundaries:
            name = boundary["name"]
            ensure(
                name in public_inputs,
                stage="run",
                error_code="missing_public_input",
                message=f"Missing public input: {name}",
            )

            runtime_value = _coerce_runtime_value(
                public_inputs[name],
                boundary["value_type"],
                stage="run",
                label=f"Public input '{name}'",
            )

            for op in operations:
                if op["kind"] == "public_input" and op["interface_port"] == name:
                    values[(op["source_object"], "value")] = runtime_value
                    break

        ui_bindings = unit.get("ui_bindings", {"inputs": [], "outputs": []})

        for binding in ui_bindings.get("inputs", []):
            widget_id = binding["widget_id"]
            raw_value = public_inputs.get(widget_id, binding.get("default_value"))

            ensure(
                raw_value is not None,
                stage="run",
                error_code="missing_ui_input",
                message=f"Missing UI value input for widget '{widget_id}'.",
            )

            runtime_value = _coerce_runtime_value(
                raw_value,
                binding["value_type"],
                stage="run",
                label=f"UI value input '{widget_id}'",
            )

            for op in operations:
                if op["kind"] == "ui_value_input" and op["widget_id"] == widget_id:
                    values[(op["source_object"], "value")] = runtime_value
                    break

        progressed = True
        while progressed:
            progressed = False

            for connection in connections:
                src_object = connection["from"]["object"]
                src_port = connection["from"]["port"]
                dst_object = connection["to"]["object"]
                dst_port = connection["to"]["port"]

                if (src_object, src_port) in values and (dst_object, dst_port) not in values:
                    values[(dst_object, dst_port)] = values[(src_object, src_port)]
                    progressed = True

            for op in operations:
                op_kind = op["kind"]
                source_object = op["source_object"]

                if op_kind == "core_primitive_add":
                    key_a = (source_object, "a")
                    key_b = (source_object, "b")
                    key_result = (source_object, "result")
                    result_type = op.get("value_type", "f64")

                    if key_result not in values and key_a in values and key_b in values:
                        values[key_result] = _add_typed_values(
                            values[key_a],
                            values[key_b],
                            result_type,
                        )
                        progressed = True

                elif op_kind == "state_init":
                    state_id = op["state_id"]
                    key_initial = (source_object, "initial")
                    key_out = (source_object, "out")
                    value_type = op["value_type"]

                    if state_id not in state_values and key_initial in values:
                        state_values[state_id] = _coerce_runtime_value(
                            values[key_initial],
                            value_type,
                            stage="run",
                            label=f"Initial state '{state_id}'",
                        )
                        values[key_out] = state_values[state_id]
                        progressed = True

                elif op_kind == "state_read":
                    state_id = op["state_id"]
                    key_out = (source_object, "out")

                    if key_out not in values and state_id in state_values:
                        values[key_out] = state_values[state_id]
                        progressed = True

                elif op_kind == "state_write" and op["id"] not in executed_ops:
                    state_id = op["state_id"]
                    key_in = (source_object, "in")
                    if key_in in values:
                        state_values[state_id] = values[key_in]
                        executed_ops.add(op["id"])
                        progressed = True

                elif op_kind == "counted_loop_execute" and op["id"] not in executed_ops:
                    key_input_value = (source_object, "loop_input_value")
                    key_initial_state = (source_object, "loop_initial_state")
                    key_output = (source_object, "loop_final_state")

                    if key_input_value in values and key_initial_state in values:
                        value_type = op["value_type"]
                        iteration_count = int(op["iteration_count"])
                        current_state = _coerce_runtime_value(
                            values[key_initial_state],
                            value_type,
                            stage="run",
                            label="Loop initial state",
                        )
                        step_value = _coerce_runtime_value(
                            values[key_input_value],
                            value_type,
                            stage="run",
                            label="Loop input value",
                        )

                        for _ in range(iteration_count):
                            current_state = _add_typed_values(current_state, step_value, value_type)

                        values[key_output] = current_state
                        if "state_id" in op:
                            state_values[op["state_id"]] = current_state

                        executed_ops.add(op["id"])
                        progressed = True

                elif op_kind == "ui_widget_reference":
                    key_ref = (source_object, "ref")
                    if key_ref not in values:
                        widget_id = op["widget_id"]
                        ensure(
                            widget_id in ui_widgets,
                            stage="run",
                            error_code="missing_runtime_widget",
                            message=f"Runtime widget '{widget_id}' is missing from UI declarations.",
                        )
                        values[key_ref] = {
                            "widget_id": widget_id,
                            "handle_kind": "reference_host_widget_handle",
                        }
                        progressed = True

                elif op_kind == "ui_property_write" and op["id"] not in executed_ops:
                    key_ref = (source_object, "ref")
                    key_value = (source_object, "value")

                    if key_ref in values and key_value in values:
                        ref_handle = values[key_ref]
                        widget_id = ref_handle["widget_id"]

                        ensure(
                            widget_id in ui_widgets,
                            stage="run",
                            error_code="missing_runtime_widget",
                            message=f"Runtime widget '{widget_id}' is missing from UI declarations.",
                        )

                        widget = ui_widgets[widget_id]
                        member_descriptor = op["widget_member"]
                        member_name = member_descriptor["member"]
                        part_name = member_descriptor.get("part")

                        if part_name is None:
                            props = widget.setdefault("props", {})
                            props[member_name] = values[key_value]
                            ui_effects.append(
                                {
                                    "widget_id": widget_id,
                                    "member": member_name,
                                    "effect_kind": "property_write_applied",
                                    "value": values[key_value],
                                }
                            )
                        else:
                            ensure(
                                part_name in widget.get("parts", {}),
                                stage="run",
                                error_code="missing_runtime_widget_part",
                                message=f"Widget '{widget_id}' does not contain part '{part_name}' at runtime.",
                            )
                            part = widget["parts"][part_name]
                            props = part.setdefault("props", {})
                            props[member_name] = values[key_value]
                            ui_effects.append(
                                {
                                    "widget_id": widget_id,
                                    "part": part_name,
                                    "member": member_name,
                                    "effect_kind": "property_write_applied",
                                    "value": values[key_value],
                                }
                            )

                        executed_ops.add(op["id"])
                        progressed = True

            # propagate again after operations that produced new values
            for connection in connections:
                src_object = connection["from"]["object"]
                src_port = connection["from"]["port"]
                dst_object = connection["to"]["object"]
                dst_port = connection["to"]["port"]

                if (src_object, src_port) in values and (dst_object, dst_port) not in values:
                    values[(dst_object, dst_port)] = values[(src_object, src_port)]
                    progressed = True

        public_outputs = [b for b in unit.get("boundaries", []) if b["kind"] == "public_output"]
        public_output_values: Dict[str, Any] = {}

        for boundary in public_outputs:
            output_name = boundary["name"]
            matched = False

            for op in operations:
                if op["kind"] == "public_output" and op["interface_port"] == output_name:
                    source_object = op["source_object"]
                    ensure(
                        (source_object, "value") in values,
                        stage="run",
                        error_code="missing_public_output_value",
                        message=f"Public output '{output_name}' did not receive a value.",
                    )
                    public_output_values[output_name] = values[(source_object, "value")]
                    matched = True
                    break

            ensure(
                matched,
                stage="run",
                error_code="missing_public_output_operation",
                message=f"No public_output operation found for '{output_name}'.",
            )

        ui_output_values: Dict[str, Any] = {}
        for binding in ui_bindings.get("outputs", []):
            widget_id = binding["widget_id"]
            matched = False

            for op in operations:
                if op["kind"] == "ui_value_output" and op["widget_id"] == widget_id:
                    source_object = op["source_object"]
                    ensure(
                        (source_object, "value") in values,
                        stage="run",
                        error_code="missing_ui_output_value",
                        message=f"UI output '{widget_id}' did not receive a value.",
                    )
                    ui_output_values[f"{widget_id}.value"] = values[(source_object, "value")]

                    if widget_id in ui_widgets:
                        widget_props = ui_widgets[widget_id].setdefault("props", {})
                        widget_props["value"] = values[(source_object, "value")]

                    matched = True
                    break

            ensure(
                matched,
                stage="run",
                error_code="missing_ui_output_operation",
                message=f"No ui_value_output operation found for '{widget_id}'.",
            )

        artifact = {
            "artifact_kind": "frog_runtime_result",
            "artifact_version": DEMO_ARTIFACT_VERSION,
            "status": "ok",
            "contract_ref": {
                "unit_ids": [unit["id"]],
                "backend_family": contract.artifact["backend_family"],
            },
            "execution_summary": {
                "mode": payload.get("execution_mode", "deterministic_step_execution"),
                "executed_unit": unit["id"],
                "iteration_count": payload.get("iteration_count"),
                "state_model": payload.get("state_model"),
            },
            "outputs": {
                "public": public_output_values,
                "ui": ui_output_values,
                "ui_effects": ui_effects,
                "state": state_values,
            },
            "ui_state": {
                "widgets": ui_widgets,
            },
            "diagnostics": [],
        }

        return RuntimeResult(artifact=artifact)


def create_runtime_for_family(backend_family: str = DEFAULT_BACKEND_FAMILY) -> ReferenceHostRuntime:
    return ReferenceHostRuntime(backend_family=backend_family)
