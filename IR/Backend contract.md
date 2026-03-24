<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG IR Backend Contract</h1>

<p align="center">
  <strong>Normative consumption contract for lowered execution forms in FROG v0.1</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#boundary-contract">2. Boundary Contract</a></li>
  <li><a href="#position-in-the-pipeline">3. Position in the Pipeline</a></li>
  <li><a href="#scope">4. Scope</a></li>
  <li><a href="#non-goals">5. Non-Goals</a></li>
  <li><a href="#core-definition">6. Core Definition</a></li>
  <li><a href="#contract-parties">7. Contract Parties</a></li>
  <li><a href="#backend-family-target-profile-and-runtime-boundary">8. Backend Family, Target Profile, and Runtime Boundary</a></li>
  <li><a href="#contract-identity-and-backend-family">9. Contract Identity and Backend Family</a></li>
  <li><a href="#contract-boundary">10. Contract Boundary</a></li>
  <li><a href="#minimum-preconditions">11. Minimum Preconditions</a></li>
  <li><a href="#required-contract-content">12. Required Contract Content</a></li>
  <li><a href="#producer-obligations">13. Producer Obligations</a></li>
  <li><a href="#consumer-obligations">14. Consumer Obligations</a></li>
  <li><a href="#preservation-invariants">15. Preservation Invariants</a></li>
  <li><a href="#control-state-and-boundaries">16. Control, State, and Boundaries</a></li>
  <li><a href="#ui-participation">17. UI Participation</a></li>
  <li><a href="#diagnostics-observability-and-fault-attribution">18. Diagnostics, Observability, and Fault Attribution</a></li>
  <li><a href="#relation-with-libraries-profiles-and-conformance">19. Relation with Libraries, Profiles, and Conformance</a></li>
  <li><a href="#minimal-conceptual-shape">20. Minimal Conceptual Shape</a></li>
  <li><a href="#contract-lifecycle">21. Contract Lifecycle</a></li>
  <li><a href="#out-of-scope-for-v01">22. Out of Scope for v0.1</a></li>
  <li><a href="#summary">23. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the <strong>backend contract</strong> for FROG v0.1.
</p>

<p>
The backend contract is the first standardized <strong>consumer-facing handoff</strong> after lowering.
It defines what a later compiler stage, backend stage, execution-preparation stage, deployment-preparation stage, or runtime intake stage
may rely on when consuming a lowered FROG execution form.
</p>

<p>
It exists to keep the following layers distinct:
</p>

<ul>
  <li>the open, inspectable, source-attributable Execution IR,</li>
  <li>the specialization space of lowering,</li>
  <li>the standardized consumer-facing handoff,</li>
  <li>the private realization that follows.</li>
</ul>

<pre><code>validated program meaning
        |
        v
open Execution IR
        |
        v
lowering
        |
        v
backend contract
        |
        v
private realization
</code></pre>

<p>
The backend contract is therefore:
</p>

<ul>
  <li>not the open IR itself,</li>
  <li>not the whole lowering space,</li>
  <li>not one private runtime representation,</li>
  <li>not one vendor ABI,</li>
  <li>not one mandatory executable artifact format.</li>
</ul>

<hr/>

<h2 id="boundary-contract">2. Boundary Contract</h2>

<p>
The backend contract is the standardized declaration by which a lowered execution form says:
</p>

<ul>
  <li>what executable content is being offered for consumption,</li>
  <li>which backend-facing assumptions are already fixed,</li>
  <li>which capabilities are required,</li>
  <li>which execution-relevant distinctions remain explicit or encoded,</li>
  <li>which source-aligned attribution obligations still apply,</li>
  <li>which later-stage freedoms remain available to the consumer,</li>
  <li>which situations must be rejected rather than silently reinterpreted.</li>
</ul>

<p>
It is therefore a <strong>consumption contract</strong>, not merely a lowered graph dump.
</p>

<p>
In practical terms, the contract says:
</p>

<pre><code>"You may consume this lowered form
under these assumptions,
with these preserved meanings,
and with these remaining obligations."</code></pre>

