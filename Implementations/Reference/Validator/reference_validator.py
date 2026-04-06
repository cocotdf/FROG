from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List, Optional, Tuple

from Implementations.Reference.common import (
    DEMO_ARTIFACT_VERSION,
    FrogPipelineError,
    LoadedSource,
    ValidationResult,
    ensure,
)


SUPPORTED_PRIMITIVES = {
    "frog.core.add",
    "frog.core.delay",
    "frog.ui.property_write",
}

SUPPORTED_WIDGET_CLASSES = {
    "frog.ui.standard.numeric_control",
    "frog.ui.standard.numeric_indicator",
}

SUPPORTED_NUMERIC_TYPES = {
    "f64",
    "u16",
    "i32",
}

SUPPORTED_COLOR_TYPE = "frog.ui.color"


def _fail(status: str, source_ref: Dict[str, Any], diagnostics: List[Dict[str, Any]]) -> ValidationResult:
    artifact = {
        "artifact_kind": "frog_validation_result",
        "artifact_version": DEMO_ARTIFACT_VERSION,
        "status": status,
        "source_ref": source_ref,
        "diagnostics": diagnostics,
    }
    return ValidationResult(artifact=artifact)


def _is_object(value: Any) -> bool:
    return isinstance(value, dict)


def _is_array(value: Any) -> bool:
    return isinstance(value, list)


def _diag(code: str, message: str, *, location: Optional[str] = None, severity: str = "error") -> Dict[str, Any]:
    diag = {
        "code": code,
        "severity": severity,
        "message": message,
    }
    if location is not None:
        diag["location"] = location
    return diag


def _type_compatible(source_type: str, target_type: str) -> bool:
    return source_type == target_type


def _require_top_level_sections(doc: Dict[str, Any], source_ref: Dict[str, Any]) -> Optional[ValidationResult]:
    required = ["spec_version", "metadata", "interface", "diagram"]
    missing = [name for name in required if name not in doc]
    if missing:
        return _fail(
            "structural_invalid",
            source_ref,
            [_diag("missing_top_level_sections", f"Missing top-level sections: {', '.join(missing)}.")],
        )
    return None


def _validate_interface(interface: Dict[str, Any], source_ref: Dict[str, Any]) -> Tuple[Optional[ValidationResult], Dict[str, str], Dict[str, str]]:
    if not _is_object(interface):
        return (
            _fail(
                "structural_invalid",
                source_ref,
                [_diag("invalid_interface_shape", "Top-level 'interface' must be an object.")],
            ),
            {},
            {},
        )

    inputs = interface.get("inputs", [])
    outputs = interface.get("outputs", [])

    if not _is_array(inputs) or not _is_array(outputs):
        return (
            _fail(
                "structural_invalid",
                source_ref,
                [_diag("invalid_interface_ports_shape", "'interface.inputs' and 'interface.outputs' must be arrays.")],
            ),
            {},
            {},
        )

    input_types: Dict[str, str] = {}
    output_types: Dict[str, str] = {}
    diagnostics: List[Dict[str, Any]] = []

    for item in inputs:
        if not _is_object(item) or "id" not in item or "type" not in item:
            diagnostics.append(_diag("invalid_input_port", "Each interface input must contain 'id' and 'type'."))
            continue
        input_types[item["id"]] = item["type"]

    for item in outputs:
        if not _is_object(item) or "id" not in item or "type" not in item:
            diagnostics.append(_diag("invalid_output_port", "Each interface output must contain 'id' and 'type'."))
            continue
        output_types[item["id"]] = item["type"]

    if diagnostics:
        return _fail("structural_invalid", source_ref, diagnostics), {}, {}

    return None, input_types, output_types


