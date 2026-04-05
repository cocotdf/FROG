<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">FROG Widget Interaction Specification</h1>

<p align="center">
  <strong>Definition of the canonical source-facing representation of object-style diagram interaction with front-panel widgets in <code>.frog</code> programs</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
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
  <li><a href="#typing-sequencing-and-effect-boundaries">12. Typing, Sequencing, and Effect Boundaries</a></li>
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
FROG widgets are structured UI objects declared in the <code>front_panel</code> section and defined at instance level by <code>Widget.md</code>.
</p>

<p>
This document specifies how the executable <code>diagram</code> represents <strong>object-style interaction</strong> with those widget instances through explicit interaction nodes.
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
</p>

<p>
The natural value path is the canonical representation for ordinary widget primary-value flow.
The object-style path is the canonical representation for:
</p>

<ul>
  <li>property reads,</li>
  <li>property writes,</li>
  <li>method invocation.</li>
</ul>

<p>
In v0.1, FROG uses three standardized widget interaction primitive families:
</p>

<ul>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
</ul>

<p>
The primary widget value has a dual status: it is the natural value terminal of a value-carrying widget, and it MAY also be exposed as an ordinary object property when the corresponding widget class contract allows it.
</p>

<p>
Accordingly, a widget value MAY be accessed naturally through <code>widget_value</code>, and MAY also be accessed through the object-style path as member <code>value</code>.
</p>

<p>
This document does not define repository-wide version policy.
Top-level <code>spec_version</code> identifies the source-format compatibility target of the containing <code>.frog</code> file, while the published specification corpus version remains governed centrally in <code>Versioning/Readme.md</code>.
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
  <li>the class-side legality of widget members,</li>
  <li>the canonical declaration and composition of the front panel,</li>
  <li>the primitive identities and full primitive signatures beyond their source-facing use here,</li>
  <li>the primitive-local execution semantics of UI interaction operations,</li>
  <li>the general executable semantics of the diagram,</li>
  <li>the repository-wide version-transition doctrine.</li>
</ul>

<hr/>

<h2 id="goals">3. Goals</h2>

<p>
The widget interaction model is designed to satisfy the following goals:
</p>

<ul>
  <li><strong>Object consistency</strong> — widget interaction MUST follow the widget object model rather than introduce ad hoc UI-specific exceptions.</li>
  <li><strong>Contract consistency</strong> — object-style access MUST remain legal only when permitted by the corresponding widget class contract.</li>
  <li><strong>Dataflow clarity</strong> — ordinary value flow and explicit object access MUST remain distinct.</li>
  <li><strong>Source explicitness</strong> — object-style interaction MUST be represented through explicit source constructs rather than hidden editor conventions.</li>
  <li><strong>Type safety</strong> — ordinary value typing MUST remain compatible with the FROG type system.</li>
  <li><strong>Token separation</strong> — ordinary typed values, widget references, and UI sequencing tokens MUST remain distinct categories and MUST NOT be silently collapsed.</li>
  <li><strong>Profile extensibility</strong> — widget classes MAY expose different properties, methods, parts, and access modes under different profiles while preserving one common interaction model.</li>
  <li><strong>Architectural separation</strong> — widget interaction MUST NOT redefine public interface semantics, front-panel composition semantics, widget class contracts, general execution semantics, or the ownership of the standardized <code>frog.ui.*</code> primitive surface.</li>
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

<p>
In particular, base v0.1 keeps the following distinction explicit:
</p>

<ul>
  <li>a widget reference is an object-access token, not an ordinary user-declared value type expression,</li>
  <li><code>ui_in</code> and <code>ui_out</code> are sequencing tokens, not ordinary typed value ports,</li>
  <li>ordinary value ports remain governed by <code>Type.md</code>.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">5. Relation with Other Specifications</h2>

<p>
This document depends on the following specifications:
</p>

<ul>
  <li><code>Expression/Type.md</code> — ordinary value types, compatibility rules, and implicit coercion rules.</li>
  <li><code>Expression/Widget.md</code> — widget instances, roles, value behavior, source-level parts, and source-level widget identity.</li>
  <li><code>Expression/Widget class contract.md</code> — class-side member contracts, part ownership, member legality, access modes, profile gating, host gating, and class-level object exposure.</li>
  <li><code>Expression/Front panel.md</code> — declaration and serialization of widget instances.</li>
  <li><code>Expression/Diagram.md</code> — executable graph structure, node categories, canonical widget node kinds, and port-resolution rules.</li>
  <li><code>Libraries/UI.md</code> — the standardized <code>frog.ui.*</code> primitive catalog, primitive signatures, primitive typing rules, sequencing rules, and primitive-local interaction semantics.</li>
  <li><code>Versioning/Readme.md</code> — centralized distinction between specification corpus version, top-level <code>spec_version</code>, and program artifact versioning.</li>
