from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, Tuple

from Implementations.Reference.common import DEFAULT_BACKEND_FAMILY, BackendContract, DEMO_ARTIFACT_VERSION, FrogPipelineError, RuntimeResult, ensure


def _coerce_runtime_value(raw_value: Any, value_type: str, *, stage: str, label: str) -> Any:
    if value_type == "f64":
        try:
            return float(raw_value)
        except (TypeError, ValueError) as exc:
            raise FrogPipelineError(stage=stage, error_code="invalid_runtime_value", message=f"{label} must be numeric for type f64.") from exc
    if value_type == "string":
        if isinstance(raw_value, str):
            return raw_value
        if raw_value is None:
            raise FrogPipelineError(stage=stage, error_code="invalid_runtime_value", message=f"{label} must be a string.")
        return str(raw_value)
    raise FrogPipelineError(stage=stage, error_code="unsupported_runtime_type", message=f"Unsupported runtime type in demo slice: {value_type}")


class ReferenceHostRuntime:
    def __init__(self, backend_family: str = DEFAULT_BACKEND_FAMILY):
        ensure(backend_family == DEFAULT_BACKEND_FAMILY, stage="runtime-create", error_code="unsupported_backend_family", message=f"Unsupported runtime family: {backend_family}")
        self.backend_family = backend_family

    def accept_contract(self, contract: BackendContract) -> Dict[str, Any]:
        artifact = contract.artifact
        ensure(artifact["artifact_kind"] == "frog_backend_contract", stage="runtime-accept", error_code="invalid_contract_kind", message="Runtime expected a frog_backend_contract artifact.")
        ensure(artifact["backend_family"] == self.backend_family, stage="runtime-accept", error_code="backend_family_mismatch", message="Runtime backend family mismatch.")
        ensure(len(artifact["units"]) == 1, stage="runtime-accept", error_code="unsupported_unit_count", message="Demo runtime expects exactly one contract unit.")
        unit = artifact["units"][0]
        ensure(unit.get("role") == "entry_unit", stage="runtime-accept", error_code="unsupported_unit_role", message="Demo runtime expects one entry_unit.")
        payload = unit.get("implementation_payload")
        ensure(isinstance(payload, dict) and payload.get("kind") == "demo_dataflow_plan", stage="runtime-accept", error_code="missing_demo_payload", message="Demo runtime requires a demo_dataflow_plan payload.")
        return {"status": "ok", "unit_ids": [unit["id"]]}

    def execute(self, contract: BackendContract, public_inputs: Dict[str, Any]) -> RuntimeResult:
        unit = contract.artifact["units"][0]
        payload = unit["implementation_payload"]
        operations = payload["operations"]
        connections = payload["connections"]
        ui_declarations = payload.get("ui_declarations", {"widgets": []})
        ui_widgets = {widget["id"]: deepcopy(widget) for widget in ui_declarations.get("widgets", [])}

        values: Dict[Tuple[str, str], Any] = {}
        executed_ops = set()
        ui_effects = []

        input_boundaries = [b for b in unit["boundaries"] if b["kind"] == "public_input"]
        for boundary in input_boundaries:
            name = boundary["name"]
            ensure(name in public_inputs, stage="run", error_code="missing_public_input", message=f"Missing public input: {name}")
            runtime_value = _coerce_runtime_value(public_inputs[name], boundary["value_type"], stage="run", label=f"Public input '{name}'")
            for op in operations:
                if op["kind"] == "public_input" and op["interface_port"] == name:
                    values[(op["source_object"], "value")] = runtime_value
                    break

        ui_bindings = unit.get("ui_bindings", {"inputs": [], "outputs": []})
        for binding in ui_bindings.get("inputs", []):
            widget_id = binding["widget_id"]
            raw_value = public_inputs.get(widget_id, binding.get("default_value"))
            ensure(raw_value is not None, stage="run", error_code="missing_ui_input", message=f"Missing UI value input for widget '{widget_id}'.")
            runtime_value = _coerce_runtime_value(raw_value, binding["value_type"], stage="run", label=f"UI value input '{widget_id}'")
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
                    if key_result not in values and key_a in values and key_b in values:
                        values[key_result] = float(values[key_a]) + float(values[key_b])
                        progressed = True
                elif op_kind == "ui_widget_reference":
                    key_ref = (source_object, "ref")
                    if key_ref not in values:
                        widget_id = op["widget_id"]
                        ensure(widget_id in ui_widgets, stage="run", error_code="missing_runtime_widget", message=f"Runtime widget '{widget_id}' is missing from UI declarations.")
                        values[key_ref] = {"widget_id": widget_id, "handle_kind": "reference_host_widget_handle"}
                        progressed = True
                elif op_kind == "ui_property_write" and op["id"] not in executed_ops:
                    key_ref = (source_object, "ref")
                    key_value = (source_object, "value")
                    if key_ref in values and key_value in values:
                        ref_handle = values[key_ref]
                        widget_id = ref_handle["widget_id"]
                        ensure(widget_id in ui_widgets, stage="run", error_code="missing_runtime_widget", message=f"Runtime widget '{widget_id}' is missing from UI declarations.")
                        widget = ui_widgets[widget_id]
                        part_name = op["widget_member"]["part"]
                        member_name = op["widget_member"]["member"]
                        ensure(part_name in widget.get("parts", {}), stage="run", error_code="missing_runtime_widget_part", message=f"Widget '{widget_id}' does not contain part '{part_name}' at runtime.")
                        part = widget["parts"][part_name]
                        props = part.setdefault("props", {})
                        props[member_name] = values[key_value]
                        ui_effects.append({
                            "kind": "property_write",
                            "widget_id": widget_id,
                            "part": part_name,
                            "member": member_name,
                            "value": values[key_value],
                        })
                        executed_ops.add(op["id"])
                        progressed = True

        public_outputs = [b for b in unit["boundaries"] if b["kind"] == "public_output"]
        public_output_values: Dict[str, Any] = {}
        for boundary in public_outputs:
            output_name = boundary["name"]
            matched = False
            for op in operations:
                if op["kind"] == "public_output" and op["interface_port"] == output_name:
                    source_object = op["source_object"]
                    ensure((source_object, "value") in values, stage="run", error_code="missing_public_output_value", message=f"Public output '{output_name}' did not receive a value.")
                    public_output_values[output_name] = values[(source_object, "value")]
                    matched = True
                    break
            ensure(matched, stage="run", error_code="missing_public_output_operation", message=f"No public_output operation found for '{output_name}'.")

        ui_output_values: Dict[str, Any] = {}
        for binding in ui_bindings.get("outputs", []):
            widget_id = binding["widget_id"]
            matched = False
            for op in operations:
                if op["kind"] == "ui_value_output" and op["widget_id"] == widget_id:
                    source_object = op["source_object"]
                    ensure((source_object, "value") in values, stage="run", error_code="missing_ui_output_value", message=f"UI output '{widget_id}' did not receive a value.")
                    ui_output_values[widget_id] = values[(source_object, "value")]
                    matched = True
                    break
            ensure(matched, stage="run", error_code="missing_ui_output_operation", message=f"No ui_value_output operation found for '{widget_id}'.")

        artifact = {
            "artifact_kind": "frog_runtime_result",
            "artifact_version": DEMO_ARTIFACT_VERSION,
            "status": "ok",
            "contract_ref": {
                "unit_ids": [unit["id"]],
                "backend_family": contract.artifact["backend_family"],
            },
            "execution_summary": {
                "mode": "deterministic_step_execution",
                "executed_unit": unit["id"],
            },
            "outputs": {
                "public": public_output_values,
                "ui": ui_output_values,
            },
            "ui_state": {
                "widgets": ui_widgets,
            },
            "ui_effects": ui_effects,
            "diagnostics": [],
        }

        return RuntimeResult(artifact=artifact)


def create_runtime_for_family(backend_family: str = DEFAULT_BACKEND_FAMILY) -> ReferenceHostRuntime:
    return ReferenceHostRuntime(backend_family=backend_family)
