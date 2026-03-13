<p align="center">
  <img src="FROG logo.svg" alt="FROG logo" width="150" />
</p>

<h1 align="center">🐸 FROG — Free Open Graphical Language</h1>

<p align="center">
  <strong>Free Open Graphical Dataflow Programming Language</strong><br/>
  FROG is an open, hardware-agnostic graphical dataflow programming language designed to describe computation as executable graphs while remaining accessible, explicit, deterministic, inspectable, and scalable across heterogeneous execution targets.
</p>

<p align="center">
  <a href="#what-is-frog">What is FROG?</a> •
  <a href="#positioning">Positioning</a> •
  <a href="#breaking-the-syntax-first-bottleneck">Breaking the syntax-first bottleneck</a> •
  <a href="#why-frog-exists">Why FROG exists</a> •
  <a href="#dataflow-programming">Dataflow programming</a> •
  <a href="#from-prototyping-to-critical-systems">From prototyping to critical systems</a> •
  <a href="#core-concept-diagram-and-front-panel">Core concept</a> •
  <a href="#repository-structure">Repository structure</a> •
  <a href="#specification-architecture">Specification architecture</a> •
  <a href="#program-representation">Program representation</a> •
  <a href="#execution-architecture">Execution architecture</a> •
  <a href="#execution-targets">Execution targets</a> •
  <a href="#open-industrial-hardware-standard">Open industrial hardware standard</a> •
  <a href="#security-and-optimization">Security &amp; Optimization</a> •
  <a href="#interoperability">Interoperability</a> •
  <a href="#separation-of-language-and-tooling">Language separation</a> •
  <a href="#project-status">Status</a> •
  <a href="#license">License</a>
</p>

<hr/>

<h2 id="what-is-frog">What is FROG?</h2>

<p>
FROG is an open, hardware-agnostic <strong>graphical dataflow programming language</strong>.
It represents computation as explicit executable graphs rather than as syntax-driven sequences of instructions.
</p>

<p>
Instead of describing a program primarily through ordered text,
FROG describes a program through:
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
Execution emerges from data availability, structural rules, explicit control structures, and explicit local-memory semantics rather than from manually authored instruction order.
</p>

<p>
FROG is designed to remain independent from any specific IDE, compiler, runtime, operating system, or hardware vendor.
This separation provides a durable basis for multiple independent implementations and long-term industrial interoperability.
</p>

<hr/>

<h2 id="positioning">Positioning</h2>

<p>
FROG is designed to combine the accessibility of graphical programming with the execution depth required for deterministic, industrial, embedded, and high-performance systems.
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
The goal is to shift complexity toward the system itself instead of toward syntax-first representation.
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
However, many historical graphical environments have been tightly coupled to proprietary ecosystems where language, tooling, runtime, and hardware support are inseparable.
</p>

<p>
That model limits portability, slows independent ecosystem growth, and prevents multiple vendors or toolchains from implementing the same language cleanly.
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
<strong>FROG is not an IDE.</strong><br/>
<strong>FROG is not a single runtime.</strong><br/>
<strong>FROG is not a vendor product.</strong><br/>
<strong>FROG is a language specification and execution model.</strong>
</p>

<hr/>

<h2 id="dataflow-programming">Dataflow programming</h2>

<p>
FROG follows a true <strong>dataflow execution model</strong>.
</p>

<p>
In traditional instruction-sequenced programming, execution is primarily described as ordered steps.
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

<h2 id="core-concept-diagram-and-front-panel">Core concept: Diagram and Front Panel</h2>

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
  <li><strong>object-style path</strong> — explicit widget access through <code>widget_reference</code> together with <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code>.</li>
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

<pre>
FROG/
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
└── frog-orville-chart.png
</pre>

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
  <li><code>Core.md</code> — the foundational <code>frog.core</code> primitive library,</li>
  <li><code>Math.md</code> — the standard <code>frog.math</code> library for numeric scalar operations beyond the minimal core,</li>
  <li><code>Collections.md</code> — the standard <code>frog.collections</code> library for array-oriented collection primitives,</li>
  <li><code>Text.md</code> — the standard <code>frog.text</code> library for text-processing primitives,</li>
  <li><code>IO.md</code> — the standard <code>frog.io</code> library for file, path, byte, and related I/O primitives,</li>
  <li><code>Signal.md</code> — the standard <code>frog.signal</code> library for first-wave signal-processing primitives,</li>
  <li><code>UI.md</code> — the standard <code>frog.ui</code> library for executable widget interaction primitives,</li>
  <li><code>Connectivity.md</code> — the standard <code>frog.connectivity</code> library for Python, native/shared-library, .NET, SQL, and related interoperability primitives.</li>
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
FROG programs exist across three distinct representation levels.
</p>

