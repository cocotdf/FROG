<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG IR Lowering</h1>

<p align="center">
  <strong>Normative lowering boundary and transformation rules for execution-facing IR in FROG v0.1</strong><br/>
  FROG — Free Open Graphical Language
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#reading-legend">2. Reading Legend</a></li>
  <li><a href="#why-this-document-exists">3. Why this Document Exists</a></li>
  <li><a href="#position-in-the-pipeline">4. Position in the Pipeline</a></li>
  <li><a href="#scope">5. Scope</a></li>
  <li><a href="#non-goals">6. Non-Goals</a></li>
  <li><a href="#what-lowering-means-in-frog">7. What "Lowering" Means in FROG</a></li>
  <li><a href="#lowering-boundary">8. Lowering Boundary</a></li>
  <li><a href="#minimum-preconditions">9. Minimum Preconditions</a></li>
  <li><a href="#lowering-stages">10. Lowering Stages</a></li>
  <li><a href="#core-invariants">11. Core Invariants</a></li>
  <li><a href="#required-preservation-obligations">12. Required Preservation Obligations</a></li>
  <li><a href="#allowed-lowering-transformations">13. Allowed Lowering Transformations</a></li>
  <li><a href="#forbidden-lowering-transformations">14. Forbidden Lowering Transformations</a></li>
  <li><a href="#control-structures-and-regions">15. Control Structures and Regions</a></li>
  <li><a href="#state-memory-and-feedback">16. State, Memory, and Feedback</a></li>
  <li><a href="#interfaces-ui-boundaries-and-object-interaction">17. Interfaces, UI Boundaries, and Object Interaction</a></li>
  <li><a href="#data-representation-storage-and-layout">18. Data Representation, Storage, and Layout</a></li>
  <li><a href="#scheduling-placement-and-partitioning">19. Scheduling, Placement, and Partitioning</a></li>
  <li><a href="#attribution-and-mapping-across-lowering">20. Attribution and Mapping Across Lowering</a></li>
  <li><a href="#relation-with-observation-debugging-and-diagnostics">21. Relation with Observation, Debugging, and Diagnostics</a></li>
  <li><a href="#conceptual-lowered-products">22. Conceptual Lowered Products</a></li>
  <li><a href="#minimal-conceptual-shape">23. Minimal Conceptual Shape</a></li>
  <li><a href="#examples">24. Examples</a></li>
  <li><a href="#out-of-scope-for-v01">25. Out of Scope for v0.1</a></li>
  <li><a href="#summary">26. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the normative architectural boundary called <strong>lowering</strong> in FROG v0.1.
</p>

<p>
Lowering begins after an open execution-facing IR has been derived and constructed from validated FROG program meaning.
Lowering exists to transform that open IR into more target-oriented, backend-oriented, or realization-oriented specialized forms without redefining:
</p>

<ul>
  <li>canonical source,</li>
  <li>language semantics,</li>
  <li>the open execution-facing role of the base IR,</li>
  <li>the architectural distinction between open representation and private realization.</li>
</ul>

<p>
In short:
</p>

<pre><code>validated meaning
      |
      v
open Execution IR
      |
      v
lowering
      |
      v
specialized derived form(s)
      |
      v
backend-facing contract and/or private realization
</code></pre>

<p>
This document does not standardize one universal compiler pipeline.
It defines what kind of transformation space belongs to lowering, what lowering MUST preserve, and what lowering MUST NOT silently erase.
</p>

<hr/>

<h2 id="reading-legend">2. Reading Legend</h2>

<ul>
  <li>🟦 <strong>Open specification-facing representation or layer</strong></li>
  <li>🟩 <strong>Semantic truth, attribution, or recoverability obligation</strong></li>
  <li>🟨 <strong>Boundary, mapping, or standardized handoff</strong></li>
  <li>🟧 <strong>Lowering / specialization / target adaptation zone</strong></li>
  <li>🟥 <strong>Implementation-private or runtime-private realization zone</strong></li>
