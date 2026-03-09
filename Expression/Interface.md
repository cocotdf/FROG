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
  <li><a href="#connection-policy">8. Input Connection Policy</a></li>
  <li><a href="#type-system">9. Type System Integration</a></li>
  <li><a href="#reserved">10. Reserved and Future-Oriented Properties</a></li>
  <li><a href="#diagram-binding">11. Binding with the Diagram</a></li>
  <li><a href="#connector-relation">12. Relation with the Connector</a></li>
  <li><a href="#front-panel-relation">13. Relation with the Front Panel</a></li>
  <li><a href="#examples">14. Examples</a></li>
  <li><a href="#validation-rules">15. Validation Rules</a></li>
  <li><a href="#extensibility">16. Extensibility</a></li>
  <li><a href="#summary">17. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <strong>interface</strong> section defines the public logical contract of a FROG program.
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
The interface describes how a FROG exchanges data with the outside world and with other FROGs.
It is the logical boundary of the program.
</p>

<p>
The interface does <strong>not</strong> define graphical placement, connector geometry, diagram layout,
UI widget layout, or execution scheduling.
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
  <li>composition of FROGs into larger graphs,</li>
  <li>static validation of public connections,</li>
  <li>clear and auditable program boundaries,</li>
  <li>safe reuse across tools, runtimes, and libraries.</li>
</ul>

<p>
The interface is part of the canonical program definition.
It remains independent from IDE-specific presentation details and from cache artifacts.
</p>

<hr/>

<h2 id="location">3. Location in a <code>.frog</code> File</h2>

<p>
The interface is defined as a top-level JSON object.
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
The <code>interface</code> section <strong>MUST</strong> be present in a canonical <code>.frog</code> source file.
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

<pre><code>"interface": {
  "inputs": [],
  "outputs": []
}</code></pre>

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
Both arrays <strong>MUST</strong> exist, even if one of them is empty.
</p>

<hr/>

<h2 id="inputs">5. Input Ports</h2>

<p>
Input ports represent data entering the FROG from the outside.
</p>

<pre><code>"inputs": [
  {
    "id": "a",
    "type": "f64"
  },
  {
    "id": "b",
    "type": "f64"
  }
]</code></pre>

<p>
Rules:
</p>

<ul>
  <li>Each input port <strong>MUST</strong> define an <code>id</code>.</li>
  <li>Each input port <strong>MUST</strong> define a <code>type</code>.</li>
  <li>Input port identifiers <strong>MUST</strong> be unique across the whole interface.</li>
  <li>Input ports represent externally provided values, signals, events, commands, or equivalent public inputs.</li>
</ul>

<hr/>

<h2 id="outputs">6. Output Ports</h2>

<p>
Output ports represent data produced by the FROG and exposed to the outside.
</p>

<pre><code>"outputs": [
  {
    "id": "result",
    "type": "f64"
  }
]</code></pre>

<p>
Rules:
</p>

<ul>
  <li>Each output port <strong>MUST</strong> define an <code>id</code>.</li>
  <li>Each output port <strong>MUST</strong> define a <code>type</code>.</li>
  <li>Output port identifiers <strong>MUST</strong> be unique across the whole interface.</li>
  <li>Output ports represent values, signals, events, status, or equivalent public outputs made available to other FROGs or hosting environments.</li>
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

<pre><code>"id": "temperature"</code></pre>

<p>
Rules:
</p>

<ul>
  <li><strong>MUST</strong> be a string.</li>
  <li><strong>MUST</strong> be unique across all interface ports, including both inputs and outputs.</li>
  <li><strong>MUST</strong> remain stable enough to support reuse, validation, connector mapping, and diagram binding.</li>
</ul>

<h3>7.2 <code>type</code></h3>

<p>
Declared type of the port.
</p>

<pre><code>"type": "f64"</code></pre>

<p>
Rules:
</p>

<ul>
  <li><strong>MUST</strong> be a valid FROG type expression.</li>
  <li><strong>MUST</strong> use the canonical type syntax defined by <code>Type.md</code>.</li>
  <li><strong>MUST</strong> be sufficient for static compatibility checks.</li>
