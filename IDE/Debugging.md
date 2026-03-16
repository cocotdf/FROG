<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG IDE Debugging Specification</h1>

<p align="center">
Definition of interactive debugging behavior in a FROG IDE<br/>
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
  <li><a href="#debugging-model">6. Debugging Model</a></li>
  <li><a href="#debug-session">7. Debug Session</a></li>
  <li><a href="#execution-highlighting">8. Execution Highlighting</a></li>
  <li><a href="#pause-and-resume-model">9. Pause and Resume Model</a></li>
  <li><a href="#breakpoints">10. Breakpoints</a></li>
  <li><a href="#single-stepping-model">11. Single-Stepping Model</a></li>
  <li><a href="#sub-frog-and-structure-stepping">12. Sub-FROG and Structure Stepping</a></li>
  <li><a href="#loop-debugging-semantics">13. Loop Debugging Semantics</a></li>
  <li><a href="#fault-handling-during-debugging">14. Fault Handling During Debugging</a></li>
  <li><a href="#front-panel-and-widget-debug-visibility">15. Front Panel and Widget Debug Visibility</a></li>
  <li><a href="#ide-requirements">16. IDE Requirements</a></li>
  <li><a href="#illustrative-debug-objects">17. Illustrative Debug Objects</a></li>
  <li><a href="#out-of-scope-for-v01">18. Out of Scope for v0.1</a></li>
  <li><a href="#summary">19. Summary</a></li>
  <li><a href="#license">20. License</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the interactive debugging behavior of a FROG IDE.
It specifies how an IDE may pause, resume, inspect, and step through a live execution of a FROG program in a source-aligned way.
</p>

<p>
The purpose of debugging is not to redefine execution semantics or language-level execution boundaries.
Execution meaning remains defined by the validated executable graph and the related language and library specifications.
This document defines the IDE-facing debugging controls and their source-level interactive meaning for:
</p>

<ul>
  <li>execution highlighting,</li>
  <li>pause and resume,</li>
  <li>breakpoints,</li>
  <li>single-step execution,</li>
  <li>source-level fault localization,</li>
  <li>debug-session state and pause reasons.</li>
</ul>

<p>
This document is IDE-facing.
It describes the behavior of interactive debugging as seen by the user and by source-aligned IDE tooling.
It does not standardize the internal runtime scheduler, transport protocol, execution engine, or language-level safe-boundary semantics used to implement that behavior.
</p>

<pre><code>Language/
    -&gt; owns execution meaning and safe debug stops

IDE/Execution observability.md
    -&gt; owns the observable projection of execution activity

IDE/Debugging.md
    -&gt; owns pause / resume / breakpoint / stepping meaning for tools
</code></pre>

<hr/>

<h2 id="goals">2. Goals</h2>

<p>This document has the following goals:</p>

<ul>
  <li>define a clear source-level debugging model for FROG diagrams,</li>
  <li>support a LabVIEW-like interactive debugging experience while remaining independent from any one implementation,</li>
  <li>keep debugging behavior aligned with dataflow execution rather than sequential source-code assumptions,</li>
  <li>define canonical IDE-facing meanings for pause, resume, breakpoints, and stepping,</li>
  <li>make debugging compatible with structures, loops, local memory, sub-FROGs, and widget interaction,</li>
  <li>provide a stable base for probes, watches, and richer execution instrumentation without relocating execution-model ownership into <code>IDE/</code>.</li>
</ul>

<hr/>

<h2 id="scope-for-v01">3. Scope for v0.1</h2>

<p>
For FROG v0.1, this document standardizes the IDE-facing meaning of:
</p>

<ul>
  <li>debug sessions,</li>
  <li>execution highlighting,</li>
  <li>manual pause and resume,</li>
  <li>user-facing stop / abort interaction,</li>
  <li>breakpoint kinds and activation rules,</li>
  <li><code>step_into</code>,</li>
  <li><code>step_over</code>,</li>
  <li><code>step_out</code>,</li>
  <li>fault-directed pause and localization when supported by the active debugging support level.</li>
</ul>

<p>
This document does <strong>not</strong> standardize:
</p>

