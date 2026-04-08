<p align="center">
  <img src="../../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Reference Runtime (Python)</h1>

<p align="center">
  <strong>Minimal Python consumer for the reference runtime family in the non-normative FROG reference implementation</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-directory-should-exist">2. Why This Directory Should Exist</a></li>
  <li><a href="#directory-shape">3. Directory Shape</a></li>
  <li><a href="#role-of-each-file">4. Role of Each File</a></li>
  <li><a href="#primary-slice-target">5. Primary Slice Target</a></li>
  <li><a href="#relation-with-runtime-boundary">6. Relation to the Runtime Boundary</a></li>
  <li><a href="#what-this-runtime-consumes">7. What This Runtime Consumes</a></li>
  <li><a href="#what-this-runtime-produces">8. What This Runtime Produces</a></li>
  <li><a href="#published-pipe">9. Published Pipe for Example 05</a></li>
  <li><a href="#design-rules">10. Design Rules</a></li>
  <li><a href="#relationship-with-rust-and-cpp">11. Relationship with Rust and C/C++ Consumers</a></li>
  <li><a href="#closure-status">12. Python Closure Status</a></li>
  <li><a href="#future-growth">13. Future Growth</a></li>
  <li><a href="#summary">14. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the minimal Python realization of the published reference runtime boundary for the FROG reference implementation.
It is a downstream runtime consumer.
It exists to demonstrate the clearest direct execution posture for bounded published example corridors.
</p>

<hr/>

<h2 id="why-this-directory-should-exist">2. Why This Directory Should Exist</h2>

<p>
The parent runtime directory already exposes Python execution material, but a dedicated <code>python/</code> documentation surface is useful because the long-term target is not “one runtime with incidental Python code”.
The long-term target is “one runtime family with several language realizations consuming the same canonical corridor”.
</p>

<p>
This directory therefore exists to make the Python side explicit and symmetric with:
</p>

<ul>
  <li><code>Runtime/rust/</code>,</li>
  <li><code>Runtime/cpp/</code>,</li>
  <li>and later any other runtime-language consumer.</li>
</ul>

<hr/>

<h2 id="directory-shape">3. Directory Shape</h2>

<pre><code>Implementations/Reference/Runtime/python/
├── Readme.md
├── runtime_core.py
├── execute_contract.py
├── cli.py
└── tests/
    └── test_slice05_execution.py
</code></pre>

<p>
The current published subset may still live partly at the parent runtime level.
The tree above is the intended useful shape for making Python-side responsibilities explicit.
</p>

<hr/>

<h2 id="role-of-each-file">4. Role of Each File</h2>

<ul>
  <li><code>Readme.md</code><br/>
      Explains the Python-side runtime posture and the role of this directory.</li>
  <li><code>runtime_core.py</code><br/>
      Python runtime core for contract loading, state handling, and bounded execution.</li>
  <li><code>execute_contract.py</code><br/>
      Python-side contract execution helpers for accepted backend contracts.</li>
  <li><code>cli.py</code><br/>
      Command-line entry surface for example execution.</li>
  <li><code>tests/test_slice05_execution.py</code><br/>
      Python-side behavioral verification for the example-05 corridor.</li>
</ul>

<p>
At the current published state, some of these responsibilities are still carried by parent-level files such as:
</p>

<ul>
  <li><code>Runtime/reference_runtime.py</code>,</li>
  <li><code>Runtime/run_slice05_contract.py</code>.</li>
</ul>

<hr/>

<h2 id="primary-slice-target">5. Primary Slice Target</h2>

<p>
The first target for this runtime is the published example:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/</code></pre>

<p>
That example already establishes a bounded executable corridor with:
</p>

<ul>
  <li>one numeric front-panel control,</li>
  <li>one numeric front-panel indicator,</li>
  <li>one bounded loop of exactly five iterations,</li>
  <li>one explicit local-memory path,</li>
  <li>one final public output,</li>
  <li>and a minimal object-style UI write surface through <code>frog.ui.property_write</code>.</li>
</ul>

<hr/>

<h2 id="relation-with-runtime-boundary">6. Relation to the Runtime Boundary</h2>

<p>
The published runtime family is:
</p>

<pre><code>reference_host_runtime_ui_binding
</code></pre>

<p>
This Python runtime is one consumer of that family posture.
It follows the same runtime-side assumptions as the parallel Rust and future C/C++ consumers.
</p>

<hr/>

