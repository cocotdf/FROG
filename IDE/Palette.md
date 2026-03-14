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
  <li><a href="#primitive-structure-and-node-insertion-presentation">10. Primitive, Structure, and Node-Insertion Presentation</a></li>
  <li><a href="#palette-categories-for-v01">11. Palette Categories for v0.1</a></li>
  <li><a href="#entry-metadata">12. Entry Metadata</a></li>
  <li><a href="#favorites-recent-and-suggested-entries">13. Favorites, Recent, and Suggested Entries</a></li>
  <li><a href="#stability-and-filtering">14. Stability and Filtering</a></li>
  <li><a href="#extensibility-and-third-party-libraries">15. Extensibility and Third-Party Libraries</a></li>
  <li><a href="#validation-and-consistency">16. Validation and Consistency</a></li>
  <li><a href="#examples">17. Examples</a></li>
  <li><a href="#out-of-scope-for-v01">18. Out of Scope for v0.1</a></li>
  <li><a href="#summary">19. Summary</a></li>
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
The palette therefore serves three complementary roles:
</p>

<ul>
  <li><strong>discovery</strong> — helping users find available constructs and insertion paths,</li>
  <li><strong>navigation</strong> — organizing the catalog in a coherent and scalable way,</li>
  <li><strong>insertion</strong> — allowing rapid placement of primitives, structures, and other source-level entries into the diagram.</li>
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
  <li><strong>Fast insertion</strong> — search and contextual suggestions SHOULD reduce friction.</li>
  <li><strong>Clarity</strong> — primitives, structures, source-node insertions, annotations, and future profile-specific entries MUST NOT be visually conflated.</li>
  <li><strong>Explicit taxonomy boundaries</strong> — UI, I/O, Connectivity, Signal, and future execution-facing families MUST remain conceptually distinct.</li>
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
  <li><code>Expression/Control structures.md</code> — defines structures such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>.</li>
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
  <li><code>IDE/Palette.md</code> defines how a conforming IDE exposes those entries for discovery and insertion.</li>
</ul>

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
A search alias, shortcut, or contextual presentation MUST NOT create a second semantic construct.
</p>

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

<h3>4.5 Primitives, structures, and source-node insertions remain distinct</h3>

<p>
Ordinary primitives such as <code>frog.core.add</code>, structures such as <code>case</code>, and source-node insertions such as
<code>interface_input</code> or <code>widget_value</code> MUST remain visibly distinct in the palette and in search results.
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

<hr/>

<h2 id="palette-access-model">5. Palette Access Model</h2>

<p>
The FROG IDE palette SHOULD expose multiple complementary access paths:
</p>

<ul>
  <li><strong>Primary palette view</strong> — intent-first hierarchical browsing,</li>
  <li><strong>Namespace view</strong> — direct browsing by standardized library namespace and explicit non-library roots,</li>
  <li><strong>Search</strong> — direct textual lookup,</li>
  <li><strong>Contextual insertion</strong> — suggestions derived from the current diagram context.</li>
</ul>

<p>
These are alternative access modes to the same underlying catalog of insertable entries.
They MUST remain semantically consistent with one another.
</p>

<hr/>

<h2 id="primary-palette-view">6. Primary Palette View</h2>

<p>
The primary palette view is the default palette presented to most users.
It is organized around user intent and common graphical programming tasks.
</p>

<p>
Convenience surfaces such as <strong>Favorites</strong>, <strong>Recent</strong>, and <strong>Search</strong> MAY appear at the top of the palette,
but they are not semantic language categories.
</p>

<p>
Recommended top-level primary palette groups for the standardized v0.1 baseline are:
</p>

<pre>
Favorites
Recent
Search

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
  <li>natural-language keyword.</li>
</ul>

<p>
Examples:
</p>

