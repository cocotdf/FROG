<h1 align="center">🐸 FROG Interface Specification</h1>

<p align="center">
Definition of public program interfaces for <strong>.frog</strong> files<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#purpose">2. Purpose of the Interface</a></li>
  <li><a href="#location">3. Location in a <code>.frog</code> File</a></li>
  <li><a href="#structure">4. Interface Structure</a></li>
  <li><a href="#inputs">5. Input Ports</a></li>
  <li><a href="#outputs">6. Output Ports</a></li>
  <li><a href="#port-properties">7. Port Properties</a></li>
  <li><a href="#input-connection-policy">8. Input Connection Policy</a></li>
  <li><a href="#type-system-integration">9. Type System Integration</a></li>
  <li><a href="#reserved-and-future-oriented-properties">10. Reserved and Future-Oriented Properties</a></li>
  <li><a href="#relation-with-the-diagram">11. Relation with the Diagram</a></li>
  <li><a href="#relation-with-the-connector">12. Relation with the Connector</a></li>
  <li><a href="#relation-with-the-front-panel">13. Relation with the Front Panel</a></li>
  <li><a href="#examples">14. Examples</a></li>
  <li><a href="#validation-rules">15. Validation Rules</a></li>
  <li><a href="#extensibility">16. Extensibility</a></li>
  <li><a href="#summary">17. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <code>interface</code> section defines the public logical contract of a FROG program.
</p>

<p>
It specifies:
</p>

<ul>
  <li>the public inputs of the program,</li>
  <li>the public outputs of the program,</li>
  <li>their stable identifiers,</li>
  <li>their declared types,</li>
  <li>their public connection expectations when applicable.</li>
</ul>

<p>
The interface defines how a FROG exchanges data with the outside world and with other FROGs.
It is the public boundary of the executable unit.
</p>

<p>
The interface does not define:
</p>

<ul>
  <li>diagram layout,</li>
  <li>connector geometry,</li>
  <li>front-panel layout,</li>
  <li>widget rendering details,</li>
  <li>execution scheduling.</li>
</ul>

<hr/>

<h2 id="purpose">2. Purpose of the Interface</h2>

<p>
The interface provides a stable and explicit contract between reusable program units.
</p>

<p>
It enables:
</p>

<ul>
  <li>composition of FROGs into larger graphs,</li>
  <li>static validation of public connections,</li>
  <li>clear and auditable program boundaries,</li>
  <li>safe reuse across tools, runtimes, and libraries.</li>
</ul>

<p>
The interface is part of the canonical source definition of a FROG.
It remains independent from IDE-specific presentation details and from non-authoritative cache artifacts.
</p>

<hr/>

<h2 id="location">3. Location in a <code>.frog</code> File</h2>

<p>
The interface is defined as a top-level JSON object.
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
The <code>interface</code> section MUST be present in a canonical <code>.frog</code> source file.
</p>

<hr/>

<h2 id="structure">4. Interface Structure</h2>

<p>
The <code>interface</code> object contains two required arrays:
</p>

<ul>
  <li><code>inputs</code></li>
  <li><code>outputs</code></li>
</ul>

<p>
Each entry in these arrays defines one public interface port.
</p>

<pre>
"interface": {
  "inputs": [],
  "outputs": []
}
</pre>

<p>
Rules:
</p>

<ul>
  <li><code>inputs</code> MUST exist and MUST be an array.</li>
  <li><code>outputs</code> MUST exist and MUST be an array.</li>
  <li>Each entry in either array MUST be an object.</li>
  <li>Port direction is defined structurally by array membership.</li>
</ul>

<p>
A port listed in <code>inputs</code> is an input port.
A port listed in <code>outputs</code> is an output port.
No separate <code>direction</code> property is required in v0.1.
</p>

<p>
The interface defines the logical contract only.
It does not define graphical placement on reusable nodes.
That responsibility belongs to the <code>connector</code> section.
</p>

<hr/>

<h2 id="inputs">5. Input Ports</h2>

