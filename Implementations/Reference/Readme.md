<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG Reference Implementation</h1>

<p align="center">
  Non-normative reference implementation workspace for executable FROG vertical slices<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#status-and-boundary">2. Status and Boundary</a></li>
  <li><a href="#architectural-position">3. Architectural Position</a></li>
  <li><a href="#current-goal">4. Current Goal</a></li>
  <li><a href="#first-executable-slice">5. First Executable Slice</a></li>
  <li><a href="#reference-pipeline">6. Reference Pipeline</a></li>
  <li><a href="#directory-structure">7. Directory Structure</a></li>
  <li><a href="#relation-with-examples-and-conformance">8. Relation with Examples and Conformance</a></li>
  <li><a href="#runtime-posture-in-v01">9. Runtime Posture in v0.1</a></li>
  <li><a href="#what-this-directory-must-not-do">10. What this Directory Must Not Do</a></li>
  <li><a href="#status-in-v01">11. Status in v0.1</a></li>
  <li><a href="#summary">12. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory is the workspace for a <strong>reference implementation</strong> of the published FROG architecture.
Its role is to make selected parts of the specification executable without turning one implementation into the definition of the language.
</p>

<p>
The purpose of this directory is practical:
</p>

<ul>
  <li>load canonical <code>.frog</code> source,</li>
  <li>validate source against published rules,</li>
  <li>derive open execution-facing IR,</li>
  <li>perform controlled lowering for a selected backend family,</li>
  <li>emit a backend contract,</li>
  <li>execute that contract in a minimal reference runtime.</li>
</ul>

<p>
This directory exists to prove that the published architectural boundaries are strong enough to support an end-to-end executable slice.
It does not replace the specification.
It consumes it.
</p>

<hr/>

<h2 id="status-and-boundary">2. Status and Boundary</h2>

<p>
This directory is <strong>non-normative</strong>.
It belongs to the repository, but it does not own the language.
</p>

<p>
Normative ownership remains in the specification layers:
</p>

<ul>
  <li><code>Expression/</code> — canonical source representation,</li>
  <li><code>Language/</code> — validated semantic truth,</li>
  <li><code>Libraries/</code> — intrinsic primitive identities and primitive-local contracts,</li>
  <li><code>Profiles/</code> — optional standardized capability families,</li>
  <li><code>IR/</code> — derivation, construction, identity, lowering, and backend contract boundaries,</li>
  <li><code>IDE/</code> — authoring, debugging, observability, and tool-facing concerns.</li>
</ul>

<p>
If the reference implementation reveals ambiguity, underspecification, or conflict, the fix belongs in the owning specification document.
The implementation must not become a hidden source of language truth.
</p>

<hr/>

<h2 id="architectural-position">3. Architectural Position</h2>

<p>
This directory is downstream from the published specification layers.
Its role is to consume already defined boundaries rather than to bypass them.
</p>

<pre><code>.frog source
    |
    v
validation
    |
    v
Execution IR
    |
    v
lowering
    |
    v
backend contract
    |
    v
reference runtime consumption
</code></pre>

<p>
This means:
</p>

<ul>
  <li>the reference implementation is not the owner of source shape,</li>
  <li>it is not the owner of validated semantic meaning,</li>
  <li>it is not the owner of the open IR model,</li>
  <li>it is a practical consumer of those published layers.</li>
</ul>

<p>
A correct reference implementation should therefore make the published architecture executable <em>through</em> the declared stages, not around them.
</p>

<hr/>

<h2 id="current-goal">4. Current Goal</h2>

<p>
The immediate goal of this directory is <strong>not</strong> to build a feature-complete industrial platform.
The immediate goal is to deliver a disciplined <strong>minimal executable vertical slice</strong>.
</p>

<p>
That slice should be small enough to remain readable and auditable, but complete enough to prove the following chain:
</p>

<ul>
  <li>canonical source can be loaded,</li>
  <li>published validation rules can be applied,</li>
  <li>an open execution-facing IR can be derived,</li>
  <li>lowering can specialize that IR for a concrete backend family,</li>
  <li>a backend contract can be emitted,</li>
  <li>a reference runtime can accept and execute that contract.</li>
</ul>

