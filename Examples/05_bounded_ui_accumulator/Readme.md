<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Example 05 — Bounded UI Accumulator</h1>

<p align="center">
  <strong>Canonical bounded corridor from <code>.frog</code> source to UI package, FIR, lowering, runtime-family consumption, and first native LLVM proof</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goal">2. Goal</a></li>
  <li><a href="#published-corridor">3. Published Corridor</a></li>
  <li><a href="#directory-shape">4. Directory Shape</a></li>
  <li><a href="#role-of-each-published-file">5. Role of Each Published File</a></li>
  <li><a href="#downstream-contract-and-runtime-handoff">6. Downstream Contract and Runtime Handoff</a></li>
  <li><a href="#observable-example-meaning">7. Observable Example Meaning</a></li>
  <li><a href="#runtime-and-native-parity-table">8. Runtime and Native Parity Table</a></li>
  <li><a href="#python-run-posture">9. Python Run Posture</a></li>
  <li><a href="#rust-run-posture">10. Rust Run Posture</a></li>
  <li><a href="#cpp-run-posture">11. C/C++ Run Posture</a></li>
  <li><a href="#llvm-run-posture">12. LLVM Run Posture</a></li>
  <li><a href="#boundary">13. Boundary</a></li>
  <li><a href="#summary">14. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>
<p>
This example is the canonical bounded vertical slice for the current published FROG repository corridor.
It exists to make one inspectable execution path visible from canonical <code>.frog</code> source through packaged front-panel publication, FIR, lowering, backend-family handoff, runtime-family consumption, and a first narrow native LLVM proof path.
</p>

<p>
The example is intentionally small.
Its value is not breadth.
Its value is that one published meaning can be followed through several downstream consumption layers without changing the example definition itself.
</p>

<h2 id="goal">2. Goal</h2>
<p>
The goal of this example is to close one small but real corridor rather than to present a large application.
The repository uses this slice to prove that FROG is not only prose:
one published source-side example can be packaged, lowered, consumed by runtime-family implementations, and also mapped into a first native arithmetic proof corridor.
</p>

<p>
The intended repository reading posture is:
</p>

<pre><code>main.frog
  -&gt; ui/accumulator_panel.wfrog
  -&gt; main.fir.json
  -&gt; main.lowering.json
  -&gt; backend-family contract handoff
  -&gt; runtime-family consumers
  -&gt; first narrow LLVM-native proof
</code></pre>

<h2 id="published-corridor">3. Published Corridor</h2>
<p>
This example publishes the source-side and package-side artifacts directly in this directory.
It is also paired with downstream runtime-family and LLVM-family directories elsewhere in the repository.
</p>

<p>
The corridor should be read as one connected publication chain:
</p>

<ul>
  <li>canonical source publication in <code>main.frog</code>,</li>
  <li>front-panel package publication in <code>ui/accumulator_panel.wfrog</code>,</li>
  <li>execution-facing publication in <code>main.fir.json</code> and <code>main.lowering.json</code>,</li>
  <li>backend-family contract handoff for the reference runtime family,</li>
  <li>runtime-family consumption in Python, Rust, and C/C++,</li>
  <li>a separate downstream LLVM-oriented native proof corridor.</li>
</ul>

<p>
The important reading rule is that this directory owns the example-local publication corridor, while contract consumption and native proof live downstream in other repository areas.
</p>

<h2 id="directory-shape">4. Directory Shape</h2>
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
        └── numeric_indicator.svg
</code></pre>

<h2 id="role-of-each-published-file">5. Role of Each Published File</h2>
<ul>
  <li><code>main.frog</code><br/>
      Canonical source-side publication of the example. This remains the owner of executable example meaning.</li>

  <li><code>main.fir.json</code><br/>
      Execution-facing FIR publication for the same slice.</li>

  <li><code>main.lowering.json</code><br/>
      Lowered execution-facing handoff posture for downstream runtime-family and compiler-family consumers.</li>

  <li><code>ui/accumulator_panel.wfrog</code><br/>
      Published front-panel package for the example-local widget realization layer.</li>

  <li><code>ui/assets/numeric_control.svg</code><br/>
      Minimal SVG realization asset used for the numeric control publication path.</li>

  <li><code>ui/assets/numeric_indicator.svg</code><br/>
      Minimal SVG realization asset used for the numeric indicator publication path.</li>

  <li><code>front_panel.objects.json</code><br/>
      Derived host-oriented realization artifact for the same example. It is useful for host realization work, but it must be read downstream from canonical source, widget contracts, FIR, and lowering. It does not redefine executable semantics.</li>
</ul>

<h2 id="downstream-contract-and-runtime-handoff">6. Downstream Contract and Runtime Handoff</h2>
<p>
This example is paired with the following downstream reference backend-family contract artifact:
</p>

<pre><code>Implementations/Reference/ContractEmitter/examples/
└── 05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json
</code></pre>

<p>
That contract is the repository-visible handoff surface for the first named runtime family:
</p>

<pre><code>reference_host_runtime_ui_binding</code></pre>

<p>
The repository-level handoff therefore reads as:
</p>

<pre><code>canonical example source
  -&gt; published UI package
  -&gt; FIR
  -&gt; lowering
  -&gt; backend-family contract
  -&gt; runtime-family consumer
</code></pre>

<p>
The LLVM-oriented native proof corridor is also downstream, but it belongs to a compiler-family path rather than to the runtime-family definition itself.
</p>

<h2 id="observable-example-meaning">7. Observable Example Meaning</h2>
<p>
The example meaning is intentionally simple and fully inspectable:
</p>

