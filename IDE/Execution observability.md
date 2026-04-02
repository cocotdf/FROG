<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">🐸 FROG IDE Execution Observability Specification</h1>

<p align="center">
IDE-facing projection of live execution activity for FROG tooling<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope-for-v01">2. Scope for v0.1</a></li>
  <li><a href="#architectural-position-and-dependencies">3. Architectural Position and Dependencies</a></li>
  <li><a href="#design-principles">4. Design Principles</a></li>
  <li><a href="#conceptual-observability-model">5. Conceptual Observability Model</a></li>
  <li><a href="#execution-instance-projection">6. Execution Instance Projection</a></li>
  <li><a href="#source-identity-and-execution-context">7. Source Identity and Execution Context</a></li>
  <li><a href="#observable-objects">8. Observable Objects</a></li>
  <li><a href="#states-and-snapshots">9. States and Snapshots</a></li>
  <li><a href="#event-vocabulary">10. Event Vocabulary</a></li>
  <li><a href="#safe-boundary-consumption">11. Safe-Boundary Consumption</a></li>
  <li><a href="#ordering-and-causal-consistency">12. Ordering and Causal Consistency</a></li>
  <li><a href="#ide-requirements">13. IDE Requirements</a></li>
  <li><a href="#illustrative-observation-shapes">14. Illustrative Observation Shapes</a></li>
  <li><a href="#out-of-scope-for-v01">15. Out of Scope for v0.1</a></li>
  <li><a href="#summary">16. Summary</a></li>
  <li><a href="#license">17. License</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the <strong>IDE-facing execution observability contract</strong> for FROG.
It specifies how language-defined execution activity becomes visible to IDE tooling in a
<strong>source-aligned</strong> way.
</p>

<p>
This document does <strong>not</strong> define execution semantics.
Execution meaning remains owned by the validated executable graph and by the relevant
language and library specifications.
This document standardizes only the <strong>observable projection</strong> that may be consumed by:
</p>

<ul>
  <li>execution highlighting,</li>
  <li>trace views and diagnostics,</li>
  <li>debugging,</li>
  <li>probes,</li>
  <li>watches,</li>
  <li>other execution-aware IDE tooling.</li>
</ul>

<pre><code>Language/ and Libraries/
        -&gt; define execution meaning

IDE/Execution observability.md
        -&gt; defines the source-aligned observable projection of that meaning

IDE/Debugging.md, IDE/Probes.md, IDE/Watch.md
        -&gt; consume that projection
</code></pre>

<p>
Execution observability is therefore an <strong>inspection-facing contract</strong>.
It is not a replacement for the execution model, not a replacement for safe observation rules,
and not a runtime-internal scheduling specification.
</p>

<hr/>

<h2 id="scope-for-v01">2. Scope for v0.1</h2>

<p>
For FROG v0.1, this document standardizes the minimal observable model needed by IDE tooling to
consume live execution in a semantically faithful way.
</p>

<p>
This document defines:
</p>

<ul>
  <li>how one live execution instance is identified from the IDE point of view,</li>
  <li>how observable activity maps back to source identity,</li>
  <li>how repeated dynamic activity is disambiguated through execution context,</li>
  <li>which source-aligned execution objects may be observed,</li>
  <li>which high-level instance and activity states may be projected,</li>
  <li>which canonical semantic event names may be exposed,</li>
  <li>which consistency guarantees the IDE may rely on when consuming safe language-level boundaries.</li>
</ul>

<p>
This document does <strong>not</strong> define:
</p>

<ul>
  <li>the execution model itself,</li>
  <li>the safe-observation, safe-pause, or safe-debug-stop semantics themselves,</li>
  <li>a mandatory runtime architecture,</li>
  <li>a mandatory event transport protocol,</li>
  <li>a mandatory binary or JSON wire format,</li>
  <li>a mandatory timestamp format,</li>
  <li>a mandatory value-serialization format,</li>
  <li>debugging controls,</li>
  <li>probe behavior,</li>
  <li>watch behavior.</li>
