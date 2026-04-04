<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Profile — Native CPU LLVM</h1>

<p align="center">
  <strong>Optional standardized native CPU compilation profile for LLVM-oriented backend families in FROG v0.1</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-profile-exists">2. Why This Profile Exists</a></li>
  <li><a href="#architectural-position">3. Architectural Position</a></li>
  <li><a href="#scope">4. Scope</a></li>
  <li><a href="#non-goals">5. Non-Goals</a></li>
  <li><a href="#profile-identity">6. Profile Identity</a></li>
  <li><a href="#core-purpose">7. Core Purpose</a></li>
  <li><a href="#compilation-corridor">8. Compilation Corridor</a></li>
  <li><a href="#profile-entry-condition">9. Profile Entry Condition</a></li>
  <li><a href="#v01-compilation-ready-subset">10. v0.1 Compilation-Ready Subset</a></li>
  <li><a href="#capability-assumptions">11. Capability Assumptions</a></li>
  <li><a href="#execution-model-posture">12. Execution Model Posture</a></li>
  <li><a href="#type-and-data-representation-posture">13. Type and Data Representation Posture</a></li>
  <li><a href="#control-structure-posture">14. Control-Structure Posture</a></li>
  <li><a href="#state-and-memory-posture">15. State and Memory Posture</a></li>
  <li><a href="#effects-io-and-ui-posture">16. Effects, IO, and UI Posture</a></li>
  <li><a href="#interop-and-external-call-posture">17. Interop and External Call Posture</a></li>
  <li><a href="#lowering-expectations">18. Lowering Expectations</a></li>
  <li><a href="#backend-contract-expectations">19. Backend Contract Expectations</a></li>
  <li><a href="#consumer-backend-family-posture">20. Consumer Backend-Family Posture</a></li>
  <li><a href="#rejection-conditions">21. Rejection Conditions</a></li>
  <li><a href="#conformance-reading">22. Conformance Reading</a></li>
  <li><a href="#relation-with-other-specification-layers">23. Relation with Other Specification Layers</a></li>
  <li><a href="#future-evolution">24. Future Evolution</a></li>
  <li><a href="#summary">25. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines <strong>Native CPU LLVM</strong> as an optional standardized FROG profile in base v0.1.
</p>

<p>
Its purpose is to define a first serious compilation-oriented profile for programs intended to pass through:
</p>

<pre><code>validated meaning
   -&gt;
canonical FROG Execution IR
   -&gt;
lowering
   -&gt;
backend contract
   -&gt;
LLVM-oriented native CPU backend family</code></pre>

<p>
This profile does not redefine FROG.
It defines a bounded optional capability surface under which a FROG program may claim compatibility with a native CPU compilation corridor oriented toward LLVM-family downstream consumers.
</p>

<p>
This profile is therefore:
</p>

<ul>
  <li>optional,</li>
  <li>compilation-oriented,</li>
  <li>CPU-native in target posture,</li>
  <li>LLVM-oriented in downstream backend-family posture,</li>
  <li>subordinate to the core FROG language architecture.</li>
</ul>

<hr/>

<h2 id="why-this-profile-exists">2. Why This Profile Exists</h2>

<p>
The core repository architecture already distinguishes:
</p>

<ul>
  <li>canonical source,</li>
  <li>validated language meaning,</li>
  <li>canonical Execution IR,</li>
  <li>lowering,</li>
  <li>backend contract,</li>
  <li>downstream backend families.</li>
</ul>

<p>
That separation makes it possible to define a first industrial compilation corridor without collapsing FROG into one specific compiler technology.
</p>

<p>
This profile exists to make one important downstream route explicit:
</p>

<ul>
  <li>a route where a conforming implementation can take an accepted subset of FROG,</li>
  <li>derive canonical open IR,</li>
  <li>lower it faithfully,</li>
  <li>emit a consumer-facing backend contract,</li>
  <li>and hand that contract to an LLVM-oriented native backend family targeting CPUs.</li>
</ul>

<p>
This profile therefore turns a general compiler direction into an explicit optional capability class.
</p>

<hr/>

<h2 id="architectural-position">3. Architectural Position</h2>

<p>
This profile must be read inside the repository-wide ownership boundaries:
</p>

<pre><code>Expression/
   - canonical source form

Language/
   - validated program meaning

Libraries/
   - intrinsic primitive vocabularies

IR/
   - canonical Execution IR
   - derivation
   - identity and recoverability
   - schema
   - lowering
   - backend contract

Profiles/
   - optional standardized capability families

Implementations/
   - non-normative executable workspaces</code></pre>

