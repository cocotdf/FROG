<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">🐸 FROG UI Library Specification</h1>

<p align="center">
  Definition of the intrinsic <strong>frog.ui</strong> primitive library for FROG v0.1<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Goals</a></li>
  <li><a href="#architectural-position">3. Architectural Position</a></li>
  <li><a href="#scope">4. Scope</a></li>
  <li><a href="#relation-with-other-specifications">5. Relation with Other Specifications</a></li>
  <li><a href="#namespace">6. Namespace</a></li>
  <li><a href="#standard-primitives-for-v01">7. Standard Primitives for v0.1</a></li>
  <li><a href="#froguiproperty_read">8. <code>frog.ui.property_read</code></a></li>
  <li><a href="#froguiproperty_write">9. <code>frog.ui.property_write</code></a></li>
  <li><a href="#froguimethod_invoke">10. <code>frog.ui.method_invoke</code></a></li>
  <li><a href="#typing-and-sequencing">11. Typing and Sequencing</a></li>
  <li><a href="#validation-rules">12. Validation Rules</a></li>
  <li><a href="#execution-facing-posture">13. Execution-Facing Posture</a></li>
  <li><a href="#examples">14. Examples</a></li>
  <li><a href="#out-of-scope-for-v01">15. Out of Scope for v0.1</a></li>
  <li><a href="#summary">16. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the intrinsic <code>frog.ui</code> primitive library for FROG v0.1.
</p>

<p>
The <code>frog.ui</code> library standardizes executable UI-interaction primitives used by diagram nodes of kind <code>primitive</code>.
These primitives provide object-style interaction with widget instances and widget parts through standardized executable operations.
</p>

<p>
In FROG, ordinary primary widget-value participation in dataflow is represented through <code>widget_value</code> nodes.
Object-style interaction is represented through <code>widget_reference</code> nodes consumed by standardized <code>frog.ui.*</code> primitives.
</p>

<p>
This document defines the intrinsic primitive catalog for that interaction.
It does not define the widget object model, front-panel serialization, general diagram graph structure, open Execution IR structure, lowering families, backend contracts, or runtime-private UI realization.
</p>

<p>
The core distinction is:
</p>

<pre>
widget_value
    -&gt; natural primary-value path

widget_reference
    -&gt; object-style widget access path

frog.ui.*
    -&gt; intrinsic executable primitive vocabulary
       that consumes widget references
</pre>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Clarity</strong> — define a small, explicit, and durable primitive vocabulary for object-style UI interaction.</li>
  <li><strong>Boundary discipline</strong> — keep widget interaction primitives distinct from widget declarations, front-panel source, IDE behavior, IR lowering, and runtime-private realization.</li>
  <li><strong>Portability</strong> — provide intrinsic primitive identities that multiple conforming implementations can recognize and carry through validation and execution-facing derivation.</li>
  <li><strong>Recoverability</strong> — preserve the distinction between natural widget-value participation and object-style widget-reference interaction.</li>
  <li><strong>Execution usefulness</strong> — support explicit property reads, property writes, and method invocation in executable diagrams without forcing a larger event model into v0.1.</li>
</ul>

<hr/>

<h2 id="architectural-position">3. Architectural Position</h2>

<p>
The architectural position of <code>frog.ui</code> is intentionally narrow and explicit:
</p>

<pre>
Expression/   -&gt; canonical source representation
Language/     -&gt; validated-program meaning
Libraries/    -&gt; intrinsic primitive identities and primitive-local contracts
Profiles/     -&gt; optional standardized capability families
IR/           -&gt; open execution-facing representation, lowering, and backend-facing boundaries
IDE/          -&gt; authoring, observability, debugging, inspection
</pre>

<p>
Within that architecture:
</p>

<ul>
  <li><code>Expression/Widget.md</code> owns widget classes, properties, methods, parts, and roles,</li>
  <li><code>Expression/Widget interaction.md</code> owns the source-facing interaction model, including <code>widget_value</code> and <code>widget_reference</code> participation,</li>
  <li><code>Libraries/UI.md</code> owns the intrinsic primitive identities, primitive-local signatures, metadata requirements, and primitive-local interaction behavior of <code>frog.ui.*</code>,</li>
  <li><code>Language/</code> owns cross-cutting validated-program meaning, including the semantic distinction between interface participation, <code>widget_value</code> participation, <code>widget_reference</code> participation, and standardized UI-object primitive operations,</li>
  <li><code>IR/</code> may later preserve these primitives and distinctions in open execution-facing form, then specialize them later through lowering and backend contracts,</li>
  <li><code>IDE/</code> may surface these primitives in palettes and authoring workflows without redefining them.</li>
