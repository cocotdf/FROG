

<h1 align="center">🐸 FROG Roadmap</h1>

<p align="center">
  <strong>Roadmap for the progressive closure of the FROG language, reference path, compiler stack, runtime path, and future IDE ecosystem</strong>
</p>

<p align="center">
  Roadmap start date: <strong>8 March 2026</strong>
</p>

<p align="center">
  <a href="#purpose-of-this-roadmap">Purpose</a> •
  <a href="#status-legend">Status legend</a> •
  <a href="#guiding-principles">Guiding principles</a> •
  <a href="#current-baseline">Current baseline</a> •
  <a href="#high-level-roadmap">High-level roadmap</a> •
  <a href="#phase-0-baseline-already-established">Phase 0</a> •
  <a href="#phase-1-close-the-v01-foundation">Phase 1</a> •
  <a href="#phase-2-stabilize-the-reference-execution-path">Phase 2</a> •
  <a href="#phase-3-build-the-first-serious-compiler-path">Phase 3</a> •
  <a href="#phase-4-build-the-first-serious-frog-ide">Phase 4</a> •
  <a href="#phase-5-expand-language-power-without-losing-clarity">Phase 5</a> •
  <a href="#phase-6-rival-and-surpass-the-historical-labview-model">Phase 6</a> •
  <a href="#cross-cutting-workstreams">Cross-cutting workstreams</a> •
  <a href="#milestone-map">Milestone map</a> •
  <a href="#definition-of-success">Definition of success</a>
</p>

<hr/>

<h2 id="purpose-of-this-roadmap">Purpose of this roadmap</h2>

<p>
This repository is intended to track the <strong>planned closure path</strong> of FROG as a full ecosystem effort.
It does <strong>not</strong> redefine the normative ownership of the main FROG specification repository.
</p>

<p>
Its role is to answer a practical project question:
</p>

<p><strong>What sequence of concrete steps must be completed to move from the currently published FROG specification baseline to a serious open graphical programming ecosystem with a credible compiler/runtime path and a future IDE that can rival and surpass the historical LabVIEW model?</strong></p>

<p>
The roadmap exists because a specification repository and a planning repository do not have the same job:
</p>

<ul>
  <li><strong>the FROG specification repository</strong> defines what the language is,</li>
  <li><strong>the roadmap repository</strong> defines in what order the project should be closed.</li>
</ul>

<hr/>

<h2 id="status-legend">Status legend</h2>

<ul>
  <li><strong>[x]</strong> completed or already established in the current working baseline</li>
  <li><strong>[~]</strong> in progress, partially established, or prepared but not yet fully closed</li>
  <li><strong>[ ]</strong> planned future work</li>
</ul>

<hr/>

<h2 id="guiding-principles">Guiding principles</h2>

<ul>
  <li>Keep the architectural boundaries explicit.</li>
  <li>Do not let reference implementation convenience become hidden language law.</li>
  <li>Do not collapse open IR into one backend-specific or runtime-private form.</li>
  <li>Do not confuse roadmap planning with normative specification ownership.</li>
  <li>Prefer small coherent closures over large speculative refactors.</li>
  <li>Keep the path from <code>.frog</code> source to deployable execution explicit and inspectable.</li>
  <li>Build an ecosystem that is stronger, clearer, and more portable than the historical proprietary graphical model.</li>
</ul>

<pre>
What the project must preserve

saved source           -> Expression
semantic truth         -> Language
derived execution form -> IR
backend specialization -> Lowering
consumable handoff     -> Backend contract
private realization    -> Runtime
authoring/debugging    -> IDE
planned closure path   -> Roadmap
</pre>

<hr/>

<h2 id="current-baseline">Current baseline</h2>

<p>
The current working baseline already includes substantial progress.
The project is no longer only an abstract design direction.
A meaningful first foundation is already present.
</p>

<h3>Already established or substantially in hand</h3>