<p>
Accordingly, this document:
</p>

<ul>
  <li>does not redefine canonical source,</li>
  <li>does not redefine semantic truth,</li>
  <li>does not redefine the canonical Execution IR,</li>
  <li>does not redefine lowering or backend contract ownership,</li>
  <li>does define an optional standardized capability family for one compilation corridor.</li>
</ul>

<hr/>

<h2 id="scope">4. Scope</h2>

<p>
This profile defines:
</p>

<ul>
  <li>a first compilation-ready subset posture for FROG v0.1,</li>
  <li>the capability assumptions required for CPU-native LLVM-oriented downstream consumption,</li>
  <li>the execution-facing and lowering-facing expectations that a conforming implementation must satisfy before claiming this profile,</li>
  <li>the rejection conditions for programs or lowered forms that exceed the profile,</li>
  <li>the relation between this profile and later backend-family consumption.</li>
</ul>

<p>
This profile does not define:
</p>

<ul>
  <li>the full FROG language,</li>
  <li>all future compilation profiles,</li>
  <li>GPU, FPGA, RT, MCU, or accelerator profiles,</li>
  <li>a universal runtime model,</li>
  <li>a mandatory LLVM pipeline shape,</li>
  <li>a mandatory ABI,</li>
  <li>a mandatory optimizer pass sequence.</li>
</ul>

<hr/>

<h2 id="non-goals">5. Non-Goals</h2>

<p>
This profile is not:
</p>

<ul>
  <li>a replacement for the core language,</li>
  <li>a hidden backend specification disguised as a profile,</li>
  <li>a way to redefine the canonical Execution IR as LLVM IR,</li>
  <li>a promise that every valid FROG program is automatically Native CPU LLVM compatible,</li>
  <li>a promise that UI-heavy or runtime-heavy programs belong to the same first compilation corridor as pure native cores,</li>
  <li>a definition of one mandatory private runtime implementation.</li>
</ul>

<p>
The purpose of this profile is to close one coherent industrial corridor first, not to absorb the whole future ecosystem immediately.
</p>

<hr/>

<h2 id="profile-identity">6. Profile Identity</h2>

<p>
The profile identifier is:
</p>

<pre><code>native_cpu_llvm</code></pre>

<p>
This identifier denotes:
</p>

<ul>
  <li>a target-facing capability class for native CPU-oriented compilation,</li>
  <li>a downstream backend-family posture that is LLVM-oriented,</li>
  <li>a profile-level claim that the accepted program slice is suitable for this corridor.</li>
</ul>

<p>
This identifier MUST NOT be misread as:
</p>

<ul>
  <li>a claim that LLVM defines FROG,</li>
  <li>a claim that one specific vendor toolchain is mandatory,</li>
  <li>a claim that the canonical open IR is itself LLVM IR.</li>
</ul>

<hr/>

<h2 id="core-purpose">7. Core Purpose</h2>

<p>
The core purpose of this profile is to enable a first industrially credible statement of the form:
</p>

<pre><code>For the accepted Native CPU LLVM v0.1 subset,
a semantically accepted FROG program
can be derived to canonical FROG Execution IR,
lowered faithfully,
emitted as a backend contract,
and consumed by an LLVM-oriented native CPU backend family.</code></pre>

<p>
This profile exists so that this statement becomes:
</p>

<ul>
  <li>bounded,</li>
  <li>auditable,</li>
  <li>conformance-readable,</li>
  <li>implementation-comparable.</li>
</ul>

<hr/>

<h2 id="compilation-corridor">8. Compilation Corridor</h2>

<p>
The intended corridor for this profile is:
</p>

<pre><code>.frog
   -&gt;
structural validation
   -&gt;
semantic validation
   -&gt;
canonical FROG Execution IR
   -&gt;
lowering
   -&gt;
backend contract
   -&gt;
LLVM-oriented native CPU consumer
   -&gt;
native executable realization</code></pre>

<p>
This profile applies only if the program remains within the accepted subset and the implementation preserves the full corridor discipline.
</p>

<p>
In particular:
</p>

<ul>
  <li>the canonical Execution IR remains open and language-owned,</li>
  <li>lowering remains downstream specialization,</li>
  <li>backend contract remains the standardized consumer-facing handoff,</li>
  <li>LLVM remains a downstream consumer family.</li>
</ul>

<hr/>

<h2 id="profile-entry-condition">9. Profile Entry Condition</h2>

<p>
A program may only claim this profile if all of the following are true:
</p>

