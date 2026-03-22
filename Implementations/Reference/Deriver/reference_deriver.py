from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List

from Implementations.Reference.common import DEMO_ARTIFACT_VERSION, DerivedIR, FrogPipelineError, ValidationResult, ensure


def derive_execution_ir(validation: ValidationResult) -> DerivedIR:
    ensure(validation.artifact.get("status") == "ok", stage="derive-ir", error_code="validation_not_ok", message="Derivation requires a successful validation result.")

    validated_program = validation.artifact["validated_program"]
    doc = validated_program["document"]
    interface = doc["interface"]
    diagram = doc["diagram"]
    front_panel = doc.get("front_panel", {})

    input_types = {item["id"]: item["type"] for item in interface["inputs"]}
    output_types = {item["id"]: item["type"] for item in interface["outputs"]}
    widget_by_id = {item["id"]: item for item in front_panel.get("widgets", [])}

    objects: List[Dict[str, Any]] = []
    connections: List[Dict[str, Any]] = []

    for node in diagram["nodes"]:
        kind = node["kind"]
        node_id = node["id"]

        if kind == "interface_input":
            port_id = node["interface_port"]
            objects.append(
                {
                    "id": f"obj:{node_id}",
                    "kind": "public_input_boundary",
                    "interface_port": port_id,
                    "direction": "out",
                    "value_type": input_types[port_id],
                    "ports": [{"id": "value", "direction": "out", "value_type": input_types[port_id]}],
                    "sources": [f"diagram.node:{node_id}"],
                }
            )
        elif kind == "interface_output":
            port_id = node["interface_port"]
            objects.append(
                {
                    "id": f"obj:{node_id}",
                    "kind": "public_output_boundary",
                    "interface_port": port_id,
                    "direction": "in",
                    "value_type": output_types[port_id],
                    "ports": [{"id": "value", "direction": "in", "value_type": output_types[port_id]}],
                    "sources": [f"diagram.node:{node_id}"],
                }
            )
        elif kind == "widget_value":
            widget_id = node["widget"]
            widget = widget_by_id.get(widget_id)
            if widget is None:
                raise FrogPipelineError(stage="derive-ir", error_code="missing_widget_metadata", message=f"Missing widget metadata for '{widget_id}' during derivation.")
            direction = "out" if widget["role"] == "control" else "in"
            default_value = widget.get("props", {}).get("default_value") if widget["role"] == "control" else None
            obj: Dict[str, Any] = {
                "id": f"obj:{node_id}",
                "kind": "widget_value_participation",
                "widget_id": widget_id,
                "widget_role": widget["role"],
                "widget_class": widget["widget"],
                "participation_kind": "widget_value",
                "direction": direction,
                "value_type": widget["value_type"],
                "ports": [{"id": "value", "direction": direction, "value_type": widget["value_type"]}],
                "sources": [f"diagram.node:{node_id}", f"front_panel.widget:{widget_id}"],
            }
            if default_value is not None:
                obj["default_value"] = float(default_value)
            objects.append(obj)
        elif kind == "widget_reference":
            widget_id = node["widget"]
            widget = widget_by_id.get(widget_id)
            if widget is None:
                raise FrogPipelineError(stage="derive-ir", error_code="missing_widget_metadata", message=f"Missing widget metadata for '{widget_id}' during derivation.")
            objects.append(
                {
                    "id": f"obj:{node_id}",
                    "kind": "widget_reference_participation",
                    "widget_id": widget_id,
                    "widget_role": widget["role"],
                    "widget_class": widget["widget"],
                    "participation_kind": "widget_reference",
                    "ports": [{"id": "ref", "direction": "out", "value_type": "widget_reference"}],
                    "sources": [f"diagram.node:{node_id}", f"front_panel.widget:{widget_id}"],
                }
            )
        elif kind == "primitive":
            primitive_ref = node["type"]
            if primitive_ref == "frog.core.add":
                objects.append(
                    {
                        "id": f"obj:{node_id}",
                        "kind": "primitive",
                        "primitive_ref": primitive_ref,
                        "ports": [
                            {"id": "a", "direction": "in", "value_type": "f64"},
                            {"id": "b", "direction": "in", "value_type": "f64"},
                            {"id": "result", "direction": "out", "value_type": "f64"},
                        ],
                        "sources": [f"diagram.node:{node_id}", f"library.primitive:{primitive_ref}"],
                    }
                )
            elif primitive_ref == "frog.core.delay":
                objects.append(
                    {
                        "id": f"obj:{node_id}",
                        "kind": "explicit_local_memory_primitive",
                        "primitive_ref": primitive_ref,
                        "state_kind": "explicit_local_memory",
                        "value_type": "f64",
                        "initial": float(node["_coerced_initial"] if "_coerced_initial" in node else node["initial"]),
                        "ports": [
                            {"id": "in", "direction": "in", "value_type": "f64"},
                            {"id": "out", "direction": "out", "value_type": "f64"},
                        ],
                        "sources": [f"diagram.node:{node_id}", f"library.primitive:{primitive_ref}"],
                    }
                )
            elif primitive_ref == "frog.ui.property_write":
                member = deepcopy(node["widget_member"])
                objects.append(
                    {
                        "id": f"obj:{node_id}",
                        "kind": "primitive",
                        "primitive_ref": primitive_ref,
                        "ui_operation_kind": "property_write",
                        "widget_member": member,
                        "target_widget_id": node.get("_resolved_widget_id"),
                        "target_widget_class": node.get("_resolved_widget_class"),
                        "ports": [
                            {"id": "ref", "direction": "in", "value_type": "widget_reference"},
                            {"id": "value", "direction": "in", "value_type": node["_resolved_value_type"]},
                        ],
                        "sources": [f"diagram.node:{node_id}", f"library.primitive:{primitive_ref}"],
                    }
                )
            else:
                raise FrogPipelineError(stage="derive-ir", error_code="unsupported_primitive", message=f"Unsupported primitive during derivation: {primitive_ref}")
        else:
            raise FrogPipelineError(stage="derive-ir", error_code="unsupported_node_kind", message=f"Unsupported node kind during derivation: {kind}")

    node_id_to_object_id = {node["id"]: f"obj:{node['id']}" for node in diagram["nodes"]}
    for edge in diagram["edges"]:
        connections.append(
            {
                "id": f"conn:{edge['id']}",
                "from": {"object": node_id_to_object_id[edge["from"]["node"]], "port": edge["from"]["port"]},
                "to": {"object": node_id_to_object_id[edge["to"]["node"]], "port": edge["to"]["port"]},
                "sources": [f"diagram.edge:{edge['id']}"],
            }
        )

    artifact = {
        "artifact_kind": "frog_derived_execution_ir",
        "artifact_version": DEMO_ARTIFACT_VERSION,
        "source_ref": dict(validation.artifact["source_ref"]),
        "execution_unit": {
            "id": "unit:main",
            "role": "entry_unit",
            "objects": objects,
            "connections": connections,
            "ui_declarations": {
                "widgets": [deepcopy(widget) for widget in front_panel.get("widgets", [])],
            },
        },
    }

    return DerivedIR(artifact=artifact)
