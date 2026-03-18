<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG IR Backend Contract</h1>

<p align="center">
Normative consumption contract for lowered execution forms in FROG v0.1<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#legend">2. Reading Legend</a></li>
  <li><a href="#why-this-document-exists">3. Why this Document Exists</a></li>
  <li><a href="#position-in-the-pipeline">4. Position in the Pipeline</a></li>
  <li><a href="#scope">5. Scope</a></li>
  <li><a href="#non-goals">6. Non-Goals</a></li>
  <li><a href="#core-definition">7. Core Definition</a></li>
  <li><a href="#contract-parties">8. Contract Parties</a></li>
  <li><a href="#contract-boundary">9. Contract Boundary</a></li>
  <li><a href="#minimum-preconditions">10. Minimum Preconditions</a></li>
  <li><a href="#backend-family-and-contract-identity">11. Backend Family and Contract Identity</a></li>
  <li><a href="#required-contract-sections">12. Required Contract Sections</a>
    <ul>
      <li><a href="#contract-header">12.1 Contract header</a></li>
      <li><a href="#capability-and-assumption-section">12.2 Capability and assumption section</a></li>
      <li><a href="#consumable-executable-section">12.3 Consumable executable section</a></li>
      <li><a href="#boundary-section">12.4 Boundary section</a></li>
      <li><a href="#state-and-memory-section">12.5 State and memory section</a></li>
      <li><a href="#placement-scheduling-and-domain-section">12.6 Placement, scheduling, and domain section</a></li>
      <li><a href="#attribution-and-diagnostics-section">12.7 Attribution and diagnostics section</a></li>
      <li><a href="#rejection-and-unsupported-features-section">12.8 Rejection and unsupported-features section</a></li>
    </ul>
  </li>
  <li><a href="#producer-obligations">13. Producer Obligations</a></li>
  <li><a href="#consumer-obligations">14. Consumer Obligations</a></li>
  <li><a href="#preservation-invariants">15. Preservation Invariants</a></li>
  <li><a href="#control-structures-state-and-boundaries">16. Control Structures, State, and Boundaries</a></li>
  <li><a href="#observability-debugging-and-fault-attribution">17. Observability, Debugging, and Fault Attribution</a></li>
  <li><a href="#relation-with-profiles-libraries-and-conformance">18. Relation with Profiles, Libraries, and Conformance</a></li>
  <li><a href="#minimal-conceptual-shape">19. Minimal Conceptual Shape</a></li>
  <li><a href="#contract-lifecycle">20. Contract Lifecycle</a></li>
  <li><a href="#examples">21. Examples</a></li>
  <li><a href="#out-of-scope-for-v01">22. Out of Scope for v0.1</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the <strong>backend contract</strong> that later compiler, backend, runtime, or execution-preparation stages MAY consume after lowering in FROG v0.1.
</p>

<p>
It exists to define a stable architectural handoff between:
</p>

<ul>
  <li>the open, source-attributable execution-facing IR world, and</li>
  <li>the specialized consumer world where compilation, backend mapping, scheduling realization, ABI binding, deployment preparation, or runtime realization may occur.</li>
</ul>

<p>
This document does <strong>not</strong> define one universal backend implementation.
It defines the minimum interoperable contract shape and obligations that a lowered form MUST satisfy if it claims to be consumable by later stages under a standardized backend-facing contract.
</p>

<hr/>

<h2 id="legend">2. Reading Legend</h2>

<p>
The diagrams below use the following visual legend:
</p>

<ul>
  <li>🟦 <strong>Open specification-facing layer</strong></li>
  <li>🟨 <strong>Standardized handoff / contract layer</strong></li>
  <li>🟧 <strong>Specialized lowering / backend-oriented layer</strong></li>
  <li>🟥 <strong>Private realization layer</strong></li>
  <li>🟩 <strong>Source-aligned attribution / diagnostic obligation</strong></li>
</ul>

<hr/>

<h2 id="why-this-document-exists">3. Why this Document Exists</h2>

<p>
The open Execution IR is intentionally kept distinct from:
</p>

