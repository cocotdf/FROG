<h1 align="center">🐸 FROG IDE Palette Specification</h1>

<p align="center">
Definition of the discovery, search, and insertion palette for the FROG IDE<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Goals</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#design-principles">4. Design Principles</a></li>
  <li><a href="#palette-access-model">5. Palette Access Model</a></li>
  <li><a href="#primary-palette-view">6. Primary Palette View</a></li>
  <li><a href="#namespace-view">7. Namespace View</a></li>
  <li><a href="#search-model">8. Search Model</a></li>
  <li><a href="#context-aware-insertion">9. Context-Aware Insertion</a></li>
  <li><a href="#primitive-structure-node-and-express-presentation">10. Primitive, Structure, Node-Insertion, and Express Presentation</a></li>
  <li><a href="#palette-categories-for-v01">11. Palette Categories for v0.1</a></li>
  <li><a href="#entry-metadata">12. Entry Metadata</a></li>
  <li><a href="#express-entries-and-guided-insertion">13. Express Entries and Guided Insertion</a></li>
  <li><a href="#favorites-recent-and-suggested-entries">14. Favorites, Recent, and Suggested Entries</a></li>
  <li><a href="#stability-and-filtering">15. Stability and Filtering</a></li>
  <li><a href="#extensibility-and-third-party-libraries">16. Extensibility and Third-Party Libraries</a></li>
  <li><a href="#validation-and-consistency">17. Validation and Consistency</a></li>
  <li><a href="#examples">18. Examples</a></li>
  <li><a href="#out-of-scope-for-v01">19. Out of Scope for v0.1</a></li>
  <li><a href="#summary">20. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The FROG IDE palette is the primary user-facing mechanism used to discover, search, understand, and insert standardized
and profile-available entries into a diagram.
</p>

<p>
Its purpose is not only to expose the available catalog, but to expose it in a way that matches how users actually think
when building a graphical program.
</p>

<p>
The palette therefore serves four complementary roles:
</p>

<ul>
  <li><strong>discovery</strong> — helping users find available constructs and insertion paths,</li>
  <li><strong>navigation</strong> — organizing the catalog in a coherent and scalable way,</li>
  <li><strong>insertion</strong> — allowing rapid placement of primitives, structures, and other source-level entries into the diagram,</li>
  <li><strong>guided authoring</strong> — allowing certain common tasks to be inserted through assisted Express-style entries without creating new language constructs.</li>
</ul>

<p>
The palette belongs to the IDE layer.
It exposes constructs owned normatively by other specifications, but it does not redefine their semantics or canonical
source identity.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Intent-first navigation</strong> — users SHOULD be able to find what they want by purpose, not only by internal specification category.</li>
  <li><strong>Namespace consistency</strong> — the palette SHOULD still reflect the actual standardized namespace model where namespaces exist.</li>
  <li><strong>Fast insertion</strong> — search, contextual suggestions, and guided Express entries SHOULD reduce friction.</li>
  <li><strong>Clarity</strong> — primitives, structures, source-node insertions, annotations, and future profile-specific entries MUST NOT be visually conflated.</li>
  <li><strong>Canonical identity preservation</strong> — authoring aliases, search aliases, UI-specific labels, and Express presentations MUST map back to one canonical insertable identity or one canonical target set.</li>
  <li><strong>Explicit taxonomy boundaries</strong> — UI, I/O, Connectivity, Signal, and future execution-facing families MUST remain conceptually distinct.</li>
  <li><strong>Express without semantic drift</strong> — task-oriented guided insertion MUST remain an IDE convenience and MUST NOT become a separate semantic family by itself.</li>
  <li><strong>Scalability</strong> — the model MUST remain usable as FROG grows from a minimal core to richer libraries and stricter profiles.</li>
  <li><strong>Extensibility</strong> — third-party libraries MUST integrate cleanly without breaking the palette model.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This document complements the following specifications:
</p>

<ul>
  <li><code>IDE/Readme.md</code> — defines the role of the palette as an IDE-facing authoring and discovery surface.</li>
  <li><code>Libraries/Readme.md</code> — defines the current standard primitive-library taxonomy.</li>
  <li><code>Libraries/Core.md</code> — defines foundational built-in primitives such as <code>frog.core.add</code> and <code>frog.core.delay</code>.</li>
  <li><code>Libraries/Math.md</code> — defines numeric scalar primitives in the <code>frog.math</code> namespace.</li>
  <li><code>Libraries/Collections.md</code> — defines collection primitives in the <code>frog.collections</code> namespace.</li>
  <li><code>Libraries/Text.md</code> — defines text-processing primitives in the <code>frog.text</code> namespace.</li>
  <li><code>Libraries/IO.md</code> — defines file, path, byte, and related I/O primitives in the <code>frog.io</code> namespace.</li>
  <li><code>Libraries/Signal.md</code> — defines signal-processing primitives in the <code>frog.signal</code> namespace.</li>
  <li><code>Libraries/UI.md</code> — defines executable widget interaction primitives in the <code>frog.ui</code> namespace.</li>
  <li><code>Libraries/Connectivity.md</code> — defines interoperability primitives in the <code>frog.connectivity</code> namespace.</li>
  <li><code>Expression/Control structures.md</code> — defines structures such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>, as well as the source-facing boundary between canonical structures and derived authoring forms.</li>
  <li><code>Language/Control structures.md</code> — defines the normative semantic families of standardized control structures and the rule that authoring-facing derived forms do not create distinct semantic families by themselves.</li>
  <li><code>Expression/Diagram.md</code> — defines how inserted primitives, structures, boundary nodes, widget nodes, and related graph objects appear in canonical source.</li>
  <li><code>Expression/Widget interaction.md</code> — defines canonical source-level widget interaction paths such as <code>widget_value</code>, <code>widget_reference</code>, property access, and method invocation.</li>
  <li><code>Expression/Front panel.md</code> and <code>Expression/Widget.md</code> — define the front-panel and widget model that inform UI-related palette entries.</li>