<ul>
  <li>searching <code>add</code> SHOULD find <code>frog.core.add</code>,</li>
  <li>searching <code>+</code> SHOULD also find <code>frog.core.add</code>,</li>
  <li>searching <code>sqrt</code> SHOULD find the relevant <code>frog.math.*</code> entry,</li>
  <li>searching <code>length</code> SHOULD find the relevant <code>frog.collections.*</code> entry,</li>
  <li>searching <code>read text</code> SHOULD find the relevant <code>frog.io.*</code> entry,</li>
  <li>searching <code>moving average</code> SHOULD find the relevant <code>frog.signal.*</code> entry,</li>
  <li>searching <code>if</code> SHOULD find the canonical boolean <code>case</code> structure,</li>
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
  <li>entry-kind relevance,</li>
  <li>contextual relevance,</li>
  <li>recent usage.</li>
</ul>

<p>
The canonical identity of the returned entry MUST remain unchanged.
For example, a search for <code>if</code> returns the canonical <code>case</code> structure rather than a separate language construct named <code>if</code>.
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
Context-aware insertion is an IDE convenience feature.
It MUST NOT alter the language semantics of the inserted construct.
</p>

<hr/>

<h2 id="primitive-structure-and-node-insertion-presentation">10. Primitive, Structure, and Node-Insertion Presentation</h2>

<p>
The palette MUST visually distinguish between:
</p>

<ul>
  <li><strong>primitive entries</strong> — ordinary callable operations defined by primitive libraries,</li>
  <li><strong>structure entries</strong> — diagram regions with owned subgraphs and explicit boundary semantics,</li>
  <li><strong>node-insertion entries</strong> — canonical source nodes or annotations inserted directly into the diagram.</li>
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
  <li><code>widget_reference</code> is a node-insertion entry.</li>
</ul>

<p>
Search results and palette entries SHOULD make this distinction visible through iconography, labeling, badges, grouping, or equivalent UI mechanisms.
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
  <li>For loop structure</li>
  <li>While loop structure</li>
</ul>

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
  <li>entry kind — primitive, structure, node insertion, annotation, or equivalent,</li>
  <li>short description,</li>
  <li>type family,</li>
  <li>statefulness where relevant,</li>
  <li>stability level,</li>
  <li>library origin or specification origin.</li>
</ul>

<p>
Examples of useful badges:
</p>

<ul>
  <li>Primitive</li>
  <li>Structure</li>
  <li>Node Insertion</li>
  <li>Pure</li>
  <li>Stateful</li>
  <li>Signal</li>
  <li>UI</li>
  <li>I/O</li>
  <li>Connectivity</li>
  <li>Experimental</li>
  <li>Third-party</li>
  <li>Profile-defined</li>
</ul>

<hr/>

<h2 id="favorites-recent-and-suggested-entries">13. Favorites, Recent, and Suggested Entries</h2>

<p>
The palette SHOULD support the following convenience groups:
</p>

<h3>13.1 Favorites</h3>

<p>
User-pinned entries for fast access.
</p>

<h3>13.2 Recent</h3>

<p>
Recently inserted entries.
</p>

<h3>13.3 Suggested</h3>

<p>
Entries recommended by the IDE based on context, type, structure location, or recent activity.
</p>

<p>
These convenience groups are optional IDE features.
They MUST NOT alter the canonical identity of the underlying entries.
</p>

<hr/>

<h2 id="stability-and-filtering">14. Stability and Filtering</h2>

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
  <li>specification origin.</li>
</ul>

<p>
This helps keep the beginner experience clean while still exposing the full active surface to advanced users.
</p>

<hr/>

<h2 id="extensibility-and-third-party-libraries">15. Extensibility and Third-Party Libraries</h2>

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

<hr/>

<h2 id="validation-and-consistency">16. Validation and Consistency</h2>

<p>
Implementations MUST ensure that all palette access modes remain consistent.
</p>

<p>
In particular:
</p>

