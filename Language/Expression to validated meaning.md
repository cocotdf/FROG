<h1>FROG Expression to Validated Meaning</h1>

<p><strong>Normative boundary from canonical <code>.frog</code> source to validated program meaning</strong><br>
FROG — Free Open Graphical Language</p>

<hr>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-document-exists">2. Why this Document Exists</a></li>
  <li><a href="#scope-of-this-document">3. Scope of this Document</a></li>
  <li><a href="#relation-with-other-specifications">4. Relation with Other Specifications</a></li>
  <li><a href="#boundary-being-defined">5. Boundary Being Defined</a></li>
  <li><a href="#inputs-to-validation">6. Inputs to Validation</a></li>
  <li><a href="#validation-result">7. Validation Result</a></li>
  <li><a href="#core-boundary-invariants">8. Core Boundary Invariants</a></li>
  <li><a href="#source-families-and-meaning-ownership">9. Source Families and Meaning Ownership</a></li>
  <li><a href="#execution-relevant-source-content">10. Execution-Relevant Source Content</a></li>
  <li><a href="#non-semantic-or-non-authoritative-source-content">11. Non-Semantic or Non-Authoritative Source Content</a></li>
  <li><a href="#interface-diagram-and-front-panel-participation">12. Interface, Diagram, and Front-Panel Participation</a></li>
  <li><a href="#structures-state-and-cycles">13. Structures, State, and Cycles</a></li>
  <li><a href="#type-value-and-state-commitments">14. Type, Value, and State Commitments</a></li>
  <li><a href="#attribution-and-recoverability-at-the-semantic-boundary">15. Attribution and Recoverability at the Semantic Boundary</a></li>
  <li><a href="#forbidden-boundary-collapses">16. Forbidden Boundary Collapses</a></li>
  <li><a href="#relation-with-ir-derivation">17. Relation with IR Derivation</a></li>
  <li><a href="#out-of-scope-for-v01">18. Out of Scope for v0.1</a></li>
  <li><a href="#summary">19. Summary</a></li>
</ul>

<hr>

<h2 id="overview">1. Overview</h2>

<p>This document defines the normative boundary between canonical FROG source representation and validated FROG program meaning.</p>

<p>It specifies:</p>
<ul>
  <li>which source-visible families participate in validated execution meaning,</li>
  <li>which source-visible families remain source-only,</li>
  <li>which distinctions MUST remain semantically recoverable after validation,</li>
  <li>which source-side information is required before IR derivation may begin,</li>
  <li>which source-side information MUST NOT be mistaken for semantic authority.</li>
</ul>

<p>The repository architecture is:</p>

<pre><code>Expression/   -&gt; canonical source form
Language/     -&gt; validated program meaning
IR/           -&gt; open execution-facing representation
Lowering      -&gt; target-family-oriented specialization
Backend       -&gt; backend-facing standardized handoff
Runtime       -&gt; private realization
</code></pre>

<p>This document governs the first normative transition in that chain:</p>

<pre><code>canonical .frog source
        |
        v
validated program meaning
</code></pre>

<p>This is not an IR derivation document.<br>
This is not a source-schema document.<br>
This is not a runtime note.<br>
This is the semantic bridge between source and meaning.</p>

<hr>

<h2 id="why-this-document-exists">2. Why this Document Exists</h2>

<p>A canonical source format is not yet validated meaning.</p>

<p>A <code>.frog</code> file may serialize:</p>
<ul>
  <li>required executable structure,</li>
  <li>public interface declarations,</li>
  <li>optional front-panel composition,</li>
  <li>connector projection,</li>
  <li>icon material,</li>
  <li>IDE-facing recoverability data,</li>
  <li>cache-like derived support data.</li>
</ul>

<p>Those source families do not all have the same architectural role.</p>

<p>Without a dedicated source-to-meaning boundary, architectural drift appears quickly:</p>

<pre><code>Expression/ becomes semantic authority
IR/ becomes the first "real" execution truth
validator behavior becomes hidden language law
runtime shortcuts redefine the language
IDE-facing metadata leaks into semantics
</code></pre>

