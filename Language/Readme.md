<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="150" />
</p>

<h1 align="center">🐸 FROG Language</h1>

<p align="center">
  Cross-cutting language semantics and repository continuity for <strong>FROG</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope-of-this-directory">2. Scope of this Directory</a></li>
  <li><a href="#current-documents">3. Current Documents</a></li>
  <li><a href="#relation-with-expression">4. Relation with Expression</a></li>
  <li><a href="#role-in-the-repository">5. Role in the Repository</a></li>
  <li><a href="#status">6. Status</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory contains language-semantics documents related to control structures, local memory, and cycle validity.
</p>

<p>
These topics are cross-cutting because they constrain executable graph meaning rather than belonging to one isolated top-level JSON section.
</p>

<p>
At the current repository stage, this directory remains present for repository continuity while the canonical source-spec reading is centered in <code>Expression/</code>.
</p>

<hr/>

<h2 id="scope-of-this-directory">2. Scope of this Directory</h2>

<p>
This directory is concerned with language-level execution semantics that apply across the executable model.
It is not a complete alternative to the canonical source specification.
</p>

<p>
This directory does not define:
</p>

<ul>
  <li>the full canonical <code>.frog</code> top-level source structure,</li>
  <li>the full widget model,</li>
  <li>the full front-panel model,</li>
  <li>the standard primitive catalog as a whole.</li>
</ul>

<p>
Those concerns are defined elsewhere in the repository.
</p>

<hr/>

<h2 id="current-documents">3. Current Documents</h2>

<p>
This directory currently contains:
</p>

<ul>
  <li><code>Control structures.md</code> — language structures such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>,</li>
  <li><code>State and cycles.md</code> — explicit local memory and rules for valid feedback cycles.</li>
</ul>

<p>
These topics are foundational for executable semantics because they constrain:
</p>

<ul>
  <li>how structural regions behave,</li>
  <li>how loops and branching are represented,</li>
  <li>how cyclic graphs become valid,</li>
  <li>how explicit local memory is interpreted.</li>
</ul>

<hr/>

<h2 id="relation-with-expression">4. Relation with Expression</h2>

<p>
The current repository also contains corresponding documents in <code>Expression/</code>:
</p>

<ul>
  <li><code>Expression/Control structures.md</code></li>
  <li><code>Expression/State and cycles.md</code></li>
</ul>

<p>
For canonical source-spec reading, the <code>Expression/</code> versions are the primary reference.
</p>

<p>
Accordingly:
</p>

<ul>
  <li><code>Expression/</code> is the canonical home of the source-level specification,</li>
  <li><code>Language/</code> remains present as part of the current repository organization and semantic continuity.</li>
</ul>

<p>
This means that the documents in this directory should be understood as repository-level semantic companions rather than as a separate canonical source layer.
</p>

<hr/>

<h2 id="role-in-the-repository">5. Role in the Repository</h2>

<p>
This directory helps preserve continuity in the repository while the specification architecture is being progressively stabilized.
</p>

<p>
Its presence makes the following easier:
</p>

<ul>
  <li>historical continuity of semantic documents,</li>
  <li>cross-checking between earlier and newer repository organization,</li>
  <li>incremental cleanup without losing semantic material.</li>
</ul>

<p>
In practical terms:
</p>

<ul>
  <li>read <code>Expression/</code> for canonical source-spec structure,</li>
  <li>read <code>Libraries/</code> for standardized primitive catalogs,</li>
  <li>treat <code>Language/</code> as the semantic continuity layer of the current repository layout.</li>
</ul>

<hr/>

<h2 id="status">6. Status</h2>

<p>
At the current repository stage, <code>Language/</code> remains intentionally small.
It contains two foundational semantic documents and exists primarily for repository continuity and clarity during the present organization phase.
</p>

<p>
Long term, the repository may continue to simplify around the canonical source-spec reading centered in <code>Expression/</code>.
Until then, this directory remains a useful semantic anchor inside the repository.
</p>
