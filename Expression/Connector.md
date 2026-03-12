<h1>FROG Connector Specification</h1>

<p>Definition of connector mapping for canonical <code>.frog</code> source files</p>
<p>FROG — Free Open Graphical Language</p>

<hr>

<h2>Contents</h2>
<ol>
  <li>Overview</li>
  <li>Purpose of the Connector</li>
  <li>Location in a <code>.frog</code> File</li>
  <li>Relationship with the Interface</li>
  <li>Connector Structure</li>
  <li>Perimeter Slot Model</li>
  <li>Port Mapping</li>
  <li>Examples</li>
  <li>Validation Rules</li>
  <li>Extensibility</li>
  <li>Summary</li>
</ol>

<hr>

<h2>1. Overview</h2>

<p>
The <code>connector</code> section defines how a FROG is graphically represented when it is instantiated
as a reusable node inside another diagram.
</p>

<p>
The connector does not define the logical public contract of the FROG. That responsibility belongs to
the <code>interface</code> section.
</p>

<p>
Instead, the connector provides a deterministic graphical mapping from declared public interface ports
to visible connection points around the reusable node boundary.
</p>

<p>
A FROG MAY be executable without a connector. The connector becomes relevant when the FROG is intended
to be reused graphically as a node inside another FROG.
</p>

<hr>

<h2>2. Purpose of the Connector</h2>

<p>The connector provides:</p>
<ul>
  <li>a consistent graphical representation of a FROG when reused as a node,</li>
  <li>a deterministic mapping between public interface ports and visible connection points,</li>
  <li>a simple and tool-independent connector layout model.</li>
</ul>

<p>The connector ensures that:</p>
<ul>
  <li>ports appear in predictable locations,</li>
  <li>graphical reuse remains stable across tools,</li>
  <li>the visual boundary of a reusable FROG remains independent from its internal diagram layout.</li>
</ul>

<p>
The connector is presentation-level source information. It MUST NOT redefine logical contract semantics
and MUST NOT alter the authoritative execution semantics established by the validated source-derived program representation.
</p>

<hr>

<h2>3. Location in a <code>.frog</code> File</h2>

<p>The <code>connector</code> is defined as a top-level object.</p>

<p>Schematic example:</p>

<pre><code>{
  "spec_version": "0.1",
  "metadata": {},
  "interface": {},
  "connector": {},
  "diagram": {},
  "front_panel": {}
}</code></pre>

<p>
Other optional top-level sections MAY also be present in a canonical <code>.frog</code> source file.
The example above shows only the sections relevant to this specification.
</p>

<p>The <code>connector</code> section is optional.</p>

<p>
It SHOULD be present when the FROG is intended to be instantiated as a reusable graphical node
inside another FROG.
</p>

<p>A top-level executable FROG MAY omit the connector entirely.</p>

<hr>

<h2>4. Relationship with the Interface</h2>

<p>The connector depends on the <code>interface</code> section.</p>

<p>
The interface defines the public logical ports of the FROG. The connector defines where those ports
appear on the reusable node perimeter when the FROG is reused graphically.
</p>

<p>Therefore:</p>
<ul>
  <li>the connector MUST NOT introduce ports that do not exist in the interface,</li>
  <li>the connector MUST reference only public interface ports,</li>
  <li>the connector MUST reference those ports by their interface <code>id</code>,</li>
  <li>a FROG MAY have an interface without a connector,</li>
  <li>a FROG MUST NOT define a connector without an interface.</li>
</ul>

<p>In practical terms:</p>
<ul>
  <li><code>interface</code> = public contract,</li>
  <li><code>connector</code> = graphical projection of that contract.</li>
</ul>

<hr>

<h2>5. Connector Structure</h2>

<p>Example connector definition:</p>

<pre><code>"connector": {
  "granularity": 40,
  "ports": [
    { "interface_port": "a", "slot": 34 },
    { "interface_port": "b", "slot": 36 },
    { "interface_port": "result", "slot": 14 }
  ]
}</code></pre>

<p>Fields:</p>
<ul>
  <li><code>granularity</code>: number of discrete connector positions along the perimeter,</li>
  <li><code>ports</code>: mapping between public interface port identifiers and perimeter slots.</li>
</ul>

<p>
If <code>granularity</code> is omitted, implementations SHOULD assume the default value of <code>40</code>.
</p>

<p>
For FROG v0.1, the canonical model is a square reusable node with a perimeter divided into
<code>40</code> slots, that is <code>10</code> slots per side.
</p>

<hr>

<h2>6. Perimeter Slot Model</h2>

<p>The connector is defined on a normalized square node boundary.</p>

<p>Slots are ordered clockwise starting from the top-left corner.</p>

<p>With the default granularity of <code>40</code>, the perimeter is divided into four equal sides:</p>
<ul>
  <li>Top side: slots <code>0..9</code></li>
  <li>Right side: slots <code>10..19</code></li>
  <li>Bottom side: slots <code>20..29</code></li>
  <li>Left side: slots <code>30..39</code></li>
</ul>

<p>Conceptual model:</p>

