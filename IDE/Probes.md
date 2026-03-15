<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="150" />
</p>

<h1 align="center">🐸 FROG IDE Probes Specification</h1>

<p align="center">
Definition of source-aligned probes for live execution inspection in a FROG IDE<br/>
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
  <li><a href="#what-a-probe-is">6. What a Probe Is</a></li>
  <li><a href="#probes-vs-watches">7. Probes vs Watches</a></li>
  <li><a href="#probe-attachment-model">8. Probe Attachment Model</a></li>
  <li><a href="#canonical-probe-kinds">9. Canonical Probe Kinds</a></li>
  <li><a href="#probe-lifecycle">10. Probe Lifecycle</a></li>
  <li><a href="#value-capture-semantics">11. Value Capture Semantics</a></li>
  <li><a href="#live-paused-and-retained-views">12. Live, Paused, and Retained Views</a></li>
  <li><a href="#edge-probes">13. Edge Probes</a></li>
  <li><a href="#node-port-probes">14. Node-Port Probes</a></li>
  <li><a href="#local-memory-probes">15. Local-Memory Probes</a></li>
  <li><a href="#ui-related-probes">16. UI-Related Probes</a></li>
  <li><a href="#probe-presentation-model">17. Probe Presentation Model</a></li>
  <li><a href="#probe-management">18. Probe Management</a></li>
  <li><a href="#custom-and-type-specific-probes">19. Custom and Type-Specific Probes</a></li>
  <li><a href="#validation-and-safety-rules">20. Validation and Safety Rules</a></li>
  <li><a href="#illustrative-examples">21. Illustrative Examples</a></li>
  <li><a href="#out-of-scope-for-v01">22. Out of Scope for v0.1</a></li>
  <li><a href="#summary">23. Summary</a></li>
  <li><a href="#license">24. License</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the probe model of a FROG IDE.
A probe is an IDE-side inspection object attached to a source-visible execution object so that a user can observe values or source-aligned execution state during or after a live execution.
</p>

<p>
In FROG, probes are part of the debugging and inspection layer.
They do not redefine execution semantics.
They consume source-aligned execution observability and present that information in a form suitable for interactive inspection.
</p>

<p>
The primary purpose of a probe is to make runtime behavior understandable at the level of the diagram and related source-visible execution objects.
For v0.1, the canonical probe model is centered on values flowing through edges, with additional probe forms for ports, local memory, and certain UI-related execution objects.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Inspectability</strong> — allow users to observe dataflow values and selected source-level execution state.</li>
  <li><strong>Source alignment</strong> — keep probes attached to source-visible objects rather than runtime-private artifacts.</li>
  <li><strong>Debugging support</strong> — make probes usable together with pause, resume, breakpoints, and stepping.</li>
  <li><strong>Deterministic meaning</strong> — ensure that probed values correspond to committed source-level execution state.</li>
  <li><strong>Clear layering</strong> — keep probes distinct from centralized watch entries and from execution semantics themselves.</li>
  <li><strong>Extensibility</strong> — allow richer type-specific or custom probes later without changing the base semantics.</li>
</ul>

<hr/>

<h2 id="scope-for-v01">3. Scope for v0.1</h2>

<p>
For FROG v0.1, this document standardizes:
</p>

<ul>
  <li>what a probe is,</li>
  <li>which source-level objects may be probed,</li>
  <li>the canonical probe kinds,</li>
  <li>the meaning of last-known committed observations,</li>
  <li>the distinction between live, paused, and retained views,</li>
  <li>minimal probe-management behavior.</li>
</ul>

<p>
FROG v0.1 does <strong>not</strong> standardize:
</p>

<ul>
  <li>a specific probe window user interface,</li>
  <li>conditional probe break semantics,</li>
  <li>watch expressions,</li>
  <li>time-series graph widgets for every type,</li>
  <li>distributed multi-runtime probe coordination,</li>
  <li>reverse-time value inspection,</li>
  <li>a mandatory value-serialization format for every runtime.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">4. Relation with Other Specifications</h2>

