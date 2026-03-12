<h1 align="center">🐸 FROG IDE Palette Specification</h1>

<p align="center">
Definition of the function, structure, and library palette for the FROG IDE<br/>
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
  <li><a href="#function-vs-structure-presentation">10. Function vs Structure Presentation</a></li>
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
The FROG IDE palette is the primary user-facing mechanism used to discover, search, understand, and insert functions, structures, and related language entries into a diagram.
</p>

<p>
Its purpose is not only to expose the language catalog, but to expose it in a way that matches how users actually think when building a graphical program.
</p>

<p>
The palette therefore serves three complementary roles:
</p>

<ul>
  <li><strong>discovery</strong> — helping users find available language constructs,</li>
  <li><strong>navigation</strong> — organizing the catalog in a coherent and scalable way,</li>
  <li><strong>insertion</strong> — allowing rapid placement of functions and structures into the diagram.</li>
</ul>

<p>
The FROG palette is intentionally designed to avoid the historical drift of palettes that became implementation-driven rather than intent-driven.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Intent-first navigation</strong> — users SHOULD be able to find what they want by purpose, not only by internal implementation category.</li>
  <li><strong>Namespace consistency</strong> — the palette SHOULD still reflect the actual language namespace model.</li>
  <li><strong>Fast insertion</strong> — search and contextual suggestions SHOULD reduce friction.</li>
  <li><strong>Clarity</strong> — functions, structures, UI operations, I/O operations, connectivity operations, and runtime tools MUST NOT be visually conflated.</li>
  <li><strong>Explicit taxonomy boundaries</strong> — UI, I/O, Connectivity, and Runtime families MUST remain conceptually distinct.</li>
  <li><strong>Scalability</strong> — the model MUST remain usable as FROG grows from a minimal core to richer libraries.</li>
  <li><strong>Extensibility</strong> — third-party libraries MUST integrate cleanly without breaking the palette model.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This document complements the following specifications:
</p>

<ul>
  <li><code>Libraries/Core.md</code> — defines the minimal built-in primitive catalog such as <code>frog.core.add</code> and <code>frog.core.delay</code>.</li>
  <li><code>Expression/Control structures.md</code> — defines structures such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>.</li>
  <li><code>Expression/Diagram.md</code> — defines how inserted functions, structures, and related nodes appear in the program source and diagram model.</li>
  <li><code>Expression/Widget interaction.md</code> — defines canonical UI interaction primitives such as widget property access and method invocation.</li>
  <li><code>Expression/Front panel.md</code> and <code>Expression/Widget.md</code> — define the front-panel and widget model that inform UI-related palette entries.</li>
</ul>

<p>
This document defines how the IDE presents language constructs to the user.
It does not define the language semantics of those constructs.
</p>

<p>
When additional standard library documents exist for namespaces such as <code>frog.ui.*</code>, <code>frog.io.*</code>, or <code>frog.connectivity.*</code>, the palette MUST remain consistent with those library specifications.
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
  <li>interact with a widget,</li>
  <li>read a file,</li>
  <li>connect to Python or SQL,</li>
  <li>use ONNX operators.</li>
</ul>

<h3>4.2 Namespace remains visible</h3>

<p>
Although the primary palette is intent-first, the true language namespace remains important.
The IDE MUST therefore also provide a namespace-oriented view.
</p>

<h3>4.3 Search is first-class</h3>

<p>
The palette is not only a tree.
Search is a primary insertion path and MUST be treated as a first-class mechanism.
</p>

<h3>4.4 Functions and structures are distinct</h3>

<p>
Ordinary functions such as <code>frog.core.add</code> and structural constructs such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code> MUST remain visibly distinct in the palette and in search results.
</p>

<h3>4.5 Taxonomy boundaries remain explicit</h3>

<p>
The palette MUST keep the following boundaries explicit:
</p>

<ul>
  <li><strong>UI</strong> — widget-facing interaction and UI-related insertion paths,</li>
  <li><strong>I/O</strong> — file, path, resource, serialization, network, and hardware I/O,</li>
  <li><strong>Connectivity</strong> — Python, native/shared library, C/C++, .NET, SQL, and external runtime/service bindings,</li>
  <li><strong>Concurrency &amp; Runtime</strong> — runtime coordination and execution tools.</li>
</ul>

<p>
These groups MAY interact in real programs, but the palette SHOULD present them as distinct conceptual families.
</p>

<h3>4.6 Context improves speed</h3>

<p>
The IDE SHOULD use type context, wire context, and insertion context to improve suggestions without changing language semantics.
</p>

<h3>4.7 Canonical identity remains singular</h3>

<p>
A language construct MAY appear in multiple discovery paths, but it MUST keep one canonical identity.
A search alias or palette shortcut MUST NOT create a second semantic construct.
</p>

<hr/>

<h2 id="palette-access-model">5. Palette Access Model</h2>

<p>
The FROG IDE palette SHOULD expose multiple complementary access paths:
</p>

