<div align="center">

<h1>FROG IDE Architecture</h1>

<p>
<b>FROG — Free Open Graphical Language</b><br>
Open Source Graphical Dataflow Programming Environment
</p>

</div>

<hr>

<h2>Overview</h2>

<p>
The FROG IDE is the graphical development environment used to create, edit, debug, and execute programs written in the FROG graphical dataflow language.
</p>

<p>
The IDE is designed as a modular system where editing, compilation, and execution are clearly separated. This architecture ensures that the FROG language remains independent from the IDE implementation while allowing multiple execution targets.
</p>

<p>
The development environment focuses on three core activities:
</p>

<ul>
<li>graphical programming using a dataflow diagram editor</li>
<li>user interface design through a front panel editor</li>
<li>visual debugging and program execution</li>
</ul>

<p>
The IDE itself is implemented primarily using modern web technologies, allowing rapid development, portability, and a rich plugin ecosystem.
</p>

<hr>

<h2>High-Level Architecture</h2>

<div align="center">

<pre>

+---------------------------------------------------+
|                     FROG IDE                      |
|                                                   |
|  +---------------------+   +--------------------+ |
|  |   Front Panel       |   |   Diagram Editor   | |
|  |      Editor         |   |    (Graph Editor)  | |
|  |   HTML / SVG / JS   |   |   WebGL / JS       | |
|  +---------------------+   +--------------------+ |
|             |                        |             |
|             +-----------+------------+             |
|                         |                          |
|                  FROG Expression                   |
|                      (.frog JSON)                  |
+-------------------------|--------------------------+
                          |
                          v
                 +--------------------+
                 |    FROG Compiler   |
                 |        Rust        |
                 +--------------------+
                          |
                          v
                 +--------------------+
                 |     FROG Runtime   |
                 |         C          |
                 +--------------------+
                          |
                          v
                       Execution

</pre>

</div>

<hr>

<h2>Main Components</h2>

<h3>IDE Shell</h3>

<p>
The IDE shell is the core application responsible for organizing the development environment and integrating all tools used by developers.
</p>

<p>
It manages the overall layout and user interaction within the IDE.
</p>

<p>
Main responsibilities include:
</p>

<ul>
<li>window and panel management</li>
<li>menus and toolbars</li>
<li>project explorer</li>
<li>file management</li>
<li>plugin infrastructure</li>
<li>integration of editors</li>
</ul>

<p>
The IDE shell is implemented using:
</p>

<ul>
<li><b>JavaScript / TypeScript</b></li>
<li><b>HTML / CSS</b></li>
</ul>

<p>
To run as a desktop application, the IDE is packaged using a desktop container such as:
</p>

<ul>
<li>Tauri</li>
<li>Electron</li>
</ul>

<p>
This approach enables the IDE to run consistently across operating systems while maintaining a modern development workflow.
</p>

<hr>

<h3>Diagram Editor</h3>

<p>
The diagram editor is the graphical programming environment where users construct programs using a dataflow model.
</p>

<p>
Programs are expressed as directed graphs composed of nodes connected by wires that represent data dependencies.
</p>

<p>
Users can:
</p>

<ul>
<li>create and place nodes</li>
<li>connect wires</li>
<li>configure node parameters</li>
<li>organize graph layouts</li>
<li>observe execution behavior</li>
</ul>

<p>
The diagram editor is implemented using:
</p>

<ul>
<li><b>JavaScript / TypeScript</b></li>
<li><b>WebGL GPU rendering</b></li>
</ul>

<p>
Using WebGL enables the editor to render complex graphs efficiently while maintaining smooth interaction.
</p>

<p>
Capabilities include:
</p>

<ul>
<li>smooth zoom and pan</li>
<li>real-time node interaction</li>
<li>execution highlighting</li>
<li>support for very large graphs</li>
<li>GPU accelerated rendering</li>
</ul>

<p>
The diagram engine is designed to scale to thousands of nodes without relying on large DOM structures.
</p>

<hr>

<h3>Front Panel Editor</h3>

<p>
The front panel editor allows the creation of user interfaces associated with FROG programs.
</p>