</ul>

<hr/>

<h2 id="why-this-document-exists">3. Why this Document Exists</h2>

<p>
Without a dedicated lowering boundary, repositories tend to accumulate architectural confusion such as:
</p>

<ul>
  <li>treating the open IR as if it were already a target-specific graph,</li>
  <li>smuggling private scheduler decisions into the normative IR,</li>
  <li>flattening execution structure too early and losing source-faithful attribution,</li>
  <li>confusing backend contracts with lowering transformations,</li>
  <li>mixing portable execution structure with deployment-specific or ABI-specific details.</li>
</ul>

<p>
FROG deliberately keeps these layers separate.
</p>

<p>
This document therefore exists to answer one precise question:
</p>

<p>
<strong>What transformations are allowed when moving from open execution-facing IR toward target-specific execution preparation, while keeping the architecture sound?</strong>
</p>

<hr/>

<h2 id="position-in-the-pipeline">4. Position in the Pipeline</h2>

<p>
The relevant surrounding pipeline is:
</p>

<pre><code>.frog canonical source
        |
        v
Expression/
        |
        v
validated program meaning
        |
        v
open Execution IR
        |
        v
lowering
        |
        v
specialized derived forms
        |
        v
backend contract
        |
        v
private realization
</code></pre>

<p>
Key rule:
</p>

<ul>
  <li><strong>Execution IR</strong> = open, inspectable, source-attributable execution-facing representation</li>
  <li><strong>Lowering</strong> = specialization boundary</li>
  <li><strong>Backend contract</strong> = later explicit consumer-facing handoff</li>
  <li><strong>Runtime</strong> = private realization</li>
</ul>

<p>
Lowering therefore begins <strong>after</strong> open IR exists and remains <strong>before</strong> backend contract emission or runtime-private execution machinery.
</p>

<hr/>

<h2 id="scope">5. Scope</h2>

<p>
This document defines:
</p>

<ul>
  <li>the lowering boundary,</li>
  <li>the transformation categories that belong to lowering,</li>
  <li>the invariants that lowering MUST preserve,</li>
  <li>the classes of specialization that lowering MAY perform,</li>
  <li>the classes of transformation that lowering MUST NOT perform.</li>
</ul>

<p>
This document does not fully define:
</p>

<ul>
  <li>the open Execution IR object model in full,</li>
  <li>the backend contract in full,</li>
  <li>one mandatory target-specific lowered representation,</li>
  <li>one mandatory runtime representation,</li>
  <li>one mandatory compiler architecture.</li>
</ul>

<hr/>

<h2 id="non-goals">6. Non-Goals</h2>

<p>
This document does <strong>not</strong> define:
</p>

<ul>
  <li>one compiler architecture,</li>
  <li>one IR format after lowering,</li>
  <li>one scheduler model,</li>
  <li>one ABI,</li>
  <li>one runtime representation.</li>
</ul>

<p>
It also does not grant permission to treat backend-private choices as though they were language-level truth.
</p>

<hr/>

<h2 id="what-lowering-means-in-frog">7. What "Lowering" Means in FROG</h2>

<p>
In FROG, <strong>lowering</strong> means the transformation of open Execution IR into forms that are closer to execution realization while still remaining semantically faithful to the validated program.
</p>

<p>
Typical lowering goals include:
</p>

<ul>
  <li>data layout concretization,</li>
  <li>control flattening or control specialization,</li>
  <li>memory materialization,</li>
  <li>interface binding,</li>
  <li>execution planning,</li>
  <li>target-oriented partitioning,</li>
  <li>backend-oriented preparation.</li>
</ul>

<p>
Lowering is therefore not one specific pass.
It is the whole transformation corridor in which open execution-facing representation becomes more target-shaped and less source-shaped while remaining correct and recoverable where required.
</p>

<hr/>

<h2 id="lowering-boundary">8. Lowering Boundary</h2>

<pre><code>OPEN ZONE
---------
Execution IR
  - structured
  - attributable
  - portable
  - specification-facing

