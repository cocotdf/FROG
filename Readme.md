<p align="center">
  <img src="FROG logo.svg" alt="FROG logo" width="150" />
</p>

<h1 align="center">🐸 FROG — Free Open Graphical Language</h1>

<p align="center">
  <strong>Free Open Graphical Dataflow Programming Language</strong><br/>
  An open, hardware-agnostic graphical dataflow language designed for accessibility, explicit execution,
  deterministic behavior, and scalable deployment across heterogeneous systems.
</p>

<p align="center">
  <a href="#what-is-frog">What is FROG?</a> •
  <a href="#why-frog-exists">Why FROG exists</a> •
  <a href="#positioning">Positioning</a> •
  <a href="#breaking-the-syntax-first-bottleneck">Breaking the syntax-first bottleneck</a> •
  <a href="#dataflow-programming">Dataflow programming</a> •
  <a href="#from-prototyping-to-critical-systems">From prototyping to critical systems</a> •
  <a href="#core-concept">Core concept</a> •
  <a href="#repository-structure">Repository structure</a> •
  <a href="#specification-architecture">Specification architecture</a> •
  <a href="#program-representation">Program representation</a> •
  <a href="#execution-architecture">Execution architecture</a> •
  <a href="#execution-targets">Execution targets</a> •
  <a href="#open-industrial-hardware-standard">Open industrial hardware standard</a> •
  <a href="#security-and-optimization">Security &amp; optimization</a> •
  <a href="#interoperability">Interoperability</a> •
  <a href="#language-separation">Language separation</a> •
  <a href="#status">Status</a> •
  <a href="#license">License</a>
</p>

<hr/>

<h2 id="what-is-frog">What is FROG?</h2>

<p>
FROG is an open, hardware-agnostic graphical dataflow programming language.
It represents computation as explicit executable graphs rather than as syntax-driven sequences of instructions.
</p>

<p>
Instead of describing a program primarily through ordered text, FROG describes a program through:
</p>

<ul>
  <li>typed nodes,</li>
  <li>typed ports,</li>
  <li>directed graph connections,</li>
  <li>structured control regions,</li>
  <li>explicit interface boundaries,</li>
  <li>front-panel widgets and interaction layers.</li>
</ul>

<p>
Execution emerges from data availability, structural rules, explicit control structures, and explicit local-memory semantics
rather than from manually authored instruction order.
</p>

<p>
FROG is designed to remain independent from any specific IDE, compiler, runtime, operating system, or hardware vendor.
That separation creates a durable foundation for multiple independent implementations and long-term industrial interoperability.
</p>

<hr/>

<h2 id="why-frog-exists">Why FROG exists</h2>

<p>
Graphical dataflow programming has already demonstrated major advantages in many engineering domains:
</p>

<ul>
  <li>natural parallelism,</li>
  <li>deterministic execution,</li>
  <li>clear orchestration of behavior,</li>
  <li>strong correspondence between software structure and system behavior,</li>
  <li>high productivity for engineers, scientists, and domain experts.</li>
</ul>

<p>
However, many historical graphical environments have been tightly coupled to proprietary ecosystems in which
language, tooling, runtime, and hardware support are inseparable.
</p>

<p>
That model limits portability, slows independent ecosystem growth, and prevents multiple vendors or toolchains
from implementing the same language cleanly.
</p>

<p>
FROG exists to define an open language specification for graphical dataflow programming that remains separate from:
</p>

<ul>
  <li>any single IDE,</li>
  <li>any single runtime,</li>
  <li>any single compiler,</li>
  <li>any single hardware vendor.</li>
</ul>

<p>
FROG is not an IDE.
FROG is not a single runtime.
FROG is not a vendor product.
FROG is a language specification and execution model.
</p>

<hr/>

<h2 id="positioning">Positioning</h2>

<p>
FROG is designed to combine the accessibility of graphical programming with the execution depth required for deterministic,
industrial, embedded, and high-performance systems.
</p>

<p>
Its ambition is not merely to make programming easier, and not merely to make execution more powerful.
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

<p>
FROG aims to combine graphical accessibility, explicit dataflow, and system-grade execution in one open language model.
</p>

