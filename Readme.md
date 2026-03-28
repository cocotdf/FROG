<p align="center">
  <img src="FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG — Free Open Graphical Language</h1>

<p align="center">
  <strong>Free Open Graphical Dataflow Programming Language</strong><br/>
  FROG is an open, hardware-agnostic graphical dataflow programming language designed to describe computation as explicit executable graphs while remaining accessible, explicit, inspectable, portable, and scalable across heterogeneous execution targets.
</p>

<p align="center">
  Specification work initiated: <strong>8 March 2026</strong>
</p>

<p align="center">
  <a href="#what-is-frog">What is FROG?</a> •
  <a href="#what-this-repository-defines">What this repository defines</a> •
  <a href="#published-repository-state">Published repository state</a> •
  <a href="#positioning">Positioning</a> •
  <a href="#breaking-the-syntax-first-bottleneck">Breaking the syntax-first bottleneck</a> •
  <a href="#why-frog-exists">Why FROG exists</a> •
  <a href="#dataflow-programming">Dataflow programming</a> •
  <a href="#from-prototyping-to-critical-systems">From prototyping to critical systems</a> •
  <a href="#core-concept-diagram-front-panel-and-public-interface">Core concept</a> •
  <a href="#repository-structure">Repository structure</a> •
  <a href="#internal-documentation-map">Internal documentation map</a> •
  <a href="#recommended-reading-path">Recommended reading path</a> •
  <a href="#specification-architecture">Specification architecture</a> •
  <a href="#program-representation">Program representation</a> •
  <a href="#execution-architecture">Execution architecture</a> •
  <a href="#execution-observability-debugging-and-inspection">Execution observability, debugging, and inspection</a> •
  <a href="#execution-targets">Execution targets</a> •
  <a href="#open-industrial-hardware-standard">Open industrial hardware standard</a> •
  <a href="#security-and-optimization-by-design">Security &amp; optimization</a> •
  <a href="#interoperability">Interoperability</a> •
  <a href="#separation-of-language-and-tooling">Language separation</a> •
  <a href="#governance-and-ecosystem">Governance and ecosystem</a> •
  <a href="#project-status">Project status</a> •
  <a href="#license">License</a>
</p>

<hr/>

<h2 id="what-is-frog">What is FROG?</h2>

<p>
FROG is an open, hardware-agnostic <strong>graphical dataflow programming language</strong>.
It represents computation as explicit executable graphs rather than as syntax-first sequences of textual instructions.
</p>

<p>
Instead of describing a program primarily through ordered text, FROG describes a program through:
</p>

<ul>
  <li>typed nodes,</li>
  <li>typed ports,</li>
  <li>directed graph connections,</li>
  <li>structured control regions,</li>
  <li>explicit public interface boundaries,</li>
  <li>optional front-panel widgets and interaction layers.</li>
</ul>

<p>
Execution emerges from data availability, dependency structure, explicit control constructs, intrinsic standardized primitive behavior, optional profile-owned capability behavior, and explicit local-memory semantics rather than from manually authored instruction order.
</p>

<p>
FROG is designed to remain independent from any specific IDE, compiler, runtime, operating system, or hardware vendor.
That separation provides a durable basis for multiple independent implementations and long-term industrial interoperability.
</p>

<p>
FROG is intended to scale from accessible graphical authoring to demanding execution contexts such as industrial automation, embedded systems, heterogeneous compute targets, and future conforming execution ecosystems.
</p>

<hr/>

<h2 id="what-this-repository-defines">What this repository defines</h2>

<p>
This repository defines the <strong>published FROG specification</strong>.
It is the repository where the language and its surrounding specification layers are written, clarified, stabilized, and progressively closed.
</p>

<p>
Its role is to provide a durable open foundation for future:
</p>

<ul>
  <li>IDEs,</li>
  <li>validators,</li>
  <li>runtimes,</li>
  <li>compilers,</li>
  <li>execution backends,</li>
  <li>profile-supporting toolchains,</li>
  <li>ecosystem services and integrations.</li>
</ul>

<p>
The repository also contains repository-level support material that helps make the specification inspectable in practice:
named examples, conformance material, and a non-normative reference implementation workspace.
Those areas support the published specification, but they do not replace its ownership boundaries.
</p>

<p>
This repository does <strong>not</strong> define one mandatory product implementation.
It does not equate the language with one IDE, one runtime, one compiler, one vendor stack, or one deployment model.
</p>

<ul>
  <li><strong>FROG is not an IDE.</strong></li>
  <li><strong>FROG is not a single runtime.</strong></li>
  <li><strong>FROG is not a single compiler.</strong></li>
  <li><strong>FROG is not a vendor product.</strong></li>
  <li><strong>FROG is an open language specification with distinct source, semantic, IR, library, profile, and IDE-facing layers.</strong></li>
</ul>

<hr/>

<h2 id="published-repository-state">Published repository state</h2>

<p>
At the current published state, the repository already contains the six core architectural specification families:
<code>Expression/</code>,
<code>Language/</code>,
<code>IR/</code>,
<code>Libraries/</code>,
<code>Profiles/</code>,
and <code>IDE/</code>.
These remain the primary ownership layers of the published language specification.
</p>

<p>
The repository also contains three important repository-level support areas:
</p>

<ul>
  <li><strong><code>Examples/</code></strong> — named source examples and the first executable vertical slices,</li>
  <li><strong><code>Conformance/</code></strong> — public accept / reject / preserve expectations for the published repository state,</li>
  <li><strong><code>Implementations/Reference/</code></strong> — a non-normative reference implementation workspace used to exercise a disciplined minimal execution path.</li>
</ul>

<p>
The currently published example slices are:
</p>

<ul>
  <li><code>01_pure_addition</code>,</li>
  <li><code>02_ui_value_roundtrip</code>,</li>
  <li><code>03_ui_property_write</code>,</li>
  <li><code>04_stateful_feedback_delay</code>.</li>
</ul>

<p>
The published repository now also makes the overall execution corridor more explicit:
canonical source ownership and source-schema posture are published in <code>Expression/</code>,
validated program meaning is staged in <code>Language/</code>,
open execution-facing representation is staged in <code>IR/</code>,
and the repository-level examples, conformance material, and reference implementation workspace together expose the first repository-visible executable vertical slices.
</p>

<p>
Together, these published materials show that the repository is no longer only architectural prose.
It already exposes a first repository-visible reference path where a controlled published subset can be loaded, structurally validated, semantically validated, derived into a canonical open execution-facing representation, lowered toward a backend family, emitted as a backend-facing contract, and consumed by a reference runtime experiment.
</p>

<p>
That published reality does <strong>not</strong> yet mean that the repository already contains:
</p>

<ul>
  <li>the final normative production compiler pipeline,</li>
  <li>the final fully stabilized FROG backend-family ecosystem,</li>
  <li>one definitive production runtime architecture.</li>
</ul>

<p>
The current repository state should therefore be read as:
published architectural specification first,
published source-schema and conformance posture for the current subset,
and published non-normative executable reference prototypes for a controlled subset.
</p>

<hr/>

<h2 id="positioning">Positioning</h2>

<p>
FROG is designed to combine the accessibility of graphical programming with the execution depth required for deterministic, industrial, embedded, and high-performance systems.
</p>

<p>
Its ambition is to reduce the historical trade-off between:
</p>

<ul>
  <li>ease of expression,</li>
  <li>clarity of system design,</li>
  <li>deterministic execution,</li>
  <li>deployment scalability,</li>
  <li>hardware integration depth.</li>
