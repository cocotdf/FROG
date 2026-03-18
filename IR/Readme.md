<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Intermediate Representation Architecture</h1>

<p align="center">
  Architectural definition of the <strong>IR</strong> layer for FROG v0.1<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#reading-legend">2. Reading legend</a></li>
  <li><a href="#why-this-layer-exists">3. Why this layer exists</a></li>
  <li><a href="#layer-boundary-snapshot">4. Layer boundary snapshot</a></li>
  <li><a href="#architectural-role">5. Architectural role</a></li>
  <li><a href="#position-in-the-representation-pipeline">6. Position in the representation pipeline</a></li>
  <li><a href="#scope-of-this-directory">7. Scope of this directory</a></li>
  <li><a href="#what-this-directory-does-not-own">8. What this directory does not own</a></li>
  <li><a href="#relation-with-expression">9. Relation with Expression</a></li>
  <li><a href="#relation-with-language">10. Relation with Language</a></li>
  <li><a href="#relation-with-libraries-and-profiles">11. Relation with Libraries and Profiles</a></li>
  <li><a href="#relation-with-the-ide-program-model">12. Relation with the IDE Program Model</a></li>
  <li><a href="#relation-with-cache-artifacts">13. Relation with cache artifacts</a></li>
  <li><a href="#relation-with-lowering-compilation-and-runtime">14. Relation with lowering, compilation, and runtime</a></li>
  <li><a href="#relation-with-observation-debugging-and-diagnostics">15. Relation with observation, debugging, and diagnostics</a></li>
  <li><a href="#ownership-quick-check">16. Ownership quick check</a></li>
  <li><a href="#local-document-map">17. Local document map</a></li>
  <li><a href="#reading-relationships">18. Reading relationships</a></li>
  <li><a href="#status-in-v01">19. Status in v0.1</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the architectural home of <strong>execution-facing derived representations</strong> in the FROG specification.
</p>

<p>
A FROG program is not authored directly as an execution IR.
It is authored as canonical source, validated against language rules, and then <strong>MAY</strong> be transformed into one or more execution-oriented intermediate forms suitable for execution preparation, inspection, normalization, attribution, and later specialization.
</p>

<p>
The purpose of <code>IR/</code> is to prevent execution-facing representation from being scattered across:
</p>

<ul>
  <li>source-format documents,</li>
  <li>IDE-internal authoring documents,</li>
  <li>cache payload examples,</li>
  <li>library or profile catalogs,</li>
  <li>runtime-private implementation notes,</li>
  <li>backend-specific realization documents.</li>
</ul>

<p>
This directory therefore provides the durable normative home for open, inspectable, specification-facing intermediate representations and adjacent handoff boundaries that are:
</p>

<ul>
  <li>derived from validated FROG program meaning,</li>
  <li>execution-facing rather than source-canonical,</li>
  <li>architecturally upstream of runtime-private realization,</li>
  <li>still source-attributable and specification-friendly.</li>
</ul>

<pre><code>🟦 canonical source
      -&gt;
🟩 validated meaning
      -&gt;
🟦 open execution-facing IR
      -&gt;
🟧 later specialization / lowering
      -&gt;
🟥 private realization
</code></pre>

<p>
The core of this layer is the open Execution IR and its derivation and construction rules.
The directory also contains downstream-adjacent documents that define how open IR connects to later stages without collapsing open IR into runtime-private form.
</p>

<hr/>

<h2 id="reading-legend">2. Reading legend</h2>

<p>
The diagrams in this README use the following visual legend:
</p>

<ul>
  <li>🟦 <strong>Open specification-facing layer or document</strong></li>
  <li>🟨 <strong>Standardized boundary, mapping, or handoff</strong></li>
  <li>🟧 <strong>Lowering or target-specialization zone</strong></li>
  <li>🟥 <strong>Implementation-private realization zone</strong></li>
  <li>🟩 <strong>Semantic truth, attribution, or diagnostic obligation</strong></li>
