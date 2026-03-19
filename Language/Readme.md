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
This directory defines cross-cutting normative execution semantics for FROG.
It specifies what a validated FROG program means when that meaning cannot be owned by one isolated source-section document, one intrinsic primitive-library document, one optional profile specification, or one execution-facing derived-representation document alone.
</p>

<p>
In the repository architecture, <code>Language/</code> is the normative home of <strong>validated program meaning</strong>.
It is the semantic truth layer that sits between canonical source representation and open execution-facing IR.
</p>

<pre><code>Expression/   -> canonical source form
Language/     -> validated program meaning
IR/           -> open execution-facing representation
Libraries/    -> intrinsic primitive vocabularies
Profiles/     -> optional standardized capability families
IDE/          -> authoring, observability, debugging, inspection

Language/ = semantic truth layer
</code></pre>

<p>
This layer does not replace source representation, primitive definitions, profile-owned capability behavior, IR construction rules, or IDE behavior.
Its role is narrower and more important:
to define the normative semantic meaning of a validated program in a stable, implementation-independent way.
</p>

<hr/>

<h2 id="why-this-layer-exists">2. Why this Layer Exists</h2>

<p>
A language needs more than a source format.
It needs a stable place where validated program behavior is defined at the semantic level.
That is the role of <code>Language/</code>.
</p>

<p>
Without a dedicated semantic layer, architectural drift appears quickly:
</p>

<pre><code>Without Language/ -> semantic drift

Expression/     starts leaking execution meaning
Libraries/      starts defining global behavior
Profiles/       starts redefining core semantics
IR/             becomes semantic authority
Runtime         becomes the "real spec"
IDE/            defines behavior implicitly
</code></pre>

<p>
The purpose of <code>Language/</code> is to stop that drift by giving validated program meaning a stable normative home.
</p>

<pre><code>With Language/ -> stable architecture

Expression/   -> how the program is written
Language/     -> what the validated program means
IR/           -> what execution-facing representation may be built
                 from that validated meaning
</code></pre>

<p>
This separation matters for durability, interoperability, conformance, and future independent implementations.
A FROG implementation MAY differ in runtime strategy, compilation strategy, lowering strategy, or tooling model, but it MUST NOT redefine validated program meaning.
</p>

<hr/>

<h2 id="scope-of-this-directory">3. Scope of this Directory</h2>

<p>
This directory owns cross-cutting semantic meaning that applies once a program has been validated against the relevant source, language, library, and profile rules.
</p>

<pre><code>Language/ owns

- cross-cutting execution meaning
- validated graph interpretation
- control-structure semantics
- local-memory and cycle semantics
- semantic execution concepts
- semantic observation and control boundaries
</code></pre>

<p>
This directory does not own the concerns below:
</p>

<pre><code>Language/ does NOT own

- source serialization and source-section structure    -> Expression/
- execution-facing IR structure                        -> IR/
- primitive catalogs and primitive identities          -> Libraries/
- optional capability families                         -> Profiles/
- IDE UX and editor workflows                          -> IDE/
- runtime-private internals                            -> implementation
</code></pre>

<p>
Accordingly, this directory MUST remain focused on semantic truth.
It MUST NOT become a second source-format directory, a second IR directory, a primitive catalog, an IDE design space, or a runtime implementation note collection.
</p>

<hr/>

<h2 id="document-map">4. Document Map</h2>

<p>
The surrounding repository architecture is:
</p>

<pre><code>Expression/  -> source
Language/    -> meaning
IR/          -> derived execution-facing representation
Libraries/   -> intrinsic primitives
Profiles/    -> optional capabilities
IDE/         -> tooling
</code></pre>

<p>
The internal structure of <code>Language/</code> is currently:
</p>

<pre><code>Language/
├── Readme.md
├── Control structures.md
├── State and cycles.md
├── Execution model.md
└── Execution control and observation boundaries.md
</code></pre>

<p>
The semantic flow inside this layer is:
</p>

<pre><code>Control structures + State and cycles
                  ->
            Execution model
                  ->
Execution control and observation boundaries
                  ->
      IR derivation / IR construction
                  ->
    IDE observability / debugging
</code></pre>

<p>
This is semantic layering, not a compiler pipeline.
The documents in this directory define meaning and boundaries that later layers depend on.
They do not define one mandatory implementation pipeline.
</p>

<hr/>

<h2 id="current-documents">5. Current Documents</h2>

<p>
The documents currently published in this directory are:
</p>

<ul>
  <li><strong><code>Readme.md</code></strong> — architectural entry point for the semantic layer and its ownership boundary.</li>
  <li><strong><code>Control structures.md</code></strong> — normative meaning of canonical control structures such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>.</li>
  <li><strong><code>State and cycles.md</code></strong> — normative meaning of explicit local memory and valid feedback cycles.</li>
  <li><strong><code>Execution model.md</code></strong> — language-level execution-model core, including validated program meaning, activation, execution context, semantic milestones, and committed source-level state.</li>
  <li><strong><code>Execution control and observation boundaries.md</code></strong> — safe semantic observation points, pause-consistent snapshots, safe stop boundaries, and minimal completion / fault / abort boundaries.</li>
</ul>

<p>
Together, these documents define the current cross-cutting semantic baseline of the FROG language.
They do not replace primitive-local behavior owned by <code>Libraries/</code> or optional capability behavior owned by <code>Profiles/</code>.
</p>

<hr/>

