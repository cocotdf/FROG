<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Reference Implementation</h1>

<p align="center">
  <strong>Non-normative reference implementation workspace for executable FROG vertical slices</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#status-and-boundary">2. Status and Boundary</a></li>
  <li><a href="#architectural-position">3. Architectural Position</a></li>
  <li><a href="#current-purpose">4. Current Purpose</a></li>
  <li><a href="#prototype-status-and-future-compiler-direction">5. Prototype Status and Future Compiler Direction</a></li>
  <li><a href="#executable-reference-slices">6. Executable Reference Slices</a></li>
  <li><a href="#reference-pipeline">7. Reference Pipeline</a></li>
  <li><a href="#directory-posture">8. Directory Posture</a></li>
  <li><a href="#relation-with-examples-and-conformance">9. Relation with Examples and Conformance</a></li>
  <li><a href="#runtime-modules-deployment-modes-and-targets">10. Runtime Modules, Deployment Modes, and Targets</a></li>
  <li><a href="#runtime-posture-in-v01">11. Runtime Posture in v0.1</a></li>
  <li><a href="#what-this-directory-does-not-standardize">12. What this Directory Does Not Standardize</a></li>
  <li><a href="#current-status-in-v01">13. Current Status in v0.1</a></li>
  <li><a href="#summary">14. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory is the workspace for a <strong>reference implementation</strong> of the published FROG architecture.
Its purpose is to make selected parts of the specification executable without turning one implementation into the definition of the language.
</p>

<p>
Its practical role is to:
</p>

<ul>
  <li>load canonical <code>.frog</code> source,</li>
  <li>validate source against published rules,</li>
  <li>derive the published open execution-facing FROG IR,</li>
  <li>perform controlled lowering for a selected backend family,</li>
  <li>emit a backend contract or equivalent execution handoff,</li>
  <li>execute that handoff through one or more reference-side runtime service bundles.</li>
</ul>

<p>
This directory exists to prove that the published architectural boundaries are strong enough to support end-to-end executable slices.
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
  <li><code>IR/</code> — derivation, identity, construction, lowering, and backend contract boundaries,</li>
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

<pre><code>.frog canonical source
    |
    v
validation
    |
    v
validated program meaning
    |
    v
standardized FROG execution IR
    |
    v
lowering
    |
    v
backend contract / backend-oriented handoff
    |
    v
runtime-side consumption on a selected target
</code></pre>

<p>
This means:
</p>

<ul>
  <li>the reference implementation is not the owner of source shape,</li>
  <li>it is not the owner of validated semantic meaning,</li>
  <li>it is not the owner of the open IR model,</li>
  <li>it is not the owner of lowering law,</li>
  <li>it is not the owner of backend contract law,</li>
  <li>it is a practical consumer of those published layers.</li>
</ul>

<p>
A correct reference implementation therefore makes the published architecture executable <em>through</em> the declared stages, not around them.
</p>

<hr/>

<h2 id="current-purpose">4. Current Purpose</h2>

<p>
The immediate goal of this directory is <strong>not</strong> to build a feature-complete industrial platform.
The immediate goal is to deliver disciplined <strong>minimal executable vertical slices</strong>.
</p>

<p>
Those slices are meant to prove that the following chain can be made real and inspectable:
</p>

<ul>
  <li>canonical source can be loaded,</li>
  <li>published validation rules can be applied,</li>
  <li>a published open execution-facing FROG IR can be derived,</li>
  <li>lowering can specialize that IR for a concrete backend family,</li>
  <li>a backend contract can be emitted,</li>
  <li>a reference runtime path can accept and execute that contract on a selected target posture.</li>
</ul>

<p>
The first success criterion is architectural coherence, not breadth of language coverage.
The second success criterion is recoverability of stage boundaries, not implementation cleverness.
</p>

<hr/>

<h2 id="prototype-status-and-future-compiler-direction">5. Prototype Status and Future Compiler Direction</h2>