<h3>FROG Expression</h3>

<p>
The <strong>FROG Expression</strong> is the serialized source representation stored in a <code>.frog</code> file.
It is the canonical source form of a FROG program.
</p>

<p>
A FROG is represented by a structured, human-readable JSON source file with the <code>.frog</code> extension.
That canonical source file is transparent, editable, portable, and version-control-friendly.
</p>

<p>
Depending on the program, the Expression may contain:
</p>

<ul>
  <li>metadata,</li>
  <li>interface definition,</li>
  <li>connector definition,</li>
  <li>diagram definition,</li>
  <li>front-panel definition,</li>
  <li>widget descriptions,</li>
  <li>icon data,</li>
  <li>IDE-interpreted preferences,</li>
  <li>optional non-authoritative cache sections.</li>
</ul>

<p>
The canonical source structure is centered around top-level sections such as
<code>metadata</code>, <code>interface</code>, <code>connector</code>, <code>diagram</code>, <code>front_panel</code>, <code>icon</code>, <code>ide</code>, and <code>cache</code>.
Optional sections MUST NOT redefine authoritative program semantics.
</p>

<p>
The Expression is designed for:
</p>

<ul>
  <li>human readability,</li>
  <li>version control compatibility,</li>
  <li>tool interoperability,</li>
  <li>long-term durability.</li>
</ul>

<h3>FROG Program Model</h3>

<p>
The <strong>FROG Program Model</strong> is the canonical editable in-memory representation used by tools.
It is reconstructed from the FROG Expression and maintained during editing.
</p>

<p>
It is the authoritative form of the program during authoring.
It maintains coherent relationships between:
</p>

<ul>
  <li>interface declarations and <code>interface_input</code> / <code>interface_output</code> nodes,</li>
  <li>front-panel widget declarations and <code>widget_value</code> / <code>widget_reference</code> nodes,</li>
  <li>structure nodes and their owned regions,</li>
  <li>semantic graph content and source-level layout information.</li>
</ul>

<h3>FROG Execution IR</h3>

<p>
The <strong>FROG Execution IR</strong> is the canonical execution-oriented representation derived from the validated Program Model.
It contains normalized information required for validation, scheduling, lowering, optimization, compilation, and target-oriented execution workflows.
</p>

<p>
It should be understood as an <strong>open, inspectable execution representation</strong> rather than as a hidden vendor artifact.
Programs are not executed directly from raw source serialization.
Execution occurs from validated execution-oriented representations derived from source.
</p>

<hr/>

<h2 id="execution-architecture">Execution architecture</h2>

<p>
A conforming ecosystem may conceptually follow the architecture below:
</p>

<pre>
                 FROG IDE
        +---------------------------+
        | Diagram + Front Panel UI  |
        +-------------+-------------+
                      |
                      v
             FROG Program Model
         (editable in-memory model)
              /               \
             /                 \
            v                   v
   FROG Expression        Validation / Lowering
(.frog source,                   |
 human-readable JSON)            v
                         FROG Execution IR
                  (open, inspectable execution form)
                                 |
                                 v
                    Compiler(s) / Backend(s)
                                 |
                                 v
                           Target Runtime
                                 |
                                 v
       CPU / RT / GPU / FPGA / Embedded / MCU / Industrial Edge
</pre>

<p>
During development, tools maintain the Program Model.
Saving serializes that model into canonical source.
Execution requests lower the validated model into FROG Execution IR, which is then consumed by compilers, backends, and runtimes.
</p>

<p>
This architecture enforces a clean separation between:
</p>

<ul>
  <li>authoring,</li>
  <li>source serialization,</li>
  <li>editable in-memory representation,</li>
  <li>execution-oriented lowering,</li>
  <li>compilation and backend processing,</li>
  <li>runtime execution.</li>
</ul>

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
Possible execution profiles may include:
</p>

