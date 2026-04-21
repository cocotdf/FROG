from __future__ import annotations

import argparse
from pathlib import Path

from .emit_backend_contract import emit_contract_to_path, ContractEmissionError


def find_repo_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "Examples").is_dir() and (candidate / "Implementations").is_dir():
            return candidate
    raise ContractEmissionError("Unable to locate repository root from current path.")


def default_paths() -> tuple[Path, Path]:
    repo_root = find_repo_root(Path(__file__).resolve())
    lowering = repo_root / "Examples" / "05_bounded_ui_accumulator" / "main.lowering.json"
    output = (
        repo_root
        / "Implementations"
        / "Reference"
        / "ContractEmitter"
        / "examples"
        / "05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json"
    )
    return lowering, output


def main() -> int:
    default_lowering, default_output = default_paths()
    parser = argparse.ArgumentParser(
        description="Emit the reference_host_runtime_ui_binding contract for Example 05 from the published lowering artifact."
    )
    parser.add_argument("--lowering", type=Path, default=default_lowering)
    parser.add_argument("--output", type=Path, default=default_output)
    parser.add_argument("--ui-package-path", type=str, default=None)
    args = parser.parse_args()

    emit_contract_to_path(args.lowering, args.output, ui_package_path=args.ui_package_path)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
