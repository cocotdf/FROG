<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">🐸 FROG Widget Interaction Specification</h1>

<p align="center">
  Definition of the canonical source-facing representation of object-style diagram interaction with front-panel widgets in <strong>.frog</strong> programs<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2 id="contents">Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope">2. Scope</a></li>
  <li><a href="#goals">3. Goals</a></li>
  <li><a href="#scope-for-v01">4. Scope for v0.1</a></li>
  <li><a href="#relation-with-other-specifications">5. Relation with Other Specifications</a></li>
  <li><a href="#conceptual-model">6. Conceptual Model</a></li>
  <li><a href="#widget-member-addressing">7. Widget Member Addressing</a></li>
  <li><a href="#interaction-node-families">8. Interaction Node Families</a></li>
  <li><a href="#property-read-representation">9. Property Read Representation</a></li>
  <li><a href="#property-write-representation">10. Property Write Representation</a></li>
  <li><a href="#method-invoke-representation">11. Method Invoke Representation</a></li>
  <li><a href="#typing-and-sequencing-references">12. Typing and Sequencing References</a></li>
  <li><a href="#diagram-representation">13. Diagram Representation</a></li>
  <li><a href="#validation-rules">14. Validation Rules</a></li>
  <li><a href="#source-to-library-mapping">15. Source-to-Library Mapping</a></li>
  <li><a href="#examples">16. Examples</a></li>
  <li><a href="#out-of-scope-for-v01">17. Out of Scope for v0.1</a></li>
  <li><a href="#summary">18. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
FROG widgets are structured UI objects declared in the <code>front_panel</code> section and defined by
<code>Widget.md</code> and <code>Front panel.md</code>.
This document specifies how the executable <code>diagram</code> represents interaction with those widget instances through
explicit object-style interaction nodes.
</p>

<p>
FROG distinguishes two different diagram-side paths for widget participation:
</p>

<ul>
  <li><strong>Natural value path</strong> — through <code>widget_value</code>, which materializes the primary widget value in ordinary dataflow.</li>
  <li><strong>Object-style path</strong> — through <code>widget_reference</code> together with explicit widget interaction primitives.</li>
</ul>

<p>
These two paths serve different purposes and MUST remain semantically distinct.
The natural value path is the canonical representation for ordinary widget primary-value flow.
The object-style path is the canonical representation for property reads, property writes, and method invocation.
</p>

<p>
In v0.1, FROG uses three standardized widget interaction primitive families:
</p>

<ul>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
</ul>

<p>
The primary widget value has a dual status:
it is the natural value terminal of a value-carrying widget,
and it MAY also be exposed as an ordinary object property when the widget class allows it.
Accordingly, a widget value MAY be accessed naturally through <code>widget_value</code>,
and MAY also be accessed through the object-style path as member <code>value</code>.
</p>

<hr/>

<h2 id="scope">2. Scope</h2>

<p>
This document specifies:
</p>

<ul>
  <li>the canonical source-facing representation of object-style widget interaction in the diagram,</li>
  <li>the member-addressing model for widget and widget-part properties and methods,</li>
  <li>the required node-local descriptor fields used by widget interaction primitives,</li>
  <li>the graph-shape constraints that tie widget interaction to <code>widget_reference</code>,</li>
  <li>the source-level validation rules for those interaction forms.</li>
</ul>

<p>
This document does not specify:
</p>

<ul>
  <li>the widget object model itself,</li>
  <li>the canonical declaration and composition of the front panel,</li>
  <li>the primitive identities and full primitive signatures beyond their source-facing use here,</li>
  <li>the primitive-local execution semantics of UI interaction operations,</li>
  <li>the general executable semantics of the diagram.</li>
</ul>

<hr/>

<h2 id="goals">3. Goals</h2>

<p>
The widget interaction model is designed to satisfy the following goals:
</p>

<ul>
  <li><strong>Object consistency</strong> — widget interaction MUST follow the widget object model rather than introduce ad hoc UI-specific exceptions.</li>
  <li><strong>Dataflow clarity</strong> — ordinary value flow and explicit object access MUST remain distinct.</li>
  <li><strong>Source explicitness</strong> — object-style interaction MUST be represented through explicit source constructs rather than hidden editor conventions.</li>
  <li><strong>Type safety</strong> — widget member types and method signatures MUST remain compatible with the FROG type system.</li>
  <li><strong>Profile extensibility</strong> — widget classes MAY expose different properties, methods, and parts under different profiles while preserving one common interaction model.</li>
  <li><strong>Architectural separation</strong> — widget interaction MUST NOT redefine public interface semantics, front-panel composition semantics, general execution semantics, or the ownership of the standardized <code>frog.ui.*</code> primitive surface.</li>
