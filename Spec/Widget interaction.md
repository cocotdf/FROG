<h1 align="center">🐸 FROG Widget Interaction Specification</h1>

<p align="center">
Definition of diagram-level interaction with front panel widgets in <strong>.frog</strong> programs<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Goals</a></li>
  <li><a href="#scope">3. Scope for v0.1</a></li>
  <li><a href="#relation-with-other-specifications">4. Relation with Other Specifications</a></li>
  <li><a href="#conceptual-model">5. Conceptual Model</a></li>
  <li><a href="#widget-member-addressing">6. Widget Member Addressing</a></li>
  <li><a href="#interaction-node-families">7. Interaction Node Families</a></li>
  <li><a href="#property-read-node">8. Property Read Node</a></li>
  <li><a href="#property-write-node">9. Property Write Node</a></li>
  <li><a href="#method-invoke-node">10. Method Invoke Node</a></li>
  <li><a href="#typing-rules">11. Typing Rules</a></li>
  <li><a href="#diagram-representation">12. Diagram Representation</a></li>
  <li><a href="#validation-rules">13. Validation Rules</a></li>
  <li><a href="#execution-semantics">14. Execution Semantics</a></li>
  <li><a href="#examples">15. Examples</a></li>
  <li><a href="#out-of-scope">16. Out of Scope for v0.1</a></li>
  <li><a href="#summary">17. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
FROG widgets are structured UI objects defined by <code>Widget.md</code>
and instantiated inside the <code>front_panel</code> section defined by <code>Front panel.md</code>.
</p>

<p>
This document defines how the executable diagram may interact with those widget instances
through object-style widget interaction primitives.
</p>

<p>
For v0.1, FROG standardizes three diagram-level widget interaction families:
</p>

<ul>
  <li><strong>property read</strong> — read a widget or widget-part property,</li>
  <li><strong>property write</strong> — write a widget or widget-part property,</li>
  <li><strong>method invoke</strong> — call a widget or widget-part method.</li>
</ul>

<p>
These interactions allow the diagram to manipulate front panel objects
in a structured and type-aware way without confusing widget objects with ordinary dataflow values.
</p>

<p>
The primary widget value has a special status in FROG:
it participates naturally in the diagram through the implicit widget value terminal model
described by <code>Widget.md</code> and <code>Diagram.md</code>.
However, that same primary value remains an ordinary widget property in the object model,
and may therefore also be accessed through widget interaction primitives.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<p>
The widget interaction model is designed to satisfy the following goals:
</p>

<ul>
  <li><strong>Object consistency</strong> — widget interactions should follow the widget object model rather than ad hoc UI hacks.</li>
  <li><strong>Type safety</strong> — widget properties and method ports must be typed consistently with the FROG type system.</li>
  <li><strong>Diagram compatibility</strong> — widget interactions should integrate cleanly into the dataflow graph.</li>
  <li><strong>Extensibility</strong> — different widget classes may expose different members while still following a common addressing model.</li>
  <li><strong>Separation of concerns</strong> — UI interaction should not redefine interface semantics or general execution semantics.</li>
  <li><strong>Architectural clarity</strong> — the natural dataflow path for a widget value should remain distinct from explicit object-style access.</li>
</ul>

<hr/>

<h2 id="scope">3. Scope for v0.1</h2>

<p>
FROG v0.1 standardizes:
</p>

<ul>
  <li>the conceptual addressing model for widget members,</li>
  <li>property read interactions,</li>
  <li>property write interactions,</li>
  <li>method invocation interactions,</li>
  <li>their type and validation rules,</li>
  <li>their integration with the widget reference model.</li>
</ul>

<p>
FROG v0.1 does <strong>not</strong> fully standardize:
</p>

<ul>
  <li>an event loop model,</li>
  <li>widget event registration nodes,</li>
  <li>asynchronous UI message delivery,</li>
  <li>runtime widget references as first-class general-purpose FROG value types,</li>
  <li>full effect-ordering semantics between independent UI mutations.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">4. Relation with Other Specifications</h2>

<p>
This document depends on the following FROG specifications:
</p>

<ul>
  <li><strong>Type.md</strong> — defines ordinary value typing and compatibility rules,</li>
  <li><strong>Widget.md</strong> — defines widget classes, roles, parts, properties, methods, and allowed members,</li>
  <li><strong>Front panel.md</strong> — defines how widget instances are serialized in the <code>front_panel</code> section,</li>
  <li><strong>Diagram.md</strong> — defines the executable graph model in which widget interaction primitives appear.</li>
