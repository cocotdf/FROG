<div align="center">

<h1>FROG IDE Architecture</h1>

<p>
<b>FROG — Free Open Graphical Language</b><br>
Open Source Graphical Dataflow Development Environment
</p>

</div>

<hr>

<h2>Overview</h2>

<p>
The FROG IDE is the graphical development environment used to design, edit, validate, debug, and execute programs written in the FROG graphical dataflow language.
</p>

<p>
The IDE does <b>not</b> treat the saved <code>.frog</code> file as an execution artifact.
Instead, it loads and maintains an internal <b>FROG Program Model</b>, which is the canonical editable representation of the program inside the development environment.
</p>

<p>
Programs are stored on disk as a serialized source representation called the <b>FROG Expression</b>.
The Expression describes the program structure, interface, front panel, metadata, and editor-related information in an open JSON-based format.
</p>

<p>
When execution is requested, the IDE and compiler transform the validated Program Model into a dedicated <b>FROG Execution IR</b>, which is the canonical execution representation used for compilation and runtime preparation.
</p>

<p>
This architecture separates:
</p>

<ul>
<li>the graphical editing environment</li>
<li>the serialized source representation</li>
<li>the internal editable program model</li>
<li>the execution-oriented intermediate representation</li>
<li>the compiler toolchain</li>
<li>the execution runtime</li>
</ul>

<p>
This separation ensures that the FROG language remains independent from any specific IDE implementation while preserving a clear boundary between authoring, storage, compilation, and execution.
</p>

<hr>

<h2>Core Representation Model</h2>

<p>
The FROG architecture is based on three distinct representation levels.
</p>

<h3>1. FROG Expression</h3>

<p>
The <b>FROG Expression</b> is the serialized source form stored in a <code>.frog</code> file.
It is the portable, tool-independent representation of the program.
</p>

<h3>2. FROG Program Model</h3>

<p>
The <b>FROG Program Model</b> is the internal editable representation maintained by the IDE.
It is reconstructed from the Expression when a program is loaded and continuously updated while the user edits the diagram or front panel.
</p>

<h3>3. FROG Execution IR</h3>

<p>
The <b>FROG Execution IR</b> is the execution-oriented representation derived from the validated Program Model.
It is intended for analysis, compilation, optimization, scheduling, and runtime preparation.
</p>

<p>
In short:
</p>

<div align="center">

<pre>

.frog file
   = FROG Expression

Loaded in IDE
   = FROG Program Model

Prepared for execution
   = FROG Execution IR

</pre>

</div>

<hr>

<h2>High-Level Architecture</h2>

<div align="center">

<pre>

+------------------------------------------------------------------+
|                             FROG IDE                             |
|                                                                  |
|  +------------------------+    +-------------------------------+ |
|  |   Front Panel Editor   |    |        Diagram Editor         | |
|  |   UI / Layout Authoring|    |   Graphical Dataflow Authoring| |
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

</div>

<hr>

<h2>Main Components</h2>

<h3>IDE Shell</h3>

<p>
The IDE shell is the host application responsible for coordinating the development environment.
It manages navigation, layout, project-level actions, file operations, and integration between editors and backend services.
</p>

<p>
Typical responsibilities include:
</p>

<ul>
<li>window and layout management</li>
<li>menus, toolbars, and command routing</li>
<li>project and file navigation</li>
<li>document lifecycle management</li>
<li>plugin and extension loading</li>
<li>integration between editors, compiler services, and runtime tools</li>
</ul>

<p>
The shell is an application layer and is intentionally separated from the language definition itself.
Different FROG IDE implementations may use different host technologies while preserving the same language and file format.
</p>

<hr>

<h3>Diagram Editor</h3>

<p>
The diagram editor is the graphical programming environment where users construct FROG dataflow programs.
</p>

<p>
As the user edits the diagram, the IDE updates the <b>FROG Program Model</b> in real time.
The diagram editor is therefore an authoring surface for the Program Model, not the execution representation itself.
</p>

<p>
The diagram editor manipulates concepts such as:
</p>

<ul>
<li>nodes and structures</li>
<li>wires and data dependencies</li>
<li>typed ports</li>
<li>placement and layout information</li>
<li>editor interaction state</li>
</ul>

<p>
Key capabilities include:
</p>

<ul>
<li>smooth zoom and pan</li>
<li>real-time node and wire manipulation</li>
<li>incremental validation feedback</li>
<li>scalable rendering for large graphs</li>
<li>debug visualization overlays</li>
</ul>

<p>
The rendering technology used by a specific IDE implementation is not part of the language specification.
A reference IDE may use GPU-accelerated rendering for responsiveness on large diagrams.
</p>

<hr>

<h3>Front Panel Editor</h3>

<p>
The front panel editor is used to design the user-facing interface associated with a FROG program.
</p>

<p>
It defines the interaction layer that exposes controls, indicators, and visual components connected to the program interface.
</p>

<p>
Typical front panel elements include:
</p>

<ul>
<li>buttons and switches</li>
<li>numeric, string, and enum controls</li>
<li>indicators and status displays</li>
<li>graphs, charts, and gauges</li>
<li>custom interactive UI elements</li>
</ul>

<p>
The front panel editor updates the <b>FROG Program Model</b> and contributes to the serialized <b>FROG Expression</b>, but it is not itself part of the execution engine.
</p>