</ul>

<p>
The key rule is:
</p>

<pre>
widget class catalog
    !=
widget interaction primitive catalog

front-panel declaration
    !=
object-style execution primitive

open Execution IR
    !=
primitive catalog ownership

runtime-private widget handle
    !=
intrinsic frog.ui primitive identity
</pre>

<hr/>

<h2 id="scope">4. Scope</h2>

<p>
For FROG v0.1, this library standardizes the following intrinsic primitive identifiers:
</p>

<ul>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
</ul>

<p>
This specification defines:
</p>

<ul>
  <li>primitive identifiers,</li>
  <li>required primitive-local metadata,</li>
  <li>canonical port signatures,</li>
  <li>primitive-local typing constraints,</li>
  <li>primitive-local sequencing behavior,</li>
  <li>primitive-level validation rules,</li>
  <li>primitive-local execution-facing semantics.</li>
</ul>

<p>
This specification does not define:
</p>

<ul>
  <li>the widget class catalog,</li>
  <li>front-panel widget serialization,</li>
  <li>the <code>widget_value</code> node kind,</li>
  <li>the <code>widget_reference</code> node kind,</li>
  <li>general diagram edge or port-resolution rules,</li>
  <li>the full cross-cutting semantic boundary from validated meaning to open Execution IR,</li>
  <li>the full source-to-IR derivation mapping,</li>
  <li>a first-class event-execution model,</li>
  <li>a generalized widget-reference value type for arbitrary storage or transport,</li>
  <li>one backend-family taxonomy,</li>
  <li>one runtime-private UI object model.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">5. Relation with Other Specifications</h2>

<p>
This document is used together with the rest of the FROG specification.
In particular:
</p>

<ul>
  <li><code>Libraries/Readme.md</code> defines the role of <code>Libraries/</code> as the intrinsic primitive-library layer.</li>
  <li><code>Expression/Diagram.md</code> defines how primitive nodes appear in executable diagrams and how general node and edge structure is represented.</li>
  <li><code>Expression/Type.md</code> defines ordinary FROG type expressions and compatibility rules.</li>
  <li><code>Expression/Widget.md</code> defines widget classes, properties, methods, parts, and roles.</li>
  <li><code>Expression/Widget interaction.md</code> defines the canonical source-facing interaction model used by these primitives.</li>
  <li><code>Expression/Front panel.md</code> defines front-panel widget declaration and composition.</li>
  <li><code>Language/Expression to validated meaning.md</code> defines the semantic boundary from canonical source to validated meaning.</li>
  <li><code>Language/Readme.md</code> defines the semantic ownership layer for validated FROG programs.</li>
  <li><code>IR/Execution IR.md</code> defines the open execution-facing representation that may preserve UI-related execution objects after validation.</li>
  <li><code>IR/Derivation rules.md</code> defines how validated UI participation and standardized UI-object primitive usage become open Execution IR.</li>
  <li><code>IR/Identity and Mapping.md</code> defines recoverability obligations for UI participation and UI-operation distinctions.</li>
  <li><code>IR/Lowering.md</code> defines later specialization boundaries that may lower these primitives toward backend-oriented forms.</li>
  <li><code>IR/Backend contract.md</code> defines later consumer-facing handoff obligations when UI participation remains relevant to a backend family.</li>
</ul>

<p>
Ownership is intentionally split:
</p>

<ul>
  <li><code>Libraries/UI.md</code> owns primitive identities, signatures, primitive typing, sequencing behavior, and primitive-local semantics,</li>
  <li><code>Expression/Widget interaction.md</code> owns the source-facing interaction model,</li>
  <li><code>Expression/Diagram.md</code> owns the general graph representation model,</li>
  <li><code>Expression/Widget.md</code> owns widget member and method availability,</li>
  <li><code>Language/</code> owns the cross-cutting semantic distinction between different UI-participation roles,</li>
  <li><code>IR/</code> owns execution-facing derived representation, recoverable mapping, lowering, and backend-facing handoff boundaries.</li>
