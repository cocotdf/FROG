<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
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
  <li><a href="#why-expression-exists">2. Why Expression Exists</a></li>
  <li><a href="#scope-of-this-directory">3. Scope of this Directory</a></li>
  <li><a href="#specification-documents">4. Specification Documents</a></li>
  <li><a href="#what-a-frog-file-describes">5. What a <code>.frog</code> File Describes</a></li>
  <li><a href="#representation-levels">6. Representation Levels</a></li>
  <li><a href="#file-tree-and-artifact-families">7. File Tree and Artifact Families</a></li>
  <li><a href="#file-types">8. File Types</a></li>
  <li><a href="#top-level-json-structure">9. Top-Level JSON Structure</a></li>
  <li><a href="#section-presence-rules">10. Section Presence Rules</a></li>
  <li><a href="#sections-overview">11. Sections Overview</a></li>
  <li><a href="#cross-cutting-subsystems">12. Cross-Cutting Subsystems</a></li>
  <li><a href="#interface-connector-diagram-and-front-panel">13. Interface, Connector, Diagram, and Front Panel</a></li>
  <li><a href="#source-well-formedness-and-structural-validity">14. Source Well-Formedness and Structural Validity</a></li>
  <li><a href="#execution-relevance-validation-and-derivation-boundary">15. Execution Relevance, Validation, and Derivation Boundary</a></li>
  <li><a href="#canonical-formatting-and-ordering">16. Canonical Formatting and Ordering</a></li>
  <li><a href="#normative-terminology">17. Normative Terminology</a></li>
  <li><a href="#status">18. Status</a></li>
  <li><a href="#license">19. License</a></li>
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
It is the authoritative, editable, transparent, and version-control-friendly description of a FROG program at the source level.
</p>

<p>
The purpose of this directory is to define:
</p>

<ul>
  <li>the canonical top-level structure of a <code>.frog</code> file,</li>
  <li>the required and optional source sections of that file,</li>
  <li>the source-level representation of those sections,</li>
  <li>the source-visible families and cross-cutting source subsystems that appear in canonical source, including the type system, the widget model, the widget interaction model, and the source-facing representation of structures and local-memory constructs,</li>
  <li>the structural validity boundary that a canonical <code>.frog</code> source file MUST satisfy before later semantic validation and execution-facing derivation,</li>
  <li>the source-schema posture under which parts of canonical source shape may be made machine-checkable without collapsing source structure into semantic validation or implementation-specific behavior.</li>
</ul>

<p>
This directory is about the authoritative source form of a FROG.
It is not the complete runtime architecture, not the complete IDE implementation model, not the complete semantic interpretation of validated programs, and not the open execution-facing IR layer.
</p>

<p>
Cross-cutting execution semantics are related to this source specification but are not owned here when they belong to validated program meaning.
Likewise, optional capability families may appear in executable diagrams, but their normative ownership remains outside <code>Expression/</code> when they belong to profile specifications rather than to the source format itself.
</p>

<pre>
Repository architecture around Expression

Expression/   -> canonical source form
Language/     -> validated program meaning
IR/           -> open execution-facing representation
Libraries/    -> intrinsic primitive vocabularies
Profiles/     -> optional standardized capability families
IDE/          -> authoring, observability, debugging, inspection

Expression/ owns source structure and source-visible object shape.
Expression/ owns source well-formedness and structural validity.
Expression/ owns source-schema posture for canonical source.
Expression/ does not own validated program meaning.
Expression/ does not own open execution-facing derivation.
</pre>

<hr/>

<h2 id="why-expression-exists">2. Why Expression Exists</h2>

<p>
A graphical language still needs a durable, explicit, tool-independent source form.
That is the role of the FROG Expression.
</p>

<p>
The Expression layer exists so that a FROG program can be:
</p>

<ul>
  <li>saved as canonical source,</li>
  <li>read and diffed by humans,</li>
  <li>versioned in source control,</li>
  <li>loaded by different tools,</li>
  <li>checked for source well-formedness and structural validity independently of one IDE implementation,</li>
  <li>checked, where appropriate, against repository-visible machine-checkable source-schema artifacts that remain subordinate to published specification ownership,</li>
  <li>used as the stable source basis for later semantic validation and execution-facing derivation.</li>
</ul>

<p>
Without a dedicated source layer, important distinctions would collapse too easily:
</p>

