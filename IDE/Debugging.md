<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG IDE Debugging Specification</h1>

<p align="center">
  <strong>Definition of interactive debugging behavior in a FROG IDE</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope-for-v01">2. Scope for v0.1</a></li>
  <li><a href="#architectural-position-and-dependencies">3. Architectural Position and Dependencies</a></li>
  <li><a href="#repository-navigation">4. Repository Navigation</a></li>
  <li><a href="#design-principles">5. Design Principles</a></li>
  <li><a href="#debug-session-model">6. Debug Session Model</a></li>
  <li><a href="#pause-resume-and-abort">7. Pause, Resume, and Abort</a></li>
  <li><a href="#breakpoints">8. Breakpoints</a></li>
  <li><a href="#stepping-model">9. Stepping Model</a></li>
  <li><a href="#nested-scope-debugging">10. Nested-Scope Debugging</a></li>
  <li><a href="#execution-highlighting">11. Execution Highlighting</a></li>
  <li><a href="#fault-handling-during-debugging">12. Fault Handling During Debugging</a></li>
  <li><a href="#front-panel-and-widget-debug-visibility">13. Front Panel and Widget Debug Visibility</a></li>
  <li><a href="#ide-requirements">14. IDE Requirements</a></li>
  <li><a href="#illustrative-debug-objects">15. Illustrative Debug Objects</a></li>
  <li><a href="#out-of-scope-for-v01">16. Out of Scope for v0.1</a></li>
  <li><a href="#summary">17. Summary</a></li>
  <li><a href="#license">18. License</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the <strong>interactive debugging behavior</strong> of a FROG IDE.
It specifies how an IDE may pause, resume, inspect, and step through a live execution instance
in a <strong>source-aligned</strong> way.
</p>

<p>
This document does <strong>not</strong> define execution semantics.
Execution meaning remains defined by the validated executable graph and by the relevant
language and library specifications.
This document standardizes only the IDE-facing control meaning needed for:
</p>

<ul>
  <li>run-under-debug behavior,</li>
  <li>manual pause and resume,</li>
  <li>user-facing abort,</li>
  <li>breakpoints,</li>
  <li>single-step commands,</li>
  <li>fault-directed pause when supported,</li>
  <li>source-aligned debug inspection.</li>
</ul>

<pre><code>Language/
    -&gt; owns execution meaning and safe debug stops

IR/
    -&gt; owns execution-facing derivation and identity preservation posture

IDE/Observability.md
    -&gt; owns the observable projection consumed by tools

IDE/Debugging.md
    -&gt; owns interactive debug control meaning for the IDE
</code></pre>

<p>
Interactive debugging is therefore a tooling-facing layer over already-defined execution meaning.
It is not a replacement for the execution model, not a replacement for safe-boundary semantics,
and not a runtime-internal scheduler specification.
</p>

<hr/>

<h2 id="scope-for-v01">2. Scope for v0.1</h2>

<p>
For FROG v0.1, this document standardizes the IDE-facing meaning of:
</p>

<ul>
  <li>debug sessions,</li>
  <li>manual pause, resume, and abort,</li>
  <li>execution highlighting during debugging,</li>
  <li>minimum interactive breakpoint behavior,</li>
  <li><code>step_into</code>,</li>
  <li><code>step_over</code>,</li>
  <li><code>step_out</code>,</li>
  <li>fault-directed pause and source localization when supported.</li>
</ul>

<p>
This document does <strong>not</strong> standardize:
</p>

<ul>
  <li>the execution model itself,</li>
  <li>the language-level safe-observation, safe-pause, or safe-debug-stop semantics themselves,</li>
  <li>the transport protocol between IDE and runtime,</li>
  <li>the exact rendering style of overlays,</li>
  <li>probe behavior,</li>
  <li>watch behavior,</li>
  <li>reverse execution,</li>
  <li>reverse stepping,</li>
  <li>timeline scrubbing,</li>
  <li>deterministic replay,</li>
  <li>performance profiling,</li>
  <li>deep value-serialization formats.</li>
</ul>

<hr/>

<h2 id="architectural-position-and-dependencies">3. Architectural Position and Dependencies</h2>

<h3>3.1 Repository position</h3>

<p>
This document belongs in <code>IDE/</code> because it defines how interactive debugging is exposed to users and tools.
It does <strong>not</strong> belong to <code>Language/</code> because it does not own execution meaning.
</p>