<ul>
  <li>the transport protocol between IDE and runtime,</li>
  <li>the exact rendering style of overlays,</li>
  <li>the execution model itself,</li>
  <li>the language-level safe-observation and safe-debug-stop semantics themselves,</li>
  <li>probe behavior,</li>
  <li>watch-list behavior,</li>
  <li>reverse execution,</li>
  <li>timeline scrubbing,</li>
  <li>deterministic replay,</li>
  <li>performance profiling,</li>
  <li>deep value-serialization formats.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">4. Relation with Other Specifications</h2>

<p>
This document depends on the following specifications:
</p>

<ul>
  <li><code>IDE/Readme.md</code> for the IDE-facing separation between authoring, source identity, execution integration, and interactive tooling,</li>
  <li><code>IDE/Execution observability.md</code> for the source-aligned observability projection on which interactive debugging builds,</li>
  <li><code>IDE/Probes.md</code> for source-aligned probe behavior that may be consumed together with debugging,</li>
  <li><code>IDE/Watch.md</code> for persistent watch behavior that may be consumed together with debugging,</li>
  <li><code>Expression/Diagram.md</code> for the canonical node, edge, and executable-graph model,</li>
  <li><code>Expression/Control structures.md</code> for the canonical source-facing representation of structure kinds, regions, boundaries, and terminals,</li>
  <li><code>Expression/State and cycles.md</code> for the canonical source-facing representation of local-memory constructs and cycle-facing source constraints,</li>
  <li><code>Expression/Widget interaction.md</code> for widget-related execution objects and explicit UI sequencing,</li>
  <li><code>Language/Execution model.md</code> for live execution instance, source identity, activation, execution context, and committed source-level state,</li>
  <li><code>Language/Execution control and observation boundaries.md</code> for safe observation points, pause-consistent snapshots, safe debug stops, and terminal boundary semantics,</li>
  <li><code>Language/Control structures.md</code> for the normative execution semantics of structures,</li>
  <li><code>Language/State and cycles.md</code> for the normative execution semantics of local memory and valid feedback behavior,</li>
  <li><code>Libraries/UI.md</code> for standardized executable widget-interaction primitives.</li>
</ul>

<p>
This document MUST NOT contradict those specifications.
If a conflict appears:
</p>

<ul>
  <li><code>Expression/</code> remains authoritative for canonical source identity and source-visible representation,</li>
  <li><code>Language/</code> remains authoritative for normative execution semantics and execution-safe boundaries,</li>
  <li><code>Libraries/</code> remain authoritative for primitive identity and primitive-local behavior,</li>
  <li><code>IDE/</code> remains authoritative only for debugging behavior, debugger-facing objects, and IDE-facing control meaning.</li>
</ul>

<hr/>

<h2 id="design-principles">5. Design Principles</h2>

<h3>5.1 Source-level debugging</h3>

<p>
Debugging MUST be expressed in terms of source-level concepts visible to the user:
nodes, edges, structures, regions, sub-FROG calls, and widget-related nodes.
It MUST NOT require the user to understand runtime-only artifacts.
</p>

<h3>5.2 Dataflow-first behavior</h3>

<p>
FROG debugging MUST respect dataflow semantics.
It MUST NOT assume that the program has an implicit sequential instruction order.
Debugging controls therefore operate on observable execution activity in the dataflow graph.
</p>

<h3>5.3 Language-derived safe boundaries</h3>

<p>
A debug pause MUST occur only at a language-valid safe debug stop.
The IDE MUST NOT expose a partially committed source-level state as if it were stable.
This document consumes that guarantee; it does not define it.
</p>

<h3>5.4 Runtime independence</h3>

<p>
Different runtimes MAY implement debugging through different internal mechanisms.
The observable source-level meaning of debugging controls MUST remain equivalent.
</p>

<h3>5.5 Capability profiles and debugging support levels remain distinct</h3>

<p>
The repository uses <code>Profiles/</code> for optional standardized capability families.
This document also needs to talk about stronger or weaker debugging support.
Those are different concerns.
</p>

<ul>
  <li>a capability profile defines what executable capability families exist,</li>
  <li>a debugging support level defines how much interactive debugging behavior is available for those capabilities.</li>
</ul>

<h3>5.6 Minimal but extensible</h3>

<p>
FROG v0.1 defines a minimal debugging core.
Stricter debugging support levels MAY expose richer control, finer-grained pause reasons, conditional breakpoints, or deeper inspection capabilities, provided that the v0.1 debugging meanings remain preserved.
</p>

