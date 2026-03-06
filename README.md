<p align="center">
  <img src="FROG logo.png" alt="FROG logo" width="400" />
</p>

<h1 align="center">🐸 FROG — Free Open Graphical Language</h1>

<p align="center">
  <strong>Free Open Graphical Language</strong><br/>
  An open, hardware-agnostic graphical dataflow language and execution model.
</p>

<p align="center">
  <a href="#what-is-frog">What is FROG?</a> •
  <a href="#why-frog-exists">Why FROG exists</a> •
  <a href="#core-concept-diagram-and-front-panel">Core concept</a> •
  <a href="#program-representation">Program representation</a> •
  <a href="#execution-architecture">Execution architecture</a> •
  <a href="#hardware-agnostic-execution">Execution targets</a> •
  <a href="#security-and-optimization">Security & Optimization</a> •
  <a href="#interoperability">Interoperability</a> •
  <a href="#project-status">Status</a> •
  <a href="#license">License</a>
</p>

<hr/>

<h2 id="what-is-frog">What is FROG?</h2>

<p>
FROG is an open, hardware-agnostic graphical dataflow language designed to orchestrate computation through explicit graph execution.
</p>

<p>
It is built on a simple principle:
<strong>the language must be independent of its tools, its runtime, and any single vendor.</strong>
</p>

<p>
FROG defines an open standard for expressing programs as executable dataflow graphs. These graphs describe the flow of data, the operations applied to it, and the interface used to observe and control execution.
</p>

<p>
A FROG program is composed of two fundamental and complementary parts:
</p>

<ul>
<li><strong>the diagram</strong>, which defines the executable dataflow graph</li>
<li><strong>the front panel</strong>, which defines the user interface and interaction layer</li>
</ul>

<p>
Programs are not opaque binaries. They are structured, readable, and fully open expressions stored in a canonical representation.
</p>

<hr/>

<h2 id="why-frog-exists">Why FROG exists</h2>

<p>
Graphical dataflow programming has demonstrated unique advantages:
</p>

<ul>
<li>natural parallelism</li>
<li>deterministic execution</li>
<li>intuitive system orchestration</li>
<li>direct mapping to hardware</li>
</ul>

<p>
However, existing implementations have historically coupled the language, runtime, and development environment into a single proprietary ecosystem.
</p>

<p>
This prevents independent implementations, limits portability, and ties the evolution of the language to a single vendor.
</p>

<p>
FROG removes this limitation.
</p>

<p>
<strong>FROG is not an IDE.</strong><br/>
<strong>FROG is not a product.</strong><br/>
<strong>FROG is a language specification.</strong>
</p>

<hr/>

<h2 id="core-concept-diagram-and-front-panel">Core concept: Diagram and Front Panel</h2>

<p>
Every FROG program is defined by the explicit association of two layers.
</p>

<h3>Diagram: the executable graph</h3>

<p>
The diagram defines the executable logic as a directed dataflow graph composed of:
</p>

<ul>
<li>nodes representing operations</li>
<li>edges representing data connections</li>
<li>typed ports defining valid data exchange</li>
<li>execution metadata describing execution behavior</li>
</ul>

<p>
The diagram is the authoritative definition of computation.  
Execution is derived exclusively from the graph structure and the availability of data.
</p>

<h3>Front Panel: the interaction layer</h3>

<p>
The front panel defines the user interface and interaction surface, composed of:
</p>

<ul>
<li>controls providing inputs to the diagram</li>
<li>indicators exposing outputs from the diagram</li>
<li>visual components representing system state</li>
<li>layout and graphical properties</li>
</ul>

<p>
Front panel graphical elements follow <strong>SVG semantics</strong> for vector definition, layout, and rendering.
</p>

<p>
SVG is used as a graphical description model embedded within the program expression.  
It does not act as a separate container for the program.
</p>

<p>
The front panel connects to the diagram through explicit typed bindings ensuring full consistency between user interaction and execution logic.
</p>

<hr/>

<h2 id="program-representation">Program representation</h2>

<p>
FROG programs exist in two complementary representations.
</p>

<h3>FROG IR — Intermediate Representation</h3>

<p>
The <strong>FROG IR</strong> is the canonical internal representation of a program.
</p>

<p>
It describes the executable graph including:
</p>

<ul>
<li>nodes and operations</li>
<li>data connections</li>
<li>type information</li>
<li>execution constraints</li>
<li>scheduling metadata</li>
</ul>

<p>
The IR is the representation used by compilers, analyzers, and runtimes.
</p>

<h3>FROG Expression — Canonical program format</h3>

<p>
The <strong>FROG Expression</strong> is the serialized representation of the program.
</p>

