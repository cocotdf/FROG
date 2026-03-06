<h1 align="center">🐸 FROG Metadata Specification</h1>

<p align="center">
Metadata definition for <strong>.frog</strong> files<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2 id="contents">Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#location">2. Location in <code>.frog</code></a></li>
  <li><a href="#structure">3. Metadata structure</a></li>
  <li><a href="#fields">4. Field definitions</a>
    <ul>
      <li><a href="#field-name">4.1 <code>name</code></a></li>
      <li><a href="#field-summary">4.2 <code>summary</code></a></li>
      <li><a href="#field-description">4.3 <code>description</code></a></li>
      <li><a href="#field-author">4.4 <code>author</code></a></li>
      <li><a href="#field-program-version">4.5 <code>program_version</code></a></li>
      <li><a href="#field-tags">4.6 <code>tags</code></a></li>
      <li><a href="#field-is-example">4.7 <code>is_example</code></a></li>
      <li><a href="#field-created">4.8 <code>created</code></a></li>
      <li><a href="#field-updated">4.9 <code>updated</code></a></li>
      <li><a href="#field-license">4.10 <code>license</code></a></li>
    </ul>
  </li>
  <li><a href="#minimal-example">5. Minimal metadata example</a></li>
  <li><a href="#extended-example">6. Extended metadata example</a></li>
  <li><a href="#validation">7. Validation rules</a></li>
  <li><a href="#extensibility">8. Extensibility</a></li>
  <li><a href="#design-goals">9. Design goals</a></li>
  <li><a href="#summary">10. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <strong>metadata</strong> section describes the identity and documentation of a Frog program.
</p>

<p>
It provides descriptive information used by development tools for indexing, search, documentation generation, and project organization.
</p>

<p>
The metadata section <strong>MUST NOT affect execution semantics</strong>.
Execution behavior MUST be derived exclusively from the <code>diagram</code>, <code>interface</code>, and language validation rules.
</p>

<p>
Runtimes MUST ignore metadata fields during execution.
</p>

<p>
Typical consumers of metadata include:
</p>

<ul>
  <li>Development environments</li>
  <li>Documentation generators</li>
  <li>Example browsers</li>
  <li>Library indexers</li>
  <li>Version tracking tools</li>
</ul>

<hr/>

<h2 id="location">2. Location in <code>.frog</code></h2>

<p>
Metadata is defined as a top-level JSON object inside a <code>.frog</code> file.
</p>

<pre>{
  "spec_version": "0.1",
  "metadata": { },
  "interface": { },
  "connector": { },
  "diagram": { },
  "front_panel": { }
}</pre>

<p>
Rules:
</p>

<ul>
  <li><code>metadata</code> MUST exist.</li>
  <li>Execution engines MUST ignore metadata when executing a Frog.</li>
</ul>

<hr/>

<h2 id="structure">3. Metadata structure</h2>

<p>
Typical metadata object:
</p>

<pre>"metadata": {
  "name": "Add",
  "summary": "Simple numeric addition example.",
  "description": "Adds two floating-point numbers.",
  "author": "Example Labs",
  "program_version": "1.0.0",
  "tags": ["math", "example"],
  "is_example": true,
  "created": "2026-03-05T10:00:00Z",
  "updated": "2026-03-05T12:00:00Z",
  "license": "Apache-2.0"
}</pre>

<p>
Only a minimal subset is required. Additional fields MAY be introduced by tools.
</p>

<hr/>

<h2 id="fields">4. Field definitions</h2>

<h3 id="field-name">4.1 <code>name</code></h3>

<p>
Human-readable name of the Frog.
</p>

<pre>"name": "Add"</pre>

<ul>
  <li>MUST be a string.</li>
  <li>SHOULD be concise and descriptive.</li>
  <li>SHOULD be unique within a project or library scope.</li>
</ul>

<hr/>

<h3 id="field-summary">4.2 <code>summary</code></h3>

<p>
Short one-line description used for indexing, search results, or UI previews.
</p>

<pre>"summary": "Simple numeric addition example."</pre>

<ul>
  <li>MUST be a string if present.</li>
  <li>SHOULD be a single sentence.</li>
</ul>

<hr/>

<h3 id="field-description">4.3 <code>description</code></h3>

<p>
Longer explanation of what the Frog does.
</p>

<pre>"description": "Adds two floating-point numbers."</pre>

<ul>
  <li>MUST be a string.</li>
  <li>SHOULD describe behavior rather than implementation.</li>
</ul>

<hr/>

<h3 id="field-author">4.4 <code>author</code></h3>

