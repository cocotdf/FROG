<h1 align="center">🐸 FROG Diagram Specification</h1>

<p align="center">
Definition of executable graphs in <strong>.frog</strong> programs<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#purpose-of-the-diagram">2. Purpose of the Diagram</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#location-in-a-frog-file">4. Location in a <code>.frog</code> File</a></li>
  <li><a href="#diagram-structure">5. Diagram Structure</a></li>
  <li><a href="#diagram-scopes">6. Diagram Scopes</a></li>
  <li><a href="#node-model">7. Node Model</a></li>
  <li><a href="#standard-node-kinds-for-v01">8. Standard Node Kinds for v0.1</a></li>
  <li><a href="#port-resolution-model">9. Port Resolution Model</a></li>
  <li><a href="#edge-model">10. Edge Model</a></li>
  <li><a href="#diagram-annotations">11. Diagram Annotations</a></li>
  <li><a href="#documentation-and-tags">12. Documentation and Tags</a></li>
  <li><a href="#layout-information">13. Layout Information</a></li>
  <li><a href="#frog-dependencies">14. FROG Dependencies</a></li>
  <li><a href="#subfrog-invocation">15. Sub-FROG Invocation</a></li>
  <li><a href="#interface-widget-and-structure-boundaries">16. Interface, Widget, and Structure Boundaries</a></li>
  <li><a href="#widget-interaction-model">17. Widget Interaction Model</a></li>
  <li><a href="#cycles-and-local-state">18. Cycles and Local State</a></li>
  <li><a href="#graph-validation">19. Graph Validation</a></li>
  <li><a href="#execution-semantics">20. Execution Semantics</a></li>
  <li><a href="#examples">21. Examples</a></li>
  <li><a href="#summary">22. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <code>diagram</code> section defines the executable dataflow graph of a FROG.
</p>

<p>
It contains:
</p>

<ul>
  <li>the nodes representing computation or other executable behavior,</li>
  <li>the edges representing directed graph connections between nodes,</li>
  <li>the structural links between the public interface, the internal graph, and front-panel widget participation,</li>
  <li>the source-level annotations used to document and organize the graph.</li>
</ul>

<p>
Execution semantics are derived from the validated graph together with:
</p>

<ul>
  <li>the public interface contract,</li>
  <li>the FROG type system,</li>
  <li>the widget model,</li>
  <li>the widget interaction model,</li>
  <li>the control-structure model,</li>
  <li>the local-state and cycle rules,</li>
  <li>any active primitive catalog or stricter execution profile.</li>
</ul>

<p>
The diagram is the canonical structural definition of execution in a FROG.
</p>

<hr/>

<h2 id="purpose-of-the-diagram">2. Purpose of the Diagram</h2>

<p>
The diagram provides:
</p>

<ul>
  <li>the executable logic of the FROG,</li>
  <li>the dependency graph of values and explicit effects,</li>
  <li>the structural link between the public interface and internal execution logic,</li>
  <li>the hierarchical composition mechanism used to invoke other FROGs,</li>
  <li>the place where front-panel widget values participate naturally in dataflow,</li>
  <li>the place where widget references, property access, method invocation, and explicit UI sequencing may participate in execution,</li>
  <li>the place where local state and valid feedback loops are expressed,</li>
  <li>the canonical source-level space for diagram annotations and documentation.</li>
</ul>

<p>
Nodes represent computation, structures, interface boundaries, widget-related interaction points, reusable sub-FROG invocations, or other standardized executable behavior.
Edges represent directional connectivity.
Annotations represent source documentation and visual organization only.
</p>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This document depends on the following FROG specifications:
</p>

<ul>
  <li><code>Expression/Type.md</code> — defines ordinary value typing and compatibility rules,</li>
  <li><code>Expression/Interface.md</code> — defines the public logical contract of a FROG,</li>
  <li><code>Expression/Front panel.md</code> — defines the serialized UI layer,</li>
  <li><code>Expression/Widget.md</code> — defines widget semantics and the primary widget-value model,</li>
  <li><code>Expression/Widget interaction.md</code> — defines object-style widget interaction primitives and optional UI sequencing,</li>
  <li><code>Language/Control structures.md</code> — defines structure semantics such as case and loop behavior,</li>
  <li><code>Language/State and cycles.md</code> — defines local state and cycle validity,</li>
  <li><code>Libraries/Core.md</code> — defines standard built-in functions such as <code>frog.core.add</code> and <code>frog.core.delay</code>.</li>
</ul>

<p>
This document defines the graph-level representation and validation rules that tie these subsystems together.
It does not redefine semantics already owned by those dedicated specifications.
</p>

<hr/>

<h2 id="location-in-a-frog-file">4. Location in a <code>.frog</code> File</h2>

