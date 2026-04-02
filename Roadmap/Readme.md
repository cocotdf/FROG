<p align="center">
  <img src="../FROG%20logo.svg" alt="FROG logo" width="200"/>
</p>

<h1 align="center">🐸 FROG Roadmap</h1>

<p align="center">
  <strong>Non-normative planning layer for the progressive closure of FROG as a language, conformance surface, reference path, compiler stack, runtime path, deployment path, and future IDE ecosystem</strong>
</p>

<p align="center">
  Roadmap start date: <strong>8 March 2026</strong><br/>
  This roadmap lives inside the FROG repository but does not redefine normative ownership.
</p>

<p align="center">
  <a href="#project-map-at-a-glance">Project map</a> •
  <a href="#purpose-of-this-roadmap">Purpose</a> •
  <a href="#what-this-roadmap-is-and-is-not">What this is / is not</a> •
  <a href="#status-legend">Status legend</a> •
  <a href="#guiding-principles">Guiding principles</a> •
  <a href="#current-published-baseline">Current baseline</a> •
  <a href="#priority-order">Priority order</a> •
  <a href="#high-level-roadmap">High-level roadmap</a> •
  <a href="#phase-0-baseline-established">Phase 0</a> •
  <a href="#phase-1-close-the-v01-foundation">Phase 1</a> •
  <a href="#phase-2-stabilize-the-reference-execution-path">Phase 2</a> •
  <a href="#phase-3-build-the-first-serious-compiler-path">Phase 3</a> •
  <a href="#phase-4-build-the-first-serious-frog-ide">Phase 4</a> •
  <a href="#phase-5-expand-language-power-without-losing-clarity">Phase 5</a> •
  <a href="#phase-6-build-the-open-industrial-ecosystem">Phase 6</a> •
  <a href="#cross-cutting-workstreams">Cross-cutting workstreams</a> •
  <a href="#milestone-navigation">Milestone navigation</a> •
  <a href="#definition-of-success">Definition of success</a>
</p>

<hr/>

<h2 id="project-map-at-a-glance">Project map at a glance</h2>

<pre>
FROG closure sequence

canonical .frog source
        |
        v
loadability
        |
        v
structural validation
        |
        v
validated language meaning
        |
        v
standardized FROG execution IR
        |
        v
backend-specific lowering
        |
        v
backend contract / consumable handoff
        |
        v
runtime or compiler/backend realization
        |
        v
deployable artifact


in parallel

authoring
   -> Program Model
   -> graphical IDE
   -> validation feedback
   -> observability / debugging
   -> reusable industrial workflow


project logic

semantic closure
   -> schema / validation closure
   -> conformance closure
   -> reference execution proof
   -> backend credibility
   -> IDE credibility
   -> ecosystem credibility
</pre>

<p>
This roadmap explains the intended closure order.
It does not replace <code>Expression/</code>, <code>Language/</code>, <code>IR/</code>, or any other normative ownership layer.
</p>

<hr/>

<h2 id="purpose-of-this-roadmap">Purpose of this roadmap</h2>

<p>
This roadmap exists to track the <strong>planned closure path</strong> of FROG as a full long-term ecosystem effort.
It is a planning layer inside the repository, not the source of normative language truth.
</p>

<p>
Its practical purpose is to answer one project question:
</p>

<p>
<strong>What sequence of concrete closures must be completed to move from the currently published FROG baseline to a serious open graphical programming ecosystem with a credible compiler/runtime path, credible deployment depth, and a serious future IDE?</strong>
</p>

<p>
That distinction matters:
</p>

<ul>
  <li><strong>the specification layers</strong> define what FROG is,</li>
  <li><strong>the roadmap layer</strong> defines in what order the project should be closed.</li>
</ul>

<hr/>

<h2 id="what-this-roadmap-is-and-is-not">What this roadmap is and is not</h2>

<h3>What it is</h3>

<ul>
  <li>a sequencing layer,</li>
  <li>a closure plan,</li>
  <li>a milestone map,</li>
  <li>a prioritization surface for technical and ecosystem work.</li>
</ul>

<h3>What it is not</h3>

<ul>
  <li>not the normative language definition,</li>
  <li>not the source of semantic truth,</li>
  <li>not a substitute for <code>Expression/</code>, <code>Language/</code>, <code>IR/</code>, or <code>Profiles/</code>,</li>
  <li>not a place where implementation convenience becomes language law,</li>
  <li>not a place where strategy prose silently replaces technical closure.</li>