LOWERING
---------
specialization begins

SPECIALIZED ZONE
----------------
lowered forms
  - target-oriented
  - less source-shaped
  - possibly backend-specific
  - still constrained by semantic faithfulness
</code></pre>

<p>
The critical architectural rule is:
</p>

<ul>
  <li>the open IR remains the last fully open execution-facing representation,</li>
  <li>lowering is where irreversible target-oriented specialization may begin,</li>
  <li>backend contract is later than lowering,</li>
  <li>runtime-private realization is later than both.</li>
</ul>

<hr/>

<h2 id="minimum-preconditions">9. Minimum Preconditions</h2>

<p>
Lowering requires a fully validated program and a conforming open Execution IR.
</p>

<p>
Lowering MUST NOT:
</p>

<ul>
  <li>fix invalid graphs,</li>
  <li>inject hidden semantics,</li>
  <li>legalize invalid cycles,</li>
  <li>resolve semantic ambiguity that should already have been resolved before or at the open-IR boundary.</li>
</ul>

<p>
Preconditions therefore include:
</p>

<ul>
  <li>validated program meaning already exists,</li>
  <li>the open Execution IR is already semantically grounded,</li>
  <li>required attribution and recoverability are already established at the open boundary.</li>
</ul>

<hr/>

<h2 id="lowering-stages">10. Lowering Stages</h2>

<h3>10.1 Stage A — IR-conservative lowering</h3>

<p>
This stage remains relatively close to the open Execution IR.
It may:
</p>

<ul>
  <li>make execution planning more explicit,</li>
  <li>prepare target-facing forms,</li>
  <li>refine memory, control, or boundary structure,</li>
  <li>add backend-relevant support records,</li>
  <li>remain substantially inspectable against open-IR structure.</li>
</ul>

<h3>10.2 Stage B — backend-oriented lowering</h3>

<p>
This stage performs stronger specialization.
It may include:
</p>

<ul>
  <li>layout concretization,</li>
  <li>scheduler-oriented preparation,</li>
  <li>placement and partitioning,</li>
  <li>ABI-facing interface adaptation,</li>
  <li>target-specific control expansion or state-cell realization.</li>
</ul>

<h3>10.3 Stage C — runtime-private realization</h3>

<p>
This stage is downstream from the normative lowering boundary as such.
It may include:
</p>

<ul>
  <li>private scheduler graphs,</li>
  <li>compiled artifacts,</li>
  <li>runtime-internal state layouts,</li>
  <li>private handles and activation machinery.</li>
</ul>

<p>
Stage C is mentioned here only to make the boundary explicit:
it is <strong>later than lowering as a normative architectural boundary</strong>,
not a redefinition of lowering itself.
</p>

<hr/>

<h2 id="core-invariants">11. Core Invariants</h2>

<p>
All lowering in base v0.1 MUST preserve the following invariants:
</p>

<ul>
  <li>semantic equivalence MUST hold,</li>
  <li>attribution MUST remain recoverable where later layers still require it,</li>
  <li>explicit memory MUST remain semantically explicit,</li>
  <li>required boundaries MUST remain distinguishable or recoverable,</li>
  <li>validated dependency meaning MUST be preserved,</li>
  <li>lowering MUST NOT silently convert optional implementation convenience into normative meaning.</li>
</ul>

<hr/>

<h2 id="required-preservation-obligations">12. Required Preservation Obligations</h2>

<p>
Lowering MUST preserve:
</p>

<ul>
  <li>dependency semantics,</li>
  <li>control semantics,</li>
  <li>state semantics,</li>
  <li>boundary roles,</li>
  <li>source attribution,</li>
  <li>recoverability of the minimal distinction surface required by open IR and downstream diagnostics.</li>
</ul>

<p>
No semantic laundering is allowed.
</p>

<p>
In particular, lowering MUST preserve, where relevant:
</p>

