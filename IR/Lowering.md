<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG IR Lowering</h1>

<p align="center">
  Normative lowering boundary and transformation rules for execution-facing IR in FROG v0.1<br/>
  <em>FROG — Free Open Graphical Language</em>
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
  <li><a href="#lowering-stages">10. Lowering Stages</a>
    <ul>
      <li><a href="#stage-a-ir-conservative-lowering">10.1 Stage A — IR-conservative lowering</a></li>
      <li><a href="#stage-b-backend-oriented-lowering">10.2 Stage B — backend-oriented lowering</a></li>
      <li><a href="#stage-c-runtime-private-realization">10.3 Stage C — runtime-private realization</a></li>
    </ul>
  </li>
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
Lowering begins <strong>after</strong> an open execution-facing IR has been derived and constructed from validated FROG program meaning.
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
Execution IR
        |
        v
Lowering
        |
        v
backend-oriented derived forms
        |
        +------&gt; backend contract
        |
        +------&gt; compiler / backend / runtime realization
</code></pre>

<p>
The key interpretation rule is:
</p>

<ul>
  <li><strong>Execution IR</strong> is still open, inspectable, and specification-facing.</li>
  <li><strong>Lowering</strong> is where specialization begins.</li>
  <li><strong>Backend contract</strong> is a later standardized consumer-facing boundary, not the definition of lowering itself.</li>
  <li><strong>Runtime-private realization</strong> is later and is not standardized here.</li>
</ul>

<hr/>

<h2 id="scope">5. Scope</h2>

<p>
This document defines:
</p>

<ul>
  <li>what lowering is in FROG,</li>
  <li>where lowering begins,</li>
  <li>which transformation categories belong to lowering,</li>
  <li>which preservation obligations continue to apply during lowering,</li>
  <li>which architectural distinctions lowering is allowed to specialize,</li>
  <li>which transformations are forbidden even after lowering has begun.</li>
</ul>

<p>
This document therefore owns the <strong>specialization boundary</strong>, not the full downstream consumption contract and not the full private runtime realization.
</p>

<hr/>

<h2 id="non-goals">6. Non-Goals</h2>

<p>
This document does not define:
</p>

<ul>
  <li>one mandatory lowered graph format,</li>
  <li>one mandatory SSA form,</li>
  <li>one mandatory control-flow graph shape,</li>
  <li>one mandatory scheduler model,</li>
  <li>one mandatory ABI,</li>
  <li>one mandatory code generation pipeline,</li>
  <li>one mandatory transport format for lowered artifacts,</li>
  <li>one mandatory runtime-private object graph.</li>
</ul>

<p>
Those topics may be constrained later by backend-family specifications, profile-specific runtime contracts, or the backend contract boundary.
</p>

<p>
This document also does not redefine the ownership of:
</p>

<ul>
  <li><code>Execution IR.md</code> for the base open IR model,</li>
  <li><code>Identity and Mapping.md</code> for cross-layer recoverability rules,</li>
  <li><code>Backend contract.md</code> for the standardized consumer-facing handoff.</li>
</ul>

<hr/>

<h2 id="what-lowering-means-in-frog">7. What "Lowering" Means in FROG</h2>

<p>
In FROG, <strong>lowering</strong> means the family of transformations that take an open execution-facing IR and make it more directly consumable by one or more backend families, runtime families, or target families.
</p>

<p>
Typical reasons to lower include:
</p>

<ul>
  <li>making target data layout explicit,</li>
  <li>making storage classes explicit,</li>
  <li>resolving calling conventions,</li>
  <li>splitting or flattening structured control into lower-level executable patterns,</li>
  <li>introducing scheduling constraints, work partitions, or placement constraints,</li>
  <li>specializing memory ownership and buffer movement,</li>
  <li>binding interface boundaries to target-specific ingress/egress forms,</li>
  <li>preparing execution for compilation, interpretation, deployment, or hybrid realization.</li>
</ul>

<p>
Lowering therefore belongs to the zone where <strong>portable execution-facing meaning starts being specialized for realization</strong>.
</p>

<pre><code>🟦 open execution-facing IR
        |
        v
🟧 specialization for target consumption
        |
        v
🟨 possible standardized consumer-facing handoff
        |
        v
🟥 private realization
</code></pre>

