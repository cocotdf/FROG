from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


DEMO_ARTIFACT_VERSION = "0.1-dev"
DEFAULT_BACKEND_FAMILY = "reference_host_runtime_ui_binding"
SUPPORTED_SCALAR_TYPES = {"f64"}


class FrogPipelineError(Exception):
    def __init__(self, stage: str, error_code: str, message: str, diagnostics: Optional[List[Dict[str, Any]]] = None):
        super().__init__(message)
        self.stage = stage
        self.error_code = error_code
        self.message = message
        self.diagnostics = diagnostics or []

    def as_dict(self) -> Dict[str, Any]:
        return {
            "status": "error",
            "stage": self.stage,
            "error_code": self.error_code,
            "message": self.message,
            "diagnostics": self.diagnostics,
        }


@dataclass
class LoadedSource:
    artifact: Dict[str, Any]


@dataclass
class ValidationResult:
    artifact: Dict[str, Any]


@dataclass
class DerivedIR:
    artifact: Dict[str, Any]


@dataclass
class LoweredForm:
    artifact: Dict[str, Any]


@dataclass
class BackendContract:
    artifact: Dict[str, Any]


@dataclass
class RuntimeResult:
    artifact: Dict[str, Any]


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def sha256_text(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_json_file(path: Path) -> Tuple[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise FrogPipelineError(
            stage="load",
            error_code="source_not_found",
            message=f"Source file not found: {path}",
        ) from exc
    except OSError as exc:
        raise FrogPipelineError(
            stage="load",
            error_code="source_read_error",
            message=f"Unable to read source file: {path}",
        ) from exc

    try:
        document = json.loads(text)
    except json.JSONDecodeError as exc:
        raise FrogPipelineError(
            stage="load",
            error_code="invalid_json",
            message=f"Invalid JSON in source file: {path}",
            diagnostics=[
                {
                    "severity": "error",
                    "message": str(exc),
                    "source_anchor": {"line": exc.lineno, "column": exc.colno},
                }
            ],
        ) from exc

    if not isinstance(document, dict):
        raise FrogPipelineError(
            stage="load",
            error_code="invalid_top_level",
            message="A .frog document must decode to a JSON object.",
        )

    return text, document


def require_keys(obj: Dict[str, Any], keys: List[str], *, stage: str, context: str) -> None:
    missing = [key for key in keys if key not in obj]
    if missing:
        raise FrogPipelineError(
            stage=stage,
            error_code="missing_required_keys",
            message=f"Missing required keys in {context}: {', '.join(missing)}",
        )


def ensure(condition: bool, *, stage: str, error_code: str, message: str, diagnostics: Optional[List[Dict[str, Any]]] = None) -> None:
    if not condition:
        raise FrogPipelineError(stage=stage, error_code=error_code, message=message, diagnostics=diagnostics)


def program_id_from_path(path: Path) -> str:
    return f"prog:{path.parent.name or path.stem}"


# -----------------------------------------------------------------------------
# Stage 1 - Load
# -----------------------------------------------------------------------------

def load_source(file_path: str) -> LoadedSource:
    path = Path(file_path)
    text, document = load_json_file(path)

    artifact = {
        "artifact_kind": "frog_loaded_source",
        "artifact_version": DEMO_ARTIFACT_VERSION,
        "source": {
            "path": str(path).replace('\\', '/'),
            "content_hash": sha256_text(text),
            "spec_version": document.get("spec_version"),
        },
        "document": document,
        "diagnostics": [],
    }
    return LoadedSource(artifact=artifact)


# -----------------------------------------------------------------------------
# Stage 2 - Validate (Example 01 subset only)
# -----------------------------------------------------------------------------

def validate_source(loaded: LoadedSource) -> ValidationResult:
    doc = loaded.artifact["document"]
    source_ref = dict(loaded.artifact["source"])
    source_path = Path(source_ref["path"])

    require_keys(doc, ["spec_version", "metadata", "interface", "diagram"], stage="validate", context="top level")
    ensure(doc["spec_version"] == "0.1", stage="validate", error_code="unsupported_spec_version", message="This demo pipeline supports spec_version '0.1' only.")

    metadata = doc["metadata"]
    interface = doc["interface"]
    diagram = doc["diagram"]
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

    ensure(len(inputs) == 2, stage="validate", error_code="unsupported_input_count", message="This demo pipeline expects exactly two public inputs.")
    ensure(len(outputs) == 1, stage="validate", error_code="unsupported_output_count", message="This demo pipeline expects exactly one public output.")

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
        elif kind == "primitive":
            require_keys(node, ["type"], stage="validate", context=f"node {node_id}")
            ensure(node["type"] == "frog.core.add", stage="validate", error_code="unsupported_primitive", message=f"This demo pipeline only supports primitive type 'frog.core.add', not '{node['type']}'.")
            primitive_nodes.append(node)
        else:
            raise FrogPipelineError(
                stage="validate",
                error_code="unsupported_node_kind",
                message=f"Unsupported node kind in demo slice: {kind}",
                diagnostics=[
                    {"severity": "error", "message": f"Node '{node_id}' has kind '{kind}'."}
                ],
            )

    ensure(set(input_nodes_by_port.keys()) == set(input_ports.keys()), stage="validate", error_code="missing_interface_input_node", message="Every public input must have exactly one interface_input node.")
    ensure(set(output_nodes_by_port.keys()) == set(output_ports.keys()), stage="validate", error_code="missing_interface_output_node", message="Every public output must have exactly one interface_output node.")
    ensure(len(primitive_nodes) == 1, stage="validate", error_code="unsupported_primitive_count", message="This demo pipeline expects exactly one primitive node of type 'frog.core.add'.")

    add_node = primitive_nodes[0]
    incoming_by_target: Dict[Tuple[str, str], List[Dict[str, Any]]] = {}
    outgoing_by_source: Dict[Tuple[str, str], List[Dict[str, Any]]] = {}
    edge_ids = set()

    def validate_port_for_endpoint(node: Dict[str, Any], endpoint_port: str, direction: str) -> None:
        kind = node["kind"]
        if kind == "interface_input":
            allowed = {"value"} if direction == "from" else set()
        elif kind == "interface_output":
            allowed = {"value"} if direction == "to" else set()
        elif kind == "primitive" and node["type"] == "frog.core.add":
            allowed = {"a", "b"} if direction == "to" else {"result"}
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

        source_key = (from_node_id, edge["from"]["port"])
        target_key = (to_node_id, edge["to"]["port"])
        outgoing_by_source.setdefault(source_key, []).append(edge)
        incoming_by_target.setdefault(target_key, []).append(edge)

        adjacency[from_node_id].append(to_node_id)
        indegree[to_node_id] += 1

    for primitive_input_port in ("a", "b"):
        key = (add_node["id"], primitive_input_port)
        ensure(len(incoming_by_target.get(key, [])) == 1, stage="validate", error_code="invalid_primitive_input_drive", message=f"Primitive input '{primitive_input_port}' must be driven by exactly one edge.")

    output_node = next(iter(output_nodes_by_port.values()))
    ensure(len(incoming_by_target.get((output_node["id"], "value"), [])) == 1, stage="validate", error_code="invalid_public_output_drive", message="Public output boundary must be driven by exactly one edge.")

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
        "widgets": [],
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
            "public_interface": True,
            "widget_value": False,
            "widget_reference": False,
            "ui_object_primitives": False,
            "explicit_local_memory": False,
        },
        "validated_program": {
            "program_id": program_id_from_path(source_path),
            "entry_kind": "single_frog_program",
            "type_facts": [
                {"interface_port": port_id, "value_type": port["type"]} for port_id, port in {**input_ports, **output_ports}.items()
            ],
            "resolved_entities": resolved_entities,
            "document": doc,
        },
        "diagnostics": [],
    }
    return ValidationResult(artifact=artifact)


