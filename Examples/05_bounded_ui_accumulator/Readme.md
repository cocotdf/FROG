<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Example 05 — Bounded UI Accumulator</h1>

<p align="center">
  <strong>First complete applicative vertical-slice anchor combining front-panel value participation, bounded structured control, explicit state, minimal object-style UI access, and a first executable corridor</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#purpose-of-this-example">2. Purpose of this Example</a></li>
  <li><a href="#behavioral-model">3. Behavioral Model</a></li>
  <li><a href="#constructs-used">4. Constructs Used</a></li>
  <li><a href="#source-shape">5. Source Shape</a></li>
  <li><a href="#front-panel-posture">6. Front-Panel Posture</a></li>
  <li><a href="#structured-control-posture">7. Structured-Control Posture</a></li>
  <li><a href="#explicit-state-posture">8. Explicit-State Posture</a></li>
  <li><a href="#validation-expectation">9. Validation Expectation</a></li>
  <li><a href="#derivation-expectation">10. Derivation Expectation</a></li>
  <li><a href="#lowering-expectation">11. Lowering Expectation</a></li>
  <li><a href="#published-backend-contract">12. Published Backend Contract</a></li>
  <li><a href="#published-reference-consumers">13. Published Reference Consumers</a></li>
  <li><a href="#reference-runtime-expectation">14. Reference Runtime Expectation</a></li>
  <li><a href="#why-this-example-matters">15. Why This Example Matters</a></li>
  <li><a href="#summary">16. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This example is the first intentionally small but complete applicative vertical-slice anchor for the published FROG repository.
It combines in one coherent corridor:
</p>

<ul>
  <li>one <code>u16</code> numeric front-panel control,</li>
  <li>one <code>u16</code> numeric front-panel indicator,</li>
  <li>one bounded <code>for_loop</code> structure with exactly five iterations,</li>
  <li>one explicit state initialized to zero,</li>
  <li>one accumulation behavior that adds the control value to the current state on each iteration,</li>
  <li>one final observable result,</li>
  <li>one public output,</li>
  <li>one minimal object-style UI interaction path for <code>face_color</code>,</li>
  <li>one persisted front-face template reference through <code>face_template</code>,</li>
  <li>and one source-to-execution reading that remains explicit across validation, IR derivation, lowering, backend handoff, and first reference execution.</li>
</ul>

<p>
This example is intentionally conservative.
It is not intended to demonstrate rich widget classes, advanced events, or broad runtime ambition.
It exists to close one small but credible end-to-end executable corridor without architectural cheating.
</p>

<hr/>

<h2 id="purpose-of-this-example">2. Purpose of this Example</h2>

<p>
The purpose of this example is to provide one named repository-visible slice that simultaneously exercises:
</p>

<ul>
  <li>optional <code>front_panel</code> serialization,</li>
  <li>natural <code>widget_value</code> participation,</li>
  <li>minimal <code>widget_reference</code>-based object access,</li>
  <li>bounded structured control,</li>
  <li>explicit local memory,</li>
  <li>public output exposure,</li>
  <li>Execution IR preservation of loop, state, and UI-participation meaning,</li>
  <li>lowering into a backend-facing contract,</li>
  <li>and one first minimal runtime path that can actually execute the slice.</li>
</ul>

<p>
This example is the first intended bridge between the currently separated example families for:
</p>

<ul>
  <li>UI value participation,</li>
  <li>minimal object-style UI access,</li>
  <li>structured control,</li>
  <li>and explicit state.</li>
</ul>

<hr/>

<h2 id="behavioral-model">3. Behavioral Model</h2>

<p>
The example defines the following conservative behavior:
</p>

<ul>
  <li>the numeric control provides one input value <code>x</code> of type <code>u16</code>,</li>
  <li>the explicit state is initialized to <code>0</code>,</li>
  <li>the loop runs exactly <code>5</code> iterations,</li>
  <li>on each iteration, the next state is computed as <code>state_next = state_current + x</code>,</li>
  <li>after the fifth iteration, the final state is exposed as the program result,</li>
  <li>the numeric indicator displays that final result,</li>
  <li>one public output exposes the same final value,</li>
  <li>and the control and indicator front-face colors are also written through explicit object-style property access.</li>
</ul>

<p>
Equivalent mathematical reading:
</p>

<pre><code>input  = x
state0 = 0

repeat 5 times:
    state = state + x

