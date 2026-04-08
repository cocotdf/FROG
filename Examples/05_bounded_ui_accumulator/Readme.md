<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Example 05 — Bounded UI Accumulator</h1>

<p align="center">
  <strong>Operational A-to-Z dossier for one bounded source → contract → runtime executable slice</strong><br/>
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
  <li><a href="#fir-posture">9. FIR Posture</a></li>
  <li><a href="#lowering-posture">10. Lowering and Backend Contract</a></li>
  <li><a href="#python-pipe">11. Python Runtime Pipe</a></li>
  <li><a href="#rust-pipe">12. Rust Runtime Pipe</a></li>
  <li><a href="#cpp-pipe">13. C/C++ Runtime Pipe</a></li>
  <li><a href="#llvm-pipe">14. LLVM-Oriented Native Pipe</a></li>
  <li><a href="#observable-parity">15. Observable Parity</a></li>
  <li><a href="#published-gaps">16. Published Gaps Still Open</a></li>
  <li><a href="#summary">17. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This example is the first serious bounded executable slice in the published FROG repository that combines:
</p>

<ul>
  <li>one canonical <code>.frog</code> source,</li>
  <li>one bounded <code>for_loop</code>,</li>
  <li>one explicit local-memory path through <code>frog.core.delay</code>,</li>
  <li>one numeric control and one numeric indicator,</li>
  <li>one public output,</li>
  <li>one published backend-family contract artifact,</li>
  <li>one published Python reference runtime consumer,</li>
  <li>and one published Rust reference runtime consumer posture.</li>
</ul>

<p>
Its purpose is not to claim that the whole language stack is closed.
Its purpose is to provide one small but credible source → contract → runtime corridor that can already be inspected and exercised repository-side.
</p>

<hr/>

<h2 id="expected-behavior">2. Expected Behavior</h2>

<ul>
  <li>the numeric control <code>ctrl_input</code> provides one input value <code>x</code> of type <code>u16</code>,</li>
  <li>the explicit state is initialized to <code>0</code>,</li>
  <li>the loop executes exactly <code>5</code> iterations,</li>
  <li>each iteration computes <code>state_next = state_current + x</code>,</li>
  <li>after the fifth iteration, the final state becomes the result,</li>
  <li>the indicator <code>ind_result</code> displays that result,</li>
  <li>the public output <code>result</code> publishes the same value,</li>
  <li>and minimal object-style UI writes apply <code>face_color</code> to the two widgets.</li>
</ul>

<pre><code>input  = x
state0 = 0

repeat 5 times:
    state = state + x

result = state
</code></pre>

<p>
For <code>x = 3</code>, the expected final result is <code>15</code>.
This mathematical restatement is informative only.
The intended reading remains the explicit loop-and-state corridor.
</p>

<hr/>

<h2 id="closure-status">3. Closure Status</h2>