<hr/>

<h2 id="lowering-boundary">8. Lowering Boundary</h2>

<p>
The lowering boundary is the first architectural point at which an implementation MAY introduce target-oriented specialization that is not required to remain the primary open representation of the program.
</p>

<p>
This boundary can be visualized as:
</p>

<pre><code>OPEN REPRESENTATION ZONE
------------------------
validated meaning
      |
      v
Execution IR
  - open
  - inspectable
  - source-attributable
  - structured
  - not backend-private

LOWERING BOUNDARY
-----------------
specialization begins

SPECIALIZED REPRESENTATION ZONE
-------------------------------
lowered forms
  - backend-oriented
  - may be less source-shaped
  - may be more explicit about layout / schedule / storage
  - may be backend-family-specific
  - may remain partly open or become implementation-private later
</code></pre>

<p>
A conforming implementation MAY expose some lowered forms for inspection.
However, exposure does not make those forms the normative definition of FROG execution meaning.
</p>

<p>
A lowered form also does not automatically become the backend contract.
Lowering produces specialized forms; a backend contract is a later explicit statement of what a downstream consumer may rely on.
</p>

<hr/>

<h2 id="minimum-preconditions">9. Minimum Preconditions</h2>

<p>
Lowering begins only after all applicable validation required for Execution IR construction has already succeeded.
</p>

<p>
At minimum, lowering presupposes:
</p>

<ul>
  <li>structural validity,</li>
  <li>type validity,</li>
  <li>primitive and structure-family validity,</li>
  <li>cycle validity,</li>
  <li>profile applicability validity where relevant,</li>
  <li>construction of a semantically valid execution-facing basis.</li>
</ul>

<p>
An implementation MUST NOT use lowering as a hidden repair step for an invalid program.
</p>

<p>
In particular, lowering MUST NOT:
</p>

<ul>
  <li>legalize an invalid cycle by secretly inserting memory,</li>
  <li>repair invalid structure ownership while pretending the source was already semantically valid,</li>
  <li>erase an invalid distinction by collapsing it into an opaque target artifact.</li>
</ul>

<pre><code>No valid open execution-facing basis
        |
        v
No conforming lowering claim
</code></pre>

<hr/>

<h2 id="lowering-stages">10. Lowering Stages</h2>

<p>
FROG does not require one fixed number of lowering stages.
However, it is useful to distinguish three architectural zones.
</p>

<h3 id="stage-a-ir-conservative-lowering">10.1 Stage A — IR-conservative lowering</h3>

<p>
This stage remains close to the open Execution IR but begins preparing target-oriented specialization.
</p>

<p>
Examples:
</p>

<ul>
  <li>materializing explicit storage classes,</li>
  <li>making calling or transfer boundaries explicit,</li>
  <li>classifying execution domains,</li>
  <li>splitting one structure into multiple lower control objects while preserving full mapping,</li>
  <li>resolving canonical interface categories into backend-family interface classes.</li>
</ul>

<p>
This stage SHOULD remain highly attributable and relatively easy to inspect.
</p>

<h3 id="stage-b-backend-oriented-lowering">10.2 Stage B — backend-oriented lowering</h3>

<p>
This stage specializes the program for a backend family, target family, or runtime family.
</p>

<p>
Examples:
</p>

<ul>
  <li>turning structured selection into backend branch form, predication form, or dispatch form,</li>
  <li>turning loop structures into explicit iterative state machines or backend loop bodies,</li>
  <li>binding ports to ABI-level argument and result conventions,</li>
  <li>introducing target storage regions, buffers, queues, or channels,</li>
  <li>partitioning work across threads, devices, or execution domains,</li>
  <li>specializing data representation for target layout constraints.</li>
</ul>

<p>
At this stage, the representation MAY be less source-shaped.
However, semantic faithfulness and required recoverability obligations still apply.
</p>

<h3 id="stage-c-runtime-private-realization">10.3 Stage C — runtime-private realization</h3>

<p>
This stage is beyond the normative ownership of this document.
</p>

<p>
Examples:
</p>

<ul>
  <li>private scheduler graphs,</li>
  <li>private bytecode plans,</li>
  <li>private executable bundles,</li>
  <li>runtime allocator internals,</li>
  <li>private event queues,</li>
  <li>private JIT data structures.</li>