</ul>

<p align="center">
  <img src="frog-orville-chart.png" alt="FROG positioning chart" width="640" />
</p>

<p align="center">
  <em>
    FROG aims to combine graphical accessibility, explicit dataflow, and system-grade execution in one open language model.
  </em>
</p>

<hr/>

<h2 id="breaking-the-syntax-first-bottleneck">Breaking the syntax-first bottleneck</h2>

<p>
A major barrier in many traditional programming environments is that useful system design often begins only after a long period of syntax learning, pattern memorization, and language-specific implementation habits.
</p>

<p>
This creates an inversion:
instead of starting from the system that should exist,
developers often start from the syntax they already know how to write.
</p>

<p>
That inversion limits experimentation and slows architectural thinking.
It encourages people to ask:
</p>

<p><strong>“What can I build with the implementation techniques I already master?”</strong></p>

<p>
rather than:
</p>

<p><strong>“What system should I build, and how should its behavior be expressed?”</strong></p>

<p>
FROG is designed to reduce that bottleneck by moving more of the developer’s effort toward:
</p>

<ul>
  <li>data movement,</li>
  <li>system structure,</li>
  <li>interfaces,</li>
  <li>control regions,</li>
  <li>state visibility,</li>
  <li>execution semantics.</li>
</ul>

<p>
The goal is not to eliminate engineering complexity.
The goal is to shift complexity toward the system itself rather than toward syntax-first representation.
</p>

<hr/>

<h2 id="why-frog-exists">Why FROG exists</h2>

<p>
Graphical dataflow programming has already demonstrated major advantages in many engineering domains:
</p>

<ul>
  <li>natural parallelism,</li>
  <li>clear orchestration of behavior,</li>
  <li>strong correspondence between software structure and system behavior,</li>
  <li>high productivity for engineers, scientists, and domain experts,</li>
  <li>strong suitability for instrumentation, control, and observable systems.</li>
</ul>

<p>
However, many historical graphical environments have been tightly coupled to proprietary ecosystems where language, tooling, runtime, and hardware support are inseparable.
</p>

<p>
That model limits portability, slows independent ecosystem growth, and prevents multiple actors from implementing the same language cleanly.
</p>

<p>
FROG exists to define an <strong>open language specification</strong> for graphical dataflow programming that remains separate from:
</p>

<ul>
  <li>any single IDE,</li>
  <li>any single runtime,</li>
  <li>any single compiler,</li>
  <li>any single hardware vendor.</li>
</ul>

<p>
This repository therefore defines the language standard and the surrounding specification layers needed to support future conforming implementations.
The objective is to make it possible for different actors to build compatible FROG tooling while targeting one shared open language definition.
</p>

<hr/>

<h2 id="dataflow-programming">Dataflow programming</h2>

<p>
FROG follows a true <strong>dataflow execution model</strong>.
</p>

<p>
In instruction-sequenced programming, execution is primarily described as ordered steps.
In dataflow programming, operations become executable when their required input data is available.
</p>

<pre>
Traditional execution

A → B → C → D


Dataflow execution

   A
  / \
 B   C
  \ /
   D
</pre>

<p>
Execution order therefore emerges from dependencies rather than from manually authored textual ordering.
This model enables:
</p>

<ul>
  <li>automatic parallelism where valid,</li>
  <li>clear dependency visibility,</li>
  <li>deterministic execution models where required,</li>
  <li>efficient mapping to heterogeneous hardware.</li>
</ul>

<hr/>

<h2 id="from-prototyping-to-critical-systems">From prototyping to critical systems</h2>

<p>
FROG is designed to support both rapid experimentation and demanding deployment.
</p>

<p>
The same programming model is intended to scale across domains such as:
</p>

<ul>
  <li>scientific computing,</li>
  <li>measurement and control,</li>
  <li>industrial automation,</li>
  <li>embedded systems,</li>
  <li>real-time control,</li>
  <li>microcontroller-oriented execution,</li>
  <li>accelerated and edge computing,</li>
  <li>high-performance systems.</li>
</ul>

<p>
Usability and execution depth are treated as complementary goals rather than mutually exclusive ones.
</p>

<hr/>

<h2 id="core-concept-diagram-front-panel-and-public-interface">Core concept: Diagram, Front Panel, and Public Interface</h2>

<p>
A FROG program combines multiple related but distinct source-level concepts.
The repository deliberately separates them so that execution meaning, public API, and UI-facing authoring remain coherent over time.
</p>

<h3>Diagram — the authoritative executable graph</h3>

<p>
The diagram defines the executable logic of the program.
It is the authoritative source-level execution graph.
</p>

<p>
It contains:
</p>

<ul>
  <li>primitive nodes,</li>
  <li>structure nodes,</li>
  <li>sub-FROG invocations,</li>
  <li>interface boundary nodes,</li>
  <li>widget-related graph nodes,</li>
  <li>directed graph edges,</li>
  <li>source-level annotations and documentation.</li>
</ul>

<p>
The diagram expresses:
</p>

<ul>
  <li>ordinary computation,</li>
  <li>control structures such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>,</li>
  <li>public interface participation through <code>interface_input</code> and <code>interface_output</code>,</li>
  <li>front-panel value participation through <code>widget_value</code>,</li>
  <li>object-style widget interaction through <code>widget_reference</code> and <code>frog.ui.*</code> primitives,</li>
  <li>optional profile-owned capability usage where supported by the active implementation,</li>
  <li>explicit local memory and valid cycles.</li>
</ul>

<h3>Public interface — the reusable program boundary</h3>

<p>
The public interface defines the typed reusable boundary of a FROG.
It describes the inputs and outputs that matter when a FROG is invoked, embedded, reused, validated, documented, or integrated by other FROGs or tools.
</p>

<p>
The public interface is not owned by the front panel.
It is defined independently and participates in the diagram through <code>interface_input</code> and <code>interface_output</code>.
</p>

<h3>Front Panel — the interaction layer</h3>

<p>
The front panel defines the graphical interaction layer of the program.
It contains widget instances, layout information, composition, styling, and optional UI-library references.
</p>

<p>
The front panel is not the public API of the FROG and it is not the execution graph of the FROG.
It defines how users see and interact with the program.
</p>

<p>
A FROG MAY exist without a front panel.
When absent, the program remains a valid executable graphical artifact centered on its diagram and public interface.
</p>

<p>
Primary widget values participate naturally in execution through <code>widget_value</code> nodes in the diagram.
There is no separate canonical front-panel binding section for ordinary value flow.
</p>

<h3>Widget interaction model</h3>

<p>
FROG distinguishes two widget interaction paths:
</p>

<ul>
  <li><strong>natural value path</strong> — widget primary value participation through <code>widget_value</code>,</li>
  <li><strong>object-style path</strong> — explicit widget access through <code>widget_reference</code> together with <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code>.</li>
</ul>

<p>
These two paths are related but distinct.
This keeps ordinary dataflow wiring simple while preserving a clean long-term object model for UI interaction.
</p>

<hr/>

<h2 id="repository-structure">Repository structure</h2>

<p>
This repository is organized by <strong>architectural responsibility</strong> plus a small number of repository-level support areas.
The six core specification families remain the architectural baseline of FROG.
The support areas exist to make that baseline more inspectable, testable, and executable without moving normative ownership away from the specification layers.
</p>

