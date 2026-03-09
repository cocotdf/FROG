<h1 align="center">🐸 FROG Expression Specification</h1>

<p align="center">
  Canonical source format for <strong>.frog</strong> programs<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope">2. Scope of this directory</a></li>
  <li><a href="#spec-documents">3. Specification documents</a></li>
  <li><a href="#what-a-frog-file-describes">4. What a <code>.frog</code> file describes</a></li>
  <li><a href="#representation-levels">5. Representation levels</a></li>
  <li><a href="#file-tree">6. FROG file tree</a></li>
  <li><a href="#file-types">7. File types</a></li>
  <li><a href="#top-level-structure">8. Top-level JSON structure</a></li>
  <li><a href="#section-presence-rules">9. Section presence rules</a></li>
  <li><a href="#sections-overview">10. Sections overview</a></li>
  <li><a href="#cross-cutting-subsystems">11. Cross-cutting subsystems</a></li>
  <li><a href="#interface-connector-front-panel">12. Interface, connector, and front panel</a></li>
  <li><a href="#execution-and-validation">13. Execution and validation</a></li>
  <li><a href="#canonical-formatting">14. Canonical formatting and ordering</a></li>
  <li><a href="#normative-terminology">15. Normative terminology</a></li>
  <li><a href="#status">16. Status</a></li>
  <li><a href="#license">17. License</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the canonical source specification of <strong>FROG — Free Open Graphical Language</strong>.
</p>

<p>
The fundamental program unit of the language is called a <strong>Frog</strong>.
A Frog is a complete graphical dataflow program represented by a structured JSON source file with the <code>.frog</code> extension.
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
  <li>the cross-cutting subsystems that apply across those sections, such as the type system, widget model, and widget interaction model.</li>
</ul>

<hr/>

<h2 id="scope">2. Scope of this directory</h2>

<p>
This directory specifies the <strong>source expression</strong> of a FROG program.
It defines what is serialized in the canonical <code>.frog</code> file and how that source must be interpreted structurally.
</p>

<p>
This specification does <strong>not</strong> attempt to fully define:
</p>

<ul>
  <li>the complete runtime architecture,</li>
  <li>the full in-memory editable program model used by IDE implementations,</li>
  <li>the full execution-oriented IR used by compilers or runtimes,</li>
  <li>the complete standard library of FROG functions.</li>
</ul>

<p>
Those concerns may be specified elsewhere.
This directory focuses on the authoritative source form.
</p>

<hr/>

<h2 id="spec-documents">3. Specification documents</h2>

<p>
The FROG Expression is defined through the following documents:
</p>

<ul>
  <li><a href="./Metadata.md"><strong>Metadata.md</strong></a></li>
  <li><a href="./Type.md"><strong>Type.md</strong></a></li>
  <li><a href="./Interface.md"><strong>Interface.md</strong></a></li>
  <li><a href="./Connector.md"><strong>Connector.md</strong></a></li>
  <li><a href="./Diagram.md"><strong>Diagram.md</strong></a></li>
  <li><a href="./Front%20panel.md"><strong>Front panel.md</strong></a></li>
  <li><a href="./Widget.md"><strong>Widget.md</strong></a></li>
  <li><a href="./Widget%20interaction.md"><strong>Widget interaction.md</strong></a></li>
  <li><a href="./Icon.md"><strong>Icon.md</strong></a></li>
  <li><a href="./IDE%20preferences.md"><strong>IDE preferences.md</strong></a></li>
  <li><a href="./Cache.md"><strong>Cache.md</strong></a></li>
</ul>

<p>
Some of these documents define dedicated top-level source sections such as <strong>metadata</strong>, <strong>interface</strong>, <strong>diagram</strong>, or <strong>front_panel</strong>.
Others define cross-cutting subsystems used throughout the source format.
</p>

<p>
In particular:
</p>

<ul>
  <li><strong>Type.md</strong> defines canonical type expressions, built-in types, compatibility rules, and coercion rules.</li>
  <li><strong>Widget.md</strong> defines the object model of front panel widgets, including classes, roles, value behavior, parts, properties, methods, and events.</li>
  <li><strong>Widget interaction.md</strong> defines how executable diagrams may interact with widgets through standardized diagram-level interaction mechanisms.</li>
</ul>

<hr/>

<h2 id="what-a-frog-file-describes">4. What a <code>.frog</code> file describes</h2>

<p>
A canonical <code>.frog</code> source file describes a complete FROG program.
</p>

