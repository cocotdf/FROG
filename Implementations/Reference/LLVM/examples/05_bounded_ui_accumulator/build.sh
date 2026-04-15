#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

clang module.ll -o bounded_ui_accumulator_llvm
./bounded_ui_accumulator_llvm 3
