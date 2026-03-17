<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG Intermediate Representation Architecture</h1>

<p align="center">
  Architectural definition of the <strong>IR</strong> layer for FROG v0.1<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-layer-exists">2. Why this layer exists</a></li>
  <li><a href="#layer-boundary-snapshot">3. Layer boundary snapshot</a></li>
  <li><a href="#architectural-role">4. Architectural role</a></li>
  <li><a href="#position-in-the-representation-pipeline">5. Position in the representation pipeline</a></li>
  <li><a href="#scope-of-this-directory">6. Scope of this directory</a></li>
  <li><a href="#what-this-directory-does-not-own">7. What this directory does not own</a></li>
  <li><a href="#relation-with-expression">8. Relation with Expression</a></li>
  <li><a href="#relation-with-language">9. Relation with Language</a></li>
  <li><a href="#relation-with-libraries-and-profiles">10. Relation with Libraries and Profiles</a></li>
  <li><a href="#relation-with-the-ide-program-model">11. Relation with the IDE Program Model</a></li>
  <li><a href="#relation-with-cache-artifacts">12. Relation with cache artifacts</a></li>
  <li><a href="#relation-with-lowering-compilation-and-runtime">13. Relation with lowering, compilation, and runtime</a></li>
  <li><a href="#ownership-quick-check">14. Ownership quick check</a></li>
  <li><a href="#local-document-map">15. Local document map</a></li>
  <li><a href="#reading-relationships">16. Reading relationships</a></li>
  <li><a href="#status-in-v01">17. Status in v0.1</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the architectural home of <strong>execution-facing derived representations</strong> in the FROG specification.
</p>

<p>
A FROG program is not authored directly as an execution IR. It is authored as canonical source, interpreted through language semantics, and then <strong>MAY</strong> be transformed into one or more execution-oriented intermediate forms suitable for validation pipelines, analysis, execution preparation, optimization, lowering, compilation, or backend mapping.
</p>

<p>
The purpose of <code>IR/</code> is to prevent those execution-facing derived forms from being scattered across:
</p>

<ul>
  <li>source-format documents,</li>
  <li>IDE-internal documents,</li>
  <li>library catalogs,</li>
  <li>profile documents,</li>
  <li>runtime-specific implementation notes.</li>
</ul>

<p>
This directory therefore exists to provide a durable normative place for open, inspectable, specification-facing intermediate representations that are <strong>derived from validated FROG program meaning</strong> but are <strong>not</strong> themselves the canonical source artifact.
</p>

<hr/>

<h2 id="why-this-layer-exists">2. Why this layer exists</h2>

<p>
FROG deliberately separates multiple architectural levels:
</p>

<ul>
  <li>the canonical saved source artifact,</li>
  <li>the IDE's editable in-memory model,</li>
  <li>the validated execution meaning of the program,</li>
  <li>the derived forms used to prepare or realize execution.</li>
</ul>

<p>
Without a dedicated IR layer, execution-oriented representation risks being redefined inconsistently by:
</p>

<ul>
  <li>IDE implementation details,</li>
  <li>cache examples,</li>
  <li>runtime-internal scheduler structures,</li>
  <li>compiler-specific lowering pipelines,</li>
  <li>backend-specific transport or deployment formats.</li>
</ul>

<p>
The IR layer exists to prevent that drift.
</p>

<p>
In simple terms:
</p>

<pre>
Expression/ says:
"what is saved"

IDE/ says:
"what is edited"

Language/ says:
"what the validated program means"

IR/ says:
"what execution-facing derived form may be built from that meaning"
</pre>

<hr/>

<h2 id="layer-boundary-snapshot">3. Layer boundary snapshot</h2>

<p>
The shortest correct mental model of the surrounding architecture is:
</p>

<pre>
+-------------------+----------------------------------------------+
| Layer             | Primary question answered                    |
+-------------------+----------------------------------------------+
| Expression/       | What is the canonical saved source?          |
| Language/         | What does the validated program mean?        |
| Libraries/        | What intrinsic primitives exist?             |
| Profiles/         | What optional standardized capabilities      |
|                   | exist beyond the intrinsic core?             |
| IDE/              | How is the program authored, inspected,      |
|                   | debugged, and presented in tools?            |
| IR/               | What execution-facing derived representation |
|                   | may be built from validated program meaning? |
+-------------------+----------------------------------------------+
</pre>

