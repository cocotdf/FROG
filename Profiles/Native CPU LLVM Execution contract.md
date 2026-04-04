<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">FROG Profile — Native CPU LLVM Execution Contract</h1>

<p align="center">
  <strong>Optional execution-contract surface for the Native CPU LLVM profile in FROG v0.1</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-document-exists">2. Why This Document Exists</a></li>
  <li><a href="#architectural-position">3. Architectural Position</a></li>
  <li><a href="#scope">4. Scope</a></li>
  <li><a href="#non-goals">5. Non-Goals</a></li>
  <li><a href="#core-definition">6. Core Definition</a></li>
  <li><a href="#execution-corridor">7. Execution Corridor</a></li>
  <li><a href="#contract-entry-condition">8. Contract Entry Condition</a></li>
  <li><a href="#execution-unit-and-entry-surface">9. Execution Unit and Entry Surface</a></li>
  <li><a href="#execution-lifecycle">10. Execution Lifecycle</a></li>
  <li><a href="#state-instantiation-and-initialization">11. State Instantiation and Initialization</a></li>
  <li><a href="#execution-modes">12. Execution Modes</a></li>
  <li><a href="#scheduling-and-order-visibility">13. Scheduling and Order Visibility</a></li>
  <li><a href="#data-representation-and-call-boundary-posture">14. Data Representation and Call-Boundary Posture</a></li>
  <li><a href="#effects-io-and-host-services">15. Effects, IO, and Host Services</a></li>
  <li><a href="#ui-posture">16. UI Posture</a></li>
  <li><a href="#fault-rejection-and-termination-posture">17. Fault, Rejection, and Termination Posture</a></li>
  <li><a href="#producer-obligations">18. Producer Obligations</a></li>
  <li><a href="#consumer-obligations">19. Consumer Obligations</a></li>
  <li><a href="#relation-with-backend-contract">20. Relation with Backend Contract</a></li>
  <li><a href="#conformance-reading">21. Conformance Reading</a></li>
  <li><a href="#future-evolution">22. Future Evolution</a></li>
  <li><a href="#summary">23. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines an optional execution-contract surface for the <code>native_cpu_llvm</code> profile in FROG v0.1.
</p>

<p>
Its purpose is to make explicit what a producer and a downstream native CPU LLVM-oriented consumer may rely on when the goal is not only profile-compatible handoff, but actual executable realization of a bounded accepted subset.
</p>

<p>
This document therefore sits after:
</p>

<pre>.frog source
   -&gt;
structural validation
   -&gt;
semantic acceptance
   -&gt;
canonical FROG Execution IR
   -&gt;
lowering
   -&gt;
backend contract</pre>

<p>
and before or at the point where a downstream consumer realizes:
</p>

<pre>native executable artifact
   and/or
native executable process image
   and/or
step-capable execution intake</pre>

<p>
This document does not redefine the language, the canonical Execution IR, or the generic backend contract. It defines the additional execution-facing closure required for one conservative first executable corridor under the Native CPU LLVM profile.
</p>

<hr/>

<h2 id="why-this-document-exists">2. Why This Document Exists</h2>

<p>
The Native CPU LLVM profile already defines a first serious compilation-oriented corridor for a bounded subset of FROG. However, a compilation-oriented profile alone does not fully answer the execution-side questions that appear once a lowered and contract-emitted program must actually begin running.
</p>

<p>
In particular, an execution-capable corridor benefits from explicit statements about:
</p>

<ul>
  <li>what execution unit is being instantiated,</li>
  <li>what the entry surface is,</li>
  <li>how explicit state is materialized initially,</li>
  <li>what execution modes are admitted,</li>
  <li>what order guarantees remain externally visible,</li>
  <li>what host or runtime services may be assumed,</li>
  <li>what must cause rejection instead of silent fallback.</li>
</ul>

<p>
This document exists to close those questions conservatively for one first native CPU executable corridor, while preserving the repository-wide ownership boundaries between language, IR, lowering, backend handoff, and private runtime realization.
</p>

<hr/>

<h2 id="architectural-position">3. Architectural Position</h2>

<p>
This document must be read under the following repository-wide layering:
</p>

<pre>Expression/
   - canonical source

