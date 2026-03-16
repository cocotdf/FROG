<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG IDE Execution Observability Specification</h1>

<p align="center">
Definition of the execution observability contract exposed to a FROG IDE<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Goals</a></li>
  <li><a href="#scope-for-v01">3. Scope for v0.1</a></li>
  <li><a href="#relation-with-other-specifications">4. Relation with Other Specifications</a></li>
  <li><a href="#design-principles">5. Design Principles</a></li>
  <li><a href="#what-this-document-defines">6. What This Document Defines</a></li>
  <li><a href="#observed-execution-instance-projection">7. Observed Execution Instance Projection</a></li>
  <li><a href="#source-projection-and-execution-context">8. Source Projection and Execution Context</a></li>
  <li><a href="#observable-state-projection">9. Observable State Projection</a></li>
  <li><a href="#observable-event-model">10. Observable Event Model</a></li>
  <li><a href="#node-activation-projection">11. Node Activation Projection</a></li>
  <li><a href="#edge-and-value-projection">12. Edge and Value Projection</a></li>
  <li><a href="#structure-and-region-projection">13. Structure and Region Projection</a></li>
  <li><a href="#local-memory-projection">14. Local-Memory Projection</a></li>
  <li><a href="#sub-frog-projection">15. Sub-FROG Projection</a></li>
  <li><a href="#ui-effect-sequencing-projection">16. UI-Effect Sequencing Projection</a></li>
  <li><a href="#projection-of-language-level-safe-boundaries">17. Projection of Language-Level Safe Boundaries</a></li>
  <li><a href="#ordering-time-delivery-and-observability-profiles">18. Ordering, Time, Delivery, and Observability Profiles</a></li>
  <li><a href="#ide-requirements">19. IDE Requirements</a></li>
  <li><a href="#illustrative-event-shapes">20. Illustrative Event Shapes</a></li>
  <li><a href="#out-of-scope-for-v01">21. Out of Scope for v0.1</a></li>
  <li><a href="#summary">22. Summary</a></li>
  <li><a href="#license">23. License</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the <strong>execution observability contract</strong> exposed to a FROG IDE.
It specifies how language-defined execution activity becomes observable to IDE-facing tooling in a source-aligned way.
</p>

<p>
Execution observability does not redefine execution semantics.
Execution meaning remains defined by the validated executable graph and by the relevant language and library specifications.
This document defines the IDE-facing projection needed by tooling such as:
</p>

<ul>
  <li>diagram execution highlighting,</li>
  <li>live node-state overlays,</li>
  <li>structure and region activity overlays,</li>
  <li>probe updates,</li>
  <li>watch updates,</li>
  <li>execution traces, logs, and diagnostics,</li>
  <li>debugger-facing observation feeds.</li>
</ul>

<p>
Execution observability is therefore an IDE-facing contract over language-defined execution activity.
It is not a replacement for the execution model and not a replacement for execution-control boundaries.
</p>

<pre><code>Execution meaning
        -&gt; defined by Language/ and Libraries/

Execution observability
        -&gt; IDE-facing projection of that meaning

Debugging / probes / watch
        -&gt; consume the projection
</code></pre>

<hr/>

<h2 id="goals">2. Goals</h2>

<p>This document has the following goals:</p>

<ul>
  <li>define what a FROG IDE may observe from a live execution,</li>
  <li>preserve source-level identity and execution context in IDE-facing projections,</li>
  <li>support debugging, probes, watch behavior, and related tooling without relocating execution semantics into <code>IDE/</code>,</li>
  <li>remain compatible with multiple runtimes, schedulers, and execution strategies,</li>
  <li>separate <strong>execution meaning</strong> from <strong>execution observability</strong>,</li>
  <li>provide a stable contract for event-oriented or snapshot-oriented tooling integration.</li>
</ul>

<hr/>

<h2 id="scope-for-v01">3. Scope for v0.1</h2>

<p>
For FROG v0.1, this document standardizes the minimal IDE-facing observability concepts needed by execution-aware tooling:
</p>

<ul>
  <li>how a live execution instance is exposed to the IDE,</li>
  <li>how source identity and execution context are projected,</li>
  <li>which high-level states an IDE may project,</li>
  <li>which canonical observable event names and event categories may be exposed,</li>
  <li>how node, edge, structure, region, local-memory, sub-FROG, and UI-effect activity may be projected,</li>
  <li>what consistency guarantees the IDE may assume when consuming language-level safe boundaries.</li>
