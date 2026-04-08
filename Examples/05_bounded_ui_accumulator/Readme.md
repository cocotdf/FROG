<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Example 05 — Bounded UI Accumulator</h1>

<p align="center">
  <strong>Operational A-to-Z dossier for the first bounded source → contract → runtime vertical slice</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#expected-behavior">2. Expected Behavior</a></li>
  <li><a href="#closure-status">3. Closure Status</a></li>
  <li><a href="#useful-file-tree">4. Useful File Tree</a></li>
  <li><a href="#file-responsibilities">5. File Responsibilities</a></li>
  <li><a href="#shared-corridor">6. Shared Canonical Corridor</a></li>
  <li><a href="#source-posture">7. Canonical Source Posture</a></li>
  <li><a href="#ui-posture">8. Front-Panel and UI Object Posture</a></li>
  <li><a href="#fir-posture">9. FIR / Execution-Facing Posture</a></li>
  <li><a href="#lowering-posture">10. Lowering and Backend-Contract Posture</a></li>
  <li><a href="#python-pipe">11. Python Runtime Pipe</a></li>
  <li><a href="#rust-pipe">12. Rust Runtime Pipe</a></li>
  <li><a href="#cpp-pipe">13. C/C++ Runtime Pipe</a></li>
  <li><a href="#llvm-path">14. LLVM-Oriented Native Path</a></li>
  <li><a href="#observable-parity">15. Observable Parity Across Published Runtimes</a></li>
  <li><a href="#published-gap">16. Published Gaps Still To Close</a></li>
  <li><a href="#summary">17. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This example is the first published applicative vertical slice in the FROG repository that is small, bounded, and already executable through downstream reference consumers.
It combines:
</p>

<ul>
  <li>one canonical <code>.frog</code> source file,</li>
  <li>one bounded counted loop,</li>
  <li>one explicit local-memory path through <code>frog.core.delay</code>,</li>
  <li>one numeric control and one numeric indicator,</li>
  <li>one public output,</li>
  <li>one published backend contract artifact,</li>
  <li>one published Python runtime consumer,</li>
  <li>and one published Rust runtime consumer posture.</li>
</ul>

<p>
Its role is not to prove the full long-term language closure.
Its role is to provide one serious bounded slice where the reader can inspect the canonical source, follow the downstream handoff, and run the same behavioral corridor through more than one runtime language.
</p>

<hr/>

<h2 id="expected-behavior">2. Expected Behavior</h2>

<p>
The behavior of this example is intentionally conservative and explicit:
</p>

<ul>
  <li>the front-panel control <code>ctrl_input</code> provides one <code>u16</code> input value <code>x</code>,</li>
  <li>the explicit state starts at <code>0</code>,</li>
  <li>the loop executes exactly <code>5</code> iterations,</li>
  <li>each iteration computes <code>state_next = state_current + x</code>,</li>
  <li>after the fifth iteration, the final state is published as the program result,</li>
  <li>the indicator <code>ind_result</code> displays that final value,</li>
  <li>the same final value is also published to the public output <code>result</code>,</li>
  <li>and the example also exercises minimal object-style UI property writes for <code>face_color</code>.</li>
</ul>

<p>
For an input value of <code>3</code>, the expected final value is <code>15</code>.
</p>

<pre><code>input  = x
state0 = 0

repeat 5 times:
    state = state + x

result = state
</code></pre>

<p>
This mathematical summary is informative only.
The intended reading remains the explicit loop-and-state execution corridor, not a semantic rewrite into “multiply by five”.
</p>

<hr/>

<h2 id="closure-status">3. Closure Status</h2>