</ul>

<hr/>

<h2 id="scope-for-v01">4. Scope for v0.1</h2>

<p>
FROG v0.1 standardizes:
</p>

<ul>
  <li>the conceptual addressing model for widget members,</li>
  <li>the source-facing representation of property reads,</li>
  <li>the source-facing representation of property writes,</li>
  <li>the source-facing representation of method invocation,</li>
  <li>their integration with <code>widget_reference</code>,</li>
  <li>their canonical descriptor fields,</li>
  <li>their diagram-level representation constraints,</li>
  <li>their source-level validation rules.</li>
</ul>

<p>
FROG v0.1 does not fully standardize in this document:
</p>

<ul>
  <li>the executable primitive catalog itself beyond its source-facing use,</li>
  <li>the detailed primitive port signatures of <code>frog.ui.*</code>,</li>
  <li>the primitive execution semantics of property read, property write, and method invocation,</li>
  <li>a complete event structure model,</li>
  <li>widget event registration nodes,</li>
  <li>asynchronous UI message delivery,</li>
  <li>widget references as general-purpose first-class value types,</li>
  <li>a complete effect system covering every UI runtime profile.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">5. Relation with Other Specifications</h2>

<p>
This document depends on the following specifications:
</p>

<ul>
  <li><code>Expression/Type.md</code> — ordinary value types, compatibility rules, and implicit coercion rules.</li>
  <li><code>Expression/Widget.md</code> — widget classes, widget roles, widget parts, properties, methods, and member availability.</li>
  <li><code>Expression/Front panel.md</code> — declaration and serialization of widget instances.</li>
  <li><code>Expression/Diagram.md</code> — executable graph structure, node categories, canonical widget node kinds, and port-resolution rules.</li>
  <li><code>Libraries/UI.md</code> — the standardized <code>frog.ui.*</code> primitive catalog, primitive signatures, primitive typing rules, sequencing rules, and primitive-local interaction semantics.</li>
</ul>

<p>
This document complements, but does not redefine, the following canonical diagram node kinds:
</p>

<ul>
  <li><code>widget_value</code> — natural primary-value participation.</li>
  <li><code>widget_reference</code> — object-style widget access anchor.</li>
</ul>

<p>
This document also does not redefine public interface semantics.
A front-panel widget does not create a public interface port by itself.
Public interface behavior remains represented canonically through
<code>interface_input</code> and <code>interface_output</code> in the diagram.
</p>

<p>
Ownership is intentionally split as follows:
</p>

<pre>Ownership split

Widget interaction.md
  -> source-facing interaction model
  -> member descriptor model
  -> graph-shape constraints
  -> source-level validation rules for widget interaction forms

Widget.md
  -> widget object model
  -> widget classes, parts, properties, methods, and member availability

Diagram.md
  -> executable graph structure
  -> widget_value / widget_reference node kinds
  -> primitive-node port resolution

Libraries/UI.md
  -> frog.ui.* primitive identities
  -> primitive signatures
  -> primitive-local typing and sequencing rules
  -> primitive-local interaction semantics</pre>

<hr/>

<h2 id="conceptual-model">6. Conceptual Model</h2>

<p>
A widget interaction node addresses a member of a widget object.
A widget member is one of:
</p>

<ul>
  <li>a widget property,</li>
  <li>a widget-part property,</li>
  <li>a widget method,</li>
  <li>a widget-part method.</li>
</ul>

<p>
Examples of conceptual member access:
</p>

<pre>ctrl_gain.value
ctrl_gain.visible
ctrl_gain.label.text
ctrl_gain.focus()
graph_1.x_scale.visible</pre>

<p>
The object-style interaction path is always represented conceptually as:
</p>

<pre>widget_reference -> frog.ui.property_read
widget_reference -> frog.ui.property_write
widget_reference -> frog.ui.method_invoke</pre>

<p>
A widget interaction node does not define the widget instance.
It operates on an already-declared widget instance from the <code>front_panel</code>.
</p>