<h3>3.2 Dependencies</h3>

<p>
This document depends conceptually on the following repository areas:
</p>

<ul>
  <li><code>IDE/Readme.md</code> — architectural ownership of tooling behavior in the IDE layer,</li>
  <li><code>IDE/Observability.md</code> — source-aligned observability projection consumed by debugging,</li>
  <li><code>IDE/Probes.md</code> — probe behavior used together with debugging,</li>
  <li><code>IDE/Watch.md</code> — watch behavior used together with debugging,</li>
  <li><code>Expression/Diagram.md</code> — canonical node, edge, and executable-graph representation,</li>
  <li><code>Expression/Front panel.md</code> — source-facing front-panel composition,</li>
  <li><code>Expression/Widget interaction.md</code> — widget-related execution objects and explicit UI sequencing,</li>
  <li><code>Language/Control structures.md</code> — normative control-structure execution semantics,</li>
  <li><code>Language/State and cycles.md</code> — normative local-memory and cycle semantics,</li>
  <li><code>IR/Execution IR.md</code> — execution-facing posture and attributable object identity,</li>
  <li><code>IR/Derivation rules.md</code> — correspondence rules from validated meaning to execution-facing representation.</li>
</ul>

<h3>3.3 Ownership boundary</h3>

<p>
If a conflict appears, the following ownership rules apply:
</p>

<ul>
  <li><code>Expression/</code> remains authoritative for source-visible representation and serialized identity,</li>
  <li><code>Language/</code> remains authoritative for execution meaning, committed state, and safe debug-stop boundaries,</li>
  <li><code>Libraries/</code> remain authoritative for primitive-local meaning,</li>
  <li><code>IR/</code> remains authoritative for derivation and mapping posture,</li>
  <li><code>IDE/</code> remains authoritative only for the user-facing and tool-facing debugging layer.</li>
</ul>

<pre><code>Expression/
    owns what the user edits and what is serialized

Language/
    owns what execution means and where a safe debug stop exists

IR/
    owns execution-facing correspondence and attributable identity posture

Libraries/
    own primitive-local executable meaning

IDE/
    owns how the debugger controls and presents the already-defined execution
</code></pre>

<hr/>

<h2 id="repository-navigation">4. Repository Navigation</h2>

<p>
This document belongs to the following IDE cluster:
</p>

<pre><code>IDE/
├── Readme.md
│   -&gt; IDE architecture and responsibility boundaries
├── Observability.md
│   -&gt; live source-aligned execution projection
├── Debugging.md
│   -&gt; this document; interactive debugger behavior
├── Probes.md
│   -&gt; local attached inspection tools
├── Watch.md
│   -&gt; persistent centralized inspection tools
└── Snippet.md
    -&gt; snippet transport and reusable authoring fragments
</code></pre>

<p>
For navigation through the supporting architectural layers, a reader should also keep in view:
</p>

<pre><code>Expression/
    -&gt; source-visible graph objects and widget interaction representation

Language/
    -&gt; execution meaning, control structures, local memory, cycle semantics

IR/
    -&gt; execution-facing derivation and source-attributed correspondence posture
</code></pre>

<hr/>

<h2 id="design-principles">5. Design Principles</h2>

<h3>5.1 Source-level debugging</h3>

<p>
Debugging MUST be expressed in terms of source-visible concepts:
nodes, edges, structures, regions, sub-FROG calls, local-memory observations,
and widget-related execution objects when relevant.
The user MUST NOT be required to reason about runtime-private artifacts.
</p>

<h3>5.2 Dataflow-first behavior</h3>

<p>
FROG debugging MUST respect dataflow semantics.
It MUST NOT assume an implicit sequential instruction stream.
Debugging controls therefore operate over source-aligned observable execution activity.
</p>

<h3>5.3 Language-derived safe boundaries</h3>

<p>
A visible debugger stop MUST occur only at a language-valid safe debug stop.
The debugger MUST NOT expose a partially committed source-level state as if it were stable.
This document consumes that guarantee; it does not define it.
</p>

<h3>5.4 Runtime independence</h3>

<p>
Different runtimes MAY implement debugging through different internal mechanisms.
The source-level meaning exposed to the IDE MUST remain equivalent.
</p>

<h3>5.5 Capability profiles and debugging support levels remain distinct</h3>