<p>
A backend contract is not necessarily identical to the lowered artifact itself.
A backend contract may be:
</p>

<ul>
  <li>embedded in a lowered artifact,</li>
  <li>stored alongside it,</li>
  <li>represented through a dedicated contract payload,</li>
  <li>represented through another equivalent explicit mechanism.</li>
</ul>

<p>
What matters is not one transport syntax.
What matters is the presence of a standardized, explicit consumer-facing handoff.
</p>

<hr/>

<h2 id="position-in-the-pipeline">3. Position in the Pipeline</h2>

<p>
The intended architecture is:
</p>

<pre><code>canonical source (.frog)
        |
        v
validated program meaning
        |
        v
Execution IR
  - open
  - inspectable
  - source-attributable
  - not backend-private
        |
        v
Lowering
  - specialization begins
        |
        v
Backend Contract
  - standardized consumable handoff
        |
        v
compiler / backend / deployment / runtime realization
</code></pre>

<p>
The key interpretation rule is:
</p>

<ul>
  <li><strong>Execution IR</strong> remains the open execution-facing representation.</li>
  <li><strong>Lowering</strong> is where specialization begins.</li>
  <li><strong>Backend Contract</strong> is where consumer assumptions become explicit.</li>
  <li><strong>Private realization</strong> remains downstream and is not standardized here.</li>
</ul>

<p>
The backend contract therefore sits:
</p>

<ul>
  <li>after lowering has begun,</li>
  <li>before private realization takes over.</li>
</ul>

<hr/>

<h2 id="scope">4. Scope</h2>

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

<p>
This document owns the <strong>standardized consumable handoff boundary</strong>.
</p>

<p>
It does not own:
</p>

<ul>
  <li>the full lowering transformation space,</li>
  <li>the full private runtime realization,</li>
  <li>the full observability protocol,</li>
  <li>the full debugger protocol,</li>
  <li>the full deployment artifact model.</li>
</ul>

<hr/>

<h2 id="non-goals">5. Non-Goals</h2>

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
  <li>one mandatory runtime-private state object model,</li>
  <li>one mandatory runtime-module layout.</li>
</ul>

<p>
This document also does not move semantic ownership away from:
</p>

<ul>
  <li><code>Expression/</code> for canonical source,</li>
  <li><code>Language/</code> for validated execution meaning,</li>
  <li><code>Libraries/</code> for intrinsic primitive identities and primitive-local behavior,</li>
  <li><code>Profiles/</code> for optional standardized capability families,</li>
  <li><code>IDE/</code> for tool-facing projection and observability behavior.</li>
</ul>

<p>
This document is also not the place to standardize:
</p>

<ul>
  <li>a first-class event execution model for UI,</li>
  <li>a general asynchronous callback model,</li>
  <li>one universal consumer-private execution architecture.</li>
</ul>

<hr/>

<h2 id="core-definition">6. Core Definition</h2>

<p>
A backend contract is the standardized handoff description by which a lowered FROG execution form declares:
</p>

<ul>
  <li>what executable content is consumable,</li>
  <li>which backend-family assumptions are already fixed,</li>
  <li>which additional capability assumptions are required,</li>
  <li>which execution-relevant distinctions are still meaningful,</li>
  <li>which source-aligned attribution obligations still apply,</li>
  <li>which remaining freedoms are left to the consumer.</li>
</ul>

<p>
A backend contract is therefore not just a payload.
It is an explicit statement of <strong>consumable truth</strong> for a backend-oriented consumer.
</p>

<pre><code>Execution IR
   -&gt; open execution-facing form

Lowering
   -&gt; specialization

Backend Contract
   -&gt; standardized consumable assumptions and obligations

Private realization
   -&gt; consumer-specific execution machinery
</code></pre>

<hr/>

<h2 id="contract-parties">7. Contract Parties</h2>

<h3>7.1 Producer</h3>

<p>
The <strong>producer</strong> is the stage that emits the backend contract.
It is typically:
</p>

