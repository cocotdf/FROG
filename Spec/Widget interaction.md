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
FROG widgets are structured UI objects defined by <code>Widget.md</code> and instantiated inside the <code>front_panel</code> section defined by <code>Front panel.md</code>.
</p>

<p>
This document defines how the executable diagram may interact with those widget instances.
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
These interactions allow the diagram to manipulate front panel objects in a structured and type-aware way without confusing widget objects with ordinary dataflow values.
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
  <li>their type and validation rules.</li>
</ul>

<p>
FROG v0.1 does <strong>not</strong> fully standardize:
</p>

<ul>
  <li>an event loop model,</li>
  <li>widget event registration nodes,</li>
  <li>asynchronous UI message delivery,</li>
  <li>runtime widget reference values as first-class general-purpose data types.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">4. Relation with Other Specifications</h2>

<p>
This document depends on the following FROG specifications:
</p>

<ul>
  <li><strong>Type.md</strong> — defines property and method port types,</li>
  <li><strong>Widget.md</strong> — defines widget classes, roles, parts, properties, methods, and allowed members,</li>
  <li><strong>Front panel.md</strong> — defines how widget instances are serialized in the <code>front_panel</code> section,</li>
  <li><strong>Diagram.md</strong> — defines the executable graph model in which interaction nodes appear.</li>
</ul>

<p>
This document does not redefine widget classes themselves.
It only defines how diagram nodes reference and interact with them.
</p>

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

<h3>6.1 Address structure</h3>

<p>
Recommended canonical addressing form:
</p>

<pre>{
  "widget": "ctrl_gain",
  "part": "label",
  "member": "text"
}</pre>

<p>
Fields:
</p>

<ul>
  <li><code>widget</code> — required widget instance identifier,</li>
  <li><code>part</code> — optional named widget part,</li>
  <li><code>member</code> — required property or method name.</li>
</ul>

<h3>6.2 Widget-level member addressing</h3>

<p>
If <code>part</code> is omitted, the member belongs to the widget itself.
</p>

<p>
Examples:
</p>

<pre>
{ "widget": "ctrl_gain", "member": "value" }
{ "widget": "ctrl_gain", "member": "visible" }
{ "widget": "ctrl_gain", "member": "focus" }
</pre>

<h3>6.3 Part-level member addressing</h3>

<p>
If <code>part</code> is present, the member belongs to the named widget part.
</p>

<p>
Examples:
</p>

<pre>
{ "widget": "ctrl_gain", "part": "label", "member": "text" }
{ "widget": "ctrl_gain", "part": "label", "member": "visible" }
</pre>

<h3>6.4 Address validity</h3>

<p>
An address is valid only if:
</p>

<ul>
  <li>the widget exists in the <code>front_panel</code>,</li>
  <li>the part exists if specified,</li>
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
The node MUST also declare a widget member target.
</p>

<hr/>

<h2 id="property-read-node">8. Property Read Node</h2>

<p>
A property read node reads a property value from a widget or widget part and exposes it to the diagram as an output.
</p>

<h3>8.1 Purpose</h3>

<p>
Typical uses:
</p>

<ul>
  <li>read a widget value,</li>
  <li>read widget visibility state,</li>
  <li>read label text,</li>
  <li>read other readable widget configuration values.</li>
</ul>

<h3>8.2 Standard primitive identifier</h3>

<pre>frog.ui.property_read</pre>

<h3>8.3 Required node fields</h3>

<pre>{
  "id": "read_gain_value",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "target": {
    "widget": "ctrl_gain",
    "member": "value"
  }
}</pre>

<h3>8.4 Standard port signature</h3>

<p>
A property read node exposes:
</p>

<ul>
  <li>no required data input for the read itself,</li>
  <li>one output port named <code>value</code>.</li>
</ul>

<p>
The output type is the type of the addressed property.
</p>

<h3>8.5 Example</h3>

<p>
Reading the numeric value of a widget:
</p>

<pre>{
  "id": "read_gain_value",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "target": {
    "widget": "ctrl_gain",
    "member": "value"
  }
}</pre>

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
  <li>update the displayed value of an indicator,</li>
  <li>change widget visibility,</li>
  <li>change label text,</li>
  <li>set a visual or state property from program logic.</li>
</ul>

<h3>9.2 Standard primitive identifier</h3>

<pre>frog.ui.property_write</pre>

<h3>9.3 Required node fields</h3>