</ul>

<p>
This document defines how the IDE presents insertable entries to the user.
It does not define the language semantics of those entries, and it does not redefine their canonical source form.
</p>

<p>
Accordingly:
</p>

<ul>
  <li><code>Libraries/</code> defines which standardized primitives exist,</li>
  <li><code>Expression/</code> defines how standardized nodes and structures appear in source,</li>
  <li><code>Language/</code> defines the normative execution meaning of language-level structures,</li>
  <li><code>IDE/Palette.md</code> defines how a conforming IDE exposes those entries for discovery and insertion.</li>
</ul>

<p>
This document also defines how a conforming IDE MAY expose <strong>Express entries</strong> as guided insertion experiences.
Such entries remain IDE-layer authoring mechanisms and MUST normalize to canonical FROG content already defined elsewhere.
</p>

<hr/>

<h2 id="design-principles">4. Design Principles</h2>

<h3>4.1 Intent before implementation</h3>

<p>
The primary palette SHOULD be organized according to user intent such as:
</p>

<ul>
  <li>do arithmetic,</li>
  <li>compare values,</li>
  <li>branch execution,</li>
  <li>repeat execution,</li>
  <li>work with collections,</li>
  <li>process text,</li>
  <li>process signals,</li>
  <li>interact with a widget,</li>
  <li>read a file,</li>
  <li>connect to Python or SQL.</li>
</ul>

<h3>4.2 Canonical identity remains singular</h3>

<p>
A construct MAY appear in multiple discovery paths, but it MUST keep one canonical identity.
A search alias, shortcut, contextual presentation, authoring-facing label, or Express presentation MUST NOT create a second
semantic or source-level construct.
</p>

<p>
For example:
</p>

<ul>
  <li><em>If</em>, <em>If / Else</em>, and <em>Else If</em> MAY be exposed as authoring-facing views, but they resolve to canonical <code>case</code> insertion in base v0.1.</li>
  <li><em>Switch</em> MAY be exposed as an authoring-facing view, but it resolves to canonical <code>case</code> insertion in the selector categories standardized by base v0.1.</li>
  <li><em>Read Text File</em> MAY be exposed as a task-oriented Express entry, but it MUST resolve to valid canonical content owned by the active specification set.</li>
</ul>

<h3>4.3 Namespace remains visible where namespaces exist</h3>

<p>
Although the primary palette is intent-first, the true standardized namespace model remains important for primitive libraries.
The IDE MUST therefore also provide a namespace-oriented view for library entries.
</p>

<h3>4.4 Search is first-class</h3>

<p>
The palette is not only a tree.
Search is a primary insertion path and MUST be treated as a first-class mechanism.
</p>

<h3>4.5 Primitives, structures, source-node insertions, and Express presentations remain distinct</h3>

<p>
Ordinary primitives such as <code>frog.core.add</code>, structures such as <code>case</code>, source-node insertions such as
<code>interface_input</code> or <code>widget_value</code>, and guided Express entries MUST remain visibly distinguishable in the
palette and in search results.
</p>

<h3>4.6 Taxonomy boundaries remain explicit</h3>

<p>
The palette MUST keep the following boundaries explicit:
</p>

<ul>
  <li><strong>Signal</strong> — signal-processing primitives,</li>
  <li><strong>UI</strong> — widget-facing interaction and UI-related insertion paths,</li>
  <li><strong>I/O</strong> — file, path, resource, and byte-oriented I/O,</li>
  <li><strong>Connectivity</strong> — Python, native/shared library, .NET, SQL, and related external-runtime or external-service bindings,</li>
  <li><strong>Reserved / Future Execution Families</strong> — categories surfaced only when explicitly provided by the active profile.</li>
</ul>

<p>
These groups MAY interact in real programs, but the palette SHOULD present them as distinct conceptual families.
</p>

<h3>4.7 Context improves speed</h3>

<p>
The IDE SHOULD use type context, wire context, and insertion context to improve suggestions without changing language semantics.
</p>

<h3>4.8 Express remains an IDE-layer convenience</h3>

<p>
An Express entry MAY improve discoverability, reduce configuration friction, and surface common tasks in more human terms.
However:
</p>

