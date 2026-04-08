<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Example 05 — Bounded UI Accumulator</h1>

<p align="center">
  <strong>Operational A-to-Z dossier for a bounded source → widget package → FIR → lowering → contract → multi-runtime execution slice</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#expected-behavior">2. Expected Behavior</a></li>
  <li><a href="#current-purpose">3. Current Purpose of This Example</a></li>
  <li><a href="#closure-status">4. Closure Status</a></li>
  <li><a href="#useful-file-tree">5. Useful File Tree</a></li>
  <li><a href="#file-responsibilities">6. File Responsibilities</a></li>
  <li><a href="#shared-corridor">7. Shared Canonical Corridor</a></li>
  <li><a href="#source-posture">8. Canonical Source Posture</a></li>
  <li><a href="#ui-posture">9. UI Package and Widget Realization Posture</a></li>
  <li><a href="#fir-posture">10. FIR / Execution-Facing Posture</a></li>
  <li><a href="#lowering-posture">11. Lowering and Backend-Contract Posture</a></li>
  <li><a href="#python-pipe">12. Python Runtime Pipe</a></li>
  <li><a href="#rust-pipe">13. Rust Runtime Pipe</a></li>
  <li><a href="#cpp-pipe">14. C/C++ Runtime Pipe</a></li>
  <li><a href="#llvm-path">15. LLVM-Oriented Native Path</a></li>
  <li><a href="#observable-parity">16. Observable Parity Across Runtime Families</a></li>
  <li><a href="#published-gaps">17. Published Gaps Still To Close</a></li>
  <li><a href="#next-closure-target">18. Next Closure Target</a></li>
  <li><a href="#summary">19. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This example is the primary bounded executable vertical slice currently used to make the FROG corridor inspectable from authored source down to downstream runtime consumption.
</p>

<p>
It combines:
</p>

<ul>
  <li>one canonical <code>.frog</code> source file,</li>
  <li>one bounded counted loop,</li>
  <li>one explicit local state path through <code>frog.core.delay</code>,</li>
  <li>one numeric control and one numeric indicator,</li>
  <li>one dedicated widget-oriented peripheral UI package,</li>
  <li>one example-local FIR artifact,</li>
  <li>one example-local lowered artifact,</li>
  <li>one repository-visible backend contract artifact,</li>
  <li>one Python runtime consumer path,</li>
  <li>one Rust runtime validation path.</li>
</ul>

<p>
Its role is not to claim that the whole long-term FROG stack is already closed.
Its role is to provide one serious, bounded, inspectable slice where a reader can follow:
</p>

<ul>
  <li>canonical source meaning,</li>
  <li>front-panel/widget packaging,</li>
  <li>execution-facing interpretation,</li>
  <li>lowering posture,</li>
  <li>runtime-family consumption.</li>
</ul>

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
  <li>the runtime also supports bounded object-style writes such as <code>face_color</code>, <code>label</code>, <code>visible</code>, and <code>enabled</code>.</li>
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

<h2 id="current-purpose">3. Current Purpose of This Example</h2>

<p>
This example is the current bounded proof that FROG can already be read as:
</p>

<pre><code>.frog source
    -&gt; widget package
    -&gt; execution-facing reading
    -&gt; lowering
    -&gt; contract
    -&gt; runtime consumption
</code></pre>

<p>
It is also the first example used to make the widget model concrete rather than merely conceptual.
</p>

<p>
The current widget closure target is intentionally small and explicit:
</p>

<ul>
  <li><code>frog.widgets.panel</code></li>
  <li><code>frog.widgets.numeric_control</code></li>
  <li><code>frog.widgets.numeric_indicator</code></li>
  <li><code>frog.widgets.label</code></li>
</ul>

<p>
The current concrete property surface exercised by the Python runtime is:
</p>

<ul>
  <li><code>value</code></li>
  <li><code>label</code></li>
  <li><code>visible</code></li>
  <li><code>enabled</code></li>
  <li><code>face_color</code></li>
</ul>

<hr/>