<pre>{
  "id": "write_result_value",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "target": {
    "widget": "ind_result",
    "member": "value"
  }
}</pre>

<h3>9.4 Standard port signature</h3>

<p>
A property write node exposes:
</p>

<ul>
  <li>one input port named <code>value</code>,</li>
  <li>no required data output.</li>
</ul>

<p>
The input type is the type of the addressed property.
</p>

<h3>9.5 Example</h3>

<p>
Writing the displayed value of an indicator:
</p>

<pre>{
  "id": "write_result_value",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "target": {
    "widget": "ind_result",
    "member": "value"
  }
}</pre>

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

<pre>frog.ui.method_invoke</pre>

<h3>10.3 Required node fields</h3>

<pre>{
  "id": "focus_name_ctrl",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "target": {
    "widget": "ctrl_name",
    "member": "focus"
  }
}</pre>

<h3>10.4 Standard port signature</h3>

<p>
A method invoke node exposes a method-specific port signature.
</p>

<p>
In general:
</p>

<ul>
  <li>each method input parameter becomes an input port,</li>
  <li>each method return value becomes an output port,</li>
  <li>if the method has no parameters or return values, the node may have no data ports.</li>
</ul>

<p>
The exact parameter and return structure of a method is defined by the widget class or part class under the active profile.
</p>

<h3>10.5 Example</h3>

<p>
Invoking a focus method with no parameters and no data outputs:
</p>

<pre>{
  "id": "focus_name_ctrl",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "target": {
    "widget": "ctrl_name",
    "member": "focus"
  }
}</pre>

<hr/>

<h2 id="typing-rules">11. Typing Rules</h2>

<p>
Widget interaction nodes are typed through the addressed member definition.
</p>

<h3>11.1 Property read typing</h3>

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
  <li>reading <code>ctrl_gain.value</code> may produce <code>f64</code>,</li>
  <li>reading <code>ctrl_gain.visible</code> produces <code>bool</code>,</li>
  <li>reading <code>ctrl_gain.label.text</code> produces <code>string</code>.</li>
</ul>

<h3>11.2 Property write typing</h3>

<p>
For <code>frog.ui.property_write</code>:
</p>

<ul>
  <li>the input port <code>value</code> MUST have the type of the addressed property.</li>
</ul>

<p>
Incoming edges MUST be compatible with that property type according to <code>Type.md</code>.
</p>

<h3>11.3 Method typing</h3>

<p>
For <code>frog.ui.method_invoke</code>:
</p>

<ul>
  <li>input port types are the parameter types of the addressed method,</li>
  <li>output port types are the return types of the addressed method.</li>
</ul>

<h3>11.4 Compatibility</h3>

<p>
Standard FROG type compatibility and implicit coercion rules apply to widget interaction ports in the same way they apply to other diagram ports.
</p>

<hr/>

<h2 id="diagram-representation">12. Diagram Representation</h2>

<p>
Widget interaction nodes are serialized as primitive nodes in the diagram.
</p>

<p>
Recommended general forms:
</p>

<h3>12.1 Property read</h3>

<pre>{
  "id": "read_gain_value",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "target": {
    "widget": "ctrl_gain",
    "member": "value"
  },
  "layout": {
    "x": 320,
    "y": 80
  }
}</pre>

<h3>12.2 Property write</h3>

<pre>{
  "id": "write_result_value",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "target": {
    "widget": "ind_result",
    "member": "value"
  },
  "layout": {
    "x": 520,
    "y": 80
  }
}</pre>

<h3>12.3 Method invoke</h3>

<pre>{
  "id": "focus_name_ctrl",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "target": {
    "widget": "ctrl_name",
    "member": "focus"
  },
  "layout": {
    "x": 420,
    "y": 160
  }
}</pre>

<h3>12.4 Part member target</h3>

<pre>{
  "id": "write_gain_label",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "target": {
    "widget": "ctrl_gain",
    "part": "label",
    "member": "text"
  }
}</pre>

<hr/>

<h2 id="validation-rules">13. Validation Rules</h2>

<p>
Implementations MUST enforce the following rules:
</p>

<ul>
  <li>the referenced widget MUST exist in the <code>front_panel</code>,</li>
  <li>the referenced part MUST exist if a <code>part</code> field is present,</li>
  <li>the addressed member MUST exist for the widget class or part class,</li>
  <li><code>frog.ui.property_read</code> MUST target a readable property,</li>
  <li><code>frog.ui.property_write</code> MUST target a writable property,</li>
  <li><code>frog.ui.method_invoke</code> MUST target a method,</li>
  <li>port types MUST match the addressed member signature,</li>
  <li>incoming and outgoing edges MUST remain type-compatible according to <code>Type.md</code>.</li>