<ul>
  <li>editor behavior could be confused with language structure,</li>
  <li>runtime behavior could be confused with source representation,</li>
  <li>implementation details could leak into the canonical program artifact,</li>
  <li>semantic rejection could be confused with malformed or structurally invalid source.</li>
</ul>

<p>
The Expression layer prevents that drift by giving the language a stable source-level contract.
</p>

<pre>
Why Expression matters

IDE view
   is not
canonical source

Runtime form
   is not
canonical source

Compiler IR
   is not
canonical source

.frog
   is
canonical source
</pre>

<hr/>

<h2 id="scope-of-this-directory">3. Scope of this Directory</h2>

<p>
This directory specifies the source expression of a FROG program.
It defines what is serialized in the canonical <code>.frog</code> file and how that source MUST be interpreted structurally as source.
</p>

<p>
This specification does not attempt to fully define:
</p>

<ul>
  <li>the complete runtime architecture,</li>
  <li>the complete in-memory editable Program Model used by IDE implementations,</li>
  <li>the complete open execution-facing IR used by toolchains,</li>
  <li>the complete cross-cutting execution semantics of the language,</li>
  <li>the complete intrinsic primitive vocabulary of FROG,</li>
  <li>the complete optional profile surface of FROG,</li>
  <li>the complete standard widget catalog of every possible IDE or UI system.</li>
</ul>

<p>
Those concerns are specified elsewhere in the repository.
This directory focuses on the authoritative source form.
</p>

<p>
Accordingly, this directory defines how a FROG is <strong>serialized</strong>, not every detail of how it is edited, semantically validated by a given tool, derived into IR, lowered, compiled, executed, or deployed.
</p>

<pre>
Expression/ answers:

- What is in a .frog file?
- Which sections exist?
- Which sections are required?
- How are source objects serialized?
- Which source-level cross-cutting models apply?
- What makes source structurally valid as canonical source?
- What belongs to source-schema posture and machine-checkable source shape?

Expression/ does not answer by itself:

- validated program meaning
- open execution-facing IR structure
- full runtime architecture
- full compiler architecture
- full IDE authoring architecture
</pre>

<hr/>

<h2 id="specification-documents">4. Specification Documents</h2>

<p>
The FROG Expression is defined through the following documents in this directory:
</p>

<pre><code>Expression/
├── Readme.md
│   -> architectural entry point for the canonical source specification
├── Schema.md
│   -> source-schema posture and machine-checkable structural validation boundary
├── schema/
│   └── frog.schema.json
│       -> conservative machine-checkable top-level canonical source schema
├── Metadata.md
│   -> descriptive program metadata and non-executable identification fields
├── Type.md
│   -> canonical type-expression model used across the source format
├── Interface.md
│   -> public typed inputs and outputs of a FROG
├── Connector.md
│   -> graphical perimeter mapping of interface ports when the FROG is reused as a node
├── Diagram.md
│   -> authoritative executable graph as canonical source representation
├── Front panel.md
│   -> optional front-panel composition and user-facing interaction surface
├── Widget.md
│   -> widget object model, widget classes, roles, properties, methods, events, and parts
├── Widget interaction.md
│   -> diagram-side widget interaction paths and execution-facing widget access model
├── Control structures.md
│   -> source-facing representation of canonical control structures
├── State and cycles.md
│   -> source-facing representation of explicit local memory and feedback-cycle formation rules
├── Icon.md
│   -> reusable-node icon representation
├── IDE preferences.md
│   -> optional IDE-facing source metadata and recoverability-oriented authoring preferences
└── Cache.md
    -> optional non-authoritative cache content for tooling convenience
</code></pre>

<p>
The documents in this directory play three different roles:
</p>

<ul>
  <li><strong>top-level source-section specifications</strong>,</li>
  <li><strong>cross-cutting source subsystems</strong>,</li>
  <li><strong>source-schema posture and machine-checkable structural support artifacts</strong>.</li>
</ul>

<h3>4.1 Top-level source-section specifications</h3>

<p>
Some documents define dedicated top-level source sections such as:
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

<h3>4.2 Cross-cutting source subsystems</h3>

<p>
Other documents define cross-cutting source subsystems used throughout the source format.
In particular:
</p>