</ul>

<p>
FROG v0.1 does <strong>not</strong> standardize:
</p>

<ul>
  <li>the execution model itself,</li>
  <li>the safe-observation and safe-debug-stop semantics themselves,</li>
  <li>a transport protocol between runtime and IDE,</li>
  <li>a binary event-stream format,</li>
  <li>a mandatory timestamp format,</li>
  <li>a mandatory value-serialization format,</li>
  <li>a single required scheduler implementation,</li>
  <li>the full debugging-control model,</li>
  <li>the full probe model,</li>
  <li>the full watch model.</li>
</ul>

<p>
Those concerns are defined elsewhere or intentionally remain out of scope for this document.
</p>

<hr/>

<h2 id="relation-with-other-specifications">4. Relation with Other Specifications</h2>

<p>
This document depends on the following specifications:
</p>

<ul>
  <li><code>IDE/Readme.md</code> for the IDE-facing architectural boundary between authoring, source identity, execution integration, and observability,</li>
  <li><code>IDE/Debugging.md</code> for pause, resume, breakpoint, and stepping behavior built on top of observability,</li>
  <li><code>IDE/Probes.md</code> for source-aligned probe targets and probe update meaning,</li>
  <li><code>IDE/Watch.md</code> for persistent watch targets and watch update meaning,</li>
  <li><code>Expression/Diagram.md</code> for the canonical source node and edge model,</li>
  <li><code>Expression/Control structures.md</code> for canonical structure and region representation,</li>
  <li><code>Expression/State and cycles.md</code> for canonical local-memory representation,</li>
  <li><code>Expression/Widget interaction.md</code> for explicit UI-effect sequencing through <code>ui_in</code> and <code>ui_out</code>,</li>
  <li><code>Language/Execution model.md</code> for validated executable graph, live execution instance, source identity, activation, execution context, semantic execution milestones, and committed source-level state,</li>
  <li><code>Language/Execution control and observation boundaries.md</code> for safe observation points, pause-consistent snapshots, safe debug stops, and completion/fault/abort boundary semantics,</li>
  <li><code>Language/Control structures.md</code> for normative control-structure execution semantics,</li>
  <li><code>Language/State and cycles.md</code> for normative local-memory and feedback-cycle execution semantics,</li>
  <li><code>Libraries/Core.md</code> for primitive-local behavior such as <code>frog.core.delay</code>,</li>
  <li><code>Libraries/UI.md</code> for standardized executable UI interaction primitives.</li>
</ul>

<p>
This document MUST NOT contradict those specifications.
If a conflict appears:
</p>

<ul>
  <li><code>Expression/</code> remains authoritative for canonical source identity and source-visible representation,</li>
  <li><code>Language/</code> remains authoritative for normative execution meaning and safe execution boundaries,</li>
  <li><code>Libraries/</code> remain authoritative for primitive identity, required ports, required metadata, and primitive-local behavior,</li>
  <li><code>IDE/</code> remains authoritative only for the observability contract exposed to tools.</li>
</ul>

<p>
This document is intentionally placed in <code>IDE/</code> because it defines how execution is projected to tools, not what execution means in the language itself.
</p>

<hr/>

<h2 id="design-principles">5. Design Principles</h2>

<h3>5.1 Source alignment</h3>

<p>
Observable execution MUST remain attributable to source-level objects known to the FROG Program Model.
A user should be able to understand runtime activity by looking at the source diagram and related front-panel elements.
</p>

<h3>5.2 Language-derived meaning</h3>

<p>
The IDE-facing projection defined here MUST be derived from language-defined execution meaning.
This document MUST NOT be used to create an alternative execution semantics layer inside <code>IDE/</code>.
</p>

<h3>5.3 Runtime independence</h3>

<p>
Different runtimes MAY use different internal schedulers, queues, threads, buffers, batching strategies, or optimization strategies.
Those internal choices MAY vary.
The observable IDE-facing meaning MUST remain equivalent.
</p>

<h3>5.4 Causal consistency</h3>

