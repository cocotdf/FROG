<h1>Reference Runtime (C/C++)</h1>

<p>C/C++ realization of the published <code>reference_host_runtime_ui_binding</code> family.</p>

<p>
  Repository governance and publication state are centralized in
  <a href="../../../../Versioning/Readme.md"><code>Versioning/Readme.md</code></a>.
</p>

<hr/>

<h2>Directory navigation</h2>

<pre><code>Implementations/Reference/Runtime/cpp/
├── Readme.md
├── CMakeLists.txt
├── include/
│   ├── contract.hpp
│   ├── execute.hpp
│   ├── json.hpp
│   ├── runtime.hpp
│   └── ui.hpp
├── src/
│   ├── contract.cpp
│   ├── execute.cpp
│   ├── json.cpp
│   ├── main.cpp
│   ├── runtime.cpp
│   └── ui.cpp
└── tests/
    └── test_slice05.cpp</code></pre>

<p>
Generated build directories may appear beside these files in the published tree.
They are not part of the intended source surface of this runtime.
</p>

<h2>Role</h2>

<p>
This directory contains the C/C++ consumer for the published Example 05 runtime corridor.
It accepts the emitted backend contract, loads the published <code>.wfrog</code> package,
resolves the referenced SVG assets, executes the bounded kernel, and can expose the panel through a minimal browser-host UI.
</p>

<p>
The important point is architectural:
this directory is a runtime-family consumer, not a language-definition layer, not a compiler-family layer,
and not a substitute for canonical source, FIR, or lowering.
</p>

<h2>Current published entry points</h2>

<h3><code>src/main.cpp</code></h3>

<p>
The main executable entry point.
It supports:
</p>

<ul>
  <li>headless execution by default or through <code>run</code>,</li>
  <li>browser-host UI through <code>ui</code>.</li>
</ul>

<p>From the repository root:</p>

<pre><code>cmake -S Implementations/Reference/Runtime/cpp -B build/frog_runtime_cpp
cmake --build build/frog_runtime_cpp
ctest --test-dir build/frog_runtime_cpp

build/frog_runtime_cpp/frog_reference_runtime_cpp 3
build/frog_runtime_cpp/frog_reference_runtime_cpp ui
build/frog_runtime_cpp/frog_reference_runtime_cpp ui --host 127.0.0.1 --port 8080 --no-open-browser</code></pre>

<h3><code>src/runtime.cpp</code> and <code>src/execute.cpp</code></h3>

<p>
These files hold the bounded runtime core and the headless execution path.
The current runtime validates the contract family, package shape, widget classes, property writes,
and the Example 05 execution model before producing a runtime result artifact.
</p>

<h3><code>src/ui.cpp</code></h3>

<p>
Browser-host realization for the same runtime core.
The current host serves a minimal HTML page, the referenced SVG assets, and a runtime snapshot surface.
</p>

<h2>Current bounded surface</h2>

<ul>
  <li>backend family <code>reference_host_runtime_ui_binding</code>,</li>
  <li>one contract unit named <code>main</code>,</li>
  <li>one public input <code>input_value : u16</code>,</li>
  <li>one public output <code>result : u16</code>,</li>
  <li>one explicit state carrier based on <code>frog.core.delay</code>,</li>
  <li>exactly five loop iterations,</li>
  <li>two widget classes: <code>frog.widgets.numeric_control</code> and <code>frog.widgets.numeric_indicator</code>,</li>
  <li>five supported widget properties: <code>value</code>, <code>label</code>, <code>visible</code>, <code>enabled</code>, and <code>foreground_color</code>.</li>
</ul>

<p>
The browser-host closure is intentionally narrow.
It exists to prove that the published contract and the published package are enough for a real visible host runtime in C/C++.
It does not claim native compiled UI closure through LLVM.
</p>

<h2>Inputs and outputs</h2>

<h3>Inputs</h3>

<ul>
  <li>The emitted contract artifact under <code>Implementations/Reference/ContractEmitter/examples/</code>.</li>
  <li>The Example 05 package <code>Examples/05_bounded_ui_accumulator/ui/accumulator_panel.wfrog</code>.</li>
  <li>The SVG assets referenced by that package.</li>
</ul>

<h3>Outputs</h3>

<ul>
  <li>A headless runtime result artifact.</li>
  <li>A browser-host page driven by the same runtime core.</li>
</ul>

<h2>Tests</h2>

<p>
The published C/C++ test target checks both the execution result and the HTML rendering path.
After configuring and building, run:
</p>

<pre><code>ctest --test-dir build/frog_runtime_cpp</code></pre>

<p>
The current test target checks:
</p>

<ul>
  <li>headless execution with input <code>3</code> and final result <code>15</code>,</li>
  <li>indicator publication through the runtime artifact,</li>
  <li>browser-host HTML rendering with both SVG asset routes.</li>
</ul>

<h2>Relationship to the other runtime consumers</h2>

<p>
This directory should remain aligned with the Python and Rust consumers on:
</p>

<ul>
  <li>contract acceptance,</li>
  <li>package acceptance,</li>
  <li>execution semantics for Example 05,</li>
  <li>the minimal widget-property surface,</li>
  <li>the browser-host UI shape for the bounded corridor.</li>
</ul>

<p>
The parent runtime-family definition is documented in
<a href="../Readme.md"><code>Implementations/Reference/Runtime/Readme.md</code></a>.
</p>

<h2>Non-goals</h2>

<ul>
  <li>General runtime support for arbitrary contracts.</li>
  <li>Language or widget-law ownership.</li>
  <li>Compiler-family responsibilities.</li>
  <li>Native compiled UI closure.</li>
</ul>

<h2>Summary</h2>

<p>
Read this directory as the C/C++ proof path for the current runtime family:
</p>

<pre><code>contract + .wfrog + SVG assets
=&gt; C/C++ runtime core
=&gt; headless result or browser-host UI</code></pre>
