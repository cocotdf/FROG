<p align="center">
  <img src="../FROG%20logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG Metadata Specification</h1>

<p align="center">
Definition of the required <code>metadata</code> section of <strong>.frog</strong> programs<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2 id="contents">Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope">2. Scope</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#location">4. Location in a <code>.frog</code> File</a></li>
  <li><a href="#structure">5. Metadata Structure</a></li>
  <li><a href="#field-definitions">6. Field Definitions</a>
    <ul>
      <li><a href="#field-name">6.1 <code>name</code></a></li>
      <li><a href="#field-summary">6.2 <code>summary</code></a></li>
      <li><a href="#field-description">6.3 <code>description</code></a></li>
      <li><a href="#field-author">6.4 <code>author</code></a></li>
      <li><a href="#field-program-version">6.5 <code>program_version</code></a></li>
      <li><a href="#field-tags">6.6 <code>tags</code></a></li>
      <li><a href="#field-is-example">6.7 <code>is_example</code></a></li>
      <li><a href="#field-created">6.8 <code>created</code></a></li>
      <li><a href="#field-updated">6.9 <code>updated</code></a></li>
      <li><a href="#field-license">6.10 <code>license</code></a></li>
    </ul>
  </li>
  <li><a href="#validation-rules">7. Validation Rules</a></li>
  <li><a href="#extensibility-and-boundary-rules">8. Extensibility and Boundary Rules</a></li>
  <li><a href="#examples">9. Examples</a>
    <ul>
      <li><a href="#minimal-example">9.1 Minimal Metadata Example</a></li>
      <li><a href="#extended-example">9.2 Extended Metadata Example</a></li>
    </ul>
  </li>
  <li><a href="#design-goals">10. Design Goals</a></li>
  <li><a href="#summary">11. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The top-level <code>metadata</code> section defines the descriptive identity of a FROG program.
</p>

<p>
It carries source-level information such as:
</p>

<ul>
  <li>program identity,</li>
  <li>human-readable description,</li>
  <li>authorship and maintenance information,</li>
  <li>version-tracking information,</li>
  <li>search and discovery hints.</li>
</ul>

<p>
The <code>metadata</code> section is part of the canonical <code>.frog</code> source representation.
It is required for a conforming canonical source file.
</p>

<p>
However, <code>metadata</code> is <strong>non-executable</strong>.
It MUST NOT define, modify, or override execution semantics.
</p>

<p>
Execution behavior MUST be derived from the validated executable source representation of the program,
centered on the public interface and the authoritative executable diagram, and interpreted according to the normative language semantics.
</p>

<p>
Runtimes, compilers, and other execution-facing systems MUST ignore metadata fields when determining executable meaning.
</p>

<hr/>

<h2 id="scope">2. Scope</h2>

<p>
This document specifies:
</p>

<ul>
  <li>the role of the required top-level <code>metadata</code> section,</li>
  <li>the structure of the metadata object,</li>
  <li>the meaning of standard metadata fields,</li>
  <li>validation rules for those fields,</li>
  <li>compatibility and extensibility rules for tool-added metadata.</li>
</ul>

<p>
This document does not specify:
</p>

<ul>
  <li>the public program interface,</li>
  <li>the executable dataflow graph,</li>
  <li>the optional front-panel composition,</li>
  <li>IDE authoring preferences,</li>
  <li>cache or derived artifacts,</li>
  <li>runtime scheduling, typing, or execution semantics.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
The <code>metadata</code> section belongs to the canonical source specification in <code>Expression/</code>.
It is one of the required top-level source sections of a canonical <code>.frog</code> file.
</p>

<p>
Its boundary with related sections is as follows:
</p>

<pre>Top-level source-section boundary

metadata   - descriptive source identity and documentation
interface  - public typed program boundary
diagram    - authoritative executable graph
front_panel - optional user-facing interaction layer
ide        - optional IDE-facing authoring preferences
cache      - optional derived non-authoritative tooling data</pre>

<p>
In particular:
</p>