</ul>

<hr/>

<h2 id="why-this-layer-exists">3. Why this layer exists</h2>

<p>
FROG deliberately separates several architectural levels that are often confused in graphical systems:
</p>

<ul>
  <li>the canonical saved source artifact,</li>
  <li>the IDE's editable in-memory model,</li>
  <li>the validated execution meaning of the program,</li>
  <li>the derived forms used to prepare execution,</li>
  <li>the later forms used to specialize execution for a target.</li>
</ul>

<p>
Without a dedicated IR layer, execution-oriented representation risks being redefined inconsistently by:
</p>

<ul>
  <li>editor-side convenience structures,</li>
  <li>cache payload examples,</li>
  <li>runtime-internal scheduler graphs,</li>
  <li>compiler-specific pipelines,</li>
  <li>backend-private deployment formats.</li>
</ul>

<p>
The IR layer exists to stop that drift and to give execution-facing representation a stable architectural home.
</p>

<pre><code>🟦 Expression/ says:
"what is saved"

🟦 IDE/ says:
"what is edited"

🟩 Language/ says:
"what the validated program means"

🟦 IR/ says:
"what execution-facing derived form may be built
from that validated meaning"

🟧 Lowering says:
"how open IR may be specialized for a target"

🟥 Runtime says:
"how one implementation realizes execution internally"
</code></pre>

<hr/>

<h2 id="layer-boundary-snapshot">4. Layer boundary snapshot</h2>

<p>
The shortest correct mental model of the surrounding architecture is:
</p>

<pre><code>+-------------------+--------------------------------------------------+
| Layer             | Primary question answered                        |
+-------------------+--------------------------------------------------+
| Expression/       | What is the canonical saved source?              |
| Language/         | What does the validated program mean?            |
| Libraries/        | What intrinsic primitives exist?                 |
| Profiles/         | What optional standardized capabilities exist?   |
| IDE/              | How is the program authored and observed?        |
| IR/               | What execution-facing derived representation     |
|                   | may be built from validated meaning?             |
+-------------------+--------------------------------------------------+
</code></pre>

<p>
A second boundary view is:
</p>

<pre><code>🟩 validated meaning
          |
          v
🟦 open execution-facing IR
          |
          v
🟨 IR handoff boundary
          |
          v
🟧 lowering / backend preparation
          |
          v
🟥 compiler / backend / runtime-private realization
</code></pre>

<hr/>

<h2 id="architectural-role">5. Architectural role</h2>

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
  <li><code>IR/</code> <strong>MUST NOT</strong> become a dumping ground for runtime-private internals,</li>
  <li><code>IR/</code> <strong>SHOULD</strong> define execution-facing derived forms that remain inspectable, portable, and specification-friendly,</li>
  <li><code>IR/</code> <strong>MAY</strong> define stable boundaries consumed by later specialization stages,</li>
  <li><code>IR/</code> <strong>MUST</strong> preserve a clear distinction between open IR and downstream realization-specific forms.</li>
</ul>

<pre><code>🟩 validated executable meaning
          |
          | semantic truth remains in Language/
          v
🟦 open execution-facing representation
          |
          | IR ownership begins here
          v
🟨 standardized handoff / identity / mapping boundary
          |
          | target specialization begins later
          v
🟧 lowering / backend-facing preparation
          |
          v
🟥 runtime-private realization
</code></pre>

<p>
This layer is therefore about <strong>derived execution representation and its immediate standardized handoffs</strong>.
It is not a replacement for the language core, and it is not a standardization vehicle for every private compiler or runtime detail.
</p>

<hr/>

<h2 id="position-in-the-representation-pipeline">6. Position in the representation pipeline</h2>

<p>
The intended position of the IR layer is illustrated below:
</p>

<pre><code>Authoring side
--------------
🟦 IDE Program Model
        |
        v
🟦 canonical .frog source
        |
        v
