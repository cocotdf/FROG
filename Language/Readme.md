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
  <li><a href="#document-map">3. Document Map</a></li>
  <li><a href="#current-documents">4. Current Documents</a></li>
  <li><a href="#relation-with-expression">5. Relation with Expression</a></li>
  <li><a href="#relation-with-libraries-and-ide">6. Relation with Libraries and IDE</a></li>
  <li><a href="#role-in-the-repository">7. Role in the Repository</a></li>
  <li><a href="#status">8. Status</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines cross-cutting language semantics for FROG.
It specifies what a validated FROG means at execution time when that meaning cannot be owned by one isolated source section or one primitive-library document alone.
</p>

<p>
These topics are cross-cutting because they constrain executable graph meaning across diagram structure, structural regions, local memory, cycle validity, execution context, committed state, and source-aligned observation/control boundaries.
</p>

<p>
In the repository architecture, <code>Language/</code> is the normative home of execution semantics.
It is distinct from:
</p>

<ul>
  <li>the canonical source representation defined in <code>Expression/</code>,</li>
  <li>the standard primitive catalogs defined in <code>Libraries/</code>,</li>
  <li>the authoring, observability, debugging, and inspection model defined in <code>IDE/</code>.</li>
</ul>

<p>
This separation exists so that FROG can keep source form, execution meaning, primitive definition, and tooling behavior as distinct long-term normative responsibilities.
</p>

<hr/>

<h2 id="scope-of-this-directory">2. Scope of this Directory</h2>

<p>
This directory is concerned with language-level execution semantics that apply across the executable model.
It defines semantic rules that remain valid independently of a particular IDE, runtime implementation, compiler pipeline, transport mechanism, or execution target.
</p>

<p>
This directory defines topics such as:
</p>

<ul>
  <li>the normative meaning of control structures,</li>
  <li>the normative meaning of explicit local memory,</li>
  <li>the conditions under which feedback cycles are valid,</li>
  <li>the execution-model concepts needed to interpret a validated FROG at runtime,</li>
  <li>the source-safe boundaries at which execution may be observed, paused, debug-stopped, completed, faulted, or aborted coherently.</li>
</ul>

<p>
This directory does not define:
</p>

<ul>
  <li>the full canonical <code>.frog</code> top-level source structure,</li>
  <li>the full widget model,</li>
  <li>the full front-panel model,</li>
  <li>the standard primitive catalog as a whole,</li>
  <li>IDE-facing breakpoint UX, watch UX, probe UX, snippet UX, or debugger command UX,</li>
  <li>a runtime-internal scheduler architecture,</li>
  <li>execution IR, lowering, compiler-backend contracts, or deployment profiles as normative closed layers for v0.1.</li>
</ul>

<p>
Those concerns are defined elsewhere in the repository or remain future work outside the current closed scope of <code>Language/</code>.
</p>

<hr/>

<h2 id="document-map">3. Document Map</h2>

<p>
The current role of <code>Language/</code> can be summarized as follows:
</p>

<pre>
Expression/  -> canonical source form
Language/    -> normative execution meaning
Libraries/   -> standard primitive families and primitive-local behavior
IDE/         -> authoring, observability, debugging, inspection, tooling UX
</pre>

<p>
Within <code>Language/</code>, the current internal split is:
</p>

<pre>
Language/
├── Control structures.md
│   └── normative execution meaning of case / for_loop / while_loop
├── State and cycles.md
│   └── normative meaning of explicit local memory and valid feedback cycles
├── Execution model.md
│   └── execution-model core: validated executable graph, live execution instance,
│       source identity, activation, execution context, committed source-level state
└── Execution control and observation boundaries.md
    └── safe observation points, pause-consistent snapshots, safe debug stops,
        and terminal control/observation boundaries
</pre>

<p>
This organization keeps the directory small enough to remain readable, while still giving execution semantics a complete enough normative baseline for observability and debugging to build on.
</p>

<hr/>

<h2 id="current-documents">4. Current Documents</h2>

<p>
This directory currently contains:
</p>

<ul>
  <li><code>Control structures.md</code> — normative execution semantics for language structures such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>,</li>
  <li><code>State and cycles.md</code> — normative semantics for explicit local memory and rules for valid feedback cycles,</li>
  <li><code>Execution model.md</code> — normative execution-model concepts such as validated executable graph, live execution instance, source identity, activation, execution context, semantic milestones, and committed source-level state,</li>
  <li><code>Execution control and observation boundaries.md</code> — normative definition of safe observation points, pause-consistent snapshots, safe debug stops, and minimal completion/fault/abort boundary semantics.</li>