<ul>
  <li><code>metadata</code> does not define the public API of the FROG. That belongs to <code>interface</code>.</li>
  <li><code>metadata</code> does not define executable logic. That belongs to <code>diagram</code>.</li>
  <li><code>metadata</code> does not define front-panel composition. That belongs to <code>front_panel</code> when present.</li>
  <li><code>metadata</code> does not carry IDE recoverability or editor-state preferences. That belongs to <code>ide</code>.</li>
  <li><code>metadata</code> does not carry derived accelerators or regenerated artifacts. That belongs to <code>cache</code>.</li>
</ul>

<hr/>

<h2 id="location">4. Location in a <code>.frog</code> File</h2>

<p>
The <code>metadata</code> section is a required top-level JSON object inside the canonical <code>.frog</code> source file.
</p>

<p>
Minimal canonical source shape:
</p>

<pre>{
  "spec_version": "0.1",
  "metadata": {},
  "interface": {},
  "diagram": {}
}</pre>

<p>
A larger canonical source file MAY additionally include optional top-level sections such as
<code>connector</code>, <code>front_panel</code>, <code>icon</code>, <code>ide</code>, and <code>cache</code>.
</p>

<pre>Canonical .frog structure

example.frog
├─ spec_version
├─ metadata     -> required descriptive source section
├─ interface    -> required public typed boundary
├─ diagram      -> required executable graph
├─ connector    -> optional reusable-node perimeter mapping
├─ front_panel  -> optional UI composition
├─ icon         -> optional node icon
├─ ide          -> optional IDE-facing preferences
└─ cache        -> optional derived tooling data</pre>

<p>
Rules:
</p>

<ul>
  <li><code>metadata</code> MUST exist in a canonical <code>.frog</code> source file.</li>
  <li><code>metadata</code> MUST be represented as a JSON object.</li>
  <li>Execution-facing systems MUST ignore <code>metadata</code> when determining executable behavior.</li>
</ul>

<hr/>

<h2 id="structure">5. Metadata Structure</h2>

<p>
A typical metadata object is:
</p>

<pre>"metadata": {
  "name": "Add",
  "summary": "Simple numeric addition example.",
  "description": "Adds two floating-point numbers and returns the result.",
  "author": "Example Labs",
  "program_version": "1.0.0",
  "tags": ["math", "example"],
  "is_example": true,
  "created": "2026-03-05T10:00:00Z",
  "updated": "2026-03-05T12:00:00Z",
  "license": "Apache-2.0"
}</pre>

<p>
The standard minimal required fields are:
</p>

<ul>
  <li><code>name</code></li>
  <li><code>description</code></li>
</ul>

<p>
All other standard fields are optional unless a profile, repository policy, or toolchain contract explicitly requires them.
</p>

<p>
Tools MAY add additional metadata fields, provided that those fields remain non-executable and safely ignorable by execution-facing systems.
</p>

<hr/>

<h2 id="field-definitions">6. Field Definitions</h2>

<h3 id="field-name">6.1 <code>name</code></h3>

<p>
Human-readable program name.
</p>

<pre>"name": "Add"</pre>

<ul>
  <li>MUST be present.</li>
  <li>MUST be a string.</li>
  <li>SHOULD be concise and descriptive.</li>
  <li>SHOULD identify the program clearly within its project, package, or library scope.</li>
</ul>

<hr/>

<h3 id="field-summary">6.2 <code>summary</code></h3>

<p>
Short one-line description suitable for listings, search results, previews, or palette-style browsers.
</p>

<pre>"summary": "Simple numeric addition example."</pre>

<ul>
  <li>MUST be a string if present.</li>
  <li>SHOULD be a single concise sentence.</li>
  <li>SHOULD complement <code>name</code> rather than repeat it verbatim.</li>
</ul>

<hr/>

<h3 id="field-description">6.3 <code>description</code></h3>

<p>
Longer descriptive text explaining what the FROG does.
</p>

<pre>"description": "Adds two floating-point numbers and returns the result."</pre>

