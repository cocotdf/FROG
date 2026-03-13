<h1 align="center">🐸 FROG IDE Execution Observability Specification</h1>

<p align="center">
Definition of the execution observability model exposed to a FROG IDE<br/>
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
  <li><a href="#live-execution-instance">7. Live Execution Instance</a></li>
  <li><a href="#source-identity-and-execution-context">8. Source Identity and Execution Context</a></li>
  <li><a href="#observable-states">9. Observable States</a></li>
  <li><a href="#observable-event-model">10. Observable Event Model</a></li>
  <li><a href="#node-activation-observation">11. Node Activation Observation</a></li>
  <li><a href="#edge-and-value-observation">12. Edge and Value Observation</a></li>
  <li><a href="#structure-and-region-observation">13. Structure and Region Observation</a></li>
  <li><a href="#local-memory-observation">14. Local Memory Observation</a></li>
  <li><a href="#sub-frog-observation">15. Sub-FROG Observation</a></li>
  <li><a href="#ui-sequencing-observation">16. UI Sequencing Observation</a></li>
  <li><a href="#pause-consistency-and-safe-observation-points">17. Pause Consistency and Safe Observation Points</a></li>
  <li><a href="#ordering-time-and-event-delivery">18. Ordering, Time, and Event Delivery</a></li>
  <li><a href="#ide-requirements">19. IDE Requirements</a></li>
  <li><a href="#illustrative-event-shapes">20. Illustrative Event Shapes</a></li>
  <li><a href="#out-of-scope-for-v01">21. Out of Scope for v0.1</a></li>
  <li><a href="#summary">22. Summary</a></li>
  <li><a href="#license">23. License</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the <strong>execution observability model</strong> exposed to a FROG IDE.
It specifies the minimal concepts, states, and events that allow an IDE to inspect a running FROG program in a source-aligned way.
</p>

<p>
The purpose of execution observability is not to redefine how the program executes.
Execution semantics remain defined by the validated FROG graph and the related language specifications.
This document defines how execution becomes <strong>observable</strong> to tools such as:
</p>

<ul>
  <li>diagram execution highlighting,</li>
  <li>live node-state overlays,</li>
  <li>future stepping controls,</li>
  <li>future breakpoints,</li>
  <li>future probes and watch windows,</li>
  <li>execution logs and diagnostics.</li>
</ul>

<p>
Execution observability is therefore an IDE-facing contract over a live execution, not a replacement for the execution model itself.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<p>This document has the following goals:</p>

<ul>
  <li>define what a FROG IDE is allowed to observe from a live execution,</li>
  <li>preserve source-level identity so that runtime activity can be projected back onto the diagram and front panel,</li>
  <li>support a LabVIEW-like interactive debugging experience later without requiring that debugging semantics be defined here,</li>
  <li>remain compatible with multiple runtimes, schedulers, and execution strategies,</li>
  <li>separate <strong>execution behavior</strong> from <strong>execution observability</strong>,</li>
  <li>provide a stable foundation for later specifications such as debugging, probes, stepping, and instrumentation.</li>
</ul>

<hr/>

<h2 id="scope-for-v01">3. Scope for v0.1</h2>

<p>
For FROG v0.1, this document standardizes the minimal observable concepts needed by an IDE:
</p>

<ul>
  <li>live execution instances,</li>
  <li>source identity mapping,</li>
  <li>execution context,</li>
  <li>observable states,</li>
  <li>observable execution events,</li>
  <li>node activation visibility,</li>
  <li>edge-level value transfer visibility,</li>
  <li>structure and region activity visibility,</li>
  <li>local-memory visibility,</li>
  <li>pause consistency requirements.</li>
</ul>

<p>
FROG v0.1 does <strong>not</strong> standardize:
</p>

<ul>
  <li>a transport protocol between runtime and IDE,</li>
  <li>a binary event stream format,</li>
  <li>a mandatory timestamp format,</li>
  <li>a breakpoint model,</li>
  <li>a stepping model,</li>
  <li>a probe UI,</li>
  <li>a watch-window UI,</li>
  <li>a single required scheduler implementation,</li>
  <li>a total order over independent parallel activity beyond causal consistency.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">4. Relation with Other Specifications</h2>

<p>
This document depends on the following specifications:
</p>