<p>
The repository uses <code>Profiles/</code> for optional standardized executable capability families.
This document may also refer to <strong>debugging support levels</strong>, meaning stronger or weaker
interactive debug capabilities for an IDE/runtime pair.
These notions MUST NOT be conflated.
</p>

<ul>
  <li>a capability profile defines what executable capability families exist,</li>
  <li>a debugging support level defines how much interactive debugging behavior is available.</li>
</ul>

<h3>5.6 Minimal but extensible</h3>

<p>
FROG v0.1 defines a minimal interactive debugging core.
Stronger debugging support levels MAY expose richer controls, additional breakpoint conditions,
or deeper inspection capabilities, provided that the v0.1 meanings remain preserved.
</p>

<hr/>

<h2 id="debug-session-model">6. Debug Session Model</h2>

<h3>6.1 Definition</h3>

<p>
A <strong>debug session</strong> is the IDE-visible control context attached to one live execution instance.
A debug session owns the active debugger configuration for that instance.
</p>

<p>
A debug session conceptually contains:
</p>

<ul>
  <li>the target <code>instance_id</code>,</li>
  <li>the current debug-session state,</li>
  <li>the current pause reason when paused,</li>
  <li>the active breakpoint set,</li>
  <li>the currently selected source-aligned object,</li>
  <li>the relevant execution context,</li>
  <li>the active step request if one exists.</li>
</ul>

<h3>6.2 Debug-session states</h3>

<p>
A debug session MUST expose one of the following high-level states:
</p>

<ul>
  <li><code>idle</code> — no live execution instance is attached,</li>
  <li><code>starting</code> — execution is being prepared under debug control,</li>
  <li><code>running</code> — execution is progressing under an active debug session,</li>
  <li><code>paused</code> — execution is suspended at a language-valid safe debug stop,</li>
  <li><code>completed</code> — the instance finished normally,</li>
  <li><code>faulted</code> — the instance terminated because of a fault without remaining paused,</li>
  <li><code>aborted</code> — the instance terminated because of a user or external abort action.</li>
</ul>

<p>
These are debugger-facing session states.
They MUST NOT be confused with additional IDE-local attachment or view-management states.
</p>

<h3>6.3 Pause reasons</h3>

<p>
When a debug session is paused, the primary pause reason SHOULD be available.
Canonical pause reasons for v0.1 are:
</p>

<ul>
  <li><code>manual_pause</code>,</li>
  <li><code>breakpoint</code>,</li>
  <li><code>step_complete</code>,</li>
  <li><code>fault</code>.</li>
</ul>

<p>
Additional pause reasons MAY exist in stronger debugging support levels,
provided that they do not contradict these canonical meanings.
</p>

<h3>6.4 Selected object and context</h3>

<p>
When paused, the debugger SHOULD identify one primary selected source-aligned object.
That object MAY be:
</p>

<ul>
  <li>a node,</li>
  <li>an edge,</li>
  <li>a structure,</li>
  <li>a region,</li>
  <li>a sub-FROG call site,</li>
  <li>another supported source-aligned execution object.</li>
</ul>

<p>
The selected object is a debugger-facing focus object.
It does not replace the full execution context, which MUST remain available when needed to interpret:
</p>

<ul>
  <li>loop iteration identity,</li>
  <li>selected region identity,</li>
  <li>caller/callee nesting,</li>
  <li>repeated activations of the same source node.</li>
</ul>

<hr/>

<h2 id="pause-resume-and-abort">7. Pause, Resume, and Abort</h2>

<h3>7.1 Manual pause</h3>

<p>
A manual pause request asks the runtime to suspend execution at the next
language-valid safe debug stop.
</p>

<p>
When the session becomes paused, the IDE-facing view MUST be interpretable as a
<strong>pause-consistent snapshot</strong>.
In particular, the debugger MUST be able to rely on the following:
</p>

<ul>
  <li>already-visible node completions are committed,</li>
  <li>already-visible edge values are committed,</li>
  <li>already-visible local-memory updates are committed,</li>
  <li>the visible structure and region context is coherent,</li>
  <li>the paused state corresponds to a coherent causal prefix.</li>
</ul>

<h3>7.2 Resume</h3>

<p>
A resume request restarts execution from the current paused state.
Unless a step request is active, execution continues freely until one of the following occurs:
</p>

