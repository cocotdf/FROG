<h1 align="center">🐸 FROG IDE Watch Specification</h1>

<p align="center">
Definition of persistent watch entries and watch views for live execution inspection in a FROG IDE<br/>
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
  <li><a href="#what-a-watch-is">6. What a Watch Is</a></li>
  <li><a href="#watches-vs-probes">7. Watches vs Probes</a></li>
  <li><a href="#watch-list-model">8. Watch List Model</a></li>
  <li><a href="#watch-target-model">9. Watch Target Model</a></li>
  <li><a href="#execution-scope-and-context">10. Execution Scope and Context</a></li>
  <li><a href="#value-and-state-model">11. Value and State Model</a></li>
  <li><a href="#live-paused-and-retained-behavior">12. Live, Paused, and Retained Behavior</a></li>
  <li><a href="#canonical-watch-kinds">13. Canonical Watch Kinds</a></li>
  <li><a href="#edge-watches">14. Edge Watches</a></li>
  <li><a href="#port-watches">15. Port Watches</a></li>
  <li><a href="#local-memory-watches">16. Local-Memory Watches</a></li>
  <li><a href="#ui-related-watches">17. UI-Related Watches</a></li>
  <li><a href="#watch-lifecycle-and-management">18. Watch Lifecycle and Management</a></li>
  <li><a href="#watch-presentation-model">19. Watch Presentation Model</a></li>
  <li><a href="#validation-and-safety-rules">20. Validation and Safety Rules</a></li>
  <li><a href="#illustrative-examples">21. Illustrative Examples</a></li>
  <li><a href="#out-of-scope-for-v01">22. Out of Scope for v0.1</a></li>
  <li><a href="#summary">23. Summary</a></li>
  <li><a href="#license">24. License</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the watch model of a FROG IDE.
A watch is a persistent IDE-side inspection entry that tracks the most relevant observable value or state associated with a selected source-visible target during or after a live execution.
</p>

<p>
A watch is not a source-language construct.
It belongs to the IDE inspection and debugging layer.
A watch consumes source-aligned execution observability and presents it in a centralized, persistent, and user-manageable form.
</p>

<p>
Typical watch workflows include:
</p>

<ul>
  <li>tracking selected values across stepping and breakpoints,</li>
  <li>keeping important observations visible even when the user pans away from the source object,</li>
  <li>monitoring multiple graph locations from one centralized inspection view,</li>
  <li>retaining recent values after a pause or completed execution when the active profile allows it.</li>
</ul>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Persistence</strong> — allow selected observations to remain visible across navigation and debugging actions.</li>
  <li><strong>Centralization</strong> — provide a list- or panel-based inspection model independent from inline diagram overlays.</li>
  <li><strong>Source alignment</strong> — keep watch entries attached to source-visible targets rather than runtime-private implementation objects.</li>
  <li><strong>Debugging support</strong> — make watch entries usable together with pause, resume, stepping, and breakpoints.</li>
  <li><strong>Non-intrusiveness</strong> — ensure that watches do not alter graph execution semantics.</li>
  <li><strong>Clear layering</strong> — keep watch behavior distinct from probe behavior and from execution semantics themselves.</li>
</ul>

<hr/>

<h2 id="scope-for-v01">3. Scope for v0.1</h2>

<p>
For FROG v0.1, this document standardizes:
</p>

<ul>
  <li>what a watch is,</li>
  <li>the distinction between watches and probes,</li>
  <li>the canonical watch target kinds,</li>
  <li>the meaning of watched last-known values or state snapshots,</li>
  <li>the basic lifecycle of watch entries,</li>
  <li>the concept of a centralized watch list or equivalent watch view.</li>
</ul>

<p>
FROG v0.1 does <strong>not</strong> standardize:
</p>

<ul>
  <li>arbitrary textual watch expressions,</li>
  <li>computed watches over user-defined expressions,</li>
  <li>reverse-time watch inspection,</li>
  <li>mandatory history graphs for every watch,</li>
  <li>distributed multi-runtime watch aggregation,</li>
  <li>a mandatory dedicated watch-window UI layout.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">4. Relation with Other Specifications</h2>

<p>
This document complements the following specifications:
</p>

