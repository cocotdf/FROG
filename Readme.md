<p align="center">
  <img src="FROG logo.svg" alt="FROG logo" width="150" />
</p>

<h1 align="center">🐸 FROG — Free Open Graphical Language</h1>

<p align="center">
  <strong>Free Open Graphical Dataflow Programming Language</strong><br/>
  An open, hardware-agnostic graphical dataflow language designed for rapid prototyping, deterministic execution, and scalable deployment across heterogeneous hardware.
</p>

<p align="center">
  <a href="#what-is-frog">What is FROG?</a> •
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
FROG is an open, hardware-agnostic <strong>graphical dataflow programming language</strong>
designed to describe computation through explicit dataflow graphs.
</p>

<p>
Instead of expressing programs as ordered sequences of instructions,
FROG represents programs as <strong>graphs of operations connected by data</strong>.
Execution emerges from the availability and movement of data through the system.
</p>

<p>
FROG defines an open standard for describing computation as
<strong>executable dataflow graphs</strong> composed of nodes, connections,
types, interfaces, interaction layers, and execution-oriented lowering rules.
</p>

<p>
The language is designed to remain independent from any particular
IDE, compiler, runtime, operating system, or vendor ecosystem.
</p>

<p>
This separation enables long-term stability, interoperability,
multiple independent implementations, and a durable foundation
for industrial graphical programming.
</p>

<hr/>

<h2 id="why-frog-exists">Why FROG exists</h2>

<p>
Graphical dataflow programming has demonstrated major advantages
for building complex systems:
</p>

<ul>
  <li>natural parallelism</li>
  <li>deterministic execution</li>
  <li>intuitive system orchestration</li>
  <li>strong mapping between software and hardware behavior</li>
  <li>high productivity for engineers and scientists</li>
</ul>

<p>
However, most graphical dataflow environments have historically been
tightly coupled to proprietary ecosystems where the language,
runtime, hardware support, and development environment are inseparable.
</p>

<p>
This limits portability, slows innovation,
prevents independent implementations of the same language,
and often locks users into a single vendor boundary.
</p>

<p>
FROG addresses this limitation by defining an <strong>open language specification</strong>
separate from any single tool, runtime, compiler, or hardware manufacturer.
</p>

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
In traditional programming languages, programs are executed
as ordered sequences of instructions.
</p>

<p>
In dataflow programming, operations execute automatically when their
required input data becomes available.
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
Execution order therefore emerges from data dependencies
rather than being manually sequenced.
</p>

<p>
This model enables:
</p>

<ul>
  <li>automatic parallel execution</li>
  <li>deterministic behavior</li>
  <li>efficient use of modern hardware</li>
  <li>clear representation of system logic</li>
</ul>

<hr/>

<h2 id="from-prototyping-to-critical-systems">From prototyping to critical systems</h2>

<p>
FROG is designed to combine two goals that are often treated as contradictory
in programming languages.
</p>

<ul>
  <li>extreme accessibility for rapid prototyping</li>
  <li>high execution performance for demanding systems</li>
</ul>

<p>
Graphical programming lowers the barrier to entry by allowing systems
to be expressed visually as dataflow graphs,
reducing the cognitive overhead of syntax-driven programming.
</p>

<p>
This makes rapid prototyping more accessible to engineers,
scientists, researchers, and system designers.
</p>

<p>
At the same time, accessibility must not come at the cost of efficiency.
</p>

<p>
Through a dedicated execution representation and compilation pipeline,
FROG is designed to support deep optimization of dataflow graphs,
allowing programs to scale from simple experiments
to deterministic and high-performance systems.
</p>

<p>
The same programming model can therefore support:
</p>

<ul>
  <li>rapid experimentation</li>
  <li>scientific computing</li>
  <li>industrial automation</li>
  <li>embedded systems</li>
  <li>microcontroller-based systems</li>
  <li>real-time control</li>
  <li>edge AI and accelerated computing</li>
  <li>high-performance computing</li>
  <li>safety-critical and resource-constrained systems</li>
</ul>

<p>
FROG aims to provide a unified programming model where
<strong>usability, performance, portability, and determinism coexist rather than compete</strong>.
</p>

<p>
Its ambition is to contribute to a significant evolution in the design
of programming languages by combining graphical programming,
dataflow execution, modern compiler architectures, and an open industrial ecosystem.
</p>

<hr/>

<h2 id="core-concept-diagram-and-front-panel">Core concept: Diagram and Front Panel</h2>

<p>
Every FROG program combines two complementary layers.
</p>

<h3>Diagram — the executable dataflow graph</h3>