<p>
The executable slices in this directory are <strong>reference prototypes</strong>.
They are serious implementation exercises, but they are <strong>not yet</strong> the final production compiler pipeline of FROG.
</p>

<p>
What they prove today is that the architecture can already support:
</p>

<ul>
  <li>source loading,</li>
  <li>semantic validation for a controlled published subset,</li>
  <li>published execution-facing IR derivation,</li>
  <li>backend-family-oriented lowering,</li>
  <li>backend contract emission,</li>
  <li>runtime-side contract consumption.</li>
</ul>

<p>
What they do <strong>not</strong> yet claim is that the repository already contains:
</p>

<ul>
  <li>the final production compiler pipeline,</li>
  <li>the final fully stabilized industrial backend set,</li>
  <li>one definitive production runtime architecture,</li>
  <li>one universal deployment model for all targets.</li>
</ul>

<p>
The long-term direction remains:
</p>

<pre><code>.frog source
    |
    v
validated FROG semantics
    |
    v
standardized FROG execution IR
    |
    v
backend-specific lowering
    |
    v
backend contract
    |
    v
known compiler/runtime backend
    |
    v
deployable artifact
</code></pre>

<p>
This directory therefore proves the stage boundaries first.
It does not prematurely collapse them into one opaque compiler implementation.
</p>

<hr/>

<h2 id="executable-reference-slices">6. Executable Reference Slices</h2>

<p>
The current executable reference path is intentionally staged.
The progression matters:
</p>

<ul>
  <li><code>Examples/01_pure_addition</code></li>
  <li><code>Examples/02_ui_value_roundtrip</code></li>
  <li><code>Examples/03_ui_property_write</code></li>
  <li><code>Examples/04_stateful_feedback_delay</code></li>
</ul>

<p>
Each slice adds one architectural concern without collapsing layer boundaries.
</p>

<h3>6.1 01_pure_addition</h3>

<p>
This is the smallest end-to-end executable case.
It proves the full path from canonical <code>.frog</code> source to observable runtime result with:
</p>

<ul>
  <li><code>interface_input</code>,</li>
  <li><code>interface_output</code>,</li>
  <li>one ordinary primitive node,</li>
  <li><code>frog.core.add</code>.</li>
</ul>

<p>
Simple interpretation:
<code>result = a + b</code>
</p>

<h3>6.2 02_ui_value_roundtrip</h3>

<p>
This is the first front-panel value-participation case.
It proves that natural widget value flow can be transported through the architecture without being collapsed into object-style UI interaction.
</p>

<p>
Simple interpretation:
<code>ind_result.value = ctrl_a.value + ctrl_b.value</code>
</p>

<h3>6.3 03_ui_property_write</h3>

<p>
This is the first object-style UI interaction case.
It proves the distinction between:
</p>

<ul>
  <li>front-panel widget declaration,</li>
  <li>diagram-side <code>widget_reference</code> participation,</li>
  <li>a side-effecting UI primitive.</li>
</ul>

<p>
Simple interpretation:
<code>ctrl_gain.label.text = status</code>
</p>

<h3>6.4 04_stateful_feedback_delay</h3>

<p>
This is the first explicit-memory and valid-feedback case.
It proves that recurrence is represented through explicit delay state rather than hidden scheduler repair or implicit runtime memory.
</p>

<p>
Simple interpretation:
</p>

<pre><code>y(t) = x(t) + state(t)
state(t + 1) = y(t)
state(0) = 0.0</code></pre>

<p>
This staged progression matters.
It keeps the implementation aligned with the specification while avoiding premature generalization.
</p>

<hr/>

<h2 id="reference-pipeline">7. Reference Pipeline</h2>

<p>
The reference pipeline should reflect the published stage boundaries.
A useful command-line model is:
</p>

<pre><code>frogc validate file.frog
frogc derive-ir file.frog
frogc lower file.frog
frogc emit-contract file.frog
frogc run file.frog
</code></pre>

<p>
The exact CLI surface may evolve, but the implementation should preserve stage separation:
</p>