</ul>

<h3>7.3 Optional metadata</h3>

<p>
Additional metadata MAY be attached to a port.
</p>

<pre><code>{
  "id": "gain",
  "type": "f64",
  "description": "Gain factor"
}</code></pre>

<p>
Such metadata does not change the meaning of the interface contract unless explicitly defined by a future specification revision or a stricter active profile.
</p>

<h3>7.4 Port order</h3>

<p>
The logical identity of a port is defined by its <code>id</code>, not by its array position.
</p>

<p>
However, tools MAY preserve array order for presentation, documentation, or default connector generation.
Array order alone <strong>MUST NOT</strong> redefine interface semantics.
</p>

<hr/>

<h2 id="connection-policy">8. Input Connection Policy</h2>

<p>
Input ports MAY define a <code>connection</code> property to express how strongly an external connection is expected.
</p>

<pre><code>{
  "id": "gain",
  "type": "f64",
  "connection": "optional",
  "default": 1.0
}</code></pre>

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
If it is not connected, validation <strong>MUST</strong> fail unless another rule in the active profile explicitly defines a valid fallback behavior.
</p>

<h3>8.2 <code>recommended</code></h3>

<p>
The input is intended to be connected in normal use.
If it is left unconnected, validation MAY succeed, but tools <strong>SHOULD</strong> emit a warning, lint message, or equivalent diagnostic.
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

<pre><code>{
  "id": "enable",
  "type": "bool",
  "connection": "optional",
  "default": true
}</code></pre>

<p>
The default value, when present, <strong>MUST</strong> be compatible with the declared port type.
</p>

<p>
A <code>default</code> value provides a fallback when the input is not externally connected and when the active execution or validation profile allows such behavior.
</p>

<p>
This document does not define a separate implicit coercion mechanism for defaults beyond the general type compatibility rules of FROG.
</p>

<p>
A <code>default</code> property on an output port is not valid in v0.1.
</p>

<hr/>

<h2 id="type-system">9. Type System Integration</h2>

<p>
The interface relies normatively on the FROG type system defined in <code>Type.md</code>.
</p>

<p>
Examples of valid type expressions in v0.1 include:
</p>

<pre><code>bool
i32
f64
string
array&lt;f64&gt;
array&lt;u8, 1024&gt;</code></pre>

<p>
Type identity, type compatibility, and implicit coercion behavior are not redefined here.
They <strong>MUST</strong> follow the rules defined in the FROG type specification.
</p>

<p>
In particular:
</p>

<ul>
  <li>canonical type names such as <code>i32</code> and <code>f64</code> <strong>MUST</strong> be used,</li>
  <li>non-canonical aliases such as <code>int32</code>, <code>float64</code>, or <code>double</code> are not valid canonical type expressions in v0.1,</li>
  <li>user-defined named types and library-defined custom types are outside the scope of v0.1 unless standardized by a future revision or stricter profile.</li>
</ul>

<hr/>

<h2 id="reserved">10. Reserved and Future-Oriented Properties</h2>

<p>
Some concepts commonly found in graphical programming systems are intentionally not standardized in the base v0.1 interface contract.
</p>

<h3>10.1 <code>direction</code></h3>

<p>
A separate <code>direction</code> property is unnecessary in v0.1 because direction is already defined by membership in <code>inputs</code> or <code>outputs</code>.
</p>

<p>
If a tool emits a redundant <code>direction</code> property, consumers <strong>SHOULD</strong> ignore it unless a stricter profile explicitly defines it.
</p>

<h3>10.2 Dispatch semantics</h3>

<p>
Concepts such as <code>static</code> versus <code>dynamic</code> dispatch for class-like or method-like reusable units are outside the scope of the base interface specification in v0.1.
</p>

<p>
Such semantics MAY be introduced later by a dedicated object model, class system, or stricter profile.
Until then, interface ports <strong>MUST NOT</strong> assume dispatch behavior solely from interface metadata.
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

<h2 id="diagram-binding">11. Binding with the Diagram</h2>