</ul>

<hr/>

<h2 id="status-legend">Status legend</h2>

<ul>
  <li><strong>[x]</strong> completed or already established in the published baseline</li>
  <li><strong>[~]</strong> partially established, active, or not yet fully closed</li>
  <li><strong>[ ]</strong> planned future work</li>
</ul>

<hr/>

<h2 id="guiding-principles">Guiding principles</h2>

<ul>
  <li>Keep the architectural boundaries explicit.</li>
  <li>Prefer small coherent closures over large speculative rewrites.</li>
  <li>Do not let reference implementation convenience become hidden language law.</li>
  <li>Do not collapse open FROG IR into one backend-specific or runtime-private form.</li>
  <li>Do not confuse backend family, target profile, deployment mode, and runtime-private realization.</li>
  <li>Do not confuse roadmap planning with normative ownership.</li>
  <li>Keep the path from canonical <code>.frog</code> source to deployable execution explicit and inspectable.</li>
  <li>Use conformance as a public truth surface, not as commentary only.</li>
  <li>Keep source-shape/schema closure distinct from later semantic validation.</li>
  <li>Only widen the ecosystem after enough closure exists to support that widening cleanly.</li>
</ul>

<pre>
What the project must preserve

saved source           -> Expression
validated meaning      -> Language
derived execution form -> IR
backend specialization -> Lowering
consumable handoff     -> Backend contract
private realization    -> Runtime / backend
authoring + debugging  -> IDE
closure sequencing     -> Roadmap
</pre>

<hr/>

<h2 id="current-published-baseline">Current published baseline</h2>

<p>
The project is no longer only conceptual.
A meaningful public foundation already exists.
</p>

<h3>Already established</h3>

<ul>
  <li>[x] FROG is explicitly structured as an open graphical dataflow language rather than a product-bound environment.</li>
  <li>[x] The six core specification families exist:
    <code>Expression</code>,
    <code>Language</code>,
    <code>IR</code>,
    <code>Libraries</code>,
    <code>Profiles</code>,
    <code>IDE</code>.
  </li>
  <li>[x] The repository contains support areas:
    <code>Examples/</code>,
    <code>Conformance/</code>,
    and <code>Implementations/Reference/</code>.
  </li>
  <li>[x] The first published executable slices already exist:
    <code>01_pure_addition</code>,
    <code>02_ui_value_roundtrip</code>,
    <code>03_ui_property_write</code>,
    <code>04_stateful_feedback_delay</code>.
  </li>
  <li>[x] The reference implementation posture is explicitly non-normative.</li>
  <li>[x] The distinction between public interface, front panel, and diagram is already explicit.</li>
  <li>[x] The distinction between <code>widget_value</code> and <code>widget_reference</code> is already explicit.</li>
  <li>[x] The strategic framing layer already exists through <code>Strategy/Heilmeier/</code>.</li>
  <li>[x] The roadmap layer already exists as a non-normative planning surface distinct from both strategy and specification.</li>
  <li>[x] The long-term chain remains explicit:
    <code>.frog source -&gt; loadability -&gt; structural validation -&gt; validated meaning -&gt; FROG execution IR -&gt; lowering -&gt; backend contract -&gt; backend/runtime</code>.
  </li>
  <li>[x] The distinction between backend family, target profile, deployment mode, and runtime-private realization is now explicit at the architectural level and no longer only implicit future intent.</li>
  <li>[x] Source-shape/schema posture now has an explicit normative home inside <code>Expression/</code>.</li>
  <li>[x] A conservative machine-checkable schema artifact now exists for canonical top-level source shape.</li>
  <li>[x] The conformance layer now reads more explicitly through
    <code>loadability -&gt; structural validity -&gt; semantic acceptance -&gt; preservation</code>.
  </li>
  <li>[x] The reference implementation posture now describes staged validation rather than a blurred validator story.</li>
</ul>

<h3>Partially formed but not yet fully closed</h3>