<ul>
  <li>one numeric control provides an input value,</li>
  <li>the loop starts from zero,</li>
  <li>the loop runs exactly five iterations,</li>
  <li>each iteration adds the input value to the carried local state,</li>
  <li>the final local state is published as the public output <code>result</code>,</li>
  <li>the same final local state is also written to the numeric indicator,</li>
  <li>the bounded object-style UI surface includes one <code>foreground_color</code> write for the control and one <code>foreground_color</code> write for the indicator.</li>
</ul>

<p>
For input <code>3</code>, the expected accumulated result is <code>15</code>.
</p>

<p>
The important parity rule is that all consumer paths discussed in this document are expected to preserve the same observable example meaning even when their private realization mechanics differ.
</p>

<h2 id="runtime-and-native-parity-table">8. Runtime and Native Parity Table</h2>
<table>
  <thead>
    <tr>
      <th>Consumer path</th>
      <th>Repository-visible posture</th>
      <th>Current status</th>
      <th>Primary observable result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Python direct contract execution</td>
      <td>Published</td>
      <td>Operational for the bounded slice</td>
      <td>Input <code>3</code> produces <code>15</code></td>
    </tr>
    <tr>
      <td>Python rendered host UI</td>
      <td>Published</td>
      <td>Bounded rendered-host proof path</td>
      <td>Control and indicator state are rendered and updated for the narrow slice</td>
    </tr>
    <tr>
      <td>Rust parity verification</td>
      <td>Published</td>
      <td>Test-driven parity posture</td>
      <td>Bounded slice parity is verified through repository-visible tests</td>
    </tr>
    <tr>
      <td>C/C++ direct example runner</td>
      <td>Published</td>
      <td>Narrow direct runner posture</td>
      <td>Input <code>3</code> produces <code>15</code></td>
    </tr>
    <tr>
      <td>LLVM-native proof corridor</td>
      <td>Published</td>
      <td>First narrow native arithmetic proof</td>
      <td>Input <code>3</code> produces <code>15</code></td>
    </tr>
  </tbody>
</table>

<p>
A path may be considered repository-visible for this example even when it is still intentionally narrow and not yet a generalized implementation corridor for the full language.
</p>

<h2 id="python-run-posture">9. Python Run Posture</h2>
<p>
The Python side is the clearest operational path for the current bounded slice.
It exposes both a direct contract runner and a bounded rendered-host runner.
</p>

<pre><code>Direct contract execution
python -m Implementations.Reference.Runtime.run_slice05_contract 3
</code></pre>

<pre><code>Rendered host UI execution
python Implementations/Reference/Runtime/python/run_slice05_ui.py 3 --autorun
</code></pre>

<p>
The direct contract runner is the simplest execution-facing proof path.
The rendered UI runner is the clearest host-facing proof path for the same narrow example.
</p>

<h2 id="rust-run-posture">10. Rust Run Posture</h2>
<p>
The Rust side currently reads most strongly as a deterministic parity-verification posture for the same bounded slice.
</p>

<pre><code>cd Implementations/Reference/Runtime/rust
cargo test
</code></pre>

<p>
Its role is to prove that the same published corridor can be consumed through a second implementation language without changing the example definition.
</p>

<h2 id="cpp-run-posture">11. C/C++ Run Posture</h2>
<p>
The C/C++ side currently publishes a narrow direct example runner posture for the same bounded corridor.
</p>

<pre><code>cmake -S Implementations/Reference/Runtime/cpp -B build/frog_runtime_cpp
cmake --build build/frog_runtime_cpp
build/frog_runtime_cpp/frog_runtime_cpp_example05 3
</code></pre>

<p>
Its role is to show that the same bounded corridor can also be consumed through a third implementation language while keeping the example-local meaning unchanged.
</p>

<h2 id="llvm-run-posture">12. LLVM Run Posture</h2>
<p>
The LLVM-oriented native path is intentionally narrow.
It should be read as a first native arithmetic proof corridor for this example, not as a claim of generalized backend closure.
</p>

<pre><code>cd Implementations/Reference/LLVM/examples/05_bounded_ui_accumulator
bash build.sh
./bounded_ui_accumulator_llvm 3
</code></pre>

<p>
The important repository rule is that this native proof path is downstream from canonical source, FIR, lowering, and backend-family separation.
LLVM does not define FROG.
</p>

<h2 id="boundary">13. Boundary</h2>
<p>
This example is a canonical bounded closure slice, not the whole language.
It exists to prove corridor integrity, artifact layering, and multi-consumer portability on one small example.
</p>

<pre><code>canonical bounded slice
    !=
full language closure
</code></pre>

<pre><code>runtime-family consumer
    !=
language definition
</code></pre>

<pre><code>derived host realization
    !=
semantic authority
</code></pre>

<p>
In particular:
</p>

<ul>
  <li><code>main.frog</code> remains the source-side owner of example meaning,</li>
  <li><code>ui/accumulator_panel.wfrog</code> remains the published package-side front-panel artifact,</li>
  <li><code>front_panel.objects.json</code> remains downstream host-oriented realization material,</li>
  <li>runtime-family consumers remain downstream from lowering and backend-family handoff,</li>
  <li>the LLVM-native proof corridor remains downstream and separate from runtime-family definition.</li>
</ul>

<h2 id="summary">14. Summary</h2>
<p>
Example 05 is the canonical bounded A-to-Z closure slice for the current repository stage.
It exposes one inspectable corridor across canonical source, packaged front panel, FIR, lowering, backend-family handoff, runtime-family consumption, and a first narrow native LLVM proof.
</p>

<p>
Its value is not scale.
Its value is closure discipline:
the same bounded example meaning is published once and then consumed across several downstream paths without changing the example definition itself.
</p>
