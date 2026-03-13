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
  <li>widget and front-panel models,</li>
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
  <li><code>Core.md</code> — the minimal standard <code>frog.core</code> library for foundational primitive behavior in FROG v0.1.</li>
  <li><code>Math.md</code> — the standard <code>frog.math</code> library for numeric scalar operations beyond the minimal core.</li>
  <li><code>Collections.md</code> — the standard <code>frog.collections</code> library for array-oriented collection primitives in FROG v0.1.</li>
  <li><code>Text.md</code> — the standard <code>frog.text</code> library for text-processing primitives in FROG v0.1.</li>
  <li><code>IO.md</code> — the standard <code>frog.io</code> library for file, path, byte, and related I/O primitives in FROG v0.1.</li>
  <li><code>Signal.md</code> — the standard <code>frog.signal</code> library for first-wave 1D signal-processing primitives in FROG v0.1.</li>
  <li><code>UI.md</code> — the standard <code>frog.ui</code> library for executable widget interaction primitives in FROG v0.1.</li>
  <li><code>Connectivity.md</code> — the standard <code>frog.connectivity</code> library for Python, native/shared-library, .NET, SQL, and related interoperability primitives in FROG v0.1.</li>
</ul>

<p>
Together, these documents define the current standard primitive taxonomy of the language at the repository stage represented by this file.
</p>

<p>
The <code>frog.core</code> library provides the foundational built-in primitive set.
The sibling libraries extend the standard primitive layer without changing the canonical source structure of FROG itself.
</p>

<hr/>

<h2 id="library-taxonomy">5. Library Taxonomy</h2>

<p>
At the current repository stage, the standard primitive taxonomy is organized as follows:
</p>

<ul>
  <li><strong><code>frog.core.*</code></strong> — minimal foundational language primitives</li>
  <li><strong><code>frog.math.*</code></strong> — numeric scalar functions beyond the minimal core</li>
  <li><strong><code>frog.collections.*</code></strong> — array-oriented collection primitives</li>
  <li><strong><code>frog.text.*</code></strong> — text-processing primitives</li>
  <li><strong><code>frog.io.*</code></strong> — file, path, resource, and byte-oriented I/O primitives</li>
  <li><strong><code>frog.signal.*</code></strong> — first-wave 1D signal-processing primitives</li>
  <li><strong><code>frog.ui.*</code></strong> — executable object-style widget interaction primitives</li>
  <li><strong><code>frog.connectivity.*</code></strong> — standardized foreign-runtime, native/shared-library, managed-platform, and SQL interoperability primitives</li>
</ul>

<p>
This taxonomy is intentionally explicit.
It separates:
</p>

<ul>
  <li>foundational language behavior,</li>
  <li>numeric computation,</li>
  <li>collection manipulation,</li>
  <li>text handling,</li>
  <li>I/O concerns,</li>
  <li>signal-processing concerns,</li>
  <li>widget interaction concerns,</li>
  <li>external interoperability concerns</li>
</ul>

<p>
into distinct normative library families.
</p>

<p>
Additional families MAY be standardized later, but they are not considered current library documents unless they exist as specifications in this directory.
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
  <li><code>Expression/Widget interaction.md</code> defines the canonical source-level UI interaction model used by <code>frog.ui.*</code> primitives,</li>
  <li><code>Expression/Front panel.md</code> defines widget instances and <code>ui_libraries</code>, which remain distinct from executable primitive libraries,</li>
  <li><code>Libraries/UI.md</code> defines executable widget interaction primitives,</li>
  <li><code>Libraries/Connectivity.md</code> defines standardized interoperability primitives,</li>
  <li><code>IDE/Palette.md</code> defines palette organization and discovery, but does not replace library specifications.</li>
</ul>

<p>
Accordingly, a primitive library specification is not a replacement for the diagram specification, the widget model, the front-panel model, or the IDE model.
It is one normative input used to interpret primitive nodes inside a validated executable graph.
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
Deeper hierarchical namespaces MAY be used when a library family requires an explicit sub-namespace.
At the current repository stage, <code>frog.connectivity.*</code> already uses such a family-based namespace structure for standardized interoperability families.
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
  <li><strong><code>frog.core.*</code></strong> owns only the minimal foundational primitive set required by the language baseline.</li>
  <li><strong><code>frog.math.*</code></strong> owns numeric scalar functions beyond the core.</li>
  <li><strong><code>frog.collections.*</code></strong> owns array-oriented collection manipulation primitives.</li>
  <li><strong><code>frog.text.*</code></strong> owns text-processing primitives.</li>
  <li><strong><code>frog.io.*</code></strong> owns file, path, resource, and byte-oriented I/O primitives.</li>
  <li><strong><code>frog.signal.*</code></strong> owns signal-processing primitives as standardized by the current repository stage.</li>
  <li><strong><code>frog.ui.*</code></strong> owns widget object interaction only.</li>
  <li><strong><code>frog.connectivity.*</code></strong> owns Python, native/shared-library, .NET, SQL, and related external-runtime or external-service binding primitives.</li>
</ul>

<p>
Therefore:
</p>

<ul>
  <li><code>frog.core.*</code> MUST NOT be treated as a generic bucket for all future functionality,</li>
  <li><code>frog.io.*</code> MUST NOT absorb unrelated external-language or foreign-runtime binding responsibilities,</li>
  <li><code>frog.ui.*</code> MUST remain limited to executable widget interaction rather than front-panel serialization or widget catalog definition,</li>
  <li><code>frog.text.*</code> MUST NOT absorb path semantics, file semantics, or network I/O semantics,</li>
  <li><code>frog.collections.*</code> MUST remain distinct from future map/dictionary or record-oriented libraries unless those are explicitly standardized,</li>
  <li><code>frog.signal.*</code> MUST remain distinct from future tensor, waveform, or hardware-acquisition libraries unless those are explicitly standardized,</li>
  <li><code>frog.connectivity.*</code> MUST remain distinct from ordinary file/path I/O, widget interaction, and future networking or hardware-access libraries unless those are explicitly standardized within that namespace.</li>
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
At the current repository stage, the standard library surface already includes:
</p>

<ul>
  <li>foundational computation,</li>
  <li>numeric functions,</li>
  <li>collections,</li>
  <li>text processing,</li>
  <li>file- and resource-oriented I/O,</li>
  <li>signal processing,</li>
  <li>widget object interaction,</li>
  <li>external interoperability and connectivity.</li>
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
Such additions SHOULD preserve the same overall architectural principle:
library catalogs define reusable primitive vocabularies without changing the canonical source structure of the language itself.
</p>

<p>
When a new library family is introduced, it SHOULD be added as a sibling specification in this directory and SHOULD be reflected in the root repository documentation and relevant IDE palette documentation.
</p>

<hr/>

<h2 id="status">10. Status</h2>

<p>
At the current repository stage, <code>Libraries/</code> defines a growing but still intentionally controlled standard primitive taxonomy used by the rest of the specification.
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
This directory is expected to grow as the language matures, but its growth SHOULD preserve explicit namespace ownership, clear library boundaries, and conservative integration with the rest of the specification.
</p>