<p>
This README exists primarily to keep that last boundary explicit and durable.
</p>

<hr/>

<h2 id="architectural-role">4. Architectural role</h2>

<p>
The <code>IR/</code> layer occupies a distinct architectural role between:
</p>

<ul>
  <li>the normative meaning of a validated FROG program, and</li>
  <li>the implementation-specific mechanisms used by compilers, runtimes, or execution backends.</li>
</ul>

<p>
This means:
</p>

<ul>
  <li><code>IR/</code> <strong>MUST NOT</strong> redefine canonical source structure,</li>
  <li><code>IR/</code> <strong>MUST NOT</strong> redefine language meaning,</li>
  <li><code>IR/</code> <strong>MUST NOT</strong> become a dumping ground for private runtime internals,</li>
  <li><code>IR/</code> <strong>SHOULD</strong> define execution-facing derived forms that remain inspectable, portable, and specification-friendly,</li>
  <li><code>IR/</code> <strong>MAY</strong> provide stable contracts that later lowering and backend-mapping stages can consume.</li>
</ul>

<p>
This layer is therefore about <strong>derived execution representation</strong>, not about replacing the language core and not about standardizing every private implementation detail of one compiler or runtime.
</p>

<p>
The intended ownership boundary can be summarized like this:
</p>

<pre>
validated meaning
      |
      |  semantic truth remains in Language/
      v
open execution-facing derived form
      |
      |  ownership begins here
      v
IR/
      |
      |  target specialization begins later
      v
lowering / backend mapping / runtime realization
</pre>

<hr/>

<h2 id="position-in-the-representation-pipeline">5. Position in the representation pipeline</h2>

<p>
The intended position of the IR layer is illustrated below:
</p>

<pre>
Authoring side
--------------
IDE Program Model
        |
        v
canonical .frog source
        |
        v
Expression/

Meaning side
------------
validated program meaning
        |
        +--> Language/
        +--> Libraries/
        +--> Profiles/

Execution-preparation side
--------------------------
derived execution-facing representation
        |
        v
IR/

Implementation side
-------------------
lowering
compilation
runtime mapping
backend-specific forms
</pre>

<p>
The transition into <code>IR/</code> begins <strong>after</strong> the program has a validated meaning.
</p>

<p>
An implementation <strong>MAY</strong> derive IR directly from canonical source, from a validated Program Model, or from another equivalent validated internal form, but the resulting IR <strong>MUST</strong> remain semantically grounded in the validated FROG program rather than in editor-only convenience state.
</p>

<p>
A second useful sketch is:
</p>

<pre>
.frog source
    |
    v
Program Model or equivalent validated tool form
    |
    v
validated executable content
    |
    v
Execution IR
    |
    v
lowered / backend-facing forms
</pre>

<hr/>

<h2 id="scope-of-this-directory">6. Scope of this directory</h2>

<p>
This directory is the normative home for questions such as:
</p>

<ul>
  <li>What execution-facing derived representations are standardized by FROG?</li>
  <li>What is the architectural boundary between validated program meaning and execution IR?</li>
  <li>Which execution-facing properties are preserved from validated program meaning into IR?</li>
  <li>Which properties may be normalized, expanded, or made more explicit in IR?</li>
  <li>How can later lowering or backend mapping consume an open IR without treating one private runtime structure as the language standard?</li>
</ul>

<p>
This directory <strong>MAY</strong> eventually define topics such as:
</p>

<ul>
  <li>an open execution IR object model,</li>
  <li>identity and mapping rules between source-level constructs and IR objects,</li>
  <li>normalization rules applied during IR construction,</li>
  <li>lowering boundaries,</li>
  <li>compiler/backend consumption contracts.</li>
</ul>

<p>
At a minimum, this directory establishes the architectural ownership of those concerns.
</p>

<hr/>

<h2 id="what-this-directory-does-not-own">7. What this directory does not own</h2>