<ul>
  <li>public interface participation versus UI participation,</li>
  <li><code>widget_value</code> participation versus <code>widget_reference</code> participation,</li>
  <li>standardized UI-object primitive operation versus widget-reference participation,</li>
  <li>explicit structure ownership and region relation,</li>
  <li>explicit local memory as the basis of valid feedback.</li>
</ul>

<hr/>

<h2 id="allowed-lowering-transformations">13. Allowed Lowering Transformations</h2>

<p>
The following lowering classes are allowed when semantic faithfulness and required recoverability are preserved:
</p>

<ul>
  <li>structure → lower control machinery,</li>
  <li>interface → ABI-facing or platform-facing binding preparation,</li>
  <li>memory → buffers, cells, registers, or equivalent target-facing storage forms,</li>
  <li>partitioning → threads, devices, domains, or target regions,</li>
  <li>scheduling → ordering, clustering, or planning forms,</li>
  <li>data representation refinement → concrete layout, width, alignment, or storage policy,</li>
  <li>support-object generation for backend preparation,</li>
  <li>target-profile-aware specialization when it remains downstream from open semantic truth.</li>
</ul>

<p>
Allowed does not mean unrestricted.
Each transformation remains subject to the preservation obligations of this document.
</p>

<hr/>

<h2 id="forbidden-lowering-transformations">14. Forbidden Lowering Transformations</h2>

<p>
The following are forbidden:
</p>

<ul>
  <li>semantic change,</li>
  <li>hidden state insertion that changes the meaning of valid versus invalid feedback,</li>
  <li>boundary collapse that destroys required distinction recoverability,</li>
  <li>loss of attribution where later layers still require diagnosability or mapping,</li>
  <li>invalid program repair disguised as lowering,</li>
  <li>promotion of editor-only presentation information into execution meaning,</li>
  <li>presenting one backend-private form as though it were normative FROG IR truth.</li>
</ul>

<hr/>

<h2 id="control-structures-and-regions">15. Control Structures and Regions</h2>

<p>
Lowering MAY transform explicit structured execution into more target-oriented control machinery.
However:
</p>

<ul>
  <li>validated control meaning MUST be preserved,</li>
  <li>structure-family meaning MUST remain recoverable where later layers still require it,</li>
  <li>region ownership and region relation MUST not be destroyed prematurely when later attribution or debugging still depends on them,</li>
  <li>boundary-terminal roles MUST not be silently erased where they remain required for faithful mapping.</li>
</ul>

<p>
Allowed examples include:
</p>

<ul>
  <li><code>case</code> to backend-oriented branch preparation,</li>
  <li><code>for_loop</code> to counted loop machinery,</li>
  <li><code>while_loop</code> to continuation-governed loop machinery.</li>
</ul>

<p>
Forbidden examples include:
</p>

<ul>
  <li>flattening that destroys all recoverable relation to structure family,</li>
  <li>cross-region or cross-boundary rewrites that blur validated region ownership,</li>
  <li>turning structured control into opaque backend-private machinery while still claiming open diagnosability.</li>
</ul>

<hr/>

<h2 id="state-memory-and-feedback">16. State, Memory, and Feedback</h2>

<p>
Lowering MAY materialize memory into target-facing storage forms.
However:
</p>

<ul>
  <li>explicit state semantics MUST be preserved,</li>
  <li>required explicit initialization MUST remain recoverable where relevant,</li>
  <li>valid feedback MUST remain grounded in explicit memory already present in validated meaning,</li>
  <li>lowering MUST NOT legalize an otherwise invalid feedback path by injecting hidden state as though it had source-level legitimacy.</li>
</ul>

<p>
Allowed examples include:
</p>

<ul>
  <li>delay state to a storage cell,</li>
  <li>delay initialization to an explicit initialization record,</li>
  <li>state placement into target-specific storage classes.</li>
</ul>

<p>
Forbidden examples include:
</p>