</ul>

<p>
This document constrains what Stage C MUST remain able to respect, but it does not standardize Stage C itself.
</p>

<pre><code>Stage A  -&gt; still close to open IR
Stage B  -&gt; specialized for backend family
Stage C  -&gt; runtime-private realization
</code></pre>

<hr/>

<h2 id="core-invariants">11. Core Invariants</h2>

<p>
All lowering stages in FROG v0.1 MUST respect the following invariants:
</p>

<ul>
  <li>Lowering MUST remain semantically faithful to validated program meaning.</li>
  <li>Lowering MUST NOT redefine language behavior.</li>
  <li>Lowering MUST NOT pretend that one private runtime form is the normative FROG execution model.</li>
  <li>Lowering MUST preserve enough attribution for diagnostics, inspection, and source-aligned execution reasoning.</li>
  <li>Lowering MUST preserve explicit memory semantics as explicit semantic fact, even if storage realization changes later.</li>
  <li>Lowering MUST preserve the distinction between open IR, lowered form, backend contract, and private realization.</li>
</ul>

<pre><code>Core lowering invariants

🟩 semantic faithfulness
🟩 attribution preservation
🟩 explicit memory remains semantically explicit
🟨 open IR / lowered form / backend contract remain distinct
🟥 one private runtime form is not the FROG standard
</code></pre>

<hr/>

<h2 id="required-preservation-obligations">12. Required Preservation Obligations</h2>

<p>
The following obligations remain in force through lowering.
</p>

<h3>12.1 Semantic preservation</h3>

<p>
A lowered form MUST remain semantically equivalent to the validated program meaning under the relevant backend assumptions.
</p>

<p>
Equivalence here means:
</p>

<ul>
  <li>dependency meaning remains coherent,</li>
  <li>boundary meaning remains coherent,</li>
  <li>state semantics remain coherent,</li>
  <li>control semantics remain coherent,</li>
  <li>fault-relevant or observation-relevant source attribution remains supportable where required.</li>
</ul>

<h3>12.2 Attribution preservation</h3>

<p>
Lowering MAY introduce many more target-oriented objects than the open IR.
However, a lowered representation MUST remain able to answer:
</p>

<ul>
  <li>which source-visible meaning this object came from,</li>
  <li>whether it is preserved, expanded, merged, or generated as support for realization,</li>
  <li>which semantically relevant distinctions were retained, encoded, or displaced.</li>
</ul>

<h3>12.3 No semantic laundering</h3>

<p>
Lowering MUST NOT hide a semantic change behind an implementation detail.
</p>

<p>
For example, an implementation MUST NOT:
</p>

<ul>
  <li>erase explicit local memory and claim equivalence,</li>
  <li>replace interface boundaries with untyped generic channels and claim no meaning was lost,</li>
  <li>silently swap structured semantics for a non-equivalent control interpretation.</li>
</ul>

<hr/>

<h2 id="allowed-lowering-transformations">13. Allowed Lowering Transformations</h2>

<p>
The following transformation families are allowed during lowering, provided all applicable invariants remain satisfied.
</p>

<h3>13.1 Structure-to-lower-control transformation</h3>

<p>
A lowering pipeline MAY transform:
</p>

<ul>
  <li>a <code>case</code> structure into a lower branch form, dispatch form, or predicated form,</li>
  <li>a <code>for_loop</code> structure into a lower iterative machine, explicit iteration state, or backend loop body,</li>
  <li>a <code>while_loop</code> structure into a lower loop guard / loop body / loop-carried state form.</li>
</ul>

<p>
However, the originating structure family, region semantics, and relevant mapping relations MUST remain recoverable where needed.
</p>

<h3 id="boundary-specialization">13.2 Boundary specialization</h3>

<p>
A lowering pipeline MAY specialize:
</p>

<ul>
  <li>public interface boundaries into ABI-level input/output contracts,</li>
  <li>UI object interaction into backend-specific call or dispatch mechanisms,</li>
  <li>sub-FROG invocation boundaries into explicit call, inline, or dispatch forms.</li>
</ul>

<h3 id="storage-and-layout-specialization">13.3 Storage and layout specialization</h3>

<p>
A lowering pipeline MAY:
</p>

