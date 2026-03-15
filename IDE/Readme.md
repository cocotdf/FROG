<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG IDE Architecture</h1>

<p align="center">
Definition of the architecture and responsibilities of a FROG development environment<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope">2. Scope of this Document</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#responsibility-boundaries">4. Responsibility Boundaries</a></li>
  <li><a href="#high-level-architecture">5. High-Level Architecture</a></li>
  <li><a href="#current-documents">6. Current Documents</a></li>
  <li><a href="#main-components">7. Main Components</a></li>
  <li><a href="#ide-shell">8. IDE Shell</a></li>
  <li><a href="#diagram-editor">9. Diagram Editor</a></li>
  <li><a href="#front-panel-editor">10. Front Panel Editor</a></li>
  <li><a href="#frog-program-model">11. FROG Program Model</a></li>
  <li><a href="#relation-with-frog-expression">12. Relation with FROG Expression</a></li>
  <li><a href="#execution-integration-boundary">13. Execution Integration Boundary</a></li>
  <li><a href="#palette">14. Palette</a></li>
  <li><a href="#express-authoring">15. Express Authoring</a></li>
  <li><a href="#execution-observability">16. Execution Observability</a></li>
  <li><a href="#debugging">17. Debugging</a></li>
  <li><a href="#probes">18. Probes</a></li>
  <li><a href="#watch">19. Watch</a></li>
  <li><a href="#snippets">20. Snippets</a></li>
  <li><a href="#design-principles">21. Design Principles</a></li>
  <li><a href="#repository-direction">22. Repository Direction</a></li>
  <li><a href="#summary">23. Summary</a></li>
  <li><a href="#license">24. License</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The FROG IDE is the graphical development environment used to design, edit, validate, inspect, debug, and execute programs
written in the FROG graphical dataflow language.
</p>

<p>
A FROG IDE does not treat the saved <code>.frog</code> file as the live execution artifact. Instead, it loads and maintains
an internal <strong>FROG Program Model</strong>, which is the canonical editable in-memory representation used during authoring.
The canonical source file remains the <strong>FROG Expression</strong>, defined elsewhere in the repository.
</p>

<p>
Interactive inspection and debugging are not performed directly on raw serialized source. They are performed on a live
execution derived from validated program content, through a source-aligned observability layer that allows the IDE to
project runtime activity back onto diagram-visible and other source-meaningful objects.
</p>

<p>
A conforming IDE MAY expose authoring-facing views, shortcuts, aliases, assistant-driven insertion flows, and other
conveniences that are more ergonomic than the raw canonical source representation. However, those authoring-facing views
do not become new language constructs by themselves. The IDE remains responsible for preserving canonical source identity
and for keeping language meaning owned by the specifications that define it normatively.
</p>

<p>
This includes <strong>Express authoring</strong>: an IDE MAY provide guided, configurable, task-oriented insertion experiences
for common operations, but those experiences MUST normalize to canonical FROG content already owned by
<code>Expression/</code>, <code>Language/</code>, <code>Libraries/</code>, and <code>Profiles/</code> where relevant.
</p>

<p>
This document defines how a conforming FROG IDE is organized as an authoring, observability, debugging, and inspection
environment without making the language dependent on one particular editor implementation.
</p>

<pre><code>Repository architecture around IDE/

Expression/   -> canonical source form
Language/     -> normative execution semantics
Libraries/    -> intrinsic primitive vocabularies
Profiles/     -> optional standardized capability families
IDE/          -> authoring, discoverability, observability, debugging, inspection

IDE/ owns tooling behavior.
IDE/ does not own source meaning or execution meaning.
</code></pre>

<hr/>

<h2 id="scope">2. Scope of this Document</h2>

<p>
This document specifies the architectural responsibilities of a FROG IDE.
</p>

<p>
It defines:
</p>

<ul>
  <li>the role of the IDE shell,</li>
  <li>the role of diagram and front panel editors,</li>
  <li>the role of the IDE-managed editable Program Model,</li>
  <li>the IDE-facing boundary between authoring and execution,</li>
  <li>the role of palette-driven authoring,</li>
  <li>the architectural role of Express authoring,</li>
  <li>the role of execution observability,</li>
  <li>the role of interactive debugging,</li>
  <li>the role of probes,</li>
  <li>the role of watch-based inspection,</li>
  <li>the role of snippet-based authoring transport.</li>
</ul>

<p>
This document does not define:
</p>

<ul>
  <li>the canonical <code>.frog</code> source format in full,</li>
  <li>the normative execution semantics of the language,</li>
  <li>the complete intrinsic primitive catalogs,</li>
  <li>the complete optional profile catalogs,</li>
  <li>the full compiler architecture,</li>
  <li>the full runtime architecture,</li>
  <li>the full execution-oriented IR architecture.</li>