<ul>
  <li>one lowering stage, or</li>
  <li>a chain of lowering stages.</li>
</ul>

<h3>7.2 Consumer</h3>

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
  <li>a hybrid interpreter or JIT intake stage,</li>
  <li>a reference host runtime intake stage.</li>
</ul>

<p>
The backend contract exists so that those parties do not need to rely on undocumented private assumptions.
</p>

<hr/>

<h2 id="backend-family-target-profile-and-runtime-boundary">8. Backend Family, Target Profile, and Runtime Boundary</h2>

<p>
The backend contract sits at a boundary where several related concepts must remain distinct.
</p>

<h3>8.1 Backend family</h3>

<p>
A <strong>backend family</strong> is the downstream execution-consumption family that the lowered form is oriented toward.
It identifies the class of consumer expected to accept the contract.
</p>

<p>
A backend family is therefore a contract-facing classification.
It is neither identical to the open Execution IR nor identical to one private runtime implementation.
</p>

<h3>8.2 Target profile</h3>

<p>
A <strong>target profile</strong> is a class of execution assumptions, constraints, and capability expectations relevant to the intended target posture.
A target profile may influence lowering choices and may affect which backend families are viable.
</p>

<p>
A target profile is not identical to a backend family.
Different backend families may target the same broad target-profile class.
Likewise, one backend family may admit more than one target posture if the contract states the assumptions explicitly enough.
</p>

<h3>8.3 Deployment mode</h3>

<p>
A <strong>deployment mode</strong> is a packaging and execution-exposure posture such as development-oriented execution,
debug-oriented execution, release-oriented execution, self-contained delivery, or shared-runtime delivery.
</p>

<p>
A deployment mode is not itself the program meaning and is not itself a backend family.
It may, however, affect what later realization stages choose to bundle, expose, or omit.
</p>

<h3>8.4 Runtime-private realization</h3>

<p>
A <strong>runtime-private realization</strong> is the consumer-private execution machinery that eventually accepts the contract and makes execution happen.
This may include runtime modules, host bindings, schedulers, retained state objects, transport adapters, or private support objects.
</p>

<p>
Such realization details remain downstream from this document.
They are not standardized here merely because they exist in an implementation.
</p>

<h3>8.5 Required distinction at the contract boundary</h3>

<p>
Accordingly:
</p>

<ul>
  <li>a backend contract MAY declare backend-family orientation explicitly,</li>
  <li>a backend contract MAY declare required target-profile assumptions explicitly,</li>
  <li>a backend contract MAY declare deployment-relevant assumptions explicitly where they matter to correct consumption,</li>
  <li>but a backend contract MUST NOT collapse backend family, target profile, deployment mode, and runtime-private realization into one undifferentiated concept.</li>
</ul>

<p>
This distinction matters because the same validated FROG meaning may legitimately be consumed:
</p>

<ul>
  <li>by different backend families,</li>
  <li>for different target postures,</li>
  <li>under different deployment modes,</li>
  <li>through different runtime-private realizations.</li>
</ul>

<p>
The contract boundary must therefore keep assumptions explicit without turning one private implementation layout into hidden language law.
</p>

<hr/>

<h2 id="contract-identity-and-backend-family">9. Contract Identity and Backend Family</h2>

<p>
Every backend contract MUST identify:
</p>

<ul>
  <li>its contract kind,</li>
  <li>its contract version,</li>
  <li>its backend-family orientation.</li>
</ul>

<p>
Every backend contract SHOULD also identify, where useful:
</p>

<ul>
  <li>its producer identity,</li>
  <li>its compatibility or expectation level,</li>
  <li>its contract flavor or contract profile if one exists for that backend family,</li>
  <li>its required target-profile assumptions,</li>
  <li>its relevant deployment-mode assumptions when those materially affect correct consumption.</li>
</ul>

<p>
A backend family is not necessarily one vendor product.
It is a class of consumers that share sufficiently similar realization assumptions.
</p>

<p>
Examples of backend-family orientation may include:
</p>