</ul>

<p>
This document does not redefine widget classes themselves.
It defines how diagram nodes interact with widget objects already defined elsewhere.
</p>

<p>
This document also complements the <code>widget_value</code> and <code>widget_reference</code> node kinds defined by <code>Diagram.md</code>:
</p>

<ul>
  <li><code>widget_value</code> is the natural dataflow representation of the primary widget value,</li>
  <li><code>widget_reference</code> is the object-style access path used by the interaction primitives defined here.</li>
</ul>

<hr/>

<h2 id="conceptual-model">5. Conceptual Model</h2>

<p>
A diagram may interact with a widget member.
A widget member is one of:
</p>

<ul>
  <li>a widget property,</li>
  <li>a widget-part property,</li>
  <li>a widget method,</li>
  <li>a widget-part method.</li>
</ul>

<p>
Examples:
</p>

<ul>
  <li><code>ctrl_gain.value</code></li>
  <li><code>ctrl_gain.visible</code></li>
  <li><code>ctrl_gain.label.text</code></li>
  <li><code>ctrl_gain.focus()</code></li>
  <li><code>graph_1.x_scale.visible</code></li>
</ul>

<p>
FROG distinguishes two paths for widget interaction:
</p>

<ul>
  <li><strong>natural value path</strong> — through the implicit widget value terminal represented by <code>widget_value</code>,</li>
  <li><strong>object-style path</strong> — through <code>widget_reference</code> and the interaction primitives defined in this document.</li>
</ul>

<p>
The primary widget value therefore has a dual status:
</p>

<ul>
  <li>it is the natural value terminal of a value-carrying widget,</li>
  <li>it is also an ordinary widget property accessible through object-style interaction.</li>
</ul>

<p>
A widget interaction node does not replace the widget instance itself.
It merely reads, writes, or invokes a member of a widget object defined in the front panel.
</p>

<hr/>

<h2 id="widget-member-addressing">6. Widget Member Addressing</h2>

<p>
Widget member addressing identifies:
</p>

<ul>
  <li>the target widget instance,</li>
  <li>optionally a named part of that widget,</li>
  <li>the addressed member name.</li>
</ul>

<h3>6.1 Full conceptual address</h3>

<p>
A full conceptual address may be understood as:
</p>

<pre><code>{
  "widget": "ctrl_gain",
  "part": "label",
  "member": "text"
}</code></pre>

<p>
Fields:
</p>

<ul>
  <li><code>widget</code> — widget instance identifier,</li>
  <li><code>part</code> — optional named widget part,</li>
  <li><code>member</code> — property or method name.</li>
</ul>

<h3>6.2 Primitive-local member descriptor</h3>

<p>
In the base diagram model of v0.1,
the widget identity is normally carried by an incoming widget reference,
not directly embedded in the primitive node.
</p>

<p>
Therefore, interaction primitives SHOULD use a member descriptor of the following form:
</p>

<pre><code>{
  "member": "text"
}</code></pre>

<p>
or, for a widget part:
</p>

<pre><code>{
  "part": "label",
  "member": "text"
}</code></pre>

<p>
This means:
</p>

<ul>
  <li>the incoming <code>ref</code> port identifies the widget instance,</li>
  <li>the primitive-local member descriptor identifies what is being addressed on that widget.</li>
</ul>

<h3>6.3 Widget-level member addressing</h3>

<p>
If <code>part</code> is omitted, the member belongs to the widget itself.
</p>

<p>
Examples:
</p>

<pre><code>{ "member": "value" }
{ "member": "visible" }
{ "member": "focus" }</code></pre>

<h3>6.4 Part-level member addressing</h3>

<p>
If <code>part</code> is present, the member belongs to the named widget part.
</p>

<p>
Examples:
</p>

<pre><code>{ "part": "label", "member": "text" }
{ "part": "label", "member": "visible" }</code></pre>

<h3>6.5 Address validity</h3>

<p>
A widget member address is valid only if:
</p>

<ul>
  <li>the referenced widget exists in the <code>front_panel</code>,</li>
  <li>the referenced part exists if specified,</li>
  <li>the addressed member exists for the widget class or part class under the active profile.</li>
</ul>

<hr/>

<h2 id="interaction-node-families">7. Interaction Node Families</h2>