<p>
The diagram appears as a top-level object in the canonical <code>.frog</code> source file.
</p>

<pre>
{
  "spec_version": "0.1",
  "metadata": {},
  "interface": {},
  "connector": {},
  "diagram": {},
  "front_panel": {}
}
</pre>

<p>
The <code>diagram</code> section MUST exist in a canonical <code>.frog</code> source file.
</p>

<hr/>

<h2 id="diagram-structure">5. Diagram Structure</h2>

<p>
The diagram object contains up to four fields:
</p>

<pre>
"diagram": {
  "nodes": [],
  "edges": [],
  "dependencies": [],
  "annotations": []
}
</pre>

<p>
Fields:
</p>

<ul>
  <li><code>nodes</code> — required array of graph nodes,</li>
  <li><code>edges</code> — required array of directed graph connections,</li>
  <li><code>dependencies</code> — optional array of referenced external FROGs,</li>
  <li><code>annotations</code> — optional array of visible diagram annotations.</li>
</ul>

<p>
The <code>nodes</code> and <code>edges</code> arrays MUST exist, even if one of them is empty.
The <code>dependencies</code> and <code>annotations</code> fields MAY be omitted when unused.
</p>

<p>
The <code>annotations</code> field belongs to canonical source because it describes author-created documentation and visual organization of the diagram.
It does not affect execution semantics.
</p>

<hr/>

<h2 id="diagram-scopes">6. Diagram Scopes</h2>

<p>
FROG diagrams are recursive.
</p>

<p>
The top-level <code>diagram</code> object defines the outer executable graph of the FROG.
Control structures MAY own internal executable regions, and each such region contains its own local diagram.
</p>

<p>
Therefore, FROG distinguishes:
</p>

<ul>
  <li><strong>top-level diagram scope</strong> — the root executable graph of the FROG,</li>
  <li><strong>region-local diagram scope</strong> — a nested executable graph owned by a structure region.</li>
</ul>

<p>
Each diagram scope has its own local node identifier space, edge identifier space, and annotation identifier space.
Rules defined in this document apply both to the top-level diagram and to region-local diagrams unless a structure-specific rule explicitly states otherwise.
</p>

<hr/>

<h2 id="node-model">7. Node Model</h2>

<p>
A node represents an executable or structurally meaningful element of the graph.
</p>

<p>
Every node MUST define:
</p>

<ul>
  <li><code>id</code> — unique node identifier within its owning diagram scope,</li>
  <li><code>kind</code> — node category.</li>
</ul>

<p>
A node MAY also define:
</p>

<ul>
  <li><code>layout</code> — graphical editor position,</li>
  <li><code>doc</code> — optional structured documentation,</li>
  <li><code>tags</code> — optional structured tags,</li>
  <li>kind-specific fields defined below.</li>
</ul>

<h3>7.1 Common node shape</h3>

<pre>
{
  "id": "node_1",
  "kind": "primitive",
  "type": "frog.core.add",
  "layout": {
    "x": 120,
    "y": 80
  }
}
</pre>

<p>
Nodes are structural objects.
Their valid ports are resolved from their kind and from the metadata required by that kind.
</p>

<hr/>

<h2 id="standard-node-kinds-for-v01">8. Standard Node Kinds for v0.1</h2>

<p>
FROG v0.1 defines the following standard node kinds:
</p>

<ul>
  <li><code>primitive</code></li>
  <li><code>structure</code></li>
  <li><code>subfrog</code></li>
  <li><code>interface_input</code></li>
  <li><code>interface_output</code></li>
  <li><code>widget_value</code></li>
  <li><code>widget_reference</code></li>
</ul>

<h3>8.1 <code>primitive</code></h3>

<p>
A <code>primitive</code> node represents a built-in or profile-defined function.
</p>

<pre>
{
  "id": "add_1",
  "kind": "primitive",
  "type": "frog.core.add",
  "layout": {
    "x": 240,
    "y": 120
  }
}
</pre>

<p>
Rules:
</p>

<ul>
  <li><code>type</code> MUST exist and identify the primitive function,</li>
  <li>primitive identifiers SHOULD use canonical namespaces such as <code>frog.core.*</code>, <code>frog.ui.*</code>, or other standardized library namespaces,</li>
  <li>the meaning and port signature of the primitive are defined by the active profile, standard library, or primitive catalog.</li>
</ul>

<p>
Primitive nodes include ordinary computational functions such as arithmetic operations, but MAY also include widget interaction primitives and local-state functions such as <code>frog.core.delay</code>.
</p>

<h3>8.2 <code>structure</code></h3>

<p>
A <code>structure</code> node represents a language-level control structure whose semantics are defined by <code>Language/Control structures.md</code>.
</p>