<ul>
  <li>[~] Expression ↔ Language ↔ IR correspondence</li>
  <li>[~] minimal primitive baseline closure</li>
  <li>[~] type / value / state semantic closure</li>
  <li>[~] execution-model and structure closure</li>
  <li>[~] source-shape / schema and validator closure as a fully stable repository-level asset</li>
  <li>[~] conformance breadth and public completeness</li>
  <li>[~] repeatable reference execution path for a clearly bounded supported subset</li>
  <li>[~] explicit target-profile taxonomy beyond the now-established architectural distinction</li>
  <li>[~] explicit deployment-mode taxonomy beyond the now-established architectural distinction</li>
  <li>[~] first serious backend-family taxonomies and first reusable contract families</li>
</ul>

<h3>Still future work</h3>

<ul>
  <li>[ ] a fully closed v0.1 foundation</li>
  <li>[ ] a fully stable schema / validator closure</li>
  <li>[ ] a first serious backend-oriented compiler path</li>
  <li>[ ] a serious FROG IDE foundation</li>
  <li>[ ] broader target-profile and deployment depth</li>
  <li>[ ] a mature conformance / certification / ecosystem layer</li>
</ul>

<h3>Interpretation of the current state</h3>

<pre>
FROG today

   +-- strong architectural base
   +-- early semantic and IR structure
   +-- first public executable reference slices
   +-- explicit conformance posture
   +-- explicit non-normative reference path
   +-- explicit profile / backend / runtime separation
   +-- explicit source-schema posture
   +-- conservative machine-checkable top-level schema support
   +-- explicit staged conformance reading
   +-- no final production compiler stack yet
   +-- no serious full IDE yet
   +-- no mature deployment ecosystem yet
</pre>

<hr/>

<h2 id="priority-order">Priority order</h2>

<p>
Not all future work is equally urgent.
The project currently benefits most from the following closure order.
</p>

<ol>
  <li>close Expression ↔ Language ↔ IR correspondence more explicitly,</li>
  <li>close the minimal primitive baseline,</li>
  <li>close type / value / state semantic ownership more tightly,</li>
  <li>close execution-model and structure semantics more tightly,</li>
  <li>stabilize source-shape/schema and validator posture as a stable repository-level closure,</li>
  <li>expand conformance in a disciplined way,</li>
  <li>strengthen the repeatable reference execution path,</li>
  <li>prepare the first serious backend contract and lowering family,</li>
  <li>deepen explicit target-profile and deployment-mode families where they materially improve execution and deployment clarity,</li>
  <li>expand examples only when they add new boundary value,</li>
  <li>expand benchmark and strategic material after enough technical closure exists.</li>
</ol>

<h3>30-day closure bias</h3>

<pre>
first
   correspondence
   + primitives
   + type/value/state

then
   execution-model closure
   + source schema / validation stabilization

then
   conformance growth
   + example growth
   + repeatable reference path

then
   backend contract preparation
   + backend family depth
   + target-profile and deployment clarity
</pre>

<hr/>

<h2 id="high-level-roadmap">High-level roadmap</h2>

<pre>
Phase 0  -> baseline established
Phase 1  -> close the v0.1 foundation
Phase 2  -> stabilize the reference execution path
Phase 3  -> build the first serious compiler/backend path
Phase 4  -> build the first serious FROG IDE
Phase 5  -> expand language power and deployment depth
Phase 6  -> build the open industrial ecosystem
</pre>

<p>
The intended project logic is:
</p>

<pre>
normative closure
        ->
schema / validation stabilization
        ->
conformance and reference-path reliability
        ->
compiler/backend credibility
        ->
IDE credibility
        ->
ecosystem depth and industrial strength
</pre>

<hr/>

<h2 id="phase-0-baseline-established">Phase 0 — Baseline established</h2>

<p>
This phase corresponds to the work that had to exist before a serious roadmap became useful.
It is substantially complete.
</p>

<h3>Objective</h3>

<p>
Establish a durable architectural base and prove that the specification can already support a first disciplined executable path without collapsing the language into one private implementation shortcut.
</p>

<h3>Checklist</h3>

