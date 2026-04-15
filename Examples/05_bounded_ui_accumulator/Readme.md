<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Example 05 — Bounded UI Accumulator</h1>

<p align="center">
  <strong>Canonical A-to-Z closure slice for source, FIR, runtime-family consumption, and first native LLVM proof</strong><br/>
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
  <li><a href="#observable-example-meaning">6. Observable Example Meaning</a></li>
  <li><a href="#runtime-and-native-parity-table">7. Runtime and Native Parity Table</a></li>
  <li><a href="#python-run-posture">8. Python Run Posture</a></li>
  <li><a href="#rust-run-posture">9. Rust Run Posture</a></li>
  <li><a href="#cpp-run-posture">10. C/C++ Run Posture</a></li>
  <li><a href="#llvm-run-posture">11. LLVM Run Posture</a></li>
  <li><a href="#boundary">12. Boundary</a></li>
  <li><a href="#summary">13. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>
<p>
This example is the canonical vertical closure slice for the early FROG repository. It exists to make one complete corridor visible from source posture through UI packaging, FIR, lowering, runtime-family consumption, and a first native LLVM proof path.
</p>

<h2 id="goal">2. Goal</h2>
<p>
The goal of this example is not to show a large application. The goal is to show a small but complete and inspectable corridor that multiple implementation languages can consume without changing the definition of the example.
</p>
<p>
The published closure target for this example is:
</p>
<pre><code>main.frog
  -&gt; accumulator_panel.wfrog
  -&gt; main.fir.json
  -&gt; main.lowering.json
  -&gt; reference runtime-family contract posture
  -&gt; Python consumer
  -&gt; Rust consumer
  -&gt; C/C++ consumer
  -&gt; first LLVM-native proof corridor
</code></pre>

<p>
This example is intentionally narrow.
Its role is to prove corridor integrity, layering discipline, and cross-language consumer portability on one small but fully inspectable slice.
</p>

<h2 id="published-corridor">3. Published Corridor</h2>
<p>
The example publishes the source-side and package-side artifacts directly in this directory, and it is paired with the runtime-family and LLVM directories for downstream consumption.
</p>

<p>
The corridor should be read as one connected publication chain rather than as isolated files:
</p>

<ul>
  <li>source publication in <code>main.frog</code>,</li>
  <li>front-panel package publication in <code>ui/accumulator_panel.wfrog</code>,</li>
  <li>execution-facing publication in <code>main.fir.json</code> and <code>main.lowering.json</code>,</li>
  <li>consumer-side interpretation in Python, Rust, and C/C++,</li>
  <li>first native arithmetic closure in the LLVM proof path.</li>
</ul>

<h2 id="directory-shape">4. Directory Shape</h2>
<pre><code>Examples/05_bounded_ui_accumulator/
├── Readme.md
├── main.frog
├── main.fir.json
├── main.lowering.json
├── ui/
│   ├── accumulator_panel.wfrog
│   └── assets/
│       └── default/
│           ├── button.svg
│           ├── numeric_control.svg
│           └── numeric_indicator.svg
</code></pre>