<p>
For v0.1, widget interactions are represented as standardized primitive nodes inside the diagram.
</p>

<p>
This keeps the interaction model compatible with the existing <code>primitive</code> node category defined in <code>Diagram.md</code>.
</p>

<p>
The standardized interaction primitive types are:
</p>

<ul>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
</ul>

<p>
Each such node MUST use:
</p>

<ul>
  <li><code>kind</code> = <code>primitive</code></li>
  <li><code>type</code> = one of the standardized widget interaction primitive identifiers above.</li>
</ul>

<p>
In the base model, each such node also consumes a widget reference through an input port named <code>ref</code>.
</p>

<p>
The node SHOULD declare its target member using a member descriptor such as:
</p>

<pre><code>"widget_member": {
  "part": "label",
  "member": "text"
}</code></pre>

<p>
or:
</p>

<pre><code>"widget_method": {
  "name": "focus"
}</code></pre>

<p>
The exact field naming MAY be profile-defined,
but the conceptual distinction between:
</p>

<ul>
  <li>the widget reference input, and</li>
  <li>the addressed member description</li>
</ul>

<p>
is normative.
</p>

<hr/>

<h2 id="property-read-node">8. Property Read Node</h2>

<p>
A property read node reads a property value from a widget or widget part
and exposes it to the diagram as an output.
</p>

<h3>8.1 Purpose</h3>

<p>
Typical uses:
</p>

<ul>
  <li>read widget visibility state,</li>
  <li>read label text,</li>
  <li>read other readable widget configuration values,</li>
  <li>explicitly read the <code>value</code> property through the object model when desired.</li>
</ul>

<h3>8.2 Standard primitive identifier</h3>

<pre><code>frog.ui.property_read</code></pre>

<h3>8.3 Required node fields</h3>

<pre><code>{
  "id": "read_gain_visible",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "widget_member": {
    "member": "visible"
  }
}</code></pre>

<h3>8.4 Standard port signature</h3>

<p>
A property read node exposes:
</p>

<ul>
  <li>one input port named <code>ref</code>,</li>
  <li>one output port named <code>value</code>.</li>
</ul>

<p>
The output type is the type of the addressed property.
The <code>ref</code> port carries an opaque widget reference token compatible with the addressed widget.
</p>

<h3>8.5 Access to <code>value</code></h3>

<p>
Reading <code>member = "value"</code> through <code>frog.ui.property_read</code> is valid.
</p>

<p>
However, when the intent is ordinary dataflow wiring of a widget primary value,
tools SHOULD prefer the natural <code>widget_value</code> representation.
</p>

<h3>8.6 Example</h3>

<p>
Reading the numeric value property of a widget explicitly through the object model:
</p>

<pre><code>{
  "id": "read_gain_value",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "widget_member": {
    "member": "value"
  }
}</code></pre>

<hr/>

<h2 id="property-write-node">9. Property Write Node</h2>

<p>
A property write node writes a value from the diagram into a writable widget or widget-part property.
</p>

<h3>9.1 Purpose</h3>

<p>
Typical uses:
</p>

<ul>
  <li>change widget visibility,</li>
  <li>change label text,</li>
  <li>set a visual or state property from program logic,</li>
  <li>explicitly write the <code>value</code> property through the object model when desired.</li>
</ul>

<h3>9.2 Standard primitive identifier</h3>

<pre><code>frog.ui.property_write</code></pre>

<h3>9.3 Required node fields</h3>

<pre><code>{
  "id": "write_gain_label",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "widget_member": {
    "part": "label",
    "member": "text"
  }
}</code></pre>

<h3>9.4 Standard port signature</h3>

<p>
A property write node exposes:
</p>

<ul>
  <li>one input port named <code>ref</code>,</li>
  <li>one input port named <code>value</code>,</li>
  <li>no required data output.</li>
</ul>

<p>
The <code>value</code> input type is the type of the addressed property.
The <code>ref</code> port carries an opaque widget reference token compatible with the addressed widget.
</p>

<h3>9.5 Access to <code>value</code></h3>

<p>
Writing <code>member = "value"</code> through <code>frog.ui.property_write</code> is valid.
</p>

<p>
However, when the intent is ordinary dataflow wiring to a widget primary value,
tools SHOULD prefer the natural <code>widget_value</code> representation.
</p>

<h3>9.6 Example</h3>

<p>
Writing the text of a widget label:
</p>

