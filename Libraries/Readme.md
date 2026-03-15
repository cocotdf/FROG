<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG Libraries</h1>

<p align="center">
  Intrinsic standard primitive library specifications for <strong>FROG</strong><br/>
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
This directory contains the <strong>intrinsic standard primitive library specifications</strong> used by FROG programs.
</p>

<p>
In FROG, executable diagrams may contain nodes of kind <code>primitive</code>.
The meaning of those nodes is defined by standardized primitive catalogs.
This directory is the normative home of the intrinsic library catalogs that belong to the core language surface.
</p>

<p>
Accordingly:
</p>

<ul>
  <li><code>Expression/</code> defines the canonical source structure of a FROG,</li>
  <li><code>Language/</code> defines cross-cutting normative execution semantics,</li>
  <li><code>Libraries/</code> defines intrinsic standardized primitive vocabularies consumed by executable diagrams,</li>
  <li><code>Profiles/</code> defines optional standardized capability families that remain outside the minimal intrinsic library core.</li>
</ul>

<hr/>

<h2 id="scope-of-this-directory">2. Scope of this Directory</h2>

<p>
This directory specifies intrinsic library-level primitive catalogs.
It defines which intrinsic standardized primitives exist, how they are named, what ports they expose,
what primitive-local metadata they require, and what primitive-local semantics they carry.
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
  <li>IDE palette organization or authoring workflows,</li>
  <li>optional profile-owned capability families,</li>
  <li>implementation-specific extensions.</li>
</ul>

<p>
Those concerns are defined elsewhere in the repository.
</p>

<hr/>

<h2 id="role-of-libraries-in-frog">3. Role of Libraries in FROG</h2>

<p>
An intrinsic primitive library provides the standardized executable vocabulary used by diagram nodes of kind <code>primitive</code>.
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
  <li>intrinsic library-defined primitive behavior,</li>
  <li>optional profile-owned capability surfaces.</li>
</ul>

<p>
The role of <code>Libraries/</code> is therefore intentionally narrow:
it defines the reusable primitive vocabularies that belong to the intrinsic standard language surface.
It is not the default home for every useful capability that may later appear in the FROG ecosystem.
</p>

<hr/>

<h2 id="current-documents">4. Current Documents</h2>

<p>
This directory currently contains the following intrinsic standard library specifications:
</p>

<ul>
  <li><code>Core.md</code> — foundational <code>frog.core</code> primitives.</li>
  <li><code>Math.md</code> — standard <code>frog.math</code> primitives.</li>
  <li><code>Collections.md</code> — standard <code>frog.collections</code> primitives.</li>
  <li><code>Text.md</code> — standard <code>frog.text</code> primitives.</li>
  <li><code>IO.md</code> — standard <code>frog.io</code> primitives.</li>
  <li><code>Signal.md</code> — standard <code>frog.signal</code> primitives.</li>
  <li><code>UI.md</code> — standard <code>frog.ui</code> interaction primitives.</li>
</ul>

<p>
Optional standardized capability families that depend on broader environment assumptions or external ecosystems
MUST be specified outside this intrinsic library layer.
</p>

<hr/>

<h2 id="library-taxonomy">5. Library Taxonomy</h2>

<p>
At the current repository stage, the intrinsic standard primitive taxonomy is organized as follows:
</p>

<ul>
  <li><strong><code>frog.core.*</code></strong> — foundational language primitives</li>
  <li><strong><code>frog.math.*</code></strong> — numeric scalar primitives</li>
  <li><strong><code>frog.collections.*</code></strong> — collection primitives</li>
  <li><strong><code>frog.text.*</code></strong> — text-processing primitives</li>
  <li><strong><code>frog.io.*</code></strong> — file, path, resource, and byte-oriented I/O primitives</li>
  <li><strong><code>frog.signal.*</code></strong> — signal-processing primitives</li>
  <li><strong><code>frog.ui.*</code></strong> — executable widget interaction primitives</li>
</ul>

<p>
Additional intrinsic library families MAY be standardized later, but they are not part of the current intrinsic
standard library surface unless a corresponding specification exists in this directory.
</p>

<p>
Optional capability families that rely on external runtimes, managed platforms, databases, host ABIs,
deployment assumptions, or other non-intrinsic execution environments SHOULD be specified as profiles rather than intrinsic libraries.
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
  <li><code>Profiles/</code> defines optional standardized capability families that are not part of the intrinsic library core,</li>
  <li><code>IDE/Palette.md</code> may organize discovery and presentation of primitives, but does not replace library specifications.</li>
</ul>

<p>
Accordingly, a library specification is one normative input used to interpret intrinsic primitive nodes inside a validated executable graph.
It is not a replacement for the diagram specification, the language semantics, the widget model, the profile layer, or the IDE model.
</p>

<hr/>

<h2 id="naming-and-namespaces">7. Naming and Namespaces</h2>

<p>
FROG primitive identifiers use stable namespace-qualified names.
For intrinsic library primitives, the general naming patterns are:
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
</ul>

<p>
This naming model keeps primitive identity explicit and portable across tools, runtimes, and implementations.
</p>