<p>
This directory does not define:
</p>

<ul>
  <li>the canonical <code>.frog</code> source structure in full,</li>
  <li>the public interface format in full,</li>
  <li>the front-panel source model in full,</li>
  <li>the complete widget model in full,</li>
  <li>the normative execution semantics of the language in full,</li>
  <li>the intrinsic primitive catalogs in full,</li>
  <li>the optional standardized profile catalogs in full,</li>
  <li>the IDE's Program Model,</li>
  <li>a private runtime scheduler architecture,</li>
  <li>a vendor-specific compiled artifact format,</li>
  <li>a backend-private transport representation.</li>
</ul>

<p>
In particular:
</p>

<ul>
  <li><code>Expression/</code> owns canonical source representation,</li>
  <li><code>Language/</code> owns normative meaning of validated execution,</li>
  <li><code>Libraries/</code> owns intrinsic primitive vocabularies and primitive-local behavior,</li>
  <li><code>Profiles/</code> owns optional standardized capability families,</li>
  <li><code>IDE/</code> owns authoring-facing editable models and tooling concerns.</li>
</ul>

<p>
The IR layer <strong>MUST NOT</strong> absorb those ownerships.
</p>

<p>
If a question sounds like one of the following, it probably does <strong>not</strong> belong here:
</p>

<pre>
"What does a valid .frog file look like?"       -> Expression/
"What does this construct mean?"                -> Language/
"What primitive exists and what are its ports?" -> Libraries/
"What optional capability family defines this?" -> Profiles/
"How does the IDE edit or present this?"        -> IDE/
</pre>

<hr/>

<h2 id="relation-with-expression">8. Relation with Expression</h2>

<p>
<code>Expression/</code> defines the canonical serialized source artifact of a FROG program.
</p>

<p>
The source file remains the durable, authoritative saved representation of the program. An execution IR is a <strong>derived form</strong>, not the canonical source.
</p>

<p>
Therefore:
</p>

<ul>
  <li>canonical source identity <strong>MUST</strong> remain owned by <code>Expression/</code>,</li>
  <li>the existence of an execution IR <strong>MUST NOT</strong> redefine what a valid <code>.frog</code> file is,</li>
  <li>the absence of an embedded or sidecar IR artifact <strong>MUST NOT</strong> invalidate canonical source,</li>
  <li>IR construction <strong>MAY</strong> depend on validated content originating from source sections such as interface, diagram, front panel, metadata, or other source-owned elements when relevant.</li>
</ul>

<p>
In simple terms:
</p>

<pre>
.frog source
   is not
execution IR

execution IR
   is derived from
validated source meaning
</pre>

<p>
A useful ownership sketch is:
</p>

<pre>
Expression/
   owns:
   - canonical source structure
   - source serialization
   - source-visible object presence

IR/
   owns:
   - execution-facing derived form
   - execution-oriented normalization
   - source-attributed execution representation
</pre>

<hr/>

<h2 id="relation-with-language">9. Relation with Language</h2>

<p>
<code>Language/</code> defines what a validated FROG program means when it executes.
</p>

<p>
That semantic layer remains normative even when an implementation uses one or more execution IRs internally or through standardized open forms.
</p>

<p>
Accordingly:
</p>

<ul>
  <li><code>Language/</code> defines semantic truth,</li>
  <li><code>IR/</code> defines execution-facing derived representation,</li>
  <li><code>IR/</code> <strong>MUST NOT</strong> silently change language meaning,</li>
  <li><code>IR/</code> <strong>MAY</strong> make semantic consequences more explicit where execution preparation requires it,</li>
  <li>when a tension appears between an IR convenience and normative language semantics, <code>Language/</code> remains authoritative.</li>
</ul>

<p>
This directory therefore depends on <code>Language/</code> semantically, but does not replace it.
</p>

<p>
The shortest correct relation is:
</p>

<pre>
Language/ answers:
"What is true?"

IR/ answers:
"How may that validated truth be represented for execution-facing use?"
</pre>

<hr/>

<h2 id="relation-with-libraries-and-profiles">10. Relation with Libraries and Profiles</h2>