<ul>
  <li><code>native_single_process_host</code>,</li>
  <li><code>deterministic_static_schedule</code>,</li>
  <li><code>host_device_split</code>,</li>
  <li><code>distributed_message_oriented</code>,</li>
  <li><code>embedded_resource_constrained</code>,</li>
  <li><code>hybrid_interpretive</code>,</li>
  <li><code>reference_host_runtime_ui_binding</code>.</li>
</ul>

<p>
This document does not freeze a universal taxonomy for all time.
It only requires that the chosen backend-family orientation be explicit enough for the consumer not to guess blindly.
</p>

<hr/>

<h2 id="contract-boundary">10. Contract Boundary</h2>

<p>
The backend contract is the first stage where a lowered representation may legitimately say:
</p>

<ul>
  <li>which backend family it is oriented toward,</li>
  <li>which target-profile assumptions are already required,</li>
  <li>which deployment-relevant assumptions materially affect correct consumption,</li>
  <li>which scheduling assumptions are already fixed,</li>
  <li>which placement, partitioning, or storage choices are already specialized,</li>
  <li>which remaining freedoms are left to the consumer.</li>
</ul>

<p>
This boundary can be visualized as:
</p>

<pre><code>Execution IR
  - open
  - source-shaped enough for inspection
  - semantically close to validated meaning

Lowering
  - specialization begins
  - structure may be expanded, clustered, or flattened
  - storage / layout / scheduling may become more explicit

Backend Contract
  - standardized statement of what is now consumable
  - standardized statement of assumptions and obligations

Private realization
  - consumer-specific internals
  - runtime-private objects
  - backend-private scheduling machinery
  - deployment-private bundling choices
</code></pre>

<p>
The contract boundary is therefore the point where a consumer is allowed to rely on <strong>declared assumptions</strong> without guessing.
Undeclared assumptions remain outside the contract.
</p>

<hr/>

<h2 id="minimum-preconditions">11. Minimum Preconditions</h2>

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
  <li>unsupported structure semantics silently rewritten into different meaning,</li>
  <li>collapsed boundary distinctions that are still required by the consumer-facing handoff.</li>
</ul>

<pre><code>No valid lowered basis
        |
        v
No conforming backend contract claim
</code></pre>

<hr/>

<h2 id="required-contract-content">12. Required Contract Content</h2>

<p>
A conforming backend contract MUST be representable through content semantically equivalent to the categories below,
even if the exact transport shape differs across implementations.
</p>

<h3>12.1 Header</h3>

<p>
The header MUST identify:
</p>

<ul>
  <li>contract kind,</li>
  <li>contract version,</li>
  <li>backend-family orientation.</li>
</ul>

<h3>12.2 Assumptions and capabilities</h3>

<p>
The contract MUST make explicit what the consumer is expected to support.
That SHOULD include, where relevant:
</p>

<ul>
  <li>required intrinsic primitive references,</li>
  <li>required profile families,</li>
  <li>required target-profile assumptions,</li>
  <li>required deployment-relevant assumptions,</li>
  <li>required execution-domain assumptions,</li>
  <li>required data-representation assumptions,</li>
  <li>required state-handling assumptions,</li>
  <li>required scheduling-model assumptions if fixed,</li>
  <li>required boundary or ABI conventions if already specialized,</li>
  <li>required UI-binding assumptions when the backend family still carries UI participation semantics.</li>
</ul>

<p>
The rule is:
</p>

<pre><code>declared requirement
    may be assumed by the consumer

undeclared requirement
    MUST NOT be silently assumed
</code></pre>

<h3>12.3 Consumable executable units</h3>

<p>
The contract MUST define what executable units or realizable units the consumer is actually being asked to consume.
That SHOULD identify, where relevant:
</p>

<ul>
  <li>entry units,</li>
  <li>callable units,</li>
  <li>partitioned execution units,</li>
  <li>lowered objects and relations,</li>
  <li>domain or device partitions,</li>
  <li>inter-unit boundaries,</li>
  <li>contract-visible UI interaction objects when present for that backend family.</li>
