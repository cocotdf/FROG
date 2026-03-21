from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Tuple

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

SUPPORTED_CONTROL_WIDGETS = {"frog.ui.standard.numeric_control"}
SUPPORTED_INDICATOR_WIDGETS = {"frog.ui.standard.numeric_indicator"}


def _validate_front_panel(front_panel: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    ensure(isinstance(front_panel, dict), stage="validate", error_code="invalid_front_panel", message="front_panel must be an object.")
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
        ensure(value_type in SUPPORTED_SCALAR_TYPES, stage="validate", error_code="unsupported_widget_value_type", message=f"Unsupported widget value_type for demo slice: {value_type}")

        if widget_class in SUPPORTED_CONTROL_WIDGETS:
            ensure(role == "control", stage="validate", error_code="invalid_widget_role", message=f"Widget '{widget_id}' must use role 'control' for class '{widget_class}'.")
            props = widget.get("props", {})
            ensure(isinstance(props, dict), stage="validate", error_code="invalid_widget_props", message=f"Widget '{widget_id}' props must be an object.")
            ensure("default_value" in props, stage="validate", error_code="missing_control_default_value", message=f"Control widget '{widget_id}' requires props.default_value in this demo slice.")
            try:
                float(props["default_value"])
            except (TypeError, ValueError) as exc:
                raise FrogPipelineError(
                    stage="validate",
                    error_code="invalid_control_default_value",
                    message=f"Control widget '{widget_id}' default_value must be numeric in this demo slice.",
                ) from exc
        elif widget_class in SUPPORTED_INDICATOR_WIDGETS:
            ensure(role == "indicator", stage="validate", error_code="invalid_widget_role", message=f"Widget '{widget_id}' must use role 'indicator' for class '{widget_class}'.")
        else:
            raise FrogPipelineError(
                stage="validate",
                error_code="unsupported_widget_class",
                message=f"Unsupported widget class in demo slice: {widget_class}",
            )

        widget_by_id[widget_id] = widget

    return widget_by_id


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
        ensure(port["type"] in SUPPORTED_SCALAR_TYPES, stage="validate", error_code="unsupported_type", message=f"Unsupported input type for demo slice: {port['type']}")
        input_ports[port["id"]] = port

    for port in outputs:
        require_keys(port, ["id", "type"], stage="validate", context="interface.outputs[]")
        ensure(isinstance(port["id"], str) and port["id"], stage="validate", error_code="invalid_interface_output_id", message="Each interface output requires a non-empty string id.")
        ensure(port["id"] not in output_ports, stage="validate", error_code="duplicate_interface_output", message=f"Duplicate interface output id: {port['id']}")
        ensure(port["type"] in SUPPORTED_SCALAR_TYPES, stage="validate", error_code="unsupported_type", message=f"Unsupported output type for demo slice: {port['type']}")
        output_ports[port["id"]] = port

    node_by_id: Dict[str, Dict[str, Any]] = {}
    primitive_nodes: List[Dict[str, Any]] = []
    input_nodes_by_port: Dict[str, Dict[str, Any]] = {}
    output_nodes_by_port: Dict[str, Dict[str, Any]] = {}
    widget_value_nodes: List[Dict[str, Any]] = []

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
            widget_id = node["widget"]
            ensure(front_panel is not None, stage="validate", error_code="missing_front_panel", message="widget_value participation requires a front_panel section in this demo slice.")
            ensure(widget_id in widget_by_id, stage="validate", error_code="unknown_widget_reference", message=f"Node {node_id} references unknown widget '{widget_id}'.")
            widget_value_nodes.append(node)
        elif kind == "primitive":
            require_keys(node, ["type"], stage="validate", context=f"node {node_id}")
            ensure(node["type"] == "frog.core.add", stage="validate", error_code="unsupported_primitive", message=f"This demo pipeline only supports primitive type 'frog.core.add', not '{node['type']}'.")
            primitive_nodes.append(node)
        else:
            raise FrogPipelineError(
                stage="validate",
                error_code="unsupported_node_kind",
                message=f"Unsupported node kind in demo slice: {kind}",
                diagnostics=[{"severity": "error", "message": f"Node '{node_id}' has kind '{kind}'."}],
            )

    uses_public_interface = bool(input_ports or output_ports or input_nodes_by_port or output_nodes_by_port)
    uses_widget_value = bool(widget_value_nodes)

    ensure(uses_public_interface or uses_widget_value, stage="validate", error_code="empty_demo_slice", message="Demo slice must use either public interface participation or widget_value participation.")
    ensure(not (uses_public_interface and uses_widget_value), stage="validate", error_code="unsupported_mixed_demo_slice", message="This demo pipeline supports either the Example 01 public-interface slice or the Example 02 widget_value slice, not a hybrid.")

    if uses_public_interface:
        ensure(len(inputs) == 2, stage="validate", error_code="unsupported_input_count", message="This public-interface demo slice expects exactly two public inputs.")
        ensure(len(outputs) == 1, stage="validate", error_code="unsupported_output_count", message="This public-interface demo slice expects exactly one public output.")
        ensure(set(input_nodes_by_port.keys()) == set(input_ports.keys()), stage="validate", error_code="missing_interface_input_node", message="Every public input must have exactly one interface_input node.")
        ensure(set(output_nodes_by_port.keys()) == set(output_ports.keys()), stage="validate", error_code="missing_interface_output_node", message="Every public output must have exactly one interface_output node.")
        ensure(front_panel is None or len(widget_by_id) == 0, stage="validate", error_code="unsupported_front_panel_in_public_slice", message="The public-interface demo slice does not support front_panel/widget_value content.")
    else:
        ensure(len(inputs) == 0 and len(outputs) == 0, stage="validate", error_code="unexpected_public_interface", message="The widget_value demo slice expects an empty public interface.")
        ensure(front_panel is not None, stage="validate", error_code="missing_front_panel", message="The widget_value demo slice requires a front_panel section.")
        control_nodes = [node for node in widget_value_nodes if widget_by_id[node["widget"]]["role"] == "control"]
        indicator_nodes = [node for node in widget_value_nodes if widget_by_id[node["widget"]]["role"] == "indicator"]
        ensure(len(control_nodes) == 2, stage="validate", error_code="unsupported_widget_value_control_count", message="The widget_value demo slice expects exactly two control-side widget_value nodes.")
        ensure(len(indicator_nodes) == 1, stage="validate", error_code="unsupported_widget_value_indicator_count", message="The widget_value demo slice expects exactly one indicator-side widget_value node.")
        ensure(not input_nodes_by_port and not output_nodes_by_port, stage="validate", error_code="unexpected_interface_nodes", message="The widget_value demo slice does not support interface_input/interface_output nodes.")

    ensure(len(primitive_nodes) == 1, stage="validate", error_code="unsupported_primitive_count", message="This demo pipeline expects exactly one primitive node of type 'frog.core.add'.")
    add_node = primitive_nodes[0]

    incoming_by_target: Dict[Tuple[str, str], List[Dict[str, Any]]] = {}
    edge_ids = set()

    def validate_port_for_endpoint(node: Dict[str, Any], endpoint_port: str, direction: str) -> None:
        kind = node["kind"]

        if kind == "interface_input":
            allowed = {"value"} if direction == "from" else set()
        elif kind == "interface_output":
            allowed = {"value"} if direction == "to" else set()
        elif kind == "primitive" and node["type"] == "frog.core.add":
            allowed = {"a", "b"} if direction == "to" else {"result"}
        elif kind == "widget_value":
            widget_role = widget_by_id[node["widget"]]["role"]
            if widget_role == "control":
                allowed = {"value"} if direction == "from" else set()
            elif widget_role == "indicator":
                allowed = {"value"} if direction == "to" else set()
            else:
                allowed = set()
        else:
            allowed = set()

        ensure(endpoint_port in allowed, stage="validate", error_code="invalid_port_reference", message=f"Invalid port '{endpoint_port}' on node '{node['id']}' for edge {direction} endpoint.")

    adjacency: Dict[str, List[str]] = {node_id: [] for node_id in node_by_id}
    indegree: Dict[str, int] = {node_id: 0 for node_id in node_by_id}

    for edge in edges:
        require_keys(edge, ["id", "from", "to"], stage="validate", context="diagram.edges[]")

        edge_id = edge["id"]
        ensure(edge_id not in edge_ids, stage="validate", error_code="duplicate_edge_id", message=f"Duplicate edge id: {edge_id}")
        edge_ids.add(edge_id)

        ensure(isinstance(edge["from"], dict) and isinstance(edge["to"], dict), stage="validate", error_code="invalid_edge_endpoints", message=f"Edge {edge_id} endpoints must be objects.")
        require_keys(edge["from"], ["node", "port"], stage="validate", context=f"edge {edge_id} from")
        require_keys(edge["to"], ["node", "port"], stage="validate", context=f"edge {edge_id} to")

        from_node_id = edge["from"]["node"]
        to_node_id = edge["to"]["node"]

        ensure(from_node_id in node_by_id, stage="validate", error_code="unknown_edge_source_node", message=f"Edge {edge_id} references unknown source node '{from_node_id}'.")
        ensure(to_node_id in node_by_id, stage="validate", error_code="unknown_edge_target_node", message=f"Edge {edge_id} references unknown target node '{to_node_id}'.")

        from_node = node_by_id[from_node_id]
        to_node = node_by_id[to_node_id]

        validate_port_for_endpoint(from_node, edge["from"]["port"], "from")
        validate_port_for_endpoint(to_node, edge["to"]["port"], "to")

        target_key = (to_node_id, edge["to"]["port"])
        incoming_by_target.setdefault(target_key, []).append(edge)

        adjacency[from_node_id].append(to_node_id)
        indegree[to_node_id] += 1

    for primitive_input_port in ("a", "b"):
        key = (add_node["id"], primitive_input_port)
        ensure(len(incoming_by_target.get(key, [])) == 1, stage="validate", error_code="invalid_primitive_input_drive", message=f"Primitive input '{primitive_input_port}' must be driven by exactly one edge.")

    if uses_public_interface:
        output_node = next(iter(output_nodes_by_port.values()))
        ensure(len(incoming_by_target.get((output_node["id"], "value"), [])) == 1, stage="validate", error_code="invalid_public_output_drive", message="Public output boundary must be driven by exactly one edge.")
    else:
        indicator_node = next(node for node in widget_value_nodes if widget_by_id[node["widget"]]["role"] == "indicator")
        ensure(len(incoming_by_target.get((indicator_node["id"], "value"), [])) == 1, stage="validate", error_code="invalid_widget_value_indicator_drive", message="Indicator-side widget_value participation must be driven by exactly one edge.")

    queue = [node_id for node_id, degree in indegree.items() if degree == 0]
    visited_count = 0

    while queue:
        node_id = queue.pop(0)
        visited_count += 1

        for target_id in adjacency[node_id]:
            indegree[target_id] -= 1
            if indegree[target_id] == 0:
                queue.append(target_id)

    ensure(visited_count == len(node_by_id), stage="validate", error_code="unexpected_cycle_in_demo_slice", message="This demo slice expects an acyclic graph.")

    resolved_entities = {
        "interface_inputs": [{"id": port_id, "type": port["type"]} for port_id, port in input_ports.items()],
        "interface_outputs": [{"id": port_id, "type": port["type"]} for port_id, port in output_ports.items()],
        "widgets": [
            {
                "id": widget["id"],
                "role": widget["role"],
                "widget": widget["widget"],
                "value_type": widget["value_type"],
            }
            for widget in widget_by_id.values()
        ],
        "primitive_refs": ["frog.core.add"],
    }

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
            "widget_reference": False,
            "ui_object_primitives": False,
            "explicit_local_memory": False,
        },
        "validated_program": {
            "program_id": program_id_from_path(source_path),
            "entry_kind": "single_frog_program",
            "type_facts": [
                {"interface_port": port_id, "value_type": port["type"]}
                for port_id, port in {**input_ports, **output_ports}.items()
            ] + [
                {"widget_id": widget["id"], "value_type": widget["value_type"]}
                for widget in widget_by_id.values()
            ],
            "resolved_entities": resolved_entities,
            "document": doc,
        },
        "diagnostics": [],
    }

    return ValidationResult(artifact=artifact)
