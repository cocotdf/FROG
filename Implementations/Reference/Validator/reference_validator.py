from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

from Implementations.Reference.common import (
    DEMO_ARTIFACT_VERSION,
    SUPPORTED_SCALAR_TYPES,
    FrogPipelineError,
    LoadedSource,
    ValidationResult,
    ensure,
    program_id_from_path,
    require_keys,
)

SUPPORTED_WIDGET_CLASSES = {
    "frog.ui.standard.numeric_control": {"role": "control", "value_type": "f64"},
    "frog.ui.standard.numeric_indicator": {"role": "indicator", "value_type": "f64"},
}

SUPPORTED_PRIMITIVES = {"frog.core.add", "frog.core.delay", "frog.ui.property_write"}

SUPPORTED_WRITABLE_MEMBERS = {
    ("frog.ui.standard.numeric_control", "label", "text"): "string",
    ("frog.ui.standard.numeric_indicator", "label", "text"): "string",
}


def _coerce_port_type(value: Any) -> str:
    ensure(isinstance(value, str) and value in SUPPORTED_SCALAR_TYPES, stage="validate", error_code="unsupported_type", message=f"Unsupported scalar type for demo slice: {value}")
    return value


def _validate_widget_parts(widget_id: str, widget: Dict[str, Any]) -> None:
    parts = widget.get("parts", {})
    ensure(isinstance(parts, dict), stage="validate", error_code="invalid_widget_parts", message=f"Widget '{widget_id}' parts must be an object when present.")
    for part_name, part in parts.items():
        ensure(isinstance(part_name, str) and part_name, stage="validate", error_code="invalid_widget_part_name", message=f"Widget '{widget_id}' contains an invalid part name.")
        ensure(isinstance(part, dict), stage="validate", error_code="invalid_widget_part", message=f"Widget '{widget_id}' part '{part_name}' must be an object.")
        require_keys(part, ["class", "props"], stage="validate", context=f"front_panel.widget:{widget_id}.parts.{part_name}")
        ensure(isinstance(part["props"], dict), stage="validate", error_code="invalid_widget_part_props", message=f"Widget '{widget_id}' part '{part_name}' props must be an object.")


