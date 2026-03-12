<h1 align="center">🐸 FROG UI Library Specification</h1>

<p align="center">
Definition of the standard <strong>frog.ui</strong> primitive library for FROG v0.1<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope">2. Scope of v0.1</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#namespace-and-role">4. Namespace and Role of <code>frog.ui</code></a></li>
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
This document defines the standard <strong>frog.ui</strong> primitive library for FROG v0.1.
</p>

<p>
The <code>frog.ui</code> library standardizes executable UI interaction primitives used inside validated executable diagrams.
These primitives provide object-style interaction with front-panel widgets and widget parts.
</p>

<p>
In FROG, ordinary primary widget value participation in dataflow is represented naturally through <code>widget_value</code> nodes.
Object-style interaction beyond the natural primary-value path is represented through <code>widget_reference</code> nodes consumed by standardized <code>frog.ui.*</code> primitives.
</p>

<p>
Accordingly, this library defines the executable primitive vocabulary for reading properties, writing properties, and invoking methods on widgets.
It does not redefine the widget object model, the front-panel serialization model, or the general diagram graph structure.
</p>

<hr/>

<h2 id="scope">2. Scope of v0.1</h2>

<p>
For FROG v0.1, this library standardizes the following executable UI primitives:
</p>

<ul>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
</ul>

<p>
This library defines:
</p>

<ul>
  <li>their stable primitive identifiers</li>
  <li>their required structural metadata</li>
  <li>their canonical port signatures</li>
  <li>their typing constraints</li>
  <li>their sequencing semantics</li>
  <li>their validation requirements</li>
</ul>

<p>
This library does <strong>not</strong> define:
</p>

<ul>
  <li>the full widget class catalog</li>
  <li>front-panel widget serialization</li>
  <li>the natural <code>widget_value</code> model</li>
  <li>the <code>widget_reference</code> node kind itself</li>
  <li>a first-class event-execution model</li>
  <li>a generalized widget-reference value type for arbitrary storage or transport</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This library specification is used together with the rest of the FROG specification.
In particular:
</p>

<ul>
  <li><strong><code>Expression/Diagram.md</code></strong> defines how UI interaction primitives appear as executable graph nodes inside a validated diagram</li>
  <li><strong><code>Expression/Type.md</code></strong> defines the type syntax, compatibility rules, and coercion rules used by primitive ports</li>
  <li><strong><code>Expression/Front panel.md</code></strong> defines front-panel serialization, including widget instances and <code>ui_libraries</code></li>
  <li><strong><code>Expression/Widget.md</code></strong> defines the widget object model, widget classes, properties, methods, parts, and roles</li>
  <li><strong><code>Expression/Widget interaction.md</code></strong> defines the canonical source-level interaction model used by these primitives</li>
</ul>

<p>
Accordingly, this document does not stand alone.
It defines the standard primitive catalog for UI interaction, while the rest of the repository defines the source structure and the widget semantics on which this catalog depends.
</p>

<hr/>

<h2 id="namespace-and-role">4. Namespace and Role of <code>frog.ui</code></h2>

<p>
The namespace defined by this library is:
</p>

<pre>
frog.ui.*
</pre>

<p>
This namespace is reserved for standardized executable UI interaction primitives.
</p>

<p>
It is important to distinguish:
</p>

<ul>
  <li><code>frog.ui.*</code> — executable primitive nodes used inside diagrams</li>
  <li><code>frog.ui.standard.*</code> — widget classes or widget-library identifiers used by the front panel and widget model</li>
</ul>

<p>
Therefore:
</p>

<ul>
  <li><code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code> are primitive identifiers</li>
  <li><code>frog.ui.standard.numeric_control</code> or similar identifiers are widget-class identifiers, not primitive identifiers</li>
</ul>

<p>
This separation keeps:
</p>

<ul>
  <li>the executable primitive vocabulary,</li>
  <li>the widget catalog,</li>
  <li>the front-panel source model</li>
</ul>

<p>
as distinct specification responsibilities.
</p>

<hr/>

<h2 id="standard-primitives">5. Standard Primitives for v0.1</h2>

<p>
FROG v0.1 standardizes the following <code>frog.ui</code> primitives:
</p>

<ul>
  <li><code>frog.ui.property_read</code> — reads a property from a widget or widget part</li>
  <li><code>frog.ui.property_write</code> — writes a property of a widget or widget part</li>
  <li><code>frog.ui.method_invoke</code> — invokes a method on a widget or widget part</li>
</ul>

<p>
All three primitives:
</p>

<ul>
  <li>MUST appear as diagram nodes of kind <code>primitive</code></li>
  <li>MUST consume a compatible widget reference through required input port <code>ref</code></li>
  <li>MAY expose optional sequencing ports <code>ui_in</code> and <code>ui_out</code></li>
  <li>MUST use widget metadata declared through <code>widget_member</code> or <code>widget_method</code> as appropriate</li>
</ul>

