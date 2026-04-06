<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">frogc Command Surface</h1>

<p align="center">
  <strong>Reference CLI surface for bounded executable FROG corridors</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#status-and-boundary">2. Status and Boundary</a></li>
  <li><a href="#design-goal">3. Design Goal</a></li>
  <li><a href="#first-priority-slice">4. First Priority Slice</a></li>
  <li><a href="#core-commands">5. Core Commands</a></li>
  <li><a href="#common-options">6. Common Options</a></li>
  <li><a href="#validate-command">7. <code>validate</code></a></li>
  <li><a href="#derive-ir-command">8. <code>derive-ir</code></a></li>
  <li><a href="#lower-command">9. <code>lower</code></a></li>
  <li><a href="#emit-contract-command">10. <code>emit-contract</code></a></li>
  <li><a href="#run-command">11. <code>run</code></a></li>
  <li><a href="#expected-status-model">12. Expected Status Model</a></li>
  <li><a href="#example-commands">13. Example Commands</a></li>
  <li><a href="#subset-honesty-rule">14. Subset Honesty Rule</a></li>
  <li><a href="#summary">15. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This file records the intended command surface for the reference implementation CLI.
It is an implementation document, not a normative language specification.
</p>

<p>
Its purpose is to expose a command surface that mirrors the published architecture rather than bypassing it.
Accordingly, <code>frogc</code> should preserve explicit stage boundaries between:
</p>

<ul>
  <li>source intake,</li>
  <li>validation,</li>
  <li>Execution IR derivation,</li>
  <li>lowering,</li>
  <li>backend contract emission,</li>
  <li>runtime-side execution.</li>
</ul>

<hr/>

<h2 id="status-and-boundary">2. Status and Boundary</h2>

<p>
This CLI is part of the non-normative reference implementation workspace.
It does not redefine:
</p>

<ul>
  <li>canonical source shape,</li>
  <li>validated semantic meaning,</li>
  <li>the canonical Execution IR model,</li>
  <li>lowering law,</li>
  <li>backend contract law.</li>
</ul>

<p>
It is a consumer-side surface that should remain aligned with the published repository layers and with the current supported subset of the reference implementation.
</p>

<hr/>

<h2 id="design-goal">3. Design Goal</h2>

<p>
The design goal of <code>frogc</code> is to make the reference corridor executable in an explicit and stage-separated way.
</p>

<p>
The command surface should therefore help a reader or implementer see:
</p>

<ul>
  <li>which stage is being exercised,</li>
  <li>which artifact should be produced,</li>
  <li>which backend family is being targeted,</li>
  <li>which bounded subset is actually supported.</li>
</ul>

<p>
The command surface should not imply that the full open-ended FROG model is already implemented merely because the architecture supports it.
</p>

<hr/>

<h2 id="first-priority-slice">4. First Priority Slice</h2>

<p>
For the current repository campaign, the first priority slice of the reference CLI is:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/main.frog</code></pre>

<p>
The CLI should therefore be able to drive a complete corridor for a bounded published subset including:
</p>

<ul>
  <li>one numeric front-panel control,</li>
  <li>one numeric front-panel indicator,</li>
  <li>natural widget value participation,</li>
  <li>minimal object-style property writes,</li>
  <li>bounded loop execution,</li>
  <li>explicit state through <code>frog.core.delay</code>,</li>
  <li>public output observation.</li>
</ul>

<hr/>

<h2 id="core-commands">5. Core Commands</h2>

<pre><code>frogc validate &lt;file.frog&gt;
frogc derive-ir &lt;file.frog&gt;
frogc lower &lt;file.frog&gt;
frogc emit-contract &lt;file.frog&gt;
frogc run &lt;file.frog&gt;
</code></pre>

<p>
These commands intentionally mirror the published reference pipeline stages.
They should remain small and architecture-aligned rather than collapsing all work into one opaque action.
</p>

<hr/>

<h2 id="common-options">6. Common Options</h2>