<hr/>

<h2 id="debugging-model">6. Debugging Model</h2>

<p>
Interactive debugging in FROG is defined over a <strong>live execution instance</strong>.
A live execution instance is defined at the language level.
A debugging-capable runtime MUST allow the IDE to observe and control such an instance in a source-aligned way.
</p>

<p>
At minimum, a debugging-capable execution instance supports, through the IDE-facing debugging layer:
</p>

<ul>
  <li>starting under debug control,</li>
  <li>pausing at language-valid safe debug stops,</li>
  <li>resuming execution,</li>
  <li>aborting execution under user control,</li>
  <li>source-level breakpoint activation,</li>
  <li>single-step commands,</li>
  <li>fault-directed pause when debugging is active and the active debugging support level provides it.</li>
</ul>

<p>
A runtime MAY also support attaching a debugger to an already-running instance, but that capability is optional in v0.1.
</p>

<hr/>

<h2 id="debug-session">7. Debug Session</h2>

<h3>7.1 Definition</h3>

<p>
A <strong>debug session</strong> is the IDE-visible control context attached to one live execution instance.
A debug session owns the active debugging configuration for that instance.
</p>

<p>
A debug session conceptually contains:
</p>

<ul>
  <li>the target <code>instance_id</code>,</li>
  <li>the current debug-session state,</li>
  <li>the projected execution state of the underlying instance,</li>
  <li>the active breakpoint set,</li>
  <li>the last pause reason,</li>
  <li>the last selected source object,</li>
  <li>the active stepping request if any.</li>
</ul>

<h3>7.2 Debug-session states</h3>

<p>
A debug session MUST expose one of the following high-level states:
</p>

<ul>
  <li><code>idle</code> — no live execution instance is attached,</li>
  <li><code>starting</code> — the instance is being prepared under debug control,</li>
  <li><code>running</code> — the instance is executing freely under an active debug session,</li>
  <li><code>paused</code> — the instance is suspended at a language-valid safe debug stop,</li>
  <li><code>completed</code> — the attached instance finished normally,</li>
  <li><code>faulted</code> — the attached instance terminated because of an execution fault without remaining paused,</li>
  <li><code>aborted</code> — the attached instance was terminated by user abort or an equivalent external stop action.</li>
</ul>

<p>
These are debugger-facing session states.
They MUST NOT be confused with any additional IDE-local transport, attachment, or view-management states.
</p>

<h3>7.3 Pause reasons</h3>

<p>
When a debug session enters the <code>paused</code> state, the IDE SHOULD know the primary pause reason.
Canonical pause reasons for v0.1 are:
</p>

<ul>
  <li><code>manual_pause</code>,</li>
  <li><code>breakpoint</code>,</li>
  <li><code>step_complete</code>,</li>
  <li><code>fault</code>.</li>
</ul>

<p>
A stricter debugging support level MAY expose additional pause reasons.
Additional reasons MUST NOT contradict the meanings above.
</p>

<h3>7.4 Selected source object</h3>

<p>
When a debug session is paused, the IDE SHOULD identify one primary selected source object associated with the stop.
That object MAY be:
</p>

<ul>
  <li>a node,</li>
  <li>an edge,</li>
  <li>a structure,</li>
  <li>a structure region,</li>
  <li>a sub-FROG call site,</li>
  <li>another source-aligned object supported by the active debugging support level.</li>
</ul>

<p>
The selected object is a debugger-facing focus object.
It does not replace full execution context.
</p>

<hr/>

<h2 id="execution-highlighting">8. Execution Highlighting</h2>

<h3>8.1 General rule</h3>

<p>
A FROG IDE SHOULD support execution highlighting during debugging.
Execution highlighting is the source-level visual projection of live execution activity onto the diagram.
</p>

<h3>8.2 Highlightable objects</h3>

<p>
A debugging-capable IDE SHOULD be able to highlight at least:
</p>

<ul>
  <li>node execution start,</li>
  <li>node execution completion,</li>
  <li>edge-level value availability,</li>
  <li>structure entry,</li>
  <li>selected case regions,</li>
  <li>loop-iteration progression.</li>
</ul>

