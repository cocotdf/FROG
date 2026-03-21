<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 frogc CLI</h1>

<p align="center">
  Initial command-line contract for the non-normative FROG reference implementation<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#status-and-boundary">2. Status and Boundary</a></li>
  <li><a href="#current-scope">3. Current Scope</a></li>
  <li><a href="#design-principles">4. Design Principles</a></li>
  <li><a href="#command-family">5. Command Family</a></li>
  <li><a href="#global-rules">6. Global Rules</a></li>
  <li><a href="#commands">7. Commands</a>
    <ul>
      <li><a href="#validate">7.1 validate</a></li>
      <li><a href="#derive-ir">7.2 derive-ir</a></li>
      <li><a href="#lower">7.3 lower</a></li>
      <li><a href="#emit-contract">7.4 emit-contract</a></li>
      <li><a href="#run">7.5 run</a></li>
    </ul>
  </li>
  <li><a href="#output-and-artifacts">8. Output and Artifacts</a></li>
  <li><a href="#diagnostics-and-exit-behavior">9. Diagnostics and Exit Behavior</a></li>
  <li><a href="#first-backend-family">10. First Backend Family</a></li>
  <li><a href="#examples">11. Examples</a></li>
  <li><a href="#non-goals">12. Non-Goals</a></li>
  <li><a href="#summary">13. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the initial command-line surface of the FROG reference implementation.
The CLI is intentionally stage-aware.
It mirrors the published reference pipeline rather than hiding all stages behind one opaque command.
</p>

<p>
The purpose of <code>frogc</code> is not to define the language.
Its purpose is to provide a practical shell around the first non-normative reference pipeline.
</p>

<pre><code>.frog source
      |
      v
validate
      |
      v
derive-ir
      |
      v
lower
      |
      v
emit-contract
      |
      v
run
</code></pre>

<hr/>

<h2 id="status-and-boundary">2. Status and Boundary</h2>

<p>
This CLI is a reference-implementation interface only.
It is <strong>not</strong> part of the normative language definition.
The command names, option surface, and artifact transport details may evolve,
but the visible stage separation should remain because it reflects already-published architectural boundaries.
</p>

<p>
The CLI must therefore remain a consumer of the published specification.
It must not become a hidden source of language truth.
</p>

<hr/>

<h2 id="current-scope">3. Current Scope</h2>

<p>
The current CLI scope is intentionally narrow.
Its first executable target is the published minimal slice:
</p>

<pre><code>Examples/01_pure_addition/main.frog</code></pre>

<p>
That slice proves the end-to-end path for:
</p>

<ul>
  <li>public interface input participation,</li>
  <li>public interface output participation,</li>
  <li>one ordinary primitive node,</li>
  <li><code>frog.core.add</code>,</li>
  <li>basic lowering and backend-contract emission,</li>
  <li>runtime-side execution of a minimal callable unit.</li>
</ul>

<p>
The CLI may expand later to additional published slices,
but this document describes the initial command family in a way that remains compatible with the current minimal milestone.
</p>

<hr/>

<h2 id="design-principles">4. Design Principles</h2>

<ul>
  <li>Commands should reflect published architecture.</li>
  <li>Each command should have one clear stage responsibility.</li>
  <li>Invalid input should fail explicitly.</li>
  <li>No command should silently skip a required stage while claiming full-pipeline fidelity.</li>
  <li>Diagnostics should remain source-aligned where possible.</li>
  <li>The CLI should be usable both by humans and by automation.</li>
  <li>The CLI should make intermediate artifacts observable during reference-implementation work.</li>
</ul>

<hr/>

<h2 id="command-family">5. Command Family</h2>

<p>
The initial command family is:
</p>

<pre><code>frogc validate &lt;file.frog&gt;
frogc derive-ir &lt;file.frog&gt;
frogc lower &lt;file.frog&gt;
frogc emit-contract &lt;file.frog&gt;
frogc run &lt;file.frog&gt;
</code></pre>

<p>
The simplest mental model for the first executable slice is:
</p>

<ul>
  <li>one canonical <code>.frog</code> file in,</li>
  <li>one explicit stage selected,</li>
  <li>one stage artifact or runtime result out.</li>