Language/
   - validated meaning

IR/
   - canonical Execution IR
   - derivation
   - identity and recoverability
   - schema
   - lowering
   - backend contract

Profiles/
   - optional standardized capability families
   - target-facing constraints and expectations

Implementations/
   - non-normative executable workspaces</pre>

<p>
Accordingly, this document:
</p>

<ul>
  <li>does not redefine canonical source form,</li>
  <li>does not redefine semantic truth,</li>
  <li>does not redefine canonical Execution IR,</li>
  <li>does not redefine the generic backend contract as the standardized consumer-facing handoff,</li>
  <li>does define additional execution-side expectations for one bounded profile corridor.</li>
</ul>

<p>
Compactly:
</p>

<pre>Language
   defines
meaning

IR
   defines
open execution-facing representation

Lowering
   specializes
for downstream realization

Backend contract
   hands off
lowered executable meaning

This document
   constrains
how one bounded native CPU LLVM corridor may actually begin execution</pre>

<hr/>

<h2 id="scope">4. Scope</h2>

<p>
This document defines:
</p>

<ul>
  <li>a conservative execution-contract posture for the accepted Native CPU LLVM subset,</li>
  <li>the minimum execution-unit assumptions needed for native executable realization,</li>
  <li>entry, initialization, lifecycle, and termination expectations,</li>
  <li>the distinction between producer-side commitments and consumer-side obligations,</li>
  <li>what kinds of host support may be relied on explicitly,</li>
  <li>what must still remain outside the default first executable promise.</li>
</ul>

<p>
This document does not define the whole future runtime story of FROG.
</p>

<hr/>

<h2 id="non-goals">5. Non-Goals</h2>

<p>
This document is not:
</p>

<ul>
  <li>a universal runtime specification for all FROG programs,</li>
  <li>a mandatory ABI for all producers and consumers,</li>
  <li>a mandatory process model for all deployment modes,</li>
  <li>a mandatory scheduler model for all implementations,</li>
  <li>a hidden replacement for <code>IR/Backend contract.md</code>,</li>
  <li>a promise that UI-heavy or runtime-heavy programs belong to the first closed native executable corridor,</li>
  <li>a definition of one mandatory vendor-specific executable packaging format.</li>
</ul>

<p>
This document also does not authorize private runtime choices to become hidden semantic law.
</p>

<hr/>

<h2 id="core-definition">6. Core Definition</h2>

<p>
For the purposes of the <code>native_cpu_llvm</code> profile, an <strong>execution contract</strong> is the explicit profile-level statement that a lowered program scope and its backend contract are sufficient to begin native execution under declared assumptions without reinterpreting upstream meaning.
</p>

<p>
An execution contract therefore defines, for one bounded executable scope:
</p>

<ul>
  <li>what execution unit is being instantiated,</li>
  <li>what inputs must exist at activation time,</li>
  <li>what explicit state must be materialized initially,</li>
  <li>what execution mode is being used,</li>
  <li>what externally visible boundaries remain significant,</li>
  <li>what host services are assumed,</li>
  <li>what faults or unsupported conditions require rejection, termination, or explicit fault reporting.</li>
</ul>

<p>
Compactly:
</p>

<pre>backend contract
   says
what a downstream consumer may rely on

execution contract
   says
how a bounded accepted program scope may actually begin and proceed under that reliance</pre>

<hr/>

<h2 id="execution-corridor">7. Execution Corridor</h2>

<p>
The intended corridor for this document is:
</p>

<pre>.frog
   -&gt;
structural validation
   -&gt;
semantic acceptance
   -&gt;
canonical FROG Execution IR
   -&gt;
lowering
   -&gt;
backend contract
   -&gt;
execution contract satisfaction
   -&gt;
native executable realization
   -&gt;
execution start</pre>

<p>
The additional <em>execution contract satisfaction</em> step exists because compilation-oriented consumability is not yet identical to executable-start readiness.
</p>

<p>
A producer or consumer MUST NOT silently pretend that:
</p>

<pre>backend consumable
   =
execution-ready</pre>

<p>
unless the execution-side assumptions of this document are actually satisfied.
</p>

<hr/>

