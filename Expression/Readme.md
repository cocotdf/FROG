<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="150" />
</p>

<h1 align="center">🐸 FROG Expression Specification</h1>

<p align="center">
  Canonical source specification for <strong>.frog</strong> programs<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope-of-this-directory">2. Scope of this Directory</a></li>
  <li><a href="#specification-documents">3. Specification Documents</a></li>
  <li><a href="#what-a-frog-file-describes">4. What a <code>.frog</code> File Describes</a></li>
  <li><a href="#representation-levels">5. Representation Levels</a></li>
  <li><a href="#file-tree-and-artifact-families">6. File Tree and Artifact Families</a></li>
  <li><a href="#file-types">7. File Types</a></li>
  <li><a href="#top-level-json-structure">8. Top-Level JSON Structure</a></li>
  <li><a href="#section-presence-rules">9. Section Presence Rules</a></li>
  <li><a href="#sections-overview">10. Sections Overview</a></li>
  <li><a href="#cross-cutting-subsystems">11. Cross-Cutting Subsystems</a></li>
  <li><a href="#interface-connector-and-front-panel">12. Interface, Connector, and Front Panel</a></li>
  <li><a href="#execution-and-validation">13. Execution and Validation</a></li>
  <li><a href="#canonical-formatting-and-ordering">14. Canonical Formatting and Ordering</a></li>
  <li><a href="#normative-terminology">15. Normative Terminology</a></li>
  <li><a href="#status">16. Status</a></li>
  <li><a href="#license">17. License</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the canonical source specification of FROG — Free Open Graphical Language.
</p>

<p>
The fundamental executable unit of the language is a FROG.
A FROG is a complete graphical dataflow program represented by a structured JSON source file with the <code>.frog</code> extension.
</p>

<p>
That canonical source file is called the <strong>FROG Expression</strong>.
It is the authoritative, editable, transparent, version-control-friendly description of a FROG program.
</p>

<p>
The purpose of this directory is to define:
</p>

<ul>
  <li>the canonical top-level structure of a <code>.frog</code> file,</li>
  <li>the required and optional source sections of that file,</li>
  <li>the source-level meaning and representation of those sections,</li>
  <li>the cross-cutting source subsystems that apply across those sections, including the type system, the widget model, the widget interaction model, and the source-facing representation of structures and local-memory constructs.</li>
</ul>

<p>
This directory is about the authoritative source form of a FROG.
It is not the complete runtime architecture, not the complete IDE implementation model, and not the complete execution IR.
</p>

<p>
Cross-cutting execution semantics are related to this source specification but are not owned here when they belong to the normative execution meaning of the language itself.
</p>

<hr/>

<h2 id="scope-of-this-directory">2. Scope of this Directory</h2>

<p>
This directory specifies the source expression of a FROG program.
It defines what is serialized in the canonical <code>.frog</code> file and how that source MUST be interpreted structurally as source.
</p>

<p>
This specification does not attempt to fully define:
</p>

<ul>
  <li>the complete runtime architecture,</li>
  <li>the complete in-memory editable program model used by IDE implementations,</li>
  <li>the complete execution-oriented IR used by compilers or runtimes,</li>
  <li>the complete cross-cutting execution semantics of the language,</li>
  <li>the complete standard library surface of FROG primitives,</li>
  <li>the complete standard library surface of FROG UI widgets.</li>
</ul>

<p>
Those concerns are specified elsewhere in the repository.
This directory focuses on the authoritative source form.
</p>

<hr/>

<h2 id="specification-documents">3. Specification Documents</h2>

<p>
The FROG Expression is defined through the following documents in this directory:
</p>

<ul>
  <li><code>Metadata.md</code></li>
  <li><code>Type.md</code></li>
  <li><code>Interface.md</code></li>
  <li><code>Connector.md</code></li>
  <li><code>Diagram.md</code></li>
  <li><code>Front panel.md</code></li>
  <li><code>Widget.md</code></li>
  <li><code>Widget interaction.md</code></li>
  <li><code>Control structures.md</code></li>
  <li><code>State and cycles.md</code></li>
  <li><code>Icon.md</code></li>
  <li><code>IDE preferences.md</code></li>
  <li><code>Cache.md</code></li>