</ul>

<p>
Future versions may accept explicit intermediate artifacts,
but the first slice remains source-driven.
</p>

<hr/>

<h2 id="global-rules">6. Global Rules</h2>

<ul>
  <li>All commands take one canonical <code>.frog</code> source path as the primary input in the first slice.</li>
  <li>Commands that emit artifacts should support <code>--out</code>.</li>
  <li>Commands that require backend-family specialization should support <code>--backend-family</code>.</li>
  <li>The first executable slice may default to the reference host backend family where that is appropriate.</li>
  <li>The CLI should emit machine-readable JSON artifacts or JSON result objects in the current reference form.</li>
  <li>Additional presentation-oriented flags may be added later, but they are not required to define the initial stage contract.</li>
</ul>

<hr/>

<h2 id="commands">7. Commands</h2>

<h3 id="validate">7.1 validate</h3>

<p>
Checks whether the canonical source satisfies the selected published validation rules for the currently supported reference slice.
</p>

<p>
Conceptual usage:
</p>

<pre><code>frogc validate &lt;file.frog&gt; [--out &lt;path&gt;]</code></pre>

<p>
Expected behavior:
</p>

<ul>
  <li>load canonical source,</li>
  <li>perform structural and semantic checks for the supported validated subset,</li>
  <li>report explicit success or failure,</li>
  <li>do not emit Execution IR as the primary artifact of this command.</li>
</ul>

<p>
Typical failures include malformed source, invalid primitive usage, illegal edge wiring, unsupported constructs for the current slice, and illegal feedback without explicit memory.
</p>

<h3 id="derive-ir">7.2 derive-ir</h3>

<p>
Derives open Execution IR from validated program meaning.
</p>

<p>
Conceptual usage:
</p>

<pre><code>frogc derive-ir &lt;file.frog&gt; [--out &lt;path&gt;]</code></pre>

<p>
Expected behavior:
</p>

<ul>
  <li>load and validate the source,</li>
  <li>derive an implementation-side open Execution IR artifact,</li>
  <li>preserve attribution and recoverable distinctions required by the published derivation rules,</li>
  <li>fail if validation did not succeed.</li>
</ul>

<p>
The emitted artifact is a derived implementation-side form.
It is not canonical source and not yet a backend-facing contract.
</p>

<h3 id="lower">7.3 lower</h3>

<p>
Specializes the derived Execution IR for one selected backend family.
</p>

<p>
Conceptual usage:
</p>

<pre><code>frogc lower &lt;file.frog&gt; --backend-family &lt;family&gt; [--out &lt;path&gt;]</code></pre>

<p>
Expected behavior:
</p>

<ul>
  <li>load and validate the source,</li>
  <li>derive open Execution IR,</li>
  <li>lower it for the selected backend family,</li>
  <li>preserve semantic meaning while making backend-family assumptions more explicit.</li>
</ul>

<p>
This command must not claim that the lowered form is itself the language definition.
</p>

<h3 id="emit-contract">7.4 emit-contract</h3>

<p>
Emits a backend contract for one selected backend family.
</p>

<p>
Conceptual usage:
</p>

<pre><code>frogc emit-contract &lt;file.frog&gt; --backend-family &lt;family&gt; [--out &lt;path&gt;]</code></pre>

<p>
Expected behavior:
</p>

<ul>
  <li>load and validate the source,</li>
  <li>derive open Execution IR,</li>
  <li>lower it for the selected backend family,</li>
  <li>emit a backend contract artifact declaring consumable units, assumptions, and unsupported features where relevant.</li>
</ul>

<p>
This command should fail explicitly if the selected backend family cannot support the required semantics.
</p>

<h3 id="run">7.5 run</h3>

<p>
Runs the program through the first reference backend family and reference runtime.
</p>

<p>
Conceptual usage:
</p>

<pre><code>frogc run &lt;file.frog&gt; [--backend-family &lt;family&gt;] [--inputs &lt;json-object&gt;] [--out &lt;path&gt;]</code></pre>

<p>
Expected behavior:
</p>

