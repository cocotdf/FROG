<h1 align="center">🐸 FROG Cache Specification</h1>

<p align="center">
Definition of optional cache data for <strong>.frog</strong> programs<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Design Goals</a></li>
  <li><a href="#storage-options">3. Cache Storage Options</a></li>
  <li><a href="#cache-file">4. External <code>.frog.cache</code> File</a></li>
  <li><a href="#embedded-cache">5. Embedded <code>cache</code> Object</a></li>
  <li><a href="#model">6. Cache Model</a></li>
  <li><a href="#structure">7. Cache Object Structure</a></li>
  <li><a href="#fields">8. Top-Level Fields</a></li>
  <li><a href="#entry-kinds">9. Common Cache Entry Kinds</a></li>
  <li><a href="#authority-rules">10. Non-Authoritative Rules</a></li>
  <li><a href="#stale-cache">11. Stale or Invalid Cache Handling</a></li>
  <li><a href="#security">12. Security Considerations</a></li>
  <li><a href="#validation">13. Validation Rules</a></li>
  <li><a href="#examples">14. Examples</a></li>
  <li><a href="#summary">15. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <strong>cache</strong> mechanism stores optional derived data associated with a FROG program.
Its purpose is to accelerate tooling workflows such as validation, indexing, analysis, compilation preparation,
and execution IR generation.
</p>

<p>
A common use case is caching an intermediate representation (IR) derived from the canonical source
<code>.frog</code> file. However, cache is not limited to IR and MAY also contain other derived artifacts
useful to tools.
</p>

<p>
Cache data is <strong>non-authoritative</strong>.
The meaning of a FROG program is always defined by the canonical source expression,
not by any cache content.
</p>

<p>
Therefore:
</p>

<ul>
  <li>cache data <strong>MUST NOT</strong> define program semantics,</li>
  <li>cache data <strong>MUST NOT</strong> alter typing, scheduling, or observable behavior,</li>
  <li>cache data <strong>MUST</strong> be safe to delete and regenerate.</li>
</ul>

<hr/>

<h2 id="goals">2. Design Goals</h2>

<ul>
  <li>Speed up loading, validation, and compilation workflows</li>
  <li>Avoid recomputing derived IR and analysis artifacts when unchanged</li>
  <li>Keep source files authoritative and human-readable</li>
  <li>Allow cache to be safely deleted, ignored, or regenerated</li>
  <li>Prevent cache data from redefining execution semantics</li>
  <li>Support clean version control workflows with minimal diff noise</li>
</ul>

<hr/>

<h2 id="storage-options">3. Cache Storage Options</h2>

<p>
FROG supports two cache storage options:
</p>

<ul>
  <li><strong>Preferred:</strong> a separate sidecar cache file (<code>.frog.cache</code>)</li>
  <li><strong>Optional:</strong> an embedded <code>cache</code> object inside the canonical <code>.frog</code> file</li>
</ul>

<p>
The sidecar file is preferred because it keeps the canonical source cleaner and reduces noisy diffs,
merge conflicts, and unnecessary version control churn.
</p>

<p>
Embedded cache is still allowed for workflows where portability or single-file transport is desirable.
</p>

<hr/>

<h2 id="cache-file">4. External <code>.frog.cache</code> File</h2>

<p>
A cache sidecar file is associated with a source file by name.
</p>

<pre><code>example.frog
example.frog.cache</code></pre>

<p>
The external cache file MAY be generated automatically by tooling and MAY be deleted at any time.
Tools SHOULD regenerate it when needed.
</p>

<p>
The external cache file is a derived artifact. It is not part of the authoritative source definition.
</p>

<hr/>

<h2 id="embedded-cache">5. Embedded <code>cache</code> Object</h2>

<p>
In some workflows, tools MAY embed cache data directly inside the canonical <code>.frog</code> file.
</p>

<p>
If embedded, the <code>cache</code> object:
</p>