<p>
Identifies the creator or maintainer.
</p>

<pre>"author": "Example Labs"</pre>

<ul>
  <li>MUST be a string if present.</li>
  <li>MAY include organization names.</li>
</ul>

<hr/>

<h3 id="field-program-version">4.5 <code>program_version</code></h3>

<p>
Version of the Frog program itself.
</p>

<pre>"program_version": "1.2.0"</pre>

<ul>
  <li>MUST be a string if present.</li>
  <li>SHOULD follow semantic versioning (<code>MAJOR.MINOR.PATCH</code>).</li>
</ul>

<hr/>

<h3 id="field-tags">4.6 <code>tags</code></h3>

<p>
Keywords used for indexing and searching.
</p>

<pre>"tags": ["math", "signal", "example"]</pre>

<ul>
  <li>MUST be an array of strings if present.</li>
  <li>SHOULD contain short lowercase keywords.</li>
</ul>

<hr/>

<h3 id="field-is-example">4.7 <code>is_example</code></h3>

<p>
Indicates whether the Frog is intended to be used as an example or tutorial element.
</p>

<pre>"is_example": true</pre>

<ul>
  <li>MUST be boolean if present.</li>
  <li>Tools MAY use this field to populate example browsers.</li>
</ul>

<hr/>

<h3 id="field-created">4.8 <code>created</code></h3>

<p>
Timestamp indicating when the Frog was created.
</p>

<pre>"created": "2026-03-05T10:00:00Z"</pre>

<ul>
  <li>MUST be a string if present.</li>
  <li>SHOULD follow ISO-8601 UTC format.</li>
</ul>

<hr/>

<h3 id="field-updated">4.9 <code>updated</code></h3>

<p>
Timestamp of the last modification.
</p>

<pre>"updated": "2026-03-05T12:00:00Z"</pre>

<ul>
  <li>MUST be a string if present.</li>
  <li>SHOULD follow ISO-8601 UTC format.</li>
</ul>

<hr/>

<h3 id="field-license">4.10 <code>license</code></h3>

<p>
Informational license identifier for the Frog.
</p>

<pre>"license": "Apache-2.0"</pre>

<ul>
  <li>MUST be a string if present.</li>
  <li>SHOULD use SPDX identifiers.</li>
</ul>

<hr/>

<h2 id="minimal-example">5. Minimal metadata example</h2>

<pre>"metadata": {
  "name": "Add",
  "description": "Adds two numbers."
}</pre>

<hr/>

<h2 id="extended-example">6. Extended metadata example</h2>

<pre>"metadata": {
  "name": "PIDController",
  "summary": "Basic PID controller example.",
  "description": "Implements a proportional–integral–derivative controller.",
  "author": "Example Automation",
  "program_version": "1.2.0",
  "tags": ["control", "pid", "automation"],
  "is_example": true,
  "created": "2026-03-05T10:00:00Z",
  "updated": "2026-03-05T14:00:00Z",
  "license": "Apache-2.0"
}</pre>

<hr/>

<h2 id="validation">7. Validation rules</h2>

<ul>
  <li><code>metadata</code> MUST exist.</li>
  <li><code>metadata.name</code> MUST exist and MUST be a string.</li>
  <li><code>metadata.description</code> MUST exist and MUST be a string.</li>
  <li>If present, <code>tags</code> MUST be an array of strings.</li>
  <li>If present, timestamps MUST be strings.</li>
</ul>

<p>
Unknown metadata fields:
</p>

<ul>
  <li>MAY be added by tools.</li>
  <li>MUST be ignored by runtimes.</li>
</ul>

<hr/>

<h2 id="extensibility">8. Extensibility</h2>

<p>
Tools MAY extend metadata with additional properties.
</p>

<pre>"metadata": {
  "name": "Example",
  "description": "Example frog",
  "organization": "Example Labs",
  "documentation_url": "https://example.com/docs"
}</pre>

<p>
Such extensions MUST NOT affect execution and MUST be safely ignorable.
</p>

<hr/>

<h2 id="design-goals">9. Design goals</h2>

<ul>
  <li>Provide clear program identity.</li>
  <li>Enable search and discovery.</li>
  <li>Support version tracking.</li>
  <li>Remain tool-agnostic.</li>
  <li>Remain non-authoritative for runtime behavior.</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The metadata section provides descriptive information about a Frog program without influencing execution.
It enables documentation, indexing, and discoverability while preserving a strict separation between
<strong>program description</strong> and <strong>program execution</strong>.
</p>