result = state
</code></pre>

<p>
This mathematical reading is informative only.
The normative reading of this example remains the explicit loop-and-state execution model, not an algebraic shortcut such as “multiply by five.”
</p>

<hr/>

<h2 id="constructs-used">4. Constructs Used</h2>

<p>
This example uses the following constructs:
</p>

<ul>
  <li>one optional <code>front_panel</code> section,</li>
  <li>one value-carrying widget of class <code>frog.ui.standard.numeric_control</code>,</li>
  <li>one value-carrying widget of class <code>frog.ui.standard.numeric_indicator</code>,</li>
  <li>one public output in <code>interface.outputs</code>,</li>
  <li>one diagram-side <code>widget_value</code> node for the control,</li>
  <li>one diagram-side <code>widget_value</code> node for the indicator,</li>
  <li>two diagram-side <code>widget_reference</code> nodes used for minimal object-style property access,</li>
  <li>two <code>frog.ui.property_write</code> primitives targeting <code>face_color</code>,</li>
  <li>one bounded structured-control node represented canonically as <code>kind: "structure"</code> and <code>structure_type: "for_loop"</code>,</li>
  <li>one explicit local-memory primitive of type <code>frog.core.delay</code> with deterministic initialization,</li>
  <li>one arithmetic primitive of type <code>frog.core.add</code>,</li>
  <li>one diagram-side <code>interface_output</code> node,</li>
  <li>and the directed edges required to keep loop, state, UI participation, object-style access, and public exposure explicit.</li>
</ul>

<p>
The carried program values in this example use the canonical FROG value type <code>u16</code>.
The bounded loop count is fixed to five for this named slice and is expressed through the canonical <code>count</code> structure terminal.
</p>

<hr/>

<h2 id="source-shape">5. Source Shape</h2>

<p>
The source contains:
</p>

<ul>
  <li>a canonical metadata section,</li>
  <li>an interface with one public output,</li>
  <li>a front panel with one numeric control and one numeric indicator,</li>
  <li>source-owned front-face metadata through <code>face_color</code> and <code>face_template</code>,</li>
  <li>and an authoritative executable diagram containing widget-value participation, widget-reference participation, one bounded loop, one explicit local-memory element, and one final observable result path.</li>
</ul>

<p>
Conceptually:
</p>

<pre><code>front_panel:
  ctrl_input   : numeric_control(u16)
  ind_result   : numeric_indicator(u16)

  ctrl_input.props.face_color    = "#D0D0D0"
  ctrl_input.props.face_template = resource(svg, "./assets/widgets/u16_numeric_control_face.svg")

  ind_result.props.face_color    = "#D8E6FF"
  ind_result.props.face_template = resource(svg, "./assets/widgets/u16_numeric_indicator_face.svg")

diagram:
  widget_value(ctrl_input)
           |
           v
  structure(for_loop, count = 5)
           |
           | body:
           |   boundary_input(input_value) --------\
           |                                        +--- frog.core.add --- state_next
           |   frog.core.delay(out) ---------------/
           |   boundary_input(initial_state) --> frog.core.delay(initial)
           |   state_next -----------------------> frog.core.delay(in)
           |   state_next -----------------------> boundary_output(final_value)
           |
           v
  final_value -------------------------> widget_value(ind_result)
           |
           +---------------------------> interface_output(result)

  widget_reference(ctrl_input) --> frog.ui.property_write(member = "face_color")
  widget_reference(ind_result) --> frog.ui.property_write(member = "face_color")
</code></pre>

<p>
This example preserves the required ownership boundaries:
</p>

<ul>
  <li>the front panel owns widget declaration and presentation metadata,</li>
  <li>the interface owns the public contract,</li>
  <li>the diagram owns executable participation,</li>
  <li>the loop remains explicit,</li>
  <li>the state remains explicit,</li>
  <li>the object-style UI path remains explicit,</li>
  <li>and the final observable value remains attributable.</li>
</ul>

<hr/>

<h2 id="front-panel-posture">6. Front-Panel Posture</h2>

<p>
The front panel is present because this slice is intended to demonstrate that a bounded executable corridor can include an operational user-facing value path and a minimal object-style UI path without forcing the full rich widget ecosystem first.
</p>

<p>
The control widget contributes one natural value into the executable graph through <code>widget_value</code>.
The indicator widget receives one natural value from the executable graph through <code>widget_value</code>.
</p>

