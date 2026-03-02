<h1 align="center">🐸 FROG Specification</h1>

<p align="center">
  <strong>FROG — Free Open Graphical Language</strong><br/>
  Official Language and File Format Specification
</p>

<hr/>

<h2>1. Purpose</h2>

<p>
This repository defines the official specification of <strong>FROG — Free Open Graphical Language</strong>.
</p>

<p>
FROG is an open, hardware-agnostic graphical dataflow language designed to provide a durable and independent foundation for graphical programming.
</p>

<p>
This specification defines:
</p>

<ul>
  <li>The fundamental executable unit: a <strong>Frog</strong></li>
  <li>The <code>.frog</code> file format</li>
  <li>The structural graph model</li>
  <li>The interface model</li>
  <li>The front panel model</li>
  <li>The execution semantics</li>
  <li>The validation rules</li>
</ul>

<p>
This document defines the language itself — not an IDE, not a runtime, not a compiler.
</p>

<p>
All compliant implementations MUST conform to this specification.
</p>

<hr/>

<h2>2. Core Concepts</h2>

<h3>2.1 The Frog</h3>

<p>
A <strong>Frog</strong> is the fundamental executable unit of the FROG language.
</p>

<p>
A Frog is:
</p>

<ul>
  <li>Self-contained</li>
  <li>Versioned</li>
  <li>Statically structured</li>
  <li>Represented as an explicit directed dataflow graph</li>
  <li>Optionally associated with a graphical interaction layer (front panel)</li>
</ul>

<p>
A Frog consists of:
</p>

<ul>
  <li>A <strong>diagram</strong> (executable graph)</li>
  <li>A <strong>typed interface</strong> (public contract)</li>
  <li>An optional <strong>front panel</strong> (interaction layer)</li>
</ul>

<hr/>

<h2>3. Design Principles</h2>

<h3>3.1 Independence</h3>

<p>
The language MUST remain independent from:
</p>

<ul>
  <li>Any specific development environment</li>
  <li>Any runtime implementation</li>
  <li>Any compiler backend</li>
</ul>

<h3>3.2 Explicit Structure</h3>

<p>
All execution semantics MUST be derivable from explicit graph structure and data availability.
</p>

<h3>3.3 Determinism</h3>

<p>
Given identical inputs and identical graph structure, execution results MUST be deterministic.
</p>

<h3>3.4 Source Transparency</h3>

<p>
A <code>.frog</code> file MUST:
</p>

<ul>
  <li>Be human-readable</li>
  <li>Be version-control friendly</li>
  <li>Contain no hidden compiled artifacts</li>
  <li>Contain no embedded binary execution code</li>
</ul>

<hr/>

<h2>4. File Format — <code>.frog</code></h2>

<h3>4.1 General Structure</h3>

<p>
A Frog is stored as a structured JSON document.
</p>

<pre>
{
  "spec_version": "0.1",
  "metadata": {},
  "interface": {},
  "diagram": {},
  "front_panel": {}
}
</pre>

<h3>4.2 Required Top-Level Fields</h3>

<ul>
  <li><code>spec_version</code> (string) — MUST be present</li>
  <li><code>metadata</code> (object) — MUST be present</li>
  <li><code>interface</code> (object) — MUST be present</li>
  <li><code>diagram</code> (object) — MUST be present</li>
  <li><code>front_panel</code> (object) — MUST be present (may be empty)</li>
</ul>

<hr/>

<h2>5. Metadata Section</h2>

<pre>
"metadata": {
  "name": "Add",
  "description": "Adds two floating-point numbers.",
  "author": "Author Name",
  "program_version": "0.1.0",
  "tags": ["math", "primitive"]
}
</pre>

<p>
The metadata section defines the identity and documentation of the Frog.
</p>

<hr/>

<h2>6. Interface Definition</h2>

<pre>
"interface": {
  "inputs": [
    { "id": "a", "type": "float64" },
    { "id": "b", "type": "float64" }
  ],
  "outputs": [
    { "id": "result", "type": "float64" }
  ]
}
</pre>

<p>
The interface defines the public contract of the Frog.
</p>

<p>
Ports declared in the interface MUST be consistent with the diagram.
</p>