<ul>
  <li>choose storage classes,</li>
  <li>materialize buffers,</li>
  <li>specialize memory layout,</li>
  <li>make transfer points explicit,</li>
  <li>introduce ownership and lifetime-support objects.</li>
</ul>

<h3 id="execution-domain-specialization">13.4 Execution-domain specialization</h3>

<p>
A lowering pipeline MAY:
</p>

<ul>
  <li>assign work to execution domains,</li>
  <li>introduce partition boundaries,</li>
  <li>annotate or realize device placement,</li>
  <li>introduce synchronization or transfer support objects.</li>
</ul>

<h3 id="scheduling-preparation">13.5 Scheduling preparation</h3>

<p>
A lowering pipeline MAY:
</p>

<ul>
  <li>compute scheduling constraints,</li>
  <li>materialize work ordering that is valid for a backend family,</li>
  <li>derive run queues, work packets, or execution clusters,</li>
  <li>prepare static schedules where the backend model requires them.</li>
</ul>

<p>
Such preparation belongs to lowering only when it remains clear that:
</p>

<ul>
  <li>the schedule is a realization aid,</li>
  <li>the schedule is not the normative meaning of FROG itself.</li>
</ul>

<hr/>

<h2 id="forbidden-lowering-transformations">14. Forbidden Lowering Transformations</h2>

<p>
The following transformations are forbidden in v0.1:
</p>

<ul>
  <li>changing validated language-level behavior,</li>
  <li>using lowering as hidden semantic repair for an invalid program,</li>
  <li>erasing source-attributable meaning so aggressively that diagnostics and source-aligned reasoning become impossible,</li>
  <li>removing the fact that explicit local memory was semantically required,</li>
  <li>introducing hidden implicit memory to legalize an invalid feedback path,</li>
  <li>collapsing all boundary families into one untyped transport model with no recoverable distinction,</li>
  <li>claiming one backend-private schedule, work graph, or runtime queue graph is the open FROG standard,</li>
  <li>smuggling editor-only presentation state into target execution semantics,</li>
  <li>making conformance depend on one private compiler pipeline shape.</li>
</ul>

<pre><code>Forbidden lowering outcomes

🟥 semantic drift
🟥 hidden semantic repair
🟥 attribution collapse
🟥 hidden implicit memory legalization
🟥 collapsed boundary-family distinctions
🟥 backend-private schedule presented as language truth
🟥 editor-only presentation semantics
</code></pre>

<hr/>

<h2 id="control-structures-and-regions">15. Control Structures and Regions</h2>

<p>
The open Execution IR keeps structured control explicit.
Lowering is the first stage where a toolchain MAY transform that structured form into lower-level control representation.
</p>

<p>
This can be pictured as:
</p>

<pre><code>open Execution IR
-----------------
structure[case]
  ├─ region[true]
  └─ region[false]

possible lowered form
---------------------
branch_test
  ├─ lowered_path[true]
  └─ lowered_path[false]
join_point
</code></pre>

<p>
Or:
</p>

<pre><code>open Execution IR
-----------------
structure[for_loop]
  ├─ init boundary
  ├─ iteration region
  └─ completion boundary

possible lowered form
---------------------
loop_state_init
loop_guard
loop_body
loop_carried_state_update
loop_exit
</code></pre>

<p>
Such transformations are allowed only when:
</p>

<ul>
  <li>the original structure family remains recoverable where needed,</li>
  <li>region-origin information remains recoverable where needed,</li>
  <li>loop-carried and branch-related semantic obligations remain correct,</li>
  <li>lowering does not claim that the lower form replaces the language-level definition of the structure.</li>
</ul>

<hr/>

<h2 id="state-memory-and-feedback">16. State, Memory, and Feedback</h2>

<p>
Explicit local memory is one of the most important preservation boundaries in FROG.
</p>

<p>
The architectural rule is:
</p>

<pre><code>validated stateful feedback
        requires
explicit local memory

therefore

lowering MAY change representation
lowering MUST NOT erase semantic memory identity
</code></pre>

<p>
Examples of allowed behavior:
</p>

<ul>
  <li>mapping <code>frog.core.delay</code> to a target register, buffer slot, state cell, retained object, or loop-carried state mechanism,</li>
  <li>making initialization and update phases explicit,</li>
  <li>separating read-state and commit-state support operations in a lowered form.</li>
