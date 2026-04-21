<h1>Reference Runtime</h1>

<p>Runtime-family consumers for the non-normative FROG reference implementation.</p>

<p>
  Repository governance and publication state are centralized in
  <a href="../../../Versioning/Readme.md"><code>Versioning/Readme.md</code></a>.
</p>

<hr/>

<h2>Directory navigation</h2>

<pre><code>Implementations/Reference/Runtime/
├── Readme.md
├── accept_contract_and_execute.md
├── reference_runtime.py
├── responsibilities.md
├── run_slice05_contract.py
├── python/
│   ├── Readme.md
│   ├── __init__.py
│   ├── cli.py
│   ├── execute_contract.py
│   ├── run_slice05_ui.py
│   ├── runtime_core.py
│   ├── ui_runtime.py
│   └── tests/
├── rust/
│   ├── Readme.md
│   ├── Cargo.toml
│   ├── src/
│   └── tests/
└── cpp/
    ├── Readme.md
    ├── CMakeLists.txt
    ├── include/
    ├── src/
    └── tests/</code></pre>

<p>
Generated cache and build directories may appear in the published tree. They are not part of the intended runtime-family source surface.
</p>

<h2>Overview</h2>

<p>
This directory contains runtime-family consumers of backend contracts for the published reference corridor.
It starts <strong>after</strong> canonical source acceptance, FIR derivation, lowering, and backend-contract emission.
Its job is to consume a published backend-family contract and a published front-panel package, then realize execution privately without redefining FROG semantics.
</p>

<p>
The first active runtime family is <code>reference_host_runtime_ui_binding</code>.
The current reference slice for that family is
<a href="../../../Examples/05_bounded_ui_accumulator/Readme.md"><code>Examples/05_bounded_ui_accumulator/</code></a>.
</p>

<h2>Current published execution corridor</h2>

<pre><code>main.frog
  -&gt; main.fir.json
  -&gt; main.lowering.json
  -&gt; backend-family contract
  -&gt; runtime-family consumer
  -&gt; .wfrog package + SVG assets
  -&gt; browser-host UI and runtime result</code></pre>

<p>
For the current published slice, the runtime-family handoff is the contract artifact emitted under
<a href="../ContractEmitter/Readme.md"><code>Implementations/Reference/ContractEmitter/</code></a>,
and the front-panel package is the published <code>.wfrog</code> package inside Example 05.
</p>

<h2>What this directory consumes</h2>

<ul>
  <li>A backend contract for <code>reference_host_runtime_ui_binding</code>.</li>
  <li>A published <code>.wfrog</code> front-panel package.</li>
  <li>The SVG assets referenced by that package.</li>
</ul>

<p>
The intended common input shape for the current runtime-family slice is therefore:
</p>

<pre><code>contract JSON
+ .wfrog package
+ package-referenced SVG assets</code></pre>

<p>
The runtime family does not need <code>main.frog</code> to execute after the contract has been emitted.
It also does not need <code>front_panel.objects.json</code> as a required input.
That file is a derived host projection for the example corridor, not the semantic or contractual authority.
</p>

<h2>What this directory produces</h2>

<ul>
  <li>A headless execution result artifact for the bounded Example 05 slice.</li>
  <li>A minimal browser-host UI that renders the panel, widgets, labels, values, and SVG assets.</li>
  <li>A runtime snapshot surface exposed by the browser host.</li>
</ul>

<p>
Across the language-specific realizations, the output model is intentionally narrow:
one numeric control, one numeric indicator, one bounded loop of five iterations, one explicit state carrier,
one public output publication, and bounded widget reference writes for <code>foreground_color</code>.
</p>

<h2>Language-specific realizations</h2>

<p>
This parent directory coordinates three parallel realizations of the same family:
</p>

<ul>
  <li><a href="python/Readme.md"><code>python/</code></a> — no-build path with headless execution, browser-host UI, and Python tests.</li>
  <li><a href="rust/Readme.md"><code>rust/</code></a> — Cargo-based path with headless execution, browser-host UI, and Rust tests.</li>
  <li><a href="cpp/Readme.md"><code>cpp/</code></a> — CMake-based path with headless execution, browser-host UI, and C/C++ tests.</li>
</ul>

<p>
The parent-level files <code>reference_runtime.py</code> and <code>run_slice05_contract.py</code> remain useful compatibility and demonstration helpers,
but the main runtime-family closure now lives in the three language-specific directories.
</p>

<h2>Published acceptance surface for Example 05</h2>

<p>From the repository root:</p>

<pre><code># Python
python -m Implementations.Reference.Runtime.python.cli run 3
python -m Implementations.Reference.Runtime.python.cli ui

# Rust
cd Implementations/Reference/Runtime/rust
cargo test
cargo run -- 3
cargo run -- ui

# C/C++
cmake -S Implementations/Reference/Runtime/cpp -B build/frog_runtime_cpp
cmake --build build/frog_runtime_cpp
ctest --test-dir build/frog_runtime_cpp
build/frog_runtime_cpp/frog_reference_runtime_cpp 3
build/frog_runtime_cpp/frog_reference_runtime_cpp ui</code></pre>

<p>
All three language paths are expected to consume the same published contract and the same published <code>.wfrog</code> package.
The UI mode is intentionally a browser-host proof path, not a claim of native compiled UI closure.
</p>

<h2>Ownership boundary</h2>

<ul>
  <li>This directory <strong>owns</strong> runtime-family consumption, host realization, and narrow execution proof for the reference slice.</li>
  <li>This directory does <strong>not own</strong> canonical source syntax, language semantics, FIR definition, lowering definition, widget-class law, or compiler-family design.</li>
</ul>

<p>
The runtime is downstream from the language and downstream from the execution-facing artifacts.
It must follow the contract and package that it consumes.
It must not redefine FROG.
</p>

<h2>Current closure and current limits</h2>

<p>
For Example 05, the repository now publishes browser-host runtime entry points in Python, Rust, and C/C++.
That closes the first common runtime-family shape much more clearly than an execution-only or test-only posture.
</p>

<p>
The runtime-family corridor is still intentionally bounded.
It does not yet claim:
</p>

<ul>
  <li>general widget coverage beyond the current Example 05 slice,</li>
  <li>general runtime acceptance for arbitrary lowered units,</li>
  <li>compiled native UI closure through LLVM,</li>
  <li>authority over widget semantics or compiler-family contracts.</li>
</ul>

<p>
LLVM remains a downstream compiler-family corridor and should be read separately from the runtime-family boundary documented here.
</p>

<h2>Summary</h2>

<p>
Read this directory as the coordination point for one published runtime family, one shared handoff model,
and three parallel language-specific consumers.
For the first executable corridor, the runtime-family contract is:
</p>

<pre><code>published contract
+ published .wfrog package
+ published SVG assets
=&gt; headless execution result and browser-host UI</code></pre>
