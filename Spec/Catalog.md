<h1 align="center">🐸 FROG Catalog Specification</h1>

<p align="center">
Catalog metadata for indexing and discovery of <strong>.frog</strong> programs<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Design goals</a></li>
  <li><a href="#location">3. Location in a .frog file</a></li>
  <li><a href="#structure">4. Catalog object structure</a></li>
  <li><a href="#fields">5. Field definitions</a>
    <ul>
      <li><a href="#field-is-example">5.1 <code>is_example</code></a></li>
      <li><a href="#field-title">5.2 <code>title</code></a></li>
      <li><a href="#field-summary">5.3 <code>summary</code></a></li>
      <li><a href="#field-keywords">5.4 <code>keywords</code></a></li>
      <li><a href="#field-categories">5.5 <code>categories</code></a></li>
      <li><a href="#field-paths">5.6 <code>paths</code> (optional)</a></li>
      <li><a href="#field-requirements">5.7 <code>requirements</code> (optional)</a></li>
      <li><a href="#field-visibility">5.8 <code>visibility</code> (optional)</a></li>
    </ul>
  </li>
  <li><a href="#examples">6. Examples</a></li>
  <li><a href="#validation">7. Validation rules</a></li>
  <li><a href="#extensibility">8. Extensibility</a></li>
  <li><a href="#summary-section">9. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <strong>catalog</strong> section provides optional metadata used by development environments to index, search, and organize Frogs.
</p>

<p>
Catalog metadata is intended for:
</p>

<ul>
  <li>search and filtering</li>
  <li>example browsing</li>
  <li>category-based navigation</li>
  <li>library organization</li>
</ul>

<p>
The catalog section <strong>MUST NOT affect execution semantics</strong>.
Runtimes MUST ignore catalog information.
</p>

<hr/>

<h2 id="goals">2. Design goals</h2>

<ul>
  <li>Enable fast indexing and search</li>
  <li>Support browsing by category/task</li>
  <li>Support example discovery</li>
  <li>Remain tool-agnostic and extensible</li>
  <li>Never influence program execution</li>
</ul>

<hr/>

<h2 id="location">3. Location in a .frog file</h2>

<p>
The catalog object is an optional top-level section.
</p>

<pre>{
  "spec_version": "0.1",
  "metadata": {},
  "interface": {},
  "connector": {},
  "diagram": {},
  "front_panel": {},
  "catalog": { }
}</pre>

<p>
If omitted, tools MAY still index the Frog using metadata, but catalog features may be limited.
</p>

<hr/>

<h2 id="structure">4. Catalog object structure</h2>

<p>
Recommended structure:
</p>

<pre>"catalog": {
  "is_example": false,
  "title": "Readable Title",
  "summary": "One-line summary",
  "keywords": [],
  "categories": [],
  "paths": [],
  "requirements": {},
  "visibility": {}
}</pre>

<p>
Only a minimal subset is required if the object exists.
</p>

<hr/>

<h2 id="fields">5. Field definitions</h2>

<h3 id="field-is-example">5.1 <code>is_example</code></h3>

<p>
Indicates whether the Frog should be treated as an example by indexing tools.
</p>

<pre>"is_example": true</pre>

<ul>
  <li>MUST be a boolean if present.</li>
  <li>When true, tools MAY list the Frog in example browsers.</li>
</ul>

<hr/>

<h3 id="field-title">5.2 <code>title</code></h3>

<p>
Human-readable title used for browsing.
</p>

<pre>"title": "Basic Addition Example"</pre>

<ul>
  <li>MUST be a string if present.</li>
  <li>SHOULD be concise and user-friendly.</li>
</ul>

<hr/>

<h3 id="field-summary">5.3 <code>summary</code></h3>

<p>
Short one-line description intended for search results and preview cards.
</p>

<pre>"summary": "Demonstrates basic numeric input/output and addition."</pre>

<ul>
  <li>MUST be a string if present.</li>
  <li>SHOULD be one sentence.</li>
</ul>

<hr/>

<h3 id="field-keywords">5.4 <code>keywords</code></h3>

<p>
Search keywords for indexing tools.
</p>

<pre>"keywords": ["math", "addition", "numeric"]</pre>

<ul>
  <li>MUST be an array of strings if present.</li>
  <li>SHOULD contain short keywords.</li>
  <li>SHOULD be normalized (e.g., lowercase).</li>