<h2 id="closure-status">4. Closure Status</h2>

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
      <td><code>main.frog</code> remains the source of truth for program semantics.</td>
    </tr>
    <tr>
      <td>Source-owned front panel</td>
      <td>Closed</td>
      <td>The canonical source declares the widgets that participate in the program.</td>
    </tr>
    <tr>
      <td>Widget-oriented peripheral UI package</td>
      <td>Defined</td>
      <td><code>ui/accumulator_panel.wfrog</code> makes widget realization and panel packaging explicit.</td>
    </tr>
    <tr>
      <td>SVG visual assets</td>
      <td>Defined</td>
      <td>Dedicated SVG assets exist as visual skins and anchors only, not as semantic truth.</td>
    </tr>
    <tr>
      <td>Behavioral model</td>
      <td>Closed</td>
      <td>Bounded counted loop, explicit delay-backed state, final result publication.</td>
    </tr>
    <tr>
      <td>FIR-readable corridor</td>
      <td>Defined example-local</td>
      <td><code>main.fir.json</code> exposes an example-local execution-facing artifact.</td>
    </tr>
    <tr>
      <td>Lowering posture</td>
      <td>Defined example-local</td>
      <td><code>main.lowering.json</code> exposes an example-local lowered artifact.</td>
    </tr>
    <tr>
      <td>Backend contract</td>
      <td>Closed</td>
      <td>A repository-visible contract artifact exists for the reference runtime family.</td>
    </tr>
    <tr>
      <td>Python runtime consumer</td>
      <td>Closed for bounded widget slice</td>
      <td>A concrete Python UI runtime and runner are now available for this example.</td>
    </tr>
    <tr>
      <td>Python build / run pipe</td>
      <td>Closed</td>
      <td>Operational commands are explicit below.</td>
    </tr>
    <tr>
      <td>Rust runtime consumer</td>
      <td>Partial</td>
      <td>A Rust consumer and tests are published; no dedicated rendered UI runner is published yet.</td>
    </tr>
    <tr>
      <td>Rust build / run pipe</td>
      <td>Partial</td>
      <td><code>cargo test</code> proves the bounded corridor; no dedicated example UI runner is published yet.</td>
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
      <td>Partially closed</td>
      <td>A concrete Python host-rendered path now exists for the bounded widget subset.</td>
    </tr>
    <tr>
      <td>LLVM-oriented native executable path</td>
      <td>Missing</td>
      <td>No native LLVM-family bridge, build, or executable is published yet.</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="useful-file-tree">5. Useful File Tree</h2>

<pre><code>Examples/
└── 05_bounded_ui_accumulator/
    ├── Readme.md
    ├── main.frog
    ├── main.fir.json
    ├── main.lowering.json
    └── ui/
        ├── accumulator_panel.wfrog
        └── assets/
            ├── numeric_control.svg
            └── numeric_indicator.svg

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
    │   │   ├── Readme.md
    │   │   ├── run_slice05_ui.py
    │   │   └── ui_runtime.py
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

<h2 id="file-responsibilities">6. File Responsibilities</h2>

<ul>
  <li><code>Examples/05_bounded_ui_accumulator/main.frog</code><br/>
      Canonical source of the example. This remains the source of truth for program meaning.</li>

  <li><code>Examples/05_bounded_ui_accumulator/ui/accumulator_panel.wfrog</code><br/>
      Peripheral widget-oriented front-panel package. It defines panel packaging, widget classes, instance layout, initial widget properties, and visual resource references without redefining executable semantics.</li>

  <li><code>Examples/05_bounded_ui_accumulator/ui/assets/numeric_control.svg</code><br/>
      Visual asset for the numeric control skin. It provides visual structure and anchors only. It does not own dynamic values or widget semantics.</li>

  <li><code>Examples/05_bounded_ui_accumulator/ui/assets/numeric_indicator.svg</code><br/>
      Visual asset for the numeric indicator skin. It provides visual structure and anchors only. It does not own dynamic values or widget semantics.</li>

  <li><code>Examples/05_bounded_ui_accumulator/main.fir.json</code><br/>
      Example-local execution-facing artifact describing the bounded executable unit, explicit state, UI binding surface, and result publication path.</li>

  <li><code>Examples/05_bounded_ui_accumulator/main.lowering.json</code><br/>
      Example-local lowered artifact that prepares the corridor for backend-family runtime consumption and future compiler-family paths.</li>

  <li><code>Implementations/Reference/ContractEmitter/examples/05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json</code><br/>
      Published backend-family contract artifact consumed downstream by the reference runtime family.</li>

  <li><code>Implementations/Reference/Runtime/python/ui_runtime.py</code><br/>
      Concrete bounded Python UI runtime for the current widget subset of this example.</li>

  <li><code>Implementations/Reference/Runtime/python/run_slice05_ui.py</code><br/>
      Python example runner that loads the widget package, opens a real window, and executes the bounded UI accumulator slice.</li>

  <li><code>Implementations/Reference/Runtime/reference_runtime.py</code><br/>
      Existing Python-side reference runtime for the already-published contract-based corridor.</li>

  <li><code>Implementations/Reference/Runtime/run_slice05_contract.py</code><br/>
      Existing Python demonstration entry point for executing the published contract artifact.</li>

  <li><code>Implementations/Reference/Runtime/rust/tests/slice05_contract_smoke.rs</code><br/>
      Rust contract-shape validation test against the published contract artifact.</li>

  <li><code>Implementations/Reference/Runtime/rust/tests/slice05_execution.rs</code><br/>
      Rust execution test showing that the published contract produces the expected bounded result.</li>