<p>
The IDE-facing event stream or snapshot model MUST represent a causally consistent view of execution.
The IDE MUST NOT be forced to interpret impossible or self-contradictory source-level states.
</p>

<h3>5.5 Capability profiles and observability profiles remain distinct</h3>

<p>
The term <strong>profile</strong> is used elsewhere in the repository for optional standardized capability families defined in <code>Profiles/</code>.
This document additionally refers to <strong>observability profiles</strong>, meaning levels of detail or strength of the IDE-facing execution-observation contract.
These two notions MUST NOT be conflated.
</p>

<ul>
  <li>a capability profile defines what executable capability families exist,</li>
  <li>an observability profile defines how much execution detail is exposed to tools.</li>
</ul>

<h3>5.6 Minimal but extensible</h3>

<p>
FROG v0.1 defines a minimal observability core.
Stricter observability profiles MAY expose additional fields, more detailed events, richer value snapshots, stronger ordering guarantees, or richer retention behavior, provided that the v0.1 meaning remains preserved.
</p>

<h3>5.7 Observability is descriptive, not prescriptive</h3>

<p>
This document describes what the IDE may observe and consume.
It does not require runtimes to execute nodes in any one internal implementation order beyond what is necessary to preserve the validated observable meaning.
</p>

<hr/>

<h2 id="what-this-document-defines">6. What This Document Defines</h2>

<p>
Execution observability defines the <strong>observable projection</strong> of language-defined execution activity to an IDE.
At minimum, this projection includes:
</p>

<ul>
  <li>instance lifecycle visibility,</li>
  <li>node activation visibility,</li>
  <li>edge value-availability visibility,</li>
  <li>structure and region visibility,</li>
  <li>local-memory visibility,</li>
  <li>sub-FROG visibility,</li>
  <li>projection of safe pause and terminal states to tools,</li>
  <li>canonical IDE-facing event categories and names.</li>
</ul>

<p>
This projection is conceptual.
Implementations MAY expose it through callbacks, event queues, polling APIs, logs, trace buffers, or equivalent mechanisms.
</p>

<hr/>

<h2 id="observed-execution-instance-projection">7. Observed Execution Instance Projection</h2>

<p>
A live execution instance is defined by <code>Language/Execution model.md</code>.
This document defines how that instance becomes observable to the IDE.
</p>

<p>
Every observable event or snapshot belongs to exactly one live execution instance.
An IDE-facing observability feed MUST therefore provide an identifier unique within the observing session.
This identifier is referred to in this document as <code>instance_id</code>.
</p>

<p>
The IDE-facing projection of an instance SHOULD make it possible to distinguish:
</p>

<ul>
  <li>different runs of the same FROG,</li>
  <li>different active instances observed concurrently,</li>
  <li>different retained histories or traces associated with different instances.</li>
</ul>

<p>
This document does not redefine what a live execution instance is.
It standardizes only the minimum information needed to observe one coherently from IDE tooling.
</p>

<hr/>

<h2 id="source-projection-and-execution-context">8. Source Projection and Execution Context</h2>

<h3>8.1 Source projection</h3>

<p>
Source identity is defined by the source model and by the language execution model.
This document defines how that identity SHOULD be carried into IDE-facing observation.
</p>

<p>
Every observable execution event SHOULD be attributable to a source-level object where applicable.
Relevant source-level objects include:
</p>

<ul>
  <li>a diagram,</li>
  <li>a node,</li>
  <li>a node port,</li>
  <li>an edge,</li>
  <li>a structure,</li>
  <li>a structure region,</li>
  <li>a sub-FROG call site,</li>
  <li>a local-memory slot owned by a node instance.</li>
</ul>

<p>
When the source specification already defines stable identifiers such as <code>node.id</code>, <code>edge.id</code>, or <code>region.id</code>, observability SHOULD use those identifiers directly.
When an observed object does not have a canonical serialized identifier, the FROG Program Model MAY assign a stable IDE-visible identifier.
</p>

<h3>8.2 Execution context projection</h3>

<p>
Execution context is defined at the language level.
This document standardizes its IDE-facing projection.
</p>

<p>
Because the same source node may activate multiple times and under nested scopes, observable activity MUST also carry an execution context whenever source identity alone is insufficient.
The projected execution context MAY include:
</p>