<p>
The front panel represents the interaction layer between the user and the underlying program logic.
</p>

<p>
Typical UI elements include:
</p>

<ul>
<li>buttons</li>
<li>numeric inputs</li>
<li>indicators</li>
<li>graphs</li>
<li>gauges</li>
<li>visual displays</li>
</ul>

<p>
The front panel editor is implemented using:
</p>

<ul>
<li><b>JavaScript</b></li>
<li><b>HTML</b></li>
<li><b>SVG</b></li>
</ul>

<p>
SVG enables scalable vector-based rendering, allowing user interfaces to remain resolution-independent and visually consistent across devices.
</p>

<p>
This architecture also makes it possible to deploy front panels directly in web environments in the future.
</p>

<hr>

<h3>FROG Expression</h3>

<p>
Programs created in the IDE are stored as structured expressions using a JSON-based format.
</p>

<p>
File extension:
</p>

<pre>
.frog
</pre>

<p>
The expression contains:
</p>

<ul>
<li>diagram definition</li>
<li>node configuration</li>
<li>connections between nodes</li>
<li>front panel layout</li>
</ul>

<p>
The JSON representation is designed to be:
</p>

<ul>
<li>human-readable</li>
<li>version-control friendly</li>
<li>open and transparent</li>
<li>portable across systems</li>
</ul>

<hr>

<h3>Compiler</h3>

<p>
The compiler transforms the FROG expression into an intermediate representation suitable for execution.
</p>

<p>
Responsibilities include:
</p>

<ul>
<li>graph validation</li>
<li>type checking</li>
<li>semantic verification</li>
<li>graph optimization</li>
<li>IR generation</li>
</ul>

<p>
The compiler is implemented in <b>Rust</b>, providing strong safety guarantees and high performance for complex transformations.
</p>

<hr>

<h3>Runtime</h3>

<p>
The runtime is the execution engine responsible for running compiled FROG programs.
</p>

<p>
It implements the dataflow scheduler that controls when nodes are executed and how data moves through the graph.
</p>

<p>
Responsibilities include:
</p>

<ul>
<li>dataflow scheduling</li>
<li>node execution</li>
<li>parallel execution</li>
<li>memory management</li>
<li>debug instrumentation</li>
</ul>

<p>
The runtime is implemented in <b>C</b> to ensure maximum portability and compatibility with embedded environments.
</p>

<p>
This allows the runtime to be deployed on:
</p>

<ul>
<li>desktop systems</li>
<li>embedded devices</li>
<li>real-time systems</li>
<li>hardware interfaces</li>
</ul>

<hr>

<h2>Execution Flow</h2>

<div align="center">

<pre>

Diagram created in IDE
          ↓
      .frog file
          ↓
   Compiler (Rust)
          ↓
Intermediate Representation
          ↓
      Runtime (C)
          ↓
       Execution

</pre>

</div>

<p>
During debugging sessions, the runtime communicates execution events back to the IDE, allowing nodes and wires to be visually highlighted in the diagram editor.
</p>

<hr>

<h2>Design Principles</h2>

<ul>
<li><b>Language independence</b> — the language specification is separate from the IDE</li>
<li><b>Hardware agnostic execution</b></li>
<li><b>Open program representation</b></li>
<li><b>Modular architecture</b></li>
<li><b>GPU accelerated graphical editing</b></li>
<li><b>Cross-platform development</b></li>
</ul>

<hr>

<h2>Future Evolution</h2>

<p>
The architecture of the FROG IDE is designed to evolve as the ecosystem grows.
</p>

<p>
Potential future capabilities include:
</p>

<ul>
<li>plugin architecture</li>
<li>collaborative editing</li>
<li>remote front panels</li>
<li>web-based IDE</li>
<li>hardware-specific toolchains (RT / FPGA)</li>
</ul>

<hr>

<h2>Repository Structure</h2>

<pre>

FROG/
│
├── IDE/
│   ├── ide-shell/
│   ├── diagram-editor/
│   └── front-panel-editor/
│
├── compiler/
│
├── runtime/
│
└── expression/

</pre>

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
