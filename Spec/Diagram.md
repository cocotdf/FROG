<h1 align="center">🐸 FROG Diagram Specification</h1>

<p align="center">
Definition of executable graphs in <strong>.frog</strong> programs<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#purpose">2. Purpose of the Diagram</a></li>
  <li><a href="#location">3. Location in a <code>.frog</code> File</a></li>
  <li><a href="#structure">4. Diagram Structure</a></li>
  <li><a href="#node-model">5. Node Model</a></li>
  <li><a href="#standard-node-kinds">6. Standard Node Kinds for v0.1</a></li>
  <li><a href="#port-resolution-model">7. Port Resolution Model</a></li>
  <li><a href="#edge-model">8. Edge Model</a></li>
  <li><a href="#diagram-annotations">9. Diagram Annotations</a></li>
  <li><a href="#documentation-and-tags">10. Documentation and Tags</a></li>
  <li><a href="#layout-information">11. Layout Information</a></li>
  <li><a href="#frog-dependencies">12. Frog Dependencies</a></li>
  <li><a href="#subfrog-invocation">13. Sub-Frog Invocation</a></li>
  <li><a href="#interface-and-widget-boundaries">14. Interface and Widget Boundary Nodes</a></li>
  <li><a href="#widget-interaction-model">15. Widget Interaction Model</a></li>
  <li><a href="#graph-validation">16. Graph Validation</a></li>
  <li><a href="#execution-semantics">17. Execution Semantics</a></li>
  <li><a href="#examples">18. Examples</a></li>
  <li><a href="#summary">19. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <strong>diagram</strong> section defines the executable dataflow graph of a FROG.
</p>

<p>
It contains:
</p>

<ul>
  <li>the nodes representing computation or other executable behavior,</li>
  <li>the edges representing directed data connections between nodes,</li>
  <li>the structural links between the public interface, the internal graph, and front panel widget participation,</li>
  <li>the source-level annotations used to document and organize the graph.</li>
</ul>

<p>
Execution semantics are derived from the validated graph together with the public interface contract,
the FROG type system,
the standardized widget model,
the widget interaction model,
and any active primitive catalog or stricter execution profile.
</p>

<hr/>

<h2 id="purpose">2. Purpose of the Diagram</h2>

<p>
The diagram provides:
</p>

<ul>
  <li>the executable logic of the FROG,</li>
  <li>the complete data dependency graph,</li>
  <li>the structural link between the public interface and internal execution logic,</li>
  <li>the hierarchical composition mechanism used to invoke other FROGs,</li>
  <li>the place where front panel widget values participate naturally in dataflow,</li>
  <li>the place where widget references, property access, method invocation, and explicit UI sequencing may participate in execution,</li>
  <li>the canonical source-level space for diagram annotations and documentation.</li>
</ul>

<p>
Nodes represent computation, interface boundaries, widget-related interaction points,
reusable sub-FROG invocations, or other standardized primitive behavior.
Edges represent directional data flow.
Annotations represent source documentation and visual organization only.
</p>

<hr/>

<h2 id="location">3. Location in a <code>.frog</code> File</h2>

<p>
The diagram appears as a top-level object in the canonical <code>.frog</code> source file.
</p>

<pre><code>{
  "spec_version": "0.1",
  "metadata": {},
  "interface": {},
  "connector": {},
  "diagram": {},
  "front_panel": {}
}</code></pre>

<p>
The <code>diagram</code> section <strong>MUST</strong> exist in a canonical <code>.frog</code> source file.
</p>

<hr/>

<h2 id="structure">4. Diagram Structure</h2>

<p>
The diagram object contains up to four fields:
</p>

<pre><code>"diagram": {
  "nodes": [],
  "edges": [],
  "dependencies": [],
  "annotations": []
}</code></pre>

<p>
Fields:
</p>

<ul>
  <li><strong>nodes</strong> — required array of graph nodes</li>
  <li><strong>edges</strong> — required array of directed data connections</li>
  <li><strong>dependencies</strong> — optional array of referenced external FROGs</li>
  <li><strong>annotations</strong> — optional array of visible diagram annotations</li>
</ul>

<p>
The <code>nodes</code> and <code>edges</code> arrays <strong>MUST</strong> exist, even if one of them is empty.
The <code>dependencies</code> and <code>annotations</code> fields MAY be omitted when unused.
</p>

<p>
The <code>annotations</code> field belongs to canonical source because it describes author-created documentation and visual organization of the diagram.
It does not affect execution semantics.
</p>

<hr/>

<h2 id="node-model">5. Node Model</h2>

<p>
A node represents an executable or structurally meaningful element of the graph.
</p>

<p>
Every node <strong>MUST</strong> define:
</p>

<ul>
  <li><strong>id</strong> — unique node identifier</li>
  <li><strong>kind</strong> — node category</li>
</ul>

<p>
A node MAY also define:
</p>

<ul>
  <li><strong>layout</strong> — graphical editor position</li>
  <li><strong>doc</strong> — optional structured documentation</li>
  <li><strong>tags</strong> — optional structured tags</li>
  <li>kind-specific fields defined below</li>