<ul>
  <li>sub-FROG invocation nesting,</li>
  <li>structure nesting,</li>
  <li>selected region identifier,</li>
  <li>loop iteration index when applicable,</li>
  <li>activation identifier for the current node activation.</li>
</ul>

<p>
This context is required so that an IDE can distinguish, for example:
</p>

<ul>
  <li>different iterations of the same <code>for_loop</code>,</li>
  <li>different activations of a node inside a <code>while_loop</code>,</li>
  <li>activity inside a selected <code>case</code> region versus an inactive region,</li>
  <li>activity inside a nested sub-FROG versus the caller diagram.</li>
</ul>

<h3>8.3 Activation identity projection</h3>

<p>
Every node activation SHOULD have an <code>activation_id</code> unique within its live execution instance when the active observability profile exposes activation-level detail.
This identifier is especially important for loops, repeated executions, traces, probes, and watch correlation.
</p>

<hr/>

<h2 id="observable-state-projection">9. Observable State Projection</h2>

<h3>9.1 Instance-state projection</h3>

<p>
Language-level high-level instance states are defined elsewhere.
This document standardizes how an IDE MAY project them.
</p>

<p>
A live execution instance MUST be projectable in one of the following execution-facing states:
</p>

<ul>
  <li><code>running</code> — execution is actively progressing,</li>
  <li><code>paused</code> — execution is suspended at a language-valid safe pause boundary,</li>
  <li><code>completed</code> — execution finished normally,</li>
  <li><code>faulted</code> — execution terminated because of an execution fault,</li>
  <li><code>aborted</code> — execution was terminated externally without normal completion.</li>
</ul>

<p>
An IDE MAY additionally use local tooling states such as <code>created</code>, <code>attached</code>, or <code>detached</code> before or around active execution integration.
Such tooling states are IDE-local and MUST NOT be confused with language-level execution states.
</p>

<h3>9.2 Node-observation states</h3>

<p>
For IDE projection purposes, a node activation MAY be observed through the following conceptual states:
</p>

<ul>
  <li><code>inactive</code> — the node is outside the currently relevant dynamic path,</li>
  <li><code>waiting</code> — the node belongs to the relevant dynamic path but its activation conditions are not yet satisfied,</li>
  <li><code>ready</code> — the node is eligible to begin execution when readiness is exposed by the active observability profile,</li>
  <li><code>running</code> — the node is currently executing,</li>
  <li><code>completed</code> — the node activation completed normally,</li>
  <li><code>faulted</code> — the node activation failed,</li>
  <li><code>canceled</code> — the node activation will not occur because the containing instance or relevant scope was aborted.</li>
</ul>

<p>
These are projection states, not a required internal runtime state machine.
A runtime MAY internally use a different representation provided that the IDE-visible meaning remains equivalent.
</p>

<h3>9.3 Region-observation states</h3>

<p>
A structure region MAY be projected as:
</p>

<ul>
  <li><code>inactive</code>,</li>
  <li><code>selected</code>,</li>
  <li><code>running</code>,</li>
  <li><code>completed</code>.</li>
</ul>

<p>
For a <code>case</code> structure, exactly one region becomes selected for each structure activation.
For loop structures, the canonical body region is repeatedly activated across iterations.
</p>

<hr/>

<h2 id="observable-event-model">10. Observable Event Model</h2>

<h3>10.1 Canonical event categories</h3>

<p>
FROG v0.1 defines the following canonical IDE-facing observable event categories:
</p>

<ul>
  <li>instance lifecycle events,</li>
  <li>node activation events,</li>
  <li>edge value-availability events,</li>
  <li>structure and region events,</li>
  <li>local-memory events,</li>
  <li>pause and resume events,</li>
  <li>fault events.</li>
</ul>

<h3>10.2 Canonical event names</h3>

<p>
The canonical IDE-facing semantic event names for v0.1 are:
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
These names define the canonical observability vocabulary.
Not every active observability profile is required to expose every event directly.
When a profile omits a finer-grained event such as <code>node_became_ready</code>, it MUST still preserve the observable meanings that remain exposed.
</p>

<p>
Implementations MAY expose additional events.
When they do, the additional events MUST NOT contradict the meaning of the canonical events above.
</p>

<h3>10.3 Common event fields</h3>