<pre><code>FROG/
│
├── Conformance/                      Public accept / reject / preserve expectations
├── Examples/                         Named source examples and first executable vertical slices
├── Expression/                       Canonical source specification for .frog programs
├── IDE/                              IDE architecture, authoring, observability, debugging, and inspection
├── IR/                               Canonical open execution-facing representation and downstream handoff boundaries
├── Implementations/
│   └── Reference/                    Non-normative reference implementation workspace and executable prototypes
├── Language/                         Normative execution semantics for validated program meaning
├── Libraries/                        Intrinsic standardized primitive-library specifications
├── Profiles/                         Optional standardized capability-family specifications
├── Roadmap/                          Non-normative closure sequencing and milestone tracking
├── Strategy/
│   └── Heilmeier/                    Strategic framing layer distinct from normative ownership
│
├── CLA.md                            Contributor license agreement requirements
├── CONTRIBUTING.md                   Contribution process and contribution rules
├── GOVERNANCE.md                     Governance, stewardship, and ecosystem model
├── FROG logo.svg                     Official logo asset
├── LICENSE                           Repository license
├── Readme.md                         Repository landing page and architectural overview
└── frog-orville-chart.png            Positioning illustration used by the repository
</code></pre>

<p>
The six core specification families are:
</p>

<ul>
  <li><strong><code>Expression/</code></strong></li>
  <li><strong><code>Language/</code></strong></li>
  <li><strong><code>IR/</code></strong></li>
  <li><strong><code>Libraries/</code></strong></li>
  <li><strong><code>Profiles/</code></strong></li>
  <li><strong><code>IDE/</code></strong></li>
</ul>

<p>
The current repository-level support areas are:
</p>

<ul>
  <li><strong><code>Examples/</code></strong> — named source cases and compact executable slices,</li>
  <li><strong><code>Conformance/</code></strong> — expected outcomes for validation, preservation, and rejection,</li>
  <li><strong><code>Implementations/Reference/</code></strong> — non-normative prototype workspace used to exercise the current reference path.</li>
</ul>

<p>
The repository also contains:
</p>

<ul>
  <li><strong><code>Strategy/Heilmeier/</code></strong> — strategic framing that remains distinct from normative ownership,</li>
  <li><strong><code>Roadmap/</code></strong> — non-normative sequencing and milestone tracking for project closure.</li>
</ul>

<h3><code>Conformance/</code> — public conformance material</h3>

<p>
This directory contains the public conformance surface for the published FROG specification.
Its role is to make expected outcomes explicit:
what a conforming toolchain should accept,
what it should reject,
what distinctions must be preserved,
and what unsupported situations must be reported explicitly rather than silently reinterpreted.
</p>

<p>
Its reading corridor is intentionally staged:
</p>

<pre><code>loadability
   -&gt;
structural validity
   -&gt;
semantic acceptance
   -&gt;
preservation expectations
</code></pre>

<h3><code>Examples/</code> — named source examples and first executable slices</h3>

<p>
This directory contains minimal example programs for the published FROG specification.
Its role is to provide compact named source cases that help make the architecture readable, teach boundary distinctions, and support the first executable vertical slices without turning examples into hidden semantic law.
</p>

<p>
At the current published state, the first visible example slices are:
</p>

<ul>
  <li><code>01_pure_addition</code>,</li>
  <li><code>02_ui_value_roundtrip</code>,</li>
  <li><code>03_ui_property_write</code>,</li>
  <li><code>04_stateful_feedback_delay</code>.</li>
</ul>

<h3><code>Expression/</code> — canonical source specification</h3>

<p>
This directory defines the canonical <code>.frog</code> source format.
It describes what a FROG source file contains, how source sections are represented, and how source-visible program objects are serialized.
</p>

<p>
It also explicitly owns source-shape/schema posture and structural validity for canonical source.
Repository-visible machine-checkable schema artifacts may assist structural reproducibility, but they remain downstream from the published prose ownership of <code>Expression/</code>.
</p>

<h3><code>Language/</code> — normative execution semantics</h3>

<p>
This directory defines cross-cutting execution semantics for validated program meaning.
It is the normative home of language meaning when that meaning cannot be owned by one isolated source section or one intrinsic primitive-library document alone.
</p>

<h3><code>IR/</code> — canonical open execution-facing representation</h3>

<p>
This directory defines the architectural home of the <strong>canonical open execution-facing representation</strong> derived from validated program meaning.
It sits between validated semantics and later lowering, backend mapping, compilation, or runtime-specific realization.
</p>

<p>
Within the current architecture, the IR layer is no longer just a loose execution-facing idea.
It is the home of:
</p>

<ul>
  <li>the <strong>canonical Execution IR Document</strong>,</li>
  <li>the derivation rules from validated meaning to that document,</li>
  <li>the construction rules for materially building it,</li>
  <li>the identity and mapping rules that preserve recoverability,</li>
  <li>the schema posture and machine-checkable validation surface of its canonical JSON form,</li>
  <li>the downstream-adjacent boundaries of lowering and backend-facing handoff.</li>
</ul>

<p>
This makes the IR layer the FROG execution-facing equivalent of a disciplined normalized graphical representation:
open, inspectable, attributable, and still upstream from private compiler or runtime machinery.
</p>

<h3><code>Implementations/Reference/</code> — non-normative reference implementation workspace</h3>

<p>
This directory is the current published non-normative reference implementation workspace.
Its immediate goal is not to define one production platform.
Its immediate goal is to exercise disciplined minimal executable vertical slices that prove stage boundaries can already be made real and inspectable.
</p>

<p>
Within the current published repository, this workspace contains prototype components such as:
</p>

<ul>
  <li><code>CLI</code>,</li>
  <li><code>Loader</code>,</li>
  <li><code>Validator</code>,</li>
  <li><code>Deriver</code>,</li>
  <li><code>Lowerer</code>,</li>
  <li><code>ContractEmitter</code>,</li>
  <li><code>Runtime</code>,</li>
  <li><code>UIHost</code>.</li>
</ul>

<p>
These executable slices are reference prototypes.
They are serious implementation exercises, but they are not yet the final production compiler pipeline of FROG.
</p>

<p>
The validator posture of this workspace is explicitly staged and downstream from the specification:
loadability,
structural validation,
semantic validation,
then derivation and later execution-preparation stages.
</p>

<h3><code>Libraries/</code> — intrinsic standardized primitive libraries</h3>

<p>
This directory defines intrinsic standardized primitive namespaces and primitive catalogs used by executable diagrams.
It is the normative home of standardized primitive identities, ports, primitive-local metadata, and primitive-local behavior that belong to the intrinsic language surface.
</p>

<h3><code>Profiles/</code> — optional standardized capability families</h3>

<p>
This directory defines optional standardized capability families that extend the usable surface of FROG without redefining the canonical source structure of the language core and without redefining core execution semantics.
It is the normative home of profile-owned primitive families and other optional capability contracts that should not be treated as intrinsic always-present language libraries.
</p>

<p>
This separation matters.
Capabilities that depend on external ecosystems, foreign runtimes, platform services, ABIs, databases, network stacks, or similar assumptions SHOULD be standardized through profiles or external ecosystem layers rather than absorbed by default into the intrinsic library core.
</p>

<p>
In the current architectural baseline, the first concrete example of that separation is:
</p>

<pre>
Libraries/Connectivity.md   -&gt; transition note only
Profiles/Interop.md         -&gt; authoritative normative home of frog.connectivity.*
</pre>

<h3><code>IDE/</code> — IDE architecture and editing model</h3>

