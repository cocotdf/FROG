<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Reference Runtime</h1>

<p align="center">
  <strong>First consumer/runtime family for the non-normative FROG reference implementation</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#non-normative-status">2. Non-Normative Status</a></li>
  <li><a href="#first-runtime-family">3. First Runtime Family</a></li>
  <li><a href="#published-reference-contract-artifact">4. Published Reference Contract Artifact</a></li>
  <li><a href="#what-this-directory-owns">5. What This Directory Owns</a></li>
  <li><a href="#what-this-directory-does-not-own">6. What This Directory Does Not Own</a></li>
  <li><a href="#design-rules">7. Design Rules</a></li>
  <li><a href="#first-execution-posture">8. First Execution Posture</a></li>
  <li><a href="#minimal-demonstration-entry-points">9. Minimal Demonstration Entry Points</a></li>
  <li><a href="#multi-runtime-posture">10. Multi-Runtime Posture</a></li>
  <li><a href="#summary">11. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory contains the first runtime-side consumer of backend contracts in the reference implementation.
Its role is to accept a contract for the selected backend family and realize execution privately while staying faithful to the declared contract obligations.
</p>

<p>
The runtime therefore begins <strong>downstream</strong> from canonical source, validation, semantic interpretation, Execution IR, and lowering.
It consumes a published backend contract artifact.
It does not replace or absorb the layers that produced that contract.
</p>

<hr/>

<h2 id="non-normative-status">2. Non-Normative Status</h2>

<p>
This runtime is not the universal FROG runtime.
It is one reference-family realization used to prove that the published boundaries can support an executable slice.
</p>

<p>
Its role is demonstrative and implementation-facing.
It helps prove that the repository-visible corridor can already be consumed and executed,
but it does not become the normative definition of the language, the Execution IR, or the backend contract boundary.
</p>

<hr/>

<h2 id="first-runtime-family">3. First Runtime Family</h2>

<p>
The recommended first family is:
</p>

<pre><code>reference_host_runtime_ui_binding</code></pre>

<p>
A useful initial shape is:
</p>

<ul>
  <li>single process,</li>
  <li>host runtime,</li>
  <li>deterministic step-oriented execution,</li>
  <li>explicit handling of state and commit points,</li>
  <li>basic UI value and UI reference support where declared by the contract.</li>
</ul>

<p>
This first family is intentionally conservative.
It exists to prove a bounded source-to-contract-to-execution corridor, not to freeze the long-term universal runtime architecture.
</p>

<hr/>

<h2 id="published-reference-contract-artifact">4. Published Reference Contract Artifact</h2>

<p>
The first named executable slice now has a repository-visible backend contract artifact:
</p>

<pre><code>Implementations/Reference/ContractEmitter/examples/
└── 05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json</code></pre>

<p>
That artifact is the first published handoff surface this runtime family is expected to consume for the bounded applicative vertical slice:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/</code></pre>

<p>
This matters because the runtime is no longer aligned only with a prose description of the contract boundary.
It can now align with a concrete repository-visible contract artifact that preserves:
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

<h2 id="what-this-directory-owns">5. What This Directory Owns</h2>

<ul>
  <li>private execution realization of accepted backend contracts,</li>
  <li>state management for the reference family,</li>
  <li>family-specific runtime objects,</li>
  <li>family-specific scheduling mechanics,</li>
  <li>runtime-private UI binding helpers for the accepted subset,</li>
  <li>and runtime-private success / failure reporting.</li>
</ul>

<hr/>

<h2 id="what-this-directory-does-not-own">6. What This Directory Does Not Own</h2>

<ul>
  <li>the language,</li>
  <li>the open Execution IR,</li>
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
reference runtime != universal FROG runtime</code></pre>

<hr/>

<h2 id="design-rules">7. Design Rules</h2>

