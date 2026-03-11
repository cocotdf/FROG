<h1 align="center">🐸 FROG IDE Architecture</h1>

<p align="center">
Definition of the architecture and responsibilities of a FROG development environment<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#core-representation-model">2. Core Representation Model</a></li>
  <li><a href="#high-level-architecture">3. High-Level Architecture</a></li>
  <li><a href="#main-components">4. Main Components</a></li>
  <li><a href="#ide-shell">5. IDE Shell</a></li>
  <li><a href="#diagram-editor">6. Diagram Editor</a></li>
  <li><a href="#front-panel-editor">7. Front Panel Editor</a></li>
  <li><a href="#frog-program-model">8. FROG Program Model</a></li>
  <li><a href="#frog-expression">9. FROG Expression</a></li>
  <li><a href="#validation-and-lowering">10. Validation and Lowering</a></li>
  <li><a href="#frog-execution-ir">11. FROG Execution IR</a></li>
  <li><a href="#compiler">12. Compiler</a></li>
  <li><a href="#runtime">13. Runtime</a></li>
  <li><a href="#execution-flow">14. Execution Flow</a></li>
  <li><a href="#design-principles">15. Design Principles</a></li>
  <li><a href="#repository-direction">16. Repository Direction</a></li>
  <li><a href="#summary">17. Summary</a></li>
  <li><a href="#license">18. License</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The FROG IDE is the graphical development environment used to design, edit, validate, inspect, debug, and execute programs written in the FROG graphical dataflow language.
</p>

<p>
A FROG IDE does not treat the saved <code>.frog</code> file as the execution artifact.
Instead, it loads and maintains an internal <strong>FROG Program Model</strong>, which is the canonical editable in-memory representation of the program.
</p>

<p>
Programs are stored on disk as a serialized source representation called the <strong>FROG Expression</strong>.
When execution is requested, the validated Program Model is transformed into a dedicated <strong>FROG Execution IR</strong>, which is the canonical execution-oriented representation used for analysis, optimization, compilation, lowering, and runtime preparation.
</p>

<p>
This architecture separates:
</p>

<ul>
  <li>authoring,</li>
  <li>source serialization,</li>
  <li>editable in-memory representation,</li>
  <li>execution-oriented representation,</li>
  <li>compiler toolchains,</li>
  <li>runtime systems.</li>
</ul>

<p>
This separation allows the FROG language to remain independent from any specific IDE implementation while preserving a clean boundary between editing, storage, compilation, and execution.
</p>

<hr/>

<h2 id="core-representation-model">2. Core Representation Model</h2>

<p>
The FROG architecture is based on three distinct representation levels.
</p>

<h3>2.1 FROG Expression</h3>

<p>
The FROG Expression is the serialized source form stored in a <code>.frog</code> file.
It is the portable, tool-independent source representation of the program.
</p>

<h3>2.2 FROG Program Model</h3>

<p>
The FROG Program Model is the canonical editable in-memory representation maintained by the IDE.
It is reconstructed from the Expression when a program is loaded and continuously updated while the user edits the program.
</p>

<h3>2.3 FROG Execution IR</h3>

<p>
The FROG Execution IR is the canonical execution-oriented representation derived from the validated Program Model.
It is intended for analysis, normalization, optimization, scheduling, lowering, compilation, and runtime preparation.
</p>

<p>
Conceptually:
</p>

<pre>
.frog file
   = FROG Expression

loaded in IDE
   = FROG Program Model

prepared for execution
   = FROG Execution IR
</pre>

<hr/>

<h2 id="high-level-architecture">3. High-Level Architecture</h2>

<pre>
+------------------------------------------------------------------+
|                             FROG IDE                             |
|                                                                  |
|  +------------------------+    +-------------------------------+ |
|  |   Front Panel Editor   |    |        Diagram Editor         | |
|  | UI / Layout Authoring  |    | Graphical Dataflow Authoring  | |
|  +------------------------+    +-------------------------------+ |
|                |                              |                  |
|                +--------------+---------------+                  |
|                               |                                  |
|                     FROG Program Model                           |
|              (canonical editable in-memory model)                |
+------------------------------|-----------------------------------+
                               |
                               v
                         Serialization
                               |
                               v
                         FROG Expression
                           (.frog file)
                               |
                               v
                           Validation
                               |
                               v
                        Lowering / Analysis
                               |
                               v
                        FROG Execution IR
                      (canonical execution form)
                               |
                               v
                            Compiler
                               |
                               v
                            Runtime
</pre>

<hr/>

<h2 id="main-components">4. Main Components</h2>

<p>
A FROG IDE typically includes the following architectural components:
</p>