<hr/>

<h2>7. Diagram Model</h2>

<pre>
"diagram": {
  "nodes": [],
  "edges": []
}
</pre>

<h3>7.1 Node Structure</h3>

<pre>
{
  "id": "node_1",
  "kind": "primitive",
  "type": "Add",
  "ports": {
    "inputs": [
      { "id": "a", "type": "float64" },
      { "id": "b", "type": "float64" }
    ],
    "outputs": [
      { "id": "result", "type": "float64" }
    ]
  },
  "parameters": {},
  "layout": {
    "x": 100,
    "y": 200
  }
}
</pre>

<p>
Node identifiers MUST be unique within the diagram.
</p>

<h3>7.2 Edge Structure</h3>

<pre>
{
  "id": "edge_1",
  "from": { "node": "node_1", "port": "result" },
  "to": { "node": "node_2", "port": "a" }
}
</pre>

<p>
Edges MUST reference existing node identifiers and port identifiers.
</p>

<hr/>

<h2>8. Execution Model</h2>

<p>
Execution follows a pure dataflow model.
</p>

<ul>
  <li>A node becomes eligible for execution when all required input data are available.</li>
  <li>Execution order MUST be derived solely from data dependencies.</li>
  <li>Nodes MAY execute in parallel if data dependencies allow.</li>
  <li>Graph structure MUST fully determine scheduling constraints.</li>
</ul>

<p>
A <code>.frog</code> file MUST NOT be executed directly.
</p>

<p>
It MUST first be validated and transformed into an intermediate representation prior to execution.
</p>

<hr/>

<h2>9. Graph Validation Rules</h2>

<ul>
  <li>Node identifiers MUST be unique.</li>
  <li>Edge identifiers MUST be unique.</li>
  <li>All edge references MUST reference existing nodes and ports.</li>
  <li>Port types connected by edges MUST be compatible.</li>
  <li>Interface ports MUST be bound to corresponding diagram ports.</li>
</ul>

<hr/>

<h2>10. Front Panel Model</h2>

<pre>
"front_panel": {
  "controls": [],
  "indicators": [],
  "layout": {}
}
</pre>

<p>
Front panel elements represent the interaction layer of the Frog.
</p>

<p>
Front panel elements MUST explicitly bind to diagram ports.
</p>

<hr/>

<h2>11. Icon Definition (Optional)</h2>

<p>
A Frog MAY define a 40x40 SVG icon.
</p>

<pre>
"icon": {
  "size": 40,
  "svg": "&lt;svg&gt;...&lt;/svg&gt;"
}
</pre>

<hr/>

<h2>12. Catalog Metadata (Optional)</h2>

<p>
A Frog MAY include a <code>catalog</code> object to support IDE indexing and discovery.
</p>

<pre>
"catalog": {
  "is_example": true,
  "title": "Basic Addition Example",
  "keywords": ["math", "example"],
  "categories": ["Examples", "Mathematics"]
}
</pre>

<hr/>

<h2>13. Versioning Policy</h2>

<p>
The specification follows semantic versioning:
</p>

<pre>
MAJOR.MINOR.PATCH
</pre>

<ul>
  <li><strong>MAJOR</strong> — incompatible structural changes</li>
  <li><strong>MINOR</strong> — backward-compatible additions</li>
  <li><strong>PATCH</strong> — clarifications</li>
</ul>

<hr/>

<h2>14. Normative Terminology</h2>

<ul>
  <li><strong>MUST</strong> — required for compliance</li>
  <li><strong>SHOULD</strong> — recommended</li>
  <li><strong>MAY</strong> — optional</li>
  <li><strong>MUST NOT</strong> — prohibited</li>
</ul>

<hr/>

<h2>15. Current Status</h2>

<p>
FROG Specification v0.1 — Draft.
</p>

<p>
This version defines a minimal but coherent structural foundation for the language.
</p>

<hr/>

<h2>16. License</h2>

<p>
This specification is released under the Apache License 2.0.
</p>

<hr/>

<p align="center">
<strong>FROG — Free Open Graphical Language</strong><br/>
An open foundation for graphical programming.
</p>