<pre>
{
  "id": "case_1",
  "kind": "structure",
  "structure_type": "case",
  "boundary": {
    "inputs": [],
    "outputs": []
  },
  "structure_terminals": {},
  "regions": [],
  "layout": {
    "x": 300,
    "y": 120,
    "width": 260,
    "height": 180
  }
}
</pre>

<p>
Rules:
</p>

<ul>
  <li><code>structure_type</code> MUST exist,</li>
  <li><code>structure_type</code> MUST identify a valid standardized or profile-defined structure family,</li>
  <li>the canonical standardized structure types for v0.1 are <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>,</li>
  <li><code>boundary</code>, <code>structure_terminals</code>, and <code>regions</code> MUST be valid for the chosen structure type,</li>
  <li>structure internals, tunnels, regions, and execution rules are defined by the control-structure specification rather than redefined here.</li>
</ul>

<h3>8.3 <code>subfrog</code></h3>

<p>
A <code>subfrog</code> node represents an invocation of another FROG.
</p>

<pre>
{
  "id": "math_add_1",
  "kind": "subfrog",
  "ref": "Math.Add",
  "layout": {
    "x": 420,
    "y": 120
  }
}
</pre>

<p>
Rules:
</p>

<ul>
  <li><code>ref</code> MUST exist,</li>
  <li><code>ref</code> MUST match a declared dependency identifier,</li>
  <li>the input and output ports of the node are derived from the referenced FROG interface.</li>
</ul>

<h3>8.4 <code>interface_input</code></h3>

<p>
An <code>interface_input</code> node represents the entry point of a declared public interface input inside the executable graph.
</p>

<pre>
{
  "id": "input_a",
  "kind": "interface_input",
  "interface_port": "a",
  "layout": {
    "x": 40,
    "y": 100
  }
}
</pre>

<p>
Rules:
</p>

<ul>
  <li><code>interface_port</code> MUST exist,</li>
  <li><code>interface_port</code> MUST reference an existing input declared in the <code>interface</code> section.</li>
</ul>

<h3>8.5 <code>interface_output</code></h3>

<p>
An <code>interface_output</code> node represents the exit point used to drive a declared public interface output from the executable graph.
</p>

<pre>
{
  "id": "output_result",
  "kind": "interface_output",
  "interface_port": "result",
  "layout": {
    "x": 760,
    "y": 100
  }
}
</pre>

<p>
Rules:
</p>

<ul>
  <li><code>interface_port</code> MUST exist,</li>
  <li><code>interface_port</code> MUST reference an existing output declared in the <code>interface</code> section.</li>
</ul>

<h3>8.6 <code>widget_value</code></h3>

<p>
A <code>widget_value</code> node represents the primary value participation of a front-panel widget in the executable graph.
It materializes the natural <code>widget.value</code> path defined by <code>Widget.md</code>.
</p>

<pre>
{
  "id": "ctrl_gain_value",
  "kind": "widget_value",
  "widget": "ctrl_gain",
  "layout": {
    "x": 60,
    "y": 220
  }
}
</pre>

<p>
Rules:
</p>

<ul>
  <li><code>widget</code> MUST exist,</li>
  <li><code>widget</code> MUST reference an existing widget anywhere in the recursive front-panel widget tree,</li>
  <li>the referenced widget MUST be value-carrying.</li>
</ul>

<h3>8.7 <code>widget_reference</code></h3>

<p>
A <code>widget_reference</code> node represents an explicit object-style reference to a widget.
It is used when the diagram needs to access widget properties, methods, parts, or other object members beyond the primary value interaction.
</p>

<pre>
{
  "id": "ctrl_gain_ref",
  "kind": "widget_reference",
  "widget": "ctrl_gain",
  "layout": {
    "x": 80,
    "y": 300
  }
}
</pre>

<p>
Rules:
</p>

<ul>
  <li><code>widget</code> MUST exist,</li>
  <li><code>widget</code> MUST reference an existing widget anywhere in the recursive front-panel widget tree.</li>
</ul>

<hr/>

<h2 id="port-resolution-model">9. Port Resolution Model</h2>

<p>
FROG v0.1 does not require every node to declare an explicit <code>ports</code> array inside the diagram source.
Instead, valid ports are resolved from the node kind and its definition source.
</p>

<h3>9.1 Port resolution by node kind</h3>

<ul>
  <li><strong>primitive</strong> — ports are defined by the primitive function signature,</li>
  <li><strong>structure</strong> — ports are defined by the structure family, its boundary, and its outer-visible structure terminals,</li>
  <li><strong>subfrog</strong> — ports are defined by the referenced FROG interface,</li>
  <li><strong>interface_input</strong> — exactly one output port named <code>value</code>,</li>
  <li><strong>interface_output</strong> — exactly one input port named <code>value</code>,</li>
  <li><strong>widget_value</strong> — exactly one port named <code>value</code>, whose direction and type are resolved from the referenced widget role and declared <code>value_type</code>,</li>
  <li><strong>widget_reference</strong> — exactly one output port named <code>ref</code>.</li>