<ul>
  <li>an Express entry MUST NOT create a new canonical primitive identity by itself,</li>
  <li>an Express entry MUST NOT create a new structure family by itself,</li>
  <li>an Express entry MUST disclose or preserve its canonical target identity,</li>
  <li>execution-facing systems MUST remain independent from Express presentation state.</li>
</ul>

<hr/>

<h2 id="palette-access-model">5. Palette Access Model</h2>

<p>
The FROG IDE palette SHOULD expose multiple complementary access paths:
</p>

<ul>
  <li><strong>Primary palette view</strong> — intent-first hierarchical browsing,</li>
  <li><strong>Namespace view</strong> — direct browsing by standardized library namespace and explicit non-library roots,</li>
  <li><strong>Search</strong> — direct textual lookup,</li>
  <li><strong>Contextual insertion</strong> — suggestions derived from the current diagram context,</li>
  <li><strong>Optional guided / Express lens</strong> — a task-oriented filtered presentation of the same insertable surface.</li>
</ul>

<p>
These are alternative access modes to the same underlying catalog of insertable entries.
They MUST remain semantically consistent with one another.
</p>

<p>
A conforming IDE MAY expose an Express-specific lens, filter, or badge-based discovery mode.
It SHOULD NOT treat Express as a separate semantic language family at the same level as library namespaces or standardized
structure families.
</p>

<hr/>

<h2 id="primary-palette-view">6. Primary Palette View</h2>

<p>
The primary palette view is the default palette presented to most users.
It is organized around user intent and common graphical programming tasks.
</p>

<p>
Convenience surfaces such as <strong>Favorites</strong>, <strong>Recent</strong>, <strong>Search</strong>, and an optional
<strong>Guided / Express</strong> lens MAY appear at the top of the palette, but they are not semantic language categories.
</p>

<p>
Recommended top-level primary palette groups for the standardized v0.1 baseline are:
</p>

<pre>
Favorites
Recent
Search
Optional Guided / Express Lens

Program Structure
Flow Control
State &amp; Timing
Math &amp; Logic
Data &amp; Types
Collections
Text
Signal
UI
I/O
Connectivity
</pre>

<p>
Additional groups such as <strong>Tensor &amp; ONNX</strong> or <strong>Concurrency &amp; Runtime</strong> MAY be surfaced by an active profile,
but they SHOULD be clearly marked as profile-defined, future-facing, or non-baseline when they are not part of the current
standardized v0.1 core repository set.
</p>

<p>
A primary palette implementation SHOULD be able to surface both:
</p>

<ul>
  <li>canonical entries directly,</li>
  <li>guided Express entries that point to those canonical entries or to deterministic canonical fragments.</li>
</ul>

<hr/>

<h2 id="namespace-view">7. Namespace View</h2>

<p>
The namespace view exposes the actual standardized library organization of the language where library namespaces exist.
</p>

<p>
At the current repository stage, the standardized primitive-library namespaces include:
</p>

<pre>
frog.core.*
frog.math.*
frog.collections.*
frog.text.*
frog.io.*
frog.signal.*
frog.ui.*
frog.connectivity.*
</pre>

<p>
Because the palette also exposes non-library constructs, a conforming IDE MUST NOT pretend that structures or source-node
insertions belong to a primitive namespace when they do not.
</p>

<p>
Accordingly, a namespace-capable IDE MAY also expose explicit non-library roots such as:
</p>

<pre>
Structures
Diagram Nodes
Annotations
</pre>

<p>
This allows the palette to expose:
</p>

<ul>
  <li>standardized library primitives through true namespaces,</li>
  <li>standardized structures through an explicit structure root,</li>
  <li>standardized source-node insertion entries through explicit non-library roots.</li>
</ul>

<p>
Future families such as <code>frog.tensor.*</code>, <code>frog.onnx.*</code>, or <code>frog.runtime.*</code> MAY be surfaced only when the active
profile explicitly exposes them.
When surfaced, they SHOULD be clearly marked if they are not part of the current standardized baseline.
</p>

<p>
The namespace view MAY additionally indicate which entries have guided Express presentations available.
However, Express presentation MUST remain secondary to canonical namespace identity.
</p>

<hr/>

<h2 id="search-model">8. Search Model</h2>

<p>
Search is a primary palette feature.
Users SHOULD be able to search by:
</p>

<ul>
  <li>primitive name,</li>
  <li>structure name,</li>
  <li>node-insertion name,</li>
  <li>namespace-qualified name,</li>
  <li>common alias,</li>
  <li>operator symbol,</li>
  <li>natural-language keyword,</li>
  <li>task-oriented phrase,</li>
  <li>common Express-style wording.</li>
</ul>

<p>
Examples:
</p>

