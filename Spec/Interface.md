<h1 align="center">🐸 FROG Interface Specification</h1>

<p align="center">
Definition of program interfaces for <strong>.frog</strong> files<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#purpose">2. Purpose of the Interface</a></li>
  <li><a href="#location">3. Location in a .frog file</a></li>
  <li><a href="#structure">4. Interface Structure</a></li>
  <li><a href="#inputs">5. Input Ports</a></li>
  <li><a href="#outputs">6. Output Ports</a></li>
  <li><a href="#port-properties">7. Port Properties</a></li>
  <li><a href="#input-connection-policy">8. Input Connection Policy</a></li>
  <li><a href="#type-system-integration">9. Type System Integration</a></li>
  <li><a href="#binding-with-the-diagram">10. Binding with the Diagram</a></li>
  <li><a href="#relation-with-connector">11. Relation with Connector</a></li>
  <li><a href="#examples">12. Examples</a></li>
  <li><a href="#validation-rules">13. Validation Rules</a></li>
  <li><a href="#extensibility">14. Extensibility</a></li>
  <li><a href="#summary">15. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <strong>interface</strong> section defines the public logical contract of a Frog.
</p>

<p>
It specifies:
</p>

<ul>
  <li>the public inputs of the program,</li>
  <li>the public outputs of the program,</li>
  <li>their stable identifiers,</li>
  <li>their declared types,</li>
  <li>their connection policy when applicable.</li>
</ul>

<p>
The interface describes how a Frog exchanges data with the outside world and with other Frogs.
It is the logical boundary of the program.
</p>

<p>
The interface does <strong>not</strong> define graphical placement, connector geometry, diagram layout, or execution scheduling.
</p>

<hr/>

<h2 id="purpose">2. Purpose of the Interface</h2>

<p>
The interface provides a stable and explicit contract between reusable program units.
</p>

<p>
It enables:
</p>

<ul>
  <li>composition of Frogs into larger graphs,</li>
  <li>static validation of public connections,</li>
  <li>clear and auditable program boundaries,</li>
  <li>safe reuse across tools, runtimes, and libraries.</li>
</ul>

<p>
The interface is part of the canonical program definition and remains independent from IDE-specific presentation details.
</p>

<hr/>

<h2 id="location">3. Location in a .frog file</h2>

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
The interface object contains two required arrays:
</p>

<ul>
  <li><strong>inputs</strong></li>
  <li><strong>outputs</strong></li>
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
The interface describes the logical contract only.
It does not define where ports are drawn on a reusable node.
That responsibility belongs to the <code>connector</code> section.
</p>

<p>
Port direction is defined structurally:
</p>

<ul>
  <li>a port inside <code>inputs</code> is an input port,</li>
  <li>a port inside <code>outputs</code> is an output port.</li>
</ul>

<p>
No additional <code>direction</code> property is required in v0.1.
</p>

<p>
Both arrays MUST exist, even if one of them is empty.
</p>

<hr/>

<h2 id="inputs">5. Input Ports</h2>

<p>
Input ports represent data entering the Frog from the outside.
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
  <li>Input ports represent externally provided values, signals, events, or equivalent public inputs.</li>
</ul>

<hr/>

<h2 id="outputs">6. Output Ports</h2>

<p>
Output ports represent data produced by the Frog and exposed to the outside.
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
  <li>Output ports represent values, signals, events, or equivalent public outputs made available to other Frogs or hosting environments.</li>
</ul>

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
  <li>MUST remain stable enough to support reuse, validation, connector mapping, and diagram binding.</li>
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
Such metadata does not change the meaning of the interface contract unless explicitly defined by a future specification revision or stricter active profile.
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
The default value, when present, MUST be compatible with the declared port type.
</p>

<p>
A <code>default</code> value provides a fallback when the input is not externally connected and when the active execution or validation profile allows such behavior.
</p>

<p>
This document does not define a separate implicit coercion mechanism for defaults beyond the general type compatibility rules of FROG.
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
  <li>user-defined named types and library-defined custom types are outside the scope of v0.1 unless standardized by a future revision.</li>
</ul>

<hr/>

<h2 id="binding-with-the-diagram">10. Binding with the Diagram</h2>

<p>
Interface ports define the external contract of the Frog and MUST be bound consistently to the internal program graph.
</p>

<p>
A diagram implementation MAY represent interface boundaries using dedicated entry and exit nodes, or any equivalent internal mechanism, provided that the logical interface contract remains preserved.
</p>

<p>
Conceptually:
</p>

<pre>
external input  ->  interface input  ->  diagram
diagram         ->  interface output ->  external output
</pre>

<p>
Rules:
</p>

<ul>
  <li>Each declared interface input MUST be consumable by the diagram.</li>
  <li>Each declared interface output MUST be producible by the diagram.</li>
  <li>Unbound or inconsistent interface definitions MUST trigger validation errors.</li>
  <li>The diagram MUST NOT silently redefine or contradict the declared interface contract.</li>
</ul>

<hr/>

<h2 id="relation-with-connector">11. Relation with Connector</h2>

<p>
The <code>interface</code> section defines the logical public ports of the Frog.
The <code>connector</code> section defines how those ports appear graphically when the Frog is reused as a node inside another diagram.
</p>

<p>
The connector does not redefine the interface.
It only maps existing interface ports to graphical positions on the node perimeter.
</p>