<p>This document prevents that drift by making the boundary explicit:</p>

<pre><code>Expression/   -&gt; what is written
Language/     -&gt; what the validated program means
IR/           -&gt; what may later be derived
</code></pre>

<p>The purpose of this document is therefore to make validation semantically meaningful without collapsing source, semantics, and execution representation into one layer.</p>

<hr>

<h2 id="scope-of-this-document">3. Scope of this Document</h2>

<p>This document owns the normative correspondence between canonical source and validated program meaning.</p>

<p>It defines:</p>
<ul>
  <li>what validation must establish before a program has language-level meaning,</li>
  <li>which source families contribute to validated program meaning,</li>
  <li>which distinctions must remain preserved at the semantic boundary,</li>
  <li>which source families remain non-semantic or non-authoritative,</li>
  <li>what semantic commitments exist before IR derivation.</li>
</ul>

<p>This document does <strong>NOT</strong> own:</p>
<ul>
  <li>full <code>.frog</code> file structure or serialization details,</li>
  <li>primitive-local behavior catalogs,</li>
  <li>optional profile capability behavior,</li>
  <li>open IR structure or material IR construction,</li>
  <li>lowering strategy,</li>
  <li>runtime-private representation,</li>
  <li>IDE UX behavior.</li>
</ul>

<p>Accordingly:</p>

<pre><code>This document MUST NOT redefine source serialization.
This document MUST NOT redefine primitive catalogs.
This document MUST NOT redefine IR wire shape.
This document MUST NOT redefine backend/runtime internals.
This document MUST define what source validation establishes as program meaning.
</code></pre>

<hr>

<h2 id="relation-with-other-specifications">4. Relation with Other Specifications</h2>

<p>This document should be read together with:</p>
<ul>
  <li><code>Expression/Readme.md</code></li>
  <li><code>Expression/Diagram.md</code></li>
  <li><code>Expression/Interface.md</code></li>
  <li><code>Expression/Front panel.md</code></li>
  <li><code>Expression/Widget interaction.md</code></li>
  <li><code>Expression/Control structures.md</code></li>
  <li><code>Expression/State and cycles.md</code></li>
  <li><code>Expression/Type.md</code></li>
  <li><code>Language/Control structures.md</code></li>
  <li><code>Language/State and cycles.md</code></li>
  <li><code>Language/Execution model.md</code></li>
  <li><code>Language/Execution control and observation boundaries.md</code></li>
  <li><code>IR/Derivation rules.md</code></li>
  <li><code>IR/Identity and Mapping.md</code></li>
  <li>relevant <code>Libraries/</code> documents</li>
  <li>relevant <code>Profiles/</code> documents when optional standardized capability families are used</li>
</ul>

<p>Ownership remains:</p>

<pre><code>Expression/   -&gt; source structure and source-visible families
Language/     -&gt; validated semantic meaning
IR/           -&gt; open execution-facing representation
Libraries/    -&gt; intrinsic primitives
Profiles/     -&gt; optional standardized capabilities
IDE/          -&gt; authoring, observability, debugging, tooling UX
</code></pre>

<p>Accordingly:</p>
<ul>
  <li><code>Expression/</code> defines how the program is represented in canonical source.</li>
  <li><code>Language/</code> defines what a validated program means.</li>
  <li><code>IR/</code> defines what execution-facing representation may be derived from that meaning.</li>
</ul>

<hr>

<h2 id="boundary-being-defined">5. Boundary Being Defined</h2>

<p>The boundary defined here is:</p>

<pre><code>canonical .frog source
        +
applicable source validation
        +
applicable type validation
        +
applicable primitive/library validation
        +
applicable profile validation
        +
applicable semantic validation
        |
        v
validated program meaning
</code></pre>

<p>This boundary has two outputs:</p>
<ul>
  <li>a conforming determination that the program is valid and semantically meaningful, or</li>
  <li>a conforming determination that the source does not establish valid program meaning.</li>
</ul>

<p>No conforming implementation may claim validated program meaning if applicable validation has not succeeded.</p>

<p>The boundary is therefore not merely syntactic. It establishes the minimum semantic truth that later IR derivation, conformance, observability, and implementations depend on.</p>