<ul>
  <li>inventing hidden buffering to rescue an invalid cycle,</li>
  <li>erasing the distinction between explicit memory and ordinary transient dataflow,</li>
  <li>destroying the source-attributable identity of state-bearing execution content when later mapping still depends on it.</li>
</ul>

<hr/>

<h2 id="interfaces-ui-boundaries-and-object-interaction">17. Interfaces, UI Boundaries, and Object Interaction</h2>

<p>
Lowering MAY bind interfaces and UI-related execution content into backend-facing or runtime-facing forms.
However, the following distinctions MUST remain preserved or recoverable where relevant:
</p>

<ul>
  <li>public interface participation versus UI participation,</li>
  <li><code>widget_value</code> versus <code>widget_reference</code>,</li>
  <li><code>widget_reference</code> participation versus standardized UI-object primitive operation,</li>
  <li>ordinary valueflow versus object-style UI interaction.</li>
</ul>

<p>
Allowed examples include:
</p>

<ul>
  <li>public interface to ABI-facing parameter or endpoint forms,</li>
  <li>widget-value channels to host-binding forms,</li>
  <li>UI-object primitives to explicit host interaction calls or message forms.</li>
</ul>

<p>
Forbidden examples include:
</p>

<ul>
  <li>collapsing all boundaries into one generic endpoint class,</li>
  <li>rewriting <code>widget_value</code> into indistinguishable property access on member <code>value</code>,</li>
  <li>absorbing standardized UI-object primitives into widget-reference identity so completely that the operation itself is no longer recoverable.</li>
</ul>

<hr/>

<h2 id="data-representation-storage-and-layout">18. Data Representation, Storage, and Layout</h2>

<p>
Lowering MAY refine data representation for target suitability.
This includes:
</p>

<ul>
  <li>storage class selection,</li>
  <li>layout concretization,</li>
  <li>buffer planning,</li>
  <li>alignment and width refinement where already justified by validated type commitments,</li>
  <li>placement of values into backend-oriented storage forms.</li>
</ul>

<p>
Such transformations MUST remain downstream from semantic type commitments already established before lowering.
They MUST NOT invent new meaning.
They MUST NOT rewrite type obligations in ways that change validated language truth.
</p>

<hr/>

<h2 id="scheduling-placement-and-partitioning">19. Scheduling, Placement, and Partitioning</h2>

<p>
Lowering MAY prepare execution through:
</p>

<ul>
  <li>scheduling,</li>
  <li>placement,</li>
  <li>partitioning,</li>
  <li>clustering,</li>
  <li>thread, device, or region assignment.</li>
</ul>

<p>
These are legitimate lowering concerns because they adapt open execution-facing structure toward realization.
However:
</p>

<ul>
  <li>validated dependency meaning MUST remain authoritative,</li>
  <li>placement MUST NOT be treated as semantic truth,</li>
  <li>partitioning MUST NOT erase recoverable attribution where later layers still require it,</li>
  <li>one scheduler policy MUST NOT be presented as though it were the normative meaning of FROG.</li>
</ul>

<hr/>

<h2 id="attribution-and-mapping-across-lowering">20. Attribution and Mapping Across Lowering</h2>

<p>
Lowering commonly expands objects:
</p>

<pre><code>open IR object
   ->
multiple lowered objects
</code></pre>

<p>
When this happens, lowering MUST preserve enough mapping information to recover:
</p>

<ul>
  <li>the origin open-IR object or objects,</li>
  <li>the validated semantic origin,</li>
  <li>the transformation relation where relevant,</li>
  <li>whether a lowered object is primary, support-derived, split-derived, or generated for backend preparation.</li>
</ul>

<p>
A conforming implementation MAY choose its own encoding of lowered mapping records.
What matters is that required diagnosability, conformance reasoning, and source-aligned attribution do not disappear silently.
</p>

<hr/>

<h2 id="relation-with-observation-debugging-and-diagnostics">21. Relation with Observation, Debugging, and Diagnostics</h2>

<p>
Lowering MUST remain compatible with:
</p>