<p>
Input ports represent data entering the FROG from the outside.
</p>

<pre>
"inputs": [
  {
    "id": "a",
    "type": "f64"
  },
  {
    "id": "b",
    "type": "f64"
  }
]
</pre>

<p>
Rules:
</p>

<ul>
  <li>Each input port MUST define an <code>id</code>.</li>
  <li>Each input port MUST define a <code>type</code>.</li>
  <li>Input port identifiers MUST be unique across the whole interface.</li>
  <li>Input ports MAY additionally define supported input-only properties such as <code>connection</code> and <code>default</code>.</li>
</ul>

<p>
Input ports represent externally provided values, signals, commands, events, or equivalent public inputs.
</p>

<hr/>

<h2 id="outputs">6. Output Ports</h2>

<p>
Output ports represent data produced by the FROG and exposed to the outside.
</p>

<pre>
"outputs": [
  {
    "id": "result",
    "type": "f64"
  }
]
</pre>

<p>
Rules:
</p>

<ul>
  <li>Each output port MUST define an <code>id</code>.</li>
  <li>Each output port MUST define a <code>type</code>.</li>
  <li>Output port identifiers MUST be unique across the whole interface.</li>
  <li>Output ports MUST NOT define input-only properties such as <code>connection</code> or <code>default</code> in v0.1.</li>
</ul>

<p>
Output ports represent values, signals, events, status, or equivalent public outputs made available to other FROGs or to hosting environments.
</p>

<hr/>

<h2 id="port-properties">7. Port Properties</h2>

<p>
Each port object contains required logical properties and MAY contain additional metadata.
</p>

<h3>7.1 <code>id</code></h3>

<p>
Unique logical identifier of the port.
</p>

<pre>
"id": "temperature"
</pre>

<p>
Rules:
</p>

<ul>
  <li>MUST be a string.</li>
  <li>MUST be unique across all interface ports, including both inputs and outputs.</li>
  <li>MUST remain stable enough to support reuse, validation, connector mapping, and diagram boundary mapping.</li>
</ul>

<h3>7.2 <code>type</code></h3>

<p>
Declared type of the port.
</p>

<pre>
"type": "f64"
</pre>

<p>
Rules:
</p>

<ul>
  <li>MUST be a valid FROG type expression.</li>
  <li>MUST use the canonical type syntax defined by <code>Type.md</code>.</li>
  <li>MUST be sufficient for static compatibility checks.</li>
</ul>

<h3>7.3 Optional metadata</h3>

<p>
Additional metadata MAY be attached to a port.
</p>

<pre>
{
  "id": "gain",
  "type": "f64",
  "description": "Gain factor"
}
</pre>

<p>
Such metadata does not change the meaning of the public contract unless explicitly defined by a future specification revision or a stricter active profile.
</p>

<h3>7.4 Port order</h3>

<p>
The logical identity of a port is defined by its <code>id</code>, not by its array position.
</p>

<p>
Tools MAY preserve array order for presentation, documentation, or default connector generation.
Array order alone MUST NOT redefine interface semantics.
</p>

<hr/>

<h2 id="input-connection-policy">8. Input Connection Policy</h2>

<p>
Input ports MAY define a <code>connection</code> property to express how strongly an external connection is expected.
</p>

<pre>
{
  "id": "gain",
  "type": "f64",
  "connection": "optional",
  "default": 1.0
}
</pre>

<p>
Allowed values are:
</p>

<ul>
  <li><code>required</code></li>
  <li><code>recommended</code></li>
  <li><code>optional</code></li>
</ul>

<h3>8.1 <code>required</code></h3>

<p>
The input is expected to be connected.
If it is not connected, validation MUST fail unless another rule in the active profile explicitly defines a valid fallback behavior.
</p>

<h3>8.2 <code>recommended</code></h3>

<p>
The input is intended to be connected in normal use.
If it is left unconnected, validation MAY succeed, but tools SHOULD emit a warning, lint message, or equivalent diagnostic.
</p>