<h2 id="contract-entry-condition">8. Contract Entry Condition</h2>

<p>
A program scope may only claim conformance with this execution contract if all of the following are true:
</p>

<ul>
  <li>the source is canonical and structurally valid where required,</li>
  <li>the program meaning is semantically accepted,</li>
  <li>the accepted program remains within the Native CPU LLVM profile subset,</li>
  <li>canonical Execution IR has been derived without loss of required distinctions,</li>
  <li>lowering has preserved required execution-facing meaning,</li>
  <li>a backend contract has been emitted for a native CPU LLVM-oriented consumer family,</li>
  <li>the producer can state the execution mode and execution unit explicitly,</li>
  <li>all host-service dependencies needed for start are explicit rather than guessed,</li>
  <li>no unresolved runtime-private assumption remains disguised as though it were already standardized upstream.</li>
</ul>

<p>
Failure of any of these conditions requires rejection of the execution-contract claim.
</p>

<hr/>

<h2 id="execution-unit-and-entry-surface">9. Execution Unit and Entry Surface</h2>

<p>
Under this document, execution begins from an explicitly identified <strong>execution unit</strong>.
</p>

<p>
An execution unit is the bounded lowered program scope that a consumer is expected to instantiate and start under the emitted backend contract and the present execution contract.
</p>

<p>
At minimum, an execution unit MUST make explicit:
</p>

<ul>
  <li>its identity,</li>
  <li>its accepted input boundary,</li>
  <li>its accepted output boundary,</li>
  <li>its explicit state boundary where present,</li>
  <li>its required initialization surface,</li>
  <li>its chosen execution mode.</li>
</ul>

<p>
The entry surface MUST be explicit.
</p>

<p>
The entry surface MAY be realized downstream as:
</p>

<ul>
  <li>a native function-like boundary,</li>
  <li>a process-main preparation boundary,</li>
  <li>a step-call boundary,</li>
  <li>an activation API boundary,</li>
  <li>another native intake boundary consistent with the backend contract.</li>
</ul>

<p>
This document does not mandate one universal representation of that entry surface.
</p>

<p>
It does require that the producer and consumer agree explicitly on:
</p>

<pre>what must exist before first execution
what is materialized at activation
what values are supplied at activation
what state is retained across permitted activations
what outputs become externally visible
what event counts as termination or quiescent completion</pre>

<hr/>

<h2 id="execution-lifecycle">10. Execution Lifecycle</h2>

<p>
The conservative lifecycle admitted by this document is:
</p>

<pre>prepare
   -&gt;
instantiate
   -&gt;
initialize explicit state
   -&gt;
activate
   -&gt;
run or step
   -&gt;
produce visible outputs
   -&gt;
terminate, quiesce, or await next permitted activation
   -&gt;
dispose</pre>

<p>
Not every implementation must expose all of these lifecycle moments as public APIs.
</p>

<p>
However, the producer and consumer MUST preserve the architectural distinction between:
</p>

<ul>
  <li>instantiation,</li>
  <li>initialization,</li>
  <li>activation,</li>
  <li>execution progress,</li>
  <li>termination or quiescence,</li>
  <li>disposal.</li>
</ul>

<p>
These moments MUST NOT be silently collapsed where that would change required state, visibility, or effect behavior.
</p>

<hr/>

<h2 id="state-instantiation-and-initialization">11. State Instantiation and Initialization</h2>

<p>
This document inherits the FROG rule that explicit state remains explicit.
</p>

<p>
Accordingly, when the accepted program scope contains explicit local memory or state participation:
</p>

<ul>
  <li>state MUST be materialized as state, not rewritten as accidental hidden persistence,</li>
  <li>required initial values MUST be supplied or derived exactly as permitted upstream,</li>
  <li>the first activation MUST observe the proper initialized state,</li>
  <li>subsequent permitted activations MUST observe state continuity only where the corridor explicitly allows it.</li>
</ul>

<p>
The execution contract MUST therefore make one of the following postures explicit:
</p>

<ul>
  <li><strong>fresh-instance posture</strong> — each activation receives newly instantiated state,</li>
  <li><strong>retained-instance posture</strong> — the execution unit persists across permitted activations,</li>
  <li><strong>externally managed-instance posture</strong> — state lifetime is controlled by an explicit host-side owner.</li>