<ul>
  <li>the program is structurally valid canonical FROG source,</li>
  <li>the program is semantically accepted by the core language and any referenced optional capability surfaces,</li>
  <li>the program remains within the accepted v0.1 subset of this profile,</li>
  <li>the implementation can derive canonical FROG Execution IR without losing required distinctions,</li>
  <li>the implementation can lower that IR faithfully toward a native CPU LLVM-oriented handoff,</li>
  <li>the implementation can emit a backend contract consistent with that handoff.</li>
</ul>

<p>
Failure of any of these conditions requires rejection of the profile claim.
</p>

<hr/>

<h2 id="v01-compilation-ready-subset">10. v0.1 Compilation-Ready Subset</h2>

<p>
The accepted v0.1 subset for this profile is intentionally conservative.
</p>

<p>
It includes, at minimum, the following capability families when they are semantically valid and otherwise conforming:
</p>

<ul>
  <li>scalar numeric computation,</li>
  <li>basic typed dataflow connectivity,</li>
  <li>intrinsic pure primitives from the accepted library surface,</li>
  <li>arrays and aggregates that can be represented by the consuming implementation,</li>
  <li>public typed interface participation,</li>
  <li>structured control forms such as case-like and loop-like families when the implementation supports their lowering under this profile,</li>
  <li>explicit local memory / delay-like state participation when the implementation supports their lowering under this profile,</li>
  <li>restricted external call boundaries where the implementation can provide a stable backend-facing interpretation.</li>
</ul>

<p>
The following remain outside the default first accepted core of this profile unless explicitly supported by a conforming implementation statement:
</p>

<ul>
  <li>UI-heavy execution surfaces,</li>
  <li>runtime-service-dependent interactive widget manipulation as a primary compiled-core feature,</li>
  <li>distributed or multi-device semantics,</li>
  <li>accelerator-specific placement semantics,</li>
  <li>hard real-time commitments,</li>
  <li>profile surfaces that require a different backend family or stronger runtime contracts.</li>
</ul>

<p>
The guiding rule is:
</p>

<pre><code>close one serious native compiled core first
before widening the profile surface</code></pre>

<hr/>

<h2 id="capability-assumptions">11. Capability Assumptions</h2>

<p>
A conforming implementation claiming <code>native_cpu_llvm</code> support assumes a consumer environment capable of:
</p>

<ul>
  <li>native CPU code generation or equivalent native CPU execution preparation,</li>
  <li>LLVM-oriented downstream code generation or optimization consumption,</li>
  <li>typed data representation compatible with the accepted subset,</li>
  <li>control-flow materialization compatible with the accepted structured subset,</li>
  <li>state and storage materialization compatible with the accepted explicit-memory subset,</li>
  <li>external call handling where the profile-supported interop subset requires it.</li>
</ul>

<p>
These are capability assumptions, not proof that one specific LLVM toolchain is mandatory.
</p>

<hr/>

<h2 id="execution-model-posture">12. Execution Model Posture</h2>

<p>
This profile remains subordinate to the core FROG execution model.
</p>

<p>
Therefore:
</p>

<ul>
  <li>dataflow meaning remains dataflow meaning,</li>
  <li>validated dependencies remain authoritative,</li>
  <li>structured control remains structured control,</li>
  <li>explicit state remains explicit state,</li>
  <li>lowering MAY specialize these for native backend consumption,</li>
  <li>lowering MUST NOT replace them with backend-private semantic invention.</li>
</ul>

<p>
The profile adds a compilation corridor.
It does not replace the language’s execution semantics.
</p>

<hr/>

<h2 id="type-and-data-representation-posture">13. Type and Data Representation Posture</h2>

<p>
Under this profile, accepted programs must use data representations that the producer can lower coherently to a native CPU LLVM-oriented backend family.
</p>

<p>
This means:
</p>

<ul>
  <li>scalar numeric types MUST have a defined lowering path,</li>
  <li>aggregate and array types MUST have a defined storage and transfer interpretation,</li>
  <li>type legality remains decided upstream by the language and library layers,</li>
  <li>representation commitments may become more explicit during lowering and backend contract emission.</li>
</ul>

<p>
A conforming implementation MUST reject profile claims for programs whose accepted types still lack a coherent lowering and contract path under this profile.
</p>

<hr/>

<h2 id="control-structure-posture">14. Control-Structure Posture</h2>

<p>
This profile accepts structured control only where the implementation can preserve semantics through the full corridor.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>case-like structures MAY be included when the producer can lower them faithfully to a native CPU LLVM-oriented consumer,</li>
  <li>loop-like structures MAY be included when the producer can preserve region, condition, iteration, and boundary semantics through lowering,</li>
  <li>structured control MUST NOT be flattened in a way that destroys required semantics before the permitted downstream boundary.</li>