</ul>

<p>
Taken together, these documents define the language-level baseline for:
</p>

<ul>
  <li>how structural regions behave,</li>
  <li>how branching and looping are interpreted,</li>
  <li>how cyclic graphs become valid,</li>
  <li>how explicit local memory is interpreted,</li>
  <li>how validated execution is modeled at the language level,</li>
  <li>where execution may be observed or controlled without losing source-level coherence.</li>
</ul>

<p>
Additional cross-cutting semantic specifications MAY be added here later when they belong to the execution semantics of the language itself rather than to source serialization, primitive catalogs, or IDE tooling.
</p>

<hr/>

<h2 id="relation-with-expression">5. Relation with Expression</h2>

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
  <li><code>Expression/</code> owns canonical source structure, serialization shape, source-level representation rules, and canonical source identity,</li>
  <li><code>Language/</code> owns cross-cutting execution semantics such as structure meaning, local-memory meaning, cycle-validity meaning, execution-model meaning, and source-safe control/observation boundaries.</li>
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

<h2 id="relation-with-libraries-and-ide">6. Relation with Libraries and IDE</h2>

<p>
<code>Language/</code> is also distinct from <code>Libraries/</code> and <code>IDE/</code>.
</p>

<p>
The responsibility split is:
</p>

<ul>
  <li><code>Libraries/</code> define standard primitive families, primitive names, primitive-local ports, metadata, and primitive-local behavior,</li>
  <li><code>Language/</code> defines cross-cutting execution meaning that spans beyond one primitive family or one source section,</li>
  <li><code>IDE/</code> defines how execution is authored, observed, debugged, inspected, and presented to users or tools.</li>
</ul>

<p>
This means, for example:
</p>

<ul>
  <li>a primitive such as <code>frog.core.delay</code> belongs to <code>Libraries/</code> for its primitive-local definition,</li>
  <li>the cross-cutting meaning of local memory and valid cycles belongs to <code>Language/</code>,</li>
  <li>the IDE-facing projection of committed observations, debug stops, probes, and watches belongs to <code>IDE/</code>.</li>
</ul>

<p>
The repository remains cleaner and more durable when these ownership boundaries stay explicit.
</p>

<hr/>

<h2 id="role-in-the-repository">7. Role in the Repository</h2>

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
  <li>clean attachment points for observability and debugging without forcing those layers to redefine execution meaning,</li>
  <li>long-term architectural cleanup without collapsing distinct responsibilities into one layer.</li>
</ul>

<p>
In practical terms:
</p>

<ul>
  <li>read <code>Expression/</code> for canonical source structure,</li>
  <li>read <code>Language/</code> for cross-cutting execution semantics,</li>
  <li>read <code>Libraries/</code> for standardized primitive catalogs and primitive families,</li>
  <li>read <code>IDE/</code> for authoring, observability, debugging, and inspection behavior.</li>
</ul>

<hr/>

<h2 id="status">8. Status</h2>

<p>
At the current repository stage, <code>Language/</code> remains intentionally focused rather than broad.
It is still significantly smaller than <code>Expression/</code> and does not attempt to define a full runtime architecture.
</p>

<p>
However, it is no longer limited to only structure semantics and cycle semantics.
For FROG v0.1, this directory now establishes the execution-semantics baseline for:
</p>

<ul>
  <li>control structures,</li>
  <li>explicit local memory,</li>
  <li>cycle validity,</li>
  <li>execution-model core concepts,</li>
  <li>source-safe observation and control boundaries.</li>
</ul>

<p>
This makes <code>Language/</code> the layer that a serious FROG IDE, runtime, validator, or compiler can rely on when it needs normative execution meaning without confusing that meaning with canonical source form or IDE-facing tooling behavior.
</p>

<p>
As the repository architecture continues to mature, additional cross-cutting semantic topics MAY be added here when they belong to the language execution model itself.
That growth SHOULD remain disciplined:
</p>

<ul>
  <li>do not move source-shape topics here when they belong to <code>Expression/</code>,</li>
  <li>do not move primitive-catalog topics here when they belong to <code>Libraries/</code>,</li>
  <li>do not move tooling-UX topics here when they belong to <code>IDE/</code>,</li>
  <li>do add topics here when they define execution meaning that multiple other layers must rely on.</li>
</ul>

<p>
The long-term goal is a stable repository architecture in which <code>Expression/</code>, <code>Language/</code>, <code>Libraries/</code>, and <code>IDE/</code> each own a clearly separated normative responsibility.
</p>