<ul>
  <li>a breakpoint is hit,</li>
  <li>a fault-directed pause occurs,</li>
  <li>the user pauses manually again,</li>
  <li>the instance completes normally,</li>
  <li>the instance is aborted.</li>
</ul>

<h3>7.3 Abort</h3>

<p>
A user-facing stop action terminates the live execution instance.
At the debugging level, that outcome MUST be represented consistently with the instance becoming
<code>aborted</code>, unless a stronger implementation defines an explicitly different but equivalent
user-stop presentation.
</p>

<h3>7.4 Inspection during pause</h3>

<p>
While paused, the IDE MAY expose:
</p>

<ul>
  <li>the selected source object,</li>
  <li>the current execution context,</li>
  <li>relevant committed values,</li>
  <li>relevant committed local-memory state,</li>
  <li>probe and watch views defined elsewhere.</li>
</ul>

<p>
All such inspection MUST remain consistent with the paused execution snapshot exposed to the IDE.
</p>

<hr/>

<h2 id="breakpoints">8. Breakpoints</h2>

<h3>8.1 General model</h3>

<p>
A breakpoint is a debugger-facing stop condition attached to a source-aligned execution object.
When its condition is satisfied, execution MUST pause only at a corresponding
language-valid safe debug stop.
</p>

<p>
Breakpoint triggering is evaluated in source-aligned terms.
It MUST NOT require exposing runtime-private execution artifacts to the user.
</p>

<h3>8.2 Minimum interactive baseline</h3>

<p>
For FROG v0.1, the <strong>minimum interactive debugging baseline</strong> requires support for:
</p>

<ul>
  <li><code>node_breakpoint</code></li>
</ul>

<p>
That is the only required breakpoint kind for a minimal interactive debugging implementation.
</p>

<h3>8.3 Optional standardized breakpoint kinds</h3>

<p>
FROG v0.1 additionally standardizes the following <strong>optional breakpoint kinds</strong>:
</p>

<ul>
  <li><code>edge_breakpoint</code>,</li>
  <li><code>structure_breakpoint</code>,</li>
  <li><code>subfrog_breakpoint</code>.</li>
</ul>

<p>
These kinds are standardized so that different implementations can expose compatible meanings,
but they are not part of the minimum baseline required by Section 14.
</p>

<h3>8.4 Node breakpoint</h3>

<p>
A node breakpoint is attached to one source node.
For the minimum v0.1 baseline, the canonical condition is:
</p>

<ul>
  <li><code>on_start</code></li>
</ul>

<p>
A stronger debugging support level MAY additionally support:
</p>

<ul>
  <li><code>on_ready</code>,</li>
  <li><code>on_complete</code>,</li>
  <li><code>on_fault</code>.</li>
</ul>

<p>
When <code>on_ready</code> is supported, it requires a compatible observability support level that exposes readiness.
</p>

<h3>8.5 Edge breakpoint</h3>

<p>
An edge breakpoint is attached to one source edge.
Its v0.1 standardized meaning is:
</p>

<ul>
  <li>pause when a value becomes available on that edge in the relevant execution context.</li>
</ul>

<h3>8.6 Structure breakpoint</h3>

<p>
A structure breakpoint is attached to one structure node.
Its v0.1 standardized meaning is:
</p>

<ul>
  <li>pause when that structure activation begins.</li>
</ul>

<p>
A stronger support level MAY additionally expose region-selection or iteration-aware structure break conditions.
</p>

<h3>8.7 Sub-FROG breakpoint</h3>

<p>
A sub-FROG breakpoint is attached to one <code>subfrog</code> call site.
Its v0.1 standardized meaning is:
</p>

<ul>
  <li>pause when that call-site activation begins.</li>
</ul>

<h3>8.8 Enabled and disabled breakpoints</h3>

<p>
A breakpoint MAY be enabled or disabled without being removed.
A disabled breakpoint MUST have no effect on execution.
</p>

<h3>8.9 Multiple simultaneous matches</h3>

<p>
If multiple breakpoint conditions are satisfied at the same safe debug stop,
the runtime MAY report one primary breakpoint cause and additional matched breakpoints.
The IDE MUST NOT present contradictory source state.
</p>

<hr/>

<h2 id="stepping-model">9. Stepping Model</h2>

<h3>9.1 General rule</h3>