<p>
Its required source sections define:
</p>

<ul>
  <li><strong>metadata</strong> — identity, documentation, authorship, and versioning information,</li>
  <li><strong>interface</strong> — the public typed inputs and outputs of the program,</li>
  <li><strong>diagram</strong> — the executable dataflow graph,</li>
  <li><strong>front_panel</strong> — the user-facing interaction layer and widget composition.</li>
</ul>

<p>
Its optional source sections may define:
</p>

<ul>
  <li><strong>connector</strong> — the graphical projection of the public interface when the Frog is reused as a node,</li>
  <li><strong>icon</strong> — the graphical icon associated with the Frog,</li>
  <li><strong>ide</strong> — IDE-facing editing preferences serialized with the Frog itself,</li>
  <li><strong>cache</strong> — optional non-authoritative derived data used to accelerate tooling workflows.</li>
</ul>

<p>
A <code>.frog</code> file is a transparent source representation.
It MUST NOT require hidden compiled payloads in order to define program meaning.
</p>

<hr/>

<h2 id="representation-levels">5. Representation levels</h2>

<p>
FROG distinguishes three conceptual representation levels:
</p>

<ul>
  <li><strong>FROG Expression</strong> — the serialized source representation stored in a <code>.frog</code> file,</li>
  <li><strong>FROG Program Model</strong> — the canonical editable in-memory representation reconstructed by tools,</li>
  <li><strong>FROG Execution IR</strong> — the execution-oriented representation derived from the validated program model.</li>
</ul>

<p>
This directory primarily specifies the <strong>FROG Expression</strong>.
</p>

<p>
Tooling MAY reconstruct a Program Model from the Expression and MAY derive an Execution IR from the validated Program Model.
However, the canonical editable source of a FROG remains the <code>.frog</code> file itself.
</p>

<hr/>

<h2 id="file-tree">6. FROG file tree</h2>

<pre>
FROG
│
├─ Canonical source
│   └─ example.frog
│
├─ Optional cache artifact
│   └─ example.frog.cache
│
└─ Optional distribution artifact
    └─ example.frogbin
</pre>

<p>
The <code>.frog</code> file is the canonical source representation.
Other file forms are optional tool artifacts.
</p>

<hr/>

<h2 id="file-types">7. File types</h2>

<h3>7.1 <code>.frog</code> — canonical source</h3>

<ul>
  <li>Human-readable JSON</li>
  <li>Version-control friendly</li>
  <li>Contains all required source sections</li>
  <li>May contain optional source sections</li>
  <li>Represents the canonical <strong>FROG Expression</strong></li>
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
See: <a href="./Cache.md"><strong>Cache.md</strong></a>
</p>

<h3>7.3 <code>.frogbin</code> — optional distribution artifact</h3>

<ul>
  <li>Intended for distribution or deployment workflows</li>
  <li>May omit non-essential source detail</li>
  <li>May contain execution-oriented or compiled payloads</li>
  <li>Is not the canonical editable source representation</li>
</ul>

<hr/>

<h2 id="top-level-structure">8. Top-level JSON structure</h2>

<p>
The canonical top-level source structure of a FROG program is:
</p>

<pre>
{
  "spec_version": "0.1",

  "metadata": {},
  "interface": {},
  "connector": {},

  "diagram": {},
  "front_panel": {},

  "icon": {},
  "ide": {},

  "cache": {}
}
</pre>

<p>
This top-level object contains both required and optional sections.
Only the required sections define the minimal canonical source program.
Optional sections MUST NOT redefine program semantics.
</p>

<p>
FROG v0.1 does <strong>not</strong> define:
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
  <li>widget instances are embedded inside <code>front_panel</code>,</li>
  <li>widget interactions are expressed inside <code>diagram</code>.</li>
</ul>

<hr/>

<h2 id="section-presence-rules">9. Section presence rules</h2>

<p>
A canonical <code>.frog</code> source file MUST contain:
</p>

<ul>
  <li><code>spec_version</code></li>
  <li><code>metadata</code></li>
  <li><code>interface</code></li>
  <li><code>diagram</code></li>
  <li><code>front_panel</code></li>
</ul>

<p>
A canonical <code>.frog</code> source file MAY additionally contain:
</p>

<ul>
  <li><code>connector</code></li>
  <li><code>icon</code></li>
  <li><code>ide</code></li>
  <li><code>cache</code></li>
</ul>

