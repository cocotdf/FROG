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
In FROG, executable diagrams may contain nodes of kind <code>primitive</code>.
The meaning of those nodes is defined by standardized primitive-library catalogs.
This directory is the normative home of those catalogs.
</p>

<p>
Accordingly:
</p>

<ul>
  <li><code>Expression/</code> defines the canonical source structure of a FROG,</li>
  <li><code>Language/</code> defines cross-cutting normative execution semantics,</li>
  <li><code>Libraries/</code> defines the standardized primitive vocabularies consumed by executable diagrams.</li>
</ul>

<hr/>

<h2 id="scope-of-this-directory">2. Scope of this Directory</h2>

<p>
This directory specifies library-level primitive catalogs.
It defines which standardized primitives exist, how they are named, what ports they expose, what primitive-local metadata they require, and what primitive-local semantics they carry.
</p>

<p>
This directory does not define:
</p>

<ul>
  <li>the canonical <code>.frog</code> source structure,</li>
  <li>the general diagram graph model,</li>
  <li>the type system,</li>
  <li>the widget object model,</li>
  <li>front-panel serialization,</li>
  <li>cross-cutting language execution semantics,</li>
  <li>IDE palette organization or authoring workflows.</li>
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
For example:
</p>

<pre><code>{
  "id": "add_1",
  "kind": "primitive",
  "type": "frog.core.add"
}</code></pre>

<p>
The meaning of <code>frog.core.add</code> is not defined directly by the diagram file itself.
It is defined by the relevant library specification in this directory.
</p>

<p>
This separation keeps the following responsibilities distinct:
</p>

<ul>
  <li>graph structure,</li>
  <li>type rules,</li>
  <li>widget and front-panel models,</li>
  <li>cross-cutting language semantics,</li>
  <li>library-defined primitive behavior.</li>
</ul>

<hr/>

<h2 id="current-documents">4. Current Documents</h2>

<p>
This directory currently contains the following standard library specifications:
</p>

<ul>
  <li><code>Core.md</code> — foundational <code>frog.core</code> primitives.</li>
  <li><code>Math.md</code> — standard <code>frog.math</code> primitives.</li>
  <li><code>Collections.md</code> — standard <code>frog.collections</code> primitives.</li>
  <li><code>Text.md</code> — standard <code>frog.text</code> primitives.</li>
  <li><code>IO.md</code> — standard <code>frog.io</code> primitives.</li>
  <li><code>Signal.md</code> — standard <code>frog.signal</code> primitives.</li>
  <li><code>UI.md</code> — standard <code>frog.ui</code> interaction primitives.</li>
  <li><code>Connectivity.md</code> — standard <code>frog.connectivity</code> interoperability primitives.</li>
</ul>

<p>
Together, these documents define the current standard primitive taxonomy of the repository stage represented by this file.
</p>

<hr/>

<h2 id="library-taxonomy">5. Library Taxonomy</h2>

<p>
At the current repository stage, the standard primitive taxonomy is organized as follows:
</p>

<ul>
  <li><strong><code>frog.core.*</code></strong> — foundational language primitives</li>
  <li><strong><code>frog.math.*</code></strong> — numeric scalar primitives</li>
  <li><strong><code>frog.collections.*</code></strong> — collection primitives</li>
  <li><strong><code>frog.text.*</code></strong> — text-processing primitives</li>
  <li><strong><code>frog.io.*</code></strong> — file, path, resource, and byte-oriented I/O primitives</li>
  <li><strong><code>frog.signal.*</code></strong> — signal-processing primitives</li>
  <li><strong><code>frog.ui.*</code></strong> — executable widget interaction primitives</li>
  <li><strong><code>frog.connectivity.*</code></strong> — interoperability and external binding primitives</li>
</ul>

<p>
Additional families MAY be standardized later, but they are not part of the current standard library surface unless a corresponding specification exists in this directory.
</p>

<hr/>

<h2 id="relation-with-other-specifications">6. Relation with Other Specifications</h2>

<p>
Library specifications are used together with the rest of the FROG specification.
In particular:
</p>

<ul>
  <li><code>Expression/Diagram.md</code> defines how primitive nodes appear in executable graphs,</li>
  <li><code>Expression/Type.md</code> defines the ordinary type rules used by primitive ports,</li>
  <li><code>Language/</code> defines cross-cutting execution semantics that remain distinct from library-local primitive behavior,</li>
  <li><code>Expression/Widget.md</code> and <code>Expression/Widget interaction.md</code> define the widget model and source-facing interaction model used by <code>frog.ui.*</code>,</li>
  <li><code>IDE/Palette.md</code> may organize discovery and presentation of primitives, but does not replace library specifications.</li>
</ul>

<p>
Accordingly, a library specification is one normative input used to interpret primitive nodes inside a validated executable graph.
It is not a replacement for the diagram specification, the language semantics, the widget model, or the IDE model.
</p>

<hr/>

<h2 id="naming-and-namespaces">7. Naming and Namespaces</h2>

