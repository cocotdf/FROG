<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="150" />
</p>

<h1 align="center">🐸 FROG Language</h1>

<p align="center">
  Normative execution semantics for <strong>FROG</strong><br/>
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
This directory defines cross-cutting language semantics for FROG.
It specifies what a validated FROG means at execution time when that meaning cannot be owned by one isolated source section or one primitive-library document alone.
</p>

<p>
These topics are cross-cutting because they constrain executable graph meaning across diagram structure, structural regions, local memory, and cycle validity.
</p>

<p>
In the repository architecture, <code>Language/</code> is the normative home of execution semantics.
It is distinct from the canonical source representation defined in <code>Expression/</code>, from the standard primitive catalogs defined in <code>Libraries/</code>, and from the authoring and inspection model defined in <code>IDE/</code>.
</p>

<hr/>

<h2 id="scope-of-this-directory">2. Scope of this Directory</h2>

<p>
This directory is concerned with language-level execution semantics that apply across the executable model.
It defines semantic rules that remain valid independently of a particular IDE, runtime implementation, compiler pipeline, or execution target.
</p>

<p>
This directory does not define:
</p>

<ul>
  <li>the full canonical <code>.frog</code> top-level source structure,</li>
  <li>the full widget model,</li>
  <li>the full front-panel model,</li>
  <li>the standard primitive catalog as a whole,</li>
  <li>IDE-facing debugging, probe, watch, or snippet behavior.</li>
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
  <li><code>Control structures.md</code> — normative execution semantics for language structures such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>,</li>
  <li><code>State and cycles.md</code> — normative semantics for explicit local memory and rules for valid feedback cycles.</li>
</ul>

<p>
These topics are foundational because they constrain:
</p>

<ul>
  <li>how structural regions behave,</li>
  <li>how branching and looping are interpreted,</li>
  <li>how cyclic graphs become valid,</li>
  <li>how explicit local memory is interpreted.</li>
</ul>

<p>
Additional cross-cutting semantic specifications MAY be added here later when they belong to the execution semantics of the language itself rather than to source serialization, primitive catalogs, or IDE tooling.
</p>

<hr/>

<h2 id="relation-with-expression">4. Relation with Expression</h2>

<p>
<code>Expression/</code> and <code>Language/</code> are related but distinct layers of the specification.
</p>

<ul>
  <li><code>Expression/</code> defines how a FROG is represented as canonical source.</li>
  <li><code>Language/</code> defines what a validated FROG means when it executes.</li>
</ul>

<p>
Accordingly:
</p>

<ul>
  <li><code>Expression/</code> owns canonical source structure, serialization shape, and source-level representation rules,</li>
  <li><code>Language/</code> owns cross-cutting execution semantics such as structure meaning, local-memory meaning, and cycle-validity meaning.</li>
</ul>

<p>
When a topic has both a source-representation aspect and an execution-semantics aspect, the responsibilities MUST remain separated:
</p>

<ul>
  <li><code>Expression/</code> defines the canonical source form,</li>
  <li><code>Language/</code> defines the normative execution meaning.</li>
</ul>

<p>
This separation allows the repository to keep the source format explicit while also giving execution semantics a stable normative home of their own.
</p>

<hr/>

<h2 id="role-in-the-repository">5. Role in the Repository</h2>

<p>
This directory provides the normative execution-semantics layer of the repository.
Its role is to keep execution meaning explicit, durable, and independent from source-serialization details or IDE behavior.
</p>

<p>
Its presence makes the following easier:
</p>

<ul>
  <li>clear separation between source representation and execution meaning,</li>
  <li>stable interpretation of validated executable graphs across independent implementations,</li>
  <li>consistent reuse of language semantics by IDEs, runtimes, validators, and compilers,</li>
  <li>long-term architectural cleanup without collapsing distinct responsibilities into one layer.</li>
</ul>

<p>
In practical terms:
</p>

<ul>
  <li>read <code>Expression/</code> for canonical source structure,</li>
  <li>read <code>Language/</code> for cross-cutting execution semantics,</li>
  <li>read <code>Libraries/</code> for standardized primitive catalogs,</li>
  <li>read <code>IDE/</code> for authoring, observability, debugging, and inspection behavior.</li>
</ul>

<hr/>

<h2 id="status">6. Status</h2>

<p>
At the current repository stage, <code>Language/</code> remains intentionally small.
It currently contains two foundational semantic documents, but its role is normative rather than transitional.
</p>

<p>
For FROG v0.1, this directory establishes the execution-semantics baseline for:
</p>

<ul>
  <li>control structures,</li>
  <li>explicit local memory,</li>
  <li>cycle validity.</li>
</ul>

<p>
As the repository architecture continues to mature, additional cross-cutting semantic topics MAY be moved here when they belong to the language execution model itself.
</p>

<p>
The long-term goal is a stable repository architecture in which <code>Expression/</code>, <code>Language/</code>, <code>Libraries/</code>, and <code>IDE/</code> each own a clearly separated normative responsibility.
</p>