</ul>

<p>
In particular:
</p>

<pre>
Libraries/UI.md
    does not own
widget catalog definition

Libraries/UI.md
    does not own
front-panel source model

Libraries/UI.md
    does not own
Execution IR object model

Libraries/UI.md
    does not own
backend-family UI binding contracts

Libraries/UI.md
    owns
intrinsic executable UI-interaction primitive contracts
</pre>

<hr/>

<h2 id="namespace">6. Namespace</h2>

<p>
The intrinsic primitive namespace defined by this library is:
</p>

<pre><code>frog.ui.*</code></pre>

<p>
This namespace is reserved for intrinsic executable UI-interaction primitives.
</p>

<p>
It MUST be distinguished from widget-class namespaces such as:
</p>

<pre><code>frog.ui.standard.*</code></pre>

<p>
Accordingly:
</p>

<ul>
  <li><code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code> are intrinsic primitive identifiers,</li>
  <li><code>frog.ui.standard.numeric_control</code> and similar identifiers are widget-class identifiers,</li>
  <li>namespace prefix similarity does not collapse primitive-library ownership and widget-class ownership into one concept.</li>
</ul>

<hr/>

<h2 id="standard-primitives-for-v01">7. Standard Primitives for v0.1</h2>

<p>
FROG v0.1 standardizes the following intrinsic <code>frog.ui</code> primitives:
</p>

<ul>
  <li><code>frog.ui.property_read</code> — read a property from a widget or widget part,</li>
  <li><code>frog.ui.property_write</code> — write a property of a widget or widget part,</li>
  <li><code>frog.ui.method_invoke</code> — invoke a method on a widget or widget part.</li>
</ul>

<p>
All three primitives:
</p>

<ul>
  <li>MUST be valid intrinsic primitive identifiers in the active library catalog,</li>
  <li>MUST consume a widget reference through required input port <code>ref</code>,</li>
  <li>MAY expose optional sequencing ports <code>ui_in</code> and <code>ui_out</code>,</li>
  <li>MUST use <code>widget_member</code> or <code>widget_method</code> metadata as appropriate.</li>
</ul>

<p>
These primitives are object-style interaction primitives.
They do not replace the natural primary-value path represented by <code>widget_value</code>.
</p>

<p>
The semantic distinction MUST remain recoverable:
</p>

<pre>
widget_value
    !=
widget_reference

widget_reference
    !=
frog.ui.property_read / property_write / method_invoke

property access to member "value"
    !=
natural widget_value participation
</pre>

<hr/>

<h2 id="froguiproperty_read">8. <code>frog.ui.property_read</code></h2>

<p>
Primitive identifier:
</p>

<pre><code>frog.ui.property_read</code></pre>

<p>
A property-read primitive reads a property value from a widget or widget part and exposes that value to the diagram.
</p>

<p>
Required primitive-local metadata:
</p>

<pre><code>{
  "widget_member": {
    "member": "visible"
  }
}</code></pre>

<p>
Canonical port signature:
</p>

<ul>
  <li>required input port <code>ref</code>,</li>
  <li>optional input port <code>ui_in</code>,</li>
  <li>required output port <code>value</code>,</li>
  <li>optional output port <code>ui_out</code>.</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>the primitive MUST declare <code>widget_member</code>,</li>
  <li>the addressed property MUST be readable for the addressed widget member under the active widget profile or widget specification,</li>
  <li>the output port <code>value</code> MUST have the declared type of the addressed property.</li>
</ul>

<p>
Reading <code>{ "member": "value" }</code> is valid when the widget class exposes <code>value</code> as a readable property.
However, when the intent is ordinary primary-value dataflow, tools SHOULD prefer the natural <code>widget_value</code> representation.
</p>

<p>
Primitive-local semantics:
</p>

<ul>
  <li>the read observes the current property value at execution time,</li>
  <li>if <code>ui_in</code> is connected, the read MUST occur only after the incoming sequencing token becomes available,</li>
  <li>if <code>ui_out</code> is connected, it MUST become available only after the read has completed,</li>
  <li>the primitive remains an object-style UI-interaction primitive even when the addressed member is named <code>value</code>.</li>