<ul>
  <li>searching <code>add</code> SHOULD find <code>frog.core.add</code>,</li>
  <li>searching <code>+</code> SHOULD also find <code>frog.core.add</code>,</li>
  <li>searching <code>sqrt</code> SHOULD find the relevant <code>frog.math.*</code> entry,</li>
  <li>searching <code>length</code> SHOULD find the relevant <code>frog.collections.*</code> entry,</li>
  <li>searching <code>read text</code> SHOULD find the relevant canonical <code>frog.io.*</code> entry and MAY also surface a guided Express presentation when available,</li>
  <li>searching <code>moving average</code> SHOULD find the relevant <code>frog.signal.*</code> entry and MAY surface an Express entry when available,</li>
  <li>searching <code>if</code> SHOULD find the canonical <code>case</code> structure through a boolean conditional authoring view,</li>
  <li>searching <code>if else</code> SHOULD also find the canonical <code>case</code> structure,</li>
  <li>searching <code>else if</code> SHOULD help surface the canonical <code>case</code> structure through an appropriate authoring presentation,</li>
  <li>searching <code>switch</code> SHOULD find the canonical <code>case</code> structure through an exact-match authoring view,</li>
  <li>searching <code>else</code> SHOULD also help surface the canonical boolean <code>case</code> structure,</li>
  <li>searching <code>case</code> SHOULD find the canonical <code>case</code> structure,</li>
  <li>searching <code>for</code> SHOULD find <code>for_loop</code>,</li>
  <li>searching <code>while</code> SHOULD find <code>while_loop</code>,</li>
  <li>searching <code>widget value</code> SHOULD find the <code>widget_value</code> insertion entry,</li>
  <li>searching <code>widget reference</code> SHOULD find the <code>widget_reference</code> insertion entry,</li>
  <li>searching <code>interface input</code> SHOULD find the <code>interface_input</code> insertion entry,</li>
  <li>searching <code>interface output</code> SHOULD find the <code>interface_output</code> insertion entry,</li>
  <li>searching <code>property write</code> SHOULD find the relevant widget interaction primitive,</li>
  <li>searching <code>python</code> SHOULD find the relevant connectivity entry when available,</li>
  <li>searching <code>sql</code> SHOULD find the relevant connectivity entry when available.</li>
</ul>

<p>
Search SHOULD rank results using at least:
</p>

<ul>
  <li>exact name match,</li>
  <li>namespace-qualified match,</li>
  <li>alias match,</li>
  <li>task-intent match,</li>
  <li>entry-kind relevance,</li>
  <li>Express availability where appropriate,</li>
  <li>contextual relevance,</li>
  <li>recent usage.</li>
</ul>

<p>
The canonical identity of the returned entry MUST remain unchanged.
For example, a search for <code>if</code> returns the canonical <code>case</code> structure rather than a separate language construct named <code>if</code>.
Likewise, a search for <code>switch</code> returns the canonical <code>case</code> structure when the active selector category is represented through exact-match case semantics.
</p>

<p>
If an Express entry is returned, the search result SHOULD make the canonical target visible through metadata, detail view,
or equivalent disclosure.
</p>

<hr/>

<h2 id="context-aware-insertion">9. Context-Aware Insertion</h2>

<p>
The IDE SHOULD support contextual insertion suggestions derived from the current diagram context.
</p>

<p>
Useful contexts include:
</p>

<ul>
  <li>dragging from a wire,</li>
  <li>inserting near a specific node,</li>
  <li>searching with a selected wire type,</li>
  <li>invoking insertion from a widget reference or widget value node,</li>
  <li>invoking insertion from an empty canvas or structure region.</li>
</ul>

<p>
Examples:
</p>

<ul>
  <li>from a <code>bool</code> wire, prefer logic and conditional suggestions,</li>
  <li>from a numeric wire, prefer arithmetic, comparison, and numeric-function suggestions,</li>
  <li>from a collection wire, prefer collection-related suggestions,</li>
  <li>from a signal-like context, prefer relevant <code>frog.signal.*</code> suggestions when type-compatible,</li>
  <li>from a <code>string</code> wire, prefer text operations and string-based <code>case</code> suggestions,</li>
  <li>from a widget reference, prefer property and method interaction suggestions,</li>
  <li>from a value feedback path, prefer <code>frog.core.delay</code>,</li>
  <li>from a path-like or file-related context, prefer I/O suggestions,</li>
  <li>from a connectivity-related insertion path, prefer Python, native binding, .NET, or SQL suggestions,</li>
  <li>from an empty top-level diagram, surface interface boundary nodes, sub-FROG insertion, annotations, and common structures where appropriate.</li>
</ul>

<p>
When the context strongly suggests a derived authoring form, the IDE MAY present that form directly.
For example:
</p>

<ul>
  <li>from a <code>bool</code> wire, the IDE MAY surface a conditional insertion entry labeled <em>If</em> or <em>If / Else</em>,</li>
  <li>from a <code>string</code> wire, the IDE MAY surface a branching insertion entry labeled <em>Switch</em>,</li>
  <li>from a file-oriented task context, the IDE MAY surface a task-oriented Express entry such as <em>Read Text File</em> when a valid canonical target exists,</li>
  <li>from a signal-processing context, the IDE MAY surface an Express filter entry when a valid canonical target exists.</li>
</ul>

<p>
Such context-aware presentations remain authoring conveniences.
They MUST NOT alter the canonical identity or language semantics of the inserted construct.
</p>

<hr/>