</ul>

<hr/>

<h2 id="shared-corridor">7. Shared Canonical Corridor</h2>

<p>
The core architectural point of this example is that one canonical corridor is shared across downstream consumers.
The intended reading is:
</p>

<pre><code>canonical .frog source
        |
        v
widget-oriented front-panel package (.wfrog)
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

<p>
This example currently closes that corridor most concretely on the Python side.
</p>

<hr/>

<h2 id="source-posture">8. Canonical Source Posture</h2>

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
  <li>and explicit object-style UI property writes.</li>
</ul>

<p>
The source may reference a peripheral UI package, but that package remains downstream and non-authoritative for program semantics.
</p>

<hr/>

<h2 id="ui-posture">9. UI Package and Widget Realization Posture</h2>

<p>
This example demonstrates two distinct UI interaction surfaces:
</p>

<ul>
  <li><strong>natural value participation</strong> through <code>widget_value</code>,</li>
  <li><strong>object-style interaction</strong> through <code>widget_reference</code> and <code>frog.ui.property_write</code>.</li>
</ul>

<p>
The <code>.wfrog</code> package makes the host-side realization boundary explicit:
</p>

<ul>
  <li>the canonical source keeps widget identity and program meaning,</li>
  <li>the peripheral package defines concrete panel packaging, initial widget realization state, and visual resource references,</li>
  <li>the runtime interprets both layers together,</li>
  <li>the host realizes the live widget objects,</li>
  <li>and no visual asset is allowed to erase the distinction between source-owned meaning and host-owned realization.</li>
</ul>

<p>
The SVG posture is intentionally disciplined:
</p>

<ul>
  <li>SVG assets provide visual skins and anchors,</li>
  <li>SVG assets do not provide dynamic widget values,</li>
  <li>SVG assets do not provide dynamic label text as semantic truth,</li>
  <li>SVG assets do not provide widget behavior.</li>
</ul>

<hr/>

<h2 id="fir-posture">10. FIR / Execution-Facing Posture</h2>

<p>
The example carries one explicit example-local FIR artifact:
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
  <li>the final result publication rule.</li>
</ul>

<hr/>

<h2 id="lowering-posture">11. Lowering and Backend-Contract Posture</h2>

<p>
The example also carries one explicit example-local lowered artifact:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/main.lowering.json</code></pre>

<p>
This lowered artifact is not yet the native compiler-family artifact itself.
It is the explicit target-oriented bridge between the FIR reading and downstream runtime-family or compiler-family consumers.
</p>

<p>
The already-published backend contract remains the first repository-visible runtime-family handoff artifact:
</p>

<pre><code>Implementations/Reference/ContractEmitter/examples/
05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json
</code></pre>

<hr/>

<h2 id="python-pipe">12. Python Runtime Pipe</h2>

<p>
There are currently two useful Python-facing corridors for this example.
</p>

<h3>12.1 Contract-based Python corridor</h3>

<pre><code>python -m Implementations.Reference.Runtime.run_slice05_contract 3
</code></pre>

<p>
Equivalent direct script-style invocation:
</p>

<pre><code>python Implementations/Reference/Runtime/run_slice05_contract.py 3
</code></pre>

<p>
This path exercises the already-published contract-driven reference runtime corridor.
</p>

<h3>12.2 Rendered Python UI corridor</h3>

<pre><code>python Implementations/Reference/Runtime/python/run_slice05_ui.py
</code></pre>

<p>
Optional initial value:
</p>

<pre><code>python Implementations/Reference/Runtime/python/run_slice05_ui.py 3
</code></pre>

<p>
Optional immediate execution after startup:
</p>