</ul>

<p>
This document complements, but does not redefine, the following canonical diagram node kinds:
</p>

<ul>
  <li><code>widget_value</code> — natural primary-value participation.</li>
  <li><code>widget_reference</code> — object-style widget access anchor.</li>
</ul>

<p>
This document also does not redefine public interface semantics. A front-panel widget does not create a public interface port by itself. Public interface behavior remains represented canonically through <code>interface_input</code> and <code>interface_output</code> in the diagram.
</p>

<p>
Ownership is intentionally split as follows:
</p>

<pre><code>Widget interaction.md
  -&gt; source-facing interaction model
  -&gt; member descriptor model used by interaction nodes
  -&gt; graph-shape constraints
  -&gt; source-level validation rules for widget interaction forms

Widget.md
  -&gt; widget instance model
  -&gt; widget roles
  -&gt; value behavior at instance level
  -&gt; source-visible widget parts and source identity

Widget class contract.md
  -&gt; class-side member contracts
  -&gt; part ownership
  -&gt; readable / writable / invocable legality
  -&gt; profile and host gating
  -&gt; design-time vs runtime access constraints

Diagram.md
  -&gt; executable graph structure
  -&gt; widget_value / widget_reference node kinds
  -&gt; primitive-node port resolution

Libraries/UI.md
  -&gt; frog.ui.* primitive identities
  -&gt; primitive signatures
  -&gt; primitive-local typing and sequencing rules
  -&gt; primitive-local interaction semantics

Versioning/Readme.md
  -&gt; repository-wide version-transition doctrine
</code></pre>

<hr/>

<h2 id="conceptual-model">6. Conceptual Model</h2>

<p>
A widget interaction node addresses a member of a widget object.
</p>

<p>
A widget member addressed through this document is one of:
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
graph_1.x_scale.visible
</code></pre>

<p>
The object-style interaction path is always represented conceptually as:
</p>

<pre><code>widget_reference -&gt; frog.ui.property_read
widget_reference -&gt; frog.ui.property_write
widget_reference -&gt; frog.ui.method_invoke
</code></pre>

<p>
A widget interaction node does not define the widget instance. It operates on an already-declared widget instance from the <code>front_panel</code>.
</p>

<p>
A widget interaction node also does not define which members are legal for the targeted class. It relies on the corresponding widget class contract.
</p>

<p>
When explicit ordering of UI side effects is required, widget interaction nodes MAY participate in a sequencing chain through <code>ui_in</code> and <code>ui_out</code>. The primitive-level meaning of those sequencing ports is defined by <code>Libraries/UI.md</code>.
</p>

<p>
The following distinction MUST remain explicit:
</p>

<pre><code>ordinary typed value
    !=
widget reference token
    !=
UI sequencing token
</code></pre>

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

<h3>7.1 Full Conceptual Address</h3>

<p>
A full conceptual address may be understood as:
</p>

<pre><code>{
  "widget": "ctrl_gain",
  "part": "label",
  "member": "text"
}
</code></pre>

<p>
For methods:
</p>

<pre><code>{
  "widget": "ctrl_gain",
  "part": "label",
  "name": "show"
}
</code></pre>

<h3>7.2 Primitive-Local Member Descriptor</h3>

<p>
In the canonical v0.1 diagram model, widget identity is carried by the incoming <code>ref</code> port, not embedded directly in the primitive node.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>property interaction nodes MUST declare a <code>widget_member</code> descriptor,</li>
  <li>method interaction nodes MUST declare a <code>widget_method</code> descriptor.</li>
</ul>

<p>
Canonical property member descriptors:
</p>

<pre><code>{ "member": "text" }
{ "part": "label", "member": "text" }
</code></pre>

<p>
Canonical method descriptors:
</p>

<pre><code>{ "name": "focus" }
{ "part": "label", "name": "show" }
</code></pre>

<h3>7.3 Widget-Level Member Addressing</h3>