</ul>

<p>
Some of these documents define dedicated top-level source sections such as:
</p>

<ul>
  <li><code>metadata</code></li>
  <li><code>interface</code></li>
  <li><code>connector</code></li>
  <li><code>diagram</code></li>
  <li><code>front_panel</code></li>
  <li><code>icon</code></li>
  <li><code>ide</code></li>
  <li><code>cache</code></li>
</ul>

<p>
Other documents define cross-cutting source subsystems used throughout the source format.
In particular:
</p>

<ul>
  <li><code>Type.md</code> defines canonical value type expressions and source-level type rules used throughout the source format.</li>
  <li><code>Widget.md</code> defines the widget object model, including classes, roles, value behavior, parts, properties, methods, and events.</li>
  <li><code>Widget interaction.md</code> defines how executable diagrams may interact with widgets through standardized diagram-level interaction mechanisms.</li>
  <li><code>Control structures.md</code> defines the source-facing representation of language structures such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>.</li>
  <li><code>State and cycles.md</code> defines the source-facing representation of explicit local memory and feedback-cycle formation constraints.</li>
</ul>

<p>
The current source specification also depends on normative specifications defined outside this directory.
At the current repository stage, that includes:
</p>

<ul>
  <li><code>Language/Control structures.md</code> — normative execution semantics for standard control structures,</li>
  <li><code>Language/State and cycles.md</code> — normative execution semantics for local memory and valid feedback cycles,</li>
  <li><code>Libraries/Core.md</code> — foundational primitive definitions such as <code>frog.core.add</code>, <code>frog.core.mul</code>, and <code>frog.core.delay</code>,</li>
  <li><code>Libraries/Math.md</code> — numeric scalar primitives beyond the minimal core,</li>
  <li><code>Libraries/Collections.md</code> — array-oriented collection primitives,</li>
  <li><code>Libraries/Text.md</code> — text-processing primitives,</li>
  <li><code>Libraries/IO.md</code> — file, path, byte, and related I/O primitives,</li>
  <li><code>Libraries/Signal.md</code> — first-wave signal-processing primitives,</li>
  <li><code>Libraries/UI.md</code> — standardized executable widget-interaction primitives,</li>
  <li><code>Libraries/Connectivity.md</code> — standardized interoperability primitives.</li>
</ul>

<p>
Accordingly, <code>Expression/</code> is the canonical home of the source-format specification, while <code>Language/</code> and <code>Libraries/</code> are normative external dependencies for execution meaning used by validated executable diagrams.
</p>

<hr/>

<h2 id="what-a-frog-file-describes">4. What a <code>.frog</code> File Describes</h2>

<p>
A canonical <code>.frog</code> source file describes a complete FROG program.
</p>

<p>
Its required source sections define:
</p>

<ul>
  <li><code>metadata</code> — identity, documentation, authorship, and versioning information,</li>
  <li><code>interface</code> — the public typed inputs and outputs of the program,</li>
  <li><code>diagram</code> — the executable dataflow graph as canonical source representation.</li>
</ul>

<p>
Its optional source sections MAY define:
</p>

<ul>
  <li><code>front_panel</code> — the user-facing interaction layer and widget composition,</li>
  <li><code>connector</code> — the graphical projection of the public interface when the FROG is reused as a node,</li>
  <li><code>icon</code> — the graphical icon associated with the FROG,</li>
  <li><code>ide</code> — IDE-facing preferences and recoverability metadata serialized with the FROG itself,</li>
  <li><code>cache</code> — optional non-authoritative derived data used to accelerate tooling workflows.</li>
</ul>

<p>
A FROG MAY therefore be diagram-only.
A conforming canonical source file does not require a user-facing interaction layer unless such a layer is intentionally part of the program description.
</p>

<p>
A <code>.frog</code> file is a transparent source representation.
It MUST NOT require hidden compiled payloads in order to define the program as canonical source.
</p>

