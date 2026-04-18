from __future__ import annotations

import unittest
from pathlib import Path

from Implementations.Reference.Runtime.python.ui_runtime import build_runtime


class Slice05UiRuntimeTests(unittest.TestCase):
    def test_headless_runtime_consumes_published_wfrog(self) -> None:
        repo_root = Path(__file__).resolve().parents[5]
        wfrog_path = repo_root / "Examples" / "05_bounded_ui_accumulator" / "ui" / "accumulator_panel.wfrog"

        runtime = build_runtime(wfrog_path, headless=True)
        runtime.property_write("ctrl_input", "value", 3)
        result = runtime.run_example_05()

        self.assertEqual(result, 15)
        self.assertEqual(runtime.property_read("ind_result", "value"), 15)
        self.assertEqual(runtime.property_read("ctrl_input", "foreground_color"), "#5B9BD5")
        self.assertEqual(runtime.property_read("ind_result", "foreground_color"), "#70AD47")

        snapshot = runtime.snapshot()
        self.assertEqual(snapshot["panel"]["title"], "Bounded UI Accumulator")
        self.assertEqual(snapshot["widgets"]["ctrl_input"]["properties"]["label"], "Input")
        self.assertEqual(
            snapshot["widgets"]["ind_result"]["properties"]["label"],
            "Accumulated result",
        )


if __name__ == "__main__":
    unittest.main()