# -----------------------------------------------------------------------------
# Stage 3 - Derive Execution IR
# -----------------------------------------------------------------------------

def derive_execution_ir(validation: ValidationResult) -> DerivedIR:
    ensure(validation.artifact.get("status") == "ok", stage="derive-ir", error_code="validation_not_ok", message="Derivation requires a successful validation result.")

    validated_program = validation.artifact["validated_program"]
    doc = validated_program["document"]
    interface = doc["interface"]
    diagram = doc["diagram"]

    input_types = {item["id"]: item["type"] for item in interface["inputs"]}
    output_types = {item["id"]: item["type"] for item in interface["outputs"]}

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
        elif kind == "primitive":
            objects.append(
                {
                    "id": f"obj:{node_id}",
                    "kind": "primitive",
                    "primitive_ref": node["type"],
                    "ports": [
                        {"id": "a", "direction": "in", "value_type": "f64"},
                        {"id": "b", "direction": "in", "value_type": "f64"},
                        {"id": "result", "direction": "out", "value_type": "f64"},
                    ],
                    "sources": [f"diagram.node:{node_id}"],
                }
            )
        else:
            raise FrogPipelineError(stage="derive-ir", error_code="unsupported_node_kind", message=f"Unsupported node kind during derivation: {kind}")

    for edge in diagram["edges"]:
        connections.append(
            {
                "id": f"conn:{edge['id']}",
                "from": {"object": f"obj:{edge['from']['node']}", "port": edge['from']['port']},
                "to": {"object": f"obj:{edge['to']['node']}", "port": edge['to']['port']},
                "sources": [f"diagram.edge:{edge['id']}"],
            }
        )

    artifact = {
        "artifact_kind": "frog_derived_execution_ir",
        "artifact_version": DEMO_ARTIFACT_VERSION,
        "source_ref": dict(validation.artifact["source_ref"]),
        "validation_ref": {
            "status": validation.artifact["status"],
            "program_id": validation.artifact["validated_program"]["program_id"],
        },
        "execution_unit": {
            "id": "unit:main",
            "family": "execution_unit",
            "objects": objects,
            "connections": connections,
            "support_objects": [],
        },
        "diagnostics": [],
    }
    return DerivedIR(artifact=artifact)


