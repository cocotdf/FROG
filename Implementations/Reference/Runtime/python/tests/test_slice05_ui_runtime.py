from __future__ import annotations

import json
import sys
import unittest
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5]))

from Implementations.Reference.Runtime.python.ui_runtime import build_runtime  # noqa: E402


class Slice05UiRuntimeTests(unittest.TestCase):
    def test_rendered_page_contains_widgets(self) -> None:
        runtime = build_runtime(open_browser=False)
        html = runtime.render_html()
        self.assertIn("Input", html)
        self.assertIn("Accumulated result", html)
        self.assertIn("/asset/numeric_control_svg", html)
        self.assertIn("/asset/numeric_indicator_svg", html)

    def test_http_state_json_reflects_execution(self) -> None:
        runtime = build_runtime(open_browser=False)
        server, thread = runtime.serve_in_thread()
        try:
            runtime.runtime.execute(control_value=3)
            url = f"http://{server.server_address[0]}:{server.server_address[1]}/state.json"
            with urllib.request.urlopen(url) as response:
                payload = json.loads(response.read().decode("utf-8"))
            self.assertEqual(payload["outputs"]["public"]["result"], 15)
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2.0)


if __name__ == "__main__":
    unittest.main()