</ul>

<hr/>

<h3 id="field-categories">5.5 <code>categories</code></h3>

<p>
Categories enable browsing by domain, task, or topic.
</p>

<pre>"categories": ["Examples", "Mathematics"]</pre>

<ul>
  <li>MUST be an array of strings if present.</li>
  <li>Order MAY be interpreted as hierarchy (from general to specific).</li>
</ul>

<hr/>

<h3 id="field-paths">5.6 <code>paths</code> (optional)</h3>

<p>
Optional navigation paths used by tools to build multiple browsing trees.
</p>

<pre>"paths": [
  "Examples/Mathematics/Basic",
  "Tutorials/Getting Started"
]</pre>

<ul>
  <li>MUST be an array of strings if present.</li>
  <li>Paths SHOULD use <code>/</code> as a separator.</li>
</ul>

<hr/>

<h3 id="field-requirements">5.7 <code>requirements</code> (optional)</h3>

<p>
Optional requirements used for filtering (hardware, software, execution profiles).
</p>

<pre>"requirements": {
  "hardware": ["Generic Sensor"],
  "software": ["frog.ui.standard"],
  "profiles": ["core"],
  "backends": []
}</pre>

<ul>
  <li>If present, MUST be an object.</li>
  <li>Tools MAY use it to filter search results.</li>
</ul>

Suggested keys:

<ul>
  <li><code>hardware</code> — array of strings</li>
  <li><code>software</code> — array of strings</li>
  <li><code>profiles</code> — array of strings (e.g., core, rt, fpga)</li>
  <li><code>backends</code> — array of strings (optional)</li>
</ul>

<hr/>

<h3 id="field-visibility">5.8 <code>visibility</code> (optional)</h3>

<p>
Optional tool hints controlling how the Frog should be displayed in catalogs.
</p>

<pre>"visibility": {
  "is_template": false,
  "is_hidden": false
}</pre>

<ul>
  <li>If present, MUST be an object.</li>
  <li>Runtimes MUST ignore this field.</li>
</ul>

<hr/>

<h2 id="examples">6. Examples</h2>

<h3>6.1 Minimal catalog</h3>

<pre>"catalog": {
  "is_example": true,
  "title": "Basic Addition Example",
  "keywords": ["math", "example"],
  "categories": ["Examples", "Mathematics"]
}</pre>

<h3>6.2 Extended catalog</h3>

<pre>"catalog": {
  "is_example": true,
  "title": "Sensor Read and Filter",
  "summary": "Reads a sensor value and applies a low-pass filter.",
  "keywords": ["sensor", "filter", "signal"],
  "categories": ["Examples", "Signal Processing"],
  "paths": ["Examples/Signal Processing/Sensors"],
  "requirements": {
    "hardware": ["Generic Sensor"],
    "software": ["frog.ui.standard"],
    "profiles": ["core"],
    "backends": []
  },
  "visibility": {
    "is_template": false,
    "is_hidden": false
  }
}</pre>

<hr/>

<h2 id="validation">7. Validation rules</h2>

Implementations MUST enforce:

<ul>
  <li>If <code>catalog</code> exists, it MUST be a JSON object.</li>
  <li>If present, <code>is_example</code> MUST be boolean.</li>
  <li>If present, <code>keywords</code> MUST be an array of strings.</li>
  <li>If present, <code>categories</code> MUST be an array of strings.</li>
</ul>

<p>
Unknown catalog fields:
</p>

<ul>
  <li>MAY be added by tools.</li>
  <li>MUST be ignored by runtimes.</li>
</ul>

<hr/>

<h2 id="extensibility">8. Extensibility</h2>

<p>
Tools MAY extend catalog metadata with additional properties.
</p>

<pre>"catalog": {
  "is_example": true,
  "title": "Example",
  "keywords": ["example"],
  "categories": ["Examples"],
  "difficulty": "beginner",
  "estimated_time_minutes": 10
}</pre>

<p>
Such fields MUST NOT affect execution and MUST be safely ignorable.
</p>

<hr/>

<h2 id="summary-section">9. Summary</h2>

<p>
The catalog section provides optional metadata for indexing and discovery.
</p>

<ul>
  <li>It enables search, browsing, and filtering.</li>
  <li>It supports example discovery.</li>
  <li>It never affects execution semantics.</li>
</ul>
