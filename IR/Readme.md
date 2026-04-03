<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Intermediate Representation Architecture</h1>

<p align="center">
  <strong>Architectural definition of the IR layer for FROG v0.1</strong><br/>
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
  <li><a href="#relation-with-surrounding-layers">8. Relation with Surrounding Layers</a></li>
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
This directory defines the architectural home of open execution-facing representations in the FROG specification.
</p>

<p>
A FROG program is not authored directly as an execution IR.
It is authored as canonical source, admitted through structural validity, interpreted as validated program meaning, and only then represented as a canonical open execution intermediate representation.
</p>

<p>
The purpose of <code>IR/</code> is to ensure that execution-facing representation is not scattered across:
</p>

<ul>
  <li>source-format documents,</li>
  <li>source-schema artifacts,</li>
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
  <li>the canonical Execution IR Document itself,</li>
  <li>the derivation boundary from validated program meaning to canonical open IR,</li>
  <li>the construction boundary for materially building conforming canonical IR documents,</li>
  <li>the identity and mapping boundary that preserves attribution and recoverability,</li>
  <li>the schema posture and machine-checkable validation surface of the canonical JSON IR form,</li>
  <li>the first downstream-adjacent boundaries toward lowering and backend-facing handoff.</li>
</ul>

<pre><code>canonical source
      -&gt;
structural validity
      -&gt;
validated program meaning
      -&gt;
canonical Execution IR Document
      -&gt;
later specialization / lowering
      -&gt;
backend-facing handoff
      -&gt;
private realization</code></pre>

<p>
The core of this layer is the canonical open Execution IR bundle.
The directory also contains downstream-adjacent documents that define how open IR connects to later stages without collapsing the open IR layer into runtime-private form.
</p>

<hr/>

<h2 id="reading-legend">2. Reading Legend</h2>

<p>
The diagrams in this README use the following visual legend:
</p>

<ul>
  <li>Open specification-facing layer or document</li>
  <li>Standardized boundary, correspondence, mapping, schema, or handoff</li>
  <li>Lowering or target-specialization zone</li>
  <li>Implementation-private realization zone</li>
  <li>Semantic truth, attribution, recoverability, or diagnostic obligation</li>
</ul>

<hr/>

<h2 id="why-this-layer-exists">3. Why this Layer Exists</h2>

<p>
FROG deliberately separates several architectural levels that are often conflated in graphical systems:
</p>

<ul>
  <li>the canonical saved source artifact,</li>
  <li>the source-owned structural admission boundary,</li>
  <li>the IDE editable in-memory model,</li>
  <li>validated program meaning,</li>
  <li>the canonical execution-facing representation used to prepare execution,</li>
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
"what is saved and structurally admitted as source"

IDE/ says:
"what is edited"

Language/ says:
"what the validated program means"

IR/ says:
"what canonical open execution-facing representation is built
from that validated meaning"

Lowering says:
"how canonical open IR is specialized for a target"

Runtime says:
"how one implementation realizes execution internally"</code></pre>

<hr/>

<h2 id="architectural-boundary">4. Architectural Boundary</h2>

<p>
The shortest correct mental model of the surrounding architecture is:
</p>

<pre><code>+-------------------+--------------------------------------------------+
| Layer             | Primary question answered                        |
+-------------------+--------------------------------------------------+
| Expression/       | What is the canonical saved source?              |
|                   | What counts as structurally valid source?        |
| Language/         | What does the validated program mean?            |
| Libraries/        | What intrinsic primitives exist?                 |
| Profiles/         | What optional standardized capabilities exist?   |
| IDE/              | How is the program authored and observed?        |
| IR/               | What canonical open execution-facing             |
|                   | representation is built from validated meaning?  |
+-------------------+--------------------------------------------------+</code></pre>

<p>
A second boundary view is:
</p>

<pre><code>validated program meaning
          |
          v
canonical open Execution IR
          |
          v
identity / mapping / derivation / construction / schema boundary
          |
          v
lowering / backend preparation
          |
          v
compiler / backend / runtime-private realization</code></pre>

<p>
The key architectural rule is:
</p>

<ul>
  <li><code>IR/</code> begins after validated program meaning,</li>
  <li><code>IR/</code> defines the canonical open execution IR boundary artifact,</li>
  <li><code>IR/</code> remains before lowering and backend-facing contract,</li>
  <li><code>IR/</code> MUST remain distinct from runtime-private realization.</li>
</ul>

<p>
More precisely, the core open-IR bundle is:
</p>

<ul>
  <li><code>Execution IR.md</code>,</li>
  <li><code>Derivation rules.md</code>,</li>
  <li><code>Construction rules.md</code>,</li>
  <li><code>Identity and Mapping.md</code>,</li>
  <li><code>Schema.md</code>,</li>
  <li><code>schema/</code>.</li>