<hr/>

<h2 id="breaking-the-syntax-first-bottleneck">Breaking the syntax-first bottleneck</h2>

<p>
A major barrier in many traditional programming environments is that useful system design often begins only after
a long period of syntax learning, pattern memorization, and language-specific implementation habits.
</p>

<p>
This creates an inversion: instead of starting from the system that should exist, developers often start from the syntax they already know how to write.
That inversion limits experimentation and slows architectural thinking.
</p>

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
The goal is to shift complexity toward the system itself instead of toward syntax-first representation.
</p>

<hr/>

<h2 id="dataflow-programming">Dataflow programming</h2>

<p>
FROG follows a true dataflow execution model.
</p>

<p>
In traditional instruction-sequenced programming, execution is primarily described as ordered steps.
In dataflow programming, operations become executable when their required input data is available.
</p>

<pre><code>Traditional execution

A → B → C → D

Dataflow execution

   A
  / \
 B   C
  \ /
   D</code></pre>

<p>
Execution order therefore emerges from dependencies.
This model enables:
</p>

<ul>
  <li>automatic parallelism where valid,</li>
  <li>clear dependency visibility,</li>
  <li>deterministic execution models,</li>
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

<h2 id="core-concept">Core concept</h2>

<p>
A FROG program combines two complementary layers:
</p>

<h3>Diagram — the authoritative executable graph</h3>

<p>
The diagram defines the executable logic of the program.
It is the authoritative execution graph.
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
  <li>explicit local memory and valid cycles.</li>
</ul>

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
Primary widget values participate naturally in execution through <code>widget_value</code> nodes in the diagram.
There is no separate canonical front-panel binding section for ordinary value flow.
</p>

<h3>Widget interaction model</h3>

<p>
FROG distinguishes two widget interaction paths:
</p>

<ul>
  <li><strong>natural value path</strong> — widget primary value participation through <code>widget_value</code>,</li>
  <li><strong>object-style path</strong> — explicit widget access through <code>widget_reference</code> together with
      <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code>.</li>
</ul>

<p>
These two paths are related but distinct.
This keeps ordinary dataflow wiring simple while preserving a clean long-term object model for UI interaction.
</p>

<hr/>

<h2 id="repository-structure">Repository structure</h2>

<p>
This repository is organized by architectural responsibility.
Each top-level directory has a specific role in the specification.
</p>

<pre><code>FROG/
│
├── Expression/
├── IDE/
├── Language/
├── Libraries/
│
├── CLA.md
├── CONTRIBUTING.md
├── FROG logo.svg
├── LICENSE
├── Readme.md
└── frog-orville-chart.png</code></pre>

<h3><code>Expression/</code> — canonical source specification</h3>

<p>
This directory defines the canonical <code>.frog</code> source format.
It describes what a FROG source file contains and how its source sections are interpreted.
</p>

<p>
It currently contains:
</p>

<ul>
  <li><code>Metadata.md</code> — metadata and descriptive program information,</li>
  <li><code>Type.md</code> — canonical type expressions and type compatibility rules,</li>
  <li><code>Interface.md</code> — public typed inputs and outputs,</li>
  <li><code>Connector.md</code> — graphical mapping of public ports when reused as a node,</li>
  <li><code>Diagram.md</code> — authoritative executable graph,</li>
  <li><code>Front panel.md</code> — UI composition and front-panel structure,</li>
  <li><code>Widget.md</code> — widget object model,</li>
  <li><code>Widget interaction.md</code> — diagram-side widget interaction model,</li>
  <li><code>Control structures.md</code> — language structures such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>,</li>
  <li><code>State and cycles.md</code> — local memory and cycle validity,</li>
  <li><code>Icon.md</code> — reusable-node icon representation,</li>
  <li><code>IDE preferences.md</code> — IDE-facing source-level preferences,</li>
  <li><code>Cache.md</code> — optional non-authoritative cache data,</li>
  <li><code>Readme.md</code> — overview of the whole Expression layer.</li>
</ul>

<p>
In short, <code>Expression/</code> defines the canonical source language representation.
</p>