</ul>

<h3>9.2 <code>widget_value</code> port rules</h3>

<p>
The <code>widget_value</code> node always materializes the primary widget value.
</p>

<ul>
  <li>if the referenced widget role is <code>control</code>, the node exposes exactly one <strong>output</strong> port named <code>value</code>,</li>
  <li>if the referenced widget role is <code>indicator</code>, the node exposes exactly one <strong>input</strong> port named <code>value</code>,</li>
  <li>the port type MUST equal the widget <code>value_type</code>,</li>
  <li>widgets that are not value-carrying MUST NOT be referenced by <code>widget_value</code>.</li>
</ul>

<h3>9.3 Primitive port resolution for widget interaction</h3>

<p>
The following standardized primitive families have additional port rules in v0.1:
</p>

<h4>9.3.1 <code>frog.ui.property_read</code></h4>

<ul>
  <li>required input port: <code>ref</code>,</li>
  <li>optional input port: <code>ui_in</code>,</li>
  <li>required output port: <code>value</code>,</li>
  <li>optional output port: <code>ui_out</code>.</li>
</ul>

<p>
The value type is defined by the addressed widget member.
The <code>ref</code> port is an opaque widget reference token.
The optional <code>ui_in</code> and <code>ui_out</code> ports are opaque UI sequencing ports.
</p>

<h4>9.3.2 <code>frog.ui.property_write</code></h4>

<ul>
  <li>required input port: <code>ref</code>,</li>
  <li>required input port: <code>value</code>,</li>
  <li>optional input port: <code>ui_in</code>,</li>
  <li>optional output port: <code>ui_out</code>.</li>
</ul>

<p>
The <code>value</code> port type is defined by the addressed widget member.
The <code>ref</code> port is an opaque widget reference token.
The optional <code>ui_in</code> and <code>ui_out</code> ports are opaque UI sequencing ports.
</p>

<h4>9.3.3 <code>frog.ui.method_invoke</code></h4>

<ul>
  <li>required input port: <code>ref</code>,</li>
  <li>zero or more required or optional method parameter input ports,</li>
  <li>optional input port: <code>ui_in</code>,</li>
  <li>zero or more method return output ports,</li>
  <li>optional output port: <code>ui_out</code>.</li>
</ul>

<p>
Method parameter and return ports are defined by the addressed widget or widget-part method signature.
The <code>ref</code> port is an opaque widget reference token.
The optional <code>ui_in</code> and <code>ui_out</code> ports are opaque UI sequencing ports.
</p>

<h3>9.4 Primitive-local member descriptors</h3>

<p>
Widget interaction primitives carry widget member metadata locally on the primitive node.
In base v0.1, the widget identity itself is carried by the incoming <code>ref</code> edge.
</p>

<p>
Canonical property descriptor:
</p>

<pre>
"widget_member": {
  "member": "visible"
}
</pre>

<p>
Canonical property descriptor for a widget part:
</p>

<pre>
"widget_member": {
  "part": "label",
  "member": "text"
}
</pre>

<p>
Canonical method descriptor:
</p>

<pre>
"widget_method": {
  "name": "focus"
}
</pre>

<h3>9.5 Structure node ports</h3>

<p>
For a <code>structure</code> node, external ports are resolved from:
</p>

<ul>
  <li>the structure <code>boundary.inputs</code>,</li>
  <li>the structure <code>boundary.outputs</code>,</li>
  <li>any outer-visible structure terminals required by the structure family.</li>
</ul>

<p>
This means, for example:
</p>

<ul>
  <li>a boolean <code>case</code> exposes an outer-visible selector terminal and any declared boundary inputs and outputs,</li>
  <li>a string <code>case</code> also exposes an outer-visible selector terminal, but its branch selection is resolved against string-literal matches and a required default region,</li>
  <li>a <code>for_loop</code> exposes its count terminal if the structure family defines it as outer-visible,</li>
  <li>a <code>while_loop</code> does not expose its continuation terminal externally in base v0.1.</li>
</ul>

<h3>9.6 Sub-FROG node ports</h3>

<p>
A <code>subfrog</code> node resolves its ports from the public interface of the referenced FROG.
</p>

<ul>
  <li>each referenced interface input becomes an input port on the node,</li>
  <li>each referenced interface output becomes an output port on the node.</li>
</ul>

<hr/>

<h2 id="edge-model">10. Edge Model</h2>

<p>
An edge represents a directed graph connection from one node port to another node port.
</p>

<h3>10.1 Canonical edge shape</h3>

<pre>
{
  "id": "e1",
  "from": { "node": "input_a", "port": "value" },
  "to": { "node": "add_1", "port": "a" }
}
</pre>

