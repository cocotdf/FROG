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
  <li><a href="#reading-legend">2. Reading Legend</a></li>
  <li><a href="#why-this-layer-exists">3. Why this Layer Exists</a></li>
  <li><a href="#architectural-boundary">4. Architectural Boundary</a></li>
  <li><a href="#position-in-the-representation-pipeline">5. Position in the Representation Pipeline</a></li>
  <li><a href="#scope-of-this-directory">6. Scope of this Directory</a></li>
  <li><a href="#what-this-directory-does-not-own">7. What this Directory Does Not Own</a></li>
  <li><a href="#relation-with-surrounding-layers">8. Relation with Surrounding Layers</a>
    <ul>
      <li><a href="#relation-with-expression">8.1 Relation with Expression</a></li>
      <li><a href="#relation-with-language">8.2 Relation with Language</a></li>
      <li><a href="#relation-with-libraries-and-profiles">8.3 Relation with Libraries and Profiles</a></li>
      <li><a href="#relation-with-the-ide-program-model">8.4 Relation with the IDE Program Model</a></li>
      <li><a href="#relation-with-cache-artifacts">8.5 Relation with Cache Artifacts</a></li>
      <li><a href="#relation-with-observation-debugging-and-diagnostics">8.6 Relation with Observation, Debugging, and Diagnostics</a></li>
    </ul>
  </li>
  <li><a href="#internal-document-structure">9. Internal Document Structure</a></li>
  <li><a href="#document-ownership-split">10. Document Ownership Split</a></li>
  <li><a href="#ownership-quick-check">11. Ownership Quick Check</a></li>
  <li><a href="#practical-reading-path">12. Practical Reading Path</a></li>
  <li><a href="#status-in-v01">13. Status in v0.1</a></li>
  <li><a href="#summary">14. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the architectural home of <strong>open execution-facing representations</strong> in the FROG specification.
</p>

<p>
A FROG program is not authored directly as an execution IR.
It is authored as canonical source, validated against the relevant semantic, intrinsic-library, and profile rules, and only then may be represented in one or more <strong>open execution-facing derived forms</strong>.
</p>

<p>
The purpose of <code>IR/</code> is to ensure that execution-facing representation is not scattered across:
</p>

<ul>
  <li>source-format documents,</li>
  <li>IDE-internal authoring models,</li>
  <li>cache payload examples,</li>
  <li>primitive or profile catalogs,</li>
  <li>runtime-private scheduler forms,</li>
  <li>backend-specific realization documents.</li>
</ul>

<p>
This directory therefore provides the durable normative home for:
</p>

<ul>
  <li>the <strong>open Execution IR</strong> itself,</li>
  <li>the <strong>derivation boundary</strong> from validated program meaning to open IR,</li>
  <li>the <strong>construction boundary</strong> for materially building conforming open IR payloads,</li>
  <li>the <strong>identity and mapping boundary</strong> that preserves attribution and recoverability,</li>
  <li>the first downstream-adjacent boundaries toward lowering and backend-facing handoff.</li>
</ul>

<pre><code>canonical source
      -&gt;
validated program meaning
      -&gt;
open execution-facing IR
      -&gt;
later specialization / lowering
      -&gt;
private realization
</code></pre>

<p>
The core of this layer is the open Execution IR bundle.
The directory also contains downstream-adjacent documents that define how open IR connects to later stages without collapsing the open IR layer into runtime-private form.
</p>

<hr/>

<h2 id="reading-legend">2. Reading Legend</h2>

<p>
The diagrams in this README use the following visual legend:
</p>

<ul>
  <li>🟦 <strong>Open specification-facing layer or document</strong></li>
  <li>🟨 <strong>Standardized boundary, correspondence, mapping, or handoff</strong></li>
  <li>🟧 <strong>Lowering or target-specialization zone</strong></li>
  <li>🟥 <strong>Implementation-private realization zone</strong></li>
  <li>🟩 <strong>Semantic truth, attribution, recoverability, or diagnostic obligation</strong></li>
</ul>

<hr/>