<p>
Single-stepping in FROG is defined over <strong>source-aligned observable execution</strong>,
not over a linear instruction stream.
A step request resumes execution in a constrained way until the first
<strong>eligible safe debug stop</strong> for that request is reached.
</p>

<h3>9.2 Eligible safe debug stop</h3>

<p>
An eligible safe debug stop is a language-valid safe debug stop that also satisfies the IDE-facing
selection rule of the active step command.
The step command defines the selection rule.
The language defines where safe debug stops may exist.
</p>

<pre><code>step request issued by IDE
        |
        v
runtime continues execution
        |
        v
language-valid safe debug stops become reachable
        |
        v
first stop matching the step-selection rule
        |
        v
debug session pauses
</code></pre>

<h3>9.3 Canonical step commands</h3>

<p>
The canonical step commands for FROG v0.1 are:
</p>

<ul>
  <li><code>step_into</code>,</li>
  <li><code>step_over</code>,</li>
  <li><code>step_out</code>.</li>
</ul>

<h3>9.4 <code>step_into</code></h3>

<p>
<code>step_into</code> resumes execution until the first eligible safe debug stop
on the current causally reachable execution path.
When the current paused object represents a nested executable unit,
<code>step_into</code> MAY stop inside that nested scope.
</p>

<h3>9.5 <code>step_over</code></h3>

<p>
<code>step_over</code> treats the currently selected source-aligned executable unit as one debugger-facing unit.
It resumes execution until that currently selected unit has completed from the point of view of its
immediate parent scope, then pauses at the first eligible safe debug stop in that parent scope.
</p>

<h3>9.6 <code>step_out</code></h3>

<p>
<code>step_out</code> is valid only when the current paused location is inside a nested debug scope.
It resumes execution until the current nested scope has completed from the point of view of its immediate
parent scope, then pauses at the first eligible safe debug stop in that parent scope.
</p>

<p>
If no parent debug scope exists, <code>step_out</code> MAY either:
</p>

<ul>
  <li>be rejected as unavailable, or</li>
  <li>behave like an ordinary resume.</li>
</ul>

<h3>9.7 Step completion</h3>

<p>
When a step request succeeds normally, the resulting pause reason SHOULD be:
</p>

<ul>
  <li><code>step_complete</code></li>
</ul>

<p>
If a breakpoint is hit before the intended step target is reached, the pause reason MAY be <code>breakpoint</code>.
If a fault-directed pause occurs, the pause reason MUST be <code>fault</code>.
</p>

<hr/>

<h2 id="nested-scope-debugging">10. Nested-Scope Debugging</h2>

<h3>10.1 General rule</h3>

<p>
FROG debugging is scope-aware.
A paused location may belong to a nested source-aligned execution scope, including:
</p>

<ul>
  <li>a sub-FROG invocation scope,</li>
  <li>a selected structure region,</li>
  <li>a loop iteration context,</li>
  <li>another nested dynamic scope exposed by a stronger debugging support level.</li>
</ul>

<p>
The debugger SHOULD preserve that nesting explicitly in the visible execution context.
</p>

<h3>10.2 Sub-FROG scopes</h3>

<p>
A <code>subfrog</code> node creates a nested source-aligned call scope for debugging purposes.
Therefore:
</p>

<ul>
  <li><code>step_into</code> MAY enter the nested sub-FROG scope,</li>
  <li><code>step_over</code> MUST treat the call as one caller-visible unit,</li>
  <li><code>step_out</code> from inside the callee MUST return to the caller scope.</li>
</ul>

<h3>10.3 Case structures</h3>

<p>
For a <code>case</code> structure:
</p>

<ul>
  <li>only the selected region belongs to the active dynamic path for that activation,</li>
  <li><code>step_into</code> MAY stop at selected-region entry or at the first eligible stop inside it,</li>
  <li><code>step_over</code> MUST execute the selected region as one structure activation and return to the parent scope,</li>
  <li><code>step_out</code> from inside the selected region MUST continue until the structure activation completes and then return to the parent scope.</li>
</ul>

<h3>10.4 Loop structures</h3>

<p>
Loop debugging is iteration-aware.
The same source node MAY therefore appear repeatedly under distinct iteration contexts.
The IDE SHOULD preserve iteration identity while debugging.
</p>

<p>
Because a <code>while_loop</code> may execute an unbounded number of iterations,
an IDE SHOULD make it visually clear that <code>step_over</code> may continue for a long time.
That warning is advisory only and does not alter stepping semantics.
</p>