<p>
Each observable event SHOULD include enough information for source projection and trace ordering.
A conceptual event therefore typically includes:
</p>

<ul>
  <li><code>event</code> — canonical event name,</li>
  <li><code>instance_id</code> — live execution instance identifier,</li>
  <li><code>sequence</code> — monotonically increasing event order within the instance,</li>
  <li><code>object</code> — the primary observed object,</li>
  <li><code>context</code> — projected execution context,</li>
  <li><code>timestamp</code> — optional runtime timestamp,</li>
  <li><code>details</code> — event-specific additional fields.</li>
</ul>

<p>
The exact concrete transport shape is not standardized by this document.
</p>

<hr/>

<h2 id="node-activation-projection">11. Node Activation Projection</h2>

<h3>11.1 General model</h3>

<p>
A source node MAY activate zero, one, or multiple times during a live execution instance, depending on language-defined execution meaning.
This document defines how such activity becomes visible to the IDE.
</p>

<h3>11.2 Ready visibility</h3>

<p>
If the active observability profile exposes readiness, the event <code>node_became_ready</code> indicates that a node activation is now eligible to start according to the validated execution semantics.
</p>

<p>
A runtime MAY internally transition from readiness to execution immediately.
Even in that case, an interactive observability profile SHOULD still preserve a logical ready step when readiness-sensitive tooling relies on it.
</p>

<h3>11.3 Start and completion</h3>

<p>
A normal node activation SHOULD be observable through an equivalent causal pattern such as:
</p>

<pre><code>node_became_ready   // when readiness is exposed
node_started
node_completed
</code></pre>

<p>
A faulting activation SHOULD be observable through an equivalent causal pattern such as:
</p>

<pre><code>node_became_ready   // when readiness is exposed
node_started
node_faulted
</code></pre>

<p>
A node MUST NOT be projected as completed before the corresponding source-visible outputs and state-related effects for that activation are committed according to the language-level model.
</p>

<h3>11.4 Source kinds</h3>

<p>
This node-activation projection applies uniformly to standard node kinds where relevant, including:
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
The exact meaning of their ports remains defined by the corresponding source, library, and language specifications.
This document defines only their observability-side projection.
</p>

<hr/>

<h2 id="edge-and-value-projection">12. Edge and Value Projection</h2>

<h3>12.1 Edge-level visibility</h3>

<p>
A FROG IDE SHOULD be able to observe when a value becomes available on an edge.
This is represented by the canonical event:
</p>

<pre><code>edge_value_available
</code></pre>

<p>
The primary observed object for that event SHOULD identify the edge by its source-level <code>edge.id</code> when such an identifier exists.
</p>

<h3>12.2 Meaning</h3>

<p>
The event <code>edge_value_available</code> means that, within the current live execution context, a value is now available for ordinary source-level understanding.
It does not require the runtime to reveal internal buffer implementation details.
</p>

<h3>12.3 Payload visibility</h3>

<p>
This document does not require every runtime to expose a full value payload for every observed edge event.
A stricter observability profile MAY expose one of the following:
</p>

<ul>
  <li>a full value snapshot,</li>
  <li>a bounded value preview,</li>
  <li>a summarized textual or structural representation,</li>
  <li>an opaque handle from which a later tool can request the value,</li>
  <li>no payload, with only value availability indicated.</li>
</ul>

<p>
The chosen payload strategy MUST NOT alter execution meaning.
It only affects what the IDE can display.
</p>

<h3>12.4 Fan-out</h3>

<p>
If one source output drives multiple edges, each edge MAY be observed separately at the source-aligned level, because probes, overlays, and diagnostics are naturally expressed on edges.
A runtime MAY internally optimize such fan-out, but the IDE-visible meaning SHOULD remain edge-based.
</p>

<hr/>

<h2 id="structure-and-region-projection">13. Structure and Region Projection</h2>

<h3>13.1 General rule</h3>

<p>
A structure activation is itself observable.
The IDE SHOULD be able to see:
</p>

<ul>
  <li>when the structure is entered,</li>
  <li>which region becomes active,</li>
  <li>when an iteration begins and ends for loops,</li>
  <li>when the structure completes.</li>
</ul>

<h3>13.2 Case structure</h3>

<p>
For a <code>case</code> structure, the canonical observable model SHOULD include an equivalent causal pattern such as:
</p>