<p>
If the active observability support level exposes readiness, the IDE SHOULD also be able to highlight node readiness or an equivalent ready-to-run state.
</p>

<h3>8.3 Meaning of highlighting</h3>

<p>
Highlighting is descriptive, not prescriptive.
It visualizes source-level execution activity.
It MUST NOT change execution meaning.
</p>

<h3>8.4 No mandatory rendering style</h3>

<p>
This document does not require a specific animation style, color model, line thickness, or visual theme.
An IDE MAY choose any rendering strategy, provided that the displayed meaning remains source-aligned and understandable.
</p>

<hr/>

<h2 id="pause-and-resume-model">9. Pause and Resume Model</h2>

<h3>9.1 Manual pause</h3>

<p>
A manual pause request asks the runtime to suspend the live execution instance at the next language-valid safe debug stop.
The exact definition of a safe debug stop belongs to <code>Language/Execution control and observation boundaries.md</code>.
</p>

<p>
When the instance becomes paused, the IDE-facing debug view MUST be interpretable as a pause-consistent snapshot.
The debugger MUST therefore be able to rely on the following:
</p>

<ul>
  <li>already-projected node completion is committed,</li>
  <li>already-projected edge values are committed,</li>
  <li>already-projected local-memory updates are committed,</li>
  <li>the active structure and region context is consistent,</li>
  <li>the debugger-visible state is a coherent causal prefix.</li>
</ul>

<h3>9.2 Resume</h3>

<p>
A resume request restarts execution from the current paused state.
Unless a stepping command is active, execution continues freely until:
</p>

<ul>
  <li>a breakpoint is hit,</li>
  <li>a fault occurs,</li>
  <li>the user pauses manually,</li>
  <li>the instance completes normally,</li>
  <li>the instance is aborted.</li>
</ul>

<h3>9.3 User stop and abort</h3>

<p>
A user-facing stop action terminates the live execution instance.
At the execution-facing and debug-session-facing level, that termination MUST be represented consistently with the instance becoming <code>aborted</code>, unless a stricter runtime support level defines an explicitly different but equivalent user-stop outcome.
</p>

<h3>9.4 Pause visibility and inspection</h3>

<p>
While paused, the IDE MAY expose:
</p>

<ul>
  <li>the selected source object,</li>
  <li>the current execution context,</li>
  <li>relevant committed edge values,</li>
  <li>relevant committed local-memory state,</li>
  <li>probe and watch views defined elsewhere.</li>
</ul>

<p>
All such inspection MUST remain consistent with the committed source-level state exposed by the active observability support level.
</p>

<hr/>

<h2 id="breakpoints">10. Breakpoints</h2>

<h3>10.1 General model</h3>

<p>
A breakpoint is a debugger-facing stop condition attached to a source-visible execution object.
When the breakpoint condition is satisfied, the live execution instance MUST enter the <code>paused</code> state at a language-valid safe debug stop corresponding to that breakpoint hit.
</p>

<h3>10.2 Canonical breakpoint kinds for v0.1</h3>

<p>
The canonical breakpoint kinds for FROG v0.1 are:
</p>

<ul>
  <li><code>node_breakpoint</code>,</li>
  <li><code>edge_breakpoint</code>,</li>
  <li><code>structure_breakpoint</code>,</li>
  <li><code>subfrog_breakpoint</code>.</li>
</ul>

<h3>10.3 Node breakpoint</h3>

<p>
A node breakpoint is attached to one source node.
By default, it breaks when an activation of that node reaches its debugger-defined break condition.
For v0.1, the canonical node-break condition is:
</p>

<ul>
  <li><code>on_start</code></li>
</ul>

<p>
A stricter debugging support level MAY additionally support:
</p>

<ul>
  <li><code>on_ready</code>,</li>
  <li><code>on_complete</code>,</li>
  <li><code>on_fault</code>.</li>
</ul>

<p>
When <code>on_ready</code> is supported, it requires an observability support level that exposes readiness in a source-aligned way.
</p>

<h3>10.4 Edge breakpoint</h3>

<p>
An edge breakpoint is attached to one source edge.
It breaks when a value becomes available on that edge in the current execution context.
This is the dataflow analogue of breaking on wire-level data arrival.
</p>

<h3>10.5 Structure breakpoint</h3>

<p>
A structure breakpoint is attached to one structure node.
For v0.1, its canonical meaning is:
</p>

