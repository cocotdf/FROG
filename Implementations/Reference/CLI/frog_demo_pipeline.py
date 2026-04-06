from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Optional

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from Implementations.Reference.common import (  # noqa: E402
    DEFAULT_BACKEND_FAMILY,
    FrogPipelineError,
)
from Implementations.Reference.Loader.reference_loader import load_source  # noqa: E402
from Implementations.Reference.Validator.reference_validator import validate_source  # noqa: E402
from Implementations.Reference.Deriver.reference_deriver import derive_execution_ir  # noqa: E402
from Implementations.Reference.Lowerer.reference_lowerer import lower_for_backend_family  # noqa: E402
from Implementations.Reference.ContractEmitter.reference_contract_emitter import (  # noqa: E402
    emit_backend_contract,
)
from Implementations.Reference.Runtime.reference_runtime import create_runtime_for_family  # noqa: E402

FIRST_PRIORITY_EXAMPLE_ID = "05_bounded_ui_accumulator"
FIRST_PRIORITY_EXAMPLE_PATH = "Examples/05_bounded_ui_accumulator/main.frog"


def pipeline_load(file_path: str):
    return load_source(file_path)


def pipeline_validate(file_path: str):
    loaded = pipeline_load(file_path)
    return validate_source(loaded)


def pipeline_derive_ir(file_path: str):
    loaded = pipeline_load(file_path)
    validation = validate_source(loaded)
    return derive_execution_ir(validation)


def pipeline_lower(file_path: str, backend_family: str = DEFAULT_BACKEND_FAMILY):
    loaded = pipeline_load(file_path)
    validation = validate_source(loaded)
    ir = derive_execution_ir(validation)
    return lower_for_backend_family(ir, backend_family)


def pipeline_emit_contract(file_path: str, backend_family: str = DEFAULT_BACKEND_FAMILY):
    loaded = pipeline_load(file_path)
    validation = validate_source(loaded)
    ir = derive_execution_ir(validation)
    lowered = lower_for_backend_family(ir, backend_family)
    return emit_backend_contract(lowered, backend_family)


def frogc_run(
    file_path: str,
    public_inputs: Dict[str, Any],
    backend_family: str = DEFAULT_BACKEND_FAMILY,
    example_id: Optional[str] = None,
) -> Dict[str, Any]:
    loaded = pipeline_load(file_path)
    validation = validate_source(loaded)
    ir = derive_execution_ir(validation)
    lowered = lower_for_backend_family(ir, backend_family)
    contract = emit_backend_contract(lowered, backend_family)

    runtime = create_runtime_for_family(backend_family)
    runtime.accept_contract(contract)
    runtime_result = runtime.execute(contract, public_inputs)

    return {
        "artifact_kind": "frog_runtime_result",
        "artifact_version": "0.1",
        "stage_ref": "run",
        "source_ref": {
            "path": loaded.artifact["source"]["path"],
            "content_hash": loaded.artifact["source"]["content_hash"],
        },
        "program_id": validation.artifact["validated_program"]["program_id"],
        "example_ref": {
            "example_id": example_id,
            "priority_slice": example_id == FIRST_PRIORITY_EXAMPLE_ID,
        },
        "status": "ok",
        "contract_ref": {
            "backend_family": contract.artifact["backend_family"],
            "unit_ids": [unit["id"] for unit in contract.artifact["units"]],
        },
        "execution_summary": {
            "backend_family": lowered.artifact["backend_family"],
            "derived_unit_id": ir.artifact["execution_unit"]["id"],
            "lowered_unit_count": len(lowered.artifact["units"]),
        },
        "outputs": runtime_result.artifact,
    }


def parse_inputs(raw: str) -> Dict[str, Any]:
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise FrogPipelineError(
            stage="run",
            error_code="invalid_inputs_json",
            message="--inputs must be valid JSON.",
        ) from exc

    if not isinstance(value, dict):
        raise FrogPipelineError(
            stage="run",
            error_code="invalid_inputs_shape",
            message="--inputs must decode to a JSON object.",
        )

    return value


