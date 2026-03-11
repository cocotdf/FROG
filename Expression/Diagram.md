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
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#location-in-a-frog-file">4. Location in a <code>.frog</code> File</a></li>
  <li><a href="#diagram-structure">5. Diagram Structure</a></li>
  <li><a href="#diagram-scopes">6. Diagram Scopes</a></li>
  <li><a href="#conceptual-model">7. Conceptual Model</a></li>
  <li><a href="#node-model">8. Node Model</a></li>
  <li><a href="#standard-node-kinds-for-v01">9. Standard Node Kinds for v0.1</a></li>
  <li><a href="#port-model">10. Port Model</a></li>
  <li><a href="#port-resolution-model">11. Port Resolution Model</a></li>
  <li><a href="#edge-model">12. Edge Model</a></li>
  <li><a href="#annotations-documentation-and-tags">13. Annotations, Documentation, and Tags</a></li>
  <li><a href="#layout-information">14. Layout Information</a></li>
  <li><a href="#frog-dependencies">15. FROG Dependencies</a></li>
  <li><a href="#sub-frog-invocation">16. Sub-FROG Invocation</a></li>
  <li><a href="#interface-widget-and-structure-boundaries">17. Interface, Widget, and Structure Boundaries</a></li>
  <li><a href="#widget-interaction-model">18. Widget Interaction Model</a></li>
  <li><a href="#cycles-and-local-state">19. Cycles and Local State</a></li>
  <li><a href="#graph-validation">20. Graph Validation</a></li>
  <li><a href="#execution-semantics">21. Execution Semantics</a></li>
  <li><a href="#examples">22. Examples</a></li>
  <li><a href="#summary">23. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The diagram is the authoritative executable graph of a FROG program.
It defines how values, structure boundaries, public interface participation, widget participation,
sub-FROG calls, and explicit local-memory elements are connected to form an executable system.
</p>

<p>
A FROG diagram is not a decorative editor view layered on top of hidden semantics.
It is the canonical source-level representation of executable graph structure.
Execution semantics are derived from the validated diagram together with:
</p>

<ul>
  <li>the primitive definitions of referenced libraries,</li>
  <li>the semantics of standardized structure kinds,</li>
  <li>the declared public interface,</li>
  <li>the widget model and widget-interaction model where front-panel widgets participate,</li>
  <li>the type system,</li>
  <li>the explicit local-memory rules that make cycles executable.</li>
</ul>

<p>
This document defines the graph-level representation itself.
It does not redefine the full semantics of all primitives, structures, widgets, or types.
</p>

<hr/>

<h2 id="purpose">2. Purpose of the Diagram</h2>

<p>
The purpose of the diagram is to provide a canonical, durable, tool-independent representation of execution structure.
A valid diagram MUST be sufficient to determine the executable graph shape of a FROG.
</p>

<p>
In particular, the diagram is responsible for representing:
</p>

<ul>
  <li>the nodes that participate in execution or graph boundaries,</li>
  <li>the directed edges that carry values or explicit sequencing dependencies,</li>
  <li>the canonical graph participation of public interface ports,</li>
  <li>the canonical graph participation of widget values and widget references,</li>
  <li>the invocation sites of other FROGs,</li>
  <li>the explicit local-memory elements required for executable feedback cycles,</li>
  <li>the source-level annotations and layout metadata that belong to a graphical language.</li>
</ul>

<p>
The diagram MUST NOT rely on hidden editor-only bindings to define execution.
If a participation in execution matters semantically, it MUST be represented explicitly in the diagram or in the referenced canonical specifications on which the diagram depends.
</p>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This document depends on the following FROG specifications:
</p>

<ul>
  <li><code>Expression/Interface.md</code> — public interface ports and their relation to the graph,</li>
  <li><code>Expression/Front panel.md</code> — front-panel widget instances and UI composition,</li>
  <li><code>Expression/Widget.md</code> — widget identity, roles, properties, methods, and value participation,</li>
  <li><code>Expression/Widget interaction.md</code> — object-style widget interaction through diagram primitives,</li>
  <li><code>Expression/Control structures.md</code> — structure kinds, regions, and structure-owned execution rules,</li>
  <li><code>Expression/State and cycles.md</code> — explicit local memory and cycle legality,</li>
  <li><code>Expression/Type.md</code> — typing rules used by ports and edges,</li>
  <li><code>Libraries/Core.md</code> and other library specifications — primitive signatures and primitive semantics.</li>