<hr/>

<h2 id="representation-levels">5. Representation Levels</h2>

<p>
FROG distinguishes three conceptual representation levels:
</p>

<ul>
  <li><strong>FROG Expression</strong> — the serialized source representation stored in a <code>.frog</code> file,</li>
  <li><strong>FROG Program Model</strong> — the canonical editable in-memory representation reconstructed by tools,</li>
  <li><strong>FROG Execution IR</strong> — the execution-oriented representation derived from the validated program model.</li>
</ul>

<p>
This directory primarily specifies the FROG Expression.
Tooling MAY reconstruct a Program Model from the Expression and MAY derive an Execution IR from the validated Program Model.
However, the canonical editable source of a FROG remains the <code>.frog</code> file itself.
</p>

<hr/>

<h2 id="file-tree-and-artifact-families">6. File Tree and Artifact Families</h2>

<pre><code>FROG
│
├─ Canonical source
│   └─ example.frog
│
├─ Optional cache artifact
│   └─ example.frog.cache
│
└─ Optional distribution artifact
    └─ example.frogbin</code></pre>

<p>
The <code>.frog</code> file is the canonical source representation.
Other file forms are optional tool artifacts.
</p>

<hr/>

<h2 id="file-types">7. File Types</h2>

<h3>7.1 <code>.frog</code> — canonical source</h3>

<ul>
  <li>Human-readable JSON</li>
  <li>Version-control friendly</li>
  <li>Contains all required source sections</li>
  <li>May contain optional source sections</li>
  <li>Represents the canonical FROG Expression</li>
</ul>

<h3>7.2 <code>.frog.cache</code> — optional cache artifact</h3>

<ul>
  <li>Generated by tools</li>
  <li>May contain cached analysis or execution-oriented data</li>
  <li>Used to accelerate loading, validation, or compilation workflows</li>
  <li>Safe to delete and regenerate</li>
  <li>Non-authoritative with respect to program meaning</li>
</ul>

<p>
See: <code>Cache.md</code>
</p>

<h3>7.3 <code>.frogbin</code> — optional distribution artifact</h3>

<ul>
  <li>Intended for distribution or deployment workflows</li>
  <li>May omit non-essential source detail</li>
  <li>May contain execution-oriented or compiled payloads</li>
  <li>Is not the canonical editable source representation</li>
</ul>

<hr/>

<h2 id="top-level-json-structure">8. Top-Level JSON Structure</h2>

<p>
The canonical top-level source structure of a FROG program is:
</p>

<pre><code>{
  "spec_version": "0.1",

  "metadata": {},
  "interface": {},
  "connector": {},

  "diagram": {},
  "front_panel": {},

  "icon": {},
  "ide": {},

  "cache": {}
}</code></pre>

<p>
This top-level object contains both required and optional sections.
Only the required sections define the minimal canonical source program.
Optional sections MUST NOT redefine authoritative program semantics.
</p>

<p>
FROG v0.1 does not define:
</p>

<ul>
  <li>a mandatory top-level <code>types</code> section,</li>
  <li>a mandatory top-level <code>widgets</code> section,</li>
  <li>a mandatory top-level <code>widget_interactions</code> section.</li>
</ul>

<p>
Instead:
</p>

<ul>
  <li>type information is embedded locally through canonical type expressions,</li>
  <li>widget instances are embedded inside <code>front_panel</code> when a front panel is present,</li>
  <li>widget interactions are expressed inside <code>diagram</code>.</li>
</ul>

<hr/>

<h2 id="section-presence-rules">9. Section Presence Rules</h2>

<p>
A canonical <code>.frog</code> source file MUST contain:
</p>

<ul>
  <li><code>spec_version</code></li>
  <li><code>metadata</code></li>
  <li><code>interface</code></li>
  <li><code>diagram</code></li>
</ul>

<p>
A canonical <code>.frog</code> source file MAY additionally contain:
</p>