<ul>
  <li><code>IDE/Readme.md</code> for the architectural separation between FROG Expression, FROG Program Model, and FROG Execution IR,</li>
  <li><code>Expression/Diagram.md</code> for the validated executable graph and its node and edge model,</li>
  <li><code>Expression/Control structures.md</code> for the canonical source-facing representation of structure families, structure boundaries, terminals, and regions,</li>
  <li><code>Language/Control structures.md</code> for the normative execution semantics of structure families,</li>
  <li><code>Expression/State and cycles.md</code> for the canonical source-facing representation of local-memory constructs and cycle-facing source constraints,</li>
  <li><code>Language/State and cycles.md</code> for the normative execution semantics of local memory and valid feedback,</li>
  <li><code>Expression/Widget interaction.md</code> for explicit UI-effect sequencing through <code>ui_in</code> and <code>ui_out</code>.</li>
</ul>

<p>
This document MUST NOT contradict those specifications.
If a conflict appears:
</p>

<ul>
  <li><code>Expression/</code> remains authoritative for canonical source identity and source-visible representation,</li>
  <li><code>Language/</code> remains authoritative for normative execution semantics,</li>
  <li><code>IDE/</code> remains authoritative only for the observability contract exposed to tools.</li>
</ul>

<p>
This document is intentionally placed in <code>IDE/</code> because it specifies what the IDE may observe and project, not the canonical source representation itself and not the execution semantics themselves.
</p>

<hr/>

<h2 id="design-principles">5. Design Principles</h2>

<h3>5.1 Source alignment</h3>

<p>
Observable execution MUST remain attributable to source-level objects known to the FROG Program Model.
A user should be able to understand runtime activity by looking at the source diagram and related front-panel elements.
</p>

<h3>5.2 Runtime independence</h3>

<p>
Different runtimes MAY use different internal schedulers, queues, threads, buffers, or optimization strategies.
Those internal choices MAY vary.
The observable meaning exposed to the IDE MUST remain equivalent.
</p>

<h3>5.3 Causal consistency</h3>

<p>
The IDE-facing event stream MUST represent a causally consistent view of execution.
The IDE MUST NOT be forced to interpret impossible or self-contradictory execution states.
</p>

<h3>5.4 Minimal but extensible</h3>

<p>
FROG v0.1 defines a minimal observability core.
Stricter profiles MAY expose additional fields, more detailed events, richer value snapshots, or stronger guarantees, provided that the v0.1 semantics remain preserved.
</p>

<h3>5.5 Observability is descriptive, not prescriptive</h3>

<p>
This document describes what may be observed.
It does not require runtimes to execute nodes in any particular internal implementation order beyond what is necessary to preserve the validated observable semantics.
</p>

<hr/>

<h2 id="what-this-document-defines">6. What This Document Defines</h2>

<p>
Execution observability defines the <strong>observable projection</strong> of a live FROG execution to an IDE.
At minimum, this projection includes:
</p>

<ul>
  <li>when a live execution instance begins and ends,</li>
  <li>when a node becomes ready, starts, completes, or faults,</li>
  <li>when a value becomes available on an edge,</li>
  <li>when a structure is entered, which region executes, and when iterations begin and end,</li>
  <li>when local memory is read and updated,</li>
  <li>when a live execution is paused, resumed, or aborted.</li>
</ul>

<p>
This projection is conceptual.
Implementations MAY expose it through callbacks, event queues, polling APIs, logs, traces, or any equivalent mechanism.
</p>

<hr/>

<h2 id="live-execution-instance">7. Live Execution Instance</h2>

<p>
A <strong>live execution instance</strong> is one running realization of a validated FROG program.
Every observable event belongs to exactly one live execution instance.
</p>

<p>
A live execution instance MUST have an identifier that is unique within the observing session.
This identifier is referred to in this document as <code>instance_id</code>.
</p>

<p>
A live execution instance conceptually owns:
</p>

<ul>
  <li>its own activation history,</li>
  <li>its own local-memory state for each local-memory primitive instance,</li>
  <li>its own sub-FROG invocation stack,</li>
  <li>its own observable event sequence.</li>
</ul>

<p>
Two separate runs of the same FROG are separate live execution instances.
Their observable states and histories MUST NOT be conflated.
</p>

<hr/>