<p>
FROG library primitives use stable namespace-qualified identifiers.
The general naming patterns are:
</p>

<pre><code>frog.&lt;library&gt;.&lt;primitive&gt;
frog.&lt;library&gt;.&lt;family&gt;.&lt;primitive&gt;</code></pre>

<p>
Examples:
</p>

<ul>
  <li><code>frog.core.add</code></li>
  <li><code>frog.math.sqrt</code></li>
  <li><code>frog.collections.length</code></li>
  <li><code>frog.text.concat</code></li>
  <li><code>frog.io.read_text</code></li>
  <li><code>frog.signal.moving_average</code></li>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.connectivity.python.call_text</code></li>
  <li><code>frog.connectivity.sql.query_text</code></li>
</ul>

<p>
This naming model keeps primitive identity explicit and portable across tools, runtimes, and implementations.
</p>

<p>
Deeper hierarchical namespaces MAY be used where a library family requires explicit sub-namespace ownership.
</p>

<hr/>

<h2 id="library-boundaries">8. Library Boundaries</h2>

<p>
The standard library families in this directory are intentionally separated by responsibility.
</p>

<ul>
  <li><strong><code>frog.core.*</code></strong> owns only the foundational primitive baseline.</li>
  <li><strong><code>frog.math.*</code></strong> owns numeric scalar primitives beyond the core.</li>
  <li><strong><code>frog.collections.*</code></strong> owns collection manipulation primitives.</li>
  <li><strong><code>frog.text.*</code></strong> owns text-processing primitives.</li>
  <li><strong><code>frog.io.*</code></strong> owns file, path, resource, and byte-oriented I/O primitives.</li>
  <li><strong><code>frog.signal.*</code></strong> owns signal-processing primitives.</li>
  <li><strong><code>frog.ui.*</code></strong> owns executable widget interaction primitives only.</li>
  <li><strong><code>frog.connectivity.*</code></strong> owns interoperability and external binding primitives.</li>
</ul>

<p>
Therefore:
</p>

<ul>
  <li><code>frog.core.*</code> MUST NOT become a generic bucket for unrelated future functionality,</li>
  <li><code>frog.io.*</code> MUST remain distinct from external-runtime binding concerns,</li>
  <li><code>frog.ui.*</code> MUST remain distinct from front-panel serialization and widget catalog definition,</li>
  <li><code>frog.text.*</code> MUST remain distinct from file, path, and network I/O semantics,</li>
  <li><code>frog.collections.*</code> MUST remain distinct from future map-, dictionary-, or record-oriented libraries unless those are explicitly standardized,</li>
  <li><code>frog.signal.*</code> MUST remain distinct from future tensor, waveform, or acquisition libraries unless those are explicitly standardized,</li>
  <li><code>frog.connectivity.*</code> MUST remain distinct from ordinary file/path I/O, widget interaction, and unrelated future networking or hardware-access families unless those are explicitly standardized there.</li>
</ul>

<p>
This separation is intended to keep the language taxonomy durable, predictable, and IDE-friendly.
</p>

<hr/>

<h2 id="library-evolution">9. Library Evolution</h2>

<p>
FROG v0.1 begins with a compact but extensible library taxonomy.
This is intentional.
</p>

<p>
The current standard library surface already covers:
</p>

<ul>
  <li>foundational computation,</li>
  <li>numeric functions,</li>
  <li>collections,</li>
  <li>text processing,</li>
  <li>I/O,</li>
  <li>signal processing,</li>
  <li>widget interaction,</li>
  <li>external interoperability.</li>
</ul>

<p>
Additional families MAY be added later for domains such as:
</p>

<ul>
  <li>tensor computation,</li>
  <li>ONNX-oriented operators,</li>
  <li>runtime coordination and scheduling,</li>
  <li>networking,</li>
  <li>hardware acquisition and control,</li>
  <li>domain-specific industrial and embedded primitives.</li>
</ul>

<p>
Such additions SHOULD preserve the same architectural principle:
library catalogs define reusable primitive vocabularies without changing the canonical source structure of the language itself.
</p>

<p>
When a new library family is introduced, it SHOULD be added as a sibling specification in this directory and SHOULD be reflected in the repository documentation and relevant IDE palette documentation.
</p>

<hr/>

<h2 id="status">10. Status</h2>

<p>
At the current repository stage, <code>Libraries/</code> defines a growing but intentionally controlled standard primitive taxonomy used by the rest of the specification.
</p>

<p>
Its role is to anchor the normative primitive vocabulary consumed by executable diagrams while remaining cleanly separated from:
</p>

<ul>
  <li>source-format structure in <code>Expression/</code>,</li>
  <li>cross-cutting execution semantics in <code>Language/</code>,</li>
  <li>widget and front-panel models,</li>
  <li>IDE palette organization and authoring workflows.</li>
</ul>

<p>
This directory is expected to grow as the language matures, but that growth SHOULD preserve explicit namespace ownership, clear library boundaries, and conservative integration with the rest of the specification.
</p>