<ul>
  <li>[x] Establish the six core specification families.</li>
  <li>[x] Separate source, semantics, IR, libraries, profiles, and IDE responsibilities.</li>
  <li>[x] Publish the source-level model for diagram, public interface, and front panel.</li>
  <li>[x] Publish the early IR bundle with explicit downstream boundaries.</li>
  <li>[x] Publish initial intrinsic library families.</li>
  <li>[x] Publish initial profile direction.</li>
  <li>[x] Publish the IDE architectural direction and Program Model posture.</li>
  <li>[x] Publish named examples.</li>
  <li>[x] Publish early conformance material.</li>
  <li>[x] Publish a non-normative reference implementation workspace.</li>
  <li>[x] Prove the first executable vertical slices.</li>
  <li>[x] Recontextualize the root repository around the real published state.</li>
  <li>[x] Publish a strategic framing layer distinct from the normative layers.</li>
  <li>[x] Publish a roadmap layer distinct from both strategy and specification.</li>
  <li>[x] Make the distinction between backend family, target profile, deployment mode, and runtime-private realization explicit at the architectural level.</li>
</ul>

<h3>Exit condition</h3>

<p>
The project has a coherent architectural base and an inspectable early execution story.
This condition is met in substance.
</p>

<hr/>

<h2 id="phase-1-close-the-v01-foundation">Phase 1 — Close the v0.1 foundation</h2>

<p>
This is the next critical closure phase.
The goal is not to widen the language aggressively.
The goal is to make the current base firmer, cleaner, and easier to build on.
</p>

<h3>Objective</h3>

<p>
Turn the current baseline into a tighter, better owned, and more machine-checkable v0.1 foundation.
</p>

<h3>Checklist</h3>

<ul>
  <li>[ ] Close remaining cross-document ambiguity between <code>Expression</code>, <code>Language</code>, and <code>IR</code>.</li>
  <li>[ ] Make normative truth versus implementation convenience fully unambiguous.</li>
  <li>[ ] Close the minimal serious primitive baseline.</li>
  <li>[ ] Close type / value / state semantic ownership more explicitly.</li>
  <li>[ ] Close execution-model and structure semantics more explicitly.</li>
  <li>[x] Publish a first disciplined source-shape/schema posture.</li>
  <li>[x] Publish a first conservative machine-checkable canonical top-level source schema artifact.</li>
  <li>[~] Publish validator expectations aligned with canonical source ownership.</li>
  <li>[~] Stabilize the distinction between schema-assisted structural validation and later semantic validation across the relevant repository layers.</li>
  <li>[ ] Tighten conformance coverage around already published boundaries.</li>
  <li>[ ] Ensure every published example slice has an explicit expected-outcome posture.</li>
  <li>[x] Make the architectural distinction between backend family, target profile, deployment mode, and runtime-private realization explicit.</li>
  <li>[ ] Decide whether first named target-profile families need publication in base v0.1 or may remain future profile work.</li>
  <li>[~] Publish and maintain this roadmap layer inside the repository.</li>
</ul>

<h3>Exit condition</h3>

<p>
A new reader should be able to understand, without ambiguity:
</p>

<ul>
  <li>what is source truth,</li>
  <li>what is structural validity and source-schema posture,</li>
  <li>what is semantic truth,</li>
  <li>what is derived execution form,</li>
  <li>what is a backend-family-facing handoff,</li>
  <li>what is target-profile or deployment-class planning rather than language truth,</li>
  <li>what is conformance truth,</li>
  <li>what is example material only,</li>
  <li>what is implementation workspace only,</li>
  <li>what is still future compiler/runtime work.</li>
</ul>

<hr/>

<h2 id="phase-2-stabilize-the-reference-execution-path">Phase 2 — Stabilize the reference execution path</h2>

<p>
Once the foundation is cleaner, the next step is to make the current executable path more disciplined, reproducible, and extensible.
</p>

<h3>Objective</h3>

<p>
Turn the first published slices into a reliable minimal reference path that proves stage boundaries through repeated use rather than one-off demonstrations.
</p>

<h3>Checklist</h3>

<ul>
  <li>[ ] Ensure each supported slice can be loaded, structurally validated, semantically validated, derived, lowered, emitted, and executed through a consistent path.</li>
  <li>[ ] Surface loadability, structural validity, semantic acceptance, preservation, and unsupported-but-valid situations consistently in the reference path.</li>
  <li>[ ] Standardize the observable artifacts produced by the reference path for the supported subset.</li>
  <li>[ ] Make the CLI path and expected outputs easy to run and inspect.</li>
  <li>[ ] Keep the pipeline stages explicit:
    <code>Loader -&gt; StructuralValidator -&gt; SemanticValidator -&gt; Deriver -&gt; Lowerer -&gt; ContractEmitter -&gt; Runtime</code>.
  </li>
  <li>[ ] Add new example slices only when they exercise a genuinely new boundary.</li>
  <li>[ ] Expand conformance around preserve, reject, unsupported, and stage-classification situations.</li>
  <li>[ ] Keep the runtime posture conservative and clearly non-normative.</li>
  <li>[ ] Prevent convenience scripts from silently becoming architecture.</li>
  <li>[ ] Demonstrate that different development and execution postures may legitimately use different runtime-service bundles without changing language meaning.</li>
