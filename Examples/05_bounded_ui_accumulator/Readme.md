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
  <li><a href="#published-gaps-still-to-close">17. Published Gaps Still To Close</a></li>
  <li><a href="#next-closure-target">18. Next Closure Target</a></li>
  <li><a href="#summary">19. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This example is the primary bounded executable vertical slice currently used to make the FROG corridor inspectable
from authored source down to downstream runtime consumption.
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
  <li>one Python runtime execution path,</li>
  <li>one Rust runtime verification path,</li>
  <li>one C/C++ runtime scaffolding path.</li>
</ul>

<p>
Its role is not to claim that the whole long-term FROG stack is already closed.
Its role is to provide one serious, bounded, inspectable slice where a reader can follow:
</p>

<ul>
  <li>canonical source meaning,</li>
  <li>front-panel and widget packaging,</li>
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
  <li>the runtime corridor also supports bounded object-style UI interaction such as widget property writes and widget realization updates for the supported subset.</li>
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
The current concrete property and interaction surface targeted by the bounded runtime slice is intentionally narrow:
</p>

<ul>
  <li><code>value</code></li>
  <li><code>label</code></li>
  <li><code>visible</code></li>
  <li><code>enabled</code></li>
  <li><code>foreground_color</code> or equivalent bounded presentation-facing properties depending on the realized subset</li>
</ul>

<p>
This example is therefore not a claim of full industrial UI closure.
It is a controlled proof corridor for one small but serious widget-object slice.
</p>

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
      <td><code>ui/accumulator_panel.wfrog</code> makes panel packaging and widget realization boundaries explicit.</td>
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
      <td>Most concrete published path</td>
      <td>Python currently provides the most direct bounded execution and rendered-UI corridor for this example family.</td>
    </tr>
    <tr>
      <td>Python build / run pipe</td>
      <td>Defined</td>
      <td>Entry points are published for contract execution and UI execution.</td>
    </tr>
    <tr>
      <td>Rust runtime consumer</td>
      <td>Structured and partially demonstrated</td>
      <td>A Rust runtime directory, source tree, and tests are published, but the corridor is still primarily validated through tests.</td>
    </tr>
    <tr>
      <td>Rust build / run pipe</td>
      <td>Partial</td>
      <td><code>cargo test</code> already proves bounded contract and execution parity; direct end-user example execution still needs stronger README-level closure.</td>
    </tr>
    <tr>
      <td>C/C++ runtime consumer</td>
      <td>Structured but not yet demonstrated at the same level</td>
      <td>A C/C++ runtime directory, build entry point, headers, and <code>main.cpp</code> are repository-visible, but the full example-05 A-to-Z proof remains to be documented and demonstrated.</td>
    </tr>
    <tr>
      <td>C/C++ build / run pipe</td>
      <td>Partial repository structure</td>
      <td>The repository now exposes a dedicated C/C++ mini-runtime layout, but the example-level operational closure still needs to be made explicit.</td>
    </tr>
    <tr>
      <td>Rendered front panel</td>
      <td>Partially closed</td>
      <td>A concrete Python host-rendered path exists for the bounded widget subset.</td>
    </tr>
    <tr>
      <td>LLVM-oriented native executable path</td>
      <td>Not yet closed for this example</td>
      <td>The compiler-facing direction is visible, but this example still does not publish a closed LLVM-to-native executable corridor.</td>
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
    └── Runtime/
        ├── Readme.md
        ├── accept_contract_and_execute.md
        ├── reference_runtime.py
        ├── run_slice05_contract.py
        ├── python/
        │   ├── Readme.md
        │   ├── runtime_core.py
        │   ├── execute_contract.py
        │   ├── ui_runtime.py
        │   ├── run_slice05_ui.py
        │   ├── cli.py
        │   └── tests/
        │       ├── test_slice05_contract.py
        │       └── test_slice05_ui_runtime.py
        ├── rust/
        │   ├── Readme.md
        │   ├── Cargo.toml
        │   ├── src/
        │   │   ├── main.rs
        │   │   ├── lib.rs
        │   │   ├── cli.rs
        │   │   ├── contract.rs
        │   │   ├── diagnostics.rs
        │   │   ├── runtime.rs
        │   │   ├── execute.rs
        │   │   └── ui.rs
        │   └── tests/
        │       ├── slice05_contract_smoke.rs
        │       └── slice05_execution.rs
        └── cpp/
            ├── Readme.md
            ├── CMakeLists.txt
            ├── include/
            │   ├── contract.hpp
            │   ├── runtime.hpp
            │   ├── execute.hpp
            │   └── ui.hpp
            └── src/
                └── main.cpp
</code></pre>

<hr/>

<h2 id="file-responsibilities">6. File Responsibilities</h2>