<h2 id="primitive-structure-node-and-express-presentation">10. Primitive, Structure, Node-Insertion, and Express Presentation</h2>

<p>
The palette MUST visually distinguish between:
</p>

<ul>
  <li><strong>primitive entries</strong> — ordinary callable operations defined by primitive libraries,</li>
  <li><strong>structure entries</strong> — diagram regions with owned subgraphs and explicit boundary semantics,</li>
  <li><strong>node-insertion entries</strong> — canonical source nodes or annotations inserted directly into the diagram,</li>
  <li><strong>Express entries</strong> — guided insertion presentations that resolve to canonical content.</li>
</ul>

<p>
Examples:
</p>

<ul>
  <li><code>frog.core.add</code> is a primitive entry,</li>
  <li><code>frog.core.delay</code> is a stateful primitive entry,</li>
  <li><code>case</code> is a structure entry,</li>
  <li><code>for_loop</code> is a structure entry,</li>
  <li><code>while_loop</code> is a structure entry,</li>
  <li><code>interface_input</code> is a node-insertion entry,</li>
  <li><code>interface_output</code> is a node-insertion entry,</li>
  <li><code>widget_value</code> is a node-insertion entry,</li>
  <li><code>widget_reference</code> is a node-insertion entry,</li>
  <li><em>Read Text File</em> MAY be an Express entry if it resolves to a valid canonical target.</li>
</ul>

<p>
Search results and palette entries SHOULD make this distinction visible through iconography, labeling, badges, grouping,
or equivalent UI mechanisms.
</p>

<p>
A structure entry MAY additionally expose one or more <strong>authoring views</strong> or <strong>presentation labels</strong>.
For example:
</p>

<ul>
  <li><code>case</code> MAY be presented as <em>If</em> or <em>If / Else</em> when inserted in a boolean conditional context,</li>
  <li><code>case</code> MAY be presented as <em>Switch</em> when inserted in a string exact-match branching context.</li>
</ul>

<p>
Such labels are presentation-level affordances.
They MUST remain attached to one canonical structure entry rather than creating additional structure identities.
</p>

<p>
Likewise, an Express entry MAY expose a task-oriented label, assistant badge, or guided configuration affordance.
However, it MUST still disclose the canonical target to which it resolves.
</p>

<hr/>

<h2 id="palette-categories-for-v01">11. Palette Categories for v0.1</h2>

<p>
The following palette layout is recommended for the standardized v0.1 baseline.
</p>

<h3>11.1 Program Structure</h3>

<ul>
  <li>Sub-FROG insertion</li>
  <li>Interface input node insertion</li>
  <li>Interface output node insertion</li>
  <li>Comments</li>
  <li>Documentation annotations</li>
</ul>

<p>
Base v0.1 SHOULD NOT treat structure-owned <code>regions</code> as a standalone palette entry with an independent language identity.
Regions are owned by structures and arise through structure insertion and structure editing.
</p>

<h3>11.2 Flow Control</h3>

<ul>
  <li>Case structure</li>
  <li>Boolean conditional authoring view for <code>case</code> such as <em>If</em> or <em>If / Else</em></li>
  <li>Exact-match authoring view for <code>case</code> such as <em>Switch</em> when appropriate</li>
  <li>For loop structure</li>
  <li>While loop structure</li>
</ul>

<p>
The canonical identity of these entries remains:
</p>

<ul>
  <li><code>case</code></li>
  <li><code>for_loop</code></li>
  <li><code>while_loop</code></li>
</ul>

<p>
A conforming IDE MAY expose multiple insertion presentations for <code>case</code>, but those presentations MUST normalize to the same canonical structure family.
Base v0.1 MUST NOT treat <em>If</em>, <em>If / Else</em>, <em>Else If</em>, or <em>Switch</em> as independent standardized structure families.
</p>

<h3>11.3 State &amp; Timing</h3>

<ul>
  <li><code>frog.core.delay</code></li>
  <li>additional timing-related entries only when standardized by the active profile or library set</li>
</ul>

<h3>11.4 Math &amp; Logic</h3>

<ul>
  <li><code>frog.core.add</code></li>
  <li><code>frog.core.sub</code></li>
  <li><code>frog.core.mul</code></li>
  <li><code>frog.core.div</code></li>
  <li><code>frog.core.neg</code></li>
  <li><code>frog.core.abs</code></li>
  <li><code>frog.core.equal</code></li>
  <li><code>frog.core.not_equal</code></li>
  <li><code>frog.core.less</code></li>
  <li><code>frog.core.less_or_equal</code></li>
  <li><code>frog.core.greater</code></li>
  <li><code>frog.core.greater_or_equal</code></li>
  <li><code>frog.core.and</code></li>
  <li><code>frog.core.or</code></li>
  <li><code>frog.core.not</code></li>
  <li><code>frog.core.xor</code></li>
  <li><code>frog.core.select</code></li>
  <li>standardized <code>frog.math.*</code> numeric entries</li>
</ul>

<h3>11.5 Data &amp; Types</h3>

<ul>
  <li>type-conversion entries when standardized by the active library/profile set</li>
  <li>cast entries when standardized by the active library/profile set</li>
  <li>future optional/value wrappers when explicitly standardized</li>