</ul>

<h3>Recommended early slice growth</h3>

<ul>
  <li>[ ] structured case selection</li>
  <li>[ ] deterministic loop behavior</li>
  <li>[ ] basic collections / arrays</li>
  <li>[ ] sub-FROG invocation boundaries</li>
  <li>[ ] interface reuse as callable boundary</li>
  <li>[ ] inspectable execution surfaces</li>
</ul>

<h3>Exit condition</h3>

<p>
A bounded supported subset can be repeatedly processed end to end with inspectable intermediate artifacts and explicit expected outcomes.
</p>

<hr/>

<h2 id="phase-3-build-the-first-serious-compiler-path">Phase 3 — Build the first serious compiler path</h2>

<p>
This phase marks the transition from “reference executable path” to “credible compiler/runtime strategy”.
</p>

<h3>Objective</h3>

<p>
Show that FROG can feed a serious backend path without abandoning its own open IR or collapsing into one downstream private technology.
</p>

<h3>Checklist</h3>

<ul>
  <li>[ ] Stabilize a first serious standardized FROG execution IR subset for compilation-oriented use.</li>
  <li>[ ] Define the first backend-family strategy more explicitly.</li>
  <li>[ ] Produce the first real backend contract family suitable for a CPU-oriented path.</li>
  <li>[ ] Demonstrate one known compiler/runtime target as a downstream consumer.</li>
  <li>[ ] Keep the downstream target explicitly downstream from FROG IR.</li>
  <li>[ ] Preserve source attribution and recoverability across derivation and lowering.</li>
  <li>[ ] Add deterministic testing around compilation-oriented execution equivalence.</li>
  <li>[ ] Decide which target-profile classes and deployment-mode classes must become first-class named profile material for serious backend work.</li>
</ul>

<h3>Architectural rule</h3>

<pre>
correct direction

.frog source
   -> validation
   -> standardized FROG execution IR
   -> backend-specific lowering
   -> backend contract / target-facing handoff
   -> known compiler/runtime backend
   -> deployable artifact
</pre>

<pre>
incorrect shortcut

.frog source
   -> one private backend IR
   -> one private runtime
</pre>

<h3>Exit condition</h3>

<p>
A bounded supported subset can be prepared through a real backend-oriented path while preserving FROG’s own stage boundaries.
</p>

<hr/>

<h2 id="phase-4-build-the-first-serious-frog-ide">Phase 4 — Build the first serious FROG IDE</h2>

<p>
Once the language base and serious execution path are credible, the project can justify a serious IDE track rather than a superficial editor shell.
</p>

<h3>Objective</h3>

<p>
Deliver the first truly usable FROG IDE foundation with coherent authoring, inspectability, debug surfaces, and a future-proof Program Model.
</p>

<h3>Checklist</h3>

<ul>
  <li>[ ] Stabilize the IDE Program Model as the editable in-memory source authority for authoring.</li>
  <li>[ ] Build diagram editing for primitive nodes, structure nodes, wires, and sub-FROG calls.</li>
  <li>[ ] Build public-interface editing and reusable callable boundaries.</li>
  <li>[ ] Build front-panel editing with proper separation from public interface.</li>
  <li>[ ] Support both <code>widget_value</code> and <code>widget_reference</code> authoring flows.</li>
  <li>[ ] Implement a first serious palette model.</li>
  <li>[ ] Implement load/save roundtrip against canonical <code>.frog</code> source.</li>
  <li>[ ] Implement validation feedback aligned with source objects.</li>
  <li>[ ] Implement source-aligned execution highlighting and observability surfaces.</li>
  <li>[ ] Implement first debugging controls:
    pause,
    resume,
    breakpoint,
    single-step.
  </li>
  <li>[ ] Implement probes and watch surfaces.</li>
  <li>[ ] Implement snippets as reusable graphical transport.</li>
  <li>[ ] Implement deployment selection that can target different backend families, target profiles, and deployment modes without blurring their distinction.</li>
  <li>[ ] Implement convenience authoring that always normalizes back to canonical FROG content.</li>