def _validate_front_panel(front_panel: Dict[str, Any], source_ref: Dict[str, Any]) -> Tuple[Optional[ValidationResult], Dict[str, Dict[str, Any]]]:
    if not _is_object(front_panel):
        return (
            _fail(
                "structural_invalid",
                source_ref,
                [_diag("invalid_front_panel_shape", "Top-level 'front_panel' must be an object when present.")],
            ),
            {},
        )

    widgets = front_panel.get("widgets", [])
    if not _is_array(widgets):
        return (
            _fail(
                "structural_invalid",
                source_ref,
                [_diag("invalid_front_panel_widgets_shape", "'front_panel.widgets' must be an array when present.")],
            ),
            {},
        )

    widget_by_id: Dict[str, Dict[str, Any]] = {}
    diagnostics: List[Dict[str, Any]] = []

    for widget in widgets:
        if not _is_object(widget):
            diagnostics.append(_diag("invalid_widget_shape", "Each front-panel widget must be an object."))
            continue

        widget_id = widget.get("id")
        widget_class = widget.get("widget")
        widget_role = widget.get("role")
        value_type = widget.get("value_type")

        if not widget_id or not widget_class or not widget_role:
            diagnostics.append(_diag("missing_widget_fields", "Each widget must define 'id', 'widget', and 'role'."))
            continue

        if widget_id in widget_by_id:
            diagnostics.append(_diag("duplicate_widget_id", f"Duplicate widget id '{widget_id}'."))
            continue

        if widget_class not in SUPPORTED_WIDGET_CLASSES:
            diagnostics.append(
                _diag(
                    "unsupported_widget_class",
                    f"Unsupported widget class in reference subset: {widget_class}.",
                )
            )

        if widget_role not in {"control", "indicator"}:
            diagnostics.append(
                _diag(
                    "unsupported_widget_role",
                    f"Unsupported widget role in reference subset: {widget_role}.",
                )
            )

        if value_type not in {"u16", "f64"}:
            diagnostics.append(
                _diag(
                    "unsupported_widget_value_type",
                    f"Unsupported widget value_type in reference subset: {value_type}.",
                )
            )

        widget_by_id[widget_id] = deepcopy(widget)

    if diagnostics:
        return _fail("unsupported_but_valid", source_ref, diagnostics), {}

    return None, widget_by_id


def _collect_diagram_node_map(diagram: Dict[str, Any], source_ref: Dict[str, Any]) -> Tuple[Optional[ValidationResult], Dict[str, Dict[str, Any]], List[Dict[str, Any]]]:
    if not _is_object(diagram):
        return (
            _fail(
                "structural_invalid",
                source_ref,
                [_diag("invalid_diagram_shape", "Top-level 'diagram' must be an object.")],
            ),
            {},
            [],
        )

    nodes = diagram.get("nodes", [])
    edges = diagram.get("edges", [])

    if not _is_array(nodes) or not _is_array(edges):
        return (
            _fail(
                "structural_invalid",
                source_ref,
                [_diag("invalid_diagram_collections", "'diagram.nodes' and 'diagram.edges' must be arrays.")],
            ),
            {},
            [],
        )

    node_map: Dict[str, Dict[str, Any]] = {}
    diagnostics: List[Dict[str, Any]] = []

    for node in nodes:
        if not _is_object(node) or "id" not in node or "kind" not in node:
            diagnostics.append(_diag("invalid_node_shape", "Each diagram node must define 'id' and 'kind'."))
            continue
        node_id = node["id"]
        if node_id in node_map:
            diagnostics.append(_diag("duplicate_node_id", f"Duplicate diagram node id '{node_id}'."))
            continue
        node_map[node_id] = deepcopy(node)

    if diagnostics:
        return _fail("structural_invalid", source_ref, diagnostics), {}, []

    return None, node_map, deepcopy(edges)


def _build_incoming_edge_map(edges: List[Dict[str, Any]], source_ref: Dict[str, Any]) -> Tuple[Optional[ValidationResult], Dict[Tuple[str, str], List[Dict[str, Any]]]]:
    incoming: Dict[Tuple[str, str], List[Dict[str, Any]]] = {}
    diagnostics: List[Dict[str, Any]] = []

    for edge in edges:
        if not _is_object(edge):
            diagnostics.append(_diag("invalid_edge_shape", "Each diagram edge must be an object."))
            continue

        edge_id = edge.get("id")
        edge_from = edge.get("from")
        edge_to = edge.get("to")

        if not edge_id or not _is_object(edge_from) or not _is_object(edge_to):
            diagnostics.append(_diag("invalid_edge_fields", "Each edge must define 'id', 'from', and 'to'."))
            continue

        key = (edge_to["node"], edge_to["port"])
        incoming.setdefault(key, []).append(deepcopy(edge))

    if diagnostics:
        return _fail("structural_invalid", source_ref, diagnostics), {}

    return None, incoming