# -----------------------------------------------------------------------------
# Stage 4 - Lower for backend family
# -----------------------------------------------------------------------------

def lower_for_backend_family(ir: DerivedIR, backend_family: str = DEFAULT_BACKEND_FAMILY) -> LoweredForm:
    ensure(backend_family == DEFAULT_BACKEND_FAMILY, stage="lower", error_code="unsupported_backend_family", message=f"This demo pipeline supports backend family '{DEFAULT_BACKEND_FAMILY}' only.")

    unit = ir.artifact["execution_unit"]
    objects = unit["objects"]

    operations: List[Dict[str, Any]] = []
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
            "ui_binding_enabled": False,
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


# -----------------------------------------------------------------------------
# Stage 5 - Emit backend contract
# -----------------------------------------------------------------------------

def emit_backend_contract(lowered: LoweredForm, backend_family: str = DEFAULT_BACKEND_FAMILY) -> BackendContract:
    ensure(lowered.artifact["backend_family"] == backend_family, stage="emit-contract", error_code="backend_family_mismatch", message="Lowered form backend family does not match requested contract backend family.")

    lowered_unit = lowered.artifact["units"][0]
    public_inputs = [op for op in lowered_unit["operations"] if op["kind"] == "public_input"]
    public_outputs = [op for op in lowered_unit["operations"] if op["kind"] == "public_output"]

    artifact = {
        "artifact_kind": "frog_backend_contract",
        "artifact_version": DEMO_ARTIFACT_VERSION,
        "source_ref": dict(lowered.artifact["source_ref"]),
        "backend_family": backend_family,
        "assumptions": {
            "state_model": "none",
            "ui_binding": {"enabled": False},
            "execution_mode": "deterministic_step_execution",
        },
        "units": [
            {
                "id": "main",
                "role": "entry_unit",
                "boundaries": [
                    *[
                        {"kind": "public_input", "name": op["interface_port"], "value_type": op["value_type"]}
                        for op in public_inputs
                    ],
                    *[
                        {"kind": "public_output", "name": op["interface_port"], "value_type": op["value_type"]}
                        for op in public_outputs
                    ],
                ],
                "implementation_payload": {
                    "kind": "demo_dataflow_plan",
                    "operations": lowered_unit["operations"],
                    "connections": lowered_unit["connections"],
                },
            }
        ],
        "unsupported": [],
        "diagnostics": [],
    }
    return BackendContract(artifact=artifact)


# -----------------------------------------------------------------------------
# Stage 6 - Runtime
# -----------------------------------------------------------------------------

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
            },
            "diagnostics": [],
        }
        return RuntimeResult(artifact=artifact)


# -----------------------------------------------------------------------------
# Orchestration
# -----------------------------------------------------------------------------

def create_runtime_for_family(backend_family: str) -> ReferenceHostRuntime:
    return ReferenceHostRuntime(backend_family=backend_family)


def pipeline_validate(file_path: str) -> ValidationResult:
    loaded = load_source(file_path)
    return validate_source(loaded)


def pipeline_derive_ir(file_path: str) -> DerivedIR:
    loaded = load_source(file_path)
    validation = validate_source(loaded)
    return derive_execution_ir(validation)


def pipeline_lower(file_path: str, backend_family: str = DEFAULT_BACKEND_FAMILY) -> LoweredForm:
    loaded = load_source(file_path)
    validation = validate_source(loaded)
    ir = derive_execution_ir(validation)
    return lower_for_backend_family(ir, backend_family)