</ul>

<hr/>

<h2 id="froguiproperty_write">9. <code>frog.ui.property_write</code></h2>

<p>
Primitive identifier:
</p>

<pre><code>frog.ui.property_write</code></pre>

<p>
A property-write primitive writes a diagram value into a writable property of a widget or widget part.
</p>

<p>
Required primitive-local metadata:
</p>

<pre><code>{
  "widget_member": {
    "part": "label",
    "member": "text"
  }
}</code></pre>

<p>
Canonical port signature:
</p>

<ul>
  <li>required input port <code>ref</code>,</li>
  <li>required input port <code>value</code>,</li>
  <li>optional input port <code>ui_in</code>,</li>
  <li>optional output port <code>ui_out</code>.</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>the primitive MUST declare <code>widget_member</code>,</li>
  <li>the addressed property MUST be writable for the addressed widget member under the active widget profile or widget specification,</li>
  <li>the input port <code>value</code> MUST be type-compatible with the declared type of the addressed property.</li>
</ul>

<p>
Writing <code>{ "member": "value" }</code> is valid when the widget class exposes <code>value</code> as a writable property.
This object-style write MUST remain semantically distinct from the natural primary-value path represented by <code>widget_value</code>.
For ordinary widget-value participation in dataflow, tools SHOULD prefer the natural <code>widget_value</code> representation.
</p>

<p>
Primitive-local semantics:
</p>

<ul>
  <li>a property write applies a UI side effect to the addressed widget member,</li>
  <li>if <code>ui_in</code> is connected, the write MUST occur only after the incoming sequencing token becomes available,</li>
  <li>if <code>ui_out</code> is connected, it MUST become available only after the write has completed according to the active implementation behavior,</li>
  <li>the primitive remains an object-style UI-interaction primitive even when the addressed member is named <code>value</code>.</li>
</ul>

<hr/>

<h2 id="froguimethod_invoke">10. <code>frog.ui.method_invoke</code></h2>

<p>
Primitive identifier:
</p>

<pre><code>frog.ui.method_invoke</code></pre>

<p>
A method-invoke primitive calls a method on a widget or widget part.
</p>

<p>
Required primitive-local metadata:
</p>

<pre><code>{
  "widget_method": {
    "name": "reset_to_default"
  }
}</code></pre>

<p>
Canonical port signature:
</p>

<ul>
  <li>required input port <code>ref</code>,</li>
  <li>zero or more method-argument input ports in canonical method order,</li>
  <li>optional input port <code>ui_in</code>,</li>
  <li>zero or more method-result output ports in canonical method order,</li>
  <li>optional output port <code>ui_out</code>.</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>the primitive MUST declare <code>widget_method</code>,</li>
  <li>the addressed method MUST exist for the addressed widget member under the active widget profile or widget specification,</li>
  <li>argument input ports MUST match the canonical method signature,</li>
  <li>result output ports MUST match the canonical method signature,</li>
  <li>each argument input MUST be type-compatible with the declared parameter type,</li>
  <li>each result output MUST have the declared result type.</li>
</ul>

<p>
Primitive-local semantics:
</p>

<ul>
  <li>a method invocation MAY produce UI side effects, ordinary return values, or both,</li>
  <li>if <code>ui_in</code> is connected, the invocation MUST occur only after the incoming sequencing token becomes available,</li>
  <li>if <code>ui_out</code> is connected, it MUST become available only after invocation has completed according to the active implementation behavior,</li>
  <li>the primitive remains distinct from both widget declaration identity and widget-reference participation identity.</li>
</ul>

<hr/>

<h2 id="typing-and-sequencing">11. Typing and Sequencing</h2>

<h3>11.1 Widget-reference typing</h3>

<p>
The required input port <code>ref</code> carries an opaque widget-reference token.
In v0.1, this token is interaction-oriented and diagram-internal.
It is not standardized here as a general-purpose first-class value type for arbitrary storage, transport, comparison, or computation.
</p>

<h3>11.2 Property typing</h3>

<p>
Property-read and property-write primitives MUST use the declared property type of the addressed widget member.
Compatibility checks and implicit coercions MUST follow the ordinary FROG type rules.
</p>