<p>
This directory defines the architecture and responsibilities of a FROG development environment.
It explains how editing relates to the Program Model, serialized Expression, validation, IR derivation, execution preparation, execution observability, debugging, probes, watch views, snippets, and Express authoring.
</p>

<hr/>

<h2 id="internal-documentation-map">Internal documentation map</h2>

<p>
The repository contains multiple normative and architectural documents.
The map below summarizes the intended role of the Markdown documents in the current v0.1 baseline of the repository.
</p>

<pre><code>FROG/
├── Readme.md
│   -&gt; repository landing page and global architectural entry point
├── CONTRIBUTING.md
│   -&gt; contribution workflow, expectations, and cross-document coherence rules
├── CLA.md
│   -&gt; contributor license agreement entry point and legal contribution notice
├── GOVERNANCE.md
│   -&gt; repository governance, stewardship model, open-specification posture,
│      ecosystem participation, conformance direction, certification direction,
│      and branding boundary
│
├── Examples/
│   └── Readme.md
│       -&gt; architectural role of named example programs, example design rules,
│          first example slices, and relation with conformance and reference implementation
│
├── Conformance/
│   └── Readme.md
│       -&gt; public conformance posture, staged expected outcomes,
│          valid/invalid case posture, preservation obligations,
│          rejection expectations, and relation with examples
│
├── Implementations/
│   └── Reference/
│       └── Readme.md
│           -&gt; non-normative reference workspace, executable-slice purpose,
│              staged validator posture, prototype status,
│              and future compiler direction
│
├── Roadmap/
│   ├── Readme.md
│   │   -&gt; non-normative closure sequencing, current baseline interpretation,
│   │      phase ordering, and project-level closure bias
│   └── Milestones.md
│       -&gt; compact milestone tracking for repository-level closure progress
│
├── Strategy/
│   └── Heilmeier/
│       └── Readme.md
│           -&gt; strategic framing distinct from normative specification
│
├── Expression/
│   ├── Readme.md
│   │   -&gt; architectural entry point for canonical source representation
│   ├── Schema.md
│   │   -&gt; source-schema posture and machine-checkable structural validation boundary
│   ├── schema/
│   │   └── frog.schema.json
│   │       -&gt; conservative machine-checkable canonical top-level source schema
│   ├── Metadata.md
│   │   -&gt; descriptive program metadata and non-executable identification fields
│   ├── Type.md
│   │   -&gt; canonical type-expression model used across the source format
│   ├── Interface.md
│   │   -&gt; public typed inputs and outputs of a FROG
│   ├── Connector.md
│   │   -&gt; graphical perimeter mapping of interface ports when reused as a node
│   ├── Diagram.md
│   │   -&gt; authoritative executable graph as canonical source representation
│   ├── Front panel.md
│   │   -&gt; optional front-panel composition and user-facing interaction surface
│   ├── Widget.md
│   │   -&gt; widget object model, widget classes, properties, methods, events, and roles
│   ├── Widget interaction.md
│   │   -&gt; diagram-side widget interaction paths and execution-facing widget access model
│   ├── Control structures.md
│   │   -&gt; source-facing representation of canonical control structures
│   ├── State and cycles.md
│   │   -&gt; source-facing representation of explicit local memory and cycle formation rules
│   ├── Icon.md
│   │   -&gt; reusable-node icon representation
│   ├── IDE preferences.md
│   │   -&gt; optional IDE-facing source metadata with no executable authority
│   └── Cache.md
│       -&gt; optional non-authoritative cache content for tooling convenience
│
├── Language/
│   ├── Readme.md
│   │   -&gt; architectural entry point for normative execution semantics
│   ├── Control structures.md
│   │   -&gt; normative execution meaning of case, for_loop, and while_loop
│   ├── State and cycles.md
│   │   -&gt; normative meaning of explicit local memory and valid feedback cycles
│   ├── Execution model.md
│   │   -&gt; language-level execution-model core: validated program meaning,
│   │      live execution instance, source identity, activation, execution context,
│   │      semantic milestones, and committed source-level state
│   └── Execution control and observation boundaries.md
│       -&gt; safe observation points, pause-consistent snapshots, safe debug stops,
│          and minimal completion / fault / abort boundary semantics
│
├── IR/
│   ├── Readme.md
│   │   -&gt; architectural entry point for the IR layer and its ownership boundary
│   ├── Execution IR.md
│   │   -&gt; canonical open execution-facing IR model
│   ├── Derivation rules.md
│   │   -&gt; normative correspondence rules from validated program meaning to the canonical Execution IR Document
│   ├── Construction rules.md
│   │   -&gt; normative rules for materially building the canonical Execution IR Document
│   ├── Identity and Mapping.md
│   │   -&gt; identity continuity and recoverable mapping across derivation and lowering boundaries
│   ├── Schema.md
│   │   -&gt; schema posture for canonical IR validation
│   ├── schema/
│   │   └── frog.execution-ir.schema.json
│   │       -&gt; machine-checkable schema for the canonical Execution IR Document
│   ├── Lowering.md
│   │   -&gt; normative lowering boundary from canonical open IR toward target-oriented executable forms
│   └── Backend contract.md
│       -&gt; normative backend-facing contract for consumption of lowered execution forms
│
├── Libraries/
│   ├── Readme.md
│   │   -&gt; architectural entry point for intrinsic standardized primitive families
│   ├── Core.md
│   │   -&gt; foundational frog.core primitive library
│   ├── Math.md
│   │   -&gt; frog.math numeric scalar operations beyond the minimal core
│   ├── Collections.md
│   │   -&gt; frog.collections collection and array-oriented primitives
│   ├── Text.md
│   │   -&gt; frog.text string and text-processing primitives
│   ├── IO.md
│   │   -&gt; frog.io file, path, byte, and related I/O primitives
│   ├── Signal.md
│   │   -&gt; frog.signal first-wave signal-processing primitives
│   ├── UI.md
│   │   -&gt; frog.ui executable widget interaction primitives
│   └── Connectivity.md
│       -&gt; transition note for frog.connectivity, redirecting normative ownership
│          to the Interop profile in Profiles/
│
├── Profiles/
│   ├── Readme.md
│   │   -&gt; architectural entry point for optional standardized capability families,
│   │      including target profiles, deployment modes, backend families,
│   │      and runtime modules as distinct categories
│   └── Interop.md
│       -&gt; Interop profile specification for frog.connectivity.* and related
│          optional foreign-runtime / SQL interoperability capability
│
└── IDE/
    ├── Readme.md
    │   -&gt; architectural entry point for the FROG IDE and Program Model
    ├── Palette.md
    │   -&gt; palette model for surfacing primitives, structures, reusable nodes,
    │      and guided authoring entries
    ├── Express.md
    │   -&gt; guided Express authoring model and normalization to canonical FROG content
    ├── Execution observability.md
    │   -&gt; source-aligned live execution observability contract for IDE tooling
    ├── Debugging.md
    │   -&gt; interactive debugging behavior built on source-aligned observability
    ├── Probes.md
    │   -&gt; live local inspection probes for values and selected execution state
    ├── Watch.md
    │   -&gt; persistent centralized watch-based inspection model
    ├── Snippet.md
    │   -&gt; image-backed snippet capture, transport, paste, and reuse workflows
    └── FROG Snippet.md
        -&gt; legacy redirect document pointing to Snippet.md
</code></pre>

<p>
This map is intentionally architectural rather than merely enumerative.
Its purpose is to make repository ownership boundaries, support layers, and recommended reading paths easier to understand.
</p>

<hr/>

