<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
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
  <li><a href="#why-this-layer-exists">2. Why this Layer Exists</a></li>
  <li><a href="#scope-of-this-directory">3. Scope of this Directory</a></li>
  <li><a href="#document-map">4. Document Map</a></li>
  <li><a href="#current-documents">5. Current Documents</a></li>
  <li><a href="#relation-with-expression">6. Relation with Expression</a></li>
  <li><a href="#relation-with-ir">7. Relation with IR</a></li>
  <li><a href="#relation-with-libraries-profiles-and-ide">8. Relation with Libraries, Profiles, and IDE</a></li>
  <li><a href="#semantic-layering-inside-language">9. Semantic Layering inside Language</a></li>
  <li><a href="#role-in-the-repository">10. Role in the Repository</a></li>
  <li><a href="#status">11. Status</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines cross-cutting language semantics for FROG.
It specifies what a validated FROG means at execution time when that meaning cannot be owned by one isolated source section, one intrinsic primitive-library document, one optional profile specification, or one execution-facing derived-representation document alone.
</p>

<p>
These topics are cross-cutting because they constrain executable graph meaning across diagram structure, structural regions, local memory, cycle validity, execution context, committed state, and source-aligned observation/control boundaries.
</p>

<p>
In the repository architecture, <code>Language/</code> is the normative home of <strong>validated execution meaning</strong>.
It is distinct from:
</p>

<ul>
  <li>the canonical source representation defined in <code>Expression/</code>,</li>
  <li>the execution-facing derived representations defined in <code>IR/</code>,</li>
  <li>the intrinsic primitive catalogs defined in <code>Libraries/</code>,</li>
  <li>the optional standardized capability families defined in <code>Profiles/</code>,</li>
  <li>the authoring, observability, debugging, and inspection model defined in <code>IDE/</code>.</li>
</ul>

<p>
This separation exists so that FROG can keep source form, validated meaning, execution-facing derivation, primitive definition, optional capability definition, and tooling behavior as distinct long-term normative responsibilities.
</p>

<pre><code>Repository architecture around Language/

Expression/   -> canonical source form
Language/     -> normative validated execution meaning
IR/           -> execution-facing derived representation
Libraries/    -> intrinsic primitive vocabularies
Profiles/     -> optional standardized capability families
IDE/          -> authoring, observability, debugging, inspection

Language/ owns semantic truth that multiple other layers rely on.
</code></pre>

<hr/>

<h2 id="why-this-layer-exists">2. Why this Layer Exists</h2>

<p>
A language needs more than a source format.
It also needs a stable place where validated program behavior is defined at the semantic level.
That is the role of <code>Language/</code>.
</p>

<p>
Without a dedicated execution-semantics layer, cross-cutting meaning would tend to drift into:
</p>

<ul>
  <li>source-shape documents,</li>
  <li>primitive-catalog documents,</li>
  <li>execution-facing IR documents,</li>
  <li>runtime implementation notes,</li>
  <li>IDE debugging behavior,</li>
  <li>vendor-specific execution assumptions.</li>
</ul>

<p>
This directory exists to prevent that drift.
It gives validated execution meaning a durable normative home that remains independent from:
</p>

<ul>
  <li>how a program is serialized,</li>
  <li>how an IDE edits it,</li>
  <li>how an IR makes execution-facing structure explicit,</li>
  <li>how a runtime internally schedules it,</li>
  <li>how a compiler lowers it,</li>
  <li>how one particular implementation presents it to users.</li>
</ul>

<p>
In simple terms:
</p>

<pre><code>Expression/ says:
"how the program is written"

Language/ says:
"what the validated program means when it executes"

IR/ says:
"how execution-facing derived form may be built from that meaning"
</code></pre>

<hr/>