<pre><code>structure_entered
region_selected
structure_completed
</code></pre>

<p>
The <code>region_selected</code> event MUST identify the selected <code>region.id</code>.
Inactive regions MUST remain non-executing for that activation.
An IDE MAY project inactive case regions with a visually dimmed state.
</p>

<h3>13.3 For loop</h3>

<p>
For a <code>for_loop</code>, the canonical observable model SHOULD include:
</p>

<ul>
  <li>one <code>structure_entered</code> event for the loop activation,</li>
  <li>zero or more pairs of <code>iteration_started</code> and <code>iteration_completed</code>,</li>
  <li>one <code>structure_completed</code> event when the loop finishes.</li>
</ul>

<p>
Each iteration event SHOULD identify the loop structure and the current iteration index.
If the loop executes zero iterations, the body region is never activated.
That fact MAY be represented either by the absence of iteration events or by a stricter observability profile-specific summary event.
</p>

<h3>13.4 While loop</h3>

<p>
For a <code>while_loop</code>, the canonical observable model is similar to <code>for_loop</code>:
</p>

<ul>
  <li>one <code>structure_entered</code> event for the loop activation,</li>
  <li>one or more <code>iteration_started</code> and <code>iteration_completed</code> event pairs unless the instance faults or aborts,</li>
  <li>one <code>structure_completed</code> event when loop termination occurs normally.</li>
</ul>

<p>
The continue/termination meaning of <code>while_loop</code> remains defined by the relevant language specifications.
This document defines only how that activity becomes visible.
</p>

<h3>13.5 Region-local activity</h3>

<p>
Nodes inside a structure region are observed in the execution context of that region.
For example, a node inside a loop body is not merely “the same node again”; it is the same source node under a different dynamic iteration context.
</p>

<hr/>

<h2 id="local-memory-projection">14. Local-Memory Projection</h2>

<h3>14.1 General rule</h3>

<p>
Local-memory primitives participate in ordinary node execution and additionally expose state-related observable meaning.
For IDE purposes, this state-related activity MUST be observable in a source-aligned way.
</p>

<h3>14.2 Canonical events</h3>

<p>
The canonical local-memory projection events are:
</p>

<ul>
  <li><code>state_read</code></li>
  <li><code>state_updated</code></li>
</ul>

<p>
These events apply to the local-memory slot owned by the node instance in the current live execution instance.
</p>

<h3>14.3 <code>frog.core.delay</code></h3>

<p>
For <code>frog.core.delay</code>, the primitive-local behavior and the language-level local-memory semantics are defined elsewhere.
This document standardizes only how the related source-aligned state activity becomes observable to the IDE.
</p>

<p>
For one normal activation of <code>frog.core.delay</code>, a conforming observability profile SHOULD make the following source-aligned facts observable in an equivalent causal order:
</p>

<ul>
  <li>the delay node activation becomes ready when readiness is exposed and then starts,</li>
  <li>the previously stored state is the state associated with the observed output of that activation,</li>
  <li>the next stored state is updated from the observed input of that activation,</li>
  <li>the activation completes only after the observable state transition for that activation is committed.</li>
</ul>

<p>
A possible conceptual event sequence is:
</p>

<pre><code>node_became_ready   // when readiness is exposed
state_read
node_started
edge_value_available   // for out
state_updated
node_completed
</code></pre>

<p>
An implementation MAY merge or internally reorder operations provided that the exposed observable meaning remains equivalent and does not contradict the primitive-local behavior defined elsewhere.
</p>

<h3>14.4 Initial state visibility</h3>

<p>
A stricter observability profile MAY expose the initial state of a local-memory node before first activation.
Such visibility is optional in v0.1.
However, if shown, it MUST match the deterministic source and language semantics already defined elsewhere.
</p>

<hr/>

<h2 id="sub-frog-projection">15. Sub-FROG Projection</h2>

<h3>15.1 Call-site visibility</h3>

<p>
A <code>subfrog</code> node is observable at least at the call-site level.
The caller diagram MUST be able to observe the invocation of the sub-FROG as activity on the <code>subfrog</code> node itself.
</p>

<h3>15.2 Nested visibility</h3>

<p>
A stricter observability profile MAY additionally expose nested observable activity inside the referenced FROG.
When this is done:
</p>