<h2 id="recommended-reading-path">Recommended reading path</h2>

<p>
Readers who are new to the repository should normally approach it in the following order:
</p>

<pre>
Readme.md
   |
   v
Expression/Readme.md
   |
   v
Expression/Schema.md
   |
   v
Language/Readme.md
   |
   v
IR/Readme.md
   |
   v
Libraries/Readme.md
   |
   v
Profiles/Readme.md
   |
   v
IDE/Readme.md
</pre>

<p>
This first path mirrors the current architectural baseline:
</p>

<ul>
  <li><strong>Expression</strong> defines the canonical saved source form,</li>
  <li><strong>Expression/Schema.md</strong> makes explicit what belongs to source-shape/schema posture and structural validity,</li>
  <li><strong>Language</strong> defines normative execution semantics for validated program meaning,</li>
  <li><strong>IR</strong> defines the canonical open execution-facing representation derived from that validated meaning,</li>
  <li><strong>Libraries</strong> define the intrinsic standardized executable primitive vocabularies,</li>
  <li><strong>Profiles</strong> define optional standardized capability families beyond the intrinsic core,</li>
  <li><strong>IDE</strong> defines authoring, observability, debugging, and inspection responsibilities built on top of those foundations.</li>
</ul>

<p>
Readers who want to understand the currently published repository-level executable/reference path SHOULD then continue with:
</p>

<pre>
Examples/Readme.md
   |
   v
Conformance/Readme.md
   |
   v
Implementations/Reference/Readme.md
</pre>

<p>
That second path answers three different questions in order:
</p>

<ul>
  <li><strong><code>Examples/</code></strong> — which named source cases are being used,</li>
  <li><strong><code>Conformance/</code></strong> — what those cases are expected to validate, preserve, or reject,</li>
  <li><strong><code>Implementations/Reference/</code></strong> — how a non-normative prototype pipeline currently tries to process them.</li>
</ul>

<p>
Readers who continue specifically into the IR layer SHOULD then follow:
</p>

<pre>
IR/Readme.md
   |
   v
Execution IR.md
   |
   v
Derivation rules.md
   |
   v
Identity and Mapping.md
   |
   v
Construction rules.md
   |
   v
Schema.md
   |
   v
schema/frog.execution-ir.schema.json
   |
   v
Lowering.md
   |
   v
Backend contract.md
</pre>

<p>
That third path reflects the current IR bundle:
the canonical open Execution IR core comes first,
identity and mapping preserve attribution continuity,
construction materializes the canonical open artifact,
schema validates its canonical JSON form,
and downstream lowering and backend contracts remain explicitly downstream from the open IR core even though they are documented in the same directory.
</p>

<hr/>

<h2 id="specification-architecture">Specification architecture</h2>

<p>
The repository is intentionally split into distinct architectural layers:
</p>

<ul>
  <li><strong>Expression</strong> — canonical source representation, source sections, source serialization rules, source-schema posture, and structural validity,</li>
  <li><strong>Language</strong> — normative execution semantics for validated program meaning,</li>
  <li><strong>IR</strong> — canonical open execution-facing representations derived from validated program meaning,</li>
  <li><strong>Libraries</strong> — intrinsic standardized primitive vocabularies and primitive-local behavior,</li>
  <li><strong>Profiles</strong> — optional standardized capability families and profile-owned capability contracts,</li>
  <li><strong>IDE</strong> — authoring architecture, editor-facing models, execution observability, debugging semantics, inspection workflows, snippets, and Express authoring.</li>
</ul>

<p>
This separation is deliberate.
It prevents the language from being reduced to one editor, one runtime, one compiler, or one vendor implementation.
</p>

<p>
It also makes the repository suitable as the basis of an open standard:
different actors may later build compatible IDEs, validators, runtimes, compilers, toolchains, ecosystem services, and profile-supporting implementations while still targeting the same language definition.
</p>

<pre>
Expression/   -> canonical source form and structural validity
Language/     -> validated program meaning
IR/           -> canonical open execution-facing representation
Libraries/    -> intrinsic standardized primitive vocabularies
Profiles/     -> optional standardized capability families
IDE/          -> authoring, observability, debugging, inspection
</pre>

<pre>
what is saved      -> Expression/
what is true       -> Language/
what is derived    -> IR/
what exists        -> Libraries/ and Profiles/
what is edited     -> IDE/
</pre>

<p>
Beyond those six core families, the published repository also contains three important support areas that should not be confused with competing semantic owners:
</p>

<pre>
what is exemplified  -> Examples/
what is expected     -> Conformance/
what is prototyped   -> Implementations/Reference/
</pre>

<p>
Within that baseline, the <code>IR/</code> directory already includes documents for derivation, identity and mapping, construction, schema, lowering, and backend-facing contracts.
Those documents remain architecturally downstream from validated program meaning and upstream from private realization.
</p>

<p>
Likewise, the repository-level support areas are already part of the published state of the repository,
but they do not redefine the ownership model:
</p>

<ul>
  <li><strong><code>Examples/</code></strong> do not define language truth,</li>
  <li><strong><code>Conformance/</code></strong> does not become the semantic owner,</li>
  <li><strong><code>Implementations/Reference/</code></strong> does not become the normative production compiler pipeline.</li>
</ul>

<p>
Beyond the six top-level families listed above, later areas such as deployment, runtime profiles, or conformance-oriented execution profiles MAY be structured more explicitly over time.
Those later areas are not yet closed top-level specification families in the same sense as the six layers listed above.
</p>

<hr/>

<h2 id="program-representation">Program representation</h2>

<p>
FROG programs should be understood across <strong>five</strong> distinct representation levels.
</p>

<h3>1. FROG Expression</h3>

<p>
The <strong>FROG Expression</strong> is the serialized source representation stored in a <code>.frog</code> file.
It is the canonical source form of a FROG program.
</p>

<p>
A FROG is represented by a structured, human-readable JSON source file with the <code>.frog</code> extension.
That canonical source file is transparent, editable, portable, and version-control-friendly.
</p>

<p>
A canonical <code>.frog</code> source file MUST contain:
</p>

<ul>
  <li><code>spec_version</code>,</li>
  <li><code>metadata</code>,</li>
  <li><code>interface</code>,</li>
  <li><code>diagram</code>.</li>
</ul>

<p>
It MAY additionally contain:
</p>

<ul>
  <li><code>front_panel</code>,</li>
  <li><code>connector</code>,</li>
  <li><code>icon</code>,</li>
  <li><code>ide</code>,</li>
  <li><code>cache</code>.</li>
</ul>

<p>
Optional sections MUST NOT redefine authoritative program semantics.
The diagram remains the authoritative source-level execution structure.
The public interface remains independent from the front panel.
The front panel remains optional and non-authoritative for public interface definition.
</p>

<h3>2. Structural validity</h3>

<p>
A loadable JSON source file is not automatically a structurally valid canonical FROG source file.
Structural validity is an explicit stage owned by <code>Expression/</code>.
</p>

<p>
At this stage, the repository distinguishes:
</p>

<ul>
  <li>raw loadability,</li>
  <li>canonical top-level source shape,</li>
  <li>source-owned structural requirements,</li>
  <li>machine-checkable schema assistance where published.</li>
</ul>

<p>
Structural validity is not yet semantic truth.
A source file may therefore be:
</p>

<ul>
  <li>not loadable,</li>
  <li>loadable but structurally invalid,</li>
  <li>structurally valid but semantically invalid.</li>
</ul>

<h3>3. FROG Program Model</h3>

