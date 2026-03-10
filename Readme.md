<p align="center">
  <img src="FROG logo.svg" alt="FROG logo" width="150" />
</p>

<h1 align="center">🐸 FROG — Free Open Graphical Language</h1>

<p align="center">
  <strong>Free Open Graphical Dataflow Programming Language</strong><br/>
  FROG is an open, hardware-agnostic graphical dataflow programming language designed to describe computation as executable dataflow graphs.  
  It aims to combine accessibility, rapid prototyping, deterministic execution, and scalable deployment across heterogeneous hardware while enabling an open ecosystem around a shared graphical programming standard.
</p>

<p align="center">
  <a href="#what-is-frog">What is FROG?</a> •
  <a href="#positioning">Positioning</a> •
  <a href="#breaking-the-syntax-first-bottleneck">Breaking the syntax-first bottleneck</a> •
  <a href="#why-frog-exists">Why FROG exists</a> •
  <a href="#dataflow-programming">Dataflow programming</a> •
  <a href="#from-prototyping-to-critical-systems">From prototyping to critical systems</a> •
  <a href="#core-concept-diagram-and-front-panel">Core concept</a> •
  <a href="#program-representation">Program representation</a> •
  <a href="#execution-architecture">Execution architecture</a> •
  <a href="#hardware-agnostic-execution">Execution targets</a> •
  <a href="#open-industrial-hardware-standard">Open industrial hardware standard</a> •
  <a href="#security-and-optimization">Security & Optimization</a> •
  <a href="#interoperability">Interoperability</a> •
  <a href="#separation-of-language-and-tooling">Language separation</a> •
  <a href="#project-status">Status</a> •
  <a href="#license">License</a>
</p>

<hr/>

<h2 id="what-is-frog">What is FROG?</h2>

<p>
FROG is an open <strong>graphical dataflow programming language</strong> designed to represent computation as explicit dataflow graphs.
</p>

<p>
Instead of expressing programs as ordered sequences of instructions,  
FROG represents programs as <strong>graphs of operations connected by data dependencies</strong>.
Execution emerges from the availability of data rather than from manually written control flow.
</p>

<p>
The language defines a standard way to describe programs as:
</p>

<ul>
<li>typed nodes representing operations</li>
<li>typed ports representing data exchange</li>
<li>explicit dataflow connections</li>
<li>structured execution constructs</li>
<li>interaction layers for user interfaces</li>
</ul>

<p>
FROG is designed to remain independent from any specific IDE, compiler, runtime, operating system, or hardware vendor.
</p>

<p>
This separation allows multiple independent implementations and enables a durable, interoperable graphical programming ecosystem.
</p>

<hr/>

<h2 id="positioning">Positioning</h2>

<p>
FROG aims to combine the accessibility of graphical programming with the execution depth required for deterministic and industrial systems.
</p>

<p>
Many programming environments force a trade-off between ease of expression and execution control.
FROG aims to reduce that trade-off by combining:
</p>

<ul>
<li>visual system representation</li>
<li>explicit dataflow execution</li>
<li>typed interfaces</li>
<li>deterministic behavior</li>
<li>scalable compilation pipelines</li>
</ul>

<p align="center">
  <img src="frog-orville-chart.png" alt="FROG positioning chart" width="640" />
</p>

<p align="center">
  <em>
    FROG aims to combine accessibility, visual programming, and system-grade execution.
  </em>
</p>

<hr/>

<h2 id="breaking-the-syntax-first-bottleneck">Breaking the syntax-first bottleneck</h2>

<p>
In many traditional programming environments, developers must first master syntax,
language conventions, and structural patterns before they can effectively explore system ideas.
</p>

<p>
This often leads to an inversion of the design process.
Instead of asking:
</p>

<p><strong>“What system should I build?”</strong></p>

<p>
developers frequently ask:
</p>

<p><strong>“What can I build with the language constructs I already master?”</strong></p>

<p>
This constraint slows experimentation and makes complex systems harder to explore early in the design process.
</p>

<p>
FROG reduces this barrier by emphasizing:
</p>

