<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Example 05 — Bounded UI Accumulator</h1>

<p align="center">
  <strong>Operational A-to-Z dossier for the first published bounded source → UI object file → FIR → lowering → contract → runtime executable slice</strong><br/>
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
  <li><a href="#observable-parity">15. Observable Parity Across Runtime Families</a></li>
  <li><a href="#published-gaps">16. Published Gaps Still To Close</a></li>
  <li><a href="#summary">17. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This example is the first published bounded applicative vertical slice in the FROG repository that already crosses a real downstream execution boundary.
It combines:
</p>

<ul>
  <li>one canonical <code>.frog</code> source file,</li>
  <li>one bounded counted loop,</li>
  <li>one explicit local-memory path through <code>frog.core.delay</code>,</li>
  <li>one numeric control and one numeric indicator,</li>
  <li>one example-local peripheral UI object realization file,</li>
  <li>one example-local FIR artifact,</li>
  <li>one example-local lowered artifact,</li>
  <li>one published backend contract artifact,</li>
  <li>one published Python runtime consumer,</li>
  <li>and one published Rust runtime consumer posture.</li>
</ul>

<p>
Its role is not to prove the full long-term closure of FROG.
Its role is to provide one serious small slice where the reader can inspect the source, the UI-host realization posture, the execution-facing reading, the lowering posture, and the downstream runtime handoff in one place.
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

<hr/>

<h2 id="closure-status">3. Closure Status</h2>

<table>
  <thead>
    <tr>
      <th>Surface</th>
      <th>Status</th>
      <th>Current posture</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Canonical source</td>
      <td>Closed</td>
      <td><code>main.frog</code> is present.</td>
    </tr>
    <tr>
      <td>Source-owned front panel</td>
      <td>Closed</td>
      <td>Two widgets are declared in canonical source.</td>
    </tr>
    <tr>
      <td>Behavioral model</td>
      <td>Closed</td>
      <td>Bounded counted loop, explicit delay-backed state, final result publication.</td>
    </tr>
    <tr>
      <td>Peripheral UI object realization file</td>
      <td>Defined</td>
      <td><code>front_panel.objects.json</code> now makes host-side object realization explicit.</td>
    </tr>
    <tr>
      <td>FIR-readable corridor</td>
      <td>Defined example-local</td>
      <td><code>main.fir.json</code> now exposes an example-local execution-facing artifact.</td>
    </tr>
    <tr>
      <td>Lowering posture</td>
      <td>Defined example-local</td>
      <td><code>main.lowering.json</code> now exposes an example-local lowered artifact.</td>
    </tr>
    <tr>
      <td>Backend contract</td>
      <td>Closed</td>
      <td>A repository-visible contract artifact exists for the reference runtime family.</td>
    </tr>
    <tr>
      <td>Python runtime consumer</td>
      <td>Closed</td>
      <td>A runnable Python entry point is published.</td>
    </tr>
    <tr>
      <td>Python build / run pipe</td>
      <td>Closed</td>
      <td>The operational command is explicit.</td>
    </tr>
    <tr>
      <td>Rust runtime consumer</td>
      <td>Partial-to-closed</td>
      <td>A Rust consumer and tests are published; proof currently lives in test-driven execution rather than one dedicated example runner binary.</td>
    </tr>
    <tr>
      <td>Rust build / run pipe</td>
      <td>Partial</td>
      <td><code>cargo test</code> proves the corridor; a dedicated example runner is still missing.</td>
    </tr>
    <tr>
      <td>C/C++ runtime consumer</td>
      <td>Missing</td>
      <td>No published C or C++ runtime consumer exists yet for this example.</td>
    </tr>
    <tr>
      <td>C/C++ build / run pipe</td>
      <td>Missing</td>
      <td>No published pipe exists yet.</td>
    </tr>
    <tr>
      <td>Rendered front panel</td>
      <td>Missing</td>
      <td>The host realization file is explicit, but no rendered host path is published yet.</td>
    </tr>
    <tr>
      <td>LLVM-oriented native executable path</td>
      <td>Missing</td>
      <td>The example-local FIR and lowering artifacts now exist, but no native LLVM-family bridge, build, or executable is published yet.</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="useful-file-tree">4. Useful File Tree</h2>

