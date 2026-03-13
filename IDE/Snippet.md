<h1 align="center">🐸 FROG IDE Snippet Specification</h1>

<p align="center">
Definition of portable IDE snippet fragments for FROG authoring workflows<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Goals</a></li>
  <li><a href="#scope-for-v01">3. Scope for v0.1</a></li>
  <li><a href="#relation-with-other-specifications">4. Relation with Other Specifications</a></li>
  <li><a href="#design-principles">5. Design Principles</a></li>
  <li><a href="#what-a-snippet-is">6. What a Snippet Is</a></li>
  <li><a href="#snippet-vs-full-frog">7. Snippet vs Full FROG</a></li>
  <li><a href="#snippet-kinds">8. Snippet Kinds</a></li>
  <li><a href="#selection-scope-model">9. Selection Scope Model</a></li>
  <li><a href="#diagram-snippet-content">10. Diagram Snippet Content</a></li>
  <li><a href="#front-panel-snippet-content">11. Front Panel Snippet Content</a></li>
  <li><a href="#composite-snippets">12. Composite Snippets</a></li>
  <li><a href="#boundary-endpoints-and-open-connections">13. Boundary Endpoints and Open Connections</a></li>
  <li><a href="#reference-closure-and-dependencies">14. Reference Closure and Dependencies</a></li>
  <li><a href="#layout-and-identity-rules">15. Layout and Identity Rules</a></li>
  <li><a href="#serialization-model">16. Serialization Model</a></li>
  <li><a href="#transport-and-container-profiles">17. Transport and Container Profiles</a></li>
  <li><a href="#paste-and-insertion-semantics">18. Paste and Insertion Semantics</a></li>
  <li><a href="#validation-and-safety-rules">19. Validation and Safety Rules</a></li>
  <li><a href="#illustrative-examples">20. Illustrative Examples</a></li>
  <li><a href="#out-of-scope-for-v01">21. Out of Scope for v0.1</a></li>
  <li><a href="#summary">22. Summary</a></li>
  <li><a href="#license">23. License</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the snippet model of a FROG IDE.
A snippet is a portable IDE artifact that captures a reusable fragment of authoring content so that it can be copied, shared, pasted, or inserted into another editing context.
</p>

<p>
A snippet is not a full FROG program.
It is a source-aligned fragment of IDE-managed content derived from the FROG Program Model.
It is intended for reuse workflows such as:
</p>

<ul>
  <li>clipboard copy and paste,</li>
  <li>drag-and-drop insertion,</li>
  <li>sharing small reusable fragments,</li>
  <li>storing reusable authoring patterns,</li>
  <li>transporting a graph fragment with its visual layout and related metadata.</li>
</ul>

<p>
For v0.1, a snippet is defined as an IDE-layer artifact rather than as a new canonical source-program form.
Its purpose is reuse and transport of authoring fragments, not full-program storage.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Portability</strong> — allow small reusable authoring fragments to move across IDE sessions and tools.</li>
  <li><strong>Source alignment</strong> — preserve source-level meaning, layout, and object relationships.</li>
  <li><strong>Deterministic insertion</strong> — define how pasted content is integrated into a target Program Model without ambiguity.</li>
  <li><strong>Non-confusion with full programs</strong> — clearly distinguish snippets from full <code>.frog</code> source files.</li>
  <li><strong>Extensibility</strong> — allow richer transport containers or preview formats later without changing the core snippet semantics.</li>
</ul>

<hr/>

<h2 id="scope-for-v01">3. Scope for v0.1</h2>

<p>
For FROG v0.1, this document standardizes:
</p>

<ul>
  <li>what a snippet is,</li>
  <li>which kinds of authoring fragments may be captured,</li>
  <li>how snippet boundaries are represented,</li>
  <li>how references and required supporting objects are carried,</li>
  <li>how paste and insertion should behave at the source-model level.</li>
</ul>

<p>
FROG v0.1 does <strong>not</strong> standardize:
</p>

<ul>
  <li>a mandatory file extension for snippet files,</li>
  <li>a mandatory clipboard MIME type,</li>
  <li>a mandatory embedded-image snippet container,</li>
  <li>a marketplace or package manager for snippet libraries,</li>
  <li>execution directly from a snippet,</li>
  <li>automatic semantic repair of invalid pasted fragments beyond defined validation rules.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">4. Relation with Other Specifications</h2>

<p>
This document complements the following specifications:
</p>

