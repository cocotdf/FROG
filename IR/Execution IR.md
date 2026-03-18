<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG Execution IR Specification</h1>

<p align="center">
  Open execution-facing intermediate representation for validated FROG programs<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#reading-legend">2. Reading Legend</a></li>
  <li><a href="#role-of-this-document">3. Role of this Document</a></li>
  <li><a href="#what-this-document-owns">4. What this Document Owns</a></li>
  <li><a href="#what-this-document-does-not-own">5. What this Document Does Not Own</a></li>
  <li><a href="#position-in-the-pipeline">6. Position in the Pipeline</a></li>
  <li><a href="#design-goals">7. Design Goals</a></li>
  <li><a href="#core-invariants">8. Core Invariants</a></li>
  <li><a href="#execution-ir-object-model">9. Execution IR Object Model</a></li>
  <li><a href="#primary-object-families">10. Primary Object Families</a></li>
  <li><a href="#ports-and-connectivity">11. Ports and Connectivity</a></li>
  <li><a href="#regions-and-structured-control">12. Regions and Structured Control</a></li>
  <li><a href="#interface-and-ui-boundaries">13. Interface and UI Boundaries</a></li>
  <li><a href="#state-local-memory-and-cycles">14. State, Local Memory, and Cycles</a></li>
  <li><a href="#relation-with-identity-and-mapping">15. Relation with Identity and Mapping</a></li>
  <li><a href="#relation-with-derivation-and-construction-rules">16. Relation with Derivation and Construction Rules</a></li>
  <li><a href="#relation-with-lowering-backend-contract-and-runtime-private-forms">17. Relation with Lowering, Backend Contract, and Runtime-Private Forms</a></li>
  <li><a href="#relation-with-cache-and-tooling">18. Relation with Cache and Tooling</a></li>
  <li><a href="#out-of-scope-for-v01">19. Out of Scope for v0.1</a></li>
  <li><a href="#summary">20. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the base <strong>open execution-facing intermediate representation</strong> for FROG v0.1.
</p>

<p>
The Execution IR is a <strong>derived representation</strong> built from a validated FROG program.
It exists to provide an execution-facing form that remains open, inspectable, source-attributable, structured, and architecturally upstream of lowering and runtime-private realization.
</p>

<p>
For v0.1, the Execution IR remains deliberately close to validated executable meaning.
It is <strong>not</strong> yet a lowered backend contract, a private scheduler graph, a compiled artifact, or a runtime history form.
</p>

<pre><code>🟦 canonical source
      -&gt;
🟩 validated meaning
      -&gt;
🟦 open Execution IR
      -&gt;
🟧 lowering / specialization
      -&gt;
🟨 backend-facing contract
      -&gt;
🟥 private realization
</code></pre>

<p>
The open Execution IR is therefore the first standardized execution-facing representation of a validated FROG program.
It is the representation that remains close enough to the language to be inspectable and attributable, while already being explicit enough to support later specialization.
</p>

<hr/>

<h2 id="reading-legend">2. Reading Legend</h2>

<ul>
  <li>🟦 <strong>Open specification-facing representation or layer</strong></li>
  <li>🟩 <strong>Semantic truth, source attribution, or recoverability obligation</strong></li>
  <li>🟨 <strong>Boundary, interface, mapping, or standardized handoff</strong></li>
  <li>🟧 <strong>Lowering / specialization / target adaptation zone</strong></li>
  <li>🟥 <strong>Implementation-private or runtime-private realization zone</strong></li>
</ul>

<hr/>

<h2 id="role-of-this-document">3. Role of this Document</h2>

<p>
This document defines <strong>what the open Execution IR is</strong> at the architectural level.
It defines the object model, the major preserved families, and the invariants that make the IR portable, inspectable, attributable, and suitable for later specialization.
</p>

<p>
This document is intentionally narrower than:
</p>

<ul>
  <li>the full source-to-IR correspondence rules,</li>
  <li>the procedural rules for constructing IR payloads,</li>
  <li>the cross-boundary identity and recoverability rules in full,</li>
  <li>later lowering or backend-facing contracts.</li>
</ul>

<p>
In compact form:
</p>

<pre><code>Execution IR.md
   -&gt; what the open IR is

Identity and Mapping.md
   -&gt; how source-aligned identity stays recoverable