<pre><code>Examples/
└── 05_bounded_ui_accumulator/
    ├── Readme.md
    ├── main.frog
    ├── front_panel.objects.json
    ├── main.fir.json
    └── main.lowering.json

Implementations/
└── Reference/
    ├── ContractEmitter/
    │   └── examples/
    │       └── 05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json
    ├── Runtime/
    │   ├── Readme.md
    │   ├── reference_runtime.py
    │   ├── run_slice05_contract.py
    │   ├── python/
    │   │   └── Readme.md
    │   ├── rust/
    │   │   ├── Readme.md
    │   │   ├── Cargo.toml
    │   │   └── tests/
    │   │       ├── slice05_contract_smoke.rs
    │   │       └── slice05_execution.rs
    │   └── cpp/
    │       └── Readme.md
    └── LLVM/
        └── Readme.md
</code></pre>

<hr/>

<h2 id="file-responsibilities">5. File Responsibilities</h2>

<ul>
  <li><code>Examples/05_bounded_ui_accumulator/main.frog</code><br/>
      Canonical source of the example. This remains the source of truth for example-level program meaning.</li>
  <li><code>Examples/05_bounded_ui_accumulator/front_panel.objects.json</code><br/>
      Peripheral host-side UI object realization file. It defines concrete widget realization and visual host metadata without redefining executable semantics.</li>
  <li><code>Examples/05_bounded_ui_accumulator/main.fir.json</code><br/>
      Example-local execution-facing artifact describing the bounded executable unit, explicit state, UI binding surface, and result publication path.</li>
  <li><code>Examples/05_bounded_ui_accumulator/main.lowering.json</code><br/>
      Example-local lowered artifact that prepares the corridor for backend-family runtime consumption and future compiler-family paths.</li>
  <li><code>Examples/05_bounded_ui_accumulator/Readme.md</code><br/>
      Operational example dossier. It explains what the example does, how the corridor is staged, what is already runnable, and what is still missing.</li>
  <li><code>Implementations/Reference/ContractEmitter/examples/05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json</code><br/>
      Published backend-family contract artifact consumed downstream by the reference runtime family.</li>
  <li><code>Implementations/Reference/Runtime/reference_runtime.py</code><br/>
      Python-side reference runtime realization for the bounded reference family.</li>
  <li><code>Implementations/Reference/Runtime/run_slice05_contract.py</code><br/>
      Python demonstration entry point for executing the published contract of this example.</li>
  <li><code>Implementations/Reference/Runtime/python/Readme.md</code><br/>
      Python runtime-family boundary, goals, and example-facing posture.</li>
  <li><code>Implementations/Reference/Runtime/rust/Readme.md</code><br/>
      Rust runtime-family boundary, goals, and example-facing posture.</li>
  <li><code>Implementations/Reference/Runtime/rust/tests/slice05_contract_smoke.rs</code><br/>
      Rust contract-shape validation test against the published contract artifact.</li>
  <li><code>Implementations/Reference/Runtime/rust/tests/slice05_execution.rs</code><br/>
      Rust execution test showing that the published contract produces the expected bounded result.</li>
  <li><code>Implementations/Reference/Runtime/cpp/Readme.md</code><br/>
      C/C++ runtime-family target posture for the same canonical corridor.</li>
  <li><code>Implementations/Reference/LLVM/Readme.md</code><br/>
      Downstream compiler-family posture for LLVM-oriented native paths.</li>
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
peripheral UI object realization file
        |
        v
FIR / execution-facing representation
        |
        v
lowering posture
        |
        v
backend-family contract artifact
        |
        +------------------------------+------------------------------+
        |                              |                              |
        v                              v                              v
Python runtime consumer        Rust runtime consumer        C/C++ runtime consumer
        |
        \-------------------- optional LLVM-oriented native path ----/
</code></pre>

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
The source also now contains one explicit pointer to a peripheral UI object realization file.
That file remains downstream and non-authoritative for semantics.
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
The new <code>front_panel.objects.json</code> file makes the host-side realization boundary explicit:
</p>

<ul>
  <li>the canonical source keeps widget identity and program meaning,</li>
  <li>the peripheral file defines host widget classes, concrete visual configuration, and runtime-facing realization metadata,</li>
  <li>and neither file alone is allowed to erase the distinction between source-owned meaning and host-owned realization.</li>
</ul>

<hr/>