<ul>
  <li><code>Type.md</code> defines canonical value-type expressions and source-level type rules used throughout the source format.</li>
  <li><code>Widget.md</code> defines the widget object model, including classes, roles, value behavior, parts, properties, methods, and events.</li>
  <li><code>Widget interaction.md</code> defines how executable diagrams may interact with widgets through standardized diagram-level interaction mechanisms.</li>
  <li><code>Control structures.md</code> defines the source-facing representation of language structures such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>.</li>
  <li><code>State and cycles.md</code> defines the source-facing representation of explicit local memory and feedback-cycle formation constraints.</li>
</ul>

<h3>4.3 Source-schema posture and machine-checkable support</h3>

<p>
This directory also publishes a source-schema posture for canonical source.
That posture is defined normatively by <code>Schema.md</code>.
</p>

<p>
Repository-visible machine-checkable artifacts MAY assist structural validation where appropriate.
At the current repository stage, the conservative machine-checkable top-level source-shape artifact is:
</p>

<ul>
  <li><code>schema/frog.schema.json</code> — a conservative machine-checkable schema for top-level canonical source shape and section-kind constraints.</li>
</ul>

<p>
These artifacts assist structural validation.
They do not replace specification ownership.
If a machine-checkable artifact and the published specification disagree, the published specification remains authoritative until the repository is corrected coherently.
</p>

<h3>4.4 Normative external dependencies</h3>

<p>
The current source specification also depends on normative specifications defined outside this directory.
At the current repository stage, that includes:
</p>

<ul>
  <li><code>Language/Expression to validated meaning.md</code> — the boundary from source expression to validated program meaning,</li>
  <li><code>Language/Control structures.md</code> — normative execution semantics for standard control structures,</li>
  <li><code>Language/State and cycles.md</code> — normative execution semantics for local memory and valid feedback cycles,</li>
  <li><code>Language/Execution model.md</code> — language-level execution concepts used to interpret validated program meaning,</li>
  <li><code>Libraries/Core.md</code> — foundational intrinsic primitive definitions such as <code>frog.core.add</code>, <code>frog.core.mul</code>, and <code>frog.core.delay</code>,</li>
  <li><code>Libraries/Math.md</code> — intrinsic numeric scalar primitives beyond the minimal core,</li>
  <li><code>Libraries/Collections.md</code> — intrinsic array-oriented collection primitives,</li>
  <li><code>Libraries/Text.md</code> — intrinsic text-processing primitives,</li>
  <li><code>Libraries/IO.md</code> — intrinsic file, path, byte, and related I/O primitives,</li>
  <li><code>Libraries/Signal.md</code> — intrinsic first-wave signal-processing primitives,</li>
  <li><code>Libraries/UI.md</code> — intrinsic standardized executable widget-interaction primitives,</li>
  <li><code>Profiles/Interop.md</code> — optional standardized interoperability primitives owned by the Interop profile.</li>
</ul>

<p>
Accordingly, <code>Expression/</code> is the canonical home of the source-format specification and source-schema posture, while <code>Language/</code>, <code>Libraries/</code>, and <code>Profiles/</code> are normative external dependencies for the meaning of validated executable diagrams.
</p>

<pre>
Source ownership vs external meaning

Expression/
   ├─ defines how source is written
   ├─ defines what sections exist
   ├─ defines how diagrams, widgets, and sections are serialized
   ├─ defines source well-formedness and structural validity
   ├─ defines source-schema posture
   │
   ├─ relies on Language/ for validated program meaning
   ├─ relies on Libraries/ for intrinsic primitive meaning
   └─ relies on Profiles/ for optional profile-owned capability meaning
</pre>

<pre>
A useful reading rule

If the question is:
- "How is it written in source?"                 -> Expression/
- "Is this canonical source structurally valid?" -> Expression/
- "What belongs to source-schema posture?"       -> Expression/
- "What does the validated program mean?"        -> Language/
- "What does this intrinsic primitive do?"       -> Libraries/
- "What does this optional capability do?"       -> Profiles/
- "How does the IDE present it?"                 -> IDE/
</pre>

<hr/>

<h2 id="what-a-frog-file-describes">5. What a <code>.frog</code> File Describes</h2>

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
A FROG MAY therefore be diagram-only with respect to user-facing interaction.
A conforming canonical source file does not require a front panel unless such a layer is intentionally part of the program description.
</p>