</ul>

<p>
Examples of forbidden behavior:
</p>

<ul>
  <li>pretending that a valid delayed feedback path was actually stateless,</li>
  <li>legalizing an invalid combinational cycle by inserting hidden backend state without semantic attribution,</li>
  <li>removing recoverable correspondence between explicit source memory and lowered state realization.</li>
</ul>

<p>
A useful sketch is:
</p>

<pre><code>validated source-aligned meaning
--------------------------------
       +-------------------------+
       |                         |
       v                         |
[frog.core.delay] --&gt; [add] --&gt; next

possible lowered realization shape
----------------------------------
[state_read] --&gt; [add] --&gt; [state_write_commit]

required truth
--------------
state_read / state_write_commit
    implement
explicit local memory
    rather than replacing it semantically
</code></pre>

<hr/>

<h2 id="interfaces-ui-boundaries-and-object-interaction">17. Interfaces, UI Boundaries, and Object Interaction</h2>

<p>
Lowering MAY specialize boundary families, but it MUST do so carefully.
</p>

<h3>17.1 Public interface boundaries</h3>

<p>
A lowering pipeline MAY transform <code>interface_input</code> and <code>interface_output</code> into:
</p>

<ul>
  <li>ABI arguments and results,</li>
  <li>call-frame entries,</li>
  <li>stream endpoints,</li>
  <li>device I/O bindings,</li>
  <li>transport endpoints.</li>
</ul>

<p>
However, the lowered representation MUST remain able to preserve the fact that those were public program boundaries, not arbitrary internal edges.
</p>

<h3>17.2 Front-panel value participation</h3>

<p>
A lowering pipeline MAY bind <code>widget_value</code> participation to host-side bindings, UI synchronization points, or runtime-accessible value channels.
</p>

<p>
But it MUST NOT silently collapse widget-value participation into public interface participation if the distinction is semantically or observationally relevant.
</p>

<h3>17.3 Object-style widget interaction</h3>

<p>
A lowering pipeline MAY transform <code>widget_reference</code>-based object interaction and <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, or <code>frog.ui.method_invoke</code> into backend-specific call or dispatch mechanisms.
</p>

<p>
However, it MUST remain recoverable that the original meaning involved object-style UI interaction rather than plain valueflow.
</p>

<hr/>

<h2 id="data-representation-storage-and-layout">18. Data Representation, Storage, and Layout</h2>

<p>
Lowering is the appropriate place to introduce representation details that are too target-oriented for the open Execution IR.
</p>

<p>
Examples include:
</p>

<ul>
  <li>bit width expansion or concretization,</li>
  <li>packing and unpacking strategy,</li>
  <li>alignment and padding strategy,</li>
  <li>buffer materialization,</li>
  <li>copy vs reference transport decisions,</li>
  <li>host/device transfer points,</li>
  <li>temporary storage classes,</li>
  <li>lifetime-support objects.</li>
</ul>

<p>
These belong to lowering because they prepare realization.
They do not belong in the base open Execution IR because they are not part of the primary open execution-facing abstraction.
</p>

<p>
Nevertheless:
</p>

<ul>
  <li>layout decisions MUST remain semantically compatible with validated types and behavior,</li>
  <li>copy/reference decisions MUST NOT silently change observable semantics,</li>
  <li>storage lowering MUST remain consistent with the identity and attribution obligations of the IR layer.</li>
</ul>

<hr/>

<h2 id="scheduling-placement-and-partitioning">19. Scheduling, Placement, and Partitioning</h2>

<p>
Lowering is also the right boundary for introducing target-oriented execution planning.
</p>

<p>
Examples include:
</p>

<ul>
  <li>topological work ordering,</li>
  <li>work clustering,</li>
  <li>thread assignment,</li>
  <li>device assignment,</li>
  <li>deterministic static scheduling for a constrained backend,</li>
  <li>partitioning across execution domains.</li>
</ul>

<p>
However, the following distinction MUST remain clear:
</p>

<pre><code>language meaning
    != one schedule

open Execution IR
    != one schedule

lowered backend-oriented form
    MAY contain schedule-oriented decisions

runtime-private graph
    MAY contain even more schedule detail
</code></pre>

<p>
A schedule is therefore a realization strategy, not the language-level truth of the program.
</p>