</ul>

<h3>11.6 Collections</h3>

<ul>
  <li>standardized <code>frog.collections.*</code> entries</li>
  <li>array construction helpers when standardized</li>
  <li>array indexing and slicing helpers when standardized</li>
</ul>

<h3>11.7 Text</h3>

<ul>
  <li>standardized <code>frog.text.*</code> entries</li>
  <li>text comparison entries</li>
  <li>text transformation entries</li>
</ul>

<h3>11.8 Signal</h3>

<ul>
  <li>standardized <code>frog.signal.*</code> entries</li>
  <li>signal filtering entries</li>
  <li>signal measurement and transformation entries</li>
  <li>Express signal-processing entries when available and when they disclose a valid canonical target</li>
</ul>

<h3>11.9 UI</h3>

<ul>
  <li><code>widget_value</code> insertion</li>
  <li><code>widget_reference</code> insertion</li>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
</ul>

<p>
This group is intended for widget-facing interaction and UI-related insertion paths.
It SHOULD NOT absorb file I/O, database access, Python bindings, or general external interop.
</p>

<p>
At the current repository stage, this category is grounded both in the source-level widget interaction model and in the standardized <code>frog.ui.*</code> primitive library.
</p>

<h3>11.10 I/O</h3>

<ul>
  <li>standardized <code>frog.io.*</code> entries</li>
  <li>file read and write entries</li>
  <li>path and resource entries</li>
  <li>byte-oriented I/O entries</li>
  <li>Express I/O entries when available and when they disclose a valid canonical target</li>
</ul>

<p>
This group SHOULD cover operations whose primary role is reading from, writing to, opening, closing, or transforming a file, path, resource, or byte-oriented I/O value.
It SHOULD NOT absorb Python, native/shared library, .NET, SQL, or general external service bindings.
</p>

<h3>11.11 Connectivity</h3>

<ul>
  <li>standardized <code>frog.connectivity.python.*</code> entries</li>
  <li>standardized <code>frog.connectivity.native.*</code> entries</li>
  <li>standardized <code>frog.connectivity.dotnet.*</code> entries</li>
  <li>standardized <code>frog.connectivity.sql.*</code> entries</li>
  <li>Express connectivity entries when available and when they disclose a valid canonical target</li>
</ul>

<p>
This group exists to keep interop and external binding workflows explicit instead of collapsing them into a generic and ambiguous external bucket.
</p>

<p>
It SHOULD cover Python bindings, native/shared-library bindings, .NET bindings, SQL and database connectivity, and related external-runtime or external-service bindings standardized by the active library and profile set.
</p>

<h3>11.12 Reserved / Future: Tensor &amp; ONNX</h3>

<p>
This group MAY be surfaced by an active profile for tensor and ONNX-related functions.
When surfaced before full standardization in the baseline repository, it SHOULD be clearly marked as profile-defined, reserved, or future-facing.
</p>

<h3>11.13 Reserved / Future: Concurrency &amp; Runtime</h3>

<p>
This group MAY be surfaced by an active profile for runtime coordination mechanisms such as queues, channels, tasks, schedulers, synchronization tools, and system-level execution utilities.
When surfaced before full standardization in the baseline repository, it SHOULD be clearly marked as profile-defined, reserved, or future-facing.
</p>

<hr/>

<h2 id="entry-metadata">12. Entry Metadata</h2>

<p>
Each palette entry SHOULD expose useful metadata to the user.
</p>

<p>
Recommended metadata includes:
</p>

<ul>
  <li>display name,</li>
  <li>canonical identity,</li>
  <li>namespace-qualified name when applicable,</li>
  <li>entry kind — primitive, structure, node insertion, annotation, Express, or equivalent,</li>
  <li>canonical target kind when the entry is Express,</li>
  <li>short description,</li>
  <li>type family,</li>
  <li>statefulness where relevant,</li>
  <li>stability level,</li>
  <li>library origin or specification origin.</li>
</ul>

<p>
When an entry exposes an authoring-facing alias, insertion view, or Express presentation, the IDE SHOULD also make the canonical identity visible.
</p>

<p>
Examples of useful badges:
</p>

<ul>
  <li>Primitive</li>
  <li>Structure</li>
  <li>Node Insertion</li>
  <li>Express</li>
  <li>Guided</li>
  <li>Configurable</li>
  <li>Expandable</li>
  <li>Pure</li>
  <li>Stateful</li>
  <li>Signal</li>
  <li>UI</li>
  <li>I/O</li>
  <li>Connectivity</li>
  <li>Experimental</li>
  <li>Third-party</li>
  <li>Profile-defined</li>
  <li>Alias</li>
  <li>Authoring View</li>
</ul>

<hr/>

<h2 id="express-entries-and-guided-insertion">13. Express Entries and Guided Insertion</h2>

<p>
A conforming IDE MAY expose <strong>Express entries</strong> as assistant-driven palette entries for common tasks.
Their purpose is to reduce authoring friction while preserving the canonical FROG model.
</p>