<h3>8.3 <code>optional</code></h3>

<p>
The input may be left unconnected without producing a validation error.
A default value MAY be provided when appropriate.
</p>

<h3>8.4 Default behavior</h3>

<p>
If <code>connection</code> is omitted on an input port, the default value is <code>required</code>.
</p>

<h3>8.5 Use on outputs</h3>

<p>
The <code>connection</code> property applies to input ports only in v0.1.
Output ports do not use <code>required</code>, <code>recommended</code>, or <code>optional</code> in this specification version.
</p>

<h3>8.6 <code>default</code></h3>

<p>
An input port MAY define a <code>default</code> value.
</p>

<pre>
{
  "id": "enable",
  "type": "bool",
  "connection": "optional",
  "default": true
}
</pre>

<p>
Rules:
</p>

<ul>
  <li>The default value, when present, MUST be compatible with the declared port type.</li>
  <li>A <code>default</code> value provides a fallback only when the input is not externally connected and when the active validation or execution profile allows such behavior.</li>
  <li>This document does not define a separate implicit coercion mechanism for defaults beyond the general type compatibility rules of FROG.</li>
</ul>

<p>
A <code>default</code> property on an output port is not valid in v0.1.
</p>

<hr/>

<h2 id="type-system-integration">9. Type System Integration</h2>

<p>
The interface relies normatively on the FROG type system defined in <code>Type.md</code>.
</p>

<p>
Examples of valid type expressions in v0.1 include:
</p>

<pre>
bool
i32
f64
string
array&lt;f64&gt;
array&lt;u8, 1024&gt;
</pre>

<p>
Type identity, type compatibility, and implicit coercion behavior are not redefined here.
They MUST follow the rules defined in the FROG type specification.
</p>

<p>
In particular:
</p>

<ul>
  <li>canonical type names such as <code>i32</code> and <code>f64</code> MUST be used,</li>
  <li>non-canonical aliases such as <code>int32</code>, <code>float64</code>, or <code>double</code> are not valid canonical type expressions in v0.1,</li>
  <li>user-defined named types and library-defined custom types are outside the scope of v0.1 unless standardized by a future revision or stricter profile.</li>
</ul>

<hr/>

<h2 id="reserved-and-future-oriented-properties">10. Reserved and Future-Oriented Properties</h2>

<p>
Some concepts commonly found in graphical programming systems are intentionally not standardized in the base v0.1 interface contract.
</p>

<h3>10.1 <code>direction</code></h3>

<p>
A separate <code>direction</code> property is unnecessary in v0.1 because direction is already defined by membership in <code>inputs</code> or <code>outputs</code>.
</p>

<p>
If a tool emits a redundant <code>direction</code> property, consumers SHOULD ignore it unless a stricter profile explicitly defines it.
</p>

<h3>10.2 Dispatch semantics</h3>

<p>
Concepts such as <code>static</code> versus <code>dynamic</code> dispatch for class-like or method-like reusable units are outside the scope of the base interface specification in v0.1.
</p>

<p>
Such semantics MAY be introduced later by a dedicated object model, class system, or stricter profile.
Until then, interface ports MUST NOT assume dispatch behavior solely from interface metadata.
</p>

<h3>10.3 Type adaptation semantics</h3>

<p>
Concepts such as <code>fixed</code> versus <code>adapt_to_type</code> are also outside the scope of the base v0.1 interface contract.
</p>

<p>
Future specifications MAY define controlled polymorphism, generic nodes, or type-adaptive ports.
Until then, declared port types are considered explicit and fixed for validation purposes.
</p>

<hr/>

<h2 id="relation-with-the-diagram">11. Relation with the Diagram</h2>

<p>
The interface defines the external contract of the FROG and MUST be reflected consistently inside the executable graph.
</p>

<p>
In v0.1, public interface participation in the diagram is represented canonically by dedicated boundary node kinds:
</p>