<ul>
  <li>break when the structure activation begins.</li>
</ul>

<p>
A stricter debugging support level MAY support region-selection or iteration-specific structure breakpoint conditions.
</p>

<h3>10.6 Sub-FROG breakpoint</h3>

<p>
A sub-FROG breakpoint is attached to a <code>subfrog</code> call site.
For v0.1, its canonical meaning is:
</p>

<ul>
  <li>break when the call-site activation begins.</li>
</ul>

<h3>10.7 Enabled and disabled breakpoints</h3>

<p>
A breakpoint MAY be enabled or disabled without being removed.
A disabled breakpoint MUST have no effect on execution.
</p>

<h3>10.8 Multiple simultaneous breakpoint hits</h3>

<p>
If multiple breakpoints become satisfied at the same safe debug stop, the runtime MAY report one primary breakpoint reason and include the others as additional matched breakpoints.
The IDE MUST NOT present contradictory source state.
</p>

<hr/>

<h2 id="single-stepping-model">11. Single-Stepping Model</h2>

<h3>11.1 General rule</h3>

<p>
Single-stepping in FROG is defined over observable source-level execution activity rather than over a linear instruction stream.
A step command resumes execution in a constrained way until the next debugger-relevant stop condition is met.
</p>

<h3>11.2 Canonical step commands for v0.1</h3>

<p>
The canonical step commands for FROG v0.1 are:
</p>

<ul>
  <li><code>step_into</code>,</li>
  <li><code>step_over</code>,</li>
  <li><code>step_out</code>.</li>
</ul>

<h3>11.3 <code>step_into</code></h3>

<p>
<code>step_into</code> resumes execution until the next debuggable source-level activation or event that belongs to the current causally reachable execution path.
When the current paused object is a sub-FROG call or a structure activation, <code>step_into</code> MAY stop inside that nested execution context.
</p>

<h3>11.4 <code>step_over</code></h3>

<p>
<code>step_over</code> treats the current selected source-level activation as one debugger-facing unit.
If the current paused object is:
</p>

<ul>
  <li>an ordinary primitive activation, <code>step_over</code> behaves like <code>step_into</code>,</li>
  <li>a sub-FROG call-site activation, <code>step_over</code> runs through the nested sub-FROG activity and stops at the next debuggable stop in the caller scope,</li>
  <li>a structure activation, <code>step_over</code> runs through the selected structure activity and stops at the next debuggable stop after that structure activation completes in the current parent scope.</li>
</ul>

<h3>11.5 <code>step_out</code></h3>

<p>
<code>step_out</code> is valid only when the current paused location is inside a nested debug scope such as:
</p>

<ul>
  <li>a sub-FROG body reached through a call site,</li>
  <li>a structure-owned region,</li>
  <li>a nested dynamic execution scope supported by the active debugging support level.</li>
</ul>

<p>
<code>step_out</code> resumes execution until the current nested scope completes, then pauses at the next debuggable stop in the immediate parent scope.
If no parent debug scope exists, <code>step_out</code> MAY behave like <code>resume</code> or MAY be rejected by the IDE as unavailable.
</p>

<h3>11.6 Step completion</h3>

<p>
When a step command succeeds, the resulting pause reason SHOULD be:
</p>

<ul>
  <li><code>step_complete</code>.</li>
</ul>

<p>
If a breakpoint is hit before the intended step target is reached, the pause reason MAY remain <code>breakpoint</code>.
If a fault-directed pause occurs, the pause reason MUST be <code>fault</code>.
</p>

<hr/>

<h2 id="sub-frog-and-structure-stepping">12. Sub-FROG and Structure Stepping</h2>

<h3>12.1 Sub-FROG calls</h3>

<p>
A <code>subfrog</code> node creates a source-level nested execution scope for debugging purposes.
Therefore:
</p>

<ul>
  <li><code>step_into</code> MAY enter the nested sub-FROG execution,</li>
  <li><code>step_over</code> MUST treat the sub-FROG invocation as one caller-visible unit,</li>
  <li><code>step_out</code> from inside the sub-FROG MUST return to the caller scope.</li>
</ul>

<h3>12.2 Case structures</h3>

<p>
For a <code>case</code> structure:
</p>