<h2 id="scope-of-this-directory">3. Scope of this Directory</h2>

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
  <li>the intrinsic primitive catalog as a whole,</li>
  <li>the optional profile catalog as a whole,</li>
  <li>IDE-facing breakpoint UX, watch UX, probe UX, snippet UX, or debugger command UX,</li>
  <li>a runtime-internal scheduler architecture,</li>
  <li>the open execution-facing IR object model itself,</li>
  <li>lowering, compiler-backend contracts, or deployment profiles as fully closed language-owned layers.</li>
</ul>

<p>
Those concerns are defined elsewhere in the repository or remain future work outside the current closed scope of <code>Language/</code>.
</p>

<pre><code>Language/ owns:
- cross-cutting execution meaning
- validated graph interpretation
- structure semantics
- cycle / memory semantics
- semantic observation/control boundaries

Language/ does not own:
- source serialization
- execution-facing IR structure
- primitive catalogs
- optional capability catalogs
- IDE UX
- runtime-private internals
</code></pre>

<hr/>

<h2 id="document-map">4. Document Map</h2>

<p>
The current role of <code>Language/</code> can be summarized as follows:
</p>

<pre><code>Expression/  -> canonical source form
Language/    -> normative validated execution meaning
IR/          -> execution-facing derived representation
Libraries/   -> intrinsic primitive families and primitive-local behavior
Profiles/    -> optional standardized capability families
IDE/         -> authoring, observability, debugging, inspection, tooling UX
</code></pre>

<p>
Within <code>Language/</code>, the current internal split is:
</p>

<pre><code>Language/
├── Readme.md
│   -> architectural entry point for normative execution semantics
├── Control structures.md
│   -> normative execution meaning of case / for_loop / while_loop
├── State and cycles.md
│   -> normative meaning of explicit local memory and valid feedback cycles
├── Execution model.md
│   -> execution-model core: validated executable graph, live execution instance,
│      source identity, activation, execution context, semantic milestones,
│      and committed source-level state
└── Execution control and observation boundaries.md
    -> safe observation points, pause-consistent snapshots, safe debug stops,
       and terminal control/observation boundaries
</code></pre>

<p>
This organization keeps the directory compact enough to remain readable while still giving execution semantics a complete enough normative baseline for IR construction, observability, and debugging to build on.
</p>

<pre><code>Internal semantic layering

Control structures / State and cycles
                |
                v
         Execution model
                |
                v
Execution control and observation boundaries
                |
                +--> IR construction can rely on validated meaning
                |
                v
   IDE-facing observability / debugging layers
</code></pre>

<hr/>

<h2 id="current-documents">5. Current Documents</h2>

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
Additional cross-cutting semantic specifications MAY be added here later when they belong to the execution semantics of the language itself rather than to source serialization, IR structure, intrinsic primitive catalogs, optional profile catalogs, or IDE tooling.
</p>

<pre><code>Current semantic baseline

Structures
   +
State / cycles
   +
Execution model
   +
Observation / control boundaries
   =
usable normative execution core
</code></pre>

<hr/>

<h2 id="relation-with-expression">6. Relation with Expression</h2>

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

<pre><code>Same topic, different ownership

Serialized structure shape  -> Expression/
Execution meaning           -> Language/
</code></pre>

<pre><code>Example

Expression/Control structures.md
    -> how a case / for_loop / while_loop is represented in source

Language/Control structures.md
    -> what that validated structure means when it executes
</code></pre>

<hr/>

<h2 id="relation-with-ir">7. Relation with IR</h2>

<p>
<code>Language/</code> and <code>IR/</code> are also related but distinct layers.
</p>

<ul>
  <li><code>Language/</code> defines the semantic truth of a validated FROG.</li>
  <li><code>IR/</code> defines execution-facing derived representations built from that validated meaning.</li>
</ul>

<p>
This means:
</p>

<ul>
  <li><code>Language/</code> remains authoritative when the question is semantic,</li>
  <li><code>IR/</code> becomes authoritative when the question is about execution-facing derived form, normalization shape, attribution-preserving derived structure, or later lowering attachment points.</li>
</ul>

<p>
The separation matters because the repository should not confuse:
</p>