<p>
An Express entry:
</p>

<ul>
  <li>MAY appear in primary browsing, search results, contextual insertion, or a dedicated guided lens,</li>
  <li>MUST remain attached to a canonical target identity or a deterministic canonical target set,</li>
  <li>SHOULD disclose that target identity to the user,</li>
  <li>MAY expose configurable parameters and optional expandable terminals,</li>
  <li>MUST NOT invent semantically invalid ports or hidden semantically required ports.</li>
</ul>

<p>
A conforming IDE SHOULD support the following palette-facing Express lifecycle when Express entries exist:
</p>

<ul>
  <li>discover the entry,</li>
  <li>insert and configure the entry,</li>
  <li>reopen the configuration experience,</li>
  <li>preserve stable mapping between the guided presentation and the canonical target,</li>
  <li>discard or detach the guided presentation without invalidating canonical content.</li>
</ul>

<p>
Express entries SHOULD be especially useful for:
</p>

<ul>
  <li>common I/O tasks,</li>
  <li>common signal-processing tasks,</li>
  <li>common connectivity tasks,</li>
  <li>other repetitive workflows where a guided configuration step is materially better than manual low-level assembly.</li>
</ul>

<p>
Express entries SHOULD NOT be required for ordinary language use.
A user MUST remain able to work directly with canonical primitives, canonical structures, and canonical node insertions.
</p>

<hr/>

<h2 id="favorites-recent-and-suggested-entries">14. Favorites, Recent, and Suggested Entries</h2>

<p>
The palette SHOULD support the following convenience groups:
</p>

<h3>14.1 Favorites</h3>

<p>
User-pinned entries for fast access.
</p>

<h3>14.2 Recent</h3>

<p>
Recently inserted entries.
</p>

<h3>14.3 Suggested</h3>

<p>
Entries recommended by the IDE based on context, type, structure location, recent activity, or Express availability.
</p>

<p>
These convenience groups are optional IDE features.
They MUST NOT alter the canonical identity of the underlying entries.
</p>

<hr/>

<h2 id="stability-and-filtering">15. Stability and Filtering</h2>

<p>
The palette SHOULD support filtering by stability level.
Recommended levels include:
</p>

<ul>
  <li>Stable</li>
  <li>Advanced</li>
  <li>Experimental</li>
  <li>Profile-defined</li>
</ul>

<p>
The palette MAY also support filtering by:
</p>

<ul>
  <li>namespace,</li>
  <li>entry kind,</li>
  <li>type family,</li>
  <li>statefulness,</li>
  <li>library origin,</li>
  <li>specification origin,</li>
  <li>Express availability,</li>
  <li>guided vs direct insertion mode.</li>
</ul>

<p>
This helps keep the beginner experience clean while still exposing the full active surface to advanced users.
</p>

<hr/>

<h2 id="extensibility-and-third-party-libraries">16. Extensibility and Third-Party Libraries</h2>

<p>
The palette model MUST support third-party libraries without breaking the built-in organizational model.
</p>

<p>
Third-party entries SHOULD:
</p>

<ul>
  <li>appear in the namespace view under their own namespace,</li>
  <li>appear in the primary palette under the most relevant intent category when appropriate,</li>
  <li>expose clear library-origin metadata.</li>
</ul>

<p>
Example namespaces:
</p>

<pre>
graiphic.vision.*
graiphic.control.*
vendor.ai.*
</pre>

<p>
A single construct SHOULD have one canonical identity even if the IDE allows multiple discovery paths.
The same construct MUST NOT become semantically duplicated just because it appears in multiple palette views.
</p>

<p>
Third-party ecosystems MAY also provide guided Express entries.
When they do:
</p>

<ul>
  <li>the Express entry MUST still disclose canonical identity,</li>
  <li>the origin of the underlying library SHOULD remain visible,</li>
  <li>the palette MUST keep third-party Express entries distinguishable from baseline standardized entries.</li>
</ul>

<hr/>

<h2 id="validation-and-consistency">17. Validation and Consistency</h2>

<p>
Implementations MUST ensure that all palette access modes remain consistent.
</p>

<p>
In particular:
</p>

<ul>
  <li>the primary palette view, namespace view, search results, contextual insertion paths, and guided / Express lens MUST refer to the same canonical entry space,</li>
  <li>every palette entry MUST resolve to a valid construct known to the active language specification and profile,</li>
  <li>search aliases MUST map back to a canonical entry identity,</li>
  <li>contextual suggestions MUST NOT invent non-existent constructs,</li>
  <li>future or profile-defined groups MUST NOT be presented as baseline standardized families unless they actually are standardized in the active specification set,</li>
  <li>UI, Signal, I/O, Connectivity, and future execution-facing entries MUST remain consistently classified across palette views,</li>
  <li>authoring-facing labels such as <em>If</em>, <em>If / Else</em>, <em>Else If</em>, or <em>Switch</em> MUST resolve to canonical entries rather than independent language constructs when no such independent constructs are standardized,</li>
  <li>Express entries MUST resolve to valid canonical content and MUST NOT become editor-private semantic constructs.</li>
</ul>