<ul>
  <li><strong>Primary palette view</strong> — intent-first hierarchical browsing,</li>
  <li><strong>Namespace view</strong> — direct browsing by library namespace,</li>
  <li><strong>Search</strong> — direct textual lookup,</li>
  <li><strong>Contextual insertion</strong> — suggestions derived from the current diagram context.</li>
</ul>

<p>
These are alternative access modes to the same language catalog.
They MUST remain semantically consistent with one another.
</p>

<hr/>

<h2 id="primary-palette-view">6. Primary Palette View</h2>

<p>
The primary palette view is the default palette presented to most users.
It is organized around user intent and common graphical programming tasks.
</p>

<p>
Recommended top-level primary palette groups:
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
Tensor &amp; ONNX
UI
I/O
Connectivity
Concurrency &amp; Runtime
</pre>

<p>
This structure is deliberately task-oriented rather than implementation-history-oriented.
It SHOULD remain compact enough for browsing while still scaling as new libraries are introduced.
</p>

<hr/>

<h2 id="namespace-view">7. Namespace View</h2>

<p>
The namespace view exposes the actual library organization of the language.
</p>

<p>
In this view, entries are grouped by namespace such as:
</p>

<pre>
frog.core.*
frog.math.*
frog.tensor.*
frog.signal.*
frog.ui.*
frog.io.*
frog.connectivity.*
frog.runtime.*
frog.onnx.*
</pre>

<p>
This view is important for:
</p>

<ul>
  <li>advanced users,</li>
  <li>documentation consistency,</li>
  <li>third-party library integration,</li>
  <li>exact function lookup.</li>
</ul>

<p>
The namespace view SHOULD coexist with the primary palette view.
It MUST NOT replace it.
</p>

<hr/>

<h2 id="search-model">8. Search Model</h2>

<p>
Search is a primary palette feature.
Users SHOULD be able to search by:
</p>

<ul>
  <li>function name,</li>
  <li>structure name,</li>
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
  <li>searching <code>if</code> SHOULD find the canonical boolean <code>case</code> structure,</li>
  <li>searching <code>else</code> SHOULD also help surface the canonical boolean <code>case</code> structure,</li>
  <li>searching <code>case</code> SHOULD find the canonical <code>case</code> structure,</li>
  <li>searching <code>for</code> SHOULD find <code>for_loop</code>,</li>
  <li>searching <code>while</code> SHOULD find <code>while_loop</code>,</li>
  <li>searching <code>property write</code> SHOULD find the relevant widget interaction entry,</li>
  <li>searching <code>python</code> SHOULD find the relevant connectivity entry when available,</li>
  <li>searching <code>sql</code> SHOULD find the relevant connectivity entry when available,</li>
  <li>searching <code>relu</code> SHOULD find the corresponding ONNX or tensor entry when available.</li>
</ul>

<p>
Search SHOULD rank results using at least:
</p>

<ul>
  <li>exact name match,</li>
  <li>namespace-qualified match,</li>
  <li>alias match,</li>
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
  <li>invoking insertion from a widget reference or widget value node.</li>
</ul>

<p>
Examples:
</p>

<ul>
  <li>from a <code>bool</code> wire, prefer logic and conditional suggestions,</li>
  <li>from a numeric wire, prefer arithmetic and comparison suggestions,</li>
  <li>from a <code>string</code> wire, prefer text operations and string-based <code>case</code> suggestions,</li>
  <li>from a widget reference, prefer property and method interaction suggestions,</li>
  <li>from a value feedback path, prefer <code>frog.core.delay</code>,</li>
  <li>from a path-like or file-related context, prefer I/O suggestions,</li>
  <li>from a connectivity-related insertion path, prefer Python, native binding, .NET, or SQL suggestions,</li>
  <li>from a tensor wire, prefer tensor and ONNX suggestions.</li>
</ul>

<p>
Context-aware insertion is an IDE convenience feature.
It MUST NOT alter the language semantics of the inserted construct.
</p>

<hr/>

<h2 id="function-vs-structure-presentation">10. Function vs Structure Presentation</h2>

<p>
The palette MUST visually distinguish between:
</p>

<ul>
  <li><strong>functions</strong> — ordinary callable operations,</li>
  <li><strong>structures</strong> — diagram regions with internal subgraphs and boundary semantics.</li>
</ul>

<p>
Examples:
</p>

<ul>
  <li><code>frog.core.add</code> is a function,</li>
  <li><code>frog.core.delay</code> is a stateful function,</li>
  <li><code>case</code> is a structure,</li>
  <li><code>for_loop</code> is a structure,</li>
  <li><code>while_loop</code> is a structure.</li>
</ul>

<p>
Search results and palette entries SHOULD make this distinction visible through iconography, labeling, badges, or grouping.
</p>

<hr/>

<h2 id="palette-categories-for-v01">11. Palette Categories for v0.1</h2>

<p>
The following palette layout is recommended for FROG v0.1.
</p>

<h3>11.1 Program Structure</h3>

<ul>
  <li>Sub-FROG insertion</li>
  <li>Interface boundary nodes</li>
  <li>Comments</li>
  <li>Documentation annotations</li>
  <li>Regions</li>
</ul>

