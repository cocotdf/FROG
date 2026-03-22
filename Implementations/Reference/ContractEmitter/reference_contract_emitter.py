from __future__ import annotations

from copy import deepcopy

from Implementations.Reference.common import DEFAULT_BACKEND_FAMILY, BackendContract, DEMO_ARTIFACT_VERSION, LoweredForm, ensure


def emit_backend_contract(lowered: LoweredForm, backend_family: str = DEFAULT_BACKEND_FAMILY) -> BackendContract:
    ensure(lowered.artifact["backend_family"] == backend_family, stage="emit-contract", error_code="backend_family_mismatch", message="Lowered form backend family does not match requested contract backend family.")

    lowered_unit = lowered.artifact["units"][0]
    public_inputs = [op for op in lowered_unit["operations"] if op["kind"] == "public_input"]
    public_outputs = [op for op in lowered_unit["operations"] if op["kind"] == "public_output"]
    ui_inputs = [op for op in lowered_unit["operations"] if op["kind"] == "ui_value_input"]
    ui_outputs = [op for op in lowered_unit["operations"] if op["kind"] == "ui_value_output"]
    ui_refs = [op for op in lowered_unit["operations"] if op["kind"] == "ui_widget_reference"]
    ui_property_writes = [op for op in lowered_unit["operations"] if op["kind"] == "ui_property_write"]
    state_delays = [op for op in lowered_unit["operations"] if op["kind"] == "state_delay"]

    ui_binding_kind = lowered.artifact["assumptions"]["ui_binding_kind"]
    has_state = bool(state_delays)

    artifact = {
        "artifact_kind": "frog_backend_contract",
        "artifact_version": DEMO_ARTIFACT_VERSION,
        "source_ref": dict(lowered.artifact["source_ref"]),
        "backend_family": backend_family,
        "assumptions": {
            "state_model": "explicit_local_memory" if has_state else "none",
            "ui_binding": {
                "enabled": ui_binding_kind != "none",
                "kind": ui_binding_kind,
            },
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
                "ui_bindings": {
                    "inputs": [
                        {
                            **{
                                "widget_id": op["widget_id"],
                                "widget_class": op["widget_class"],
                                "value_type": op["value_type"],
                                "participation_kind": op["ui_participation_kind"],
                            },
                            **({"default_value": op["default_value"]} if "default_value" in op else {}),
                        }
                        for op in ui_inputs
                    ],
                    "outputs": [
                        {
                            "widget_id": op["widget_id"],
                            "widget_class": op["widget_class"],
                            "value_type": op["value_type"],
                            "participation_kind": op["ui_participation_kind"],
                        }
                        for op in ui_outputs
                    ],
                },
                "ui_objects": {
                    "references": [
                        {
                            "widget_id": op["widget_id"],
                            "widget_class": op["widget_class"],
                            "widget_role": op["widget_role"],
                            "participation_kind": op["ui_participation_kind"],
                        }
                        for op in ui_refs
                    ],
                    "property_writes": [
                        {
                            "target_widget_id": op["target_widget_id"],
                            "target_widget_class": op["target_widget_class"],
                            "part": op["widget_member"]["part"],
                            "member": op["widget_member"]["member"],
                            "value_type": op["value_type"],
                            "primitive_ref": op["primitive_ref"],
                        }
                        for op in ui_property_writes
                    ],
                },
                "state": {
                    "cells": [
                        {
                            "operation_id": op["id"],
                            "primitive_ref": op["primitive_ref"],
                            "state_kind": op["state_kind"],
                            "value_type": op["value_type"],
                            "initial": op["initial"],
                        }
                        for op in state_delays
                    ]
                },
                "implementation_payload": {
                    "kind": "demo_dataflow_plan",
                    "operations": deepcopy(lowered_unit["operations"]),
                    "connections": deepcopy(lowered_unit["connections"]),
                    "ui_declarations": deepcopy(lowered_unit.get("ui_declarations", {"widgets": []})),
                },
            }
        ],
    }

    return BackendContract(artifact=artifact)