<ul>
  <li>the nested activity MUST remain associated with the live caller instance through execution context,</li>
  <li>the nested activity MUST identify the sub-FROG call stack,</li>
  <li>the IDE MUST be able to distinguish caller-level and callee-level activity.</li>
</ul>

<p>
This distinction is necessary for debugging behaviors such as step-into and step-over, but those controls are standardized elsewhere.
</p>

<hr/>

<h2 id="ui-effect-sequencing-projection">16. UI-Effect Sequencing Projection</h2>

<h3>16.1 General rule</h3>

<p>
The widget interaction model defines optional <code>ui_in</code> and <code>ui_out</code> ports for explicit UI-effect sequencing.
These ports are opaque sequencing ports, not ordinary data values.
</p>

<h3>16.2 Observability meaning</h3>

<p>
If a runtime exposes activity related to <code>ui_in</code> and <code>ui_out</code>, the IDE MUST interpret that activity as effect-order visibility rather than ordinary valueflow visibility.
</p>

<p>
In practice:
</p>

<ul>
  <li>an IDE MAY highlight these edges differently from ordinary data edges,</li>
  <li>a stricter observability profile MAY expose explicit UI-effect start and completion events,</li>
  <li>the absence of explicit UI-effect events in v0.1 does not invalidate UI sequencing semantics already defined by source and library specifications.</li>
</ul>

<h3>16.3 No implicit UI semantics</h3>

<p>
This document MUST NOT be interpreted as introducing implicit UI event scheduling.
Only the existing explicit UI sequencing model and the ordinary node execution model apply.
</p>

<hr/>

<h2 id="projection-of-language-level-safe-boundaries">17. Projection of Language-Level Safe Boundaries</h2>

<h3>17.1 General rule</h3>

<p>
Safe observation points, pause-consistent snapshots, and safe debug stops are defined by
<code>Language/Execution control and observation boundaries.md</code>.
This document defines how the IDE consumes and projects those boundaries.
</p>

<h3>17.2 Safe observation projection</h3>

<p>
When a runtime exposes an observation point to an IDE-facing observability feed, the exposed view MUST correspond to a language-valid safe observation boundary.
The IDE MUST therefore be able to interpret the received state as a coherent causal prefix rather than as an arbitrary transient runtime microstate.
</p>

<h3>17.3 Paused projection</h3>

<p>
If a live execution instance enters the <code>paused</code> state, it MUST do so only at a language-valid safe pause boundary.
The IDE-facing paused view MUST therefore be interpretable as a pause-consistent snapshot.
</p>

<p>
The IDE MAY then project:
</p>

<ul>
  <li>instance state,</li>
  <li>currently relevant or last-completed observable activity,</li>
  <li>current local-memory values if exposed by the active observability profile,</li>
  <li>already committed edge values if such visibility is supported,</li>
  <li>execution context required to interpret the paused state correctly.</li>
</ul>

<h3>17.4 No contradiction rule for IDE projection</h3>

<p>
The IDE MUST NOT be forced to represent:
</p>

<ul>
  <li>a node as both completed and not yet committed,</li>
  <li>a value as available when it is not yet committed at the language level,</li>
  <li>a local-memory state as half-updated,</li>
  <li>a selected region in a contradictory way,</li>
  <li>caller/callee nesting in a way that loses the relevant execution context.</li>
</ul>

<p>
This section defines the observability-side consumption rule.
It does not redefine the boundary semantics themselves.
</p>

<hr/>

<h2 id="ordering-time-delivery-and-observability-profiles">18. Ordering, Time, Delivery, and Observability Profiles</h2>

<h3>18.1 Sequence order</h3>

<p>
Within one live execution instance, observable events MUST admit a monotonically increasing sequence order.
This order MUST be causally consistent.
</p>

<h3>18.2 Parallel activity</h3>

<p>
Independent parallel activity need not imply one universal semantic order beyond causal consistency.
If two independent node activations are both valid and concurrent, a runtime MAY choose either event-emission order, provided that:
</p>

<ul>
  <li>causal dependencies are preserved,</li>
  <li>the IDE is not misled about impossible source-level behavior,</li>
  <li>event order remains internally consistent for the instance.</li>
</ul>

<h3>18.3 Timestamps</h3>