</ul>

<hr/>

<h2 id="architectural-position-and-dependencies">3. Architectural Position and Dependencies</h2>

<h3>3.1 Repository position</h3>

<p>
This document belongs in <code>IDE/</code> because it defines how execution is made visible to tools.
It does <strong>not</strong> belong to <code>Language/</code> because it does not own execution meaning.
</p>

<h3>3.2 Dependencies</h3>

<p>
This document depends on the following specifications:
</p>

<ul>
  <li><code>IDE/Readme.md</code> — architectural role of observability in the IDE layer,</li>
  <li><code>IDE/Debugging.md</code> — debugger-facing control behavior built on top of observability,</li>
  <li><code>IDE/Probes.md</code> — source-attached probe behavior consuming observable execution,</li>
  <li><code>IDE/Watch.md</code> — persistent watch behavior consuming observable execution,</li>
  <li><code>Expression/Diagram.md</code> — canonical graph-level source identity,</li>
  <li><code>Expression/Control structures.md</code> — canonical structure and region representation,</li>
  <li><code>Expression/State and cycles.md</code> — canonical local-memory representation,</li>
  <li><code>Expression/Widget interaction.md</code> — explicit UI sequencing through <code>ui_in</code> and <code>ui_out</code>,</li>
  <li><code>Language/Execution model.md</code> — live execution instance, source identity, activation, execution context, and committed source-level state,</li>
  <li><code>Language/Execution control and observation boundaries.md</code> — safe observation points, pause-consistent snapshots, and safe debug stops,</li>
  <li><code>Language/Control structures.md</code> — normative control-structure execution semantics,</li>
  <li><code>Language/State and cycles.md</code> — normative local-memory and cycle semantics,</li>
  <li><code>Libraries/Core.md</code> — primitive-local behavior such as <code>frog.core.delay</code>,</li>
  <li><code>Libraries/UI.md</code> — standardized executable UI interaction primitives.</li>
</ul>

<h3>3.3 Ownership boundary</h3>

<p>
If a conflict appears, the following ownership rules apply:
</p>

<ul>
  <li><code>Expression/</code> remains authoritative for canonical source identity and serialized representation,</li>
  <li><code>Language/</code> remains authoritative for execution meaning, committed state, and safe boundaries,</li>
  <li><code>Libraries/</code> remain authoritative for primitive identity, port surfaces, metadata, and primitive-local behavior,</li>
  <li><code>IDE/</code> remains authoritative only for the tooling-facing projection and its consumption by IDE features.</li>
</ul>

<pre><code>Expression/
    owns what is serialized and source-visible

Language/
    owns what execution means

Libraries/
    own primitive-local meaning

IDE/
    owns how tools observe and consume the already-defined meaning
</code></pre>

<hr/>

<h2 id="design-principles">4. Design Principles</h2>

<h3>4.1 Source alignment</h3>

<p>
Observable execution MUST remain attributable to source-visible objects known to the FROG Program Model.
An IDE user SHOULD be able to understand the observed activity in terms of diagrams, edges, nodes,
structures, regions, sub-FROG calls, widget-related execution objects, and local memory.
</p>

<h3>4.2 Language-derived meaning</h3>

<p>
The observable projection MUST be derived from language-defined meaning.
This document MUST NOT be used to create an alternative execution-semantics layer inside <code>IDE/</code>.
</p>

<h3>4.3 Runtime independence</h3>

<p>
Different runtimes MAY use different schedulers, queues, threads, batching strategies,
buffering strategies, or backend optimizations.
Those implementation choices MAY vary.
The IDE-visible semantic meaning MUST remain equivalent.
</p>

<h3>4.4 Causal consistency</h3>

<p>
The IDE-facing projection MUST represent a causally coherent view of execution.
The IDE MUST NOT be forced to interpret impossible or self-contradictory source-level states.
</p>