<ul>
  <li><code>IDE/Readme.md</code> — defines the role of the Program Model and the distinction between IDE artifacts and canonical source.</li>
  <li><code>IDE/Palette.md</code> — defines reusable authoring elements surfaced by the IDE.</li>
  <li><code>Expression/Diagram.md</code> — defines executable graph objects, layout metadata, annotations, and dependencies.</li>
  <li><code>Expression/Front panel.md</code> — defines front-panel composition and widget-tree structure.</li>
  <li><code>Expression/Widget.md</code> — defines widget identity and widget object structure.</li>
  <li><code>Expression/Icon.md</code> — defines reusable icon representation where relevant to source-aligned reusable content.</li>
</ul>

<p>
This document does not redefine the canonical <code>.frog</code> source format.
It defines how the IDE may serialize, transport, and reinsert fragments of source-aligned authoring content.
</p>

<hr/>

<h2 id="design-principles">5. Design Principles</h2>

<h3>5.1 Snippets are IDE artifacts</h3>

<p>
A snippet belongs to the IDE and authoring workflow layer.
It is not the canonical persisted form of a full FROG program.
</p>

<h3>5.2 Snippets are source-aligned</h3>

<p>
Although snippets are IDE artifacts, their contents MUST remain expressible in terms of source-level objects already defined elsewhere, such as:
</p>

<ul>
  <li>diagram nodes and edges,</li>
  <li>diagram annotations,</li>
  <li>front-panel widgets,</li>
  <li>layout metadata,</li>
  <li>documentation metadata.</li>
</ul>

<h3>5.3 Snippets must be paste-safe</h3>

<p>
A snippet MUST carry enough information for a target IDE to either:
</p>

<ul>
  <li>insert it deterministically,</li>
  <li>or reject it deterministically with an explicit reason.</li>
</ul>

<h3>5.4 Snippets do not invent semantics</h3>

<p>
A snippet MUST NOT introduce ad hoc execution semantics that do not already exist in the FROG language or Program Model.
It transports content; it does not redefine the language.
</p>

<h3>5.5 Minimal but extensible</h3>

<p>
FROG v0.1 defines a minimal snippet core.
Stricter profiles MAY define richer transport containers, previews, sharing conventions, or snippet-library mechanisms.
</p>

<hr/>

<h2 id="what-a-snippet-is">6. What a Snippet Is</h2>

<p>
A snippet is a serialized authoring fragment captured from one editing context so that it may be inserted into another editing context.
</p>

<p>
Conceptually, a snippet contains:
</p>

<ul>
  <li>a snippet kind,</li>
  <li>a payload containing source-aligned fragment content,</li>
  <li>boundary information for open connections or incomplete surroundings,</li>
  <li>optional presentation metadata for transport or preview.</li>
</ul>

<p>
A snippet is usually derived from a user selection, but the exact UI gesture used to create that selection is outside the scope of this document.
</p>

<hr/>

<h2 id="snippet-vs-full-frog">7. Snippet vs Full FROG</h2>

<p>
A full FROG program is a complete source-level unit described by the canonical FROG Expression.
A snippet is only a fragment.
</p>

<p>
Therefore, a snippet:
</p>

<ul>
  <li>MAY be incomplete relative to a full program,</li>
  <li>MAY have open boundaries,</li>
  <li>MAY omit unrelated program sections,</li>
  <li>MUST NOT be treated as a complete executable FROG unless a stricter profile explicitly wraps it into a complete FROG.</li>
</ul>

<p>
A snippet is not a substitute for:
</p>

<ul>
  <li>a reusable library FROG,</li>
  <li>a dependency package,</li>
  <li>a canonical source file,</li>
  <li>an execution artifact.</li>
</ul>

<hr/>

<h2 id="snippet-kinds">8. Snippet Kinds</h2>

<p>
The canonical snippet kinds for FROG v0.1 are:
</p>

<ul>
  <li><code>diagram_snippet</code> — a fragment of one diagram scope,</li>
  <li><code>front_panel_snippet</code> — a fragment of a front-panel widget tree,</li>
  <li><code>composite_snippet</code> — a snippet carrying both diagram and front-panel content when they are semantically linked.</li>
</ul>

<p>
A <code>diagram_snippet</code> is the primary snippet kind for v0.1.
</p>

<hr/>

<h2 id="selection-scope-model">9. Selection Scope Model</h2>

<h3>9.1 Single-scope rule</h3>

<p>
A v0.1 snippet payload MUST be rooted in exactly one source scope for each carried content family.
For example:
</p>