</ul>

<p>
A producer MUST NOT rely on implicit state retention that is neither semantically justified nor made explicit by the execution contract.
</p>

<hr/>

<h2 id="execution-modes">12. Execution Modes</h2>

<p>
This document recognizes the following conservative execution modes for the first Native CPU LLVM executable corridor:
</p>

<ul>
  <li><strong>one-shot mode</strong> — instantiate, run to completion or quiescence, then terminate,</li>
  <li><strong>step mode</strong> — instantiate once, then advance through explicit repeated activations,</li>
  <li><strong>host-driven retained-instance mode</strong> — the host controls repeated activations of an already materialized execution unit.</li>
</ul>

<p>
A conforming producer and consumer MUST state which execution mode is being used.
</p>

<p>
They MUST NOT assume that:
</p>

<pre>compiled
   implies
always process-main one-shot execution</pre>

<p>
because some accepted scopes may instead be intended for repeated step-style activation under host control.
</p>

<p>
For the first conservative corridor:
</p>

<ul>
  <li>one-shot mode is the simplest default,</li>
  <li>step mode is permitted where state and activation boundaries remain explicit,</li>
  <li>continuous event-loop ownership is not part of the default first executable promise.</li>
</ul>

<hr/>

<h2 id="scheduling-and-order-visibility">13. Scheduling and Order Visibility</h2>

<p>
The consumer MAY choose downstream scheduling strategies consistent with the lowered form and backend contract.
</p>

<p>
However, this document requires preservation of all order-visible obligations that still matter at execution start and during execution.
</p>

<p>
In particular:
</p>

<ul>
  <li>data dependencies remain binding,</li>
  <li>explicit structure boundaries remain binding where required upstream,</li>
  <li>explicit state visibility rules remain binding,</li>
  <li>effect ordering remains binding where preserved by lowering and handoff,</li>
  <li>externally visible outputs MUST NOT appear in an order that contradicts the accepted lowered meaning.</li>
</ul>

<p>
Compactly:
</p>

<pre>consumer may schedule freely
only inside
the freedom left open
by
meaning
   -&gt;
IR
   -&gt;
lowering
   -&gt;
backend contract
   -&gt;
execution contract</pre>

<p>
This document does not mandate one scheduler model, but it does forbid scheduler freedom from rewriting preserved semantics.
</p>

<hr/>

<h2 id="data-representation-and-call-boundary-posture">14. Data Representation and Call-Boundary Posture</h2>

<p>
This document does not define one mandatory ABI.
</p>

<p>
It does require that execution-start assumptions around data representation and callable boundaries be explicit enough for the consumer to begin execution without hidden guesses.
</p>

<p>
Accordingly, where execution depends on externally visible call boundaries, the producer MUST make explicit, through the backend contract and any execution-side companion material:
</p>

<ul>
  <li>what values are passed at activation,</li>
  <li>what values are returned or made visible at completion or quiescence,</li>
  <li>what stateful handles or instance references exist, if any,</li>
  <li>what representation-sensitive obligations remain important,</li>
  <li>what ownership or lifetime assumptions are in force at the boundary.</li>
</ul>

<p>
This may be realized through:
</p>

<ul>
  <li>native-call conventions,</li>
  <li>generated wrappers,</li>
  <li>host-side adapter layers,</li>
  <li>deployment-mode-specific intake surfaces.</li>
</ul>

<p>
The exact private representation remains downstream.
</p>

<p>
What is forbidden is:
</p>

<pre>opaque hidden boundary assumption
presented as though
the profile had already standardized it</pre>

<hr/>

<h2 id="effects-io-and-host-services">15. Effects, IO, and Host Services</h2>

<p>
The first Native CPU LLVM executable corridor is conservative around effects.
</p>

<p>
Pure or mostly pure executable scopes belong most naturally to this contract.
</p>

<p>
Effectful behavior MAY belong to this contract only if:
</p>

<ul>
  <li>the effect boundary is explicit,</li>
  <li>the lowering path preserved it explicitly,</li>
  <li>the backend contract makes the assumptions explicit,</li>
  <li>any required host service is declared explicitly,</li>
  <li>execution may begin without hidden service discovery or hidden semantic invention.</li>