<h3>4.5 Capability profiles and observability profiles remain distinct</h3>

<p>
The repository uses <code>Profiles/</code> for optional standardized executable capability families.
This document may additionally refer to <strong>observability profiles</strong>, meaning stronger or weaker
IDE-facing observation contracts.
These notions MUST NOT be conflated.
</p>

<ul>
  <li>a capability profile defines what executable capability families exist,</li>
  <li>an observability profile defines how much execution detail is exposed to tools.</li>
</ul>

<h3>4.6 Minimal but extensible</h3>

<p>
FROG v0.1 defines a minimal observability core.
Stricter observability profiles MAY expose richer snapshots, more events, more detailed payloads,
retained history, stronger ordering guarantees, or richer contextual metadata,
provided that the base v0.1 meaning remains preserved.
</p>

<h3>4.7 Descriptive, not prescriptive</h3>

<p>
This document describes what tools MAY observe.
It does not prescribe one runtime-internal micro-order or one transport implementation.
</p>

<hr/>

<h2 id="conceptual-observability-model">5. Conceptual Observability Model</h2>

<p>
Execution observability is the conceptual layer that projects live execution toward IDE tooling.
That projection MAY be exposed through:
</p>

<ul>
  <li>an event stream,</li>
  <li>a polling API,</li>
  <li>paused snapshots,</li>
  <li>a retained trace buffer,</li>
  <li>or any equivalent hybrid model.</li>
</ul>

<p>
Regardless of transport, a conforming implementation MUST preserve the same source-aligned meaning.
</p>

<p>
At minimum, the projection may expose:
</p>

<ul>
  <li>instance lifecycle,</li>
  <li>node activity,</li>
  <li>edge value availability,</li>
  <li>structure and region activity,</li>
  <li>local-memory activity,</li>
  <li>sub-FROG activity,</li>
  <li>paused and terminal execution state.</li>
</ul>

<pre><code>live execution instance
        |
        v
source-aligned observable projection
        |
        +--&gt; execution overlays
        +--&gt; debugging
        +--&gt; probes
        +--&gt; watches
        +--&gt; traces / diagnostics
</code></pre>

<hr/>

<h2 id="execution-instance-projection">6. Execution Instance Projection</h2>

<h3>6.1 General rule</h3>

<p>
Every observable event, snapshot, or retained observation belongs to exactly one
<strong>live execution instance</strong>.
The definition of a live execution instance belongs to <code>Language/Execution model.md</code>.
This document defines only how that instance becomes observable to tools.
</p>

<h3>6.2 Instance identity</h3>

<p>
An IDE-facing observability feed MUST expose an identifier unique within the observing session.
This identifier is referred to here as <code>instance_id</code>.
</p>

<p>
That identity SHOULD make it possible to distinguish:
</p>

<ul>
  <li>different runs of the same FROG,</li>
  <li>different active instances observed concurrently,</li>
  <li>retained observations originating from different runs.</li>
</ul>

<h3>6.3 Instance association rule</h3>

<p>
An IDE MUST NOT silently conflate observations from unrelated execution instances.
If retained data from multiple instances is shown, the instance association SHOULD remain available.
</p>

<hr/>

<h2 id="source-identity-and-execution-context">7. Source Identity and Execution Context</h2>

<h3>7.1 Source identity</h3>

<p>
Observable activity SHOULD be attributable to source-level objects whenever applicable.
Relevant source-level objects include:
</p>

<ul>
  <li>a diagram,</li>
  <li>a node,</li>
  <li>a node port,</li>
  <li>an edge,</li>
  <li>a structure,</li>
  <li>a region,</li>
  <li>a sub-FROG call site,</li>
  <li>a local-memory slot owned by a node instance.</li>
</ul>

<p>
When canonical serialized identifiers already exist, observability SHOULD use them directly,
for example:
</p>