<ul>
  <li>one private compiler pipeline,</li>
  <li>one private runtime scheduler graph,</li>
  <li>one vendor ABI,</li>
  <li>one target-specific executable bundle.</li>
</ul>

<p>
However, once lowering begins, later stages still need a stable notion of:
</p>

<ul>
  <li>what executable content is being consumed,</li>
  <li>which assumptions are already fixed,</li>
  <li>which distinctions must still remain recoverable,</li>
  <li>what a backend consumer is allowed to assume,</li>
  <li>what it must reject instead of silently reinterpreting.</li>
</ul>

<p>
This document exists to define that handoff cleanly.
</p>

<p>
Without such a contract, each implementation risks inventing its own implicit rules for:
</p>

<ul>
  <li>lowered unit boundaries,</li>
  <li>state and memory interpretation,</li>
  <li>public boundary handling,</li>
  <li>profile requirements,</li>
  <li>debug attribution,</li>
  <li>error and unsupported-feature reporting.</li>
</ul>

<hr/>

<h2 id="position-in-the-pipeline">4. Position in the Pipeline</h2>

<p>
The intended architecture is:
</p>

<pre><code>🟦 canonical source (.frog)
          |
          v
🟦 validated program meaning
          |
          v
🟦 Execution IR
   (open, inspectable, source-attributable,
    execution-facing, not backend-private)
          |
          v
🟧 Lowering
          |
          v
🟨 Backend Contract
   (standardized consumable handoff)
          |
          v
🟥 compiler / backend / runtime realization
          |
          +-----------------------------+
          |                             |
          v                             v
🟩 source-aligned diagnostics      🟥 target-private activity
🟩 source-aligned observability
🟩 source-aligned debug attribution
</code></pre>

<p>
The backend contract therefore sits <strong>after lowering begins</strong> and <strong>before private realization takes over</strong>.
</p>

<hr/>

<h2 id="scope">5. Scope</h2>

<p>
This document defines:
</p>

<ul>
  <li>what a backend contract is in FROG,</li>
  <li>what information a lowered producer MUST provide to later stages,</li>
  <li>what a backend consumer MAY assume,</li>
  <li>what a backend consumer MUST preserve or reject,</li>
  <li>what remains attributable across the handoff,</li>
  <li>which architectural categories MUST remain explicit at the contract boundary.</li>
</ul>

<hr/>

<h2 id="non-goals">6. Non-Goals</h2>

<p>
This document does not define:
</p>

<ul>
  <li>one mandatory serialized artifact format,</li>
  <li>one mandatory ABI,</li>
  <li>one mandatory scheduler representation,</li>
  <li>one mandatory bytecode format,</li>
  <li>one mandatory JIT interface,</li>
  <li>one mandatory deployment package format,</li>
  <li>one mandatory debugging protocol,</li>
  <li>one mandatory runtime-private state object model.</li>
</ul>

<p>
This document also does not move semantic ownership away from:
</p>

<ul>
  <li><code>Expression/</code> for canonical source,</li>
  <li><code>Language/</code> for validated execution meaning,</li>
  <li><code>Libraries/</code> for intrinsic primitive identities and primitive-local behavior,</li>
  <li><code>Profiles/</code> for optional standardized capability families,</li>
  <li><code>IDE/</code> for tool-facing projection and UI behavior.</li>
</ul>

<hr/>

<h2 id="core-definition">7. Core Definition</h2>

<p>
A <strong>backend contract</strong> is the standardized handoff description by which a lowered FROG execution form declares:
</p>

<ul>
  <li>what executable content is being offered for consumption,</li>
  <li>under which assumptions it was lowered,</li>
  <li>which capabilities are required,</li>
  <li>which execution-relevant distinctions remain explicit or encoded,</li>
  <li>which source-aligned attribution obligations still apply,</li>
  <li>which later-stage freedoms remain allowed.</li>
</ul>

<p>
It is therefore a <strong>consumption contract</strong>, not merely a graph dump.
</p>

<p>
It tells the next stage:
</p>

<pre><code>"You may consume this lowered form
under these assumptions,
with these required preserved meanings,
and with these remaining obligations."</code></pre>

<hr/>

