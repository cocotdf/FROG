# Example 05 — Bounded UI Accumulator

<p>Canonical bounded corridor from <code>.frog</code> source to UI package, FIR, lowering, runtime-family consumption, and first downstream LLVM proof</p>
<p>FROG — Free Open Graphical Language</p>

---

## Navigation

- Examples index: [`../Readme.md`](../Readme.md)
- Example UI package: [`ui/Readme.md`](ui/Readme.md)
- Runtime-family parent: [`../../Implementations/Reference/Runtime/Readme.md`](../../Implementations/Reference/Runtime/Readme.md)
- Python runtime consumer: [`../../Implementations/Reference/Runtime/python/Readme.md`](../../Implementations/Reference/Runtime/python/Readme.md)
- Rust runtime consumer: [`../../Implementations/Reference/Runtime/rust/Readme.md`](../../Implementations/Reference/Runtime/rust/Readme.md)
- C/C++ runtime consumer: [`../../Implementations/Reference/Runtime/cpp/Readme.md`](../../Implementations/Reference/Runtime/cpp/Readme.md)
- Contract handoff family: [`../../Implementations/Reference/ContractEmitter/Readme.md`](../../Implementations/Reference/ContractEmitter/Readme.md)
- LLVM proof corridor: [`../../Implementations/Reference/LLVM/examples/05_bounded_ui_accumulator/Readme.md`](../../Implementations/Reference/LLVM/examples/05_bounded_ui_accumulator/Readme.md)

## Overview

This example is the canonical bounded vertical slice for the current published FROG corridor.

It is the small but serious reference case used to read one connected chain:

```text
main.frog
  -> ui/accumulator_panel.wfrog
  -> main.fir.json
  -> main.lowering.json
  -> backend-family contract
  -> runtime-family consumers
  -> first downstream LLVM proof
```

This example exists to prove corridor integrity, not to model a large application.

## Goal of the example

The goal is to publish one inspectable end-to-end slice that is concrete enough to support:

- canonical source publication,
- front-panel package publication,
- execution-facing publication,
- backend-family runtime handoff,
- host-visible runtime realization,
- downstream compiler-family experimentation.

The example therefore matters as a closure anchor, not as a feature showcase.

## Current published directory shape

```text
Examples/05_bounded_ui_accumulator/
├── Readme.md
├── front_panel.objects.json
├── main.fir.json
├── main.frog
├── main.lowering.json
└── ui/
    ├── Readme.md
    ├── accumulator_panel.wfrog
    └── assets/
        ├── numeric_control.svg
        └── numeric_indicator.svg
```

## Role of each published artifact

### `main.frog`

Canonical source publication of the example. This remains the owner of example meaning.

### `main.fir.json`

Execution-facing FIR publication for the same example corridor.

### `main.lowering.json`

Lowered execution-facing handoff posture used by downstream runtime-family and compiler-family consumers.

### `ui/accumulator_panel.wfrog`

Published front-panel package for the example-local realization layer.

### `ui/assets/numeric_control.svg` and `ui/assets/numeric_indicator.svg`

Minimal SVG realization assets referenced by the published package.

### `front_panel.objects.json`

Derived host-oriented realization material for the same example.

It is useful for host work, inspection, and comparison, but it stays downstream from canonical source, widget contracts, FIR, lowering, and the published `.wfrog` package. It does not redefine executable meaning.

## Observable example meaning

The example meaning is intentionally simple and fully inspectable:

- one numeric control provides the public input value,
- the loop starts from zero,
- the loop runs exactly five iterations,
- each iteration adds the input value to the carried explicit state,
- the final state is published as public output `result`,
- the same final state is written to the numeric indicator,
- the bounded UI object surface includes one `foreground_color` write for the control and one `foreground_color` write for the indicator.

The example is small on purpose. Its value comes from publication clarity, not complexity.

## Downstream runtime-family handoff

This example is paired with the following repository-visible backend contract artifact:

```text
Implementations/Reference/ContractEmitter/examples/
└── 05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json
```

That contract is the current handoff surface for the first named runtime family:

```text
reference_host_runtime_ui_binding
```

The runtime-family reading posture is therefore:

```text
canonical example source
  -> published .wfrog package
  -> FIR
  -> lowering
  -> backend-family contract
  -> runtime-family consumer
```

The LLVM proof corridor is also downstream from this example, but it belongs to a compiler-family path rather than to the runtime-family definition itself.

## Published runtime and compiler posture

For this example, the repository now publishes two different downstream families:

### Runtime-family posture

The runtime-family posture uses the contract artifact together with the `.wfrog` package and its SVG assets.

At the current published code state, the runtime-family corridor is visible in three consumer languages:

- Python headless execution and browser-host UI,
- Rust headless execution and browser-host UI,
- C/C++ headless execution and browser-host UI.

All three remain intentionally narrow. They close the first host-visible runtime slice for this example. They do **not** claim native compiled UI closure.

### Compiler-family posture

The LLVM example remains a separate downstream compiler-family proof path. It shares the same example corridor, but it is not the runtime family.

```text
runtime-family UI closure
  !=
native compiled UI closure
```

## Current repository-visible run surfaces

### Python

Primary language-specific CLI:

```text
python -m Implementations.Reference.Runtime.python.cli run 3
python -m Implementations.Reference.Runtime.python.cli ui
python -m Implementations.Reference.Runtime.python.cli ui --host 127.0.0.1 --port 8080 --no-open-browser
```

Example-specific convenience wrappers:

```text
python -m Implementations.Reference.Runtime.run_slice05_contract 3
python Implementations/Reference/Runtime/python/run_slice05_ui.py
```

### Rust

From `Implementations/Reference/Runtime/rust/`:

```text
cargo test
cargo run -- 3
cargo run -- ui
cargo run -- ui --host 127.0.0.1 --port 8080 --no-open-browser
```

### C/C++

From the repository root:

```text
cmake -S Implementations/Reference/Runtime/cpp -B build/frog_runtime_cpp
cmake --build build/frog_runtime_cpp
ctest --test-dir build/frog_runtime_cpp
build/frog_runtime_cpp/frog_reference_runtime_cpp 3
build/frog_runtime_cpp/frog_reference_runtime_cpp ui
build/frog_runtime_cpp/frog_reference_runtime_cpp ui --host 127.0.0.1 --port 8080 --no-open-browser
```

### LLVM

The LLVM proof corridor stays under the dedicated compiler-family example directory:

```text
Implementations/Reference/LLVM/examples/05_bounded_ui_accumulator/
```

Read that path as a separate downstream proof corridor.

## Boundary

This example is a bounded closure slice, not the whole language.

```text
canonical bounded slice
  !=
full language closure

published browser-host runtime UI
  !=
native compiled UI closure

derived host realization
  !=
semantic authority
```

In particular:

- `main.frog` remains the source-side owner of example meaning,
- `ui/accumulator_panel.wfrog` remains the package-side owner of the published front-panel realization contract,
- `front_panel.objects.json` remains derived host-oriented realization material,
- runtime-family consumers remain downstream from lowering and backend-family handoff,
- the LLVM proof remains downstream and separate from the runtime-family definition.

## Summary

Example 05 is the reference corridor used to close the first serious FROG execution slice.

The correct repository reading posture is now:

```text
one canonical source example
  -> one published .wfrog package
  -> one FIR publication
  -> one lowering publication
  -> one runtime-family handoff contract
  -> several runtime-family consumers
  -> one separate compiler-family proof path
```

That is why this example is the anchor for runtime closure, package closure, and the next wave of widget-definition work.