<ul>
  <li><strong>MUST</strong> remain optional,</li>
  <li><strong>MUST</strong> remain non-authoritative,</li>
  <li><strong>MUST NOT</strong> be required for correctness,</li>
  <li><strong>MUST</strong> be safe to remove without changing program meaning.</li>
</ul>

<p>
Embedded cache is allowed for convenience, but it is generally less desirable than a sidecar file for collaborative source control workflows.
</p>

<hr/>

<h2 id="model">6. Cache Model</h2>

<p>
The cache model is intentionally simple:
</p>

<pre><code>        Canonical source
     +----------------------+
     |     program.frog     |
     |----------------------|
     | metadata             |
     | interface            |
     | connector            |
     | diagram              |
     | front_panel          |
     | icon                 |
     | ide                  |
     | cache (optional)     |
     +----------+-----------+
                |
                | derived from source
                v
     +----------------------+
     |   source fingerprint |
     +----------+-----------+
                |
                v
     +----------------------+
     |       entries        |
     |----------------------|
     | frog.ir              |
     | frog.validation      |
     | frog.analysis        |
     | tool-specific data   |
     +----------------------+

Cache can be:
- embedded inside .frog
- external in .frog.cache

In all cases:
- derived
- optional
- non-authoritative
- safe to delete
</code></pre>

<hr/>

<h2 id="structure">7. Cache Object Structure</h2>

<p>
Recommended cache structure:
</p>

<pre><code>"cache": {
  "format_version": "0.1",
  "generator": {
    "tool": "frog-ide",
    "version": "0.1.0"
  },
  "source_fingerprint": "sha256:...",
  "entries": {
    "frog.ir": {
      "kind": "execution_ir",
      "schema_version": "0.1",
      "created": "2026-03-05T12:00:00Z",
      "depends_on": ["interface", "diagram", "front_panel"],
      "data": {}
    }
  }
}</code></pre>

<p>
This structure is generic enough to support multiple derived artifacts while keeping a stable,
simple contract.
</p>

<hr/>

<h2 id="fields">8. Top-Level Fields</h2>

<h3>8.1 <code>format_version</code></h3>

<p>
Version of the cache container format.
</p>

<ul>
  <li><strong>MUST</strong> be a string if present.</li>
  <li><strong>SHOULD</strong> identify the cache container schema version.</li>
</ul>

<h3>8.2 <code>generator</code></h3>

<p>
Describes the tool that generated the cache.
</p>

<pre><code>"generator": {
  "tool": "frog-ide",
  "version": "0.1.0"
}</code></pre>

<ul>
  <li><strong>MUST</strong> be an object if present.</li>
  <li>All fields are informational only.</li>
  <li><strong>MUST NOT</strong> affect program meaning.</li>
</ul>

<h3>8.3 <code>source_fingerprint</code></h3>

<p>
Fingerprint of the canonical source state from which the cache was derived.
</p>

<ul>
  <li><strong>MUST</strong> be a string if present.</li>
  <li><strong>SHOULD</strong> be stable for identical canonical source content.</li>
  <li><strong>SHOULD</strong> change when authoritative source content changes.</li>
  <li>Tools <strong>MUST</strong> treat cache as stale if the fingerprint does not match the current source.</li>
</ul>

<h3>8.4 <code>entries</code></h3>

<p>
Collection of named cache entries.
</p>

<ul>
  <li><strong>MUST</strong> be an object if present.</li>
  <li>Each property name identifies one cache entry.</li>
  <li>Unknown entries <strong>MUST</strong> be safely ignorable.</li>
</ul>

<p>
Recommended naming:
</p>

<ul>
  <li><code>frog.*</code> for project-defined common entries</li>
  <li>reverse-domain prefixes for tool-specific entries</li>
</ul>

<p>
Examples:
</p>

<ul>
  <li><code>frog.ir</code></li>
  <li><code>frog.validation</code></li>
  <li><code>frog.analysis</code></li>
  <li><code>com.graiphic.ide.symbol_index</code></li>
</ul>

<h3>8.5 Entry structure</h3>

<p>
Each entry SHOULD follow this general structure:
</p>

