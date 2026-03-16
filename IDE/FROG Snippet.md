<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG IDE Snippet Legacy Redirect</h1>

<p align="center">
Legacy redirect for the deprecated duplicate snippet specification file<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#normative-status">2. Normative Status</a></li>
  <li><a href="#architectural-position">3. Architectural Position</a></li>
  <li><a href="#migration-rule">4. Migration Rule</a></li>
  <li><a href="#future-repository-cleanup">5. Future Repository Cleanup</a></li>
  <li><a href="#summary">6. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This file is a <strong>legacy redirect document</strong>.
</p>

<p>
The single canonical specification for FROG IDE snippets is:
</p>

<p>
<strong><code>IDE/Snippet.md</code></strong>
</p>

<p>
This file is retained temporarily only to preserve repository continuity, avoid broken references, and make the cleanup transition explicit.
It MUST NOT be treated as an independent normative specification.
</p>

<pre>
Snippet specification ownership

IDE/FROG Snippet.md -> legacy redirect only
IDE/Snippet.md      -> canonical specification
</pre>

<hr/>

<h2 id="normative-status">2. Normative Status</h2>

<ul>
  <li><code>IDE/Snippet.md</code> is the single canonical specification for FROG IDE snippets.</li>
  <li>This file is a legacy redirect only.</li>
  <li>This file MUST NOT define, override, interpret, or extend snippet semantics independently.</li>
  <li>If any conflict appears between this file and <code>IDE/Snippet.md</code>, <code>IDE/Snippet.md</code> always takes precedence.</li>
</ul>

<p>
Accordingly, implementers, tools, and readers MUST treat this file as non-authoritative for snippet semantics.
</p>

<hr/>

<h2 id="architectural-position">3. Architectural Position</h2>

<p>
This document belongs to the IDE layer only as a repository transition aid.
It does not introduce a second snippet model.
</p>

<pre>
Repository architecture around snippet documents

Expression/   -> canonical source form
Language/     -> normative execution semantics
Libraries/    -> intrinsic primitive vocabularies
Profiles/     -> optional standardized capability families
IDE/          -> authoring, observability, debugging, inspection, snippets

Within IDE/
- Snippet.md         -> normative snippet specification
- FROG Snippet.md    -> legacy redirect only
</pre>

<p>
This file therefore exists for navigation continuity, not for semantic ownership.
</p>

<hr/>

<h2 id="migration-rule">4. Migration Rule</h2>

<p>
Any existing internal or external reference to:
</p>

<p>
<code>IDE/FROG Snippet.md</code>
</p>

<p>
SHOULD be updated to:
</p>

<p>
<code>IDE/Snippet.md</code>
</p>

<p>
New references SHOULD point directly to <code>IDE/Snippet.md</code> rather than to this file.
</p>

<pre>
Migration rule

Old reference  -> IDE/FROG Snippet.md
New reference  -> IDE/Snippet.md
</pre>

<hr/>

<h2 id="future-repository-cleanup">5. Future Repository Cleanup</h2>

<p>
This file MAY be removed entirely in a future repository cleanup pass once continuity and inbound-reference concerns are no longer relevant.
</p>

<p>
Until then, it SHOULD remain short and SHOULD continue to function only as a redirect document.
</p>

<p>
It SHOULD NOT accumulate duplicated examples, transport rules, payload rules, or insertion semantics already owned by <code>IDE/Snippet.md</code>.
</p>

<hr/>

<h2 id="summary">6. Summary</h2>

<p>
This file is a temporary legacy redirect.
The canonical FROG snippet specification is <code>IDE/Snippet.md</code>.
</p>

<ul>
  <li>This file exists only for continuity and redirect purposes.</li>
  <li>It MUST NOT act as a second normative specification.</li>
  <li>Conflicts are resolved in favor of <code>IDE/Snippet.md</code>.</li>
  <li>References SHOULD be migrated to <code>IDE/Snippet.md</code>.</li>
  <li>This file MAY be removed in a later cleanup phase.</li>
</ul>