</ul>

<p>
Those concerns are defined elsewhere in the repository or are expected to be further specified in dedicated execution-facing
layers outside this document.
</p>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
The FROG repository separates several normative concerns.
</p>

<ul>
  <li><code>Expression/</code> defines the canonical source representation of a FROG program.</li>
  <li><code>Language/</code> defines cross-cutting normative execution semantics.</li>
  <li><code>Libraries/</code> defines intrinsic standardized primitive catalogs and primitive-local semantics.</li>
  <li><code>Profiles/</code> defines optional standardized capability families and profile-owned capability contracts.</li>
  <li><code>IDE/</code> defines authoring, observability, debugging, inspection, snippet behavior, and IDE-facing insertion behavior.</li>
</ul>

<p>
Accordingly:
</p>

<ul>
  <li>this document is IDE-facing,</li>
  <li>it may reference source, language, intrinsic-library, and profile-owned concepts,</li>
  <li>but it does not replace the specifications that own those concepts normatively.</li>
</ul>

<p>
More specifically:
</p>

<ul>
  <li><code>Expression/</code> owns canonical serialized identity, including the source-facing representation of structures, widgets, interface nodes, and other graph objects,</li>
  <li><code>Language/</code> owns normative meaning, including cross-cutting execution rules,</li>
  <li><code>Libraries/</code> owns intrinsic primitive identity and primitive-local semantics,</li>
  <li><code>Profiles/</code> owns optional standardized capability families and profile-owned capability definitions,</li>
  <li><code>IDE/</code> owns the authoring environment, the editable Program Model, discoverability, Express authoring behavior, observability, debugging, inspection, and authoring transport.</li>
</ul>

<p>
An IDE MAY expose richer authoring views than the source layer exposes directly. That does not transfer ownership of
source, intrinsic primitive meaning, profile-owned capability meaning, or language execution meaning to the IDE layer.
</p>

<pre><code>Ownership summary

Canonical source identity          -> Expression/
Execution semantics               -> Language/
Intrinsic primitive-local meaning -> Libraries/
Optional capability meaning       -> Profiles/
Tooling behavior and UX           -> IDE/
</code></pre>

<hr/>

<h2 id="responsibility-boundaries">4. Responsibility Boundaries</h2>

<p>
A conforming FROG IDE MUST preserve the architectural separation between:
</p>

<ul>
  <li>authoring,</li>
  <li>canonical source serialization,</li>
  <li>cross-cutting execution semantics,</li>
  <li>intrinsic primitive definitions,</li>
  <li>optional profile-owned capability definitions,</li>
  <li>execution-oriented processing,</li>
  <li>runtime execution,</li>
  <li>source-aligned observability,</li>
  <li>interactive debugging and inspection.</li>
</ul>

<p>
In particular:
</p>

<ul>
  <li>the IDE edits programs through an IDE-managed Program Model,</li>
  <li>the canonical saved artifact remains the <code>.frog</code> source representation,</li>
  <li>language meaning is not defined by the editor UI,</li>
  <li>primitive meaning is not defined by palette placement,</li>
  <li>profile support is not defined by authoring convenience alone,</li>
  <li>debugging and inspection do not redefine execution semantics.</li>
</ul>

<p>
A conforming IDE MAY additionally maintain authoring-oriented abstractions that are more convenient than raw canonical source.
Examples include:
</p>

<ul>
  <li>presentation-specific labels,</li>
  <li>search aliases,</li>
  <li>derived insertion views,</li>
  <li>assistant-driven Express entries,</li>
  <li>editor-side grouping and normalization helpers.</li>
</ul>

<p>
However:
</p>

<ul>
  <li>authoring convenience MUST NOT redefine canonical source identity,</li>
  <li>authoring convenience MUST NOT redefine semantic family identity,</li>
  <li>editor-specific views MUST normalize back to canonical source before serialization,</li>
  <li>editor-specific views MUST preserve source-level meaning across load, edit, serialize, and reload cycles.</li>
</ul>

<p>
More specifically for Express authoring:
</p>

<ul>
  <li>an Express entry MUST NOT become a new semantic node kind by itself,</li>
  <li>an Express entry MUST resolve to canonical source objects already defined by the active specification set,</li>
  <li>assistant-driven configuration MUST remain an IDE concern,</li>
  <li>detaching or discarding an Express presentation MUST leave canonical content valid and recoverable.</li>
</ul>

<hr/>

<h2 id="high-level-architecture">5. High-Level Architecture</h2>

<pre><code>                         FROG IDE