<h3>10.5 Local memory inside nested scopes</h3>

<p>
When local-memory primitives are active inside nested scopes,
the debugger MUST preserve the source meaning of local state for the current live execution instance.
A paused view MUST NOT misrepresent stored state across iterations or nested activations.
</p>

<hr/>

<h2 id="execution-highlighting">11. Execution Highlighting</h2>

<h3>11.1 General rule</h3>

<p>
A debugging-capable IDE SHOULD support execution highlighting.
Execution highlighting is the source-level visual projection of live execution activity onto the diagram.
</p>

<h3>11.2 Highlightable objects</h3>

<p>
An IDE SHOULD be able to highlight at least:
</p>

<ul>
  <li>node execution start,</li>
  <li>node execution completion,</li>
  <li>edge value availability,</li>
  <li>structure entry,</li>
  <li>selected case regions,</li>
  <li>loop iteration progression.</li>
</ul>

<h3>11.3 Meaning of highlighting</h3>

<p>
Highlighting is descriptive, not prescriptive.
It visualizes execution activity already made observable to the IDE.
It MUST NOT alter execution meaning.
</p>

<h3>11.4 No mandatory rendering style</h3>

<p>
This specification does not require a particular animation model, color model, line style, or theme.
Any rendering strategy is acceptable provided that the displayed meaning remains source-aligned and understandable.
</p>

<hr/>

<h2 id="fault-handling-during-debugging">12. Fault Handling During Debugging</h2>

<h3>12.1 General rule</h3>

<p>
If a fault occurs while debugging is active, the debug session SHOULD pause at the most relevant
language-valid safe debug stop associated with that fault when the active debugging support level
supports fault-directed pause.
</p>

<p>
The debug-session state MUST then become either:
</p>

<ul>
  <li><code>paused</code> with pause reason <code>fault</code>, or</li>
  <li><code>faulted</code> if the implementation does not support fault-directed pause before termination.</li>
</ul>

<h3>12.2 Fault localization</h3>

<p>
When possible, the IDE SHOULD identify at least one primary source object related to the fault, such as:
</p>

<ul>
  <li>a node,</li>
  <li>a structure,</li>
  <li>a sub-FROG call site,</li>
  <li>a widget interaction node.</li>
</ul>

<h3>12.3 Consistency rule</h3>

<p>
Fault-directed pause MUST still obey language-level safe debug-stop rules.
The debugger MUST NOT show a contradictory partial state merely because the pause reason is <code>fault</code>.
</p>

<hr/>

<h2 id="front-panel-and-widget-debug-visibility">13. Front Panel and Widget Debug Visibility</h2>

<h3>13.1 Widget-related execution objects</h3>

<p>
Widget participation in debugging occurs through the diagram-level execution objects already defined by source
and consumed through the relevant primitive contracts, including:
</p>

<ul>
  <li><code>widget_value</code>,</li>
  <li><code>widget_reference</code>,</li>
  <li><code>frog.ui.property_read</code>,</li>
  <li><code>frog.ui.property_write</code>,</li>
  <li><code>frog.ui.method_invoke</code>.</li>
</ul>

<p>
These objects are debuggable like other diagram-level execution objects,
subject to source representation, language semantics, primitive-local behavior,
and explicit UI sequencing where present.
</p>

<h3>13.2 Front-panel reflection</h3>

<p>
A debugging-capable IDE MAY reflect debug state on the front panel when that reflection is source-meaningful.
Examples include:
</p>

<ul>
  <li>showing the current widget value when relevant,</li>
  <li>showing that a property write has occurred,</li>
  <li>showing the result of a property read,</li>
  <li>showing explicit UI-effect sequencing progress.</li>
</ul>

<p>
However, the front panel remains a user-facing UI composition, not the authoritative executable graph.
Pause locations and step targets therefore remain defined primarily in diagram terms.
</p>

<hr/>

<h2 id="ide-requirements">14. IDE Requirements</h2>

<h3>14.1 Minimum interactive debugging baseline</h3>

<p>
An IDE that claims support for FROG interactive debugging SHOULD provide at least:
</p>