<p>
A <code>.frog</code> file is a transparent source representation.
It MUST NOT require hidden compiled payloads in order to define the program as canonical source.
</p>

<pre>
Minimal canonical FROG

example.frog
├─ spec_version
├─ metadata
├─ interface
└─ diagram
</pre>

<pre>
Extended canonical FROG

example.frog
├─ spec_version
├─ metadata
├─ interface
├─ connector
├─ diagram
├─ front_panel
├─ icon
├─ ide
└─ cache
</pre>

<p>
The key idea is simple:
</p>

<pre>
Required sections
    -> define the minimal canonical program source

Optional sections
    -> enrich source representation
    -> MUST NOT redefine authoritative execution meaning
</pre>

<hr/>

<h2 id="representation-levels">6. Representation Levels</h2>

<p>
FROG distinguishes four related but distinct representation levels:
</p>

<ul>
  <li><strong>FROG Expression</strong> — the serialized canonical source representation stored in a <code>.frog</code> file,</li>
  <li><strong>FROG Program Model</strong> — the canonical editable in-memory representation reconstructed and maintained by tools during authoring,</li>
  <li><strong>Validated program meaning</strong> — the normative semantic state established after validation against the relevant language, library, and profile rules,</li>
  <li><strong>Open execution-facing representation</strong> — the IR-layer representation derived from validated program meaning.</li>
</ul>

<p>
This directory primarily specifies the FROG Expression.
Tooling MAY reconstruct a Program Model from the Expression and MAY derive an open execution-facing representation from validated program meaning.
However, the canonical editable source of a FROG remains the <code>.frog</code> file itself.
</p>

<pre>
Representation pipeline

.frog source
   |
   v
FROG Expression
   |
   v
Program Model
   |
   v
validated program meaning
   |
   v
open execution-facing representation
</pre>

<p>
These levels are related but not identical:
</p>

<ul>
  <li>the Expression is the durable source artifact,</li>
  <li>the Program Model is the editable in-memory tool model,</li>
  <li>validated program meaning is the semantic truth layer,</li>
  <li>the open execution-facing representation is the derived execution layer.</li>
</ul>

<pre>
Think of the four levels like this

Expression     -> what is saved
Program Model  -> what is edited
Language       -> what is true
IR             -> what is derived
</pre>

<hr/>

<h2 id="file-tree-and-artifact-families">7. File Tree and Artifact Families</h2>

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

<p>
Only the canonical <code>.frog</code> source is the authoritative editable source artifact.
Cache and distribution artifacts MAY exist, but they do not replace canonical source ownership.
</p>

<pre>
Authority rule

example.frog        -> authoritative editable source
example.frog.cache  -> non-authoritative cache artifact
example.frogbin     -> non-authoritative distribution artifact
</pre>

<hr/>

<h2 id="file-types">8. File Types</h2>

<h3>8.1 <code>.frog</code> — canonical source</h3>

<ul>
  <li>Human-readable JSON</li>
  <li>Version-control friendly</li>
  <li>Contains all required source sections</li>
  <li>May contain optional source sections</li>
  <li>Represents the canonical FROG Expression</li>
</ul>

<h3>8.2 <code>.frog.cache</code> — optional cache artifact</h3>

<ul>
  <li>Generated by tools</li>
  <li>May contain cached analysis or derived execution-facing data</li>
  <li>Used to accelerate loading, validation, or compilation workflows</li>
  <li>Safe to delete and regenerate</li>
  <li>Non-authoritative with respect to program meaning</li>
</ul>

<p>
See: <code>Cache.md</code>
</p>

<h3>8.3 <code>.frogbin</code> — optional distribution artifact</h3>

<ul>
  <li>Intended for distribution or deployment workflows</li>
  <li>May omit non-essential source detail</li>
  <li>May contain derived execution-facing or compiled payloads</li>
  <li>Is not the canonical editable source representation</li>
</ul>

<hr/>

<h2 id="top-level-json-structure">9. Top-Level JSON Structure</h2>

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

<pre>
Top-level simplicity rule

No dedicated top-level:
- types
- widgets
- widget_interactions

These concerns are embedded where they naturally belong.
</pre>

<p>
For machine-checkable support of this top-level canonical source shape, see:
</p>

<ul>
  <li><code>Schema.md</code></li>
  <li><code>schema/frog.schema.json</code></li>
