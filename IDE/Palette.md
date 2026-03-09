<h1 align="center">🐸 FROG IDE Palette Specification</h1>

<p align="center">
Definition of the function and structure palette for the FROG IDE<br/>
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
  <li><a href="#favorites-recent-and-suggested">13. Favorites, Recent, and Suggested Entries</a></li>
  <li><a href="#stability-and-filtering">14. Stability and Filtering</a></li>
  <li><a href="#extensibility-and-third-party-libraries">15. Extensibility and Third-Party Libraries</a></li>
  <li><a href="#validation-and-consistency">16. Validation and Consistency</a></li>
  <li><a href="#examples">17. Examples</a></li>
  <li><a href="#out-of-scope">18. Out of Scope for v0.1</a></li>
  <li><a href="#summary">19. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The FROG IDE palette is the primary user-facing mechanism used to discover, search, understand, and insert functions and structures into a diagram.
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
The FROG palette is intentionally designed to do better than traditional historical palettes that grew from implementation history rather than from user intent.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Intent-first navigation</strong> — users should be able to find what they want by purpose, not only by internal implementation category.</li>
  <li><strong>Namespace consistency</strong> — the palette should still reflect the actual language namespace model.</li>
  <li><strong>Fast insertion</strong> — search and contextual suggestions should reduce friction.</li>
  <li><strong>Clarity</strong> — functions, structures, UI operations, and runtime tools should not be visually conflated.</li>
  <li><strong>Scalability</strong> — the model must remain usable as FROG grows from a minimal core to richer libraries.</li>
  <li><strong>Extensibility</strong> — third-party libraries must integrate cleanly without breaking the palette model.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This document complements the following specifications:
</p>

<ul>
  <li><strong>Libraries/Core.md</strong> — defines the minimal built-in function catalog such as <code>frog.core.add</code> and <code>frog.core.delay</code>.</li>
  <li><strong>Language/Control structures.md</strong> — defines structures such as <code>case</code> and <code>loop</code>.</li>
  <li><strong>Expression/Diagram.md</strong> — defines how inserted functions and structures appear in the program source and diagram model.</li>
  <li><strong>Expression/Widget interaction.md</strong> — defines UI interaction functions such as widget property access and method invocation.</li>
</ul>

<p>
This document defines how the IDE presents language constructs to the user.
It does not define the language semantics of those constructs.
</p>

<hr/>

<h2 id="design-principles">4. Design Principles</h2>

<p>
The FROG palette follows the following principles:
</p>

<h3>4.1 Intent before implementation</h3>

<p>
The primary palette should be organized according to user intent such as:
</p>

<ul>
  <li>do arithmetic,</li>
  <li>compare values,</li>
  <li>repeat execution,</li>
  <li>interact with a widget,</li>
  <li>read a file,</li>
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
Search is a primary insertion path and must be treated as a first-class mechanism.
</p>

<h3>4.4 Functions and structures are distinct</h3>

<p>
Ordinary functions such as <code>frog.core.add</code> and structural constructs such as <code>loop</code> must remain visibly distinct in the palette and in search results.
</p>

<h3>4.5 Context improves speed</h3>

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
Concurrency &amp; Runtime
External
</pre>

<p>
This structure is deliberately task-oriented rather than history-oriented.
It should remain compact enough for browsing while still scaling as new libraries are introduced.
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
  <li>searching <code>add</code> should find <code>frog.core.add</code>,</li>
  <li>searching <code>+</code> should also find <code>frog.core.add</code>,</li>
  <li>searching <code>if</code> should find the case structure or equivalent conditional structure,</li>
  <li>searching <code>property write</code> should find the relevant widget interaction entry,</li>
  <li>searching <code>relu</code> should find the corresponding ONNX or tensor entry when available.</li>
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
  <li>from a widget reference, prefer property and method interaction suggestions,</li>
  <li>from a value feedback path, prefer <code>frog.core.delay</code>,</li>
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
  <li><code>loop</code> is a structure.</li>
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
  <li>Loop structure</li>
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
This group is intended for future tensor and ONNX-related functions and should remain separate from <code>frog.core</code>.
</p>

<h3>11.9 UI</h3>

<ul>
  <li>widget value insertion</li>
  <li>widget reference insertion</li>
  <li>property read</li>
  <li>property write</li>
  <li>method invoke</li>
</ul>

<h3>11.10 I/O</h3>

<p>
This group is intended for file, path, serialization, network, and hardware I/O families defined later.
</p>

<h3>11.11 Concurrency &amp; Runtime</h3>

<p>
This group is intended for future runtime coordination mechanisms such as queues, channels, tasks, and system-level execution tools.
</p>

<h3>11.12 External</h3>