</ul>

<h3>IDE maturity path</h3>

<pre>
viewer
   -> lightweight editor
   -> source-roundtripping authoring tool
   -> executable debugging IDE
   -> reusable development environment
   -> serious industrial platform
</pre>

<h3>Exit condition</h3>

<p>
A user can author, inspect, validate, execute, debug, and prepare deployment for a meaningful supported subset in one coherent graphical environment.
</p>

<hr/>

<h2 id="phase-5-expand-language-power-without-losing-clarity">Phase 5 — Expand language power without losing clarity</h2>

<p>
This phase broadens the language and toolchain toward real industrial breadth.
It must happen only after the foundation and serious path are stable enough.
</p>

<h3>Objective</h3>

<p>
Expand the usable language surface, execution depth, and reusable ecosystem power while preserving architectural discipline and inspectability.
</p>

<h3>Checklist</h3>

<ul>
  <li>[ ] Review primitive completeness across core computation categories.</li>
  <li>[ ] Expand structured control coverage where still missing.</li>
  <li>[ ] Refine sequential versus parallel structure semantics where required.</li>
  <li>[ ] Define a simpler and cleaner event model than historical complexity traps.</li>
  <li>[ ] Expand memory semantics carefully:
    delays,
    explicit local state,
    safe references,
    reusable state holders,
    and stronger controlled memory patterns.
  </li>
  <li>[ ] Expand collections, text, IO, signal, and interop libraries where genuinely required.</li>
  <li>[ ] Add stronger sub-FROG packaging and reusable component patterns.</li>
  <li>[ ] Expand named target-profile thinking for CPU, RT, embedded, GPU, FPGA, and microcontroller classes.</li>
  <li>[ ] Define stronger packaging, dependency, and deployment preparation rules.</li>
  <li>[ ] Define practical runtime-module strategies for development, debug, release, self-contained, and constrained deployment postures without creating one monolithic universal runtime.</li>
</ul>

<hr/>

<h2 id="phase-6-build-the-open-industrial-ecosystem">Phase 6 — Build the open industrial ecosystem</h2>

<p>
This is the ecosystem phase.
The goal is not imitation.
The goal is structural superiority.
</p>

<h3>Objective</h3>

<p>
Deliver an open graphical ecosystem that retains the strengths of graphical engineering workflows while removing their structural weaknesses.
</p>

<h3>To rival the historical model, FROG must provide</h3>

<ul>
  <li>[ ] fast and natural graphical authoring</li>
  <li>[ ] a usable and broad primitive palette</li>
  <li>[ ] reusable component authoring</li>
  <li>[ ] front-panel and UI workflow support</li>
  <li>[ ] real debugging, probes, and watch tools</li>
  <li>[ ] deployable local execution</li>
  <li>[ ] credible hardware and external-runtime interoperability</li>
  <li>[ ] deterministic target profiles where relevant</li>
  <li>[ ] an execution story that scales from prototyping to industrial deployment</li>
</ul>

<h3>To surpass the historical model, FROG must additionally provide</h3>

<ul>
  <li>[ ] fully open and inspectable canonical source</li>
  <li>[ ] fully open and inspectable execution-facing IR</li>
  <li>[ ] explicit source-to-IR-to-backend traceability</li>
  <li>[ ] explicit separation between language, IDE, runtime, backend, deployment, and vendor ecosystem</li>
  <li>[ ] multiple independent implementation potential</li>
  <li>[ ] cleaner interop and profile boundaries</li>
  <li>[ ] a cleaner compiler path</li>
  <li>[ ] less lock-in around tooling, runtime, deployment, and hardware</li>
  <li>[ ] stronger suitability for automation, AI tooling, code generation, static analysis, and modern collaboration workflows</li>
  <li>[ ] a usable conformance / certification / branding layer for serious ecosystem participation</li>
</ul>

<h3>Strategic superiority model</h3>

<pre>
historical proprietary model
   language + IDE + runtime + vendor stack are tightly coupled

FROG target model
   open language
   + open canonical source
   + open execution-facing IR
   + explicit conformance boundary
   + multiple toolchain potential
   + multiple backend/runtime potential
   + explicit deployment and target-profile surface
   + explicit ecosystem and certification layer
