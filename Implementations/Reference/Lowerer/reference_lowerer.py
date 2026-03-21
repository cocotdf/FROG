from __future__ import annotations

from typing import Any, Dict, List

from Implementations.Reference.common import DEFAULT_BACKEND_FAMILY, DEMO_ARTIFACT_VERSION, DerivedIR, LoweredForm, FrogPipelineError, ensure


def lower_for_backend_family(ir: DerivedIR, backend_family: str = DEFAULT_BACKEND_FAMILY) -> LoweredForm:
    ensure(backend_family == DEFAULT_BACKEND_FAMILY, stage="lower", error_code="unsupported_backend_family", message=f"This demo pipeline supports backend family '{DEFAULT_BACKEND_FAMILY}' only.")

    unit = ir.artifact["execution_unit"]
    objects = unit["objects"]

    operations: List[Dict[str, Any]] = []
    ui_binding_enabled = False

    for obj in objects:
        if obj["kind"] == "public_input_boundary":
            operations.append(
                {
                    "id": obj["id"].replace("obj:", "op:"),
                    "kind": "public_input",
                    "interface_port": obj["interface_port"],
                    "value_type": obj["value_type"],
                    "source_object": obj["id"],
                }
            )
        elif obj["kind"] == "primitive":
            ensure(obj["primitive_ref"] == "frog.core.add", stage="lower", error_code="unsupported_primitive", message="This demo lowerer supports frog.core.add only.")
            operations.append(
                {
                    "id": obj["id"].replace("obj:", "op:"),
                    "kind": "core_primitive_add",
                    "primitive_ref": obj["primitive_ref"],
                    "source_object": obj["id"],
                }
            )
        elif obj["kind"] == "public_output_boundary":
            operations.append(
                {
                    "id": obj["id"].replace("obj:", "op:"),
                    "kind": "public_output",
                    "interface_port": obj["interface_port"],
                    "value_type": obj["value_type"],
                    "source_object": obj["id"],
                }
            )
        elif obj["kind"] == "widget_value_participation":
            ui_binding_enabled = True
            if obj["widget_role"] == "control":
                op: Dict[str, Any] = {
                    "id": obj["id"].replace("obj:", "op:"),
                    "kind": "ui_value_input",
                    "widget_id": obj["widget_id"],
                    "widget_class": obj["widget_class"],
                    "value_type": obj["value_type"],
                    "ui_participation_kind": "widget_value",
                    "source_object": obj["id"],
                }
                if "default_value" in obj:
                    op["default_value"] = obj["default_value"]
                operations.append(op)
            elif obj["widget_role"] == "indicator":
                operations.append(
                    {
                        "id": obj["id"].replace("obj:", "op:"),
                        "kind": "ui_value_output",
                        "widget_id": obj["widget_id"],
                        "widget_class": obj["widget_class"],
                        "value_type": obj["value_type"],
                        "ui_participation_kind": "widget_value",
                        "source_object": obj["id"],
                    }
                )
            else:
                raise FrogPipelineError(stage="lower", error_code="unsupported_widget_role", message=f"Unsupported widget role during lowering: {obj['widget_role']}")
        else:
            raise FrogPipelineError(stage="lower", error_code="unsupported_ir_object", message=f"Unsupported IR object kind during lowering: {obj['kind']}")

    artifact = {
        "artifact_kind": "frog_lowered_form",
        "artifact_version": DEMO_ARTIFACT_VERSION,
        "source_ref": dict(ir.artifact["source_ref"]),
        "ir_ref": {
            "unit_id": unit["id"],
            "program_id": ir.artifact["validation_ref"]["program_id"],
        },
        "backend_family": backend_family,
        "assumptions": {
            "deterministic_step_execution": True,
            "ui_binding_enabled": ui_binding_enabled,
        },
        "units": [
            {
                "id": "lowered:main",
                "role": "entry_unit",
                "operations": operations,
                "connections": unit["connections"],
            }
        ],
        "diagnostics": [],
    }

    return LoweredForm(artifact=artifact)