def _resolve_source_port_type(
    *,
    node: Dict[str, Any],
    port: str,
    input_types: Dict[str, str],
    output_types: Dict[str, str],
    widget_by_id: Dict[str, Dict[str, Any]],
) -> Optional[str]:
    kind = node["kind"]

    if kind == "constant":
        return node.get("type")

    if kind == "interface_input" and port == "value":
        return input_types.get(node["interface_port"])

    if kind == "interface_output" and port == "value":
        return output_types.get(node["interface_port"])

    if kind == "widget_value" and port == "value":
        widget = widget_by_id.get(node["widget"])
        return None if widget is None else widget.get("value_type")

    if kind == "widget_reference" and port == "ref":
        return "widget_reference"

    if kind == "primitive":
        primitive_ref = node["type"]
        if primitive_ref == "frog.core.add":
            if port in {"a", "b", "result"}:
                return node.get("_resolved_value_type") or node.get("value_type")
        if primitive_ref == "frog.core.delay":
            if port in {"in", "initial", "out"}:
                return node.get("_resolved_value_type") or node.get("value_type")
        if primitive_ref == "frog.ui.property_write":
            if port == "ref":
                return "widget_reference"
            if port == "value":
                return node.get("_resolved_value_type")

    if kind == "for_loop":
        if port in {"loop_input_value", "loop_initial_state", "loop_final_state"}:
            return node.get("_resolved_value_type") or node.get("value_type")

    return None