<p>
The <strong>FROG Program Model</strong> is the canonical editable in-memory representation used by IDEs during authoring.
It is reconstructed from the FROG Expression and maintained while the user edits the program.
</p>

<p>
It maintains coherent relationships between:
</p>

<ul>
  <li>interface declarations and <code>interface_input</code> / <code>interface_output</code> nodes,</li>
  <li>front-panel widget declarations and <code>widget_value</code> / <code>widget_reference</code> nodes,</li>
  <li>structure nodes and their owned regions,</li>
  <li>semantic graph content and source-level layout information,</li>
  <li>authoring-facing insertion views and canonical source identities,</li>
  <li>Express presentation state and the canonical objects that an Express entry edits or materializes.</li>
</ul>

<p>
This Program Model is an IDE architectural concept.
It is not the same thing as the raw serialized source file.
It is also not, by itself, the normative execution-semantics layer of the language.
</p>

<h3>4. Validated program meaning</h3>

<p>
A source-derived FROG program must first be validated against the relevant language, primitive-library, and profile rules.
That validated state is where normative execution meaning becomes a trustworthy basis for later derivation.
</p>

<p>
At this level, the repository defines:
</p>

<ul>
  <li>cross-cutting execution semantics,</li>
  <li>control-structure behavior,</li>
  <li>state and cycle validity,</li>
  <li>execution and observation boundaries,</li>
  <li>intrinsic primitive-local behavior,</li>
  <li>optional profile-owned capability behavior where applicable.</li>
</ul>

<h3>5. Canonical open execution-facing representation</h3>

<p>
A validated FROG is not executed directly from raw source text.
A conforming toolchain validates the source-derived program representation and then derives a canonical open execution-facing representation suitable for execution preparation, analysis, normalization, optimization, lowering, or compilation.
</p>

<p>
That execution-facing level is the role of the <strong>IR layer</strong>.
It is not the canonical source, not the IDE Program Model, and not one private runtime graph.
It is the canonical open execution-facing representation derived from validated program meaning.
</p>

<p>
Within the current architecture, that representation is centered on a <strong>canonical Execution IR Document</strong>.
That canonical document is then preserved across identity and mapping rules, materialized through construction rules, validated through a canonical JSON schema surface, and only then handed to later lowering and backend-facing stages.
</p>

<pre>
.frog source
    |
    v
loadability
    |
    v
structural validity
    |
    v
Program Model / validated source-derived program
    |
    v
validated program meaning
    |
    v
canonical Execution IR Document
    |
    v
lowering / backend-facing handoff
</pre>

<hr/>

<h2 id="execution-architecture">Execution architecture</h2>

<p>
A conforming FROG ecosystem should separate <strong>authoring</strong>, <strong>canonical source</strong>, <strong>structural validity</strong>, <strong>validated program meaning</strong>, <strong>canonical open execution-facing representation</strong>, and <strong>target-specific execution realization</strong>.
</p>

<p>
A FROG is <strong>not</strong> executed directly from raw source text.
A toolchain edits a Program Model, serializes canonical source, validates structural source shape against the published source-owned rules, validates program meaning against the relevant semantic, intrinsic-library, and profile rules, derives a canonical open execution-facing representation, preserves recoverable attribution and mapping across that derivation, and only then proceeds toward lowering, backend preparation, compilation, or runtime realization.
</p>

<pre>
                              FROG IDE
                   +-------------------------------+
                   | Diagram + Front Panel UI      |
                   +---------------+---------------+
                                   |
                                   v
                        FROG Program Model
                    (editable in-memory model)
                                   |
                     +-------------+-------------+
                     |                           |
                     | save / load               | execute / validate
                     v                           v
        🟩 OPEN SOURCE LAYER                Validation against
        🟩 FROG Expression                 +----------------------+
        (.frog, canonical source)         | Expression/          |
                                          | Language/            |
                                          | Libraries/           |
                                          | Profiles/            |
                                          +----------+-----------+
                                                     |
                                                     v
                                  🟦 OPEN EXECUTION LAYER
                                  🟦 FROG Execution IR
                         (canonical Execution IR Document,
                          derived, inspectable, source-attributed,
                          execution-facing, not backend-private)
                                                     |
                                                     v
                               Identity / Mapping preservation
                                                     |
                                                     v
                              Lowering / backend-facing handoff
                                                     |
                                                     v
                            Compiler(s) / Backend(s) / Runtime(s)
                                                     |
                                                     v
                                     ▶ Target execution instance
                                                     |
                            +------------------------+------------------------+
                            |                                                 |
                            v                                                 v
              Source-aligned execution observability              Runtime activity
             (mapped back to meaningful FROG objects)           on the active target
                            |
                            v
                         Debugging
                (pause / resume / break / step)
                            |
                     +------+
                     |      |
                     v      v
                   Probes  Watch
</pre>

<p>
This architecture intentionally distinguishes two open specification-facing representation layers:
</p>

<ul>
  <li><strong>FROG Expression</strong> — the canonical saved source artifact.</li>
  <li><strong>FROG Execution IR</strong> — the canonical open execution-facing representation derived from validated program meaning.</li>
</ul>

<p>
It also separates what remains <strong>normatively open and inspectable</strong> from what may remain <strong>implementation-specific</strong>:
</p>

<ul>
  <li>canonical source remains open, durable, and authoritative,</li>
  <li>structural validity remains source-owned and distinct from semantic acceptance,</li>
  <li>Execution IR remains canonical, open, inspectable, and specification-facing,</li>
  <li>identity and mapping remain recoverable where required for attribution and diagnostics,</li>
  <li>lowering, backend preparation, compiler internals, runtime scheduling, and target realization MAY vary across implementations.</li>
</ul>

<p>
Execution observability and debugging sit <strong>after live execution exists</strong>, but they are not defined as raw runtime internals.
They are source-aligned views and controls that allow implementations to project live execution back onto meaningful FROG concepts such as graph activity, structures, regions, values, local memory, and selected execution objects.
</p>

<pre>
what is saved       -> Expression/
what is validated   -> Expression/ + Language/ + Libraries/ + Profiles/
what is derived     -> IR/
what is executed    -> compiler / backend / runtime implementations
what is observed    -> IDE-facing source-aligned observability and debugging
</pre>

<p>
This separation keeps FROG open as a language while still allowing multiple independent implementations to build different execution pipelines, runtimes, and target backends on top of the same specification.
</p>

<p>
During development, tools maintain the Program Model.
Saving serializes that model into canonical source.
Execution requests validate the relevant program content, derive a canonical open execution-facing representation, and then pass that derived form into later execution-preparation or target-facing stages.
</p>

<p>
A serious downstream compiler path MAY eventually target compiler families such as LLVM.
However, those downstream families remain consumers of lowered FROG forms rather than the definition of FROG itself.
The canonical FROG Execution IR remains architecturally upstream and distinct.
</p>

<hr/>

<h2 id="execution-observability-debugging-and-inspection">Execution observability, debugging, and inspection</h2>

<p>
Interactive inspection and debugging are not performed directly on raw serialized source.
They are performed on a live execution derived from validated program content and projected back onto source-meaningful objects.
</p>

<p>
<strong>Execution observability</strong> is the source-aligned live view that allows runtime activity to be mapped back to concepts such as:
</p>

<ul>
  <li>node activations,</li>
  <li>edge-level value availability,</li>
  <li>structure entry and region selection,</li>
  <li>loop iteration progression,</li>
  <li>local-memory state activity,</li>
  <li>pause-consistent execution snapshots.</li>