<p>
A practical reference CLI MAY support common options such as:
</p>

<pre><code>--backend-family &lt;name&gt;
--out &lt;path&gt;
--format json
--diagnostics pretty
--strict-subset
</code></pre>

<p>
Useful interpretations:
</p>

<ul>
  <li><code>--backend-family</code> selects the downstream execution-consumption family used by <code>lower</code>, <code>emit-contract</code>, or <code>run</code>.</li>
  <li><code>--out</code> writes the produced artifact to a chosen path.</li>
  <li><code>--format json</code> requests machine-readable output.</li>
  <li><code>--diagnostics pretty</code> requests a human-readable diagnostic surface.</li>
  <li><code>--strict-subset</code> treats unsupported-but-valid broader-model constructs as hard failures for the reference subset.</li>
</ul>

<p>
The exact option set may evolve.
The important rule is that option growth must preserve stage separation and subset honesty.
</p>

<hr/>

<h2 id="validate-command">7. <code>validate</code></h2>

<h3>7.1 Intent</h3>

<p>
<code>validate</code> checks whether canonical source satisfies the selected published rules for the supported reference subset.
</p>

<h3>7.2 Minimum responsibilities</h3>

<ul>
  <li>load the source,</li>
  <li>distinguish load failure from structural invalidity,</li>
  <li>distinguish structural invalidity from semantic rejection,</li>
  <li>distinguish semantic rejection from unsupported-but-valid situations,</li>
  <li>emit a validation artifact.</li>
</ul>

<h3>7.3 Example</h3>

<pre><code>frogc validate Examples/05_bounded_ui_accumulator/main.frog --format json
</code></pre>

<h3>7.4 Expected artifact kind</h3>

<pre><code>frog_validation_result</code></pre>

<hr/>

<h2 id="derive-ir-command">8. <code>derive-ir</code></h2>

<h3>8.1 Intent</h3>

<p>
<code>derive-ir</code> emits an open execution-facing derived form from validated program meaning.
</p>

<h3>8.2 Minimum responsibilities</h3>

<ul>
  <li>consume successful validation,</li>
  <li>derive an attributable execution-facing representation,</li>
  <li>preserve explicit state, boundaries, and supported UI distinctions,</li>
  <li>emit an Execution-IR-facing artifact.</li>
</ul>

<h3>8.3 Example</h3>

<pre><code>frogc derive-ir Examples/05_bounded_ui_accumulator/main.frog --out artifacts/05.ir.json
</code></pre>

<h3>8.4 Expected artifact kind</h3>

<pre><code>frog_derived_execution_ir</code></pre>

<hr/>

<h2 id="lower-command">9. <code>lower</code></h2>

<h3>9.1 Intent</h3>

<p>
<code>lower</code> specializes the derived open execution-facing form for a selected backend family.
</p>

<h3>9.2 Minimum responsibilities</h3>

<ul>
  <li>consume a valid derived execution-facing artifact,</li>
  <li>make backend-family assumptions explicit,</li>
  <li>lower bounded loops, explicit state, and supported UI surfaces without redefining their language ownership,</li>
  <li>emit a lowered artifact.</li>
</ul>

<h3>9.3 Example</h3>

<pre><code>frogc lower Examples/05_bounded_ui_accumulator/main.frog --backend-family reference_host_runtime_ui_binding --out artifacts/05.lowered.json
</code></pre>

<h3>9.4 Expected artifact kind</h3>

<pre><code>frog_lowered_form</code></pre>

<hr/>

<h2 id="emit-contract-command">10. <code>emit-contract</code></h2>

<h3>10.1 Intent</h3>

<p>
<code>emit-contract</code> emits a backend contract artifact for the selected backend family.
</p>

<h3>10.2 Minimum responsibilities</h3>

<ul>
  <li>consume a valid lowered form,</li>
  <li>emit explicit units, assumptions, and unsupported surfaces,</li>
  <li>preserve the distinction between semantic execution surfaces and presentation-only metadata,</li>
  <li>produce a runtime-consumable contract artifact.</li>