<ul>
  <li><code>IDE/Readme.md</code> — defines the role of execution observability, debugging, probes, and watches in the FROG IDE architecture.</li>
  <li><code>IDE/Execution observability.md</code> — defines the source-aligned observable execution events from which watch values are derived.</li>
  <li><code>IDE/Debugging.md</code> — defines pause, resume, stepping, and breakpoint behavior used together with watches.</li>
  <li><code>IDE/Probes.md</code> — defines local source-attached probes and the distinction between probes and watches.</li>
  <li><code>Expression/Diagram.md</code> — defines source-visible edges, ports, nodes, and annotations.</li>
  <li><code>Expression/State and cycles.md</code> — defines the source-facing representation of local-memory constructs and cycle-facing source constraints.</li>
  <li><code>Language/State and cycles.md</code> — defines the normative execution semantics of local memory and valid feedback behavior.</li>
  <li><code>Expression/Widget interaction.md</code> — defines explicit UI sequencing through <code>ui_in</code> and <code>ui_out</code>.</li>
  <li><code>Libraries/Core.md</code> — defines the standardized primitive identity and primitive-local behavior of <code>frog.core.delay</code>.</li>
  <li><code>Libraries/UI.md</code> — defines standardized executable UI interaction primitives.</li>
</ul>

<p>
This document does not redefine execution semantics, primitive-local behavior, breakpoint semantics, or probe semantics.
It defines how persistent watch entries consume and present source-aligned observations.
</p>

<p>
Accordingly:
</p>

<ul>
  <li><code>Expression/</code> remains authoritative for source-visible targets and source identity,</li>
  <li><code>Language/</code> remains authoritative for normative execution semantics,</li>
  <li><code>Libraries/</code> remains authoritative for primitive identity, ports, required metadata, and primitive-local behavior,</li>
  <li><code>IDE/Debugging.md</code> remains authoritative for pause, resume, breakpoint, and stepping controls,</li>
  <li><code>IDE/Probes.md</code> remains authoritative for local source-attached probe behavior,</li>
  <li><code>IDE/Watch.md</code> remains authoritative only for persistent centralized watch behavior and meaning.</li>
</ul>

<hr/>

<h2 id="design-principles">5. Design Principles</h2>

<h3>5.1 Source-visible targets only</h3>

<p>
A watch MUST track a source-visible target.
It MUST NOT require the user to reason about runtime-private buffers, queues, or scheduler internals.
</p>

<h3>5.2 Watches are persistent, not merely local</h3>

<p>
A watch is intended to remain visible and manageable independently from the immediate viewport around the target source object.
This is what distinguishes it from purely local inline inspection mechanisms.
</p>

<h3>5.3 Watches are non-intrusive</h3>

<p>
Creating, updating, or removing a watch MUST NOT change the semantics of the program being executed.
Watches belong to the IDE inspection layer only.
</p>

<h3>5.4 Watches show causally committed observations</h3>

<p>
A watch MUST NOT present speculative or half-committed source-level observations as stable values.
Watched values and state snapshots MUST correspond to causally committed source-level execution state.
</p>

<h3>5.5 Minimal but extensible</h3>

<p>
FROG v0.1 defines a minimal watch model.
Stricter profiles MAY add richer filtering, grouping, formatting, value history, or custom watch renderers, provided that the core semantic meaning remains preserved.
</p>

<hr/>

<h2 id="what-a-watch-is">6. What a Watch Is</h2>

<p>
A watch is an IDE-managed persistent inspection entry associated with a selected target.
Conceptually, a watch contains:
</p>

<ul>
  <li>a watch identifier,</li>
  <li>a watch target,</li>
  <li>a current watch state,</li>
  <li>a last-known observed value or state snapshot when available,</li>
  <li>optional retained information from earlier execution activity when supported by the active profile.</li>
</ul>

<p>
A watch does not exist inside the canonical FROG Expression.
It is an IDE-side construct that may be created, removed, or managed without altering the source program.
</p>

<hr/>

<h2 id="watches-vs-probes">7. Watches vs Probes</h2>

<p>
Watches and probes are related but distinct.
Both consume the same source-aligned observability model, but they serve different roles.
</p>

<h3>7.1 Probe</h3>