<hr>

<h2 id="inputs-to-validation">6. Inputs to Validation</h2>

<p>Before validated program meaning exists, a conforming implementation MUST evaluate all applicable validation obligations, including at minimum:</p>

<ul>
  <li>source-shape validation,</li>
  <li>required-section presence validation,</li>
  <li>interface declaration validation,</li>
  <li>diagram structure validation,</li>
  <li>boundary and region validation,</li>
  <li>structure-terminal validation,</li>
  <li>edge and connectivity validation,</li>
  <li>canonical type validation,</li>
  <li>primitive existence and usage validation,</li>
  <li>profile requirement validation where applicable,</li>
  <li>widget declaration and participation validation where applicable,</li>
  <li>UI primitive usage validation where applicable,</li>
  <li>state and cycle legality validation,</li>
  <li>all other applicable source and semantic constraints defined by the published specification.</li>
</ul>

<p>Validation is not owned by one directory alone. Validation spans the relevant specification layers. But the semantic result of successful validation is owned here.</p>

<hr>

<h2 id="validation-result">7. Validation Result</h2>

<p>If validation succeeds, the result is one validated FROG program meaning for one canonical FROG source.</p>

<p>That validated meaning MUST include enough semantic truth to establish:</p>

<ul>
  <li>the validated public interface boundary,</li>
  <li>the validated executable graph participation,</li>
  <li>the validated structure semantics,</li>
  <li>the validated state and cycle legality,</li>
  <li>the validated participation of widgets and UI objects where execution-relevant,</li>
  <li>the validated typed value flow and boundary compatibility,</li>
  <li>the validated distinction between semantic content and non-semantic support content.</li>
</ul>

<p>A validated program meaning is not yet an open IR payload. It is semantic truth upstream of IR derivation.</p>

<hr>

<h2 id="core-boundary-invariants">8. Core Boundary Invariants</h2>

<h3>8.1 Source authority invariant</h3>

<p>Canonical <code>.frog</code> source is authoritative for source representation only.</p>

<p>It is authoritative for:</p>
<ul>
  <li>required source sections,</li>
  <li>source-visible graph structure,</li>
  <li>declared interface,</li>
  <li>source-visible structure placement,</li>
  <li>serialized front-panel composition where present,</li>
  <li>source-level recoverability material where standardized.</li>
</ul>

<p>It is not authoritative for:</p>
<ul>
  <li>derived IR shape,</li>
  <li>lowering strategy,</li>
  <li>runtime-private representation.</li>
</ul>

<h3>8.2 Semantic authority invariant</h3>

<p>Validated program meaning is the first normative execution-relevant truth layer.</p>

<p>Once validation succeeds:</p>
<ul>
  <li><code>Language/</code> becomes authoritative for meaning,</li>
  <li><code>IR/</code> may only derive from that meaning,</li>
  <li>implementations MUST NOT redefine the meaning that validation has established.</li>
</ul>

<h3>8.3 No silent semantic enrichment invariant</h3>

<p>Validation MAY determine whether source establishes valid meaning.</p>
<p>Validation MUST NOT silently invent new user-visible semantics not justified by the published specification.</p>

<h3>8.4 Recoverable distinction invariant</h3>

<p>Validation MAY normalize understanding of source-visible execution relevance, but it MUST preserve recoverable distinctions required by the published architecture.</p>

<h3>8.5 No source-loss invariant</h3>

<p>Validation MUST NOT erase distinctions that later layers are required to preserve or attribute.</p>

<h3>8.6 No implementation-authority invariant</h3>

<p>A validator, interpreter, compiler, IDE, or runtime MAY implement this boundary, but none of them becomes the source of language truth by doing so.</p>

<hr>

<h2 id="source-families-and-meaning-ownership">9. Source Families and Meaning Ownership</h2>

<p>The canonical source may contain several source families with different ownership roles.</p>

<h3>9.1 Families that directly contribute to validated program meaning</h3>