<table>
  <thead>
    <tr>
      <th>Surface</th>
      <th>Status</th>
      <th>Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Canonical source</td>
      <td>Closed</td>
      <td><code>main.frog</code> is published and semantically attributable.</td>
    </tr>
    <tr>
      <td>Behavioral model</td>
      <td>Closed</td>
      <td>Bounded accumulation with explicit state is clear and repository-visible.</td>
    </tr>
    <tr>
      <td>Front-panel declaration</td>
      <td>Closed</td>
      <td>The source declares two widgets and their basic properties.</td>
    </tr>
    <tr>
      <td>FIR artifact</td>
      <td>Missing</td>
      <td>No example-local FIR serialization is published yet.</td>
    </tr>
    <tr>
      <td>Lowering artifact</td>
      <td>Missing as separate example-local surface</td>
      <td>The backend contract exists, but no distinct example-local lowered artifact is published in this example directory.</td>
    </tr>
    <tr>
      <td>Backend contract</td>
      <td>Closed</td>
      <td>A repository-visible backend-family contract artifact is published.</td>
    </tr>
    <tr>
      <td>Python runtime consumer</td>
      <td>Closed</td>
      <td>The example can be executed through the published Python reference runtime path.</td>
    </tr>
    <tr>
      <td>Python pipe</td>
      <td>Closed</td>
      <td>A concrete command path is available.</td>
    </tr>
    <tr>
      <td>Rust runtime consumer</td>
      <td>Partial</td>
      <td>The example is consumed by Rust through tests, but no dedicated runner binary is published yet.</td>
    </tr>
    <tr>
      <td>Rust pipe</td>
      <td>Partial</td>
      <td>Proof exists through <code>cargo test</code>, not yet through a dedicated example runner.</td>
    </tr>
    <tr>
      <td>C/C++ runtime consumer</td>
      <td>Missing</td>
      <td>No published C or C++ runtime consumer exists for this example yet.</td>
    </tr>
    <tr>
      <td>C/C++ pipe</td>
      <td>Missing</td>
      <td>No build/run pipe is published yet.</td>
    </tr>
    <tr>
      <td>Peripheral UI object realization file</td>
      <td>Missing</td>
      <td>No distinct host-side UI object realization file is published for this example.</td>
    </tr>
    <tr>
      <td>Rendered front panel</td>
      <td>Missing</td>
      <td>Runtime-visible widget state exists, but no real rendered host UI path is published.</td>
    </tr>
    <tr>
      <td>LLVM-oriented native executable path</td>
      <td>Missing</td>
      <td>No LLVM-native path is published for this example.</td>
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
      Canonical source of the example. This remains the source-owned program meaning.</li>
  <li><code>Examples/05_bounded_ui_accumulator/Readme.md</code><br/>
      Operational example dossier describing behavior, closure status, runtime pipes, and remaining gaps.</li>
  <li><code>Implementations/Reference/ContractEmitter/examples/05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json</code><br/>
      Published backend-family contract artifact consumed downstream by reference runtimes.</li>
  <li><code>Implementations/Reference/Runtime/reference_runtime.py</code><br/>
      Python reference runtime implementation for the accepted backend family.</li>
  <li><code>Implementations/Reference/Runtime/run_slice05_contract.py</code><br/>
      Python runner for this example contract.</li>
  <li><code>Implementations/Reference/Runtime/rust/tests/slice05_contract_smoke.rs</code><br/>
      Rust contract-shape validation for the published contract artifact.</li>
  <li><code>Implementations/Reference/Runtime/rust/tests/slice05_execution.rs</code><br/>
      Rust execution proof for the published example corridor.</li>
</ul>

<hr/>

<h2 id="shared-corridor">6. Shared Canonical Corridor</h2>

<pre><code>canonical .frog source
        |
        v
validated example meaning
        |
        v
FIR-target execution-facing posture
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
The runtime implementations are downstream consumers.
They are not the definition of the language and not the hidden source of semantic truth.
</p>

<hr/>

<h2 id="source-posture">7. Canonical Source Posture</h2>

<p>
The source explicitly declares:
</p>

<ul>
  <li>one <code>u16</code> control widget,</li>
  <li>one <code>u16</code> indicator widget,</li>
  <li>one bounded loop of count <code>5</code>,</li>
  <li>one explicit initial state of <code>0</code>,</li>
  <li>one explicit state carrier through <code>frog.core.delay</code>,</li>
  <li>one explicit accumulation step through <code>frog.core.add</code>,</li>
  <li>one indicator value path,</li>
  <li>one public output path,</li>
  <li>and two explicit <code>frog.ui.property_write</code> operations on <code>face_color</code>.</li>
</ul>

<p>
The source therefore already preserves explicit loop meaning, explicit state meaning, explicit UI value participation, and explicit object-style UI interaction.
</p>

<hr/>

<h2 id="ui-posture">8. Front-Panel and UI Object Posture</h2>

<p>
This example demonstrates both:
</p>

<ul>
  <li><strong>natural value participation</strong> through <code>widget_value</code>,</li>
  <li><strong>object-style access</strong> through <code>widget_reference</code> and <code>frog.ui.property_write</code>.</li>
</ul>

<p>
What is still missing is a distinct downstream peripheral UI object realization file and a real rendered host UI path.
Current published runtime outputs expose widget runtime state, but that is not yet equivalent to a true rendered front panel.
</p>

<hr/>

<h2 id="fir-posture">9. FIR Posture</h2>

<p>
This example already has a clear execution-facing reading, but no example-local published FIR artifact exists yet.
So the FIR posture is architecturally present, but not yet serialized as a repository-visible example artifact.
</p>

<hr/>