</ul>

<p>
<strong>Debugging</strong> is the interactive control layer built on top of that observability.
It allows an IDE to inspect and guide execution through source-level concepts such as:
</p>

<ul>
  <li>execution highlighting,</li>
  <li>manual pause and resume,</li>
  <li>breakpoints,</li>
  <li>single-step controls,</li>
  <li>fault-directed source localization.</li>
</ul>

<p>
<strong>Probes</strong> are source-aligned live inspection tools built on top of execution observability and used together with debugging.
They allow an IDE to inspect values or selected execution state associated with objects such as:
</p>

<ul>
  <li>edges,</li>
  <li>node ports,</li>
  <li>local-memory state,</li>
  <li>selected UI-related execution objects in stricter profiles.</li>
</ul>

<p>
<strong>Watch</strong> provides persistent centralized inspection of selected source-visible targets during or after live execution.
Unlike probes, which are primarily local inspection objects, watches are intended to remain visible in a managed watch list or equivalent watch view.
</p>

<p>
In FROG, debugging and inspection are dataflow-first rather than line-oriented.
They operate on observable graph activity, structures, sub-FROG scopes, value flow, local memory, and explicit UI-related execution objects rather than on a fictional sequential instruction list.
</p>

<hr/>

<h2 id="execution-targets">Execution targets</h2>

<p>
FROG programs are designed to remain source-level stable across multiple hardware classes.
The language is not tied to one processor family, one operating system, one runtime architecture, or one vendor.
</p>

<p>
Representative target classes include:
</p>

<ul>
  <li><strong>General-purpose CPUs</strong> — workstation, server, and industrial PC execution,</li>
  <li><strong>Real-time targets</strong> — deterministic measurement and control systems,</li>
  <li><strong>Embedded systems</strong> — ARM and edge-oriented devices,</li>
  <li><strong>GPUs</strong> — accelerated compute targets,</li>
  <li><strong>FPGAs</strong> — programmable-logic targets,</li>
  <li><strong>Microcontrollers</strong> — constrained embedded execution,</li>
  <li><strong>Industrial edge controllers</strong> — integrated vendor-specific control and acquisition platforms.</li>
</ul>

<p>
The programming model is intended to remain conceptually stable across such targets.
What changes is the active execution profile, the validation or lowering strategy, the backend, and the available platform services.
</p>

<p>
More explicit target-profile standardization MAY be refined over time.
At the current repository stage, target diversity is an architectural direction rather than a fully closed standalone profile taxonomy.
</p>

<hr/>

<h2 id="open-industrial-hardware-standard">Open industrial hardware standard</h2>

<p>
FROG aims to be more than a language that merely supports multiple targets.
Its long-term goal is to provide an <strong>open industrial graphical programming standard</strong> that hardware and software ecosystems can build on without requiring a proprietary language boundary.
</p>

<p>
That means hardware vendors, runtime builders, compiler builders, industrial software platforms, embedded-system providers, and specialized toolchain developers should be able to support the same core language while preserving their own:
</p>

<ul>
  <li>runtime strategies,</li>
  <li>deployment models,</li>
  <li>validation constraints,</li>
  <li>hardware services,</li>
  <li>library stacks,</li>
  <li>target-specific optimization layers.</li>
</ul>

<p>
In practice, this may include:
</p>

<ul>
  <li>FROG-compatible runtimes,</li>
  <li>target-specific compilers and backends,</li>
  <li>driver-backed hardware libraries exposed as FROG nodes,</li>
  <li>deployment environments built around FROG execution,</li>
  <li>vendor-specific profiles or conformance targets.</li>
</ul>

<hr/>

<h2 id="security-and-optimization-by-design">Security and optimization by design</h2>

<p>
FROG integrates validation and optimization into its architecture.
</p>

<p>
Base principles include:
</p>

<ul>
  <li>strict type validation,</li>
  <li>graph validation before execution,</li>
  <li>controlled execution and observation boundaries,</li>
  <li>explicit structure semantics,</li>
  <li>explicit local-memory semantics for valid feedback loops,</li>
  <li>deterministic execution guarantees where supported by the active profile.</li>
</ul>

<p>
Optimization occurs primarily in execution preparation, IR normalization, lowering, compilation, and backend stages:
</p>

<ul>
  <li>graph simplification,</li>
  <li>dead-node elimination,</li>
  <li>constant folding,</li>
  <li>memory optimization,</li>
  <li>parallel scheduling where valid,</li>
  <li>target-specific lowering,</li>
  <li>profile-aware specialization,</li>
  <li>compiler-family-oriented backend preparation where applicable.</li>
</ul>

<hr/>

<h2 id="interoperability">Interoperability</h2>

<p>
FROG is designed for interoperability at several levels:
</p>

<ul>
  <li><strong>source interoperability</strong> — the canonical <code>.frog</code> file is readable, structured, and tool-independent,</li>
  <li><strong>editing interoperability</strong> — multiple IDEs may reconstruct equivalent Program Models,</li>
  <li><strong>structural interoperability</strong> — canonical source shape can be checked against shared source-owned structural rules,</li>
  <li><strong>semantic interoperability</strong> — validated programs are interpreted against shared language, intrinsic-library, and profile specifications,</li>
  <li><strong>IR interoperability</strong> — multiple toolchains may derive compatible canonical open execution-facing representations,</li>
  <li><strong>execution interoperability</strong> — multiple toolchains may lower, contract, compile, or run compatible program meanings across different backend families,</li>
  <li><strong>ecosystem interoperability</strong> — the language remains separate from vendor lock-in.</li>
</ul>

<p>
FROG is also designed to integrate with external languages and platform APIs through stable interoperation mechanisms.
In the current repository architecture, such environment-dependent capability families SHOULD be standardized through optional profiles rather than treated automatically as intrinsic standardized libraries.
</p>

<p>
At the current architectural baseline, the first concrete standardized interop capability family is owned by:
</p>

<pre><code>Profiles/Interop.md</code></pre>

<p>
Representative integration targets may include:
</p>

<ul>
  <li>C / C++,</li>
  <li>Rust,</li>
  <li>Python,</li>
  <li>.NET,</li>
  <li>other ABI-compatible environments.</li>
</ul>

<p>
External functions and platform services can be exposed as FROG nodes while preserving graph-level validation and explicit type behavior.
This is also essential for hardware support, because drivers, SDKs, real-time services, FPGA toolflows, embedded platform stacks, and external software ecosystems can be integrated without collapsing the language into one closed ecosystem.
</p>

<hr/>

<h2 id="separation-of-language-and-tooling">Language separation</h2>

<p>
FROG explicitly separates:
</p>

<ul>
  <li>the language specification,</li>
  <li>the canonical source representation,</li>
  <li>source-schema posture and structural validity,</li>
  <li>the editable program model,</li>
  <li>validated program meaning,</li>
  <li>the canonical open execution-facing representation,</li>
  <li>intrinsic standardized primitive vocabularies,</li>
  <li>optional standardized capability profiles,</li>
  <li>execution observability,</li>
  <li>interactive debugging semantics,</li>
  <li>live inspection through probes,</li>
  <li>persistent watch-based inspection,</li>
  <li>snippet-based authoring transport,</li>
  <li>compiler implementations,</li>
  <li>backend implementations,</li>
  <li>runtime implementations,</li>
  <li>development environments,</li>
  <li>hardware adaptation layers,</li>
  <li>deployment and orchestration layers.</li>
</ul>