</ul>

<p>
Additionally:
</p>

<ul>
  <li>a write to a read-only property MUST fail validation,</li>
  <li>a read from a write-only property MUST fail validation,</li>
  <li>invoking an unknown method MUST fail validation.</li>
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
  <li>a property read node produces a value from widget state,</li>
  <li>a property write node consumes a value and updates widget state,</li>
  <li>a method invoke node performs a widget action.</li>
</ul>

<p>
These interactions do not redefine the public interface and do not introduce new dataflow rules.
They are integrated into the diagram through ordinary node execution and port connectivity.
</p>

<p>
Implementations MAY restrict certain widget interactions in headless runtimes or non-interactive profiles.
Such restrictions belong to the active runtime profile and do not alter the canonical source meaning of the node.
</p>

<hr/>

<h2 id="examples">15. Examples</h2>

<h3>15.1 Read a control value</h3>

<pre>{
  "id": "read_gain_value",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "target": {
    "widget": "ctrl_gain",
    "member": "value"
  }
}</pre>

<p>
Conceptual output:
</p>

<pre>read_gain_value.value : f64</pre>

<h3>15.2 Write an indicator value</h3>

<pre>{
  "id": "write_result_value",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "target": {
    "widget": "ind_result",
    "member": "value"
  }
}</pre>

<p>
Conceptual input:
</p>

<pre>write_result_value.value : f64</pre>

<h3>15.3 Read a label text</h3>

<pre>{
  "id": "read_gain_label_text",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "target": {
    "widget": "ctrl_gain",
    "part": "label",
    "member": "text"
  }
}</pre>

<p>
Conceptual output:
</p>

<pre>read_gain_label_text.value : string</pre>

<h3>15.4 Write a label text</h3>

<pre>{
  "id": "write_gain_label_text",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "target": {
    "widget": "ctrl_gain",
    "part": "label",
    "member": "text"
  }
}</pre>

<p>
Conceptual input:
</p>

<pre>write_gain_label_text.value : string</pre>

<h3>15.5 Invoke a focus method</h3>

<pre>{
  "id": "focus_name_ctrl",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "target": {
    "widget": "ctrl_name",
    "member": "focus"
  }
}</pre>

<p>
Conceptual behavior:
</p>

<ul>
  <li>no data input required,</li>
  <li>no data output required,</li>
  <li>the widget method is invoked when the node executes.</li>
</ul>

<h3>15.6 Example graph fragment</h3>

<pre>"nodes": [
  {
    "id": "read_gain_value",
    "kind": "primitive",
    "type": "frog.ui.property_read",
    "target": {
      "widget": "ctrl_gain",
      "member": "value"
    }
  },
  {
    "id": "mul_1",
    "kind": "primitive",
    "type": "Multiply"
  },
  {
    "id": "write_result_value",
    "kind": "primitive",
    "type": "frog.ui.property_write",
    "target": {
      "widget": "ind_result",
      "member": "value"
    }
  }
],
"edges": [
  {
    "id": "e1",
    "from": { "node": "read_gain_value", "port": "value" },
    "to": { "node": "mul_1", "port": "x" }
  },
  {
    "id": "e2",
    "from": { "node": "mul_1", "port": "result" },
    "to": { "node": "write_result_value", "port": "value" }
  }
]</pre>

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
  <li>threading guarantees for UI mutation in every runtime profile.</li>
</ul>

<hr/>

<h2 id="summary">17. Summary</h2>

<p>
This specification defines how diagrams interact with front panel widgets in a structured and type-aware way.
</p>

<p>
FROG v0.1 standardizes:
</p>

<ul>
  <li>widget member addressing,</li>
  <li>property read nodes,</li>
  <li>property write nodes,</li>
  <li>method invoke nodes.</li>
</ul>

<p>
These interactions are serialized as standardized primitive nodes and validated against the widget object model and the FROG type system.
</p>

<p>
This provides a clean bridge between the executable diagram and the structured front panel without conflating UI objects, public interface ports, and ordinary data values.
</p>

<hr/>

<p align="center">
End of FROG Widget Interaction Specification
</p>