<h2 id="why-this-layer-exists">3. Why this Layer Exists</h2>

<p>
FROG deliberately separates several architectural levels that are often conflated in graphical systems:
</p>

<ul>
  <li>the canonical saved source artifact,</li>
  <li>the IDE editable in-memory model,</li>
  <li>validated program meaning,</li>
  <li>the derived forms used to prepare execution,</li>
  <li>the later forms used to specialize execution for a target.</li>
</ul>

<p>
Without a dedicated IR layer, execution-facing representation tends to drift into:
</p>

<ul>
  <li>editor-side convenience structures,</li>
  <li>cache examples,</li>
  <li>runtime-private scheduler graphs,</li>
  <li>compiler-specific internal pipelines,</li>
  <li>backend-private deployment formats.</li>
</ul>

<p>
The IR layer exists to stop that drift and to give execution-facing representation a stable architectural home.
</p>

<pre><code>Expression/ says:
"what is saved"

IDE/ says:
"what is edited"

Language/ says:
"what the validated program means"

IR/ says:
"what open execution-facing representation may be built
from that validated meaning"

Lowering says:
"how open IR may be specialized for a target"

Runtime says:
"how one implementation realizes execution internally"
</code></pre>

<hr/>

<h2 id="architectural-boundary">4. Architectural Boundary</h2>

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
| IR/               | What open execution-facing representation        |
|                   | may be built from validated meaning?             |
+-------------------+--------------------------------------------------+
</code></pre>

<p>
A second boundary view is:
</p>

<pre><code>validated program meaning
          |
          v
open execution-facing IR
          |
          v
identity / mapping / construction / handoff boundary
          |
          v
lowering / backend preparation
          |
          v
compiler / backend / runtime-private realization
</code></pre>

<p>
The key architectural rule is:
</p>

<ul>
  <li><code>IR/</code> begins <strong>after validated program meaning</strong>,</li>
  <li><code>IR/</code> remains <strong>before lowering and backend-facing contract</strong>,</li>
  <li><code>IR/</code> MUST remain distinct from runtime-private realization.</li>
</ul>

<hr/>

<h2 id="position-in-the-representation-pipeline">5. Position in the Representation Pipeline</h2>

<p>
The intended position of the IR layer is illustrated below:
</p>

<pre><code>Authoring side
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
        +--&gt; Language/
        +--&gt; Libraries/
        +--&gt; Profiles/

IR side
-------
Execution IR
Derivation rules
Construction rules
Identity and Mapping
        |
        v
IR/

Downstream IR-adjacent side
---------------------------
Lowering
Backend contract

Implementation side
-------------------
compiler preparation
backend mapping
runtime realization
deployment-specific forms
</code></pre>

<p>
The transition into <code>IR/</code> begins <strong>after</strong> the program has validated program meaning.
</p>

<p>
An implementation MAY derive IR directly from canonical source, from a validated Program Model, or from another equivalent validated internal form, but the resulting IR MUST remain semantically grounded in validated program meaning rather than in editor-only convenience state.
</p>

<pre><code>.frog source
    |
    v
validated authoring form or equivalent
    |
    v
validated program meaning
    |
    v
open Execution IR
    |
    v
lowered / backend-facing forms
    |
    v
compiler / runtime-private forms
</code></pre>

<hr/>

<h2 id="scope-of-this-directory">6. Scope of this Directory</h2>

<p>
This directory is the normative home for questions such as:
</p>

<ul>
  <li>What open execution-facing representations are standardized by FROG?</li>
  <li>What is the architectural boundary between validated program meaning and open IR?</li>
  <li>Which execution-facing properties are preserved from validated program meaning into IR?</li>
  <li>Which properties may be made more explicit in IR without changing semantic truth?</li>
  <li>How is open Execution IR derived and constructed from validated program meaning?</li>
  <li>How are identity, attribution, and recoverability preserved between source-visible content and IR content?</li>
  <li>Where does open IR stop and later specialization begin?</li>
  <li>What downstream handoff assumptions may be standardized without collapsing into runtime-private realization?</li>
</ul>

<p>
This directory therefore contains both:
</p>

