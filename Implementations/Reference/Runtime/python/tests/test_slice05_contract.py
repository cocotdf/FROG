from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5]))

from Implementations.Reference.Runtime.python.execute_contract import execute_contract  # noqa: E402


class Slice05ContractTests(unittest.TestCase):
    def test_contract_execution_matches_expected_result(self) -> None:
        artifact = execute_contract(3)
        self.assertEqual(artifact["status"], "ok")
        self.assertEqual(artifact["execution_summary"]["iterations"], 5)
        self.assertEqual(artifact["execution_summary"]["initial_state"], 0)
        self.assertEqual(artifact["execution_summary"]["final_state"], 15)
        self.assertEqual(artifact["outputs"]["public"]["result"], 15)
        self.assertEqual(artifact["outputs"]["ui"]["ctrl_input"], 3)
        self.assertEqual(artifact["outputs"]["ui"]["ind_result"], 15)

        widgets = {item["widget_id"]: item["runtime"] for item in artifact["ui_runtime"]["widgets"]}
        self.assertEqual(widgets["ctrl_input"]["foreground_color"], "#5B9BD5")
        self.assertEqual(widgets["ind_result"]["foreground_color"], "#70AD47")
        self.assertEqual(widgets["ind_result"]["value"], 15)

    def test_u16_overflow_is_rejected(self) -> None:
        with self.assertRaises(Exception):
            execute_contract(65535)


if __name__ == "__main__":
    unittest.main()