<p>
When explicit ordering of UI side effects is required,
widget interaction nodes MAY participate in a sequencing chain through <code>ui_in</code> and <code>ui_out</code>.
The primitive-level meaning of those sequencing ports is defined by <code>Libraries/UI.md</code>.
</p>

<hr/>

<h2 id="widget-member-addressing">7. Widget Member Addressing</h2>

<p>
Widget member addressing identifies:
</p>

<ul>
  <li>the target widget instance,</li>
  <li>optionally a named widget part,</li>
  <li>the addressed property or method.</li>
</ul>

<h3 id="full-conceptual-address">7.1 Full Conceptual Address</h3>

<p>
A full conceptual address may be understood as:
</p>

<pre>{
  "widget": "ctrl_gain",
  "part": "label",
  "member": "text"
}</pre>

<p>
For methods:
</p>

<pre>{
  "widget": "ctrl_gain",
  "part": "label",
  "name": "show"
}</pre>

<h3 id="primitive-local-member-descriptor">7.2 Primitive-Local Member Descriptor</h3>

<p>
In the canonical v0.1 diagram model, widget identity is carried by the incoming <code>ref</code> port,
not embedded directly in the primitive node.
Accordingly:
</p>

<ul>
  <li>property interaction nodes MUST declare a <code>widget_member</code> descriptor,</li>
  <li>method interaction nodes MUST declare a <code>widget_method</code> descriptor.</li>
</ul>

<p>
Canonical property member descriptors:
</p>

<pre>{ "member": "text" }
{ "part": "label", "member": "text" }</pre>

<p>
Canonical method descriptors:
</p>

<pre>{ "name": "focus" }
{ "part": "label", "name": "show" }</pre>

<h3 id="widget-level-member-addressing">7.3 Widget-Level Member Addressing</h3>

<p>
If <code>part</code> is omitted, the addressed member belongs to the widget itself.
</p>

<p>
Examples:
</p>

<pre>{ "member": "value" }
{ "member": "visible" }
{ "name": "focus" }</pre>

<h3 id="part-level-member-addressing">7.4 Part-Level Member Addressing</h3>

<p>
If <code>part</code> is present, the addressed member belongs to the named widget part.
</p>

<p>
Examples:
</p>

<pre>{ "part": "label", "member": "text" }
{ "part": "label", "member": "visible" }
{ "part": "label", "name": "show" }</pre>

<h3 id="address-validity">7.5 Address Validity</h3>

<p>
A widget member address is valid only if all of the following hold:
</p>

<ul>
  <li>the referenced widget exists in <code>front_panel</code>,</li>
  <li>the referenced part exists when <code>part</code> is specified,</li>
  <li>the addressed member exists for the widget class or widget-part class under the active profile,</li>
  <li>the addressed member is compatible with the interaction kind being used.</li>
</ul>

<p>
For example:
</p>

<ul>
  <li><code>frog.ui.property_read</code> MUST target a readable property,</li>
  <li><code>frog.ui.property_write</code> MUST target a writable property,</li>
  <li><code>frog.ui.method_invoke</code> MUST target a method.</li>
</ul>

<hr/>

<h2 id="interaction-node-families">8. Interaction Node Families</h2>

<p>
In v0.1, widget interactions are represented canonically as <code>primitive</code> nodes in the diagram.
</p>

<p>
The standardized primitive identifiers used by this source model are:
</p>

<ul>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
</ul>

<p>
Each widget interaction node MUST satisfy all of the following source-facing constraints:
</p>

<ul>
  <li><code>kind</code> MUST be <code>primitive</code>,</li>
  <li><code>type</code> MUST be one of the standardized primitive identifiers above,</li>
  <li>the node MUST consume a widget reference through required input port <code>ref</code>,</li>
  <li>property interaction nodes MUST declare <code>widget_member</code>,</li>
  <li>method interaction nodes MUST declare <code>widget_method</code>.</li>
</ul>

<p>
The full primitive signatures, including required and optional ports beyond the source-facing reference model,
are owned by <code>Libraries/UI.md</code> together with <code>Expression/Diagram.md</code>.
</p>

<hr/>

<h2 id="property-read-representation">9. Property Read Representation</h2>

<p>
A property read interaction represents a read of a property value from a widget or widget part into the diagram.
</p>

<h3 id="property-read-identifier">9.1 Standard Primitive Identifier</h3>

<pre>frog.ui.property_read</pre>

<h3 id="property-read-structure">9.2 Required Structural Fields</h3>

