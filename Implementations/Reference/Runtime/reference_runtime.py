from __future__ import annotations

from typing import Any, Dict, Tuple

from Implementations.Reference.common import DEFAULT_BACKEND_FAMILY, BackendContract, DEMO_ARTIFACT_VERSION, FrogPipelineError, RuntimeResult, ensure


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
        values: Dict[Tuple[str, str], Any] = {}

        input_boundaries = [b for b in unit["boundaries"] if b["kind"] == "public_input"]
        for boundary in input_boundaries:
            name = boundary["name"]
            ensure(name in public_inputs, stage="run", error_code="missing_public_input", message=f"Missing public input: {name}")
            try:
                numeric_value = float(public_inputs[name])
            except (TypeError, ValueError) as exc:
                raise FrogPipelineError(stage="run", error_code="invalid_public_input", message=f"Public input '{name}' must be numeric for this demo runtime.") from exc

            for op in operations:
                if op["kind"] == "public_input" and op["interface_port"] == name:
                    values[(op["source_object"], "value")] = numeric_value
                    break

        ui_bindings = unit.get("ui_bindings", {"inputs": [], "outputs": []})
        for binding in ui_bindings.get("inputs", []):
            widget_id = binding["widget_id"]
            raw_value = public_inputs.get(widget_id, binding.get("default_value"))
            ensure(raw_value is not None, stage="run", error_code="missing_ui_input", message=f"Missing UI value input for widget '{widget_id}'.")

            try:
                numeric_value = float(raw_value)
            except (TypeError, ValueError) as exc:
                raise FrogPipelineError(stage="run", error_code="invalid_ui_input", message=f"UI value input '{widget_id}' must be numeric for this demo runtime.") from exc

            for op in operations:
                if op["kind"] == "ui_value_input" and op["widget_id"] == widget_id:
                    values[(op["source_object"], "value")] = numeric_value
                    break

        for connection in connections:
            src_object = connection["from"]["object"]
            src_port = connection["from"]["port"]
            dst_object = connection["to"]["object"]
            dst_port = connection["to"]["port"]
            if (src_object, src_port) in values:
                values[(dst_object, dst_port)] = values[(src_object, src_port)]

        add_ops = [op for op in operations if op["kind"] == "core_primitive_add"]
        ensure(len(add_ops) == 1, stage="run", error_code="unsupported_add_operation_count", message="Demo runtime expects exactly one add operation.")

        add_op = add_ops[0]
        add_object = add_op["source_object"]
        ensure((add_object, "a") in values and (add_object, "b") in values, stage="run", error_code="missing_primitive_inputs", message="Add primitive did not receive both inputs.")

        add_result = float(values[(add_object, "a")]) + float(values[(add_object, "b")])
        values[(add_object, "result")] = add_result

        for connection in connections:
            src_object = connection["from"]["object"]
            src_port = connection["from"]["port"]
            dst_object = connection["to"]["object"]
            dst_port = connection["to"]["port"]
            if (src_object, src_port) in values:
                values[(dst_object, dst_port)] = values[(src_object, src_port)]

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
            "diagnostics": [],
        }

        return RuntimeResult(artifact=artifact)


def create_runtime_for_family(backend_family: str = DEFAULT_BACKEND_FAMILY) -> ReferenceHostRuntime:
    return ReferenceHostRuntime(backend_family=backend_family)
