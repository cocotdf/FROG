<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="150" />
</p>

<h1 align="center">🐸 FROG Widget Interaction Specification</h1>

<p align="center">
  Definition of object-style diagram interaction with front-panel widgets in <strong>.frog</strong> programs<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Goals</a></li>
  <li><a href="#scope-for-v01">3. Scope for v0.1</a></li>
  <li><a href="#relation-with-other-specifications">4. Relation with Other Specifications</a></li>
  <li><a href="#conceptual-model">5. Conceptual Model</a></li>
  <li><a href="#widget-member-addressing">6. Widget Member Addressing</a></li>
  <li><a href="#interaction-node-families">7. Interaction Node Families</a></li>
  <li><a href="#property-read-node">8. Property Read Node</a></li>
  <li><a href="#property-write-node">9. Property Write Node</a></li>
  <li><a href="#method-invoke-node">10. Method Invoke Node</a></li>
  <li><a href="#typing-and-sequencing">11. Typing and Sequencing</a></li>
  <li><a href="#diagram-representation">12. Diagram Representation</a></li>
  <li><a href="#validation-rules">13. Validation Rules</a></li>
  <li><a href="#execution-semantics">14. Execution Semantics</a></li>
  <li><a href="#examples">15. Examples</a></li>
  <li><a href="#out-of-scope-for-v01">16. Out of Scope for v0.1</a></li>
  <li><a href="#summary">17. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
FROG widgets are structured UI objects declared in the <code>front_panel</code> section and described by
<code>Widget.md</code> and <code>Front panel.md</code>.
This document defines how the executable <code>diagram</code> may interact with those widget instances through
explicit object-style interaction nodes.
</p>

<p>
FROG distinguishes two different paths for widget participation in a diagram:
</p>

<ul>
  <li><strong>Natural value path</strong> — through <code>widget_value</code>, which materializes the primary widget value in ordinary dataflow.</li>
  <li><strong>Object-style path</strong> — through <code>widget_reference</code> plus explicit widget interaction primitives.</li>
</ul>

<p>
These two paths serve different purposes and MUST remain semantically distinct.
The natural value path is the canonical representation for ordinary value flow.
The object-style path is the canonical representation for reading properties, writing properties, and invoking widget methods.
</p>

<p>
In v0.1, FROG standardizes three widget interaction primitive families:
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

<h2 id="goals">2. Goals</h2>

<p>
The widget interaction model is designed to satisfy the following goals:
</p>

<ul>
  <li><strong>Object consistency</strong> — widget interaction MUST follow the widget object model rather than ad hoc UI-specific exceptions.</li>
  <li><strong>Dataflow clarity</strong> — ordinary value flow and explicit object access MUST remain distinct.</li>
  <li><strong>Type safety</strong> — widget member types and method signatures MUST remain compatible with the FROG type system.</li>
  <li><strong>Deterministic ordering when needed</strong> — UI side effects MAY be ordered explicitly through <code>ui_in</code> / <code>ui_out</code>.</li>
  <li><strong>Profile extensibility</strong> — widget classes MAY expose different properties, methods, and parts under different profiles while preserving one common interaction model.</li>
  <li><strong>Architectural separation</strong> — widget interaction MUST NOT redefine public interface semantics, general execution semantics, or front-panel layout semantics.</li>
</ul>

<hr/>

<h2 id="scope-for-v01">3. Scope for v0.1</h2>

<p>
FROG v0.1 standardizes:
</p>

<ul>
  <li>the conceptual addressing model for widget members,</li>
  <li>property reads,</li>
  <li>property writes,</li>
  <li>method invocation,</li>
  <li>their integration with <code>widget_reference</code>,</li>
  <li>their type constraints,</li>
  <li>their validation rules,</li>
  <li>their optional UI sequencing ports.</li>
</ul>

<p>
FROG v0.1 does not fully standardize:
</p>

<ul>
  <li>a complete event structure model,</li>
  <li>widget event registration nodes,</li>
  <li>asynchronous UI message delivery,</li>
  <li>widget references as general-purpose first-class value types,</li>
  <li>a complete effect system covering every UI runtime profile.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">4. Relation with Other Specifications</h2>