<pre>{
  "id": "read_gain_visible",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "widget_member": {
    "member": "visible"
  }
}</pre>

<h3 id="property-read-rules">9.3 Representation Rules</h3>

<ul>
  <li>the node MUST consume a compatible widget reference through <code>ref</code>,</li>
  <li>the node MUST declare <code>widget_member</code>,</li>
  <li>the addressed member MUST be a readable property under the active widget profile.</li>
</ul>

<h3 id="property-read-primary-value">9.4 Access to Primary Value as a Property</h3>

<p>
Reading <code>{ "member": "value" }</code> through <code>frog.ui.property_read</code> is valid when the widget class exposes
<code>value</code> as a readable property.
However, when the intent is ordinary value flow, tools SHOULD prefer the natural <code>widget_value</code> representation.
</p>

<p>
Primitive signature details, typing, sequencing-port behavior, and read semantics belong to <code>Libraries/UI.md</code>.
</p>

<hr/>

<h2 id="property-write-representation">10. Property Write Representation</h2>

<p>
A property write interaction represents a write of a diagram value into a writable widget or widget-part property.
</p>

<h3 id="property-write-identifier">10.1 Standard Primitive Identifier</h3>

<pre>frog.ui.property_write</pre>

<h3 id="property-write-structure">10.2 Required Structural Fields</h3>

<pre>{
  "id": "write_gain_label",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "widget_member": {
    "part": "label",
    "member": "text"
  }
}</pre>

<h3 id="property-write-rules">10.3 Representation Rules</h3>

<ul>
  <li>the node MUST consume a compatible widget reference through <code>ref</code>,</li>
  <li>the node MUST declare <code>widget_member</code>,</li>
  <li>the addressed member MUST be a writable property under the active widget profile.</li>
</ul>

<h3 id="property-write-primary-value">10.4 Access to Primary Value as a Property</h3>

<p>
Writing <code>{ "member": "value" }</code> through <code>frog.ui.property_write</code> is valid when the widget class exposes
<code>value</code> as a writable property.
This object-style write MUST remain semantically distinct from the natural primary value path represented by
<code>widget_value</code>.
For ordinary widget value participation in dataflow, tools SHOULD prefer <code>widget_value</code>.
</p>

<p>
Primitive signature details, typing, sequencing-port behavior, and write semantics belong to <code>Libraries/UI.md</code>.
</p>

<hr/>

<h2 id="method-invoke-representation">11. Method Invoke Representation</h2>

<p>
A method invoke interaction represents a method call on a widget or widget part.
</p>

<h3 id="method-invoke-identifier">11.1 Standard Primitive Identifier</h3>

<pre>frog.ui.method_invoke</pre>

<h3 id="method-invoke-structure">11.2 Required Structural Fields</h3>

<pre>{
  "id": "invoke_reset",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "widget_method": {
    "name": "reset_to_default"
  }
}</pre>

<h3 id="method-invoke-rules">11.3 Representation Rules</h3>

<ul>
  <li>the node MUST consume a compatible widget reference through <code>ref</code>,</li>
  <li>the node MUST declare <code>widget_method</code>,</li>
  <li>the addressed member MUST be a method under the active widget profile.</li>
</ul>

<p>
Primitive signature details, typing, sequencing-port behavior, argument ordering, result ordering, and invocation semantics
belong to <code>Libraries/UI.md</code>.
</p>

<hr/>

<h2 id="typing-and-sequencing-references">12. Typing and Sequencing References</h2>

<h3 id="widget-reference-typing">12.1 Widget Reference Typing</h3>

<p>
The <code>ref</code> port carries an opaque widget reference token.
In v0.1, this token is diagram-internal and interaction-specific.
It is not standardized in this document as a general-purpose first-class value type for arbitrary storage, transport, or computation.
</p>

<h3 id="property-and-method-typing">12.2 Property and Method Typing</h3>

<p>
Property interaction nodes MUST remain compatible with the declared property type of the addressed widget member.
Method interaction nodes MUST remain compatible with the declared method signature of the addressed widget member.
All compatibility checks and implicit coercions MUST follow the ordinary FROG type rules.
</p>

<h3 id="ui-sequencing-references">12.3 UI Sequencing References</h3>

<p>
The optional ports <code>ui_in</code> and <code>ui_out</code> define explicit ordering between UI interactions.
These sequencing ports are part of the standardized primitive surface owned by <code>Libraries/UI.md</code>.
</p>