</ul>

<hr/>

<h2 id="section-presence-rules">10. Section Presence Rules</h2>

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
When absent, the FROG is interpreted as a program with no serialized front-panel composition.
</p>

<p>
The <code>connector</code> section is optional.
It SHOULD be present when the FROG is intended to be reused as a graphical node inside another diagram.
</p>

<p>
Optional sections MUST NOT modify the authoritative execution semantics established by validated program meaning.
</p>

<pre>
Presence summary

MUST:
- spec_version
- metadata
- interface
- diagram

MAY:
- connector
- front_panel
- icon
- ide
- cache
</pre>

<hr/>

<h2 id="sections-overview">11. Sections Overview</h2>

<h3>11.1 Metadata</h3>

<p>
Required section defining identity, documentation, authorship, and related descriptive information.
</p>

<p>
Detailed specification: <code>Metadata.md</code>
</p>

<h3>11.2 Interface</h3>

<p>
Required section defining the public typed inputs and outputs of the FROG.
All declared types MUST use canonical FROG type expressions.
</p>

<p>
Detailed specifications: <code>Interface.md</code>, <code>Type.md</code>
</p>

<h3>11.3 Connector</h3>

<p>
Optional section defining the graphical mapping of interface ports when the FROG is reused as a node.
The connector never defines new logical ports.
</p>

<p>
Detailed specification: <code>Connector.md</code>
</p>

<h3>11.4 Diagram</h3>

<p>
Required section defining the executable dataflow graph of the FROG.
The diagram contains nodes, edges, dependencies, regions, boundaries, and annotations as source-level constructs.
It is the authoritative source-level execution structure of the program.
</p>

<p>
Detailed specifications:
<code>Diagram.md</code>,
<code>Type.md</code>,
<code>Widget interaction.md</code>,
the source-facing companion documents <code>Control structures.md</code> and <code>State and cycles.md</code>,
the normative semantic documents in <code>Language/</code>,
the relevant intrinsic primitive-library specifications in <code>Libraries/</code>,
and any relevant optional standardized capability specifications in <code>Profiles/</code>.
</p>

<h3>11.5 Front Panel</h3>

<p>
Optional section defining the user interaction layer of the FROG through widget instances, layout, style, and related UI composition data.
</p>

<p>
When absent, the canonical source defines no serialized front-panel composition for that FROG.
</p>

<p>
Detailed specifications: <code>Front panel.md</code>, <code>Widget.md</code>
</p>

<h3>11.6 Icon</h3>

<p>
Optional section containing the icon used by tools when the FROG is represented as a reusable node.
</p>

<p>
Detailed specification: <code>Icon.md</code>
</p>

<h3>11.7 IDE Preferences</h3>

<p>
Optional section containing IDE-facing preferences and recoverability metadata serialized with the FROG itself.
This section belongs to the FROG Expression because a FROG behaves as a durable editable program unit and may embed source-level IDE preferences together with non-authoritative authoring recoverability aids.
</p>

<p>
Runtimes and other execution-facing systems MUST ignore this section for execution semantics.
</p>

<p>
Detailed specification: <code>IDE preferences.md</code>
</p>

<h3>11.8 Cache</h3>

<p>
Optional section containing derived, non-authoritative tooling data used to accelerate workflows.
</p>

<p>
Detailed specification: <code>Cache.md</code>
</p>

<pre>
Section role summary

metadata    -> descriptive identity
interface   -> public typed boundary
connector   -> graphical node-side projection of interface
diagram     -> authoritative executable graph
front_panel -> optional user interaction surface
icon        -> reusable-node icon
ide         -> non-authoritative IDE-facing metadata
cache       -> non-authoritative tooling cache
</pre>

<hr/>

<h2 id="cross-cutting-subsystems">12. Cross-Cutting Subsystems</h2>

<h3>12.1 Type System</h3>

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

<h3>12.2 Widget Model</h3>

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

<h3>12.3 Widget Interaction Model</h3>

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
Future intrinsic UI primitive specifications and future profile-based capability expansions MUST remain consistent with that source-level interaction model.
</p>