<p>
The <code>front_panel</code> section is required even for programs that may execute in a headless context.
A runtime MAY ignore the interaction layer at execution time when appropriate, but the section remains part of the canonical source description.
</p>

<p>
The <code>connector</code> section is optional.
It SHOULD be present when the Frog is intended to be reused as a graphical node inside another diagram.
</p>

<p>
Optional sections MUST NOT modify the authoritative execution semantics established by the validated source-derived program representation.
</p>

<hr/>

<h2 id="sections-overview">10. Sections overview</h2>

<h3>10.1 Metadata</h3>

<p>
Required section defining identity, documentation, authorship, and related descriptive information.
</p>

<p>
Detailed specification: <a href="./Metadata.md"><strong>Metadata.md</strong></a>
</p>

<h3>10.2 Interface</h3>

<p>
Required section defining the public typed inputs and outputs of the Frog.
All declared types MUST use canonical FROG type expressions.
</p>

<p>
Detailed specifications:
<a href="./Interface.md"><strong>Interface.md</strong></a>,
<a href="./Type.md"><strong>Type.md</strong></a>
</p>

<h3>10.3 Connector</h3>

<p>
Optional section defining the graphical mapping of interface ports when the Frog is reused as a node.
The connector never defines new logical ports.
</p>

<p>
Detailed specification: <a href="./Connector.md"><strong>Connector.md</strong></a>
</p>

<h3>10.4 Diagram</h3>

<p>
Required section defining the executable dataflow graph of the Frog.
The diagram contains nodes, edges, dependencies, and annotations.
It is the authoritative source-level execution structure of the program.
</p>

<p>
Detailed specifications:
<a href="./Diagram.md"><strong>Diagram.md</strong></a>,
<a href="./Type.md"><strong>Type.md</strong></a>,
<a href="./Widget%20interaction.md"><strong>Widget interaction.md</strong></a>
</p>

<h3>10.5 Front panel</h3>

<p>
Required section defining the user interaction layer of the Frog through widget instances, layout, style, and related UI composition data.
</p>

<p>
Detailed specifications:
<a href="./Front%20panel.md"><strong>Front panel.md</strong></a>,
<a href="./Widget.md"><strong>Widget.md</strong></a>
</p>

<h3>10.6 Icon</h3>

<p>
Optional section containing the icon used by tools when the Frog is represented as a reusable node.
</p>

<p>
Detailed specification: <a href="./Icon.md"><strong>Icon.md</strong></a>
</p>

<h3>10.7 IDE preferences</h3>

<p>
Optional section containing IDE-facing preferences serialized with the Frog itself.
This section belongs to the FROG Expression because a Frog behaves as a durable editable program unit and may embed source-level IDE interpretation preferences.
</p>

<p>
Runtimes MUST ignore this section for execution semantics.
</p>

<p>
Detailed specification: <a href="./IDE%20preferences.md"><strong>IDE preferences.md</strong></a>
</p>

<h3>10.8 Cache</h3>

<p>
Optional section containing derived, non-authoritative tooling data used to accelerate workflows.
</p>

<p>
Detailed specification: <a href="./Cache.md"><strong>Cache.md</strong></a>
</p>

<hr/>

<h2 id="cross-cutting-subsystems">11. Cross-cutting subsystems</h2>

<h3>11.1 Type system</h3>

<p>
FROG v0.1 defines a normative built-in type system described in <a href="./Type.md"><strong>Type.md</strong></a>.
</p>

<p>
This subsystem applies wherever values are declared, connected, constrained, validated, or coerced, including:
</p>

<ul>
  <li>interface ports,</li>
  <li>diagram ports and wire validation,</li>
  <li>constants and typed fields,</li>
  <li>widget value types,</li>
  <li>widget interaction node ports.</li>
</ul>

<p>
The type system is cross-cutting.
It is not represented as a dedicated required top-level section.
</p>

<h3>11.2 Widget model</h3>

<p>
FROG v0.1 defines a normative widget object model described in <a href="./Widget.md"><strong>Widget.md</strong></a>.
</p>

<p>
A widget is not merely a drawing.
It is a structured UI object with identity, class, role, optional typed value, properties, methods, and optional attached parts.
</p>

<p>
The widget model is cross-cutting.
It governs widget instances contained inside <code>front_panel</code>.
</p>

<h3>11.3 Widget interaction model</h3>

