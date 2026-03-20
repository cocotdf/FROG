<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
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
  <li><a href="#status">2. Status</a></li>
  <li><a href="#design-principles">3. Design Principles</a></li>
  <li><a href="#command-family">4. Command Family</a></li>
  <li><a href="#global-rules">5. Global Rules</a></li>
  <li><a href="#commands">6. Commands</a>
    <ul>
      <li><a href="#validate">6.1 validate</a></li>
      <li><a href="#derive-ir">6.2 derive-ir</a></li>
      <li><a href="#lower">6.3 lower</a></li>
      <li><a href="#emit-contract">6.4 emit-contract</a></li>
      <li><a href="#run">6.5 run</a></li>
    </ul>
  </li>
  <li><a href="#output-modes">7. Output Modes</a></li>
  <li><a href="#diagnostics-and-exit-codes">8. Diagnostics and Exit Codes</a></li>
  <li><a href="#first-backend-family">9. First Backend Family</a></li>
  <li><a href="#examples">10. Examples</a></li>
  <li><a href="#non-goals">11. Non-Goals</a></li>
  <li><a href="#summary">12. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the initial command-line surface of the FROG reference implementation.
The CLI is intentionally stage-aware.
It mirrors the published architectural pipeline rather than hiding all stages behind one opaque command.
</p>

<p>
The purpose of <code>frogc</code> is not to define the language.
Its purpose is to provide a practical shell around the first non-normative reference pipeline.
</p>

<pre><code>canonical source
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

<h2 id="status">2. Status</h2>

<p>
This CLI is a reference-implementation interface only.
It is not part of the normative language definition.
The command names and option surface may evolve,
but the stage separation should remain visible because it reflects already-published architectural boundaries.
</p>

<hr/>

<h2 id="design-principles">3. Design Principles</h2>

<ul>
  <li>Commands should reflect published architecture.</li>
  <li>Each command should have one clear stage responsibility.</li>
  <li>Invalid input should fail explicitly.</li>
  <li>No command should silently skip a required stage.</li>
  <li>Diagnostics should remain source-aligned where possible.</li>
  <li>The CLI should be usable both by humans and by automation.</li>
</ul>

<hr/>

<h2 id="command-family">4. Command Family</h2>

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
The first version may also accept explicit artifacts from previous stages,
but the simplest mental model is file-in, staged pipeline out.
</p>

<hr/>

<h2 id="global-rules">5. Global Rules</h2>

<ul>
  <li>All commands take one canonical <code>.frog</code> source path as the primary input in the first slice.</li>
  <li>All commands should support <code>--backend-family</code> where backend-family specialization is relevant.</li>
  <li>All commands should support <code>--out</code> when emitting stage artifacts.</li>
  <li>All commands should support <code>--json</code> for machine-readable diagnostics.</li>
  <li>All commands should support <code>--quiet</code> and <code>--verbose</code>.</li>
</ul>

<hr/>

<h2 id="commands">6. Commands</h2>

<h3 id="validate">6.1 validate</h3>

<p>
Checks whether the canonical source satisfies the selected published validation rules for the MVP slice.
</p>

<p>
Conceptual usage:
</p>

<pre><code>frogc validate &lt;file.frog&gt; [--json] [--quiet] [--verbose]</code></pre>

<p>
Expected behavior:
</p>

<ul>
  <li>load canonical source,</li>
  <li>perform structural and semantic checks for the selected MVP subset,</li>
  <li>report explicit success or failure,</li>
  <li>do not emit Execution IR.</li>
</ul>

<p>
Typical failures:
</p>

<ul>
  <li>malformed source,</li>
  <li>invalid primitive usage,</li>
  <li>invalid widget participation,</li>
  <li>illegal feedback without explicit memory,</li>
  <li>interface/widget role confusion.</li>
</ul>

<h3 id="derive-ir">6.2 derive-ir</h3>

<p>
Derives open Execution IR from validated program meaning.
</p>

<p>
Conceptual usage:
</p>

<pre><code>frogc derive-ir &lt;file.frog&gt; [--out &lt;path&gt;] [--json] [--quiet] [--verbose]</code></pre>

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
The emitted artifact is an implementation-side derived form.
It is not the canonical source and not yet a backend-facing contract.
</p>

<h3 id="lower">6.3 lower</h3>

<p>
Specializes the derived Execution IR for one selected backend family.
</p>

<p>
Conceptual usage:
</p>

<pre><code>frogc lower &lt;file.frog&gt; --backend-family &lt;family&gt; [--out &lt;path&gt;] [--json] [--quiet] [--verbose]</code></pre>

<p>
Expected behavior:
</p>

<ul>
  <li>load and validate the source,</li>
  <li>derive open Execution IR,</li>
  <li>lower it for the selected backend family,</li>
  <li>preserve semantic meaning while making family assumptions more explicit.</li>
</ul>

<p>
This command must not claim that the lowered form is itself the language definition.
</p>

<h3 id="emit-contract">6.4 emit-contract</h3>

<p>
Emits a backend contract for one selected backend family.
</p>

<p>
Conceptual usage:
</p>