<h2 id="relation-with-expression">6. Relation with Expression</h2>

<p>
<code>Expression/</code> and <code>Language/</code> are directly related but they do not own the same thing.
</p>

<pre><code>Same program — different ownership

Expression/   -> how the program is written
Language/     -> what the validated program means
</code></pre>

<p>
For example:
</p>

<pre><code>Expression/Control structures.md
    -> source-facing representation

Language/Control structures.md
    -> normative execution semantics
</code></pre>

<p>
That distinction is fundamental.
Expression documents define canonical source shape and source-visible structure.
Language documents define validated semantic meaning.
Expression MUST NOT become the semantic authority for execution behavior, and Language MUST NOT redefine canonical source serialization.
</p>

<hr/>

<h2 id="relation-with-ir">7. Relation with IR</h2>

<p>
<code>Language/</code> and <code>IR/</code> are also directly related but they are not interchangeable.
</p>

<pre><code>Language/ = semantic truth
        ↓
IR/      = open execution-facing representation
</code></pre>

<p>
The invariant is:
</p>

<pre><code>- IR derives from validated program meaning
- IR MUST NOT redefine semantics
- Language remains authoritative for semantic meaning
</code></pre>

<p>
The architectural flow is:
</p>

<pre><code>validated program meaning
        ↓
Language/
        ↓
IR/
        ↓
lowering / backend handoff
        ↓
runtime-private realization
</code></pre>

<p>
This means that <code>Language/</code> defines what is true,
while <code>IR/</code> defines what execution-facing representation may be built from that truth.
The semantic layer is therefore upstream of IR derivation and construction, even though IR documents may restate semantic dependencies for clarity.
</p>

<hr/>

<h2 id="relation-with-libraries-profiles-and-ide">8. Relation with Libraries, Profiles, and IDE</h2>

<p>
FROG deliberately separates cross-cutting semantics from primitive-local behavior, optional capability behavior, and tooling behavior.
</p>

<pre><code>Libraries/   -> intrinsic primitive-local meaning
Profiles/    -> optional capability meaning
Language/    -> cross-cutting validated program meaning
IR/          -> derived execution-facing representation
IDE/         -> user-facing tooling
</code></pre>

<p>
Examples:
</p>

<pre><code>frog.core.delay              -> Libraries/
frog.connectivity.*          -> Profiles/
cycle validity               -> Language/
execution-facing IR shape    -> IR/
debugging UX                 -> IDE/
</code></pre>

<p>
This separation prevents several common specification failures:
</p>

<ul>
  <li>primitive catalogs silently redefining global execution behavior,</li>
  <li>profile documents redefining the language core,</li>
  <li>IR documents becoming the semantic source of truth,</li>
  <li>IDE behavior being mistaken for language semantics.</li>
</ul>

<p>
Cross-cutting semantic rules belong here whenever they cannot be cleanly owned elsewhere.
</p>

<hr/>

<h2 id="semantic-layering-inside-language">9. Semantic Layering inside Language</h2>

<p>
The internal semantic layering of this directory can be summarized as follows:
</p>

<pre><code>VALIDATED PROGRAM MEANING

    ├── Control structures
    │     case / for_loop / while_loop
    │
    ├── State and cycles
    │     explicit local memory / feedback validity
    │
    ↓

Execution model
    activation / context / milestones / committed state

    ↓

Execution control and observation boundaries
    safe stop / snapshot / completion / fault / abort

    ↓
    ├── IR derivation and construction
    └── IDE observability and debugging
</code></pre>

<p>
This ordering is intentional.
Structure semantics and state semantics define core semantic validity.
The execution model defines language-level execution concepts.
Observation and control boundaries then define where implementations may safely observe, pause, snapshot, or surface execution in a source-aligned way.
</p>

<hr/>

<h2 id="role-in-the-repository">10. Role in the Repository</h2>

<p>
The simplest reading rule for the repository is:
</p>

<pre><code>Expression/ -> how it is written
Language/   -> what it means
IR/         -> what execution-facing representation may be derived
Libraries/  -> what intrinsic primitives exist and how they behave locally
Profiles/   -> what optional capabilities exist and how they behave
IDE/        -> how programs are authored, observed, and debugged
</code></pre>

<p>
Within that architecture, <code>Language/</code> has a narrow but central role.
It is the normative semantic bridge between canonical source and execution-facing derivation.
</p>

<p>
If this layer remains clean, later layers can evolve without semantic drift.
If this layer becomes blurred, the entire repository becomes harder to stabilize.
</p>

<hr/>

<h2 id="status">11. Status</h2>

<p>
The current semantic baseline of <code>Language/</code> already covers:
</p>

<ul>
  <li>control structures,</li>
  <li>state and cycles,</li>
  <li>execution-model concepts,</li>
  <li>execution control and observation boundaries.</li>
</ul>

<p>
The discipline for future additions is:
</p>

<pre><code>Add here:
- cross-cutting semantics
- semantic invariants
- execution concepts
- language-level boundaries

Do NOT add here:
- IR structure
- source shape
- primitive catalogs
- IDE UX
- runtime internals
</code></pre>

<p>
The target architecture remains:
</p>

<pre><code>Expression/
Language/
IR/
Libraries/
Profiles/
IDE/

-> clean ownership
-> no semantic overlap
-> durable industrial-grade specification layering
</code></pre>

<p>
This directory is therefore not a temporary holding area.
It is the long-term semantic authority for validated program meaning in the FROG specification.
</p>