<h3>12.4 Control-Structure and Local-Memory Source Dependencies</h3>

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
This separation allows <code>Expression/</code> to remain the canonical source-specification layer while <code>Language/</code> remains the normative semantic layer.
Intrinsic primitive catalogs consumed by executable diagrams remain defined in <code>Libraries/</code>, while optional standardized capability families remain defined in <code>Profiles/</code>.
</p>

<pre>
Cross-cutting ownership

Serialized shape of structures/cycles  -> Expression/
Execution meaning of structures/cycles -> Language/
Intrinsic primitive meaning            -> Libraries/
Optional capability meaning            -> Profiles/
</pre>

<pre>
Cross-cutting rule of thumb

If it must appear in source, Expression/ cares.
If it defines validated program meaning, Language/ cares.
If it defines a primitive contract, Libraries/ or Profiles/ care.
</pre>

<hr/>

<h2 id="interface-connector-diagram-and-front-panel">13. Interface, Connector, Diagram, and Front Panel</h2>

<p>
FROG explicitly distinguishes four concepts that may appear related but serve different purposes:
</p>

<ul>
  <li><code>interface</code> — the public logical contract of the FROG,</li>
  <li><code>connector</code> — the graphical projection of that public contract when the FROG is reused as a node,</li>
  <li><code>diagram</code> — the authoritative executable graph of the FROG,</li>
  <li><code>front_panel</code> — the optional user-facing interaction layer of the FROG itself.</li>
</ul>

<pre>
Public contract vs graphical projections vs execution

interface
   |
   +--> connector     (node-facing graphical projection)
   |
   +--> diagram       (authoritative executable use of interface boundaries)

front_panel
   |
   +--> widgets       (user-facing interaction surface)
   |
   +--> diagram       (all executable linkage MUST pass through the diagram)
</pre>

<h3>13.1 Interface</h3>

<p>
The interface defines public inputs and outputs.
It is part of the program contract and is used for reuse, validation, and boundary semantics.
</p>

<h3>13.2 Connector</h3>

<p>
The connector defines where those public ports appear on the perimeter of the reusable node representation.
It is graphical mapping, not logical contract.
</p>

<h3>13.3 Diagram</h3>

<p>
The diagram defines the executable graph.
It is the authoritative source-level execution structure of the program.
</p>

<p>
Execution-relevant source families are expressed here in source form, including ordinary primitives, sub-FROG invocation nodes, structure nodes, interface boundary nodes, widget participation nodes, explicit edges, regions, structure terminals, and explicit local-memory participation where applicable.
</p>

<h3>13.4 Front Panel</h3>

<p>
When present, the front panel defines widgets, layout, and visual interaction for the FROG itself.
It does not define the public API and it does not replace the executable graph.
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

<pre>
Do not collapse these into one concept

interface   != front_panel
connector   != interface
diagram     != front_panel
diagram     is the executable authority
</pre>

<pre>
Widget participation model

front_panel widget declaration
             |
             +--> widget_value
             |      -> natural value participation through the diagram
             |
             +--> widget_reference
                    -> explicit object-style UI interaction through frog.ui.*
</pre>

<hr/>

<h2 id="source-well-formedness-and-structural-validity">14. Source Well-Formedness and Structural Validity</h2>

<p>
The canonical <code>.frog</code> source layer MUST remain distinct from later semantic validation.
Accordingly, this specification distinguishes three different questions:
</p>

<ul>
  <li><strong>Is the file parseable as source?</strong></li>
  <li><strong>Is the parsed source structurally valid as a canonical FROG Expression?</strong></li>
  <li><strong>Does the structurally valid source yield accepted validated program meaning?</strong></li>
</ul>

<p>
These questions MUST NOT be collapsed into one undifferentiated notion of “validity”.
</p>

<h3>14.1 Parseability</h3>

<p>
A candidate <code>.frog</code> file is parseable when it is syntactically readable as JSON and can be loaded as a top-level source object.
Parseability alone does not make the file a conforming canonical FROG Expression.
</p>

<h3>14.2 Structural validity</h3>

<p>
A parsed source object is <strong>structurally valid</strong> when it satisfies the canonical source-shape rules owned by <code>Expression/</code>.
That includes, as applicable:
</p>

<ul>
  <li>required top-level section presence,</li>
  <li>top-level object-shape expectations,</li>
  <li>section-local structural rules,</li>
  <li>identifier-shape and uniqueness rules owned by source documents,</li>
  <li>source-level containment and placement rules,</li>
  <li>source-level structural consistency of optional sections when they are present.</li>