<h2 id="contract-parties">8. Contract Parties</h2>

<p>
Two abstract parties are involved:
</p>

<h3>8.1 Producer</h3>

<p>
The <strong>producer</strong> is the stage that emits the backend-facing contract.
It is typically a lowering stage or a chain of lowering stages.
</p>

<h3>8.2 Consumer</h3>

<p>
The <strong>consumer</strong> is the later stage that accepts the contract and turns it into more specific realization.
Examples include:
</p>

<ul>
  <li>a compiler frontend for one backend family,</li>
  <li>a scheduler-preparation stage,</li>
  <li>a code generator,</li>
  <li>a runtime deployment preparer,</li>
  <li>a target binding stage,</li>
  <li>a hybrid interpreter/JIT intake stage.</li>
</ul>

<p>
The backend contract exists so that these parties do not need to rely on undocumented private assumptions.
</p>

<hr/>

<h2 id="contract-boundary">9. Contract Boundary</h2>

<p>
The backend contract is the first stage where a lowered representation may legitimately say:
</p>

<ul>
  <li>which target family it is oriented toward,</li>
  <li>which scheduling assumptions are already fixed,</li>
  <li>which placement or storage choices are already specialized,</li>
  <li>which remaining freedoms are left to the consumer.</li>
</ul>

<p>
That boundary can be visualized as:
</p>

<pre><code>🟦 Execution IR
   - open
   - source-shaped enough for inspection
   - semantically close to validated meaning

🟧 Lowering
   - specialization begins
   - structure may be expanded or flattened
   - storage / layout / scheduling may become more explicit

🟨 Backend Contract
   - standardized statement of what is now consumable
   - standardized statement of assumptions and obligations

🟥 Private realization
   - consumer-specific internals
   - runtime-private objects
   - backend-private scheduling machinery
</code></pre>

<hr/>

<h2 id="minimum-preconditions">10. Minimum Preconditions</h2>

<p>
A backend contract MUST only be emitted after:
</p>

<ul>
  <li>the program has already been validated,</li>
  <li>Execution IR construction was semantically legitimate,</li>
  <li>the performed lowering steps are semantically preserving,</li>
  <li>all declared assumptions relevant to the contract have been made explicit.</li>
</ul>

<p>
A backend contract MUST NOT be used to hide:
</p>

<ul>
  <li>invalid source structure,</li>
  <li>invalid cycles,</li>
  <li>invalid memory semantics,</li>
  <li>unsupported structure semantics silently rewritten into a different meaning.</li>
</ul>

<hr/>

<h2 id="backend-family-and-contract-identity">11. Backend Family and Contract Identity</h2>

<p>
Every backend contract SHOULD identify:
</p>

<ul>
  <li>its contract kind,</li>
  <li>its contract version,</li>
  <li>its backend family orientation,</li>
  <li>its producer identity where useful,</li>
  <li>its compatibility or expectation level.</li>
</ul>

<p>
A backend family is not necessarily one vendor product.
It is a class of consumers that share sufficiently similar realization assumptions.
</p>

<p>
Examples of backend-family orientation may include:
</p>

<ul>
  <li>native compiled single-process execution,</li>
  <li>deterministic static-schedule runtime,</li>
  <li>host/device split execution,</li>
  <li>distributed message-oriented realization,</li>
  <li>embedded resource-constrained realization,</li>
  <li>hybrid interpretive execution.</li>
</ul>

<p>
This document does not freeze a universal taxonomy for all time.
It only requires that the chosen backend-family orientation be explicit enough for the consumer not to guess blindly.
</p>

<hr/>

<h2 id="required-contract-sections">12. Required Contract Sections</h2>

<p>
A conforming backend contract SHOULD be representable through the sections below, even if the exact transport shape differs across implementations.
</p>

<h3 id="contract-header">12.1 Contract header</h3>

<p>
The header SHOULD identify:
</p>

<ul>
  <li>contract kind,</li>
  <li>contract version,</li>
  <li>backend-family orientation,</li>
  <li>producer identifier where relevant,</li>
  <li>compatibility declaration.</li>
</ul>

<p>
Example conceptual fields:
</p>