<ul>
<li>visual system representation</li>
<li>explicit data movement</li>
<li>typed interfaces</li>
<li>clear execution semantics</li>
</ul>

<p>
The objective is not to remove complexity from engineering,
but to shift developer effort from syntax mechanics toward system architecture and behavior.
</p>

<hr/>

<h2 id="why-frog-exists">Why FROG exists</h2>

<p>
Graphical dataflow programming has demonstrated strong advantages in many domains:
</p>

<ul>
<li>natural parallelism</li>
<li>deterministic execution</li>
<li>clear system orchestration</li>
<li>strong mapping between software and hardware behavior</li>
<li>high productivity for engineers and scientists</li>
</ul>

<p>
However, most existing graphical environments have historically been tied to proprietary ecosystems
where the language, runtime, IDE, and hardware platform are tightly coupled.
</p>

<p>
This limits portability, slows ecosystem growth, and prevents independent implementations.
</p>

<p>
FROG addresses this limitation by defining an <strong>open language specification</strong> independent from any specific product or vendor.
</p>

<p>
<strong>FROG is not an IDE.</strong><br/>
<strong>FROG is not a single runtime.</strong><br/>
<strong>FROG is not a vendor platform.</strong><br/>
<strong>FROG is a language specification.</strong>
</p>

<hr/>

<h2 id="dataflow-programming">Dataflow programming</h2>

<p>
FROG follows a true <strong>dataflow execution model</strong>.
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
Operations execute automatically when their required input data becomes available.
</p>

<p>
Execution order therefore emerges from data dependencies.
</p>

<p>
This enables:
</p>

<ul>
<li>automatic parallelism</li>
<li>deterministic execution</li>
<li>clear system behavior</li>
<li>efficient hardware utilization</li>
</ul>

<hr/>

<h2 id="from-prototyping-to-critical-systems">From prototyping to critical systems</h2>

<p>
FROG is designed to support both rapid experimentation and demanding system deployment.
</p>

<p>
The same programming model can scale across domains including:
</p>

<ul>
<li>scientific computing</li>
<li>industrial automation</li>
<li>measurement and control</li>
<li>embedded systems</li>
<li>real-time control</li>
<li>edge computing</li>
<li>accelerated computing</li>
<li>high-performance computing</li>
</ul>

<p>
Accessibility and execution performance are treated as complementary goals rather than competing ones.
</p>

<hr/>

<h2 id="core-concept-diagram-and-front-panel">Core concept: Diagram and Front Panel</h2>

<p>
A FROG program combines two complementary layers.
</p>

<h3>Diagram — the executable dataflow graph</h3>

<p>
The diagram defines program logic as a directed dataflow graph composed of:
</p>

<ul>
<li>nodes representing operations</li>
<li>typed input and output ports</li>
<li>connections representing data dependencies</li>
<li>structured control constructs</li>
</ul>

<p>
Execution semantics derive entirely from the graph structure and data availability.
</p>

<h3>Front Panel — the interaction layer</h3>

<p>
The front panel defines the user interaction layer of the program.
</p>

<ul>
<li>controls providing inputs</li>
<li>indicators exposing outputs</li>
<li>widgets representing state and interaction</li>
<li>layout and presentation information</li>
</ul>

<p>
Front panel elements are structured widgets.
A widget may expose its primary value directly to the diagram through dedicated diagram nodes.
</p>

<p>
The diagram remains the authoritative execution graph.
</p>

<hr/>

<h2 id="program-representation">Program representation</h2>

<p>
FROG programs exist across three representation levels.
</p>

<h3>FROG Expression</h3>

<p>
The <strong>FROG Expression</strong> is the serialized source representation stored in a <code>.frog</code> file.
</p>

<p>
It is the canonical source form of a program.
</p>

<p>
Typical sections include:
</p>

<ul>
<li>diagram definition</li>
<li>front panel definition</li>
<li>interface definition</li>
<li>widget descriptions</li>
<li>metadata and icons</li>
<li>IDE-interpreted preferences</li>
</ul>