<p>
At the modeling level, FROG also separates:
</p>

<ul>
  <li>language from IDE,</li>
  <li>source from structural validation,</li>
  <li>structural validity from semantic truth,</li>
  <li>semantic truth from derived execution-facing representation,</li>
  <li>intrinsic libraries from optional profiles,</li>
  <li>IDE from runtime,</li>
  <li>runtime from hardware,</li>
  <li>public interface from front panel,</li>
  <li>diagram from connector,</li>
  <li>natural widget value flow from object-style widget interaction,</li>
  <li>canonical Execution IR from downstream compiler-family forms such as LLVM-oriented artifacts.</li>
</ul>

<p>
This enables:
</p>

<ul>
  <li>multiple IDE implementations,</li>
  <li>multiple validators,</li>
  <li>multiple IR-producing toolchains,</li>
  <li>multiple compilers,</li>
  <li>multiple backends,</li>
  <li>multiple runtimes,</li>
  <li>multiple profile-supporting ecosystems around the same core language,</li>
  <li>independent ecosystem evolution around a shared graphical standard.</li>
</ul>

<p>
The specification defines the language, not one product.
</p>

<hr/>

<h2 id="governance-and-ecosystem">Governance and ecosystem</h2>

<p>
FROG is governed as an <strong>open specification</strong>.
The repository is intended to remain readable, implementable, and usable by independent parties while preserving long-term architectural coherence.
</p>

<p>
The current governance model is steward-led.
Graiphic is the initial steward of the FROG specification repository and is responsible for maintaining architectural coherence, reviewing proposed changes, and publishing authoritative repository revisions.
</p>

<p>
Open specification does not imply a single implementation model.
Different actors may build open-source or proprietary IDEs, validators, runtimes, compilers, libraries, profiles, integrations, deployment systems, and related services around the FROG specification.
</p>

<p>
Openness of the specification does not automatically grant trademark rights or official compatibility claims.
Names, logos, certification marks, and claims such as <em>official</em>, <em>certified</em>, <em>endorsed</em>, or <em>FROG-certified</em> MAY be governed by separate conformance, certification, and branding policies.
</p>

<p>
Over time, the governance model is intended to distinguish clearly between:
</p>

<ul>
  <li>implementing core FROG,</li>
  <li>implementing core FROG plus explicitly named profiles,</li>
  <li>claiming a conformant implementation under an applicable conformance policy,</li>
  <li>claiming certified or official compatibility status under an applicable certification or branding policy.</li>
</ul>

<p>
The intended ecosystem direction is that the specification remains open, while official certification, official branding, and equivalent steward-controlled compatibility claims MAY be governed separately.
Commercial implementations seeking official certification or branding MAY be subject to paid verification or licensing policies, while non-commercial implementations MAY be verified free of charge or at minimal cost under applicable steward policies.
</p>

<hr/>

<h2 id="project-status">Project status</h2>

<p>
FROG is currently under active design, cleanup, and stabilization.
The repository already contains substantial material across canonical source representation, source-schema posture, language semantics, canonical open execution-facing IR architecture, intrinsic standardized primitive libraries, optional profile architecture, and IDE architecture, but the overall specification is still converging toward a coherent v0.1 foundation.
</p>

<p>
At the same time, the repository has now moved beyond a purely architectural document set.
It already contains:
</p>

<ul>
  <li>a published <code>Examples/</code> directory with the first four repository-visible executable slices,</li>
  <li>a published <code>Conformance/</code> directory with explicit staged expected-outcome posture,</li>
  <li>a published <code>Implementations/Reference/</code> workspace whose current purpose is to exercise disciplined minimal executable vertical slices for a controlled subset.</li>
</ul>

<p>
The first currently published executable slices are:
</p>

<ul>
  <li><code>01_pure_addition</code>,</li>
  <li><code>02_ui_value_roundtrip</code>,</li>
  <li><code>03_ui_property_write</code>,</li>
  <li><code>04_stateful_feedback_delay</code>.</li>
</ul>

<p>
Current repository direction therefore includes both <strong>architectural stabilization</strong> and <strong>repository-visible reference-path proof work</strong>.
</p>

<ul>
  <li>stabilizing the canonical source specification,</li>
  <li>stabilizing source-shape/schema posture and structural validation boundaries,</li>
  <li>stabilizing the separation between canonical source representation and normative execution semantics,</li>
  <li>stabilizing the separation between normative execution semantics and the canonical open execution-facing IR layer,</li>
  <li>clarifying language semantics and execution behavior,</li>
  <li>maintaining a distinct canonical open execution-facing IR layer without collapsing FROG into one private runtime pipeline,</li>
  <li>stabilizing recoverable identity and mapping across derivation and later specialization boundaries,</li>
  <li>clarifying lowering and backend-facing handoff boundaries without over-freezing private runtime internals,</li>
  <li>stabilizing the intrinsic library boundary,</li>
  <li>establishing optional profile families without collapsing them into the intrinsic core,</li>
  <li>keeping profile-owned capability families explicitly distinct from intrinsic libraries,</li>
  <li>defining IDE responsibilities without coupling the language to one implementation,</li>
  <li>defining source-aligned execution observability for live execution,</li>
  <li>defining dataflow-native debugging semantics for FROG IDEs,</li>
  <li>defining source-aligned live inspection through probes,</li>
  <li>defining persistent centralized watch-based inspection for FROG IDEs,</li>
  <li>defining image-backed snippet-based reusable authoring transport,</li>
  <li>defining guided Express authoring as an IDE convenience layer that normalizes to canonical FROG content,</li>
  <li>keeping the executable reference path clean, reproducible, and inspectable,</li>
  <li>keeping <code>Examples/</code>, <code>Conformance/</code>, and <code>Implementations/Reference/</code> aligned without letting them silently become hidden language law,</li>
  <li>preparing the path from canonical <code>.frog</code> source toward a serious future compiler/runtime story, including downstream compiler-family paths such as LLVM-oriented ones.</li>
</ul>

<p>
The currently published reference workspace proves stage boundaries first.
It does not yet claim that the repository already contains the final normative production compiler pipeline, one definitive production runtime architecture, or one universal downstream compiler-family route.
</p>

<p>
At the same time, some broader execution-facing and deployment-facing areas remain architectural direction rather than fully closed top-level repository families.
Topics such as deployment, runtime profiles, target-profile taxonomies, and broader conformance or certification growth MAY be refined further over time.
</p>

<p>
The long-term ambition is to establish a durable open graphical programming ecosystem that can scale from experimentation to deeply integrated industrial deployment.
</p>

<p>
Discussions, feedback, and contributions are welcome.
</p>

<hr/>

<h2 id="license">License</h2>

<p>
This project is licensed under the <strong>Apache License 2.0</strong>.
See <code>LICENSE</code> for details.
</p>

<p>
External contributions are governed through the repository contribution process and Contributor License Agreement requirements.
See <code>CONTRIBUTING.md</code> and <code>CLA.md</code>.
</p>

<p>
Repository stewardship, governance direction, and ecosystem positioning are described in <code>GOVERNANCE.md</code>.
</p>

<p align="center">
  <a href="https://cla-assistant.io/Graiphic/FROG">
    <img src="https://cla-assistant.io/readme/badge/Graiphic/FROG" alt="CLA Assistant" />
  </a>
</p>

<hr/>

<p align="center">
  <strong>FROG — Free Open Graphical Language</strong><br/>
  Open graphical dataflow programming, specified as a language rather than owned as a product.
</p>