<p>
This document complements the following specifications:
</p>

<ul>
  <li><code>IDE/Readme.md</code> — defines the role of execution observability, debugging, probes, and watches within the IDE architecture.</li>
  <li><code>IDE/Execution observability.md</code> — defines the source-aligned observable execution projection from which probe values are derived.</li>
  <li><code>IDE/Debugging.md</code> — defines pause, resume, breakpoints, and stepping behavior used together with probes.</li>
  <li><code>IDE/Watch.md</code> — defines persistent centralized inspection and the distinction between watches and probes.</li>
  <li><code>Expression/Diagram.md</code> — defines nodes, ports, edges, and executable graph structure.</li>
  <li><code>Expression/State and cycles.md</code> — defines the source-facing representation of local-memory constructs and cycle-facing source constraints.</li>
  <li><code>Expression/Widget interaction.md</code> — defines explicit UI sequencing through <code>ui_in</code> and <code>ui_out</code>.</li>
  <li><code>Language/Execution model.md</code> — defines execution context, committed source-level state, and instance-relative execution meaning consumed by probes.</li>
  <li><code>Language/Execution control and observation boundaries.md</code> — defines safe observation points and pause-consistent snapshots that probes must respect.</li>
  <li><code>Language/State and cycles.md</code> — defines the normative execution semantics of local memory and valid feedback behavior.</li>
  <li><code>Libraries/Core.md</code> — defines the standardized primitive identity and primitive-local behavior of <code>frog.core.delay</code>.</li>
  <li><code>Libraries/UI.md</code> — defines standardized executable UI interaction primitives.</li>
</ul>

<p>
This document does not redefine execution semantics, execution-model ownership, primitive-local behavior, or debugging controls.
It defines how probes attach to source-visible execution objects and what probed observations mean.
</p>

<p>
Accordingly:
</p>

<ul>
  <li><code>Expression/</code> remains authoritative for source-visible targets and source identity,</li>
  <li><code>Language/</code> remains authoritative for normative execution semantics, execution context, committed source-level state, and safe observation boundaries,</li>
  <li><code>Libraries/</code> remain authoritative for primitive identity, ports, required metadata, and primitive-local behavior,</li>
  <li><code>IDE/Debugging.md</code> remains authoritative for pause, resume, breakpoint, and stepping controls,</li>
  <li><code>IDE/Watch.md</code> remains authoritative for persistent centralized watch behavior,</li>
  <li><code>IDE/Probes.md</code> remains authoritative only for source-attached probe behavior and meaning.</li>
</ul>

<hr/>

<h2 id="design-principles">5. Design Principles</h2>

<h3>5.1 Source-visible attachment</h3>

<p>
A probe MUST attach to a source-visible execution object such as an edge, a node port, a local-memory slot, or another explicitly standardized probe target.
A probe MUST NOT require the user to understand runtime-private buffers or scheduler internals.
</p>

<h3>5.2 Non-intrusive observation</h3>

<p>
A standard probe MUST NOT change program semantics.
Adding or removing a probe MUST NOT alter the meaning of the FROG graph.
</p>

<h3>5.3 Committed observations only</h3>

<p>
Probe-visible values MUST correspond to committed source-level execution state.
A probe MUST NOT present speculative or half-committed source values as stable observations.
</p>

<h3>5.4 Dataflow-first design</h3>

<p>
Because FROG is dataflow-based, the canonical first-class probe target in v0.1 is the <strong>edge</strong>.
This preserves the natural debugging model of observing values as they become available in the graph.
</p>

<h3>5.5 Local rather than centralized inspection</h3>

<p>
A probe is a source-attached local inspection object.
It is not the same thing as a centralized persistent watch entry.
The base probe model therefore emphasizes attachment to a local source target rather than aggregation into a global watch list.
</p>

<h3>5.6 Minimal but extensible</h3>

