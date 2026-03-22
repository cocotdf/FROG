from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List

from Implementations.Reference.common import DEFAULT_BACKEND_FAMILY, DEMO_ARTIFACT_VERSION, DerivedIR, FrogPipelineError, LoweredForm, ensure


def lower_for_backend_family(ir: DerivedIR, backend_family: str = DEFAULT_BACKEND_FAMILY) -> LoweredForm:
    ensure(backend_family == DEFAULT_BACKEND_FAMILY, stage="lower", error_code="unsupported_backend_family", message=f"This demo pipeline supports backend family '{DEFAULT_BACKEND_FAMILY}' only.")

    unit = ir.artifact["execution_unit"]
    objects = unit["objects"]

    operations: List[Dict[str, Any]] = []
    has_natural_ui = False
    has_object_ui = False

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
            if obj["primitive_ref"] == "frog.core.add":
                operations.append(
                    {
                        "id": obj["id"].replace("obj:", "op:"),
                        "kind": "core_primitive_add",
                        "primitive_ref": obj["primitive_ref"],
                        "source_object": obj["id"],
                    }
                )
            elif obj["primitive_ref"] == "frog.ui.property_write":
                has_object_ui = True
                operations.append(
                    {
                        "id": obj["id"].replace("obj:", "op:"),
                        "kind": "ui_property_write",
                        "primitive_ref": obj["primitive_ref"],
                        "widget_member": deepcopy(obj["widget_member"]),
                        "target_widget_id": obj.get("target_widget_id"),
                        "target_widget_class": obj.get("target_widget_class"),
                        "value_type": obj["ports"][1]["value_type"],
                        "source_object": obj["id"],
                    }
                )
            else:
                raise FrogPipelineError(stage="lower", error_code="unsupported_primitive", message=f"This demo lowerer does not support primitive '{obj['primitive_ref']}'.")
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
            has_natural_ui = True
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
        elif obj["kind"] == "widget_reference_participation":
            has_object_ui = True
            operations.append(
                {
                    "id": obj["id"].replace("obj:", "op:"),
                    "kind": "ui_widget_reference",
                    "widget_id": obj["widget_id"],
                    "widget_role": obj["widget_role"],
                    "widget_class": obj["widget_class"],
                    "ui_participation_kind": "widget_reference",
                    "source_object": obj["id"],
                }
            )
        else:
            raise FrogPipelineError(stage="lower", error_code="unsupported_object_kind", message=f"Unsupported IR object kind during lowering: {obj['kind']}")

    if has_natural_ui and has_object_ui:
        ui_binding_kind = "mixed"
    elif has_natural_ui:
        ui_binding_kind = "natural_widget_value"
    elif has_object_ui:
        ui_binding_kind = "object_style_ui_interaction"
    else:
        ui_binding_kind = "none"

    artifact = {
        "artifact_kind": "frog_lowered_form",
        "artifact_version": DEMO_ARTIFACT_VERSION,
        "source_ref": dict(ir.artifact["source_ref"]),
        "backend_family": backend_family,
        "assumptions": {
            "ui_binding_enabled": ui_binding_kind != "none",
            "ui_binding_kind": ui_binding_kind,
        },
        "units": [
            {
                "id": "main",
                "role": "entry_unit",
                "operations": operations,
                "connections": deepcopy(unit["connections"]),
                "ui_declarations": deepcopy(unit.get("ui_declarations", {"widgets": []})),
            }
        ],
    }

    return LoweredForm(artifact=artifact)
