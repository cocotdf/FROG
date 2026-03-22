from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Optional

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from Implementations.Reference.common import DEFAULT_BACKEND_FAMILY, FrogPipelineError
from Implementations.Reference.Loader.reference_loader import load_source
from Implementations.Reference.Validator.reference_validator import validate_source
from Implementations.Reference.Deriver.reference_deriver import derive_execution_ir
from Implementations.Reference.Lowerer.reference_lowerer import lower_for_backend_family
from Implementations.Reference.ContractEmitter.reference_contract_emitter import emit_backend_contract
from Implementations.Reference.Runtime.reference_runtime import create_runtime_for_family


def pipeline_validate(file_path: str):
    loaded = load_source(file_path)
    return validate_source(loaded)


def pipeline_derive_ir(file_path: str):
    loaded = load_source(file_path)
    validation = validate_source(loaded)
    return derive_execution_ir(validation)


def pipeline_lower(file_path: str, backend_family: str = DEFAULT_BACKEND_FAMILY):
    loaded = load_source(file_path)
    validation = validate_source(loaded)
    ir = derive_execution_ir(validation)
    return lower_for_backend_family(ir, backend_family)


def pipeline_emit_contract(file_path: str, backend_family: str = DEFAULT_BACKEND_FAMILY):
    loaded = load_source(file_path)
    validation = validate_source(loaded)
    ir = derive_execution_ir(validation)
    lowered = lower_for_backend_family(ir, backend_family)
    return emit_backend_contract(lowered, backend_family)


def frogc_run(
    file_path: str,
    public_inputs: Dict[str, Any],
    backend_family: str = DEFAULT_BACKEND_FAMILY,
) -> Dict[str, Any]:
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


def parse_inputs(raw: str) -> Dict[str, Any]:
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise FrogPipelineError(stage="run", error_code="invalid_inputs_json", message="--inputs must be valid JSON.") from exc

    if not isinstance(value, dict):
        raise FrogPipelineError(stage="run", error_code="invalid_inputs_shape", message="--inputs must decode to a JSON object.")

    return value


def dump_json(data: Dict[str, Any], output_path: Optional[str] = None) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False)
    if output_path:
        Path(output_path).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="FROG demonstration pipeline for the first executable published slices.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_common_arguments(cmd: argparse.ArgumentParser) -> None:
        cmd.add_argument("file", help="Path to the .frog source file.")
        cmd.add_argument("--out", help="Optional path where the JSON artifact or result will be written.")

    p_validate = subparsers.add_parser("validate", help="Validate a .frog source for the current demonstration subset.")
    add_common_arguments(p_validate)

    p_derive = subparsers.add_parser("derive-ir", help="Derive the open execution-facing IR.")
    add_common_arguments(p_derive)

    p_lower = subparsers.add_parser("lower", help="Lower the derived IR for the selected backend family.")
    add_common_arguments(p_lower)
    p_lower.add_argument("--backend-family", default=DEFAULT_BACKEND_FAMILY, help=f"Backend family to target. Default: {DEFAULT_BACKEND_FAMILY}")

    p_emit = subparsers.add_parser("emit-contract", help="Emit the backend contract for the selected backend family.")
    add_common_arguments(p_emit)
    p_emit.add_argument("--backend-family", default=DEFAULT_BACKEND_FAMILY, help=f"Backend family to target. Default: {DEFAULT_BACKEND_FAMILY}")

    p_run = subparsers.add_parser("run", help="Run the full end-to-end demonstration pipeline.")
    add_common_arguments(p_run)
    p_run.add_argument("--backend-family", default=DEFAULT_BACKEND_FAMILY, help=f"Backend family to target. Default: {DEFAULT_BACKEND_FAMILY}")
    p_run.add_argument(
        "--inputs",
        default='{"a": 1.5, "b": 2.5}',
        help='External input JSON object. For Example 01 use {"a": 2.0, "b": 3.0}. For Example 02 use {"ctrl_a": 2.0, "ctrl_b": 3.0}. For Example 03 use {"status": "Ready"}. For Example 04 use {"x": 2.0}.',
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

        dump_json(artifact, getattr(args, "out", None))
        return 0
    except FrogPipelineError as exc:
        dump_json(exc.as_dict(), getattr(args, "out", None))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