<ul>
  <li>a diagram snippet is rooted in one diagram scope,</li>
  <li>a front-panel snippet is rooted in one widget-tree scope.</li>
</ul>

<h3>9.2 No mixed diagram scopes in one diagram payload</h3>

<p>
A single <code>diagram_snippet</code> payload MUST NOT directly mix executable objects taken from multiple diagram scopes.
For example, it MUST NOT combine objects from both:
</p>

<ul>
  <li>a parent diagram scope, and</li>
  <li>a nested structure-region scope</li>
</ul>

<p>
inside one flat diagram payload.
</p>

<h3>9.3 Whole-structure capture</h3>

<p>
If a selection includes a structure node as a selected object, the snippet MUST carry that structure node together with its owned regions and their source-aligned content.
</p>

<h3>9.4 Region-local snippet</h3>

<p>
A stricter profile MAY allow creating a snippet from content inside one structure-owned region without selecting the containing structure itself.
In that case, the snippet root is that region-local diagram scope rather than the parent scope.
</p>

<hr/>

<h2 id="diagram-snippet-content">10. Diagram Snippet Content</h2>

<p>
A <code>diagram_snippet</code> MAY contain:
</p>

<ul>
  <li>selected nodes,</li>
  <li>selected internal edges between those nodes,</li>
  <li>selected annotations,</li>
  <li>node-local documentation fields,</li>
  <li>node tags,</li>
  <li>layout metadata relevant to pasted placement,</li>
  <li>scope-local dependency references needed by selected <code>subfrog</code> nodes.</li>
</ul>

<p>
A diagram snippet MUST preserve source-level node kinds and kind-specific fields.
It MUST NOT rewrite a selected node into a different node kind merely for snippet transport.
</p>

<h3>10.1 Internal edges</h3>

<p>
An edge is internal to the snippet if both its source endpoint and destination endpoint are carried by the snippet payload.
Internal edges SHOULD be carried directly as ordinary snippet-owned edges.
</p>

<h3>10.2 Partial-edge crossings</h3>

<p>
An edge that crosses the snippet selection boundary is not fully internal.
Such a crossing MUST be represented through snippet boundary endpoints as defined later in this document.
</p>

<hr/>

<h2 id="front-panel-snippet-content">11. Front Panel Snippet Content</h2>

<p>
A <code>front_panel_snippet</code> MAY contain:
</p>

<ul>
  <li>one or more widget instances,</li>
  <li>widget subtrees,</li>
  <li>layout and composition metadata,</li>
  <li>styling metadata,</li>
  <li>widget-local configuration.</li>
</ul>

<p>
For v0.1, a front-panel snippet SHOULD preserve widget-tree structure rather than flattening it into unrelated widgets.
If a selected widget has selected descendants, their parent-child relationship MUST remain preserved.
</p>

<p>
A snippet MUST NOT silently break a widget subtree in a way that makes the resulting payload structurally ambiguous.
An IDE MAY therefore require subtree closure for certain widget selections.
</p>

<hr/>

<h2 id="composite-snippets">12. Composite Snippets</h2>

<p>
A <code>composite_snippet</code> carries both:
</p>

<ul>
  <li>a diagram fragment, and</li>
  <li>a related front-panel fragment.</li>
</ul>

<p>
This is especially useful when the diagram fragment contains:
</p>

<ul>
  <li><code>widget_value</code> nodes,</li>
  <li><code>widget_reference</code> nodes,</li>
  <li><code>frog.ui.*</code> widget-interaction primitives whose meaning depends on referenced widgets.</li>
</ul>

<p>
If a snippet carries widget-related diagram nodes and is intended to be portable across documents, it SHOULD include the required referenced widget definitions in a front-panel fragment rather than assuming they already exist in the target FROG.
</p>

<hr/>

<h2 id="boundary-endpoints-and-open-connections">13. Boundary Endpoints and Open Connections</h2>

<h3>13.1 Purpose</h3>

<p>
A snippet is often created from a larger graph fragment that was connected to surrounding content.
Those external relationships must be represented without pretending that the snippet is a full closed diagram.
</p>

<h3>13.2 Boundary endpoints</h3>

<p>
FROG v0.1 defines conceptual snippet boundary endpoints:
</p>

<ul>
  <li><code>snippet_input</code> — a value or sequencing dependency expected from outside the snippet,</li>
  <li><code>snippet_output</code> — a value or sequencing dependency produced by the snippet for use outside the snippet.</li>
</ul>

<p>
These are snippet-level transport concepts, not canonical node kinds of the FROG source language.
They exist only inside the snippet payload model.
</p>