<ul>
  <li><code>step_into</code> MAY stop at the selected region entry or at the first debuggable activation inside the selected region,</li>
  <li><code>step_over</code> MUST execute the selected region and stop after the structure completes in the parent scope,</li>
  <li><code>step_out</code> from inside the selected region MUST continue until the structure completes and then stop in the parent scope.</li>
</ul>

<p>
Inactive case regions MUST NOT produce stepping stops for that activation.
</p>

<h3>12.3 Loop structures</h3>

<p>
For loop structures, stepping operates on the currently active dynamic iteration context.
Loop-specific rules are defined in the next section.
</p>

<hr/>

<h2 id="loop-debugging-semantics">13. Loop Debugging Semantics</h2>

<h3>13.1 General rule</h3>

<p>
A loop body activation is debugged in an iteration-aware way.
The same source node MAY therefore appear repeatedly under different iteration contexts.
The IDE SHOULD preserve iteration identity while debugging.
</p>

<h3>13.2 <code>for_loop</code></h3>

<p>
For a <code>for_loop</code>:
</p>

<ul>
  <li><code>step_into</code> from the loop entry MAY pause at the first debuggable stop of the first active iteration,</li>
  <li><code>step_over</code> from the loop entry MUST run through all iterations of that loop activation and stop after loop completion in the parent scope,</li>
  <li><code>step_out</code> from inside the loop body MUST run until the current loop activation completes and then stop in the parent scope.</li>
</ul>

<p>
A stricter debugging support level MAY support iteration-specific debug commands, but those commands are not part of v0.1.
</p>

<h3>13.3 <code>while_loop</code></h3>

<p>
For a <code>while_loop</code>:
</p>

<ul>
  <li><code>step_into</code> from the loop entry MAY pause at the first debuggable stop of the first executed iteration,</li>
  <li><code>step_over</code> from the loop entry MUST run until that loop activation terminates normally, faults, or is aborted,</li>
  <li><code>step_out</code> from inside the loop body MUST run until the current loop activation terminates and then stop in the parent scope.</li>
</ul>

<p>
Because a <code>while_loop</code> may execute an unbounded number of iterations, an IDE SHOULD make it visually clear that <code>step_over</code> may run for an extended period.
This warning is advisory only and does not alter debugging semantics.
</p>

<h3>13.4 Local memory in loops</h3>

<p>
When local-memory primitives such as <code>frog.core.delay</code> are active inside a loop, debugging MUST preserve the source meaning of state across activations.
A paused debug view MUST NOT misrepresent the stored state for the current live execution instance.
</p>

<hr/>

<h2 id="fault-handling-during-debugging">14. Fault Handling During Debugging</h2>

<h3>14.1 General rule</h3>

<p>
If a fault occurs while debugging is active, the debug session SHOULD pause at the most relevant language-valid safe debug stop associated with that fault when the active debugging support level provides fault-directed pause.
The debug-session state MUST then become either:
</p>

<ul>
  <li><code>paused</code> with pause reason <code>fault</code>, or</li>
  <li><code>faulted</code> if the active debugging support level does not support fault-directed pause before termination.</li>
</ul>

<h3>14.2 Fault localization</h3>

<p>
When possible, the IDE SHOULD identify at least one primary source object related to the fault, such as:
</p>

<ul>
  <li>a node,</li>
  <li>a structure,</li>
  <li>a sub-FROG call site,</li>
  <li>a widget interaction node.</li>
</ul>

<h3>14.3 Consistency</h3>

<p>
Fault-directed pause MUST still obey language-level safe debug-stop rules.
The IDE MUST NOT show a contradictory partial state merely because the pause reason is <code>fault</code>.
</p>

<hr/>

<h2 id="front-panel-and-widget-debug-visibility">15. Front Panel and Widget Debug Visibility</h2>

<h3>15.1 Widget-related nodes</h3>

<p>
Widget participation in debugging occurs through the diagram-level node forms already defined by source:
</p>

<ul>
  <li><code>widget_value</code>,</li>
  <li><code>widget_reference</code>,</li>
  <li><code>frog.ui.property_read</code>,</li>
  <li><code>frog.ui.property_write</code>,</li>
  <li><code>frog.ui.method_invoke</code>.</li>
</ul>