<ul>
  <li>load and validate the source,</li>
  <li>derive open Execution IR,</li>
  <li>lower it for the selected backend family,</li>
  <li>emit or materialize a backend contract,</li>
  <li>pass that contract to the reference runtime,</li>
  <li>execute the program or reject it explicitly.</li>
</ul>

<p>
For the first slice, the default backend family may be the reference host family if no explicit family is provided.
For callable examples, runtime inputs may be supplied explicitly.
</p>

<hr/>

<h2 id="output-and-artifacts">8. Output and Artifacts</h2>

<p>
The initial CLI should make stage results observable.
For the first executable slice, that means:
</p>

<ul>
  <li><strong>validate</strong> returns a validation result artifact,</li>
  <li><strong>derive-ir</strong> returns a derived Execution IR artifact,</li>
  <li><strong>lower</strong> returns a lowered-form artifact,</li>
  <li><strong>emit-contract</strong> returns a backend contract artifact,</li>
  <li><strong>run</strong> returns a runtime result object.</li>
</ul>

<p>
In the current reference form, JSON is an appropriate transport for these outputs.
Human-oriented presentation may be layered on top later, but should not obscure the underlying stage results.
</p>

<hr/>

<h2 id="diagnostics-and-exit-behavior">9. Diagnostics and Exit Behavior</h2>

<p>
The initial CLI should fail explicitly and identify the failed stage clearly.
At minimum, diagnostics should remain explicit about:
</p>

<ul>
  <li>the failed stage,</li>
  <li>the source target,</li>
  <li>the backend family if relevant,</li>
  <li>the reason for failure,</li>
  <li>the most useful source-aligned anchor available.</li>
</ul>

<p>
Exact exit-code partitioning may evolve during reference-implementation work.
What matters in the first slice is stable stage visibility and explicit failure behavior.
</p>

<hr/>

<h2 id="first-backend-family">10. First Backend Family</h2>

<p>
The recommended first backend family is:
</p>

<pre><code>reference_host_runtime_ui_binding</code></pre>

<p>
That family should remain deliberately conservative in the initial reference implementation.
The first closed executable milestone is the pure-computation path of <code>Examples/01_pure_addition</code>.
Broader support for UI value participation, UI object interaction, and explicit memory may be added incrementally as later published slices are closed.
</p>

<p>
The backend family must not silently imply a universal runtime-private architecture or a standardized event execution model for all future implementations.
</p>

<hr/>

<h2 id="examples">11. Examples</h2>

<pre><code>frogc validate Examples/01_pure_addition/main.frog

frogc derive-ir Examples/01_pure_addition/main.frog \
  --out build/01_pure_addition.ir.json

frogc lower Examples/01_pure_addition/main.frog \
  --backend-family reference_host_runtime_ui_binding \
  --out build/01_pure_addition.lowered.json

frogc emit-contract Examples/01_pure_addition/main.frog \
  --backend-family reference_host_runtime_ui_binding \
  --out build/01_pure_addition.contract.json

frogc run Examples/01_pure_addition/main.frog \
  --inputs "{\"a\": 2.25, \"b\": 3.75}"
</code></pre>

<p>
These examples describe the initial executable reference path.
Additional examples may be added once later published slices are actually supported by the reference implementation.
</p>

<hr/>

<h2 id="non-goals">12. Non-Goals</h2>

<p>
This CLI does not attempt to define:
</p>

<ul>
  <li>the normative language,</li>
  <li>the permanent transport shape of open Execution IR for all time,</li>
  <li>the universal backend contract transport format,</li>
  <li>the universal runtime API for all implementations,</li>
  <li>a universal deployment model.</li>
</ul>

<p>
Its purpose is narrower:
to make the first reference pipeline explicit,
testable,
inspectable,
and automatable.
</p>

<hr/>

<h2 id="summary">13. Summary</h2>

<p>
The <code>frogc</code> CLI is the operational shell of the first FROG reference pipeline.
It exists to expose the published stage boundaries clearly:
validation,
Execution IR derivation,
lowering,
backend contract emission,
and runtime execution.
</p>

<p>
In the current milestone, it is primarily the command-line path for closing the first executable slice around <code>Examples/01_pure_addition</code> without collapsing the published architecture into one opaque private tool flow.
</p>
