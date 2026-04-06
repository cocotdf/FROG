from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List, Optional

from Implementations.Reference.common import (
    DEMO_ARTIFACT_VERSION,
    DerivedIR,
    FrogPipelineError,
    ValidationResult,
    ensure,
)


def _build_port(port_id: str, direction: str, value_type: str) -> Dict[str, Any]:
    return {
        "id": port_id,
        "direction": direction,
        "value_type": value_type,
    }


def _find_widget(widget_by_id: Dict[str, Dict[str, Any]], widget_id: str) -> Dict[str, Any]:
    widget = widget_by_id.get(widget_id)
    if widget is None:
        raise FrogPipelineError(
            stage="derive-ir",
            error_code="missing_widget_metadata",
            message=f"Missing widget metadata for '{widget_id}' during derivation.",
        )
    return widget


def _find_constant_value(
    node_id_to_node: Dict[str, Dict[str, Any]],
    node_id: str,
) -> Optional[Any]:
    node = node_id_to_node.get(node_id)
    if node is None:
        return None
    if node.get("kind") != "constant":
        return None
    return node.get("value")


def _infer_edge_constant_for_port(
    *,
    target_node_id: str,
    target_port: str,
    edges: List[Dict[str, Any]],
    node_id_to_node: Dict[str, Dict[str, Any]],
) -> Optional[Any]:
    for edge in edges:
        if edge["to"]["node"] == target_node_id and edge["to"]["port"] == target_port:
            source_node_id = edge["from"]["node"]
            source_port = edge["from"]["port"]
            if source_port != "value":
                continue
            constant_value = _find_constant_value(node_id_to_node, source_node_id)
            if constant_value is not None:
                return constant_value
    return None


def _normalize_numeric_default(raw: Any, value_type: str) -> Any:
    if value_type == "f64":
        return float(raw)
    if value_type in {"u16", "i32"}:
        return int(raw)
    return raw


