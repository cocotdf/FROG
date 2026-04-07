<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Reference Pipeline</h1>

<p align="center">
  <strong>First executable reference pipeline for the non-normative FROG reference implementation workspace</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#pipeline-goal">2. Pipeline Goal</a></li>
  <li><a href="#current-closure-target">3. Current Closure Target</a></li>
  <li><a href="#pipeline-stages">4. Pipeline Stages</a></li>
  <li><a href="#first-slice-coverage">5. First-Slice Coverage</a></li>
  <li><a href="#stage-contracts">6. Stage Contracts</a></li>
  <li><a href="#published-corridor-artifacts">7. Published Corridor Artifacts</a></li>
  <li><a href="#pseudo-code">8. Pseudo-Code</a></li>
  <li><a href="#error-handling">9. Error Handling</a></li>
  <li><a href="#ui-handling">10. UI Handling</a></li>
  <li><a href="#state-handling">11. State Handling</a></li>
  <li><a href="#multi-runtime-posture">12. Multi-Runtime Posture</a></li>
  <li><a href="#summary">13. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document sketches the first executable pipeline of the FROG reference implementation workspace.
It is intentionally small, stage-separated, and implementation-oriented.
Its purpose is to prove that the published specification layers are already strong enough to support one coherent bounded executable slice.
</p>

<p>
This pipeline is <strong>non-normative</strong>.
It does not redefine the language, the semantic layer, the Execution IR, the lowering boundary, or the backend-contract boundary.
It is a reference workspace path that consumes those published layers through explicit stages.
</p>

<hr/>

<h2 id="pipeline-goal">2. Pipeline Goal</h2>

<p>
The first pipeline goal is:
</p>

<pre><code>canonical source
  -&gt; validation
  -&gt; open Execution IR derivation
  -&gt; backend-family lowering
  -&gt; backend contract emission
  -&gt; reference runtime execution</code></pre>

<p>
A successful first corridor should be able to carry one published named example from canonical <code>.frog</code> source to a repository-visible backend contract artifact and then to a published reference runtime consumer,
without inventing hidden semantic repairs.
</p>

<hr/>

<h2 id="current-closure-target">3. Current Closure Target</h2>

<p>
The current closure target is the first bounded applicative vertical slice:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/</code></pre>

<p>
That slice is the current reference anchor because it visibly combines:
</p>

<ul>
  <li>front-panel value participation,</li>
  <li>minimal object-style UI access,</li>
  <li>bounded structured control,</li>
  <li>explicit local state,</li>
  <li>public output publication,</li>
  <li>a published backend contract artifact,</li>
  <li>and published downstream reference runtime consumers.</li>
</ul>

<p>
Accordingly, the first reference pipeline should now be read primarily as the pipeline that closes the corridor for <code>05_bounded_ui_accumulator</code>,
not as a vague sketch for an older pre-applicative example family only.
</p>

<hr/>

<h2 id="pipeline-stages">4. Pipeline Stages</h2>

<h3>4.1 Load</h3>

<p>
Read the canonical <code>.frog</code> file and decode it into a structured source intake form.
</p>

<h3>4.2 Validate</h3>

<p>
Check the selected supported subset against the published structural and semantic rules.
If validation fails, the pipeline stops.
</p>

<h3>4.3 Derive Execution IR</h3>

<p>
Derive an open execution-facing representation from validated program meaning.
Preserve attribution, explicit memory, structured control, widget-value participation, widget-reference participation, and declared public interface obligations.
</p>

<h3>4.4 Lower</h3>

<p>
Specialize the open Execution IR for one selected backend family.
Make family assumptions explicit without pretending that the lowered form is normative language truth.
</p>

<h3>4.5 Emit Backend Contract</h3>

<p>
Produce a backend contract artifact that declares consumable units, assumptions, preserved obligations, and unsupported features.
For the current corridor, that emitted artifact should be materially inspectable in the repository.
</p>