<p>
The v0.1 probe model is intentionally minimal.
Stricter profiles MAY add richer displays, deeper value views, specialized visualizations, or custom-probe registration mechanisms, provided that the base semantic meaning remains preserved.
</p>

<hr/>

<h2 id="what-a-probe-is">6. What a Probe Is</h2>

<p>
A probe is an IDE-managed inspection object associated with one source-level target.
It receives source-aligned observable execution information and presents a user-facing view of that information.
</p>

<p>
Conceptually, a probe has:
</p>

<ul>
  <li>a probe identifier,</li>
  <li>a target object,</li>
  <li>a display strategy,</li>
  <li>a current probe-entry state,</li>
  <li>a last-known observed value or state snapshot when available,</li>
  <li>optional execution-context metadata for the most recent relevant observation.</li>
</ul>

<p>
A probe is not itself part of the FROG Expression.
It is an IDE/runtime inspection construct layered over a live execution or a retained post-execution view.
It is also distinct from a watch entry, which belongs to a centralized persistent watch view.
</p>

<hr/>

<h2 id="probes-vs-watches">7. Probes vs Watches</h2>

<p>
Probes and watches consume the same source-aligned observability space, but they are optimized for different inspection workflows.
</p>

<pre>
same underlying execution observations
                │
        ┌───────┴────────┐
        │                │
        ▼                ▼
   local probe       centralized watch
   source-attached   persistent list entry
   diagram-centric   monitoring-centric
   nearby context    cross-navigation context
</pre>

<h3>7.1 Probe</h3>

<p>
A probe is primarily local and source-attached.
It is commonly used near the target being inspected and is naturally associated with diagram-centric workflows.
</p>

<h3>7.2 Watch</h3>

<p>
A watch is primarily persistent and centralized.
It is designed to keep important observations visible across navigation, stepping, and broader inspection workflows.
</p>

<h3>7.3 Relationship</h3>

<p>
An IDE MAY allow:
</p>

<ul>
  <li>creating a probe directly from a source target,</li>
  <li>creating a watch directly from a source target,</li>
  <li>creating a watch from an existing probe,</li>
  <li>creating a probe from an existing watch target.</li>
</ul>

<p>
However, a probe MUST NOT be treated as merely a differently rendered watch.
Its defining property is local source attachment.
</p>

<hr/>

<h2 id="probe-attachment-model">8. Probe Attachment Model</h2>

<p>
A probe MUST be attached to exactly one primary target.
For v0.1, a primary target MAY be:
</p>

<ul>
  <li>an edge,</li>
  <li>a node input port,</li>
  <li>a node output port,</li>
  <li>a local-memory slot owned by a local-memory node instance,</li>
  <li>a UI-sequencing edge in a stricter profile.</li>
</ul>

<p>
A probe MAY also be associated with contextual execution information such as:
</p>

<ul>
  <li>sub-FROG call stack,</li>
  <li>structure nesting,</li>
  <li>selected region,</li>
  <li>loop iteration index,</li>
  <li>activation identifier.</li>
</ul>

<p>
This context is necessary so that the IDE can distinguish repeated observations of the same source object across iterations, structure activations, and nested sub-FROG calls.
</p>

<pre>
probe entry
  ├── primary target
  │     └── edge / port / local_memory / stricter-profile target
  ├── latest compatible observation
  │     └── committed value or committed state snapshot
  └── execution context
        ├── subfrog stack
        ├── structure stack
        ├── selected region
        ├── iteration
        └── activation id
</pre>

<hr/>

<h2 id="canonical-probe-kinds">9. Canonical Probe Kinds</h2>

<p>
The canonical probe kinds for FROG v0.1 are:
</p>

<ul>
  <li><code>edge_probe</code> — attached to one source edge,</li>
  <li><code>port_probe</code> — attached to one source node port,</li>
  <li><code>local_memory_probe</code> — attached to one local-memory slot owned by a node instance.</li>
</ul>