<ul>
  <li><code>Examples/05_bounded_ui_accumulator/main.frog</code><br/>
      Canonical source of the example. This remains the source of truth for program meaning.</li>

  <li><code>Examples/05_bounded_ui_accumulator/ui/accumulator_panel.wfrog</code><br/>
      Peripheral widget-oriented front-panel package. It defines panel packaging, widget realization metadata, and visual resource references without redefining executable semantics.</li>

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

  <li><code>Implementations/Reference/Runtime/reference_runtime.py</code><br/>
      Existing Python-side reference runtime realization for the already-published contract-based corridor.</li>

  <li><code>Implementations/Reference/Runtime/run_slice05_contract.py</code><br/>
      Existing Python demonstration entry point for executing the published contract artifact.</li>

  <li><code>Implementations/Reference/Runtime/python/runtime_core.py</code><br/>
      Python runtime core for the bounded reference corridor.</li>

  <li><code>Implementations/Reference/Runtime/python/execute_contract.py</code><br/>
      Python-side contract execution entry surface within the Python runtime family split.</li>

  <li><code>Implementations/Reference/Runtime/python/ui_runtime.py</code><br/>
      Concrete bounded Python UI runtime for the current widget subset of this example family.</li>

  <li><code>Implementations/Reference/Runtime/python/run_slice05_ui.py</code><br/>
      Python example runner that loads the widget package, opens a real host window, and executes the bounded UI accumulator slice.</li>

  <li><code>Implementations/Reference/Runtime/python/cli.py</code><br/>
      Python-side command-line dispatch surface for bounded runtime operations.</li>

  <li><code>Implementations/Reference/Runtime/python/tests/test_slice05_contract.py</code><br/>
      Python contract-level verification for the example corridor.</li>

  <li><code>Implementations/Reference/Runtime/python/tests/test_slice05_ui_runtime.py</code><br/>
      Python runtime verification for the bounded UI slice.</li>

  <li><code>Implementations/Reference/Runtime/rust/src/main.rs</code><br/>
      Rust-side command-line entry surface for direct runtime execution posture.</li>

  <li><code>Implementations/Reference/Runtime/rust/src/lib.rs</code><br/>
      Rust library entry surface that re-exports the runtime family.</li>

  <li><code>Implementations/Reference/Runtime/rust/src/contract.rs</code><br/>
      Rust-side contract loading and contract-shape data structures.</li>

  <li><code>Implementations/Reference/Runtime/rust/src/runtime.rs</code><br/>
      Runtime state structures and contract-consumption orchestration.</li>

  <li><code>Implementations/Reference/Runtime/rust/src/execute.rs</code><br/>
      Rust-side bounded execution logic for accepted contracts.</li>

  <li><code>Implementations/Reference/Runtime/rust/src/ui.rs</code><br/>
      Rust-side UI binding helpers for the currently supported subset.</li>

  <li><code>Implementations/Reference/Runtime/rust/tests/slice05_contract_smoke.rs</code><br/>
      Rust contract-shape validation test against the published contract artifact.</li>

  <li><code>Implementations/Reference/Runtime/rust/tests/slice05_execution.rs</code><br/>
      Rust execution test showing that the published contract produces the expected bounded result.</li>

  <li><code>Implementations/Reference/Runtime/cpp/CMakeLists.txt</code><br/>
      Build-system entry point for the C/C++ mini runtime and example consumers.</li>

  <li><code>Implementations/Reference/Runtime/cpp/include/contract.hpp</code><br/>
      Contract-loading declarations and data structures.</li>

  <li><code>Implementations/Reference/Runtime/cpp/include/runtime.hpp</code><br/>
      C/C++ runtime state declarations.</li>

  <li><code>Implementations/Reference/Runtime/cpp/include/execute.hpp</code><br/>
      Execution interface for accepted contracts.</li>

  <li><code>Implementations/Reference/Runtime/cpp/include/ui.hpp</code><br/>
      UI binding declarations for the supported subset.</li>

  <li><code>Implementations/Reference/Runtime/cpp/src/main.cpp</code><br/>
      C/C++ entry point for the mini-runtime family.</li>
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
        +------------------------------+------------------------------+------------------------------+
        |                              |                              |
        v                              v                              v
Python runtime consumer        Rust runtime consumer        C/C++ runtime consumer
        |
        \-------------------- optional LLVM-oriented native path ----/
</code></pre>

<p>
This example currently closes that corridor most concretely on the Python side.
The Rust side is structurally much more explicit than before.
The C/C++ side now has a visible repository-level mini-runtime shape, but still needs example-level proof closure.
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
  <li>and bounded object-style UI interaction through the standardized widget interaction model.</li>
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
  <li><strong>object-style interaction</strong> through <code>widget_reference</code> and standardized <code>frog.ui.*</code> primitives.</li>
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
Python currently exposes the most concrete published corridor for this example.
There are two useful Python-facing paths.
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

<h3>12.3 What the Python path currently proves</h3>

<ol>
  <li>the runtime loads the example-local <code>.wfrog</code> package,</li>
  <li>constructs concrete live widget objects for the bounded subset,</li>
  <li>supports contract-oriented execution for example 05,</li>
  <li>opens a real host window for the bounded rendered path,</li>
  <li>renders the bounded widget subset,</li>
  <li>executes the bounded accumulator logic,</li>
  <li>publishes the result into the indicator surface.</li>
</ol>