<p>
Implementations MAY attach wall-clock or monotonic timestamps to observable events.
Such timestamps are informative only unless a stricter observability profile defines stronger timing requirements.
</p>

<h3>18.4 Delivery model</h3>

<p>
This document does not require push delivery or pull delivery.
Implementations MAY use:
</p>

<ul>
  <li>event callbacks,</li>
  <li>queues,</li>
  <li>polling APIs,</li>
  <li>trace buffers,</li>
  <li>structured logs,</li>
  <li>or any equivalent delivery model.</li>
</ul>

<h3>18.5 Event loss and weaker observability profiles</h3>

<p>
An observability profile intended for interactive debugging SHOULD avoid dropping canonical observability events.
A lower-overhead telemetry or monitoring observability profile MAY summarize or sample events, but only if it is explicitly identified as weaker than the full interactive observability profile.
</p>

<hr/>

<h2 id="ide-requirements">19. IDE Requirements</h2>

<p>
An IDE that claims support for FROG execution observability SHOULD be able to project at least the following:
</p>

<ul>
  <li>instance lifecycle state,</li>
  <li>node start and completion overlays,</li>
  <li>edge-level value-availability highlighting,</li>
  <li>structure entry and selected-region visualization,</li>
  <li>loop iteration progression,</li>
  <li>fault localization to the most relevant source object when possible.</li>
</ul>

<p>
If the active observability profile exposes readiness, the IDE SHOULD also be able to project readiness-sensitive overlays or equivalent readiness-aware diagnostic views.
</p>

<p>
An IDE MAY present this information through:
</p>

<ul>
  <li>diagram overlays,</li>
  <li>execution traces,</li>
  <li>logs,</li>
  <li>status panes,</li>
  <li>probe integrations,</li>
  <li>watch integrations,</li>
  <li>debugging controls defined elsewhere.</li>
</ul>

<p>
The visual design is not standardized here.
Only the IDE-facing observable meaning is standardized here.
</p>

<hr/>

<h2 id="illustrative-event-shapes">20. Illustrative Event Shapes</h2>

<p>
The following examples are illustrative only.
They show one possible structured representation of the conceptual observability model.
They are not a required transport format.
</p>

<h3>20.1 Node start</h3>

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

<h3>20.2 Edge value available inside a loop iteration</h3>

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

<h3>20.3 Case region selected</h3>

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

<h3>20.4 Local-memory update for <code>frog.core.delay</code></h3>

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

<h2 id="out-of-scope-for-v01">21. Out of Scope for v0.1</h2>

<p>
The following are intentionally out of scope for this document:
</p>

<ul>
  <li>execution-model ownership,</li>
  <li>safe-observation and safe-debug-stop semantic ownership,</li>
  <li>breakpoint semantics,</li>
  <li>single-step semantics,</li>
  <li>step into / over / out behavior,</li>
  <li>probe window behavior,</li>
  <li>watch expressions,</li>
  <li>timeline scrubbing,</li>
  <li>reverse execution,</li>
  <li>deterministic replay,</li>
  <li>distributed multi-runtime observability,</li>
  <li>profiling counters and performance metrics beyond basic timestamps,</li>
  <li>value serialization formats for deep inspection,</li>
  <li>transport API standardization.</li>
</ul>

<p>
Those topics MAY be defined later in separate IDE-facing or runtime-facing specifications.
</p>

<hr/>

<h2 id="summary">22. Summary</h2>

<p>
FROG execution observability defines the minimal source-aligned execution view that a FROG IDE may consume from a live execution instance.
It does not redefine execution semantics.
Instead, it standardizes:
</p>

<ul>
  <li>how language-defined execution objects are projected to the IDE,</li>
  <li>which high-level states the IDE may project,</li>
  <li>which canonical observable events may be exposed,</li>
  <li>how runtime activity maps back to source identity and execution context,</li>
  <li>what consistency guarantees the IDE may rely on when consuming language-level safe boundaries.</li>
</ul>

<p>
This observability layer is the foundation for debugging, probes, watches, traces, and richer execution instrumentation without confusing IDE-facing observation with normative language or primitive behavior.
</p>

<hr/>

<h2 id="license">23. License</h2>

<p>
This specification is part of the FROG repository and is governed by the repository license and contribution rules.
</p>