<ul>
  <li><strong>validate</strong> — check that the source belongs to the supported validated subset,</li>
  <li><strong>derive-ir</strong> — produce the published open execution-facing representation with recoverable source attribution,</li>
  <li><strong>lower</strong> — specialize the open IR for a selected backend family,</li>
  <li><strong>emit-contract</strong> — produce the handoff consumed by a runtime or backend,</li>
  <li><strong>run</strong> — execute through runtime-side contract consumption rather than by silently jumping from source straight to private execution.</li>
</ul>

<p>
This directory may temporarily contain compact demonstration code for that pipeline, including early monolithic scripts used to prove first slices.
Such code remains implementation-side convenience.
It does not redefine the specification and does not eliminate the intended internal separation between loader, validator, derivation, lowering, contract emission, and runtime-side consumption.
</p>

<hr/>

<h2 id="directory-posture">8. Directory Posture</h2>

<p>
A useful posture for the reference implementation workspace is to keep implementation concerns explicit without pretending they are new language layers.
</p>

<p>
A practical internal structure may eventually distinguish work areas such as:
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
  <li><code>Deriver/</code> — derivation of the published open execution-facing IR,</li>
  <li><code>Lowerer/</code> — backend-family-oriented specialization,</li>
  <li><code>ContractEmitter/</code> — backend contract emission,</li>
  <li><code>Runtime/</code> — runtime-side contract acceptance and execution services,</li>
  <li><code>UIHost/</code> — host-side UI binding support for the first host-oriented family.</li>
</ul>

<p>
A compact demonstration script may exist early in the process, but the long-term direction should still respect these implementation boundaries.
Early convenience must not become accidental architecture.
</p>

<hr/>

<h2 id="relation-with-examples-and-conformance">9. Relation with Examples and Conformance</h2>

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
The reference implementation should therefore start from published named slices rather than from an unbounded language ambition.
A correct implementation should prove each published example path before widening scope.
</p>

<p>
In practical terms, the first implementation milestones should be able to consume the published example slices, produce the expected intermediate artifacts, and return the expected observable results or effects.
Only after those paths are stable should the implementation widen further.
</p>

<hr/>

<h2 id="runtime-modules-deployment-modes-and-targets">10. Runtime Modules, Deployment Modes, and Targets</h2>

<p>
This directory may realize execution through different runtime-service bundles depending on the target posture being exercised.
That flexibility is an implementation concern, not a redefinition of the language.
</p>

<p>
For implementation clarity, it is useful to distinguish the following:
</p>

<ul>
  <li><strong>backend family</strong> — the downstream technical execution-consumption family selected after lowering,</li>
  <li><strong>target profile</strong> — the class of execution assumptions and constraints being aimed at,</li>
  <li><strong>deployment mode</strong> — the packaging and observability posture used for execution,</li>
  <li><strong>runtime module</strong> — an implementation-side service bundle used to make execution possible on a selected target posture.</li>
</ul>

<p>
These terms must not be collapsed into one word such as <code>runtime</code>.
A runtime module is not identical to a target profile.
A target profile is not identical to a backend family.
A deployment mode is not itself the program meaning.
</p>

<p>
Accordingly, a compiled artifact does not automatically imply one universal runtime shape.
Different deployment modes and different target postures may require different runtime-service bundles while still preserving the same validated FROG meaning.
</p>

<p>
Examples of implementation-side runtime-module families that may appear in this workspace include:
</p>

<ul>
  <li><code>runtime.core</code> — minimal execution services,</li>
  <li><code>runtime.ui</code> — host-side UI event-loop and widget binding services,</li>
  <li><code>runtime.observability</code> — tracing, probes, watch, and inspection services,</li>
  <li><code>runtime.interop</code> — external host interaction and interop services,</li>
  <li><code>runtime.rt</code> — stricter execution-support services for constrained real-time-oriented paths,</li>
  <li><code>runtime.embedded_support</code> — reduced services for constrained deployment families.</li>
