<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Reference Implementation Workspace</h1>

<p align="center">
  <strong>Non-normative executable workspace for inspecting and exercising the published FROG corridor from source to contract to runtime consumption</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#non-normative-status">2. Non-Normative Status</a></li>
  <li><a href="#why-this-directory-exists">3. Why This Directory Exists</a></li>
  <li><a href="#architectural-position">4. Architectural Position</a></li>
  <li><a href="#published-workspace-shape">5. Published Workspace Shape</a></li>
  <li><a href="#first-bounded-executable-corridor">6. First Bounded Executable Corridor</a></li>
  <li><a href="#what-this-workspace-owns">7. What This Workspace Owns</a></li>
  <li><a href="#what-this-workspace-does-not-own">8. What This Workspace Does Not Own</a></li>
  <li><a href="#stage-separation-discipline">9. Stage-Separation Discipline</a></li>
  <li><a href="#example-contract-runtime-reading">10. Example → Contract → Runtime Reading</a></li>
  <li><a href="#multi-runtime-posture">11. Multi-Runtime Posture</a></li>
  <li><a href="#design-rules">12. Design Rules</a></li>
  <li><a href="#summary">13. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory contains the non-normative reference implementation workspace for FROG.
It exists to make selected repository-visible corridors executable and inspectable without turning implementation convenience into normative language law.
</p>

<p>
The workspace is intentionally stage-separated.
It is not a monolithic hidden compiler/runtime product.
It is a repository-visible execution workspace that consumes the published specification layers through explicit intermediate boundaries.
</p>

<hr/>

<h2 id="non-normative-status">2. Non-Normative Status</h2>

<p>
This workspace is <strong>non-normative</strong>.
It is not the definition of FROG.
It is not the owner of source law, semantic law, Execution IR law, or backend-contract law.
</p>

<p>
Its role is to demonstrate that the published repository can already support bounded executable corridors through inspectable reference-family components.
</p>

<p>
The architectural rule remains:
</p>

<pre><code>published specification layers
   -&gt; define and bound meaning

reference implementation workspace
   -&gt; consumes those layers without owning them</code></pre>

<hr/>

<h2 id="why-this-directory-exists">3. Why This Directory Exists</h2>

<p>
A serious open language repository should be able to expose more than prose-only architecture.
It should also be able to show that at least one bounded slice can be carried through executable downstream stages without collapsing the language into one private implementation.
</p>

<p>
This workspace therefore exists to:
</p>

<ul>
  <li>load canonical source artifacts where relevant,</li>
  <li>exercise structural and semantic checks in reference form where relevant,</li>
  <li>derive or consume execution-facing representations in reference form,</li>
  <li>lower into backend-facing reference-family forms,</li>
  <li>emit consumer-facing backend contracts,</li>
  <li>and execute selected bounded slices through explicit runtime consumers.</li>
</ul>

<p>
It is a proof workspace for repository-visible corridor closure, not a replacement for the specification.
</p>

<hr/>

<h2 id="architectural-position">4. Architectural Position</h2>

<pre><code>canonical .frog source
      |
      v
published structural + semantic boundaries
      |
      v
published Execution IR posture
      |
      v
published lowering posture
      |
      v
reference implementation stages
      |
      +-- Loader/
      +-- Validator/
      +-- Deriver/
      +-- Lowerer/
      +-- ContractEmitter/
      +-- Runtime/
      +-- UIHost/
      \-- CLI/</code></pre>

<p>
The key rule is that this workspace follows the published corridor.
It does not silently replace it.
</p>

<hr/>

<h2 id="published-workspace-shape">5. Published Workspace Shape</h2>

<p>
The reference workspace is organized as explicit stage-separated areas, including:
</p>

<ul>
  <li><code>Loader/</code></li>
  <li><code>Validator/</code></li>
  <li><code>Deriver/</code></li>
  <li><code>Lowerer/</code></li>
  <li><code>ContractEmitter/</code></li>
  <li><code>Runtime/</code></li>
  <li><code>UIHost/</code></li>
  <li><code>CLI/</code></li>
</ul>

<p>
That separation matters.
It keeps the executable corridor inspectable and prevents backend emission, runtime realization, and host integration from collapsing into one hidden implementation blob.
</p>

<hr/>

<h2 id="first-bounded-executable-corridor">6. First Bounded Executable Corridor</h2>

<p>
The first repository-visible bounded executable corridor is centered on:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/</code></pre>

<p>
That named example is the first small applicative vertical slice that visibly combines:
</p>

<ul>
  <li>front-panel participation,</li>
  <li>widget-value participation,</li>
  <li>minimal widget-reference participation,</li>
  <li>bounded structured control,</li>
  <li>explicit local state,</li>
  <li>public output publication,</li>
  <li>and a first published runtime-consumption posture.</li>
</ul>

<p>
The corresponding repository-visible reference-family backend contract artifact is:
</p>

<pre><code>Implementations/Reference/ContractEmitter/examples/
└── 05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json</code></pre>

<p>
That contract is then consumed downstream by the reference runtime family under:
</p>

<pre><code>Implementations/Reference/Runtime/</code></pre>

<p>
This makes the first bounded executable corridor inspectable as:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/
      |
      v
Implementations/Reference/ContractEmitter/examples/
05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json
      |
      v