<p>
The diagram defines the program logic as a directed dataflow graph composed of:
</p>

<ul>
  <li>nodes representing operations</li>
  <li>edges representing data connections</li>
  <li>typed ports defining valid data exchange</li>
  <li>execution metadata describing execution-related constraints</li>
  <li>structured annotations and documentation</li>
</ul>

<p>
Execution is derived exclusively from the graph structure
and the availability of data.
</p>

<h3>Front Panel — the interaction layer</h3>

<p>
The front panel defines the user-facing interaction layer of the program.
</p>

<ul>
  <li>controls providing inputs</li>
  <li>indicators exposing outputs</li>
  <li>widgets representing system state</li>
  <li>layout and graphical properties</li>
  <li>explicit typed bindings to the executable graph</li>
</ul>

<p>
Front panel elements follow a structured widget model rather than a purely visual ad hoc model.
</p>

<p>
These interface elements are connected to the diagram through explicit,
typed bindings.
</p>

<hr/>

<h2 id="program-representation">Program representation</h2>

<p>
FROG programs exist across three distinct representation levels.
</p>

<h3>FROG Expression</h3>

<p>
The <strong>FROG Expression</strong> is the serialized source representation
stored in a <code>.frog</code> file.
</p>

<p>
It is the canonical source form of a FROG program.
</p>

<p>
It may contain:
</p>

<ul>
  <li>diagram definition</li>
  <li>front panel definition</li>
  <li>interface definitions</li>
  <li>widget definitions and widget bindings</li>
  <li>icon and metadata sections</li>
  <li>IDE-related preferences</li>
  <li>other source-level program sections defined by the specification</li>
</ul>

<p>
The Expression is designed for:
</p>

<ul>
  <li>human readability</li>
  <li>version control compatibility</li>
  <li>tool interoperability</li>
  <li>long-term durability</li>
</ul>

<h3>FROG Program Model</h3>

<p>
The <strong>FROG Program Model</strong> is the canonical editable in-memory representation
used by development tools.
</p>

<p>
It is reconstructed from the FROG Expression when a program is loaded,
and it is continuously updated while the user edits the diagram or front panel.
</p>

<p>
The Program Model exists for authoring, synchronization, validation,
and preparation for execution-oriented processing.
</p>

<h3>FROG Execution IR</h3>

<p>
The <strong>FROG Execution IR</strong> is the canonical execution-oriented representation
derived from the validated Program Model.
</p>

<p>
It contains the information required for execution-related workflows such as:
</p>

<ul>
  <li>resolved operations and nodes</li>
  <li>validated data connections</li>
  <li>normalized type information</li>
  <li>execution constraints</li>
  <li>scheduling metadata</li>
  <li>compiler preparation data</li>
  <li>target-specific lowering metadata</li>
</ul>

<p>
Programs are not executed directly from the Expression.
Execution occurs from source-derived, validated execution representations.
</p>

<p>
Optional cache files may store derived execution data such as cached Execution IR,
but cache content is always non-authoritative.
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
 CPU / RT / GPU / FPGA / Embedded ARM / MCU / Industrial Edge
</pre>

<p>
During development, tools maintain the <strong>FROG Program Model</strong>.
Saving a program serializes that model into the canonical
<strong>FROG Expression</strong>.
</p>

<p>
When execution is requested, the validated Program Model is lowered into the
<strong>FROG Execution IR</strong>, which is then used by compilers, backends, and runtimes.
</p>

<hr/>

<h2 id="hardware-agnostic-execution">Hardware-agnostic execution</h2>

<p>
FROG programs are designed to run across multiple hardware classes without changing
their source-level programming model.
</p>

<p>
The language is not tied to one processor family, one operating system,
one runtime architecture, or one hardware vendor.
</p>

<p>
Representative target classes include:
</p>

<ul>
  <li><strong>General-purpose CPUs</strong> — workstation, server, and industrial PC execution</li>
  <li><strong>Real-time targets</strong> — deterministic control and measurement systems</li>
  <li><strong>Embedded ARM systems</strong> — edge devices, gateways, and accelerated embedded platforms</li>
  <li><strong>GPUs</strong> — parallel and accelerated compute targets</li>
  <li><strong>FPGAs</strong> — programmable logic targets</li>
  <li><strong>Microcontrollers</strong> — resource-constrained embedded execution</li>
  <li><strong>Industrial edge controllers</strong> — vendor-specific acquisition, control, and automation platforms</li>
</ul>

<p>
Possible execution profiles may include:
</p>

