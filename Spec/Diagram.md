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
  <li><a href="#location">3. Location in a .frog file</a></li>
  <li><a href="#structure">4. Diagram Structure</a></li>
  <li><a href="#node-model">5. Node Model</a></li>
  <li><a href="#port-resolution-model">6. Port Resolution Model</a></li>
  <li><a href="#edge-model">7. Edge Model</a></li>
  <li><a href="#diagram-annotations">8. Diagram Annotations</a></li>
  <li><a href="#documentation-and-tags">9. Documentation and Tags</a></li>
  <li><a href="#layout-information">10. Layout Information</a></li>
  <li><a href="#frog-dependencies">11. Frog Dependencies</a></li>
  <li><a href="#subfrog-invocation">12. Sub-Frog Invocation</a></li>
  <li><a href="#interface-boundary-nodes">13. Interface Boundary Nodes</a></li>
  <li><a href="#graph-validation">14. Graph Validation</a></li>
  <li><a href="#execution-semantics">15. Execution Semantics</a></li>
  <li><a href="#examples">16. Examples</a></li>
  <li><a href="#summary">17. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <strong>diagram</strong> section defines the executable dataflow graph of a Frog.
</p>

<p>
It contains the nodes representing operations, the edges representing directed data connections between them, and the source-level annotations used to document and organize the graph.
</p>

<p>
Execution semantics are derived from the validated graph together with the public interface contract, the FROG type system, and any standardized interaction rules that apply to diagram nodes.
</p>

<hr/>

<h2 id="purpose">2. Purpose of the Diagram</h2>

<p>
The diagram provides:
</p>

<ul>
  <li>the executable logic of the Frog,</li>
  <li>the complete data dependency graph,</li>
  <li>the structural link between the public interface and internal execution logic,</li>
  <li>the hierarchical composition mechanism used to invoke other Frogs,</li>
  <li>the place where standardized primitive operations, including widget interaction primitives, participate in execution,</li>
  <li>the canonical source-level space for diagram annotations and documentation.</li>
</ul>

<p>
Nodes represent computation, interface boundaries, reusable sub-Frog invocations, or other standardized primitive behavior.
Edges represent directional data flow.
Annotations represent source documentation and visual organization only.
</p>

<hr/>

<h2 id="location">3. Location in a .frog file</h2>

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

<h2 id="structure">4. Diagram Structure</h2>

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
  <li><strong>nodes</strong> — required array of graph nodes</li>
  <li><strong>edges</strong> — required array of directed data connections</li>
  <li><strong>dependencies</strong> — optional array of referenced external Frogs</li>
  <li><strong>annotations</strong> — optional array of visible diagram annotations</li>
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

<h2 id="node-model">5. Node Model</h2>

<p>
A node represents an executable or structurally meaningful element of the graph.
</p>

<p>
Every node MUST define:
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

<pre>
{
  "id": "node_1",
  "kind": "primitive",
  "type": "Add",
  "layout": {
    "x": 120,
    "y": 80
  }
}
</pre>

<h3>5.2 Supported node kinds in v0.1</h3>

<ul>
  <li><code>primitive</code></li>
  <li><code>subfrog</code></li>
  <li><code>interface_input</code></li>
  <li><code>interface_output</code></li>
</ul>

<h3>5.3 Primitive nodes</h3>

<p>
A <code>primitive</code> node represents a built-in or profile-defined operation.
</p>