<table>
  <thead>
    <tr>
      <th>Surface</th>
      <th>Status</th>
      <th>Published posture</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Canonical source</td>
      <td>Closed</td>
      <td><code>main.frog</code> is published.</td>
    </tr>
    <tr>
      <td>Source-owned front panel</td>
      <td>Closed</td>
      <td>Two widgets are declared in the canonical source.</td>
    </tr>
    <tr>
      <td>Behavioral model</td>
      <td>Closed</td>
      <td>Bounded counted loop, explicit delay-backed state, final output path.</td>
    </tr>
    <tr>
      <td>Structural / semantic reading</td>
      <td>Closed at example-document level</td>
      <td>The example meaning is clearly attributable in the source and in this dossier.</td>
    </tr>
    <tr>
      <td>FIR-readable corridor</td>
      <td>Partial</td>
      <td>The execution-facing corridor is described, but no example-local FIR artifact is published yet in this directory.</td>
    </tr>
    <tr>
      <td>Lowering posture</td>
      <td>Partial</td>
      <td>The lowering intent is explicit, but the example does not yet publish a separate lowered artifact alongside the source.</td>
    </tr>
    <tr>
      <td>Backend contract</td>
      <td>Closed</td>
      <td>A published contract artifact exists for the reference runtime family.</td>
    </tr>
    <tr>
      <td>Python runtime consumer</td>
      <td>Closed</td>
      <td>A runnable Python entry point is published.</td>
    </tr>
    <tr>
      <td>Python build / run pipe</td>
      <td>Partial</td>
      <td>The runtime entry point exists, but this README now makes the operational pipe explicit.</td>
    </tr>
    <tr>
      <td>Rust runtime consumer</td>
      <td>Partial-to-closed</td>
      <td>A Rust consumer and tests are published; a dedicated example-local run entry point is still missing.</td>
    </tr>
    <tr>
      <td>Rust build / run pipe</td>
      <td>Partial</td>
      <td>Test-based execution proof exists; an explicit example runner binary is not yet published.</td>
    </tr>
    <tr>
      <td>C/C++ runtime consumer</td>
      <td>Missing</td>
      <td>No published C or C++ runtime consumer was found for this example.</td>
    </tr>
    <tr>
      <td>C/C++ build / run pipe</td>
      <td>Missing</td>
      <td>No published pipe was found.</td>
    </tr>
    <tr>
      <td>Peripheral UI object realization file</td>
      <td>Missing as distinct example-local file</td>
      <td>The source publishes widget declarations and face templates, but not yet one distinct downstream peripheral UI object realization file for this example.</td>
    </tr>
    <tr>
      <td>Rendered front panel</td>
      <td>Missing</td>
      <td>Published runtime outputs expose UI state, but no real rendered host UI path is published for this example yet.</td>
    </tr>
    <tr>
      <td>LLVM-oriented native executable path</td>
      <td>Missing</td>
      <td>No example-local LLVM-native corridor is published yet.</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="useful-file-tree">4. Useful File Tree</h2>

<pre><code>Examples/
└── 05_bounded_ui_accumulator/
    ├── Readme.md
    └── main.frog

Implementations/
└── Reference/
    ├── ContractEmitter/
    │   └── examples/
    │       └── 05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json
    └── Runtime/
        ├── Readme.md
        ├── accept_contract_and_execute.md
        ├── reference_runtime.py
        ├── run_slice05_contract.py
        └── rust/
            ├── Cargo.toml
            ├── Readme.md
            └── tests/
                ├── slice05_contract_smoke.rs
                └── slice05_execution.rs
</code></pre>

<hr/>

<h2 id="file-responsibilities">5. File Responsibilities</h2>

<ul>
  <li><code>Examples/05_bounded_ui_accumulator/main.frog</code><br/>
      Canonical source of the example. This is the source of truth for the example-level program meaning.</li>
  <li><code>Examples/05_bounded_ui_accumulator/Readme.md</code><br/>
      Operational example dossier. It explains what the example does, how the corridor is staged, what is already runnable, and what is still missing.</li>
  <li><code>Implementations/Reference/ContractEmitter/examples/05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json</code><br/>
      Published backend-family contract artifact consumed downstream by the reference runtime family.</li>
  <li><code>Implementations/Reference/Runtime/reference_runtime.py</code><br/>
      Python-side reference runtime realization for the bounded reference family.</li>
  <li><code>Implementations/Reference/Runtime/run_slice05_contract.py</code><br/>
      Python demonstration entry point for executing the published contract of this example.</li>
  <li><code>Implementations/Reference/Runtime/accept_contract_and_execute.md</code><br/>
      Non-normative runtime execution sketch and staged execution posture.</li>
  <li><code>Implementations/Reference/Runtime/rust/Cargo.toml</code><br/>
      Rust package manifest for the Rust-side consumer.</li>
  <li><code>Implementations/Reference/Runtime/rust/tests/slice05_contract_smoke.rs</code><br/>
      Rust contract-shape validation test against the published contract artifact.</li>
  <li><code>Implementations/Reference/Runtime/rust/tests/slice05_execution.rs</code><br/>
      Rust execution test showing the published contract produces the expected result for the bounded accumulation behavior.</li>
</ul>

<hr/>

<h2 id="shared-corridor">6. Shared Canonical Corridor</h2>

<p>
The core architectural point of this example is that one canonical corridor is shared across downstream consumers.
The intended reading is:
</p>

<pre><code>canonical .frog source
        |
        v
validated example meaning
        |
        v
execution-facing representation (FIR-target posture)
        |
        v
lowering posture
        |
        v
backend-family contract artifact
        |
        +------------------------------+
        |                              |
        v                              v
Python reference runtime        Rust reference runtime
</code></pre>

<p>
This example must not be read as “Python defines the example” or “Rust defines the example”.
The source and the downstream handoff corridor remain primary.
The runtimes are downstream consumers.
</p>

<hr/>