<p>
Interface ports define the external contract of the FROG and <strong>MUST</strong> be bound consistently to the internal program graph.
</p>

<p>
A diagram implementation MAY represent interface boundaries using dedicated entry and exit nodes, or any equivalent internal mechanism, provided that the logical interface contract remains preserved.
</p>

<p>
Conceptually:
</p>

<pre><code>external input  -&gt; interface input  -&gt; diagram
diagram         -&gt; interface output -&gt; external output</code></pre>

<p>
Rules:
</p>

<ul>
  <li>Each declared interface input <strong>MUST</strong> be consumable by the diagram.</li>
  <li>Each declared interface output <strong>MUST</strong> be producible by the diagram.</li>
  <li>Unbound or inconsistent interface definitions <strong>MUST</strong> trigger validation errors.</li>
  <li>The diagram <strong>MUST NOT</strong> silently redefine or contradict the declared interface contract.</li>
</ul>

<hr/>

<h2 id="connector-relation">12. Relation with the Connector</h2>

<p>
The <code>interface</code> section defines the logical public ports of the FROG.
The <code>connector</code> section defines how those ports appear graphically when the FROG is reused as a node inside another diagram.
</p>

<p>
The connector does not redefine the interface.
It only maps existing interface ports to graphical positions on the node perimeter.
</p>

<p>
This mapping is done by referencing the interface port identifier and assigning it to a perimeter <code>slot</code>.
</p>

<pre><code>"connector": {
  "granularity": 40,
  "ports": [
    { "interface_port": "a", "slot": 82 },
    { "interface_port": "b", "slot": 94 },
    { "interface_port": "result", "slot": 14 }
  ]
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li>Each <code>interface_port</code> value in the connector <strong>MUST</strong> reference an existing port declared in <code>interface</code>.</li>
  <li>The connector <strong>MUST NOT</strong> introduce new logical ports.</li>
  <li>The connector <strong>MUST NOT</strong> modify port types, connection policy, or interface semantics.</li>
  <li>A port MAY exist in the interface without appearing in the connector if a given tool or profile allows it.</li>
</ul>

<hr/>

<h2 id="front-panel-relation">13. Relation with the Front Panel</h2>

<p>
The <code>front_panel</code> section defines interactive user-facing widgets and layout.
It is not a substitute for the program interface.
</p>

<p>
A front panel MAY expose, drive, or display values related to interface ports, but the front panel <strong>MUST NOT</strong> redefine the public logical contract of the program.
</p>

<p>
In particular:
</p>

<ul>
  <li>an interface input remains an interface input even if no front panel control is bound to it,</li>
  <li>an interface output remains an interface output even if no front panel indicator is bound to it,</li>
  <li>a widget binding does not create a new public interface port by itself.</li>
</ul>

<p>
The interface defines what the program exposes logically.
The front panel defines how a user may interact with some of that data visually.
</p>

<hr/>

<h2 id="examples">14. Examples</h2>

<h3>14.1 Minimal interface</h3>

<pre><code>"interface": {
  "inputs": [
    { "id": "a", "type": "f64" }
  ],
  "outputs": [
    { "id": "result", "type": "f64" }
  ]
}</code></pre>

<h3>14.2 Interface with optional and recommended inputs</h3>

<pre><code>"interface": {
  "inputs": [
    { "id": "temperature", "type": "f64", "connection": "required" },
    { "id": "pressure", "type": "f64", "connection": "recommended" },
    { "id": "enable", "type": "bool", "connection": "optional", "default": true }
  ],
  "outputs": [
    { "id": "density", "type": "f64" },
    { "id": "status", "type": "string" }
  ]
}</code></pre>

<h3>14.3 Interface with array types</h3>

<pre><code>"interface": {
  "inputs": [
    { "id": "samples", "type": "array&lt;f64&gt;" },
    { "id": "window", "type": "array&lt;f64, 256&gt;", "connection": "recommended" }
  ],
  "outputs": [
    { "id": "spectrum", "type": "array&lt;f64&gt;" }
  ]
}</code></pre>

<h3>14.4 Interface with descriptive metadata</h3>

<pre><code>"interface": {
  "inputs": [
    {
      "id": "speed",
      "type": "f64",
      "connection": "recommended",
      "unit": "m/s",
      "description": "Measured linear speed"
    }
  ],
  "outputs": [
    {
      "id": "speed_ok",
      "type": "bool",
      "description": "True when speed is within range"
    }
  ]
}</code></pre>

<h3>14.5 Arithmetic node with connector mapping</h3>

<pre><code>{
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
      { "interface_port": "a", "slot": 82 },
      { "interface_port": "b", "slot": 94 },
      { "interface_port": "result", "slot": 14 }
    ]
  }
}</code></pre>