</ul>

<p>
These names are implementation-facing examples.
They are not, by themselves, normative profile specifications.
</p>

<p>
A useful build and deployment posture is therefore:
</p>

<ul>
  <li>select a supported target posture,</li>
  <li>select a backend family,</li>
  <li>lower accordingly,</li>
  <li>emit the appropriate handoff,</li>
  <li>bundle or provide only the runtime modules required for that execution path.</li>
</ul>

<p>
This keeps the executable reference path honest:
the language stays stable,
the stage boundaries stay visible,
and the implementation remains free to avoid one unnecessarily heavy monolithic runtime.
</p>

<hr/>

<h2 id="runtime-posture-in-v01">11. Runtime Posture in v0.1</h2>

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
  <li>explicit local state only where already justified by published slices,</li>
  <li>no requirement to standardize one universal runtime-private architecture,</li>
  <li>no silent collapse of the backend contract into private runtime internals,</li>
  <li>narrow UI support only where already justified by the published slices,</li>
  <li>observability support only where needed to keep the early slices inspectable,</li>
  <li>no assumption that development execution and deployable execution must bundle the same runtime-service set.</li>
</ul>

<p>
The reference runtime should therefore prove architecture and recoverability first.
It should not pretend to define the full long-term FROG runtime story.
</p>

<hr/>

<h2 id="what-this-directory-does-not-standardize">12. What this Directory Does Not Standardize</h2>

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
  <li>treat one chosen runtime-module layout as the universal FROG runtime architecture,</li>
  <li>treat one development convenience bundle as the mandatory deployment shape for every target,</li>
  <li>hide unsupported features behind silent reinterpretation,</li>
  <li>pretend that current vertical slices already constitute the final production compiler pipeline.</li>
</ul>

<p>
If an implementation shortcut appears attractive but conflicts with the published architecture, the specification should be clarified first.
Implementation habit must not overwrite architectural intent.
</p>

<hr/>

<h2 id="current-status-in-v01">13. Current Status in v0.1</h2>

<p>
In base v0.1, this directory should stay compact, explicit, and testable.
The current objective is a coherent executable path through small published example slices.
</p>

<p>
A good current success condition is:
</p>

<ul>
  <li>load a published example <code>.frog</code> source,</li>
  <li>validate the supported subset,</li>
  <li>derive the published open execution-facing IR,</li>
  <li>lower for the first backend family,</li>
  <li>emit a backend contract,</li>
  <li>execute it through a minimal reference runtime path and obtain the expected observable result or effect.</li>
</ul>

<p>
A useful implementation form may still be a compact Python demonstration pipeline living under <code>Implementations/Reference/CLI/</code>.
That remains acceptable as long as it stays explicitly non-normative and does not blur intended stage ownership.
</p>

<p>
The next long-term step after the early executable slices is not to hide the architecture behind a private monolith.
It is to stabilize the published IR and show how disciplined FROG lowering can feed known backend/compiler/runtime families in a reproducible way.
</p>

<hr/>

<h2 id="summary">14. Summary</h2>

<p>
This directory is the home of the non-normative FROG reference implementation workspace.
Its job is to make the published architecture executable through disciplined vertical slices:
source,
validation,
published execution IR derivation,
lowering,
backend contract emission,
and runtime-side contract consumption.
</p>

<p>
It is practical by design, but it does not own the language.
It is:
</p>

<ul>
  <li>a consumer of the published specification,</li>
  <li>a detector of specification gaps,</li>
  <li>a proving ground for executable slices.</li>
</ul>

<p>
It is also a bridge toward a future full compiler/runtime story,
but it is not yet that final compiler pipeline.
That distinction must remain explicit.
</p>

<p>
In particular, this workspace may execute through different runtime-service bundles depending on the
target posture and deployment mode under test.
That flexibility is an implementation strength, not a license to blur the architectural boundaries
between language meaning, IR, backend contract, and runtime realization.
</p>