<p>
These primitives are object-style interaction primitives.
They do not replace the natural primary-value path represented by <code>widget_value</code>.
</p>

<hr/>

<h2 id="property-read">6. <code>frog.ui.property_read</code></h2>

<p>
The primitive identifier is:
</p>

<pre>
frog.ui.property_read
</pre>

<p>
A property read node reads a property value from a widget or widget part and exposes that value to the diagram.
</p>

<p>
Required structural fields:
</p>

<pre>
{
  "id": "read_gain_visible",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "widget_member": {
    "member": "visible"
  }
}
</pre>

<p>
Canonical port signature:
</p>

<ul>
  <li>required input port <code>ref</code></li>
  <li>optional input port <code>ui_in</code></li>
  <li>required output port <code>value</code></li>
  <li>optional output port <code>ui_out</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>the output port <code>value</code> MUST have the type of the addressed property</li>
  <li>the addressed property MUST be readable under the active widget profile</li>
  <li>the <code>ref</code> port MUST carry a widget reference compatible with the addressed widget</li>
</ul>

<p>
Reading <code>{ "member": "value" }</code> through <code>frog.ui.property_read</code> is valid when the widget class exposes <code>value</code> as a readable property.
However, when the intent is ordinary primary-value dataflow, tools SHOULD prefer the natural <code>widget_value</code> representation.
</p>

<p>
Semantics:
</p>

<ul>
  <li>the read observes the current property value at execution time</li>
  <li>if <code>ui_in</code> is connected, the read MUST occur only after the preceding sequencing token becomes available</li>
  <li>if <code>ui_out</code> is connected, it MUST become available only after the read has completed</li>
</ul>

<hr/>

<h2 id="property-write">7. <code>frog.ui.property_write</code></h2>

<p>
The primitive identifier is:
</p>

<pre>
frog.ui.property_write
</pre>

<p>
A property write node writes a diagram value into a writable property of a widget or widget part.
</p>

<p>
Required structural fields:
</p>

<pre>
{
  "id": "write_gain_label",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "widget_member": {
    "part": "label",
    "member": "text"
  }
}
</pre>

<p>
Canonical port signature:
</p>

<ul>
  <li>required input port <code>ref</code></li>
  <li>required input port <code>value</code></li>
  <li>optional input port <code>ui_in</code></li>
  <li>optional output port <code>ui_out</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>the input port <code>value</code> MUST be type-compatible with the addressed property type</li>
  <li>the addressed property MUST be writable under the active widget profile</li>
  <li>the <code>ref</code> port MUST carry a widget reference compatible with the addressed widget</li>
</ul>

<p>
Writing <code>{ "member": "value" }</code> through <code>frog.ui.property_write</code> is valid when the widget class exposes <code>value</code> as a writable property.
This object-style write MUST remain semantically distinct from the natural primary-value path represented by <code>widget_value</code>.
For ordinary widget value participation in dataflow, tools SHOULD prefer the natural <code>widget_value</code> representation.
</p>

<p>
Semantics:
</p>

<ul>
  <li>a property write applies a UI side effect to the addressed widget member</li>
  <li>if <code>ui_in</code> is connected, the write MUST occur only after the preceding sequencing token becomes available</li>
  <li>if <code>ui_out</code> is connected, it MUST become available only after the write has completed according to the active runtime profile</li>
</ul>

<hr/>

<h2 id="method-invoke">8. <code>frog.ui.method_invoke</code></h2>

<p>
The primitive identifier is:
</p>

<pre>
frog.ui.method_invoke
</pre>

<p>
A method invoke node calls a method on a widget or widget part.
</p>

<p>
Required structural fields:
</p>

<pre>
{
  "id": "invoke_reset",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "widget_method": {
    "name": "reset_to_default"
  }
}
</pre>

<p>
Canonical port signature:
</p>

<ul>
  <li>required input port <code>ref</code></li>
  <li>zero or more method argument input ports, in canonical method order</li>
  <li>optional input port <code>ui_in</code></li>
  <li>zero or more method result output ports, in canonical method order</li>
  <li>optional output port <code>ui_out</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>method argument input port names MUST match the canonical method signature of the addressed method</li>
  <li>method result output port names MUST match the canonical method signature of the addressed method</li>
  <li>each method argument input MUST be type-compatible with the declared parameter type</li>
  <li>each method result output MUST have the declared result type</li>
  <li>the addressed method MUST exist for the addressed widget member under the active widget profile</li>
</ul>

<p>
Semantics:
</p>

<ul>
  <li>a method invocation MAY produce UI side effects, ordinary return values, or both</li>
  <li>if <code>ui_in</code> is connected, the invocation MUST occur only after the preceding sequencing token becomes available</li>
  <li>if <code>ui_out</code> is connected, it MUST become available only after invocation has completed according to the active runtime profile</li>
</ul>

<hr/>

<h2 id="typing-and-sequencing">9. Typing and Sequencing</h2>