<ul>
  <li>an IDE shell,</li>
  <li>a diagram editor,</li>
  <li>a front panel editor,</li>
  <li>a FROG Program Model,</li>
  <li>serialization services for the FROG Expression,</li>
  <li>validation and lowering services,</li>
  <li>compiler integration,</li>
  <li>runtime integration.</li>
</ul>

<p>
These components may be implemented as one application or as multiple cooperating modules, but their conceptual responsibilities remain distinct.
</p>

<hr/>

<h2 id="ide-shell">5. IDE Shell</h2>

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
  <li>integration between editors, compiler services, and runtime tools.</li>
</ul>

<p>
Different IDE implementations MAY use different host technologies while preserving the same language and file format.
</p>

<hr/>

<h2 id="diagram-editor">6. Diagram Editor</h2>

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
  <li>debug and inspection overlays.</li>
</ul>

<p>
The rendering technology used by a specific IDE implementation is not part of the language specification.
A reference IDE MAY use GPU-accelerated rendering or any equivalent scalable rendering strategy.
</p>

<hr/>

<h2 id="front-panel-editor">7. Front Panel Editor</h2>

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
The front panel is <strong>not</strong>:
</p>

<ul>
  <li>the public logical interface of the FROG,</li>
  <li>the executable graph of the FROG,</li>
  <li>the place where ordinary value-flow bindings are defined.</li>
</ul>

<p>
Primary widget values participate in execution through <code>widget_value</code> nodes in the diagram.
Object-style widget interaction is expressed through <code>widget_reference</code> nodes together with <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code>.
</p>

<p>
The front panel editor therefore manages widget declaration and presentation, while executable interaction remains diagram-driven.
</p>

<hr/>

<h2 id="frog-program-model">8. FROG Program Model</h2>

<p>
The FROG Program Model is the canonical editable in-memory representation maintained by the IDE.
It is the authoritative form of the program during authoring.
</p>

<p>
It unifies the information required for editing and validation, including:
</p>

<ul>
  <li>metadata,</li>
  <li>public interface definitions,</li>
  <li>connector information,</li>
  <li>diagram content,</li>
  <li>structure regions and nested scopes,</li>
  <li>front-panel widget trees,</li>
  <li>icon and editor-related data,</li>
  <li>cross-section consistency information.</li>
</ul>

<p>
The Program Model is where the IDE maintains coherent relationships between:
</p>

<ul>
  <li>interface declarations and <code>interface_input</code> / <code>interface_output</code> nodes,</li>
  <li>front-panel widget declarations and <code>widget_value</code> / <code>widget_reference</code> nodes,</li>
  <li>structure nodes and their owned regions,</li>
  <li>semantic graph content and source-level layout information.</li>
</ul>

<p>
The Program Model is designed for:
</p>

<ul>
  <li>editing,</li>
  <li>incremental validation,</li>
  <li>synchronization between views,</li>
  <li>preparation for execution-oriented lowering.</li>
</ul>

<hr/>

<h2 id="frog-expression">9. FROG Expression</h2>

<p>
The FROG Expression is the serialized source representation of a FROG program.
</p>

<p>
File extension:
</p>

<pre>.frog</pre>

<p>
The Expression is produced by serializing the current Program Model.
It is intended to be stable, readable, portable, and independent from any one IDE implementation.
</p>

<p>
Depending on the program, the Expression may contain:
</p>

<ul>
  <li>metadata,</li>
  <li>interface definitions,</li>
  <li>connector definitions,</li>
  <li>diagram structure,</li>
  <li>front-panel description,</li>
  <li>icon data,</li>
  <li>IDE preferences,</li>
  <li>optional non-authoritative cache sections.</li>
</ul>

<p>
The Expression is designed to be:
</p>

<ul>
  <li>human-readable,</li>
  <li>version-control friendly,</li>
  <li>portable across tools and platforms,</li>
  <li>suitable as the canonical source file.</li>
</ul>

<hr/>

<h2 id="validation-and-lowering">10. Validation and Lowering</h2>

<p>
Before execution, the Program Model is validated and transformed into the FROG Execution IR.
</p>

<p>
This phase includes responsibilities such as:
</p>

<ul>
  <li>structural validation,</li>
  <li>type checking,</li>
  <li>interface consistency checks,</li>
  <li>widget consistency checks,</li>
  <li>structure validation,</li>
  <li>cycle and local-state validation,</li>
  <li>dependency resolution,</li>
  <li>preparation for scheduling and optimization.</li>
</ul>

<p>
This phase forms the architectural boundary between interactive authoring and execution-oriented processing.
</p>