<p>
The first success criterion is architectural coherence, not coverage breadth.
</p>

<hr/>

<h2 id="first-executable-slice">5. First Executable Slice</h2>

<p>
The first executable target for the reference implementation should be the smallest published example slice:
</p>

<pre><code>Examples/01_pure_addition</code></pre>

<p>
This first slice is intentionally narrow.
It should demonstrate:
</p>

<ul>
  <li><code>interface_input</code>,</li>
  <li><code>interface_output</code>,</li>
  <li>one ordinary primitive node,</li>
  <li><code>frog.core.add</code>,</li>
  <li>a complete end-to-end path from <code>.frog</code> source to runtime result.</li>
</ul>

<p>
The first slice is deliberately chosen because it exercises the full architectural chain while avoiding premature UI, state, and scheduling complexity.
It is the smallest published case that can prove the implementation path without weakening the layer boundaries.
</p>

<p>
After that first slice is stable, the reference implementation can expand in order to cover:
</p>

<ul>
  <li><code>Examples/02_ui_value_roundtrip</code>,</li>
  <li><code>Examples/03_ui_property_write</code>,</li>
  <li><code>Examples/04_stateful_feedback_delay</code>.</li>
</ul>

<p>
That staged progression matters.
It keeps the implementation aligned with the specification while avoiding premature runtime complexity.
</p>

<hr/>

<h2 id="reference-pipeline">6. Reference Pipeline</h2>

<p>
The reference pipeline should reflect the already published stage boundaries.
A useful command-line model is:
</p>

<pre><code>frogc validate file.frog
frogc derive-ir file.frog
frogc lower file.frog
frogc emit-contract file.frog
frogc run file.frog
</code></pre>

<p>
The exact CLI surface may evolve, but the implementation should preserve the stage separation:
</p>

<ul>
  <li><strong>validate</strong> — check that the source belongs to the supported validated subset,</li>
  <li><strong>derive-ir</strong> — produce an open execution-facing representation with recoverable source attribution,</li>
  <li><strong>lower</strong> — specialize the open IR for a selected backend family,</li>
  <li><strong>emit-contract</strong> — produce the handoff consumed by a runtime or backend,</li>
  <li><strong>run</strong> — execute through runtime-side contract consumption rather than by silently jumping from source straight to private execution.</li>
</ul>

<p>
This directory may temporarily contain compact demonstration code for that pipeline, including early monolithic scripts used to prove a first slice.
Such code remains implementation-side convenience.
It does not redefine the specification and does not eliminate the intended internal separation between loader, validator, derivation, lowering, contract emission, and runtime consumption.
</p>

<hr/>

<h2 id="directory-structure">7. Directory Structure</h2>

<p>
A useful structure for the reference implementation is:
</p>

<pre><code>Implementations/Reference/
├── CLI/
├── Loader/
├── Validator/
├── Deriver/
├── Lowerer/
├── ContractEmitter/
├── Runtime/
└── UIHost/
</code></pre>

<p>
These are implementation-facing work areas inside one reference implementation.
They are not additional language layers.
</p>

<ul>
  <li><code>CLI/</code> — command entry points for the reference toolchain,</li>
  <li><code>Loader/</code> — canonical source intake, decoding, and structural loading,</li>
  <li><code>Validator/</code> — supported-subset validation against published rules,</li>
  <li><code>Deriver/</code> — derivation of open execution-facing IR,</li>
  <li><code>Lowerer/</code> — backend-family-oriented specialization,</li>
  <li><code>ContractEmitter/</code> — backend contract emission,</li>
  <li><code>Runtime/</code> — runtime-side contract acceptance and execution,</li>
  <li><code>UIHost/</code> — host-side UI binding support for the first host-oriented family.</li>
</ul>

<p>
A compact demonstration script may exist early in the process, but the long-term direction should still respect these implementation boundaries.
Early convenience must not become accidental architecture.
</p>

<hr/>

<h2 id="relation-with-examples-and-conformance">8. Relation with Examples and Conformance</h2>

<p>
This directory works together with:
</p>

<ul>
  <li><code>Examples/</code> — published named source programs,</li>
  <li><code>Conformance/</code> — expected acceptance, rejection, and preservation outcomes.</li>