Derivation rules.md
   -&gt; what must remain correspondingly recoverable

Construction rules.md
   -&gt; how a conforming open IR is materially built

Lowering.md
   -&gt; how later specialization may begin

Backend contract.md
   -&gt; what a later backend-facing consumer may rely on
</code></pre>

<hr/>

<h2 id="what-this-document-owns">4. What this Document Owns</h2>

<p>
This document owns:
</p>

<ul>
  <li>the architectural role of the open Execution IR,</li>
  <li>its position between validated meaning and later specialization,</li>
  <li>its core invariants,</li>
  <li>its high-level object model,</li>
  <li>the major execution-facing families that remain visible in base v0.1,</li>
  <li>the execution-facing distinctions that base open IR MUST preserve,</li>
  <li>the boundary between open Execution IR and later runtime-private realization.</li>
</ul>

<pre><code>🟦 This document owns
- open execution-facing identity of the IR layer
- object model
- preserved execution-facing families
- invariants
- explicit structured execution-facing representation
- open IR vs downstream realization boundary
</code></pre>

<hr/>

<h2 id="what-this-document-does-not-own">5. What this Document Does Not Own</h2>

<p>
This document does not define:
</p>

<ul>
  <li>the canonical <code>.frog</code> source structure in full,</li>
  <li>the IDE Program Model,</li>
  <li>the complete normative semantics of all FROG execution behavior,</li>
  <li>the full source-to-IR derivation mapping,</li>
  <li>the full procedural construction rules for building open IR payloads,</li>
  <li>the complete identity and mapping contract across all later stages,</li>
  <li>one mandatory runtime scheduler architecture,</li>
  <li>one mandatory compiled artifact format,</li>
  <li>one mandatory lowering pipeline,</li>
  <li>one mandatory backend contract payload shape.</li>
</ul>

<p>
This document also does not require every implementation to expose every private internal execution form.
</p>

<pre><code>🟥 This document does NOT own
- source serialization
- IDE editing models
- full language semantics
- derivation mapping details
- construction procedure details
- full cross-stage identity contract
- runtime scheduler internals
- compiled artifact formats
- backend-private realization
</code></pre>

<hr/>

<h2 id="position-in-the-pipeline">6. Position in the Pipeline</h2>

<p>
The base architectural pipeline is:
</p>

<pre><code>🟦 canonical .frog source
        |
        v
🟦 Expression
        |
        v
🟦 Program Model or equivalent validated tool form
        |
        v
🟩 validated executable meaning
        |
        v
🟦 Execution IR
        |
        v
🟧 lowering / backend preparation
        |
        v
🟨 backend contract
        |
        v
🟥 runtime-private realization
</code></pre>

<p>
The validated executable meaning is the language-level truth of the program.
The Execution IR is the open execution-facing form built from that validated meaning.
</p>

<p>
Execution IR therefore begins <strong>after validation</strong> and remains <strong>before lowering</strong>.
It is also <strong>before backend contract emission</strong> and <strong>before private realization</strong>.
</p>

<pre><code>🟩 semantic truth
      |
      v
🟦 open execution-facing form
      |
      v
🟧 specialization
      |
      v
🟨 standardized consumable handoff
      |
      v
🟥 private execution machinery
</code></pre>

<hr/>

<h2 id="design-goals">7. Design Goals</h2>

<p>
The base Execution IR for v0.1 SHOULD be:
</p>

<ul>
  <li>execution-facing,</li>
  <li>source-attributable,</li>
  <li>recoverable for later inspection and diagnostics,</li>
  <li>inspectable,</li>
  <li>portable across implementations,</li>
  <li>stable enough to support later tooling,</li>
  <li>strict enough to support later lowering,</li>
  <li>conservative enough to avoid freezing one private compiler or runtime design too early.</li>
</ul>

<pre><code>Design balance

🟦 open enough      -&gt; inspectable / portable / standard-friendly
🟩 faithful enough  -&gt; semantically grounded
🟩 attributable     -&gt; recoverable for later tooling
🟧 strict enough    -&gt; useful for later lowering
🟥 not frozen as    -&gt; one private runtime design
</code></pre>

<hr/>

<h2 id="core-invariants">8. Core Invariants</h2>

<p>
The following invariants apply to the base open Execution IR of v0.1:
</p>