<h3>4.6 Run</h3>

<p>
Pass the emitted contract to the reference runtime family.
Accept or reject it explicitly.
If accepted, execute the contract privately while preserving declared obligations.
</p>

<hr/>

<h2 id="first-slice-coverage">5. First-Slice Coverage</h2>

<p>
For the current closure target, the first slice should cover the smallest sufficient surface required by <code>05_bounded_ui_accumulator</code>.
</p>

<p>
That surface includes at least:
</p>

<ul>
  <li><code>widget_value</code>,</li>
  <li><code>widget_reference</code>,</li>
  <li><code>frog.ui.property_write</code>,</li>
  <li><code>frog.core.add</code>,</li>
  <li><code>frog.core.delay</code>,</li>
  <li>bounded <code>for_loop</code> structured control,</li>
  <li>explicit public input participation,</li>
  <li>explicit public output publication.</li>
</ul>

<p>
This document intentionally does <strong>not</strong> treat broader UI interaction forms as required for the first closed corridor.
In particular, <code>frog.ui.property_read</code> and <code>frog.ui.method_invoke</code> are not required to claim closure for the current slice unless a published corridor later depends on them.
</p>

<hr/>

<h2 id="stage-contracts">6. Stage Contracts</h2>

<p>
Each stage should expose a small explicit contract:
</p>

<ul>
  <li><strong>Load</strong> returns structured source or load failure.</li>
  <li><strong>Validate</strong> returns validated meaning basis or validation failure.</li>
  <li><strong>Derive</strong> returns open Execution IR or derivation failure.</li>
  <li><strong>Lower</strong> returns a backend-family-specialized form or lowering failure.</li>
  <li><strong>Emit contract</strong> returns a backend contract artifact or emission failure.</li>
  <li><strong>Run</strong> returns runtime success or explicit runtime rejection/failure.</li>
</ul>

<p>
No stage should continue after a failed predecessor by silently inventing missing semantics.
</p>

<hr/>

<h2 id="published-corridor-artifacts">7. Published Corridor Artifacts</h2>

<p>
For the current bounded corridor, the repository-visible reading chain is:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/
      |
      v
Implementations/Reference/ContractEmitter/examples/
05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json
      |
      v
Implementations/Reference/Runtime/</code></pre>

<p>
This matters because the reference pipeline is no longer only a prose ambition.
For the first closed slice, the source anchor, backend contract artifact, and runtime-side consumers are all intended to be repository-visible.
</p>

<hr/>

<h2 id="pseudo-code">8. Pseudo-Code</h2>

<pre><code>function frogc_run(file_path, backend_family = "reference_host_runtime_ui_binding"):
    source = load_source(file_path)
    if source.is_error:
        return fail(stage = "load", error = source.error)

    validation = validate_source(source)
    if validation.is_error:
        return fail(stage = "validate", error = validation.error)

    validated_program = validation.value

    ir = derive_execution_ir(validated_program)
    if ir.is_error:
        return fail(stage = "derive-ir", error = ir.error)

    lowered = lower_for_backend_family(ir.value, backend_family)
    if lowered.is_error:
        return fail(stage = "lower", error = lowered.error)

    contract = emit_backend_contract(lowered.value, backend_family)
    if contract.is_error:
        return fail(stage = "emit-contract", error = contract.error)

    runtime = create_runtime_for_family(backend_family)
    if runtime.is_error:
        return fail(stage = "runtime-create", error = runtime.error)

    acceptance = runtime.accept_contract(contract.value)
    if acceptance.is_error:
        return fail(stage = "runtime-accept", error = acceptance.error)

    result = runtime.execute(
        contract.value,
        public_inputs = {
            "input_value": sampled_control_value
        }
    )
    if result.is_error:
        return fail(stage = "run", error = result.error)

    return success(
        source = source.summary,
        validation = validation.summary,
        ir = ir.summary,
        lowered = lowered.summary,
        contract = contract.summary,
        runtime = result.summary
    )</code></pre>