<hr/>

<h2 id="attribution-and-mapping-across-lowering">20. Attribution and Mapping Across Lowering</h2>

<p>
Lowering MAY be highly expansive.
One source-visible or open-IR object may produce many lowered objects.
</p>

<p>
The general mapping model remains:
</p>

<pre><code>source-visible object(s)
        |
        v
validated executable meaning
        |
        v
open IR object(s)
        |
        v
lowered object(s)
</code></pre>

<p>
For lowered objects, the implementation SHOULD preserve information equivalent to:
</p>

<ul>
  <li>a lowered object identity,</li>
  <li>its lowering role,</li>
  <li>its originating open-IR contributor(s),</li>
  <li>its validated semantic contributor(s),</li>
  <li>whether it is preserved, expanded, merged, or realization-supporting.</li>
</ul>

<p>
A useful conceptual shape is:
</p>

<pre><code>open IR structure[for_loop]
      |
      +--&gt; lowered loop_init
      +--&gt; lowered loop_guard
      +--&gt; lowered loop_body_dispatch
      +--&gt; lowered state_update
      +--&gt; lowered exit_join
</code></pre>

<p>
This expansion is acceptable only if the chain of meaning remains recoverable.
</p>

<p>
Lowering therefore does not cancel the mapping discipline of the IR layer.
It extends it into a more specialized space.
</p>

<p>
The exact representation of that mapping remains implementation-dependent unless a stricter downstream contract standardizes it more narrowly.
What remains mandatory is recoverable origin, not one universal lowering-identity encoding.
</p>

<hr/>

<h2 id="relation-with-observation-debugging-and-diagnostics">21. Relation with Observation, Debugging, and Diagnostics</h2>

<p>
This document does not define debugger commands or runtime trace protocols.
</p>

<p>
However, lowering MUST remain compatible with the language-level requirement that meaningful stops, observation points, and execution-state transitions remain source-aligned where relevant.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>lowering MAY introduce additional internal steps,</li>
  <li>but those steps MUST NOT make source-aligned stop attribution impossible,</li>
  <li>lowering MAY refine execution contexts,</li>
  <li>but later layers MUST remain able to relate those refined contexts back to meaningful source-visible locations where required,</li>
  <li>fault diagnostics SHOULD remain able to recover contributing source-visible meaning rather than only reporting opaque private artifacts.</li>
</ul>

<p>
This can be summarized as:
</p>

<pre><code>lowered internal detail
        is allowed

loss of source-aligned diagnosability
        is not allowed
</code></pre>

<hr/>

<h2 id="conceptual-lowered-products">22. Conceptual Lowered Products</h2>

<p>
This document does not freeze one mandatory lowered payload.
</p>

<p>
However, it is useful to distinguish the kinds of products a lowering stage MAY emit:
</p>

<ul>
  <li><strong>lowered control form</strong> — lower branch / loop / dispatch representation,</li>
  <li><strong>lowered state form</strong> — explicit realization-facing state cells and updates,</li>
  <li><strong>lowered interface form</strong> — ABI, transport, or endpoint specialization,</li>
  <li><strong>lowered storage form</strong> — buffers, ownership, layout, transfer, lifetime,</li>
  <li><strong>lowered placement form</strong> — domain assignment, partitioning, device mapping,</li>
  <li><strong>lowered schedule form</strong> — work ordering, execution clusters, queues, or static schedule support.</li>
</ul>

<p>
A single implementation MAY keep these in one lowered graph or split them across several interrelated lowered artifacts.
</p>

<p>
Some of those forms MAY later be the input to a backend contract boundary.
That later handoff is downstream from lowering itself.
</p>

<hr/>

<h2 id="minimal-conceptual-shape">23. Minimal Conceptual Shape</h2>

<p>
This document does not define a mandatory serialized format.
</p>

<p>
Still, a conforming lowering stage SHOULD be representable in a conceptual shape equivalent to:
</p>

<pre><code>{
  "kind": "lowered_form",
  "lowering_stage": "backend_oriented",
  "target_family": "example_backend_family",
  "objects": [
    {
      "lowered_id": "l_001",
      "role": "loop_guard",
      "origin": {
        "ir_objects": ["obj_loop_1"],
        "semantic_objects": ["sem.loop_1"],
        "mapping_relation": "1_to_n"
      }
    }
  ],
  "connections": [],
  "storage": [],
  "placement": [],
  "schedule": []
}
</code></pre>