</ul>

<h3>12.4 Boundaries</h3>

<p>
The contract MUST define how relevant boundaries have been specialized.
That SHOULD cover, where applicable:
</p>

<ul>
  <li>public program boundaries,</li>
  <li>sub-FROG call boundaries,</li>
  <li>cross-domain boundaries,</li>
  <li>host/device transfer boundaries,</li>
  <li>profile-owned foreign or interop boundaries,</li>
  <li>UI interaction boundaries when they remain relevant to the backend family.</li>
</ul>

<h3>12.5 State and memory</h3>

<p>
The contract MUST define how explicit source-semantic memory has been carried into backend-facing form.
That SHOULD identify:
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

<h3>12.6 Placement, scheduling, and domains</h3>

<p>
If lowering already fixed placement, work clustering, partitioning, or scheduling constraints,
those decisions MUST be stated here.
If such decisions are not fixed yet,
the contract SHOULD say so explicitly rather than leaving ambiguity.
</p>

<h3>12.7 Attribution and diagnostics</h3>

<p>
The contract MUST define what source-aligned attribution the consumer MUST preserve or remain able to reconstruct.
That SHOULD include information equivalent to:
</p>

<ul>
  <li>source contributor references,</li>
  <li>Execution IR contributor references,</li>
  <li>lowering relation category,</li>
  <li>structure and region origin where relevant,</li>
  <li>state-origin identity where relevant,</li>
  <li>fault-attribution anchors where available,</li>
  <li>debug-stop-relevant anchors where available,</li>
  <li>UI-participation origin where relevant.</li>
</ul>

<h3>12.8 Unsupported features and rejection conditions</h3>

<p>
A contract MUST be able to declare features that the intended consumer family:
</p>

<ul>
  <li>requires,</li>
  <li>supports conditionally,</li>
  <li>does not support,</li>
  <li>must reject if encountered.</li>
</ul>

<p>
Correct rejection is architecturally better than silent semantic laundering.
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
  <li>collapse backend-family orientation, target-profile assumptions, deployment-mode assumptions, and runtime-private realization into one undifferentiated classification,</li>
  <li>collapse public interface participation, <code>widget_value</code> participation, and <code>widget_reference</code>-driven UI interaction into one undifferentiated class when the distinction still matters to consumption or attribution,</li>
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
  <li>erase required public-boundary, structure-origin, or UI-origin distinctions if later diagnostics depend on them,</li>
  <li>reinterpret unsupported UI participation semantics as arbitrary runtime-private behavior while still claiming contract conformance.</li>
</ul>

<p>
A consumer MAY:
</p>

<ul>
  <li>refine scheduling detail,</li>
  <li>refine storage realization,</li>
  <li>introduce backend-private support objects,</li>
  <li>introduce deployment-private bundling choices,</li>
  <li>select runtime modules privately,</li>
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
  <li>UI participation meaning MUST remain recoverable where the contract claims support for it,</li>
  <li>source-aligned diagnostic anchors MUST remain preservable where relevant,</li>
  <li>profile-owned capability requirements MUST remain explicit rather than implicit,</li>
  <li>contract-facing target-profile assumptions MUST remain explicit rather than being silently deferred into runtime-private interpretation when they materially affect correct consumption.</li>
</ul>

<pre><code>semantic truth
      stays true

specialization
      may grow

contract obligations
      must stay explicit

private realization
      may vary

source-aligned diagnosability
      must remain supportable
</code></pre>

<hr/>

<h2 id="control-state-and-boundaries">16. Control, State, and Boundaries</h2>

<h3>16.1 Structured control</h3>

<p>
A backend contract MAY expose lowered branch, dispatch, or loop machinery instead of source-shaped structures.
However, where relevant for diagnostics, fault attribution, or source-aligned observability,
it MUST preserve enough information to relate those lowered elements back to:
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

<pre><code>source-semantic idea
   [frog.core.delay] --&gt; [add] --&gt; next

lowered form
   [state_read] --&gt; [lowered_add] --&gt; [state_commit]