<p>
For the current slice, the conservative sampled input is one <code>u16</code> numeric control value.
The deterministic execution result is the final explicit state after five iterations.
</p>

<hr/>

<h2 id="error-handling">9. Error Handling</h2>

<p>
Every stage should fail explicitly and return:
</p>

<ul>
  <li>failed stage name,</li>
  <li>machine-readable error code,</li>
  <li>human-readable explanation,</li>
  <li>best available source-aligned anchor.</li>
</ul>

<p>
Typical rule:
</p>

<pre><code>invalid source
  -&gt; no derivation

invalid derivation basis
  -&gt; no lowering

unsupported lowered family requirement
  -&gt; no contract acceptance

runtime family mismatch
  -&gt; explicit rejection</code></pre>

<p>
No stage should convert rejection into silent fallback if the corridor claims explicit bounded support.
</p>

<hr/>

<h2 id="ui-handling">10. UI Handling</h2>

<p>
For the first reference family, UI handling should remain narrow and explicit.
</p>

<p>
The rule set for the current slice is:
</p>

<ul>
  <li><code>widget_value</code> lowers to runtime-visible value bindings,</li>
  <li><code>widget_reference</code> lowers to explicit widget-reference support in the emitted contract,</li>
  <li><code>frog.ui.property_write</code> lowers to explicit runtime-visible UI update obligations,</li>
  <li>the first bounded corridor only requires support for the member <code>face_color</code>,</li>
  <li>no first-class standardized event execution model is assumed.</li>
</ul>

<p>
This keeps the first pipeline aligned with the actual published applicative corridor instead of claiming a broader UI execution surface than the first closed slice really needs.
</p>

<hr/>

<h2 id="state-handling">11. State Handling</h2>

<p>
The first bounded corridor requires explicit state handling.
</p>

<p>
The rule set is:
</p>

<ul>
  <li>state must remain explicit,</li>
  <li>the explicit carrier for the current slice is <code>frog.core.delay</code>,</li>
  <li>the deterministic initial state is <code>0</code>,</li>
  <li>the state evolution rule remains visible as <code>state_next = state_current + input_value</code>,</li>
  <li>the runtime must not repair cycles through hidden persistence.</li>
</ul>

<p>
For the current slice, the carried program value domain is <code>u16</code>.
The reference pipeline should therefore remain coherent with a first bounded scalar surface that already includes <code>u16</code>.
</p>

<hr/>

<h2 id="multi-runtime-posture">12. Multi-Runtime Posture</h2>

<p>
The first closed corridor must remain compatible with more than one runtime realization.
</p>

<p>
That means:
</p>

<ul>
  <li>one emitted backend contract family,</li>
  <li>one named source slice,</li>
  <li>one bounded execution meaning,</li>
  <li>but multiple runtime consumers where the workspace publishes them.</li>
</ul>

<p>
For the current reference family, the intended posture is:
</p>

<ul>
  <li>a Python runtime consumer,</li>
  <li>a Rust runtime consumer,</li>
  <li>possibly later other consumers,</li>
  <li>all aligned on the same published contract obligations.</li>
</ul>

<hr/>

<h2 id="summary">13. Summary</h2>

<p>
This document defines the first executable reference pipeline for the non-normative FROG reference workspace.
Its immediate closure target is the bounded applicative slice <code>05_bounded_ui_accumulator</code>.
</p>

<p>
The pipeline is therefore no longer just:
</p>

<pre><code>source
  -&gt; validation
  -&gt; IR
  -&gt; lowering
  -&gt; contract
  -&gt; runtime</code></pre>

<p>
It is now also a materially inspectable repository-visible corridor through:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/
  -&gt; ContractEmitter/examples/...contract.json
  -&gt; Runtime/</code></pre>

<p>
That makes the first bounded reference corridor easier to inspect, easier to test, and harder to misread as implementation-only rhetoric.
</p>