<h2 id="source-posture">7. Canonical Source Posture</h2>

<p>
The canonical source declares:
</p>

<ul>
  <li>one numeric control widget <code>ctrl_input</code> of value type <code>u16</code>,</li>
  <li>one numeric indicator widget <code>ind_result</code> of value type <code>u16</code>,</li>
  <li>one explicit constant <code>0</code> for initial state,</li>
  <li>one explicit constant <code>5</code> for loop count,</li>
  <li>one explicit <code>for_loop</code> structure,</li>
  <li>one explicit state carrier through <code>frog.core.delay</code>,</li>
  <li>one <code>frog.core.add</code> accumulation step,</li>
  <li>one indicator value path,</li>
  <li>one interface output path,</li>
  <li>and two explicit <code>frog.ui.property_write</code> operations for <code>face_color</code>.</li>
</ul>

<p>
This makes the example semantically attributable at the source level.
The loop is explicit.
The state is explicit.
The UI value participation is explicit.
The UI object-style property-write path is explicit.
</p>

<hr/>

<h2 id="ui-posture">8. Front-Panel and UI Object Posture</h2>

<p>
This example demonstrates two distinct UI interaction surfaces:
</p>

<ul>
  <li><strong>natural value participation</strong> through <code>widget_value</code>,</li>
  <li><strong>object-style interaction</strong> through <code>widget_reference</code> and <code>frog.ui.property_write</code>.</li>
</ul>

<p>
At the current published state, the source owns widget declarations and face-template references.
However, the repository does not yet publish one separate example-local peripheral UI object realization file that would define host-side object realization independently from the canonical source.
That boundary remains future work for this example.
</p>

<p>
Likewise, the published runtime result posture already exposes runtime-side widget state, but this is not yet equivalent to a real rendered front panel.
A true rendered host UI corridor is therefore still open work.
</p>

<hr/>

<h2 id="fir-posture">9. FIR / Execution-Facing Posture</h2>

<p>
The example already has a clear execution-facing reading:
</p>

<ul>
  <li>one bounded executable unit,</li>
  <li>one counted loop,</li>
  <li>one explicit state carrier,</li>
  <li>one deterministic initial value,</li>
  <li>one final result publication path,</li>
  <li>and one bounded UI property-write surface.</li>
</ul>

<p>
However, this example directory does not yet publish one explicit example-local FIR artifact or FIR JSON file.
The FIR reading is therefore architecturally clear but not yet materialized as a repository-visible example-local artifact.
</p>

<hr/>

<h2 id="lowering-posture">10. Lowering and Backend-Contract Posture</h2>

<p>
The example already crosses the most important downstream boundary currently visible in the repository:
</p>

<pre><code>Example source
    ->
backend-family contract artifact
    ->
runtime-family execution
</code></pre>

<p>
The published contract proves that this example is no longer only prose.
It already supports a repository-visible handoff into the family:
</p>

<pre><code>reference_host_runtime_ui_binding
</code></pre>

<p>
What is still missing is a more explicit example-local intermediate lowered artifact and a clearer FIR-to-lowering publication surface for this example itself.
</p>

<hr/>

<h2 id="python-pipe">11. Python Runtime Pipe</h2>

<p>
The published Python pipe is the clearest operational corridor currently available for this example.
</p>

<h3>Inputs</h3>
<ul>
  <li>published backend contract artifact,</li>
  <li>one numeric control value in the <code>u16</code> domain.</li>
</ul>

<h3>Python pipe</h3>

<pre><code>python -m Implementations.Reference.Runtime.run_slice05_contract 3
</code></pre>

<p>
Equivalent direct script-style invocation, depending on local working posture:
</p>

<pre><code>python Implementations/Reference/Runtime/run_slice05_contract.py 3
</code></pre>

<h3>What happens</h3>
<ol>
  <li>the script loads the published contract artifact,</li>
  <li>creates the Python reference runtime for the expected backend family,</li>
  <li>binds <code>input_value = 3</code>,</li>
  <li>applies the declared <code>face_color</code> property writes,</li>
  <li>initializes state to <code>0</code>,</li>
  <li>executes five deterministic accumulation iterations,</li>
  <li>publishes the final value to the public output and the indicator surface,</li>
  <li>prints a runtime-result JSON artifact.</li>
</ol>

<h3>Expected observable result for input 3</h3>

<pre><code>public.result = 15
ui.ctrl_input = 3
ui.ind_result = 15
</code></pre>

<p>
This is the strongest currently published run path for the example.
</p>

<hr/>

<h2 id="rust-pipe">12. Rust Runtime Pipe</h2>

<p>
The published Rust corridor already proves downstream multi-runtime consumption, but it is currently exposed primarily through tests rather than through one example-local runner binary.
</p>

<h3>Rust build / verification pipe</h3>