def _validate_and_enrich_nodes(
    *,
    node_map: Dict[str, Dict[str, Any]],
    edges: List[Dict[str, Any]],
    incoming: Dict[Tuple[str, str], List[Dict[str, Any]]],
    widget_by_id: Dict[str, Dict[str, Any]],
    input_types: Dict[str, str],
    output_types: Dict[str, str],
    source_ref: Dict[str, Any],
) -> Optional[ValidationResult]:
    diagnostics: List[Dict[str, Any]] = []

    for node_id, node in node_map.items():
        kind = node["kind"]

        if kind == "constant":
            node_type = node.get("type")
            if node_type not in {"u16", "f64", "i32", "frog.ui.color"}:
                diagnostics.append(
                    _diag(
                        "unsupported_constant_type",
                        f"Unsupported constant type in reference subset: {node_type}.",
                        location=f"diagram.node:{node_id}",
                    )
                )

        elif kind == "interface_input":
            port_id = node.get("interface_port")
            if port_id not in input_types:
                diagnostics.append(
                    _diag(
                        "unknown_interface_input",
                        f"Unknown interface input '{port_id}'.",
                        location=f"diagram.node:{node_id}",
                    )
                )

        elif kind == "interface_output":
            port_id = node.get("interface_port")
            if port_id not in output_types:
                diagnostics.append(
                    _diag(
                        "unknown_interface_output",
                        f"Unknown interface output '{port_id}'.",
                        location=f"diagram.node:{node_id}",
                    )
                )

        elif kind == "widget_value":
            widget_id = node.get("widget")
            widget = widget_by_id.get(widget_id)
            if widget is None:
                diagnostics.append(
                    _diag(
                        "unknown_widget_for_widget_value",
                        f"Unknown widget '{widget_id}' for widget_value node.",
                        location=f"diagram.node:{node_id}",
                    )
                )

        elif kind == "widget_reference":
            widget_id = node.get("widget")
            widget = widget_by_id.get(widget_id)
            if widget is None:
                diagnostics.append(
                    _diag(
                        "unknown_widget_for_widget_reference",
                        f"Unknown widget '{widget_id}' for widget_reference node.",
                        location=f"diagram.node:{node_id}",
                    )
                )

        elif kind == "primitive":
            primitive_ref = node.get("type")
            if primitive_ref not in SUPPORTED_PRIMITIVES:
                diagnostics.append(
                    _diag(
                        "unsupported_primitive",
                        f"Unsupported primitive in reference subset: {primitive_ref}.",
                        location=f"diagram.node:{node_id}",
                    )
                )
                continue

            if primitive_ref == "frog.core.add":
                incoming_a = incoming.get((node_id, "a"), [])
                incoming_b = incoming.get((node_id, "b"), [])
                if len(incoming_a) != 1 or len(incoming_b) != 1:
                    diagnostics.append(
                        _diag(
                            "invalid_add_inputs",
                            "frog.core.add requires exactly one incoming edge for ports 'a' and 'b'.",
                            location=f"diagram.node:{node_id}",
                        )
                    )
                    continue

                src_a = node_map[incoming_a[0]["from"]["node"]]
                src_b = node_map[incoming_b[0]["from"]["node"]]
                type_a = _resolve_source_port_type(
                    node=src_a,
                    port=incoming_a[0]["from"]["port"],
                    input_types=input_types,
                    output_types=output_types,
                    widget_by_id=widget_by_id,
                )
                type_b = _resolve_source_port_type(
                    node=src_b,
                    port=incoming_b[0]["from"]["port"],
                    input_types=input_types,
                    output_types=output_types,
                    widget_by_id=widget_by_id,
                )

                if type_a is None or type_b is None:
                    diagnostics.append(
                        _diag(
                            "unresolved_add_input_type",
                            "frog.core.add requires resolvable input types.",
                            location=f"diagram.node:{node_id}",
                        )
                    )
                    continue

                if type_a not in SUPPORTED_NUMERIC_TYPES or type_b not in SUPPORTED_NUMERIC_TYPES:
                    diagnostics.append(
                        _diag(
                            "unsupported_add_type",
                            "frog.core.add supports numeric types only in the reference subset.",
                            location=f"diagram.node:{node_id}",
                        )
                    )
                    continue

                if type_a != type_b:
                    diagnostics.append(
                        _diag(
                            "type_mismatch_add",
                            f"frog.core.add input type mismatch: '{type_a}' vs '{type_b}'.",
                            location=f"diagram.node:{node_id}",
                        )
                    )
                    continue

                node["_resolved_value_type"] = type_a

            elif primitive_ref == "frog.core.delay":
                incoming_in = incoming.get((node_id, "in"), [])
                incoming_initial = incoming.get((node_id, "initial"), [])

                if len(incoming_in) != 1 or len(incoming_initial) != 1:
                    diagnostics.append(
                        _diag(
                            "invalid_delay_inputs",
                            "frog.core.delay requires exactly one incoming edge for ports 'in' and 'initial'.",
                            location=f"diagram.node:{node_id}",
                        )
                    )
                    continue

                src_in = node_map[incoming_in[0]["from"]["node"]]
                src_initial = node_map[incoming_initial[0]["from"]["node"]]

                type_in = _resolve_source_port_type(
                    node=src_in,
                    port=incoming_in[0]["from"]["port"],
                    input_types=input_types,
                    output_types=output_types,
                    widget_by_id=widget_by_id,
                )
                type_initial = _resolve_source_port_type(
                    node=src_initial,
                    port=incoming_initial[0]["from"]["port"],
                    input_types=input_types,
                    output_types=output_types,
                    widget_by_id=widget_by_id,
                )

                if type_in is None or type_initial is None:
                    diagnostics.append(
                        _diag(
                            "unresolved_delay_input_type",
                            "frog.core.delay requires resolvable input types.",
                            location=f"diagram.node:{node_id}",
                        )
                    )
                    continue

                if type_in != type_initial:
                    diagnostics.append(
                        _diag(
                            "type_mismatch_delay",
                            f"frog.core.delay input type mismatch: '{type_in}' vs '{type_initial}'.",
                            location=f"diagram.node:{node_id}",
                        )
                    )
                    continue

                if type_in not in SUPPORTED_NUMERIC_TYPES:
                    diagnostics.append(
                        _diag(
                            "unsupported_delay_type",
                            f"Unsupported frog.core.delay type in reference subset: {type_in}.",
                            location=f"diagram.node:{node_id}",
                        )
                    )
                    continue

                node["_resolved_value_type"] = type_in

                const_initial = _find_constant_input_value(
                    target_node_id=node_id,
                    target_port="initial",
                    incoming=incoming,
                    node_map=node_map,
                )
                if const_initial is not None:
                    if type_in == "f64":
                        node["_coerced_initial"] = float(const_initial)
                    elif type_in in {"u16", "i32"}:
                        node["_coerced_initial"] = int(const_initial)

            elif primitive_ref == "frog.ui.property_write":
                incoming_ref = incoming.get((node_id, "ref"), [])
                incoming_value = incoming.get((node_id, "value"), [])

                if len(incoming_ref) != 1 or len(incoming_value) != 1:
                    diagnostics.append(
                        _diag(
                            "invalid_property_write_inputs",
                            "frog.ui.property_write requires exactly one incoming edge for ports 'ref' and 'value'.",
                            location=f"diagram.node:{node_id}",
                        )
                    )
                    continue

                ref_source = node_map[incoming_ref[0]["from"]["node"]]
                if ref_source["kind"] != "widget_reference":
                    diagnostics.append(
                        _diag(
                            "invalid_property_write_ref_source",
                            "frog.ui.property_write 'ref' must come from a widget_reference node.",
                            location=f"diagram.node:{node_id}",
                        )
                    )
                    continue

                widget_id = ref_source["widget"]
                widget = widget_by_id.get(widget_id)
                if widget is None:
                    diagnostics.append(
                        _diag(
                            "unknown_property_write_widget",
                            f"Unknown widget '{widget_id}' in property_write reference path.",
                            location=f"diagram.node:{node_id}",
                        )
                    )
                    continue

                member = node.get("widget_member")
                if not _is_object(member) or "member" not in member:
                    diagnostics.append(
                        _diag(
                            "invalid_property_write_member",
                            "frog.ui.property_write requires a 'widget_member' object with a 'member' field.",
                            location=f"diagram.node:{node_id}",
                        )
                    )
                    continue

                part_name = member.get("part")
                member_name = member["member"]

                if part_name is not None:
                    diagnostics.append(
                        _diag(
                            "unsupported_part_property_write",
                            "The current reference subset supports only class-level property writes.",
                            location=f"diagram.node:{node_id}",
                        )
                    )
                    continue

                if member_name != "face_color":
                    diagnostics.append(
                        _diag(
                            "unsupported_property_write_member",
                            f"Unsupported property_write target in reference subset: {member_name}.",
                            location=f"diagram.node:{node_id}",
                        )
                    )
                    continue

                value_source = node_map[incoming_value[0]["from"]["node"]]
                value_type = _resolve_source_port_type(
                    node=value_source,
                    port=incoming_value[0]["from"]["port"],
                    input_types=input_types,
                    output_types=output_types,
                    widget_by_id=widget_by_id,
                )

                if value_type != SUPPORTED_COLOR_TYPE:
                    diagnostics.append(
                        _diag(
                            "invalid_property_write_value_type",
                            f"face_color property_write requires value type '{SUPPORTED_COLOR_TYPE}', got '{value_type}'.",
                            location=f"diagram.node:{node_id}",
                        )
                    )
                    continue

                node["_resolved_value_type"] = SUPPORTED_COLOR_TYPE
                node["_resolved_widget_id"] = widget_id
                node["_resolved_widget_class"] = widget["widget"]

        elif kind == "for_loop":
            region = node.get("region")
            count_from = node.get("count_from")

            if not _is_object(region):
                diagnostics.append(
                    _diag(
                        "invalid_for_loop_region",
                        "Reference subset expects for_loop.region to be an object.",
                        location=f"diagram.node:{node_id}",
                    )
                )
                continue

            if not _is_object(count_from):
                diagnostics.append(
                    _diag(
                        "invalid_for_loop_count_from",
                        "Reference subset expects for_loop.count_from to be an object.",
                        location=f"diagram.node:{node_id}",
                    )
                )
                continue

            count_node_id = count_from.get("node")
            count_port = count_from.get("port")
            count_node = node_map.get(count_node_id)

            if count_node is None or count_node.get("kind") != "constant" or count_port != "value":
                diagnostics.append(
                    _diag(
                        "unsupported_for_loop_count_source",
                        "Reference subset expects for_loop.count_from to reference a constant node 'value' port.",
                        location=f"diagram.node:{node_id}",
                    )
                )
                continue

            if count_node.get("type") != "i32" or int(count_node.get("value")) != 5:
                diagnostics.append(
                    _diag(
                        "unsupported_for_loop_iteration_count",
                        "Reference subset currently supports only a constant i32 iteration count of exactly 5.",
                        location=f"diagram.node:{node_id}",
                    )
                )
                continue

            region_inputs = region.get("inputs", [])
            region_outputs = region.get("outputs", [])
            region_nodes = region.get("nodes", [])
            region_edges = region.get("edges", [])

            if not (_is_array(region_inputs) and _is_array(region_outputs) and _is_array(region_nodes) and _is_array(region_edges)):
                diagnostics.append(
                    _diag(
                        "invalid_for_loop_region_shape",
                        "Reference subset expects region.inputs, region.outputs, region.nodes, and region.edges to be arrays.",
                        location=f"diagram.node:{node_id}",
                    )
                )
                continue

            expected_input_ids = {"loop_input_value", "loop_initial_state"}
            actual_input_ids = {item.get("id") for item in region_inputs if _is_object(item)}
            if actual_input_ids != expected_input_ids:
                diagnostics.append(
                    _diag(
                        "unsupported_for_loop_region_inputs",
                        "Reference subset expects exactly region inputs 'loop_input_value' and 'loop_initial_state'.",
                        location=f"diagram.node:{node_id}",
                    )
                )
                continue

            if len(region_outputs) != 1 or region_outputs[0].get("id") != "loop_final_state":
                diagnostics.append(
                    _diag(
                        "unsupported_for_loop_region_outputs",
                        "Reference subset expects exactly one region output 'loop_final_state'.",
                        location=f"diagram.node:{node_id}",
                    )
                )
                continue

            region_delay_nodes = [
                item for item in region_nodes
                if _is_object(item) and item.get("kind") == "primitive" and item.get("type") == "frog.core.delay"
            ]
            region_add_nodes = [
                item for item in region_nodes
                if _is_object(item) and item.get("kind") == "primitive" and item.get("type") == "frog.core.add"
            ]

            if len(region_delay_nodes) != 1 or len(region_add_nodes) != 1:
                diagnostics.append(
                    _diag(
                        "unsupported_for_loop_region_primitives",
                        "Reference subset expects exactly one frog.core.delay and one frog.core.add inside the loop region.",
                        location=f"diagram.node:{node_id}",
                    )
                )
                continue

            incoming_value = incoming.get((node_id, "loop_input_value"), [])
            incoming_initial = incoming.get((node_id, "loop_initial_state"), [])

            if len(incoming_value) != 1 or len(incoming_initial) != 1:
                diagnostics.append(
                    _diag(
                        "invalid_for_loop_inputs",
                        "Reference subset expects exactly one incoming edge for loop_input_value and loop_initial_state.",
                        location=f"diagram.node:{node_id}",
                    )
                )
                continue

            src_value = node_map[incoming_value[0]["from"]["node"]]
            src_initial = node_map[incoming_initial[0]["from"]["node"]]

            value_type = _resolve_source_port_type(
                node=src_value,
                port=incoming_value[0]["from"]["port"],
                input_types=input_types,
                output_types=output_types,
                widget_by_id=widget_by_id,
            )
            initial_type = _resolve_source_port_type(
                node=src_initial,
                port=incoming_initial[0]["from"]["port"],
                input_types=input_types,
                output_types=output_types,
                widget_by_id=widget_by_id,
            )

            if value_type is None or initial_type is None or value_type != initial_type:
                diagnostics.append(
                    _diag(
                        "invalid_for_loop_input_types",
                        "Reference subset expects loop_input_value and loop_initial_state to have the same resolvable type.",
                        location=f"diagram.node:{node_id}",
                    )
                )
                continue

            if value_type not in {"u16", "f64"}:
                diagnostics.append(
                    _diag(
                        "unsupported_for_loop_value_type",
                        f"Unsupported for_loop value type in reference subset: {value_type}.",
                        location=f"diagram.node:{node_id}",
                    )
                )
                continue

            node["_resolved_value_type"] = value_type

        else:
            diagnostics.append(
                _diag(
                    "unsupported_node_kind",
                    f"Unsupported diagram node kind in reference subset: {kind}.",
                    location=f"diagram.node:{node_id}",
                )
            )

    if diagnostics:
        status = "unsupported_but_valid"
        if any(diag["code"].startswith("invalid_") or diag["code"].startswith("missing_") or diag["code"].startswith("type_mismatch") for diag in diagnostics):
            status = "semantic_rejected"
        return _fail(status, source_ref, diagnostics)

    return None