<ul>
  <li>run under debug control,</li>
  <li>manual pause and resume,</li>
  <li>manual abort,</li>
  <li>execution highlighting,</li>
  <li><code>node_breakpoint</code>,</li>
  <li><code>step_into</code>,</li>
  <li><code>step_over</code>,</li>
  <li><code>step_out</code>.</li>
</ul>

<h3>14.2 Optional standardized additions</h3>

<p>
An IDE MAY additionally provide:
</p>

<ul>
  <li><code>edge_breakpoint</code>,</li>
  <li><code>structure_breakpoint</code>,</li>
  <li><code>subfrog_breakpoint</code>,</li>
  <li>fault-directed pause with source localization,</li>
  <li>readiness-aware overlays when readiness is exposed,</li>
  <li>front-panel debug reflection,</li>
  <li>execution traces,</li>
  <li>probe integration as defined by <code>IDE/Probes.md</code>,</li>
  <li>watch integration as defined by <code>IDE/Watch.md</code>.</li>
</ul>

<p>
User-interface design is not standardized here.
Only the source-level meaning of the debugging controls is standardized here.
</p>

<hr/>

<h2 id="illustrative-debug-objects">15. Illustrative Debug Objects</h2>

<p>
The examples below are illustrative only.
They show possible debugger-facing representations.
They are <strong>not</strong> a required transport format.
</p>

<h3>15.1 Node breakpoint</h3>

<pre><code>{
  "kind": "node_breakpoint",
  "enabled": true,
  "target": {
    "kind": "node",
    "id": "add_1"
  },
  "condition": "on_start"
}</code></pre>

<h3>15.2 Edge breakpoint</h3>

<pre><code>{
  "kind": "edge_breakpoint",
  "enabled": true,
  "target": {
    "kind": "edge",
    "id": "e_sum"
  }
}</code></pre>

<h3>15.3 Paused debug snapshot</h3>

<pre><code>{
  "debug_state": "paused",
  "pause_reason": "step_complete",
  "instance_id": "run_42",
  "selected_object": {
    "kind": "node",
    "id": "add_1"
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
  }
}</code></pre>

<h3>15.4 Fault-directed pause</h3>

<pre><code>{
  "debug_state": "paused",
  "pause_reason": "fault",
  "instance_id": "run_42",
  "selected_object": {
    "kind": "node",
    "id": "write_gain"
  },
  "details": {
    "fault_kind": "ui_write_failure"
  }
}</code></pre>

<hr/>

<h2 id="out-of-scope-for-v01">16. Out of Scope for v0.1</h2>

<p>
The following topics remain intentionally out of scope for this document:
</p>

<ul>
  <li>execution-model ownership,</li>
  <li>safe-debug-stop semantic ownership,</li>
  <li>probe behavior,</li>
  <li>watch behavior and watch expressions,</li>
  <li>conditional breakpoints,</li>
  <li>break-on-value-change semantics,</li>
  <li>break-on-fault filters,</li>
  <li>iteration-specific breakpoint expressions,</li>
  <li>reverse stepping,</li>
  <li>reverse execution,</li>
  <li>deterministic replay,</li>
  <li>distributed multi-runtime debug coordination,</li>
  <li>deep value-inspection protocols,</li>
  <li>performance profiling and timing analysis.</li>
</ul>

<hr/>

<h2 id="summary">17. Summary</h2>

<p>
FROG interactive debugging defines the IDE-facing meaning of pause, resume, abort,
breakpoints, and stepping for live executions of FROG programs.
It preserves the dataflow nature of the language and avoids imposing a false sequential execution model.
</p>

<p>
For FROG v0.1, this specification standardizes:
</p>

<ul>
  <li>debug sessions,</li>
  <li>pause, resume, and abort behavior,</li>
  <li>execution highlighting,</li>
  <li>the minimum interactive breakpoint baseline,</li>
  <li><code>step_into</code>,</li>
  <li><code>step_over</code>,</li>
  <li><code>step_out</code>,</li>
  <li>fault-directed pause and localization when supported.</li>
</ul>

<p>
This debugging layer provides the foundation for richer inspection tooling while preserving the architectural separation between:
</p>

<ul>
  <li>execution semantics,</li>
  <li>observable execution projection,</li>
  <li>interactive debugger control,</li>
  <li>probe and watch consumption.</li>
</ul>

<hr/>

<h2 id="license">18. License</h2>

<p>
This specification is part of the FROG repository and is governed by the repository license and contribution rules.
</p>