<p>
Rules:
</p>

<ul>
  <li><code>id</code> MUST exist and MUST be unique within the owning diagram scope,</li>
  <li><code>from</code> MUST exist and MUST identify a valid source node and source port,</li>
  <li><code>to</code> MUST exist and MUST identify a valid destination node and destination port.</li>
</ul>

<h3>10.2 Directionality</h3>

<p>
Edges are directional.
They represent value movement or explicit sequencing according to the semantics of the connected ports.
</p>

<ul>
  <li>a source endpoint MUST refer to an output port,</li>
  <li>a destination endpoint MUST refer to an input port.</li>
</ul>

<h3>10.3 Type compatibility</h3>

<p>
The source port type and destination port type MUST be compatible under the active type rules and active profile.
If they are not compatible, validation MUST fail.
</p>

<h3>10.4 Fan-out</h3>

<p>
A source output MAY feed multiple destination inputs unless a stricter profile forbids it.
</p>

<h3>10.5 Multiple writers</h3>

<p>
Multiple distinct source edges MUST NOT drive the same destination input port unless the destination port semantics explicitly allow it under a stricter profile.
Base v0.1 assumes one writer per input port.
</p>

<hr/>

<h2 id="diagram-annotations">11. Diagram Annotations</h2>

<p>
Annotations are source-level documentation and visual organization objects associated with a diagram scope.
They do not affect execution semantics.
</p>

<h3>11.1 Annotation model</h3>

<p>
Each annotation MUST define:
</p>

<ul>
  <li><code>id</code> — unique annotation identifier within the owning diagram scope,</li>
  <li><code>kind</code> — annotation category.</li>
</ul>

<p>
An annotation MAY additionally define:
</p>

<ul>
  <li><code>layout</code>,</li>
  <li><code>text</code>,</li>
  <li><code>targets</code>,</li>
  <li><code>style</code>,</li>
  <li><code>doc</code>,</li>
  <li><code>tags</code>.</li>
</ul>

<h3>11.2 Canonical annotation shape</h3>

<pre>
{
  "id": "ann_1",
  "kind": "comment",
  "text": "Normalize gain before scaling.",
  "layout": {
    "x": 120,
    "y": 40,
    "width": 180,
    "height": 60
  }
}
</pre>

<h3>11.3 Standard annotation kinds for v0.1</h3>

<ul>
  <li><code>free_label</code></li>
  <li><code>comment</code></li>
  <li><code>wire_label</code></li>
  <li><code>region</code></li>
</ul>

<h3>11.4 Free label</h3>

<p>
A <code>free_label</code> is free-standing visible text placed on the diagram.
</p>

<h3>11.5 Comment</h3>

<p>
A <code>comment</code> is a textual annotation that MAY optionally target a node or an edge.
</p>

<h3>11.6 Wire label</h3>

<p>
A <code>wire_label</code> is a textual annotation attached to an edge.
</p>

<h3>11.7 Region</h3>

<p>
A <code>region</code> groups or frames a functional portion of the diagram visually.
It MAY optionally reference nodes.
</p>

<hr/>

<h2 id="documentation-and-tags">12. Documentation and Tags</h2>

<p>
Nodes and annotations MAY contain:
</p>

<ul>
  <li><code>doc</code> — structured documentation metadata,</li>
  <li><code>tags</code> — structured tag strings.</li>
</ul>

<p>
These fields are source-level authoring metadata.
They do not change execution semantics.
</p>

<hr/>

<h2 id="layout-information">13. Layout Information</h2>

<p>
Nodes and annotations MAY contain <code>layout</code> metadata used by graphical editors.
</p>

<p>
Typical layout fields include:
</p>

<ul>
  <li><code>x</code></li>
  <li><code>y</code></li>
  <li><code>width</code></li>
  <li><code>height</code></li>
</ul>

<p>
Layout information belongs to source because diagram readability and editor reconstruction matter.
However, layout MUST NOT alter the executable meaning of the graph.
</p>

<hr/>

<h2 id="frog-dependencies">14. FROG Dependencies</h2>

<p>
When a diagram uses nodes implemented by other FROGs, those FROGs MUST be referenced in <code>dependencies</code>.
</p>

<pre>
"dependencies": [
  {
    "name": "Math.Add",
    "path": "lib/math/add.frog"
  }
]
</pre>

<p>
Dependency fields:
</p>

<ul>
  <li><code>name</code> — logical identifier used by <code>subfrog.ref</code>,</li>
  <li><code>path</code> — relative path or equivalent source reference.</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>dependency names MUST be unique within the diagram,</li>
  <li>each <code>subfrog.ref</code> MUST resolve to an existing dependency name,</li>
  <li>the referenced FROG MUST expose an interface usable to resolve the sub-FROG node ports.</li>
