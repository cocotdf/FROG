<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">🐸 Reference Pipeline</h1>

<p align="center">
  First implementation pipeline sketch for the non-normative FROG reference implementation<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#pipeline-goal">2. Pipeline Goal</a></li>
  <li><a href="#pipeline-stages">3. Pipeline Stages</a></li>
  <li><a href="#first-slice-coverage">4. First-Slice Coverage</a></li>
  <li><a href="#stage-contracts">5. Stage Contracts</a></li>
  <li><a href="#pseudo-code">6. Pseudo-Code</a></li>
  <li><a href="#error-handling">7. Error Handling</a></li>
  <li><a href="#ui-handling">8. UI Handling</a></li>
  <li><a href="#state-handling">9. State Handling</a></li>
  <li><a href="#summary">10. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document sketches the first end-to-end pipeline of the FROG reference implementation.
It is intentionally small and implementation-oriented.
Its purpose is to prove that the published specification layers are already strong enough to support one coherent executable slice.
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
  -&gt; reference runtime execution
</code></pre>

<p>
A successful first slice should be able to process the initial example cases from start to finish without inventing hidden semantic repairs.
</p>

<hr/>

<h2 id="pipeline-stages">3. Pipeline Stages</h2>

<h3>3.1 Load</h3>

<p>
Read the canonical <code>.frog</code> file and decode it into a structured source intake form.
</p>

<h3>3.2 Validate</h3>

<p>
Check the selected MVP subset against the published rules.
If validation fails, the pipeline stops.
</p>

<h3>3.3 Derive Execution IR</h3>

<p>
Derive an open execution-facing representation from validated program meaning.
Preserve attribution, explicit memory, and required boundary distinctions.
</p>

<h3>3.4 Lower</h3>

<p>
Specialize the open Execution IR for one selected backend family.
Make family assumptions explicit without pretending that the lowered form is normative language truth.
</p>

<h3>3.5 Emit Backend Contract</h3>

<p>
Produce a backend contract artifact that declares consumable units, assumptions, preserved obligations, and unsupported features.
</p>

<h3>3.6 Run</h3>

<p>
Pass the emitted contract to the reference runtime family.
Accept or reject it explicitly.
If accepted, execute the contract privately while preserving declared obligations.
</p>

<hr/>

<h2 id="first-slice-coverage">4. First-Slice Coverage</h2>

<p>
The first slice should cover:
</p>

<ul>
  <li><code>interface_input</code></li>
  <li><code>interface_output</code></li>
  <li><code>primitive</code></li>
  <li><code>widget_value</code></li>
  <li><code>widget_reference</code></li>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
  <li><code>frog.core.delay</code></li>
</ul>

<p>
That is enough to support the four initial example cases already drafted in the repository.
</p>

<hr/>

<h2 id="stage-contracts">5. Stage Contracts</h2>

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

<h2 id="pseudo-code">6. Pseudo-Code</h2>

<pre><code class="language-text">function frogc_run(file_path, backend_family = "reference_host_runtime_ui_binding"):
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

    result = runtime.execute(contract.value)
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

<hr/>

<h2 id="error-handling">7. Error Handling</h2>

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
  -&gt; explicit rejection
</code></pre>

<hr/>

<h2 id="ui-handling">8. UI Handling</h2>

<p>
For the first reference family, UI handling should remain narrow and explicit.
</p>

<p>
Suggested rule set:
</p>

<ul>
  <li><code>widget_value</code> lowers to runtime-visible value bindings,</li>
  <li><code>widget_reference</code> lowers to widget handles or equivalent runtime-visible reference slots,</li>
  <li><code>frog.ui.property_*</code> and <code>frog.ui.method_invoke</code> lower to explicit runtime-visible UI operations,</li>
  <li>no first-class standardized event execution model is assumed.</li>
</ul>

<hr/>

<h2 id="state-handling">9. State Handling</h2>

<p>
Explicit local memory must remain explicit through the whole pipeline.
For the first slice:
</p>

<ul>
  <li><code>frog.core.delay</code> must validate only when <code>initial</code> is present,</li>
  <li>derivation must preserve the explicit state object,</li>
  <li>lowering may represent the state as read/commit style machinery,</li>
  <li>the backend contract must still declare explicit state semantics,</li>
  <li>the runtime must not replace that meaning with hidden semantic repair.</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The first FROG reference pipeline is a disciplined executable path through the already-published architecture:
load,
validate,
derive open Execution IR,
lower for one backend family,
emit a backend contract,
and run through one reference runtime family.
</p>

<p>
Its purpose is not to replace the specification.
Its purpose is to prove that the specification can already support one coherent executable slice.
</p>
