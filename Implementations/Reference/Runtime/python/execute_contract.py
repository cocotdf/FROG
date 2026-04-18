from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from Implementations.Reference.common import BackendContract
from Implementations.Reference.Runtime.python.runtime_core import build_runtime_core


DEFAULT_CONTRACT_PATH = (
    Path(__file__).resolve().parents[2]
    / "ContractEmitter"
    / "examples"
    / "05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json"
)


def load_contract(path: str | Path = DEFAULT_CONTRACT_PATH) -> BackendContract:
    contract_path = Path(path).resolve()
    artifact = json.loads(contract_path.read_text(encoding="utf-8"))
    return BackendContract(artifact=artifact)


def execute_contract(control_value: int = 3, path: str | Path = DEFAULT_CONTRACT_PATH) -> Dict[str, Any]:
    runtime = build_runtime_core()
    contract = load_contract(path)
    return runtime.execute(contract, {"input_value": control_value}).artifact
