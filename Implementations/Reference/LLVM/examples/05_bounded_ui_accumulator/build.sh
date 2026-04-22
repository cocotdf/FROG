#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

clang module.ll -o bounded_ui_accumulator_llvm

OUTPUT="$(./bounded_ui_accumulator_llvm 3)"
printf '%s\n' "$OUTPUT"

EXPECTED=$'final_state=15\npublic_output=15\nstatus=ok'
if [[ "$OUTPUT" != "$EXPECTED" ]]; then
  echo "Unexpected LLVM proof output." >&2
  exit 1
fi