+----------------------+        +------------------------------+
| Front Panel Editor   |        | Diagram Editor               |
| UI / Layout          |        | Graphical Dataflow           |
| Authoring            |        | Authoring                    |
+----------+-----------+        +---------------+--------------+
           \                                 /
            \                               /
             +-----------------------------+
             |      FROG Program Model     |
             | canonical editable          |
             | in-memory model             |
             +-------------+---------------+
                           |
            +--------------+---------------+
            |                              |
            v                              v
+--------------------------+    +-------------------------------+
| Palette Services         |    | Express Authoring Services    |
| search / discovery       |    | guided insertion / configure  |
| aliases / contextual     |    | reopen / detach               |
| views                    |    |                               |
+-------------+------------+    +---------------+---------------+
              \                               /
               \                             /
                +---------------------------+
                | Source serialization      |
                | / reload                  |
                +-------------+-------------+
                              |
                              v
                    FROG Expression (.frog)
                              |
                              v
          Validation / execution preparation boundary
                              |
                              v
     execution-facing systems (semantics / lowering / compiler /
                     runtime / profile support)
                              |
                              v
                Execution Observability Layer
                              |
                 +------------+------------+
                 |                         |
                 v                         v
            Debugging                IDE Inspection
                                              |
                                   +----------+----------+
                                   |                     |
                                   v                     v
                                Probes                 Watch


Snippet Services
  - image-backed snippet export / import / drag-and-drop / paste
  - visible as image outside the IDE
  - decodable as structured payload inside the IDE
</code></pre>

<p>
This architecture is conceptual. Different IDE implementations MAY distribute these responsibilities differently across
modules or processes, but the responsibility boundaries SHOULD remain stable.
</p>

<hr/>

<h2 id="current-documents">6. Current Documents</h2>

<p>
The IDE layer is currently organized as follows:
</p>

<pre><code>IDE/
├── Readme.md
│   -> architectural entry point for the FROG IDE and Program Model
├── Palette.md
│   -> palette model for surfacing primitives, structures, reusable nodes,
│      profiles, and guided authoring entries
├── Express.md
│   -> guided Express authoring model and normalization to canonical FROG content
├── Execution observability.md
│   -> source-aligned live execution observability contract for IDE tooling
├── Debugging.md
│   -> interactive debugging behavior built on source-aligned observability
├── Probes.md
│   -> live local inspection probes for values and selected execution state
├── Watch.md
│   -> persistent centralized watch-based inspection model
├── Snippet.md
│   -> image-backed snippet capture, transport, paste, and reuse workflows
└── FROG Snippet.md
    -> legacy redirect document pointing to Snippet.md
</code></pre>

<p>
Together, these documents define the current IDE-facing baseline for authoring, discoverability, source-aligned execution
visibility, interactive debugging, inspection, and portable authoring-fragment transport.
</p>

<hr/>

<h2 id="main-components">7. Main Components</h2>

<p>
A FROG IDE typically includes the following architectural components:
</p>

<ul>
  <li>an IDE shell,</li>
  <li>a diagram editor,</li>
  <li>a front panel editor,</li>
  <li>a FROG Program Model,</li>
  <li>source serialization and reload services,</li>
  <li>validation and execution-preparation integration,</li>
  <li>palette services,</li>
  <li>Express authoring services,</li>
  <li>execution observability integration,</li>
  <li>debugging services,</li>
  <li>probe services,</li>
  <li>watch services,</li>
  <li>snippet services.</li>
</ul>

<p>
These components MAY be implemented inside one application or across cooperating modules, but their conceptual
responsibilities remain distinct.
</p>

<hr/>

<h2 id="ide-shell">8. IDE Shell</h2>

<p>
The IDE shell is the host application responsible for coordinating the development environment.
It manages the surrounding application experience rather than the language itself.
</p>

<p>
Typical responsibilities include:
</p>

<ul>
  <li>window and layout management,</li>
  <li>menus, toolbars, and command routing,</li>
  <li>project and file navigation,</li>
  <li>document lifecycle management,</li>
  <li>plugin and extension loading,</li>
  <li>integration between editors, palette tools, Express configuration tools, validation services, execution tooling, debugging tools, probe tools, watch tools, and snippet tools.</li>
</ul>

<p>
A conforming IDE MAY implement Express authoring through dialogs, panels, sidebars, inline popovers, staged wizards,
or equivalent interaction surfaces.
That presentation choice is an implementation concern as long as canonical identity, round-trip stability, and source-level
meaning remain preserved.
</p>

<p>
Different IDE implementations MAY use different host technologies while preserving the same language and file format.
</p>

<hr/>

<h2 id="diagram-editor">9. Diagram Editor</h2>