<ul>
  <li>[x] FROG is explicitly structured as an open graphical dataflow language rather than a product-bound environment.</li>
  <li>[x] The core architectural split is established:
    <code>Expression</code>,
    <code>Language</code>,
    <code>IR</code>,
    <code>Libraries</code>,
    <code>Profiles</code>,
    <code>IDE</code>.
  </li>
  <li>[x] The source model distinguishes diagram, public interface, and front panel.</li>
  <li>[x] The widget model distinguishes <code>widget_value</code> and <code>widget_reference</code>.</li>
  <li>[x] The IR bundle already includes open execution-facing IR, derivation rules, construction rules, identity/mapping, lowering, and backend contract boundaries.</li>
  <li>[x] The repository already contains <code>Examples/</code>, <code>Conformance/</code>, and <code>Implementations/Reference/</code>.</li>
  <li>[x] The first published executable vertical slices exist:
    <code>01_pure_addition</code>,
    <code>02_ui_value_roundtrip</code>,
    <code>03_ui_property_write</code>,
    <code>04_stateful_feedback_delay</code>.
  </li>
  <li>[x] The reference implementation posture is explicitly non-normative and prototype-oriented.</li>
  <li>[x] The long-term direction toward a real compiler/runtime chain remains explicit:
    <code>.frog source -> validation -> FROG execution IR -> lowering -> backend contract -> backend/runtime</code>.
  </li>
  <li>[~] Repository-level landing-page alignment is being tightened so that the published root README fully reflects the real repository state.</li>
  <li>[ ] A separate roadmap repository and long-term milestone structure still need to be formalized and maintained over time.</li>
</ul>

<h3>Immediate interpretation of the current state</h3>

<pre>
FROG today
   |
   +-- strong architectural base
   +-- first executable reference slices
   +-- explicit non-normative reference path
   +-- no final production compiler pipeline yet
   +-- no full serious IDE yet
   +-- no full target and deployment ecosystem yet
</pre>

<hr/>

<h2 id="high-level-roadmap">High-level roadmap</h2>

<pre>
Phase 0  -> establish the architectural baseline and first executable proof slices
Phase 1  -> close the v0.1 normative foundation
Phase 2  -> stabilize the reference execution path
Phase 3  -> build the first serious compiler/backend path
Phase 4  -> build the first serious FROG IDE
Phase 5  -> expand language power without losing clarity
Phase 6  -> rival and surpass the historical LabVIEW model
</pre>

<p>
The logic is intentionally staged:
</p>

<pre>
specification closure
        ->
reference-path stability
        ->
compiler/runtime credibility
        ->
IDE credibility
        ->
language breadth and ecosystem depth
        ->
clear superiority as an open graphical platform
</pre>

<hr/>

<h2 id="phase-0-baseline-already-established">Phase 0 — Baseline already established</h2>

<p>
This phase corresponds to the work that had to exist before a serious roadmap became useful.
Most of it is already achieved.
</p>

<h3>Phase 0 objective</h3>

<p>
Establish a durable architectural basis and prove that the specification can already support a first disciplined executable path without collapsing the language into one private implementation shortcut.
</p>

<h3>Phase 0 checklist</h3>

<ul>
  <li>[x] Establish the six core specification families.</li>
  <li>[x] Separate source, semantics, IR, libraries, profiles, and IDE responsibilities.</li>
  <li>[x] Publish the source-level model for diagram, interface, and front panel.</li>
  <li>[x] Publish the early IR bundle with explicit downstream boundaries.</li>
  <li>[x] Publish the first intrinsic library families.</li>
  <li>[x] Publish the first optional profile direction.</li>
  <li>[x] Publish the IDE architectural direction and Program Model posture.</li>
  <li>[x] Publish named examples.</li>
  <li>[x] Publish early conformance posture.</li>
  <li>[x] Publish a non-normative reference implementation workspace.</li>
  <li>[x] Prove the first executable vertical slices.</li>
  <li>[~] Recontextualize the repository landing page around the real published state.</li>