<p>
A probe is a direct inspection object attached to a specific source-visible target and commonly used as a local or inline inspection aid.
Probe workflows are target-centric and often diagram-centric.
</p>

<h3>7.2 Watch</h3>

<p>
A watch is a persistent inspection entry maintained in a centralized watch view such as a watch list, watch panel, or equivalent IDE-managed collection.
Watch workflows are persistence-centric and monitoring-centric.
</p>

<h3>7.3 Relationship</h3>

<p>
An IDE MAY allow:
</p>

<ul>
  <li>creating a watch directly from a source target,</li>
  <li>creating a watch from an existing probe,</li>
  <li>creating a probe from an existing watch target.</li>
</ul>

<p>
However, a watch is not merely a probe with a different window.
Its defining property is persistent centralized surveillance of selected observations across debugging activity.
</p>

<hr/>

<h2 id="watch-list-model">8. Watch List Model</h2>

<p>
For v0.1, the canonical logical model of watches is a <strong>watch list</strong>.
A watch list is an IDE-managed collection of persistent watch entries associated with one editing or debugging context.
</p>

<p>
A watch list MAY be presented as:
</p>

<ul>
  <li>a dedicated watch window,</li>
  <li>a dockable watch panel,</li>
  <li>a side inspector pane,</li>
  <li>another equivalent IDE presentation.</li>
</ul>

<p>
The exact UI layout is not standardized here.
The standardized semantic model is that watch entries belong to an ordered and user-manageable collection.
</p>

<h3>8.1 Minimal watch-list capabilities</h3>

<p>
A debugging-capable IDE SHOULD support at least:
</p>

<ul>
  <li>adding a watch,</li>
  <li>removing a watch,</li>
  <li>listing active watches,</li>
  <li>mapping a watch entry back to its source target,</li>
  <li>showing last-known values or state snapshots when available.</li>
</ul>

<hr/>

<h2 id="watch-target-model">9. Watch Target Model</h2>

<p>
For v0.1, a watch target MUST be one of the following source-visible targets:
</p>

<ul>
  <li>a source edge,</li>
  <li>a source node port,</li>
  <li>a local-memory slot owned by a local-memory node instance,</li>
  <li>a stricter-profile UI-related target that remains source-visible and semantically well-defined.</li>
</ul>

<p>
The target model of watches intentionally overlaps with the target model of probes.
This overlap is deliberate, because both mechanisms observe the same source-level execution space.
</p>

<p>
A watch target MUST be specific enough that the IDE can determine:
</p>

<ul>
  <li>which source object is being watched,</li>
  <li>which observable events update the watch entry,</li>
  <li>which execution context applies when repeated activity occurs.</li>
</ul>

<hr/>

<h2 id="execution-scope-and-context">10. Execution Scope and Context</h2>

<p>
Because the same source target may be observed multiple times under nested scopes or repeated iterations, watch values MUST remain interpretable in execution context.
</p>

<p>
Relevant context MAY include:
</p>

<ul>
  <li>sub-FROG call stack,</li>
  <li>structure nesting,</li>
  <li>selected region,</li>
  <li>loop iteration index,</li>
  <li>activation identifier.</li>
</ul>

<p>
A watch entry is normally attached to a stable source target, not to one permanently fixed dynamic iteration.
Therefore, repeated observations of the same watched target MAY update one watch entry over time, while the IDE MAY also display contextual metadata about the most recent observation.
</p>

<hr/>

<h2 id="value-and-state-model">11. Value and State Model</h2>

<h3>11.1 Last-known committed observation</h3>

<p>
For v0.1, the primary semantic value model of a watch is the <strong>last-known committed observation</strong> associated with the watched target in the relevant execution context.
</p>

<p>
This may be:
</p>

<ul>
  <li>a value observed on an edge,</li>
  <li>a value observed at a node port,</li>
  <li>a state snapshot observed for local memory,</li>
  <li>another source-aligned observation defined by a stricter profile.</li>
</ul>

<h3>11.2 No fabricated values</h3>

<p>
A watch MUST NOT fabricate values that were not actually observed through the source-aligned observability model.
If no compatible observation exists yet, the watch entry MUST remain explicitly unavailable rather than inventing a placeholder as if it were a real value.
</p>

