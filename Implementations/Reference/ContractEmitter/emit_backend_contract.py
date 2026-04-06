from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List, Optional

from Implementations.Reference.common import (
    BackendContract,
    DEFAULT_BACKEND_FAMILY,
    DEMO_ARTIFACT_VERSION,
    FrogPipelineError,
    LoweredForm,
    ensure,
)


LLVM_FAMILY_ID = "llvm_cpu_v1"


def _infer_contract_family(lowered_backend_family: str) -> str:
    if lowered_backend_family == LLVM_FAMILY_ID:
        return LLVM_FAMILY_ID
    if lowered_backend_family == DEFAULT_BACKEND_FAMILY:
        return DEFAULT_BACKEND_FAMILY
    return lowered_backend_family


def _extract_main_unit(lowered: LoweredForm) -> Dict[str, Any]:
    units = lowered.artifact.get("units", [])
    ensure(
        isinstance(units, list) and len(units) == 1,
        stage="emit-backend-contract",
        error_code="invalid_lowered_units",
        message="Reference contract emission expects exactly one lowered entry unit.",
    )
    unit = units[0]
    ensure(
        isinstance(unit, dict),
        stage="emit-backend-contract",
        error_code="invalid_lowered_unit_shape",
        message="Lowered entry unit must be an object.",
    )
    return unit