<p>
This group is intended for future integrations such as Python, C/C++, .NET, or external runtime bindings.
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
  <li><strong>display name</strong></li>
  <li><strong>namespace-qualified name</strong></li>
  <li><strong>entry kind</strong> — function or structure</li>
  <li><strong>short description</strong></li>
  <li><strong>type family</strong></li>
  <li><strong>statefulness</strong></li>
  <li><strong>stability level</strong></li>
  <li><strong>library origin</strong></li>
</ul>

<p>
Examples of useful badges:
</p>

<ul>
  <li><strong>Pure</strong></li>
  <li><strong>Stateful</strong></li>
  <li><strong>UI</strong></li>
  <li><strong>ONNX</strong></li>
  <li><strong>Experimental</strong></li>
  <li><strong>Third-party</strong></li>
</ul>

<hr/>

<h2 id="favorites-recent-and-suggested">13. Favorites, Recent, and Suggested Entries</h2>

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
  <li><strong>Stable</strong></li>
  <li><strong>Advanced</strong></li>
  <li><strong>Experimental</strong></li>
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
A single function SHOULD have one canonical identity even if the IDE allows multiple discovery paths.
The same function must not become semantically duplicated just because it appears in multiple palette views.
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
  <li>every palette entry MUST resolve to a valid function or structure definition known to the active language profile,</li>
  <li>search aliases MUST map back to a canonical entry identity,</li>
  <li>contextual suggestions MUST NOT invent non-existent constructs.</li>
</ul>

<p>
The palette is an IDE presentation mechanism.
It MUST NOT change the source semantics of the inserted construct.
</p>

<hr/>

<h2 id="examples">17. Examples</h2>

<h3>17.1 Finding addition</h3>

<p>
A user may find addition through:
</p>

<ul>
  <li>Primary palette → <strong>Math &amp; Logic</strong> → <code>frog.core.add</code></li>
  <li>Namespace view → <strong>frog.core.*</strong> → <code>frog.core.add</code></li>
  <li>Search → <code>add</code></li>
  <li>Search → <code>+</code></li>
</ul>

<p>
All of these paths must lead to the same canonical function.
</p>

<h3>17.2 Finding delayed feedback</h3>

<p>
A user may find delayed feedback through:
</p>

<ul>
  <li>Primary palette → <strong>State &amp; Timing</strong> → <code>frog.core.delay</code></li>
  <li>Namespace view → <strong>frog.core.*</strong> → <code>frog.core.delay</code></li>
  <li>Contextual insertion from a feedback wire suggestion</li>
</ul>

<h3>17.3 Finding a loop</h3>

<p>
A user may find a loop through:
</p>

<ul>
  <li>Primary palette → <strong>Flow Control</strong> → <code>loop</code></li>
  <li>Search → <code>loop</code></li>
  <li>Search → <code>for</code> or <code>while</code> when the IDE supports those aliases or profile-specific forms</li>
</ul>

<p>
The IDE must present it as a structure, not as an ordinary function.
</p>

<h3>17.4 Widget property access</h3>

<p>
A user may find widget interaction through:
</p>

<ul>
  <li>Primary palette → <strong>UI</strong> → <code>property read</code></li>
  <li>Primary palette → <strong>UI</strong> → <code>property write</code></li>
  <li>Contextual insertion from a widget reference</li>
  <li>Search → <code>property write</code></li>
</ul>

<hr/>

<h2 id="out-of-scope">18. Out of Scope for v0.1</h2>

<p>
The following topics are outside the strict scope of this document in v0.1:
</p>

<ul>
  <li>precise visual styling of every palette widget,</li>
  <li>full adaptive ranking algorithms for search results,</li>
  <li>AI-assisted palette recommendations,</li>
  <li>full plugin marketplace integration,</li>
  <li>full localization rules for every language,</li>
  <li>exact drag-and-drop animation behavior,</li>
  <li>exact touch-optimized mobile palette interactions.</li>
</ul>

<hr/>

<h2 id="summary">19. Summary</h2>

<p>
The FROG IDE palette is designed to expose the language in a way that is both scalable and intuitive.
</p>

<p>
This specification establishes that:
</p>

<ul>
  <li>the primary palette is organized by user intent,</li>
  <li>a namespace view exposes the true language library organization,</li>
  <li>search is a first-class insertion path,</li>
  <li>context-aware insertion improves speed without changing semantics,</li>
  <li>functions and structures remain clearly distinct,</li>
  <li>third-party libraries integrate through the same model.</li>
</ul>

<p>
This gives FROG a palette architecture that remains more coherent, more discoverable, and more extensible than historically grown palettes, while still feeling natural to users of graphical programming environments.
</p>

<hr/>

<p align="center">
End of FROG IDE Palette Specification
</p>