<ul>
  <li><strong>core open-IR documents</strong> that define the open execution-facing layer itself, and</li>
  <li><strong>downstream IR-adjacent documents</strong> that define how later stages connect to that layer.</li>
</ul>

<pre><code>Core open-IR bundle
- Execution IR model
- derivation rules
- construction rules
- identity and mapping support

Downstream IR-adjacent documents
- lowering
- backend contract
</code></pre>

<hr/>

<h2 id="what-this-directory-does-not-own">7. What this Directory Does Not Own</h2>

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
  <li><code>Language/</code> owns validated program meaning,</li>
  <li><code>Libraries/</code> owns intrinsic primitive vocabularies and primitive-local behavior,</li>
  <li><code>Profiles/</code> owns optional standardized capability families,</li>
  <li><code>IDE/</code> owns authoring-facing editable models and tooling-facing concerns.</li>
</ul>

<p>
The IR layer <strong>MUST NOT</strong> absorb those ownerships.
</p>

<pre><code>Ownership quick denial

"What does a valid .frog file look like?"          -&gt; Expression/
"What does this construct mean?"                   -&gt; Language/
"What primitive exists and what are its ports?"    -&gt; Libraries/
"What optional capability family defines this?"    -&gt; Profiles/
"How does the IDE edit or present this?"           -&gt; IDE/
"What debugger UI is shown to the user?"           -&gt; IDE/
"What private scheduler graph does runtime X use?" -&gt; outside IR ownership
</code></pre>

<hr/>

<h2 id="relation-with-surrounding-layers">8. Relation with Surrounding Layers</h2>

<h3 id="relation-with-expression">8.1 Relation with Expression</h3>

<p>
<code>Expression/</code> defines the canonical serialized source artifact of a FROG program.
The source file remains the durable authoritative saved representation of the program.
An execution IR is a <strong>derived form</strong>, not the canonical source.
</p>

<ul>
  <li>canonical source identity MUST remain owned by <code>Expression/</code>,</li>
  <li>the existence of an execution IR MUST NOT redefine what a valid <code>.frog</code> file is,</li>
  <li>the absence of an embedded or sidecar IR artifact MUST NOT invalidate canonical source,</li>
  <li>IR attribution SHOULD remain able to refer back to source-visible objects defined by <code>Expression/</code>.</li>
</ul>

<pre><code>.frog source
   is not
execution IR

execution IR
   is derived from
validated program meaning
</code></pre>

<h3 id="relation-with-language">8.2 Relation with Language</h3>

<p>
<code>Language/</code> defines what a validated FROG program means when it executes.
That semantic layer remains authoritative even when one or more execution IRs exist.
</p>

<ul>
  <li><code>Language/</code> defines semantic truth,</li>
  <li><code>IR/</code> defines open execution-facing representation,</li>
  <li><code>IR/</code> MUST NOT silently change language meaning,</li>
  <li><code>IR/</code> MAY make semantic consequences more explicit where execution preparation requires it.</li>
</ul>

<pre><code>Language/ answers:
"What is true?"

IR/ answers:
"How may that validated truth be represented
for execution-facing use?"
</code></pre>

<h3 id="relation-with-libraries-and-profiles">8.3 Relation with Libraries and Profiles</h3>

<p>
IR is not a replacement for primitive-library or profile definitions.
When an IR refers to executable operations, it SHOULD preserve or reference the primitive and capability identities defined elsewhere rather than redefining them privately.
</p>

<ul>
  <li><code>Libraries/</code> owns intrinsic primitive namespaces, ports, and primitive-local behavior,</li>
  <li><code>Profiles/</code> owns optional standardized capability families,</li>
  <li><code>IR/</code> MAY carry normalized references to those operations for execution-facing purposes,</li>
  <li><code>IR/</code> MUST NOT redefine a primitive catalog or capability-family catalog as if that catalog belonged here.</li>
</ul>

<h3 id="relation-with-the-ide-program-model">8.4 Relation with the IDE Program Model</h3>

