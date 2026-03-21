from __future__ import annotations

from Implementations.Reference.common import DEFAULT_BACKEND_FAMILY, BackendContract, DEMO_ARTIFACT_VERSION, LoweredForm, ensure


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