<p>
If <code>part</code> is omitted, the addressed member belongs to the widget itself.
</p>

<p>
Examples:
</p>

<pre><code>{ "member": "value" }
{ "member": "visible" }
{ "name": "focus" }
</code></pre>

<h3>7.4 Part-Level Member Addressing</h3>

<p>
If <code>part</code> is present, the addressed member belongs to the named widget part.
</p>

<p>
Examples:
</p>

<pre><code>{ "part": "label", "member": "text" }
{ "part": "label", "member": "visible" }
{ "part": "label", "name": "show" }
</code></pre>

<h3>7.5 Address Validity</h3>

<p>
A widget member address is valid only if all of the following hold:
</p>

<ul>
  <li>the referenced widget exists in <code>front_panel</code>,</li>
  <li>the referenced part exists when <code>part</code> is specified,</li>
  <li>the addressed member exists for the widget class or widget-part contract under the active profile,</li>
  <li>the addressed member is compatible with the interaction kind being used,</li>
  <li>the relevant access mode is allowed in the current context,</li>
  <li>profile and host requirements are satisfied when such gates exist.</li>
</ul>

<p>
For example:
</p>

<ul>
  <li><code>frog.ui.property_read</code> MUST target a readable property,</li>
  <li><code>frog.ui.property_write</code> MUST target a writable property,</li>
  <li><code>frog.ui.method_invoke</code> MUST target an invocable method.</li>
</ul>

<p>
Those legality rules are owned by the corresponding widget class contract, not by this document.
</p>

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
The full primitive signatures, including required and optional ports beyond the source-facing reference model, are owned by <code>Libraries/UI.md</code> together with <code>Expression/Diagram.md</code>.
</p>

<hr/>

<h2 id="property-read-representation">9. Property Read Representation</h2>

<p>
A property read interaction represents a read of a property value from a widget or widget part into the diagram.
</p>

<h3>9.1 Standard Primitive Identifier</h3>

<pre><code>frog.ui.property_read
</code></pre>

<h3>9.2 Required Structural Fields</h3>

<pre><code>{
  "id": "read_gain_visible",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "widget_member": {
    "member": "visible"
  }
}
</code></pre>

<h3>9.3 Representation Rules</h3>

<ul>
  <li>the node MUST consume a compatible widget reference through <code>ref</code>,</li>
  <li>the node MUST declare <code>widget_member</code>,</li>
  <li>the addressed member MUST be a readable property under the applicable widget class contract and active profile.</li>
</ul>

<h3>9.4 Access to Primary Value as a Property</h3>

<p>
Reading <code>{ "member": "value" }</code> through <code>frog.ui.property_read</code> is valid only when the widget class contract exposes <code>value</code> as a readable property.
</p>

<p>
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

<h3>10.1 Standard Primitive Identifier</h3>

<pre><code>frog.ui.property_write
</code></pre>

<h3>10.2 Required Structural Fields</h3>

<pre><code>{
  "id": "write_gain_label",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "widget_member": {
    "part": "label",
    "member": "text"
  }
}
</code></pre>

<h3>10.3 Representation Rules</h3>

<ul>
  <li>the node MUST consume a compatible widget reference through <code>ref</code>,</li>
  <li>the node MUST declare <code>widget_member</code>,</li>
  <li>the addressed member MUST be a writable property under the applicable widget class contract and active profile.</li>
</ul>

<h3>10.4 Access to Primary Value as a Property</h3>

<p>
Writing <code>{ "member": "value" }</code> through <code>frog.ui.property_write</code> is valid only when the widget class contract exposes <code>value</code> as a writable property.
</p>

<p>
This object-style write MUST remain semantically distinct from the natural primary value path represented by <code>widget_value</code>. For ordinary widget value participation in dataflow, tools SHOULD prefer <code>widget_value</code>.
</p>

<p>
Primitive signature details, typing, sequencing-port behavior, and write semantics belong to <code>Libraries/UI.md</code>.
</p>

<hr/>

<h2 id="method-invoke-representation">11. Method Invoke Representation</h2>

<p>
A method invoke interaction represents a method call on a widget or widget part.
</p>

<h3>11.1 Standard Primitive Identifier</h3>

<pre><code>frog.ui.method_invoke
</code></pre>

<h3>11.2 Required Structural Fields</h3>

<pre><code>{
  "id": "invoke_reset",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "widget_method": {
    "name": "reset_to_default"
  }
}
</code></pre>