<ul>
  <li>Every execution-visible IR object MUST be attributable to validated program meaning.</li>
  <li>The Execution IR MUST remain source-aligned at the level of attributable execution-facing objects.</li>
  <li>The Execution IR MUST preserve enough object identity and structure to support later recoverable mapping obligations.</li>
  <li>The Execution IR MUST NOT silently change the normative language meaning of the validated program.</li>
  <li>The Execution IR MUST preserve explicit local memory as explicit local memory.</li>
  <li>The Execution IR MUST preserve structured control as structured control in the open IR.</li>
  <li>The Execution IR MUST preserve the distinction between public interface participation and UI participation.</li>
  <li>The Execution IR MUST NOT encode editor-only presentation state as execution semantics.</li>
  <li>The Execution IR MUST NOT be treated as a runtime history, event trace, or debugger session log.</li>
</ul>

<pre><code>Core invariants

🟩 attributable
🟩 source-aligned
🟩 mapping-supporting
🟩 semantically faithful
🟩 explicit-memory preserving
🟩 structured-control preserving
🟩 interface / UI distinction preserving
🟥 not editor-state semantics
🟥 not runtime history
</code></pre>

<hr/>

<h2 id="execution-ir-object-model">9. Execution IR Object Model</h2>

<p>
The base Execution IR represents one validated FROG as one <strong>execution unit</strong> containing execution-facing objects and their relationships.
</p>

<p>
Conceptually:
</p>

<pre><code>🟦 Execution IR
└── 🟦 execution unit
    ├── 🟨 boundary objects
    ├── 🟦 executable objects
    ├── 🟦 region objects
    ├── 🟦 typed ports
    ├── 🟦 directed connections
    ├── 🟩 execution-facing identities
    └── 🟩 source attribution anchors
</code></pre>

<p>
This execution unit is the architectural container of the open IR for one validated FROG in base v0.1.
</p>

<p>
The open Execution IR MAY contain support objects that make execution-facing structure more explicit, but such support objects MUST remain attributable and MUST NOT replace primary validated execution-visible content with opaque generated machinery.
</p>

<pre><code>Support objects are allowed when they are:

✔ attributable
✔ execution-facing
✔ semantically justified
✔ structurally recoverable
✘ opaque replacement machinery
✘ hidden semantic redefinition
✘ premature backend-private invention
</code></pre>

<p>
The execution unit is not required to be the same thing as:
</p>

<ul>
  <li>the canonical source file shape,</li>
  <li>the editable Program Model shape,</li>
  <li>a lowered target-oriented unit,</li>
  <li>a runtime-private scheduled unit.</li>
</ul>

<hr/>

<h2 id="primary-object-families">10. Primary Object Families</h2>

<p>
In base v0.1, the Execution IR SHOULD preserve the major validated object families rather than aggressively lowering them away.
</p>

<p>
Those families include:
</p>

<ul>
  <li>primitive execution objects,</li>
  <li>structured execution objects,</li>
  <li>sub-FROG invocation objects,</li>
  <li>public interface boundary objects,</li>
  <li>widget-value participation objects,</li>
  <li>widget-reference participation objects where applicable,</li>
  <li>explicit local-memory-bearing objects where applicable.</li>
</ul>

<p>
This conservative model keeps the open IR readable and attributable while still making execution-facing structure explicit.
</p>

<p>
Base v0.1 therefore favors:
</p>

<pre><code>🟩 validated structured meaning
        |
        v
🟦 open structured IR
        |
        v
🟧 later specialization
</code></pre>

<p>
rather than:
</p>

<pre><code>🟩 validated structured meaning
        |
        v
🟥 immediate backend-shaped flattening
</code></pre>

<p>
This does not prevent later specialization.
It means that specialization belongs to later stages, not to the base open Execution IR itself.
</p>

<hr/>

<h2 id="ports-and-connectivity">11. Ports and Connectivity</h2>

<p>
The Execution IR MUST represent execution-relevant connectivity explicitly.
</p>

<p>
At minimum:
</p>

<ul>
  <li>execution-facing objects MUST expose explicit typed ports or an equivalent explicit terminal interface,</li>
  <li>port direction MUST be explicit,</li>
  <li>directed connections MUST be explicit,</li>
  <li>the resulting IR graph MUST preserve the validated dependency structure of the program,</li>
  <li>connection endpoints MUST remain attributable to validated execution-facing objects and validated ports or terminals.</li>