<h2 id="role-of-each-published-file">5. Role of Each Published File</h2>
<ul>
  <li><code>main.frog</code>: canonical source-side example posture.</li>
  <li><code>main.fir.json</code>: first repository-visible FIR posture for the example.</li>
  <li><code>main.lowering.json</code>: first repository-visible lowering posture for downstream consumers.</li>
  <li><code>ui/accumulator_panel.wfrog</code>: packaged front-panel-side posture for the example.</li>
  <li><code>ui/assets/default/*</code>: minimal default-family realization assets used by rendered-host and UI packaging work.</li>
</ul>

<h2 id="observable-example-meaning">6. Observable Example Meaning</h2>
<p>
The example meaning is intentionally simple:
</p>
<ul>
  <li>one numeric control provides an input value,</li>
  <li>the loop starts from zero,</li>
  <li>the loop runs exactly five iterations,</li>
  <li>each iteration adds the input value to the local state,</li>
  <li>the final local state is published both as public output and as indicator value,</li>
  <li>the minimal UI property-write surface includes one <code>foreground_color</code> write on the indicator path.</li>
</ul>
<p>
For input <code>3</code>, the expected result is <code>15</code>.
</p>

<p>
The important parity rule is that all consumer paths discussed in this example are expected to preserve the same observable example meaning even when their implementation posture differs.
</p>

<h2 id="runtime-and-native-parity-table">7. Runtime and Native Parity Table</h2>
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
      <td>Python runtime CLI</td>
      <td>Published</td>
      <td>Closed</td>
      <td>Input <code>3</code> produces <code>15</code></td>
    </tr>
    <tr>
      <td>Python rendered host UI</td>
      <td>Published</td>
      <td>Closed for the narrow example subset</td>
      <td>Control and indicator state are rendered and updated</td>
    </tr>
    <tr>
      <td>Rust runtime parity</td>
      <td>Published</td>
      <td>Closed through repository-visible test posture</td>
      <td>Example parity for the bounded slice is verified</td>
    </tr>
    <tr>
      <td>C/C++ runtime parity</td>
      <td>Published</td>
      <td>Closed for the narrow example runner posture</td>
      <td>Input <code>3</code> produces <code>15</code></td>
    </tr>
    <tr>
      <td>LLVM-native proof corridor</td>
      <td>Published</td>
      <td>Closed for the first native arithmetic proof slice</td>
      <td>Input <code>3</code> produces <code>15</code></td>
    </tr>
  </tbody>
</table>

<p>
The reading rule for this table is strict:
a path may be considered closed for this example even if it is not yet a generalized implementation corridor for the full language.
</p>

<h2 id="python-run-posture">8. Python Run Posture</h2>
<pre><code>python Implementations/Reference/Runtime/python/run_example05.py 3
</code></pre>
<p>
The Python path is the most feature-complete early host consumer and remains the clearest rendered-host demonstration path for this example.
</p>

<h2 id="rust-run-posture">9. Rust Run Posture</h2>
<pre><code>cargo test -p frog-runtime-rust --test slice05_execution -- --nocapture
</code></pre>
<p>
The Rust path publishes deterministic parity evidence for the same bounded slice.
</p>

<h2 id="cpp-run-posture">10. C/C++ Run Posture</h2>
<pre><code>cmake -S Implementations/Reference/Runtime/cpp -B build/frog_runtime_cpp
cmake --build build/frog_runtime_cpp
build/frog_runtime_cpp/frog_runtime_cpp_example05 3
</code></pre>
<p>
The C/C++ path is intentionally narrow. Its purpose is to prove that the same corridor can be consumed through a third implementation language without changing the example definition.
</p>

<h2 id="llvm-run-posture">11. LLVM Run Posture</h2>
<pre><code>cd Implementations/Reference/LLVM/examples/05_bounded_ui_accumulator
bash build.sh
./bounded_ui_accumulator_llvm 3
</code></pre>
<p>
The LLVM-native path is also intentionally narrow. It is a first native proof corridor, not a claim of generalized backend closure.
</p>

<h2 id="boundary">12. Boundary</h2>
<p>
This example is a closure slice, not the whole language. It exists to prove corridor integrity, artifact layering, and runtime-family portability on one bounded example.
</p>
<p>
The important reading rule is:
</p>
<pre><code>canonical vertical slice
    !=
full language closure
</code></pre>

<p>
Likewise:
</p>
<pre><code>closed example corridor
    !=
fully generalized backend family
</code></pre>

<h2 id="summary">13. Summary</h2>
<p>
Example 05 is the canonical A-to-Z closure slice for the current FROG repository stage. It now exposes one inspectable example corridor across source, packaged front panel, FIR, lowering, Python runtime, Rust runtime, C/C++ runtime, and a first LLVM-native proof path.
</p>

<p>
Its value is not scale but closure:
the same bounded example meaning can now be published once and consumed across several implementation paths without changing the example definition itself.
</p>
