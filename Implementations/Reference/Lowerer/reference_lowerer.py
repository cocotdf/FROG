from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List, Optional

from Implementations.Reference.common import (
    DEFAULT_BACKEND_FAMILY,
    DEMO_ARTIFACT_VERSION,
    DerivedIR,
    FrogPipelineError,
    LoweredForm,
    ensure,
)


def _derive_ui_binding_kind(has_natural_ui: bool, has_object_ui: bool) -> str:
    if has_natural_ui and has_object_ui:
        return "mixed"
    if has_natural_ui:
        return "natural_widget_value"
    if has_object_ui:
        return "object_style_ui_interaction"
    return "none"


def _infer_initial_value_from_connections(
    *,
    object_id: str,
    port_name: str,
    connections: List[Dict[str, Any]],
    constant_values: Dict[str, Any],
) -> Optional[Any]:
    for connection in connections:
        if (
            connection["to"]["object"] == object_id
            and connection["to"]["port"] == port_name
        ):
            source_object = connection["from"]["object"]
            source_port = connection["from"]["port"]
            if source_port == "value" and source_object in constant_values:
                return constant_values[source_object]
    return None


def lower_for_backend_family(
    ir: DerivedIR,
    backend_family: str = DEFAULT_BACKEND_FAMILY,
) -> LoweredForm:
    ensure(
        backend_family == DEFAULT_BACKEND_FAMILY,
        stage="lower",
        error_code="unsupported_backend_family",
        message=f"This demo lowerer supports backend family '{DEFAULT_BACKEND_FAMILY}' only.",
    )

    unit = ir.artifact["execution_unit"]
    objects = unit["objects"]
    connections = deepcopy(unit["connections"])
    ui_declarations = deepcopy(unit.get("ui_declarations", {"widgets": []}))

    operations: List[Dict[str, Any]] = []
    constant_values: Dict[str, Any] = {}

    has_natural_ui = False
    has_object_ui = False
    has_explicit_local_memory = False
    iteration_count: Optional[int] = None

    for obj in objects:
        obj_kind = obj["kind"]

        if obj_kind == "constant":
            constant_values[obj["id"]] = obj["value"]

        elif obj_kind == "public_input_boundary":
            operations.append(
                {
                    "id": obj["id"].replace("obj:", "op:"),
                    "kind": "public_input",
                    "interface_port": obj["interface_port"],
                    "value_type": obj["value_type"],
                    "source_object": obj["id"],
                }
            )

        elif obj_kind == "public_output_boundary":
            operations.append(
                {
                    "id": obj["id"].replace("obj:", "op:"),
                    "kind": "public_output",
                    "interface_port": obj["interface_port"],
                    "value_type": obj["value_type"],
                    "source_object": obj["id"],
                }
            )

        elif obj_kind == "widget_value_participation":
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
                raise FrogPipelineError(
                    stage="lower",
                    error_code="unsupported_widget_role",
                    message=f"Unsupported widget role during lowering: {obj['widget_role']}",
                )

        elif obj_kind == "widget_reference_participation":
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

        elif obj_kind == "primitive":
            primitive_ref = obj["primitive_ref"]

            if primitive_ref == "frog.core.add":
                operations.append(
                    {
                        "id": obj["id"].replace("obj:", "op:"),
                        "kind": "core_primitive_add",
                        "primitive_ref": primitive_ref,
                        "value_type": obj.get("value_type", "f64"),
                        "source_object": obj["id"],
                    }
                )

            elif primitive_ref == "frog.ui.property_write":
                has_object_ui = True
                ports = obj.get("ports", [])
                value_type = None
                for port in ports:
                    if port["name"] == "value":
                        value_type = port["value_type"]
                        break

                if value_type is None:
                    raise FrogPipelineError(
                        stage="lower",
                        error_code="missing_property_write_value_type",
                        message="frog.ui.property_write requires a typed value port.",
                    )

                operations.append(
                    {
                        "id": obj["id"].replace("obj:", "op:"),
                        "kind": "ui_property_write",
                        "primitive_ref": primitive_ref,
                        "widget_member": deepcopy(obj["widget_member"]),
                        "target_widget_id": obj.get("target_widget_id"),
                        "target_widget_class": obj.get("target_widget_class"),
                        "value_type": value_type,
                        "source_object": obj["id"],
                    }
                )

            else:
                raise FrogPipelineError(
                    stage="lower",
                    error_code="unsupported_primitive",
                    message=f"This demo lowerer does not support primitive '{primitive_ref}'.",
                )

        elif obj_kind == "explicit_local_memory_primitive":
            has_explicit_local_memory = True

            initial_value = obj.get("initial")
            if initial_value is None:
                initial_value = _infer_initial_value_from_connections(
                    object_id=obj["id"],
                    port_name="initial",
                    connections=connections,
                    constant_values=constant_values,
                )

            operations.append(
                {
                    "id": obj["id"].replace("obj:", "op:"),
                    "kind": "state_init",
                    "primitive_ref": obj["primitive_ref"],
                    "state_id": obj["state_id"],
                    "state_kind": obj["state_kind"],
                    "value_type": obj["value_type"],
                    "initial_value": initial_value,
                    "source_object": obj["id"],
                }
            )

        elif obj_kind == "counted_loop_region":
            iteration_count = int(obj["iteration_count"])
            has_explicit_local_memory = has_explicit_local_memory or obj.get(
                "uses_explicit_local_memory",
                False,
            )

            loop_operation: Dict[str, Any] = {
                "id": obj["id"].replace("obj:", "op:"),
                "kind": "counted_loop_execute",
                "iteration_count": iteration_count,
                "value_type": obj["value_type"],
                "source_object": obj["id"],
            }

            if "state_id" in obj:
                loop_operation["state_id"] = obj["state_id"]

            initial_value = _infer_initial_value_from_connections(
                object_id=obj["id"],
                port_name="loop_initial_state",
                connections=connections,
                constant_values=constant_values,
            )
            if initial_value is not None:
                loop_operation["initial_value"] = initial_value

            operations.append(loop_operation)

        else:
            raise FrogPipelineError(
                stage="lower",
                error_code="unsupported_object_kind",
                message=f"Unsupported IR object kind during lowering: {obj_kind}",
            )

    ui_binding_kind = _derive_ui_binding_kind(has_natural_ui, has_object_ui)

    artifact = {
        "artifact_kind": "frog_lowered_form",
        "artifact_version": DEMO_ARTIFACT_VERSION,
        "source_ref": dict(ir.artifact["source_ref"]),
        "program_id": ir.artifact.get("program_id"),
        "backend_family": backend_family,
        "assumptions": {
            "ui_binding_enabled": ui_binding_kind != "none",
            "ui_binding_kind": ui_binding_kind,
            "ui_object_surface_enabled": has_object_ui,
            "explicit_local_memory": has_explicit_local_memory,
            "state_model": "explicit_local_memory" if has_explicit_local_memory else "none",
            "execution_mode": "bounded_ui_accumulator" if iteration_count is not None else "deterministic_step_execution",
            "bounded_loop_lowering_mode": "counted_loop" if iteration_count is not None else "none",
            "presentation_template_runtime_support": "optional",
        },
        "units": [
            {
                "id": "main",
                "role": "entry_unit",
                "operations": operations,
                "connections": connections,
                "ui_declarations": ui_declarations,
            }
        ],
        "diagnostics": [],
    }

    return LoweredForm(artifact=artifact)