<p>
This document depends on the following specifications:
</p>

<ul>
  <li><code>Type.md</code> — ordinary value types, compatibility, and coercion rules,</li>
  <li><code>Widget.md</code> — widget classes, roles, parts, properties, methods, and member availability,</li>
  <li><code>Front panel.md</code> — declaration and serialization of widget instances,</li>
  <li><code>Diagram.md</code> — executable graph structure and node categories.</li>
</ul>

<p>
This document complements, but does not redefine, the following canonical diagram node kinds:
</p>

<ul>
  <li><code>widget_value</code> — natural primary value participation,</li>
  <li><code>widget_reference</code> — object-style widget access anchor.</li>
</ul>

<p>
This document also does not redefine public interface semantics.
A front-panel widget does not create a public interface port by itself.
Public interface behavior remains represented canonically through <code>interface_input</code> and <code>interface_output</code> in the diagram.
</p>

<hr/>

<h2 id="conceptual-model">5. Conceptual Model</h2>

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

<pre><code>ctrl_gain.value
ctrl_gain.visible
ctrl_gain.label.text
ctrl_gain.focus()
graph_1.x_scale.visible</code></pre>

<p>
The object-style interaction path is always:
</p>

<pre><code>widget_reference  →  frog.ui.property_read
widget_reference  →  frog.ui.property_write
widget_reference  →  frog.ui.method_invoke</code></pre>

<p>
A widget interaction node does not define the widget instance.
It operates on an already-declared widget instance from the <code>front_panel</code>.
</p>

<p>
When explicit ordering of UI side effects is required, widget interaction nodes MAY participate in a sequencing chain through
<code>ui_in</code> and <code>ui_out</code>.
These sequencing ports are separate from ordinary dataflow values.
</p>

<hr/>

<h2 id="widget-member-addressing">6. Widget Member Addressing</h2>

<p>
Widget member addressing identifies:
</p>

<ul>
  <li>the target widget instance,</li>
  <li>optionally a named widget part,</li>
  <li>the addressed property or method.</li>
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
For methods:
</p>

<pre><code>{
  "widget": "ctrl_gain",
  "part": "label",
  "name": "show"
}</code></pre>

<h3>6.2 Primitive-local member descriptor</h3>

<p>
In the canonical v0.1 diagram model, widget identity is carried by the incoming <code>ref</code> port, not embedded directly in the primitive node.
Accordingly:
</p>

<ul>
  <li>property nodes MUST declare a <code>widget_member</code> descriptor,</li>
  <li>method nodes MUST declare a <code>widget_method</code> descriptor.</li>
</ul>

<p>
Canonical property member descriptors:
</p>

<pre><code>{ "member": "text" }
{ "part": "label", "member": "text" }</code></pre>

<p>
Canonical method descriptors:
</p>

<pre><code>{ "name": "focus" }
{ "part": "label", "name": "show" }</code></pre>

<h3>6.3 Widget-level member addressing</h3>

<p>
If <code>part</code> is omitted, the addressed member belongs to the widget itself.
</p>

<p>Examples:</p>

<pre><code>{ "member": "value" }
{ "member": "visible" }
{ "name": "focus" }</code></pre>

<h3>6.4 Part-level member addressing</h3>

<p>
If <code>part</code> is present, the addressed member belongs to the named widget part.
</p>

<p>Examples:</p>

<pre><code>{ "part": "label", "member": "text" }
{ "part": "label", "member": "visible" }
{ "part": "label", "name": "show" }</code></pre>

<h3>6.5 Address validity</h3>

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

<h2 id="interaction-node-families">7. Interaction Node Families</h2>

<p>
In v0.1, widget interactions are represented canonically as <code>primitive</code> nodes in the diagram.
</p>

<p>
The standardized primitive identifiers are:
</p>

<ul>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
</ul>

<p>
Each widget interaction node MUST satisfy all of the following:
</p>