</pre>

<h3>Exit condition</h3>

<p>
FROG becomes a credible open industrial graphical programming platform with serious technical depth and real ecosystem gravity.
</p>

<hr/>

<h2 id="cross-cutting-workstreams">Cross-cutting workstreams</h2>

<h3>1. Specification coherence</h3>

<ul>
  <li>[x] architectural ownership is explicit in principle</li>
  <li>[~] cross-document closure is advanced but not fully complete</li>
  <li>[ ] no accidental duplicate normative homes remain</li>
</ul>

<h3>2. Conformance discipline</h3>

<ul>
  <li>[x] conformance posture exists</li>
  <li>[~] coverage is growing but still incomplete</li>
  <li>[ ] valid / invalid / preserve / reject coverage becomes broad enough for serious implementation comparison</li>
  <li>[ ] future certification policy can be layered on top cleanly</li>
</ul>

<h3>3. Source schema and validation</h3>

<ul>
  <li>[x] validation posture exists in principle</li>
  <li>[x] source-shape/schema posture is now explicit and repository-visible</li>
  <li>[~] validator expectations are now more repository-visible and partially machine-checkable</li>
  <li>[ ] source-shape/schema and validator closure becomes stable enough to count as a closed repository-level asset</li>
</ul>

<h3>4. Reference-path reproducibility</h3>

<ul>
  <li>[x] first slices exist</li>
  <li>[~] the path exists but is not yet fully standardized as a repeatable supported-subset pipeline</li>
  <li>[ ] artifact generation becomes stable and routine</li>
</ul>

<h3>5. Compiler/backend depth</h3>

<ul>
  <li>[x] the conceptual chain is explicit</li>
  <li>[~] backend-family / target-profile / deployment-mode architectural distinction is now explicit</li>
  <li>[ ] the first real backend path is stabilized</li>
  <li>[ ] deployable artifact stories become concrete</li>
</ul>

<h3>6. IDE maturity</h3>

<ul>
  <li>[x] the IDE layer is architecturally separated</li>
  <li>[ ] the first serious graphical IDE exists</li>
  <li>[ ] debugging and observability become industrially credible</li>
</ul>

<h3>7. Deployment and runtime posture</h3>

<ul>
  <li>[x] the project no longer assumes one universal runtime shape</li>
  <li>[~] implementation-side runtime-module thinking is explicit but not yet ecosystem-stable</li>
  <li>[ ] first reusable deployment bundles and runtime-module strategies become concrete</li>
  <li>[ ] target-profile-specific deployment depth becomes practically usable</li>
</ul>

<h3>8. Ecosystem and governance</h3>

<ul>
  <li>[x] governance direction exists</li>
  <li>[~] roadmap governance begins with this layer</li>
  <li>[ ] conformance, certification, branding, and ecosystem participation become practically usable</li>
</ul>

<hr/>

<h2 id="milestone-navigation">Milestone navigation</h2>

<p>
Detailed milestone tracking is maintained in:
</p>

<p>
<a href="./Milestones.md"><strong>Roadmap/Milestones.md</strong></a>
</p>

<hr/>

<h2 id="definition-of-success">Definition of success</h2>

<p>
FROG succeeds if it reaches the following end state:
</p>

<pre>
authoring
   -> serious graphical IDE

source
   -> open canonical .frog representation

validation
   -> explicit loadability
   -> explicit structural validation and source ownership
   -> explicit distinction from later semantic validation

meaning
   -> clean normative language semantics

execution form
   -> open standardized FROG execution IR

specialization
   -> explicit lowering and backend contract

realization
   -> multiple credible compiler/runtime/backend paths
   -> explicit target-profile and deployment depth
   -> no collapse into one monolithic hidden runtime

inspection
   -> serious observability, debugging, probes, and watch

ecosystem
   -> open specification, multiple implementations, clear conformance boundary,
      usable certification/governance layer, and durable industrial relevance
</pre>

<p>
That end state would mean that FROG has achieved its long-term objective:
</p>

<p>
<strong>take the best of graphical engineering workflows, remove their structural weaknesses, and build what a modern open graphical dataflow ecosystem should have become.</strong>
</p>

<hr/>

<p align="center">
  <strong>FROG Roadmap</strong><br/>
  Plan the closure path clearly. Keep the architecture explicit. Build the ecosystem deliberately.
</p>