<pre><code>{
  "kind": "frog_backend_contract",
  "contract_version": "0.1",
  "backend_family": "deterministic_static_schedule",
  "producer": "example_lowering_pipeline",
  "compatibility": "family_specific"
}</code></pre>

<h3 id="capability-and-assumption-section">12.2 Capability and assumption section</h3>

<p>
This section MUST make explicit what the consumer is expected to support.
</p>

<p>
It SHOULD include:
</p>

<ul>
  <li>required intrinsic primitive references,</li>
  <li>required profile families if any,</li>
  <li>required execution-domain assumptions,</li>
  <li>required data-representation assumptions,</li>
  <li>required state-handling assumptions,</li>
  <li>required scheduling model assumptions if fixed,</li>
  <li>required boundary or ABI conventions if already specialized.</li>
</ul>

<p>
The key rule is:
</p>

<pre><code>declared requirement
    may be assumed by the consumer

undeclared requirement
    MUST NOT be silently assumed
</code></pre>

<h3 id="consumable-executable-section">12.3 Consumable executable section</h3>

<p>
This section defines what executable units or realizable units the consumer is actually being asked to consume.
</p>

<p>
It SHOULD identify, where relevant:
</p>

<ul>
  <li>entry units,</li>
  <li>callable units,</li>
  <li>partitioned execution units,</li>
  <li>lowered objects and relations,</li>
  <li>domain or device partitions,</li>
  <li>inter-unit boundaries.</li>
</ul>

<p>
This section MUST be rich enough that the consumer does not need to reconstruct the program blindly from private out-of-band assumptions.
</p>

<h3 id="boundary-section">12.4 Boundary section</h3>

<p>
This section defines how relevant boundaries have been specialized.
</p>

<p>
It SHOULD cover, where applicable:
</p>

<ul>
  <li>public program boundaries,</li>
  <li>sub-FROG call boundaries,</li>
  <li>cross-domain boundaries,</li>
  <li>host/device transfer boundaries,</li>
  <li>profile-owned foreign or interop boundaries,</li>
  <li>UI interaction boundaries when they remain relevant to the backend family.</li>
</ul>

<p>
A consumer MUST remain able to distinguish:
</p>

<ul>
  <li>public interface boundaries,</li>
  <li>internal execution edges,</li>
  <li>cross-domain transfer boundaries,</li>
  <li>external capability or profile-owned boundaries.</li>
</ul>

<h3 id="state-and-memory-section">12.5 State and memory section</h3>

<p>
This section defines how explicit source-semantic memory has been carried into backend-facing form.
</p>

<p>
It SHOULD identify:
</p>

<ul>
  <li>state-bearing objects or state cells,</li>
  <li>initialization obligations,</li>
  <li>update or commit boundaries,</li>
  <li>loop-carried state where relevant,</li>
  <li>transfer or lifetime constraints where relevant.</li>
</ul>

<p>
Most importantly, it MUST remain true that:
</p>

<pre><code>explicit semantic memory
      remains
explicitly representable as semantic memory

even if

its storage realization becomes backend-specific
</code></pre>

<h3 id="placement-scheduling-and-domain-section">12.6 Placement, scheduling, and domain section</h3>

<p>
If lowering already fixed placement, work clustering, or scheduling constraints, those decisions MUST be stated here.
</p>

<p>
This section MAY include:
</p>

<ul>
  <li>execution domains,</li>
  <li>device assignments,</li>
  <li>partition ownership,</li>
  <li>deterministic scheduling constraints,</li>
  <li>ordering constraints,</li>
  <li>parallelism permissions or prohibitions,</li>
  <li>resource constraints relevant to correct consumption.</li>
</ul>

<p>
If such decisions are <strong>not</strong> fixed yet, the contract SHOULD say so explicitly rather than leaving ambiguity.
</p>

<h3 id="attribution-and-diagnostics-section">12.7 Attribution and diagnostics section</h3>

<p>
This section defines what source-aligned attribution the consumer MUST preserve or remain able to reconstruct.
</p>

<p>
It SHOULD include information equivalent to:
</p>