<p>
When explicit UI ordering is represented in canonical source:
</p>

<ul>
  <li>it MUST be represented through the standardized sequencing ports,</li>
  <li>it MUST NOT be encoded through hidden editor conventions,</li>
  <li>it MUST NOT be interpreted as an ordinary data-value dependency.</li>
</ul>

<hr/>

<h2 id="diagram-representation">13. Diagram Representation</h2>

<p>
Widget interaction primitives appear as ordinary <code>primitive</code> nodes inside the diagram.
They are connected to a canonical <code>widget_reference</code> node that identifies the widget instance.
</p>

<p>
Example shape:
</p>

<pre>{
  "nodes": [
    {
      "id": "ctrl_gain_ref",
      "kind": "widget_reference",
      "widget": "ctrl_gain"
    },
    {
      "id": "read_label_text",
      "kind": "primitive",
      "type": "frog.ui.property_read",
      "widget_member": {
        "part": "label",
        "member": "text"
      }
    }
  ],
  "edges": [
    {
      "id": "e1",
      "from": { "node": "ctrl_gain_ref", "port": "ref" },
      "to":   { "node": "read_label_text", "port": "ref" }
    }
  ]
}</pre>

<p>
Canonical representation rules:
</p>

<ul>
  <li>a widget interaction node MUST be connected to a compatible <code>widget_reference</code>,</li>
  <li>a widget interaction node MUST NOT identify the target widget only through ad hoc local string fields,</li>
  <li>the widget member or method being addressed MUST be declared through <code>widget_member</code> or <code>widget_method</code>,</li>
  <li>ordinary value ports MUST be represented through ordinary diagram edges,</li>
  <li>explicit UI ordering, when used, MUST be represented through the standardized sequencing ports.</li>
</ul>

<p>
Canonical interaction shape:
</p>

<pre>front_panel widget instance
          |
          v
  widget_reference node
          |
          v
frog.ui.property_read / property_write / method_invoke
          |
          +-- ordinary value ports
          +-- optional ui_in / ui_out sequencing ports</pre>

<p>
The exact port set and port typing of the interaction primitives are resolved by <code>Libraries/UI.md</code>
together with the primitive-port resolution rules of <code>Expression/Diagram.md</code>.
</p>

<hr/>

<h2 id="validation-rules">14. Validation Rules</h2>

<p>
A validator MUST reject a widget interaction when any of the following conditions fails:
</p>

<ul>
  <li>the referenced widget exists in the <code>front_panel</code>,</li>
  <li>the widget class is known under the active profile,</li>
  <li>the interaction node type is one of the standardized widget interaction primitives,</li>
  <li>the node includes the correct descriptor field:
    <ul>
      <li><code>widget_member</code> for property nodes,</li>
      <li><code>widget_method</code> for method nodes,</li>
    </ul>
  </li>
  <li>the addressed part exists when specified,</li>
  <li>the addressed member exists,</li>
  <li>the addressed member kind matches the interaction kind,</li>
  <li>all connected value ports are type-compatible,</li>
  <li>all required method arguments are present according to the standardized primitive signature,</li>
  <li>the <code>ref</code> port is connected to a compatible <code>widget_reference</code> node,</li>
  <li><code>widget_value</code> is not used as a substitute for object-style member access,</li>
  <li>object-style interaction is not used to redefine public interface semantics.</li>
</ul>

<p>
A validator SHOULD diagnose at least the following error classes:
</p>

<ul>
  <li>unknown widget,</li>
  <li>unknown widget part,</li>
  <li>unknown member,</li>
  <li>property versus method mismatch,</li>
  <li>read of non-readable property,</li>
  <li>write of non-writable property,</li>
  <li>method argument mismatch,</li>
  <li>type incompatibility,</li>
  <li>missing <code>ref</code> connection,</li>
  <li>invalid use of a non-value-carrying widget as though it exposed <code>value</code>.</li>
</ul>

<hr/>

<h2 id="source-to-library-mapping">15. Source-to-Library Mapping</h2>

<p>
Canonical source representation and primitive-library ownership are intentionally separated in FROG.
This section defines how the source form declared here maps to the standardized <code>frog.ui</code> library layer.
</p>

<h3 id="property-read-mapping">15.1 Property Read Mapping</h3>