</ul>

<p>
This document defines how those elements appear at graph level.
It does not replace the specifications that define their detailed semantics.
</p>

<hr/>

<h2 id="location-in-a-frog-file">4. Location in a <code>.frog</code> File</h2>

<p>
The executable graph of a FROG is stored in the top-level <code>diagram</code> section.
</p>

<pre><code>{
  "interface": { ... },
  "front_panel": { ... },
  "diagram": {
    "nodes": [ ... ],
    "edges": [ ... ]
  }
}</code></pre>

<p>
For v0.1, the top-level <code>diagram</code> object is the canonical outer executable graph of the FROG.
Structures MAY own nested executable regions inside their node definitions according to the control-structure specification.
</p>

<hr/>

<h2 id="diagram-structure">5. Diagram Structure</h2>

<p>
The top-level diagram object has the following canonical shape:
</p>

<pre><code>{
  "diagram": {
    "nodes": [ ... ],
    "edges": [ ... ],
    "dependencies": [ ... ],
    "annotations": { ... }
  }
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>nodes</code> MUST exist and MUST be an array.</li>
  <li><code>edges</code> MUST exist and MUST be an array.</li>
  <li><code>dependencies</code> MAY be omitted when unused.</li>
  <li><code>annotations</code> MAY be omitted when unused.</li>
</ul>

<p>
The <code>annotations</code> field belongs to canonical source because it expresses author-created documentation and visible diagram organization.
It MUST NOT change validated execution semantics.
</p>

<hr/>

<h2 id="diagram-scopes">6. Diagram Scopes</h2>

<p>
FROG diagrams are recursive.
The top-level <code>diagram</code> object defines the outer executable graph of the FROG.
Certain structure nodes MAY own internal executable regions, and each such region contains its own local diagram scope.
</p>

<p>
Accordingly, FROG distinguishes:
</p>

<ul>
  <li>top-level diagram scope — the outer executable graph of the FROG,</li>
  <li>region-local diagram scope — a nested executable graph owned by a structure region.</li>
</ul>

<p>
Each diagram scope has its own local:
</p>

<ul>
  <li>node identifier namespace,</li>
  <li>edge identifier namespace,</li>
  <li>set of locally contained nodes and edges.</li>
</ul>

<p>
A graph edge MUST connect ports that are valid within the same diagram scope.
Crossing a structure boundary MUST occur only through explicit structure boundary ports or terminals defined by the owning structure semantics.
No hidden cross-scope edge is permitted.
</p>

<hr/>

<h2 id="conceptual-model">7. Conceptual Model</h2>

<p>
A validated diagram defines a directed graph whose nodes expose typed ports and whose edges connect compatible ports.
The graph is structural and executable:
</p>

<ul>
  <li>structural, because it explicitly defines graph boundaries and nesting,</li>
  <li>executable, because value availability, structure rules, and explicit local state determine run-time behavior.</li>
</ul>

<p>
At conceptual level:
</p>

<ul>
  <li>a node is a graph element that owns ports and participates in execution or graph boundaries,</li>
  <li>a port is a typed participation point on a node,</li>
  <li>an edge is a directed connection from one node port to another node port,</li>
  <li>a diagram scope is a container of nodes and edges with its own local namespaces.</li>
</ul>

<p>
The diagram itself does not impose a textual instruction order.
Ordinary execution follows dataflow readiness, structure semantics, explicit UI sequencing where used, and explicit local-memory rules where required by cycles.
</p>

<hr/>

<h2 id="node-model">8. Node Model</h2>

<p>
A node represents an executable or structurally meaningful element of the graph.
Every node owns a set of input and output ports, whether those ports are declared directly in the node, derived from a referenced primitive signature, derived from a structure family, derived from an interface boundary, or derived from widget semantics.
</p>

<p>
Every node MUST define:
</p>

<ul>
  <li><code>id</code> — unique node identifier within the owning diagram scope,</li>
  <li><code>kind</code> — node category.</li>
</ul>

<p>
A node MAY also define:
</p>

<ul>
  <li><code>layout</code> — graphical editor position and size metadata,</li>
  <li><code>doc</code> — optional structured documentation,</li>
  <li><code>tags</code> — optional structured tags,</li>
  <li>kind-specific fields defined by this document or by a referenced specification.</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>Node identifiers MUST be unique within the owning diagram scope.</li>
  <li>Node identifiers MAY be reused in different nested scopes.</li>
  <li>A node MUST NOT expose hidden semantically required ports outside the canonical resolution rules of its kind.</li>
</ul>

<hr/>

<h2 id="standard-node-kinds-for-v01">9. Standard Node Kinds for v0.1</h2>

<p>
The following node kinds are standardized for FROG v0.1:
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

<h3>9.1 <code>primitive</code></h3>

<p>
A <code>primitive</code> node represents a library-defined primitive operation.
</p>

<pre><code>{
  "id": "mul_1",
  "kind": "primitive",
  "type": "frog.core.multiply",
  "layout": {
    "x": 320,
    "y": 120
  }
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>type</code> MUST exist.</li>
  <li><code>type</code> MUST identify a valid primitive definition.</li>
  <li>The node ports are derived from the referenced primitive definition and any kind-specific canonical rules.</li>
</ul>

<h3>9.2 <code>structure</code></h3>

<p>
A <code>structure</code> node represents a language structure whose execution semantics are defined by the control-structure specification.
Examples include <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>.
</p>

<pre><code>{
  "id": "case_1",
  "kind": "structure",
  "structure_type": "case",
  "regions": [ ... ],
  "layout": {
    "x": 240,
    "y": 80,
    "width": 320,
    "height": 220
  }
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>structure_type</code> MUST exist.</li>
  <li><code>regions</code> MUST be present when required by the referenced structure family.</li>
  <li>Boundary ports, region ownership, and execution rules are defined by the structure specification.</li>
</ul>

<h3>9.3 <code>subfrog</code></h3>

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
  <li><code>ref</code> MUST exist.</li>
  <li><code>ref</code> MUST match a declared dependency identifier.</li>
  <li>The input and output ports of the node are derived from the referenced FROG interface.</li>
</ul>

<h3>9.4 <code>interface_input</code></h3>

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
  <li><code>interface_port</code> MUST exist.</li>
  <li><code>interface_port</code> MUST reference an existing input declared in the <code>interface</code> section.</li>
  <li>The node exposes exactly one output port named <code>value</code>.</li>
</ul>

<h3>9.5 <code>interface_output</code></h3>

<p>
An <code>interface_output</code> node represents the exit point of a declared public interface output inside the executable graph.
</p>

<pre><code>{
  "id": "output_result",
  "kind": "interface_output",
  "interface_port": "result",
  "layout": {
    "x": 720,
    "y": 140
  }
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>interface_port</code> MUST exist.</li>
  <li><code>interface_port</code> MUST reference an existing output declared in the <code>interface</code> section.</li>
  <li>The node exposes exactly one input port named <code>value</code>.</li>
</ul>

<h3>9.6 <code>widget_value</code></h3>

<p>
A <code>widget_value</code> node represents the natural graph participation of the primary value of a front-panel widget.
</p>

<pre><code>{
  "id": "ctrl_gain_value",
  "kind": "widget_value",
  "widget": "ctrl_gain",
  "layout": {
    "x": 80,
    "y": 200
  }
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>widget</code> MUST exist.</li>
  <li><code>widget</code> MUST reference an existing value-carrying widget in the front panel.</li>
  <li>The node exposes exactly one value port whose direction and type are defined by the widget role and widget class.</li>
</ul>

<h3>9.7 <code>widget_reference</code></h3>

<p>
A <code>widget_reference</code> node represents an object-style reference to a front-panel widget.
It is used when the diagram interacts with widget properties or methods through standardized UI primitives.
</p>

<pre><code>{
  "id": "ctrl_gain_ref",
  "kind": "widget_reference",
  "widget": "ctrl_gain",
  "layout": {
    "x": 80,
    "y": 320
  }
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>widget</code> MUST exist.</li>
  <li><code>widget</code> MUST reference an existing widget in the front panel.</li>
  <li>The node exposes exactly one output port named <code>ref</code>.</li>
  <li>The <code>ref</code> port type is an opaque widget-reference token compatible with the addressed widget class.</li>
</ul>

<hr/>

<h2 id="port-model">10. Port Model</h2>

<p>
A port is a typed participation point on a node.
A port belongs to exactly one node and has a direction relative to that node.
</p>

<p>
For v0.1, a port is characterized conceptually by:
</p>

<ul>
  <li>its owning node,</li>
  <li>its local port name,</li>
  <li>its direction — input or output,</li>
  <li>its type, including opaque sequencing-token or widget-reference types where applicable.</li>
</ul>

<p>
This specification does not require ports to be redundantly serialized inside every node instance.
Instead, port sets are usually derived by canonical resolution rules.
However, once resolved, ports are semantically real parts of the validated graph.
</p>

<p>
Rules:
</p>

<ul>
  <li>A port name MUST be unique within the resolved port set of its owning node.</li>
  <li>Each input port accepts at most one incoming ordinary driver edge unless a referenced primitive or structure explicitly defines otherwise.</li>
  <li>An output port MAY fan out to multiple consumer ports where type and scope rules allow.</li>
</ul>

<hr/>

<h2 id="port-resolution-model">11. Port Resolution Model</h2>

<p>
Node ports are resolved according to node kind.
</p>

<h3>11.1 Primitive port resolution</h3>

<p>
For an ordinary <code>primitive</code> node, the input and output ports are derived from the referenced primitive definition.
</p>

<h3>11.2 Primitive port resolution for widget interaction</h3>

<p>
The following standardized primitive families have additional canonical port rules in v0.1:
</p>

<h4>11.2.1 <code>frog.ui.property_read</code></h4>

<ul>
  <li>required input port: <code>ref</code>,</li>
  <li>optional input port: <code>ui_in</code>,</li>
  <li>required output port: <code>value</code>,</li>
  <li>optional output port: <code>ui_out</code>.</li>
</ul>

<p>
The <code>value</code> port type is defined by the addressed widget member.
The <code>ref</code> port is an opaque widget-reference token.
The optional <code>ui_in</code> and <code>ui_out</code> ports are opaque UI sequencing ports.
</p>

<h4>11.2.2 <code>frog.ui.property_write</code></h4>

<ul>
  <li>required input port: <code>ref</code>,</li>
  <li>required input port: <code>value</code>,</li>
  <li>optional input port: <code>ui_in</code>,</li>
  <li>optional output port: <code>ui_out</code>.</li>
</ul>

<p>
The <code>value</code> port type is defined by the addressed widget member.
The <code>ref</code> port is an opaque widget-reference token.
The optional <code>ui_in</code> and <code>ui_out</code> ports are opaque UI sequencing ports.
</p>

<h4>11.2.3 <code>frog.ui.method_invoke</code></h4>

<ul>
  <li>required input port: <code>ref</code>,</li>
  <li>zero or more method argument input ports in canonical method order,</li>
  <li>optional input port: <code>ui_in</code>,</li>
  <li>zero or more method result output ports in canonical method order,</li>
  <li>optional output port: <code>ui_out</code>.</li>
</ul>

<p>
Method argument and result types are defined by the addressed method signature.
The <code>ref</code> port is an opaque widget-reference token.
The optional <code>ui_in</code> and <code>ui_out</code> ports are opaque UI sequencing ports.
</p>

<h3>11.3 Structure port resolution</h3>

<p>
For a <code>structure</code> node, visible boundary ports are derived from the semantics of the referenced structure family.
This includes selector ports, loop-carried ports, region outputs, and other structure-defined terminals where applicable.
</p>

<h3>11.4 Sub-FROG port resolution</h3>

<p>
For a <code>subfrog</code> node, ports are derived from the declared public interface of the referenced dependency.
</p>

<h3>11.5 Interface boundary port resolution</h3>

<ul>
  <li><code>interface_input</code> exposes one output port named <code>value</code>,</li>
  <li><code>interface_output</code> exposes one input port named <code>value</code>.</li>
</ul>

<p>
The type of that port is derived from the referenced public interface declaration.
</p>

<h3>11.6 Widget participation port resolution</h3>

<ul>
  <li><code>widget_value</code> exposes one primary-value port whose direction and type are determined by widget role and widget class,</li>
  <li><code>widget_reference</code> exposes one output port named <code>ref</code>.</li>
</ul>

<hr/>

<h2 id="edge-model">12. Edge Model</h2>

<p>
An edge is a directed connection between a source node port and a target node port in the same diagram scope.
</p>

<p>
Canonical shape:
</p>

<pre><code>{
  "id": "e1",
  "from": { "node": "input_a", "port": "value" },
  "to":   { "node": "mul_1",   "port": "x" }
}</code></pre>

<p>
Every edge MUST define:
</p>

<ul>
  <li><code>id</code> — unique edge identifier within the owning diagram scope,</li>
  <li><code>from.node</code>,</li>
  <li><code>from.port</code>,</li>
  <li><code>to.node</code>,</li>
  <li><code>to.port</code>.</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>The source endpoint MUST resolve to an existing output port.</li>
  <li>The target endpoint MUST resolve to an existing input port.</li>
  <li>Both endpoints MUST belong to nodes in the same diagram scope.</li>
  <li>The source and target port types MUST be compatible according to the type system and the referenced primitive or structure rules.</li>
  <li>An ordinary input port MUST NOT have more than one incoming ordinary driver edge unless explicitly allowed by the referenced definition.</li>
  <li>An output port MAY fan out to multiple consumers.</li>
</ul>

<p>
This specification uses the explicit <code>{ "node": "...", "port": "..." }</code> endpoint form because it is durable, tool-friendly, and unambiguous.
</p>

<hr/>

<h2 id="annotations-documentation-and-tags">13. Annotations, Documentation, and Tags</h2>

<p>
The diagram MAY contain source-level annotations, including visible grouping, comments, labels, and author documentation.
These belong to canonical source because they are part of the authored graphical representation.
</p>

<p>
Typical uses include:
</p>

<ul>
  <li>group labels,</li>
  <li>free comments,</li>
  <li>documentation boxes,</li>
  <li>structured tags for tooling, review, or navigation.</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>Annotations MAY be preserved in canonical source.</li>
  <li>Annotations MUST NOT change validated execution semantics.</li>
  <li>Documentation and tags attached to nodes or edges MUST remain semantically non-operative unless another specification explicitly states otherwise.</li>
</ul>

<hr/>

<h2 id="layout-information">14. Layout Information</h2>

<p>
Layout information belongs to canonical source because FROG is a graphical language.
</p>

<p>
Typical layout fields include:
</p>

<ul>
  <li><code>x</code>,</li>
  <li><code>y</code>,</li>
  <li><code>width</code>,</li>
  <li><code>height</code>.</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>Layout metadata MAY be omitted where unnecessary.</li>
  <li>Layout metadata MUST NOT change validated execution semantics.</li>
  <li>Structure layout MAY include size information for editor rendering.</li>
  <li>Implementations MAY normalize purely visual layout details as long as semantic graph identity is preserved.</li>
</ul>

<hr/>

<h2 id="frog-dependencies">15. FROG Dependencies</h2>

<p>
When a diagram invokes other FROGs through <code>subfrog</code> nodes, those external FROGs MUST be declared in <code>diagram.dependencies</code>.
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
  <li><code>name</code> — logical identifier used by <code>subfrog.ref</code>,</li>
  <li><code>path</code> — relative path or equivalent source reference.</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>Dependency names MUST be unique within the owning diagram.</li>
  <li>A <code>subfrog.ref</code> value MUST match one declared dependency name.</li>
  <li>The referenced dependency MUST resolve to a FROG whose interface can define the node boundary.</li>
</ul>

<p>
Future versions MAY extend dependency declarations with versioning, package identifiers, integrity metadata, or repository references.
Such extensions MUST remain compatible with the canonical role of dependency declarations as graph-level invocation references.
</p>

<hr/>

<h2 id="sub-frog-invocation">16. Sub-FROG Invocation</h2>

<p>
A <code>subfrog</code> node is a call site to another FROG.
The call boundary is defined by the referenced dependency interface.
</p>

<p>
Conceptually:
</p>

<pre><code>caller diagram  →  subfrog boundary  →  referenced FROG interface</code></pre>

<p>
Rules:
</p>

<ul>
  <li>The caller graph MUST satisfy the input requirements of the referenced interface.</li>
  <li>The caller graph MAY consume zero or more outputs of the referenced interface.</li>
  <li>A sub-FROG call does not inline hidden ports into the caller beyond the resolved boundary ports.</li>
</ul>

<hr/>

<h2 id="interface-widget-and-structure-boundaries">17. Interface, Widget, and Structure Boundaries</h2>

<h3>17.1 Public interface boundaries</h3>

<p>
Public interface participation in the diagram is represented canonically by:
</p>

<ul>
  <li><code>interface_input</code></li>
  <li><code>interface_output</code></li>
</ul>

<p>
A front-panel widget does not create a public interface port by itself.
Public API semantics belong to the <code>interface</code> section and are made graph-visible by interface boundary nodes.
</p>

<h3>17.2 Widget boundaries</h3>

<p>
Front-panel widget participation is represented canonically by:
</p>

<ul>
  <li><code>widget_value</code> — the natural value path,</li>
  <li><code>widget_reference</code> — the object-style reference path.</li>
</ul>

<p>
A widget MAY expose its primary value both naturally through <code>widget_value</code> and as a property through object-style interaction when the widget class allows it.
Those two paths remain semantically distinct representations.
</p>

<h3>17.3 Structure boundaries</h3>

<p>
A structure creates explicit graph boundaries between its outer scope and its owned regions.
Crossing those boundaries MUST occur only through structure-defined terminals or ports.
Structure semantics define which values enter a region, which values leave a region, and how region-local execution contributes to outer-scope behavior.
</p>

<hr/>

<h2 id="widget-interaction-model">18. Widget Interaction Model</h2>

<p>
Object-style widget interaction is represented canonically as diagram-side primitive nodes together with a <code>widget_reference</code> node.
The standardized primitive identifiers are:
</p>

<ul>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
</ul>

<p>
The natural primary value path remains <code>widget_value</code>.
The object-style path remains:
</p>

<pre><code>widget_reference + frog.ui.property_read / frog.ui.property_write / frog.ui.method_invoke</code></pre>

<p>
Optional sequencing ports <code>ui_in</code> and <code>ui_out</code> MAY be used to impose explicit ordering on UI side effects.
Ordinary value flow and UI sequencing are distinct concerns and MUST NOT be conflated.
</p>

<hr/>

<h2 id="cycles-and-local-state">19. Cycles and Local State</h2>

<p>
A cycle is legal only when it contains valid explicit local memory according to the state-and-cycles specification.
For v0.1, the canonical minimal standard local-memory primitive is <code>frog.core.delay</code>.
</p>

<p>
Rules:
</p>

<ul>
  <li>A pure combinational cycle is invalid.</li>
  <li>A cycle becomes executable only if explicit local memory breaks immediate circular dependency.</li>
  <li>Initial state required by the local-memory primitive MUST be present when mandated by the state specification.</li>
</ul>

<p>
State is attached to node instances inside a live FROG instance, not to static source edges.
</p>

<hr/>

<h2 id="graph-validation">20. Graph Validation</h2>

<h3>20.1 General checks</h3>

<ul>
  <li>All node identifiers MUST be unique within their scope.</li>
  <li>All edge identifiers MUST be unique within their scope.</li>
  <li>All node kinds MUST be valid standardized or otherwise validly extended kinds.</li>
  <li>All referenced primitive, structure, widget, interface, and dependency identifiers MUST resolve.</li>
</ul>

<h3>20.2 Port checks</h3>

<ul>
  <li>Every edge source MUST resolve to an output port.</li>
  <li>Every edge target MUST resolve to an input port.</li>
  <li>Source and target ports MUST be type-compatible.</li>
  <li>An ordinary input port MUST NOT have multiple ordinary drivers unless explicitly allowed by the referenced definition.</li>
</ul>

<h3>20.3 Scope checks</h3>

<ul>
  <li>Edges MUST remain within one diagram scope.</li>
  <li>Cross-scope transfer MUST occur only through explicit structure-defined boundaries.</li>
  <li>Nested region-local nodes and edges MUST be valid within their owning structure.</li>
</ul>

<h3>20.4 Interface participation checks</h3>

<ul>
  <li>Each declared interface input MUST be consumable by the graph.</li>
  <li>Each declared interface output MUST be producible by the graph.</li>
  <li>Canonical source SHOULD represent each declared public interface port through a dedicated matching boundary node.</li>
</ul>

<h3>20.5 Widget participation checks</h3>

<ul>
  <li>A <code>widget_value</code> node MUST reference a value-carrying widget.</li>
  <li>A <code>widget_reference</code> node MUST reference an existing widget.</li>
  <li>Object-style widget interaction MUST use <code>widget_reference</code> plus a valid <code>frog.ui.*</code> primitive.</li>
</ul>

<h3>20.6 Cycle checks</h3>

<ul>
  <li>A pure immediate cycle is invalid.</li>
  <li>A feedback cycle MUST contain valid explicit local memory.</li>
  <li>The local-memory primitive used in a cycle MUST satisfy its own validity rules.</li>
</ul>

<hr/>

<h2 id="execution-semantics">21. Execution Semantics</h2>

<h3>21.1 General model</h3>

<p>
The validated diagram defines a directed executable graph.
Node execution is constrained by:
</p>

<ul>
  <li>ordinary data dependencies,</li>
  <li>structure semantics,</li>
  <li>optional explicit UI sequencing dependencies,</li>
  <li>local-memory semantics where present.</li>
</ul>

<h3>21.2 Ordinary value propagation</h3>

<p>
Ordinary value ports participate in normal dataflow.
A consumer may execute only when the required input values defined by the active profile are available.
For pure dataflow nodes, execution readiness is therefore determined by resolved input availability together with any additional primitive-specific or structure-specific constraints.
</p>

<h3>21.3 Boundary participation</h3>

<p>
Public interface values enter and leave the graph through <code>interface_input</code> and <code>interface_output</code>.
Widget primary values participate through <code>widget_value</code>.
Object-style widget interaction participates through <code>widget_reference</code> plus the standardized <code>frog.ui.*</code> primitives.
</p>

<h3>21.4 UI sequencing</h3>

<p>
The optional <code>ui_in</code> and <code>ui_out</code> ports define explicit sequencing of UI side effects where required.
They do not replace ordinary value dependencies.
A UI action that has side effects MUST respect incoming sequencing dependencies when such dependencies are present.
</p>

<h3>21.5 Structure execution</h3>

<p>
Structure execution semantics are owned by <code>Expression/Control structures.md</code>.
This document only requires that structure participation in the graph be explicit, valid, and canonical.
</p>

<h3>21.6 Local memory and cycles</h3>

<p>
A cycle becomes executable only when the graph contains valid local memory according to the cycle rules.
For <code>frog.core.delay</code>, the observed output is the stored previous value, and the current input becomes the next stored value.
</p>

<h3>21.7 Determinacy of graph meaning</h3>

<p>
For a validated source diagram, graph meaning MUST be determined by canonical source plus referenced specifications.
Purely visual editor presentation MUST NOT alter that meaning.
</p>

<hr/>

<h2 id="examples">22. Examples</h2>

<h3>22.1 Interface input to primitive to interface output</h3>

<pre><code>{
  "interface": {
    "inputs": [
      { "id": "a", "type": "f64" },
      { "id": "b", "type": "f64" }
    ],
    "outputs": [
      { "id": "result", "type": "f64" }
    ]
  },
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
        "id": "add_1",
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
        "to":   { "node": "add_1",   "port": "a" }
      },
      {
        "id": "e2",
        "from": { "node": "input_b", "port": "value" },
        "to":   { "node": "add_1",   "port": "b" }
      },
      {
        "id": "e3",
        "from": { "node": "add_1",         "port": "result" },
        "to":   { "node": "output_result", "port": "value" }
      }
    ]
  }
}</code></pre>

<h3>22.2 Widget value participating in ordinary dataflow</h3>

<pre><code>{
  "front_panel": {
    "widgets": [
      {
        "id": "ctrl_gain",
        "class": "frog.ui.numeric",
        "role": "control",
        "value_type": "f64"
      },
      {
        "id": "ind_result",
        "class": "frog.ui.numeric",
        "role": "indicator",
        "value_type": "f64"
      }
    ]
  },
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
        "type": "frog.core.multiply"
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
        "from": { "node": "input_signal",    "port": "value" },
        "to":   { "node": "mul_1",           "port": "x" }
      },
      {
        "id": "e2",
        "from": { "node": "ctrl_gain_value", "port": "value" },
        "to":   { "node": "mul_1",           "port": "y" }
      },
      {
        "id": "e3",
        "from": { "node": "mul_1",           "port": "result" },
        "to":   { "node": "ind_result_value","port": "value" }
      }
    ]
  }
}</code></pre>