<p>
Among these, <code>edge_probe</code> is the primary and most important probe kind for v0.1.
It is the canonical probe form for ordinary dataflow inspection.
</p>

<p>
A stricter profile MAY additionally support:
</p>

<ul>
  <li><code>ui_sequence_probe</code>,</li>
  <li><code>structure_probe</code>,</li>
  <li><code>custom_probe</code>.</li>
</ul>

<hr/>

<h2 id="probe-lifecycle">10. Probe Lifecycle</h2>

<h3 id="creation">10.1 Creation</h3>

<p>
A probe is created when the IDE attaches a new probe object to a valid source-level target.
Probe creation MUST fail if the requested target is not a valid probe target in the active profile.
</p>

<h3 id="probe-entry-states">10.2 Probe-entry states</h3>

<p>
A probe MAY conceptually be in one of the following states:
</p>

<ul>
  <li><code>created</code> — probe exists but has not yet observed any compatible execution activity,</li>
  <li><code>live</code> — probe is currently observing a running or paused execution instance,</li>
  <li><code>retained</code> — probe is showing the most recent retained value after execution,</li>
  <li><code>unavailable</code> — probe target exists but no compatible value or state snapshot is currently available,</li>
  <li><code>closed</code> — probe has been removed.</li>
</ul>

<p>
These are probe-entry states.
They MUST NOT be confused with the execution state of the underlying live instance.
</p>

<h3 id="removal">10.3 Removal</h3>

<p>
Removing a probe MUST affect only the inspection layer.
It MUST NOT alter the program graph, execution semantics, or source representation.
</p>

<hr/>

<h2 id="value-capture-semantics">11. Value Capture Semantics</h2>

<h3>11.1 General rule</h3>

<p>
A probe does not invent values.
It displays values or execution state only when those values or states become available through the source-aligned observability model.
</p>

<h3>11.2 Last-known committed observation</h3>

<p>
For v0.1, the primary value model of a probe is the <strong>last-known committed observation</strong>.
This means the most recent committed source-level value or state snapshot observed for the probe target in the relevant execution context.
</p>

<h3>11.3 Multiple observations</h3>

<p>
If a probe target receives multiple compatible observations over time, the base v0.1 model requires that the probe be able to show at least the most recent one.
A stricter profile MAY additionally keep a bounded history or a richer time-series representation.
</p>

<h3>11.4 Value previews and full values</h3>

<p>
A runtime is not required to expose a fully materialized value for every observation.
A probe MAY display:
</p>

<ul>
  <li>a full value snapshot,</li>
  <li>a summarized preview,</li>
  <li>a type-aware rendering,</li>
  <li>an opaque placeholder indicating availability without a full displayable value.</li>
</ul>

<p>
Whatever rendering strategy is used, the semantic meaning MUST remain that the probe refers to the last-known committed source-level observation for its target.
</p>

<h3>11.5 No fabricated values</h3>

<p>
If no compatible committed observation exists yet, the probe MUST remain unavailable rather than implying that a value exists.
</p>

<hr/>

<h2 id="live-paused-and-retained-views">12. Live, Paused, and Retained Views</h2>

<h3>12.1 General model</h3>

<pre>
running execution
      │
      ├── compatible committed observation arrives
      │        └── probe may update live
      │
      ├── debugger pauses at safe boundary
      │        └── probe must match paused snapshot
      │
      └── execution ends
               └── probe may become retained if profile allows
</pre>

<h3>12.2 Live view</h3>

<p>
During a running execution, a probe MAY update continuously as new compatible source-aligned observations become available.
The exact UI refresh strategy is implementation-defined.
</p>

<h3>12.3 Paused view</h3>

<p>
When a debug session is paused, probe values MUST reflect the causally consistent paused snapshot exposed to the IDE.
A probe MUST NOT show values that contradict the paused execution view.
</p>

<h3>12.4 Retained view</h3>

