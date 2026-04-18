from __future__ import annotations

import argparse
import json

from Implementations.Reference.Runtime.python.execute_contract import execute_contract


def main() -> None:
    parser = argparse.ArgumentParser(description="Bounded Python CLI for Example 05.")
    parser.add_argument("input_value", nargs="?", type=int, default=3)
    args = parser.parse_args()

    artifact = execute_contract(args.input_value)
    print(json.dumps(artifact, indent=2))


if __name__ == "__main__":
    main()