<p>
The diagram editor is the graphical programming environment where users construct executable FROG graphs.
It is an authoring surface for the FROG Program Model.
</p>

<p>
The diagram editor manipulates concepts such as:
</p>

<ul>
  <li>primitive nodes,</li>
  <li>structure nodes,</li>
  <li>sub-FROG invocation nodes,</li>
  <li>interface boundary nodes,</li>
  <li><code>widget_value</code> nodes,</li>
  <li><code>widget_reference</code> nodes,</li>
  <li>wires and typed ports,</li>
  <li>annotations and layout information,</li>
  <li>editor interaction state.</li>
</ul>

<p>
Key capabilities typically include:
</p>

<ul>
  <li>smooth zoom and pan,</li>
  <li>real-time node and wire manipulation,</li>
  <li>incremental validation feedback,</li>
  <li>large-graph navigation,</li>
  <li>execution observability overlays,</li>
  <li>debugging overlays and source-level pause localization,</li>
  <li>probe placement and probe visualization,</li>
  <li>watch creation and watch/source navigation workflows,</li>
  <li>snippet capture, paste, image export, and drag-and-drop insertion workflows,</li>
  <li>Express insertion, reconfiguration, and detach/materialize workflows where supported.</li>
</ul>

<p>
A conforming diagram editor MAY expose authoring-facing insertion modes that are more ergonomic than raw canonical structure names.
For example, it MAY present a boolean <code>case</code> through an <em>If</em> or <em>If / Else</em> authoring view when that helps users work faster.
Such views remain editor-side authoring projections and MUST normalize to canonical source through the Program Model.
</p>

<p>
Likewise, a conforming diagram editor MAY expose task-oriented Express entries for common authoring scenarios.
Those entries MUST still resolve to canonical objects already defined by the active specification set, such as:
</p>

<ul>
  <li>a canonical <code>primitive</code> node,</li>
  <li>a canonical <code>subfrog</code> node,</li>
  <li>or another canonical source-aligned fragment that the IDE knows how to materialize deterministically.</li>
</ul>

<p>
The rendering technology used by a specific IDE implementation is not part of the language specification.
A reference IDE MAY use GPU-accelerated rendering or any equivalent scalable rendering strategy.
</p>

<hr/>

<h2 id="front-panel-editor">10. Front Panel Editor</h2>

<p>
The front panel editor is used to design the graphical interaction layer associated with a FROG program.
It edits the widget tree declared in the <code>front_panel</code> section of the FROG Expression.
</p>

<p>
The front panel editor is responsible for:
</p>

<ul>
  <li>widget declaration,</li>
  <li>widget composition and nesting,</li>
  <li>layout and positioning,</li>
  <li>styling and visual presentation,</li>
  <li>design-time widget configuration.</li>
</ul>

<p>
The front panel is not:
</p>

<ul>
  <li>the public logical interface of the FROG,</li>
  <li>the executable graph of the FROG,</li>
  <li>the place where ordinary value-flow bindings are defined.</li>
</ul>

<p>
Primary widget values participate in execution through <code>widget_value</code> nodes in the diagram.
Object-style widget interaction is expressed through <code>widget_reference</code> nodes together with
<code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code>.
The front panel editor therefore manages widget declaration and presentation, while executable interaction remains
diagram-driven.
</p>

<p>
A debugging-capable IDE MAY additionally reflect source-meaningful execution state on the front panel, and a
snippet-capable IDE MAY support front-panel or composite snippet workflows, but the canonical pause and stepping model
remains diagram-based.
</p>

<hr/>

<h2 id="frog-program-model">11. FROG Program Model</h2>

<p>
The FROG Program Model is the canonical editable in-memory representation maintained by the IDE.
It is the authoritative form of the program during authoring.
</p>

<p>
It unifies the information required for editing and IDE-side consistency management, including:
</p>

<ul>
  <li>metadata,</li>
  <li>public interface definitions,</li>
  <li>connector information,</li>
  <li>diagram content,</li>
  <li>structure regions and nested scopes,</li>
  <li>front-panel widget trees,</li>
  <li>icon and editor-related data,</li>
  <li>cross-section consistency information,</li>
  <li>authoring-side view state where such state is needed to preserve a stable editing experience without redefining canonical meaning.</li>
</ul>

<p>
The Program Model is where the IDE maintains coherent relationships between:
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
The Program Model is designed for:
</p>

<ul>
  <li>editing,</li>
  <li>incremental validation,</li>
  <li>synchronization between views,</li>
  <li>deterministic source serialization,</li>
  <li>source-level mapping between editable objects and runtime-observable objects,</li>
  <li>snippet capture and deterministic paste insertion.</li>
</ul>