<ul>
  <li>a node with <code>kind: "primitive"</code> and <code>type: "frog.ui.property_read"</code> maps to the standardized property-read primitive family,</li>
  <li><code>widget_member</code> identifies the addressed property in source form,</li>
  <li>the incoming <code>ref</code> edge identifies the target widget instance in source form.</li>
</ul>

<h3 id="property-write-mapping">15.2 Property Write Mapping</h3>

<ul>
  <li>a node with <code>type: "frog.ui.property_write"</code> maps to the standardized property-write primitive family,</li>
  <li><code>widget_member</code> identifies the addressed property in source form,</li>
  <li>the incoming <code>ref</code> edge identifies the target widget instance in source form.</li>
</ul>

<h3 id="method-invoke-mapping">15.3 Method Invoke Mapping</h3>

<ul>
  <li>a node with <code>type: "frog.ui.method_invoke"</code> maps to the standardized method-invoke primitive family,</li>
  <li><code>widget_method</code> identifies the addressed method in source form,</li>
  <li>the incoming <code>ref</code> edge identifies the target widget instance in source form.</li>
</ul>

<h3 id="natural-vs-object-style-value-mapping">15.4 Natural versus Object-Style Value Mapping</h3>

<ul>
  <li><code>widget_value</code> remains the canonical source representation of ordinary primary-value participation in dataflow.</li>
  <li>Object-style access to member <code>value</code> through <code>frog.ui.property_read</code> or <code>frog.ui.property_write</code> remains a distinct canonical source form.</li>
</ul>

<h3 id="no-primitive-semantic-redefinition">15.5 No Primitive-Semantic Redefinition in This Document</h3>

<p>
This document MUST NOT be interpreted as redefining:
</p>

<ul>
  <li>the primitive signatures of <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, or <code>frog.ui.method_invoke</code>,</li>
  <li>the primitive-level behavior of UI sequencing ports,</li>
  <li>the execution semantics of property reads, property writes, or method invocations,</li>
  <li>the widget object model itself,</li>
  <li>the general primitive port-resolution rules of the diagram.</li>
</ul>

<p>
Those topics are owned by <code>Libraries/UI.md</code>, <code>Expression/Widget.md</code>, and <code>Expression/Diagram.md</code>.
</p>

<hr/>

<h2 id="examples">16. Examples</h2>

<h3 id="example-read-label-text">16.1 Read a Label Text Property</h3>

<pre>{
  "front_panel": {
    "widgets": [
      {
        "id": "ctrl_gain",
        "role": "control",
        "widget": "frog.ui.standard.numeric_control",
        "value_type": "f64"
      }
    ]
  },
  "diagram": {
    "nodes": [
      {
        "id": "ctrl_gain_ref",
        "kind": "widget_reference",
        "widget": "ctrl_gain"
      },
      {
        "id": "read_label_text",
        "kind": "primitive",
        "type": "frog.ui.property_read",
        "widget_member": {
          "part": "label",
          "member": "text"
        }
      }
    ],
    "edges": [
      {
        "id": "e1",
        "from": { "node": "ctrl_gain_ref", "port": "ref" },
        "to":   { "node": "read_label_text", "port": "ref" }
      }
    ]
  }
}</pre>

<h3 id="example-write-part-property">16.2 Write a Widget-Part Property</h3>

<pre>{
  "diagram": {
    "nodes": [
      {
        "id": "status_text",
        "kind": "interface_input",
        "interface_port": "status"
      },
      {
        "id": "ctrl_gain_ref",
        "kind": "widget_reference",
        "widget": "ctrl_gain"
      },
      {
        "id": "write_label_text",
        "kind": "primitive",
        "type": "frog.ui.property_write",
        "widget_member": {
          "part": "label",
          "member": "text"
        }
      }
    ],
    "edges": [
      {
        "id": "e1",
        "from": { "node": "status_text", "port": "value" },
        "to":   { "node": "write_label_text", "port": "value" }
      },
      {
        "id": "e2",
        "from": { "node": "ctrl_gain_ref", "port": "ref" },
        "to":   { "node": "write_label_text", "port": "ref" }
      }
    ]
  }
}</pre>

<h3 id="example-method-invoke">16.3 Invoke a Widget Method</h3>