<pre><code>python Implementations/Reference/Runtime/python/run_slice05_ui.py 3 --autorun
</code></pre>

<h3>12.3 What the rendered Python UI path currently proves</h3>

<ol>
  <li>the runtime loads the example-local <code>.wfrog</code> package,</li>
  <li>constructs concrete live widget objects,</li>
  <li>opens a real host window,</li>
  <li>renders the bounded widget subset,</li>
  <li>supports runtime property writes such as <code>value</code>, <code>label</code>, <code>visible</code>, <code>enabled</code>, and <code>face_color</code>,</li>
  <li>executes the bounded accumulator logic,</li>
  <li>publishes the result into the indicator surface.</li>
</ol>

<p>
This is intentionally a bounded runtime slice, not yet a complete industrial widget system.
</p>

<hr/>

<h2 id="rust-pipe">13. Rust Runtime Pipe</h2>

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
  <li>the final result for input <code>3</code> is <code>15</code>.</li>
</ul>

<hr/>

<h2 id="cpp-pipe">14. C/C++ Runtime Pipe</h2>

<p>
No published C or C++ runtime consumer exists yet for this example.
Accordingly:
</p>

<ul>
  <li>there is no published C/C++ mini runtime for this example,</li>
  <li>there is no published C/C++ build pipe,</li>
  <li>there is no published C/C++ run pipe,</li>
  <li>runtime modularity is therefore only partially demonstrated today at the repository level.</li>
</ul>

<hr/>

<h2 id="llvm-path">15. LLVM-Oriented Native Path</h2>

<p>
The example-local FIR and lowered artifacts make the compiler-facing corridor easier to close, but this example still does not publish a closed LLVM-oriented downstream path to a native executable.
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

<h2 id="observable-parity">16. Observable Parity Across Runtime Families</h2>

<p>
At the current published state, the strongest shared parity statement that can be made is:
</p>

<ul>
  <li>the Python contract path consumes the published contract and produces the expected bounded result,</li>
  <li>the Python rendered UI path produces the same bounded result through a real host window,</li>
  <li>the Rust path validates the same contract shape and confirms the same final bounded result through tests,</li>
  <li>all current paths preserve the explicit loop-and-state reading rather than replacing it with a shortcut semantic narrative.</li>
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

<h2 id="published-gaps">17. Published Gaps Still To Close</h2>

<ol>
  <li>publish one real C/C++ mini runtime consumer and its build/run pipe,</li>
  <li>publish one dedicated Rust runner entry point comparable to the Python runner,</li>
  <li>connect the rendered UI path more directly to the already-published contract corridor,</li>
  <li>publish one real rendered front-panel host path beyond the bounded Python subset,</li>
  <li>publish one lowering-to-LLVM-family bridge artifact,</li>
  <li>publish one LLVM-oriented native build corridor,</li>
  <li>keep source, <code>.wfrog</code>, FIR, lowering, contract, and runtime-visible UI metadata aligned across the corridor.</li>
</ol>

<hr/>

<h2 id="next-closure-target">18. Next Closure Target</h2>

<p>
The next closure target for this example is not another prose-only refinement.
It is the next concrete executable corridor extension:
</p>

<ul>
  <li>either a contract-driven rendered Python UI path,</li>
  <li>or a first C/C++ consumer,</li>
  <li>or a first LLVM-facing native bridge.</li>
</ul>

<p>
That is the point where the example starts proving real downstream modularity rather than only architectural plausibility.
</p>

<hr/>

<h2 id="summary">19. Summary</h2>

<p>
This example is currently the strongest bounded executable slice published in the FROG repository.
It now exposes, in one named location:
</p>

<ul>
  <li>a canonical FROG source,</li>
  <li>a widget-oriented peripheral UI package,</li>
  <li>SVG visual assets used as skins and anchors only,</li>
  <li>an example-local FIR artifact,</li>
  <li>an example-local lowered artifact,</li>
  <li>a repository-visible backend-family contract artifact,</li>
  <li>a Python contract path,</li>
  <li>a Python rendered UI path,</li>
  <li>and a Rust proof path.</li>
</ul>

<pre><code>serious bounded executable slice:
yes

example-local widget package:
yes

example-local FIR artifact:
yes

example-local lowered artifact:
yes

rendered host window:
yes, bounded Python subset

full multi-runtime closure:
not yet

native executable closure:
not yet
</code></pre>