<ul>
  <li><code>front_panel</code></li>
  <li><code>connector</code></li>
  <li><code>icon</code></li>
  <li><code>ide</code></li>
  <li><code>cache</code></li>
</ul>

<p>
The <code>front_panel</code> section is optional.
It SHOULD be present when the FROG intentionally includes a user-facing interaction layer.
When absent, the FROG is interpreted as a diagram-only program with no serialized front-panel composition.
</p>

<p>
The <code>connector</code> section is optional.
It SHOULD be present when the FROG is intended to be reused as a graphical node inside another diagram.
</p>

<p>
Optional sections MUST NOT modify the authoritative execution semantics established by the validated source-derived program representation.
</p>

<hr/>

<h2 id="sections-overview">10. Sections Overview</h2>

<h3>10.1 Metadata</h3>

<p>
Required section defining identity, documentation, authorship, and related descriptive information.
</p>

<p>
Detailed specification: <code>Metadata.md</code>
</p>

<h3>10.2 Interface</h3>

<p>
Required section defining the public typed inputs and outputs of the FROG.
All declared types MUST use canonical FROG type expressions.
</p>

<p>
Detailed specifications: <code>Interface.md</code>, <code>Type.md</code>
</p>

<h3>10.3 Connector</h3>

<p>
Optional section defining the graphical mapping of interface ports when the FROG is reused as a node.
The connector never defines new logical ports.
</p>

<p>
Detailed specification: <code>Connector.md</code>
</p>

<h3>10.4 Diagram</h3>

<p>
Required section defining the executable dataflow graph of the FROG.
The diagram contains nodes, edges, dependencies, and annotations.
It is the authoritative source-level execution structure of the program.
</p>

<p>
Detailed specifications:
<code>Diagram.md</code>,
<code>Type.md</code>,
<code>Widget interaction.md</code>,
the source-facing companion documents <code>Control structures.md</code> and <code>State and cycles.md</code>,
the normative execution-semantics documents in <code>Language/</code>,
and the relevant primitive-library specifications in <code>Libraries/</code>.
</p>

<h3>10.5 Front Panel</h3>

<p>
Optional section defining the user interaction layer of the FROG through widget instances, layout, style, and related UI composition data.
</p>

<p>
When absent, the canonical source defines no serialized front-panel composition for that FROG.
</p>

<p>
Detailed specifications: <code>Front panel.md</code>, <code>Widget.md</code>
</p>

<h3>10.6 Icon</h3>

<p>
Optional section containing the icon used by tools when the FROG is represented as a reusable node.
</p>

<p>
Detailed specification: <code>Icon.md</code>
</p>

<h3>10.7 IDE Preferences</h3>

<p>
Optional section containing IDE-facing preferences and recoverability metadata serialized with the FROG itself.
This section belongs to the FROG Expression because a FROG behaves as a durable editable program unit and may embed
source-level IDE preferences together with non-authoritative authoring recoverability aids.
</p>

<p>
Runtimes and other execution-facing systems MUST ignore this section for execution semantics.
</p>

<p>
Detailed specification: <code>IDE preferences.md</code>
</p>

<h3>10.8 Cache</h3>

<p>
Optional section containing derived, non-authoritative tooling data used to accelerate workflows.
</p>

<p>
Detailed specification: <code>Cache.md</code>
</p>

<hr/>

<h2 id="cross-cutting-subsystems">11. Cross-Cutting Subsystems</h2>

<h3>11.1 Type System</h3>

<p>
FROG v0.1 defines a normative built-in type system described in <code>Type.md</code>.
</p>

<p>
This subsystem applies wherever values are declared, connected, constrained, validated, or coerced, including:
</p>

<ul>
  <li>interface ports,</li>
  <li>diagram ports and edge validation,</li>
  <li>structure boundaries,</li>
  <li>typed configuration values such as <code>default</code> or <code>initial</code>,</li>
  <li>widget primary values,</li>
  <li>typed widget members.</li>
</ul>

<p>
The type system is cross-cutting.
It is not represented as a dedicated required top-level section.
</p>

<h3>11.2 Widget Model</h3>

