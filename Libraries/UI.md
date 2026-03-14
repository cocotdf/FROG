<h1 align="center">🐸 FROG UI Library Specification</h1>

<p align="center">
Definition of the standard <strong>frog.ui</strong> primitive library for FROG v0.1<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope">2. Scope</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#namespace">4. Namespace</a></li>
  <li><a href="#standard-primitives">5. Standard Primitives for v0.1</a></li>
  <li><a href="#property-read">6. <code>frog.ui.property_read</code></a></li>
  <li><a href="#property-write">7. <code>frog.ui.property_write</code></a></li>
  <li><a href="#method-invoke">8. <code>frog.ui.method_invoke</code></a></li>
  <li><a href="#typing-and-sequencing">9. Typing and Sequencing</a></li>
  <li><a href="#validation-rules">10. Validation Rules</a></li>
  <li><a href="#examples">11. Examples</a></li>
  <li><a href="#out-of-scope">12. Out of Scope for v0.1</a></li>
  <li><a href="#summary">13. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the standard <code>frog.ui</code> primitive library for FROG v0.1.
</p>

<p>
The <code>frog.ui</code> library standardizes executable UI interaction primitives used by diagram nodes of kind <code>primitive</code>.
These primitives provide object-style interaction with widget instances and widget parts.
</p>

<p>
In FROG, ordinary primary widget value participation in dataflow is represented through <code>widget_value</code> nodes.
Object-style interaction is represented through <code>widget_reference</code> nodes consumed by standardized <code>frog.ui.*</code> primitives.
</p>

<p>
This document defines the primitive catalog for that interaction.
It does not define the widget object model, front-panel serialization, or general diagram graph structure.
</p>

<hr/>

<h2 id="scope">2. Scope</h2>

<p>
For FROG v0.1, this library standardizes the following primitive identifiers:
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
  <li>primitive-level validation rules.</li>
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
  <li>a first-class event-execution model,</li>
  <li>a generalized widget-reference value type for arbitrary storage or transport.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This document is used together with the rest of the FROG specification.
In particular:
</p>

<ul>
  <li><code>Libraries/Readme.md</code> defines the role of <code>Libraries/</code> as the standard primitive-library layer,</li>
  <li><code>Expression/Diagram.md</code> defines how primitive nodes appear in executable diagrams and how general node and edge structure is represented,</li>
  <li><code>Expression/Type.md</code> defines ordinary FROG type expressions and compatibility rules,</li>
  <li><code>Expression/Widget.md</code> defines widget classes, properties, methods, parts, and roles,</li>
  <li><code>Expression/Widget interaction.md</code> defines the canonical source-facing interaction model used by these primitives,</li>
  <li><code>Expression/Front panel.md</code> defines front-panel widget declaration and composition.</li>
</ul>

<p>
Ownership is intentionally split:
</p>

<ul>
  <li><code>Libraries/UI.md</code> owns primitive identities, signatures, primitive typing, sequencing behavior, and primitive-local semantics,</li>
  <li><code>Expression/Widget interaction.md</code> owns the source-facing interaction model,</li>
  <li><code>Expression/Diagram.md</code> owns the general graph representation model,</li>
  <li><code>Expression/Widget.md</code> owns widget member and method availability.</li>
</ul>

<hr/>

<h2 id="namespace">4. Namespace</h2>

<p>
The namespace defined by this library is:
</p>

<pre><code>frog.ui.*</code></pre>

<p>
This namespace is reserved for standardized executable UI interaction primitives.
</p>

<p>
It MUST be distinguished from widget-class namespaces such as:
</p>

<pre><code>frog.ui.standard.*</code></pre>

<p>
Accordingly:
</p>

<ul>
  <li><code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code> are primitive identifiers,</li>
  <li><code>frog.ui.standard.numeric_control</code> and similar identifiers are widget-class identifiers.</li>
</ul>

<hr/>

<h2 id="standard-primitives">5. Standard Primitives for v0.1</h2>

<p>
FROG v0.1 standardizes the following <code>frog.ui</code> primitives:
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
  <li>MUST be valid primitive identifiers in the active library catalog,</li>
  <li>MUST consume a widget reference through required input port <code>ref</code>,</li>
  <li>MAY expose optional sequencing ports <code>ui_in</code> and <code>ui_out</code>,</li>
  <li>MUST use <code>widget_member</code> or <code>widget_method</code> metadata as appropriate.</li>
</ul>

<p>
These primitives are object-style interaction primitives.
They do not replace the natural primary-value path represented by <code>widget_value</code>.
</p>

<hr/>

<h2 id="property-read">6. <code>frog.ui.property_read</code></h2>

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
  <li>the addressed property MUST be readable for the addressed widget member under the active widget profile,</li>
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
  <li>if <code>ui_out</code> is connected, it MUST become available only after the read has completed.</li>
</ul>

<hr/>

<h2 id="property-write">7. <code>frog.ui.property_write</code></h2>

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
  <li>the addressed property MUST be writable for the addressed widget member under the active widget profile,</li>
  <li>the input port <code>value</code> MUST be type-compatible with the declared type of the addressed property.</li>
</ul>

<p>
Writing <code>{ "member": "value" }</code> is valid when the widget class exposes <code>value</code> as a writable property.
This object-style write MUST remain semantically distinct from the natural primary-value path represented by <code>widget_value</code>.
For ordinary widget value participation in dataflow, tools SHOULD prefer the natural <code>widget_value</code> representation.
</p>