<h3>11.3 Representation Rules</h3>

<ul>
  <li>the node MUST consume a compatible widget reference through <code>ref</code>,</li>
  <li>the node MUST declare <code>widget_method</code>,</li>
  <li>the addressed member MUST be an invocable method under the applicable widget class contract and active profile.</li>
</ul>

<h3>11.4 Method Invocation and Parts</h3>

<p>
Part-scoped method invocation is represented by including <code>part</code> in the method descriptor.
</p>

<pre><code>{
  "id": "invoke_label_show",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "widget_method": {
    "part": "label",
    "name": "show"
  }
}
</code></pre>

<p>
Whether the targeted part exists, and whether the named method is invocable on that part, depends on the corresponding widget class contract.
</p>

<p>
Primitive signature details, typing, sequencing-port behavior, and invocation semantics belong to <code>Libraries/UI.md</code>.
</p>

<hr/>

<h2 id="typing-sequencing-and-effect-boundaries">12. Typing, Sequencing, and Effect Boundaries</h2>

<p>
Typing rules for widget interaction nodes are not owned entirely by this document.
</p>

<p>
They depend on:
</p>

<ul>
  <li>the FROG type system defined in <code>Type.md</code>,</li>
  <li>the member types and method signatures declared by the widget class contract,</li>
  <li>the primitive-level typing rules owned by <code>Libraries/UI.md</code>.</li>
</ul>

<p>
Similarly, explicit sequencing through <code>ui_in</code> and <code>ui_out</code> is not owned entirely by this document.
</p>

<p>
This document only states that widget interaction nodes MAY participate in explicit UI sequencing when the underlying primitive contract supports it.
</p>

<p>
The following distinction MUST remain explicit:
</p>

<pre><code>member legality
  !=
primitive signature
  !=
primitive-local execution semantics
</code></pre>

<p>
Respectively:
</p>

<ul>
  <li>member legality belongs to <code>Widget class contract.md</code>,</li>
  <li>primitive signature belongs to <code>Libraries/UI.md</code>,</li>
  <li>primitive-local execution semantics belong to <code>Libraries/UI.md</code> and the relevant execution-semantics layers.</li>
</ul>

<p>
The following distinction MUST also remain explicit:
</p>

<pre><code>ordinary typed value ports
  !=
widget reference ports
  !=
UI sequencing ports
</code></pre>

<p>
Accordingly:
</p>

<ul>
  <li>ordinary value ports are governed by <code>Type.md</code>,</li>
  <li><code>ref</code> ports carry widget-reference tokens defined by the widget interaction model and the corresponding primitive contracts,</li>
  <li><code>ui_in</code> and <code>ui_out</code> carry opaque sequencing tokens used only for explicit UI ordering when supported.</li>
</ul>

<hr/>

<h2 id="diagram-representation">13. Diagram Representation</h2>

<p>
Widget interaction nodes appear inside the authoritative executable <code>diagram</code> as primitive nodes.
</p>

<p>
Conceptually:
</p>

<pre><code>front_panel widget instance
        |
        +-- widget_value -----------------&gt; ordinary value flow
        |
        +-- widget_reference ------------&gt; object-style interaction
                                             |
                                             +-- frog.ui.property_read
                                             +-- frog.ui.property_write
                                             +-- frog.ui.method_invoke
</code></pre>

<p>
The interaction node itself does not carry widget identity directly. Widget identity is supplied through the incoming <code>ref</code> edge from a <code>widget_reference</code> node.
</p>

<p>
This separation is intentional:
</p>

<ul>
  <li><code>widget_reference</code> identifies the target widget instance,</li>
  <li>the interaction primitive identifies the kind of access,</li>
  <li>the local descriptor identifies the targeted member,</li>
  <li>the widget class contract determines whether that member access is legal.</li>
</ul>

<hr/>

<h2 id="validation-rules">14. Validation Rules</h2>

<p>
Validators MUST enforce at least the following rules:
</p>