🟦 Expression/

Meaning side
------------
🟩 validated program meaning
        |
        +--&gt; 🟩 Language/
        +--&gt; 🟦 Libraries/
        +--&gt; 🟦 Profiles/

IR side
-------
🟦 Execution IR
🟨 Identity and Mapping
🟨 Derivation rules
🟨 Construction rules
        |
        v
🟦 IR/

Specialization side
-------------------
🟧 Lowering
🟨 Backend contract

Implementation side
-------------------
🟥 compiler preparation
🟥 backend mapping
🟥 runtime realization
🟥 deployment-specific forms
</code></pre>

<p>
The transition into <code>IR/</code> begins <strong>after</strong> the program has a validated meaning.
</p>

<p>
An implementation <strong>MAY</strong> derive IR directly from canonical source, from a validated Program Model, or from another equivalent validated internal form, but the resulting IR <strong>MUST</strong> remain semantically grounded in the validated FROG program rather than in editor-only convenience state.
</p>

<pre><code>🟦 .frog source
    |
    v
🟦 validated authoring form or equivalent
    |
    v
🟩 validated executable content
    |
    v
🟦 open Execution IR
    |
    v
🟧 lowered / backend-facing forms
    |
    v
🟥 compiler / runtime-private forms
</code></pre>

<hr/>

<h2 id="scope-of-this-directory">7. Scope of this directory</h2>

<p>
This directory is the normative home for questions such as:
</p>

<ul>
  <li>What execution-facing derived representations are standardized by FROG?</li>
  <li>What is the architectural boundary between validated program meaning and open IR?</li>
  <li>Which execution-facing properties are preserved from validated program meaning into IR?</li>
  <li>Which properties may be normalized, expanded, or made more explicit in IR?</li>
  <li>How is open Execution IR derived and constructed from validated program meaning?</li>
  <li>How are identity and attribution preserved between source-visible objects and IR objects?</li>
  <li>Where does open IR stop and later specialization begin?</li>
  <li>What downstream handoff assumptions may be standardized without collapsing into runtime-private realization?</li>
</ul>

<p>
This directory currently defines:
</p>

<ul>
  <li>the architectural boundary of the IR layer,</li>
  <li>the open Execution IR model,</li>
  <li>the derivation rules from validated FROG to open Execution IR,</li>
  <li>the construction rules for building open Execution IR,</li>
  <li>the identity and mapping boundary needed for recoverability and attribution,</li>
  <li>the first lowering boundary,</li>
  <li>the first backend-facing contract boundary.</li>
</ul>

<p>
The directory therefore contains both:
</p>

<ul>
  <li><strong>core IR documents</strong> that define the open execution-facing layer itself, and</li>
  <li><strong>IR-adjacent downstream documents</strong> that define how later stages connect to that layer.</li>
</ul>

<pre><code>🟦 Core IR ownership
- layer boundary
- Execution IR model
- derivation rules
- construction rules

🟨 Cross-boundary IR support
- identity and mapping

🟧 Downstream IR-adjacent ownership
- lowering
- backend contract
</code></pre>

<hr/>

<h2 id="what-this-directory-does-not-own">8. What this directory does not own</h2>

<p>
This directory does not define:
</p>

<ul>
  <li>the canonical <code>.frog</code> source structure in full,</li>
  <li>the public interface source model in full,</li>
  <li>the front-panel source model in full,</li>
  <li>the complete widget source model in full,</li>
  <li>the normative execution semantics of the language in full,</li>
  <li>the intrinsic primitive catalogs in full,</li>
  <li>the optional standardized profile catalogs in full,</li>
  <li>the IDE Program Model,</li>
  <li>IDE-facing debug UX or observability UX,</li>
  <li>a runtime-private scheduler architecture,</li>
  <li>a vendor-specific compiled artifact format,</li>
  <li>a backend-private transport representation.</li>
</ul>

<p>
In particular:
</p>