<ul>
  <li><code>kind</code> MUST be <code>primitive</code>,</li>
  <li><code>type</code> MUST be one of the standardized primitive identifiers above,</li>
  <li>the node MUST consume a widget reference through required input port <code>ref</code>,</li>
  <li>property nodes MUST declare <code>widget_member</code>,</li>
  <li>method nodes MUST declare <code>widget_method</code>.</li>
</ul>

<p>
Additionally:
</p>

<ul>
  <li><code>ui_in</code> is an optional sequencing input port,</li>
  <li><code>ui_out</code> is an optional sequencing output port.</li>
</ul>

<hr/>

<h2 id="property-read-node">8. Property Read Node</h2>

<p>
A property read node reads a property value from a widget or widget part and exposes that value to the diagram.
</p>

<h3>8.1 Standard primitive identifier</h3>

<pre><code>frog.ui.property_read</code></pre>

<h3>8.2 Required fields</h3>

<pre><code>{
  "id": "read_gain_visible",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "widget_member": {
    "member": "visible"
  }
}</code></pre>

<h3>8.3 Standard port signature</h3>

<p>
A property read node exposes:
</p>

<ul>
  <li>required input port <code>ref</code>,</li>
  <li>optional input port <code>ui_in</code>,</li>
  <li>required output port <code>value</code>,</li>
  <li>optional output port <code>ui_out</code>.</li>
</ul>

<p>
The type of output port <code>value</code> MUST equal the type of the addressed property.
The <code>ref</code> port carries an opaque widget reference token compatible with the addressed widget.
</p>

<h3>8.4 Access to primary value as a property</h3>

<p>
Reading <code>{ "member": "value" }</code> through <code>frog.ui.property_read</code> is valid when the widget class exposes
<code>value</code> as a readable property.
However, when the intent is ordinary value flow, tools SHOULD prefer the natural <code>widget_value</code> representation.
</p>

<h3>8.5 Read semantics</h3>

<p>
A property read observes the current value of the addressed property at execution time.
If <code>ui_in</code> is connected, the observation MUST occur after the preceding UI interaction in that sequencing chain.
If <code>ui_out</code> is connected, it becomes available only after the read has completed.
</p>

<hr/>

<h2 id="property-write-node">9. Property Write Node</h2>

<p>
A property write node writes a diagram value into a writable widget or widget-part property.
</p>

<h3>9.1 Standard primitive identifier</h3>

<pre><code>frog.ui.property_write</code></pre>

<h3>9.2 Required fields</h3>

<pre><code>{
  "id": "write_gain_label",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "widget_member": {
    "part": "label",
    "member": "text"
  }
}</code></pre>

<h3>9.3 Standard port signature</h3>

<p>
A property write node exposes:
</p>

<ul>
  <li>required input port <code>ref</code>,</li>
  <li>required input port <code>value</code>,</li>
  <li>optional input port <code>ui_in</code>,</li>
  <li>optional output port <code>ui_out</code>.</li>
</ul>

<p>
The input port <code>value</code> MUST be type-compatible with the addressed property.
The <code>ref</code> port carries an opaque widget reference token compatible with the addressed widget.
</p>

<h3>9.4 Access to primary value as a property</h3>

<p>
Writing <code>{ "member": "value" }</code> through <code>frog.ui.property_write</code> is valid when the widget class exposes
<code>value</code> as a writable property.
This object-style write MUST remain semantically distinct from the natural primary value path represented by <code>widget_value</code>.
For ordinary widget value participation in dataflow, tools SHOULD prefer <code>widget_value</code>.
</p>

<h3>9.5 Write semantics</h3>

<p>
A property write applies a side effect to the addressed widget member.
If <code>ui_in</code> is connected, the write MUST occur only after the preceding sequencing token becomes available.
If <code>ui_out</code> is connected, it becomes available only after the write side effect has completed according to the active runtime profile.
</p>

<hr/>

<h2 id="method-invoke-node">10. Method Invoke Node</h2>

<p>
A method invoke node calls a method on a widget or widget part.
</p>