<p>
Concrete rendering technologies may vary between IDE implementations.
For example, a reference implementation may use web-based UI technologies such as HTML, SVG, and JavaScript for scalable, resolution-independent interface authoring.
</p>

<hr>

<h3>FROG Program Model</h3>

<p>
The <b>FROG Program Model</b> is the canonical editable in-memory representation maintained by the IDE.
</p>

<p>
It unifies the program sections required for editing and validation, including:
</p>

<ul>
<li>program structure</li>
<li>diagram content</li>
<li>interface definitions</li>
<li>front panel bindings</li>
<li>metadata and editor state</li>
<li>cross-section consistency information</li>
</ul>

<p>
The Program Model is the authoritative representation inside the IDE during authoring.
It is designed for editing, validation, synchronization between views, and preparation for lowering to execution form.
</p>

<hr>

<h3>FROG Expression</h3>

<p>
The <b>FROG Expression</b> is the serialized source representation of a FROG program.
</p>

<p>
File extension:
</p>

<pre>.frog</pre>

<p>
The Expression is generated by serializing the current <b>FROG Program Model</b>.
It is intended to be stable, readable, portable, and independent from any single IDE implementation.
</p>

<p>
Depending on the program, the Expression may contain:
</p>

<ul>
<li>metadata</li>
<li>interface definitions</li>
<li>diagram structure</li>
<li>front panel description</li>
<li>icon data</li>
<li>IDE preferences</li>
<li>optional non-authoritative cache sections</li>
</ul>

<p>
This format is designed to be:
</p>

<ul>
<li>human readable</li>
<li>version-control friendly</li>
<li>portable across tools and platforms</li>
<li>suitable as the canonical source file</li>
</ul>

<hr>

<h3>Validation and Lowering</h3>

<p>
Before execution, the Program Model is validated and transformed into the <b>FROG Execution IR</b>.
</p>

<p>
This phase includes responsibilities such as:
</p>

<ul>
<li>structural validation</li>
<li>type checking</li>
<li>interface consistency checks</li>
<li>semantic verification</li>
<li>binding resolution</li>
<li>preparation for scheduling and optimization</li>
</ul>

<p>
This stage forms the boundary between interactive authoring and execution-oriented processing.
</p>

<hr>

<h3>FROG Execution IR</h3>

<p>
The <b>FROG Execution IR</b> is the canonical execution-oriented representation derived from the validated Program Model.
</p>

<p>
It contains only the information required for execution-related workflows, such as:
</p>

<ul>
<li>resolved operations and nodes</li>
<li>validated data dependencies</li>
<li>normalized type information</li>
<li>execution constraints</li>
<li>scheduling metadata</li>
<li>target preparation data</li>
</ul>

<p>
The Execution IR is not the primary authoring format and is not the same thing as the saved <code>.frog</code> source file.
It exists to support compilation, optimization, target lowering, and runtime integration.
</p>

<hr>

<h3>Compiler</h3>

<p>
The compiler transforms the validated <b>FROG Execution IR</b> into executable artifacts for specific targets.
</p>

<p>
Compiler responsibilities include:
</p>

<ul>
<li>IR analysis</li>
<li>optimization passes</li>
<li>target-specific lowering</li>
<li>code generation</li>
<li>artifact production for deployment or execution</li>
</ul>

<p>
The compiler is a separate subsystem from the IDE and may evolve independently from the editor implementation.
</p>

<hr>

<h3>Runtime</h3>

<p>
The runtime is the execution subsystem responsible for running compiled FROG programs or target-specific execution artifacts.
</p>

<p>
Typical runtime responsibilities include:
</p>

<ul>
<li>dataflow scheduling</li>
<li>data propagation</li>
<li>parallel execution support</li>
<li>memory and buffer coordination</li>
<li>debug and instrumentation hooks</li>
<li>platform integration</li>
</ul>

<p>
The runtime is independent from the serialized Expression and from the graphical authoring environment.
This separation allows FROG programs to execute without requiring the IDE itself.
</p>

<hr>

<h2>Execution Flow</h2>

<div align="center">

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

</div>

<hr>

<h2>Design Principles</h2>

<ul>
<li><b>Clear separation of source, model, and execution</b></li>
<li><b>Language independence from IDE implementation</b></li>
<li><b>Open serialized program representation</b></li>
<li><b>Instant editing feedback</b></li>
<li><b>Incremental validation</b></li>
<li><b>Hardware-agnostic execution</b></li>
<li><b>Cross-platform tooling</b></li>
<li><b>Scalable graphical editing for large programs</b></li>
</ul>

<hr>

<h2>Repository Direction</h2>

<p>
A full FROG ecosystem may be organized into distinct components such as:
</p>

<pre>

FROG/
│
├── IDE/
│   ├── shell/
│   ├── diagram-editor/
│   ├── front-panel-editor/
│   └── shared-services/
│
├── compiler/
├── runtime/
├── Spec/
└── tools/

</pre>

<p>
The exact repository layout may evolve over time.
What matters architecturally is the separation between editing, representation, compilation, and execution.
</p>

<hr>

<h2>License</h2>

<p>
FROG is distributed under the Apache 2.0 license and uses a Contributor License Agreement (CLA) for external contributions.
</p>

<hr>

<div align="center">

<p>
FROG — Free Open Graphical Language
</p>

</div>