<hr/>

<h2 id="validation-rules">15. Validation Rules</h2>

<p>
Implementations <strong>MUST</strong> enforce the following rules:
</p>

<ul>
  <li><code>interface</code> <strong>MUST</strong> exist.</li>
  <li><code>inputs</code> and <code>outputs</code> <strong>MUST</strong> exist and <strong>MUST</strong> be arrays.</li>
  <li>Each port object <strong>MUST</strong> define an <code>id</code>.</li>
  <li>Each port object <strong>MUST</strong> define a <code>type</code>.</li>
  <li>Port identifiers <strong>MUST</strong> be unique across the whole interface.</li>
  <li>Declared type expressions <strong>MUST</strong> be syntactically valid according to <code>Type.md</code>.</li>
  <li>The diagram binding <strong>MUST</strong> be consistent with the declared interface.</li>
</ul>

<p>
Additional rules for input connection policy:
</p>

<ul>
  <li>if <code>connection</code> is present, it <strong>MUST</strong> be one of <code>required</code>, <code>recommended</code>, or <code>optional</code>,</li>
  <li>if <code>connection</code> is omitted on an input, it <strong>MUST</strong> be interpreted as <code>required</code>,</li>
  <li>if <code>default</code> is present, it <strong>MUST</strong> be compatible with the declared input type,</li>
  <li>an unconnected <code>required</code> input <strong>MUST</strong> trigger a validation error unless the active profile defines an allowed fallback,</li>
  <li>an unconnected <code>recommended</code> input <strong>SHOULD</strong> trigger a warning or equivalent diagnostic,</li>
  <li>an unconnected <code>optional</code> input <strong>MUST NOT</strong> trigger a validation error solely because it is unconnected,</li>
  <li><code>connection</code> and <code>default</code> on output ports are not valid in v0.1.</li>
</ul>

<p>
When a connector is present:
</p>

<ul>
  <li>each referenced <code>interface_port</code> <strong>MUST</strong> exist in the interface,</li>
  <li>connector mappings <strong>MUST</strong> remain compatible with the interface definition.</li>
</ul>

<p>
Unknown properties <strong>MUST</strong> be ignored unless a stricter profile explicitly defines them.
</p>

<hr/>

<h2 id="extensibility">16. Extensibility</h2>

<p>
Tools and libraries MAY add additional non-breaking metadata fields to port definitions.
</p>

<pre><code>{
  "id": "speed",
  "type": "f64",
  "connection": "recommended",
  "unit": "m/s",
  "description": "Measured linear speed"
}</code></pre>

<p>
Examples of such metadata may include:
</p>

<ul>
  <li>human-readable descriptions,</li>
  <li>units,</li>
  <li>documentation annotations,</li>
  <li>editor hints,</li>
  <li>domain-specific tags.</li>
</ul>

<p>
Runtime systems and validators that do not understand these extra properties <strong>MUST</strong> ignore them unless a stricter profile specifies otherwise.
</p>

<hr/>

<h2 id="summary">17. Summary</h2>

<p>
The interface defines the external logical contract of a FROG.
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
The interface describes <strong>what</strong> a FROG exposes.
The connector describes <strong>where</strong> those ports appear graphically.
The diagram defines how those public ports are bound to internal execution logic.
The front panel defines how a user may interact visually with some of that data.
</p>

<p>
Together, these sections allow FROGs to be safely validated, reused, and composed into larger executable graphs.
</p>