<h3>9.1 Widget reference typing</h3>

<p>
The input port <code>ref</code> carries an opaque widget reference token.
In v0.1, this token is interaction-oriented and diagram-internal.
It is not standardized here as a general-purpose first-class value type for arbitrary storage, transport, or computation.
</p>

<h3>9.2 Property typing</h3>

<p>
Property read and property write primitives MUST use the declared property type of the addressed widget member.
All compatibility checks and implicit coercions MUST follow the ordinary FROG type rules.
</p>

<h3>9.3 Method typing</h3>

<p>
Method invoke primitives MUST use the declared method signature of the addressed widget member.
Argument and result ports MUST follow the canonical method signature defined by the widget class under the active profile.
</p>

<h3>9.4 UI sequencing ports</h3>

<p>
The optional ports <code>ui_in</code> and <code>ui_out</code> define explicit ordering between UI interactions.
These ports:
</p>

<ul>
  <li>MUST NOT be interpreted as ordinary data values</li>
  <li>MUST NOT redefine ordinary data dependency typing</li>
  <li>MAY be omitted when no explicit UI ordering is required</li>
  <li>SHOULD be used when deterministic ordering of UI side effects matters</li>
</ul>

<p>
In v0.1, the sequencing token carried by <code>ui_in</code> / <code>ui_out</code> is opaque.
Its internal runtime representation is implementation-defined, but its ordering meaning in the graph is standardized by this document.
</p>

<hr/>

<h2 id="validation-rules">10. Validation Rules</h2>

<p>
Implementations MUST enforce the following rules:
</p>

<ul>
  <li>a <code>frog.ui.*</code> primitive MUST appear as a node of kind <code>primitive</code></li>
  <li>the primitive identifier MUST be one of the standardized identifiers defined by this document</li>
  <li>the node MUST consume a compatible widget reference through required input port <code>ref</code></li>
  <li>a property node MUST declare <code>widget_member</code></li>
  <li>a method node MUST declare <code>widget_method</code></li>
  <li>a widget interaction node MUST NOT identify its target only through ad hoc local string fields unrelated to the widget reference model</li>
  <li>ordinary value ports MUST be represented through ordinary diagram edges</li>
  <li>explicit UI ordering, when used, MUST be represented through <code>ui_in</code> / <code>ui_out</code> edges</li>
</ul>

<p>
Additionally:
</p>

<ul>
  <li><code>frog.ui.property_read</code> MUST address a readable property</li>
  <li><code>frog.ui.property_write</code> MUST address a writable property</li>
  <li><code>frog.ui.method_invoke</code> MUST address a valid method</li>
  <li>part names, member names, and method names MUST be valid for the addressed widget class or active profile</li>
</ul>

<p>
Invalid widget interaction primitives MUST trigger validation errors.
</p>

<hr/>

<h2 id="examples">11. Examples</h2>

<h3>11.1 Property read</h3>

<pre>
{
  "id": "read_label_text",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "widget_member": {
    "part": "label",
    "member": "text"
  }
}
</pre>

<h3>11.2 Property write</h3>

<pre>
{
  "id": "write_visible",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "widget_member": {
    "member": "visible"
  }
}
</pre>

<h3>11.3 Method invoke</h3>

<pre>
{
  "id": "invoke_focus",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "widget_method": {
    "name": "focus"
  }
}
</pre>

<h3>11.4 Example diagram fragment</h3>

<pre>
{
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
}
</pre>

<hr/>

<h2 id="out-of-scope">12. Out of Scope for v0.1</h2>

<ul>
  <li>a full industrial UI widget catalog</li>
  <li>pixel-perfect cross-runtime rendering equivalence</li>
  <li>a standardized first-class event structure for executable event handling</li>
  <li>registration-based event nodes</li>
  <li>asynchronous callback delivery</li>
  <li>a generalized widget reference value type for arbitrary storage or transport</li>
  <li>complete theme and style systems</li>
  <li>automatic inference of UI sequencing in all cases</li>
  <li>full standardization of every possible widget-library member set</li>
</ul>

<hr/>

<h2 id="summary">13. Summary</h2>

<p>
The <code>frog.ui</code> library defines the standard executable UI interaction primitives of FROG v0.1.
</p>

<p>
In v0.1, it standardizes:
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
  <li>operate on widget references</li>
  <li>use <code>widget_member</code> or <code>widget_method</code> metadata</li>
  <li>support optional explicit UI sequencing through <code>ui_in</code> / <code>ui_out</code></li>
  <li>complement, but do not replace, the natural <code>widget_value</code> path</li>
</ul>

<p>
In short:
</p>

<ul>
  <li><strong><code>widget_value</code></strong> is the natural primary-value path</li>
  <li><strong><code>widget_reference</code></strong> is the object-style widget reference path</li>
  <li><strong><code>frog.ui.*</code></strong> defines the standardized primitive interaction vocabulary that consumes those references</li>
</ul>