<h3>11.3 Full values and previews</h3>

<p>
A watch MAY display:
</p>

<ul>
  <li>a full materialized value,</li>
  <li>a summarized preview,</li>
  <li>a type-aware structured rendering,</li>
  <li>an availability marker with limited value detail.</li>
</ul>

<p>
The semantic meaning remains the same in all cases: the display corresponds to the last-known committed source-level observation for the watched target.
</p>

<hr/>

<h2 id="live-paused-and-retained-behavior">12. Live, Paused, and Retained Behavior</h2>

<h3>12.1 Live behavior</h3>

<p>
During running execution, a watch MAY update whenever a relevant observation becomes available for its target.
The refresh strategy and update frequency are implementation-defined.
</p>

<h3>12.2 Paused behavior</h3>

<p>
When execution is paused under debugging control, a watch MUST reflect the causally consistent paused view.
A watch MUST NOT display a value or state snapshot that contradicts the paused snapshot visible to the IDE.
</p>

<h3>12.3 Retained behavior</h3>

<p>
A stricter profile MAY allow a watch to retain its last-known observation after pause completion, normal completion, or abort.
If retained behavior is supported, the IDE MUST distinguish clearly between:
</p>

<ul>
  <li>live-updating watch entries,</li>
  <li>paused-snapshot watch entries,</li>
  <li>retained watch entries from prior live execution.</li>
</ul>

<h3>12.4 No false history</h3>

<p>
If a watch retains only one last-known observation, the IDE MUST NOT imply that a full historical trace exists.
A history exists only when the active profile explicitly supports one.
</p>

<hr/>

<h2 id="canonical-watch-kinds">13. Canonical Watch Kinds</h2>

<p>
The canonical watch kinds for FROG v0.1 are:
</p>

<ul>
  <li><code>edge_watch</code> — persistent watch entry attached to one source edge,</li>
  <li><code>port_watch</code> — persistent watch entry attached to one source node port,</li>
  <li><code>local_memory_watch</code> — persistent watch entry attached to one local-memory slot owned by a node instance.</li>
</ul>

<p>
Among these, <code>edge_watch</code> is the primary and most natural watch form for v0.1, because ordinary FROG dataflow is most naturally observed at the edge level.
</p>

<hr/>

<h2 id="edge-watches">14. Edge Watches</h2>

<h3>14.1 Meaning</h3>

<p>
An <code>edge_watch</code> tracks the last-known committed value that became available on a specific source edge.
It is updated from source-aligned edge observations.
</p>

<h3>14.2 Update rule</h3>

<p>
An edge watch SHOULD update when the watched edge receives a relevant <code>edge_value_available</code> observation.
</p>

<h3>14.3 Fan-out</h3>

<p>
If one source output fans out to multiple edges, each edge MAY have its own watch entry.
This remains correct because source-level watch semantics are edge-based even if runtime implementation details are optimized differently.
</p>

<h3>14.4 Iterative contexts</h3>

<p>
If the same watched edge is activated repeatedly across loop iterations or nested scopes, the watch entry MAY continue updating with the most recent observation while displaying contextual metadata about that observation.
</p>

<hr/>

<h2 id="port-watches">15. Port Watches</h2>

<h3>15.1 Role</h3>

<p>
A <code>port_watch</code> tracks observations at a specific node input port or output port.
This watch form is useful when the IDE wants to center surveillance on node boundaries rather than on edges.
</p>

<h3>15.2 Input and output ports</h3>

<p>
A port watch MAY target:
</p>

<ul>
  <li>an input port,</li>
  <li>an output port.</li>
</ul>

<p>
An IDE SHOULD prefer edge watches for ordinary graph valueflow whenever an explicit edge identity already exists, but port watches remain valid in v0.1.
</p>

<h3>15.3 Semantics</h3>

<p>
A port watch attached to an output port SHOULD be semantically equivalent to watching the source-visible outgoing value from that port.
A port watch attached to an input port SHOULD reflect the committed value received at that input.
</p>

<hr/>

<h2 id="local-memory-watches">16. Local-Memory Watches</h2>

<h3>16.1 Purpose</h3>