</ul>

<p>
Structural validity is still a source-level notion.
It does not by itself imply accepted executable semantics.
</p>

<p>
Structural validity may be assisted by repository-visible machine-checkable schema artifacts where appropriate.
However, schema-assisted structural acceptance MUST remain distinct from later semantic acceptance.
Likewise, not every structural rule is required to live inside one declarative machine artifact merely because it belongs to source structure.
</p>

<h3>14.3 Source-schema posture</h3>

<p>
The source-schema posture of canonical FROG source is owned by <code>Expression/Schema.md</code>.
</p>

<p>
That posture exists so that machine-checkable structural validation can become repository-visible without collapsing:
</p>

<ul>
  <li>canonical source structure into semantic validation,</li>
  <li>published specification ownership into validator implementation folklore,</li>
  <li>source shape into IR design,</li>
  <li>source validity into runtime behavior.</li>
</ul>

<p>
At the current repository stage, a conservative machine-checkable support artifact exists for top-level canonical source shape and section-kind constraints.
That artifact assists the structural validation corridor.
It does not replace the published source specification.
</p>

<h3>14.4 Semantic acceptance</h3>

<p>
A structurally valid source file may still be rejected later during validation against:
</p>

<ul>
  <li><code>Language/</code> semantic rules,</li>
  <li>intrinsic primitive contracts in <code>Libraries/</code>,</li>
  <li>optional capability contracts in <code>Profiles/</code>.</li>
</ul>

<p>
Examples include type incompatibility, invalid cycle formation, invalid local-memory usage, unsupported primitive use, invalid structure semantics, or profile-related semantic rejection.
Those are not structural-source failures merely because they are detected after parsing.
</p>

<h3>14.5 Ownership rule</h3>

<pre>
Source validity ownership

Parseable JSON                       -> load/parsing concern
Structurally valid canonical source  -> Expression/
Accepted validated meaning           -> Language/ + Libraries/ + Profiles/
Derived execution-facing form        -> IR/
</pre>

<h3>14.6 Conformance relevance</h3>

<p>
This distinction matters to public conformance.
A public conformance surface SHOULD be able to distinguish at least:
</p>

<ul>
  <li>malformed or non-loadable source,</li>
  <li>parsed but structurally invalid canonical source,</li>
  <li>structurally valid source later rejected semantically,</li>
  <li>accepted source whose relevant truth is preserved across derivation and execution-facing handling.</li>
</ul>

<h3>14.7 Structural-source examples</h3>

<p>
Typical structural-source failures may include:
</p>

<ul>
  <li>missing required top-level sections,</li>
  <li>duplicate identifiers where source uniqueness is required,</li>
  <li>an optional section present with the wrong object shape,</li>
  <li>a widget tree violating explicit containment rules,</li>
  <li>a connector object attempting to define new logical ports instead of projecting the public interface,</li>
  <li>a source object placed in the wrong top-level section family.</li>
</ul>

<p>
These are source-shape failures.
They are not to be repaired by runtime behavior, implementation convenience, or post-hoc semantic interpretation.
</p>

<hr/>

<h2 id="execution-relevance-validation-and-derivation-boundary">15. Execution Relevance, Validation, and Derivation Boundary</h2>

<p>
The canonical <code>.frog</code> source file is the authoritative source artifact of the program.
However, execution is not performed directly from unvalidated raw text.
</p>

<p>
A conforming toolchain SHOULD apply the following conceptual pipeline:
</p>

<pre><code>FROG Expression
    ↓ parse / load
Source-derived program content
    ↓ reconstruct as needed
Program Model
    ↓ structural checks owned by Expression/
Structurally valid canonical source
    ↓ validate against Language/ + Libraries/ + Profiles/
Validated program meaning
    ↓ derive
Open execution-facing representation
    ↓ lower / compile / execute</code></pre>

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
  <li>primitive reference validation against the relevant intrinsic library catalogs and any relevant supported profile specifications.</li>
</ul>

<p>
Normative execution meaning is not owned by raw source alone.
It is established from validated program meaning interpreted against the relevant language semantics and primitive specifications.
Optional sections such as <code>front_panel</code>, <code>icon</code>, <code>ide</code>, and <code>cache</code> MUST NOT redefine executable semantics.
</p>

