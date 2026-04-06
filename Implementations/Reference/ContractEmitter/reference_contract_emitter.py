from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List, Optional

from Implementations.Reference.common import (
    DEFAULT_BACKEND_FAMILY,
    BackendContract,
    DEMO_ARTIFACT_VERSION,
    LoweredForm,
    ensure,
)


def _collect_operations_by_kind(operations: List[Dict[str, Any]], kind: str) -> List[Dict[str, Any]]:
    return [op for op in operations if op.get("kind") == kind]


def _build_public_boundaries(operations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    boundaries: List[Dict[str, Any]] = []

    for op in operations:
        if op.get("kind") == "public_input":
            boundaries.append(
                {
                    "kind": "public_input",
                    "name": op["interface_port"],
                    "value_type": op["value_type"],
                }
            )
        elif op.get("kind") == "public_output":
            boundaries.append(
                {
                    "kind": "public_output",
                    "name": op["interface_port"],
                    "value_type": op["value_type"],
                }
            )

    return boundaries


def _build_ui_bindings(operations: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    inputs: List[Dict[str, Any]] = []
    outputs: List[Dict[str, Any]] = []

    for op in operations:
        if op.get("kind") == "ui_value_input":
            binding = {
                "widget_id": op["widget_id"],
                "widget_class": op["widget_class"],
                "value_type": op["value_type"],
                "participation_kind": op.get("ui_participation_kind", "widget_value"),
            }
            if "default_value" in op:
                binding["default_value"] = op["default_value"]
            inputs.append(binding)

        elif op.get("kind") == "ui_value_output":
            outputs.append(
                {
                    "widget_id": op["widget_id"],
                    "widget_class": op["widget_class"],
                    "value_type": op["value_type"],
                    "participation_kind": op.get("ui_participation_kind", "widget_value"),
                }
            )

    return {
        "inputs": inputs,
        "outputs": outputs,
    }


def _build_state_cells(operations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    state_cells: List[Dict[str, Any]] = []

    for op in operations:
        if op.get("kind") == "state_init":
            state_cells.append(
                {
                    "id": op["state_id"],
                    "kind": "explicit_local_memory",
                    "value_type": op["value_type"],
                    "initial": op.get("initial_value"),
                }
            )
        elif op.get("kind") == "counted_loop_execute" and "state_id" in op:
            already_present = any(cell["id"] == op["state_id"] for cell in state_cells)
            if not already_present:
                state_cells.append(
                    {
                        "id": op["state_id"],
                        "kind": "explicit_local_memory",
                        "value_type": op["value_type"],
                        "initial": op.get("initial_value"),
                    }
                )

    return state_cells


def _collect_unsupported_surfaces(
    lowered_unit: Dict[str, Any],
    assumptions: Dict[str, Any],
) -> List[Dict[str, Any]]:
    unsupported: List[Dict[str, Any]] = []

    ui_declarations = lowered_unit.get("ui_declarations", {"widgets": []})
    supports_presentation_templates = assumptions.get("presentation_template_runtime_support", "optional")

    if supports_presentation_templates == "optional":
        for widget in ui_declarations.get("widgets", []):
            face_template = widget.get("props", {}).get("face_template")
            if face_template is not None:
                unsupported.append(
                    {
                        "surface": "face_template",
                        "widget_id": widget["id"],
                        "reason": (
                            "presentation-only metadata may be preserved without being executed "
                            "as semantic behavior"
                        ),
                    }
                )

    return unsupported


def emit_backend_contract(
    lowered: LoweredForm,
    backend_family: str = DEFAULT_BACKEND_FAMILY,
) -> BackendContract:
    ensure(
        lowered.artifact["backend_family"] == backend_family,
        stage="emit-contract",
        error_code="backend_family_mismatch",
        message="Lowered form backend family does not match requested contract backend family.",
    )

    units = lowered.artifact.get("units", [])
    ensure(
        len(units) == 1,
        stage="emit-contract",
        error_code="unsupported_unit_count",
        message="Reference contract emitter expects exactly one lowered unit.",
    )

    lowered_unit = units[0]
    operations = deepcopy(lowered_unit.get("operations", []))
    connections = deepcopy(lowered_unit.get("connections", []))
    ui_declarations = deepcopy(lowered_unit.get("ui_declarations", {"widgets": []}))
    lowered_assumptions = deepcopy(lowered.artifact.get("assumptions", {}))

    ui_bindings = _build_ui_bindings(operations)
    public_boundaries = _build_public_boundaries(operations)
    state_cells = _build_state_cells(operations)

    counted_loops = _collect_operations_by_kind(operations, "counted_loop_execute")
    iteration_count: Optional[int] = None
    if counted_loops:
        iteration_count = int(counted_loops[0]["iteration_count"])

    state_model = lowered_assumptions.get("state_model", "none")
    execution_mode = lowered_assumptions.get("execution_mode", "deterministic_step_execution")
    ui_binding_enabled = bool(ui_bindings["inputs"] or ui_bindings["outputs"] or _collect_operations_by_kind(operations, "ui_property_write"))
    widget_reference_path = bool(_collect_operations_by_kind(operations, "ui_widget_reference"))
    widget_value_path = bool(ui_bindings["inputs"] or ui_bindings["outputs"])

    contract_assumptions = {
        "state_model": state_model,
        "loop_model": "counted_loop" if iteration_count is not None else "none",
        "execution_mode": execution_mode,
        "ui_binding": {
            "enabled": ui_binding_enabled,
            "widget_value_path": widget_value_path,
            "widget_reference_path": widget_reference_path,
            "presentation_template_runtime_support": lowered_assumptions.get(
                "presentation_template_runtime_support",
                "optional",
            ),
        },
    }

    unsupported = _collect_unsupported_surfaces(lowered_unit, lowered_assumptions)

    implementation_payload = {
        "kind": "demo_dataflow_plan",
        "execution_mode": execution_mode,
        "iteration_count": iteration_count,
        "state_model": state_model,
        "operations": operations,
        "connections": connections,
        "ui_bindings": deepcopy(ui_bindings),
        "ui_declarations": ui_declarations,
    }

    artifact = {
        "artifact_kind": "frog_backend_contract",
        "artifact_version": DEMO_ARTIFACT_VERSION,
        "source_ref": dict(lowered.artifact["source_ref"]),
        "program_id": lowered.artifact.get("program_id"),
        "backend_family": backend_family,
        "assumptions": contract_assumptions,
        "units": [
            {
                "id": lowered_unit.get("id", "main"),
                "role": lowered_unit.get("role", "entry_unit"),
                "boundaries": public_boundaries,
                "ui_bindings": ui_bindings,
                "state_cells": state_cells,
                "implementation_payload": implementation_payload,
            }
        ],
        "unsupported": unsupported,
        "diagnostics": [],
    }

    return BackendContract(artifact=artifact)
