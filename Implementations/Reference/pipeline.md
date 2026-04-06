<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">FROG Reference Pipeline</h1>

<p align="center">
  <strong>Stage-separated reference pipeline for bounded executable FROG corridors</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#pipeline-goal">2. Pipeline Goal</a></li>
  <li><a href="#first-priority-slice">3. First Priority Slice</a></li>
  <li><a href="#pipeline-stages">4. Pipeline Stages</a></li>
  <li><a href="#first-slice-coverage">5. First-Slice Coverage</a></li>
  <li><a href="#stage-contracts">6. Stage Contracts</a></li>
  <li><a href="#pseudo-code">7. Pseudo-Code</a></li>
  <li><a href="#subset-honesty-rule">8. Subset Honesty Rule</a></li>
  <li><a href="#summary">9. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document describes the intended stage-separated pipeline of the FROG reference implementation workspace.
</p>

<p>
It is a consumer-side implementation document.
It does not redefine the normative ownership of:
</p>

<ul>
  <li>canonical source shape,</li>
  <li>validated semantic meaning,</li>
  <li>the canonical Execution IR,</li>
  <li>lowering law,</li>
  <li>or backend contract law.</li>
</ul>

<p>
Its purpose is to keep the reference implementation honest about which stage it is executing, which published surface it is consuming, and which bounded subset it actually supports today.
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
A successful first slice should be able to process a bounded published example from start to finish without inventing hidden semantic repairs.
</p>

<p>
The pipeline therefore exists to prove stage boundaries first.
It does not exist to hide those boundaries behind one monolithic execution shortcut.
</p>

<hr/>

<h2 id="first-priority-slice">3. First Priority Slice</h2>

<p>
For the current repository campaign, the first priority slice of this pipeline is a small but complete UI-bearing accumulation corridor.
</p>

<p>
That slice should demonstrate support for a bounded published subset including:
</p>

<ul>
  <li>one numeric control,</li>
  <li>one numeric indicator,</li>
  <li>bounded loop execution,</li>
  <li>explicit state through <code>frog.core.delay</code>,</li>
  <li>one final observable output,</li>
  <li>and the distinction between natural widget value participation and minimal object-style presentation-property interaction.</li>
</ul>

<p>
This first priority slice is intentionally small.
It proves corridor credibility before broader language coverage.
</p>

<hr/>

<h2 id="pipeline-stages">4. Pipeline Stages</h2>

<h3>4.1 Load</h3>

<p>
Read the canonical <code>.frog</code> file and decode it into a structured source intake form.
</p>

<h3>4.2 Validate</h3>

<p>
Check the selected supported subset against the published rules.
Validation MUST distinguish:
</p>

<ul>
  <li>load failure,</li>
  <li>structural invalidity,</li>
  <li>semantic rejection,</li>
  <li>unsupported-but-valid situations caused by a narrower implementation subset.</li>
</ul>

<p>
If validation fails, the pipeline stops.
</p>

<h3>4.3 Derive Execution IR</h3>

<p>
Derive an open execution-facing representation from validated program meaning.
Preserve attribution, explicit memory, boundary distinctions, and the distinction between semantic state and presentation-only metadata.
</p>

<h3>4.4 Lower</h3>

<p>
Specialize the open Execution IR for one selected backend family.
Make backend-family assumptions explicit without pretending that the lowered form is normative language truth.
</p>

<h3>4.5 Emit Backend Contract</h3>

<p>
Produce a backend contract artifact that declares consumable units, assumptions, preserved obligations, unsupported features, and relevant host/runtime requirements.
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
The first slice should cover only a bounded published subset.
At minimum, the current priority corridor should aim to support:
</p>

<ul>
  <li><code>interface_output</code>,</li>
  <li><code>primitive</code>,</li>
  <li><code>widget_value</code>,</li>
  <li><code>widget_reference</code>,</li>
  <li><code>frog.ui.property_write</code> for a minimal published presentation-property case,</li>
  <li><code>frog.core.delay</code>,</li>
  <li>bounded loop structure in the published supported form.</li>
</ul>

<p>
Support for other language surfaces MAY exist, but this pipeline document should treat them as additional coverage only when explicitly implemented and claimed.
</p>

<p>
The first slice MUST NOT pretend to cover the full open-ended widget model merely because the architectural contract model allows it.
</p>

<hr/>

<h2 id="stage-contracts">6. Stage Contracts</h2>

<p>
Each stage should expose a small explicit contract:
</p>

<ul>
  <li><strong>Load</strong> returns structured source or load failure.</li>
  <li><strong>Validate</strong> returns validated meaning basis, semantic rejection, structural rejection, or unsupported-but-valid status.</li>
  <li><strong>Derive</strong> returns open Execution IR or derivation failure.</li>
  <li><strong>Lower</strong> returns a backend-family-specialized form or lowering failure.</li>
  <li><strong>Emit contract</strong> returns a backend contract artifact or emission failure.</li>
  <li><strong>Run</strong> returns runtime success or explicit runtime rejection/failure.</li>
</ul>

<p>
No stage should continue after a failed predecessor by silently inventing missing semantics.
</p>

<hr/>

<h2 id="pseudo-code">7. Pseudo-Code</h2>

<pre><code>function frogc_run(file_path, backend_family = "reference_host_runtime_ui_binding"):
    source = load_source(file_path)
    if source.is_error:
        return fail(stage = "load", error = source.error)

    validation = validate_source(source)
    if validation.is_error:
        return fail(stage = "validate", error = validation.error)

    if validation.is_unsupported_but_valid:
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

    runtime = run_backend_contract(contract.value, backend_family)
    if runtime.is_error:
        return fail(stage = "run", error = runtime.error)

    return success(
        stage = "run",
        outputs = runtime.outputs,
        diagnostics = runtime.diagnostics
    )</code></pre>

<hr/>

<h2 id="subset-honesty-rule">8. Subset Honesty Rule</h2>

<p>
The reference pipeline MUST remain explicit about the difference between:
</p>

<ul>
  <li>the general extensible FROG model published by the repository,</li>
  <li>the specific published subset that this pipeline currently supports,</li>
  <li>and implementation-private conveniences used internally.</li>
</ul>

<p>
Accordingly:
</p>

<ul>
  <li>unsupported-but-valid situations SHOULD be reported explicitly,</li>
  <li>stage reports SHOULD identify which published slice is being exercised,</li>
  <li>the pipeline SHOULD avoid implying that all future widget families, profiles, or backend families are already supported,</li>
  <li>the first success condition remains one complete supported corridor, not maximal coverage.</li>
</ul>

<hr/>

<h2 id="summary">9. Summary</h2>

<p>
The reference pipeline is a stage-separated consumer path for bounded published FROG corridors.
</p>

<p>
Its current mission is to prove that one real published subset can travel through:
</p>

<ul>
  <li>source loading,</li>
  <li>validation,</li>
  <li>Execution IR derivation,</li>
  <li>lowering,</li>
  <li>backend contract emission,</li>
  <li>and runtime-side execution.</li>
</ul>

<p>
It must therefore stay:
</p>

<ul>
  <li>explicit about stage boundaries,</li>
  <li>explicit about supported subset boundaries,</li>
  <li>aligned with published examples and conformance,</li>
  <li>and explicit about the difference between the general extensible model and the corridor actually executed today.</li>
</ul>