<p>
The Program Model MAY temporarily preserve editor-side intent such as preferred insertion view, collapsed presentation,
convenience aliases, Express configuration state, or optional-port visibility where that helps round-trip editing.
However, the Program Model MUST keep canonical structural identity and source meaning recoverable and serializable.
</p>

<p>
If an IDE supports Express authoring, the Program Model SHOULD be able to preserve enough non-authoritative IDE state to:
</p>

<ul>
  <li>reopen the configuration experience for a previously inserted Express-authored instance,</li>
  <li>identify the canonical target edited by that instance,</li>
  <li>preserve deterministic mapping between configuration state and visible optional terminals,</li>
  <li>drop the Express presentation without losing the underlying canonical object model.</li>
</ul>

<p>
This Program Model is an IDE concern.
It is not the canonical serialized source file, and it is not by itself the normative execution-semantics layer of the language.
</p>

<pre><code>Authoring ownership

IDE edits Program Model
        |
        v
Program Model preserves canonical source identity
        |
        v
Source serialization produces .frog Expression
</code></pre>

<hr/>

<h2 id="relation-with-frog-expression">12. Relation with FROG Expression</h2>

<p>
The canonical saved source artifact of a FROG program is the FROG Expression stored in a <code>.frog</code> file.
That source format is defined in <code>Expression/</code>.
</p>

<p>
The IDE is expected to:
</p>

<ul>
  <li>load canonical source into the Program Model,</li>
  <li>edit the Program Model during authoring,</li>
  <li>serialize the Program Model back into canonical source,</li>
  <li>preserve source-level meaning and identity across those operations.</li>
</ul>

<p>
A FROG IDE SHOULD treat the canonical source representation as authoritative at the source level while still maintaining
an internal editable model for interactive tooling.
</p>

<p>
The source format MAY optionally carry IDE-facing preferences or recoverability aids through the source-level
<code>ide</code> section defined by the Expression layer.
Such fields MUST remain non-authoritative for execution semantics.
They MAY help a conforming IDE restore authoring intent, including Express-related presentation state, but they MUST NOT be
required in order to determine canonical executable meaning.
</p>

<p>
If the IDE exposes authoring-facing derived views, aliases, or insertion labels, those facilities MUST survive round-trip
authoring without corrupting canonical source identity.
A stable load → edit → serialize → reload cycle MUST preserve the canonical construct represented by the source, even when
the IDE chooses to present that construct through a more ergonomic authoring form.
</p>

<hr/>

<h2 id="execution-integration-boundary">13. Execution Integration Boundary</h2>

<p>
A FROG IDE MAY integrate validation, execution preparation, compiler services, runtime services, or equivalent execution-facing
subsystems.
</p>

<p>
However, this document does not define those subsystems in full.
It defines only the IDE-facing architectural boundary around them.
</p>

<p>
At minimum, an execution-capable IDE typically needs:
</p>

<ul>
  <li>validation before live execution or build preparation,</li>
  <li>a transition from editable authoring state to execution-prepared state,</li>
  <li>a way to attach source identity to execution-observable objects,</li>
  <li>a way to consume live execution observations for debugging and inspection.</li>
</ul>

<p>
Whether an implementation uses a dedicated execution IR, direct lowering pipeline, intermediate scheduler graph, compiled artifact,
or another equivalent execution-facing form is outside the ownership of this document unless separately standardized elsewhere.
</p>

<p>
The execution integration boundary SHOULD consume canonical source meaning, validated source identity, or equivalent
canonicalized program content.
It SHOULD NOT depend on editor-only labels as if they were semantic language constructs.
</p>

<p>
This also applies to Express authoring:
</p>

<ul>
  <li>execution-facing systems MUST consume canonicalized program content rather than assistant-specific presentation state,</li>
  <li>an IDE MUST NOT require an Express UI in order to validate, prepare, or execute a program,</li>
  <li>Express configuration MUST therefore be reducible to ordinary canonical program content before execution-facing processing.</li>
</ul>

<p>
This also applies to optional profile support:
</p>

<ul>
  <li>the IDE MAY surface profile availability, profile-aware insertion, or profile-scoped validation feedback,</li>
  <li>but profile support claims and profile-owned capability meaning remain owned by the relevant profile specifications and execution-facing support layers,</li>
  <li>the IDE MUST NOT imply profile support merely because it can display or insert a profile-owned construct.</li>
</ul>

<hr/>

<h2 id="palette">14. Palette</h2>

<p>
The palette is the primary IDE mechanism for discovering and inserting reusable authoring elements such as primitives,
structures, interface-related nodes, profile-owned entries, and other editor-supported constructs.
</p>