<p>
Primitive-local semantics:
</p>

<ul>
  <li>a property write applies a UI side effect to the addressed widget member,</li>
  <li>if <code>ui_in</code> is connected, the write MUST occur only after the incoming sequencing token becomes available,</li>
  <li>if <code>ui_out</code> is connected, it MUST become available only after the write has completed according to the active runtime profile.</li>
</ul>

<hr/>

<h2 id="method-invoke">8. <code>frog.ui.method_invoke</code></h2>

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
  <li>zero or more method argument input ports in canonical method order,</li>
  <li>optional input port <code>ui_in</code>,</li>
  <li>zero or more method result output ports in canonical method order,</li>
  <li>optional output port <code>ui_out</code>.</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>the primitive MUST declare <code>widget_method</code>,</li>
  <li>the addressed method MUST exist for the addressed widget member under the active widget profile,</li>
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
  <li>if <code>ui_out</code> is connected, it MUST become available only after invocation has completed according to the active runtime profile.</li>
</ul>

<hr/>

<h2 id="typing-and-sequencing">9. Typing and Sequencing</h2>

<h3>9.1 Widget reference typing</h3>

<p>
The required input port <code>ref</code> carries an opaque widget reference token.
In v0.1, this token is interaction-oriented and diagram-internal.
It is not standardized here as a general-purpose first-class value type for arbitrary storage, transport, or computation.
</p>

<h3>9.2 Property typing</h3>

<p>
Property-read and property-write primitives MUST use the declared property type of the addressed widget member.
Compatibility checks and implicit coercions MUST follow the ordinary FROG type rules.
</p>

<h3>9.3 Method typing</h3>

<p>
Method-invoke primitives MUST use the declared method signature of the addressed widget member.
Argument and result ports MUST follow the canonical method signature defined by the active widget profile.
</p>

<h3>9.4 UI sequencing ports</h3>

<p>
The optional ports <code>ui_in</code> and <code>ui_out</code> define explicit ordering between UI interactions.
These ports:
</p>

<ul>
  <li>MUST NOT be interpreted as ordinary data values,</li>
  <li>MUST NOT redefine ordinary data dependency typing,</li>
  <li>MAY be omitted when no explicit UI ordering is required,</li>
  <li>SHOULD be used when deterministic ordering of UI side effects matters.</li>
</ul>

<p>
In v0.1, the sequencing token carried by <code>ui_in</code> and <code>ui_out</code> is opaque.
Its runtime representation is implementation-defined, but its ordering meaning between standardized UI interaction primitives is defined by this specification.
</p>

<hr/>

<h2 id="validation-rules">10. Validation Rules</h2>

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
  <li>part names, member names, and method names MUST be valid for the addressed widget class or active widget profile.</li>
</ul>

<p>
Invalid UI interaction primitives MUST trigger validation errors.
</p>

<p>
Source-level graph-shape constraints remain owned by <code>Expression/Widget interaction.md</code> and <code>Expression/Diagram.md</code>.
</p>

<hr/>

<h2 id="examples">11. Examples</h2>

<h3>11.1 Property read</h3>

<pre><code>{
  "id": "read_label_text",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "widget_member": {
    "part": "label",
    "member": "text"
  }
}</code></pre>

<h3>11.2 Property write</h3>

<pre><code>{
  "id": "write_visible",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "widget_member": {
    "member": "visible"
  }
}</code></pre>

<h3>11.3 Method invoke</h3>

<pre><code>{
  "id": "invoke_focus",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "widget_method": {
    "name": "focus"
  }
}</code></pre>

<h3>11.4 Example diagram fragment</h3>

<pre><code>{
  "nodes": [
    {
      "id": "ctrl_gain_ref",
      "kind": "widget_reference",
      "widget": "ctrl_gain"
    },
    {
      "id": "read_gain_value",
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
      "to":   { "node": "read_gain_value", "port": "ref" }
    },
    {
      "id": "e2",
      "from": { "node": "ctrl_gain_ref", "port": "ref" },
      "to":   { "node": "write_visible", "port": "ref" }
    }
  ]
}</code></pre>

<hr/>

<h2 id="out-of-scope">12. Out of Scope for v0.1</h2>

<ul>
  <li>a full standardized widget catalog,</li>
  <li>pixel-perfect cross-runtime rendering equivalence,</li>
  <li>a standardized first-class event execution model,</li>
  <li>registration-based event nodes,</li>
  <li>asynchronous callback delivery,</li>
  <li>a generalized widget-reference value type for arbitrary storage or transport,</li>
  <li>complete theme and style systems,</li>
  <li>automatic inference of UI sequencing in all cases,</li>
  <li>full standardization of all possible widget-library member sets.</li>
</ul>

<hr/>

<h2 id="summary">13. Summary</h2>

<p>
The <code>frog.ui</code> library defines the standard executable UI interaction primitives of FROG v0.1.
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
  <li>complement, but do not replace, the natural <code>widget_value</code> path.</li>
</ul>

<p>
In short:
</p>

<ul>
  <li><strong><code>widget_value</code></strong> is the natural primary-value path,</li>
  <li><strong><code>widget_reference</code></strong> is the object-style reference path,</li>
  <li><strong><code>frog.ui.*</code></strong> is the standardized executable interaction vocabulary that consumes those references.</li>
</ul>