<p>
These nodes are debuggable like other diagram nodes, subject to their source representation, execution semantics, library-defined primitive behavior, and explicit UI sequencing rules.
</p>

<h3>15.2 Front-panel reflection</h3>

<p>
A debugging-capable IDE MAY reflect debug state on the front panel when that reflection is source-meaningful.
Examples include:
</p>

<ul>
  <li>showing the current primary value of a widget,</li>
  <li>showing that a property write has occurred,</li>
  <li>showing the result of a property read,</li>
  <li>showing explicit UI-effect sequencing progress.</li>
</ul>

<p>
However, the front panel remains a user-facing UI composition, not the canonical executable graph.
Therefore, pause locations and step targets remain defined primarily in diagram terms.
</p>

<hr/>

<h2 id="ide-requirements">16. IDE Requirements</h2>

<p>
An IDE that claims support for FROG interactive debugging SHOULD provide at least:
</p>

<ul>
  <li>run under debug control,</li>
  <li>manual pause and resume,</li>
  <li>manual abort,</li>
  <li>execution highlighting,</li>
  <li>node breakpoints,</li>
  <li><code>step_into</code>,</li>
  <li><code>step_over</code>,</li>
  <li><code>step_out</code>,</li>
  <li>fault-directed source localization when supported by the active debugging support level.</li>
</ul>

<p>
An IDE MAY additionally provide:
</p>

<ul>
  <li>edge breakpoints,</li>
  <li>structure breakpoints,</li>
  <li>sub-FROG call breakpoints,</li>
  <li>readiness-aware overlays when the active observability support level exposes readiness,</li>
  <li>front-panel debug reflection,</li>
  <li>execution traces,</li>
  <li>probe integrations defined by <code>IDE/Probes.md</code>,</li>
  <li>watch integrations defined by <code>IDE/Watch.md</code>.</li>
</ul>

<p>
The user-interface design is not standardized here.
Only the source-level meaning of the debugging controls is standardized here.
</p>

<hr/>

<h2 id="illustrative-debug-objects">17. Illustrative Debug Objects</h2>

<p>
The following examples are illustrative only.
They show one possible structured representation of debugger-facing objects.
They are not a required transport format.
</p>

<h3>17.1 Node breakpoint</h3>

<pre><code>{
  "kind": "node_breakpoint",
  "enabled": true,
  "target": {
    "kind": "node",
    "id": "add_1"
  },
  "condition": "on_start"
}</code></pre>

<h3>17.2 Edge breakpoint</h3>

<pre><code>{
  "kind": "edge_breakpoint",
  "enabled": true,
  "target": {
    "kind": "edge",
    "id": "e_sum"
  }
}</code></pre>

<h3>17.3 Paused debug snapshot</h3>

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

<h3>17.4 Fault-directed pause</h3>

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

<h2 id="out-of-scope-for-v01">18. Out of Scope for v0.1</h2>

<p>
The following topics are intentionally out of scope for this document:
</p>

<ul>
  <li>execution-model ownership,</li>
  <li>safe-debug-stop semantic ownership,</li>
  <li>probe behavior,</li>
  <li>watch-list behavior and watch expressions,</li>
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

<p>
Those topics MAY be defined later in separate IDE-facing or runtime-facing specifications.
</p>

<hr/>

<h2 id="summary">19. Summary</h2>

<p>
FROG interactive debugging defines the IDE-facing meaning of pause, resume, breakpoints, and stepping for live executions of FROG programs.
It preserves the dataflow nature of the language and avoids imposing a false sequential execution model.
</p>

<p>
For FROG v0.1, this specification standardizes:
</p>

<ul>
  <li>debug sessions,</li>
  <li>execution highlighting,</li>
  <li>debugger-facing pause and resume behavior,</li>
  <li>canonical breakpoint kinds,</li>
  <li><code>step_into</code>,</li>
  <li><code>step_over</code>,</li>
  <li><code>step_out</code>,</li>
  <li>fault-directed source localization and pause behavior when supported.</li>
</ul>

<p>
This debugging layer provides the foundation for probes, watches, richer instrumentation, and advanced debugging support levels without confusing IDE-facing control with normative language or primitive semantics.
</p>

<hr/>

<h2 id="license">20. License</h2>

<p>
This specification is part of the FROG repository and is governed by the repository license and contribution rules.
</p>