<ul>
  <li>the primary palette view, namespace view, search results, and contextual insertion paths MUST refer to the same canonical entries,</li>
  <li>every palette entry MUST resolve to a valid construct known to the active language specification and profile,</li>
  <li>search aliases MUST map back to a canonical entry identity,</li>
  <li>contextual suggestions MUST NOT invent non-existent constructs,</li>
  <li>future or profile-defined groups MUST NOT be presented as baseline standardized families unless they actually are standardized in the active specification set,</li>
  <li>UI, Signal, I/O, Connectivity, and future execution-facing entries MUST remain consistently classified across palette views.</li>
</ul>

<p>
The palette is an IDE presentation mechanism.
It MUST NOT change the source semantics or source identity of the inserted construct.
</p>

<hr/>

<h2 id="examples">17. Examples</h2>

<h3>17.1 Search aliases</h3>

<ul>
  <li><code>if</code> → canonical <code>case</code> structure with boolean selector</li>
  <li><code>else</code> → canonical <code>case</code> structure with boolean selector</li>
  <li><code>for</code> → canonical <code>for_loop</code> structure</li>
  <li><code>while</code> → canonical <code>while_loop</code> structure</li>
  <li><code>+</code> → canonical <code>frog.core.add</code></li>
  <li><code>widget value</code> → canonical <code>widget_value</code> insertion entry</li>
</ul>

<h3>17.2 Contextual suggestions from a <code>bool</code> wire</h3>

<ul>
  <li><code>case</code> (boolean conditional view)</li>
  <li><code>frog.core.and</code></li>
  <li><code>frog.core.or</code></li>
  <li><code>frog.core.not</code></li>
  <li><code>frog.core.select</code></li>
</ul>

<h3>17.3 Contextual suggestions from a <code>string</code> wire</h3>

<ul>
  <li><code>case</code> (string selector view)</li>
  <li>standardized <code>frog.text.*</code> entries</li>
  <li>text comparison entries</li>
</ul>

<h3>17.4 Contextual suggestions from a widget reference</h3>

<ul>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
</ul>

<h3>17.5 Connectivity discovery examples</h3>

<ul>
  <li><code>python</code> → relevant <code>frog.connectivity.*</code> entry when available</li>
  <li><code>dll</code> → relevant native/shared-library binding entry when available</li>
  <li><code>sql</code> → relevant database connectivity entry when available</li>
  <li><code>.net</code> → relevant .NET connectivity entry when available</li>
</ul>

<hr/>

<h2 id="out-of-scope-for-v01">18. Out of Scope for v0.1</h2>

<ul>
  <li>full personalization of ranking algorithms,</li>
  <li>remote cloud palette federation,</li>
  <li>marketplace-style commercial discovery UX,</li>
  <li>cross-project recommendation systems,</li>
  <li>automatic insertion of profile-specific hidden helper nodes,</li>
  <li>semantic transformation of one canonical structure into another language construct,</li>
  <li>a requirement that every future palette family already be fully standardized in v0.1.</li>
</ul>

<hr/>

<h2 id="summary">19. Summary</h2>

<p>
The FROG IDE palette is the primary discovery and insertion mechanism for diagram entries.
</p>

<ul>
  <li>It provides intent-first browsing, namespace browsing, search, and contextual insertion.</li>
  <li>It MUST distinguish primitive entries, structure entries, and node-insertion entries.</li>
  <li>It MUST preserve one canonical identity per construct.</li>
  <li>It SHOULD support aliases such as <code>if</code> for boolean <code>case</code>.</li>
  <li>It SHOULD expose <code>case</code>, <code>for_loop</code>, and <code>while_loop</code> as the standard control structures of v0.1.</li>
  <li>It SHOULD expose the currently standardized library families of the active repository stage, including <code>frog.signal.*</code>.</li>
  <li>It SHOULD expose UI, I/O, Connectivity, and Signal as distinct palette families.</li>
  <li>It MAY surface reserved or profile-defined future families, but they SHOULD remain clearly marked when not part of the baseline standardized set.</li>
  <li>It MUST remain semantically consistent with the active language specification and profile.</li>
</ul>

<p>
This gives FROG a palette model that is scalable for experts, clear for implementers, and intuitive for users working from intent.
</p>
