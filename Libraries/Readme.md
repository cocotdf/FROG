<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="150" />
</p>

<h1 align="center">🐸 FROG Libraries</h1>

<p align="center">
  Standard primitive library specifications for <strong>FROG</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope-of-this-directory">2. Scope of this Directory</a></li>
  <li><a href="#role-of-libraries-in-frog">3. Role of Libraries in FROG</a></li>
  <li><a href="#current-documents">4. Current Documents</a></li>
  <li><a href="#relation-with-other-specifications">5. Relation with Other Specifications</a></li>
  <li><a href="#naming-and-namespaces">6. Naming and Namespaces</a></li>
  <li><a href="#library-evolution">7. Library Evolution</a></li>
  <li><a href="#status">8. Status</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory contains the standard primitive library specifications used by FROG programs.
</p>

<p>
In FROG, the executable <code>diagram</code> is composed of graph nodes.
Some of those nodes are <code>primitive</code> nodes whose meaning is defined by a standardized library catalog.
This directory is where those library catalogs are specified.
</p>

<p>
In other words:
</p>

<ul>
  <li><code>Expression/</code> defines the canonical source structure of a FROG,</li>
  <li><code>Libraries/</code> defines standardized primitive vocabularies used inside executable diagrams.</li>
</ul>

<hr/>

<h2 id="scope-of-this-directory">2. Scope of this Directory</h2>

<p>
This directory specifies library-level primitive catalogs.
It defines what standardized primitives exist, how they are named, what ports they expose, and what semantics they carry.
</p>

<p>
This directory does not redefine:
</p>

<ul>
  <li>the canonical <code>.frog</code> source structure,</li>
  <li>the general diagram graph model,</li>
  <li>the type system,</li>
  <li>the widget object model,</li>
  <li>the IDE architecture.</li>
</ul>

<p>
Those concerns are defined elsewhere in the repository.
</p>

<hr/>

<h2 id="role-of-libraries-in-frog">3. Role of Libraries in FROG</h2>

<p>
A primitive library provides the standardized executable vocabulary used by diagram nodes of kind <code>primitive</code>.
</p>

<p>
For example, a diagram may contain nodes such as:
</p>

<pre><code>{
  "id": "add_1",
  "kind": "primitive",
  "type": "frog.core.add"
}</code></pre>

<p>
The meaning of <code>frog.core.add</code> is not defined directly in the diagram file itself.
It is defined by the appropriate library specification in this directory.
</p>

<p>
This separation is important because it keeps:
</p>

<ul>
  <li>graph structure,</li>
  <li>type rules,</li>
  <li>library semantics</li>
</ul>

<p>
as distinct specification responsibilities.
</p>

<hr/>

<h2 id="current-documents">4. Current Documents</h2>

<p>
This directory currently contains:
</p>

<ul>
  <li><code>Core.md</code> — the minimal standard <code>frog.core</code> library for FROG v0.1.</li>
</ul>

<p>
The <code>frog.core</code> library is the foundational built-in primitive set of the language.
It defines the smallest standard primitive vocabulary expected to exist in conforming FROG implementations.
</p>

<p>
At the current repository stage, <code>Core.md</code> is the only library specification in this directory.
Future revisions MAY add additional library specifications in sibling documents.
</p>

<hr/>

<h2 id="relation-with-other-specifications">5. Relation with Other Specifications</h2>

<p>
Library specifications in this directory are used together with the rest of the FROG specification.
In particular:
</p>

<ul>
  <li><code>Expression/Diagram.md</code> defines how primitives appear as executable graph nodes,</li>
  <li><code>Expression/Type.md</code> defines type syntax, compatibility, and coercion rules used by primitive ports,</li>
  <li><code>Expression/Control structures.md</code> defines language structures, which remain distinct from ordinary primitive functions,</li>
  <li><code>Expression/State and cycles.md</code> defines explicit local memory and cycle-validity rules that constrain stateful primitives such as <code>frog.core.delay</code>.</li>
</ul>

<p>
Accordingly, a primitive library specification is not a replacement for the diagram specification.
It is one normative input used to interpret primitive nodes inside a validated executable graph.
</p>

<hr/>

<h2 id="naming-and-namespaces">6. Naming and Namespaces</h2>

<p>
FROG library primitives use stable namespace-qualified identifiers.
The general naming pattern is:
</p>

<pre><code>frog.&lt;library&gt;.&lt;primitive&gt;</code></pre>

<p>
Examples:
</p>

<ul>
  <li><code>frog.core.add</code></li>
  <li><code>frog.core.mul</code></li>
  <li><code>frog.core.select</code></li>
  <li><code>frog.core.delay</code></li>
</ul>

<p>
This naming model keeps primitive identity explicit and portable across tools, runtimes, and implementations.
</p>

<hr/>

<h2 id="library-evolution">7. Library Evolution</h2>

<p>
The current repository defines only the minimal standard core primitive library.
This is intentional.
</p>

<p>
FROG v0.1 prioritizes a compact and durable base vocabulary before broader library expansion.
Future library families MAY be added later for domains such as:
</p>

<ul>
  <li>mathematics,</li>
  <li>signal processing,</li>
  <li>tensor computation,</li>
  <li>ONNX-oriented operators,</li>
  <li>domain-specific industrial and embedded primitives.</li>
</ul>

<p>
Such additions SHOULD preserve the same overall architectural principle:
library catalogs define reusable primitive vocabularies without changing the canonical source structure of the language itself.
</p>

<hr/>

<h2 id="status">8. Status</h2>

<p>
At the current repository stage, <code>Libraries/</code> is intentionally small.
It contains the foundational <code>frog.core</code> library specification and is expected to grow as the language matures.
</p>

<p>
The immediate role of this directory is to anchor the normative primitive vocabulary used by the rest of the specification.
</p>
