<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Reference Runtime</h1>

<p align="center">
  <strong>First runtime-family consumer for the non-normative FROG reference implementation</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#status">2. Status</a></li>
  <li><a href="#runtime-family">3. First Runtime Family</a></li>
  <li><a href="#published-contract">4. Published Reference Contract Artifact</a></li>
  <li><a href="#owns">5. What This Directory Owns</a></li>
  <li><a href="#does-not-own">6. What This Directory Does Not Own</a></li>
  <li><a href="#design-rules">7. Design Rules</a></li>
  <li><a href="#execution-posture">8. First Execution Posture</a></li>
  <li><a href="#entry-points">9. Published Demonstration Entry Points</a></li>
  <li><a href="#closure-status">10. Runtime Closure Status</a></li>
  <li><a href="#multi-runtime">11. Multi-Runtime Posture</a></li>
  <li><a href="#next-closure">12. Next Closure Targets</a></li>
  <li><a href="#summary">13. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory contains the first runtime-side consumer of backend contracts in the non-normative FROG reference implementation.
Its role is to accept a contract for one selected backend family and realize execution privately while staying faithful to the declared contract obligations.
</p>

<p>
The runtime therefore begins downstream from canonical source, validation, semantic interpretation, FIR-target execution-facing derivation, lowering, and backend contract emission.
It consumes a published backend contract artifact.
It does not replace or absorb the layers that produced that contract.
</p>

<hr/>

<h2 id="status">2. Status</h2>

<p>
This runtime family is non-normative.
It exists to prove that the published repository corridor is no longer only prose.
It already has one repository-visible contract artifact and two repository-visible downstream consumer languages.
</p>

<p>
At the current published state, the runtime family demonstrates:
</p>

<ul>
  <li>one Python execution entry point for the published example <code>05_bounded_ui_accumulator</code>,</li>
  <li>one Rust consumer posture that validates and executes that same contract through tests,</li>
  <li>and no published C/C++ runtime consumer yet.</li>
</ul>

<hr/>

<h2 id="runtime-family">3. First Runtime Family</h2>

<p>
The first published runtime family is:
</p>

<pre><code>reference_host_runtime_ui_binding
</code></pre>

<p>
A useful initial shape is:
</p>

<ul>
  <li>single-process host execution,</li>
  <li>deterministic step-oriented execution,</li>
  <li>explicit handling of state and commit points,</li>
  <li>basic UI value and UI reference support where declared by the contract.</li>
</ul>

<p>
This first family is intentionally conservative.
It exists to prove a bounded source-to-contract-to-execution corridor, not to freeze the long-term universal runtime architecture.
</p>

<hr/>

<h2 id="published-contract">4. Published Reference Contract Artifact</h2>

<p>
The first named executable slice has a repository-visible backend contract artifact:
</p>

<pre><code>Implementations/Reference/ContractEmitter/examples/
└── 05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json
</code></pre>

<p>
That artifact is the published handoff surface this runtime family consumes for the bounded applicative vertical slice:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/
</code></pre>

<p>
This matters because the runtime is no longer aligned only with a prose description of the contract boundary.
It aligns with one concrete repository-visible contract artifact that preserves:
</p>

<ul>
  <li>the bounded loop requirement,</li>
  <li>the explicit state requirement,</li>
  <li>the deterministic initial value,</li>
  <li>the control input binding,</li>
  <li>the indicator publication path,</li>
  <li>the public output publication path,</li>
  <li>and the minimal object-style UI write surface for <code>face_color</code>.</li>
</ul>

<hr/>

<h2 id="owns">5. What This Directory Owns</h2>

<ul>
  <li>private execution realization of accepted backend contracts,</li>
  <li>state management for the reference family,</li>
  <li>family-specific runtime objects,</li>
  <li>family-specific scheduling mechanics,</li>
  <li>runtime-private UI binding helpers for the accepted subset,</li>
  <li>and runtime-private success / failure reporting.</li>
</ul>

<hr/>

<h2 id="does-not-own">6. What This Directory Does Not Own</h2>

<ul>
  <li>the language,</li>
  <li>the canonical <code>.frog</code> source model,</li>
  <li>the semantic acceptance boundary,</li>
  <li>the open FIR / execution-facing layer,</li>
  <li>the lowering boundary,</li>
  <li>the backend contract boundary,</li>
  <li>the normative meaning of UI constructs,</li>
  <li>the structural-validation boundary,</li>
  <li>or the semantic-acceptance boundary.</li>
</ul>

<p>
The architectural rule remains:
</p>

<pre><code>validated meaning != runtime implementation
backend contract != runtime-private structures
reference runtime != universal FROG runtime
</code></pre>

<hr/>

<h2 id="design-rules">7. Design Rules</h2>

