<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Reference Contract Emitter</h1>

<p align="center">
  <strong>Backend contract emission stage for the non-normative FROG reference implementation</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#non-normative-status">2. Non-Normative Status</a></li>
  <li><a href="#architectural-position">3. Architectural Position</a></li>
  <li><a href="#published-example-contract-artifacts">4. Published Example Contract Artifacts</a></li>
  <li><a href="#what-this-directory-owns">5. What This Directory Owns</a></li>
  <li><a href="#what-this-directory-does-not-own">6. What This Directory Does Not Own</a></li>
  <li><a href="#first-slice-responsibilities">7. First-Slice Responsibilities</a></li>
  <li><a href="#relation-with-examples">8. Relation with Examples</a></li>
  <li><a href="#relation-with-runtime-consumers">9. Relation with Runtime Consumers</a></li>
  <li><a href="#design-rules">10. Design Rules</a></li>
  <li><a href="#summary">11. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory contains the stage that emits backend contracts from lowered execution forms.
Its role is to produce a standardized consumer-facing handoff aligned with the published backend-contract boundary.
</p>

<p>
The emitted artifacts are downstream from canonical source, structural validation, semantic interpretation, Execution IR, and lowering.
They are upstream from runtime-side or backend-family-side private realization.
</p>

<hr/>

<h2 id="non-normative-status">2. Non-Normative Status</h2>

<p>
This directory belongs to the non-normative reference implementation.
It does not redefine the normative backend-contract boundary.
</p>

<p>
Its role is to materialize repository-visible contract artifacts that are aligned with the published specification surfaces strongly enough to support executable corridor inspection and reference-family consumption.
</p>

<p>
Accordingly, the emitter implementation is not the owner of:
</p>

<ul>
  <li>source law,</li>
  <li>semantic law,</li>
  <li>Execution IR law,</li>
  <li>or backend-contract law.</li>
</ul>

<p>
It is a reference producer of artifacts, not the normative source of backend-contract meaning.
</p>

<hr/>

<h2 id="architectural-position">3. Architectural Position</h2>

<pre><code>canonical .frog source
      |
      v
structural validation
      |
      v
semantic interpretation
      |
      v
Execution IR
      |
      v
lowering
      |
      v
backend contract emission   &lt;-- this directory
      |
      v
backend contract artifact
      |
      v
consumer-side realization</code></pre>

<p>
The architectural rule remains explicit:
</p>

<pre><code>lowering != backend contract emission
backend contract emission != runtime realization
emitted artifact != private consumer implementation</code></pre>

<hr/>

<h2 id="published-example-contract-artifacts">4. Published Example Contract Artifacts</h2>

<p>
This directory may publish repository-visible contract artifacts for named example slices under:
</p>

<pre><code>Implementations/Reference/ContractEmitter/examples/</code></pre>

<p>
These artifacts are intended to make a bounded handoff corridor materially inspectable.
They are example-aligned emitted artifacts, not canonical source files.
</p>

<p>
For the first applicative vertical slice, the published artifact is:
</p>

<pre><code>Implementations/Reference/ContractEmitter/examples/
└── 05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json</code></pre>

<p>
That file is the first repository-visible reference contract artifact for the named example:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/</code></pre>

<p>
It exists to make the backend handoff explicit rather than leaving it as prose-only expectation.
</p>

<hr/>

<h2 id="what-this-directory-owns">5. What This Directory Owns</h2>

<ul>
  <li>material emission of backend-contract artifacts for the selected family,</li>
  <li>declaration of family assumptions,</li>
  <li>declaration of consumable execution units,</li>
  <li>declaration of preserved attribution and unsupported features,</li>
  <li>selection of emitted artifact shape for the non-normative reference corridor,</li>
  <li>and repository-visible publication of reference contract artifacts where that helps close an executable slice.</li>
</ul>

<hr/>

<h2 id="what-this-directory-does-not-own">6. What This Directory Does Not Own</h2>

<ul>
  <li>the normative backend-contract rules themselves,</li>
  <li>runtime-private realization,</li>
  <li>deployment packaging,</li>
  <li>debugger protocol definition,</li>
  <li>the canonical example source,</li>
  <li>or semantic acceptance of the example.</li>
</ul>