<h3>13.3 Meaning</h3>

<p>
A snippet boundary endpoint represents an open connection between the carried fragment and content that was not included in the snippet.
When the snippet is pasted, the IDE MAY:
</p>

<ul>
  <li>leave the corresponding boundary as an unwired open endpoint,</li>
  <li>offer reconnection assistance,</li>
  <li>or map it to a suitable target connection if the paste operation explicitly defines one.</li>
</ul>

<h3>13.4 Type information</h3>

<p>
When type information is resolvable from the source fragment, a snippet boundary endpoint SHOULD carry that type information so that paste validation can remain deterministic.
</p>

<hr/>

<h2 id="reference-closure-and-dependencies">14. Reference Closure and Dependencies</h2>

<h3>14.1 General rule</h3>

<p>
A snippet SHOULD carry the minimum supporting information needed to remain meaningful after transport.
</p>

<h3>14.2 Primitive references</h3>

<p>
Primitive nodes are carried by their canonical type identifiers such as <code>frog.core.add</code> or <code>frog.ui.property_read</code>.
A snippet does not inline primitive-library definitions.
</p>

<h3>14.3 Sub-FROG dependencies</h3>

<p>
If a snippet contains <code>subfrog</code> nodes, it SHOULD carry the relevant dependency references needed to keep those <code>subfrog.ref</code> identifiers meaningful at paste time.
A snippet does not inline the full referenced dependent FROGs.
</p>

<h3>14.4 Widget references</h3>

<p>
If a snippet contains <code>widget_value</code> or <code>widget_reference</code> nodes and is intended to remain portable across documents, it SHOULD carry the required widget definitions through a front-panel fragment or equivalent widget payload.
</p>

<h3>14.5 No unrelated closure</h3>

<p>
A snippet SHOULD NOT capture unrelated surrounding program content merely to avoid open boundaries.
Closure should be minimal and semantically relevant.
</p>

<hr/>

<h2 id="layout-and-identity-rules">15. Layout and Identity Rules</h2>

<h3>15.1 Layout preservation</h3>

<p>
Because FROG is a graphical language, snippet payloads SHOULD preserve layout metadata relevant to visual reinsertion.
</p>

<h3>15.2 Relative positioning</h3>

<p>
A snippet SHOULD preserve relative geometry between carried objects.
A transport profile MAY normalize coordinates so that the snippet has a local origin, provided that relative placement remains preserved.
</p>

<h3>15.3 Identifier preservation in payload</h3>

<p>
A snippet MAY preserve original source identifiers inside its payload for traceability.
However, on paste into a target Program Model, the IDE MUST resolve identifier collisions deterministically.
</p>

<h3>15.4 Identifier remapping on paste</h3>

<p>
If the target FROG already contains an identifier used by the snippet payload, the IDE MUST rename or remap the inserted objects so that identifier uniqueness rules remain valid in the target scope.
</p>

<hr/>

<h2 id="serialization-model">16. Serialization Model</h2>

<p>
FROG v0.1 defines a logical snippet payload model.
A snippet payload is a structured serialization of snippet content and its snippet-specific transport metadata.
</p>

<p>
Conceptually, a snippet payload includes:
</p>

<ul>
  <li>format version,</li>
  <li>snippet kind,</li>
  <li>content payload,</li>
  <li>boundary endpoints,</li>
  <li>optional transport metadata.</li>
</ul>

<p>
Illustrative high-level shape:
</p>

<pre><code>{
  "snippet_version": "0.1",
  "kind": "diagram_snippet",
  "payload": { ... },
  "boundary": { ... },
  "transport": { ... }
}</code></pre>

<p>
This document defines the logical content model, not one mandatory concrete file or clipboard encoding.
</p>

<hr/>

<h2 id="transport-and-container-profiles">17. Transport and Container Profiles</h2>

<h3>17.1 Transport independence</h3>

<p>
A snippet MAY be transported through different containers, including:
</p>

<ul>
  <li>clipboard transfer,</li>
  <li>a dedicated snippet file,</li>
  <li>drag-and-drop payloads,</li>
  <li>a preview-carrying container defined by a stricter profile.</li>
</ul>

<h3>17.2 Preview-carrying containers</h3>

<p>
A stricter profile MAY define a transport container that includes both:
</p>

<ul>
  <li>a human-visible preview image, and</li>
  <li>an embedded machine-readable snippet payload.</li>
</ul>