<ul>
  <li>Accept or reject contracts explicitly.</li>
  <li>Do not silently reinterpret undeclared assumptions.</li>
  <li>Preserve explicit local-memory meaning where required.</li>
  <li>Preserve source-aligned attribution where the contract claims support for it.</li>
  <li>Reject unsupported runtime obligations explicitly.</li>
  <li>Keep widget-value handling and widget-reference handling distinguishable where the contract distinguishes them.</li>
  <li>Do not promote runtime-private convenience into normative language law.</li>
</ul>

<hr/>

<h2 id="first-execution-posture">8. First Execution Posture</h2>

<p>
For the first named applicative slice, a conservative execution posture is:
</p>

<ol>
  <li>load the published backend contract artifact,</li>
  <li>confirm backend-family compatibility,</li>
  <li>confirm the supported execution assumptions,</li>
  <li>prepare one host-side execution unit,</li>
  <li>bind the sampled numeric control value,</li>
  <li>apply the declared <code>face_color</code> property writes,</li>
  <li>initialize explicit state to <code>0</code>,</li>
  <li>execute five deterministic accumulation iterations,</li>
  <li>publish the final value to the indicator,</li>
  <li>publish the same final value to the public output surface,</li>
  <li>and report explicit success or explicit failure.</li>
</ol>

<p>
This first execution posture is bounded on purpose.
It does not require continuous event-driven UI behavior, hidden persistence between runs, or a broad object-model implementation.
</p>

<hr/>

<h2 id="minimal-demonstration-entry-points">9. Minimal Demonstration Entry Points</h2>

<p>
This directory also contains minimal reference-facing entry points that exercise the published contract artifact directly rather than through a private simplified schema.
</p>

<p>
The intended first bounded demonstration surfaces are:
</p>

<pre><code>Implementations/Reference/Runtime/
├── reference_runtime.py
├── run_slice05_contract.py
└── rust/
    └── tests/
        ├── slice05_contract_smoke.rs
        └── slice05_execution.rs</code></pre>

<p>
The Python entry point:
</p>

<pre><code>run_slice05_contract.py</code></pre>

<p>
loads the published contract artifact for <code>05_bounded_ui_accumulator</code>,
binds a sampled control value,
executes the bounded accumulation corridor,
and prints the resulting runtime artifact.
</p>

<p>
The Rust tests serve two complementary purposes:
</p>

<ul>
  <li><code>slice05_contract_smoke.rs</code> verifies that the published contract artifact deserializes and exposes the expected bounded slice shape,</li>
  <li><code>slice05_execution.rs</code> verifies that the runtime executes the published contract artifact and produces the expected final result.</li>
</ul>

<p>
These entry points do not make the runtime normative.
They make the first published contract-to-runtime demonstration materially inspectable.
</p>

<hr/>

<h2 id="multi-runtime-posture">10. Multi-Runtime Posture</h2>

<p>
This directory defines a runtime family boundary, not a single mandatory runtime language.
</p>

<p>
Where the reference implementation publishes multiple runtime realizations, such as:
</p>

<ul>
  <li>a Python realization,</li>
  <li>a Rust realization,</li>
  <li>and possibly later other realizations,</li>
</ul>

<p>
those runtimes must be understood as parallel consumers of the same published corridor.
They may differ in private structures and host mechanics,
but they should remain aligned on:
</p>

<ul>
  <li>contract acceptance criteria,</li>
  <li>explicit-state meaning,</li>
  <li>bounded loop meaning,</li>
  <li>UI binding obligations declared by the contract,</li>
  <li>and public result publication obligations.</li>
</ul>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
The reference runtime is the first private consumer-side realization of the reference backend family.
It proves executability,
but it does not become the language definition.
</p>

<p>
It now aligns explicitly with a repository-visible backend contract artifact for the first named applicative vertical slice.
That makes the runtime boundary more concrete:
the contract is visible,
the consumer is visible,
and the ownership boundary between them remains explicit.
</p>

<p>
The first bounded demonstration is now intended to be readable directly from the published contract artifact to Python and Rust reference-family consumers.
</p>