</ul>

<h3>Phase 0 exit condition</h3>

<p>
The project already has a coherent foundation and an inspectable early execution story.
This exit condition is substantially met.
</p>

<hr/>

<h2 id="phase-1-close-the-v01-foundation">Phase 1 — Close the v0.1 foundation</h2>

<p>
This is the next essential closure phase.
Its purpose is not to widen the language aggressively.
Its purpose is to make the current base cleaner, firmer, and easier to build on.
</p>

<h3>Phase 1 objective</h3>

<p>
Turn the current architectural baseline into a tighter and more explicit v0.1 foundation with fewer ambiguities and better repository-level coherence.
</p>

<h3>Phase 1 checklist</h3>

<ul>
  <li>[~] Align the repository root documentation with the real published state.</li>
  <li>[ ] Close remaining cross-document ambiguities between <code>Expression</code>, <code>Language</code>, and <code>IR</code>.</li>
  <li>[ ] Make the ownership of normative truth versus implementation convenience fully unambiguous.</li>
  <li>[ ] Review the first conformance material for coverage gaps against already published example slices.</li>
  <li>[ ] Ensure every currently published example slice has an explicit expected-outcome posture.</li>
  <li>[ ] Identify any remaining duplicate, competing, or weakly-owned explanations across the repository.</li>
  <li>[ ] Publish the roadmap repository as a clearly non-normative planning layer.</li>
</ul>

<h3>Phase 1 exit condition</h3>

<p>
A new reader should be able to understand:
</p>

<ul>
  <li>what is already published,</li>
  <li>what is normative,</li>
  <li>what is only example material,</li>
  <li>what is conformance expectation,</li>
  <li>what is non-normative executable reference work,</li>
  <li>what is still future compiler/runtime work.</li>
</ul>

<h3>Why this phase matters</h3>

<p>
Without this closure, every later milestone risks drifting because the project will be broadening itself before it has fully stabilized its baseline.
</p>

<hr/>

<h2 id="phase-2-stabilize-the-reference-execution-path">Phase 2 — Stabilize the reference execution path</h2>

<p>
Once the baseline is clean, the next step is to make the current executable path more disciplined, reproducible, and extensible.
</p>

<h3>Phase 2 objective</h3>

<p>
Turn the first reference slices into a reliable minimal reference path that proves stage boundaries through repeated use rather than through one-off demonstrations.
</p>

<h3>Phase 2 checklist</h3>

<ul>
  <li>[ ] Ensure each published example slice can be loaded, validated, derived, lowered, emitted, and executed through a consistent reference path.</li>
  <li>[ ] Standardize the observable artifacts produced by the reference path for the currently supported subset.</li>
  <li>[ ] Make the CLI path and artifact expectations easy to run and inspect.</li>
  <li>[ ] Keep the pipeline stages explicit:
    <code>Loader -> Validator -> Deriver -> Lowerer -> ContractEmitter -> Runtime</code>.
  </li>
  <li>[ ] Add more compact example slices only when they exercise a genuinely new boundary.</li>
  <li>[ ] Expand conformance cases around preservation, rejection, and unsupported situations.</li>
  <li>[ ] Keep the current runtime posture deliberately conservative and host-oriented.</li>
  <li>[ ] Prevent monolithic convenience scripts from silently becoming architecture.</li>
</ul>

<h3>Recommended early slice growth after the first four</h3>

<ul>
  <li>[ ] structured case selection</li>
  <li>[ ] deterministic loop behavior</li>
  <li>[ ] simple array / collection handling</li>
  <li>[ ] sub-FROG call boundaries</li>
  <li>[ ] explicit interface reuse as node invocation</li>
  <li>[ ] selected probeable / inspectable execution surfaces</li>
</ul>

<h3>Phase 2 exit condition</h3>

<p>
The project has a small but reliable execution story.
A published supported subset can be repeatedly processed end to end through the reference path with inspectable intermediate artifacts and expected results.
</p>