<pre><code>"frog.ir": {
  "kind": "execution_ir",
  "schema_version": "0.1",
  "created": "2026-03-05T12:00:00Z",
  "depends_on": ["interface", "diagram", "front_panel"],
  "data": {}
}</code></pre>

<ul>
  <li><code>kind</code> — high-level category of cache entry</li>
  <li><code>schema_version</code> — version of the entry payload schema</li>
  <li><code>created</code> — creation timestamp in ISO 8601 UTC form</li>
  <li><code>depends_on</code> — source sections or stable dependency identifiers</li>
  <li><code>data</code> — opaque JSON payload containing the cached artifact</li>
</ul>

<p>
The <code>data</code> field MAY contain any valid JSON value, but it <strong>MUST</strong> contain only derived information.
</p>

<hr/>

<h2 id="entry-kinds">9. Common Cache Entry Kinds</h2>

<h3>9.1 Execution IR cache</h3>

<p>
Stores a cached execution-oriented intermediate representation derived from the source graph.
</p>

<p>
This is the most common and most important cache use case.
It is intended to accelerate repeated validation, compilation, and execution preparation.
</p>

<h3>9.2 Validation cache</h3>

<p>
Stores derived validation outcomes, such as:
</p>

<ul>
  <li>validation status,</li>
  <li>diagnostic counts,</li>
  <li>resolved warning sets,</li>
  <li>last validated profile.</li>
</ul>

<h3>9.3 Analysis cache</h3>

<p>
Stores derived structural information, such as:
</p>

<ul>
  <li>symbol indexes,</li>
  <li>dependency analysis results,</li>
  <li>graph summaries,</li>
  <li>editor lookup tables.</li>
</ul>

<h3>9.4 Tool-specific cache</h3>

<p>
Tools MAY store private derived data under their own namespace, provided that the data remains optional,
safe to ignore, and non-authoritative.
</p>

<hr/>

<h2 id="authority-rules">10. Non-Authoritative Rules</h2>

<p>
Cache data <strong>MUST</strong> be treated as an optimization only.
</p>

<ul>
  <li>Runtimes <strong>MUST NOT</strong> require cache data to execute a program.</li>
  <li>Runtimes <strong>MUST NOT</strong> trust cache data for correctness.</li>
  <li>Tools <strong>MUST</strong> be able to rebuild cache data from the canonical <code>.frog</code> source.</li>
  <li>If cache conflicts with source content, the source content <strong>MUST</strong> win.</li>
  <li>Removing cache <strong>MUST NOT</strong> change the meaning of the program.</li>
</ul>

<hr/>

<h2 id="stale-cache">11. Stale or Invalid Cache Handling</h2>

<p>
Cache data SHOULD be treated as stale when:
</p>

<ul>
  <li><code>source_fingerprint</code> does not match the current source content,</li>
  <li><code>format_version</code> is not supported,</li>
  <li>an entry <code>schema_version</code> is not supported,</li>
  <li>an entry payload fails validation,</li>
  <li>required dependencies listed in <code>depends_on</code> have changed,</li>
  <li>the cache payload is incomplete or corrupted.</li>
</ul>

<p>
When stale or invalid:
</p>

<ul>
  <li>tools <strong>SHOULD</strong> discard the cache and regenerate it,</li>
  <li>runtimes <strong>MUST</strong> ignore the cache for correctness decisions,</li>
  <li>tools <strong>MAY</strong> keep only the valid cache entries and regenerate the others.</li>
</ul>

<hr/>

<h2 id="security">12. Security Considerations</h2>

<p>
Cache content MUST NOT be treated as executable truth.
</p>

<ul>
  <li>Tools <strong>SHOULD</strong> validate cache payloads before use.</li>
  <li>Runtimes <strong>MUST</strong> validate source-derived IR regardless of cache presence.</li>
  <li>Tools <strong>SHOULD</strong> avoid storing secrets or sensitive information in cache.</li>
  <li>Cache data MAY be treated as untrusted input.</li>