<ul>
  <li>Accept or reject contracts explicitly.</li>
  <li>Do not silently reinterpret undeclared assumptions.</li>
  <li>Preserve explicit local-memory meaning where required.</li>
  <li>Preserve source-aligned attribution where the contract claims support for it.</li>
  <li>Reject unsupported runtime obligations explicitly.</li>
  <li>Keep <code>widget_value</code> handling and <code>widget_reference</code> handling distinguishable where the contract distinguishes them.</li>
  <li>Do not promote runtime-private convenience into normative language law.</li>
</ul>

<hr/>

<h2 id="execution-posture">8. First Execution Posture</h2>

<p>
The first execution posture is intentionally bounded.
It is designed for the first named applicative vertical slice, not for the full future FROG runtime surface.
</p>

<p>
The current bounded corridor already supports:
</p>

<ul>
  <li>one public input value sampled from the control binding,</li>
  <li>one bounded loop of exactly five iterations,</li>
  <li>one explicit state cell initialized to zero,</li>
  <li>one final public result publication,</li>
  <li>one indicator publication path,</li>
  <li>and minimal object-style UI property writes for <code>face_color</code>.</li>
</ul>

<p>
This first execution posture does not require continuous event-driven UI behavior, hidden persistence between runs, or a broad widget object model.
</p>

<hr/>

<h2 id="entry-points">9. Published Demonstration Entry Points</h2>

<p>
This directory already contains repository-visible entry points that exercise the published contract artifact directly rather than through a private simplified schema.
</p>

<pre><code>Implementations/Reference/Runtime/
├── reference_runtime.py
├── run_slice05_contract.py
└── rust/
    └── tests/
        ├── slice05_contract_smoke.rs
        └── slice05_execution.rs
</code></pre>

<p>
The Python entry point:
</p>

<pre><code>python -m Implementations.Reference.Runtime.run_slice05_contract 3
</code></pre>

<p>
loads the published contract artifact for <code>05_bounded_ui_accumulator</code>, binds a sampled control value, executes the bounded accumulation corridor, and prints the resulting runtime artifact.
</p>

<p>
The Rust tests serve two complementary purposes:
</p>

<ul>
  <li><code>slice05_contract_smoke.rs</code> verifies that the published contract artifact deserializes and exposes the expected bounded slice shape,</li>
  <li><code>slice05_execution.rs</code> verifies that the runtime executes the published contract artifact and produces the expected final result.</li>
</ul>

<hr/>

<h2 id="closure-status">10. Runtime Closure Status</h2>

<table>
  <thead>
    <tr>
      <th>Runtime family surface</th>
      <th>Status</th>
      <th>Published posture</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Family definition posture</td>
      <td>Closed enough for the first slice</td>
      <td><code>reference_host_runtime_ui_binding</code> is explicit.</td>
    </tr>
    <tr>
      <td>Python consumer</td>
      <td>Closed</td>
      <td>Runnable entry point is published.</td>
    </tr>
    <tr>
      <td>Rust consumer</td>
      <td>Partial-to-closed</td>
      <td>Execution proof exists through tests, but not yet through one dedicated example runner binary.</td>
    </tr>
    <tr>
      <td>C/C++ consumer</td>
      <td>Missing</td>
      <td>No published consumer exists yet.</td>
    </tr>
    <tr>
      <td>Rendered host UI</td>
      <td>Missing</td>
      <td>UI runtime state is exposed in output artifacts, but no rendered host UI exists yet.</td>
    </tr>
    <tr>
      <td>LLVM-oriented native path</td>
      <td>Missing</td>
      <td>No runtime-family native executable corridor is published here yet.</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="multi-runtime">11. Multi-Runtime Posture</h2>

<p>
This directory defines a runtime-family boundary, not a single mandatory runtime language.
</p>

<p>
Where the reference implementation publishes multiple runtime realizations, such as:
</p>

<ul>
  <li>a Python realization,</li>
  <li>a Rust realization,</li>
  <li>and later a C/C++ realization,</li>
</ul>

<p>
those runtimes must be understood as parallel consumers of the same published corridor.
They may differ in private structures and host mechanics, but they should remain aligned on:
</p>

<ul>
  <li>contract acceptance criteria,</li>
  <li>explicit-state meaning,</li>
  <li>bounded loop meaning,</li>
  <li>UI binding obligations declared by the contract,</li>
  <li>and public result publication obligations.</li>
</ul>

<hr/>

<h2 id="next-closure">12. Next Closure Targets</h2>

<ol>
  <li>publish one explicit C/C++ consumer for the same example corridor,</li>
  <li>publish one dedicated Rust runner command in addition to the tests,</li>
  <li>publish one distinct peripheral UI object realization file,</li>
  <li>publish one rendered front-panel host path,</li>
  <li>and publish one LLVM-oriented native executable corridor for declared native examples.</li>
</ol>

<hr/>

<h2 id="summary">13. Summary</h2>

<p>
The reference runtime is the first private consumer-side realization of the reference backend family.
It proves executability, but it does not become the language definition.
</p>

<p>
At the current published state, the runtime family already supports one real Python execution path and one real Rust consumer posture for the same named example corridor.
What is still missing is the third runtime language, a rendered host UI, and a native LLVM-oriented executable closure.
</p>
