from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from .execute_contract import execute_contract
    from .runtime_core import default_contract_path, default_wfrog_path
    from .ui_runtime import build_runtime
except ImportError:  # pragma: no cover
    from execute_contract import execute_contract
    from runtime_core import default_contract_path, default_wfrog_path
    from ui_runtime import build_runtime


def main() -> int:
    parser = argparse.ArgumentParser(description="Python reference runtime family for Example 05.")
    subparsers = parser.add_subparsers(dest="command", required=False)

    run_parser = subparsers.add_parser("run", help="Execute the runtime in headless mode.")
    run_parser.add_argument("input_value", nargs="?", type=int, default=3)
    run_parser.add_argument("--contract", type=Path, default=default_contract_path())
    run_parser.add_argument("--wfrog", type=Path, default=default_wfrog_path())

    ui_parser = subparsers.add_parser("ui", help="Serve the browser-based UI host.")
    ui_parser.add_argument("--contract", type=Path, default=default_contract_path())
    ui_parser.add_argument("--wfrog", type=Path, default=default_wfrog_path())
    ui_parser.add_argument("--host", type=str, default="127.0.0.1")
    ui_parser.add_argument("--port", type=int, default=0)
    ui_parser.add_argument("--no-open-browser", action="store_true")

    args = parser.parse_args()

    if args.command in {None, "run"}:
        artifact = execute_contract(
            getattr(args, "input_value", 3),
            contract_path=getattr(args, "contract", default_contract_path()),
            wfrog_path=getattr(args, "wfrog", default_wfrog_path()),
        )
        print(json.dumps(artifact, indent=2))
        return 0

    runtime = build_runtime(
        contract_path=args.contract,
        wfrog_path=args.wfrog,
        host=args.host,
        port=args.port,
        open_browser=not args.no_open_browser,
    )
    runtime.serve()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