<p>
This example also introduces one deliberately small object-style surface:
</p>

<ul>
  <li><code>widget_reference</code> to the control,</li>
  <li><code>widget_reference</code> to the indicator,</li>
  <li><code>frog.ui.property_write</code> on member <code>face_color</code>.</li>
</ul>

<p>
This example therefore demonstrates both canonical widget interaction paths:
</p>

<ul>
  <li>natural value participation through <code>widget_value</code>,</li>
  <li>explicit object-style access through <code>widget_reference</code> and <code>frog.ui.property_write</code>.</li>
</ul>

<p>
The front panel also persists <code>face_template</code> for both widgets.
That metadata is source-owned presentation data.
It does not by itself define executable semantics.
</p>

<hr/>

<h2 id="structured-control-posture">7. Structured-Control Posture</h2>

<p>
The loop is represented as bounded structured control, not as an unrolled hidden expansion and not as scheduler-private repetition.
The loop count for this named example is exactly five.
</p>

<p>
The loop is represented canonically as:
</p>

<ul>
  <li><code>kind: "structure"</code>,</li>
  <li><code>structure_type: "for_loop"</code>,</li>
  <li>an explicit <code>count</code> terminal,</li>
  <li>an explicit boundary,</li>
  <li>one owned region with <code>id: "body"</code>.</li>
</ul>

<p>
The structured-control object must preserve at least:
</p>

<ul>
  <li>its identity as a loop-shaped execution region,</li>
  <li>its deterministic iteration count,</li>
  <li>its region boundary,</li>
  <li>its relation to explicit local memory,</li>
  <li>and its final-value exit toward both indicator display and public output.</li>
</ul>

<p>
This example therefore acts as the first small bridge between UI participation, object-style UI access, and structured control.
</p>

<hr/>

<h2 id="explicit-state-posture">8. Explicit-State Posture</h2>

<p>
The example contains one explicit state-carrying element.
That state is not inferred from repeated execution, not hidden in runtime-private persistence, and not silently repaired by a scheduler.
</p>

<p>
The explicit state remains attributable across the corridor through:
</p>

<ul>
  <li>one explicit local-memory primitive,</li>
  <li>one deterministic initial value of <code>0</code>,</li>
  <li>one feedback path that is valid only because local memory is explicit,</li>
  <li>and one state evolution rule that is visible in the executable region.</li>
</ul>

<p>
The state reading remains:
</p>

<pre><code>state_next = state_current + control_value
</code></pre>

<p>
No conforming reading of this example may replace that stateful execution meaning with hidden persistence or implicit recurrence repair.
</p>

<hr/>

<h2 id="validation-expectation">9. Validation Expectation</h2>

<p>
This example is expected to validate successfully in the first conservative executable corridor of FROG v0.1.
</p>

<p>
A conforming validator should confirm at least that:
</p>

<ul>
  <li>the <code>front_panel</code> section is structurally valid,</li>
  <li>widget identifiers are unique,</li>
  <li>the declared widget classes are valid standard numeric widget classes,</li>
  <li>the control and indicator are value-carrying widgets with compatible value type <code>u16</code>,</li>
  <li>the <code>face_color</code> values are structurally valid source-owned presentation properties,</li>
  <li>the <code>face_template</code> values are structurally valid source-owned template references under the active profile,</li>
  <li>the interface output is structurally valid,</li>
  <li>the <code>widget_value</code> nodes reference existing value-carrying widgets,</li>
  <li>the <code>widget_reference</code> nodes reference existing widgets,</li>
  <li>the <code>frog.ui.property_write</code> nodes target a class-supported member,</li>
  <li>the bounded loop node is structurally valid as canonical structured control,</li>
  <li>the loop count is deterministically defined as five for this example,</li>
  <li>the primitive reference <code>frog.core.add</code> is valid,</li>
  <li>the primitive reference <code>frog.core.delay</code> is valid,</li>
  <li>the delay node defines the required explicit initial value,</li>
  <li>the initial value is type-compatible with the carried state type,</li>
  <li>the feedback path is valid because it contains explicit local memory,</li>
  <li>the indicator receives the final loop result through a valid value path,</li>
  <li>the public output receives the same final result through a valid interface-output path,</li>
  <li>and the graph does not rely on hidden persistence, implicit state insertion, or scheduler-private semantic repair.</li>