<h3><code>Language/</code> — repository transition and semantic continuity</h3>

<p>
This directory remains present in the repository as a transition and continuity layer.
It retains language-semantic documents related to structural execution and cycles while the repository architecture remains split across layers.
</p>

<p>
It currently contains:
</p>

<ul>
  <li><code>Readme.md</code> — overview of the Language directory and its current transitional role,</li>
  <li><code>Control structures.md</code> — language structures such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>,</li>
  <li><code>State and cycles.md</code> — explicit local memory and rules for valid feedback cycles.</li>
</ul>

<p>
For canonical source-spec reading, the corresponding documents in <code>Expression/</code> are now the primary reference.
The presence of <code>Language/</code> reflects repository continuity and semantic organization rather than a separate canonical source layer.
</p>

<h3><code>Libraries/</code> — standard primitive libraries</h3>

<p>
This directory defines standard library namespaces and primitive catalogs used by diagrams.
</p>

<p>
It currently contains:
</p>

<ul>
  <li><code>Readme.md</code> — overview of the standard library layer and how primitive namespaces relate to the rest of the specification,</li>
  <li><code>Core.md</code> — the base primitive library, including canonical <code>frog.core.*</code> primitives.</li>
</ul>

<p>
In short, <code>Libraries/</code> defines what standard primitives exist and what their ports and semantics are.
</p>

<h3><code>IDE/</code> — IDE architecture and editing model</h3>

<p>
This directory defines the architecture and responsibilities of a FROG development environment.
It explains how editing relates to the Program Model, the serialized Expression, validation, lowering, and runtime independence.
</p>

<p>
It currently contains:
</p>

<ul>
  <li><code>Readme.md</code> — overall IDE architecture,</li>
  <li><code>Palette.md</code> — palette model for surfacing functions, structures, and reusable authoring elements.</li>
</ul>

<p>
In short, <code>IDE/</code> defines how a FROG IDE should be organized without making the language dependent on one specific editor.
</p>

<h3>Root files</h3>

<ul>
  <li><code>Readme.md</code> — repository landing page and architectural overview,</li>
  <li><code>LICENSE</code> — repository license,</li>
  <li><code>CONTRIBUTING.md</code> — contribution process and contribution rules,</li>
  <li><code>CLA.md</code> — contributor license agreement requirements,</li>
  <li><code>FROG logo.svg</code> — official logo asset,</li>
  <li><code>frog-orville-chart.png</code> — positioning illustration used by the repository.</li>
</ul>

<hr/>

<h2 id="specification-architecture">Specification architecture</h2>

<p>
The repository is intentionally split into distinct architectural layers:
</p>

<ul>
  <li><strong>Expression</strong> — canonical source representation and source-level semantics,</li>
  <li><strong>Libraries</strong> — standardized primitive vocabularies,</li>
  <li><strong>IDE</strong> — authoring architecture and editor-facing models.</li>
</ul>

<p>
The repository also currently retains a <strong>Language</strong> directory as a transition and semantic-continuity layer.
</p>

<p>
This separation is deliberate.
It prevents the language from being reduced to one editor, one runtime, or one vendor implementation.
</p>

<hr/>

<h2 id="program-representation">Program representation</h2>

<p>
FROG distinguishes three conceptual representation levels:
</p>

<ul>
  <li><strong>FROG Expression</strong> — the serialized source representation stored in a <code>.frog</code> file,</li>
  <li><strong>FROG Program Model</strong> — the canonical editable in-memory representation reconstructed by tools,</li>
  <li><strong>FROG Execution IR</strong> — the execution-oriented representation derived from the validated Program Model.</li>
</ul>

<p>
This distinction is essential:
</p>

<ul>
  <li>the language remains stable even if IDE implementations evolve,</li>
  <li>editing concerns remain separate from execution concerns,</li>
  <li>execution-oriented lowering remains explicit and auditable.</li>
</ul>

<hr/>

<h2 id="execution-architecture">Execution architecture</h2>

<p>
A conforming ecosystem may conceptually follow the pipeline below:
</p>

<pre><code>FROG Expression (.frog)
        ↓ parse