<ul>
  <li><strong>FROG Core</strong> — general-purpose systems</li>
  <li><strong>FROG RT</strong> — deterministic real-time execution</li>
  <li><strong>FROG FPGA</strong> — programmable logic targets</li>
  <li><strong>FROG Embedded</strong> — embedded ARM and edge systems</li>
  <li><strong>FROG MCU</strong> — microcontroller-oriented subsets and constrained runtimes</li>
  <li><strong>FROG Accelerated</strong> — heterogeneous or accelerated execution profiles</li>
</ul>

<p>
The diagram and front panel remain conceptually consistent across targets.
What changes is the runtime profile, compilation strategy, backend capabilities, and available platform services.
</p>

<hr/>

<h2 id="open-industrial-hardware-standard">Open industrial hardware standard</h2>

<p>
FROG is intended to be more than a language that happens to support multiple targets.
Its long-term goal is to provide an <strong>open industrial graphical programming standard</strong>.
</p>

<p>
This means that any hardware manufacturer should be able to implement support for FROG on its own platforms without requiring permission from a single controlling vendor.
</p>

<p>
In practical terms, this may include:
</p>

<ul>
  <li>FROG-compatible runtimes</li>
  <li>target-specific compilers or backends</li>
  <li>driver-backed hardware libraries exposed as FROG nodes</li>
  <li>platform profiles for determinism, memory, timing, and deployment constraints</li>
  <li>vendor-certified toolchains and support layers</li>
</ul>

<p>
The goal is to make it possible for ecosystems built around NVIDIA Jetson, industrial ARM systems, microcontrollers, FPGA-based platforms, or hardware vendors such as UEI, ADLINK, Gantner, Advantech, and others to support the same core graphical language model.
</p>

<p>
FROG therefore aims to do in an open way what proprietary ecosystems only achieved within their own hardware boundaries:
provide a common programming model across heterogeneous industrial targets without locking users into a single manufacturer.
</p>

<hr/>

<h2 id="security-and-optimization">Security and optimization by design</h2>

<p>
FROG integrates validation and optimization directly into its architecture.
</p>

<ul>
  <li>strict type validation</li>
  <li>graph verification before execution</li>
  <li>controlled execution boundaries</li>
  <li>optional sandboxed runtime environments</li>
  <li>deterministic execution guarantees where supported by the active profile</li>
</ul>

<p>
Optimization is performed at the Execution IR and compilation levels:
</p>

<ul>
  <li>graph simplification</li>
  <li>dead node elimination</li>
  <li>constant folding</li>
  <li>memory reuse optimization</li>
  <li>automatic parallel scheduling</li>
  <li>target-specific optimizations</li>
  <li>profile-aware lowering for constrained or deterministic targets</li>
</ul>

<hr/>

<h2 id="interoperability">Interoperability</h2>

<p>
FROG is designed to integrate with external languages
through stable ABI-based interfaces and compatible toolchains.
</p>

<ul>
  <li>C / C++</li>
  <li>Rust</li>
  <li>Python</li>
  <li>.NET</li>
  <li>other languages via compatible ABI bindings</li>
</ul>

<p>
External functions can be exposed as nodes in the dataflow graph
while preserving type safety and execution guarantees.
</p>

<p>
This interoperability is also essential for hardware support,
because vendor-specific drivers, low-level APIs, RT frameworks,
FPGA toolflows, and embedded SDKs can be integrated through open bindings
rather than through a closed monolithic environment.
</p>

<hr/>

<h2 id="separation-of-language-and-tooling">Separation of language and tooling</h2>

<p>
FROG explicitly separates:
</p>

<ul>
  <li>the language specification</li>
  <li>the serialized source representation</li>
  <li>the editable program model</li>
  <li>the execution-oriented representation</li>
  <li>compiler implementations</li>
  <li>backend implementations</li>
  <li>runtime implementations</li>
  <li>development environments</li>
  <li>hardware adaptation layers</li>
</ul>

<p>
This architecture enables:
</p>

<ul>
  <li>multiple IDE implementations</li>
  <li>multiple compilers</li>
  <li>multiple backends</li>
  <li>multiple runtimes</li>
  <li>multiple hardware vendors to support the same language</li>
  <li>independent ecosystem evolution</li>
</ul>

<p>
The specification defines the language, not a specific product or implementation.
</p>

<hr/>

<h2 id="project-status">Project status</h2>

<p>
FROG is currently in early development.
The language specification, program representation model,
execution architecture, widget model, diagram/front-panel semantics,
and reference tooling are under active design.
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

<p align="center">
<a href="https://cla-assistant.io/Graiphic/FROG">
<img src="https://cla-assistant.io/readme/badge/Graiphic/FROG" alt="CLA Assistant"/>
</a>
</p>