<p>
FROG v0.1 defines a normative widget interaction model described in <a href="./Widget%20interaction.md"><strong>Widget interaction.md</strong></a>.
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

<hr/>

<h2 id="interface-connector-front-panel">12. Interface, connector, and front panel</h2>

<p>
FROG explicitly distinguishes three concepts that may appear related but serve different purposes:
</p>

<ul>
  <li><strong>interface</strong> — the public logical contract of the Frog,</li>
  <li><strong>connector</strong> — the graphical projection of that public contract when reused as a node,</li>
  <li><strong>front_panel</strong> — the user interaction layer of the Frog.</li>
</ul>

<p>
The <strong>interface</strong> defines what the Frog exposes to the outside world.
</p>

<p>
The <strong>connector</strong> does not introduce new logical ports.
It only defines how existing interface ports appear on the perimeter of the reusable graphical node.
</p>

<p>
The <strong>front_panel</strong> does not define the public program contract.
It defines how users see and interact with the program through widgets and UI composition.
</p>

<p>
Therefore:
</p>

<ul>
  <li>a Frog MAY have an interface without a connector,</li>
  <li>a Frog MAY be executable without a connector,</li>
  <li>a Frog MUST NOT define a connector without an interface,</li>
  <li>the front panel MUST NOT be interpreted as the public logical API of the Frog.</li>
</ul>

<hr/>

<h2 id="execution-and-validation">13. Execution and validation</h2>

<p>
Execution follows a dataflow model.
</p>

<ul>
  <li>A node becomes executable when all required inputs are available.</li>
  <li>Execution order derives from dependency structure rather than source ordering.</li>
  <li>Independent nodes MAY execute in parallel.</li>
</ul>

<p>
A <code>.frog</code> source file MUST be validated before execution.
Execution MUST proceed from a validated source-derived representation rather than directly from raw unvalidated source text.
</p>

<p>
In a typical architecture:
</p>

<ul>
  <li>the FROG Expression is parsed,</li>
  <li>a Program Model is reconstructed,</li>
  <li>that model is validated,</li>
  <li>an Execution IR may then be derived for compilation or execution.</li>
</ul>

<p>
Optional sections such as <code>connector</code>, <code>icon</code>, <code>ide</code>, and <code>cache</code> MUST NOT directly redefine execution semantics.
</p>

<p>
Validation MUST ensure at least that:
</p>

<ul>
  <li>all required top-level sections are present,</li>
  <li>all type expressions are valid according to <a href="./Type.md"><strong>Type.md</strong></a>,</li>
  <li>all diagram references are valid,</li>
  <li>all connected ports are type-compatible,</li>
  <li>all widget instances are valid according to <a href="./Widget.md"><strong>Widget.md</strong></a>,</li>
  <li>all widget interaction nodes are valid according to <a href="./Widget%20interaction.md"><strong>Widget interaction.md</strong></a>,</li>
  <li>all connector entries reference existing interface ports.</li>
</ul>

<hr/>

<h2 id="canonical-formatting">14. Canonical formatting and ordering</h2>

<p>
JSON key ordering MUST NOT affect semantics.
</p>

<p>
The recommended canonical top-level ordering is:
</p>

<pre>
spec_version
metadata
interface
connector
diagram
front_panel
icon
ide
cache
</pre>

<p>
Canonical source values SHOULD use the normalized forms defined by their respective specifications, including:
</p>

<ul>
  <li>canonical type expressions from <a href="./Type.md"><strong>Type.md</strong></a>,</li>
  <li>canonical widget instance conventions from <a href="./Widget.md"><strong>Widget.md</strong></a>,</li>
  <li>canonical widget interaction forms from <a href="./Widget%20interaction.md"><strong>Widget interaction.md</strong></a>.</li>
</ul>

<hr/>

<h2 id="normative-terminology">15. Normative terminology</h2>

<ul>
  <li><strong>MUST</strong> — required</li>
  <li><strong>SHOULD</strong> — recommended</li>
  <li><strong>MAY</strong> — optional</li>
  <li><strong>MUST NOT</strong> — prohibited</li>
</ul>

<hr/>

<h2 id="status">16. Status</h2>

<p>
FROG Expression Specification v0.1 — Draft.
</p>

<hr/>

<h2 id="license">17. License</h2>

<p>
This specification is released under the Apache License 2.0.
</p>

<hr/>

<p align="center">
  <strong>FROG — Free Open Graphical Language</strong><br/>
  Canonical source expression for open graphical programming.
</p>