<p>
The exact field names are illustrative only.
</p>

<p>
What matters is the preserved information equivalent to:
</p>

<ul>
  <li>lowered object identity,</li>
  <li>lowering stage classification,</li>
  <li>target-family orientation,</li>
  <li>recoverable origin mapping,</li>
  <li>specialized execution-relevant objects and relations.</li>
</ul>

<pre><code>Minimal lowering intent

🟧 lowered object identity
🟧 lowering role
🟩 recoverable origin mapping
🟧 specialized execution-facing relations
</code></pre>

<hr/>

<h2 id="examples">24. Examples</h2>

<h3>24.1 Structured case lowered to branch form</h3>

<pre><code>open Execution IR
-----------------
structure[case]
  ├─ region[true]
  └─ region[false]

possible lowered form
---------------------
selector_test
  ├─ branch_true
  ├─ branch_false
  └─ join
</code></pre>

<p>
Allowed if:
</p>

<ul>
  <li>the case-origin remains attributable,</li>
  <li>branch semantics remain equivalent,</li>
  <li>join behavior remains consistent with validated meaning.</li>
</ul>

<h3>24.2 Explicit delay lowered to state-cell form</h3>

<pre><code>open Execution IR
-----------------
[frog.core.delay] --&gt; [frog.core.add]

possible lowered form
---------------------
[state_read] --&gt; [lowered_add] --&gt; [state_commit]
</code></pre>

<p>
Allowed if the lowered state-cell path is still attributable to explicit local memory and not presented as hidden semantic invention.
</p>

<h3>24.3 Public interface lowered to ABI form</h3>

<pre><code>open Execution IR
-----------------
interface_input[a] --&gt; primitive[add] --&gt; interface_output[result]

possible lowered form
---------------------
abi_arg[0] --&gt; op_add --&gt; abi_ret[0]
</code></pre>

<p>
Allowed if:
</p>

<ul>
  <li>the public-boundary origin remains recoverable,</li>
  <li>the dependency meaning remains equivalent,</li>
  <li>the ABI mapping does not silently redefine public program meaning.</li>
</ul>

<h3>24.4 Loop lowered with explicit carried state</h3>

<pre><code>open Execution IR
-----------------
for_loop
  └─ region[body]

possible lowered form
---------------------
iter_init
iter_guard
body_dispatch
iter_state_update
iter_exit
</code></pre>

<p>
Allowed if the loop-origin, iteration semantics, and carried-state correspondence remain recoverable.
</p>

<hr/>

<h2 id="out-of-scope-for-v01">25. Out of Scope for v0.1</h2>

<p>
The following topics remain out of scope for this document in v0.1:
</p>

<ul>
  <li>one frozen lowered wire format,</li>
  <li>one universal backend family taxonomy,</li>
  <li>one universal ABI contract,</li>
  <li>one mandatory schedule encoding,</li>
  <li>one universal placement model,</li>
  <li>one mandatory runtime-private state representation,</li>
  <li>one mandatory debugger attribution payload for lowered stops,</li>
  <li>complete conformance rules for every possible lowering pipeline.</li>
</ul>

<p>
The purpose of v0.1 is narrower:
</p>

<pre><code>define the lowering boundary clearly
without collapsing FROG into one compiler architecture
</code></pre>

<hr/>

<h2 id="summary">26. Summary</h2>

<p>
Lowering in FROG v0.1 is the first standardized specialization zone after open Execution IR.
It may reshape control, storage, boundaries, scheduling, placement, and target-facing representation, but it MUST remain semantically faithful and attribution-preserving.
</p>

<p>
It does not redefine the language.
It does not replace the open Execution IR as the primary open execution-facing representation.
It does not standardize the backend contract itself.
It does not standardize private runtime realization.
</p>

<p>
In compact form:
</p>

<pre><code>🟦 open Execution IR
        |
        v
🟧 lowering
        |
        +-- specialize for target consumption
        +-- preserve semantic meaning
        +-- preserve recoverable attribution
        |
        v
🟨 backend-facing handoff and/or 🟥 private realization
</code></pre>