<p>
IR is not a replacement for primitive-library or profile definitions.
</p>

<p>
When an IR refers to executable operations, it <strong>SHOULD</strong> preserve or reference the primitive and capability identities defined elsewhere rather than redefining them privately.
</p>

<p>
Therefore:
</p>

<ul>
  <li><code>Libraries/</code> continues to own intrinsic primitive namespaces, ports, and primitive-local behavior,</li>
  <li><code>Profiles/</code> continues to own optional standardized capability families,</li>
  <li><code>IR/</code> <strong>MAY</strong> carry normalized references to those operations for execution-facing purposes,</li>
  <li><code>IR/</code> <strong>MUST NOT</strong> redefine a primitive catalog or capability-family catalog as if that catalog belonged here.</li>
</ul>

<p>
A compact sketch:
</p>

<pre>
Libraries/ and Profiles/
      provide operation identities
                 |
                 v
IR/
      may reference them
      may normalize their execution-facing use
      must not re-own them
</pre>

<hr/>

<h2 id="relation-with-the-ide-program-model">11. Relation with the IDE Program Model</h2>

<p>
The IDE Program Model is the authoritative editable in-memory representation during authoring.
</p>

<p>
The execution IR is not the Program Model.
</p>

<p>
These layers are related but distinct:
</p>

<pre>
Expression   -> what is saved
Program Model-> what is edited
Execution IR -> what is prepared for execution
</pre>

<p>
The Program Model <strong>MAY</strong> preserve editor-side state that is useful for round-trip authoring. The execution IR <strong>SHOULD NOT</strong> depend on editor-only presentation state as if that state were part of normative program meaning.
</p>

<p>
An IDE <strong>MAY</strong> construct, inspect, cache, compare, or visualize execution IR, but such capabilities do not transfer ownership of IR architecture to the IDE layer.
</p>

<p>
A useful distinction is:
</p>

<pre>
IDE concern
-----------
editable convenience
guided authoring
round-trip preservation
authoring-side state

IR concern
----------
execution-facing structure
source attribution
normalization for execution preparation
input to later lowering stages
</pre>

<hr/>

<h2 id="relation-with-cache-artifacts">12. Relation with cache artifacts</h2>

<p>
A FROG source or toolchain <strong>MAY</strong> embed or associate cache artifacts that store derived execution-facing data such as <code>frog.ir</code>.
</p>

<p>
However, the cache container does not own the semantic definition of IR. It merely provides a transport or storage location for derived artifacts.
</p>

<p>
Therefore:
</p>

<ul>
  <li>cache entries such as <code>frog.ir</code> <strong>MAY</strong> carry execution-oriented derived data,</li>
  <li>cache presence <strong>MUST NOT</strong> change canonical source meaning,</li>
  <li>cache metadata such as generator information <strong>MUST NOT</strong> affect execution semantics,</li>
  <li>the normative architectural meaning of execution IR belongs in <code>IR/</code>, not in cache examples,</li>
  <li>tools <strong>MAY</strong> define additional non-standard cache entries without redefining the FROG IR layer itself.</li>
</ul>

<p>
That relationship can be pictured like this:
</p>

<pre>
IR meaning
   lives in
IR/

serialized derived artifact
   may live in
cache entry: frog.ir

cache container
   is not
IR ownership
</pre>

<hr/>

<h2 id="relation-with-lowering-compilation-and-runtime">13. Relation with lowering, compilation, and runtime</h2>

<p>
This directory sits before implementation-specific execution realization.
</p>

<p>
In broad terms:
</p>

<pre>
validated meaning
      ->
open execution IR
      ->
lowering
      ->
compiler/backend/runtime-specific realization
</pre>

<p>
This means:
</p>

<ul>
  <li><code>IR/</code> <strong>MAY</strong> provide standardized open forms that later lowering stages consume,</li>
  <li>lowering <strong>MAY</strong> specialize or transform IR for target-specific needs,</li>
  <li>runtime-private scheduler graphs, compiled objects, deployment bundles, and backend-private executable forms <strong>SHOULD</strong> remain outside the ownership of this directory unless later standardized explicitly,</li>
  <li>the existence of an open FROG IR <strong>DOES NOT</strong> require every conforming implementation to expose every private internal execution form.</li>