<ul>
  <li>MUST be present.</li>
  <li>MUST be a string.</li>
  <li>SHOULD describe externally meaningful behavior rather than internal implementation details.</li>
  <li>MAY contain multiple sentences.</li>
</ul>

<hr/>

<h3 id="field-author">6.4 <code>author</code></h3>

<p>
Identifies the creator, maintainer, or owning organization.
</p>

<pre>"author": "Example Labs"</pre>

<ul>
  <li>MUST be a string if present.</li>
  <li>MAY name an individual, a team, or an organization.</li>
  <li>SHOULD be treated as descriptive information, not as an access-control mechanism.</li>
</ul>

<hr/>

<h3 id="field-program-version">6.5 <code>program_version</code></h3>

<p>
Version identifier of the FROG program itself.
</p>

<pre>"program_version": "1.2.0"</pre>

<ul>
  <li>MUST be a string if present.</li>
  <li>SHOULD use a stable project-defined versioning convention.</li>
  <li>Semantic versioning (<code>MAJOR.MINOR.PATCH</code>) is RECOMMENDED when appropriate.</li>
</ul>

<hr/>

<h3 id="field-tags">6.6 <code>tags</code></h3>

<p>
Keyword list for search, indexing, filtering, or example browsing.
</p>

<pre>"tags": ["math", "signal", "example"]</pre>

<ul>
  <li>MUST be an array of strings if present.</li>
  <li>Each element SHOULD be a short keyword or short phrase.</li>
  <li>Tags SHOULD avoid meaningless duplication.</li>
  <li>Lowercase normalized tags are RECOMMENDED when practical.</li>
</ul>

<hr/>

<h3 id="field-is-example">6.7 <code>is_example</code></h3>

<p>
Indicates whether the FROG is primarily intended as an example, tutorial artifact, or demonstration program.
</p>

<pre>"is_example": true</pre>

<ul>
  <li>MUST be a boolean if present.</li>
  <li>Tools MAY use this field to populate example browsers or tutorial collections.</li>
</ul>

<hr/>

<h3 id="field-created">6.8 <code>created</code></h3>

<p>
Creation timestamp of the source artifact or of the program record tracked by the owning workflow.
</p>

<pre>"created": "2026-03-05T10:00:00Z"</pre>

<ul>
  <li>MUST be a string if present.</li>
  <li>ISO-8601 UTC format is RECOMMENDED.</li>
  <li>This field is descriptive and MUST NOT be used to derive execution behavior.</li>
</ul>

<hr/>

<h3 id="field-updated">6.9 <code>updated</code></h3>

<p>
Timestamp of the last significant metadata or source update tracked by the owning workflow.
</p>

<pre>"updated": "2026-03-05T12:00:00Z"</pre>

<ul>
  <li>MUST be a string if present.</li>
  <li>ISO-8601 UTC format is RECOMMENDED.</li>
  <li>When both <code>created</code> and <code>updated</code> are present, <code>updated</code> SHOULD NOT represent an earlier instant than <code>created</code>.</li>
</ul>

<hr/>

<h3 id="field-license">6.10 <code>license</code></h3>

<p>
Informational license identifier associated with the program or its distribution context.
</p>

<pre>"license": "Apache-2.0"</pre>

<ul>
  <li>MUST be a string if present.</li>
  <li>SPDX identifiers are RECOMMENDED when applicable.</li>
  <li>This field is informational metadata. It does not alter execution semantics.</li>
</ul>

<hr/>

<h2 id="validation-rules">7. Validation Rules</h2>