<p>These source families directly contribute to semantic meaning when present and valid:</p>
<ul>
  <li><code>interface</code></li>
  <li>execution-relevant parts of <code>diagram</code></li>
  <li>execution-relevant widget participation defined through source-visible linkage</li>
  <li>source-visible control structures</li>
  <li>source-visible explicit local-memory participation</li>
  <li>type declarations and type-constrained value declarations</li>
  <li>intrinsic primitive usage</li>
  <li>optional profile-governed capability usage when applicable</li>
</ul>

<h3>9.2 Families that may support meaning but do not independently define it</h3>

<p>These families may support interpretation or recoverability without independently owning semantic truth:</p>
<ul>
  <li><code>connector</code></li>
  <li>serialized front-panel composition details not used as execution participants</li>
  <li>icon material</li>
  <li>IDE-facing preferences</li>
  <li>cache-like derived support data</li>
</ul>

<h3>9.3 Families that are explicitly non-authoritative for execution meaning</h3>

<p>The following MUST NOT redefine validated execution meaning:</p>
<ul>
  <li><code>ide</code></li>
  <li><code>cache</code></li>
  <li>purely graphical layout information</li>
  <li>styling information</li>
  <li>connector placement choices</li>
  <li>icon presentation data</li>
</ul>

<hr>

<h2 id="execution-relevant-source-content">10. Execution-Relevant Source Content</h2>

<p>A source-side family is execution-relevant when it contributes to validated program meaning as opposed to tooling-only recoverability or presentation.</p>

<p>Execution-relevant source content includes, where applicable:</p>
<ul>
  <li>public interface inputs and outputs,</li>
  <li>executable diagram nodes,</li>
  <li>executable edges and explicit dependencies,</li>
  <li>structure boundaries, regions, and structure terminals,</li>
  <li>typed constants and typed configuration values that affect execution,</li>
  <li>explicit state participation,</li>
  <li>valid feedback participation,</li>
  <li>widget-value participation where the widget contributes a value to execution,</li>
  <li>widget-reference participation where a standardized UI object reference is validly used,</li>
  <li>standardized UI primitives used as executable primitives.</li>
</ul>

<p>Execution relevance does not mean direct IR identity. It means the source family contributes to the validated semantic meaning that IR derivation must later preserve.</p>

<hr>

<h2 id="non-semantic-or-non-authoritative-source-content">11. Non-Semantic or Non-Authoritative Source Content</h2>

<p>The following source-visible families do not directly define validated execution meaning by themselves:</p>
<ul>
  <li>connector geometry,</li>
  <li>front-panel layout,</li>
  <li>front-panel styling,</li>
  <li>icon data,</li>
  <li>IDE preferences,</li>
  <li>cache data,</li>
  <li>editor convenience metadata,</li>
  <li>tool acceleration metadata.</li>
</ul>

<p>These families MAY still matter for durability, authoring, recoverability, and user experience. They remain valid source concerns. But they are not semantic authority for execution.</p>

<pre><code>executable meaning      != editor convenience
executable meaning      != graphical layout
executable meaning      != cache payload
executable meaning      != runtime-private shortcut
</code></pre>

<hr>

<h2 id="interface-diagram-and-front-panel-participation">12. Interface, Diagram, and Front-Panel Participation</h2>

<p>Validation must preserve the explicit distinction between public contract, executable graph, and optional user interaction surface.</p>

<h3>12.1 Interface</h3>

<p>The interface defines the validated public boundary of the program.</p>

<p>Validation MUST establish:</p>
<ul>
  <li>declared public inputs,</li>
  <li>declared public outputs,</li>
  <li>canonical types,</li>
  <li>any applicable boundary constraints defined by the specification.</li>
</ul>

<h3>12.2 Diagram</h3>

<p>The diagram defines the authoritative source-level executable graph.</p>

<p>Validation MUST establish:</p>
<ul>
  <li>executable node legality,</li>
  <li>edge legality,</li>
  <li>region legality,</li>
  <li>boundary legality,</li>
  <li>structure-terminal legality,</li>
  <li>applicable primitive and profile usage legality.</li>
</ul>

<h3>12.3 Front panel</h3>

<p>The front panel defines optional serialized user interaction composition.</p>

<p>Its presence alone does not create execution meaning.</p>