<ul>
  <li>what a validated FROG means,</li>
  <li>how an implementation may represent that meaning for execution-facing use.</li>
</ul>

<pre><code>Language/ says:
"what is true"

IR/ says:
"how that validated truth may be represented for execution-facing use"
</code></pre>

<p>
Accordingly:
</p>

<ul>
  <li><code>Language/</code> SHOULD NOT become an IR object-model directory,</li>
  <li><code>IR/</code> MUST NOT silently redefine language meaning,</li>
  <li>IR construction SHOULD rely on language semantics rather than replace them,</li>
  <li>when tension appears between execution-facing convenience and normative semantics, <code>Language/</code> remains authoritative.</li>
</ul>

<pre><code>Validated meaning
      |
      v
 Language/
      |
      v
 execution-facing derived form
      |
      v
 IR/
</code></pre>

<hr/>

<h2 id="relation-with-libraries-profiles-and-ide">8. Relation with Libraries, Profiles, and IDE</h2>

<p>
<code>Language/</code> is also distinct from <code>Libraries/</code>, <code>Profiles/</code>, and <code>IDE/</code>.
</p>

<p>
The responsibility split is:
</p>

<ul>
  <li><code>Libraries/</code> define intrinsic primitive families, primitive names, primitive-local ports, metadata, and primitive-local behavior,</li>
  <li><code>Profiles/</code> define optional standardized capability families and profile-owned capability contracts,</li>
  <li><code>Language/</code> defines cross-cutting execution meaning that spans beyond one primitive family, one optional profile family, or one source section,</li>
  <li><code>IDE/</code> defines how execution is authored, observed, debugged, inspected, and presented to users or tools.</li>
</ul>

<p>
This means, for example:
</p>

<ul>
  <li>a primitive such as <code>frog.core.delay</code> belongs to <code>Libraries/</code> for its intrinsic primitive-local definition,</li>
  <li>a profile-owned primitive such as <code>frog.connectivity.python.call_text</code> belongs to <code>Profiles/</code> for its optional capability definition,</li>
  <li>the cross-cutting meaning of local memory and valid cycles belongs to <code>Language/</code>,</li>
  <li>the execution-facing representation of validated graph content belongs to <code>IR/</code>,</li>
  <li>the IDE-facing projection of committed observations, debug stops, probes, and watches belongs to <code>IDE/</code>.</li>
</ul>

<p>
The repository remains cleaner and more durable when these ownership boundaries stay explicit.
</p>

<pre><code>Ownership split

Primitive-local intrinsic meaning   -> Libraries/
Primitive-local optional meaning    -> Profiles/
Cross-cutting execution meaning     -> Language/
Execution-facing derived form       -> IR/
Tool-facing projection and UX       -> IDE/
</code></pre>

<pre><code>What Language/ should not become

Not:
- a source-format directory
- an IR object-model directory
- a primitive catalog directory
- a profile catalog directory
- an IDE behavior directory

But:
- the semantic layer that those other directories can rely on
</code></pre>

<hr/>

<h2 id="semantic-layering-inside-language">9. Semantic Layering inside Language</h2>

<p>
The current documents in <code>Language/</code> are not just a list.
They form a useful semantic stack.
</p>

<p>
At a high level:
</p>

<ul>
  <li><strong>Control structures</strong> and <strong>state/cycles</strong> define key semantic building blocks of validated executable graphs,</li>
  <li><strong>Execution model</strong> defines the language-level execution concepts needed to talk coherently about a running validated FROG,</li>
  <li><strong>Execution control and observation boundaries</strong> defines where observation and control remain semantically safe and source-coherent.</li>
</ul>

<p>
That stack can be visualized as follows:
</p>

<pre><code>Validated executable graph
          |
          +--> structure semantics
          |      (case / for_loop / while_loop)
          |
          +--> state / cycle semantics
                 (explicit local memory, valid feedback)
                          |
                          v
                   Execution model
      (activation, context, milestones, committed state)
                          |
                          v
      Execution control and observation boundaries
   (safe stops, consistent snapshots, terminal boundaries)
                          |
                          +--> IR construction
                          |    (execution-facing derivation built from
                          |     validated semantic meaning)
                          |
                          v
       Source-aligned observability and debugging layers