<hr/>

<h2 id="phase-3-build-the-first-serious-compiler-path">Phase 3 — Build the first serious compiler path</h2>

<p>
This phase marks the transition from “reference executable path” to “credible compiler/runtime strategy”.
</p>

<h3>Phase 3 objective</h3>

<p>
Show that FROG can feed a serious backend path without abandoning its own open IR or collapsing into one downstream technology.
</p>

<h3>Phase 3 checklist</h3>

<ul>
  <li>[ ] Stabilize a first serious standardized FROG execution IR subset for compilation-oriented use.</li>
  <li>[ ] Define the first backend-family strategy more explicitly.</li>
  <li>[ ] Produce a first backend contract family suitable for a real CPU-oriented path.</li>
  <li>[ ] Demonstrate one known compiler/runtime target as a downstream consumer.</li>
  <li>[ ] Keep the downstream target explicitly downstream from FROG IR.</li>
  <li>[ ] Show source attribution and recoverability across derivation and lowering boundaries.</li>
  <li>[ ] Add deterministic testing around compilation-oriented execution equivalence for supported slices.</li>
</ul>

<h3>Important architectural rule</h3>

<pre>
Correct direction

.frog source
   -> validation
   -> standardized FROG execution IR
   -> backend-specific lowering
   -> backend contract / backend-oriented IR
   -> known compiler/runtime backend
   -> deployable artifact
</pre>

<p>
The project must <strong>not</strong> redefine this path as:
</p>

<pre>
incorrect shortcut

.frog source
   -> one private backend IR
   -> one private runtime
</pre>

<h3>Potential first backend target family</h3>

<p>
A CPU-oriented backend path is the most useful early serious target.
A backend such as LLVM may become a strong downstream illustrative target,
but it must remain downstream from FROG’s own execution IR rather than becoming the normative definition of FROG itself.
</p>

<h3>Phase 3 exit condition</h3>

<p>
A clearly bounded supported subset can be compiled or prepared through a real backend-oriented path while preserving FROG’s own architectural boundaries.
</p>

<hr/>

<h2 id="phase-4-build-the-first-serious-frog-ide">Phase 4 — Build the first serious FROG IDE</h2>

<p>
Once the language base and serious execution path are credible, the project can justify a serious IDE track rather than a superficial editor shell.
</p>

<h3>Phase 4 objective</h3>

<p>
Deliver the first truly usable FROG IDE foundation with coherent authoring, inspectability, debug surfaces, and a future-proof Program Model.
</p>

<h3>Phase 4 checklist</h3>

<ul>
  <li>[ ] Stabilize the IDE Program Model as the editable in-memory source authority for authoring.</li>
  <li>[ ] Build diagram editing for primitive nodes, structure nodes, wires, and sub-FROG calls.</li>
  <li>[ ] Build interface editing and connector-facing reuse support.</li>
  <li>[ ] Build front-panel editing with proper separation from public interface.</li>
  <li>[ ] Support both <code>widget_value</code> and <code>widget_reference</code> editing flows.</li>
  <li>[ ] Implement a first serious palette model.</li>
  <li>[ ] Implement load/save roundtrip against canonical <code>.frog</code> source.</li>
  <li>[ ] Implement validation feedback aligned with source objects.</li>
  <li>[ ] Implement source-aligned execution highlighting and observability surfaces.</li>
  <li>[ ] Implement first debugging controls: pause, resume, breakpoint, single-step.</li>
  <li>[ ] Implement probes and watch surfaces.</li>
  <li>[ ] Implement snippets as reusable graphical transport.</li>
  <li>[ ] Implement Express authoring as a convenience layer that always normalizes back to canonical FROG content.</li>
</ul>

<h3>Phase 4 exit condition</h3>

<p>
The project has a serious IDE foundation rather than only a specification and a command-line prototype path.
A user can author, inspect, validate, execute, and debug a meaningful supported subset in a coherent graphical environment.
</p>