<ul>
  <li><code>Expression/</code> owns canonical source representation,</li>
  <li><code>Language/</code> owns normative validated meaning,</li>
  <li><code>Libraries/</code> owns intrinsic primitive vocabularies and primitive-local behavior,</li>
  <li><code>Profiles/</code> owns optional standardized capability families,</li>
  <li><code>IDE/</code> owns authoring-facing editable models and tooling-facing concerns.</li>
</ul>

<p>
The IR layer <strong>MUST NOT</strong> absorb those ownerships.
</p>

<pre><code>Ownership quick denial

"What does a valid .frog file look like?"          -&gt; 🟦 Expression/
"What does this construct mean?"                   -&gt; 🟩 Language/
"What primitive exists and what are its ports?"    -&gt; 🟦 Libraries/
"What optional capability family defines this?"    -&gt; 🟦 Profiles/
"How does the IDE edit or present this?"           -&gt; 🟦 IDE/
"What debugger UI is shown to the user?"           -&gt; 🟦 IDE/
"What private scheduler graph does runtime X use?" -&gt; 🟥 outside IR ownership
</code></pre>

<hr/>

<h2 id="relation-with-expression">9. Relation with Expression</h2>

<p>
<code>Expression/</code> defines the canonical serialized source artifact of a FROG program.
</p>

<p>
The source file remains the durable, authoritative saved representation of the program.
An execution IR is a <strong>derived form</strong>, not the canonical source.
</p>

<p>
Therefore:
</p>

<ul>
  <li>canonical source identity <strong>MUST</strong> remain owned by <code>Expression/</code>,</li>
  <li>the existence of an execution IR <strong>MUST NOT</strong> redefine what a valid <code>.frog</code> file is,</li>
  <li>the absence of an embedded or sidecar IR artifact <strong>MUST NOT</strong> invalidate canonical source,</li>
  <li>IR construction <strong>MAY</strong> depend on validated content originating from source-owned sections when relevant,</li>
  <li>IR attribution <strong>SHOULD</strong> remain able to refer back to source-visible objects defined by <code>Expression/</code>.</li>
</ul>

<pre><code>🟦 .frog source
   is not
🟦 execution IR

🟦 execution IR
   is derived from
🟩 validated source meaning
</code></pre>

<pre><code>🟦 Expression/
   owns:
   - canonical source structure
   - source serialization
   - source-visible object identity

🟦 IR/
   owns:
   - execution-facing derived form
   - execution-oriented normalization
   - source-attributed execution representation
</code></pre>

<hr/>

<h2 id="relation-with-language">10. Relation with Language</h2>

<p>
<code>Language/</code> defines what a validated FROG program means when it executes.
</p>

<p>
That semantic layer remains authoritative even when an implementation uses one or more execution IRs internally or through standardized open forms.
</p>

<p>
Accordingly:
</p>

<ul>
  <li><code>Language/</code> defines semantic truth,</li>
  <li><code>IR/</code> defines execution-facing derived representation,</li>
  <li><code>IR/</code> <strong>MUST NOT</strong> silently change language meaning,</li>
  <li><code>IR/</code> <strong>MAY</strong> make semantic consequences more explicit where execution preparation requires it,</li>
  <li>when tension appears between an IR convenience and normative language semantics, <code>Language/</code> remains authoritative.</li>
</ul>

<pre><code>🟩 Language/ answers:
"What is true?"

🟦 IR/ answers:
"How may that validated truth be represented
for execution-facing use?"
</code></pre>

<pre><code>🟩 semantic truth
      |
      v
🟦 derived execution-facing form
</code></pre>

<hr/>

<h2 id="relation-with-libraries-and-profiles">11. Relation with Libraries and Profiles</h2>

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

<pre><code>🟦 Libraries/ and Profiles/
      provide operation identities
                 |
                 v
🟦 IR/
      may reference them
      may normalize execution-facing use
      must not re-own them