</ul>

<p>
The downstream IR-adjacent documents are:
</p>

<ul>
  <li><code>Lowering.md</code>,</li>
  <li><code>Backend contract.md</code>.</li>
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

Admission side
--------------
loadability
        |
        v
structural validity
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
Schema
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
deployment-specific forms</code></pre>

<p>
The transition into <code>IR/</code> begins after the program has validated program meaning.
An implementation MAY derive IR directly from canonical source, from a validated Program Model, or from another equivalent validated internal form, but the resulting IR MUST remain semantically grounded in validated program meaning rather than in parser-only acceptance, structural-source admission alone, or editor-only convenience state.
</p>

<p>
The practical corridor that the IR layer closes explicitly is:
</p>

<pre><code>.frog source
    |
    v
loadability
    |
    v
structural validity
    |
    v
validated authoring form or equivalent
    |
    v
validated program meaning
    |
    v
derivation
    |
    v
identity / mapping preservation
    |
    v
construction
    |
    v
canonical Execution IR Document
    |
    v
canonical JSON validation
    |
    v
lowered / backend-facing forms
    |
    v
compiler / runtime-private forms</code></pre>

<p>
This is the practical corridor that the IR layer closes explicitly:
</p>

<pre><code>validated program meaning
        -&gt;
derivation
        -&gt;
recoverable IR identity and mapping
        -&gt;
material IR construction
        -&gt;
canonical Execution IR Document
        -&gt;
canonical JSON schema validation
        -&gt;
later lowering and backend-facing handoff</code></pre>

<hr/>

<h2 id="scope-of-this-directory">6. Scope of this Directory</h2>

<p>
This directory owns the architectural answers to questions such as:
</p>

<ul>
  <li>What open execution-facing representations are standardized by FROG?</li>
  <li>What is the architectural boundary between validated program meaning and open IR?</li>
  <li>Which execution-facing properties are preserved from validated program meaning into IR?</li>
  <li>Which properties may be made more explicit in IR without changing semantic truth?</li>
  <li>How is the canonical Execution IR Document derived and constructed from validated program meaning?</li>
  <li>How are identity, attribution, and recoverability preserved between source-visible content and IR content?</li>
  <li>How is the canonical JSON form of the Execution IR validated?</li>
  <li>Where does open IR stop and later specialization begin?</li>
  <li>What downstream handoff assumptions may be standardized without collapsing into runtime-private realization?</li>
</ul>

<p>
This directory therefore contains both:
</p>

<ul>
  <li>core open-IR documents that define the open execution-facing layer itself, and</li>
  <li>downstream IR-adjacent documents that define how later stages connect to that layer.</li>
</ul>

<pre><code>Core open-IR bundle
- Execution IR model
- derivation rules
- construction rules
- recoverable identity and mapping
- schema posture
- machine-checkable schema artifacts

Downstream IR-adjacent documents
- lowering
- backend contract</code></pre>

<hr/>

<h2 id="what-this-directory-does-not-own">7. What this Directory Does Not Own</h2>

<p>
This directory does not define:
</p>

<ul>
  <li>the canonical <code>.frog</code> source structure in full,</li>
  <li>source-schema posture or machine-checkable source shape artifacts,</li>
  <li>the public interface source model in full,</li>
  <li>the front-panel source model in full,</li>
  <li>the complete widget source model in full,</li>
  <li>the normative execution semantics of the language in full,</li>
  <li>the intrinsic primitive catalogs in full,</li>
  <li>the optional standardized profile catalogs in full,</li>
  <li>the IDE Program Model,</li>
  <li>IDE-facing debug UX or observability UX,</li>
  <li>cache ownership,</li>
  <li>runtime-private execution formats,</li>
  <li>one mandatory compiler architecture,</li>
  <li>one mandatory backend-family implementation,</li>
  <li>one mandatory runtime-private storage model.</li>
</ul>

<p>
This non-ownership rule is essential.
Without it, the IR layer would become a catch-all replacement for other parts of the architecture.
</p>

<hr/>

<h2 id="relation-with-surrounding-layers">8. Relation with Surrounding Layers</h2>

<h3>8.1 Relation with Expression</h3>

<p>
<code>Expression/</code> owns canonical source representation and structural validity.
That ownership remains authoritative even when canonical IR exists.
</p>

<ul>
  <li>canonical source identity MUST remain owned by <code>Expression/</code>,</li>
  <li>the existence of an Execution IR document MUST NOT redefine what a valid <code>.frog</code> file is,</li>
  <li>the absence of an embedded or sidecar IR artifact MUST NOT invalidate canonical source,</li>
  <li>IR attribution SHOULD remain able to refer back to source-visible objects defined by <code>Expression/</code>.</li>