<pre><code>{
  "id": "write_gain_label_text",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "widget_member": {
    "part": "label",
    "member": "text"
  }
}</code></pre>

<hr/>

<h2 id="method-invoke-node">10. Method Invoke Node</h2>

<p>
A method invoke node calls a widget or widget-part method.
</p>

<h3>10.1 Purpose</h3>

<p>
Typical uses:
</p>

<ul>
  <li>focus a control,</li>
  <li>reset a widget to its default state,</li>
  <li>show or hide a widget through an explicit action method,</li>
  <li>call other class-defined interaction behavior.</li>
</ul>

<h3>10.2 Standard primitive identifier</h3>

<pre><code>frog.ui.method_invoke</code></pre>

<h3>10.3 Required node fields</h3>

<pre><code>{
  "id": "focus_name_ctrl",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "widget_method": {
    "name": "focus"
  }
}</code></pre>

<h3>10.4 Standard port signature</h3>

<p>
A method invoke node exposes:
</p>

<ul>
  <li>one input port named <code>ref</code>,</li>
  <li>zero or more input ports for method parameters,</li>
  <li>zero or more output ports for method return values.</li>
</ul>

<p>
The exact parameter and return structure of a method is defined by the widget class or part class under the active profile.
</p>

<h3>10.5 Example</h3>

<p>
Invoking a focus method with no parameters and no data outputs:
</p>

<pre><code>{
  "id": "focus_name_ctrl",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "widget_method": {
    "name": "focus"
  }
}</code></pre>

<hr/>

<h2 id="typing-rules">11. Typing Rules</h2>

<p>
Widget interaction nodes are typed through:
</p>

<ul>
  <li>the addressed widget class,</li>
  <li>the addressed part class when applicable,</li>
  <li>the addressed property or method signature.</li>
</ul>

<h3>11.1 Reference typing</h3>

<p>
The <code>ref</code> port used by widget interaction primitives carries an opaque widget reference token.
</p>

<p>
In v0.1, this token is not standardized as a general-purpose user-level FROG data type.
It exists specifically to connect <code>widget_reference</code> nodes to widget interaction primitives.
</p>

<h3>11.2 Property read typing</h3>

<p>
For <code>frog.ui.property_read</code>:
</p>

<ul>
  <li>the output port <code>value</code> MUST have the type of the addressed property.</li>
</ul>

<p>
Examples:
</p>

<ul>
  <li>reading <code>value</code> of a numeric control may produce <code>f64</code>,</li>
  <li>reading <code>visible</code> produces <code>bool</code>,</li>
  <li>reading <code>label.text</code> produces <code>string</code>.</li>
</ul>

<h3>11.3 Property write typing</h3>

<p>
For <code>frog.ui.property_write</code>:
</p>

<ul>
  <li>the input port <code>value</code> MUST have the type of the addressed property.</li>
</ul>

<p>
Incoming edges MUST be compatible with that property type according to <code>Type.md</code>.
</p>

<h3>11.4 Method typing</h3>

<p>
For <code>frog.ui.method_invoke</code>:
</p>

<ul>
  <li>input port types other than <code>ref</code> are the parameter types of the addressed method,</li>
  <li>output port types are the return types of the addressed method.</li>
</ul>

<h3>11.5 Compatibility</h3>

<p>
Standard FROG type compatibility and implicit coercion rules apply to ordinary value ports of widget interaction nodes
in the same way they apply to other diagram ports.
</p>

<hr/>

<h2 id="diagram-representation">12. Diagram Representation</h2>

<p>
Widget interaction nodes are serialized as primitive nodes in the diagram.
</p>

<p>
In the base model, they are expected to consume a widget reference produced by a <code>widget_reference</code> node.
</p>

<h3>12.1 Property read</h3>

<pre><code>{
  "id": "read_gain_visible",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "widget_member": {
    "member": "visible"
  },
  "layout": {
    "x": 320,
    "y": 80
  }
}</code></pre>

<h3>12.2 Property write</h3>

<pre><code>{
  "id": "write_gain_label",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "widget_member": {
    "part": "label",
    "member": "text"
  },
  "layout": {
    "x": 520,
    "y": 80
  }
}</code></pre>

<h3>12.3 Method invoke</h3>

<pre><code>{
  "id": "focus_name_ctrl",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "widget_method": {
    "name": "focus"
  },
  "layout": {
    "x": 420,
    "y": 160
  }
}</code></pre>

<h3>12.4 Reference connection example</h3>