<p>
FROG v0.1 defines a normative widget object model described in <code>Widget.md</code>.
</p>

<p>
A widget is not merely a drawing.
It is a structured UI object with identity, class, role, optional typed value, properties, methods, and optional attached parts.
</p>

<p>
The widget model is cross-cutting.
It governs widget instances contained inside <code>front_panel</code> when that section is present.
</p>

<h3>11.3 Widget Interaction Model</h3>

<p>
FROG v0.1 defines a normative widget interaction model described in <code>Widget interaction.md</code>.
</p>

<p>
This model governs diagram-level interaction with widgets through standardized mechanisms such as:
</p>

<ul>
  <li>property read,</li>
  <li>property write,</li>
  <li>method invocation.</li>
</ul>

<p>
These interactions are represented inside the executable diagram rather than as a dedicated top-level source section.
</p>

<p>
The current source-level widget interaction model already uses standardized primitive identifiers in the <code>frog.ui.*</code> namespace.
Future standardized UI primitive-library specifications MUST remain consistent with that source-level interaction model.
</p>

<h3>11.4 Control-Structure and Local-Memory Source Dependencies</h3>

<p>
FROG v0.1 includes source-facing representation rules for structures, explicit local memory, and feedback-cycle formation inside this directory:
</p>

<ul>
  <li><code>Control structures.md</code> defines the source-facing representation of structure families and their serialized form,</li>
  <li><code>State and cycles.md</code> defines the source-facing representation of explicit local-memory elements and feedback-cycle constraints.</li>
</ul>

<p>
However, the normative execution semantics for these topics are owned by <code>Language/</code>.
</p>

<ul>
  <li><code>Language/Control structures.md</code> defines the normative execution meaning of standard language structures,</li>
  <li><code>Language/State and cycles.md</code> defines the normative execution meaning of local memory and valid cycles.</li>
</ul>

<p>
This separation allows <code>Expression/</code> to remain the canonical source-specification layer while <code>Language/</code> remains the normative execution-semantics layer.
The standardized primitive catalogs consumed by executable diagrams remain defined in <code>Libraries/</code>.
</p>

<hr/>

<h2 id="interface-connector-and-front-panel">12. Interface, Connector, and Front Panel</h2>

<p>
FROG explicitly distinguishes three concepts that may appear related but serve different purposes:
</p>

<ul>
  <li><code>interface</code> — the public logical contract of the FROG,</li>
  <li><code>connector</code> — the graphical projection of that public contract when the FROG is reused as a node,</li>
  <li><code>front_panel</code> — the optional user-facing interaction layer of the FROG itself.</li>
</ul>

<h3>12.1 Interface</h3>

<p>
The interface defines public inputs and outputs.
It is part of the program contract and is used for reuse, validation, and boundary semantics.
</p>

<h3>12.2 Connector</h3>

<p>
The connector defines where those public ports appear on the perimeter of the reusable node representation.
It is graphical mapping, not logical contract.
</p>

<h3>12.3 Front Panel</h3>

<p>
When present, the front panel defines widgets, layout, and visual interaction for the FROG itself.
It does not define the public API.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>a front-panel widget does not create a public interface port by itself,</li>
  <li>a control widget is not automatically a public input,</li>
  <li>an indicator widget is not automatically a public output.</li>
</ul>

<p>
Any relationship between public interface behavior and front-panel behavior MUST be represented through the diagram.
</p>

<hr/>

<h2 id="execution-and-validation">13. Execution and Validation</h2>

<p>
The canonical <code>.frog</code> source file is the authoritative source artifact of the program.
However, execution is not performed directly from unvalidated raw text.
</p>

<p>
A conforming toolchain SHOULD apply the following conceptual pipeline:
</p>

<pre><code>FROG Expression
    ↓ parse
Parsed source
    ↓ validate
Validated source-derived program model
    ↓ lower
Execution-oriented representation
    ↓ execute or compile</code></pre>

<p>
Validation includes, as applicable:
</p>