<h3>22.3 Object-style widget property read</h3>

<pre><code>{
  "diagram": {
    "nodes": [
      {
        "id": "ctrl_gain_ref",
        "kind": "widget_reference",
        "widget": "ctrl_gain"
      },
      {
        "id": "read_visible",
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
        "to":   { "node": "read_visible",  "port": "ref" }
      }
    ]
  }
}</code></pre>

<h3>22.4 Object-style widget property write</h3>

<pre><code>{
  "diagram": {
    "nodes": [
      {
        "id": "ctrl_gain_ref",
        "kind": "widget_reference",
        "widget": "ctrl_gain"
      },
      {
        "id": "status_text",
        "kind": "primitive",
        "type": "frog.core.concat"
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
        "from": { "node": "status_text",      "port": "value" },
        "to":   { "node": "write_label_text", "port": "value" }
      },
      {
        "id": "e2",
        "from": { "node": "ctrl_gain_ref",    "port": "ref" },
        "to":   { "node": "write_label_text", "port": "ref" }
      }
    ]
  }
}</code></pre>

<h3>22.5 Valid feedback cycle with local memory</h3>

<pre><code>{
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
        "to":   { "node": "add_1",   "port": "a" }
      },
      {
        "id": "e2",
        "from": { "node": "delay_1", "port": "value" },
        "to":   { "node": "add_1",   "port": "b" }
      },
      {
        "id": "e3",
        "from": { "node": "add_1",   "port": "result" },
        "to":   { "node": "delay_1", "port": "next" }
      },
      {
        "id": "e4",
        "from": { "node": "add_1",    "port": "result" },
        "to":   { "node": "output_y", "port": "value" }
      }
    ]
  }
}</code></pre>

<hr/>

<h2 id="summary">23. Summary</h2>

<p>
For FROG v0.1, the diagram is the canonical executable graph of a <code>.frog</code> program.
It defines nodes, edges, scopes, boundaries, and graph-level participation of interfaces, widgets, sub-FROG calls, and explicit local state.
</p>

<p>
The canonical standard node kinds are:
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

<p>
Ordinary execution follows validated dataflow and structure semantics.
UI side effects MAY use explicit sequencing through <code>ui_in</code> and <code>ui_out</code>.
Cycles are legal only with explicit local memory.
</p>

<p>
In short:
</p>

<pre><code>diagram = authoritative executable graph</code></pre>