<p>
The palette belongs to the IDE layer because it is an authoring and discovery surface rather than a primitive catalog.
Accordingly:
</p>

<ul>
  <li><code>Libraries/</code> defines what intrinsic standard primitives exist,</li>
  <li><code>Profiles/</code> defines what optional standardized capability families exist,</li>
  <li><code>Language/</code> defines normative execution semantics where relevant,</li>
  <li><code>Expression/</code> defines canonical source representation,</li>
  <li><code>IDE/Palette.md</code> defines how a FROG IDE exposes those insertable elements to the user.</li>
</ul>

<p>
The palette MAY expose search aliases, contextual insertion views, assistant-driven entries, and authoring-facing labels
that are easier for users to discover than raw canonical names.
For example, a palette MAY surface an <em>If</em> insertion view for the canonical boolean <code>case</code> structure.
It MAY also surface a profile-owned interoperability entry in a profile-scoped category while still preserving the canonical
target identity.
</p>

<p>
However:
</p>

<ul>
  <li>palette presentation MUST NOT create independent canonical identities,</li>
  <li>palette presentation MUST NOT redefine language semantics,</li>
  <li>palette insertion MUST resolve to valid canonical objects known to the active specification set.</li>
</ul>

<p>
Express entries are a special case of palette-driven discoverability:
</p>

<ul>
  <li>they MAY be organized by task or user intent rather than by canonical namespace,</li>
  <li>they SHOULD make canonical target identity visible somewhere in the entry metadata or detail view,</li>
  <li>they MUST remain reducible to canonical source objects.</li>
</ul>

<p>
The detailed palette model SHOULD be defined in <code>IDE/Palette.md</code>.
</p>

<hr/>

<h2 id="express-authoring">15. Express Authoring</h2>

<p>
Express authoring is the IDE-layer capability that allows a user to insert or edit common programming constructs through
a guided configuration experience rather than through raw low-level assembly alone.
It exists to improve discoverability, speed of use, and usability for common tasks without creating a separate language.
</p>

<p>
An Express entry is therefore:
</p>

<ul>
  <li>assistant-driven,</li>
  <li>instance-local,</li>
  <li>task-oriented,</li>
  <li>normalizable to canonical FROG content.</li>
</ul>

<p>
An Express entry is not:
</p>

<ul>
  <li>a new semantic family of node,</li>
  <li>a replacement for canonical source identity,</li>
  <li>a permission to bypass standardized primitive or structure definitions,</li>
  <li>a reason for execution-facing systems to depend on editor-private state.</li>
</ul>

<p>
A conforming IDE MAY implement Express authoring in several ways, including:
</p>

<ul>
  <li>configuration of a canonical <code>primitive</code> node,</li>
  <li>configuration of a canonical <code>subfrog</code> node,</li>
  <li>deterministic materialization of a canonical source fragment that the IDE can preserve and re-edit safely.</li>
</ul>

<p>
If Express authoring is supported, the IDE SHOULD distinguish clearly between:
</p>

<ul>
  <li><strong>configurable parameters</strong> — values or options primarily edited through the configuration experience,</li>
  <li><strong>expandable terminals</strong> — optional visible inputs or outputs that the user may expose directly on the diagram,</li>
  <li><strong>canonical target identity</strong> — the actual primitive, sub-FROG, or canonical fragment to which the Express instance resolves.</li>
</ul>

<p>
Expandable terminals MUST correspond to ports that are valid for the canonical target.
An Express presentation MUST NOT invent semantically invalid ports merely for convenience.
</p>

<p>
A conforming IDE SHOULD support at least the following Express lifecycle operations where Express authoring exists:
</p>

<ul>
  <li>insert and configure,</li>
  <li>reopen configuration,</li>
  <li>preserve instance-local configuration state across round-trip editing,</li>
  <li>reveal the canonical target identity,</li>
  <li>detach, flatten, or otherwise discard the Express presentation without corrupting canonical content.</li>
</ul>

<p>
This document defines the architectural role of Express authoring.
More detailed behavioral standardization MAY later be refined in dedicated IDE-facing specifications.
</p>

<hr/>

<h2 id="execution-observability">16. Execution Observability</h2>

<p>
Execution observability is the architectural layer that exposes a source-aligned live view of a running FROG instance to
the IDE.
It allows runtime activity to be projected back onto diagram and front-panel-related source objects without redefining the
execution semantics of the language.
</p>

<p>
Conceptually, execution observability sits between live execution and IDE inspection/debugging features.
It is responsible for making runtime activity visible in terms such as:
</p>

<ul>
  <li>node activation,</li>
  <li>edge-level value availability,</li>
  <li>structure entry and region selection,</li>
  <li>loop iteration progression,</li>
  <li>local-memory state activity,</li>
  <li>pause-consistent execution snapshots.</li>