<pre><code>                 0   1   2   3   4   5   6   7   8   9
               ●   ●   ●   ●   ●   ●   ●   ●   ●   ●
          39 ●                                     ● 10
          38 ●                                     ● 11
          37 ●                                     ● 12
          36 ●                                     ● 13
          35 ●                                     ● 14
          34 ●                                     ● 15
          33 ●                                     ● 16
          32 ●                                     ● 17
          31 ●                                     ● 18
          30 ●                                     ● 19
               ●   ●   ●   ●   ●   ●   ●   ●   ●   ●
                29  28  27  26  25  24  23  22  21  20</code></pre>

<p>
Each slot represents one discrete connection position on the perimeter of the reusable node.
</p>

<p>
The connector model defines logical placement only. Actual rendering, spacing, padding, and pixel geometry
remain implementation-dependent.
</p>

<hr>

<h2>7. Port Mapping</h2>

<p>
Each entry in <code>connector.ports</code> maps one public interface port to one connector slot.
</p>

<p>Example:</p>

<pre><code>{
  "interface_port": "temperature",
  "slot": 12
}</code></pre>

<p>Fields:</p>
<ul>
  <li><code>interface_port</code>: the <code>id</code> of a public port declared in the interface,</li>
  <li><code>slot</code>: connector slot index on the node perimeter.</li>
</ul>

<p>
The slot determines where the corresponding connection point appears when the FROG is drawn
as a reusable node.
</p>

<p>
The connector does not redefine port type, direction, defaulting rules, or semantics.
Those properties remain defined by the <code>interface</code>.
</p>

<hr>

<h2>8. Examples</h2>

<h3>8.1 Basic Arithmetic Node</h3>

<pre><code>"connector": {
  "granularity": 40,
  "ports": [
    { "interface_port": "a", "slot": 34 },
    { "interface_port": "b", "slot": 36 },
    { "interface_port": "result", "slot": 14 }
  ]
}</code></pre>

<h3>8.2 Control System Node</h3>

<pre><code>"connector": {
  "granularity": 40,
  "ports": [
    { "interface_port": "enable", "slot": 1 },
    { "interface_port": "setpoint", "slot": 3 },
    { "interface_port": "measurement", "slot": 6 },
    { "interface_port": "output", "slot": 22 }
  ]
}</code></pre>

<h3>8.3 Top-Level Executable FROG Without Connector</h3>

<pre><code>{
  "spec_version": "0.1",
  "metadata": {},
  "interface": {
    "inputs": [
      { "id": "file_path", "type": "string" }
    ],
    "outputs": [
      { "id": "status", "type": "bool" }
    ]
  },
  "diagram": {},
  "front_panel": {}
}</code></pre>

<p>
In this case, the FROG remains executable, but it does not define a reusable graphical connector.
</p>

<hr>

<h2>9. Validation Rules</h2>

<p>Implementations MUST enforce the following rules:</p>
<ul>
  <li>the connector MUST be a top-level object when present,</li>
  <li>each connector entry MUST reference an existing public interface port,</li>
  <li>each <code>interface_port</code> value MUST reference the port <code>id</code> declared in the interface,</li>
  <li>slot values MUST satisfy <code>0 ≤ slot &lt; granularity</code>,</li>
  <li>each connector slot MUST be used at most once,</li>
  <li>each interface port referenced in the connector MUST appear at most once.</li>
</ul>

<p>Additionally, for a FROG declared or interpreted as a reusable graphical node:</p>
<ul>
  <li>every public interface input SHOULD have a connector mapping,</li>
  <li>every public interface output SHOULD have a connector mapping.</li>
</ul>

<p>
Implementations MAY treat incomplete mappings as validation errors when full graphical reusability is required.
</p>

<p>Invalid connector mappings MUST trigger validation errors.</p>

<hr>

<h2>10. Extensibility</h2>

<p>
Tools MAY extend connector entries with additional non-semantic properties.
</p>

<p>Example:</p>

<pre><code>{
  "interface_port": "speed",
  "slot": 8,
  "label": "Speed Input"
}</code></pre>

<p>
Such properties MAY be used for authoring, visualization, editor hints, accessibility metadata,
or other non-semantic presentation purposes.
</p>

<p>
Unknown connector properties MUST be ignored by runtimes and by tools that do not support them.
</p>

<p>
Extensions MUST preserve the core distinction between:
</p>
<ul>
  <li>logical public interface semantics,</li>
  <li>graphical reusable-node projection semantics,</li>
  <li>authoring- or tool-specific presentation details.</li>
</ul>

<hr>

<h2>11. Summary</h2>

<p>
The connector defines how a FROG appears when it is reused as a node inside another diagram.
</p>

<p>
It does not define the logical contract of the FROG. That responsibility belongs to the
<code>interface</code>.
</p>

<p>The connector provides:</p>
<ul>
  <li>a deterministic connector placement model,</li>
  <li>a simple and standardized perimeter slot layout,</li>
  <li>a clear separation between logical public ports and graphical node representation.</li>
</ul>

<p>In short:</p>
<ul>
  <li><code>interface</code> defines what the FROG exposes,</li>
  <li><code>connector</code> defines how that interface appears when the FROG is used as a reusable node.</li>
</ul>