</code></pre>

<hr/>

<h2 id="relation-with-the-ide-program-model">12. Relation with the IDE Program Model</h2>

<p>
The IDE Program Model is the authoritative editable in-memory representation during authoring.
The execution IR is not the Program Model.
</p>

<pre><code>🟦 Expression/   -&gt; what is saved
🟦 Program Model -&gt; what is edited
🟦 Execution IR  -&gt; what is prepared for execution
</code></pre>

<p>
The Program Model <strong>MAY</strong> preserve editor-side state that is useful for round-trip authoring.
The execution IR <strong>SHOULD NOT</strong> depend on editor-only presentation state as if that state were part of normative program meaning.
</p>

<p>
An IDE <strong>MAY</strong> construct, inspect, cache, compare, or visualize execution IR, but such capabilities do not transfer ownership of IR architecture to the IDE layer.
</p>

<pre><code>🟦 IDE concern
--------------
editable convenience
guided authoring
round-trip preservation
authoring-side state
debug UX
probe/watch presentation
paused-view rendering

🟦 IR concern
-------------
execution-facing structure
source attribution
identity continuity
normalization for execution preparation
derivation and construction rules
lowering handoff boundary
</code></pre>

<hr/>

<h2 id="relation-with-cache-artifacts">13. Relation with cache artifacts</h2>

<p>
A FROG source or toolchain <strong>MAY</strong> embed or associate cache artifacts that store derived execution-facing data such as <code>frog.ir</code>.
</p>

<p>
However, the cache container does not own the architectural definition of IR.
It only provides a storage or transport location for derived artifacts.
</p>

<p>
Therefore:
</p>

<ul>
  <li>cache entries such as <code>frog.ir</code> <strong>MAY</strong> carry execution-oriented derived data,</li>
  <li>cache presence <strong>MUST NOT</strong> change canonical source meaning,</li>
  <li>cache metadata such as generator information <strong>MUST NOT</strong> affect execution semantics,</li>
  <li>the normative meaning of execution IR belongs in <code>IR/</code>, not in cache examples,</li>
  <li>tools <strong>MAY</strong> define additional non-standard cache entries without redefining the FROG IR layer itself.</li>
</ul>

<pre><code>🟨 IR meaning
   lives in
🟦 IR/

🟨 serialized derived artifact
   may live in
cache entry: frog.ir

cache container
   is not
IR ownership
</code></pre>

<hr/>

<h2 id="relation-with-lowering-compilation-and-runtime">14. Relation with lowering, compilation, and runtime</h2>

<p>
This directory spans the boundary between open execution-facing IR and the first standardized downstream stages that may consume it.
</p>

<pre><code>🟩 validated meaning
      -&gt;
🟦 open execution IR
      -&gt;
🟨 identity / mapping / handoff boundary
      -&gt;
🟧 lowering
      -&gt;
🟨 backend contract
      -&gt;
🟥 compiler / backend / runtime-private realization
</code></pre>

<p>
This means:
</p>

<ul>
  <li><code>IR/Execution IR.md</code> defines an open representation, not a private scheduler graph,</li>
  <li><code>IR/Lowering.md</code> defines later specialization rules and boundaries,</li>
  <li><code>IR/Backend contract.md</code> defines assumptions for downstream consumption of later-stage forms,</li>
  <li>runtime-private scheduler graphs, compiled objects, deployment bundles, and backend-private executable forms <strong>SHOULD</strong> remain outside the ownership of this directory unless later standardized explicitly,</li>
  <li>the existence of an open FROG IR <strong>DOES NOT</strong> require every conforming implementation to expose every private internal form.</li>
</ul>

<pre><code>🟦 open IR
   != 🟥 private scheduler graph

🟦 open IR
   != 🟥 compiled artifact

🟦 open IR
   != 🟥 runtime trace

🟧 lowering
   != 🟥 runtime-private realization

🟨 backend contract
   != 🟥 backend-private internals