<p>
In particular:
</p>

<ul>
  <li><code>Examples/</code> owns the named illustrative source slice,</li>
  <li>the specification layers own the meaning of that slice,</li>
  <li><code>ContractEmitter/</code> owns emitted reference artifacts,</li>
  <li>and <code>Runtime/</code> owns private consumption of accepted artifacts.</li>
</ul>

<hr/>

<h2 id="first-slice-responsibilities">7. First-Slice Responsibilities</h2>

<p>
For the first slice, the emitter should produce artifacts rich enough to make explicit:
</p>

<ul>
  <li>contract identity,</li>
  <li>backend family orientation,</li>
  <li>declared assumptions,</li>
  <li>consumable executable units,</li>
  <li>state semantics where present,</li>
  <li>UI participation or UI-object interaction support where relevant,</li>
  <li>diagnostic and attribution support.</li>
</ul>

<p>
For the first published applicative slice, this means the emitted contract must preserve at least:
</p>

<ul>
  <li>the existence of one bounded executable unit,</li>
  <li>the fact that the loop runs for exactly five iterations,</li>
  <li>the fact that explicit state is required,</li>
  <li>the deterministic initial value of <code>0</code>,</li>
  <li>the public input / output binding posture,</li>
  <li>the indicator publication posture,</li>
  <li>and the minimal object-style property-write support for <code>face_color</code>.</li>
</ul>

<hr/>

<h2 id="relation-with-examples">8. Relation with Examples</h2>

<p>
The emitted artifacts under <code>examples/</code> are related to named repository examples, but they are not the examples themselves.
</p>

<p>
The ownership model remains:
</p>

<pre><code>Examples/
   -&gt; illustrate named source-level and corridor-level slices

Implementations/Reference/ContractEmitter/examples/
   -&gt; publish emitted backend-contract artifacts for selected example slices</code></pre>

<p>
This distinction matters because the canonical <code>.frog</code> source remains the source-owned representation of the example,
while the emitted contract artifact is a downstream handoff product for a selected consumer family.
</p>

<p>
Accordingly, an emitted example contract:
</p>

<ul>
  <li>must remain attributable to the named example slice,</li>
  <li>must remain downstream from the published ownership chain,</li>
  <li>must not silently add new semantic law,</li>
  <li>and must not be mistaken for the canonical saved program.</li>
</ul>

<hr/>

<h2 id="relation-with-runtime-consumers">9. Relation with Runtime Consumers</h2>

<p>
The primary downstream consumers of these emitted artifacts live under:
</p>

<pre><code>Implementations/Reference/Runtime/</code></pre>

<p>
That means the reading corridor for the first bounded executable slice is now materially inspectable as:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/
      |
      v
Implementations/Reference/ContractEmitter/examples/
05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json
      |
      v
Implementations/Reference/Runtime/</code></pre>

<p>
The runtime consumer must treat the emitted artifact as a declared contract boundary.
It may accept, reject, or fail during execution according to the runtime family posture,
but it must not treat the emitted artifact as optional prose.
</p>

<p>
Likewise, the emitter must not collapse into runtime-private assumptions that are not declared in the artifact.
</p>

<hr/>

<h2 id="design-rules">10. Design Rules</h2>

<ul>
  <li>Do not hide undeclared assumptions.</li>
  <li>Do not erase state semantics.</li>
  <li>Do not erase UI participation distinctions when the family claims support for them.</li>
  <li>Make rejection conditions explicit.</li>
  <li>Keep emitted artifacts attributable to their source slice.</li>
  <li>Do not promote reference-emitter convenience into normative backend-contract law.</li>
  <li>Do not mix canonical source ownership with emitted artifact ownership.</li>
</ul>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
The contract emitter is the stage that turns lowered implementation-facing forms into declared consumer-facing backend contracts for the reference family.
</p>

<p>
It now also serves as the publication point for repository-visible example-aligned contract artifacts under <code>examples/</code>.
Those artifacts help close the first executable corridor more explicitly:
the source slice is visible,
the emitted contract is visible,
and the runtime-side consumer boundary is visible.
</p>

<p>
That makes the first applicative vertical slice materially easier to inspect from source to contract to reference execution,
while keeping the ownership boundaries explicit.
</p>