<p>
A <code>local_memory_watch</code> tracks the source-level memory state associated with a local-memory primitive instance.
Its purpose is to inspect persistent state rather than only ordinary graph valueflow.
</p>

<h3>16.2 Canonical v0.1 case</h3>

<p>
For <code>frog.core.delay</code>, a local-memory watch SHOULD support at least the ability to show:
</p>

<ul>
  <li>the most recent observed state read when available,</li>
  <li>the most recent observed state update when available,</li>
  <li>the current committed stored value in a paused snapshot when the active profile exposes it.</li>
</ul>

<h3>16.3 Local scope</h3>

<p>
A local-memory watch MUST respect node-instance-local scope.
It MUST NOT imply shared state across unrelated node instances or across unrelated live FROG instances.
</p>

<h3>16.4 Meaning</h3>

<p>
A local-memory watch observes source-aligned local-memory activity associated with the node instance.
It does not redefine the primitive-local behavior of <code>frog.core.delay</code> or the language-level semantics of local memory.
</p>

<hr/>

<h2 id="ui-related-watches">17. UI-Related Watches</h2>

<h3>17.1 Ordinary widget-related valueflow</h3>

<p>
Ordinary widget-related valueflow SHOULD be watched through the same canonical mechanisms as any other dataflow:
</p>

<ul>
  <li>edge watches on edges connected to <code>widget_value</code>,</li>
  <li>port watches on relevant widget-related ports when supported.</li>
</ul>

<h3>17.2 Object-style widget interaction</h3>

<p>
Object-style widget interaction through <code>widget_reference</code>, <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code> MAY be watched through ordinary watched valueflow or through stricter-profile UI-oriented renderers.
</p>

<h3>17.3 UI sequencing</h3>

<p>
The <code>ui_in</code> / <code>ui_out</code> sequencing edges are not ordinary data-value edges.
A stricter profile MAY allow watching such sequencing activity, but it MUST be interpreted as effect-order observation rather than ordinary value observation.
</p>

<p>
When such watches are supported, they MUST remain aligned both with the source-facing widget interaction model and with the standardized <code>frog.ui.*</code> primitive definitions.
</p>

<hr/>

<h2 id="watch-lifecycle-and-management">18. Watch Lifecycle and Management</h2>

<h3>18.1 Creation</h3>

<p>
A watch is created when the IDE attaches a new watch entry to a valid watch target.
Creation MUST fail if the requested target is not valid in the active profile.
</p>

<h3>18.2 States</h3>

<p>
A watch entry MAY conceptually be in one of the following states:
</p>

<ul>
  <li><code>created</code> — watch exists but has not yet received a compatible observation,</li>
  <li><code>live</code> — watch is receiving live updates from an active execution,</li>
  <li><code>paused</code> — watch reflects a paused consistent snapshot,</li>
  <li><code>retained</code> — watch shows a retained last-known observation after live execution,</li>
  <li><code>unavailable</code> — no compatible value or state snapshot is currently available,</li>
  <li><code>closed</code> — watch has been removed.</li>
</ul>

<h3>18.3 Management operations</h3>

<p>
A debugging-capable IDE SHOULD support at least:
</p>

<ul>
  <li>add watch,</li>
  <li>remove watch,</li>
  <li>clear retained value when supported,</li>
  <li>show source target from watch entry,</li>
  <li>show watch entry from source target,</li>
  <li>list active watches.</li>
</ul>

<h3>18.4 Optional management behavior</h3>

<p>
A stricter profile MAY additionally support:
</p>

<ul>
  <li>sorting watches,</li>
  <li>grouping watches by scope or target kind,</li>
  <li>pinning selected watches,</li>
  <li>enabling or disabling live updates for selected watches,</li>
  <li>duplicating a watch as a probe or vice versa.</li>
</ul>

<hr/>

<h2 id="watch-presentation-model">19. Watch Presentation Model</h2>

<p>
This document does not standardize one mandatory watch-window layout.
It standardizes the semantic meaning of watch entries.
</p>

<p>
A watch presentation SHOULD be able to show at least:
</p>

<ul>
  <li>watch target identity,</li>
  <li>watch kind,</li>
  <li>last-known value or state snapshot when available,</li>
  <li>execution-state status such as live, paused, retained, or unavailable,</li>
  <li>basic context information when relevant.</li>