<hr/>

<h2 id="frog-execution-ir">11. FROG Execution IR</h2>

<p>
The FROG Execution IR is the canonical execution-oriented representation derived from the validated Program Model.
</p>

<p>
It contains only the information required for execution-related workflows, such as:
</p>

<ul>
  <li>resolved operations and nodes,</li>
  <li>validated data dependencies,</li>
  <li>normalized type information,</li>
  <li>execution constraints,</li>
  <li>scheduling metadata,</li>
  <li>target preparation data.</li>
</ul>

<p>
The Execution IR is not the primary authoring format and is not the same thing as the saved <code>.frog</code> file.
It exists to support compilation, optimization, target lowering, and runtime integration.
</p>

<hr/>

<h2 id="compiler">12. Compiler</h2>

<p>
The compiler transforms the validated FROG Execution IR into executable artifacts for specific targets.
</p>

<p>
Compiler responsibilities typically include:
</p>

<ul>
  <li>IR analysis,</li>
  <li>optimization passes,</li>
  <li>target-specific lowering,</li>
  <li>code generation,</li>
  <li>artifact production for deployment or execution.</li>
</ul>

<p>
The compiler is a separate subsystem from the IDE and MAY evolve independently from the editor implementation.
</p>

<hr/>

<h2 id="runtime">13. Runtime</h2>

<p>
The runtime is the execution subsystem responsible for running compiled FROG programs or target-specific execution artifacts.
</p>

<p>
Typical runtime responsibilities include:
</p>

<ul>
  <li>dataflow scheduling,</li>
  <li>data propagation,</li>
  <li>parallel execution support,</li>
  <li>memory and buffer coordination,</li>
  <li>debug and instrumentation hooks,</li>
  <li>platform integration.</li>
</ul>

<p>
The runtime is independent from the serialized Expression and from the graphical authoring environment.
This separation allows FROG programs to execute without requiring the IDE itself.
</p>

<hr/>

<h2 id="execution-flow">14. Execution Flow</h2>

<pre>
User edits diagram or front panel
              ↓
IDE updates FROG Program Model
              ↓
IDE serializes Program Model as FROG Expression (.frog)
              ↓
User requests execution
              ↓
Program Model is validated
              ↓
Program Model is lowered to FROG Execution IR
              ↓
Compiler generates target-specific executable form
              ↓
Runtime executes the program
</pre>

<hr/>

<h2 id="design-principles">15. Design Principles</h2>

<ul>
  <li>Clear separation of source, model, and execution</li>
  <li>Language independence from IDE implementation</li>
  <li>Open serialized program representation</li>
  <li>Instant editing feedback</li>
  <li>Incremental validation</li>
  <li>Hardware-agnostic execution</li>
  <li>Cross-platform tooling</li>
  <li>Scalable graphical editing for large programs</li>
  <li>Explicit separation between interface, front panel, and diagram</li>
</ul>

<hr/>

<h2 id="repository-direction">16. Repository Direction</h2>

<p>
A full FROG ecosystem may be organized into distinct components such as:
</p>

<pre>
FROG/
│
├── Expression/
├── IDE/
│   ├── shell/
│   ├── diagram-editor/
│   ├── front-panel-editor/
│   └── shared-services/
│
├── Language/
├── Libraries/
├── compiler/
├── runtime/
└── tools/
</pre>

<p>
The exact repository layout may evolve over time.
What matters architecturally is the separation between canonical source specification, language semantics, editing, compilation, and execution.
</p>

<hr/>

<h2 id="summary">17. Summary</h2>

<p>
The FROG IDE is an authoring environment built around a three-layer representation model:
</p>

<ul>
  <li><strong>FROG Expression</strong> — canonical serialized source,</li>
  <li><strong>FROG Program Model</strong> — canonical editable in-memory representation,</li>
  <li><strong>FROG Execution IR</strong> — canonical execution-oriented representation.</li>
</ul>

<p>
This architecture ensures that:
</p>

<ul>
  <li>the language remains independent from the IDE,</li>
  <li>editing remains distinct from execution,</li>
  <li>front-panel composition remains distinct from executable graph semantics,</li>
  <li>validation and lowering remain explicit architectural phases.</li>
</ul>

<p>
It provides a clean foundation for multiple IDEs, compilers, and runtimes to support the same open graphical language.
</p>

<hr/>

<h2 id="license">18. License</h2>

<p>
FROG is distributed under the Apache 2.0 license and uses a Contributor License Agreement (CLA) for external contributions.
</p>

<hr/>

<p align="center">
  <strong>FROG — Free Open Graphical Language</strong>
</p>