</ul>

<p>
If a particular structure family is semantically valid in FROG but not yet lowerable under this profile, the correct result is:
</p>

<pre><code>language acceptance
+
profile rejection</code></pre>

<p>
and not silent reinterpretation.
</p>

<hr/>

<h2 id="state-and-memory-posture">15. State and Memory Posture</h2>

<p>
This profile accepts explicit local memory only where the implementation can lower it faithfully.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>explicit state remains explicit state,</li>
  <li>initialization remains explicit when semantically required,</li>
  <li>state participation must remain distinguishable from ordinary dataflow through the contract boundary,</li>
  <li>hidden persistence MUST NOT be invented as a substitute for explicit state.</li>
</ul>

<p>
A profile-supporting implementation MUST reject any program whose accepted state semantics cannot be preserved through the native CPU LLVM-oriented corridor.
</p>

<hr/>

<h2 id="effects-io-and-ui-posture">16. Effects, IO, and UI Posture</h2>

<p>
This profile is intentionally conservative around effectful and UI-dependent features.
</p>

<p>
The default posture is:
</p>

<ul>
  <li>pure or mostly pure computation belongs naturally to this first corridor,</li>
  <li>effect surfaces may be admitted only when the producer can model them explicitly in lowering and backend contract form,</li>
  <li>UI-heavy interactive surfaces are not part of the default first compiled-core promise of this profile,</li>
  <li>runtime-mediated UI services may be supported later, but they are not assumed by default in the first closed profile corridor.</li>
</ul>

<p>
This keeps the first industrial profile focused on closing a real native compiled core instead of prematurely absorbing the full UI runtime story.
</p>

<hr/>

<h2 id="interop-and-external-call-posture">17. Interop and External Call Posture</h2>

<p>
Restricted interop MAY belong to this profile if and only if:
</p>

<ul>
  <li>the callable boundary is explicit,</li>
  <li>the type boundary is explicit,</li>
  <li>the lowering path is coherent,</li>
  <li>the backend contract makes the assumptions explicit,</li>
  <li>the consumer can honor the call-surface obligations.</li>
</ul>

<p>
Interop support under this profile is therefore:
</p>

<ul>
  <li>possible,</li>
  <li>restricted,</li>
  <li>contract-bound,</li>
  <li>not license for arbitrary foreign-runtime dependency surfaces.</li>
</ul>

<hr/>

<h2 id="lowering-expectations">18. Lowering Expectations</h2>

<p>
A producer claiming this profile MUST be able to lower the accepted subset toward a native CPU LLVM-oriented consumer family while preserving:
</p>

<ul>
  <li>semantic faithfulness,</li>
  <li>required attribution continuity,</li>
  <li>required control and state distinctions,</li>
  <li>backend-relevant type and storage commitments,</li>
  <li>explicit rejection where unsupported features remain.</li>
</ul>

<p>
The producer MAY:
</p>

<ul>
  <li>normalize control toward CFG-friendly forms,</li>
  <li>normalize pure computation toward SSA-friendly forms,</li>
  <li>materialize storage and state more explicitly,</li>
  <li>introduce backend-oriented support structure.</li>
</ul>

<p>
The producer MUST NOT:
</p>

<ul>
  <li>collapse FROG IR into LLVM IR,</li>
  <li>treat backend-family convenience as language truth,</li>
  <li>repair unsupported profile features silently.</li>
</ul>

<hr/>

<h2 id="backend-contract-expectations">19. Backend Contract Expectations</h2>

<p>
A profile-supporting producer MUST emit a backend contract explicit enough for a native CPU LLVM-oriented consumer to decide whether it can consume the lowered form without guessing.
</p>

<p>
That contract SHOULD make explicit, as applicable:
</p>

<ul>
  <li>backend family posture,</li>
  <li>accepted lowered executable scope,</li>
  <li>representation commitments,</li>
  <li>state and control commitments,</li>
  <li>effect or interop commitments,</li>
  <li>required capabilities,</li>
  <li>rejection conditions.</li>
</ul>

<p>
The backend contract remains downstream from canonical open IR and lowering.
This profile depends on that distinction and does not replace it.
</p>

<hr/>

<h2 id="consumer-backend-family-posture">20. Consumer Backend-Family Posture</h2>

<p>
A consumer under this profile is any backend-family consumer that is:
</p>

<ul>
  <li>native CPU oriented,</li>
  <li>LLVM oriented in downstream compilation posture,</li>
  <li>able to honor the emitted backend contract.</li>
</ul>

<p>
Such a consumer MAY:
</p>