<ul>
  <li>source contributor references,</li>
  <li>Execution IR contributor references,</li>
  <li>lowering relation category,</li>
  <li>structure and region origin where relevant,</li>
  <li>state-origin identity where relevant,</li>
  <li>fault-attribution anchors where available,</li>
  <li>debug-stop-relevant anchors where available.</li>
</ul>

<p>
The purpose is not to standardize one debugger transport.
The purpose is to prevent the consumer from destroying source-aligned diagnosability.
</p>

<h3 id="rejection-and-unsupported-features-section">12.8 Rejection and unsupported-features section</h3>

<p>
A contract SHOULD be able to declare features that the intended consumer family:
</p>

<ul>
  <li>requires,</li>
  <li>supports conditionally,</li>
  <li>does not support,</li>
  <li>must reject if encountered.</li>
</ul>

<p>
This matters because correct rejection is architecturally better than silent semantic laundering.
</p>

<hr/>

<h2 id="producer-obligations">13. Producer Obligations</h2>

<p>
A conforming producer of a backend contract MUST:
</p>

<ul>
  <li>preserve validated meaning through lowering,</li>
  <li>declare the backend-family orientation explicitly,</li>
  <li>declare assumptions the consumer is expected to rely on,</li>
  <li>preserve enough attribution for diagnostics and source-aligned reasoning,</li>
  <li>declare unsupported or unresolved requirements explicitly,</li>
  <li>avoid pretending that private realization details are already language truth.</li>
</ul>

<p>
A producer MUST NOT:
</p>

<ul>
  <li>hide semantic repair inside the contract,</li>
  <li>erase explicit local-memory meaning,</li>
  <li>collapse all boundaries into one opaque transport class,</li>
  <li>claim that one private runtime graph is the normative FROG execution model,</li>
  <li>silently require undeclared profile capabilities.</li>
</ul>

<hr/>

<h2 id="consumer-obligations">14. Consumer Obligations</h2>

<p>
A conforming consumer of a backend contract MUST either:
</p>

<ul>
  <li>accept the contract and preserve its declared obligations, or</li>
  <li>reject the contract explicitly.</li>
</ul>

<p>
A consumer MUST NOT:
</p>

<ul>
  <li>reinterpret undeclared freedoms as fixed requirements,</li>
  <li>reinterpret fixed requirements as optional freedoms,</li>
  <li>erase source-aligned attribution that the contract declares necessary,</li>
  <li>change state semantics while claiming faithful consumption,</li>
  <li>erase required public-boundary or structure-origin distinctions if later diagnostics depend on them.</li>
</ul>

<p>
A consumer MAY:
</p>

<ul>
  <li>refine scheduling detail,</li>
  <li>refine storage realization,</li>
  <li>introduce backend-private support objects,</li>
  <li>perform further family-specific specialization,</li>
  <li>hide private realization details from open layers.</li>
</ul>

<p>
But it MAY do so only while respecting the contract’s preserved obligations.
</p>

<hr/>

<h2 id="preservation-invariants">15. Preservation Invariants</h2>

<p>
Across the backend contract boundary, the following invariants remain mandatory:
</p>

<ul>
  <li>validated language-level behavior MUST remain semantically equivalent,</li>
  <li>explicit state semantics MUST remain semantically explicit,</li>
  <li>public interface meaning MUST remain recoverable where relevant,</li>
  <li>structure and region meaning MUST remain recoverable where relevant,</li>
  <li>source-aligned diagnostic anchors MUST remain preservable where relevant,</li>
  <li>profile-owned capability requirements MUST remain explicit rather than implicit.</li>
</ul>

<p>
This can be summarized as:
</p>

<pre><code>🟦 semantic truth
      stays true

🟧 specialization
      may grow

🟨 contract obligations
      must stay explicit

🟥 private realization
      may vary

🟩 source-aligned diagnosability
      must remain supportable
</code></pre>

<hr/>

<h2 id="control-structures-state-and-boundaries">16. Control Structures, State, and Boundaries</h2>

<h3>16.1 Structured control</h3>

<p>
A backend contract MAY expose lowered branch, dispatch, or loop machinery instead of source-shaped structures.
However, where relevant for diagnostics, fault attribution, or source-aligned observability, it MUST preserve enough information to relate those lowered elements back to:
</p>