</code></pre>

<hr/>

<h2 id="relation-with-observation-debugging-and-diagnostics">15. Relation with observation, debugging, and diagnostics</h2>

<p>
This directory does not own debugger UX, probe presentation, watch presentation, or runtime command surfaces.
</p>

<p>
It <strong>does</strong> own part of what makes later source-aligned observation and diagnostics possible:
</p>

<ul>
  <li>source attribution,</li>
  <li>identity preservation across derivation,</li>
  <li>recoverable mapping between source-visible and derived objects,</li>
  <li>preservation of structure and region origin where required,</li>
  <li>preservation of explicit local-memory identity where required,</li>
  <li>execution-facing anchors that later tooling can consume.</li>
</ul>

<pre><code>🟩 Language/
   owns:
   - safe observation boundaries
   - pause-consistent snapshots
   - safe debug-stop validity

🟦 IR/
   owns:
   - execution-facing attribution foundations
   - recoverable derived identity
   - mapping anchors
   - structure-preserving execution-facing anchors

🟦 IDE/
   owns:
   - observability UX
   - debugger UX
   - watch/probe presentation
   - tooling projections built on the layers above
</code></pre>

<hr/>

<h2 id="ownership-quick-check">16. Ownership quick check</h2>

<p>
When writing or reviewing documents in this layer, the following quick check SHOULD help avoid ownership drift:
</p>

<pre><code>Does this define canonical source syntax or section structure?
-&gt; move to 🟦 Expression/

Does this define what validated behavior means?
-&gt; move to 🟩 Language/

Does this define intrinsic primitive identity or primitive-local behavior?
-&gt; move to 🟦 Libraries/

Does this define an optional standardized capability family?
-&gt; move to 🟦 Profiles/

Does this define authoring UX, editing behavior, debugging UX,
or IDE model behavior?
-&gt; move to 🟦 IDE/

Does this define an execution-facing derived representation
built from validated meaning?
-&gt; it likely belongs in 🟦 core IR

Does this define recoverable correspondence between source and IR?
-&gt; it likely belongs in 🟨 identity / mapping support

Does this define later specialization, target assumptions,
or a backend-facing handoff from IR?
-&gt; it likely belongs in 🟧 downstream IR-adjacent documents
</code></pre>

<hr/>

<h2 id="local-document-map">17. Local document map</h2>

<p>
The current published structure of the IR layer in repository state v0.1 is:
</p>

<pre><code>IR/
├─ Readme.md                  Architectural role and ownership of the IR layer
├─ Execution IR.md            Open execution-facing IR model
├─ Derivation rules.md        Mapping from validated FROG to open Execution IR
├─ Construction rules.md      Construction rules for open Execution IR
├─ Identity and Mapping.md    Identity continuity and recoverable mapping boundary
├─ Lowering.md                Lowering boundary from open IR toward target-facing forms
└─ Backend contract.md        Backend-facing contract boundary for later consumption
</code></pre>

<p>
The current ownership split of these documents is:
</p>

<ul>
  <li><code>Readme.md</code> defines the layer boundary and internal map,</li>
  <li><code>Execution IR.md</code> defines the first concrete open execution-facing IR model,</li>
  <li><code>Derivation rules.md</code> defines what must remain correspondingly recoverable between validated program meaning and open Execution IR,</li>
  <li><code>Construction rules.md</code> defines how a conforming open Execution IR is materially built,</li>
  <li><code>Identity and Mapping.md</code> defines how object identity and recoverable mapping survive derivation,</li>
  <li><code>Lowering.md</code> defines where open IR ends and target-oriented specialization begins,</li>
  <li><code>Backend contract.md</code> defines what later backend-facing stages may rely on once lowering has occurred.</li>
</ul>

<p>
A useful internal reading split is:
</p>

<pre><code>🟦 Core IR documents
- Readme.md
- Execution IR.md
- Derivation rules.md
- Construction rules.md