<ul>
  <li><code>node.id</code>,</li>
  <li><code>edge.id</code>,</li>
  <li><code>region.id</code>.</li>
</ul>

<p>
When an observed object has no directly serialized identifier, the Program Model MAY provide
a stable IDE-visible identity derived from canonical source meaning.
</p>

<h3>7.2 Execution context</h3>

<p>
Source identity alone is not sufficient for repeated or nested dynamic activity.
Observable activity MUST therefore carry an <strong>execution context</strong> whenever source identity alone
would be ambiguous.
</p>

<p>
For v0.1, execution context MAY include:
</p>

<ul>
  <li>the relevant <code>instance_id</code>,</li>
  <li>sub-FROG invocation nesting,</li>
  <li>structure nesting,</li>
  <li>selected region identity,</li>
  <li>loop iteration index when applicable,</li>
  <li>activation identity when applicable.</li>
</ul>

<p>
Execution context MUST be rich enough to distinguish semantically different dynamic occurrences of the
same source object, such as:
</p>

<ul>
  <li>different iterations of one loop body,</li>
  <li>different activations of one node inside repeated control flow,</li>
  <li>activity in one selected <code>case</code> region versus other inactive regions,</li>
  <li>callee activity inside a nested sub-FROG versus caller-level activity.</li>
</ul>

<h3>7.3 Activation identity</h3>

<p>
When the active observability profile exposes activation-level detail, repeated node activity SHOULD include
an <code>activation_id</code> unique within the relevant live execution instance.
</p>

<hr/>

<h2 id="observable-objects">8. Observable Objects</h2>

<h3>8.1 Node activity</h3>

<p>
A source node MAY activate zero, one, or multiple times during one live execution instance.
The observable model SHOULD allow an IDE to correlate that activity to:
</p>

<ul>
  <li>the source node identity,</li>
  <li>the relevant execution context,</li>
  <li>the relevant activation identity when exposed.</li>
</ul>

<p>
This rule applies to source node kinds where relevant, including:
</p>

<ul>
  <li><code>primitive</code>,</li>
  <li><code>structure</code>,</li>
  <li><code>subfrog</code>,</li>
  <li><code>interface_input</code>,</li>
  <li><code>interface_output</code>,</li>
  <li><code>widget_value</code>,</li>
  <li><code>widget_reference</code>.</li>
</ul>

<p>
This document defines only the observable projection of such activity.
The meaning of each node kind remains defined elsewhere.
</p>

<h3>8.2 Edge value availability</h3>

<p>
An IDE SHOULD be able to observe when a source-level value becomes available on an edge.
This is represented by the canonical semantic event:
</p>

<pre><code>edge_value_available</code></pre>

<p>
At the source-aligned level, the primary observed object for that event SHOULD be the target edge.
The event means that a source-level meaningful value is now available for observation in the relevant
execution context.
</p>

<p>
This does <strong>not</strong> require exposing runtime-private buffering details.
</p>

<p>
Payload exposure is profile-dependent.
A conforming implementation MAY expose:
</p>

<ul>
  <li>a full value snapshot,</li>
  <li>a bounded value preview,</li>
  <li>a summarized structural rendering,</li>
  <li>an opaque handle for later inspection,</li>
  <li>or no payload beyond availability.</li>
</ul>

<p>
If one producing output fans out to multiple source edges, observability SHOULD remain edge-based,
because source-level overlays, probes, watches, and diagnostics are naturally edge-oriented.
</p>

<h3>8.3 Structure and region activity</h3>

<p>
A structure activation is itself observable.
The IDE SHOULD be able to observe at least:
</p>

<ul>
  <li>structure entry,</li>
  <li>region selection when applicable,</li>
  <li>loop iteration progression when applicable,</li>
  <li>structure completion.</li>
</ul>

<p>
For a <code>case</code> structure:
</p>