</ul>

<pre><code>.frog source
   is not
Execution IR

Execution IR
   is derived from
validated program meaning

structural validity
   is not
Execution IR</code></pre>

<h3>8.2 Relation with Language</h3>

<p>
<code>Language/</code> defines what a validated FROG program means when it executes.
That semantic layer remains authoritative even when one or more execution IR artifacts exist.
</p>

<ul>
  <li><code>Language/</code> defines semantic truth,</li>
  <li><code>IR/</code> defines canonical open execution-facing representation,</li>
  <li><code>IR/</code> MUST NOT silently change language meaning,</li>
  <li><code>IR/</code> MAY make semantic consequences more explicit where execution preparation requires it.</li>
</ul>

<pre><code>Language/ answers:
"What is true?"

IR/ answers:
"What open execution-facing representation is built
from that truth?"</code></pre>

<h3>8.3 Relation with Libraries and Profiles</h3>

<p>
<code>Libraries/</code> owns intrinsic primitive vocabularies.
<code>Profiles/</code> owns optional standardized capability families.
The IR layer does not re-own either catalog.
</p>

<ul>
  <li>primitive identity remains owned by the relevant library layer,</li>
  <li>optional capability identity remains owned by the relevant profile layer,</li>
  <li><code>IR/</code> derives execution-facing representation from validated use of those surfaces,</li>
  <li><code>IR/</code> may standardize how those validated uses appear in open IR, but not what primitives or profiles exist in the first place.</li>
</ul>

<h3>8.4 Relation with the IDE Program Model</h3>

<p>
The IDE Program Model is an authoring-facing internal or semi-internal representation used to support editing, round-trip operations, diagnostics workflows, and related tooling.
It is not the same thing as the canonical open Execution IR.
</p>

<ul>
  <li>the Program Model MAY contain editor-side convenience state,</li>
  <li>the Program Model MAY preserve round-trip authoring detail that the canonical open IR does not own,</li>
  <li>the canonical Execution IR SHOULD NOT depend on editor-only presentation state as if that state were part of validated program meaning.</li>
</ul>

<h3>8.5 Relation with Cache Artifacts</h3>

<p>
A FROG source or toolchain MAY embed or associate cache artifacts that store derived execution-facing data such as <code>frog.ir</code>.
However, the cache container does not own the architectural definition of IR.
It only provides a storage or transport location for derived artifacts.
</p>

<ul>
  <li>cache entries such as <code>frog.ir</code> MAY carry serialized canonical Execution IR data,</li>
  <li>cache presence MUST NOT change canonical source meaning,</li>
  <li>cache metadata MUST NOT affect execution semantics,</li>
  <li>the normative meaning of Execution IR belongs in <code>IR/</code>, not in cache examples.</li>
</ul>

<pre><code>IR meaning
   lives in
IR/

serialized derived artifact
   may live in
cache entry: frog.ir

cache container
   is not
IR ownership</code></pre>

<h3>8.6 Relation with Observation, Debugging, and Diagnostics</h3>

<p>
This directory does not own debugger UX, probe presentation, watch presentation, or runtime command surfaces.
It does own part of what makes later source-aligned observation and diagnostics possible:
</p>

<ul>
  <li>recoverable identity and mapping,</li>
  <li>attribution and correspondence carriers,</li>
  <li>stable execution-facing categories,</li>
  <li>a canonical open boundary that can be referred to before runtime-private realization begins.</li>
</ul>

<p>
In other words:
</p>

<pre><code>IDE/
   owns
how users inspect and interact

IR/
   owns part of
what makes source-aligned inspection and attribution possible</code></pre>

<hr/>

<h2 id="internal-document-structure">9. Internal Document Structure</h2>

<p>
The current directory structure is:
</p>

<pre><code>IR/
├── schema/
├── Backend contract.md
├── Construction rules.md
├── Derivation rules.md
├── Execution IR.md
├── Identity and Mapping.md
├── Lowering.md
├── Readme.md
└── Schema.md</code></pre>

<p>
This structure is intentionally split between:
</p>

<ul>
  <li>the core open-IR bundle, and</li>
  <li>the downstream IR-adjacent bundle.</li>
</ul>

<p>
The core open-IR bundle is:
</p>

<ul>
  <li><code>Execution IR.md</code></li>
  <li><code>Derivation rules.md</code></li>
  <li><code>Construction rules.md</code></li>
  <li><code>Identity and Mapping.md</code></li>
  <li><code>Schema.md</code></li>
  <li><code>schema/</code></li>
</ul>

<p>
The downstream IR-adjacent bundle is:
</p>

<ul>
  <li><code>Lowering.md</code></li>
  <li><code>Backend contract.md</code></li>