<p>
Deeper hierarchical namespaces MAY be used where an intrinsic library family requires explicit sub-namespace ownership.
</p>

<p>
Other repository layers, including optional profiles, MAY define additional namespace families.
Such namespaces are not automatically intrinsic library namespaces merely because they begin with <code>frog.</code>.
Architectural ownership is defined by the specification layer that normatively owns them.
</p>

<hr/>

<h2 id="library-boundaries">8. Library Boundaries</h2>

<p>
The intrinsic standard library families in this directory are intentionally separated by responsibility.
</p>

<ul>
  <li><strong><code>frog.core.*</code></strong> owns only the foundational primitive baseline.</li>
  <li><strong><code>frog.math.*</code></strong> owns numeric scalar primitives beyond the core.</li>
  <li><strong><code>frog.collections.*</code></strong> owns collection manipulation primitives.</li>
  <li><strong><code>frog.text.*</code></strong> owns text-processing primitives.</li>
  <li><strong><code>frog.io.*</code></strong> owns file, path, resource, and byte-oriented I/O primitives.</li>
  <li><strong><code>frog.signal.*</code></strong> owns signal-processing primitives.</li>
  <li><strong><code>frog.ui.*</code></strong> owns executable widget interaction primitives only.</li>
</ul>

<p>
Therefore:
</p>

<ul>
  <li><code>frog.core.*</code> MUST NOT become a generic bucket for unrelated future functionality,</li>
  <li><code>frog.io.*</code> MUST remain distinct from foreign-runtime interoperability, networking, deployment, and hardware-access concerns unless those are explicitly standardized as intrinsic libraries,</li>
  <li><code>frog.ui.*</code> MUST remain distinct from front-panel serialization and widget catalog definition,</li>
  <li><code>frog.text.*</code> MUST remain distinct from file, path, and external-service semantics,</li>
  <li><code>frog.collections.*</code> MUST remain distinct from future map-, dictionary-, record-, or object-oriented families unless those are explicitly standardized,</li>
  <li><code>frog.signal.*</code> MUST remain distinct from broader acquisition, streaming, tensor, or specialized domain families unless those are explicitly standardized,</li>
  <li><code>Libraries/</code> MUST NOT become a catch-all container for ecosystem-specific capability growth,</li>
  <li>optional capability families that depend on external runtimes, host ABIs, managed platforms, databases, or comparable execution-environment assumptions SHOULD be specified in <code>Profiles/</code> rather than in <code>Libraries/</code>.</li>
</ul>

<p>
This separation is intended to keep the intrinsic language taxonomy durable, predictable, portable, and IDE-friendly.
</p>

<hr/>

<h2 id="library-evolution">9. Library Evolution</h2>

<p>
FROG v0.1 begins with a compact but extensible intrinsic library taxonomy.
This is intentional.
</p>

<p>
The current intrinsic standard library surface already covers:
</p>

<ul>
  <li>foundational computation,</li>
  <li>numeric functions,</li>
  <li>collections,</li>
  <li>text processing,</li>
  <li>I/O,</li>
  <li>signal processing,</li>
  <li>widget interaction.</li>
</ul>

<p>
Additional intrinsic library families MAY be added later where they remain:
</p>

<ul>
  <li>generic,</li>
  <li>portable,</li>
  <li>intrinsic to the language ecosystem,</li>
  <li>not dependent on one specific foreign runtime, managed platform, database stack, host ABI, or vendor technology.</li>
</ul>

<p>
Examples of possible future intrinsic library areas may include:
</p>

<ul>
  <li>broader collection families,</li>
  <li>additional numeric or signal-processing families,</li>
  <li>general-purpose data representation utilities,</li>
  <li>other reusable primitive vocabularies that remain intrinsic to FROG itself.</li>
</ul>

<p>
Capability areas that are useful but environment-dependent SHOULD be specified as profiles or as implementation-specific extensions rather than being folded into the intrinsic library core.
</p>

<p>
When a new intrinsic library family is introduced, it SHOULD be added as a sibling specification in this directory and SHOULD be reflected in the repository documentation and relevant IDE palette documentation.
</p>

<hr/>

<h2 id="status">10. Status</h2>

<p>
At the current repository stage, <code>Libraries/</code> defines a growing but intentionally controlled intrinsic standard primitive taxonomy used by the rest of the specification.
</p>

<p>
Its role is to anchor the normative primitive vocabulary consumed by executable diagrams while remaining cleanly separated from:
</p>

<ul>
  <li>source-format structure in <code>Expression/</code>,</li>
  <li>cross-cutting execution semantics in <code>Language/</code>,</li>
  <li>optional standardized capability families in <code>Profiles/</code>,</li>
  <li>widget and front-panel models,</li>
  <li>IDE palette organization and authoring workflows,</li>
  <li>implementation-specific extensions.</li>
</ul>

<p>
This directory is expected to evolve as the language matures, but that evolution MUST preserve explicit namespace ownership,
clear architectural boundaries, and conservative integration with the rest of the specification.
</p>