backend contract truth
   state_read / state_commit
      implement
   explicit semantic local memory

private runtime freedom
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

<h3>16.4 Boundary truth before private realization</h3>

<p>
The backend contract is the last standardized point before private realization.
If a boundary distinction matters for correct execution, diagnosability, UI binding, compatibility checking, or target-compatibility checking,
it MUST still be explicit here rather than being deferred entirely into consumer-private interpretation.
</p>

<hr/>

<h2 id="ui-participation">17. UI Participation</h2>

<p>
Some backend families do not carry UI participation at all.
Others still need a consumable account of UI participation, especially reference runtimes or host runtimes that bind front-panel behavior to execution.
</p>

<p>
When UI participation remains relevant to the backend family, the contract MUST preserve enough information to distinguish:
</p>

<ul>
  <li>public interface participation,</li>
  <li><code>widget_value</code> participation,</li>
  <li><code>widget_reference</code> participation,</li>
  <li>standardized UI-object primitive operations performed through widget references.</li>
</ul>

<p>
For the purposes of a reference host runtime or similar family:
</p>

<ul>
  <li><code>widget_value</code> participation MAY be lowered into value channels, UI binding endpoints, or host-visible synchronized value cells,</li>
  <li><code>widget_reference</code> participation MAY be lowered into widget-handle references, widget slots, or equivalent backend-family handles,</li>
  <li><code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code> MAY be lowered into contract-visible callable interaction operations or operation descriptors,</li>
  <li>but the contract MUST NOT collapse those categories into one untyped generic endpoint concept if later runtime behavior or diagnostics still depends on the distinction.</li>
</ul>

<p>
A contract family MAY also state explicit UI synchronization assumptions such as:
</p>

<ul>
  <li>value propagation happens on deterministic execution steps,</li>
  <li>UI write-back points are explicit,</li>
  <li>UI refresh is host-managed rather than semantically part of the language core.</li>
</ul>

<p>
This document does not standardize:
</p>

<ul>
  <li>a first-class event execution model,</li>
  <li>registration-based event nodes,</li>
  <li>asynchronous callback delivery.</li>
</ul>

<p>
If a backend family supports richer UI eventing,
that support must be declared as a backend-family capability or as an external profile obligation rather than being silently assumed here.
</p>

<hr/>

<h2 id="diagnostics-observability-and-fault-attribution">18. Diagnostics, Observability, and Fault Attribution</h2>

<p>
This document does not define debugger UI, probe rendering, watch transport, or event protocol.
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
  <li>mapping structure-lowered activity back to structure or region semantics where relevant,</li>
  <li>mapping UI-related lowered activity back to widget participation or UI-object operation origin where relevant.</li>
</ul>

<p>
The rule is:
</p>

<pre><code>backend-private detail
        is allowed

loss of source-aligned diagnosability
        is not allowed when the contract claims support for it
</code></pre>

<hr/>

<h2 id="relation-with-libraries-profiles-and-conformance">19. Relation with Libraries, Profiles, and Conformance</h2>

<h3>19.1 Relation with Libraries</h3>

<p>
A backend contract MUST NOT redefine intrinsic primitive catalogs.
It MAY reference intrinsic primitive identities and lowered consumption consequences.
</p>

<h3>19.2 Relation with Profiles</h3>

<p>
A backend contract MUST NOT redefine profile-owned capability families.
It MAY declare that specific profile support is required by the lowered form.
</p>

<p>
When target-profile assumptions are relevant, the contract MAY reference profile-owned capability classes or equivalent declared assumptions,
but it MUST NOT pretend that one backend family or one runtime-private realization exhausts the meaning of those profile classes.
</p>

<h3>19.3 Relation with Conformance</h3>

<p>
This document is not yet a full conformance policy.
However, it lays groundwork for later conformance by making backend-facing obligations explicit instead of leaving them private.
</p>

<p>
A future conformance layer MAY distinguish:
</p>

