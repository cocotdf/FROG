<h1>Reference Runtime (Python)</h1>

<p>Python realization of the published <code>reference_host_runtime_ui_binding</code> family.</p>

<p>
  Repository governance and publication state are centralized in
  <a href="../../../../Versioning/Readme.md"><code>Versioning/Readme.md</code></a>.
</p>

<hr/>

<h2>Directory navigation</h2>

<pre><code>Implementations/Reference/Runtime/python/
├── Readme.md
├── __init__.py
├── cli.py
├── execute_contract.py
├── run_slice05_ui.py
├── runtime_core.py
├── ui_runtime.py
└── tests/
    ├── test_slice05_contract.py
    └── test_slice05_ui_runtime.py</code></pre>

<p>
Generated cache directories may appear next to these files in the published tree.
They are not part of the intended source surface of this runtime.
</p>

<h2>Role</h2>

<p>
This directory contains the Python consumer for the published Example 05 runtime corridor.
It accepts the emitted backend contract, loads the published <code>.wfrog</code> package,
resolves the referenced SVG assets, executes the bounded kernel, and can expose the panel through a minimal browser-host UI.
</p>

<p>
This directory is downstream from:
</p>

<pre><code>main.frog
  -&gt; main.fir.json
  -&gt; main.lowering.json
  -&gt; reference_host_runtime_ui_binding contract</code></pre>

<p>
It is not a source parser, not a lowering stage, and not a language-definition layer.
</p>

<h2>Current published entry points</h2>

<h3><code>cli.py</code></h3>

<p>
The main entry point for this directory.
It exposes two modes:
</p>

<ul>
  <li><code>run</code> — headless contract + <code>.wfrog</code> execution.</li>
  <li><code>ui</code> — browser-host UI service for the same runtime core.</li>
</ul>

<p>Examples from the repository root:</p>

<pre><code>python -m Implementations.Reference.Runtime.python.cli run 3
python -m Implementations.Reference.Runtime.python.cli ui
python -m Implementations.Reference.Runtime.python.cli ui --host 127.0.0.1 --port 8080 --no-open-browser</code></pre>

<h3><code>run_slice05_ui.py</code></h3>

<p>
Convenience wrapper that starts the same browser-host UI path as <code>cli.py ui</code>.
It is still useful as a small example-specific launcher, but <code>cli.py</code> is the primary surface.
</p>

<h3><code>execute_contract.py</code> and <code>runtime_core.py</code></h3>

<p>
These files hold the actual execution path.
The current runtime core validates the bounded Example 05 contract and package shape, then produces a runtime result artifact.
</p>

<h3><code>ui_runtime.py</code></h3>

<p>
Browser-host realization for the same runtime core.
The published tests exercise HTML rendering and the JSON snapshot endpoint.
</p>

<h2>Current bounded surface</h2>

<p>
The Python runtime is intentionally strict.
The currently published bounded surface is:
</p>

<ul>
  <li>backend family <code>reference_host_runtime_ui_binding</code>,</li>
  <li>one contract unit named <code>main</code>,</li>
  <li>one public input <code>input_value : u16</code>,</li>
  <li>one public output <code>result : u16</code>,</li>
  <li>one explicit state carrier based on <code>frog.core.delay</code>,</li>
  <li>exactly five loop iterations,</li>
  <li>two widget classes: <code>frog.widgets.numeric_control</code> and <code>frog.widgets.numeric_indicator</code>,</li>
  <li>five supported widget properties: <code>value</code>, <code>label</code>, <code>visible</code>, <code>enabled</code>, and <code>foreground_color</code>,</li>
  <li>two bounded method accepts: <code>ctrl_input.focus</code> and <code>ind_result.reset_to_default_style</code>.</li>
</ul>

<p>
The Python runtime validates the published host binding for
<code>window</code>, <code>basic_widget_rendering</code>, <code>property_write</code>, and <code>widget_value_binding</code>.
Widget-reference member support is then validated from the contract unit itself through <code>widget_reference_support</code> and <code>property_writes</code>.
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
  <li>A headless runtime result artifact with public output publication and UI snapshot data.</li>
  <li>A browser-host page that renders both widgets and serves a runtime snapshot endpoint.</li>
</ul>

<p>
The browser-host UI is intentionally minimal.
It is a proof that the published contract and the published package are sufficient to realize the first host-facing slice.
It is not a claim of native desktop UI closure.
</p>

<h2>Tests</h2>

<p>From the repository root:</p>

<pre><code>python -m unittest \
  Implementations.Reference.Runtime.python.tests.test_slice05_contract \
  Implementations.Reference.Runtime.python.tests.test_slice05_ui_runtime</code></pre>

<p>
The published tests currently check:
</p>

<ul>
  <li>headless execution with input <code>3</code> and final result <code>15</code>,</li>
  <li>foreground-color application on both widgets,</li>
  <li>runtime rejection when accumulation leaves the <code>u16</code> domain,</li>
  <li>browser-host HTML rendering with both widget labels and both asset routes,</li>
  <li>JSON snapshot publication through the HTTP runtime host.</li>
</ul>

<h2>Relationship to the parent runtime directory</h2>

<p>
This directory is one language-specific realization of the family described in
<a href="../Readme.md"><code>Implementations/Reference/Runtime/Readme.md</code></a>.
It should remain aligned with the Rust and C/C++ consumers on:
</p>

<ul>
  <li>accepted contract shape,</li>
  <li>accepted <code>.wfrog</code> package shape,</li>
  <li>execution result meaning,</li>
  <li>minimal widget and property surface,</li>
  <li>browser-host UI obligations for Example 05.</li>
</ul>

<h2>Non-goals</h2>

<ul>
  <li>General-purpose runtime support for arbitrary lowered artifacts.</li>
  <li>Authority over widget-class semantics.</li>
  <li>Compiler-family behavior or LLVM lowering.</li>
  <li>Native compiled UI closure.</li>
</ul>

<h2>Summary</h2>

<p>
Read this directory as the easiest no-build realization of the published runtime family:
</p>

<pre><code>contract + .wfrog + SVG assets
=&gt; Python runtime core
=&gt; headless result or browser-host UI</code></pre>
