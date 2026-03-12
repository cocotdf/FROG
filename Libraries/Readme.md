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
  <li><a href="#library-taxonomy">5. Library Taxonomy</a></li>
  <li><a href="#relation-with-other-specifications">6. Relation with Other Specifications</a></li>
  <li><a href="#naming-and-namespaces">7. Naming and Namespaces</a></li>
  <li><a href="#library-boundaries">8. Library Boundaries</a></li>
  <li><a href="#library-evolution">9. Library Evolution</a></li>
  <li><a href="#status">10. Status</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory contains the standard primitive library specifications used by FROG programs.
</p>

<p>
In FROG, the executable <code>diagram</code> is composed of graph nodes.
Some of those nodes are <code>primitive</code> nodes whose meaning is defined by a standardized library catalog.
This directory is where those primitive-library catalogs are specified.
</p>

<p>
In other words:
</p>

<ul>
  <li><code>Expression/</code> defines the canonical source structure of a FROG,</li>
  <li><code>Libraries/</code> defines the standardized primitive vocabularies used inside executable diagrams.</li>
</ul>

<hr/>

<h2 id="scope-of-this-directory">2. Scope of this Directory</h2>

<p>
This directory specifies library-level primitive catalogs.
It defines what standardized primitives exist, how they are named, what ports they expose, what metadata they require, and what semantics they carry.
</p>

<p>
This directory does not redefine:
</p>

<ul>
  <li>the canonical <code>.frog</code> source structure,</li>
  <li>the general diagram graph model,</li>
  <li>the type system,</li>
  <li>the widget object model,</li>
  <li>the front-panel serialization model,</li>
  <li>the IDE architecture or palette UX model.</li>
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
The meaning of <code>frog.core.add</code> is not defined directly by the diagram file itself.
It is defined by the appropriate library specification in this directory.
</p>

<p>
This separation is important because it keeps:
</p>

<ul>
  <li>graph structure,</li>
  <li>type rules,</li>
  <li>widget/front-panel models,</li>
  <li>library semantics</li>
</ul>

<p>
as distinct specification responsibilities.
</p>

<hr/>

<h2 id="current-documents">4. Current Documents</h2>

<p>
This directory currently contains the following standard library specifications:
</p>

<ul>
  <li><code>Core.md</code> — the minimal standard <code>frog.core</code> library for FROG v0.1.</li>
  <li><code>UI.md</code> — the standard <code>frog.ui</code> primitive library for widget object interaction in FROG v0.1.</li>
  <li><code>IO.md</code> — the standard <code>frog.io</code> primitive library for file, path, resource, and related I/O in FROG v0.1.</li>
  <li><code>Connectivity.md</code> — the standard <code>frog.connectivity</code> primitive library for external language, runtime, library, service, and database bindings in FROG v0.1.</li>
</ul>

<p>
Together, these documents define the initial standard primitive taxonomy of the language.
</p>

<p>
The <code>frog.core</code> library provides the foundational built-in primitive set.
The other libraries define standardized families beyond the minimal core, while remaining part of the same overall primitive-library layer.
</p>

<hr/>

<h2 id="library-taxonomy">5. Library Taxonomy</h2>

<p>
At the current repository stage, the standard primitive taxonomy is organized as follows:
</p>

<ul>
  <li><strong><code>frog.core.*</code></strong> — minimal foundational language primitives</li>
  <li><strong><code>frog.ui.*</code></strong> — widget object interaction primitives</li>
  <li><strong><code>frog.io.*</code></strong> — file/path/resource I/O primitives</li>
  <li><strong><code>frog.connectivity.*</code></strong> — external binding and interoperability primitives</li>
</ul>

<p>
This taxonomy is intentionally explicit.
It separates:
</p>

<ul>
  <li>core language functionality,</li>
  <li>UI object interaction,</li>
  <li>I/O concerns,</li>
  <li>external interoperability and bindings</li>
</ul>

<p>
into distinct normative library families.
</p>

<hr/>

<h2 id="relation-with-other-specifications">6. Relation with Other Specifications</h2>

<p>
Library specifications in this directory are used together with the rest of the FROG specification.
In particular:
</p>