<h2 id="lowering-posture">10. Lowering and Backend Contract</h2>

<p>
The key currently published downstream handoff for this example is the backend-family contract artifact.
That is the strongest closed handoff boundary presently visible for this slice.
</p>

<p>
What is still missing is a cleaner separation between:
</p>

<ul>
  <li>example-local FIR,</li>
  <li>example-local lowering output,</li>
  <li>backend contract,</li>
  <li>and runtime-private realization.</li>
</ul>

<hr/>

<h2 id="python-pipe">11. Python Runtime Pipe</h2>

<h3>Run command</h3>

<pre><code>python -m Implementations.Reference.Runtime.run_slice05_contract 3
</code></pre>

<p>
Equivalent local invocation:
</p>

<pre><code>python Implementations/Reference/Runtime/run_slice05_contract.py 3
</code></pre>

<h3>Expected observable result</h3>

<pre><code>public.result = 15
ui.ctrl_input = 3
ui.ind_result = 15
</code></pre>

<p>
This is the strongest currently published operational pipe for the example.
</p>

<hr/>

<h2 id="rust-pipe">12. Rust Runtime Pipe</h2>

<h3>Current proof command</h3>

<pre><code>cd Implementations/Reference/Runtime/rust
cargo test
</code></pre>

<p>
This currently proves:
</p>

<ul>
  <li>contract deserialization,</li>
  <li>contract-shape acceptance for the supported slice,</li>
  <li>bounded accumulation execution,</li>
  <li>and expected final result for input <code>3</code>.</li>
</ul>

<p>
This is real downstream consumption, but it is still partial because the example does not yet publish one dedicated Rust runner binary comparable to the Python runner.
</p>

<hr/>

<h2 id="cpp-pipe">13. C/C++ Runtime Pipe</h2>

<p>
No published C or C++ runtime consumer exists yet for this example.
Accordingly, no C/C++ build/run pipe can currently be claimed.
</p>

<hr/>

<h2 id="llvm-pipe">14. LLVM-Oriented Native Pipe</h2>

<p>
This example does not yet publish:
</p>

<ul>
  <li>an example-local FIR artifact,</li>
  <li>an explicit FIR-to-lowering bridge artifact,</li>
  <li>an LLVM-family lowered artifact,</li>
  <li>a native build command,</li>
  <li>a packaged native executable,</li>
  <li>or a rendered native front-panel host path.</li>
</ul>

<p>
So native-executable closure is not yet reached.
</p>

<hr/>

<h2 id="observable-parity">15. Observable Parity</h2>

<p>
The strongest published parity statement today is:
</p>

<ul>
  <li>the Python path consumes the published contract and produces the expected bounded result,</li>
  <li>the Rust path consumes the same contract corridor through tests and validates the same behavioral outcome,</li>
  <li>and both remain aligned with explicit loop-and-state behavior.</li>
</ul>

<table>
  <thead>
    <tr>
      <th>Observable</th>
      <th>Expected value for input 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Iteration count</td>
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
    <tr>
      <td>Control runtime value</td>
      <td>3</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="published-gaps">16. Published Gaps Still Open</h2>

<ol>
  <li>publish an explicit FIR artifact for the example,</li>
  <li>publish an explicit example-local lowering artifact,</li>
  <li>publish a distinct peripheral UI object realization file,</li>
  <li>publish a dedicated Rust runner binary,</li>
  <li>publish a C/C++ mini runtime and its build/run pipe,</li>
  <li>publish a real rendered front-panel host path,</li>
  <li>publish an LLVM-oriented native path,</li>
  <li>and keep source-owned UI metadata aligned with all downstream contracts and runtime checks.</li>
</ol>

<hr/>

<h2 id="summary">17. Summary</h2>

<p>
This example is already a serious bounded executable slice.
It proves that a canonical FROG source can drive a repository-visible downstream contract and can be consumed by more than one runtime language.
</p>

<p>
It does not yet prove full closure.
C/C++ parity is still missing.
A distinct FIR artifact is still missing.
A rendered front panel is still missing.
An LLVM-native path is still missing.
</p>

<pre><code>serious executable slice:
yes

python runtime closure:
yes

rust runtime closure:
partial

c/c++ runtime closure:
no

rendered front-panel closure:
no

llvm native closure:
no
</code></pre>