<pre>{
  "diagram": {
    "nodes": [
      {
        "id": "ctrl_gain_ref",
        "kind": "widget_reference",
        "widget": "ctrl_gain"
      },
      {
        "id": "invoke_reset",
        "kind": "primitive",
        "type": "frog.ui.method_invoke",
        "widget_method": {
          "name": "reset_to_default"
        }
      }
    ],
    "edges": [
      {
        "id": "e1",
        "from": { "node": "ctrl_gain_ref", "port": "ref" },
        "to":   { "node": "invoke_reset", "port": "ref" }
      }
    ]
  }
}</pre>

<h3 id="example-natural-vs-object-value">16.4 Natural Value Path versus Object-Style Value Access</h3>

<p>
Natural value path:
</p>

<pre>{
  "diagram": {
    "nodes": [
      {
        "id": "input_signal",
        "kind": "interface_input",
        "interface_port": "signal"
      },
      {
        "id": "ctrl_gain_value",
        "kind": "widget_value",
        "widget": "ctrl_gain"
      },
      {
        "id": "mul_1",
        "kind": "primitive",
        "type": "frog.core.mul"
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
        "from": { "node": "input_signal", "port": "value" },
        "to":   { "node": "mul_1", "port": "a" }
      },
      {
        "id": "e2",
        "from": { "node": "ctrl_gain_value", "port": "value" },
        "to":   { "node": "mul_1", "port": "b" }
      },
      {
        "id": "e3",
        "from": { "node": "mul_1", "port": "result" },
        "to":   { "node": "ind_result_value", "port": "value" }
      }
    ]
  }
}</pre>

<p>
Object-style access to the same widget primary value:
</p>

<pre>{
  "diagram": {
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
      }
    ],
    "edges": [
      {
        "id": "e1",
        "from": { "node": "ctrl_gain_ref", "port": "ref" },
        "to":   { "node": "read_gain_value", "port": "ref" }
      }
    ]
  }
}</pre>

<h3 id="example-sequenced-ui-side-effects">16.5 Sequenced UI Side Effects</h3>

<pre>{
  "diagram": {
    "nodes": [
      {
        "id": "ctrl_gain_ref",
        "kind": "widget_reference",
        "widget": "ctrl_gain"
      },
      {
        "id": "write_visible",
        "kind": "primitive",
        "type": "frog.ui.property_write",
        "widget_member": {
          "member": "visible"
        }
      },
      {
        "id": "invoke_focus",
        "kind": "primitive",
        "type": "frog.ui.method_invoke",
        "widget_method": {
          "name": "focus"
        }
      }
    ],
    "edges": [
      {
        "id": "e1",
        "from": { "node": "ctrl_gain_ref", "port": "ref" },
        "to":   { "node": "write_visible", "port": "ref" }
      },
      {
        "id": "e2",
        "from": { "node": "ctrl_gain_ref", "port": "ref" },
        "to":   { "node": "invoke_focus", "port": "ref" }
      },
      {
        "id": "e3",
        "from": { "node": "write_visible", "port": "ui_out" },
        "to":   { "node": "invoke_focus", "port": "ui_in" }
      }
    ]
  }
}</pre>

<hr/>

<h2 id="out-of-scope-for-v01">17. Out of Scope for v0.1</h2>

<ul>
  <li>event structures and event-case dispatch,</li>
  <li>registration-based UI event nodes,</li>
  <li>asynchronous callback delivery,</li>
  <li>general widget reference storage and transport semantics,</li>
  <li>cross-thread UI affinity rules beyond what an active runtime profile defines,</li>
  <li>automatic inference of UI sequencing in all cases,</li>
  <li>full standardization of every possible widget-library member set.</li>
</ul>

<hr/>

<h2 id="summary">18. Summary</h2>

<p>
FROG widget interaction in v0.1 is based on one explicit principle:
ordinary widget value flow and object-style widget access are different mechanisms and MUST remain different mechanisms.
</p>

<ul>
  <li><code>widget_value</code> is the natural primary-value path.</li>
  <li><code>widget_reference</code> plus <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code> is the object-style path.</li>
  <li>Property descriptors use <code>widget_member</code>.</li>
  <li>Method descriptors use <code>widget_method</code>.</li>
  <li>Primitive signatures and primitive-local interaction behavior belong to <code>Libraries/UI.md</code>.</li>
  <li>The general diagram representation of <code>widget_value</code> and <code>widget_reference</code> remains owned by <code>Expression/Diagram.md</code>.</li>
</ul>

<p>
This gives FROG a clean and durable source-facing interaction model for front-panel widgets without collapsing UI objects into ordinary value wires.
</p>