<h3>10.1 Standard primitive identifier</h3>

<pre><code>frog.ui.method_invoke</code></pre>

<h3>10.2 Required fields</h3>

<pre><code>{
  "id": "invoke_reset",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "widget_method": {
    "name": "reset_to_default"
  }
}</code></pre>

<h3>10.3 Standard port signature</h3>

<p>
A method invoke node exposes:
</p>

<ul>
  <li>required input port <code>ref</code>,</li>
  <li>zero or more method argument input ports, in canonical method order,</li>
  <li>optional input port <code>ui_in</code>,</li>
  <li>zero or more method result output ports, in canonical method order,</li>
  <li>optional output port <code>ui_out</code>.</li>
</ul>

<p>
Method argument and result port names MUST be defined by the addressed method signature.
Each method argument input MUST be type-compatible with the declared method parameter type.
Each method result output MUST have the declared result type.
</p>

<h3>10.4 Invocation semantics</h3>

<p>
A method invocation MAY produce:
</p>

<ul>
  <li>UI side effects,</li>
  <li>ordinary return values,</li>
  <li>both.</li>
</ul>

<p>
If <code>ui_in</code> is connected, the invocation MUST occur only after the preceding sequencing token becomes available.
If <code>ui_out</code> is connected, it becomes available only after invocation has completed according to the active runtime profile.
</p>

<hr/>

<h2 id="typing-and-sequencing">11. Typing and Sequencing</h2>

<h3>11.1 Widget reference typing</h3>

<p>
The <code>ref</code> port carries an opaque widget reference token.
In v0.1, this token is diagram-internal and interaction-specific.
It is not standardized as a general-purpose first-class value type for arbitrary storage, transport, or computation.
</p>

<h3>11.2 Property typing</h3>

<p>
Property read and write nodes MUST use the declared property type of the addressed widget member.
All compatibility checks and implicit coercions MUST follow the ordinary FROG type rules.
</p>

<h3>11.3 Method typing</h3>

<p>
Method invoke nodes MUST use the declared method signature of the addressed widget member.
Argument ports and result ports MUST follow the canonical method signature defined by the widget class under the active profile.
</p>

<h3>11.4 UI sequencing ports</h3>

<p>
The optional ports <code>ui_in</code> and <code>ui_out</code> define explicit ordering between UI interactions.
These ports:
</p>

<ul>
  <li>MUST NOT be interpreted as ordinary data values,</li>
  <li>MUST NOT redefine data dependency typing,</li>
  <li>MAY be omitted when no explicit UI ordering is required,</li>
  <li>SHOULD be used when deterministic ordering of UI side effects matters.</li>
</ul>

<p>
In v0.1, the sequencing token carried by <code>ui_in</code> / <code>ui_out</code> is opaque.
Its internal representation is runtime-defined, but its ordering meaning in the graph is standardized by this document.
</p>

<hr/>

<h2 id="diagram-representation">12. Diagram Representation</h2>

<p>
Widget interaction primitives appear as ordinary <code>primitive</code> nodes inside the diagram.
They are connected to a canonical <code>widget_reference</code> node that identifies the widget instance.
</p>

<p>
Example shape:
</p>

<pre><code>{
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
}</code></pre>

<p>
Canonical representation rules:
</p>

<ul>
  <li>a widget interaction node MUST be connected to a compatible <code>widget_reference</code>,</li>
  <li>a widget interaction node MUST NOT identify the target widget only through ad hoc local string fields,</li>
  <li>the widget member or method being addressed MUST be declared through <code>widget_member</code> or <code>widget_method</code>,</li>
  <li>ordinary value ports MUST be represented through ordinary diagram edges,</li>
  <li>explicit UI ordering, when used, MUST be represented through <code>ui_in</code> / <code>ui_out</code> edges.</li>
</ul>

<hr/>

<h2 id="validation-rules">13. Validation Rules</h2>

<p>
A diagram using widget interaction is valid only if all of the following hold:
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
  <li>all required method arguments are present,</li>
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

<h2 id="execution-semantics">14. Execution Semantics</h2>