<pre><code>"nodes": [
  {
    "id": "ctrl_gain_ref",
    "kind": "widget_reference",
    "widget": "ctrl_gain"
  },
  {
    "id": "read_gain_visible",
    "kind": "primitive",
    "type": "frog.ui.property_read",
    "widget_member": {
      "member": "visible"
    }
  }
],
"edges": [
  {
    "id": "e1",
    "from": { "node": "ctrl_gain_ref", "port": "ref" },
    "to": { "node": "read_gain_visible", "port": "ref" }
  }
]</code></pre>

<hr/>

<h2 id="validation-rules">13. Validation Rules</h2>

<p>
Implementations MUST enforce the following rules:
</p>

<ul>
  <li>every widget interaction primitive <strong>MUST</strong> receive a valid widget reference on its <code>ref</code> input, unless a stricter profile explicitly defines an alternative mechanism,</li>
  <li>the referenced widget <strong>MUST</strong> exist in the <code>front_panel</code>,</li>
  <li>the referenced part <strong>MUST</strong> exist if a <code>part</code> field is present,</li>
  <li>the addressed member <strong>MUST</strong> exist for the widget class or part class,</li>
  <li><code>frog.ui.property_read</code> <strong>MUST</strong> target a readable property,</li>
  <li><code>frog.ui.property_write</code> <strong>MUST</strong> target a writable property,</li>
  <li><code>frog.ui.method_invoke</code> <strong>MUST</strong> target a method,</li>
  <li>port types <strong>MUST</strong> match the addressed member signature,</li>
  <li>incoming and outgoing edges <strong>MUST</strong> remain type-compatible according to <code>Type.md</code>.</li>
</ul>

<p>
Additionally:
</p>

<ul>
  <li>a write to a read-only property <strong>MUST</strong> fail validation,</li>
  <li>a read from a write-only property <strong>MUST</strong> fail validation,</li>
  <li>invoking an unknown method <strong>MUST</strong> fail validation.</li>
</ul>

<p>
For <code>member = "value"</code>:
</p>

<ul>
  <li><code>frog.ui.property_read</code> and <code>frog.ui.property_write</code> remain valid when the widget class exposes <code>value</code> as a property,</li>
  <li>tools MAY warn when ordinary primary value wiring is modeled through object-style primitives instead of <code>widget_value</code>.</li>
</ul>

<hr/>

<h2 id="execution-semantics">14. Execution Semantics</h2>

<p>
Widget interaction nodes participate in the diagram as ordinary execution nodes.
</p>

<p>
Conceptually:
</p>

<ul>
  <li>a property read node consumes a widget reference and produces a property value from widget state,</li>
  <li>a property write node consumes a widget reference and a value, then updates widget state,</li>
  <li>a method invoke node consumes a widget reference and performs a widget action.</li>
</ul>

<p>
These interactions do not redefine the public interface and do not introduce a separate graph model.
They are integrated into the diagram through ordinary node execution and port connectivity.
</p>

<p>
When the addressed member is <code>value</code>,
the interaction remains valid as an object-style operation.
However, the natural terminal model remains the preferred representation for ordinary widget value dataflow.
</p>

<p>
Implementations MAY restrict certain widget interactions in headless runtimes or non-interactive profiles.
Such restrictions belong to the active runtime profile and do not alter the canonical source meaning of the node.
</p>

<p>
Detailed sequencing guarantees between independent widget side effects are outside the strict scope of v0.1.
If deterministic ordering between multiple widget mutations is required,
the active profile SHOULD define an explicit sequencing strategy.
</p>

<hr/>

<h2 id="examples">15. Examples</h2>

<h3>15.1 Read a control value explicitly through the object model</h3>

<pre><code>{
  "id": "read_gain_value",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "widget_member": {
    "member": "value"
  }
}</code></pre>

<p>
Conceptual output:
</p>

<pre><code>read_gain_value.value : f64</code></pre>

<h3>15.2 Write an indicator value explicitly through the object model</h3>

<pre><code>{
  "id": "write_result_value",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "widget_member": {
    "member": "value"
  }
}</code></pre>

<p>
Conceptual input:
</p>

<pre><code>write_result_value.value : f64</code></pre>

<h3>15.3 Read a label text</h3>

<pre><code>{
  "id": "read_gain_label_text",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "widget_member": {
    "part": "label",
    "member": "text"
  }
}</code></pre>

<p>
Conceptual output:
</p>