<ul>
  <li>core FROG consumption,</li>
  <li>core FROG plus named profile consumption,</li>
  <li>backend-family-specific compatibility claims,</li>
  <li>target-profile-specific compatibility claims,</li>
  <li>certified compatibility claims under steward policy.</li>
</ul>

<hr/>

<h2 id="minimal-conceptual-shape">20. Minimal Conceptual Shape</h2>

<p>
This document does not freeze one mandatory serialized format.
Still, a conforming backend contract SHOULD be representable in a conceptual shape equivalent to:
</p>

<pre><code>{
  "kind": "frog_backend_contract",
  "contract_version": "0.1",
  "backend_family": "reference_host_runtime_ui_binding",
  "assumptions": {
    "profiles_required": [],
    "target_profiles_required": [],
    "deployment_mode_assumptions": [],
    "state_model": "explicit_local_memory_preserved",
    "scheduling": {
      "fixed": true,
      "family_rule": "deterministic_step_execution"
    },
    "ui_binding": {
      "enabled": true,
      "event_model": "not_standardized",
      "value_binding": "supported",
      "reference_binding": "supported"
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
The exact field names are illustrative only.
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

<pre><code>Minimal contract intent

contract identity
backend-family orientation
declared assumptions
consumable specialized units
attribution and diagnostic support
</code></pre>

<hr/>

<h2 id="contract-lifecycle">21. Contract Lifecycle</h2>

<p>
A useful mental model is:
</p>

<pre><code>validated meaning
        |
        v
Execution IR
        |
        v
Lowering step(s)
        |
        +-- adds specialization
        +-- fixes assumptions
        +-- preserves mapping
        |
        v
Backend Contract
        |
        +--&gt; accepted by consumer
        |        |
        |        v
        |    private realization
        |
        +--&gt; rejected by consumer
                 |
                 v
            explicit incompatibility
</code></pre>

<p>
This lifecycle matters because explicit rejection is preferable to silent reinterpretation.
</p>

<hr/>

<h2 id="out-of-scope-for-v01">22. Out of Scope for v0.1</h2>

<p>
The following remain out of scope for this document in v0.1:
</p>

<ul>
  <li>one frozen universal backend-family taxonomy,</li>
  <li>one frozen universal target-profile taxonomy,</li>
  <li>one frozen deployment-mode taxonomy,</li>
  <li>one frozen binary or JSON exchange format,</li>
  <li>one universal ABI descriptor model,</li>
  <li>one universal schedule encoding,</li>
  <li>one universal debugger event payload format,</li>
  <li>one full cross-vendor conformance suite for all backend families,</li>
  <li>one universal deployment package model,</li>
  <li>one mandatory runtime-private representation,</li>
  <li>one standardized first-class UI event execution model.</li>
</ul>

<p>
The goal of v0.1 is narrower and more architectural:
</p>

<pre><code>define a clean, explicit, durable handoff
between lowering and later realization
without collapsing FROG into one implementation pipeline
</code></pre>

<hr/>

<h2 id="summary">23. Summary</h2>

<p>
The FROG backend contract of v0.1 is the standardized consumption boundary after lowering.
It declares:
</p>

<ul>
  <li>what a consumer may rely on,</li>
  <li>what remains attributable,</li>
  <li>which assumptions are fixed,</li>
  <li>what must be rejected rather than silently reinterpreted.</li>
</ul>

<p>
It does not redefine the language.
It does not replace the open Execution IR.
It does not standardize private runtime realization.
</p>

<p>
It also fixes an important practical point for v0.1:
a backend contract may carry backend-family orientation,
may declare target-profile assumptions,
and may declare deployment-relevant assumptions where they materially affect correct consumption,
but doing so does not standardize one universal runtime shape or one universal runtime-module layout.
</p>

<pre><code>open Execution IR
        |
        v
lowering
        |
        v
backend contract
        |
        +-- declare consumable specialized form
        +-- declare assumptions and obligations
        +-- preserve diagnosability where claimed
        +-- preserve boundary truth where still relevant
        |
        v
private realization
</code></pre>