</ul>

<p>
The open IR MAY be more explicit than source where validation has already resolved execution-relevant facts.
That explicitness belongs to open execution-facing representation, not yet to target-specific lowering.
</p>

<pre><code>Connectivity invariants

🟦 explicit ports
🟦 explicit direction
🟦 explicit directed connections
🟩 preserved validated dependencies
🟩 attributable endpoints
</code></pre>

<p>
Execution IR connectivity MUST therefore remain:
</p>

<ul>
  <li>structurally inspectable,</li>
  <li>directionally unambiguous,</li>
  <li>semantically grounded in validated dependency meaning.</li>
</ul>

<hr/>

<h2 id="regions-and-structured-control">12. Regions and Structured Control</h2>

<p>
Structured control remains explicit in the base Execution IR.
</p>

<p>
For v0.1, control structures such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code> SHOULD remain represented as structured execution objects with explicit owned regions and explicit boundary participation rather than being immediately flattened into backend-oriented branch or loop machinery.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>a structured execution object MUST identify its standardized structure family,</li>
  <li>owned regions MUST remain explicit,</li>
  <li>structure-boundary participation MUST remain explicit,</li>
  <li>region-local execution content MUST remain attributable to source-level region content.</li>
</ul>

<p>
This keeps the open IR aligned with validated control meaning while leaving backend-oriented branching and loop realization to later stages.
</p>

<pre><code>🟩 validated structured control
        |
        v
🟦 explicit structured IR object
        ├── 🟦 explicit owned regions
        ├── 🟨 explicit boundary participation
        └── 🟩 attributable region-local content
</code></pre>

<p>
In v0.1, the open Execution IR SHOULD still make it possible to recover:
</p>

<ul>
  <li>which structure family is involved,</li>
  <li>which regions belong to that structure,</li>
  <li>which execution-facing objects are region-local,</li>
  <li>which boundary roles connect outer and inner execution content.</li>
</ul>

<hr/>

<h2 id="interface-and-ui-boundaries">13. Interface and UI Boundaries</h2>

<p>
The Execution IR MUST preserve the distinction between:
</p>

<ul>
  <li>public interface participation,</li>
  <li>widget primary-value participation,</li>
  <li>widget object-style reference participation.</li>
</ul>

<p>
Therefore:
</p>

<ul>
  <li>public interface entry and exit semantics MUST remain represented explicitly,</li>
  <li>widget primary-value participation MUST remain distinguishable from public interface participation,</li>
  <li>widget-reference access MUST remain distinguishable from ordinary valueflow participation,</li>
  <li>the open IR MUST NOT collapse those roles into one undifferentiated generic boundary concept.</li>
</ul>

<p>
In base v0.1, a source-aligned implementation SHOULD preserve recognizable families corresponding to:
</p>

<ul>
  <li><code>interface_input</code>,</li>
  <li><code>interface_output</code>,</li>
  <li><code>widget_value</code>,</li>
  <li><code>widget_reference</code>.</li>
</ul>

<pre><code>Boundary distinction

🟨 public interface participation
   !=
🟦 widget primary-value participation
   !=
🟦 widget object-style reference participation
</code></pre>

<p>
This distinction matters because:
</p>

<ul>
  <li>public reusable program boundaries are not the same thing as UI participation,</li>
  <li>widget valueflow is not the same thing as object-style widget interaction,</li>
  <li>later lowering and backend-facing forms still need those distinctions to remain recoverable where required.</li>
</ul>

<hr/>

<h2 id="state-local-memory-and-cycles">14. State, Local Memory, and Cycles</h2>

<p>
Explicit local memory remains explicit in the base Execution IR.
This is a hard architectural requirement.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>the IR MUST preserve explicit local-memory objects such as <code>frog.core.delay</code>,</li>
  <li>the IR MUST NOT legalize an otherwise invalid combinational cycle by introducing hidden implicit memory,</li>
  <li>the IR MUST NOT erase explicit memory attribution in a valid feedback path,</li>
  <li>cycles represented in the IR MUST remain consistent with validated cycle rules.</li>
</ul>