<p>
This directory also defines the <strong>source-visible families</strong> from which validated meaning and later derivation proceed.
However, this directory does not define the open IR object model, the detailed source-to-IR mapping, or the procedural rules for building open execution-facing payloads.
Those concerns belong to <code>IR/</code>.
</p>

<pre>
Boundary rule

Expression/
   defines source-visible execution-relevant content
   defines source structural validity
   defines source-schema posture

Language/
   defines validated meaning of that content

IR/
   defines how validated meaning is represented
   in open execution-facing form
</pre>

<pre>
Execution rule

raw source
   ->
source-derived program content
   ->
structurally valid canonical source
   ->
validated program meaning
   ->
open execution-facing representation
   ->
lower / compile / execute

Never:
optional source decoration -> semantic override
schema-assisted structural acceptance -> semantic acceptance
</pre>

<hr/>

<h2 id="canonical-formatting-and-ordering">16. Canonical Formatting and Ordering</h2>

<p>
Canonical source is JSON.
For interoperability and stable diffs, tools SHOULD preserve predictable formatting and section ordering.
</p>

<h3>16.1 Top-level ordering</h3>

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

<h3>16.2 Stable identifiers</h3>

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

<h3>16.3 Canonical local expressions</h3>

<p>
Tools SHOULD preserve canonical local forms for:
</p>

<ul>
  <li>type expressions,</li>
  <li>intrinsic primitive identifiers,</li>
  <li>profile-owned primitive identifiers when used,</li>
  <li>widget class identifiers,</li>
  <li>structure identifiers,</li>
  <li>property names and method names defined by the active intrinsic or profile-owned capability surface.</li>
</ul>

<h3>16.4 Optional tool freedom</h3>

<p>
Pretty-printing details such as indentation width are not semantically significant.
However, tools SHOULD avoid needless churn in emitted source.
</p>

<pre>
Formatting goal

Not:
"every tool formats however it wants"

But:
"formatting may vary in detail, while canonical identity and stable diffs remain practical"
</pre>

<hr/>

<h2 id="normative-terminology">17. Normative Terminology</h2>

<p>
The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY in this specification are to be interpreted in their ordinary normative sense:
</p>

<ul>
  <li>MUST / MUST NOT — absolute requirement or prohibition,</li>
  <li>SHOULD / SHOULD NOT — strong recommendation that may be overridden only with good reason,</li>
  <li>MAY — permitted option.</li>
</ul>

<hr/>

<h2 id="status">18. Status</h2>

<p>
This document describes the FROG Expression for specification version <code>0.1</code>.
</p>

<p>
FROG v0.1 is intentionally conservative.
It prioritizes explicit canonical source semantics, structural validity clarity, source-schema posture, long-term durability, and tool interoperability over premature expansion of the language surface.
</p>

<p>
At the current repository stage, the intrinsic primitive layer already extends beyond the minimal core, and the repository now also distinguishes optional standardized profile-owned capability families.
Future revisions MAY continue to expand both areas while preserving the architectural role of <code>Expression/</code> as the canonical source-specification layer.
</p>

<p>
Future revisions SHOULD also preserve the core architectural distinctions already established here:
</p>

<ul>
  <li>source expression versus Program Model versus validated program meaning versus open execution-facing representation,</li>
  <li>canonical source representation versus normative execution semantics,</li>
  <li>source structural validity versus semantic acceptance,</li>
  <li>source-schema posture versus validator implementation behavior,</li>
  <li>intrinsic primitive vocabularies versus optional profile-owned capability families,</li>
  <li>public interface versus connector versus diagram versus optional front panel,</li>
  <li>natural widget value flow versus object-style widget interaction,</li>
  <li>authoritative source sections versus non-authoritative optional artifacts.</li>
</ul>

<pre>
Long-term stability goals

Keep Expression/ as:
- canonical
- explicit
- portable
- source-owned
- structurally checkable
- schema-aware
- durable

Do not let Expression/ drift into:
- IDE ownership
- runtime ownership
- full semantic ownership
- implementation-private formats
</pre>

<hr/>

<h2 id="license">19. License</h2>

<p>
This specification is part of the FROG repository and follows the repository licensing and governance rules.
</p>

<p>
See the repository root and associated licensing documents for the governing license terms of the specification text and related assets.
</p>