<ul>
  <li><code>metadata</code> MUST be present.</li>
  <li><code>metadata</code> MUST be a JSON object.</li>
  <li><code>metadata.name</code> MUST be present and MUST be a string.</li>
  <li><code>metadata.description</code> MUST be present and MUST be a string.</li>
  <li>If present, <code>metadata.summary</code> MUST be a string.</li>
  <li>If present, <code>metadata.author</code> MUST be a string.</li>
  <li>If present, <code>metadata.program_version</code> MUST be a string.</li>
  <li>If present, <code>metadata.tags</code> MUST be an array of strings.</li>
  <li>If present, <code>metadata.is_example</code> MUST be a boolean.</li>
  <li>If present, <code>metadata.created</code> MUST be a string.</li>
  <li>If present, <code>metadata.updated</code> MUST be a string.</li>
  <li>If present, <code>metadata.license</code> MUST be a string.</li>
</ul>

<p>
Unknown metadata fields:
</p>

<ul>
  <li>MAY be present.</li>
  <li>MUST NOT affect executable meaning.</li>
  <li>MUST be ignored by runtimes and other execution-facing systems.</li>
</ul>

<p>
Validation of metadata is structural and descriptive.
A metadata validation failure MUST NOT be interpreted as a dataflow execution rule by itself.
</p>

<hr/>

<h2 id="extensibility-and-boundary-rules">8. Extensibility and Boundary Rules</h2>

<p>
Tools, repositories, or organizations MAY extend the metadata object with additional descriptive fields.
</p>

<p>
Such extensions MUST remain:
</p>

<ul>
  <li>non-executable,</li>
  <li>safely ignorable by runtimes,</li>
  <li>compatible with canonical source transparency.</li>
</ul>

<p>
Example:
</p>

<pre>"metadata": {
  "name": "Example",
  "description": "Example FROG.",
  "organization": "Example Labs",
  "documentation_url": "https://example.com/docs"
}</pre>

<p>
However, transient authoring state SHOULD NOT be stored in <code>metadata</code>.
That kind of information belongs in <code>ide</code> when it is source-carried authoring metadata,
or in <code>cache</code> when it is derived and regenerable tooling data.
</p>

<pre>Non-executable boundary inside Expression/

metadata -> durable descriptive identity
ide      -> IDE-facing authoring preferences and recoverability aids
cache    -> derived tooling accelerators safe to delete and regenerate</pre>

<hr/>

<h2 id="examples">9. Examples</h2>

<h3 id="minimal-example">9.1 Minimal Metadata Example</h3>

<pre>"metadata": {
  "name": "Add",
  "description": "Adds two numbers."
}</pre>

<hr/>

<h3 id="extended-example">9.2 Extended Metadata Example</h3>

<pre>"metadata": {
  "name": "PIDController",
  "summary": "Basic PID controller example.",
  "description": "Implements a proportional-integral-derivative controller.",
  "author": "Example Automation",
  "program_version": "1.2.0",
  "tags": ["control", "pid", "automation"],
  "is_example": true,
  "created": "2026-03-05T10:00:00Z",
  "updated": "2026-03-05T14:00:00Z",
  "license": "Apache-2.0"
}</pre>

<hr/>

<h2 id="design-goals">10. Design Goals</h2>

<ul>
  <li>Provide a stable descriptive identity for a FROG program.</li>
  <li>Support documentation, indexing, search, and discovery.</li>
  <li>Support authorship and version-tracking workflows.</li>
  <li>Remain compatible with transparent canonical source representation.</li>
  <li>Remain strictly non-authoritative for execution semantics.</li>
  <li>Preserve a clean architectural boundary with <code>interface</code>, <code>diagram</code>, <code>front_panel</code>, <code>ide</code>, and <code>cache</code>.</li>
</ul>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
The required <code>metadata</code> section provides descriptive source information about a FROG program.
It defines identity and documentation-oriented information without changing executable meaning.
</p>

<p>
This preserves a clean long-term separation between:
</p>

<ul>
  <li>descriptive source identity (<code>metadata</code>),</li>
  <li>public program boundary (<code>interface</code>),</li>
  <li>authoritative executable logic (<code>diagram</code>),</li>
  <li>optional user-facing composition (<code>front_panel</code>),</li>
  <li>optional IDE-facing authoring metadata (<code>ide</code>),</li>
  <li>optional derived tooling data (<code>cache</code>).</li>
</ul>