def _validate_front_panel(front_panel: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    ensure(isinstance(front_panel, dict), stage="validate", error_code="invalid_front_panel", message="front_panel must be an object.")
    canvas = front_panel.get("canvas", {})
    ensure(isinstance(canvas, dict), stage="validate", error_code="invalid_front_panel_canvas", message="front_panel.canvas must be an object when present.")
    widgets = front_panel.get("widgets")
    ensure(isinstance(widgets, list), stage="validate", error_code="invalid_front_panel_widgets", message="front_panel.widgets must be a list.")

    widget_by_id: Dict[str, Dict[str, Any]] = {}

    for widget in widgets:
        require_keys(widget, ["id", "role", "widget", "value_type"], stage="validate", context="front_panel.widgets[]")
        widget_id = widget["id"]
        role = widget["role"]
        widget_class = widget["widget"]
        value_type = widget["value_type"]

        ensure(isinstance(widget_id, str) and widget_id, stage="validate", error_code="invalid_widget_id", message="Each widget requires a non-empty string id.")
        ensure(widget_id not in widget_by_id, stage="validate", error_code="duplicate_widget_id", message=f"Duplicate widget id: {widget_id}")
        ensure(widget_class in SUPPORTED_WIDGET_CLASSES, stage="validate", error_code="unsupported_widget_class", message=f"Unsupported widget class in demo slice: {widget_class}")
        ensure(role == SUPPORTED_WIDGET_CLASSES[widget_class]["role"], stage="validate", error_code="invalid_widget_role", message=f"Widget '{widget_id}' must use role '{SUPPORTED_WIDGET_CLASSES[widget_class]['role']}' for class '{widget_class}'.")
        ensure(_coerce_port_type(value_type) == SUPPORTED_WIDGET_CLASSES[widget_class]["value_type"], stage="validate", error_code="invalid_widget_value_type", message=f"Widget '{widget_id}' must use value_type '{SUPPORTED_WIDGET_CLASSES[widget_class]['value_type']}' for class '{widget_class}'.")

        props = widget.get("props", {})
        ensure(isinstance(props, dict), stage="validate", error_code="invalid_widget_props", message=f"Widget '{widget_id}' props must be an object.")
        if role == "control":
            ensure("default_value" in props, stage="validate", error_code="missing_control_default_value", message=f"Control widget '{widget_id}' requires props.default_value in this demo slice.")
            try:
                float(props["default_value"])
            except (TypeError, ValueError) as exc:
                raise FrogPipelineError(stage="validate", error_code="invalid_control_default_value", message=f"Control widget '{widget_id}' default_value must be numeric in this demo slice.") from exc

        _validate_widget_parts(widget_id, widget)
        widget_by_id[widget_id] = widget

    return widget_by_id


def _node_port_specs(node: Dict[str, Any], *, input_ports: Dict[str, Dict[str, Any]], output_ports: Dict[str, Dict[str, Any]], widget_by_id: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, str]]:
    kind = node["kind"]
    if kind == "interface_input":
        port_id = node["interface_port"]
        return {"value": {"direction": "out", "value_type": input_ports[port_id]["type"]}}
    if kind == "interface_output":
        port_id = node["interface_port"]
        return {"value": {"direction": "in", "value_type": output_ports[port_id]["type"]}}
    if kind == "widget_value":
        widget = widget_by_id[node["widget"]]
        direction = "out" if widget["role"] == "control" else "in"
        return {"value": {"direction": direction, "value_type": widget["value_type"]}}
    if kind == "widget_reference":
        return {"ref": {"direction": "out", "value_type": "widget_reference"}}
    if kind == "primitive":
        if node["type"] == "frog.core.add":
            return {
                "a": {"direction": "in", "value_type": "f64"},
                "b": {"direction": "in", "value_type": "f64"},
                "result": {"direction": "out", "value_type": "f64"},
            }
        if node["type"] == "frog.core.delay":
            return {
                "in": {"direction": "in", "value_type": "f64"},
                "out": {"direction": "out", "value_type": "f64"},
            }
        if node["type"] == "frog.ui.property_write":
            return {
                "ref": {"direction": "in", "value_type": "widget_reference"},
                "value": {"direction": "in", "value_type": node["_resolved_value_type"]},
            }
    raise FrogPipelineError(stage="validate", error_code="unsupported_node_kind", message=f"Unsupported node kind in demo slice: {kind}")


