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
In the repository architecture, <code>Language/</code> is the normative home of <strong>validated execution meaning</strong>.
</p>

<pre><code>🟦 Expression/   -> canonical source form
🟩 Language/     -> normative validated execution meaning
🟦 IR/           -> execution-facing derived representation
🟦 Libraries/    -> intrinsic primitive vocabularies
🟦 Profiles/     -> optional standardized capability families
🟦 IDE/          -> authoring, observability, debugging, inspection

🟩 Language/ = semantic truth layer
</code></pre>

<hr/>

<h2 id="why-this-layer-exists">2. Why this Layer Exists</h2>

<p>
A language needs more than a source format.
It needs a stable place where validated program behavior is defined at the semantic level.
That is the role of <code>Language/</code>.
</p>

<pre><code>Without Language/ → semantic drift

Expression/     ❌ starts leaking execution meaning
Libraries/      ❌ starts defining global behavior
IR/             ❌ becomes semantic authority (wrong)
Runtime         ❌ becomes the "real spec"
IDE             ❌ defines behavior implicitly

With Language/ → stable architecture

🟦 Expression/   -> shape
🟩 Language/     -> meaning
🟦 IR/           -> representation of meaning
</code></pre>

<hr/>

<h2 id="scope-of-this-directory">3. Scope of this Directory</h2>

<pre><code>🟩 Language/ owns

✔ cross-cutting execution meaning
✔ validated graph interpretation
✔ structure semantics
✔ cycle / memory semantics
✔ semantic observation/control boundaries


🟥 Language/ does NOT own

✘ source serialization              -> Expression/
✘ execution-facing IR structure     -> IR/
✘ primitive catalogs                -> Libraries/
✘ optional capabilities             -> Profiles/
✘ IDE UX                            -> IDE/
✘ runtime internals                 -> implementation
</code></pre>

<hr/>

<h2 id="document-map">4. Document Map</h2>

<pre><code>Global architecture

🟦 Expression/  -> source
🟩 Language/    -> meaning
🟦 IR/          -> derived execution form
🟦 Libraries/   -> intrinsic primitives
🟦 Profiles/    -> optional capabilities
🟦 IDE/         -> tooling
</code></pre>

<pre><code>Internal structure

Language/
├── Readme.md
├── Control structures.md
├── State and cycles.md
├── Execution model.md
└── Execution control and observation boundaries.md
</code></pre>

<pre><code>🟩 Semantic layering

Structures + State
        ↓
Execution model
        ↓
Observation / Control boundaries
        ↓
🟦 IR construction
        ↓
🟦 IDE observability / debugging
</code></pre>

<hr/>

<h2 id="relation-with-expression">6. Relation with Expression</h2>

<pre><code>Same concept — different ownership

🟦 Expression/   -> "how it is written"
🟩 Language/     -> "what it means"
</code></pre>

<pre><code>Example

Expression/Control structures.md
    -> representation

Language/Control structures.md
    -> execution meaning
</code></pre>

<hr/>

<h2 id="relation-with-ir">7. Relation with IR</h2>

<pre><code>🟩 Language/ = semantic truth
        ↓
🟦 IR/ = execution-facing representation
</code></pre>

<pre><code>Invariant

✔ IR derives from Language
✘ IR MUST NOT redefine semantics
✔ Language remains authoritative
</code></pre>

<pre><code>Flow

Validated program
        ↓
🟩 Language/
        ↓
🟦 IR/
        ↓
🟧 Lowering / backend
        ↓
🟥 Runtime
</code></pre>

<hr/>

<h2 id="relation-with-libraries-profiles-and-ide">8. Relation with Libraries, Profiles, and IDE</h2>

<pre><code>Ownership split

🟦 Libraries/   -> intrinsic primitive-local meaning
🟦 Profiles/    -> optional capability meaning
🟩 Language/    -> cross-cutting execution meaning
🟦 IR/          -> derived execution form
🟦 IDE/         -> user-facing tooling
</code></pre>

<pre><code>Example

frog.core.delay              -> Libraries/
frog.connectivity.*          -> Profiles/
cycle validity               -> Language/
execution graph structure    -> IR/
debugging UX                 -> IDE/
</code></pre>

<hr/>

<h2 id="semantic-layering-inside-language">9. Semantic Layering inside Language</h2>

<pre><code>🟩 VALIDATED EXECUTABLE GRAPH

    ├── Structures
    │     case / for_loop / while_loop
    │
    ├── State & Cycles
    │     explicit memory / feedback validity
    │
    ↓

🟩 Execution Model
    activation / context / milestones / committed state

    ↓

🟩 Observation & Control Boundaries
    safe stop / snapshot / completion / fault

    ↓
    ├── 🟦 IR construction
    └── 🟦 IDE observability / debugging
</code></pre>

<hr/>

<h2 id="role-in-the-repository">10. Role in the Repository</h2>

<pre><code>Reading rule

🟦 Expression/ -> how it is written
🟩 Language/   -> what it means
🟦 IR/         -> how meaning is represented for execution
🟦 Libraries/  -> primitive meaning
🟦 Profiles/   -> optional capability meaning
🟦 IDE/        -> how it is used
</code></pre>

<hr/>

<h2 id="status">11. Status</h2>

<pre><code>🟩 Current semantic baseline

✔ control structures
✔ state / cycles
✔ execution model
✔ observation boundaries
</code></pre>

<pre><code>🟨 Discipline

Add:
✔ cross-cutting semantics
✔ invariants
✔ execution concepts

Do NOT add:
✘ IR structure
✘ source shape
✘ primitive catalogs
✘ IDE UX
✘ runtime internals
</code></pre>

<pre><code>Target architecture

🟦 Expression/
🟩 Language/
🟦 IR/
🟦 Libraries/
🟦 Profiles/
🟦 IDE/

→ clean ownership
→ no overlap
→ industrial-grade spec
</code></pre>