<pre><code>cd Implementations/Reference/Runtime/rust
cargo test
</code></pre>

<h3>What this currently proves</h3>
<ul>
  <li>the published contract deserializes correctly,</li>
  <li>the expected contract shape is preserved,</li>
  <li>the example executes with the expected bounded accumulation behavior,</li>
  <li>and the final result for input <code>3</code> is <code>15</code>.</li>
</ul>

<h3>Current limitation</h3>
<p>
The Rust side is already a real downstream consumer, but the example does not yet publish one dedicated Rust runner command comparable to the Python entry point.
So the Rust consumer exists, but its example-local operational pipe is still best classified as partial rather than fully closed.
</p>

<hr/>

<h2 id="cpp-pipe">13. C/C++ Runtime Pipe</h2>

<p>
No published C or C++ runtime consumer was found for this example.
Accordingly:
</p>

<ul>
  <li>there is no published C/C++ mini runtime for this example,</li>
  <li>there is no published C/C++ build pipe,</li>
  <li>there is no published C/C++ run pipe,</li>
  <li>and runtime modularity is therefore only partially demonstrated today at the repository level.</li>
</ul>

<p>
Closing this gap is one of the highest-value next steps for the example portfolio.
</p>

<hr/>

<h2 id="llvm-path">14. LLVM-Oriented Native Path</h2>

<p>
This example does not yet publish a closed LLVM-oriented downstream path to a native executable.
In particular, the repository does not yet expose, for this example:
</p>

<ul>
  <li>one explicit FIR-to-lowering bridge artifact,</li>
  <li>one explicit lowering-to-LLVM-family bridge artifact,</li>
  <li>one compiler-facing lowered artifact for this example,</li>
  <li>one native build command,</li>
  <li>one packaged executable result,</li>
  <li>or one rendered native front-panel host path.</li>
</ul>

<p>
Therefore this example is not yet allowed to claim native-executable closure.
</p>

<hr/>

<h2 id="observable-parity">15. Observable Parity Across Published Runtimes</h2>

<p>
At the current published state, the strongest shared parity statement that can be made is:
</p>

<ul>
  <li>the Python path consumes the published contract and produces the expected bounded result,</li>
  <li>the Rust path validates the same contract shape and confirms the same final bounded result through tests,</li>
  <li>and both paths preserve the explicit loop-and-state reading rather than replacing it with a shortcut semantic narrative.</li>
</ul>

<p>
For the canonical example case <code>input = 3</code>, the expected observable equivalence is:
</p>

<table>
  <thead>
    <tr>
      <th>Observable</th>
      <th>Expected value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Loop iteration count</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Initial state</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Final public output</td>
      <td>15</td>
    </tr>
    <tr>
      <td>Indicator value</td>
      <td>15</td>
    </tr>
  </tbody>
</table>

<p>
This is already a meaningful multi-runtime proof point, but it is not yet the full Python/Rust/C/C++ parity target.
</p>

<hr/>

<h2 id="published-gap">16. Published Gaps Still To Close</h2>

<p>
The main remaining gaps for this example are:
</p>

<ol>
  <li>publish one explicit example-local FIR artifact or FIR serialization surface,</li>
  <li>publish one explicit example-local lowered artifact or clearer example-local lowering output,</li>
  <li>publish one distinct peripheral UI object realization file,</li>
  <li>publish one C/C++ mini runtime consumer and its build/run pipe,</li>
  <li>publish one Rust runner entry point comparable to the Python runner,</li>
  <li>publish one real rendered front-panel host path,</li>
  <li>publish one LLVM-oriented native build corridor,</li>
  <li>and close any source-to-contract mismatches so that source-owned UI metadata and downstream runtime-visible values remain aligned.</li>
</ol>

<hr/>

<h2 id="summary">17. Summary</h2>

<p>
This example is currently the strongest published bounded executable slice in the FROG repository.
It already proves that:
</p>

<ul>
  <li>a canonical FROG source can define a bounded UI-participating executable program,</li>
  <li>that source can be lowered into a repository-visible backend-family contract artifact,</li>
  <li>the contract can be consumed by a Python runtime path,</li>
  <li>the same corridor can also be consumed by a Rust runtime path,</li>
  <li>and the example remains attributable as explicit loop + explicit state rather than runtime-private hidden behavior.</li>
</ul>

<p>
What it does <strong>not</strong> prove yet is full closure.
C/C++ runtime parity is still missing.
A real rendered front panel is still missing.
An LLVM-native executable path is still missing.
A distinct peripheral UI object realization file is still missing.
</p>

<p>
This example should therefore be read as:
</p>

<pre><code>serious bounded executable slice:
yes

full multi-runtime closure:
not yet

native executable closure:
not yet

rendered front-panel closure:
not yet
</code></pre>