</ul>

<hr/>

<h2 id="document-ownership-split">10. Document Ownership Split</h2>

<p>
The ownership split inside <code>IR/</code> is:
</p>

<pre><code>Execution IR.md
   - canonical open execution-facing architecture

Derivation rules.md
   - normative derivation from validated meaning to canonical IR

Construction rules.md
   - material construction of conforming canonical IR payloads

Identity and Mapping.md
   - attribution, correspondence, and recoverability law

Schema.md
   - schema posture for canonical JSON IR

schema/
   - machine-checkable schema artifacts

Lowering.md
   - downstream specialization boundary

Backend contract.md
   - standardized consumer-facing handoff after lowering</code></pre>

<p>
This split matters because it prevents one giant document from blurring architectural responsibility.
</p>

<hr/>

<h2 id="ownership-quick-check">11. Ownership Quick Check</h2>

<p>
A fast ownership check is:
</p>

<pre><code>If the question is:
"What does the validated program mean?"
   -&gt; Language/

If the question is:
"What canonical open execution-facing representation exists?"
   -&gt; IR/Execution IR.md

If the question is:
"How does validated meaning become canonical IR?"
   -&gt; IR/Derivation rules.md

If the question is:
"How is conforming canonical IR materially built?"
   -&gt; IR/Construction rules.md

If the question is:
"How are attribution and recoverability preserved?"
   -&gt; IR/Identity and Mapping.md

If the question is:
"How is canonical JSON IR structurally validated?"
   -&gt; IR/Schema.md and IR/schema/

If the question is:
"How does open IR become target-oriented?"
   -&gt; IR/Lowering.md

If the question is:
"What may a downstream backend consumer rely on?"
   -&gt; IR/Backend contract.md</code></pre>

<hr/>

<h2 id="practical-reading-path">12. Practical Reading Path</h2>

<p>
A practical reading path for this directory is:
</p>

<pre><code>1. Read this README first
2. Read Execution IR.md
3. Read Derivation rules.md
4. Read Identity and Mapping.md
5. Read Construction rules.md
6. Read Schema.md
7. Inspect schema/
8. Read Lowering.md
9. Read Backend contract.md</code></pre>

<p>
That order follows the architectural corridor from validated meaning toward later downstream specialization.
</p>

<p>
A second practical path, when working from conformance or compiler-corridor questions, is:
</p>

<pre><code>Conformance case
   -&gt;
IR/Readme.md
   -&gt;
Derivation rules.md
   -&gt;
Identity and Mapping.md
   -&gt;
Schema.md
   -&gt;
Lowering.md
   -&gt;
Backend contract.md</code></pre>

<hr/>

<h2 id="status-in-v01">13. Status in v0.1</h2>

<p>
In the current published v0.1 posture, the IR layer is no longer only architectural prose.
It already defines a real corridor:
</p>

<ul>
  <li>validated program meaning,</li>
  <li>canonical Execution IR derivation,</li>
  <li>recoverable identity and mapping,</li>
  <li>material canonical IR construction,</li>
  <li>canonical JSON schema validation,</li>
  <li>later lowering and backend-facing handoff.</li>
</ul>

<p>
This means the repository is already beyond a purely aspirational architecture-only stage.
It already exposes the documents needed to reason about a serious compiler-oriented handoff, while keeping LLVM or any other compiler family strictly downstream from the language-owned IR layer.
</p>

<p>
The active closure direction in v0.1 is therefore not to invent a new IR concept, but to keep tightening:
</p>

<ul>
  <li>conformance alignment,</li>
  <li>identity and recoverability law,</li>
  <li>derivation correctness,</li>
  <li>schema posture,</li>
  <li>lowering and backend-contract discipline.</li>
</ul>

<hr/>

<h2 id="summary">14. Summary</h2>

<p>
<code>IR/</code> is the architectural home of canonical open execution-facing representation in FROG.
</p>

<p>
It begins after validated program meaning and remains upstream from lowering, backend-facing contract, and runtime-private realization.
</p>

<p>
Its core role is to ensure that execution-facing structure becomes:
</p>

<ul>
  <li>open,</li>
  <li>inspectable,</li>
  <li>attributable,</li>
  <li>recoverable,</li>
  <li>schema-checkable in canonical JSON form,</li>
  <li>ready for disciplined downstream specialization.</li>
</ul>

<p>
The internal split of the directory is intentional:
</p>

<ul>
  <li>the core open-IR bundle defines the canonical execution-facing layer itself,</li>
  <li>the downstream IR-adjacent documents define how later stages connect to that layer without replacing it.</li>
</ul>

<p>
That is the architectural purpose of <code>IR/</code> in FROG v0.1.
</p>