<ul>
  <li>exactly one region becomes selected for each activation,</li>
  <li>the selected region SHOULD remain identifiable by <code>region.id</code>,</li>
  <li>inactive regions MUST NOT be represented as executing for that activation.</li>
</ul>

<p>
For a <code>for_loop</code> or <code>while_loop</code>:
</p>

<ul>
  <li>the loop activation itself is observable,</li>
  <li>the body activity repeats across iterations,</li>
  <li>iteration identity SHOULD remain available when the active observability profile exposes it.</li>
</ul>

<h3>8.4 Local memory</h3>

<p>
Local-memory primitives participate in ordinary node execution and additionally expose source-aligned
state activity.
For IDE purposes, the canonical semantic events are:
</p>

<pre><code>state_read
state_updated
</code></pre>

<p>
These events refer to the local-memory slot owned by the relevant node instance inside one live execution instance.
</p>

<p>
For <code>frog.core.delay</code>, this document does not redefine the primitive-local behavior or the language-level
cycle semantics.
It standardizes only the observable projection of the already-defined source-aligned state activity.
</p>

<p>
For one normal activation of <code>frog.core.delay</code>, a conforming observable view SHOULD preserve the following
causal meaning:
</p>

<ul>
  <li>the node activation becomes relevant in the current execution context,</li>
  <li>the previously stored state is the source-aligned basis of the observed output for that activation,</li>
  <li>the next stored state is updated from the observed input for that activation,</li>
  <li>the activation completion MUST NOT be exposed before the source-visible state transition for that activation is committed.</li>
</ul>

<p>
A stricter observability profile MAY also expose the current stored state during a valid paused snapshot.
If it does, that state MUST match the committed source-level meaning.
</p>

<h3>8.5 Sub-FROG activity</h3>

<p>
A <code>subfrog</code> node MUST be observable at least at the call-site level.
The caller diagram MUST be able to observe activity on the <code>subfrog</code> node itself.
</p>

<p>
A stricter observability profile MAY additionally expose nested callee activity.
When it does:
</p>

<ul>
  <li>caller/callee nesting MUST remain explicit in execution context,</li>
  <li>the IDE MUST be able to distinguish caller-level and callee-level activity,</li>
  <li>the nested view MUST remain source-aligned rather than runtime-internal.</li>
</ul>

<h3>8.6 UI-effect sequencing</h3>

<p>
The widget interaction model defines optional <code>ui_in</code> and <code>ui_out</code> ports for explicit UI-effect ordering.
Those ports are <strong>sequencing ports</strong>, not ordinary data-value ports.
</p>

<p>
If a runtime exposes activity related to <code>ui_in</code> and <code>ui_out</code>, the IDE MUST interpret that activity as
<strong>effect-order visibility</strong> rather than ordinary valueflow visibility.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>an IDE MAY render such edges differently from ordinary data edges,</li>
  <li>a stricter observability profile MAY expose richer UI-oriented execution events,</li>
  <li>the absence of such richer events in v0.1 does not weaken the already-defined sequencing semantics.</li>
</ul>

<p>
This document MUST NOT be interpreted as introducing implicit UI scheduling.
Only the existing explicit sequencing model and the normal execution model apply.
</p>

<hr/>

<h2 id="states-and-snapshots">9. States and Snapshots</h2>

<h3>9.1 Instance states</h3>

<p>
From the IDE point of view, a live execution instance MUST be projectable in one of the following
execution-facing states:
</p>

<ul>
  <li><code>running</code>,</li>
  <li><code>paused</code>,</li>
  <li><code>completed</code>,</li>
  <li><code>faulted</code>,</li>
  <li><code>aborted</code>.</li>
</ul>

<p>
An IDE MAY also use additional local view-management states such as <code>attached</code> or <code>detached</code>.
Such states are IDE-local only and MUST NOT be confused with language-level instance state.
</p>

<h3>9.2 Conceptual activity states</h3>