</ul>

<hr/>

<h2 id="derivation-expectation">10. Derivation Expectation</h2>

<p>
Execution IR derivation should preserve the following distinctions explicitly:
</p>

<ul>
  <li>execution-unit identity for the whole program,</li>
  <li>widget-value participation for the numeric control,</li>
  <li>widget-value participation for the numeric indicator,</li>
  <li>widget-reference participation for both widgets,</li>
  <li>explicit property-write operations for <code>face_color</code>,</li>
  <li>structured-control identity for the bounded loop,</li>
  <li>region-bounded execution inside the loop,</li>
  <li>primitive execution identity for <code>frog.core.add</code>,</li>
  <li>explicit local-memory execution identity for <code>frog.core.delay</code>,</li>
  <li>the deterministic initial-state value <code>0</code>,</li>
  <li>the final result path to the numeric indicator,</li>
  <li>the final result path to the public output,</li>
  <li>and the validated dependencies that make the accumulation attributable.</li>
</ul>

<p>
The derived IR must not reinterpret this program as:
</p>

<ul>
  <li>a pure combinational graph,</li>
  <li>a UI-only data-binding artifact with no structured execution meaning,</li>
  <li>a loop erased into runtime-private repetition with no attributable region,</li>
  <li>a valid cycle repaired by hidden memory insertion,</li>
  <li>a presentation-only widget definition with no executable participation,</li>
  <li>or a pure multiply-by-five rewrite at the semantic ownership boundary.</li>
</ul>

<hr/>

<h2 id="lowering-expectation">11. Lowering Expectation</h2>

<p>
Lowering for this example should remain explicit about the difference between FROG Execution IR meaning and backend-family specialization.
</p>

<p>
A lowered form may specialize:
</p>

<ul>
  <li>the bounded loop into a backend-family loop construct or repeated block,</li>
  <li>the delay-backed state into explicit backend-family state storage,</li>
  <li>the widget-value paths into host-driven input sampling and output publication bindings,</li>
  <li>the widget-reference property writes into host-facing UI update operations,</li>
  <li>and the final observable result into one backend-facing result channel.</li>
</ul>

<p>
However, lowering must preserve that:
</p>

<ul>
  <li>the loop is bounded,</li>
  <li>the state is explicit,</li>
  <li>the initial value is deterministic,</li>
  <li>the control value participates as an input to the repeated computation,</li>
  <li>the indicator and public output receive the final post-loop value rather than one arbitrary intermediate value,</li>
  <li>and presentation metadata such as <code>face_template</code> does not become executable semantic law.</li>
</ul>

<hr/>

<h2 id="published-backend-contract">12. Published Backend Contract</h2>

<p>
This example is now paired with one repository-visible backend contract artifact for the first published reference runtime family:
</p>

<pre><code>Implementations/Reference/ContractEmitter/examples/
└── 05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json</code></pre>

<p>
That artifact is the published reference handoff surface for the first bounded executable corridor of this example.
It is downstream from canonical source, validation, semantic interpretation, Execution IR, and lowering.
It is upstream from runtime-private execution realization.
</p>

<p>
The published contract is expected to make explicit at least:
</p>

<ul>
  <li>that one consumable execution unit is being offered,</li>
  <li>that one bounded repeated computation of five iterations is required,</li>
  <li>that one explicit local state cell is required for correct meaning,</li>
  <li>that the state cell has deterministic initialization to <code>0</code>,</li>
  <li>that one host-provided numeric input value feeds the repeated computation,</li>
  <li>that one final numeric result is observable for public-output publication,</li>
  <li>that one final numeric result is observable for indicator publication,</li>
  <li>and that one minimal object-style UI write surface exists for <code>face_color</code>.</li>
</ul>

<p>
A backend family may choose its own private realization strategy, but it must not erase the public fact that this example depends on:
</p>

<ul>
  <li>bounded structured repetition,</li>
  <li>explicit local memory,</li>
  <li>front-panel value participation,</li>
  <li>and explicit object-style UI access.</li>
</ul>

<p>
This makes the corridor more explicit than a contract expectation described only in prose.
The artifact itself is now part of the repository-visible reading chain for this named slice.
</p>

<hr/>

<h2 id="published-reference-consumers">13. Published Reference Consumers</h2>

<p>
The first published downstream reference consumers for this contract live under:
</p>

<pre><code>Implementations/Reference/Runtime/</code></pre>