<h3>First visual capability map</h3>

<pre>
IDE maturity path

viewer
  -> lightweight editor
  -> source-roundtripping authoring tool
  -> executable debugging IDE
  -> reusable development environment
  -> serious industrial platform
</pre>

<hr/>

<h2 id="phase-5-expand-language-power-without-losing-clarity">Phase 5 — Expand language power without losing clarity</h2>

<p>
This phase broadens the language and toolchain toward real industrial breadth.
It must be done only after the foundation and serious path are stable enough.
</p>

<h3>Phase 5 objective</h3>

<p>
Expand the usable language surface, execution depth, and reusable ecosystem power while preserving architectural discipline and inspectability.
</p>

<h3>Phase 5 checklist</h3>

<ul>
  <li>[ ] Review primitive completeness across core computation categories.</li>
  <li>[ ] Expand structured control coverage where still missing.</li>
  <li>[ ] Refine sequential versus parallel structure semantics where required.</li>
  <li>[ ] Define a simpler and cleaner event model than the historical complexity traps of legacy graphical platforms.</li>
  <li>[ ] Expand memory semantics carefully:
    delays,
    explicit local state,
    safe references,
    reusable state holders,
    and stronger controlled memory patterns.
  </li>
  <li>[ ] Expand collections, text, IO, signal, and interop libraries where genuinely required.</li>
  <li>[ ] Add stronger sub-FROG packaging and reusable component patterns.</li>
  <li>[ ] Expand target-profile thinking for CPU, RT, embedded, GPU, FPGA, and microcontroller classes.</li>
  <li>[ ] Define stronger packaging, dependency, and deployment preparation rules.</li>
</ul>

<h3>Key warning for this phase</h3>

<p>
This phase is where many projects become incoherent.
Breadth must grow only after enough closure exists to prevent the platform from becoming a pile of special cases.
</p>

<hr/>

<h2 id="phase-6-rival-and-surpass-the-historical-labview-model">Phase 6 — Rival and surpass the historical LabVIEW model</h2>

<p>
This is the ambitious ecosystem phase.
The target is not imitation.
The target is structural superiority.
</p>

<h3>Phase 6 objective</h3>

<p>
Deliver an open graphical ecosystem that retains the strengths historically associated with LabVIEW while removing its structural weaknesses.
</p>

<h3>To rival LabVIEW, FROG must provide</h3>

<ul>
  <li>[ ] fast and natural graphical authoring</li>
  <li>[ ] a usable and broad palette</li>
  <li>[ ] reusable component authoring</li>
  <li>[ ] front-panel and UI workflow support</li>
  <li>[ ] real debugging, probes, and watch tools</li>
  <li>[ ] deployable local execution</li>
  <li>[ ] credible hardware and external-runtime interoperability</li>
  <li>[ ] deterministic target profiles where relevant</li>
  <li>[ ] an execution story that can scale from prototyping to industrial deployment</li>
</ul>

<h3>To surpass LabVIEW, FROG must additionally provide</h3>

<ul>
  <li>[ ] fully open and inspectable canonical source</li>
  <li>[ ] fully open and inspectable execution-facing IR</li>
  <li>[ ] explicit source-to-IR-to-backend traceability</li>
  <li>[ ] explicit separation between language, IDE, runtime, and vendor ecosystem</li>
  <li>[ ] multiple independent implementation potential</li>
  <li>[ ] cleaner interop and profile boundaries</li>
  <li>[ ] clearer execution architecture and compiler path</li>
  <li>[ ] less lock-in around tooling, runtime, deployment, and hardware</li>
  <li>[ ] stronger suitability for automation, AI tooling, code generation, static analysis, and modern collaboration workflows</li>
</ul>

<h3>Strategic superiority model</h3>

<pre>
Historical proprietary model
   language + IDE + runtime + vendor stack are tightly coupled