Parsed source
        ↓ validate
Validated Program Model
        ↓ lower
FROG Execution IR
        ↓ compile or interpret
Target-specific executable form
        ↓
Runtime execution</code></pre>

<p>
This architecture enforces a clean separation between:
</p>

<ul>
  <li>authoring,</li>
  <li>validation,</li>
  <li>lowering,</li>
  <li>compilation,</li>
  <li>runtime execution.</li>
</ul>

<hr/>

<h2 id="execution-targets">Execution targets</h2>

<p>
FROG is designed to remain hardware-agnostic while supporting different deployment classes.
</p>

<p>
Target ecosystems may include:
</p>

<ul>
  <li>desktop execution,</li>
  <li>industrial control systems,</li>
  <li>embedded targets,</li>
  <li>real-time environments,</li>
  <li>edge and accelerated systems,</li>
  <li>heterogeneous compute targets.</li>
</ul>

<p>
The language itself remains separate from any one execution backend.
</p>

<hr/>

<h2 id="open-industrial-hardware-standard">Open industrial hardware standard</h2>

<p>
FROG is intended to provide an open language foundation compatible with industrial and hardware-oriented engineering workflows.
</p>

<p>
The long-term objective is not only open source code.
It is also open language interoperability:
</p>

<ul>
  <li>multiple IDEs may author the same language,</li>
  <li>multiple compilers may lower the same validated model,</li>
  <li>multiple runtimes may execute compatible target artifacts,</li>
  <li>multiple hardware ecosystems may expose support without owning the language itself.</li>
</ul>

<hr/>

<h2 id="security-and-optimization">Security &amp; optimization</h2>

<p>
Because FROG defines explicit graphs, explicit interfaces, and explicit local-memory semantics,
it provides a good basis for:
</p>

<ul>
  <li>auditable program structure,</li>
  <li>predictable validation pipelines,</li>
  <li>execution analysis,</li>
  <li>target-specific optimization,</li>
  <li>deterministic deployment-oriented lowering.</li>
</ul>

<p>
Security and optimization are not afterthoughts layered on top of hidden semantics.
They are enabled by structural explicitness.
</p>

<hr/>

<h2 id="interoperability">Interoperability</h2>

<p>
FROG is designed for interoperability at several levels:
</p>

<ul>
  <li><strong>source interoperability</strong> — the canonical <code>.frog</code> file is readable and tool-independent,</li>
  <li><strong>editing interoperability</strong> — multiple IDEs may reconstruct equivalent Program Models,</li>
  <li><strong>execution interoperability</strong> — multiple toolchains may lower validated programs to target-specific artifacts,</li>
  <li><strong>ecosystem interoperability</strong> — the language remains separate from vendor lock-in.</li>
</ul>

<hr/>

<h2 id="language-separation">Language separation</h2>

<p>
One of the core principles of FROG is explicit architectural separation:
</p>

<ul>
  <li>language is not IDE,</li>
  <li>IDE is not runtime,</li>
  <li>runtime is not hardware,</li>
  <li>public interface is not front panel,</li>
  <li>diagram is not connector,</li>
  <li>natural widget value flow is not object-style widget interaction.</li>
</ul>

<p>
This separation is what makes FROG durable as an open language rather than as a single product implementation.
</p>

<hr/>

<h2 id="status">Status</h2>

<p>
FROG is currently specified as an open draft language architecture and source specification.
The repository is being progressively refined toward a coherent, canonical, long-term language definition.
</p>

<p>
Current repository direction includes:
</p>

<ul>
  <li>stabilizing the canonical source specification,</li>
  <li>clarifying language semantics,</li>
  <li>standardizing the core primitive library,</li>
  <li>defining IDE responsibilities without coupling the language to one implementation.</li>
</ul>

<hr/>

<h2 id="license">License</h2>

<p>
FROG is distributed under the Apache 2.0 license.
External contributions are governed through the repository contribution process and Contributor License Agreement requirements.
</p>

<hr/>

<p align="center">
  <strong>FROG — Free Open Graphical Language</strong><br/>
  Open graphical dataflow programming, specified as a language rather than owned as a product.
</p>
