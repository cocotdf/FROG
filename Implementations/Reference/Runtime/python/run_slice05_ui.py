from __future__ import annotations

import argparse
from pathlib import Path

from ui_runtime import build_runtime


def resolve_example_wfrog_path() -> Path:
    current_file = Path(__file__).resolve()
    repo_root = current_file.parents[4]
    return repo_root / "Examples" / "05_bounded_ui_accumulator" / "ui" / "accumulator_panel.wfrog"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run Example 05 with a concrete Python UI runtime."
    )
    parser.add_argument(
        "input_value",
        nargs="?",
        type=int,
        default=None,
        help="Optional initial value for ctrl_input."
    )
    parser.add_argument(
        "--autorun",
        action="store_true",
        help="Execute the bounded accumulator immediately after the window is built."
    )
    args = parser.parse_args()

    wfrog_path = resolve_example_wfrog_path()
    runtime = build_runtime(wfrog_path)

    if args.input_value is not None:
        runtime.property_write("ctrl_input", "value", args.input_value)

    if args.autorun:
        runtime.run_example_05()

    runtime.mainloop()


if __name__ == "__main__":
    main()