<pre><code>frogc emit-contract &lt;file.frog&gt; --backend-family &lt;family&gt; [--out &lt;path&gt;] [--json] [--quiet] [--verbose]</code></pre>

<p>
Expected behavior:
</p>

<ul>
  <li>load and validate the source,</li>
  <li>derive open Execution IR,</li>
  <li>lower it for the selected family,</li>
  <li>emit a backend contract artifact that declares consumable units, assumptions, attribution support, and unsupported features.</li>
</ul>

<p>
This command should fail explicitly if the selected backend family cannot support the required semantics.
</p>

<h3 id="run">6.5 run</h3>

<p>
Runs the program through the first reference backend family and reference runtime.
</p>

<p>
Conceptual usage:
</p>

<pre><code>frogc run &lt;file.frog&gt; [--backend-family &lt;family&gt;] [--json] [--quiet] [--verbose]</code></pre>

<p>
Expected behavior:
</p>

<ul>
  <li>load and validate the source,</li>
  <li>derive open Execution IR,</li>
  <li>lower it for the selected family,</li>
  <li>emit or materialize a backend contract,</li>
  <li>pass that contract to the reference runtime,</li>
  <li>execute the program or reject it explicitly.</li>
</ul>

<p>
For the first slice, the default backend family should be the reference host family if no explicit family is provided.
</p>

<hr/>

<h2 id="output-modes">7. Output Modes</h2>

<p>
The first CLI should support at least two output styles:
</p>

<ul>
  <li><strong>human mode</strong> — concise readable diagnostics,</li>
  <li><strong>JSON mode</strong> — machine-readable diagnostics and stage summaries.</li>
</ul>

<p>
Suggested human output pattern:
</p>

<pre><code>[ok] loaded source
[ok] validated
[ok] derived execution IR
[ok] lowered for backend family: reference_host_runtime_ui_binding
[ok] emitted backend contract
[ok] executed</code></pre>

<p>
Suggested failure pattern:
</p>

<pre><code>[error] validation failed
- case: illegal_feedback_without_explicit_memory
- location: diagram edge e3
- reason: directed cycle without explicit local-memory primitive</code></pre>

<hr/>

<h2 id="diagnostics-and-exit-codes">8. Diagnostics and Exit Codes</h2>

<p>
The first CLI should use simple stable exit codes.
A minimal proposal is:
</p>

<ul>
  <li><code>0</code> — success,</li>
  <li><code>1</code> — source load failure,</li>
  <li><code>2</code> — validation failure,</li>
  <li><code>3</code> — derivation failure,</li>
  <li><code>4</code> — lowering failure,</li>
  <li><code>5</code> — backend-contract emission failure,</li>
  <li><code>6</code> — runtime rejection or runtime execution failure.</li>
</ul>

<p>
Diagnostics should remain explicit about:
</p>

<ul>
  <li>the failed stage,</li>
  <li>the source target,</li>
  <li>the backend family if relevant,</li>
  <li>the reason for failure,</li>
  <li>the most useful source-aligned anchor available.</li>
</ul>

<hr/>

<h2 id="first-backend-family">9. First Backend Family</h2>

<p>
The recommended first backend family is:
</p>

<pre><code>reference_host_runtime_ui_binding</code></pre>

<p>
That family is intentionally narrow.
It should support:
</p>

<ul>
  <li>ordinary primitive execution,</li>
  <li>public interface participation,</li>
  <li>explicit local memory through <code>frog.core.delay</code>,</li>
  <li><code>widget_value</code> participation,</li>
  <li><code>widget_reference</code> plus standardized UI-object primitives.</li>
</ul>

<p>
It should not silently assume a first-class standardized event execution model.
</p>

<hr/>

<h2 id="examples">10. Examples</h2>

<pre><code>frogc validate Examples/01_pure_addition/main.frog

frogc derive-ir Examples/02_ui_value_roundtrip/main.frog \
  --out build/02_ui_value_roundtrip.ir.json

frogc lower Examples/03_ui_property_write/main.frog \
  --backend-family reference_host_runtime_ui_binding \
  --out build/03_ui_property_write.lowered.json

frogc emit-contract Examples/04_stateful_feedback_delay/main.frog \
  --backend-family reference_host_runtime_ui_binding \
  --out build/04_stateful_feedback_delay.contract.json

frogc run Examples/02_ui_value_roundtrip/main.frog
</code></pre>

<hr/>

<h2 id="non-goals">11. Non-Goals</h2>

<p>
This CLI does not attempt to define:
</p>

<ul>
  <li>the normative language,</li>
  <li>the canonical transport shape of open Execution IR for all time,</li>
  <li>the universal backend contract transport format,</li>
  <li>the universal runtime API for all implementations,</li>
  <li>a universal deployment model.</li>
</ul>

<p>
Its purpose is narrower:
to make the first reference pipeline explicit,
testable,
and automatable.
</p>

<hr/>

<h2 id="summary">12. Summary</h2>

<p>
The <code>frogc</code> CLI is the operational shell of the first FROG reference pipeline.
It exists to expose the published stage boundaries clearly:
validation,
Execution IR derivation,
lowering,
backend contract emission,
and runtime execution.
</p>