<ul>
  <li><code>Expression/Diagram.md</code> defines how primitives appear as executable graph nodes,</li>
  <li><code>Expression/Type.md</code> defines type syntax, compatibility, and coercion rules used by primitive ports,</li>
  <li><code>Expression/Control structures.md</code> defines language structures, which remain distinct from ordinary primitive functions,</li>
  <li><code>Expression/State and cycles.md</code> defines explicit local memory and cycle-validity rules that constrain stateful primitives such as <code>frog.core.delay</code>,</li>
  <li><code>Expression/Widget interaction.md</code> defines the canonical source-level interaction model used by <code>frog.ui.*</code> primitives,</li>
  <li><code>Expression/Front panel.md</code> defines widget instances and <code>ui_libraries</code>, which remain distinct from executable primitive libraries,</li>
  <li><code>IDE/Palette.md</code> defines palette organization and discovery, but does not replace library specifications.</li>
</ul>

<p>
Accordingly, a primitive library specification is not a replacement for the diagram specification, the widget model, or the IDE model.
It is one normative input used to interpret primitive nodes inside a validated executable graph.
</p>

<hr/>

<h2 id="naming-and-namespaces">7. Naming and Namespaces</h2>

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
  <li><code>frog.core.delay</code></li>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.io.read_text</code></li>
  <li><code>frog.connectivity.python.call</code></li>
</ul>

<p>
This naming model keeps primitive identity explicit and portable across tools, runtimes, and implementations.
</p>

<p>
Library specifications MAY define deeper hierarchical namespaces when needed, for example:
</p>

<ul>
  <li><code>frog.connectivity.python.*</code></li>
  <li><code>frog.connectivity.sql.*</code></li>
  <li><code>frog.connectivity.dotnet.*</code></li>
  <li><code>frog.connectivity.native.*</code></li>
</ul>

<p>
Such deeper namespaces remain subject to the same stability and clarity requirements as top-level library families.
</p>

<hr/>

<h2 id="library-boundaries">8. Library Boundaries</h2>

<p>
The standard library families in this directory are intentionally separated by responsibility.
</p>

<p>
The following boundaries apply:
</p>

<ul>
  <li><strong><code>frog.ui.*</code></strong> owns widget object interaction only, including standardized primitives such as <code>property_read</code>, <code>property_write</code>, and <code>method_invoke</code>.</li>
  <li><strong><code>frog.io.*</code></strong> owns file/path/resource I/O only.</li>
  <li><strong><code>frog.connectivity.*</code></strong> owns Python, native/shared library, C/C++, .NET, SQL, and external runtime/service bindings.</li>
</ul>

<p>
Therefore:
</p>

<ul>
  <li><code>frog.ui.*</code> MUST NOT absorb general file I/O or external-language binding responsibilities,</li>
  <li><code>frog.io.*</code> MUST NOT absorb Python, .NET, SQL, or foreign-library interoperability,</li>
  <li><code>frog.connectivity.*</code> MUST NOT be used as a generic replacement for ordinary file/path/resource I/O.</li>
</ul>

<p>
This separation is intended to keep the language taxonomy durable, predictable, and IDE-friendly.
</p>

<hr/>

<h2 id="library-evolution">9. Library Evolution</h2>

<p>
The current repository begins with a compact but extensible library taxonomy.
This is intentional.
</p>

<p>
FROG v0.1 prioritizes a durable base vocabulary before broader expansion.
Future library families MAY be added later for domains such as:
</p>

<ul>
  <li>mathematics,</li>
  <li>signal processing,</li>
  <li>tensor computation,</li>
  <li>ONNX-oriented operators,</li>
  <li>runtime coordination and scheduling,</li>
  <li>domain-specific industrial and embedded primitives.</li>
</ul>

<p>
Such additions SHOULD preserve the same overall architectural principle:
library catalogs define reusable primitive vocabularies without changing the canonical source structure of the language itself.
</p>

<hr/>

<h2 id="status">10. Status</h2>

<p>
At the current repository stage, <code>Libraries/</code> defines the initial standard primitive taxonomy used by the rest of the specification.
</p>

<p>
Its immediate role is to anchor the normative primitive vocabulary consumed by executable diagrams while remaining cleanly separated from:
</p>

<ul>
  <li>source-format structure in <code>Expression/</code>,</li>
  <li>widget and front-panel models,</li>
  <li>IDE palette organization and authoring workflows.</li>
</ul>

<p>
This directory is expected to grow as the language matures, but its growth SHOULD preserve explicit namespace ownership and clear library boundaries.
</p>