<ul>
  <li>structure family,</li>
  <li>structure activation,</li>
  <li>region origin,</li>
  <li>loop-carried state origin.</li>
</ul>

<h3>16.2 Explicit memory</h3>

<p>
A backend contract MUST NOT erase the fact that valid feedback depended on explicit local memory.
</p>

<p>
A useful sketch is:
</p>

<pre><code>🟦 source-semantic idea
   [frog.core.delay] --> [add] --> next

🟧 lowered form
   [state_read] --> [lowered_add] --> [state_commit]

🟨 backend contract truth
   state_read/state_commit
      implement
   explicit semantic local memory

🟥 private runtime freedom
   register / buffer slot / retained object / state cell
</code></pre>

<h3>16.3 Public boundaries</h3>

<p>
A backend contract MAY translate public boundaries into ABI arguments, transport endpoints, or domain endpoints.
But it MUST still preserve enough distinction that a consumer can tell:
</p>

<ul>
  <li>which boundaries are public program boundaries,</li>
  <li>which are internal edges only,</li>
  <li>which are domain-transfer points,</li>
  <li>which are external capability boundaries.</li>
</ul>

<hr/>

<h2 id="observability-debugging-and-fault-attribution">17. Observability, Debugging, and Fault Attribution</h2>

<p>
This document does not define debugger UI, probe rendering, watch transport, or event protocol.
</p>

<p>
However, it MUST remain compatible with later layers that need:
</p>

<ul>
  <li>source-aligned observability,</li>
  <li>pause-consistent snapshots,</li>
  <li>safe debug stop attribution,</li>
  <li>fault-relevant source attribution where possible.</li>
</ul>

<p>
Accordingly, a backend contract SHOULD preserve or expose enough attribution to support:
</p>

<ul>
  <li>mapping lowered activities back to source-visible targets,</li>
  <li>mapping lowered fault sites back to meaningful source contributors where possible,</li>
  <li>mapping lowered execution contexts back to source-relevant execution context,</li>
  <li>mapping structure-lowered activity back to selected structure or region semantics where relevant.</li>
</ul>

<p>
The rule is:
</p>

<pre><code>🟥 backend-private detail
        is allowed

🟩 loss of source-aligned diagnosability
        is not allowed when the contract claims support for it
</code></pre>

<hr/>

<h2 id="relation-with-profiles-libraries-and-conformance">18. Relation with Profiles, Libraries, and Conformance</h2>

<h3>18.1 Relation with Libraries</h3>

<p>
A backend contract MUST NOT redefine intrinsic primitive catalogs.
It MAY reference intrinsic primitive identities and lowered consumption consequences.
</p>

<h3>18.2 Relation with Profiles</h3>

<p>
A backend contract MUST NOT redefine profile-owned capability families.
It MAY declare that specific profile support is required by the lowered form.
</p>

<h3>18.3 Relation with conformance</h3>

<p>
This document is not yet a full conformance policy.
However, it lays the groundwork for later conformance by making backend-facing obligations explicit instead of leaving them private.
</p>

<p>
A future conformance layer MAY distinguish:
</p>

<ul>
  <li>core FROG consumption,</li>
  <li>core FROG plus named profile consumption,</li>
  <li>backend-family-specific compatibility claims,</li>
  <li>certified compatibility claims under steward policy.</li>
</ul>

<hr/>

<h2 id="minimal-conceptual-shape">19. Minimal Conceptual Shape</h2>

<p>
This document does not freeze one mandatory serialized format.
Still, a conforming backend contract SHOULD be representable in a conceptual shape equivalent to:
</p>

<pre><code>{
  "kind": "frog_backend_contract",
  "contract_version": "0.1",
  "backend_family": "host_device_split",
  "assumptions": {
    "profiles_required": ["interop.example"],
    "state_model": "explicit_local_memory_preserved",
    "scheduling": {
      "fixed": false
    }
  },
  "units": [
    {
      "id": "main",
      "role": "entry_unit",
      "objects": [],
      "connections": [],
      "boundaries": [],
      "state": [],
      "placement": [],
      "attribution": {}
    }
  ],
  "diagnostic_support": {
    "source_mapping_available": true,
    "fault_anchor_support": true,
    "debug_anchor_support": true
  },
  "unsupported": []
}
</code></pre>