<ul>
  <li><code>interface_input</code> — entry point of a declared public input inside the graph,</li>
  <li><code>interface_output</code> — exit point used to drive a declared public output from the graph.</li>
</ul>

<p>
Conceptually:
</p>

<pre>
external input  → interface_input.value   → internal graph
internal graph  → interface_output.value  → external output
</pre>

<p>
Rules:
</p>

<ul>
  <li>An <code>interface_input</code> node MUST reference an existing interface input through <code>interface_port</code>.</li>
  <li>An <code>interface_output</code> node MUST reference an existing interface output through <code>interface_port</code>.</li>
  <li>An <code>interface_input</code> node exposes exactly one output port named <code>value</code>.</li>
  <li>An <code>interface_output</code> node exposes exactly one input port named <code>value</code>.</li>
  <li>Each declared interface input MUST be consumable by the graph.</li>
  <li>Each declared interface output MUST be producible by the graph.</li>
  <li>Unbound, contradictory, or unreachable interface boundary definitions MUST trigger validation errors.</li>
  <li>The diagram MUST NOT silently redefine or contradict the declared interface contract.</li>
</ul>

<p>
For canonical source authoring, tools SHOULD represent each declared public interface port through a dedicated matching boundary node in the owning diagram.
A stricter profile MAY strengthen this recommendation.
</p>

<hr/>

<h2 id="relation-with-the-connector">12. Relation with the Connector</h2>

<p>
The <code>interface</code> section defines the logical public ports of the FROG.
The <code>connector</code> section defines how those ports appear graphically when the FROG is reused as a node inside another diagram.
</p>

<p>
The connector does not redefine the interface.
It only maps existing interface ports to graphical positions on the reusable node boundary.
</p>

<p>
This mapping is done by referencing the interface port identifier and assigning it to a perimeter <code>slot</code>.
</p>

<pre>
"connector": {
  "granularity": 40,
  "ports": [
    { "interface_port": "a", "slot": 82 },
    { "interface_port": "b", "slot": 94 },
    { "interface_port": "result", "slot": 14 }
  ]
}
</pre>

<p>
Rules:
</p>

<ul>
  <li>Each <code>interface_port</code> value in the connector MUST reference an existing port declared in <code>interface</code>.</li>
  <li>The connector MUST NOT introduce new logical ports.</li>
  <li>The connector MUST NOT modify port types, connection policy, or public interface semantics.</li>
  <li>A port MAY exist in the interface without appearing in the connector if a given tool or active profile allows it.</li>
</ul>

<hr/>

<h2 id="relation-with-the-front-panel">13. Relation with the Front Panel</h2>

<p>
The <code>front_panel</code> section defines interactive user-facing widgets and layout.
It is not a substitute for the public program interface.
</p>

<p>
A front panel MAY expose, drive, or display values related to interface ports, but it MUST NOT redefine the public logical contract of the program.
</p>

<p>
In particular:
</p>

<ul>
  <li>an interface input remains an interface input even if no front-panel widget reflects it,</li>
  <li>an interface output remains an interface output even if no front-panel widget reflects it,</li>
  <li>a front-panel widget does not create a public interface port by itself.</li>
</ul>

<p>
FROG distinguishes the public interface contract from front-panel interaction:
</p>

<ul>
  <li>public interface participation uses <code>interface_input</code> and <code>interface_output</code> nodes,</li>
  <li>primary widget value participation uses <code>widget_value</code> nodes,</li>
  <li>object-style widget access uses <code>widget_reference</code> nodes together with <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code>.</li>
</ul>

<p>
The interface defines what the program exposes publicly.
The front panel defines how a user may interact with some program data visually.
The diagram is where both become structurally connected to executable logic.
</p>

<hr/>

<h2 id="examples">14. Examples</h2>

<h3>14.1 Minimal numeric interface</h3>

<pre>
"interface": {
  "inputs": [
    { "id": "a", "type": "f64" },
    { "id": "b", "type": "f64" }
  ],
  "outputs": [
    { "id": "sum", "type": "f64" }
  ]
}
</pre>