<p>
A stricter profile MAY support retained probe values after a run has completed, faulted, aborted, or paused.
In that case, a probe MAY continue displaying the most recent retained observation even when execution is no longer live.
</p>

<p>
Retained values are optional in v0.1.
If they are supported, the IDE MUST clearly distinguish retained values from live-updating values.
</p>

<h3>12.5 No fabricated history</h3>

<p>
If retained values are supported, the IDE MUST NOT imply that a full historical sequence exists unless such history is actually preserved by the active profile.
</p>

<h3>12.6 Instance association</h3>

<p>
A retained probe value SHOULD remain attributable to the live execution instance from which it was derived when the active profile exposes that distinction.
An IDE MUST NOT silently conflate retained observations from unrelated instances.
</p>

<hr/>

<h2 id="edge-probes">13. Edge Probes</h2>

<h3>13.1 Role</h3>

<p>
An <code>edge_probe</code> is attached to a single source edge.
It is the canonical probe type for observing ordinary dataflow in FROG.
</p>

<h3>13.2 Trigger</h3>

<p>
An edge probe is updated when the probe target receives an observable <code>edge_value_available</code> event in the current execution context, or when an equivalent paused committed observation confirms the current edge value in the active profile.
</p>

<h3>13.3 Meaning</h3>

<p>
The meaning of an edge probe is:
</p>

<pre><code>show the last-known committed value
that became available on this source edge
in the relevant execution context</code></pre>

<h3>13.4 Fan-out</h3>

<p>
If one source output fans out to multiple edges, each edge MAY have its own probe.
This is correct because source-level inspection is naturally edge-based, even if the runtime internally optimizes fan-out.
</p>

<h3>13.5 Context-sensitive repeated values</h3>

<p>
If the same edge is activated across different loop iterations or nested execution contexts, the probe SHOULD remain aware of that context.
A stricter profile MAY show iteration metadata or a context stack together with the displayed value.
</p>

<hr/>

<h2 id="node-port-probes">14. Node-Port Probes</h2>

<h3>14.1 Purpose</h3>

<p>
A <code>port_probe</code> is attached to a specific source node port rather than to a full edge.
This is useful when the IDE wishes to present inspection at the node boundary level.
</p>

<h3>14.2 Input and output ports</h3>

<p>
A port probe MAY target:
</p>

<ul>
  <li>an input port,</li>
  <li>an output port.</li>
</ul>

<p>
However, an implementation SHOULD prefer edge probes for ordinary valueflow inspection whenever the source graph already provides an explicit edge identity.
</p>

<h3>14.3 Semantics</h3>

<p>
A port probe attached to an output port SHOULD be semantically equivalent to probing an outgoing edge, except that the presentation is port-centered rather than edge-centered.
A port probe attached to an input port SHOULD reflect the committed value received at that input in the relevant execution context.
</p>

<hr/>

<h2 id="local-memory-probes">15. Local-Memory Probes</h2>

<h3>15.1 Purpose</h3>

<p>
A <code>local_memory_probe</code> is attached to the local-memory slot owned by a local-memory primitive instance.
Its purpose is to inspect source-level memory behavior rather than only the values present on ordinary edges.
</p>

<h3>15.2 Canonical v0.1 case: <code>frog.core.delay</code></h3>

<p>
For <code>frog.core.delay</code>, a local-memory probe SHOULD make it possible to inspect at least:
</p>

<ul>
  <li>the current stored state visible at pause time when such state exposure is supported,</li>
  <li>the most recent observed <code>state_read</code>,</li>
  <li>the most recent observed <code>state_updated</code>.</li>
</ul>

<h3>15.3 Meaning</h3>

<p>
A local-memory probe is not just another edge probe.
It is attached to the stateful source-aligned object owned by the node instance.
For <code>frog.core.delay</code>, it therefore observes source-aligned local-memory activity without redefining the primitive-local behavior itself.
</p>

<h3>15.4 Deterministic interpretation</h3>

<p>
If a local-memory probe displays a current stored value during a paused snapshot, that value MUST be the value that is committed for the paused live execution instance.
</p>