<h3>14.1 General model</h3>

<p>
Widget interaction nodes participate in normal graph execution like other diagram nodes, subject to their data dependencies,
their optional UI sequencing dependencies, and the active runtime profile.
</p>

<h3>14.2 Property read</h3>

<p>
A property read produces an output value representing the addressed property at the moment of observation.
It does not itself define public interface behavior.
</p>

<h3>14.3 Property write</h3>

<p>
A property write produces a UI side effect on the addressed widget member.
A runtime MUST preserve ordering implied by ordinary data dependencies and by explicit <code>ui_in</code> / <code>ui_out</code> chains.
</p>

<h3>14.4 Method invocation</h3>

<p>
A method invocation applies the semantics defined by the addressed widget method.
This MAY include state change, visual change, focus change, value change, or other profile-defined behavior.
</p>

<h3>14.5 Natural versus object-style value access</h3>

<p>
When a widget exposes a primary value:
</p>

<ul>
  <li><code>widget_value</code> is the canonical natural representation for ordinary diagram value flow,</li>
  <li><code>frog.ui.property_read</code> / <code>frog.ui.property_write</code> with member <code>value</code> are explicit object-style representations.</li>
</ul>

<p>
These two forms MAY coexist in the same program when semantically justified,
but tools SHOULD preserve the distinction rather than collapsing them into one undifferentiated mechanism.
</p>

<hr/>

<h2 id="examples">15. Examples</h2>

<h3>15.1 Read a label text property</h3>

<pre><code>{
  "front_panel": {
    "widgets": [
      {
        "id": "ctrl_gain",
        "class": "frog.ui.numeric",
        "role": "control",
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
}</code></pre>

<h3>15.2 Write to a label text property from a public input</h3>

<pre><code>{
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
}</code></pre>

<h3>15.3 Invoke a widget method</h3>

<pre><code>{
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
}</code></pre>

<h3>15.4 Natural value path versus object-style value access</h3>

<p>
Natural value path:
</p>

<pre><code>{
  "nodes": [
    {
      "id": "ctrl_gain_value",
      "kind": "widget_value",
      "widget": "ctrl_gain"
    },
    {
      "id": "input_signal",
      "kind": "interface_input",
      "interface_port": "signal"
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
}</code></pre>

<p>
Object-style access to the same widget primary value:
</p>

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
    }
  ],
  "edges": [
    {
      "id": "e1",
      "from": { "node": "ctrl_gain_ref", "port": "ref" },
      "to":   { "node": "read_gain_value", "port": "ref" }
    }
  ]
}</code></pre>

<h3>15.5 Sequenced UI side effects</h3>

<pre><code>{
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
}</code></pre>

<hr/>

<h2 id="out-of-scope-for-v01">16. Out of Scope for v0.1</h2>

<ul>
  <li>event structures and event case dispatch,</li>
  <li>registration-based UI event nodes,</li>
  <li>asynchronous callback delivery,</li>
  <li>general widget reference storage and transport semantics,</li>
  <li>cross-thread UI affinity rules beyond what an active runtime profile defines,</li>
  <li>automatic inference of UI sequencing in all cases,</li>
  <li>full standardization of every possible widget library member set.</li>
</ul>

<hr/>

<h2 id="summary">17. Summary</h2>

<p>
FROG widget interaction in v0.1 is based on one explicit principle:
ordinary widget value flow and object-style widget access are different mechanisms and MUST remain different mechanisms.
</p>

<ul>
  <li><code>widget_value</code> is the canonical natural path for a widget primary value.</li>
  <li><code>widget_reference</code> is the canonical anchor for object-style access.</li>
  <li><code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code> are the standardized interaction primitives.</li>
  <li><code>widget_member</code> and <code>widget_method</code> are the canonical primitive-local descriptors.</li>
  <li><code>ui_in</code> / <code>ui_out</code> provide optional explicit ordering for UI side effects.</li>
</ul>

<p>
This keeps the language understandable for graphical dataflow users while preserving a clean long-term object model for UI interaction.
</p>