<p>
This mapping is done by referencing the interface port identifier and assigning it to a perimeter <code>slot</code>.
</p>

<pre>
"connector": {
  "granularity": 40,
  "ports": [
    { "interface_port": "a", "slot": 34 },
    { "interface_port": "b", "slot": 36 },
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
  <li>The connector MUST NOT modify port types, connection policy, or interface semantics.</li>
  <li>A port MAY exist in the interface without appearing in the connector if a given tool or profile allows it.</li>
</ul>

<hr/>

<h2 id="examples">12. Examples</h2>

<h3>12.1 Minimal interface</h3>

<pre>
"interface": {
  "inputs": [
    { "id": "a", "type": "f64" }
  ],
  "outputs": [
    { "id": "result", "type": "f64" }
  ]
}
</pre>

<h3>12.2 Interface with optional and recommended inputs</h3>

<pre>
"interface": {
  "inputs": [
    { "id": "temperature", "type": "f64", "connection": "required" },
    { "id": "pressure", "type": "f64", "connection": "recommended" },
    { "id": "enable", "type": "bool", "connection": "optional", "default": true }
  ],
  "outputs": [
    { "id": "density", "type": "f64" },
    { "id": "status", "type": "string" }
  ]
}
</pre>

<h3>12.3 Interface with array types</h3>

<pre>
"interface": {
  "inputs": [
    { "id": "samples", "type": "array<f64>" },
    { "id": "window", "type": "array<f64, 256>", "connection": "recommended" }
  ],
  "outputs": [
    { "id": "spectrum", "type": "array<f64>" }
  ]
}
</pre>

<h3>12.4 Arithmetic node with connector mapping</h3>

<pre>
{
  "interface": {
    "inputs": [
      { "id": "a", "type": "f64", "connection": "required" },
      { "id": "b", "type": "f64", "connection": "required" }
    ],
    "outputs": [
      { "id": "result", "type": "f64" }
    ]
  },
  "connector": {
    "granularity": 40,
    "ports": [
      { "interface_port": "a", "slot": 34 },
      { "interface_port": "b", "slot": 36 },
      { "interface_port": "result", "slot": 14 }
    ]
  }
}
</pre>

<hr/>

<h2 id="validation-rules">13. Validation Rules</h2>

<p>
Implementations MUST enforce the following rules:
</p>

<ul>
  <li><code>interface</code> MUST exist.</li>
  <li><code>inputs</code> and <code>outputs</code> MUST exist and MUST be arrays.</li>
  <li>Each port object MUST define an <code>id</code>.</li>
  <li>Each port object MUST define a <code>type</code>.</li>
  <li>Port identifiers MUST be unique across the whole interface.</li>
  <li>Declared type expressions MUST be syntactically valid according to <code>Type.md</code>.</li>
  <li>The diagram binding MUST be consistent with the declared interface.</li>
</ul>

<p>
Additional rules for input connection policy:
</p>

<ul>
  <li>if <code>connection</code> is present, it MUST be one of <code>required</code>, <code>recommended</code>, or <code>optional</code>,</li>
  <li>if <code>connection</code> is omitted on an input, it MUST be interpreted as <code>required</code>,</li>
  <li>if <code>default</code> is present, it MUST be compatible with the declared input type,</li>
  <li>an unconnected <code>required</code> input MUST trigger a validation error unless the active profile defines an allowed fallback,</li>
  <li>an unconnected <code>recommended</code> input SHOULD trigger a warning or equivalent diagnostic,</li>
  <li>an unconnected <code>optional</code> input MUST NOT trigger a validation error solely because it is unconnected.</li>
</ul>

<p>
When a connector is present:
</p>

<ul>
  <li>each referenced <code>interface_port</code> MUST exist in the interface,</li>
  <li>connector mappings MUST remain compatible with the interface definition.</li>
</ul>

<p>
Unknown properties MUST be ignored unless a stricter profile explicitly defines them.
</p>

<hr/>

<h2 id="extensibility">14. Extensibility</h2>

<p>
Tools and libraries MAY add additional non-breaking metadata fields to port definitions.
</p>

<pre>
{
  "id": "speed",
  "type": "f64",
  "connection": "recommended",
  "unit": "m/s",
  "description": "Measured linear speed"
}
</pre>

<p>
Examples of such metadata may include:
</p>

<ul>
  <li>human-readable descriptions,</li>
  <li>units,</li>
  <li>default values,</li>
  <li>editor hints,</li>
  <li>documentation annotations.</li>
</ul>

<p>
Runtime systems and validators that do not understand these extra properties MUST ignore them unless a stricter profile specifies otherwise.
</p>

<hr/>

<h2 id="summary">15. Summary</h2>

<p>
The interface defines the external logical contract of a Frog.
</p>

<p>
It provides:
</p>

<ul>
  <li>clear program boundaries,</li>
  <li>type-aware composition,</li>
  <li>stable port identifiers,</li>
  <li>explicit input connection policy,</li>
  <li>a foundation for reusable graphical nodes.</li>
</ul>

<p>
The interface describes <strong>what</strong> a Frog exposes.
The connector describes <strong>where</strong> those ports appear graphically.
The diagram defines how those public ports are bound to internal execution logic.
Together, they allow Frogs to be safely validated, reused, and composed into larger executable graphs.
</p>