<p>Execution meaning arises only where the specification defines valid execution-relevant participation between front-panel-owned objects and the executable program.</p>

<h3>12.4 Widget participation distinction</h3>

<p>Validation MUST preserve the distinction between:</p>
<ul>
  <li><code>widget_value</code></li>
  <li><code>widget_reference</code></li>
</ul>

<p>A widget primary value participating in execution is not the same thing as a standardized UI object reference participating in execution.</p>

<p>These families differ in:</p>
<ul>
  <li>source role,</li>
  <li>semantic meaning,</li>
  <li>legal usage,</li>
  <li>later derivation obligations.</li>
</ul>

<h3>12.5 Interface vs front-panel distinction</h3>

<p>Validation MUST preserve the distinction between:</p>
<ul>
  <li><code>interface_input</code> / <code>interface_output</code></li>
  <li>front-panel widget participation</li>
</ul>

<p>A public interface boundary is not a widget.<br>
A widget is not a public interface boundary.<br>
Any linkage between them must remain explicit and source-attributable.</p>

<p>The boundary can be summarized as:</p>

<pre><code>interface         = public program contract
diagram           = executable source graph
front panel       = optional user interaction surface
widget_value      = widget contributes a value
widget_reference  = widget contributes a standardized UI object reference
</code></pre>

<hr>

<h2 id="structures-state-and-cycles">13. Structures, State, and Cycles</h2>

<p>Validation is not complete unless source-visible structures, state, and cycles have been validated against their published rules.</p>

<h3>13.1 Structures</h3>

<p>For source-visible structures such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>, validation MUST establish:</p>
<ul>
  <li>legal structure identity,</li>
  <li>legal region organization,</li>
  <li>legal boundary participation,</li>
  <li>legal structure-terminal usage,</li>
  <li>semantic compatibility with the published language rules.</li>
</ul>

<h3>13.2 State</h3>

<p>Where explicit local memory exists, validation MUST establish that the memory participation is legal, explicit, typed where required, and semantically consistent with published state rules.</p>

<h3>13.3 Cycles</h3>

<p>Cycles are not valid merely because a graph contains a loop.</p>

<p>Validation MUST establish cycle legality according to the published language rules. Illegal cycles do not produce validated program meaning.</p>

<h3>13.4 Explicit-memory invariant</h3>

<p>Stateful behavior requiring explicit memory MUST NOT be inferred from an illegal or underspecified source cycle. The required explicit state participation must remain explicit at the source-to-meaning boundary.</p>

<p>Useful mental model:</p>

<pre><code>graph loop alone            != valid stateful behavior
explicit legal memory       -> possible valid stateful behavior
illegal feedback cycle      -> validation failure
</code></pre>

<hr>

<h2 id="type-value-and-state-commitments">14. Type, Value, and State Commitments</h2>

<p>Validation establishes not only structural legality but also semantic commitments about type, value flow, and state participation.</p>

<p>At minimum, validation MUST establish:</p>
<ul>
  <li>that declared types are canonical and legal,</li>
  <li>that connected value flow is type-compatible under applicable rules,</li>
  <li>that boundary values are semantically well-formed,</li>
  <li>that stateful participation is explicit where required,</li>
  <li>that typed defaults, initials, and other typed execution-relevant source values are legal where used.</li>
</ul>

<p>This document does not define the full type system. It defines that validated program meaning depends on successful satisfaction of applicable type and state constraints.</p>

<hr>

<h2 id="attribution-and-recoverability-at-the-semantic-boundary">15. Attribution and Recoverability at the Semantic Boundary</h2>

<p>The transition from source to validated meaning MUST preserve enough attribution for later layers to remain inspectable and recoverable.</p>

<p>At minimum, validated meaning MUST preserve recoverable attribution for execution-relevant source distinctions such as:</p>
<ul>
  <li>interface participation,</li>
  <li>diagram object participation,</li>
  <li>structure ownership,</li>
  <li>structure-terminal participation,</li>
  <li>widget-value participation,</li>
  <li>widget-reference participation,</li>
  <li>explicit state participation,</li>
  <li>source-visible boundaries relevant to later derivation.</li>
