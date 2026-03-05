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
<li><a href="#port-types">8. Type System Integration</a></li>
<li><a href="#binding">9. Binding with the Diagram</a></li>
<li><a href="#connector">10. Relation with Connector</a></li>
<li><a href="#examples">11. Examples</a></li>
<li><a href="#validation">12. Validation Rules</a></li>
<li><a href="#extensibility">13. Extensibility</a></li>
<li><a href="#summary">14. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <strong>interface</strong> section defines the public contract of a Frog.
</p>

<p>
It specifies:
</p>

<ul>
<li>the program inputs</li>
<li>the program outputs</li>
<li>their data types</li>
<li>their identifiers</li>
</ul>

<p>
The interface defines how a Frog communicates with the outside world and with other Frogs.
</p>

<hr/>

<h2 id="purpose">2. Purpose of the Interface</h2>

<p>
The interface provides a stable and explicit contract between programs.
</p>

<p>
It allows:
</p>

<ul>
<li>composition of Frogs into larger graphs</li>
<li>static validation of connections</li>
<li>clear program boundaries</li>
<li>safe integration across libraries</li>
</ul>

<p>
The interface is independent from layout or execution scheduling.
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
The <code>interface</code> section MUST be present.
</p>

<hr/>

<h2 id="structure">4. Interface Structure</h2>

<p>
The interface object contains two arrays:
</p>

<ul>
<li><strong>inputs</strong></li>
<li><strong>outputs</strong></li>
</ul>

Example:

<pre>
"interface": {
  "inputs": [],
  "outputs": []
}
</pre>

Each entry describes a port.

<hr/>

<h2 id="inputs">5. Input Ports</h2>

Input ports represent data entering the Frog.

Example:

<pre>
"inputs": [
  {
    "id": "a",
    "type": "float64"
  },
  {
    "id": "b",
    "type": "float64"
  }
]
</pre>

Rules:

<ul>
<li>Input ports MUST have unique identifiers.</li>
<li>Input ports MUST define a type.</li>
<li>Input ports represent external data sources.</li>
</ul>

<hr/>

<h2 id="outputs">6. Output Ports</h2>

Output ports represent data produced by the Frog.

Example:

<pre>
"outputs": [
  {
    "id": "result",
    "type": "float64"
  }
]
</pre>

Rules:

<ul>
<li>Output ports MUST have unique identifiers.</li>
<li>Output ports MUST define a type.</li>
<li>Output ports represent values exposed to other Frogs.</li>
</ul>

<hr/>

<h2 id="port-properties">7. Port Properties</h2>

Each port object contains the following properties.

<h3>id</h3>

Unique identifier of the port.

Example:

<pre>
"id": "temperature"
</pre>

Rules:

<ul>
<li>MUST be a string.</li>
<li>MUST be unique within its port list.</li>
</ul>

<h3>type</h3>

Defines the data type.

Example:

<pre>
"type": "float64"
</pre>

Rules:

<ul>
<li>MUST reference a valid FROG type.</li>
</ul>

<h3>optional properties</h3>

Additional metadata may be defined.

Example:

<pre>
{
  "id": "gain",
  "type": "float64",
  "default": 1.0,
  "description": "Gain factor"
}
</pre>

<hr/>

<h2 id="port-types">8. Type System Integration</h2>

The interface relies on the FROG type system.

Examples:

<pre>
float64
int32
bool
string
array&lt;float64&gt;
</pre>

Custom types MAY be introduced by libraries.

Type compatibility MUST be validated during graph validation.

<hr/>

<h2 id="binding">9. Binding with the Diagram</h2>

Interface ports must connect to nodes inside the diagram.

Example:

<pre>
diagram input
      ↓
interface input
</pre>

The diagram may contain special nodes representing interface entry and exit points.

Rules:

<ul>
<li>Each interface port MUST be reachable in the diagram.</li>
<li>Unbound interface ports MUST trigger validation errors.</li>
</ul>

<hr/>

<h2 id="connector">10. Relation with Connector</h2>

The <code>connector</code> section defines how interface ports appear when the Frog is used as a node.

The connector maps interface ports to graphical positions.

Example:

<pre>
"connector": {
  "pattern": "2x2",
  "ports": [
    { "interface_port": "a", "side": "left", "index": 0 },
    { "interface_port": "b", "side": "left", "index": 1 },
    { "interface_port": "result", "side": "right", "index": 0 }
  ]
}
</pre>

<hr/>

<h2 id="examples">11. Examples</h2>

<h3>Minimal Interface</h3>

<pre>
"interface": {
  "inputs": [
    { "id": "a", "type": "float64" }
  ],
  "outputs": [
    { "id": "result", "type": "float64" }
  ]
}
</pre>

<h3>Multi-Input Example</h3>

<pre>
"interface": {
  "inputs": [
    { "id": "temperature", "type": "float64" },
    { "id": "pressure", "type": "float64" }
  ],
  "outputs": [
    { "id": "density", "type": "float64" }
  ]
}
</pre>

<hr/>

<h2 id="validation">12. Validation Rules</h2>

Implementations MUST enforce:

<ul>
<li>interface MUST exist</li>
<li>inputs and outputs MUST be arrays</li>
<li>port ids MUST be unique</li>
<li>ports MUST define a type</li>
<li>diagram connections MUST match interface ports</li>
</ul>

Unknown properties MUST be ignored.

<hr/>

<h2 id="extensibility">13. Extensibility</h2>

Tools MAY add additional fields.

Example:

<pre>
{
  "id": "speed",
  "type": "float64",
  "unit": "m/s"
}
</pre>

Runtime systems MUST ignore unknown fields.

<hr/>

<h2 id="summary">14. Summary</h2>

The interface defines the external contract of a Frog.

It ensures:

<ul>
<li>clear program boundaries</li>
<li>type-safe composition</li>
<li>modular program construction</li>
</ul>

The interface is the foundation for connecting Frogs into larger executable graphs.