<p>
The Expression is designed for readability, version control compatibility, and long-term durability.
</p>

<h3>FROG Program Model</h3>

<p>
The <strong>FROG Program Model</strong> is the editable in-memory representation used by development tools.
</p>

<p>
It is reconstructed from the Expression and maintained during editing.
</p>

<h3>FROG Execution IR</h3>

<p>
The <strong>FROG Execution IR</strong> is the execution-oriented representation derived from the validated Program Model.
</p>

<p>
It contains normalized structures required for execution, scheduling, optimization, and compilation.
</p>

<p>
Programs are not executed directly from the Expression.
Execution occurs from validated execution representations.
</p>

<hr/>

<h2 id="execution-architecture">Execution architecture</h2>

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
    (.frog source)               |
                                 v
                       FROG Execution IR
                    (execution-oriented form)
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

<hr/>

<h2 id="hardware-agnostic-execution">Hardware-agnostic execution</h2>

<p>
FROG programs are designed to execute across multiple hardware classes.
</p>

<ul>
<li>general-purpose CPUs</li>
<li>real-time systems</li>
<li>embedded ARM devices</li>
<li>GPUs</li>
<li>FPGAs</li>
<li>microcontrollers</li>
<li>industrial edge controllers</li>
</ul>

<p>
Execution targets may implement specialized profiles such as:
</p>

<ul>
<li>FROG Core</li>
<li>FROG RT</li>
<li>FROG FPGA</li>
<li>FROG Embedded</li>
<li>FROG MCU</li>
<li>FROG Accelerated</li>
</ul>

<hr/>

<h2 id="open-industrial-hardware-standard">Open industrial hardware standard</h2>

<p>
FROG aims to enable an open ecosystem where hardware manufacturers and software vendors
can build integrated platforms around a shared graphical language.
</p>

<p>
Possible ecosystem components include:
</p>

<ul>
<li>FROG runtimes</li>
<li>hardware-specific compilers</li>
<li>vendor libraries exposed as nodes</li>
<li>deployment platforms</li>
<li>target-specific execution profiles</li>
</ul>

<p>
This allows hardware-software integration without requiring a proprietary language boundary.
</p>

<hr/>

<h2 id="security-and-optimization">Security and optimization</h2>

<ul>
<li>strict type validation</li>
<li>graph verification before execution</li>
<li>controlled execution boundaries</li>
<li>deterministic execution where supported</li>
</ul>

<p>
Optimization occurs primarily at the Execution IR and compilation levels:
</p>

<ul>
<li>dead node elimination</li>
<li>constant propagation</li>
<li>parallel scheduling</li>
<li>memory optimization</li>
<li>target-specific lowering</li>
</ul>

<hr/>

<h2 id="interoperability">Interoperability</h2>

<p>
FROG integrates with external languages through stable ABI interfaces.
</p>

<ul>
<li>C / C++</li>
<li>Rust</li>
<li>Python</li>
<li>.NET</li>
</ul>

<p>
External functions can be exposed as nodes in the dataflow graph while preserving type safety.
</p>

<hr/>

<h2 id="separation-of-language-and-tooling">Language separation</h2>

<p>
FROG explicitly separates:
</p>

<ul>
<li>language specification</li>
<li>serialized program representation</li>
<li>editable program model</li>
<li>execution representation</li>
<li>compiler implementations</li>
<li>runtime implementations</li>
<li>development environments</li>
</ul>

<p>
This separation enables multiple independent ecosystems to implement the language.
</p>

<hr/>

<h2 id="project-status">Project status</h2>

<p>
FROG is currently under active design.
The language specification and program architecture are evolving.
</p>

<p>
Feedback, discussions, and contributions are welcome.
</p>

<hr/>

<h2 id="license">License</h2>

<p>
This project is licensed under the <strong>Apache License 2.0</strong>.
See <code>LICENSE</code> for details.
</p>

<p align="center">
  <a href="https://cla-assistant.io/Graiphic/FROG">
    <img src="https://cla-assistant.io/readme/badge/Graiphic/FROG" alt="CLA Assistant" />
  </a>
</p>