</ul>

<p>This does not require one frozen internal representation. It requires that later conforming layers do not lose distinctions they are obligated to preserve.</p>

<hr>

<h2 id="forbidden-boundary-collapses">16. Forbidden Boundary Collapses</h2>

<h3>16.1 Source into IR collapse</h3>
<p>A conforming implementation MUST NOT treat canonical source as though it were already open Execution IR.</p>

<h3>16.2 Validator into language collapse</h3>
<p>A validator implementation MUST NOT become the hidden definition of the language.</p>

<h3>16.3 Front panel into interface collapse</h3>
<p>Front-panel widgets MUST NOT be treated as equivalent to public interface declarations.</p>

<h3>16.4 Widget-value into widget-reference collapse</h3>
<p>These families MUST remain distinct.</p>

<h3>16.5 Semantics into runtime collapse</h3>
<p>Validated program meaning MUST NOT be defined by runtime-private behavior.</p>

<h3>16.6 Tooling metadata into semantics collapse</h3>
<p>IDE metadata, cache material, styling, and layout MUST NOT redefine execution meaning.</p>

<p>Forbidden collapses at a glance:</p>

<pre><code>source          -/-> IR
validator       -/-> language law
front panel     -/-> interface
widget_value    -/-> widget_reference
runtime         -/-> semantic authority
IDE/cache       -/-> execution meaning
</code></pre>

<hr>

<h2 id="relation-with-ir-derivation">17. Relation with IR Derivation</h2>

<p>This document is upstream of <code>IR/Derivation rules.md</code>.</p>

<p>The architectural sequence is:</p>

<pre><code>canonical source
        |
        v
validated program meaning
        |
        v
open execution-facing IR
        |
        v
lowering
        |
        v
backend contract
        |
        v
runtime-private realization
</code></pre>

<p>This document answers:</p>

<pre><code>What must be true before derivation may begin?
</code></pre>

<p><code>IR/Derivation rules.md</code> answers:</p>

<pre><code>How does validated meaning become open execution-facing IR?
</code></pre>

<p>The two documents are therefore complementary and non-overlapping.</p>

<p>This document MUST NOT redefine IR derivation obligations.<br>
<code>IR/Derivation rules.md</code> MUST NOT redefine what validated program meaning is.</p>

<hr>

<h2 id="out-of-scope-for-v01">18. Out of Scope for v0.1</h2>

<p>The following are out of scope for this document in base v0.1:</p>
<ul>
  <li>one frozen machine schema for all <code>.frog</code> validation,</li>
  <li>one mandatory validator algorithm,</li>
  <li>one mandatory internal semantic representation,</li>
  <li>one mandatory IR wire format,</li>
  <li>one mandatory lowering path,</li>
  <li>backend-private representation rules,</li>
  <li>runtime-private scheduling internals,</li>
  <li>IDE workflow policy.</li>
</ul>

<p>Those concerns may be addressed elsewhere in the repository architecture, but they are not owned here.</p>

<hr>

<h2 id="summary">19. Summary</h2>

<p>This document defines the normative boundary from canonical FROG source to validated program meaning.</p>

<p>It establishes that:</p>
<ul>
  <li>canonical <code>.frog</code> source is the authoritative source representation,</li>
  <li>validated program meaning is the first semantic truth layer,</li>
  <li>validation determines whether source successfully establishes that meaning,</li>
  <li>execution-relevant source families contribute to meaning,</li>
  <li>non-semantic support families remain non-authoritative for execution,</li>
  <li>critical distinctions such as interface vs widget participation, widget value vs widget reference, and explicit state vs illegal feedback must remain preserved,</li>
  <li>IR derivation is downstream from validated meaning, not a replacement for it.</li>
</ul>

<p>The architectural reading rule remains:</p>

<pre><code>Expression/   -&gt; how the program is written
Language/     -&gt; what the validated program means
IR/           -&gt; what execution-facing representation may be derived
</code></pre>

<p>Keeping that boundary explicit is necessary for conformance, inspectability, portability, future independent implementations, and a durable open graphical language architecture.</p>