Implementations/Reference/Runtime/</code></pre>

<hr/>

<h2 id="what-this-workspace-owns">7. What This Workspace Owns</h2>

<ul>
  <li>reference-family executable staging,</li>
  <li>reference-family loading, validation, derivation, lowering, and contract-emission mechanics where implemented,</li>
  <li>reference-family runtime consumption of accepted backend contracts,</li>
  <li>reference-family host/UI binding helpers where the bounded corridor requires them,</li>
  <li>and repository-visible executable artifacts used to exercise selected named slices.</li>
</ul>

<hr/>

<h2 id="what-this-workspace-does-not-own">8. What This Workspace Does Not Own</h2>

<ul>
  <li>the canonical <code>.frog</code> source model,</li>
  <li>the normative structural-validation boundary,</li>
  <li>the normative semantic-acceptance boundary,</li>
  <li>the normative Execution IR boundary,</li>
  <li>the normative backend-contract boundary,</li>
  <li>the universal runtime architecture for all future implementations,</li>
  <li>or the universal UI toolkit/object model for all future hosts.</li>
</ul>

<p>
In particular:
</p>

<pre><code>example source != emitted contract
emitted contract != runtime-private realization
reference runtime != universal FROG runtime</code></pre>

<hr/>

<h2 id="stage-separation-discipline">9. Stage-Separation Discipline</h2>

<p>
Each stage in this workspace should remain explicit about its ownership boundary.
</p>

<ul>
  <li><strong>Loader</strong> handles loading concerns.</li>
  <li><strong>Validator</strong> handles reference checking against the supported corridor.</li>
  <li><strong>Deriver</strong> handles execution-facing derivation work in reference form.</li>
  <li><strong>Lowerer</strong> handles backend-family-oriented specialization.</li>
  <li><strong>ContractEmitter</strong> materializes backend contract artifacts.</li>
  <li><strong>Runtime</strong> privately consumes accepted contract artifacts.</li>
  <li><strong>UIHost</strong> handles host-facing UI realization where applicable.</li>
  <li><strong>CLI</strong> provides bounded entry surfaces for inspection and exercise.</li>
</ul>

<p>
That separation keeps the corridor attributable.
It also makes it easier to inspect where a failure belongs:
</p>

<ul>
  <li>source problem,</li>
  <li>validation problem,</li>
  <li>derivation problem,</li>
  <li>lowering problem,</li>
  <li>contract-emission problem,</li>
  <li>or runtime-consumption problem.</li>
</ul>

<hr/>

<h2 id="example-contract-runtime-reading">10. Example → Contract → Runtime Reading</h2>

<p>
For the first bounded executable slice, the recommended reading order is:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/
      |
      v
Implementations/Reference/ContractEmitter/examples/
05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json
      |
      v
Implementations/Reference/Runtime/
      |
      +-- reference_runtime.py
      \-- rust/</code></pre>

<p>
This reading order matters because it preserves the ownership chain:
</p>

<ul>
  <li>the example exposes the named source-level and corridor-level slice,</li>
  <li>the emitted contract exposes the reference-family backend handoff,</li>
  <li>the runtime exposes private downstream consumption.</li>
</ul>

<p>
A reader should therefore be able to follow the same bounded slice across source, contract, and execution without mistaking any one of those surfaces for the owner of the whole language.
</p>

<hr/>

<h2 id="multi-runtime-posture">11. Multi-Runtime Posture</h2>

<p>
This workspace already supports the intended rule that one runtime must not become the definition of FROG.
</p>

<p>
Within the reference family, multiple runtime language realizations may coexist, for example:
</p>

<ul>
  <li>a Python realization,</li>
  <li>a Rust realization,</li>
  <li>and later other realizations if the published corridor justifies them.</li>
</ul>

<p>
Those runtimes should remain parallel consumers of the same emitted contract family for the same named slice.
They may differ in private structures or host mechanics,
but they should stay aligned on declared contract obligations.
</p>

<hr/>

<h2 id="design-rules">12. Design Rules</h2>

<ul>
  <li>Keep stage boundaries explicit.</li>
  <li>Do not hide undeclared assumptions across stages.</li>
  <li>Do not erase loop, state, or UI-participation meaning when the bounded corridor depends on them.</li>
  <li>Do not treat runtime-private convenience as normative specification truth.</li>
  <li>Keep emitted artifacts attributable to named example slices.</li>
  <li>Keep reference-family consumers aligned with the published contract artifacts they claim to support.</li>
  <li>Prefer one complete bounded corridor over many disconnected implementation fragments.</li>
</ul>

<hr/>

<h2 id="summary">13. Summary</h2>

<p>
This directory is the non-normative executable workspace for the FROG reference family.
Its purpose is to exercise bounded published corridors through explicit reference stages without collapsing the language into one implementation.
</p>

<p>
The first repository-visible executable corridor is now materially readable across:
</p>

<ul>
  <li><code>Examples/05_bounded_ui_accumulator/</code>,</li>
  <li><code>Implementations/Reference/ContractEmitter/examples/05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json</code>,</li>
  <li><code>Implementations/Reference/Runtime/</code>.</li>
</ul>

<p>
That does not make this workspace the owner of FROG.
It makes the first bounded source-to-contract-to-runtime corridor inspectable while preserving explicit ownership boundaries.
</p>