<pre>
delay node instance
   ├── observed state_read
   ├── observed state_updated
   └── paused current stored value
        (only when the active profile exposes it)
</pre>

<hr/>

<h2 id="ui-related-probes">16. UI-Related Probes</h2>

<h3>16.1 Ordinary widget-related valueflow</h3>

<p>
Ordinary widget-related valueflow SHOULD be inspected through the same canonical mechanisms as other dataflow:
</p>

<ul>
  <li>edge probes on edges connected to <code>widget_value</code>,</li>
  <li>port probes on relevant widget-related ports if supported.</li>
</ul>

<h3>16.2 Object-style widget interaction</h3>

<p>
Object-style widget interaction through <code>widget_reference</code>, <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code> MAY also be probed indirectly through:
</p>

<ul>
  <li>ordinary valueflow edges,</li>
  <li>pause-localized debugging state,</li>
  <li>a stricter profile’s dedicated UI-oriented probe renderers.</li>
</ul>

<h3>16.3 UI sequencing edges</h3>

<p>
The <code>ui_in</code> / <code>ui_out</code> sequencing edges are not ordinary data-value edges.
A stricter profile MAY support probes on these sequencing edges, but such probes MUST be interpreted as effect-order inspection rather than ordinary value inspection.
</p>

<p>
When such probes are supported, they MUST remain aligned both with the source-facing widget interaction model and with the standardized <code>frog.ui.*</code> primitive definitions.
</p>

<hr/>

<h2 id="probe-presentation-model">17. Probe Presentation Model</h2>

<h3>17.1 General rule</h3>

<p>
This document does not standardize one required probe window layout.
It standardizes the source-level meaning of probe displays.
</p>

<h3>17.2 Minimal displayed information</h3>

<p>
For v0.1, a probe display SHOULD be able to show at least:
</p>

<ul>
  <li>the probe target identity,</li>
  <li>the most recent value or state snapshot when available,</li>
  <li>the target type when useful,</li>
  <li>the last update status,</li>
  <li>basic execution-context information when relevant.</li>
</ul>

<h3>17.3 Possible presentations</h3>

<p>
An IDE MAY present probes through:
</p>

<ul>
  <li>inline overlay bubbles near the diagram target,</li>
  <li>detachable probe windows,</li>
  <li>a centralized probe-management window,</li>
  <li>status panes or inspector panels.</li>
</ul>

<h3>17.4 Probe numbering or naming</h3>

<p>
An IDE MAY assign probe numbers or probe names for management purposes.
Such numbering is an IDE concern only and is not part of the FROG source model.
</p>

<hr/>

<h2 id="probe-management">18. Probe Management</h2>

<p>
A debugging-capable IDE SHOULD support at least the following probe-management operations:
</p>

<ul>
  <li>create probe,</li>
  <li>remove probe,</li>
  <li>list active probes,</li>
  <li>locate a probe from its source target,</li>
  <li>locate a source target from its probe entry.</li>
</ul>

<p>
A stricter profile MAY additionally support:
</p>

<ul>
  <li>pinning a probe window,</li>
  <li>grouping probes by FROG or by execution instance,</li>
  <li>sorting by creation order,</li>
  <li>showing last-update timestamps,</li>
  <li>bulk removal.</li>
</ul>

<hr/>

<h2 id="custom-and-type-specific-probes">19. Custom and Type-Specific Probes</h2>

<h3>19.1 Rationale</h3>

<p>
Different data types benefit from different visualizations.
For example, a scalar, an array, a waveform-like value, and an external reference handle may require different display strategies.
</p>

<h3>19.2 Base rule</h3>

<p>
FROG v0.1 allows the concept of type-specific and custom probes, but does not standardize a full plugin or packaging system for them.
</p>

<h3>19.3 Semantic constraints</h3>

<p>
A custom or type-specific probe MUST still obey the base semantic rules of this document:
</p>