<p>
It contains:
</p>

<ul>
<li>the diagram definition</li>
<li>the front panel definition</li>
<li>embedded SVG elements</li>
<li>type system definitions</li>
<li>program metadata</li>
</ul>

<p>
The expression is designed for:
</p>

<ul>
<li>human readability</li>
<li>version control compatibility</li>
<li>tool interoperability</li>
<li>long-term program durability</li>
</ul>

<p>
The expression is not executed directly.  
Execution always occurs through the validated intermediate representation.
</p>

<hr/>

<h2 id="execution-architecture">Execution architecture</h2>

<p>
FROG defines a clear execution pipeline separating editing, representation, and compilation.
</p>

<pre>
                FROG IDE
               /        \
              /          \
             ↓            ↓
   FROG Expression     FROG IR
     (storage)      (execution graph)
              \          /
               \        /
                ↓      ↓
               Compiler(s)
                    ↓
             Target runtime
                    ↓
     CPU / RT / FPGA / GPU / Embedded
</pre>

<p>
During development, the IDE constructs and maintains the FROG IR directly as the user edits the diagram.
</p>

<p>
Saving a program serializes the IR into the canonical program expression.
</p>

<p>
Compilers operate exclusively on the validated IR.
</p>

<hr/>

<h2 id="hardware-agnostic-execution">Hardware-agnostic execution</h2>

<p>
FROG programs are designed to execute across multiple targets without modification.
</p>

<p>
The language supports several execution profiles:
</p>

<ul>
<li><strong>FROG Core</strong> — general purpose systems</li>
<li><strong>FROG RT</strong> — deterministic real-time execution</li>
<li><strong>FROG FPGA</strong> — compilation targeting programmable logic</li>
</ul>

<p>
The diagram and front panel remain identical across targets.
Only the compiler and runtime change.
</p>

<hr/>

<h2 id="security-and-optimization">Security and optimization by design</h2>

<p>
Security and optimization are integral parts of the FROG architecture.
</p>

<p><strong>FROG enforces:</strong></p>

<ul>
<li>strict type validation</li>
<li>graph validation before execution</li>
<li>controlled execution boundaries</li>
<li>optional sandboxed runtimes</li>
<li>deterministic and auditable execution</li>
</ul>

<p><strong>Optimization occurs at the IR and compilation levels and includes:</strong></p>

<ul>
<li>graph simplification</li>
<li>dead node elimination</li>
<li>constant folding</li>
<li>memory reuse and allocation optimization</li>
<li>automatic parallel scheduling</li>
<li>target-specific optimizations</li>
</ul>

<hr/>

<h2 id="interoperability">Interoperability</h2>

<p>
FROG supports integration with external languages through stable interfaces.
</p>

<p><strong>Supported interoperability includes:</strong></p>

<ul>
<li>C and C++</li>
<li>Rust</li>
<li>Python</li>
<li>.NET</li>
<li>other languages through stable ABI interfaces</li>
</ul>

<p>
External functions can be exposed as nodes within the dataflow graph while preserving execution safety and type consistency.
</p>

<hr/>

<h2>Separation of language and tooling</h2>

<p>
FROG explicitly separates:
</p>

<ul>
<li>the language specification</li>
<li>the intermediate representation</li>
<li>the runtime implementations</li>
<li>the development environments</li>
</ul>

<p>
This separation enables:
</p>

<ul>
<li>multiple IDE implementations</li>
<li>multiple runtimes</li>
<li>multiple compilers</li>
<li>independent ecosystem evolution</li>
</ul>

<p>
No single implementation defines the language.  
The specification defines the language.
</p>

<hr/>

<h2>Deterministic dataflow execution</h2>

<p>
FROG follows a true dataflow execution model.
</p>

<p>
Nodes execute when their inputs become available.
</p>

<p><strong>This enables:</strong></p>

<ul>
<li>parallel execution by default</li>
<li>deterministic behavior</li>
<li>efficient hardware utilization</li>
<li>scalable performance</li>
</ul>

<p>
Execution is driven by data availability rather than instruction order.
</p>

<hr/>

<h2>Open by design</h2>

<p>
FROG is fully open and openly specified.
</p>

<p><strong>This guarantees:</strong></p>

<ul>
<li>vendor independence</li>
<li>long-term stability</li>
<li>transparent execution</li>
<li>community-driven evolution</li>
</ul>

<p>
Anyone can implement the language.  
Anyone can build tools, runtimes, or compilers.
</p>

<hr/>

<h2 id="project-status">Project status</h2>

<p>
FROG is currently in early development.  
The language specification, intermediate representation, and reference tooling are under active design.
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