def _find_single_incoming(node_id: str, port: str, edges: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    matches = [edge for edge in edges if edge["to"]["node"] == node_id and edge["to"]["port"] == port]
    if not matches:
        return None
    if len(matches) > 1:
        raise FrogPipelineError(stage="validate", error_code="multiple_incoming_edges", message=f"Node '{node_id}' port '{port}' received multiple incoming edges in the demo slice.")
    return matches[0]


def _find_outgoing(node_id: str, port: str, edges: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [edge for edge in edges if edge["from"]["node"] == node_id and edge["from"]["port"] == port]


def validate_source(loaded: LoadedSource) -> ValidationResult:
    doc = loaded.artifact["document"]
    source_ref = dict(loaded.artifact["source"])
    source_path = Path(source_ref["path"])

    require_keys(doc, ["spec_version", "metadata", "interface", "diagram"], stage="validate", context="top level")
    ensure(doc["spec_version"] == "0.1", stage="validate", error_code="unsupported_spec_version", message="This demo pipeline supports spec_version '0.1' only.")

    metadata = doc["metadata"]
    interface = doc["interface"]
    diagram = doc["diagram"]
    front_panel = doc.get("front_panel")

    ensure(isinstance(metadata, dict), stage="validate", error_code="invalid_metadata", message="metadata must be an object.")
    ensure(isinstance(interface, dict), stage="validate", error_code="invalid_interface", message="interface must be an object.")
    ensure(isinstance(diagram, dict), stage="validate", error_code="invalid_diagram", message="diagram must be an object.")

    require_keys(interface, ["inputs", "outputs"], stage="validate", context="interface")
    require_keys(diagram, ["nodes", "edges"], stage="validate", context="diagram")

    inputs = interface["inputs"]
    outputs = interface["outputs"]
    nodes = diagram["nodes"]
    edges = diagram["edges"]

    ensure(isinstance(inputs, list), stage="validate", error_code="invalid_interface_inputs", message="interface.inputs must be a list.")
    ensure(isinstance(outputs, list), stage="validate", error_code="invalid_interface_outputs", message="interface.outputs must be a list.")
    ensure(isinstance(nodes, list), stage="validate", error_code="invalid_diagram_nodes", message="diagram.nodes must be a list.")
    ensure(isinstance(edges, list), stage="validate", error_code="invalid_diagram_edges", message="diagram.edges must be a list.")

    widget_by_id: Dict[str, Dict[str, Any]] = {}
    if front_panel is not None:
        widget_by_id = _validate_front_panel(front_panel)

    input_ports: Dict[str, Dict[str, Any]] = {}
    output_ports: Dict[str, Dict[str, Any]] = {}

    for port in inputs:
        require_keys(port, ["id", "type"], stage="validate", context="interface.inputs[]")
        ensure(isinstance(port["id"], str) and port["id"], stage="validate", error_code="invalid_interface_input_id", message="Each interface input requires a non-empty string id.")
        ensure(port["id"] not in input_ports, stage="validate", error_code="duplicate_interface_input", message=f"Duplicate interface input id: {port['id']}")
        _coerce_port_type(port["type"])
        input_ports[port["id"]] = port

    for port in outputs:
        require_keys(port, ["id", "type"], stage="validate", context="interface.outputs[]")
        ensure(isinstance(port["id"], str) and port["id"], stage="validate", error_code="invalid_interface_output_id", message="Each interface output requires a non-empty string id.")
        ensure(port["id"] not in output_ports, stage="validate", error_code="duplicate_interface_output", message=f"Duplicate interface output id: {port['id']}")
        _coerce_port_type(port["type"])
        output_ports[port["id"]] = port

    node_by_id: Dict[str, Dict[str, Any]] = {}
    input_nodes_by_port: Dict[str, Dict[str, Any]] = {}
    output_nodes_by_port: Dict[str, Dict[str, Any]] = {}
    widget_value_nodes: List[Dict[str, Any]] = []
    widget_reference_nodes: List[Dict[str, Any]] = []
    primitive_nodes: List[Dict[str, Any]] = []
    delay_nodes: List[Dict[str, Any]] = []

    for node in nodes:
        require_keys(node, ["id", "kind"], stage="validate", context="diagram.nodes[]")
        node_id = node["id"]
        kind = node["kind"]
        ensure(isinstance(node_id, str) and node_id, stage="validate", error_code="invalid_node_id", message="Each diagram node requires a non-empty string id.")
        ensure(node_id not in node_by_id, stage="validate", error_code="duplicate_node_id", message=f"Duplicate node id: {node_id}")
        node_by_id[node_id] = node

        if kind == "interface_input":
            require_keys(node, ["interface_port"], stage="validate", context=f"node {node_id}")
            port_id = node["interface_port"]
            ensure(port_id in input_ports, stage="validate", error_code="unknown_interface_input", message=f"Node {node_id} references unknown interface input port '{port_id}'.")
            ensure(port_id not in input_nodes_by_port, stage="validate", error_code="duplicate_interface_input_node", message=f"Multiple interface_input nodes reference port '{port_id}'.")
            input_nodes_by_port[port_id] = node
        elif kind == "interface_output":
            require_keys(node, ["interface_port"], stage="validate", context=f"node {node_id}")
            port_id = node["interface_port"]
            ensure(port_id in output_ports, stage="validate", error_code="unknown_interface_output", message=f"Node {node_id} references unknown interface output port '{port_id}'.")
            ensure(port_id not in output_nodes_by_port, stage="validate", error_code="duplicate_interface_output_node", message=f"Multiple interface_output nodes reference port '{port_id}'.")
            output_nodes_by_port[port_id] = node
        elif kind == "widget_value":
            require_keys(node, ["widget"], stage="validate", context=f"node {node_id}")
            ensure(front_panel is not None, stage="validate", error_code="missing_front_panel", message="widget_value participation requires a front_panel section in this demo slice.")
            ensure(node["widget"] in widget_by_id, stage="validate", error_code="unknown_widget_reference", message=f"Node {node_id} references unknown widget '{node['widget']}'.")
            widget_value_nodes.append(node)
        elif kind == "widget_reference":
            require_keys(node, ["widget"], stage="validate", context=f"node {node_id}")
            ensure(front_panel is not None, stage="validate", error_code="missing_front_panel", message="widget_reference participation requires a front_panel section in this demo slice.")
            ensure(node["widget"] in widget_by_id, stage="validate", error_code="unknown_widget_reference", message=f"Node {node_id} references unknown widget '{node['widget']}'.")
            widget_reference_nodes.append(node)
        elif kind == "primitive":
            require_keys(node, ["type"], stage="validate", context=f"node {node_id}")
            ensure(node["type"] in SUPPORTED_PRIMITIVES, stage="validate", error_code="unsupported_primitive", message=f"Unsupported primitive type in demo slice: {node['type']}")
            if node["type"] == "frog.ui.property_write":
                require_keys(node, ["widget_member"], stage="validate", context=f"node {node_id}")
                ensure(isinstance(node["widget_member"], dict), stage="validate", error_code="invalid_widget_member", message=f"Node {node_id} widget_member must be an object.")
                require_keys(node["widget_member"], ["part", "member"], stage="validate", context=f"node {node_id}.widget_member")
            if node["type"] == "frog.core.delay":
                require_keys(node, ["initial"], stage="validate", context=f"node {node_id}")
                try:
                    node["_coerced_initial"] = float(node["initial"])
                except (TypeError, ValueError) as exc:
                    raise FrogPipelineError(stage="validate", error_code="invalid_delay_initial", message=f"Delay node '{node_id}' requires a numeric initial value for this demo slice.") from exc
                delay_nodes.append(node)
            primitive_nodes.append(node)
        else:
            raise FrogPipelineError(stage="validate", error_code="unsupported_node_kind", message=f"Unsupported node kind in demo slice: {kind}")

    uses_public_interface = bool(input_ports or output_ports)
    uses_widget_value = bool(widget_value_nodes)
    uses_widget_reference = bool(widget_reference_nodes)
    uses_ui_object_primitives = any(node["type"] == "frog.ui.property_write" for node in primitive_nodes)
    uses_explicit_local_memory = bool(delay_nodes)

    for edge in edges:
        require_keys(edge, ["id", "from", "to"], stage="validate", context="diagram.edges[]")
        edge_id = edge["id"]
        ensure(isinstance(edge_id, str) and edge_id, stage="validate", error_code="invalid_edge_id", message="Each edge requires a non-empty string id.")
        ensure(isinstance(edge["from"], dict) and isinstance(edge["to"], dict), stage="validate", error_code="invalid_edge_endpoints", message=f"Edge {edge_id} endpoints must be objects.")
        require_keys(edge["from"], ["node", "port"], stage="validate", context=f"edge {edge_id} from")
        require_keys(edge["to"], ["node", "port"], stage="validate", context=f"edge {edge_id} to")
        from_node_id = edge["from"]["node"]
        to_node_id = edge["to"]["node"]
        ensure(from_node_id in node_by_id, stage="validate", error_code="unknown_edge_source_node", message=f"Edge {edge_id} references unknown source node '{from_node_id}'.")
        ensure(to_node_id in node_by_id, stage="validate", error_code="unknown_edge_target_node", message=f"Edge {edge_id} references unknown target node '{to_node_id}'.")

    for node in primitive_nodes:
        if node["type"] != "frog.ui.property_write":
            continue
        node_id = node["id"]
        ref_edge = _find_single_incoming(node_id, "ref", edges)
        ensure(ref_edge is not None, stage="validate", error_code="missing_property_write_ref", message=f"Property write node '{node_id}' requires one incoming ref edge.")
        ref_source_node = node_by_id[ref_edge["from"]["node"]]
        ensure(ref_source_node["kind"] == "widget_reference", stage="validate", error_code="invalid_property_write_ref_source", message=f"Property write node '{node_id}' ref input must come from a widget_reference node.")
        widget = widget_by_id[ref_source_node["widget"]]
        member = node["widget_member"]
        part_name = member["part"]
        property_name = member["member"]
        ensure(part_name in widget.get("parts", {}), stage="validate", error_code="unknown_widget_part", message=f"Widget '{ref_source_node['widget']}' does not declare part '{part_name}'.")
        part_props = widget["parts"][part_name]["props"]
        ensure(property_name in part_props, stage="validate", error_code="unknown_widget_member", message=f"Widget '{ref_source_node['widget']}' part '{part_name}' does not declare property '{property_name}'.")
        expected_value_type = SUPPORTED_WRITABLE_MEMBERS.get((widget["widget"], part_name, property_name))
        ensure(expected_value_type is not None, stage="validate", error_code="unsupported_widget_member_write", message=f"Unsupported writable widget member in demo slice: {widget['widget']}.{part_name}.{property_name}")
        node["_resolved_widget_id"] = ref_source_node["widget"]
        node["_resolved_widget_class"] = widget["widget"]
        node["_resolved_value_type"] = expected_value_type

    port_specs_by_node = {
        node_id: _node_port_specs(node, input_ports=input_ports, output_ports=output_ports, widget_by_id=widget_by_id)
        for node_id, node in node_by_id.items()
    }

    for edge in edges:
        edge_id = edge["id"]
        from_node_id = edge["from"]["node"]
        to_node_id = edge["to"]["node"]
        src_port = edge["from"]["port"]
        dst_port = edge["to"]["port"]
        src_specs = port_specs_by_node[from_node_id]
        dst_specs = port_specs_by_node[to_node_id]
        ensure(src_port in src_specs, stage="validate", error_code="unknown_edge_source_port", message=f"Edge {edge_id} references unknown source port '{src_port}' on node '{from_node_id}'.")
        ensure(dst_port in dst_specs, stage="validate", error_code="unknown_edge_target_port", message=f"Edge {edge_id} references unknown target port '{dst_port}' on node '{to_node_id}'.")
        ensure(src_specs[src_port]["direction"] == "out", stage="validate", error_code="invalid_edge_source_direction", message=f"Edge {edge_id} source port '{from_node_id}.{src_port}' is not an output port.")
        ensure(dst_specs[dst_port]["direction"] == "in", stage="validate", error_code="invalid_edge_target_direction", message=f"Edge {edge_id} target port '{to_node_id}.{dst_port}' is not an input port.")
        ensure(src_specs[src_port]["value_type"] == dst_specs[dst_port]["value_type"], stage="validate", error_code="edge_type_mismatch", message=f"Edge {edge_id} type mismatch: {from_node_id}.{src_port} ({src_specs[src_port]['value_type']}) -> {to_node_id}.{dst_port} ({dst_specs[dst_port]['value_type']}).")

    for node in primitive_nodes:
        node_id = node["id"]
        if node["type"] == "frog.core.add":
            ensure(_find_single_incoming(node_id, "a", edges) is not None, stage="validate", error_code="missing_add_input_a", message=f"Primitive '{node_id}' requires one incoming edge on port 'a'.")
            ensure(_find_single_incoming(node_id, "b", edges) is not None, stage="validate", error_code="missing_add_input_b", message=f"Primitive '{node_id}' requires one incoming edge on port 'b'.")
        elif node["type"] == "frog.core.delay":
            ensure(_find_single_incoming(node_id, "in", edges) is not None, stage="validate", error_code="missing_delay_input", message=f"Delay node '{node_id}' requires one incoming edge on port 'in'.")
            ensure(len(_find_outgoing(node_id, "out", edges)) >= 1, stage="validate", error_code="missing_delay_output_use", message=f"Delay node '{node_id}' requires at least one outgoing edge on port 'out'.")
        elif node["type"] == "frog.ui.property_write":
            value_edge = _find_single_incoming(node_id, "value", edges)
            ensure(value_edge is not None, stage="validate", error_code="missing_property_write_value", message=f"Property write node '{node_id}' requires one incoming value edge.")

    artifact = {
        "artifact_kind": "frog_validation_result",
        "artifact_version": DEMO_ARTIFACT_VERSION,
        "source_ref": {
            "path": source_ref["path"],
            "content_hash": source_ref["content_hash"],
        },
        "status": "ok",
        "validated_subset": {
            "core_primitives": True,
            "public_interface": uses_public_interface,
            "widget_value": uses_widget_value,
            "widget_reference": uses_widget_reference,
            "ui_object_primitives": uses_ui_object_primitives,
            "explicit_local_memory": uses_explicit_local_memory,
        },
        "validated_program": {
            "program_id": program_id_from_path(source_path),
            "entry_kind": "single_frog_program",
            "type_facts": [
                *[
                    {"interface_port": port_id, "value_type": port["type"]}
                    for port_id, port in input_ports.items()
                ],
                *[
                    {"interface_port": port_id, "value_type": port["type"]}
                    for port_id, port in output_ports.items()
                ],
            ],
            "document": doc,
        },
        "diagnostics": [],
    }

    return ValidationResult(artifact=artifact)
