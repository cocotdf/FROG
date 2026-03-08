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
  <li><a href="#layout-information">8. Layout Information</a></li>
  <li><a href="#frog-dependencies">9. Frog Dependencies</a></li>
  <li><a href="#subfrog-invocation">10. Sub-Frog Invocation</a></li>
  <li><a href="#interface-boundary-nodes">11. Interface Boundary Nodes</a></li>
  <li><a href="#graph-validation">12. Graph Validation</a></li>
  <li><a href="#execution-semantics">13. Execution Semantics</a></li>
  <li><a href="#examples">14. Examples</a></li>
  <li><a href="#summary">15. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <strong>diagram</strong> section defines the executable dataflow graph of a Frog.
</p>

<p>
It contains the nodes representing operations and the edges representing directed data connections between them.
</p>

<p>
Execution semantics are derived from this graph together with the validated interface contract, the FROG type system, and any standardized interaction rules that apply to diagram nodes.
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
  <li>the location where standardized primitive operations, including widget interaction primitives, participate in execution.</li>
</ul>

<p>
Nodes represent computation, interface boundaries, reusable sub-Frog invocations, or other standardized primitive behavior.
Edges represent directional data flow.
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
The diagram object contains three fields:
</p>

<pre>
"diagram": {
  "nodes": [],
  "edges": [],
  "dependencies": []
}
</pre>

<p>
Fields:
</p>

<ul>
  <li><strong>nodes</strong> — required array of graph nodes</li>
  <li><strong>edges</strong> — required array of directed data connections</li>
  <li><strong>dependencies</strong> — optional array of referenced external Frogs</li>
</ul>

<p>
The <code>nodes</code> and <code>edges</code> arrays MUST exist, even if one of them is empty.
The <code>dependencies</code> field MAY be omitted when no external Frog is referenced.
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

<h2 id="layout-information">8. Layout Information</h2>

<p>
Nodes MAY include layout information for graphical editors.
</p>

<pre>
"layout": {
  "x": 240,
  "y": 120
}
</pre>

<p>
Layout information is optional and affects graphical rendering only.
It MUST NOT influence execution semantics, scheduling, typing, or dataflow behavior.
</p>

<hr/>

<h2 id="frog-dependencies">9. Frog Dependencies</h2>

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

<h2 id="subfrog-invocation">10. Sub-Frog Invocation</h2>

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

<h2 id="interface-boundary-nodes">11. Interface Boundary Nodes</h2>

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

<h2 id="graph-validation">12. Graph Validation</h2>

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
Unknown node properties MAY be ignored unless a stricter active profile defines them.
</p>

<hr/>

<h2 id="execution-semantics">13. Execution Semantics</h2>

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
Layout, connector placement, icon content, IDE preferences, and cache data MUST NOT alter execution semantics.
</p>

<p>
When widget interaction nodes are present, they participate in execution as ordinary validated diagram nodes.
However, they do not redefine the public interface contract and do not alter the core dataflow execution model.
</p>

<hr/>

<h2 id="examples">14. Examples</h2>

<h3>14.1 Minimal arithmetic diagram</h3>

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

<h3>14.2 Primitive-based diagram</h3>

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
  ]
}
</pre>

<h3>14.3 Diagram using widget interaction primitives</h3>

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

<h3>14.4 Diagram writing a widget part property</h3>

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

<hr/>

<h2 id="summary">15. Summary</h2>

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
  <li>a place where standardized primitive node families, including widget interaction primitives, participate in execution.</li>
</ul>

<p>
The diagram is the authoritative definition of execution structure.
The interface defines the public contract.
The type system defines compatibility and coercion.
The widget interaction model defines how diagrams may safely interact with front panel widgets.
Together, they make a Frog executable, composable, and statically verifiable.
</p>