<h3>11.2 Flow Control</h3>

<ul>
  <li>Case structure</li>
  <li>For loop structure</li>
  <li>While loop structure</li>
</ul>

<h3>11.3 State &amp; Timing</h3>

<ul>
  <li><code>frog.core.delay</code></li>
  <li>future timing-related structures or functions</li>
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
</ul>

<h3>11.5 Data &amp; Types</h3>

<ul>
  <li>type conversion entries</li>
  <li>cast entries</li>
  <li>future optional/value wrappers</li>
</ul>

<h3>11.6 Collections</h3>

<p>
Collection-oriented entries MAY remain minimal in v0.1 if not yet standardized.
This group is included to preserve long-term palette coherence.
</p>

<h3>11.7 Text</h3>

<p>
Text-related entries MAY remain minimal in v0.1 if not yet standardized.
</p>

<h3>11.8 Tensor &amp; ONNX</h3>

<p>
This group is intended for future tensor and ONNX-related functions and SHOULD remain separate from <code>frog.core</code>.
</p>

<h3>11.9 UI</h3>

<ul>
  <li>widget value insertion</li>
  <li>widget reference insertion</li>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
</ul>

<p>
This group is intended for widget-facing interaction and UI-related insertion paths.
It SHOULD NOT absorb file I/O, database access, Python bindings, or general external interop.
</p>

<h3>11.10 I/O</h3>

<p>
This group is intended for file, path, resource, serialization, network, and hardware I/O families defined later.
</p>

<p>
It SHOULD cover operations whose primary role is reading from, writing to, opening, closing, or transforming an I/O resource.
It SHOULD NOT absorb Python, native/shared library, .NET, SQL, or general external service bindings.
</p>

<h3>11.11 Connectivity</h3>

<p>
This group is intended for future integrations such as:
</p>

<ul>
  <li>Python bindings,</li>
  <li>native/shared library bindings,</li>
  <li>C/C++ bindings,</li>
  <li>.NET bindings,</li>
  <li>SQL and database connectivity,</li>
  <li>external runtime or service bindings.</li>
</ul>

<p>
This group exists to keep interop and external binding workflows explicit instead of collapsing them into a generic and ambiguous external bucket.
</p>

<h3>11.12 Concurrency &amp; Runtime</h3>

<p>
This group is intended for future runtime coordination mechanisms such as queues, channels, tasks, schedulers, synchronization tools, and system-level execution utilities.
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
  <li>namespace-qualified name,</li>
  <li>entry kind — function or structure,</li>
  <li>short description,</li>
  <li>type family,</li>
  <li>statefulness,</li>
  <li>stability level,</li>
  <li>library origin.</li>
</ul>

<p>
Examples of useful badges:
</p>

<ul>
  <li>Pure</li>
  <li>Stateful</li>
  <li>UI</li>
  <li>I/O</li>
  <li>Connectivity</li>
  <li>ONNX</li>
  <li>Experimental</li>
  <li>Third-party</li>
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
They MUST NOT alter the canonical identity of the underlying functions or structures.
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
</ul>

<p>
The palette MAY also support filtering by:
</p>

<ul>
  <li>namespace,</li>
  <li>entry kind,</li>
  <li>type family,</li>
  <li>statefulness,</li>
  <li>library origin.</li>
</ul>

<p>
This helps keep the beginner experience clean while still exposing the full language surface to advanced users.
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
A single function or structure SHOULD have one canonical identity even if the IDE allows multiple discovery paths.
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
  <li>the primary palette view, namespace view, and search results MUST refer to the same canonical language entries,</li>
  <li>every palette entry MUST resolve to a valid function or structure definition known to the active language specification and profile,</li>
  <li>search aliases MUST map back to a canonical entry identity,</li>
  <li>contextual suggestions MUST NOT invent non-existent constructs,</li>
  <li>UI, I/O, Connectivity, and Runtime entries MUST remain consistently classified across palette views.</li>
</ul>

<p>
The palette is an IDE presentation mechanism.
It MUST NOT change the source semantics of the inserted construct.
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
  <li>text comparison entries</li>
  <li>future string manipulation entries</li>
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
  <li><code>dll</code> → relevant native/shared library binding entry when available</li>
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
The FROG IDE palette is the primary discovery and insertion mechanism for language constructs.
</p>

<ul>
  <li>It provides intent-first browsing, namespace browsing, search, and contextual insertion.</li>
  <li>It MUST distinguish functions from structures.</li>
  <li>It MUST preserve one canonical identity per language construct.</li>
  <li>It SHOULD support aliases such as <code>if</code> for boolean <code>case</code>.</li>
  <li>It SHOULD expose <code>case</code>, <code>for_loop</code>, and <code>while_loop</code> as the standard control structures of v0.1.</li>
  <li>It SHOULD expose UI, I/O, Connectivity, and Concurrency &amp; Runtime as distinct palette families.</li>
  <li>It MUST remain semantically consistent with the active language specification and profile.</li>
</ul>

<p>
This gives FROG a palette model that is both scalable for experts and intuitive for users working from intent.
</p>