<h3>11.3 Method typing</h3>

<p>
Method-invoke primitives MUST use the declared method signature of the addressed widget member.
Argument and result ports MUST follow the canonical method signature defined by the active widget specification.
</p>

<h3>11.4 UI sequencing ports</h3>

<p>
The optional ports <code>ui_in</code> and <code>ui_out</code> define explicit ordering between UI interactions.
These ports:
</p>

<ul>
  <li>MUST NOT be interpreted as ordinary data values,</li>
  <li>MUST NOT redefine ordinary data-dependency typing,</li>
  <li>MAY be omitted when no explicit UI ordering is required,</li>
  <li>SHOULD be used when deterministic ordering of UI side effects matters.</li>
</ul>

<p>
In v0.1, the sequencing token carried by <code>ui_in</code> and <code>ui_out</code> is opaque.
Its runtime representation is implementation-defined, but its ordering meaning between standardized UI-interaction primitives is defined by this specification.
</p>

<h3>11.5 Boundary rule</h3>

<p>
The presence of sequencing ports does not convert these primitives into a general event model, callback model, or asynchronous orchestration model.
They remain explicit object-style UI-interaction primitives with optional ordering support.
</p>

<hr/>

<h2 id="validation-rules">12. Validation Rules</h2>

<p>
Implementations MUST enforce at least the following primitive-level rules:
</p>

<ul>
  <li>the primitive identifier MUST be one of the standardized identifiers defined by this document,</li>
  <li>the required input port <code>ref</code> MUST be present,</li>
  <li>a property primitive MUST declare <code>widget_member</code>,</li>
  <li>a method primitive MUST declare <code>widget_method</code>,</li>
  <li>required and optional ports MUST match the standardized signature of the primitive,</li>
  <li>primitive-local typing MUST remain valid under the ordinary FROG type rules.</li>
</ul>

<p>
Additionally:
</p>

<ul>
  <li><code>frog.ui.property_read</code> MUST address a readable property,</li>
  <li><code>frog.ui.property_write</code> MUST address a writable property,</li>
  <li><code>frog.ui.method_invoke</code> MUST address a valid method,</li>
  <li>part names, member names, and method names MUST be valid for the addressed widget class or active widget specification,</li>
  <li>the distinction between object-style interaction and natural <code>widget_value</code> participation MUST remain semantically recoverable,</li>
  <li>use of a property named <code>value</code> through <code>frog.ui.property_read</code> or <code>frog.ui.property_write</code> MUST NOT be silently normalized into <code>widget_value</code> participation,</li>
  <li>natural <code>widget_value</code> participation MUST NOT be silently reclassified as property-based access to member <code>value</code>.</li>
</ul>

<p>
Invalid UI-interaction primitives MUST trigger validation errors.
</p>

<p>
Source-level graph-shape constraints remain owned by <code>Expression/Widget interaction.md</code> and <code>Expression/Diagram.md</code>.
Cross-cutting semantic acceptance remains owned by <code>Language/</code>.
Execution-facing derivation, mapping, lowering, and backend-facing handoff remain owned by <code>IR/</code>.
</p>

<hr/>

<h2 id="execution-facing-posture">13. Execution-Facing Posture</h2>

<p>
This document defines intrinsic primitive-local truth, not one execution-facing representation.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>open Execution IR MAY preserve recognizable primitive execution objects corresponding to <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code>,</li>
  <li>derivation MAY add execution-facing explicitness such as resolved member descriptors, method descriptors, classification records, or source-attribution records,</li>
  <li>identity and mapping rules MAY require these primitives to remain distinguishable from widget-reference participation and from natural widget-value participation,</li>
  <li>lowering MAY later specialize these primitives into backend-oriented UI-binding operations, callable descriptors, handle-oriented operations, or equivalent lower forms,</li>
  <li>backend contracts MAY later declare consumer-facing assumptions about UI binding, UI capability support, or UI-interaction transport,</li>
  <li>runtime-private realization MAY choose private widget handles, tokens, dispatch tables, or host-binding objects,</li>
  <li>but none of those later stages redefines the intrinsic primitive identities or primitive-local contracts owned here.</li>
</ul>

<p>
This corridor matters:
</p>