</ul>

<h3>5.1 Common node shape</h3>

<pre><code>{
  "id": "node_1",
  "kind": "primitive",
  "type": "Add",
  "layout": {
    "x": 120,
    "y": 80
  }
}</code></pre>

<p>
Nodes are structural objects.
Their valid ports are resolved from their kind and from the metadata required by that kind.
</p>

<hr/>

<h2 id="standard-node-kinds">6. Standard Node Kinds for v0.1</h2>

<p>
FROG v0.1 defines the following standard node kinds:
</p>

<ul>
  <li><code>primitive</code></li>
  <li><code>subfrog</code></li>
  <li><code>interface_input</code></li>
  <li><code>interface_output</code></li>
  <li><code>widget_value</code></li>
  <li><code>widget_reference</code></li>
</ul>

<h3>6.1 <code>primitive</code></h3>

<p>
A <code>primitive</code> node represents a built-in or profile-defined operation.
</p>

<pre><code>{
  "id": "add_1",
  "kind": "primitive",
  "type": "Add",
  "layout": {
    "x": 240,
    "y": 120
  }
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>type</code> <strong>MUST</strong> exist and identify the primitive operation.</li>
  <li>The meaning and port signature of the primitive are defined by the active profile, standard library, or primitive catalog.</li>
</ul>

<p>
Primitive nodes include ordinary computational primitives such as arithmetic operations,
but may also include widget interaction primitives such as property access or method invocation.
</p>

<h3>6.2 <code>subfrog</code></h3>

<p>
A <code>subfrog</code> node represents an invocation of another FROG.
</p>

<pre><code>{
  "id": "math_add_1",
  "kind": "subfrog",
  "ref": "Math.Add",
  "layout": {
    "x": 420,
    "y": 120
  }
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>ref</code> <strong>MUST</strong> exist.</li>
  <li><code>ref</code> <strong>MUST</strong> match a declared dependency identifier.</li>
  <li>The input and output ports of the node are derived from the referenced FROG interface.</li>
</ul>

<h3>6.3 <code>interface_input</code></h3>

<p>
An <code>interface_input</code> node represents the entry point of a declared public interface input inside the executable graph.
</p>

<pre><code>{
  "id": "input_a",
  "kind": "interface_input",
  "interface_port": "a",
  "layout": {
    "x": 40,
    "y": 100
  }
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>interface_port</code> <strong>MUST</strong> exist.</li>
  <li><code>interface_port</code> <strong>MUST</strong> reference an existing input declared in the <code>interface</code> section.</li>
</ul>

<h3>6.4 <code>interface_output</code></h3>

<p>
An <code>interface_output</code> node represents the exit point used to drive a declared public interface output from the executable graph.
</p>

<pre><code>{
  "id": "output_result",
  "kind": "interface_output",
  "interface_port": "result",
  "layout": {
    "x": 760,
    "y": 100
  }
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>interface_port</code> <strong>MUST</strong> exist.</li>
  <li><code>interface_port</code> <strong>MUST</strong> reference an existing output declared in the <code>interface</code> section.</li>
</ul>

<h3>6.5 <code>widget_value</code></h3>

<p>
A <code>widget_value</code> node represents the primary value participation of a front panel widget in the executable graph.
It materializes the implicit <code>widget.value</code> terminal defined by <code>Widget.md</code>.
</p>

<pre><code>{
  "id": "ctrl_gain_value",
  "kind": "widget_value",
  "widget": "ctrl_gain",
  "layout": {
    "x": 60,
    "y": 220
  }
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>widget</code> <strong>MUST</strong> exist.</li>
  <li><code>widget</code> <strong>MUST</strong> reference an existing widget in <code>front_panel.widgets</code>.</li>
  <li>The referenced widget <strong>MUST</strong> be value-carrying.</li>
</ul>

<h3>6.6 <code>widget_reference</code></h3>

<p>
A <code>widget_reference</code> node represents an explicit object-style reference to a widget.
It is used when the diagram needs to access widget properties, methods, parts, or other object members beyond the primary value interaction.
</p>

<pre><code>{
  "id": "ctrl_gain_ref",
  "kind": "widget_reference",
  "widget": "ctrl_gain",
  "layout": {
    "x": 80,
    "y": 300
  }
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>widget</code> <strong>MUST</strong> exist.</li>
  <li><code>widget</code> <strong>MUST</strong> reference an existing widget in <code>front_panel.widgets</code>.</li>
</ul>

<hr/>

<h2 id="port-resolution-model">7. Port Resolution Model</h2>

<p>
FROG v0.1 does not require every node to declare an explicit <code>ports</code> array inside the diagram source.
Instead, valid ports are resolved from the node kind and its definition source.
</p>

<h3>7.1 Port resolution by node kind</h3>

<ul>
  <li><strong>primitive</strong> — ports are defined by the primitive operation signature.</li>
  <li><strong>subfrog</strong> — ports are defined by the referenced FROG interface.</li>
  <li><strong>interface_input</strong> — exactly one output port named <code>value</code>.</li>
  <li><strong>interface_output</strong> — exactly one input port named <code>value</code>.</li>
  <li><strong>widget_value</strong> — port direction and type are resolved from the referenced widget role and value type.</li>
  <li><strong>widget_reference</strong> — exactly one output port named <code>ref</code>.</li>
</ul>

<h3>7.2 Primitive node ports</h3>

<p>
For a <code>primitive</code> node, port names, directions, arity, and types are defined by the active primitive catalog or profile.
</p>

<p>
However, the following widget interaction primitive families are standardized conceptually in v0.1:
</p>

<ul>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
</ul>

<p>
Their signatures MUST be interpreted consistently with <code>Widget interaction.md</code>.
</p>

<h3>7.3 Standard widget interaction primitive signatures</h3>

<p>
The following signatures apply in the base v0.1 model:
</p>

<h4>7.3.1 <code>frog.ui.property_read</code></h4>

<ul>
  <li>required input port: <code>ref</code></li>
  <li>optional input port: <code>ui_in</code></li>
  <li>required output port: <code>value</code></li>
  <li>optional output port: <code>ui_out</code></li>
</ul>

<p>
The <code>value</code> output type is the type of the addressed property.
The <code>ref</code> port is an opaque widget reference token.
The optional <code>ui_in</code> and <code>ui_out</code> ports are opaque UI sequencing ports.
</p>

<h4>7.3.2 <code>frog.ui.property_write</code></h4>

<ul>
  <li>required input port: <code>ref</code></li>
  <li>required input port: <code>value</code></li>
  <li>optional input port: <code>ui_in</code></li>
  <li>optional output port: <code>ui_out</code></li>
</ul>

<p>
The <code>value</code> input type is the type of the addressed property.
The <code>ref</code> port is an opaque widget reference token.
The optional <code>ui_in</code> and <code>ui_out</code> ports are opaque UI sequencing ports.
</p>

<h4>7.3.3 <code>frog.ui.method_invoke</code></h4>

<ul>
  <li>required input port: <code>ref</code></li>
  <li>zero or more required or optional method parameter input ports</li>
  <li>optional input port: <code>ui_in</code></li>
  <li>zero or more method return output ports</li>
  <li>optional output port: <code>ui_out</code></li>
</ul>

<p>
Method parameter and return ports are defined by the addressed widget or widget-part method signature.
The <code>ref</code> port is an opaque widget reference token.
The optional <code>ui_in</code> and <code>ui_out</code> ports are opaque UI sequencing ports.
</p>

<h3>7.4 Sub-FROG node ports</h3>

<p>
For a <code>subfrog</code> node:
</p>

<ul>
  <li>every referenced FROG input becomes an input port of the node using the same interface port identifier,</li>
  <li>every referenced FROG output becomes an output port of the node using the same interface port identifier.</li>
</ul>

<p>
The types of these ports are exactly the types declared by the referenced FROG interface.
</p>

<h3>7.5 Interface boundary node ports</h3>

<p>
For interface boundary nodes, the following fixed port model applies:
</p>

<ul>
  <li><code>interface_input</code> exposes one output port named <code>value</code>,</li>
  <li><code>interface_output</code> exposes one input port named <code>value</code>.</li>
</ul>

<p>
The type of that <code>value</code> port is the type of the referenced interface port.
</p>

<h3>7.6 Widget value node ports</h3>

<p>
For a <code>widget_value</code> node:
</p>

<ul>
  <li>if the referenced widget role is <code>control</code>, the node exposes one output port named <code>value</code>,</li>
  <li>if the referenced widget role is <code>indicator</code>, the node exposes one input port named <code>value</code>.</li>
</ul>

<p>
The type of the <code>value</code> port is the widget <code>value_type</code>.
</p>

<p>
For v0.1, standard <code>container</code> and <code>decoration</code> widgets are not value-carrying
and therefore cannot be used by <code>widget_value</code> nodes.
</p>

<h3>7.7 Widget reference node ports</h3>

<p>
A <code>widget_reference</code> node exposes exactly one output port named <code>ref</code>.
</p>

<p>
This port represents an opaque widget reference token suitable for widget interaction primitives.
It is not a general-purpose user-visible data value in v0.1.
</p>

<h3>7.8 UI sequencing ports</h3>

<p>
The optional <code>ui_in</code> and <code>ui_out</code> ports used by widget interaction primitives are opaque sequencing ports.
</p>

<p>
They do not represent ordinary user-level FROG data values.
They exist only to express explicit ordering constraints between UI interactions.
</p>

<h3>7.9 Port validation consequence</h3>

<p>
Any edge endpoint referencing a node port is valid only if that port exists after resolution under the rules above.
</p>

<hr/>

<h2 id="edge-model">8. Edge Model</h2>

<p>
Edges define directional connections between node ports.
</p>

<pre><code>{
  "id": "edge_1",
  "from": {
    "node": "node_1",
    "port": "result"
  },
  "to": {
    "node": "node_2",
    "port": "a"
  }
}</code></pre>

<p>
Fields:
</p>

<ul>
  <li><strong>id</strong> — unique edge identifier</li>
  <li><strong>from</strong> — source node and source output port</li>
  <li><strong>to</strong> — destination node and destination input port</li>
</ul>

<p>
An edge MAY also define:
</p>

<ul>
  <li><strong>doc</strong> — optional structured documentation</li>
  <li><strong>tags</strong> — optional structured tags</li>
</ul>

<p>
Edges represent directional graph connectivity and <strong>MUST</strong> respect resolved port direction.
</p>

<p>
Most edges represent ordinary data flow.
Some edges may represent UI sequencing flow when they connect <code>ui_out</code> to <code>ui_in</code>.
</p>

<p>
A valid edge endpoint object has the following form:
</p>

<pre><code>{
  "node": "some_node_id",
  "port": "some_port_name"
}</code></pre>

<h3>8.1 Ordinary data edges</h3>

<p>
Ordinary data edges connect ordinary typed value ports.
They obey standard type compatibility rules from <code>Type.md</code>.
</p>

<h3>8.2 UI sequencing edges</h3>

<p>
A UI sequencing edge connects:
</p>

<ul>
  <li>an output port named <code>ui_out</code></li>
  <li>to an input port named <code>ui_in</code></li>
</ul>

<p>
Such an edge expresses ordering only.
It does not represent an ordinary user-level data value.
</p>

<hr/>

<h2 id="diagram-annotations">9. Diagram Annotations</h2>

<p>
The <code>annotations</code> array contains visible, non-executable source annotations created by the author to document, organize, or label the diagram.
</p>

<p>
Annotations are part of the canonical expression when they represent intended source documentation.
They <strong>MUST NOT</strong> alter execution semantics.
</p>

<h3>9.1 Purpose of annotations</h3>

<p>
Annotations may be used for:
</p>

<ul>
  <li>free labels,</li>
  <li>attached comments,</li>
  <li>wire labels,</li>
  <li>functional regions or framed sections,</li>
  <li>other visible note forms standardized by an active profile.</li>
</ul>

<h3>9.2 Annotation structure</h3>

<p>
Recommended annotation shape:
</p>

<pre><code>{
  "id": "ann_1",
  "kind": "free_label",
  "text": "Initialization",
  "layout": {
    "x": 20,
    "y": 20,
    "width": 140,
    "height": 24
  }
}</code></pre>

<p>
Common annotation fields:
</p>

<ul>
  <li><code>id</code> — unique annotation identifier</li>
  <li><code>kind</code> — annotation category</li>
  <li><code>text</code> — annotation text when applicable</li>
  <li><code>layout</code> — visible placement and size when applicable</li>
  <li><code>target</code> — optional attachment to a node or edge</li>
  <li><code>targets</code> — optional grouped target collection</li>
  <li><code>style_ref</code> — optional style reference</li>
  <li><code>doc</code> — optional structured documentation</li>
  <li><code>tags</code> — optional structured tags</li>
</ul>

<h3>9.3 Standard annotation kinds for v0.1</h3>

<ul>
  <li><code>free_label</code></li>
  <li><code>comment</code></li>
  <li><code>wire_label</code></li>
  <li><code>region</code></li>
</ul>

<h3>9.4 Free label</h3>

<p>
A <code>free_label</code> is free-standing visible text placed on the diagram.
</p>

<h3>9.5 Comment</h3>

<p>
A <code>comment</code> is a textual annotation that may optionally target a node or an edge.
</p>

<h3>9.6 Wire label</h3>

<p>
A <code>wire_label</code> is a textual annotation attached to an edge.
</p>

<h3>9.7 Region</h3>

<p>
A <code>region</code> groups or frames a functional portion of the diagram visually.
It may optionally reference nodes.
</p>

<h3>9.8 Annotation targets</h3>

<p>
When <code>target</code> is present, it SHOULD follow one of these forms:
</p>

<ul>
  <li><code>{ "scope": "node", "id": "node_id" }</code></li>
  <li><code>{ "scope": "edge", "id": "edge_id" }</code></li>
</ul>

<h3>9.9 Execution neutrality</h3>

<p>
Annotations are source documentation and visual structure only.
They <strong>MUST NOT</strong> alter:
</p>

<ul>
  <li>node behavior,</li>
  <li>edge behavior,</li>
  <li>scheduling,</li>
  <li>type compatibility,</li>
  <li>the public interface contract.</li>
</ul>

<hr/>

<h2 id="documentation-and-tags">10. Documentation and Tags</h2>

<p>
FROG v0.1 distinguishes between:
</p>

<ul>
  <li><strong>visible annotations</strong> stored in <code>diagram.annotations</code>,</li>
  <li><strong>structured documentation</strong> attached directly to nodes, edges, or annotations,</li>
  <li><strong>editor-only navigation state</strong> that belongs to IDE-specific data rather than the canonical diagram expression.</li>
</ul>

<h3>10.1 Structured documentation</h3>

<p>
A node, edge, or annotation MAY define a <code>doc</code> object.
</p>

<p>
Recommended shape:
</p>

<pre><code>"doc": {
  "summary": "Short human-readable summary",
  "description": "Longer structured explanation."
}</code></pre>

<h3>10.2 Structured tags</h3>

<p>
A node, edge, or annotation MAY define a <code>tags</code> array.
</p>

<pre><code>"tags": ["todo", "warning", "performance"]</code></pre>

<p>
This document does not impose a closed vocabulary for tags in v0.1.
</p>

<h3>10.3 Source documentation vs IDE-only state</h3>

<p>
The following belong in canonical source when author-intended:
</p>

<ul>
  <li>free labels,</li>
  <li>comments,</li>
  <li>wire labels,</li>
  <li>regions,</li>
  <li>structured documentation,</li>
  <li>structured tags.</li>
</ul>

<p>
The following do <strong>not</strong> belong in the canonical diagram source and should instead belong to IDE-specific data such as <code>ide</code>:
</p>

<ul>
  <li>bookmarks used only for navigation,</li>
  <li>viewport position,</li>
  <li>zoom state,</li>
  <li>temporary selection state,</li>
  <li>other editor-session-only navigation metadata.</li>
</ul>

<hr/>

<h2 id="layout-information">11. Layout Information</h2>

<p>
Nodes and annotations MAY include layout information for graphical editors.
</p>

<pre><code>"layout": {
  "x": 240,
  "y": 120
}</code></pre>

<p>
Typical layout fields may include:
</p>

<ul>
  <li><code>x</code></li>
  <li><code>y</code></li>
  <li><code>width</code></li>
  <li><code>height</code></li>
  <li><code>z</code> when needed by a stricter profile</li>
</ul>

<p>
Layout information is optional and affects graphical rendering only.
It <strong>MUST NOT</strong> influence execution semantics, scheduling, typing, or dataflow behavior.
</p>

<hr/>

<h2 id="frog-dependencies">12. Frog Dependencies</h2>

<p>
When a diagram uses nodes implemented by other FROGs, those FROGs <strong>MUST</strong> be referenced in <code>dependencies</code>.
</p>

<pre><code>"dependencies": [
  {
    "name": "Math.Add",
    "path": "lib/math/add.frog"
  }
]</code></pre>

<p>
Dependency fields:
</p>

<ul>
  <li><strong>name</strong> — logical identifier used by <code>subfrog.ref</code></li>
  <li><strong>path</strong> — relative path or equivalent source reference</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>Dependency names <strong>MUST</strong> be unique within the diagram.</li>
  <li>Each <code>subfrog.ref</code> <strong>MUST</strong> resolve to an existing dependency name.</li>
  <li>The referenced FROG <strong>MUST</strong> expose an interface usable to resolve the sub-FROG node ports.</li>
</ul>

<p>
This document does not standardize packaging, search paths, remote resolution, or dependency locking mechanisms.
</p>

<hr/>

<h2 id="subfrog-invocation">13. Sub-Frog Invocation</h2>

<p>
Sub-FROG invocation enables hierarchical program composition.
A sub-FROG behaves as a reusable node whose public ports are derived from the referenced FROG interface.
</p>

<p>
Conceptually:
</p>

<ul>
  <li>the invoked FROG interface defines the node contract,</li>
  <li>the connector, if any, only affects graphical presentation when reused in tools,</li>
  <li>execution semantics depend on the referenced FROG program, not on its connector or icon.</li>
</ul>

<hr/>

<h2 id="interface-and-widget-boundaries">14. Interface and Widget Boundary Nodes</h2>

<p>
The executable graph <strong>MUST</strong> be consistent with the public interface declared in the <code>interface</code> section
and with the widget model declared in the <code>front_panel</code> section.
</p>

<p>
In v0.1:
</p>

<ul>
  <li>public interface participation is expressed through <code>interface_input</code> and <code>interface_output</code> nodes,</li>
  <li>front panel primary value participation is expressed through <code>widget_value</code> nodes,</li>
  <li>richer front panel object interaction is expressed through <code>widget_reference</code> nodes combined with widget interaction primitives.</li>
</ul>

<p>
Conceptually:
</p>

<pre><code>external input   → interface_input.value   → internal graph
internal graph   → interface_output.value  → external output
control widget   → widget_value.value      → internal graph
internal graph   → widget_value.value      → indicator widget</code></pre>

<p>
The interface defines the public contract.
The front panel defines the UI composition.
The diagram is where both become structurally connected to executable logic.
</p>

<hr/>

<h2 id="widget-interaction-model">15. Widget Interaction Model</h2>

<p>
FROG distinguishes two interaction paths for widgets:
</p>

<ul>
  <li><strong>primary value interaction</strong> — handled through <code>widget_value</code> nodes,</li>
  <li><strong>object-style interaction</strong> — handled through <code>widget_reference</code> nodes and widget interaction primitives.</li>
</ul>

<h3>15.1 Primary value interaction</h3>

<p>
Primary value interaction uses the implicit <code>widget.value</code> terminal materialized by <code>widget_value</code>.
This is the normal path for dataflow wiring of controls and indicators.
</p>

<h3>15.2 Object-style interaction</h3>

<p>
Object-style interaction is used when the diagram needs to:
</p>

<ul>
  <li>read a property, including optionally <code>value</code>,</li>
  <li>write a property, including optionally <code>value</code>,</li>
  <li>invoke a widget or widget-part method,</li>
  <li>address a widget part such as <code>label</code>,</li>
  <li>introduce explicit sequencing constraints between UI side effects.</li>
</ul>

<p>
This path requires a <code>widget_reference</code> node.
</p>

<h3>15.3 Widget interaction primitive families</h3>

<p>
The base v0.1 model recognizes the following primitive families:
</p>

<ul>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
</ul>

<p>
These primitives remain ordinary <code>primitive</code> nodes.
They are validated using:
</p>

<ul>
  <li>their standardized signature,</li>
  <li>the referenced widget class,</li>
  <li>the addressed widget part when present,</li>
  <li>the property or method being addressed.</li>
</ul>

<h3>15.4 Member descriptors</h3>

<p>
A widget interaction primitive MAY declare a property target description such as:
</p>

<pre><code>{
  "widget_member": {
    "member": "visible"
  }
}</code></pre>

<p>
or, for a widget part:
</p>

<pre><code>{
  "widget_member": {
    "part": "label",
    "member": "text"
  }
}</code></pre>

<p>
A method target description MAY use:
</p>

<pre><code>{
  "widget_method": {
    "name": "focus"
  }
}</code></pre>

<p>
or, for a widget part method:
</p>

<pre><code>{
  "widget_method": {
    "part": "label",
    "name": "show"
  }
}</code></pre>

<p>
The exact field naming MAY be profile-defined,
but the addressed member <strong>MUST</strong> be valid for the widget or addressed widget part.
</p>

<h3>15.5 Special status of <code>value</code></h3>

<p>
The primary widget value has special status.
Using <code>frog.ui.property_read</code> or <code>frog.ui.property_write</code> on <code>member = "value"</code> is valid in the base model.
</p>

<p>
However, when a <code>widget_value</code> node can express the same intent more directly,
tools SHOULD prefer <code>widget_value</code> for ordinary primary value wiring
and MAY warn when value interaction is modeled indirectly through property primitives.
</p>

<h3>15.6 UI sequencing</h3>

<p>
Widget interaction primitives MAY use the optional <code>ui_in</code> and <code>ui_out</code> ports
to form explicit ordering chains between UI side effects or UI observations.
</p>

<p>
Conceptually:
</p>

<pre><code>A.ui_out → B.ui_in</code></pre>

<p>
means that <code>B</code> cannot perform its UI-visible action or observation before <code>A</code> has completed according to the semantics of the corresponding primitive.
</p>

<hr/>

<h2 id="graph-validation">16. Graph Validation</h2>

<p>
Implementations <strong>MUST</strong> enforce the following rules:
</p>

<ul>
  <li>the <code>diagram</code> section <strong>MUST</strong> exist,</li>
  <li><code>nodes</code> and <code>edges</code> <strong>MUST</strong> exist and <strong>MUST</strong> be arrays,</li>
  <li>node identifiers <strong>MUST</strong> be unique within the diagram,</li>
  <li>edge identifiers <strong>MUST</strong> be unique within the diagram,</li>
  <li>every edge endpoint <strong>MUST</strong> reference an existing node,</li>
  <li>every referenced port <strong>MUST</strong> exist after port resolution,</li>
  <li>edge direction <strong>MUST</strong> match the direction of the referenced ports,</li>
  <li>connected ordinary value ports <strong>MUST</strong> be type-compatible according to <code>Type.md</code>,</li>
  <li>every <code>interface_input</code> node <strong>MUST</strong> reference an existing interface input,</li>
  <li>every <code>interface_output</code> node <strong>MUST</strong> reference an existing interface output,</li>
  <li>every <code>subfrog.ref</code> <strong>MUST</strong> resolve to a declared dependency,</li>
  <li>the diagram <strong>MUST</strong> remain consistent with the interface contract.</li>
</ul>

<p>
Additional widget-related rules:
</p>

<ul>
  <li>every <code>widget_value.widget</code> <strong>MUST</strong> reference an existing widget,</li>
  <li>the referenced widget of a <code>widget_value</code> node <strong>MUST</strong> be value-carrying,</li>
  <li>every <code>widget_reference.widget</code> <strong>MUST</strong> reference an existing widget,</li>
  <li>the resolved direction of a <code>widget_value</code> node <strong>MUST</strong> be compatible with the referenced widget role,</li>
  <li>widget interaction primitives <strong>MUST</strong> receive a valid widget reference on their <code>ref</code> input unless a stricter profile defines an alternative mechanism,</li>
  <li>widget interaction primitives <strong>MUST</strong> address valid widget members or valid widget-part members,</li>
  <li>widget interaction primitives <strong>MUST</strong> be compatible with the referenced widget class and addressed member kind,</li>
  <li>the resolved widget interaction ordinary value ports <strong>MUST</strong> remain type-compatible with connected edges.</li>
</ul>

<p>
Additional sequencing-related rules:
</p>

<ul>
  <li>if connected, <code>ui_in</code> <strong>MUST</strong> receive a valid UI sequencing edge,</li>
  <li>if connected, <code>ui_out</code> <strong>MUST</strong> connect only to compatible <code>ui_in</code> ports,</li>
  <li>ordinary value ports <strong>MUST NOT</strong> connect to <code>ui_in</code> or <code>ui_out</code>,</li>
  <li>multiple non-sequenced widget mutations that may conflict on the same widget member MAY trigger tool warnings,</li>
  <li>mixing <code>widget_value</code> and <code>property_write(value)</code> on the same widget without explicit sequencing MAY trigger tool warnings.</li>
</ul>

<p>
Interface consistency rules:
</p>

<ul>
  <li>each declared interface input <strong>MUST</strong> be consumable by the graph,</li>
  <li>each declared interface output <strong>MUST</strong> be producible by the graph,</li>
  <li>unbound, contradictory, or unreachable interface boundary definitions <strong>MUST</strong> trigger validation errors.</li>
</ul>

<p>
For annotations and source documentation:
</p>

<ul>
  <li>if present, <code>annotations</code> <strong>MUST</strong> be an array,</li>
  <li>annotation identifiers <strong>MUST</strong> be unique within the diagram,</li>
  <li>annotation targets <strong>MUST</strong> reference existing nodes or edges when specified,</li>
  <li><code>doc</code> fields <strong>MUST</strong> be objects when present,</li>
  <li><code>tags</code> fields <strong>MUST</strong> be arrays of strings when present,</li>
  <li>annotations <strong>MUST NOT</strong> be interpreted as executable nodes or executable edges.</li>
</ul>

<p>
Unknown node or annotation properties MAY be ignored unless a stricter active profile defines them.
</p>

<hr/>

<h2 id="execution-semantics">17. Execution Semantics</h2>

<p>
Execution follows a dataflow model.
</p>

<ul>
  <li>A node becomes executable when all required ordinary value inputs are available.</li>
  <li>Execution order derives from data dependencies, not from source ordering.</li>
  <li>Independent nodes MAY execute in parallel.</li>
</ul>

<p>
The diagram is the authoritative structural definition of execution logic inside a FROG.
However, the graph <strong>MUST</strong> be interpreted together with:
</p>

<ul>
  <li>the public interface contract,</li>
  <li>the type system and implicit coercion rules,</li>
  <li>the primitive and sub-FROG operation definitions available in the active execution profile,</li>
  <li>the widget model for any widget-related nodes or widget interaction primitives.</li>
</ul>

<p>
Layout, connector placement, icon content, IDE preferences, cache data, annotations, structured documentation, and structured tags <strong>MUST NOT</strong> alter execution semantics.
</p>

<p>
When widget-related nodes are present:
</p>

<ul>
  <li><code>widget_value</code> nodes participate in dataflow as ordinary validated nodes,</li>
  <li><code>widget_reference</code> nodes expose object-style interaction handles,</li>
  <li>widget interaction primitives remain ordinary executable nodes,</li>
  <li>none of these redefine the public interface contract.</li>
</ul>

<h3>17.1 Unsequenced UI interaction</h3>

<p>
If <code>ui_in</code> and <code>ui_out</code> are not used,
a widget interaction primitive executes when its required ordinary inputs are available,
including <code>ref</code> and any required ordinary value inputs.
</p>

<p>
In that case, the relative ordering between independent UI interactions is not guaranteed
unless already implied by ordinary dataflow dependencies.
</p>

<h3>17.2 Sequenced UI interaction</h3>

<p>
If <code>ui_in</code> and <code>ui_out</code> are used to form a sequencing chain,
then execution order along that chain is guaranteed.
</p>

<p>
Conceptually:
</p>

<pre><code>A.ui_out → B.ui_in</code></pre>

<p>
means that <code>B</code> cannot perform its UI-visible effect or UI-visible observation before <code>A</code> has completed according to the semantics of the corresponding primitive.
</p>

<h3>17.3 Observable sequencing guarantees</h3>

<ul>
  <li>a sequenced property read observes widget state after prior sequenced UI interactions in the same chain,</li>
  <li>a sequenced property write produces <code>ui_out</code> only after the mutation has been applied,</li>
  <li>a sequenced method invoke produces <code>ui_out</code> only after the method action has been applied and any method return values are stable.</li>
</ul>

<p>
This keeps:
</p>

<ul>
  <li>the front panel as the UI layer,</li>
  <li>the interface as the public contract,</li>
  <li>the diagram as the single authoritative place where execution structure is wired.</li>
</ul>

<hr/>

<h2 id="examples">18. Examples</h2>

<h3>18.1 Minimal arithmetic diagram</h3>

<pre><code>"diagram": {
  "dependencies": [
    {
      "name": "Math.Add",
      "path": "lib/math/add.frog"
    }
  ],
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
      "kind": "subfrog",
      "ref": "Math.Add"
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
}</code></pre>

<h3>18.2 Diagram using widget value terminals</h3>

<pre><code>"diagram": {
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
      "from": { "node": "input_signal", "port": "value" },
      "to": { "node": "mul_1", "port": "x" }
    },
    {
      "id": "e2",
      "from": { "node": "ctrl_gain_value", "port": "value" },
      "to": { "node": "mul_1", "port": "y" }
    },
    {
      "id": "e3",
      "from": { "node": "mul_1", "port": "result" },
      "to": { "node": "ind_result_value", "port": "value" }
    }
  ]
}</code></pre>

<h3>18.3 Diagram using a widget reference and property write</h3>

<pre><code>"diagram": {
  "nodes": [
    {
      "id": "ctrl_gain_ref",
      "kind": "widget_reference",
      "widget": "ctrl_gain"
    },
    {
      "id": "status_text",
      "kind": "interface_input",
      "interface_port": "status_text"
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
}</code></pre>

<h3>18.4 Diagram invoking a widget method</h3>

<pre><code>"diagram": {
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
}</code></pre>

<h3>18.5 Sequenced widget interactions</h3>

<pre><code>"diagram": {
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
      "id": "e_ref_1",
      "from": { "node": "ctrl_gain_ref", "port": "ref" },
      "to": { "node": "write_visible", "port": "ref" }
    },
    {
      "id": "e_ref_2",
      "from": { "node": "ctrl_gain_ref", "port": "ref" },
      "to": { "node": "write_label_text", "port": "ref" }
    },
    {
      "id": "e_ui_1",
      "from": { "node": "write_visible", "port": "ui_out" },
      "to": { "node": "write_label_text", "port": "ui_in" }
    }
  ]
}</code></pre>

<h3>18.6 Primitive-based diagram with annotations</h3>

<pre><code>"diagram": {
  "nodes": [
    {
      "id": "input_samples",
      "kind": "interface_input",
      "interface_port": "samples"
    },
    {
      "id": "gain",
      "kind": "interface_input",
      "interface_port": "gain"
    },
    {
      "id": "mul_1",
      "kind": "primitive",
      "type": "Multiply"
    },
    {
      "id": "output_scaled",
      "kind": "interface_output",
      "interface_port": "scaled"
    }
  ],
  "edges": [
    {
      "id": "e1",
      "from": { "node": "input_samples", "port": "value" },
      "to": { "node": "mul_1", "port": "x" }
    },
    {
      "id": "e2",
      "from": { "node": "gain", "port": "value" },
      "to": { "node": "mul_1", "port": "y" }
    },
    {
      "id": "e3",
      "from": { "node": "mul_1", "port": "result" },
      "to": { "node": "output_scaled", "port": "value" }
    }
  ],
  "annotations": [
    {
      "id": "ann_section",
      "kind": "region",
      "text": "Signal processing",
      "layout": {
        "x": 10,
        "y": 10,
        "width": 360,
        "height": 160
      }
    }
  ]
}</code></pre>

<h3>18.7 Node documentation and tags</h3>

<pre><code>{
  "id": "kalman_1",
  "kind": "primitive",
  "type": "KalmanFilter",
  "doc": {
    "summary": "Kalman filter step",
    "description": "Computes the next state estimate and covariance update."
  },
  "tags": ["algorithm:kalman", "performance", "rt-safe"]
}</code></pre>

<h3>18.8 Comment attached to a node</h3>

<pre><code>{
  "id": "ann_todo_1",
  "kind": "comment",
  "text": "TODO: replace with FPGA version",
  "target": {
    "scope": "node",
    "id": "kalman_1"
  },
  "tags": ["todo", "performance"]
}</code></pre>

<hr/>

<h2 id="summary">19. Summary</h2>

<p>
The diagram defines the executable structure of a FROG.
</p>

<p>
It provides:
</p>

<ul>
  <li>a directed dataflow graph,</li>
  <li>a resolved node and port model,</li>
  <li>a dependency mechanism for reusable FROGs,</li>
  <li>a structural bridge between the public interface, front panel widget participation, and internal execution logic,</li>
  <li>a place where standardized primitive node families, including widget interaction primitives, participate in execution,</li>
  <li>a canonical source-level place for diagram annotations, documentation, and structured tags.</li>
</ul>

<p>
The diagram is the authoritative definition of execution structure.
The interface defines the public contract.
The front panel defines the UI composition.
The widget model defines widget semantics.
The widget interaction model defines object-style widget access and UI sequencing.
The type system defines compatibility and coercion.
</p>

<p>
Together, these specifications make a FROG executable, composable, documented, UI-aware, and statically verifiable.
</p>