</ul>

<p>
This document does not standardize packaging, search paths, remote resolution, or dependency locking mechanisms.
</p>

<hr/>

<h2 id="subfrog-invocation">15. Sub-FROG Invocation</h2>

<p>
A <code>subfrog</code> node represents reuse of another FROG as a callable executable unit.
</p>

<p>
The invocation contract of a sub-FROG is derived from the referenced FROG interface.
This means:
</p>

<ul>
  <li>the reusable unit behaves like a callable graphical program unit,</li>
  <li>public inputs are consumed through node input ports,</li>
  <li>public outputs are produced through node output ports.</li>
</ul>

<p>
A sub-FROG invocation does not inline or redefine the referenced FROG in source.
It references an external dependency contract.
</p>

<hr/>

<h2 id="interface-widget-and-structure-boundaries">16. Interface, Widget, and Structure Boundaries</h2>

<p>
FROG distinguishes three different kinds of structural boundary participation in the diagram:
</p>

<ul>
  <li><strong>public interface boundary</strong>,</li>
  <li><strong>front-panel widget boundary</strong>,</li>
  <li><strong>structure boundary</strong>.</li>
</ul>

<h3>16.1 Public interface boundary</h3>

<p>
Public interface participation is represented canonically by:
</p>

<ul>
  <li><code>interface_input</code></li>
  <li><code>interface_output</code></li>
</ul>

<p>
These nodes bind the public FROG contract to the executable graph.
</p>

<h3>16.2 Front-panel widget boundary</h3>

<p>
Front-panel primary value participation is represented canonically by:
</p>

<ul>
  <li><code>widget_value</code></li>
</ul>

<p>
Object-style widget interaction is represented canonically by:
</p>

<ul>
  <li><code>widget_reference</code>,</li>
  <li><code>frog.ui.property_read</code>,</li>
  <li><code>frog.ui.property_write</code>,</li>
  <li><code>frog.ui.method_invoke</code>.</li>
</ul>

<p>
A widget MAY expose its primary value both naturally through <code>widget_value</code> and as a property through the object-style path when the widget class allows it.
</p>

<h3>16.3 Structure boundary</h3>

<p>
Structure participation is represented by the structure node itself and by its:
</p>

<ul>
  <li><code>boundary.inputs</code>,</li>
  <li><code>boundary.outputs</code>,</li>
  <li>outer-visible structure terminals.</li>
</ul>

<p>
The structure wall is part of program meaning.
It is not a purely visual editor artifact.
</p>

<hr/>

<h2 id="widget-interaction-model">17. Widget Interaction Model</h2>

<p>
The executable widget interaction model distinguishes the natural primary-value path from object-style widget access.
</p>

<h3>17.1 Natural primary-value path</h3>

<p>
The natural path is:
</p>

<pre>
widget instance → widget primary value → widget_value node → dataflow graph
</pre>

<p>
This path SHOULD be used for ordinary control and indicator wiring.
</p>

<h3>17.2 Object-style path</h3>

<p>
The object-style path is:
</p>

<pre>
widget instance → widget_reference node → frog.ui.* primitive
</pre>

<p>
This path is used for:
</p>

<ul>
  <li>property reads,</li>
  <li>property writes,</li>
  <li>method invocation,</li>
  <li>addressing widget parts.</li>
</ul>

<h3>17.3 UI sequencing ports</h3>

<p>
The optional <code>ui_in</code> and <code>ui_out</code> ports MAY be used to make ordering of UI side effects explicit.
</p>

<p>
These sequencing ports:
</p>

<ul>
  <li>are opaque UI-ordering tokens,</li>
  <li>do not replace ordinary data dependencies,</li>
  <li>SHOULD be used only where explicit UI ordering is needed.</li>
</ul>

<hr/>

<h2 id="cycles-and-local-state">18. Cycles and Local State</h2>

<p>
FROG allows cycles in executable graphs only under the rules defined by <code>Language/State and cycles.md</code>.
</p>

<p>
The base rule of v0.1 is:
</p>

<ul>
  <li>a directed cycle without explicit local state is invalid,</li>
  <li>a directed cycle is valid only if it contains at least one local-state function.</li>
</ul>

<p>
In the standard library, the minimal local-state function for v0.1 is typically <code>frog.core.delay</code>.
This means that the diagram is not restricted to acyclic graphs, but feedback MUST remain explicit, deterministic, and statically verifiable.
</p>

<p>
Cycle validity is therefore part of diagram validation, even though the detailed local-state semantics are defined by the language-level state specification.
A validator MAY implement this rule through strongly connected component analysis or any equivalent graph-theoretic method.
</p>

<hr/>

<h2 id="graph-validation">19. Graph Validation</h2>