</ul>

<p>
The relationship is intentionally simple:
</p>

<pre><code>Examples/
  provides source programs

Conformance/
  states what is expected

Implementations/Reference/
  tries to do it correctly
</code></pre>

<p>
The reference implementation should therefore start from the published named slices rather than from an unbounded language ambition.
A correct first implementation should prove the first example path before widening scope.
</p>

<p>
In practical terms, the first implementation milestone should be able to consume <code>Examples/01_pure_addition/main.frog</code>, produce the expected intermediate artifacts, and return the expected public result.
Only after that path is stable should the implementation expand to the UI-oriented and state-oriented examples.
</p>

<hr/>

<h2 id="runtime-posture-in-v01">9. Runtime Posture in v0.1</h2>

<p>
The first target family should remain deliberately conservative.
A suitable first family is a host-oriented family such as:
</p>

<pre><code>reference_host_runtime_ui_binding</code></pre>

<p>
In v0.1, the runtime posture should remain compact:
</p>

<ul>
  <li>single-process host execution,</li>
  <li>deterministic step-oriented behavior,</li>
  <li>no requirement to standardize one universal runtime-private architecture,</li>
  <li>no silent collapse of the backend contract into private runtime internals,</li>
  <li>narrow UI support only where already justified by the published slices.</li>
</ul>

<p>
When the implementation moves beyond pure computation, the next published concerns include:
</p>

<ul>
  <li><code>widget_value</code>,</li>
  <li><code>widget_reference</code>,</li>
  <li><code>frog.ui.property_read</code>,</li>
  <li><code>frog.ui.property_write</code>,</li>
  <li><code>frog.ui.method_invoke</code>,</li>
  <li><code>frog.core.delay</code> with explicit local memory.</li>
</ul>

<p>
Those expansions should happen slice by slice, not through a premature general runtime model.
The first runtime should prove the architecture, not attempt to standardize all future runtime behavior.
</p>

<hr/>

<h2 id="what-this-directory-must-not-do">10. What this Directory Must Not Do</h2>

<p>
This directory must not:
</p>

<ul>
  <li>pretend that one implementation becomes the language definition,</li>
  <li>silently redefine canonical source structure,</li>
  <li>silently redefine semantic truth,</li>
  <li>replace published IR boundaries with private shortcuts,</li>
  <li>merge open IR with runtime-private scheduling internals,</li>
  <li>treat backend contract as if it were identical to one private runtime representation,</li>
  <li>hide unsupported features behind silent reinterpretation,</li>
  <li>claim that one runtime-private architecture is the universal FROG runtime.</li>
</ul>

<p>
If an implementation shortcut appears attractive but conflicts with the published architecture, the specification should be clarified first.
Implementation habit must not overwrite architectural intent.
</p>

<hr/>

<h2 id="status-in-v01">11. Status in v0.1</h2>

<p>
In base v0.1, this directory should stay compact, explicit, and testable.
The first target is a coherent path from a small published example to an observable runtime result.
</p>

<p>
A good initial success condition is:
</p>

<ul>
  <li>load <code>Examples/01_pure_addition/main.frog</code>,</li>
  <li>validate the supported subset,</li>
  <li>derive open execution-facing IR,</li>
  <li>lower for the first backend family,</li>
  <li>emit a backend contract,</li>
  <li>execute it in a minimal reference runtime and obtain the expected public output.</li>
</ul>

<p>
A useful early implementation form may be a compact Python demonstration pipeline living under <code>Implementations/Reference/CLI/</code>.
That is acceptable as a first proving step as long as it remains explicitly non-normative and does not blur the intended stage ownership.
</p>

<p>
Once that path is stable, the next expansions should remain incremental and published-slice-driven.
</p>

<hr/>

<h2 id="summary">12. Summary</h2>

<p>
This directory is the home of the non-normative FROG reference implementation workspace.
Its job is to make the published architecture executable through a disciplined vertical slice:
source,
validation,
IR derivation,
lowering,
backend contract emission,
and runtime-side contract consumption.
</p>

<p>
It is practical by design, but it does not own the language.
It is a consumer of the published specification, a detector of specification gaps, and a proving ground for executable slices.
It must remain that, and no more.
</p>