def dump_json(data: Dict[str, Any], output_path: Optional[str] = None) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False)
    if output_path:
        Path(output_path).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "FROG reference demonstration pipeline for bounded executable published slices. "
            "The current priority slice is "
            f"{FIRST_PRIORITY_EXAMPLE_PATH}."
        )
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_common_arguments(cmd: argparse.ArgumentParser) -> None:
        cmd.add_argument("file", help="Path to the .frog source file.")
        cmd.add_argument(
            "--out",
            help="Optional path where the JSON artifact or result will be written.",
        )
        cmd.add_argument(
            "--example-id",
            default=None,
            help=(
                "Optional published example identifier used for reporting. "
                f"Current priority slice: {FIRST_PRIORITY_EXAMPLE_ID}."
            ),
        )
        cmd.add_argument(
            "--strict-subset",
            action="store_true",
            help=(
                "Reject unsupported-but-valid source as an explicit failure for the current "
                "reference subset."
            ),
        )

    p_load = subparsers.add_parser(
        "load",
        help="Load and decode a .frog source file into a reference loader artifact.",
    )
    add_common_arguments(p_load)

    p_validate = subparsers.add_parser(
        "validate",
        help="Validate a .frog source for the current reference subset.",
    )
    add_common_arguments(p_validate)

    p_derive = subparsers.add_parser(
        "derive-ir",
        help="Derive the open execution-facing IR from validated source.",
    )
    add_common_arguments(p_derive)

    p_lower = subparsers.add_parser(
        "lower",
        help="Lower the derived execution-facing IR for the selected backend family.",
    )
    add_common_arguments(p_lower)
    p_lower.add_argument(
        "--backend-family",
        default=DEFAULT_BACKEND_FAMILY,
        help=f"Backend family to target. Default: {DEFAULT_BACKEND_FAMILY}",
    )

    p_emit = subparsers.add_parser(
        "emit-contract",
        help="Emit the backend contract for the selected backend family.",
    )
    add_common_arguments(p_emit)
    p_emit.add_argument(
        "--backend-family",
        default=DEFAULT_BACKEND_FAMILY,
        help=f"Backend family to target. Default: {DEFAULT_BACKEND_FAMILY}",
    )

    p_run = subparsers.add_parser(
        "run",
        help="Run the full bounded demonstration corridor through runtime-side contract consumption.",
    )
    add_common_arguments(p_run)
    p_run.add_argument(
        "--backend-family",
        default=DEFAULT_BACKEND_FAMILY,
        help=f"Backend family to target. Default: {DEFAULT_BACKEND_FAMILY}",
    )
    p_run.add_argument(
        "--inputs",
        default='{"ctrl_input": 3}',
        help=(
            "External input JSON object. "
            'For the current priority slice, a useful default is {"ctrl_input": 3}. '
            'For earlier bounded examples, supply the fields expected by the selected source.'
        ),
    )

    return parser


def annotate_artifact(
    artifact: Dict[str, Any],
    *,
    stage_ref: str,
    example_id: Optional[str],
    strict_subset: bool,
) -> Dict[str, Any]:
    enriched = dict(artifact)

    enriched.setdefault("artifact_version", "0.1")
    enriched["stage_ref"] = stage_ref
    enriched["example_ref"] = {
        "example_id": example_id,
        "priority_slice": example_id == FIRST_PRIORITY_EXAMPLE_ID,
        "strict_subset": strict_subset,
    }

    return enriched


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "load":
            artifact = annotate_artifact(
                pipeline_load(args.file).artifact,
                stage_ref="load",
                example_id=args.example_id,
                strict_subset=args.strict_subset,
            )
        elif args.command == "validate":
            artifact = annotate_artifact(
                pipeline_validate(args.file).artifact,
                stage_ref="validate",
                example_id=args.example_id,
                strict_subset=args.strict_subset,
            )
        elif args.command == "derive-ir":
            artifact = annotate_artifact(
                pipeline_derive_ir(args.file).artifact,
                stage_ref="derive-ir",
                example_id=args.example_id,
                strict_subset=args.strict_subset,
            )
        elif args.command == "lower":
            artifact = annotate_artifact(
                pipeline_lower(args.file, args.backend_family).artifact,
                stage_ref="lower",
                example_id=args.example_id,
                strict_subset=args.strict_subset,
            )
        elif args.command == "emit-contract":
            artifact = annotate_artifact(
                pipeline_emit_contract(args.file, args.backend_family).artifact,
                stage_ref="emit-contract",
                example_id=args.example_id,
                strict_subset=args.strict_subset,
            )
        elif args.command == "run":
            artifact = frogc_run(
                args.file,
                parse_inputs(args.inputs),
                args.backend_family,
                args.example_id,
            )
            artifact = annotate_artifact(
                artifact,
                stage_ref="run",
                example_id=args.example_id,
                strict_subset=args.strict_subset,
            )
        else:
            parser.error(f"Unknown command: {args.command}")
            return 2

        dump_json(artifact, getattr(args, "out", None))
        return 0

    except FrogPipelineError as exc:
        failure = exc.as_dict()
        failure = annotate_artifact(
            failure,
            stage_ref=getattr(exc, "stage", "unknown"),
            example_id=getattr(args, "example_id", None),
            strict_subset=getattr(args, "strict_subset", False),
        )
        dump_json(failure, getattr(args, "out", None))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