🟨 Boundary-support document
- Identity and Mapping.md

🟧 Downstream IR-adjacent documents
- Lowering.md
- Backend contract.md
</code></pre>

<p>
These documents are all part of the published <code>IR/</code> directory, but they do not all sit at the same architectural depth.
The open Execution IR remains the core of the layer.
Lowering and backend contract remain downstream from that core even when documented in the same directory.
</p>

<hr/>

<h2 id="reading-relationships">18. Reading relationships</h2>

<p>
This README should not be read in isolation.
</p>

<p>
A practical reading path is:
</p>

<pre><code>root Readme.md
      -&gt;
IR/Readme.md
      -&gt;
IR/Execution IR.md
      -&gt;
IR/Derivation rules.md
      -&gt;
IR/Construction rules.md
      -&gt;
IR/Identity and Mapping.md
      -&gt;
IR/Lowering.md
      -&gt;
IR/Backend contract.md
      -&gt;
Language/Readme.md
      -&gt;
Language/Execution model.md
      -&gt;
Language/Execution control and observation boundaries.md
      -&gt;
IDE/Execution observability.md
      -&gt;
Expression/Readme.md
      -&gt;
Expression/Cache.md
</code></pre>

<p>
That reading path is useful because:
</p>

<ul>
  <li>the root README explains repository-wide architecture,</li>
  <li>this file defines the ownership boundary of the IR layer,</li>
  <li><code>Execution IR.md</code> defines the first concrete execution-facing representation,</li>
  <li><code>Derivation rules.md</code> closes the validated-program-to-IR correspondence boundary,</li>
  <li><code>Construction rules.md</code> closes the IR build boundary,</li>
  <li><code>Identity and Mapping.md</code> explains recoverability and attribution continuity,</li>
  <li><code>Lowering.md</code> explains later specialization boundaries,</li>
  <li><code>Backend contract.md</code> explains downstream backend-facing assumptions,</li>
  <li><code>Language/</code> defines semantic truth and execution boundaries,</li>
  <li><code>IDE/</code> defines observability-facing and tooling-facing projections,</li>
  <li><code>Expression/</code> defines canonical source and cache-carried derived artifacts.</li>
</ul>

<hr/>

<h2 id="status-in-v01">19. Status in v0.1</h2>

<p>
In repository state v0.1, this directory now defines a substantially clearer IR architecture than before.
</p>

<p>
The current closure of the directory is:
</p>

<ul>
  <li>a clear architectural home for open execution-facing derived representations,</li>
  <li>a first concrete open Execution IR model,</li>
  <li>a derivation boundary from validated FROG to open Execution IR,</li>
  <li>a construction boundary for building open Execution IR,</li>
  <li>an explicit identity and mapping boundary,</li>
  <li>a first documented lowering boundary,</li>
  <li>a first documented backend-facing contract boundary.</li>
</ul>

<p>
What is still intentionally <strong>not</strong> frozen in v0.1 includes:
</p>

<ul>
  <li>one universal serialized IR wire format,</li>
  <li>one universal normalization pipeline shape,</li>
  <li>one mandatory lowering pipeline shape,</li>
  <li>one mandatory backend-family taxonomy,</li>
  <li>one mandatory runtime-private execution structure,</li>
  <li>one mandatory debugger or observability transport protocol.</li>
</ul>

<p>
The directory is therefore closed enough to define the first coherent IR architecture, but it still deliberately avoids over-freezing implementation-private realization.
</p>

<pre><code>🟦 IR is the published architectural home for:
- open execution-facing representation
- derivation and construction rules
- recoverable identity and mapping
- downstream handoff boundaries

It is not:
- the source
- the Program Model
- the full language semantics
- the debugger UX
- one private runtime's internal graph

It is the architectural bridge between:
🟩 validated meaning
and
🟧 later specialization for realization
while keeping
🟥 runtime-private internals outside the open layer
</code></pre>