</ul>

<p>
A malformed cache file MUST NOT compromise correctness.
At worst, it should be ignored and regenerated.
</p>

<hr/>

<h2 id="validation">13. Validation Rules</h2>

<p>
Implementations MUST enforce the following rules:
</p>

<ul>
  <li>If present, embedded <code>cache</code> <strong>MUST</strong> be a JSON object.</li>
  <li>If present, external <code>.frog.cache</code> root content <strong>MUST</strong> be a JSON object.</li>
  <li>If present, <code>format_version</code> <strong>MUST</strong> be a string.</li>
  <li>If present, <code>generator</code> <strong>MUST</strong> be an object.</li>
  <li>If present, <code>source_fingerprint</code> <strong>MUST</strong> be a string.</li>
  <li>If present, <code>entries</code> <strong>MUST</strong> be an object.</li>
  <li>Each entry value inside <code>entries</code> <strong>MUST</strong> be an object.</li>
  <li>If present, entry <code>kind</code> <strong>MUST</strong> be a string.</li>
  <li>If present, entry <code>schema_version</code> <strong>MUST</strong> be a string or integer.</li>
  <li>If present, entry <code>created</code> <strong>MUST</strong> be a string.</li>
  <li>If present, entry <code>depends_on</code> <strong>MUST</strong> be an array of strings.</li>
  <li>Entry <code>data</code> <strong>MAY</strong> be any valid JSON value.</li>
  <li>Unknown cache entries <strong>MUST</strong> be ignorable.</li>
  <li>Invalid, unreadable, stale, or incompatible cache <strong>MUST NOT</strong> change correctness.</li>
</ul>

<hr/>

<h2 id="examples">14. Examples</h2>

<h3>14.1 Minimal embedded cache object</h3>

<pre><code>"cache": {
  "format_version": "0.1",
  "source_fingerprint": "sha256:...",
  "entries": {
    "frog.ir": {
      "kind": "execution_ir",
      "schema_version": "0.1",
      "data": {}
    }
  }
}</code></pre>

<h3>14.2 Extended embedded cache object</h3>

<pre><code>"cache": {
  "format_version": "0.1",
  "generator": {
    "tool": "frog-ide",
    "version": "0.1.0"
  },
  "source_fingerprint": "sha256:7d1b...c9",
  "entries": {
    "frog.ir": {
      "kind": "execution_ir",
      "schema_version": "0.1",
      "created": "2026-03-05T12:00:00Z",
      "depends_on": ["interface", "diagram", "front_panel"],
      "data": {
        "graph": {},
        "types": {}
      }
    },
    "frog.validation": {
      "kind": "validation",
      "schema_version": "0.1",
      "created": "2026-03-05T12:00:01Z",
      "depends_on": ["interface", "diagram"],
      "data": {
        "valid": true,
        "errors": []
      }
    }
  }
}</code></pre>

<h3>14.3 External sidecar cache file</h3>

<pre><code>{
  "format_version": "0.1",
  "generator": {
    "tool": "frog-cli",
    "version": "0.1.0"
  },
  "source_fingerprint": "sha256:7d1b...c9",
  "entries": {
    "frog.ir": {
      "kind": "execution_ir",
      "schema_version": "0.1",
      "created": "2026-03-05T12:00:00Z",
      "depends_on": ["interface", "diagram", "front_panel"],
      "data": {
        "graph": {}
      }
    }
  }
}</code></pre>

<hr/>

<h2 id="summary">15. Summary</h2>

<p>
The cache mechanism provides optional acceleration for tooling workflows.
</p>

<ul>
  <li>Preferred storage is a separate <code>.frog.cache</code> file.</li>
  <li>Embedded cache is allowed but secondary.</li>
  <li>Cache data is derived, optional, and non-authoritative.</li>
  <li>Execution IR is a primary cache use case, but not the only one.</li>
  <li>Source content always defines program meaning.</li>
</ul>

<p>
In FROG, source is authoritative.<br/>
Cache is only an optimization.
</p>