def derive_execution_ir(validation: ValidationResult) -> DerivedIR:
    ensure(
        validation.artifact.get("status") == "ok",
        stage="derive-ir",
        error_code="validation_not_ok",
        message="Derivation requires a successful validation result.",
    )

    validated_program = validation.artifact["validated_program"]
    doc = validated_program["document"]
    interface = doc["interface"]
    diagram = doc["diagram"]
    front_panel = doc.get("front_panel", {})

    input_types = {item["id"]: item["type"] for item in interface["inputs"]}
    output_types = {item["id"]: item["type"] for item in interface["outputs"]}
    widget_by_id = {item["id"]: item for item in front_panel.get("widgets", [])}
    node_id_to_node = {node["id"]: node for node in diagram["nodes"]}

    objects: List[Dict[str, Any]] = []
    connections: List[Dict[str, Any]] = []

    for node in diagram["nodes"]:
        kind = node["kind"]
        node_id = node["id"]
        object_id = f"obj:{node_id}"

        if kind == "interface_input":
            port_id = node["interface_port"]
            objects.append(
                {
                    "id": object_id,
                    "kind": "public_input_boundary",
                    "interface_port": port_id,
                    "direction": "out",
                    "value_type": input_types[port_id],
                    "ports": [
                        _build_port("value", "out", input_types[port_id]),
                    ],
                    "sources": [f"diagram.node:{node_id}"],
                }
            )

        elif kind == "interface_output":
            port_id = node["interface_port"]
            objects.append(
                {
                    "id": object_id,
                    "kind": "public_output_boundary",
                    "interface_port": port_id,
                    "direction": "in",
                    "value_type": output_types[port_id],
                    "ports": [
                        _build_port("value", "in", output_types[port_id]),
                    ],
                    "sources": [f"diagram.node:{node_id}"],
                }
            )

        elif kind == "constant":
            value_type = node["type"]
            value = node["value"]
            objects.append(
                {
                    "id": object_id,
                    "kind": "constant",
                    "value_type": value_type,
                    "value": _normalize_numeric_default(value, value_type),
                    "ports": [
                        _build_port("value", "out", value_type),
                    ],
                    "sources": [f"diagram.node:{node_id}"],
                }
            )

        elif kind == "widget_value":
            widget_id = node["widget"]
            widget = _find_widget(widget_by_id, widget_id)

            direction = "out" if widget["role"] == "control" else "in"
            obj: Dict[str, Any] = {
                "id": object_id,
                "kind": "widget_value_participation",
                "widget_id": widget_id,
                "widget_role": widget["role"],
                "widget_class": widget["widget"],
                "participation_kind": "widget_value",
                "direction": direction,
                "value_type": widget["value_type"],
                "ports": [
                    _build_port("value", direction, widget["value_type"]),
                ],
                "sources": [f"diagram.node:{node_id}", f"front_panel.widget:{widget_id}"],
            }

            default_value = widget.get("props", {}).get("default_value")
            if widget["role"] == "control" and default_value is not None:
                obj["default_value"] = _normalize_numeric_default(default_value, widget["value_type"])

            objects.append(obj)

        elif kind == "widget_reference":
            widget_id = node["widget"]
            widget = _find_widget(widget_by_id, widget_id)

            objects.append(
                {
                    "id": object_id,
                    "kind": "widget_reference_participation",
                    "widget_id": widget_id,
                    "widget_role": widget["role"],
                    "widget_class": widget["widget"],
                    "participation_kind": "widget_reference",
                    "ports": [
                        _build_port("ref", "out", "widget_reference"),
                    ],
                    "sources": [f"diagram.node:{node_id}", f"front_panel.widget:{widget_id}"],
                }
            )

        elif kind == "primitive":
            primitive_ref = node["type"]

            if primitive_ref == "frog.core.add":
                value_type = node.get("_resolved_value_type", node.get("value_type", "f64"))
                objects.append(
                    {
                        "id": object_id,
                        "kind": "primitive",
                        "primitive_ref": primitive_ref,
                        "value_type": value_type,
                        "ports": [
                            _build_port("a", "in", value_type),
                            _build_port("b", "in", value_type),
                            _build_port("result", "out", value_type),
                        ],
                        "sources": [f"diagram.node:{node_id}", f"library.primitive:{primitive_ref}"],
                    }
                )

            elif primitive_ref == "frog.core.delay":
                value_type = node.get("_resolved_value_type", node.get("value_type", "f64"))
                state_id = f"state:{node_id}"

                initial_value = node.get("_coerced_initial")
                if initial_value is None and "initial" in node:
                    initial_value = node["initial"]
                if initial_value is None:
                    initial_value = _infer_edge_constant_for_port(
                        target_node_id=node_id,
                        target_port="initial",
                        edges=diagram["edges"],
                        node_id_to_node=node_id_to_node,
                    )

                objects.append(
                    {
                        "id": object_id,
                        "kind": "explicit_local_memory_primitive",
                        "primitive_ref": primitive_ref,
                        "state_id": state_id,
                        "state_kind": "explicit_local_memory",
                        "value_type": value_type,
                        "initial": _normalize_numeric_default(initial_value, value_type)
                        if initial_value is not None
                        else None,
                        "ports": [
                            _build_port("in", "in", value_type),
                            _build_port("initial", "in", value_type),
                            _build_port("out", "out", value_type),
                        ],
                        "sources": [f"diagram.node:{node_id}", f"library.primitive:{primitive_ref}"],
                    }
                )

            elif primitive_ref == "frog.ui.property_write":
                member = deepcopy(node["widget_member"])
                value_type = node.get("_resolved_value_type")
                if value_type is None:
                    raise FrogPipelineError(
                        stage="derive-ir",
                        error_code="missing_property_write_value_type",
                        message="frog.ui.property_write requires a resolved value type.",
                    )

                objects.append(
                    {
                        "id": object_id,
                        "kind": "primitive",
                        "primitive_ref": primitive_ref,
                        "ui_operation_kind": "property_write",
                        "widget_member": member,
                        "target_widget_id": node.get("_resolved_widget_id"),
                        "target_widget_class": node.get("_resolved_widget_class"),
                        "ports": [
                            _build_port("ref", "in", "widget_reference"),
                            _build_port("value", "in", value_type),
                        ],
                        "sources": [f"diagram.node:{node_id}", f"library.primitive:{primitive_ref}"],
                    }
                )

            else:
                raise FrogPipelineError(
                    stage="derive-ir",
                    error_code="unsupported_primitive",
                    message=f"Unsupported primitive during derivation: {primitive_ref}",
                )

        elif kind == "for_loop":
            value_type = node.get("_resolved_value_type", "f64")
            iteration_count = None

            count_from = node.get("count_from")
            if isinstance(count_from, dict):
                source_node_id = count_from.get("node")
                source_port = count_from.get("port")
                if source_port == "value" and source_node_id is not None:
                    raw_count = _find_constant_value(node_id_to_node, source_node_id)
                    if raw_count is not None:
                        iteration_count = int(raw_count)

            if iteration_count is None:
                raise FrogPipelineError(
                    stage="derive-ir",
                    error_code="unsupported_loop_count_source",
                    message="Reference derivation expects a constant-count for_loop for the bounded slice.",
                )

            state_id = None
            region = node.get("region", {})
            region_nodes = region.get("nodes", [])
            for region_node in region_nodes:
                if region_node.get("kind") == "primitive" and region_node.get("type") == "frog.core.delay":
                    state_id = f"state:{region_node['id']}"
                    break

            objects.append(
                {
                    "id": object_id,
                    "kind": "counted_loop_region",
                    "iteration_count": iteration_count,
                    "value_type": value_type,
                    "uses_explicit_local_memory": state_id is not None,
                    **({"state_id": state_id} if state_id is not None else {}),
                    "ports": [
                        _build_port("loop_input_value", "in", value_type),
                        _build_port("loop_initial_state", "in", value_type),
                        _build_port("loop_final_state", "out", value_type),
                    ],
                    "sources": [f"diagram.node:{node_id}"],
                }
            )

        else:
            raise FrogPipelineError(
                stage="derive-ir",
                error_code="unsupported_node_kind",
                message=f"Unsupported node kind during derivation: {kind}",
            )

    node_id_to_object_id = {node["id"]: f"obj:{node['id']}" for node in diagram["nodes"]}

    for edge in diagram["edges"]:
        connections.append(
            {
                "id": f"conn:{edge['id']}",
                "from": {
                    "object": node_id_to_object_id[edge["from"]["node"]],
                    "port": edge["from"]["port"],
                },
                "to": {
                    "object": node_id_to_object_id[edge["to"]["node"]],
                    "port": edge["to"]["port"],
                },
                "sources": [f"diagram.edge:{edge['id']}"],
            }
        )

    artifact = {
        "artifact_kind": "frog_derived_execution_ir",
        "artifact_version": DEMO_ARTIFACT_VERSION,
        "source_ref": dict(validation.artifact["source_ref"]),
        "program_id": validated_program["program_id"],
        "execution_unit": {
            "id": "unit:main",
            "role": "entry_unit",
            "objects": objects,
            "connections": connections,
            "ui_declarations": {
                "widgets": [deepcopy(widget) for widget in front_panel.get("widgets", [])],
            },
        },
        "diagnostics": [],
    }

    return DerivedIR(artifact=artifact)