<p>
The palette is an IDE presentation mechanism.
It MUST NOT change the source semantics or source identity of the inserted construct.
</p>

<hr/>

<h2 id="examples">18. Examples</h2>

<h3>18.1 Search aliases</h3>

<ul>
  <li><code>if</code> → canonical <code>case</code> structure with boolean selector</li>
  <li><code>if else</code> → canonical <code>case</code> structure with boolean selector</li>
  <li><code>else if</code> → canonical <code>case</code> structure through a derived authoring view</li>
  <li><code>switch</code> → canonical <code>case</code> structure with exact-match branching semantics for the active selector category</li>
  <li><code>for</code> → canonical <code>for_loop</code> structure</li>
  <li><code>while</code> → canonical <code>while_loop</code> structure</li>
  <li><code>+</code> → canonical <code>frog.core.add</code></li>
  <li><code>widget value</code> → canonical <code>widget_value</code> insertion entry</li>
</ul>

<h3>18.2 Contextual suggestions from a <code>bool</code> wire</h3>

<ul>
  <li><code>case</code> (boolean conditional authoring view)</li>
  <li><em>If</em> or <em>If / Else</em> presentation for canonical <code>case</code></li>
  <li><code>frog.core.and</code></li>
  <li><code>frog.core.or</code></li>
  <li><code>frog.core.not</code></li>
  <li><code>frog.core.select</code></li>
</ul>

<h3>18.3 Contextual suggestions from a <code>string</code> wire</h3>

<ul>
  <li><code>case</code> (string selector view)</li>
  <li><em>Switch</em> presentation for canonical <code>case</code></li>
  <li>standardized <code>frog.text.*</code> entries</li>
  <li>text comparison entries</li>
</ul>

<h3>18.4 Contextual suggestions from a widget reference</h3>

<ul>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
</ul>

<h3>18.5 Connectivity discovery examples</h3>

<ul>
  <li><code>python</code> → relevant <code>frog.connectivity.*</code> entry when available</li>
  <li><code>dll</code> → relevant native/shared-library binding entry when available</li>
  <li><code>sql</code> → relevant database connectivity entry when available</li>
  <li><code>.net</code> → relevant .NET connectivity entry when available</li>
</ul>

<h3>18.6 Express discovery examples</h3>

<ul>
  <li><code>read text file</code> → guided Express entry that resolves to a valid canonical I/O target</li>
  <li><code>moving average</code> → canonical signal entry and MAY also surface a guided Express signal entry when available</li>
  <li><code>python call</code> → canonical connectivity entry and MAY also surface a guided Express connectivity entry when available</li>
</ul>

<hr/>

<h2 id="out-of-scope-for-v01">19. Out of Scope for v0.1</h2>

<ul>
  <li>full personalization of ranking algorithms,</li>
  <li>remote cloud palette federation,</li>
  <li>marketplace-style commercial discovery UX,</li>
  <li>cross-project recommendation systems,</li>
  <li>automatic insertion of profile-specific hidden helper nodes,</li>
  <li>semantic transformation of one canonical structure into another language construct,</li>
  <li>a requirement that every future palette family already be fully standardized in v0.1,</li>
  <li>turning authoring-facing aliases such as <em>If</em> or <em>Switch</em> into independent canonical entries without corresponding language standardization,</li>
  <li>requiring execution-facing systems to depend on Express presentation state,</li>
  <li>opaque Express entries whose canonical target cannot be determined by a conforming IDE.</li>
</ul>

<hr/>

<h2 id="summary">20. Summary</h2>

<p>
The FROG IDE palette is the primary discovery and insertion mechanism for diagram entries.
</p>

<ul>
  <li>It provides intent-first browsing, namespace browsing, search, contextual insertion, and optional guided / Express discovery.</li>
  <li>It MUST distinguish primitive entries, structure entries, node-insertion entries, and Express presentations.</li>
  <li>It MUST preserve one canonical identity per construct.</li>
  <li>It SHOULD support aliases such as <code>if</code> for boolean <code>case</code>.</li>
  <li>It MAY expose authoring-facing views such as <em>If</em>, <em>If / Else</em>, <em>Else If</em>, and <em>Switch</em>, but those views MUST resolve to canonical standardized entries.</li>
  <li>It MAY expose task-oriented Express entries, but those entries MUST resolve to valid canonical FROG content.</li>
  <li>It SHOULD expose <code>case</code>, <code>for_loop</code>, and <code>while_loop</code> as the standard control structures of v0.1.</li>
  <li>It SHOULD expose the currently standardized library families of the active repository stage, including <code>frog.signal.*</code>.</li>
  <li>It SHOULD expose UI, I/O, Connectivity, and Signal as distinct palette families.</li>
  <li>It MAY surface reserved or profile-defined future families, but they SHOULD remain clearly marked when not part of the baseline standardized set.</li>
  <li>It MUST remain semantically consistent with the active language specification and profile.</li>
</ul>

<p>
This gives FROG a palette model that is scalable for experts, clear for implementers, intuitive for users working from intent,
and compatible with guided Express-style workflows without creating semantic drift.
</p>