<p>
For projection purposes, an IDE MAY use conceptual activity states for nodes or regions.
For nodes, a useful conceptual set is:
</p>

<ul>
  <li><code>inactive</code>,</li>
  <li><code>waiting</code>,</li>
  <li><code>ready</code> when readiness is exposed,</li>
  <li><code>running</code>,</li>
  <li><code>completed</code>,</li>
  <li><code>faulted</code>,</li>
  <li><code>canceled</code>.</li>
</ul>

<p>
For regions, a useful conceptual set is:
</p>

<ul>
  <li><code>inactive</code>,</li>
  <li><code>selected</code>,</li>
  <li><code>running</code>,</li>
  <li><code>completed</code>.</li>
</ul>

<p>
These are <strong>projection states</strong>, not a required runtime-internal state machine.
A runtime MAY use different internal machinery provided that the IDE-visible meaning remains equivalent.
</p>

<h3>9.3 Paused snapshots</h3>

<p>
If a live execution instance is shown as <code>paused</code>, the visible state MUST correspond to a valid
language-level safe pause boundary.
The IDE-facing paused view MUST therefore be interpretable as a
<strong>pause-consistent snapshot</strong>.
</p>

<p>
A paused snapshot MAY include, where supported by the active observability profile:
</p>

<ul>
  <li>instance state,</li>
  <li>relevant node and structure activity,</li>
  <li>relevant committed edge values,</li>
  <li>relevant committed local-memory state,</li>
  <li>the execution context needed to interpret the paused state correctly.</li>
</ul>

<hr/>

<h2 id="event-vocabulary">10. Event Vocabulary</h2>

<h3>10.1 General rule</h3>

<p>
FROG v0.1 defines a <strong>canonical semantic event vocabulary</strong> for observability.
These names define meaning.
They do <strong>not</strong> define a mandatory wire format or mandatory API shape.
</p>

<p>
Not every implementation is required to expose every event as a standalone transport-level record.
A profile MAY expose an equivalent snapshot-oriented or summarized form,
provided that the semantic meaning that remains exposed is preserved.
</p>

<h3>10.2 Canonical event names</h3>

<p>
The canonical semantic event names for v0.1 are:
</p>

<ul>
  <li><code>instance_started</code></li>
  <li><code>instance_paused</code></li>
  <li><code>instance_resumed</code></li>
  <li><code>instance_completed</code></li>
  <li><code>instance_faulted</code></li>
  <li><code>instance_aborted</code></li>
  <li><code>node_became_ready</code></li>
  <li><code>node_started</code></li>
  <li><code>node_completed</code></li>
  <li><code>node_faulted</code></li>
  <li><code>edge_value_available</code></li>
  <li><code>structure_entered</code></li>
  <li><code>region_selected</code></li>
  <li><code>iteration_started</code></li>
  <li><code>iteration_completed</code></li>
  <li><code>structure_completed</code></li>
  <li><code>state_read</code></li>
  <li><code>state_updated</code></li>
</ul>

<p>
Readiness exposure is optional in v0.1.
Therefore <code>node_became_ready</code> MAY be omitted by a weaker profile,
but if readiness-sensitive tooling is supported, its meaning MUST remain consistent.
</p>

<p>
Implementations MAY expose additional events.
Additional events MUST NOT contradict the meaning of the canonical names above.
</p>

<h3>10.3 Common semantic fields</h3>

<p>
A conceptual event SHOULD carry enough information for source projection and causal interpretation.
Typical semantic fields include:
</p>

<ul>
  <li><code>event</code> — canonical semantic event name,</li>
  <li><code>instance_id</code> — live execution instance identity,</li>
  <li><code>sequence</code> — monotonically increasing causal order within the instance,</li>
  <li><code>object</code> — primary observed source-aligned object,</li>
  <li><code>context</code> — relevant execution context,</li>
  <li><code>timestamp</code> — optional implementation timestamp,</li>
  <li><code>details</code> — event-specific additional data.</li>