</ul>

<p>
Host services MAY include, for example:
</p>

<ul>
  <li>basic process services,</li>
  <li>memory allocation services,</li>
  <li>time or clock access where explicitly admitted,</li>
  <li>declared external call surfaces,</li>
  <li>declared runtime-service bridges introduced by lowering.</li>
</ul>

<p>
A producer MUST NOT claim conformance with this execution contract if execution start depends on an undeclared host-service assumption.
</p>

<hr/>

<h2 id="ui-posture">16. UI Posture</h2>

<p>
UI-heavy interactive execution is outside the default first executable promise of this document.
</p>

<p>
This document therefore adopts the following conservative posture:
</p>

<ul>
  <li>pure compiled cores are in scope,</li>
  <li>explicit non-UI effects may be in scope if they are contract-bound,</li>
  <li>runtime-mediated UI services are out of scope by default,</li>
  <li>interactive event-loop ownership is out of scope by default,</li>
  <li>widget-object manipulation as a primary execution-service dependency is out of scope by default.</li>
</ul>

<p>
If a conforming implementation wishes to admit some UI-related execution surface later, it MUST do so by explicit extension and MUST preserve:
</p>

<ul>
  <li><code>widget_value</code> versus <code>widget_reference</code>,</li>
  <li>UI-object operation versus ordinary connectivity,</li>
  <li>explicit UI sequencing where present,</li>
  <li>runtime-service call boundaries introduced during lowering.</li>
</ul>

<p>
This document therefore does not close the full UI runtime story. It leaves room for it without pretending it is already solved by the first executable corridor.
</p>

<hr/>

<h2 id="fault-rejection-and-termination-posture">17. Fault, Rejection, and Termination Posture</h2>

<p>
A conforming implementation MUST distinguish at least the following situations:
</p>

<ul>
  <li><strong>profile rejection</strong> — the accepted FROG program is valid but outside the executable subset admitted here,</li>
  <li><strong>execution-contract rejection</strong> — the compilation corridor exists, but execution-start assumptions are incomplete, inconsistent, or unsupported,</li>
  <li><strong>startup fault</strong> — execution was permitted to begin but failed during preparation, instantiation, or initialization,</li>
  <li><strong>runtime fault</strong> — execution began and later failed under explicit runtime or host conditions,</li>
  <li><strong>normal termination</strong> — execution reached completion under the chosen mode,</li>
  <li><strong>quiescent continuation posture</strong> — execution reached a stable wait state under a retained-instance or step-capable mode.</li>
</ul>

<p>
These conditions MUST NOT be silently collapsed.
</p>

<p>
In particular:
</p>

<pre>language-valid
   +
profile-valid
   +
backend-consumable
does not guarantee
execution-start success</pre>

<p>
unless the execution-side assumptions of this document are also satisfied.
</p>

<hr/>

<h2 id="producer-obligations">18. Producer Obligations</h2>

<p>
A producer claiming this execution contract MUST:
</p>

<ul>
  <li>emit a backend contract consistent with the Native CPU LLVM profile,</li>
  <li>identify the bounded execution unit explicitly,</li>
  <li>state the execution mode explicitly,</li>
  <li>state the state-instantiation posture explicitly where state exists,</li>
  <li>make required host-service assumptions explicit,</li>
  <li>reject unsupported execution-start conditions instead of silently inventing private semantics,</li>
  <li>avoid implying that one private ABI or runtime model is already standardized if it is not.</li>
</ul>

<p>
The producer MAY also provide additional implementation-side metadata or manifests. Those MAY help execution, but they do not replace the architectural obligations defined here.
</p>

<hr/>

<h2 id="consumer-obligations">19. Consumer Obligations</h2>

<p>
A consumer claiming conformance with this execution contract MUST:
</p>

<ul>
  <li>honor the backend contract assumptions it accepts,</li>
  <li>honor the execution mode it accepts,</li>
  <li>materialize initialization in a way consistent with explicit state requirements,</li>
  <li>avoid rewriting preserved semantic distinctions at execution intake,</li>
  <li>reject unsupported assumptions explicitly rather than silently degrading meaning,</li>
  <li>keep runtime-private realization downstream from the standardized handoff surfaces.</li>