<p>
This remains a bounded runtime slice, not yet a complete industrial widget system.
</p>

<hr/>

<h2 id="rust-pipe">13. Rust Runtime Pipe</h2>

<p>
The published Rust corridor already proves downstream multi-runtime consumption and now exposes a real repository-level runtime structure rather than tests alone.
</p>

<h3>13.1 Rust verification command</h3>

<pre><code>cd Implementations/Reference/Runtime/rust
cargo test
</code></pre>

<h3>13.2 Rust posture</h3>

<ul>
  <li>the runtime family now has an explicit <code>src/</code> structure,</li>
  <li>contract loading, runtime state, execution, diagnostics, CLI, and UI helper boundaries are split into named Rust files,</li>
  <li>example 05 is still most visibly demonstrated through tests,</li>
  <li>the README-level A-to-Z closure still needs to be tightened around direct runner usage and observable rendered parity.</li>
</ul>

<h3>13.3 What this currently proves</h3>

<ul>
  <li>the published contract deserializes correctly,</li>
  <li>the expected contract shape is preserved,</li>
  <li>the example executes with the expected bounded accumulation behavior,</li>
  <li>the final result for input <code>3</code> is <code>15</code>.</li>
</ul>

<hr/>

<h2 id="cpp-pipe">14. C/C++ Runtime Pipe</h2>

<p>
The repository now publishes a real C/C++ runtime directory shape for this corridor.
That matters because the C/C++ path is no longer purely hypothetical at tree level.
</p>

<h3>14.1 Current repository-visible C/C++ posture</h3>

<ul>
  <li>a dedicated <code>cpp/</code> runtime directory exists,</li>
  <li>a dedicated <code>CMakeLists.txt</code> exists,</li>
  <li>header boundaries are published for contract loading, runtime state, execution, and UI binding,</li>
  <li>a <code>src/main.cpp</code> entry point exists.</li>
</ul>

<h3>14.2 What is still not yet closed at example level</h3>

<ul>
  <li>one explicit example-05 build command documented here,</li>
  <li>one explicit example-05 run command documented here,</li>
  <li>one demonstrated observable parity statement at the same confidence level as Python,</li>
  <li>one rendered front-panel proof path for the C/C++ family.</li>
</ul>

<p>
Accordingly, the right current statement is:
</p>

<ul>
  <li>the C/C++ runtime family is now structurally present in the published repository,</li>
  <li>but the example-05 operational A-to-Z proof remains incomplete compared with Python.</li>
</ul>

<hr/>

<h2 id="llvm-path">15. LLVM-Oriented Native Path</h2>

<p>
The example-local FIR and lowered artifacts make the compiler-facing corridor easier to close,
but this example still does not publish a closed LLVM-oriented downstream path to a native executable.
In particular, the repository does not yet expose, for this example:
</p>

<ul>
  <li>one explicit lowering-to-LLVM-family bridge artifact for example 05,</li>
  <li>one compiler-facing lowered artifact specialized for LLVM-family consumption,</li>
  <li>one native build command for this example,</li>
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
  <li>the Python rendered UI path produces the same bounded result through a real host window for the supported subset,</li>
  <li>the Rust path validates the same contract shape and confirms the same final bounded result through tests,</li>
  <li>the C/C++ path now has visible runtime scaffolding but still needs example-level proof closure,</li>
  <li>all current proof paths preserve the explicit loop-and-state reading rather than replacing it with a shortcut semantic narrative.</li>
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

<h2 id="published-gaps-still-to-close">17. Published Gaps Still To Close</h2>

<ol>
  <li>tighten the Python rendered path so that the relation between <code>.wfrog</code>, contract consumption, and rendered execution is even more explicit,</li>
  <li>document one direct Rust runner corridor as clearly as the Python one,</li>
  <li>document one real C/C++ example-05 build and run corridor,</li>
  <li>demonstrate observable example-05 parity for the C/C++ family,</li>
  <li>publish one lowering-to-LLVM-family bridge artifact for this example,</li>
  <li>publish one LLVM-oriented native build corridor,</li>
  <li>keep source, <code>.wfrog</code>, FIR, lowering, contract, and runtime-visible UI metadata aligned across the full corridor.</li>
</ol>

<hr/>

<h2 id="next-closure-target">18. Next Closure Target</h2>

<p>
The next closure target for this example is not another prose-only refinement.
It is the next concrete executable corridor extension:
</p>

<ul>
  <li>either a contract-driven rendered Python UI path with tighter end-to-end traceability,</li>
  <li>or a first fully documented C/C++ example consumer,</li>
  <li>or a first LLVM-facing native bridge for example 05.</li>
</ul>

<p>
That is the point where the example starts proving stronger downstream modularity rather than only architectural plausibility.
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
  <li>a concrete Python execution corridor,</li>
  <li>a Python rendered UI corridor,</li>
  <li>a structured Rust runtime corridor,</li>
  <li>and a structured C/C++ runtime corridor that still needs operational closure.</li>
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

multi-runtime repository structure:
yes

full multi-runtime operational closure:
not yet

native executable closure:
not yet
</code></pre>