<h2 id="what-this-runtime-consumes">7. What This Runtime Consumes</h2>

<p>
This Python runtime starts after source loading, structural validation, semantic validation, FIR-target derivation, and lowering have already produced an acceptable backend contract.
</p>

<p>
For the first bounded published slice, it consumes:
</p>

<ul>
  <li>one backend contract artifact from the reference contract emitter,</li>
  <li>one declared backend family equal to <code>reference_host_runtime_ui_binding</code>,</li>
  <li>one explicit bounded loop model,</li>
  <li>one explicit delay-backed state carrier,</li>
  <li>one control-input binding,</li>
  <li>one indicator/public-output publication rule,</li>
  <li>and one minimal <code>face_color</code> property-write surface.</li>
</ul>

<hr/>

<h2 id="what-this-runtime-produces">8. What This Runtime Produces</h2>

<p>
For the current bounded corridor, the Python consumer produces runtime-visible evidence that:
</p>

<ul>
  <li>the contract was accepted,</li>
  <li>the loop ran exactly five iterations,</li>
  <li>the state started at zero,</li>
  <li>the final state for input <code>3</code> is <code>15</code>,</li>
  <li>the public output is correct,</li>
  <li>the indicator value is correct,</li>
  <li>and the minimal UI runtime state is preserved for the supported widgets.</li>
</ul>

<hr/>

<h2 id="published-pipe">9. Published Pipe for Example 05</h2>

<p>
At the current published state, the Python pipe for the first serious example is:
</p>

<pre><code>python -m Implementations.Reference.Runtime.run_slice05_contract 3
</code></pre>

<p>
Equivalent direct script-style invocation:
</p>

<pre><code>python Implementations/Reference/Runtime/run_slice05_contract.py 3
</code></pre>

<p>
This is currently the clearest direct execution path in the reference runtime family.
</p>

<hr/>

<h2 id="design-rules">10. Design Rules</h2>

<ul>
  <li>Accept or reject contracts explicitly.</li>
  <li>Do not silently reinterpret undeclared assumptions.</li>
  <li>Keep explicit local-memory meaning visible in runtime execution.</li>
  <li>Keep loop iteration count explicit where the contract declares it.</li>
  <li>Keep runtime-private helper structures downstream from the published backend contract.</li>
  <li>Reject unsupported widget-reference or property-write operations explicitly.</li>
  <li>Do not let Python implementation convenience become semantic law.</li>
</ul>

<hr/>

<h2 id="relationship-with-rust-and-cpp">11. Relationship with Rust and C/C++ Consumers</h2>

<p>
The Python runtime is not “the FROG runtime”.
It is one runtime-language realization of the same runtime family.
It must remain aligned with:
</p>

<ul>
  <li>the Rust consumer,</li>
  <li>the future C/C++ consumer,</li>
  <li>and the same canonical example corridor.</li>
</ul>

<hr/>

<h2 id="closure-status">12. Python Closure Status</h2>

<table>
  <thead>
    <tr>
      <th>Python-side surface</th>
      <th>Status</th>
      <th>Posture</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contract loading</td>
      <td>Closed</td>
      <td>Published contract artifact is consumed successfully.</td>
    </tr>
    <tr>
      <td>Direct example runner</td>
      <td>Closed</td>
      <td>A direct command exists for example 05.</td>
    </tr>
    <tr>
      <td>Parity with Rust</td>
      <td>Partial-to-closed</td>
      <td>Both consume the same contract, but structure symmetry is still incomplete.</td>
    </tr>
    <tr>
      <td>Parity with C/C++</td>
      <td>Missing</td>
      <td>No C/C++ peer consumer is published yet.</td>
    </tr>
    <tr>
      <td>Rendered UI host</td>
      <td>Missing</td>
      <td>Runtime-visible UI state exists, but no rendered Python host UI is published yet.</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="future-growth">13. Future Growth</h2>

<ol>
  <li>factor parent-level Python files into an explicit <code>python/</code> directory structure,</li>
  <li>add Python-side tests that mirror runtime parity expectations,</li>
  <li>align Python, Rust, and future C/C++ pipes around the same example-local artifact set,</li>
  <li>and integrate with peripheral UI object realization and optional rendered host work.</li>
</ol>

<hr/>

<h2 id="summary">14. Summary</h2>

<p>
This directory makes the Python runtime posture explicit as one consumer of the reference runtime family.
Its role is to provide the clearest direct execution corridor while remaining only one downstream realization of the same published contract family.
</p>