<ul>
  <li>it must attach to a valid source-level target,</li>
  <li>it must display committed observations only,</li>
  <li>it must not change program semantics,</li>
  <li>it must not pretend to expose more execution history than the active profile actually provides.</li>
</ul>

<h3>19.4 Default probe behavior</h3>

<p>
If no specialized probe exists for a type, the IDE SHOULD fall back to a generic value-oriented probe representation.
</p>

<hr/>

<h2 id="validation-and-safety-rules">20. Validation and Safety Rules</h2>

<ul>
  <li>A probe MUST target a valid source-visible object supported by the active profile.</li>
  <li>A probe MUST NOT alter the execution semantics of the graph.</li>
  <li>A probe shown during pause MUST reflect the paused causal snapshot exposed to the IDE.</li>
  <li>A retained probe value MUST be clearly distinguishable from a live-updating value.</li>
  <li>A probe MUST NOT expose a contradictory combination of target identity, execution context, and value.</li>
  <li>A local-memory probe MUST respect the node-instance-local scope of local memory.</li>
  <li>A UI-sequencing probe, if supported, MUST NOT be misrepresented as an ordinary data-value probe.</li>
  <li>A probe MUST NOT be presented as a watch entry unless the IDE explicitly re-exposes it through the watch model defined elsewhere.</li>
  <li>A probe MUST NOT silently conflate observations from unrelated live execution instances when retained behavior is supported.</li>
</ul>

<hr/>

<h2 id="illustrative-examples">21. Illustrative Examples</h2>

<h3>21.1 Edge probe</h3>

<pre><code>{
  "probe_id": "p1",
  "kind": "edge_probe",
  "target": {
    "kind": "edge",
    "id": "e_sum"
  },
  "state": "live",
  "last_value": {
    "preview": "17.5"
  }
}</code></pre>

<h3>21.2 Port probe</h3>

<pre><code>{
  "probe_id": "p2",
  "kind": "port_probe",
  "target": {
    "kind": "port",
    "node_id": "add_1",
    "port": "result",
    "direction": "output"
  },
  "state": "live",
  "last_value": {
    "preview": "17.5"
  }
}</code></pre>

<h3>21.3 Local-memory probe for <code>frog.core.delay</code></h3>

<pre><code>{
  "probe_id": "p3",
  "kind": "local_memory_probe",
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

<h3>21.4 Retained edge probe</h3>

<pre><code>{
  "probe_id": "p4",
  "kind": "edge_probe",
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
  <li>conditional probes that trigger break behavior,</li>
  <li>watch expressions over arbitrary graph expressions,</li>
  <li>mandatory history buffers for every probe,</li>
  <li>reverse-time probe inspection,</li>
  <li>standardized distributed probe aggregation,</li>
  <li>remote probe streaming protocols,</li>
  <li>probe-driven execution modification,</li>
  <li>mandatory custom-probe packaging and discovery rules.</li>
</ul>

<hr/>

<h2 id="summary">23. Summary</h2>

<p>
FROG probes are source-aligned inspection objects for live, paused, and retained execution views.
For v0.1, the canonical probe model is centered on the inspection of values flowing through edges, while also allowing probes on ports and local-memory state where appropriate.
</p>

<p>
This specification establishes that:
</p>

<ul>
  <li>probes belong to the IDE/debugging layer rather than the source language itself,</li>
  <li>probes attach to source-visible execution objects,</li>
  <li><code>edge_probe</code> is the primary probe form in v0.1,</li>
  <li>probe values represent last-known committed observations,</li>
  <li>paused probe views must remain causally consistent,</li>
  <li>retained values are optional and must be clearly identified as such,</li>
  <li>probes remain distinct from centralized watch entries,</li>
  <li>custom and type-specific probes may exist without changing the base semantics.</li>
</ul>

<hr/>

<h2 id="license">24. License</h2>

<p>
This specification is part of the FROG repository and is governed by the repository license and contribution rules.
</p>