<p>
The bounded demonstration corridor is intended to be readable as:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/
      |
      v
Implementations/Reference/ContractEmitter/examples/
05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json
      |
      v
Implementations/Reference/Runtime/
      |
      +-- reference_runtime.py
      +-- run_slice05_contract.py
      \-- rust/
          \-- tests/
              +-- slice05_contract_smoke.rs
              \-- slice05_execution.rs</code></pre>

<p>
In that reading:
</p>

<ul>
  <li>the named example remains the source-level and corridor-level anchor,</li>
  <li>the emitted contract remains the backend handoff artifact,</li>
  <li>and the runtime surfaces remain downstream private consumers of that artifact.</li>
</ul>

<p>
This does not make the runtime normative.
It makes the first contract-to-runtime proof materially inspectable from the published repository itself.
</p>

<hr/>

<h2 id="reference-runtime-expectation">14. Reference Runtime Expectation</h2>

<p>
The first non-normative reference runtime path for this example may remain minimal and host-oriented.
</p>

<p>
A conservative execution reading is:
</p>

<ol>
  <li>load the published backend contract artifact for the selected runtime family,</li>
  <li>accept or reject the contract explicitly,</li>
  <li>prepare one host-side execution unit,</li>
  <li>read the current numeric control value once for the run,</li>
  <li>apply the two explicit <code>face_color</code> property writes,</li>
  <li>initialize the explicit state to <code>0</code>,</li>
  <li>execute five iterations of accumulation,</li>
  <li>publish the final result to the numeric indicator,</li>
  <li>publish the same final result to the public output observation surface,</li>
  <li>and report successful completion or explicit failure.</li>
</ol>

<p>
This runtime expectation does not require:
</p>

<ul>
  <li>continuous event-driven widget interaction,</li>
  <li>hidden persistence between runs,</li>
  <li>asynchronous UI-driven re-execution,</li>
  <li>advanced object-style widget behavior,</li>
  <li>or pixel-identical front-face rendering across hosts.</li>
</ul>

<p>
The first runtime corridor is therefore intentionally bounded: one sampled input value, one deterministic execution, a small explicit UI write surface, and one final observable output value.
</p>

<p>
Where the reference implementation publishes more than one runtime language realization, those runtimes remain parallel consumers of the same corridor rather than competing definitions of FROG.
</p>

<hr/>

<h2 id="why-this-example-matters">15. Why This Example Matters</h2>

<p>
A serious open graphical language cannot remain credible if UI participation, object-style widget access, structured control, explicit state, IR preservation, lowering, backend handoff, and executable runtime posture are only published as separate partial slices.
</p>

<p>
This example matters because it is the smallest applicative case that proves all of the following at once:
</p>

<ul>
  <li>the front panel is not decorative metadata,</li>
  <li>the diagram remains the authoritative executable graph,</li>
  <li>structured control can remain explicit,</li>
  <li>state can remain explicit,</li>
  <li>widget value participation can remain explicit,</li>
  <li>widget object participation can remain explicit,</li>
  <li>presentation metadata can be persisted without becoming hidden semantic law,</li>
  <li>IR can preserve meaning without collapsing into a runtime-private form,</li>
  <li>backend handoff can remain attributable,</li>
  <li>and a first minimal runtime corridor can execute the slice without redefining the language.</li>
</ul>

<p>
That is why this example is the preferred anchor for the first complete executable vertical slice.
</p>

<hr/>

<h2 id="summary">16. Summary</h2>

<p>
This example is the first complete small applicative corridor for the published FROG repository.
It combines:
</p>

<ul>
  <li>one <code>u16</code> numeric control,</li>
  <li>one <code>u16</code> numeric indicator,</li>
  <li>one bounded loop of five iterations,</li>
  <li>one explicit state initialized to zero,</li>
  <li>one final observable output,</li>
  <li>one minimal object-style UI write surface,</li>
  <li>and one source-to-execution reading that remains explicit across the published corridor.</li>
</ul>

<p>
It is now also paired with one repository-visible backend contract artifact and with published downstream reference consumers for that same bounded corridor.
Together, the named example, the published contract, and the published consumer surfaces make the first bounded executable corridor materially inspectable across source, contract, and runtime-consumption layers.
</p>

<p>
It should remain the primary named anchor for the first end-to-end executable-slice closure campaign.
</p>