</ul>

<p>
This separation keeps the repository open to:
</p>

<ul>
  <li>interpreted implementations,</li>
  <li>compiled implementations,</li>
  <li>hybrid implementations,</li>
  <li>specialized runtimes,</li>
  <li>future conformance targets.</li>
</ul>

<p>
A useful non-confusion sketch is:
</p>

<pre>
open IR
   != private scheduler graph

open IR
   != compiled artifact

open IR
   != runtime trace

open IR
   = standardized execution-facing derived representation
</pre>

<hr/>

<h2 id="ownership-quick-check">14. Ownership quick check</h2>

<p>
When writing or reviewing documents in this layer, the following quick check SHOULD help avoid ownership drift:
</p>

<pre>
Does this define canonical source syntax or section structure?
-> move to Expression/

Does this define what validated behavior means?
-> move to Language/

Does this define intrinsic primitive identity or primitive-local behavior?
-> move to Libraries/

Does this define an optional standardized capability family?
-> move to Profiles/

Does this define authoring UX, editing behavior, debugging UX, or IDE model behavior?
-> move to IDE/

Does this define an execution-facing derived representation built from validated meaning?
-> it likely belongs in IR/
</pre>

<hr/>

<h2 id="local-document-map">15. Local document map</h2>

<p>
The directory is expected to grow over time.
</p>

<p>
A likely structure for the early IR layer is:
</p>

<pre>
IR/
├─ Readme.md                    Architectural role of the IR layer
├─ Execution IR.md              Open execution-facing IR model
├─ Identity and Mapping.md      Source / semantic / IR identity relations
├─ Lowering.md                  Standardized lowering boundaries
└─ Backend contract.md          Consumption contract for later stages
</pre>

<p>
This tree is partly indicative and partly directional:
</p>

<ul>
  <li><code>Readme.md</code> defines the layer boundary,</li>
  <li><code>Execution IR.md</code> defines the first concrete execution-facing IR document,</li>
  <li>the remaining documents describe likely next closures of the layer, but are not automatically frozen by being listed here.</li>
</ul>

<hr/>

<h2 id="reading-relationships">16. Reading relationships</h2>

<p>
This README should not be read in isolation.
</p>

<p>
A practical reading path is:
</p>

<pre>
root Readme.md
      ->
IR/Readme.md
      ->
IR/Execution IR.md
      ->
Expression/Readme.md
      ->
Language/Readme.md
      ->
IDE/Readme.md
      ->
Expression/Cache.md
</pre>

<p>
That reading path is useful because:
</p>

<ul>
  <li>the root README explains repository-wide architecture,</li>
  <li>this file defines the ownership boundary of the IR layer,</li>
  <li><code>Execution IR.md</code> defines the first concrete execution-facing representation,</li>
  <li><code>Expression/</code> defines canonical source,</li>
  <li><code>Language/</code> defines semantic truth,</li>
  <li><code>IDE/</code> defines the Program Model and authoring responsibilities,</li>
  <li><code>Expression/Cache.md</code> explains how derived IR artifacts may be stored without becoming the canonical source of truth.</li>
</ul>

<hr/>

<h2 id="status-in-v01">17. Status in v0.1</h2>

<p>
In repository state v0.1, this document establishes the <strong>architectural ownership</strong> of the IR layer.
</p>

<p>
It does <strong>not yet</strong> fully freeze:
</p>

<ul>
  <li>one complete execution IR object schema for every implementation,</li>
  <li>one complete normalization pipeline,</li>
  <li>one complete lowering model,</li>
  <li>one complete backend contract,</li>
  <li>one mandatory runtime-private execution structure.</li>
</ul>

<p>
Those topics <strong>MAY</strong> be added as separate documents over time.
</p>

<p>
For now, the key rule is simple:
</p>

<pre>
IR is a derived execution-facing layer.
It is not the source.
It is not the Program Model.
It is not the full language semantics.
It is not one private runtime's internal graph.
</pre>

<p>
That boundary is the purpose of this directory.
</p>
