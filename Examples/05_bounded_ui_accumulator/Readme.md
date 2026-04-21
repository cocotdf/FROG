<h1>Example 05 — Bounded UI Accumulator</h1>

<p>
Canonical bounded corridor from <code>.frog</code> source to front-panel package, FIR, lowering,
runtime-family consumption, and a separate narrow LLVM proof path.
</p>

<p>
  Repository governance and publication state are centralized in
  <a href="../../Versioning/Readme.md"><code>Versioning/Readme.md</code></a>.
</p>

<hr/>

<h2>Directory navigation</h2>

<pre><code>Examples/05_bounded_ui_accumulator/
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
        └── numeric_indicator.svg</code></pre>

<h2>Purpose</h2>

<p>
This directory is the current reference slice for the first executable corridor that includes:
</p>

<ul>
  <li>canonical source-owned program meaning,</li>
  <li>a published minimal front-panel package,</li>
  <li>execution-facing artifacts,</li>
  <li>a backend-family contract,</li>
  <li>runtime-family consumption with a real visible UI,</li>
  <li>a separate downstream compiler-family proof path.</li>
</ul>

<p>
The current example is intentionally narrow:
one numeric control, one numeric indicator, one explicit <code>u16</code> state,
one bounded loop of exactly five iterations, one public output, and bounded widget-reference property writes for <code>foreground_color</code>.
</p>

<h2>Published corridor</h2>

<pre><code>main.frog
  -&gt; ui/accumulator_panel.wfrog + ui/assets/*.svg
  -&gt; main.fir.json
  -&gt; main.lowering.json
  -&gt; reference_host_runtime_ui_binding contract
  -&gt; Python / Rust / C/C++ browser-host runtimes
  -&gt; separate narrow LLVM proof path</code></pre>

<h2>What each published artifact owns</h2>

<h3><code>main.frog</code></h3>

<p>
The canonical source of the example.
It owns the program meaning, the public interface, the diagram,
the participation of <code>widget_value</code>, the availability of <code>widget_reference</code>,
and the two <code>frog.ui.property_write</code> operations that target <code>foreground_color</code>.
</p>

<h3><code>main.fir.json</code></h3>

<p>
The execution-facing IR artifact for the same slice.
It remains downstream from the canonical source.
</p>

<h3><code>main.lowering.json</code></h3>

<p>
The bounded lowering artifact that makes the runtime-family and compiler-family handoff visible.
For this example it preserves:
</p>

<ul>
  <li>one public input <code>input_value : u16</code>,</li>
  <li>one public output <code>result : u16</code>,</li>
  <li>one control binding to <code>ctrl_input</code>,</li>
  <li>one indicator binding to <code>ind_result</code>,</li>
  <li>two reference writes to <code>foreground_color</code>,</li>
  <li>one explicit bounded kernel with exactly five iterations.</li>
</ul>

<h3><code>ui/accumulator_panel.wfrog</code> and <code>ui/assets/</code></h3>

<p>
The published front-panel package and its SVG realization assets.
These files define the package-level widget realization surface for this example:
panel metadata, widget class references, default props, layout, assets, and host-binding metadata.
They do not redefine program meaning.
</p>

<h3><code>front_panel.objects.json</code></h3>

<p>
A derived host projection for the same slice.
This file is useful as a concrete host-facing realization view, but it is not the required runtime-family input,
and it is not the semantic or contractual authority.
</p>

<h2>Runtime-family handoff</h2>

<p>
The runtime-family contract for this example is emitted under:
</p>

<pre><code>Implementations/Reference/ContractEmitter/examples/
└── 05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json</code></pre>

<p>
That contract is downstream from <code>main.frog</code>, <code>main.fir.json</code>, <code>main.lowering.json</code>,
and <code>ui/accumulator_panel.wfrog</code>.
It is the handoff surface consumed by the runtime-family directories under
<a href="../../Implementations/Reference/Runtime/Readme.md"><code>Implementations/Reference/Runtime/</code></a>.
</p>

<h2>Current runtime closure</h2>

<p>
For the runtime-family slice, Example 05 now has three published browser-host realizations:
</p>

<ul>
  <li><a href="../../Implementations/Reference/Runtime/python/Readme.md">Python</a>,</li>
  <li><a href="../../Implementations/Reference/Runtime/rust/Readme.md">Rust</a>,</li>
  <li><a href="../../Implementations/Reference/Runtime/cpp/Readme.md">C/C++</a>.</li>
</ul>

<p>
All three are expected to consume the same emitted contract and the same published <code>.wfrog</code> package.
The UI closure for this slice is therefore:
</p>

<pre><code>contract + .wfrog + SVG assets
=&gt; headless runtime result
and
=&gt; browser-host panel with real widgets</code></pre>

<h2>Published runtime commands</h2>

<p>Representative commands from the repository root:</p>

<pre><code># Python
python -m Implementations.Reference.Runtime.python.cli run 3
python -m Implementations.Reference.Runtime.python.cli ui

# Rust
cd Implementations/Reference/Runtime/rust
cargo run -- 3
cargo run -- ui

# C/C++
cmake -S Implementations/Reference/Runtime/cpp -B build/frog_runtime_cpp
cmake --build build/frog_runtime_cpp
build/frog_runtime_cpp/frog_reference_runtime_cpp 3
build/frog_runtime_cpp/frog_reference_runtime_cpp ui</code></pre>

<h2>LLVM note</h2>

<p>
This example also remains the anchor for a first LLVM-oriented proof path.
That compiler-family path is downstream and separate from the runtime-family closure.
It should not be read as a compiled native UI closure.
</p>

<p>
The current split is therefore:
</p>

<pre><code>runtime family
  =&gt; browser-host UI and runtime result

compiler family
  =&gt; narrow native execution proof path</code></pre>

<h2>Current remaining gaps</h2>

<p>
This example closes the first visible runtime-family UI slice, but three edges remain intentionally open:
</p>

<ul>
  <li>The published <code>.wfrog</code> host binding still needs explicit convergence with the contract on widget-reference binding.</li>
  <li>The contract still carries a family-specific overflow wording instead of a single fully normalized corridor-wide rule.</li>
  <li>The LLVM proof path is still separate from host-rendered UI closure.</li>
</ul>

<h2>How to read this example correctly</h2>

<ul>
  <li><code>main.frog</code> owns the source meaning.</li>
  <li><code>ui/accumulator_panel.wfrog</code> owns example-local package publication.</li>
  <li><code>front_panel.objects.json</code> is a downstream host projection.</li>
  <li>The emitted backend contract is the runtime-family handoff artifact.</li>
  <li>The three runtime directories consume the same slice in parallel.</li>
  <li>LLVM is downstream and separate.</li>
</ul>

<h2>Summary</h2>

<p>
This example is the current reference corridor for closing the first real host-facing slice.
It already proves that the published source, package, lowering, contract, and assets are sufficient for a real minimal UI runtime in Python, Rust, and C/C++.
What it does <strong>not</strong> yet prove is compiled native UI closure through LLVM.
</p>