FROG target model
   open language
   + open source representation
   + open execution-facing IR
   + multiple toolchain potential
   + multiple runtime/backend potential
   + explicit conformance/certification boundary
</pre>

<h3>Phase 6 exit condition</h3>

<p>
FROG is not merely an interesting open language project.
It is a credible open industrial graphical programming platform with a serious IDE, a serious compiler/runtime path, and enough ecosystem depth to become a practical alternative and long-term successor model.
</p>

<hr/>

<h2 id="cross-cutting-workstreams">Cross-cutting workstreams</h2>

<p>
These workstreams span multiple phases and should be tracked continuously.
</p>

<h3>1. Specification coherence</h3>

<ul>
  <li>[x] architectural ownership is explicit in principle</li>
  <li>[ ] remaining cross-document ambiguities are fully removed</li>
  <li>[ ] no accidental duplicate normative homes remain</li>
</ul>

<h3>2. Conformance discipline</h3>

<ul>
  <li>[x] conformance posture exists</li>
  <li>[ ] valid/invalid/preserve/reject coverage becomes broad enough for serious implementation comparison</li>
  <li>[ ] future certified-implementation policy can be layered on top cleanly</li>
</ul>

<h3>3. Reference-path reproducibility</h3>

<ul>
  <li>[x] first slices exist</li>
  <li>[ ] repeatable artifact generation is stable for the supported subset</li>
  <li>[ ] new slices widen scope only when they add new boundary value</li>
</ul>

<h3>4. Compiler/backend depth</h3>

<ul>
  <li>[x] the conceptual chain is explicit</li>
  <li>[ ] the first real backend path is stabilized</li>
  <li>[ ] deployable artifact stories become concrete</li>
</ul>

<h3>5. IDE maturity</h3>

<ul>
  <li>[x] the IDE layer is architecturally separated</li>
  <li>[ ] the first serious graphical IDE exists</li>
  <li>[ ] execution observability and debugging become production-credible</li>
</ul>

<h3>6. Ecosystem growth</h3>

<ul>
  <li>[x] governance direction exists</li>
  <li>[ ] roadmap governance exists</li>
  <li>[ ] conformance, certification, branding, and ecosystem participation become operationally usable</li>
</ul>

<hr/>

<h2 id="milestone-map">Milestone map</h2>

<pre>
M0  [x] Architectural separation established
M1  [x] First published example slices established
M2  [x] Non-normative reference implementation posture established
M3  [~] Repository-level recontextualization aligned with the real published state
M4  [ ] Roadmap repository published and maintained
M5  [ ] v0.1 baseline closed with cleaner conformance and ownership boundaries
M6  [ ] Stable repeatable reference execution path for the supported subset
M7  [ ] First serious backend-oriented compiler path
M8  [ ] First serious FROG IDE foundation
M9  [ ] Expanded language breadth and execution depth
M10 [ ] Practical open industrial graphical platform with clear superiority over the legacy proprietary model
</pre>

<hr/>

<h2 id="definition-of-success">Definition of success</h2>

<p>
FROG succeeds if it can reach the following end state:
</p>

<pre>
authoring
   -> serious graphical IDE

source
   -> open canonical .frog representation

meaning
   -> clean normative language semantics

execution form
   -> open standardized FROG execution IR

specialization
   -> explicit lowering and backend contract

realization
   -> multiple credible compiler/runtime/backend paths

inspection
   -> serious observability, debugging, probes, and watch

ecosystem
   -> open specification, multiple implementations, clear conformance boundary
</pre>

<p>
That end state would mean FROG has achieved the project’s long-term objective:
</p>

<p><strong>take the best of LabVIEW, remove its structural weaknesses, and build what a modern open graphical dataflow ecosystem should have become.</strong></p>

<hr/>

<p align="center">
  <strong>FROG Roadmap</strong><br/>
  Plan the closure path clearly. Keep the architecture explicit. Build the ecosystem deliberately.
</p>