<pre>
{
  "id": "add_1",
  "kind": "primitive",
  "type": "Add",
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
  <li><code>type</code> MUST exist and identify the primitive operation.</li>
  <li>The meaning and port signature of the primitive are defined by the active profile, standard library, or implementation-defined primitive catalog.</li>
</ul>

<p>
Primitive nodes include ordinary computational primitives such as arithmetic operations, but may also include other standardized primitive families defined elsewhere in the specification.
</p>

<p>
For example, <code>Widget interaction.md</code> defines standardized primitive identifiers such as:
</p>

<ul>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
</ul>

<p>
These remain <code>primitive</code> nodes and are validated according to both this document and the widget interaction specification.
</p>

<h3>5.4 Sub-Frog nodes</h3>

<p>
A <code>subfrog</code> node represents an invocation of another Frog.
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
  <li><code>ref</code> MUST exist.</li>
  <li><code>ref</code> MUST match a declared dependency identifier.</li>
  <li>The input and output ports of the node are derived from the referenced Frog interface.</li>
</ul>

<h3>5.5 Interface input nodes</h3>

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
  <li><code>interface_port</code> MUST exist.</li>
  <li><code>interface_port</code> MUST reference an existing input declared in the <code>interface</code> section.</li>
</ul>

<h3>5.6 Interface output nodes</h3>

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
  <li><code>interface_port</code> MUST exist.</li>
  <li><code>interface_port</code> MUST reference an existing output declared in the <code>interface</code> section.</li>
</ul>

<hr/>

<h2 id="port-resolution-model">6. Port Resolution Model</h2>

<p>
FROG v0.1 does not require every node to declare an explicit <code>ports</code> array inside the diagram source.
Instead, valid ports are resolved from the node kind and its definition source.
</p>

<h3>6.1 Port resolution by node kind</h3>

<ul>
  <li><strong>primitive</strong> — ports are defined by the primitive operation signature.</li>
  <li><strong>subfrog</strong> — ports are defined by the referenced Frog interface.</li>
  <li><strong>interface_input</strong> — exactly one output port named <code>value</code>.</li>
  <li><strong>interface_output</strong> — exactly one input port named <code>value</code>.</li>
</ul>

<h3>6.2 Primitive node ports</h3>

<p>
For a <code>primitive</code> node, port names, directions, arity, and types are defined by the active primitive catalog or profile.
This document does not standardize the full primitive catalog itself.
</p>

<p>
However, some primitive families are standardized by other specification documents.
When this is the case, their port model MUST be resolved according to the corresponding document.
</p>

<p>
In particular:
</p>

<ul>
  <li>ordinary computational primitives resolve ports according to the active primitive catalog,</li>
  <li>widget interaction primitives resolve ports according to <code>Widget interaction.md</code>.</li>
</ul>

<h3>6.3 Sub-Frog node ports</h3>

<p>
For a <code>subfrog</code> node:
</p>

<ul>
  <li>every referenced Frog input becomes an input port of the node using the same interface port identifier,</li>
  <li>every referenced Frog output becomes an output port of the node using the same interface port identifier.</li>
</ul>

<p>
The types of these ports are exactly the types declared by the referenced Frog interface.
</p>

<h3>6.4 Interface boundary node ports</h3>

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

<h3>6.5 Port validation consequence</h3>

<p>
Any edge endpoint referencing a node port is valid only if that port exists after resolution under the rules above.
</p>

<hr/>

<h2 id="edge-model">7. Edge Model</h2>

<p>
Edges define directional data connections between node ports.
</p>

<pre>
{
  "id": "edge_1",
  "from": {
    "node": "node_1",
    "port": "result"
  },
  "to": {
    "node": "node_2",
    "port": "a"
  }
}
</pre>

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
Edges represent directional data flow and MUST respect resolved port direction.
</p>

<p>
A valid edge endpoint object has the following form:
</p>

<pre>
{
  "node": "some_node_id",
  "port": "some_port_name"
}
</pre>

<hr/>

<h2 id="diagram-annotations">8. Diagram Annotations</h2>

<p>
The <code>annotations</code> array contains visible, non-executable source annotations created by the author to document, organize, or label the diagram.
</p>

<p>
Annotations are part of the canonical expression when they represent intended source documentation.
They MUST NOT alter execution semantics.
</p>

<h3>8.1 Purpose of annotations</h3>

<p>
Annotations may be used for:
</p>

<ul>
  <li>free labels,</li>
  <li>attached comments,</li>
  <li>wire labels,</li>
  <li>functional regions or framed sections,</li>
  <li>other documented visible note forms standardized by an active profile.</li>
</ul>

<h3>8.2 Annotation structure</h3>

<p>
Recommended annotation shape:
</p>

<pre>
{
  "id": "ann_1",
  "kind": "free_label",
  "text": "Initialization",
  "layout": {
    "x": 20,
    "y": 20,
    "width": 140,
    "height": 24
  }
}
</pre>

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

<h3>8.3 Standard annotation kinds for v0.1</h3>

<ul>
  <li><code>free_label</code></li>
  <li><code>comment</code></li>
  <li><code>wire_label</code></li>
  <li><code>region</code></li>
</ul>

<h3>8.4 Free label</h3>

<p>
A <code>free_label</code> is free-standing visible text placed on the diagram.
</p>

<pre>
{
  "id": "ann_init",
  "kind": "free_label",
  "text": "Initialization",
  "layout": {
    "x": 20,
    "y": 20,
    "width": 160,
    "height": 24
  }
}
</pre>

<h3>8.5 Comment</h3>

<p>
A <code>comment</code> is a textual annotation that may optionally target a node or an edge.
</p>

<pre>
{
  "id": "ann_todo",
  "kind": "comment",
  "text": "TODO: optimize for RT target",
  "target": {
    "scope": "node",
    "id": "mul_1"
  },
  "tags": ["todo", "performance", "rt-safe"]
}
</pre>

<h3>8.6 Wire label</h3>

<p>
A <code>wire_label</code> is a textual annotation attached to an edge.
</p>

<pre>
{
  "id": "ann_wire_1",
  "kind": "wire_label",
  "text": "temperature_filtered",
  "target": {
    "scope": "edge",
    "id": "e1"
  }
}
</pre>

<h3>8.7 Region</h3>

<p>
A <code>region</code> groups or frames a functional portion of the diagram visually.
It may optionally reference nodes.
</p>

<pre>
{
  "id": "ann_region_1",
  "kind": "region",
  "text": "Acquisition",
  "layout": {
    "x": 10,
    "y": 10,
    "width": 300,
    "height": 180
  },
  "targets": {
    "nodes": ["n1", "n2", "n3"]
  }
}
</pre>

<h3>8.8 Annotation targets</h3>

<p>
When <code>target</code> is present, it SHOULD follow one of these forms:
</p>

<ul>
  <li><code>{ "scope": "node", "id": "node_id" }</code></li>
  <li><code>{ "scope": "edge", "id": "edge_id" }</code></li>
</ul>

<p>
A <code>targets</code> object MAY be used when an annotation references multiple nodes or edges for organizational purposes.
</p>

<h3>8.9 Execution neutrality</h3>

<p>
Annotations are source documentation and visual structure only.
They MUST NOT alter:
</p>

<ul>
  <li>node behavior,</li>
  <li>edge behavior,</li>
  <li>scheduling,</li>
  <li>type compatibility,</li>
  <li>the public interface contract.</li>
</ul>

<hr/>

<h2 id="documentation-and-tags">9. Documentation and Tags</h2>

<p>
FROG v0.1 distinguishes between:
</p>

<ul>
  <li><strong>visible annotations</strong> stored in <code>diagram.annotations</code>,</li>
  <li><strong>structured documentation</strong> attached directly to nodes, edges, or annotations,</li>
  <li><strong>editor-only navigation state</strong> that belongs to IDE-specific data rather than the canonical diagram expression.</li>
</ul>

<h3>9.1 Structured documentation</h3>

<p>
A node, edge, or annotation MAY define a <code>doc</code> object.
</p>

<p>
Recommended shape:
</p>

<pre>
"doc": {
  "summary": "Short human-readable summary",
  "description": "Longer structured explanation."
}
</pre>

<p>
This documentation is canonical source documentation.
It is not required to be rendered directly on the diagram surface.
</p>

<h3>9.2 Structured tags</h3>

<p>
A node, edge, or annotation MAY define a <code>tags</code> array.
</p>

<pre>
"tags": ["todo", "warning", "performance"]
</pre>

<p>
Tags are intended to support structured source organization, filtering, searching, tooling, and future documentation workflows.
</p>

<p>
Examples of meaningful tags:
</p>

<ul>
  <li><code>todo</code></li>
  <li><code>fixme</code></li>
  <li><code>warning</code></li>
  <li><code>note</code></li>
  <li><code>performance</code></li>
  <li><code>rt-safe</code></li>
  <li><code>deprecated</code></li>
  <li><code>algorithm:kalman</code></li>
</ul>

<p>
This document does not impose a closed vocabulary for tags in v0.1.
</p>

<h3>9.3 Source documentation vs IDE-only state</h3>

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

<h2 id="layout-information">10. Layout Information</h2>

<p>
Nodes and annotations MAY include layout information for graphical editors.
</p>

<pre>
"layout": {
  "x": 240,
  "y": 120
}
</pre>

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
It MUST NOT influence execution semantics, scheduling, typing, or dataflow behavior.
</p>

<hr/>

<h2 id="frog-dependencies">11. Frog Dependencies</h2>

<p>
When a diagram uses nodes implemented by other Frogs, those Frogs MUST be referenced in <code>dependencies</code>.
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
  <li><strong>name</strong> — logical identifier used by <code>subfrog.ref</code></li>
  <li><strong>path</strong> — relative path or equivalent source reference</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>Dependency names MUST be unique within the diagram.</li>
  <li>Each <code>subfrog.ref</code> MUST resolve to an existing dependency name.</li>
  <li>The referenced Frog MUST expose an interface usable to resolve the sub-Frog node ports.</li>
</ul>

<p>
This document does not standardize packaging, search paths, remote resolution, or dependency locking mechanisms.
</p>

<hr/>

<h2 id="subfrog-invocation">12. Sub-Frog Invocation</h2>

<p>
Sub-Frog invocation enables hierarchical program composition.
A sub-Frog behaves as a reusable node whose public ports are derived from the referenced Frog interface.
</p>

<pre>
{
  "id": "node_2",
  "kind": "subfrog",
  "ref": "Math.Add",
  "layout": {
    "x": 320,
    "y": 80
  }
}
</pre>

<p>
Conceptually:
</p>

<ul>
  <li>the invoked Frog interface defines the node contract,</li>
  <li>the connector, if any, only affects graphical presentation when reused in tools,</li>
  <li>execution semantics depend on the referenced Frog program, not on its connector or icon.</li>
</ul>

<hr/>

<h2 id="interface-boundary-nodes">13. Interface Boundary Nodes</h2>

<p>
The executable graph MUST be consistent with the public interface declared in the <code>interface</code> section.
In v0.1, this consistency is established through dedicated interface boundary nodes.
</p>

<p>
Therefore:
</p>

<ul>
  <li>each public interface input SHOULD be represented by one <code>interface_input</code> node,</li>
  <li>each public interface output SHOULD be represented by one <code>interface_output</code> node.</li>
</ul>

<p>
For canonical v0.1 source diagrams, tools SHOULD emit exactly one boundary node for each declared interface port.
</p>

<p>
Conceptually:
</p>

<pre>
external input  ->  interface_input.value  ->  internal graph
internal graph  ->  interface_output.value ->  external output
</pre>

<p>
An <code>interface_input</code> node introduces externally provided data into the diagram.
An <code>interface_output</code> node consumes internal data and exposes it as a public output.
</p>

<hr/>

<h2 id="graph-validation">14. Graph Validation</h2>

<p>
Implementations MUST enforce the following rules:
</p>

<ul>
  <li>the <code>diagram</code> section MUST exist,</li>
  <li><code>nodes</code> and <code>edges</code> MUST exist and MUST be arrays,</li>
  <li>node identifiers MUST be unique within the diagram,</li>
  <li>edge identifiers MUST be unique within the diagram,</li>
  <li>every edge endpoint MUST reference an existing node,</li>
  <li>every referenced port MUST exist after port resolution,</li>
  <li>edge direction MUST match the direction of the referenced ports,</li>
  <li>connected ports MUST be type-compatible according to <code>Type.md</code>,</li>
  <li>every <code>interface_input</code> node MUST reference an existing interface input,</li>
  <li>every <code>interface_output</code> node MUST reference an existing interface output,</li>
  <li>every <code>subfrog.ref</code> MUST resolve to a declared dependency,</li>
  <li>the diagram MUST remain consistent with the interface contract.</li>
</ul>

<p>
In particular:
</p>

<ul>
  <li>each declared interface input MUST be consumable by the graph,</li>
  <li>each declared interface output MUST be producible by the graph,</li>
  <li>unbound, contradictory, or unreachable interface boundary definitions MUST trigger validation errors.</li>
</ul>

<p>
For widget interaction primitives:
</p>

<ul>
  <li>the node MUST satisfy the rules defined in <code>Widget interaction.md</code>,</li>
  <li>the referenced widget MUST exist in the <code>front_panel</code>,</li>
  <li>the referenced widget member MUST be valid for the addressed widget or widget part,</li>
  <li>the resolved widget interaction ports MUST remain type-compatible with connected edges.</li>
</ul>

<p>
For annotations and source documentation:
</p>

<ul>
  <li>if present, <code>annotations</code> MUST be an array,</li>
  <li>annotation identifiers MUST be unique within the diagram,</li>
  <li>annotation targets MUST reference existing nodes or edges when specified,</li>
  <li><code>doc</code> fields MUST be objects when present,</li>
  <li><code>tags</code> fields MUST be arrays of strings when present,</li>
  <li>annotations MUST NOT be interpreted as executable nodes or executable edges.</li>
</ul>

<p>
Unknown node or annotation properties MAY be ignored unless a stricter active profile defines them.
</p>

<hr/>

<h2 id="execution-semantics">15. Execution Semantics</h2>

<p>
Execution follows a pure dataflow model.
</p>

<ul>
  <li>A node becomes executable when all required input values are available.</li>
  <li>Execution order derives from data dependencies, not from source ordering.</li>
  <li>Independent nodes MAY execute in parallel.</li>
</ul>

<p>
The diagram is the authoritative structural definition of execution logic inside a Frog.
However, the graph MUST be interpreted together with:
</p>

<ul>
  <li>the public interface contract,</li>
  <li>the type system and implicit coercion rules,</li>
  <li>the primitive and sub-Frog operation definitions available in the active execution profile,</li>
  <li>the widget interaction rules for any standardized widget interaction primitive nodes.</li>
</ul>

<p>
Layout, connector placement, icon content, IDE preferences, cache data, annotations, structured documentation, and structured tags MUST NOT alter execution semantics.
</p>

<p>
When widget interaction nodes are present, they participate in execution as ordinary validated diagram nodes.
However, they do not redefine the public interface contract and do not alter the core dataflow execution model.
</p>

<hr/>

<h2 id="examples">16. Examples</h2>

<h3>16.1 Minimal arithmetic diagram</h3>

<pre>
"diagram": {
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
}
</pre>

<h3>16.2 Primitive-based diagram</h3>

<pre>
"diagram": {
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
}
</pre>

<h3>16.3 Diagram using widget interaction primitives</h3>

<pre>
"diagram": {
  "nodes": [
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
  ]
}
</pre>

<h3>16.4 Diagram writing a widget part property</h3>

<pre>
"diagram": {
  "nodes": [
    {
      "id": "status_text",
      "kind": "interface_input",
      "interface_port": "status_text"
    },
    {
      "id": "write_label_text",
      "kind": "primitive",
      "type": "frog.ui.property_write",
      "target": {
        "widget": "ctrl_gain",
        "part": "label",
        "member": "text"
      }
    }
  ],
  "edges": [
    {
      "id": "e1",
      "from": { "node": "status_text", "port": "value" },
      "to": { "node": "write_label_text", "port": "value" }
    }
  ]
}
</pre>

<h3>16.5 Node documentation and tags</h3>

<pre>
{
  "id": "kalman_1",
  "kind": "primitive",
  "type": "KalmanFilter",
  "doc": {
    "summary": "Kalman filter step",
    "description": "Computes the next state estimate and covariance update."
  },
  "tags": ["algorithm:kalman", "performance", "rt-safe"]
}
</pre>

<h3>16.6 Comment attached to a node</h3>

<pre>
{
  "id": "ann_todo_1",
  "kind": "comment",
  "text": "TODO: replace with FPGA version",
  "target": {
    "scope": "node",
    "id": "kalman_1"
  },
  "tags": ["todo", "performance"]
}
</pre>

<h3>16.7 Wire label attached to an edge</h3>

<pre>
{
  "id": "ann_wire_temp",
  "kind": "wire_label",
  "text": "temperature_filtered",
  "target": {
    "scope": "edge",
    "id": "e_temp"
  }
}
</pre>

<hr/>

<h2 id="summary">17. Summary</h2>

<p>
The diagram defines the executable structure of a Frog.
</p>

<p>
It provides:
</p>

<ul>
  <li>a directed dataflow graph,</li>
  <li>a resolved node and port model,</li>
  <li>a dependency mechanism for reusable Frogs,</li>
  <li>a structural bridge between the public interface and internal execution logic,</li>
  <li>a place where standardized primitive node families, including widget interaction primitives, participate in execution,</li>
  <li>a canonical source-level place for diagram annotations, documentation, and structured tags.</li>
</ul>

<p>
The diagram is the authoritative definition of execution structure.
The interface defines the public contract.
The type system defines compatibility and coercion.
The widget interaction model defines how diagrams may safely interact with front panel widgets.
Annotations and documentation define how authors explain and organize the graph without altering execution.
Together, they make a Frog executable, composable, documented, and statically verifiable.
</p>