<p>
The IDE Program Model is the authoritative editable in-memory representation during authoring.
The open Execution IR is not the Program Model.
</p>

<pre><code>Expression/   -&gt; what is saved
Program Model -&gt; what is edited
Execution IR  -&gt; what is prepared for execution
</code></pre>

<p>
The Program Model MAY preserve editor-side state useful for round-trip authoring.
The open Execution IR SHOULD NOT depend on editor-only presentation state as if that state were part of validated program meaning.
</p>

<h3 id="relation-with-cache-artifacts">8.5 Relation with Cache Artifacts</h3>

<p>
A FROG source or toolchain MAY embed or associate cache artifacts that store derived execution-facing data such as <code>frog.ir</code>.
However, the cache container does not own the architectural definition of IR.
It only provides a storage or transport location for derived artifacts.
</p>

<ul>
  <li>cache entries such as <code>frog.ir</code> MAY carry execution-facing derived data,</li>
  <li>cache presence MUST NOT change canonical source meaning,</li>
  <li>cache metadata MUST NOT affect execution semantics,</li>
  <li>the normative meaning of execution IR belongs in <code>IR/</code>, not in cache examples.</li>
</ul>

<pre><code>IR meaning
   lives in
IR/

serialized derived artifact
   may live in
cache entry: frog.ir

cache container
   is not
IR ownership
</code></pre>

<h3 id="relation-with-observation-debugging-and-diagnostics">8.6 Relation with Observation, Debugging, and Diagnostics</h3>

<p>
This directory does not own debugger UX, probe presentation, watch presentation, or runtime command surfaces.
It <strong>does</strong> own part of what makes later source-aligned observation and diagnostics possible:
</p>

<ul>
  <li>source attribution,</li>
  <li>recoverable derived identity,</li>
  <li>mapping anchors between source-visible and derived objects,</li>
  <li>preservation of structure and region origin where required,</li>
  <li>preservation of explicit local-memory identity where required.</li>
</ul>

<pre><code>Language/
   owns:
   - safe observation boundaries
   - pause-consistent snapshots
   - safe debug-stop validity

IR/
   owns:
   - execution-facing attribution foundations
   - recoverable derived identity
   - mapping anchors
   - structure-preserving execution-facing anchors

IDE/
   owns:
   - observability UX
   - debugger UX
   - watch/probe presentation
   - tooling projections built on the layers above
</code></pre>

<hr/>

<h2 id="internal-document-structure">9. Internal Document Structure</h2>

<p>
The current published structure of the IR layer is:
</p>

<pre><code>IR/
├─ Readme.md                  Architectural role and ownership of the IR layer
├─ Execution IR.md            Open execution-facing IR model
├─ Derivation rules.md        Correspondence from validated program meaning to open Execution IR
├─ Construction rules.md      Material construction rules for open Execution IR
├─ Identity and Mapping.md    Recoverable identity and mapping boundary
├─ Lowering.md                Boundary from open IR toward target-oriented specialization
└─ Backend contract.md        Backend-facing contract boundary for later consumption
</code></pre>

<p>
These documents all belong to <code>IR/</code>, but they do not all sit at the same architectural depth.
The open Execution IR bundle remains the core of the layer.
Lowering and backend contract remain downstream from that core even when documented in the same directory.
</p>

<pre><code>Core open-IR bundle
- Execution IR.md
- Derivation rules.md
- Construction rules.md
- Identity and Mapping.md

Downstream IR-adjacent documents
- Lowering.md
- Backend contract.md
</code></pre>

<hr/>

<h2 id="document-ownership-split">10. Document Ownership Split</h2>

<p>
The ownership split inside this directory is:
</p>

<ul>
  <li><code>Readme.md</code> defines the layer boundary, scope, and internal map.</li>
  <li><code>Execution IR.md</code> defines what the open Execution IR is at the architectural level.</li>
  <li><code>Derivation rules.md</code> defines what must correspond between validated program meaning and open Execution IR.</li>
  <li><code>Construction rules.md</code> defines how a conforming open Execution IR payload is materially built.</li>
  <li><code>Identity and Mapping.md</code> defines how attribution, recoverability, and mapping continuity survive derivation.</li>
  <li><code>Lowering.md</code> defines where open IR ends and target-oriented specialization begins.</li>
  <li><code>Backend contract.md</code> defines what later backend-facing stages may rely on once lowering has occurred.</li>
