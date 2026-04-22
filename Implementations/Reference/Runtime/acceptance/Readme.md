<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Reference Runtime Acceptance Artifacts</h1>

<p align="center">
  <strong>Shared non-normative acceptance material for the Example 05 runtime-family closure</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Navigation</h2>

<ul>
  <li><a href="../Readme.md">Runtime-family parent</a></li>
  <li><a href="../../../Examples/05_bounded_ui_accumulator/Readme.md">Example 05 corridor</a></li>
  <li><a href="../../../Implementations/Reference/ContractEmitter/Readme.md">ContractEmitter</a></li>
  <li><a href="./example05_runtime_family.acceptance.json"><code>example05_runtime_family.acceptance.json</code></a></li>
  <li><a href="./example05_input_3.snapshot.json"><code>example05_input_3.snapshot.json</code></a></li>
</ul>

<hr/>

<h2>Overview</h2>

<p>
This directory publishes the shared acceptance artifacts used to keep the Python, Rust, and C/C++ reference runtimes aligned on the same Example 05 corridor.
</p>

<p>
These files are intentionally non-normative.
They do not define FROG semantics.
They define the shared acceptance posture for the current published runtime-family slice.
</p>

<hr/>

<h2>Published artifacts</h2>

<ul>
  <li><code>example05_runtime_family.acceptance.json</code> — shared runtime-family acceptance description for Example 05.</li>
  <li><code>example05_input_3.snapshot.json</code> — expected execution result and UI state after running the slice with input value <code>3</code>.</li>
</ul>

<hr/>

<h2>Why this directory exists</h2>

<p>
The runtime-family closure is only credible if the three published reference runtimes are checked against the same observable facts:
</p>

<ul>
  <li>the same contract artifact,</li>
  <li>the same <code>.wfrog</code> package,</li>
  <li>the same browser-host routes,</li>
  <li>the same runtime snapshot after input <code>3</code>,</li>
  <li>the same overflow rejection message for the shared bounded slice.</li>
</ul>

<p>
These files give the tests one common target instead of letting each runtime drift toward a slightly different local proof.
</p>

<hr/>

<h2>Ownership boundary</h2>

<ul>
  <li>canonical source remains owned by <code>Examples/05_bounded_ui_accumulator/main.frog</code>,</li>
  <li>execution-facing artifacts remain owned by the published FIR and lowering,</li>
  <li>runtime handoff remains owned by the emitted backend contract,</li>
  <li>this directory only owns the non-normative shared acceptance posture for the reference runtime family.</li>
</ul>

<hr/>

<h2>Summary</h2>

<p>
Use this directory to keep the three reference runtimes aligned on one observable Example 05 closure.
Do not use it as a replacement for source, FIR, lowering, widget law, or runtime-family contract ownership.
</p>