<ul>
  <li>a widget interaction node MUST be a <code>primitive</code> node,</li>
  <li>its <code>type</code> MUST be one of the standardized widget interaction primitive identifiers,</li>
  <li>it MUST consume a compatible widget reference through <code>ref</code>,</li>
  <li>property interaction nodes MUST declare <code>widget_member</code>,</li>
  <li>method interaction nodes MUST declare <code>widget_method</code>,</li>
  <li>the referenced widget MUST exist,</li>
  <li>the referenced part MUST exist when a part is specified,</li>
  <li>the addressed member MUST exist on the targeted class or targeted part contract,</li>
  <li>the requested access mode MUST be legal in the current context,</li>
  <li>profile gates and host gates MUST be respected when present.</li>
</ul>

<p>
Validators SHOULD diagnose at least the following error classes:
</p>

<ul>
  <li>missing widget reference input,</li>
  <li>invalid primitive kind,</li>
  <li>unknown widget interaction primitive identifier,</li>
  <li>missing <code>widget_member</code> or <code>widget_method</code> descriptor,</li>
  <li>unknown widget instance,</li>
  <li>unknown widget part,</li>
  <li>unknown member,</li>
  <li>read of non-readable property,</li>
  <li>write to non-writable property,</li>
  <li>invocation of non-invocable method,</li>
  <li>use of profile-gated member outside the required profile,</li>
  <li>use of host-gated member without required host capability,</li>
  <li>attempt to use object-style access where only natural value access is valid,</li>
  <li>treating a widget reference token as an ordinary typed value,</li>
  <li>treating a sequencing port as an ordinary typed value port.</li>
</ul>

<p>
These checks validate the source-facing widget-object interaction model.
They do not, by themselves, redefine top-level <code>spec_version</code> policy or repository-wide corpus-version governance.
</p>

<hr/>

<h2 id="source-to-library-mapping">15. Source-to-Library Mapping</h2>

<p>
The source-facing interaction model standardized here maps to intrinsic UI primitives in the <code>frog.ui.*</code> namespace.
</p>

<p>
At minimum:
</p>

<ul>
  <li>source-level property read maps to <code>frog.ui.property_read</code>,</li>
  <li>source-level property write maps to <code>frog.ui.property_write</code>,</li>
  <li>source-level method invoke maps to <code>frog.ui.method_invoke</code>.</li>
</ul>

<p>
This document standardizes the source-facing use of those primitives, not their full primitive definitions.
</p>

<hr/>

<h2 id="examples">16. Examples</h2>

<h3>16.1 Read widget property</h3>

<pre><code>{
  "id": "read_gain_visible",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "widget_member": {
    "member": "visible"
  }
}
</code></pre>

<h3>16.2 Write part property</h3>

<pre><code>{
  "id": "write_gain_label",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "widget_member": {
    "part": "label",
    "member": "text"
  }
}
</code></pre>

<h3>16.3 Invoke widget method</h3>

<pre><code>{
  "id": "invoke_reset",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "widget_method": {
    "name": "reset_to_default"
  }
}
</code></pre>

<h3>16.4 Invoke part method</h3>

<pre><code>{
  "id": "invoke_label_show",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "widget_method": {
    "part": "label",
    "name": "show"
  }
}
</code></pre>

<hr/>

<h2 id="out-of-scope-for-v01">17. Out of Scope for v0.1</h2>

<p>
The following are intentionally out of scope for this document in v0.1:
</p>

<ul>
  <li>a complete event registration model,</li>
  <li>asynchronous UI message delivery,</li>
  <li>general-purpose widget references as ordinary first-class values,</li>
  <li>one mandatory UI runtime architecture,</li>
  <li>the full execution semantics of every UI interaction primitive,</li>
  <li>the complete effect model for all UI runtimes and profiles.</li>
</ul>

<hr/>

<h2 id="summary">18. Summary</h2>

<p>
This document defines the canonical source-facing representation of object-style widget interaction in the FROG diagram.
</p>

<p>
It standardizes:
</p>

<ul>
  <li>how a widget reference is consumed,</li>
  <li>how a targeted property or method is identified,</li>
  <li>how property reads, property writes, and method invocations are represented in source,</li>
  <li>how those interactions are validated structurally.</li>
</ul>

<p>
It does not standardize:
</p>

<ul>
  <li>widget instance composition,</li>
  <li>widget class member legality,</li>
  <li>primitive-local execution semantics,</li>
  <li>general execution semantics of the language,</li>
  <li>source-format compatibility law,</li>
  <li>published specification corpus versioning.</li>
</ul>

<p>
That separation allows FROG to support rich widget-object interaction while keeping instance model, class contract, diagram representation, primitive semantics, and runtime realization explicitly distinct.
</p>