<p>
The exact field names are indicative only.
What matters is the presence of information equivalent to:
</p>

<ul>
  <li>contract identity,</li>
  <li>backend-family orientation,</li>
  <li>declared assumptions,</li>
  <li>consumable units,</li>
  <li>boundary semantics,</li>
  <li>state semantics,</li>
  <li>attribution support,</li>
  <li>unsupported-feature declaration.</li>
</ul>

<hr/>

<h2 id="contract-lifecycle">20. Contract Lifecycle</h2>

<p>
A useful mental model is:
</p>

<pre><code>🟦 validated meaning
        |
        v
🟦 Execution IR
        |
        v
🟧 Lowering step(s)
        |
        +--> adds specialization
        +--> fixes assumptions
        +--> preserves mapping
        |
        v
🟨 Backend Contract
        |
        +--> accepted by consumer
        |        |
        |        v
        |    🟥 private realization
        |
        +--> rejected by consumer
                 |
                 v
            explicit incompatibility
</code></pre>

<p>
This lifecycle matters because explicit rejection is preferable to silent reinterpretation.
</p>

<hr/>

<h2 id="examples">21. Examples</h2>

<h3>21.1 Deterministic static-schedule backend family</h3>

<p>
A lowering pipeline may emit a backend contract that states:
</p>

<ul>
  <li>schedule constraints are already fixed,</li>
  <li>parallel freedom is restricted,</li>
  <li>state commit order is fixed,</li>
  <li>source mapping remains available for diagnostics.</li>
</ul>

<p>
A consumer in that backend family may rely on the fixed schedule constraints.
A consumer outside that family MUST reject or re-lower rather than guessing.
</p>

<h3>21.2 Host/device split backend family</h3>

<p>
A contract may declare:
</p>

<ul>
  <li>specific execution domains,</li>
  <li>device-transfer boundaries,</li>
  <li>host-visible vs device-resident state categories,</li>
  <li>fault anchors on cross-domain transfer points.</li>
</ul>

<p>
The consumer may then generate device-specific realization while preserving the source-aligned boundary anchors where relevant.
</p>

<h3>21.3 ABI-oriented callable unit</h3>

<pre><code>🟦 source-facing idea
   interface_input[a] --> add --> interface_output[result]

🟧 lowered executable idea
   abi_arg[0] --> op_add --> abi_ret[0]

🟨 backend contract truth
   - public boundary origin preserved
   - callable unit identity preserved
   - ABI assumption declared explicitly

🟥 runtime/private realization
   - register assignment
   - stack slot usage
   - calling stub implementation
</code></pre>

<h3>21.4 Explicit delay preserved across contract handoff</h3>

<pre><code>🟦 semantic requirement
   valid feedback requires explicit local memory

🟧 lowered realization-facing form
   state_read -> op -> state_commit

🟨 backend contract requirement
   consumer MUST preserve state semantics
   consumer MUST NOT reinterpret this as pure combinational flow

🟥 private runtime freedom
   storage mechanism remains implementation-specific
</code></pre>

<hr/>

<h2 id="out-of-scope-for-v01">22. Out of Scope for v0.1</h2>

<p>
The following remain out of scope for this document in v0.1:
</p>

<ul>
  <li>one frozen universal backend-family taxonomy,</li>
  <li>one frozen binary or JSON exchange format,</li>
  <li>one universal ABI descriptor model,</li>
  <li>one universal schedule encoding,</li>
  <li>one universal debugger event payload format,</li>
  <li>one full cross-vendor conformance test suite for all backend families,</li>
  <li>one universal deployment package model,</li>
  <li>one mandatory runtime-private representation.</li>
</ul>

<p>
The goal of v0.1 is narrower and more architectural:
</p>

<pre><code>define a clean, explicit, durable handoff
between lowering and later realization
without collapsing FROG into one implementation pipeline
</code></pre>