<ul>
  <li>source-level debugging,</li>
  <li>traceability,</li>
  <li>fault attribution,</li>
  <li>recoverable mapping from specialized forms back to open-IR and source-facing concepts where later tooling still depends on it.</li>
</ul>

<p>
Rule:
</p>

<pre><code>internal complexity allowed
loss of diagnosability forbidden
</code></pre>

<p>
This does not mean every lowered form must remain as readable as the open IR.
It means that lowering MUST not destroy the mapping surface required for trustworthy later tooling and diagnostics.
</p>

<hr/>

<h2 id="conceptual-lowered-products">22. Conceptual Lowered Products</h2>

<p>
Conceptual lowered products may include:
</p>

<ul>
  <li>control form,</li>
  <li>state form,</li>
  <li>interface form,</li>
  <li>storage form,</li>
  <li>placement form,</li>
  <li>schedule form,</li>
  <li>backend-preparation form,</li>
  <li>consumer-facing contract-preparation form.</li>
</ul>

<p>
These are conceptual product classes, not one mandatory taxonomy for every implementation.
</p>

<hr/>

<h2 id="minimal-conceptual-shape">23. Minimal Conceptual Shape</h2>

<p>
This document does not define one mandatory lowered wire format.
However, a lowered form SHOULD be representable in a broadly equivalent conceptual shape such as:
</p>

<pre><code>{
  "kind": "lowered_form",
  "target_family": "...",
  "objects": [],
  "connections": [],
  "mapping": {}
}
</code></pre>

<p>
The example above is illustrative only.
What matters is that a lowered form remains:
</p>

<ul>
  <li>target-oriented,</li>
  <li>semantically faithful,</li>
  <li>mapping-compatible where required,</li>
  <li>distinguishable from both open Execution IR and backend contract.</li>
</ul>

<hr/>

<h2 id="examples">24. Examples</h2>

<h3>24.1 Structured control lowering</h3>

<pre><code>structured execution object
    ->
backend-oriented branch / loop preparation
with preserved control semantics
</code></pre>

<h3>24.2 State lowering</h3>

<pre><code>explicit delay object
    ->
state cell + initialization form
with preserved explicit state semantics
</code></pre>

<h3>24.3 Interface lowering</h3>

<pre><code>public interface boundary object
    ->
ABI-facing or endpoint-facing lowered boundary form
with preserved public boundary role
</code></pre>

<h3>24.4 Partitioning</h3>

<pre><code>open IR graph
    ->
device / thread / domain partitioned lowered graph
with preserved dependency meaning
</code></pre>

<h3>24.5 Forbidden example</h3>

<pre><code>invalid feedback path
    ->
hidden injected storage
    ->
"valid" lowered form
</code></pre>

<p>
This is forbidden because lowering is not allowed to repair invalid meaning by inventing hidden semantics.
</p>

<hr/>

<h2 id="out-of-scope-for-v01">25. Out of Scope for v0.1</h2>

<ul>
  <li>one universal IR after lowering,</li>
  <li>one runtime model,</li>
  <li>one scheduler,</li>
  <li>one ABI,</li>
  <li>one mandatory multi-stage compiler architecture,</li>
  <li>one mandatory target-family taxonomy,</li>
  <li>one universal deployment representation.</li>
</ul>

<p>
Those concerns remain implementation-specific or belong to later, more specialized specification surfaces.
</p>

<hr/>

<h2 id="summary">26. Summary</h2>

<p>
Lowering is the specialization boundary after open Execution IR.
</p>

<p>
It:
</p>

<ul>
  <li>adapts IR for execution,</li>
  <li>preserves semantic truth,</li>
  <li>preserves attribution and required recoverability,</li>
  <li>does not redefine the language,</li>
  <li>does not collapse open IR into private realization by normative shortcut.</li>
</ul>

<pre><code>open Execution IR
        |
        v
lowering
        |
        v
specialized execution forms
        |
        v
backend contract / private realization
</code></pre>