<h2 id="source-identity-and-execution-context">8. Source Identity and Execution Context</h2>

<h3>8.1 Source identity</h3>

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

<h3>8.2 Execution context</h3>

<p>
Because the same source node may activate multiple times and under nested scopes, observable activity MUST also carry an <strong>execution context</strong>.
The execution context identifies the dynamic path under which an observation occurs.
</p>

<p>
The execution context MAY include:
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

<h3>8.3 Activation identity</h3>

<p>
Every node activation SHOULD have an <code>activation_id</code> unique within its live execution instance.
This identifier is especially important for loops, repeated executions, and detailed trace analysis.
</p>

<hr/>

<h2 id="observable-states">9. Observable States</h2>

<h3>9.1 Instance states</h3>

<p>
A live execution instance MUST be observable in one of the following high-level states:
</p>

<ul>
  <li><code>created</code> — the instance exists but execution has not yet started,</li>
  <li><code>running</code> — execution is actively progressing,</li>
  <li><code>paused</code> — execution is suspended at a safe observation point,</li>
  <li><code>completed</code> — execution finished normally,</li>
  <li><code>faulted</code> — execution terminated because of an execution fault,</li>
  <li><code>aborted</code> — execution was terminated externally without normal completion.</li>
</ul>

<h3>9.2 Node-observation states</h3>

<p>
For IDE projection purposes, a node activation MAY be observed through the following conceptual states:
</p>

<ul>
  <li><code>inactive</code> — the node is outside the currently executing dynamic path,</li>
  <li><code>waiting</code> — the node belongs to the active execution path but its required activation conditions are not yet satisfied,</li>
  <li><code>ready</code> — the node is eligible to begin execution,</li>
  <li><code>running</code> — the node is currently executing,</li>
  <li><code>completed</code> — the node activation completed normally,</li>
  <li><code>faulted</code> — the node activation failed,</li>
  <li><code>canceled</code> — the node activation will not occur because the containing instance or scope was aborted.</li>
</ul>

<p>
These are observability states, not a required internal runtime state machine.
A runtime MAY internally use a different representation provided that the IDE-visible meaning remains equivalent.
</p>

<h3>9.3 Region-observation states</h3>

<p>
A structure region MAY be observed as:
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
FROG v0.1 defines the following canonical event categories:
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
  <li><code>context</code> — execution context,</li>
  <li><code>timestamp</code> — optional runtime timestamp,</li>
  <li><code>details</code> — event-specific additional fields.</li>
</ul>

<p>
The exact concrete transport shape is not standardized by this document.
</p>

<hr/>

<h2 id="node-activation-observation">11. Node Activation Observation</h2>

<h3>11.1 General model</h3>

<p>
A source node MAY activate zero, one, or multiple times during a live execution instance, depending on:
</p>

<ul>
  <li>ordinary dataflow,</li>
  <li>structure selection,</li>
  <li>loop iteration,</li>
  <li>sub-FROG invocation,</li>
  <li>local-memory feedback behavior,</li>
  <li>runtime-specific execution progress.</li>
</ul>

<h3>11.2 Ready visibility</h3>

<p>
If a runtime supports interactive inspection, it SHOULD make node readiness observable.
The event <code>node_became_ready</code> indicates that a node activation is now eligible to start according to the validated execution semantics.
</p>

<p>
A runtime MAY internally transition from readiness to execution immediately.
Even in that case, an interactive observability profile SHOULD still preserve a logical ready step so that future stepping and highlighting mechanisms remain definable.
</p>

<h3>11.3 Start and completion</h3>

<p>
A normal node activation SHOULD be observable through:
</p>

<pre><code>node_became_ready
node_started
node_completed
</code></pre>

<p>
A faulting activation SHOULD be observable through:
</p>

<pre><code>node_became_ready
node_started
node_faulted
</code></pre>

<p>
A node MUST NOT be reported as completed before its observable outputs and state effects for that activation are causally committed.
</p>

<h3>11.4 Source kinds</h3>

<p>
This node activation model applies uniformly to standard node kinds where relevant, including:
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
The exact meaning of their ports remains defined by the corresponding source and language specifications.
This document defines only their observability behavior.
</p>

<hr/>

