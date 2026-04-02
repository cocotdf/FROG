<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">🐸 Reference CLI</h1>

<p align="center">
  Command-line entry points for the non-normative FROG reference implementation<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#status-and-boundary">2. Status and Boundary</a></li>
  <li><a href="#current-role">3. Current Role</a></li>
  <li><a href="#command-surface">4. Command Surface</a></li>
  <li><a href="#relation-with-the-reference-pipeline">5. Relation with the Reference Pipeline</a></li>
  <li><a href="#current-entry-points">6. Current Entry Points</a></li>
  <li><a href="#design-rules">7. Design Rules</a></li>
  <li><a href="#relation-with-examples-and-stage-results">8. Relation with Examples and Stage Results</a></li>
  <li><a href="#what-this-directory-must-not-do">9. What this Directory Must Not Do</a></li>
  <li><a href="#summary">10. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory contains the command-line surface of the non-normative FROG reference implementation.
Its role is to expose a small, explicit, stage-aware toolchain for the first executable vertical slices of FROG.
</p>

<p>
The CLI is not a language specification layer.
It is a practical implementation-facing shell around the published source → validation → IR → lowering → backend contract → runtime path.
</p>

<p>
Its purpose is to make the first executable reference path observable and testable without collapsing the repository's architectural stages into one opaque command.
</p>

<hr/>

<h2 id="status-and-boundary">2. Status and Boundary</h2>

<p>
This directory is <strong>non-normative</strong>.
It does not define the language,
the canonical source format,
the validated program meaning,
the open Execution IR,
or the backend contract boundary.
Those remain owned by the published specification layers.
</p>

<p>
The CLI exists to make those published boundaries executable and inspectable.
It must not become a hidden source of language truth.
</p>

<hr/>

<h2 id="current-role">3. Current Role</h2>

<p>
At the current stage of the repository, the CLI serves three practical purposes:
</p>

<ul>
  <li>provide explicit stage entry points for the first executable slice,</li>
  <li>make intermediate stage results observable during reference-implementation work,</li>
  <li>support repeatable command-line execution of the minimal published example path.</li>
</ul>

<p>
The current priority is the first executable slice built around:
</p>

<pre><code>Examples/01_pure_addition/main.frog</code></pre>

<p>
The CLI should therefore remain compact, explicit, and easy to audit before it expands to broader UI-oriented and state-oriented slices.
</p>

<hr/>

<h2 id="command-surface">4. Command Surface</h2>

<p>
A useful command model for the reference CLI is:
</p>

<pre><code>frogc validate &lt;file.frog&gt;
frogc derive-ir &lt;file.frog&gt;
frogc lower &lt;file.frog&gt;
frogc emit-contract &lt;file.frog&gt;
frogc run &lt;file.frog&gt;
</code></pre>

<p>
The exact command surface may evolve,
but the stage separation should remain explicit.
The CLI should mirror the published architecture rather than collapsing multiple stages into one opaque tool behavior.
</p>

<hr/>

<h2 id="relation-with-the-reference-pipeline">5. Relation with the Reference Pipeline</h2>

<p>
The CLI is the operational shell of the reference pipeline described under:
</p>

<pre><code>Implementations/Reference/</code></pre>

<p>
Its commands should remain aligned with the stage boundaries used by the reference implementation:
</p>

<ul>
  <li><strong>validate</strong> — confirm that source belongs to the supported validated subset,</li>
  <li><strong>derive-ir</strong> — derive an open execution-facing representation with recoverable attribution,</li>
  <li><strong>lower</strong> — specialize the open IR for a selected backend family,</li>
  <li><strong>emit-contract</strong> — produce the handoff consumed by a backend or runtime,</li>
  <li><strong>run</strong> — execute through runtime-side contract consumption.</li>
</ul>

<p>
The CLI should make those stages visible.
It should not silently bypass them while still claiming to represent the full pipeline.
</p>

<hr/>

<h2 id="current-entry-points">6. Current Entry Points</h2>

<p>
A compact demonstration entry point may exist in this directory for early executable slices.
That is acceptable as long as it remains explicitly non-normative and does not blur ownership of the stages.
</p>

<p>
In the current reference direction, the practical CLI entry point may be:
</p>

<pre><code>frog_demo_pipeline.py</code></pre>

<p>
while the implementation logic progressively lives in specialized modules under:
</p>

<pre><code>Implementations/Reference/
├── Loader/
├── Validator/
├── Deriver/
├── Lowerer/
├── ContractEmitter/
└── Runtime/
</code></pre>

<p>
This is the preferred direction because it preserves a simple command-line surface without turning one convenience script into accidental architecture.
</p>

<hr/>

<h2 id="design-rules">7. Design Rules</h2>

<ul>
  <li>Commands should reflect published architectural boundaries.</li>
  <li>Commands should fail explicitly rather than silently skipping invalid stages.</li>
  <li>Commands should remain implementation-oriented, not normative.</li>
  <li>Diagnostics should remain source-aligned where possible.</li>
  <li>The CLI should remain usable for inspecting intermediate stage results during the first executable slices.</li>
  <li>Convenience wrappers must not erase the intended separation between loading, validation, derivation, lowering, contract emission, and runtime consumption.</li>
</ul>

<hr/>

<h2 id="relation-with-examples-and-stage-results">8. Relation with Examples and Stage Results</h2>

<p>
The CLI should work directly with the published example slices.
For the current milestone, the baseline path is:
</p>

<pre><code>Examples/01_pure_addition/main.frog</code></pre>

<p>
A correct CLI should make it straightforward to:
</p>

<ul>
  <li>validate that example,</li>
  <li>derive its Execution IR,</li>
  <li>lower it for the first backend family,</li>
  <li>emit a backend contract,</li>
  <li>run it and observe the expected arithmetic result.</li>
</ul>

<p>
The CLI therefore plays an important role in locking down the first executable slice before wider expansion to UI and stateful cases.
</p>

<hr/>

<h2 id="what-this-directory-must-not-do">9. What this Directory Must Not Do</h2>

<p>
This directory must not:
</p>

<ul>
  <li>pretend that the CLI defines the language,</li>
  <li>hide stage ownership behind one opaque private command flow,</li>
  <li>replace published IR and backend boundaries with implementation shortcuts,</li>
  <li>silently jump from source directly to private execution while claiming stage fidelity,</li>
  <li>turn a convenience script into the de facto normative architecture.</li>
</ul>

<p>
If the CLI reveals a specification gap, the fix belongs in the owning specification or implementation-layer document, not in undocumented command behavior.
</p>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The CLI is the operational shell of the non-normative FROG reference implementation.
It exists to expose the first reference pipeline clearly and explicitly,
to keep the stage boundaries visible,
and to support executable example slices without collapsing the repository's published architecture into one opaque tool command.
</p>

<p>
In the current milestone, it is primarily the command-line path for the first executable slice around <code>Examples/01_pure_addition</code>.
</p>