</ul>

<p>
Execution observability is source-aligned.
It is expressed in terms of diagram-visible and other source-meaningful objects rather than runtime-private implementation details.
</p>

<p>
The detailed source-level contract for this layer SHOULD be defined in <code>IDE/Execution observability.md</code>.
</p>

<hr/>

<h2 id="debugging">17. Debugging</h2>

<p>
Debugging is the interactive control layer built on top of live execution observability.
It allows an IDE to pause, resume, inspect, and guide execution in a source-level way.
</p>

<p>
Canonical debugging capabilities include:
</p>

<ul>
  <li>execution highlighting,</li>
  <li>manual pause and resume,</li>
  <li>breakpoints,</li>
  <li>single-step controls,</li>
  <li>fault-directed source localization.</li>
</ul>

<p>
Debugging in FROG is dataflow-first rather than line-oriented.
The IDE therefore debugs observable graph activity, structures, sub-FROG scopes, and explicit UI-related execution
objects rather than pretending that the program is a sequential instruction list.
</p>

<p>
A debugging-capable IDE MAY present user-facing labels that are easier to understand than raw canonical names, but pause,
step, and inspection behavior MUST remain source-aligned and semantically faithful to the underlying standardized constructs.
</p>

<p>
The detailed source-level behavior of these controls SHOULD be defined in <code>IDE/Debugging.md</code>.
</p>

<hr/>

<h2 id="probes">18. Probes</h2>

<p>
Probes are source-aligned live inspection tools built on top of execution observability and used together with debugging.
They allow an IDE to observe values or source-level execution state associated with objects such as:
</p>

<ul>
  <li>edges,</li>
  <li>node ports,</li>
  <li>local-memory state,</li>
  <li>selected UI-related execution objects in stricter profiles.</li>
</ul>

<p>
For FROG v0.1, the canonical probe model is centered on edge-oriented inspection, because ordinary dataflow is most
naturally observed at the level of value availability on edges.
</p>

<p>
Probes belong to the inspection and debugging layer.
They do not alter program semantics, and they are not part of the canonical <code>.frog</code> source representation.
</p>

<p>
The detailed source-level behavior of probes SHOULD be defined in <code>IDE/Probes.md</code>.
</p>

<hr/>

<h2 id="watch">19. Watch</h2>

<p>
Watch is the persistent inspection layer of the IDE.
Where probes are attached directly to visible source locations, watch entries are persistent inspection objects gathered
in a centralized view.
</p>

<p>
A watch-capable IDE typically supports:
</p>

<ul>
  <li>persistent observation across pauses and resumes,</li>
  <li>multiple simultaneous watched objects,</li>
  <li>navigation from watch entry to source object,</li>
  <li>inspection of values, state, and selected source-aligned execution objects,</li>
  <li>combination with debugging workflows.</li>
</ul>

<p>
Watch belongs to the IDE layer and does not alter language semantics.
The detailed watch model SHOULD be defined in <code>IDE/Watch.md</code>.
</p>

<hr/>

<h2 id="snippets">20. Snippets</h2>

<p>
Snippets are portable IDE artifacts used to capture, transport, preview, and reinsert reusable authoring fragments.
They support workflows such as:
</p>

<ul>
  <li>copy and paste of reusable diagram fragments,</li>
  <li>drag-and-drop insertion into a target editor,</li>
  <li>sharing small reusable authoring patterns,</li>
  <li>transporting a graph fragment with its visual layout and related metadata,</li>
  <li>front-panel or composite authoring reuse,</li>
  <li>visual sharing of reusable fragments outside the IDE.</li>
</ul>

<p>
In FROG, a standalone snippet artifact is intended to be <strong>image-backed</strong>:
</p>

<ul>
  <li>it is visible as a normal image outside the IDE,</li>
  <li>it carries embedded structured snippet payload data,</li>
  <li>a conforming FROG IDE can decode that payload during import, paste, or drag-and-drop.</li>
</ul>

<p>
This means that snippet workflows operate at the authoring layer rather than the execution-semantics layer.
They complement the Program Model and the editing experience without changing the canonical source-program model itself.
</p>

<p>
If a snippet carries content originating from an Express-authored instance, a conforming IDE MAY preserve related
IDE-facing Express recoverability metadata where that metadata remains source-safe and non-authoritative.
Dropping such metadata MUST NOT invalidate the carried canonical content.
</p>

<p>
The detailed snippet transport and insertion model SHOULD be defined in <code>IDE/Snippet.md</code>.
</p>

<hr/>

<h2 id="design-principles">21. Design Principles</h2>