</ul>

<pre><code>Readme.md
   -&gt; layer architecture and ownership

Execution IR.md
   -&gt; open IR model

Derivation rules.md
   -&gt; correspondence obligations

Construction rules.md
   -&gt; build obligations

Identity and Mapping.md
   -&gt; recoverability obligations

Lowering.md
   -&gt; downstream specialization boundary

Backend contract.md
   -&gt; downstream consumer-facing boundary
</code></pre>

<hr/>

<h2 id="ownership-quick-check">11. Ownership Quick Check</h2>

<p>
When writing or reviewing documents in this layer, the following quick check SHOULD help avoid ownership drift:
</p>

<pre><code>Does this define canonical source syntax or section structure?
-&gt; move to Expression/

Does this define what validated behavior means?
-&gt; move to Language/

Does this define intrinsic primitive identity or primitive-local behavior?
-&gt; move to Libraries/

Does this define an optional standardized capability family?
-&gt; move to Profiles/

Does this define authoring UX, editing behavior, debugging UX,
or IDE model behavior?
-&gt; move to IDE/

Does this define an execution-facing derived representation
built from validated meaning?
-&gt; it likely belongs in core IR

Does this define recoverable correspondence between source and IR?
-&gt; it likely belongs in Identity and Mapping.md
   and related IR documents

Does this define later specialization, target assumptions,
or a backend-facing handoff from IR?
-&gt; it likely belongs in downstream IR-adjacent documents
</code></pre>

<hr/>

<h2 id="practical-reading-path">12. Practical Reading Path</h2>

<p>
This README should not be read in isolation.
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
Expression/Readme.md
      -&gt;
Expression/Cache.md
      -&gt;
IDE/ relevant observability and tooling documents
</code></pre>

<p>
That path is useful because:
</p>

<ul>
  <li>the root README explains repository-wide architecture,</li>
  <li>this file defines the ownership boundary of the IR layer,</li>
  <li><code>Execution IR.md</code> defines the open execution-facing model,</li>
  <li><code>Derivation rules.md</code> closes the validated-program-to-IR correspondence boundary,</li>
  <li><code>Construction rules.md</code> closes the IR build boundary,</li>
  <li><code>Identity and Mapping.md</code> explains attribution continuity and recoverability,</li>
  <li><code>Lowering.md</code> explains where specialization begins,</li>
  <li><code>Backend contract.md</code> explains downstream backend-facing assumptions,</li>
  <li><code>Language/</code> remains the authority for semantic truth,</li>
  <li><code>Expression/</code> remains the authority for canonical source.</li>
</ul>

<hr/>

<h2 id="status-in-v01">13. Status in v0.1</h2>

<p>
In repository state v0.1, this directory defines a coherent first IR architecture.
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
The directory is therefore closed enough to define the first coherent IR architecture, while still deliberately avoiding over-freezing implementation-private realization.
</p>

<pre><code>IR is the published architectural home for:
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
validated program meaning
and
later specialization for realization
while keeping
runtime-private internals outside the open layer
</code></pre>

<hr/>

<h2 id="summary">14. Summary</h2>

<p>
The <code>IR/</code> layer is the architectural bridge between:
</p>

<ul>
  <li><strong>validated FROG program meaning</strong>, and</li>
  <li><strong>later specialization for execution realization</strong>.</li>
</ul>

<p>
Its core responsibility is to define an <strong>open, execution-facing, attributable, and recoverable representation layer</strong> without collapsing that layer into source syntax, IDE authoring models, or runtime-private realization.
</p>

<p>
In compact form:
</p>

<pre><code>🟩 validated program meaning
      -&gt;
🟦 open execution-facing IR
      -&gt;
🟧 later specialization
      -&gt;
🟨 backend-facing handoff
      -&gt;
🟥 private realization
</code></pre>