<ul>
  <li><strong>FROG Core</strong>,</li>
  <li><strong>FROG RT</strong>,</li>
  <li><strong>FROG FPGA</strong>,</li>
  <li><strong>FROG Embedded</strong>,</li>
  <li><strong>FROG MCU</strong>,</li>
  <li><strong>FROG Accelerated</strong>.</li>
</ul>

<p>
The programming model remains conceptually stable across these targets.
What changes is the execution profile, the lowering strategy, the backend, and the available platform services.
</p>

<hr/>

<h2 id="open-industrial-hardware-standard">Open industrial hardware standard</h2>

<p>
FROG aims to be more than a language that merely supports multiple targets.
Its long-term goal is to provide an <strong>open industrial graphical programming standard</strong> that hardware and software ecosystems can build on without requiring a proprietary language boundary.
</p>

<p>
That means hardware vendors, runtime builders, industrial software platforms, embedded-system providers, and specialized toolchain developers should be able to support the same core language while preserving their own:
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
  <li>vendor-certified industrial profiles.</li>
</ul>

<hr/>

<h2 id="security-and-optimization">Security and optimization by design</h2>

<p>
FROG integrates validation and optimization into its architecture.
</p>

<p>
Base principles include:
</p>

<ul>
  <li>strict type validation,</li>
  <li>graph validation before execution,</li>
  <li>controlled execution boundaries,</li>
  <li>explicit structure semantics,</li>
  <li>explicit local-memory semantics for valid feedback loops,</li>
  <li>deterministic execution guarantees where supported by the active profile.</li>
</ul>

<p>
Optimization occurs primarily at the Execution IR and compilation levels:
</p>

<ul>
  <li>graph simplification,</li>
  <li>dead-node elimination,</li>
  <li>constant folding,</li>
  <li>memory optimization,</li>
  <li>parallel scheduling where valid,</li>
  <li>target-specific lowering,</li>
  <li>profile-aware specialization.</li>
</ul>

<hr/>

<h2 id="interoperability">Interoperability</h2>

<p>
FROG is designed for interoperability at several levels:
</p>

<ul>
  <li><strong>source interoperability</strong> — the canonical <code>.frog</code> file is readable, structured, and tool-independent,</li>
  <li><strong>editing interoperability</strong> — multiple IDEs may reconstruct equivalent Program Models,</li>
  <li><strong>execution interoperability</strong> — multiple toolchains may lower validated programs into compatible execution-oriented forms and target artifacts,</li>
  <li><strong>ecosystem interoperability</strong> — the language remains separate from vendor lock-in.</li>
</ul>

<p>
FROG is also designed to integrate with external languages and external platform APIs through stable interoperation mechanisms.
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
This is also essential for hardware support, because drivers, SDKs, real-time services, FPGA toolflows, and embedded platform stacks can be integrated without collapsing the language into one closed ecosystem.
</p>

<hr/>

<h2 id="separation-of-language-and-tooling">Language separation</h2>

<p>
FROG explicitly separates:
</p>

<ul>
  <li>the language specification,</li>
  <li>the canonical source representation,</li>
  <li>the editable program model,</li>
  <li>the execution-oriented representation,</li>
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
  <li>IDE from runtime,</li>
  <li>runtime from hardware,</li>
  <li>public interface from front panel,</li>
  <li>diagram from connector,</li>
  <li>natural widget value flow from object-style widget interaction.</li>
</ul>

<p>
This enables:
</p>

<ul>
  <li>multiple IDE implementations,</li>
  <li>multiple compilers,</li>
  <li>multiple backends,</li>
  <li>multiple runtimes,</li>
  <li>multiple vendor ecosystems supporting the same language,</li>
  <li>independent ecosystem evolution around a shared graphical standard.</li>
</ul>

<p>
The specification defines the language, not one product.
</p>

<hr/>

<h2 id="project-status">Project status</h2>

<p>
FROG is currently under active design.
The language specification, representation model, execution architecture, widget system, structure model, standard libraries, and tooling architecture are evolving toward a coherent v0.1 foundation.
</p>

<p>
Current repository direction includes:
</p>

<ul>
  <li>stabilizing the canonical source specification,</li>
  <li>clarifying language semantics and execution semantics,</li>
  <li>growing the standard primitive libraries beyond the minimal core,</li>
  <li>defining IDE responsibilities without coupling the language to one implementation,</li>
  <li>preparing the transition toward a more fully specified execution-oriented layer.</li>
</ul>

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