</ul>

<p>
A consumer MAY:
</p>

<ul>
  <li>choose its own optimizer sequence,</li>
  <li>choose its own internal scheduler model,</li>
  <li>choose its own ABI strategy,</li>
  <li>choose AOT, JIT, or hybrid realization,</li>
  <li>choose deployment packaging consistent with accepted assumptions.</li>
</ul>

<p>
Those freedoms remain valid only so long as they do not violate preserved upstream meaning and explicit execution-side commitments.
</p>

<hr/>

<h2 id="relation-with-backend-contract">20. Relation with Backend Contract</h2>

<p>
This document MUST be read as a companion to, not a replacement for, <code>IR/Backend contract.md</code>.
</p>

<p>
The distinction is:
</p>

<pre>backend contract
   =
standardized downstream handoff

execution contract
   =
additional profile-level closure for beginning execution
under one bounded accepted native CPU LLVM corridor</pre>

<p>
A practical reading order is therefore:
</p>

<pre>Profiles/Native CPU LLVM.md
   -&gt;
IR/Lowering.md
   -&gt;
IR/Backend contract.md
   -&gt;
this document</pre>

<p>
If any contradiction appears, the reader must first check whether:
</p>

<ul>
  <li>the issue belongs to generic backend-handoff ownership,</li>
  <li>the issue belongs to this profile-specific execution closure,</li>
  <li>the issue is actually a private implementation detail that should remain outside the specification.</li>
</ul>

<hr/>

<h2 id="conformance-reading">21. Conformance Reading</h2>

<p>
This document is intended to support later executable conformance growth without pretending that such a corpus is already complete.
</p>

<p>
A future executable conformance family may read cases through a corridor such as:
</p>

<pre>valid/executable/...
   source accepted
   -&gt;
   IR preserved
   -&gt;
   lowering accepted
   -&gt;
   backend contract accepted
   -&gt;
   execution contract satisfied
   -&gt;
   observable execution outcome matches expectation</pre>

<p>
Corresponding negative families may distinguish:
</p>

<ul>
  <li>language-valid but profile-rejected,</li>
  <li>profile-valid but execution-contract-rejected,</li>
  <li>execution-start fault conditions,</li>
  <li>runtime-fault conditions where relevant to the published corridor.</li>
</ul>

<p>
Until such executable conformance families are published, this document should be read as the architectural closure point that makes those future cases possible in a disciplined way.
</p>

<hr/>

<h2 id="future-evolution">22. Future Evolution</h2>

<p>
Later revisions may extend this execution contract with more detailed treatment of:
</p>

<ul>
  <li>declared ABI families,</li>
  <li>stronger deployment-mode taxonomies,</li>
  <li>stricter real-time-oriented execution contracts,</li>
  <li>more explicit interop execution surfaces,</li>
  <li>runtime-mediated UI service contracts,</li>
  <li>multi-thread or partition-aware execution contracts,</li>
  <li>embedded or reduced-service execution contracts.</li>
</ul>

<p>
Any such extension MUST preserve the repository-wide ownership rule:
</p>

<pre>open language and IR truth upstream
private realization downstream</pre>

<p>
and MUST NOT treat one private implementation strategy as though it had always been part of the language definition.
</p>

<hr/>

<h2 id="summary">23. Summary</h2>

<p>
This document closes one missing question in the Native CPU LLVM corridor:
</p>

<pre>When may a bounded accepted FROG program
not only be compiled toward a native CPU LLVM-oriented consumer,
but actually be considered ready to begin execution?</pre>

<p>
Its answer is conservative:
</p>

<ul>
  <li>only for an accepted bounded subset,</li>
  <li>only when execution-unit assumptions are explicit,</li>
  <li>only when state initialization and lifecycle are explicit,</li>
  <li>only when host-service dependencies are explicit,</li>
  <li>only when the consumer honors the backend contract and this execution contract,</li>
  <li>and without pretending that the entire future runtime ecosystem is already standardized.</li>
</ul>

<p>
That is the intended role of the Native CPU LLVM execution contract in FROG v0.1.
</p>
