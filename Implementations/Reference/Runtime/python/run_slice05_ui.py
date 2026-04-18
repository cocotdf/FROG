from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from .ui_runtime import build_runtime
except ImportError:  # pragma: no cover - direct script execution
    from ui_runtime import build_runtime


def resolve_example_wfrog_path() -> Path:
    current_file = Path(__file__).resolve()
    repo_root = current_file.parents[4]
    return repo_root / "Examples" / "05_bounded_ui_accumulator" / "ui" / "accumulator_panel.wfrog"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run Example 05 with the bounded Python UI runtime."
    )
    parser.add_argument(
        "input_value",
        nargs="?",
        type=int,
        default=None,
        help="Optional initial value for ctrl_input.",
    )
    parser.add_argument(
        "--autorun",
        action="store_true",
        help="Execute the bounded accumulator immediately after the window is built.",
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Load the published .wfrog package without creating a visible Tk window.",
    )
    parser.add_argument(
        "--dump-state",
        action="store_true",
        help="Print the final runtime state as JSON instead of entering the UI loop.",
    )
    args = parser.parse_args()

    wfrog_path = resolve_example_wfrog_path()
    runtime = build_runtime(wfrog_path, headless=args.headless)

    if args.input_value is not None:
        runtime.property_write("ctrl_input", "value", args.input_value)

    result = None
    if args.autorun:
        result = runtime.run_example_05()

    if args.headless or args.dump_state:
        payload = {
            "status": "ok",
            "result": result,
            "ui": runtime.snapshot(),
        }
        print(json.dumps(payload, indent=2))
        return

    runtime.mainloop()


if __name__ == "__main__":
    main()
