<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="150" />
</p>

<h1 align="center">🐸 FROG IDE Snippet Legacy Redirect</h1>

<p align="center">
Legacy redirect for the deprecated duplicate snippet specification file<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Overview</h2>

<p>
This file is deprecated.
The canonical FROG snippet specification is:
</p>

<p>
<strong><code>IDE/Snippet.md</code></strong>
</p>

<p>
This legacy file is retained temporarily only to avoid broken references during repository cleanup and transition.
It MUST NOT be treated as an independent normative specification.
</p>

<hr/>

<h2>Normative Status</h2>

<ul>
  <li><code>IDE/Snippet.md</code> is the single canonical specification for FROG IDE snippets.</li>
  <li>This file is a legacy redirect only.</li>
  <li>This file MUST NOT define, override, or extend snippet semantics independently.</li>
  <li>If any conflict appears between this file and <code>IDE/Snippet.md</code>, <code>IDE/Snippet.md</code> always takes precedence.</li>
</ul>

<hr/>

<h2>Reason for Deprecation</h2>

<p>
This file duplicated the snippet topic under a competing document name and created unnecessary ambiguity in repository ownership.
The repository architecture now uses a single canonical snippet specification located at <code>IDE/Snippet.md</code>.
</p>

<p>
The canonical specification defines the FROG snippet as an image-backed IDE artifact whose embedded structured payload can be
decoded by a conforming FROG IDE during import, paste, or drag-and-drop.
</p>

<hr/>

<h2>Migration Rule</h2>

<p>
Any existing internal or external reference to:
</p>

<p>
<code>IDE/FROG Snippet.md.</code>
</p>

<p>
SHOULD be updated to:
</p>

<p>
<code>IDE/Snippet.md</code>
</p>

<hr/>

<h2>Future Repository Cleanup</h2>

<p>
This file MAY be removed entirely in a future repository cleanup pass once all references have been updated.
</p>