def pipeline_emit_contract(file_path: str, backend_family: str = DEFAULT_BACKEND_FAMILY) -> BackendContract:
    loaded = load_source(file_path)
    validation = validate_source(loaded)
    ir = derive_execution_ir(validation)
    lowered = lower_for_backend_family(ir, backend_family)
    return emit_backend_contract(lowered, backend_family)


def frogc_run(file_path: str, public_inputs: Dict[str, Any], backend_family: str = DEFAULT_BACKEND_FAMILY) -> Dict[str, Any]:
    source = load_source(file_path)
    validation = validate_source(source)
    ir = derive_execution_ir(validation)
    lowered = lower_for_backend_family(ir, backend_family)
    contract = emit_backend_contract(lowered, backend_family)
    runtime = create_runtime_for_family(backend_family)
    runtime.accept_contract(contract)
    result = runtime.execute(contract, public_inputs)
    return {
        "status": "ok",
        "source": {
            "path": source.artifact["source"]["path"],
            "content_hash": source.artifact["source"]["content_hash"],
        },
        "validation": {
            "status": validation.artifact["status"],
            "program_id": validation.artifact["validated_program"]["program_id"],
        },
        "ir": {
            "unit_id": ir.artifact["execution_unit"]["id"],
            "object_count": len(ir.artifact["execution_unit"]["objects"]),
            "connection_count": len(ir.artifact["execution_unit"]["connections"]),
        },
        "lowered": {
            "backend_family": lowered.artifact["backend_family"],
            "unit_count": len(lowered.artifact["units"]),
        },
        "contract": {
            "backend_family": contract.artifact["backend_family"],
            "unit_ids": [unit["id"] for unit in contract.artifact["units"]],
        },
        "runtime": result.artifact,
    }


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------

def parse_inputs(raw: str) -> Dict[str, Any]:
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise FrogPipelineError(stage="run", error_code="invalid_inputs_json", message="--inputs must be valid JSON.") from exc
    ensure(isinstance(value, dict), stage="run", error_code="invalid_inputs_shape", message="--inputs must decode to a JSON object.")
    return value


def dump_json(data: Dict[str, Any], output_path: Optional[str] = None) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False)
    if output_path:
        Path(output_path).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="FROG demonstration pipeline for Example 01 (pure addition).")
    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_common_arguments(cmd: argparse.ArgumentParser) -> None:
        cmd.add_argument("file", help="Path to the .frog source file.")
        cmd.add_argument("--out", help="Optional path where the JSON artifact/result will be written.")

    p_validate = subparsers.add_parser("validate", help="Validate a .frog source for the demo subset.")
    add_common_arguments(p_validate)

    p_derive = subparsers.add_parser("derive-ir", help="Derive the open execution-facing IR.")
    add_common_arguments(p_derive)

    p_lower = subparsers.add_parser("lower", help="Lower the derived IR for the demo backend family.")
    add_common_arguments(p_lower)
    p_lower.add_argument("--backend-family", default=DEFAULT_BACKEND_FAMILY)

    p_emit = subparsers.add_parser("emit-contract", help="Emit the backend contract.")
    add_common_arguments(p_emit)
    p_emit.add_argument("--backend-family", default=DEFAULT_BACKEND_FAMILY)

    p_run = subparsers.add_parser("run", help="Run the full end-to-end demonstration pipeline.")
    add_common_arguments(p_run)
    p_run.add_argument("--backend-family", default=DEFAULT_BACKEND_FAMILY)
    p_run.add_argument(
        "--inputs",
        default='{"a": 1.5, "b": 2.5}',
        help='Public input JSON object, e.g. {"a": 2.0, "b": 3.0}',
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "validate":
            artifact = pipeline_validate(args.file).artifact
        elif args.command == "derive-ir":
            artifact = pipeline_derive_ir(args.file).artifact
        elif args.command == "lower":
            artifact = pipeline_lower(args.file, args.backend_family).artifact
        elif args.command == "emit-contract":
            artifact = pipeline_emit_contract(args.file, args.backend_family).artifact
        elif args.command == "run":
            artifact = frogc_run(args.file, parse_inputs(args.inputs), args.backend_family)
        else:
            parser.error(f"Unknown command: {args.command}")
            return 2

        dump_json(artifact, args.out)
        return 0
    except FrogPipelineError as exc:
        dump_json(exc.as_dict(), getattr(args, "out", None))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