</ul>

<h3>10.3 Example</h3>

<pre><code>frogc emit-contract Examples/05_bounded_ui_accumulator/main.frog --backend-family reference_host_runtime_ui_binding --out artifacts/05.contract.json
</code></pre>

<h3>10.4 Expected artifact kind</h3>

<pre><code>frog_backend_contract</code></pre>

<hr/>

<h2 id="run-command">11. <code>run</code></h2>

<h3>11.1 Intent</h3>

<p>
<code>run</code> executes the program through the first reference runtime family after the earlier stages have been satisfied.
</p>

<h3>11.2 Minimum responsibilities</h3>

<ul>
  <li>consume a valid backend contract,</li>
  <li>accept or reject it explicitly,</li>
  <li>execute through a runtime-side consumer rather than by silently skipping the declared stages,</li>
  <li>emit a runtime result artifact.</li>
</ul>

<h3>11.3 Example</h3>

<pre><code>frogc run Examples/05_bounded_ui_accumulator/main.frog --backend-family reference_host_runtime_ui_binding --format json
</code></pre>

<h3>11.4 Expected artifact kind</h3>

<pre><code>frog_runtime_result</code></pre>

<p>
For the first priority slice, a successful runtime result should make it possible to observe at least:
</p>

<ul>
  <li>the final public output,</li>
  <li>the final indicator value,</li>
  <li>the counted-loop execution fact,</li>
  <li>the explicit state presence,</li>
  <li>minimal UI property-write effects such as <code>face_color</code>.</li>
</ul>

<hr/>

<h2 id="expected-status-model">12. Expected Status Model</h2>

<p>
The CLI should distinguish at least the following statuses:
</p>

<ul>
  <li><code>ok</code> — the command succeeded for the selected supported subset,</li>
  <li><code>load_error</code> — the source could not be loaded,</li>
  <li><code>structural_error</code> — canonical source shape is invalid,</li>
  <li><code>semantic_error</code> — validated meaning is rejected,</li>
  <li><code>unsupported_but_valid</code> — valid in the broader published model but outside the current reference subset,</li>
  <li><code>lowering_error</code> — backend-family lowering failed,</li>
  <li><code>contract_error</code> — contract emission failed,</li>
  <li><code>runtime_error</code> — runtime-side execution failed or rejected the contract.</li>
</ul>

<p>
The CLI SHOULD avoid reporting a later-stage success if an earlier required stage failed.
</p>

<hr/>

<h2 id="example-commands">13. Example Commands</h2>

<h3>13.1 Validate the first priority slice</h3>

<pre><code>frogc validate Examples/05_bounded_ui_accumulator/main.frog --format json
</code></pre>

<h3>13.2 Derive IR for the first priority slice</h3>

<pre><code>frogc derive-ir Examples/05_bounded_ui_accumulator/main.frog --out artifacts/05.ir.json
</code></pre>

<h3>13.3 Lower the first priority slice</h3>

<pre><code>frogc lower Examples/05_bounded_ui_accumulator/main.frog --backend-family reference_host_runtime_ui_binding --out artifacts/05.lowered.json
</code></pre>

<h3>13.4 Emit the contract for the first priority slice</h3>

<pre><code>frogc emit-contract Examples/05_bounded_ui_accumulator/main.frog --backend-family reference_host_runtime_ui_binding --out artifacts/05.contract.json
</code></pre>

<h3>13.5 Run the first priority slice</h3>

<pre><code>frogc run Examples/05_bounded_ui_accumulator/main.frog --backend-family reference_host_runtime_ui_binding --format json
</code></pre>

<hr/>

<h2 id="subset-honesty-rule">14. Subset Honesty Rule</h2>

<p>
The CLI MUST remain explicit about the distinction between:
</p>

<ul>
  <li>the general extensible FROG model published by the