<h2 id="edge-and-value-observation">12. Edge and Value Observation</h2>

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
The event <code>edge_value_available</code> means that, within the current live execution context, a value is now available on that edge for ordinary source-level understanding.
It does not require the runtime to reveal internal buffer implementation details.
</p>

<h3>12.3 Payload visibility</h3>

<p>
This document does not require every runtime to expose a full value payload for every observed edge event.
A stricter profile MAY expose one of the following:
</p>

<ul>
  <li>a full value snapshot,</li>
  <li>a bounded value preview,</li>
  <li>a summarized textual or structural representation,</li>
  <li>an opaque handle from which a later tool can request the value,</li>
  <li>no payload, with only value availability indicated.</li>
</ul>

<p>
The chosen payload strategy MUST NOT alter the execution semantics.
It only affects what the IDE can display.
</p>

<h3>12.4 Fan-out</h3>

<p>
If one source output drives multiple edges, each edge MAY be observed separately at the source-aligned level, because probes, overlays, and diagnostics are naturally expressed on edges.
A runtime MAY internally optimize such fan-out, but the IDE-visible meaning SHOULD remain edge-based.
</p>

<hr/>

<h2 id="structure-and-region-observation">13. Structure and Region Observation</h2>

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
For a <code>case</code> structure, the canonical event sequence SHOULD include:
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
That fact MAY be represented either by the absence of iteration events or by a stricter profile-specific summary event.
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
The post-test continuation meaning of <code>while_loop</code> remains defined by the control-structure specification.
This document defines only how that activity becomes visible.
</p>

<h3>13.5 Region-local activity</h3>

<p>
Nodes inside a structure region are observed in the execution context of that region.
For example, a node inside a loop body is not merely “the same node again”; it is the same source node under a different dynamic iteration context.
</p>

<hr/>

<h2 id="local-memory-observation">14. Local Memory Observation</h2>

<h3>14.1 General rule</h3>

<p>
Local-memory primitives participate in ordinary node execution and additionally expose state-related observable meaning.
For IDE purposes, this state behavior MUST be observable in a source-aligned way.
</p>

<h3>14.2 Canonical events</h3>

<p>
The canonical local-memory events are:
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
For <code>frog.core.delay</code>, the execution specifications already define the intended observable meaning:
</p>

<pre><code>out(t) = state(t)
state(t + 1) = in(t)
</code></pre>

<p>
Therefore, the canonical observability sequence for one normal activation of <code>frog.core.delay</code> SHOULD be conceptually understood as:
</p>

<pre><code>node_became_ready
state_read
node_started
edge_value_available   // for out
state_updated
node_completed
</code></pre>

<p>
An implementation MAY merge or reorder internal operations provided that the exposed observable meaning remains equivalent to:
</p>

<ul>
  <li>the value seen on <code>out</code> is the stored state before the update of that activation,</li>
  <li>the value captured from <code>in</code> becomes the state for a later activation,</li>
  <li>the initial activation uses the deterministic initial state defined by source or a stricter equivalent profile.</li>
</ul>

<h3>14.4 Initial state visibility</h3>

<p>
A stricter profile MAY expose the initial state of a local-memory node before first activation.
Such visibility is optional in v0.1.
However, if shown, it MUST match the deterministic semantics already defined by source and language semantics.
</p>

<hr/>

<h2 id="sub-frog-observation">15. Sub-FROG Observation</h2>

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
This distinction is necessary for future stepping models such as “step into” and “step over”, but those controls are not standardized in this document.
</p>

<hr/>

<h2 id="ui-sequencing-observation">16. UI Sequencing Observation</h2>

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
  <li>a stricter profile MAY expose explicit UI-effect start and completion events,</li>
  <li>the absence of explicit UI-effect events in v0.1 does not invalidate UI sequencing semantics already defined by source.</li>
</ul>

<h3>16.3 No implicit UI semantics</h3>

<p>
This document MUST NOT be interpreted as introducing implicit UI event scheduling.
Only the existing explicit UI sequencing model and the ordinary node execution model apply.
</p>

<hr/>

<h2 id="pause-consistency-and-safe-observation-points">17. Pause Consistency and Safe Observation Points</h2>

<h3>17.1 Safe observation point</h3>

<p>
A <strong>safe observation point</strong> is a moment at which a live execution instance may be observed or paused without exposing a partially committed source-level state to the IDE.
</p>