<pre><code>read_gain_label_text.value : string</code></pre>

<h3>15.4 Write a label text</h3>

<pre><code>{
  "id": "write_gain_label_text",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "widget_member": {
    "part": "label",
    "member": "text"
  }
}</code></pre>

<p>
Conceptual input:
</p>

<pre><code>write_gain_label_text.value : string</code></pre>

<h3>15.5 Invoke a focus method</h3>

<pre><code>{
  "id": "focus_name_ctrl",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "widget_method": {
    "name": "focus"
  }
}</code></pre>

<p>
Conceptual behavior:
</p>

<ul>
  <li>the node consumes a widget reference,</li>
  <li>no additional data input is required,</li>
  <li>no data output is required,</li>
  <li>the widget method is invoked when the node executes.</li>
</ul>

<h3>15.6 Example graph fragment using widget reference</h3>

<pre><code>"nodes": [
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
    "id": "mul_1",
    "kind": "primitive",
    "type": "Multiply"
  },
  {
    "id": "ind_result_ref",
    "kind": "widget_reference",
    "widget": "ind_result"
  },
  {
    "id": "write_result_value",
    "kind": "primitive",
    "type": "frog.ui.property_write",
    "widget_member": {
      "member": "value"
    }
  }
],
"edges": [
  {
    "id": "e_ref_1",
    "from": { "node": "ctrl_gain_ref", "port": "ref" },
    "to": { "node": "read_gain_value", "port": "ref" }
  },
  {
    "id": "e1",
    "from": { "node": "read_gain_value", "port": "value" },
    "to": { "node": "mul_1", "port": "x" }
  },
  {
    "id": "e_ref_2",
    "from": { "node": "ind_result_ref", "port": "ref" },
    "to": { "node": "write_result_value", "port": "ref" }
  },
  {
    "id": "e2",
    "from": { "node": "mul_1", "port": "result" },
    "to": { "node": "write_result_value", "port": "value" }
  }
]</code></pre>

<h3>15.7 Preferred natural value representation for ordinary dataflow</h3>

<p>
For ordinary primary value wiring, the following representation is generally preferred:
</p>

<pre><code>"nodes": [
  {
    "id": "ctrl_gain_value",
    "kind": "widget_value",
    "widget": "ctrl_gain"
  },
  {
    "id": "mul_1",
    "kind": "primitive",
    "type": "Multiply"
  },
  {
    "id": "ind_result_value",
    "kind": "widget_value",
    "widget": "ind_result"
  }
],
"edges": [
  {
    "id": "e1",
    "from": { "node": "ctrl_gain_value", "port": "value" },
    "to": { "node": "mul_1", "port": "x" }
  },
  {
    "id": "e2",
    "from": { "node": "mul_1", "port": "result" },
    "to": { "node": "ind_result_value", "port": "value" }
  }
]</code></pre>

<hr/>

<h2 id="out-of-scope">16. Out of Scope for v0.1</h2>

<p>
The following are outside the scope of this specification version:
</p>

<ul>
  <li>widget event registration nodes,</li>
  <li>event structure semantics,</li>
  <li>asynchronous UI callback delivery,</li>
  <li>general-purpose widget references as a standard FROG value type,</li>
  <li>dynamic reflective member enumeration APIs,</li>
  <li>threading guarantees for UI mutation in every runtime profile,</li>
  <li>fully standardized sequencing rules for independent UI side effects.</li>
</ul>

<hr/>

<h2 id="summary">17. Summary</h2>

<p>
This specification defines how diagrams interact with front panel widgets
in a structured and type-aware object model.
</p>

<p>
FROG v0.1 standardizes:
</p>

<ul>
  <li>widget member addressing,</li>
  <li>property read nodes,</li>
  <li>property write nodes,</li>
  <li>method invoke nodes,</li>
  <li>their relationship to widget references.</li>
</ul>

<p>
The primary widget value remains special:
</p>

<ul>
  <li>it is naturally represented in dataflow by <code>widget_value</code>,</li>
  <li>it may also be accessed explicitly as a property through widget interaction primitives.</li>
</ul>

<p>
These interactions are serialized as standardized primitive nodes
and validated against the widget object model and the FROG type system.
</p>

<p>
This provides a clean bridge between the executable diagram and the structured front panel
without conflating UI objects, public interface ports, and ordinary data values.
</p>

<hr/>

<p align="center">
End of FROG Widget Interaction Specification
</p>