<h3>14.2 Optional input with default value</h3>

<pre>
"interface": {
  "inputs": [
    { "id": "signal", "type": "f64" },
    { "id": "gain", "type": "f64", "connection": "optional", "default": 1.0 }
  ],
  "outputs": [
    { "id": "scaled", "type": "f64" }
  ]
}
</pre>

<h3>14.3 Interface aligned with canonical diagram boundary nodes</h3>

<pre>
"interface": {
  "inputs": [
    { "id": "samples", "type": "array&lt;f64&gt;" },
    { "id": "gain", "type": "f64", "connection": "recommended", "default": 1.0 }
  ],
  "outputs": [
    { "id": "scaled", "type": "array&lt;f64&gt;" }
  ]
},
"diagram": {
  "nodes": [
    {
      "id": "input_samples",
      "kind": "interface_input",
      "interface_port": "samples"
    },
    {
      "id": "input_gain",
      "kind": "interface_input",
      "interface_port": "gain"
    },
    {
      "id": "mul_1",
      "kind": "primitive",
      "type": "frog.core.mul"
    },
    {
      "id": "output_scaled",
      "kind": "interface_output",
      "interface_port": "scaled"
    }
  ]
}
</pre>

<hr/>

<h2 id="validation-rules">15. Validation Rules</h2>

<p>
The following rules apply to the base v0.1 interface contract:
</p>

<ul>
  <li>the <code>interface</code> section MUST exist,</li>
  <li><code>inputs</code> and <code>outputs</code> MUST exist and MUST be arrays,</li>
  <li>every port object MUST define <code>id</code> and <code>type</code>,</li>
  <li>every port identifier MUST be unique across the whole interface,</li>
  <li>every declared <code>type</code> MUST be a valid canonical FROG type expression,</li>
  <li>if present on an input, <code>connection</code> MUST be one of <code>required</code>, <code>recommended</code>, or <code>optional</code>,</li>
  <li>if omitted on an input, <code>connection</code> defaults to <code>required</code>,</li>
  <li>if present, <code>default</code> MUST be type-compatible with the declared input type,</li>
  <li><code>default</code> MUST NOT appear on outputs in v0.1,</li>
  <li><code>connection</code> MUST NOT appear on outputs in v0.1,</li>
  <li>the diagram MUST remain consistent with the declared interface contract,</li>
  <li>each declared interface input MUST be consumable by the graph,</li>
  <li>each declared interface output MUST be producible by the graph.</li>
</ul>

<p>
Unknown additional properties MAY be ignored unless a stricter active profile defines them.
</p>

<hr/>

<h2 id="extensibility">16. Extensibility</h2>

<p>
The interface model is intentionally minimal in v0.1.
It defines the public contract required for composition, validation, and execution boundary mapping.
</p>

<p>
Future revisions or stricter profiles MAY extend the model with concepts such as:
</p>

<ul>
  <li>generic or type-parameterized public ports,</li>
  <li>dispatch-aware reusable units,</li>
  <li>class-oriented method interfaces,</li>
  <li>richer public metadata for documentation and tooling,</li>
  <li>profile-specific contract qualifiers.</li>
</ul>

<p>
Such extensions MUST remain compatible with the principle that the interface defines the public logical contract, while diagram structure, front-panel interaction, and connector presentation remain distinct concerns.
</p>

<hr/>

<h2 id="summary">17. Summary</h2>

<p>
The <code>interface</code> section defines the public data contract of a FROG.
</p>

<ul>
  <li>It declares public inputs and outputs.</li>
  <li>It assigns stable identifiers and canonical types to those ports.</li>
  <li>It may express input connection expectations and defaults.</li>
  <li>It maps to the executable graph through canonical <code>interface_input</code> and <code>interface_output</code> diagram nodes.</li>
  <li>It remains distinct from connector geometry and front-panel UI composition.</li>
</ul>

<p>
This separation provides a clean and durable foundation for reusable graphical programs, independent tools, and long-term language evolution.
</p>