def _collect_operations_by_kind(operations: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    grouped: Dict[str, List[Dict[str, Any]]] = {}
    for op in operations:
        grouped.setdefault(op["kind"], []).append(op)
    return grouped


def _infer_program_io(
    operations: List[Dict[str, Any]],
) -> Dict[str, Any]:
    public_inputs: List[Dict[str, Any]] = []
    public_outputs: List[Dict[str, Any]] = []
    ui_inputs: List[Dict[str, Any]] = []
    ui_outputs: List[Dict[str, Any]] = []
    ui_widget_refs: List[Dict[str, Any]] = []
    ui_property_writes: List[Dict[str, Any]] = []

    for op in operations:
        kind = op["kind"]

        if kind == "public_input":
            public_inputs.append(
                {
                    "interface_port": op["interface_port"],
                    "value_type": op["value_type"],
                    "source_operation": op["id"],
                }
            )

        elif kind == "public_output":
            public_outputs.append(
                {
                    "interface_port": op["interface_port"],
                    "value_type": op["value_type"],
                    "source_operation": op["id"],
                }
            )

        elif kind == "ui_value_input":
            ui_inputs.append(
                {
                    "widget_id": op["widget_id"],
                    "widget_class": op["widget_class"],
                    "value_type": op["value_type"],
                    "ui_participation_kind": op["ui_participation_kind"],
                    "source_operation": op["id"],
                    **({"default_value": op["default_value"]} if "default_value" in op else {}),
                }
            )

        elif kind == "ui_value_output":
            ui_outputs.append(
                {
                    "widget_id": op["widget_id"],
                    "widget_class": op["widget_class"],
                    "value_type": op["value_type"],
                    "ui_participation_kind": op["ui_participation_kind"],
                    "source_operation": op["id"],
                }
            )

        elif kind == "ui_widget_reference":
            ui_widget_refs.append(
                {
                    "widget_id": op["widget_id"],
                    "widget_class": op["widget_class"],
                    "widget_role": op["widget_role"],
                    "ui_participation_kind": op["ui_participation_kind"],
                    "source_operation": op["id"],
                }
            )

        elif kind == "ui_property_write":
            ui_property_writes.append(
                {
                    "target_widget_id": op.get("target_widget_id"),
                    "target_widget_class": op.get("target_widget_class"),
                    "widget_member": deepcopy(op["widget_member"]),
                    "value_type": op["value_type"],
                    "source_operation": op["id"],
                }
            )

    return {
        "public_inputs": public_inputs,
        "public_outputs": public_outputs,
        "ui_inputs": ui_inputs,
        "ui_outputs": ui_outputs,
        "ui_widget_references": ui_widget_refs,
        "ui_property_writes": ui_property_writes,
    }


def _infer_state_contract(
    operations: List[Dict[str, Any]],
    region_units: List[Dict[str, Any]],
) -> Dict[str, Any]:
    state_cells: List[Dict[str, Any]] = []

    for op in operations:
        if op["kind"] == "state_init":
            state_cells.append(
                {
                    "state_id": op["state_id"],
                    "state_kind": op["state_kind"],
                    "value_type": op["value_type"],
                    "initial_value": op.get("initial_value"),
                    "source_operation": op["id"],
                    "scope": "entry_unit",
                }
            )

    for region_unit in region_units:
        for op in region_unit.get("operations", []):
            if op["kind"] == "state_init":
                state_cells.append(
                    {
                        "state_id": op["state_id"],
                        "state_kind": op["state_kind"],
                        "value_type": op["value_type"],
                        "initial_value": op.get("initial_value"),
                        "source_operation": op["id"],
                        "scope": region_unit["id"],
                    }
                )

    return {
        "explicit_local_memory": len(state_cells) > 0,
        "state_cells": state_cells,
    }


def _infer_loop_contract(
    operations: List[Dict[str, Any]],
    region_units: List[Dict[str, Any]],
) -> Dict[str, Any]:
    loop_ops = [op for op in operations if op["kind"] == "counted_loop_execute"]

    if not loop_ops:
        return {
            "bounded_loop_present": False,
            "counted_loops": [],
        }

    counted_loops: List[Dict[str, Any]] = []

    for loop_op in loop_ops:
        matching_regions = [
            region_unit
            for region_unit in region_units
            if region_unit.get("parent_loop_object") == loop_op["source_object"]
        ]

        counted_loops.append(
            {
                "operation_id": loop_op["id"],
                "structure_type": loop_op.get("structure_type", "for_loop"),
                "iteration_count": loop_op["iteration_count"],
                "count_value": loop_op.get("count_value", loop_op["iteration_count"]),
                "value_type": loop_op["value_type"],
                "boundary": deepcopy(loop_op.get("boundary", {})),
                "structure_terminals": deepcopy(loop_op.get("structure_terminals", {})),
                "initial_value": loop_op.get("initial_value"),
                "region_units": [region_unit["id"] for region_unit in matching_regions],
                "source_operation": loop_op["id"],
            }
        )

    return {
        "bounded_loop_present": True,
        "counted_loops": counted_loops,
    }


def _infer_core_operations(
    operations: List[Dict[str, Any]],
    region_units: List[Dict[str, Any]],
) -> Dict[str, Any]:
    top_level_adds = [op for op in operations if op["kind"] == "core_primitive_add"]
    region_adds = [
        op
        for region_unit in region_units
        for op in region_unit.get("operations", [])
        if op["kind"] == "core_primitive_add"
    ]

    return {
        "top_level_add_count": len(top_level_adds),
        "region_add_count": len(region_adds),
        "total_add_count": len(top_level_adds) + len(region_adds),
    }


def emit_backend_contract(lowered: LoweredForm) -> BackendContract:
    ensure(
        lowered.artifact.get("artifact_kind") == "frog_lowered_form",
        stage="emit-backend-contract",
        error_code="invalid_lowered_artifact_kind",
        message="Backend contract emission requires a lowered form artifact.",
    )

    lowered_backend_family = lowered.artifact.get("backend_family")
    contract_family = _infer_contract_family(lowered_backend_family)

    main_unit = _extract_main_unit(lowered)
    operations = deepcopy(main_unit.get("operations", []))
    connections = deepcopy(main_unit.get("connections", []))
    region_units = deepcopy(main_unit.get("region_units", []))
    ui_declarations = deepcopy(main_unit.get("ui_declarations", {"widgets": []}))
    non_semantic_ui_metadata = deepcopy(main_unit.get("non_semantic_ui_metadata", {}))
    assumptions = deepcopy(lowered.artifact.get("assumptions", {}))

    ensure(
        isinstance(operations, list),
        stage="emit-backend-contract",
        error_code="invalid_lowered_operations_shape",
        message="Lowered entry unit 'operations' must be an array.",
    )
    ensure(
        isinstance(connections, list),
        stage="emit-backend-contract",
        error_code="invalid_lowered_connections_shape",
        message="Lowered entry unit 'connections' must be an array.",
    )
    ensure(
        isinstance(region_units, list),
        stage="emit-backend-contract",
        error_code="invalid_lowered_region_units_shape",
        message="Lowered entry unit 'region_units' must be an array.",
    )

    grouped_ops = _collect_operations_by_kind(operations)
    io_contract = _infer_program_io(operations)
    state_contract = _infer_state_contract(operations, region_units)
    loop_contract = _infer_loop_contract(operations, region_units)
    core_contract = _infer_core_operations(operations, region_units)

    contract_unit: Dict[str, Any] = {
        "id": "contract_unit:main",
        "role": "entry_unit",
        "consumer_surface": {
            "public_inputs": io_contract["public_inputs"],
            "public_outputs": io_contract["public_outputs"],
            "ui_inputs": io_contract["ui_inputs"],
            "ui_outputs": io_contract["ui_outputs"],
            "ui_widget_references": io_contract["ui_widget_references"],
            "ui_property_writes": io_contract["ui_property_writes"],
        },
        "execution_requirements": {
            "bounded_loop": loop_contract,
            "state": state_contract,
            "core_operations": core_contract,
        },
        "operations": operations,
        "connections": connections,
        "region_units": region_units,
        "ui_declarations": ui_declarations,
        "non_semantic_ui_metadata": non_semantic_ui_metadata,
        "preserved_attribution": {
            "operation_groups": {kind: [op["id"] for op in ops] for kind, ops in grouped_ops.items()},
            "source_stage": "lowered_form",
        },
    }

    contract_assumptions = {
        "backend_family": contract_family,
        "lowered_backend_family": lowered_backend_family,
        "ui_binding_enabled": assumptions.get("ui_binding_enabled", False),
        "ui_binding_kind": assumptions.get("ui_binding_kind", "none"),
        "ui_object_surface_enabled": assumptions.get("ui_object_surface_enabled", False),
        "explicit_local_memory": assumptions.get("explicit_local_memory", False),
        "state_model": assumptions.get("state_model", "none"),
        "execution_mode": assumptions.get("execution_mode", "deterministic_step_execution"),
        "bounded_loop_lowering_mode": assumptions.get("bounded_loop_lowering_mode", "none"),
        "presentation_template_runtime_support": assumptions.get("presentation_template_runtime_support", "optional"),
        "non_semantic_ui_metadata_preserved": assumptions.get("non_semantic_ui_metadata_preserved", False),
        "llvm_orientation": contract_family == LLVM_FAMILY_ID,
    }

    artifact = {
        "artifact_kind": "frog_backend_contract",
        "artifact_version": DEMO_ARTIFACT_VERSION,
        "source_ref": dict(lowered.artifact["source_ref"]),
        "program_id": lowered.artifact.get("program_id"),
        "contract_family": contract_family,
        "contract_version": "0.1",
        "assumptions": contract_assumptions,
        "units": [contract_unit],
        "diagnostics": [],
    }

    return BackendContract(artifact=artifact)