</code></pre>

<p>
This is one of the main reasons <code>Language/</code> matters:
it provides the semantic bridge between canonical source and serious execution-facing tooling without forcing that bridge to live inside the IDE layer and without forcing derived execution representation to own semantic truth.
</p>

<hr/>

<h2 id="role-in-the-repository">10. Role in the Repository</h2>

<p>
This directory provides the normative execution-semantics layer of the repository.
Its role is to keep execution meaning explicit, durable, and independent from source-serialization details, IR structure, or IDE behavior.
</p>

<p>
Its presence makes the following easier:
</p>

<ul>
  <li>clear separation between source representation and execution meaning,</li>
  <li>clear separation between semantic truth and execution-facing derived representation,</li>
  <li>stable interpretation of validated executable graphs across independent implementations,</li>
  <li>consistent reuse of language semantics by IDEs, validators, IR-producing toolchains, runtimes, and compilers,</li>
  <li>clean attachment points for observability and debugging without forcing those layers to redefine execution meaning,</li>
  <li>long-term architectural cleanup without collapsing distinct responsibilities into one layer.</li>
</ul>

<p>
In practical terms:
</p>

<ul>
  <li>read <code>Expression/</code> for canonical source structure,</li>
  <li>read <code>Language/</code> for cross-cutting execution semantics,</li>
  <li>read <code>IR/</code> for execution-facing derived representations,</li>
  <li>read <code>Libraries/</code> for intrinsic standardized primitive catalogs and primitive families,</li>
  <li>read <code>Profiles/</code> for optional standardized capability families,</li>
  <li>read <code>IDE/</code> for authoring, observability, debugging, and inspection behavior.</li>
</ul>

<pre><code>Repository reading rule

Expression/ -> how it is written
Language/   -> what it means
IR/         -> how validated meaning is derived for execution-facing use
Libraries/  -> what intrinsic primitives mean
Profiles/   -> what optional capability families mean
IDE/        -> how tools expose and manipulate it
</code></pre>

<hr/>

<h2 id="status">11. Status</h2>

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
This makes <code>Language/</code> the layer that a serious FROG IDE, validator, IR-producing toolchain, runtime, or compiler can rely on when it needs normative execution meaning without confusing that meaning with canonical source form, execution-facing derived representation, intrinsic primitive definitions, optional profile-owned capability definitions, or IDE-facing tooling behavior.
</p>

<p>
As the repository architecture continues to mature, additional cross-cutting semantic topics MAY be added here when they belong to the language execution model itself.
That growth SHOULD remain disciplined:
</p>

<ul>
  <li>do not move source-shape topics here when they belong to <code>Expression/</code>,</li>
  <li>do not move IR-shape topics here when they belong to <code>IR/</code>,</li>
  <li>do not move intrinsic primitive-catalog topics here when they belong to <code>Libraries/</code>,</li>
  <li>do not move optional capability-family definitions here when they belong to <code>Profiles/</code>,</li>
  <li>do not move tooling-UX topics here when they belong to <code>IDE/</code>,</li>
  <li>do add topics here when they define execution meaning that multiple other layers must rely on.</li>
</ul>

<p>
The long-term goal is a stable repository architecture in which <code>Expression/</code>, <code>Language/</code>, <code>IR/</code>, <code>Libraries/</code>, <code>Profiles/</code>, and <code>IDE/</code> each own a clearly separated normative responsibility.
</p>

<pre><code>Long-term discipline for Language/

Add here:
- cross-cutting execution semantics
- semantic invariants
- language-level execution concepts
- source-safe semantic boundaries

Do not add here:
- source-only shape rules
- IR object-model shape rules
- primitive catalog bulk
- profile catalog bulk
- debugger UX details
- runtime-private implementation mechanics
</code></pre>