<p>
At a safe observation point:
</p>

<ul>
  <li>every emitted observable event belongs to a consistent causal prefix of the execution,</li>
  <li>no already-emitted source-level event is contradicted by later pause interpretation,</li>
  <li>no IDE-visible local-memory state is half-updated,</li>
  <li>no already-highlighted node or region is left in an impossible intermediate state.</li>
</ul>

<h3>17.2 Pause semantics</h3>

<p>
If a live execution instance enters the <code>paused</code> state, it MUST do so only at a safe observation point.
The IDE MUST then observe a causally consistent snapshot of:
</p>

<ul>
  <li>instance state,</li>
  <li>currently running or last-completed observable activity,</li>
  <li>current local-memory values if they are exposed,</li>
  <li>already-available edge values if such visibility is supported by the active profile.</li>
</ul>

<h3>17.3 No partial node completion</h3>

<p>
A node MUST NOT appear both completed and not-yet-committed within the same paused snapshot.
Likewise, an edge value that is shown as available MUST correspond to a causally committed value in the paused view.
</p>

<hr/>

<h2 id="ordering-time-and-event-delivery">18. Ordering, Time, and Event Delivery</h2>

<h3>18.1 Sequence order</h3>

<p>
Within one live execution instance, observable events MUST admit a monotonically increasing sequence order.
This order MUST be causally consistent.
</p>

<h3>18.2 Parallel activity</h3>

<p>
Independent parallel activity need not imply one universal semantic order beyond causal consistency.
If two independent node activations are both valid and concurrent, a runtime MAY choose either event emission order, provided that:
</p>

<ul>
  <li>causal dependencies are preserved,</li>
  <li>the IDE is not misled about impossible source-level behavior,</li>
  <li>event order remains internally consistent for the instance.</li>
</ul>

<h3>18.3 Timestamps</h3>

<p>
Implementations MAY attach wall-clock or monotonic timestamps to observable events.
Such timestamps are informative only unless a stricter profile defines stronger timing requirements.
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

<h3>18.5 Event loss</h3>

<p>
A profile intended for interactive debugging SHOULD avoid dropping canonical observability events.
A lower-overhead telemetry profile MAY summarize or sample events, but only if it is explicitly identified as weaker than the full interactive observability profile.
</p>

<hr/>

<h2 id="ide-requirements">19. IDE Requirements</h2>

<p>
An IDE that claims support for FROG execution observability SHOULD be able to project at least the following:
</p>

<ul>
  <li>instance lifecycle state,</li>
  <li>node readiness, start, and completion overlays,</li>
  <li>edge-level value-availability highlighting,</li>
  <li>structure entry and selected-region visualization,</li>
  <li>loop iteration progression,</li>
  <li>fault localization to the most relevant source object when possible.</li>
</ul>

<p>
An IDE MAY present this information through:
</p>

<ul>
  <li>diagram overlays,</li>
  <li>execution traces,</li>
  <li>logs,</li>
  <li>status panes,</li>
  <li>future probe windows,</li>
  <li>future stepping controls.</li>
</ul>

<p>
The visual design is not standardized here.
Only the source-aligned meaning is standardized.
</p>

<hr/>

<h2 id="illustrative-event-shapes">20. Illustrative Event Shapes</h2>

<p>
The following examples are illustrative only.
They show one possible structured representation of the conceptual event model.
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
Those topics MAY be defined later in separate IDE or runtime-facing specifications.
</p>

<hr/>

<h2 id="summary">22. Summary</h2>

<p>
FROG execution observability defines the minimal source-aligned execution view that a FROG IDE may consume from a live execution instance.
It does not redefine execution semantics.
Instead, it standardizes:
</p>

<ul>
  <li>what execution objects are observable,</li>
  <li>which states they may expose,</li>
  <li>which canonical events may be emitted,</li>
  <li>how runtime activity maps back to source identity,</li>
  <li>what consistency guarantees an IDE may rely on when projecting execution.</li>
</ul>

<p>
This observability layer is the foundation for later specifications covering debugging, stepping, breakpoints, probes, and richer execution instrumentation.
</p>

<hr/>

<h2 id="license">23. License</h2>

<p>
This specification is part of the FROG repository and is governed by the repository license and contribution rules.
</p>