<pre>
intrinsic primitive truth
    -&gt; frog.ui.* primitive-local contract

validated meaning
    -&gt; preserves semantic distinction between participation roles and UI-operation roles

open Execution IR
    -&gt; may preserve recognizable UI-operation execution objects

lowered form
    -&gt; may specialize them for a backend family

backend contract
    -&gt; may declare what a consumer may rely on

private runtime
    -&gt; may realize them through private widget-handle and host-binding machinery
</pre>

<p>
The primitive stays the same intrinsic primitive across that corridor.
Only the later representation and realization change.
</p>

<hr/>

<h2 id="examples">14. Examples</h2>

<h3>14.1 Property read</h3>

<pre><code>{
  "id": "read_label_text",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "widget_member": {
    "part": "label",
    "member": "text"
  }
}</code></pre>

<h3>14.2 Property write</h3>

<pre><code>{
  "id": "write_visible",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "widget_member": {
    "member": "visible"
  }
}</code></pre>

<h3>14.3 Method invoke</h3>

<pre><code>{
  "id": "invoke_focus",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "widget_method": {
    "name": "focus"
  }
}</code></pre>

<h3>14.4 Example diagram fragment</h3>

<pre><code>{
  "nodes": [
    {
      "id": "ctrl_gain_ref",
      "kind": "widget_reference",
      "widget": "ctrl_gain"
    },
    {
      "id": "read_gain_value_property",
      "kind": "primitive",
      "type": "frog.ui.property_read",
      "widget_member": {
        "member": "value"
      }
    },
    {
      "id": "write_visible",
      "kind": "primitive",
      "type": "frog.ui.property_write",
      "widget_member": {
        "member": "visible"
      }
    }
  ],
  "edges": [
    {
      "id": "e1",
      "from": { "node": "ctrl_gain_ref", "port": "ref" },
      "to":   { "node": "read_gain_value_property", "port": "ref" }
    },
    {
      "id": "e2",
      "from": { "node": "ctrl_gain_ref", "port": "ref" },
      "to":   { "node": "write_visible", "port": "ref" }
    }
  ]
}</code></pre>

<p>
In this example, reading member <code>value</code> through <code>frog.ui.property_read</code> remains object-style property access.
It is not the same thing as natural <code>widget_value</code> participation.
</p>

<hr/>

<h2 id="out-of-scope-for-v01">15. Out of Scope for v0.1</h2>

<ul>
  <li>a full standardized widget catalog,</li>
  <li>pixel-perfect cross-runtime rendering equivalence,</li>
  <li>a standardized first-class event execution model,</li>
  <li>registration-based event nodes,</li>
  <li>asynchronous callback delivery,</li>
  <li>a generalized widget-reference value type for arbitrary storage or transport,</li>
  <li>complete theme and style systems,</li>
  <li>automatic inference of UI sequencing in all cases,</li>
  <li>full standardization of all possible widget-library member sets,</li>
  <li>one mandatory Execution IR UI-object schema,</li>
  <li>one mandatory lowering family for UI interaction,</li>
  <li>one mandatory backend-family UI contract model,</li>
  <li>one mandatory runtime-private widget-handle architecture.</li>
</ul>

<hr/>

<h2 id="summary">16. Summary</h2>

<p>
The <code>frog.ui</code> library defines the intrinsic executable UI-interaction primitives of FROG v0.1:
</p>

<ul>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
</ul>

<p>
These primitives:
</p>

<ul>
  <li>consume widget references,</li>
  <li>use <code>widget_member</code> or <code>widget_method</code> metadata,</li>
  <li>support optional explicit UI sequencing through <code>ui_in</code> and <code>ui_out</code>,</li>
  <li>complement, but do not replace, the natural <code>widget_value</code> path,</li>
  <li>remain distinct from widget declarations, front-panel source, IR ownership, lowering ownership, backend-contract ownership, and runtime-private realization.</li>
</ul>

<p>
In short:
</p>

<ul>
  <li><strong><code>widget_value</code></strong> is the natural primary-value path,</li>
  <li><strong><code>widget_reference</code></strong> is the object-style reference path,</li>
  <li><strong><code>frog.ui.*</code></strong> is the intrinsic executable interaction vocabulary that consumes those references.</li>
</ul>
