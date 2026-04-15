<p align="center">
  <img src="../../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">LLVM Closure Example — 05 Bounded UI Accumulator</h1>

<p align="center">
  <strong>First native LLVM corridor for the canonical bounded UI accumulator slice</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#published-files">2. Published Files</a></li>
  <li><a href="#goal">3. Goal</a></li>
  <li><a href="#scope">4. Scope</a></li>
  <li><a href="#run-posture">5. Run Posture</a></li>
  <li><a href="#expected-observable-result">6. Expected Observable Result</a></li>
  <li><a href="#boundary">7. Boundary</a></li>
  <li><a href="#summary">8. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>
<p>
This directory publishes the first LLVM-native closure material for the canonical <code>05_bounded_ui_accumulator</code> example. Its role is not to define a general-purpose LLVM backend. Its role is to make the first native corridor repository-visible and executable.
</p>

<h2 id="published-files">2. Published Files</h2>
<pre><code>Implementations/Reference/LLVM/examples/05_bounded_ui_accumulator/
├── Readme.md
├── main.fir.json
├── main.lowering.json
├── module.ll
├── build.sh
└── expected-output.json
</code></pre>

<h2 id="goal">3. Goal</h2>
<p>
The goal of this directory is to prove that the same canonical example corridor can be expressed as a first native LLVM artifact without changing the meaning of the example.
</p>
<p>
The first observable proof target is intentionally narrow:
</p>
<ul>
  <li>accept one bounded accumulator input value,</li>
  <li>run five deterministic iterations,</li>
  <li>publish the final bounded accumulated value,</li>
  <li>match the same observable output posture as the Python, Rust, and C/C++ consumers for the same example.</li>
</ul>

<h2 id="scope">4. Scope</h2>
<p>
This first LLVM closure stays deliberately small:
</p>
<ul>
  <li>one function-level accumulator kernel,</li>
  <li>one example-specific run posture,</li>
  <li>no claim of general backend completeness,</li>
  <li>no claim of full widget-host rendering closure,</li>
  <li>no claim of full FIR-to-LLVM automatic lowering coverage.</li>
</ul>

<h2 id="run-posture">5. Run Posture</h2>
<pre><code>cd Implementations/Reference/LLVM/examples/05_bounded_ui_accumulator
bash build.sh
./bounded_ui_accumulator_llvm 3
</code></pre>
<p>
The current native run posture prints the final value for the bounded accumulator kernel. For input <code>3</code>, the expected final value is <code>15</code>.
</p>

<h2 id="expected-observable-result">6. Expected Observable Result</h2>
<p>
For input <code>3</code>, the expected observable result is:
</p>
<pre><code>final_state=15
public_output=15
status=ok
</code></pre>

<h2 id="boundary">7. Boundary</h2>
<p>
This directory is downstream from canonical source, downstream from FIR, downstream from lowering, and downstream from runtime-family discussion. It is a native proof corridor, not a language-definition directory.
</p>
<p>
The important reading rule is:
</p>
<pre><code>first native example closure
    !=
fully generalized production LLVM backend
</code></pre>

<h2 id="summary">8. Summary</h2>
<p>
This directory publishes the first executable LLVM-native closure for the canonical bounded UI accumulator slice. It is intentionally narrow, but it makes the native backend direction repository-visible and operational for the first example corridor.
</p>