<p>
The open Execution IR MAY classify explicit memory-bearing objects as execution-relevant state objects, but it MUST remain faithful to the validated FROG rule that valid feedback depends on explicit local memory.
</p>

<pre><code>Cycle discipline

invalid cycle
   != legalized by hidden memory

valid feedback
   requires
🟩 explicit local memory

therefore

🟦 Execution IR
   must preserve
🟩 explicit memory identity
</code></pre>

<p>
This requirement is intentionally conservative.
State elimination, storage remapping, or state-cell realization belong to later lowering stages, not to the base open Execution IR definition.
</p>

<hr/>

<h2 id="relation-with-identity-and-mapping">15. Relation with Identity and Mapping</h2>

<p>
This document defines the open Execution IR as an attributable execution-facing representation.
It does not define the full normative mapping contract by which every source-visible object, validated semantic object, and IR object remain recoverably related.
</p>

<p>
That concern belongs primarily to <strong><code>Identity and Mapping.md</code></strong>.
</p>

<p>
The relationship is:
</p>

<ul>
  <li><code>Execution IR.md</code> defines the kinds of execution-facing objects the open IR contains,</li>
  <li><code>Identity and Mapping.md</code> defines how those objects remain connected to validated meaning and source-visible contributors,</li>
  <li>the open Execution IR MUST preserve enough identity and structure for those mapping obligations to remain satisfiable.</li>
</ul>

<pre><code>Execution IR.md
   -&gt; what execution-facing objects exist

Identity and Mapping.md
   -&gt; how those objects remain recoverably connected
      to validated meaning and source-visible origin
</code></pre>

<p>
Therefore, the base open Execution IR MUST be designed so that later tools and later stages can still answer questions such as:
</p>

<ul>
  <li>Which validated structure does this IR object come from?</li>
  <li>Which source-visible region or port does this execution-facing object represent?</li>
  <li>Which distinctions remain recoverable after execution-facing normalization?</li>
</ul>

<hr/>

<h2 id="relation-with-derivation-and-construction-rules">16. Relation with Derivation and Construction Rules</h2>

<p>
This document defines the architectural shape of the open Execution IR.
It does not fully define either:
</p>

<ul>
  <li>the normative correspondence between validated source-visible content and IR objects, or</li>
  <li>the full procedural rules for materially building an open IR payload.</li>
</ul>

<p>
Those concerns belong to companion documents of the IR layer:
</p>

<ul>
  <li><strong>Derivation rules</strong> define what must remain correspondingly recoverable between validated FROG meaning and open Execution IR.</li>
  <li><strong>Construction rules</strong> define how a conforming open Execution IR is materially built.</li>
</ul>

<p>
In compact form:
</p>

<pre><code>Execution IR.md
   -&gt; what the open IR is

Derivation rules.md
   -&gt; what must remain recoverable

Construction rules.md
   -&gt; how the open IR is built
</code></pre>

<p>
This separation is important:
</p>

<ul>
  <li>Execution IR SHOULD stay architectural and durable,</li>
  <li>Derivation SHOULD stay about correspondence obligations,</li>
  <li>Construction SHOULD stay about build obligations and payload shape.</li>
</ul>

<hr/>

<h2 id="relation-with-lowering-backend-contract-and-runtime-private-forms">17. Relation with Lowering, Backend Contract, and Runtime-Private Forms</h2>

<p>
The open Execution IR sits before lowering and before runtime-private realization.
It also sits before the backend-facing contract boundary that later consumers may rely on.
</p>

<p>
Therefore:
</p>

<ul>
  <li>the open Execution IR MAY serve as the input to later lowering stages,</li>
  <li>later stages MAY specialize, normalize further, partition, schedule, or compile execution for specific targets,</li>
  <li>a backend contract MAY later define what a lowered form explicitly offers to a downstream consumer,</li>
  <li>runtime-private scheduler structures, compiled objects, target-private state layouts, and equivalent realization forms remain outside the ownership of this document unless later standardized explicitly.</li>
</ul>

<p>
This means:
</p>

<pre><code>🟦 open Execution IR
   != 🟥 private scheduler graph

🟦 open Execution IR
   != 🟥 compiled artifact

🟦 open Execution IR
   != 🟥 runtime trace

🟦 open Execution IR
   != 🟨 backend-facing contract

🟦 open Execution IR
   = open execution-facing representation
</code></pre>