<ul>
  <li>compile to machine code,</li>
  <li>optimize through LLVM-oriented passes,</li>
  <li>produce native object or executable artifacts,</li>
  <li>participate in JIT or AOT flows,</li>
  <li>delegate some support needs to a runtime surface declared by the contract.</li>
</ul>

<p>
Such a consumer MUST NOT:
</p>

<ul>
  <li>reinterpret unsupported profile features silently,</li>
  <li>pretend LLVM defines the language,</li>
  <li>erase contract-required distinctions without honoring them.</li>
</ul>

<hr/>

<h2 id="rejection-conditions">21. Rejection Conditions</h2>

<p>
A profile claim MUST be rejected if any of the following applies:
</p>

<ul>
  <li>the program exceeds the accepted v0.1 subset,</li>
  <li>the implementation cannot derive canonical FROG Execution IR faithfully,</li>
  <li>the implementation cannot lower the accepted semantics coherently,</li>
  <li>the implementation cannot emit a backend contract explicit enough for the consumer,</li>
  <li>the consumer cannot honor required control, state, representation, or capability commitments,</li>
  <li>the route would require silent semantic invention or hidden runtime assumptions beyond the declared profile surface.</li>
</ul>

<p>
This is one of the key benefits of the profile:
</p>

<pre><code>explicit profile rejection
is better than
implicit backend drift</code></pre>

<hr/>

<h2 id="conformance-reading">22. Conformance Reading</h2>

<p>
This profile should be read together with the repository conformance corridor.
</p>

<p>
In particular, claiming <code>native_cpu_llvm</code> support does not weaken the public truth surface around:
</p>

<ul>
  <li>accept / reject correctness,</li>
  <li>IR derivation correctness,</li>
  <li>identity and recoverability,</li>
  <li>schema validity,</li>
  <li>lowering discipline,</li>
  <li>backend-contract discipline.</li>
</ul>

<p>
Future conformance growth for this profile SHOULD therefore introduce cases that distinguish:
</p>

<ul>
  <li>language-valid but profile-rejected,</li>
  <li>IR-derivable but not lowerable under this profile,</li>
  <li>lowerable but not contract-emittable under this profile,</li>
  <li>contract-emittable but consumer-rejected under this profile.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specification-layers">23. Relation with Other Specification Layers</h2>

<p>
This profile remains subordinate to the rest of the published architecture:
</p>

<ul>
  <li><code>Expression/</code> still owns source form,</li>
  <li><code>Language/</code> still owns validated meaning,</li>
  <li><code>Libraries/</code> still own intrinsic primitive law,</li>
  <li><code>IR/</code> still owns canonical IR, derivation, schema, lowering, and backend contract,</li>
  <li><code>Profiles/</code> only owns the optional standardized capability claim described here.</li>
</ul>

<p>
This is critical:
</p>

<pre><code>Native CPU LLVM
   is a profile claim

it is not
the definition of FROG</code></pre>

<hr/>

<h2 id="future-evolution">24. Future Evolution</h2>

<p>
This profile is intentionally a first closure step.
It MAY evolve later through:
</p>

<ul>
  <li>wider accepted structured-control coverage,</li>
  <li>wider explicit-state coverage,</li>
  <li>better effect-surface support,</li>
  <li>restricted UI-service support,</li>
  <li>better interop coverage,</li>
  <li>richer native deployment modes,</li>
  <li>additional backend-family refinements.</li>
</ul>

<p>
However, future growth SHOULD remain disciplined:
</p>

<pre><code>close one coherent corridor
before broadening the optional surface</code></pre>

<hr/>

<h2 id="summary">25. Summary</h2>

<p>
This document defines <code>native_cpu_llvm</code> as an optional standardized FROG profile for a first industrial native CPU compilation corridor oriented toward LLVM-family downstream consumers.
</p>

<p>
Its core rules are:
</p>

<ul>
  <li>the profile is optional,</li>
  <li>the profile is downstream-compilation-oriented,</li>
  <li>the profile does not redefine the language core or the canonical IR,</li>
  <li>the profile accepts only a conservative v0.1 subset,</li>
  <li>the profile requires faithful derivation, lowering, and backend-contract emission,</li>
  <li>the profile requires explicit rejection when the corridor cannot be honored.</li>
</ul>

<p>
This profile therefore enables a serious public statement:
</p>

<pre><code>FROG can support a real native compiled corridor
without collapsing the language into LLVM,
because LLVM remains downstream from
validated meaning,
canonical open IR,
lowering,
and backend contract.</code></pre>

<p>
That is the purpose of this profile in base v0.1.
</p>