<p>
A diagram is valid only if all of the following hold under the active base specification and active profile:
</p>

<ul>
  <li>the <code>diagram</code> section exists,</li>
  <li><code>nodes</code> and <code>edges</code> exist and are arrays,</li>
  <li>every node identifier is unique within its owning diagram scope,</li>
  <li>every edge identifier is unique within its owning diagram scope,</li>
  <li>every annotation identifier is unique within its owning diagram scope,</li>
  <li>every edge source endpoint references an existing node and valid output port,</li>
  <li>every edge destination endpoint references an existing node and valid input port,</li>
  <li>every edge connects type-compatible ports,</li>
  <li>each destination input has at most one source edge in base v0.1,</li>
  <li>each <code>interface_input</code> references an existing declared interface input,</li>
  <li>each <code>interface_output</code> references an existing declared interface output,</li>
  <li>each <code>widget_value</code> references an existing value-carrying widget,</li>
  <li>each <code>widget_reference</code> references an existing widget,</li>
  <li>each <code>subfrog.ref</code> resolves to a declared dependency,</li>
  <li>each structure node is valid under its structure-family rules,</li>
  <li>all reachable directed cycles satisfy the local-state rule,</li>
  <li>the graph remains consistent with the declared public interface contract.</li>
</ul>

<p>
Consistency with the public interface contract includes:
</p>

<ul>
  <li>each declared interface input MUST be consumable by the graph,</li>
  <li>each declared interface output MUST be producible by the graph,</li>
  <li>unbound, contradictory, or unreachable interface boundary definitions MUST trigger validation errors.</li>
</ul>

<hr/>

<h2 id="execution-semantics">20. Execution Semantics</h2>

<p>
The diagram is the authoritative execution graph of the FROG.
</p>

<p>
Programs are not executed directly from raw source text as mere text.
Execution occurs from validated execution-oriented representations derived from the source diagram and the rest of the program model.
</p>

<h3>20.1 Primitive execution</h3>

<p>
A primitive executes according to its primitive definition and its resolved inputs.
</p>

<h3>20.2 Structure execution</h3>

<p>
A structure executes according to its standardized structure family semantics.
</p>

<ul>
  <li>a boolean <code>case</code> executes exactly one of its <code>true</code> or <code>false</code> regions,</li>
  <li>a string <code>case</code> executes exactly one matching string-literal region or its required default region,</li>
  <li>a <code>for_loop</code> executes its body region according to its count terminal,</li>
  <li>a <code>while_loop</code> executes its body region according to its continuation rule.</li>
</ul>

<h3>20.3 Widget participation</h3>

<p>
Widget participation does not weaken the principle that the diagram is authoritative.
</p>

<ul>
  <li><code>widget_value</code> contributes the primary value path of a widget,</li>
  <li><code>widget_reference</code> contributes a reference token for explicit object-style interaction,</li>
  <li><code>frog.ui.*</code> primitives define executable widget-member interaction where supported.</li>
</ul>

<h3>20.4 Determinism</h3>

<p>
Under a validated program and a compatible runtime profile, the observable execution meaning of the diagram MUST remain inspectable and deterministic within the guarantees of that profile.
</p>

<hr/>

<h2 id="examples">21. Examples</h2>

<h3>21.1 Minimal arithmetic diagram</h3>

<pre>
"diagram": {
  "nodes": [
    {
      "id": "input_a",
      "kind": "interface_input",
      "interface_port": "a"
    },
    {
      "id": "input_b",
      "kind": "interface_input",
      "interface_port": "b"
    },
    {
      "id": "add_node",
      "kind": "primitive",
      "type": "frog.core.add"
    },
    {
      "id": "output_result",
      "kind": "interface_output",
      "interface_port": "result"
    }
  ],
  "edges": [
    {
      "id": "e1",
      "from": { "node": "input_a", "port": "value" },
      "to": { "node": "add_node", "port": "a" }
    },
    {
      "id": "e2",
      "from": { "node": "input_b", "port": "value" },
      "to": { "node": "add_node", "port": "b" }
    },
    {
      "id": "e3",
      "from": { "node": "add_node", "port": "result" },
      "to": { "node": "output_result", "port": "value" }
    }
  ]
}
</pre>

<h3>21.2 Diagram using widget primary values</h3>

<pre>
"diagram": {
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
      "to": { "node": "mul_1", "port": "a" }
    },
    {
      "id": "e2",
      "from": { "node": "ctrl_gain_value", "port": "value" },
      "to": { "node": "mul_1", "port": "b" }
    },
    {
      "id": "e3",
      "from": { "node": "mul_1", "port": "result" },
      "to": { "node": "ind_result_value", "port": "value" }
    }
  ]
}
</pre>

<h3>21.3 Diagram reading a widget property</h3>