def _find_constant_input_value(
    *,
    target_node_id: str,
    target_port: str,
    incoming: Dict[Tuple[str, str], List[Dict[str, Any]]],
    node_map: Dict[str, Dict[str, Any]],
) -> Optional[Any]:
    candidates = incoming.get((target_node_id, target_port), [])
    if len(candidates) != 1:
        return None
    edge = candidates[0]
    source_node = node_map.get(edge["from"]["node"])
    if source_node is None or source_node.get("kind") != "constant":
        return None
    return source_node.get("value")


def validate_source(loaded: LoadedSource) -> ValidationResult:
    source_ref = dict(loaded.artifact["source"])

    if loaded.artifact.get("status") != "ok":
        return _fail(
            "load_failed",
            source_ref,
            deepcopy(loaded.artifact.get("diagnostics", [])),
        )

    doc = deepcopy(loaded.artifact["document"])

    top_level_failure = _require_top_level_sections(doc, source_ref)
    if top_level_failure is not None:
        return top_level_failure

    interface_failure, input_types, output_types = _validate_interface(doc["interface"], source_ref)
    if interface_failure is not None:
        return interface_failure

    front_panel = doc.get("front_panel", {"widgets": []})
    front_panel_failure, widget_by_id = _validate_front_panel(front_panel, source_ref)
    if front_panel_failure is not None:
        return front_panel_failure

    diagram_failure, node_map, edges = _collect_diagram_node_map(doc["diagram"], source_ref)
    if diagram_failure is not None:
        return diagram_failure

    incoming_failure, incoming = _build_incoming_edge_map(edges, source_ref)
    if incoming_failure is not None:
        return incoming_failure

    enrich_failure = _validate_and_enrich_nodes(
        node_map=node_map,
        edges=edges,
        incoming=incoming,
        widget_by_id=widget_by_id,
        input_types=input_types,
        output_types=output_types,
        source_ref=source_ref,
    )
    if enrich_failure is not None:
        return enrich_failure

    validated_nodes = [node_map[node["id"]] for node in doc["diagram"]["nodes"]]

    validated_document = deepcopy(doc)
    validated_document["diagram"]["nodes"] = validated_nodes
    validated_document["diagram"]["edges"] = edges

    validated_subset = {
        "core_primitives": True,
        "public_interface": True,
        "widget_value": any(node["kind"] == "widget_value" for node in validated_nodes),
        "widget_reference": any(node["kind"] == "widget_reference" for node in validated_nodes),
        "ui_object_primitives": any(
            node["kind"] == "primitive" and node.get("type") == "frog.ui.property_write"
            for node in validated_nodes
        ),
        "explicit_local_memory": any(
            node["kind"] == "primitive" and node.get("type") == "frog.core.delay"
            for node in validated_nodes
        ),
        "bounded_loop": any(node["kind"] == "for_loop" for node in validated_nodes),
        "minimal_u16_widget_family": all(
            widget.get("widget") in SUPPORTED_WIDGET_CLASSES
            for widget in widget_by_id.values()
        ),
        "presentation_metadata_persisted_in_source": any(
            "face_template" in widget.get("props", {}) or "face_color" in widget.get("props", {})
            for widget in widget_by_id.values()
        ),
    }

    artifact = {
        "artifact_kind": "frog_validation_result",
        "artifact_version": DEMO_ARTIFACT_VERSION,
        "status": "ok",
        "source_ref": source_ref,
        "validated_subset": validated_subset,
        "validated_program": {
            "program_id": f"prog:{doc['metadata']['name']}",
            "entry_kind": "single_frog_program",
            "document": validated_document,
        },
        "diagnostics": [],
    }

    return ValidationResult(artifact=artifact)