<pre><code>🟦 open IR
      -&gt;
🟧 lowering / specialization
      -&gt;
🟨 backend contract
      -&gt;
🟥 private realization
</code></pre>

<p>
The architectural reading rule is:
</p>

<ul>
  <li><strong>Execution IR</strong> remains source-shaped enough for inspection and attribution,</li>
  <li><strong>Lowering</strong> is where specialization begins,</li>
  <li><strong>Backend contract</strong> is where a standardized consumable handoff may be declared,</li>
  <li><strong>private realization</strong> is later and is not owned by this document.</li>
</ul>

<hr/>

<h2 id="relation-with-cache-and-tooling">18. Relation with Cache and Tooling</h2>

<p>
A tool MAY serialize an Execution IR artifact inside a cache entry such as <code>frog.ir</code>.
</p>

<p>
However:
</p>

<ul>
  <li>the cache container does not own the meaning of Execution IR,</li>
  <li>cache metadata does not affect program semantics,</li>
  <li>cache absence does not invalidate the canonical source artifact,</li>
  <li>cache presence does not make the cached artifact the canonical source of truth.</li>
</ul>

<p>
This document owns the architectural meaning of the open Execution IR itself.
Cache specifications only define how such derived artifacts may be stored or associated.
</p>

<p>
Likewise, IDEs and other tools MAY inspect, compare, cache, render, or analyze open IR forms without thereby taking ownership of the IR definition itself.
</p>

<pre><code>🟦 Execution IR meaning
   lives in
IR/

🟨 cached derived artifact
   may live in
frog.ir

cache container
   is not
IR ownership
</code></pre>

<p>
Tooling MAY therefore use the open IR for:
</p>

<ul>
  <li>inspection,</li>
  <li>comparison,</li>
  <li>validation support,</li>
  <li>diagnostic correlation,</li>
  <li>execution preparation.</li>
</ul>

<p>
But such uses MUST NOT redefine the architectural meaning of the open Execution IR as if it were merely a cache convention or an IDE-internal view.
</p>

<hr/>

<h2 id="out-of-scope-for-v01">19. Out of Scope for v0.1</h2>

<p>
The following topics remain out of scope for this document in v0.1:
</p>

<ul>
  <li>a fully frozen transport schema for every implementation,</li>
  <li>one mandatory SSA-style form,</li>
  <li>one mandatory scheduler graph,</li>
  <li>one mandatory lowering pipeline,</li>
  <li>one mandatory backend contract payload format,</li>
  <li>distributed execution IR,</li>
  <li>asynchronous execution IR beyond the baseline language model,</li>
  <li>one mandatory runtime state snapshot format,</li>
  <li>one mandatory trace or observability event protocol.</li>
</ul>

<pre><code>Not frozen in v0.1

🟥 one universal private execution form
🟥 one mandatory SSA form
🟥 one mandatory scheduler graph
🟧 one mandatory lowering pipeline
🟨 one mandatory backend contract payload
🟨 one mandatory trace / observability transport
</code></pre>

<hr/>

<h2 id="summary">20. Summary</h2>

<p>
The FROG Execution IR of v0.1 is an <strong>open execution-facing representation</strong> built from
<strong>validated program meaning</strong>.
It remains <strong>source-attributable</strong>, <strong>structured</strong>, <strong>portable</strong>, and
<strong>conservative</strong> by design.
</p>

<p>
It preserves:
</p>

<ul>
  <li>major validated execution-facing object families,</li>
  <li>explicit connectivity,</li>
  <li>structured control and explicit regions,</li>
  <li>public interface versus UI distinctions,</li>
  <li>explicit local memory and valid stateful cycles,</li>
  <li>enough identity and structure to support later recoverability obligations.</li>
</ul>

<p>
It does not define:
</p>

<ul>
  <li>full derivation correspondence,</li>
  <li>full construction procedure,</li>
  <li>full identity and mapping rules,</li>
  <li>full lowering,</li>
  <li>full backend contract,</li>
  <li>runtime-private realization.</li>
</ul>

<p>
In one line:
</p>

<pre><code>🟦 Execution IR is the open architectural bridge
between 🟩 validated FROG meaning
and 🟧 later specialization for execution realization,
while remaining upstream of 🟨 backend contract
and outside 🟥 private runtime realization.
</code></pre>