</ul>

<p>
The exact concrete transport representation is intentionally left open.
</p>

<hr/>

<h2 id="safe-boundary-consumption">11. Safe-Boundary Consumption</h2>

<h3>11.1 Safe observation points</h3>

<p>
When a runtime exposes an observable view to the IDE, that view MUST correspond to a language-valid
safe observation point whenever the observation claims to represent committed source-level state.
The IDE MUST therefore be able to interpret the visible state as a coherent causal prefix,
not as an arbitrary runtime microstate.
</p>

<h3>11.2 Paused state</h3>

<p>
If a live execution instance is reported as <code>paused</code>, it MUST be paused only at a valid safe pause boundary.
The IDE-facing paused view MUST be consistent with the corresponding pause-consistent snapshot.
</p>

<h3>11.3 No impossible source state</h3>

<p>
The IDE MUST NOT be forced to represent any impossible intermediate source state, including:
</p>

<ul>
  <li>a node as completed when the corresponding source-visible completion is not yet committed,</li>
  <li>a value as available before its source-level availability is committed,</li>
  <li>a local-memory value as half-updated,</li>
  <li>a region selection that contradicts the active structure context,</li>
  <li>a sub-FROG observation that loses the required caller/callee relationship.</li>
</ul>

<p>
This section defines the IDE-side consumption rule only.
It does not redefine the boundary semantics themselves.
</p>

<hr/>

<h2 id="ordering-and-causal-consistency">12. Ordering and Causal Consistency</h2>

<h3>12.1 Sequence order</h3>

<p>
Within one live execution instance, observable events MUST admit a monotonically increasing causal order.
This order MUST be sufficient for an IDE to reconstruct a consistent source-aligned interpretation.
</p>

<h3>12.2 Parallel activity</h3>

<p>
Independent parallel activity need not imply one universal total semantic order beyond causal consistency.
If two independent node activations are both valid and concurrent, a runtime MAY emit them in either order,
provided that:
</p>

<ul>
  <li>causal dependencies are preserved,</li>
  <li>impossible source behavior is not implied,</li>
  <li>the instance-local order remains internally consistent.</li>
</ul>

<h3>12.3 Timestamps</h3>

<p>
Implementations MAY attach wall-clock or monotonic timestamps to observations.
Such timestamps are informative unless a stricter observability profile defines stronger timing meaning.
</p>

<h3>12.4 Event loss and weaker profiles</h3>

<p>
A profile intended for interactive debugging SHOULD avoid dropping canonical observability events.
A lower-overhead profile MAY summarize or sample observations, but only if it is explicitly weaker than the
full interactive observation profile.
</p>

<hr/>

<h2 id="ide-requirements">13. IDE Requirements</h2>

<p>
An IDE that claims support for FROG execution observability SHOULD be able to project at least:
</p>

<ul>
  <li>instance lifecycle state,</li>
  <li>node start and completion overlays,</li>
  <li>edge-level value-availability visibility,</li>
  <li>structure entry and selected-region visibility,</li>
  <li>loop-iteration progression when relevant,</li>
  <li>fault localization to the most relevant source object when possible.</li>
</ul>

<p>
If readiness is exposed by the active observability profile, the IDE SHOULD also be able to project
readiness-sensitive overlays or equivalent readiness-aware diagnostic views.
</p>

<p>
An IDE MAY present the observable meaning through:
</p>

<ul>
  <li>diagram overlays,</li>
  <li>trace panes,</li>
  <li>logs,</li>
  <li>debugging views,</li>
  <li>probe integrations,</li>
  <li>watch integrations,</li>
  <li>other equivalent inspection views.</li>
</ul>

<p>
Visual rendering style is not standardized here.
Only the tooling-facing observable meaning is standardized here.
</p>

<hr/>

<h2 id="illustrative-observation-shapes">14. Illustrative Observation Shapes</h2>

