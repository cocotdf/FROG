from __future__ import annotations

from typing import Any, Dict, List

from Implementations.Reference.common import DEMO_ARTIFACT_VERSION, DerivedIR, ValidationResult, FrogPipelineError, ensure


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