<p>
Such a profile is compatible with this specification provided that the embedded snippet payload remains semantically equivalent to the logical snippet model defined here.
</p>

<h3>17.3 No mandatory container in v0.1</h3>

<p>
FROG v0.1 intentionally does not require one mandatory transport container.
The semantic content of the snippet matters more than the transport wrapper.
</p>

<hr/>

<h2 id="paste-and-insertion-semantics">18. Paste and Insertion Semantics</h2>

<h3>18.1 General rule</h3>

<p>
Pasting a snippet means inserting its carried fragment into a target editing context and integrating it into the target Program Model.
</p>

<h3>18.2 Valid insertion target</h3>

<p>
A snippet MAY be pasted only into a target context compatible with its snippet kind.
For example:
</p>

<ul>
  <li>a <code>diagram_snippet</code> must be pasted into a compatible diagram scope,</li>
  <li>a <code>front_panel_snippet</code> must be pasted into a compatible widget-tree context,</li>
  <li>a <code>composite_snippet</code> requires the IDE to handle both diagram-side and front-panel-side insertion.</li>
</ul>

<h3>18.3 Paste result</h3>

<p>
A successful paste operation MUST produce:
</p>

<ul>
  <li>valid inserted source objects,</li>
  <li>collision-free identifiers,</li>
  <li>preserved relative layout,</li>
  <li>preserved internal snippet relationships,</li>
  <li>explicitly represented open boundaries where external reconnection is still required.</li>
</ul>

<h3>18.4 Reconnection behavior</h3>

<p>
This document does not require automatic reconnection of open boundaries.
An IDE MAY provide assisted reconnection or matching heuristics, but if such heuristics are used they MUST remain explicit and reversible from the user’s point of view.
</p>

<h3>18.5 Validation after paste</h3>

<p>
The inserted result MUST be validated under the same Program Model and source-validation rules as any other edited content.
If the pasted result is invalid in the target context, the IDE MUST report that invalidity clearly.
</p>

<hr/>

<h2 id="validation-and-safety-rules">19. Validation and Safety Rules</h2>

<ul>
  <li>A snippet MUST declare its snippet kind.</li>
  <li>A snippet MUST carry only source-aligned objects valid for that snippet kind.</li>
  <li>A diagram snippet MUST preserve internal source-level relationships among carried nodes, edges, and annotations.</li>
  <li>A front-panel snippet MUST preserve carried widget-tree relationships.</li>
  <li>A composite snippet carrying widget-related diagram nodes SHOULD carry the required widget definitions needed for portability.</li>
  <li>Snippet boundary endpoints MUST NOT be misrepresented as canonical FROG node kinds.</li>
  <li>Pasting MUST preserve target-scope identifier uniqueness.</li>
  <li>Pasting MUST NOT silently change carried execution semantics.</li>
  <li>A snippet MUST NOT be treated as a full executable FROG unless it is explicitly wrapped into one by a stricter profile or tool action.</li>
</ul>

<hr/>

<h2 id="illustrative-examples">20. Illustrative Examples</h2>

<h3>20.1 Minimal diagram snippet</h3>

<pre><code>{
  "snippet_version": "0.1",
  "kind": "diagram_snippet",
  "payload": {
    "nodes": [
      {
        "id": "add_1",
        "kind": "primitive",
        "type": "frog.core.add",
        "layout": { "x": 120, "y": 80 }
      }
    ],
    "edges": [],
    "annotations": []
  },
  "boundary": {
    "inputs": [
      { "id": "in_a", "port": "a" },
      { "id": "in_b", "port": "b" }
    ],
    "outputs": [
      { "id": "out_result", "port": "result" }
    ]
  }
}</code></pre>

<h3>20.2 Diagram snippet with internal edge and annotation</h3>

<pre><code>{
  "snippet_version": "0.1",
  "kind": "diagram_snippet",
  "payload": {
    "nodes": [
      {
        "id": "mul_1",
        "kind": "primitive",
        "type": "frog.core.mul",
        "layout": { "x": 80, "y": 120 }
      },
      {
        "id": "add_1",
        "kind": "primitive",
        "type": "frog.core.add",
        "layout": { "x": 260, "y": 120 }
      }
    ],
    "edges": [
      {
        "id": "e1",
        "from": { "node": "mul_1", "port": "result" },
        "to": { "node": "add_1", "port": "a" }
      }
    ],
    "annotations": [
      {
        "id": "ann_1",
        "kind": "text",
        "text": "Reusable numeric fragment",
        "layout": { "x": 80, "