<ul>
  <li>Clear separation of source, authoring model, and execution-facing systems</li>
  <li>Language independence from IDE implementation</li>
  <li>Open serialized program representation</li>
  <li>Instant editing feedback</li>
  <li>Incremental validation</li>
  <li>Hardware-agnostic execution</li>
  <li>Cross-platform tooling</li>
  <li>Scalable graphical editing for large programs</li>
  <li>Explicit separation between interface, front panel, and diagram</li>
  <li>Source-aligned execution observability</li>
  <li>Dataflow-native debugging semantics</li>
  <li>Non-intrusive live inspection through probes</li>
  <li>Persistent centralized inspection through watch views</li>
  <li>Portable authoring-fragment transport through snippets</li>
  <li>Image-backed reusable snippet workflows for drag-and-drop authoring reuse</li>
  <li>Authoring convenience without semantic drift</li>
  <li>Preservation of canonical identity across aliases, views, assistant-driven flows, and contextual insertion workflows</li>
  <li>Express authoring as an IDE convenience layer rather than a separate language</li>
  <li>Deterministic normalization from guided authoring to canonical source content</li>
  <li>Optional IDE recoverability metadata without executable authority</li>
  <li>Clear distinction between intrinsic capability discovery and optional profile discovery</li>
</ul>

<hr/>

<h2 id="repository-direction">22. Repository Direction</h2>

<p>
At the current repository stage, <code>IDE/</code> is the home for IDE-facing specifications such as:
</p>

<ul>
  <li>overall IDE architecture,</li>
  <li>palette behavior,</li>
  <li>Express authoring behavior,</li>
  <li>execution observability,</li>
  <li>debugging,</li>
  <li>probes,</li>
  <li>watch,</li>
  <li>snippets.</li>
</ul>

<p>
The long-term repository architecture SHOULD preserve a stable separation between:
</p>

<ul>
  <li><code>Expression/</code> for canonical source representation,</li>
  <li><code>Language/</code> for normative execution semantics,</li>
  <li><code>Libraries/</code> for intrinsic standardized primitive catalogs,</li>
  <li><code>Profiles/</code> for optional standardized capability families,</li>
  <li><code>IDE/</code> for authoring, discoverability, Express behavior, observability, debugging, and inspection.</li>
</ul>

<p>
Additional execution-facing layers such as IR, compilation, deployment, or runtime specifications MAY be structured more
explicitly elsewhere in the repository over time.
</p>

<p>
As the repository grows, the IDE layer SHOULD continue to absorb authoring-facing concerns such as discovery,
presentation, Express interaction, snippet transport, and source-aligned inspection, while leaving canonical source and
semantic ownership to the layers that already own them normatively.
</p>

<p>
More detailed Express lifecycle behavior MAY later be refined in a dedicated IDE-facing specification while preserving the
ownership boundaries defined here.
</p>

<hr/>

<h2 id="summary">23. Summary</h2>

<p>
A FROG IDE is not just a diagram editor.
It is a layered authoring and inspection environment centered on:
</p>

<ul>
  <li>a canonical editable Program Model,</li>
  <li>a canonical source representation defined outside the IDE layer,</li>
  <li>palette-driven and Express-capable authoring workflows,</li>
  <li>a source-aligned execution observability layer,</li>
  <li>dataflow-native debugging and inspection tools,</li>
  <li>portable snippet-based authoring reuse workflows.</li>
</ul>

<p>
In that architecture:
</p>

<ul>
  <li>editing operates on the Program Model,</li>
  <li>storage operates through the canonical FROG Expression,</li>
  <li>execution-facing systems remain separate from IDE ownership,</li>
  <li>runtime activity becomes visible through execution observability,</li>
  <li>debugging, probes, and watch consume that observable view,</li>
  <li>snippets provide portable, image-backed authoring-fragment reuse workflows,</li>
  <li>Express authoring provides guided insertion and reconfiguration without creating a separate language layer,</li>
  <li>optional profile-facing discoverability remains an IDE concern while profile meaning remains owned elsewhere.</li>
</ul>

<p>
A conforming IDE MAY provide rich authoring-facing conveniences, including aliases, derived insertion views, assistant-driven
Express entries, and contextual presentations.
Those conveniences remain valid only if they preserve canonical source identity and avoid semantic drift.
</p>

<p>
This architecture allows FROG to remain an open graphical language while supporting serious IDE implementations without
confusing source ownership, language ownership, intrinsic primitive ownership, optional profile ownership, execution-facing systems, and IDE-facing tooling.
</p>

<hr/>

<h2 id="license">24. License</h2>

<p>
This document is part of the FROG specification repository and is distributed under the repository license.
See the root repository files for the current licensing terms.
</p>