</ul>

<p>
An IDE MAY present this information through:
</p>

<ul>
  <li>a dedicated watch window,</li>
  <li>a docked watch pane,</li>
  <li>a structured inspection sidebar,</li>
  <li>another equivalent centralized view.</li>
</ul>

<p>
A watch presentation MAY also allow expanding structured values into child fields or child elements when the active profile and available type information permit it.
This expansion behavior is optional in v0.1.
</p>

<hr/>

<h2 id="validation-and-safety-rules">20. Validation and Safety Rules</h2>

<ul>
  <li>A watch MUST target a valid source-visible object supported by the active profile.</li>
  <li>A watch MUST NOT alter program execution semantics.</li>
  <li>A watch shown during pause MUST remain consistent with the paused execution snapshot.</li>
  <li>A retained watch value MUST be clearly distinguishable from a live-updating value.</li>
  <li>A watch MUST NOT misrepresent a sequencing observation as an ordinary data value.</li>
  <li>A local-memory watch MUST respect node-instance-local scope.</li>
  <li>A watch MUST NOT imply arbitrary user-defined watch expressions unless a later stricter specification defines them.</li>
  <li>A watch MUST NOT be presented as a probe unless the IDE explicitly re-exposes the same target through the probe model defined elsewhere.</li>
</ul>

<hr/>

<h2 id="illustrative-examples">21. Illustrative Examples</h2>

<h3>21.1 Edge watch</h3>

<pre><code>{
  "watch_id": "w1",
  "kind": "edge_watch",
  "target": {
    "kind": "edge",
    "id": "e_sum"
  },
  "state": "live",
  "last_value": {
    "preview": "17.5"
  }
}</code></pre>

<h3>21.2 Port watch</h3>

<pre><code>{
  "watch_id": "w2",
  "kind": "port_watch",
  "target": {
    "kind": "port",
    "node_id": "add_1",
    "port": "result",
    "direction": "output"
  },
  "state": "paused",
  "last_value": {
    "preview": "17.5"
  }
}</code></pre>

<h3>21.3 Local-memory watch</h3>

<pre><code>{
  "watch_id": "w3",
  "kind": "local_memory_watch",
  "target": {
    "kind": "local_memory",
    "node_id": "delay_1"
  },
  "state": "paused",
  "last_value": {
    "preview": "5.0"
  },
  "details": {
    "last_event": "state_updated"
  }
}</code></pre>

<h3>21.4 Retained watch</h3>

<pre><code>{
  "watch_id": "w4",
  "kind": "edge_watch",
  "target": {
    "kind": "edge",
    "id": "e_output"
  },
  "state": "retained",
  "last_value": {
    "preview": "42"
  }
}</code></pre>

<hr/>

<h2 id="out-of-scope-for-v01">22. Out of Scope for v0.1</h2>

<ul>
  <li>arbitrary textual watch expressions,</li>
  <li>computed watches over user-defined graph expressions,</li>
  <li>mandatory time history for every watch entry,</li>
  <li>reverse-time watch browsing,</li>
  <li>mandatory remote watch streaming,</li>
  <li>standardized distributed aggregation of watch lists,</li>
  <li>watch-triggered execution modification,</li>
  <li>a mandatory dedicated watch-window UI toolkit or layout.</li>
</ul>

<hr/>

<h2 id="summary">23. Summary</h2>

<p>
FROG watches are persistent IDE-side inspection entries used to monitor selected source-visible targets across debugging activity.
They are distinct from probes, even though both mechanisms consume the same source-aligned execution observability.
</p>

<p>
This specification establishes that:
</p>

<ul>
  <li>watches belong to the IDE inspection layer,</li>
  <li>watches track source-visible targets such as edges, ports, and local-memory state,</li>
  <li><code>edge_watch</code> is the primary watch form in v0.1,</li>
  <li>watched values represent last-known committed observations,</li>
  <li>paused and retained watch views must be clearly distinguishable,</li>
  <li>watches provide centralized persistent surveillance rather than local inline inspection.</li>
</ul>

<hr/>

<h2 id="license">24. License</h2>

<p>
This specification is part of the FROG repository and is governed by the repository license and contribution rules.
</p>