<h2 id="fir-posture">9. FIR / Execution-Facing Posture</h2>

<p>
The example now carries one explicit example-local FIR artifact:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/main.fir.json</code></pre>

<p>
That artifact makes visible:
</p>

<ul>
  <li>the bounded executable unit,</li>
  <li>the public input and output binding model,</li>
  <li>the UI binding surface,</li>
  <li>the explicit state carrier,</li>
  <li>the loop execution model,</li>
  <li>and the final result publication rule.</li>
</ul>

<hr/>

<h2 id="lowering-posture">10. Lowering and Backend-Contract Posture</h2>

<p>
The example now also carries one explicit example-local lowered artifact:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/main.lowering.json</code></pre>

<p>
This lowered artifact is not yet the compiler-family artifact itself.
It is the explicit target-oriented bridge between the FIR reading and downstream runtime-family or compiler-family consumers.
</p>

<p>
The already-published backend contract remains the first repository-visible runtime-family handoff artifact:
</p>

<pre><code>Implementations/Reference/ContractEmitter/examples/
05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json
</code></pre>

<hr/>

<h2 id="python-pipe">11. Python Runtime Pipe</h2>

<p>
The published Python pipe is the clearest operational corridor currently available for this example.
</p>

<h3>Python run command</h3>

<pre><code>python -m Implementations.Reference.Runtime.run_slice05_contract 3
</code></pre>

<p>
Equivalent direct script-style invocation:
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

<hr/>

<h2 id="rust-pipe">12. Rust Runtime Pipe</h2>

<p>
The published Rust corridor already proves downstream multi-runtime consumption, but it is currently exposed primarily through tests rather than through one dedicated example runner binary.
</p>

<h3>Rust verification command</h3>

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

<hr/>

<h2 id="cpp-pipe">13. C/C++ Runtime Pipe</h2>

<p>
No published C or C++ runtime consumer exists yet for this example.
Accordingly:
</p>

<ul>
  <li>there is no published C/C++ mini runtime for this example,</li>
  <li>there is no published C/C++ build pipe,</li>
  <li>there is no published C/C++ run pipe,</li>
  <li>and runtime modularity is therefore only partially demonstrated today at the repository level.</li>
</ul>

<hr/>

<h2 id="llvm-path">14. LLVM-Oriented Native Path</h2>

<p>
The example-local FIR and lowered artifacts now make the compiler-facing corridor easier to close, but this example still does not publish a closed LLVM-oriented downstream path to a native executable.
In particular, the repository does not yet expose, for this example:
</p>

<ul>
  <li>one explicit lowering-to-LLVM-family bridge artifact,</li>
  <li>one compiler-facing lowered artifact specialized for LLVM-family consumption,</li>
  <li>one native build command,</li>
  <li>one packaged executable result,</li>
  <li>or one rendered native front-panel host path.</li>
</ul>

<hr/>

<h2 id="observable-parity">15. Observable Parity Across Runtime Families</h2>

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

<hr/>

<h2 id="published-gaps">16. Published Gaps Still To Close</h2>

<ol>
  <li>publish one real C/C++ mini runtime consumer and its build/run pipe,</li>
  <li>publish one dedicated Rust runner entry point comparable to the Python runner,</li>
  <li>publish one real rendered front-panel host path,</li>
  <li>publish one lowering-to-LLVM-family bridge artifact,</li>
  <li>publish one LLVM-oriented native build corridor,</li>
  <li>and keep source, FIR, lowering, contract, and runtime-visible UI metadata aligned across the corridor.</li>
</ol>

<hr/>

<h2 id="summary">17. Summary</h2>

<p>
This example is currently the strongest published bounded executable slice in the FROG repository.
It now exposes, in one named location:
</p>

<ul>
  <li>a canonical FROG source,</li>
  <li>a peripheral UI object realization file,</li>
  <li>an example-local FIR artifact,</li>
  <li>an example-local lowered artifact,</li>
  <li>a repository-visible backend-family contract artifact,</li>
  <li>a Python runtime path,</li>
  <li>and a Rust runtime proof path.</li>
</ul>

<pre><code>serious bounded executable slice:
yes

example-local UI object file:
yes

example-local FIR artifact:
yes

example-local lowered artifact:
yes

full multi-runtime closure:
not yet

native executable closure:
not yet

rendered front-panel closure:
not yet
</code></pre>