<pre>
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
      "to": { "node": "read_label_text", "port": "ref" }
    }
  ]
}
</pre>

<h3>21.4 Diagram writing a widget property</h3>

<pre>
"diagram": {
  "nodes": [
    {
      "id": "ctrl_gain_ref",
      "kind": "widget_reference",
      "widget": "ctrl_gain"
    },
    {
      "id": "status_text",
      "kind": "interface_input",
      "interface_port": "status"
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
      "from": { "node": "ctrl_gain_ref", "port": "ref" },
      "to": { "node": "write_label_text", "port": "ref" }
    },
    {
      "id": "e2",
      "from": { "node": "status_text", "port": "value" },
      "to": { "node": "write_label_text", "port": "value" }
    }
  ]
}
</pre>

<h3>21.5 Diagram invoking a widget method</h3>

<pre>
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
      "to": { "node": "invoke_reset", "port": "ref" }
    }
  ]
}
</pre>

<h3>21.6 Boolean case structure</h3>

<pre>
"diagram": {
  "nodes": [
    {
      "id": "case_1",
      "kind": "structure",
      "structure_type": "case",
      "boundary": {
        "inputs": [
          { "id": "x", "type": "f64" }
        ],
        "outputs": [
          { "id": "y", "type": "f64" }
        ]
      },
      "structure_terminals": {
        "selector": {
          "type": "bool",
          "outer_visible": true,
          "exposed_in_body": false,
          "read_only": true,
          "role": "selector"
        }
      },
      "regions": [
        {
          "id": "true_case",
          "match": true,
          "diagram": {
            "nodes": [],
            "edges": []
          }
        },
        {
          "id": "false_case",
          "match": false,
          "diagram": {
            "nodes": [],
            "edges": []
          }
        }
      ]
    }
  ],
  "edges": []
}
</pre>

<h3>21.7 String case structure</h3>

<pre>
"diagram": {
  "nodes": [
    {
      "id": "case_mode",
      "kind": "structure",
      "structure_type": "case",
      "boundary": {
        "inputs": [],
        "outputs": [
          { "id": "status", "type": "string" }
        ]
      },
      "structure_terminals": {
        "selector": {
          "type": "string",
          "outer_visible": true,
          "exposed_in_body": false,
          "read_only": true,
          "role": "selector"
        }
      },
      "regions": [
        {
          "id": "case_start",
          "match": "start",
          "diagram": {
            "nodes": [],
            "edges": []
          }
        },
        {
          "id": "case_stop",
          "match": "stop",
          "diagram": {
            "nodes": [],
            "edges": []
          }
        },
        {
          "id": "default_case",
          "default": true,
          "diagram": {
            "nodes": [],
            "edges": []
          }
        }
      ]
    }
  ],
  "edges": []
}
</pre>

<h3>21.8 Diagram using explicit local state</h3>

<pre>
"diagram": {
  "nodes": [
    {
      "id": "input_x",
      "kind": "interface_input",
      "interface_port": "x"
    },
    {
      "id": "delay_1",
      "kind": "primitive",
      "type": "frog.core.delay",
      "initial": 0.0
    },
    {
      "id": "add_1",
      "kind": "primitive",
      "type": "frog.core.add"
    },
    {
      "id": "output_y",
      "kind": "interface_output",
      "interface_port": "y"
    }
  ],
  "edges": [
    {
      "id": "e1",
      "from": { "node": "input_x", "port": "value" },
      "to": { "node": "add_1", "port": "a" }
    },
    {
      "id": "e2",
      "from": { "node": "delay_1", "port": "out" },
      "to": { "node": "add_1", "port": "b" }
    },
    {
      "id": "e3",
      "from": { "node": "add_1", "port": "result" },
      "to": { "node": "delay_1", "port": "in" }
    },
    {
      "id": "e4",
      "from": { "node": "add_1", "port": "result" },
      "to": { "node": "output_y", "port": "value" }
    }
  ]
}
</pre>

<hr/>

<h2 id="summary">22. Summary</h2>

<p>
The <code>diagram</code> section is the authoritative executable graph of a FROG.
</p>

<ul>
  <li>It contains nodes, edges, optional dependencies, and optional annotations.</li>
  <li>It defines how interface ports participate in execution through <code>interface_input</code> and <code>interface_output</code>.</li>
  <li>It defines how widgets participate through <code>widget_value</code> and <code>widget_reference</code>.</li>
  <li>It supports standardized structure nodes such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>.</li>
  <li>It supports recursive nested scopes through structure-owned regions.</li>
  <li>It validates type-safe directed connectivity and explicit local-state feedback.</li>
  <li>It remains distinct from UI layout, public interface definition, and primitive-library ownership.</li>
</ul>

<p>
This provides a durable and explicit structural foundation for executable graphical programs in FROG.
</p>