<ul>
  <li>top-level section presence and structure checks,</li>
  <li>type-expression validation,</li>
  <li>interface consistency checks,</li>
  <li>connector consistency checks,</li>
  <li>diagram graph validation,</li>
  <li>front-panel and widget validation when <code>front_panel</code> is present,</li>
  <li>widget interaction validation,</li>
  <li>control-structure source validation,</li>
  <li>cycle and local-memory source validation,</li>
  <li>primitive reference validation against the relevant standardized library catalogs.</li>
</ul>

<p>
Normative execution meaning is derived from the validated program representation interpreted against the relevant language semantics and primitive specifications.
Optional sections such as <code>front_panel</code>, <code>icon</code>, <code>ide</code>, and <code>cache</code> MUST NOT redefine executable semantics.
</p>

<hr/>

<h2 id="canonical-formatting-and-ordering">14. Canonical Formatting and Ordering</h2>

<p>
Canonical source is JSON.
For interoperability and stable diffs, tools SHOULD preserve predictable formatting and section ordering.
</p>

<h3>14.1 Top-level ordering</h3>

<p>
When tools emit canonical source, they SHOULD preserve this top-level order:
</p>

<pre><code>{
  "spec_version": "0.1",

  "metadata": {},
  "interface": {},
  "connector": {},

  "diagram": {},
  "front_panel": {},

  "icon": {},
  "ide": {},

  "cache": {}
}</code></pre>

<p>
That ordering recommendation applies whether optional sections are present or absent.
Omitted optional sections SHOULD simply be omitted without changing the relative ordering of the remaining emitted sections.
</p>

<h3>14.2 Stable identifiers</h3>

<p>
Tools SHOULD preserve stable identifiers for:
</p>

<ul>
  <li>interface ports,</li>
  <li>diagram nodes,</li>
  <li>diagram edges,</li>
  <li>widget instances where a front panel is present,</li>
  <li>annotations where relevant.</li>
</ul>

<h3>14.3 Canonical local expressions</h3>

<p>
Tools SHOULD preserve canonical local forms for:
</p>

<ul>
  <li>type expressions,</li>
  <li>primitive identifiers,</li>
  <li>widget class identifiers,</li>
  <li>structure identifiers,</li>
  <li>property names and method names defined by active profiles.</li>
</ul>

<h3>14.4 Optional tool freedom</h3>

<p>
Pretty-printing details such as indentation width are not semantically significant.
However, tools SHOULD avoid needless churn in emitted source.
</p>

<hr/>

<h2 id="normative-terminology">15. Normative Terminology</h2>

<p>
The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY in this specification are to be interpreted in their ordinary normative sense:
</p>

<ul>
  <li>MUST / MUST NOT — absolute requirement or prohibition,</li>
  <li>SHOULD / SHOULD NOT — strong recommendation that may be overridden only with good reason,</li>
  <li>MAY — permitted option.</li>
</ul>

<hr/>

<h2 id="status">16. Status</h2>

<p>
This document describes the FROG Expression for specification version <code>0.1</code>.
</p>

<p>
FROG v0.1 is intentionally conservative.
It prioritizes explicit canonical source semantics, long-term durability, and tool interoperability over premature expansion of the language surface.
</p>

<p>
At the current repository stage, the standard primitive-library layer already extends beyond the minimal core.
Future revisions MAY continue to expand those external library catalogs while preserving the architectural role of <code>Expression/</code> as the canonical source-specification layer.
</p>

<p>
Future revisions SHOULD also preserve the core architectural distinctions already established here:
</p>

<ul>
  <li>source expression versus program model versus execution IR,</li>
  <li>canonical source representation versus normative execution semantics,</li>
  <li>public interface versus connector versus optional front panel,</li>
  <li>natural widget value flow versus object-style widget interaction,</li>
  <li>authoritative source sections versus non-authoritative optional artifacts.</li>
</ul>

<hr/>

<h2 id="license">17. License</h2>

<p>
This specification is part of the FROG repository and follows the repository licensing and governance rules.
</p>

<p>
See the repository root and associated licensing documents for the governing license terms of the specification text and related assets.
</p>