<p>
The examples below are illustrative only.
They show one possible structured representation of the conceptual observability model.
They are <strong>not</strong> a required transport format.
</p>

<h3>14.1 Node start</h3>

<pre><code>{
  "event": "node_started",
  "instance_id": "run_42",
  "sequence": 118,
  "object": {
    "kind": "node",
    "id": "add_1"
  },
  "context": {
    "subfrog_stack": [],
    "structure_stack": []
  },
  "details": {
    "activation_id": "act_118"
  }
}</code></pre>

<h3>14.2 Edge value available inside a loop iteration</h3>

<pre><code>{
  "event": "edge_value_available",
  "instance_id": "run_42",
  "sequence": 241,
  "object": {
    "kind": "edge",
    "id": "e_sum"
  },
  "context": {
    "subfrog_stack": [],
    "structure_stack": [
      {
        "structure_id": "loop_1",
        "region_id": "body",
        "iteration": 3
      }
    ]
  },
  "details": {
    "source_node": "add_1",
    "source_port": "result",
    "value_preview": "17.5"
  }
}</code></pre>

<h3>14.3 Region selected</h3>

<pre><code>{
  "event": "region_selected",
  "instance_id": "run_42",
  "sequence": 89,
  "object": {
    "kind": "region",
    "structure_id": "case_enabled",
    "region_id": "true_case"
  },
  "context": {
    "subfrog_stack": [],
    "structure_stack": []
  },
  "details": {
    "selector_preview": true
  }
}</code></pre>

<h3>14.4 Local-memory update</h3>

<pre><code>{
  "event": "state_updated",
  "instance_id": "run_42",
  "sequence": 132,
  "object": {
    "kind": "local_memory",
    "node_id": "delay_1"
  },
  "context": {
    "subfrog_stack": [],
    "structure_stack": []
  },
  "details": {
    "activation_id": "act_130",
    "value_preview": "5.0"
  }
}</code></pre>

<hr/>

<h2 id="out-of-scope-for-v01">15. Out of Scope for v0.1</h2>

<p>
The following remain intentionally out of scope for this document:
</p>

<ul>
  <li>execution-model ownership,</li>
  <li>safe-observation and safe-debug-stop semantic ownership,</li>
  <li>breakpoint semantics,</li>
  <li>single-step semantics,</li>
  <li>step-into / step-over / step-out behavior,</li>
  <li>probe-specific UI behavior,</li>
  <li>watch-specific UI behavior,</li>
  <li>timeline scrubbing,</li>
  <li>reverse execution,</li>
  <li>deterministic replay,</li>
  <li>distributed multi-runtime observability,</li>
  <li>profiling counters and performance metrics beyond optional timestamps,</li>
  <li>deep value-serialization formats,</li>
  <li>transport API standardization.</li>
</ul>

<hr/>

<h2 id="summary">16. Summary</h2>

<p>
FROG execution observability defines the minimal source-aligned execution view that an IDE may consume from
a live execution instance.
It does <strong>not</strong> redefine execution semantics.
Instead, it standardizes:
</p>

<ul>
  <li>how execution activity maps back to source identity,</li>
  <li>how dynamic repetitions are disambiguated through execution context,</li>
  <li>which source-aligned execution objects may be observed,</li>
  <li>which canonical semantic event names may be exposed,</li>
  <li>which consistency guarantees the IDE may rely on when consuming safe language-level boundaries.</li>
</ul>

<p>
This observability layer is the foundation consumed by execution overlays, debugging, probes, watches,
and richer inspection tooling, while preserving the architectural separation between:
</p>

<ul>
  <li>source representation,</li>
  <li>execution semantics,</li>
  <li>primitive-local behavior,</li>
  <li>tooling-facing observation.</li>
</ul>

<hr/>

<h2 id="license">17. License</h2>

<p>
This specification is part of the FROG repository and is governed by the repository license and contribution rules.
</p>
