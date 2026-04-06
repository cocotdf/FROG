<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">Reference CLI</h1>

<p align="center">
  <strong>Command-line entry surface for the non-normative FROG reference implementation</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#status-and-boundary">2. Status and Boundary</a></li>
  <li><a href="#current-role">3. Current Role</a></li>
  <li><a href="#current-priority-slice">4. Current Priority Slice</a></li>
  <li><a href="#command-surface">5. Command Surface</a></li>
  <li><a href="#relation-with-the-reference-pipeline">6. Relation with the Reference Pipeline</a></li>
  <li><a href="#relation-with-reference-artifacts">7. Relation with Reference Artifacts</a></li>
  <li><a href="#current-entry-points">8. Current Entry Points</a></li>
  <li><a href="#design-rules">9. Design Rules</a></li>
  <li><a href="#relation-with-examples-and-stage-results">10. Relation with Examples and Stage Results</a></li>
  <li><a href="#what-this-directory-must-not-do">11. What this Directory Must Not Do</a></li>
  <li><a href="#summary">12. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory contains the command-line surface of the non-normative FROG reference implementation.
Its role is to expose a small, explicit, stage-aware toolchain for the bounded executable slices currently exercised by the reference workspace.
</p>

<p>
The CLI is not a language specification layer.
It is a practical implementation-facing shell around the published:
</p>

<ul>
  <li>canonical source intake,</li>
  <li>validation,</li>
  <li>Execution IR derivation,</li>
  <li>lowering,</li>
  <li>backend contract emission,</li>
  <li>runtime-side execution path.</li>
</ul>

<p>
Its purpose is to make the reference corridor observable and testable without collapsing the repository's architectural stages into one opaque command.
</p>

<hr/>

<h2 id="status-and-boundary">2. Status and Boundary</h2>

<p>
This directory is non-normative.
It does not define the language, the canonical source format, the validated program meaning, the open Execution IR, or the backend contract boundary.
Those remain owned by the published specification layers.
</p>

<p>
The CLI exists to make those published boundaries executable and inspectable for the supported reference subset.
It must not become a hidden source of language truth.
</p>

<hr/>

<h2 id="current-role">3. Current Role</h2>

<p>
At the current stage of the repository, the CLI serves four practical purposes:
</p>

<ul>
  <li>provide explicit stage entry points for the supported reference subset,</li>
  <li>make intermediate stage artifacts observable during reference-implementation work,</li>
  <li>support repeatable command-line execution of bounded published example paths,</li>
  <li>make supported-subset boundaries explicit rather than implicit.</li>
</ul>

<p>
The CLI should therefore remain compact, explicit, and easy to audit before it expands to broader coverage.
</p>

<hr/>

<h2 id="current-priority-slice">4. Current Priority Slice</h2>

<p>
The current reference priority is no longer the first arithmetic-only example.
The current reference priority is the first complete executable UI-bearing vertical slice:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/main.frog</code></pre>

<p>
The CLI should therefore make it straightforward to inspect and execute a corridor that includes:
</p>

<ul>
  <li>one numeric control,</li>
  <li>one numeric indicator,</li>
  <li>natural <code>widget_value</code> participation,</li>
  <li>minimal object-style property interaction through <code>widget_reference</code>,</li>
  <li>bounded loop execution,</li>
  <li>explicit state via <code>frog.core.delay</code>,</li>
  <li>public output observation,</li>
  <li>runtime-visible UI effects.</li>
</ul>

<p>
This priority does not mean that the full open-ended FROG widget model is already implemented.
It means the CLI should first make one complete bounded published slice executable from source to runtime-visible result.
</p>

<hr/>

<h2 id="command-surface">5. Command Surface</h2>

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
The exact command surface may evolve, but stage separation should remain explicit.
The CLI should mirror the published architecture rather than collapsing multiple stages into one opaque tool behavior.
</p>

<p>
A useful shared option set may include:
</p>

<pre><code>--backend-family &lt;family_id&gt;
--output &lt;path&gt;
--format json
--strict-subset
--example-id &lt;example_id&gt;
</code></pre>

<p>
These options are implementation-side conveniences.
They do not replace the architectural stage boundaries.
</p>

<hr/>

<h2 id="relation-with-the-reference-pipeline">6. Relation with the Reference Pipeline</h2>

<p>
The CLI is the operational shell of the reference pipeline described under:
</p>

<pre><code>Implementations/Reference/</code></pre>

<p>
Its commands should remain aligned with the stage boundaries used by the reference implementation:
</p>

<ul>
  <li><strong>validate</strong> — distinguish loadability, structural invalidity, semantic rejection, unsupported-but-valid situations, and successful validation,</li>
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

<h2 id="relation-with-reference-artifacts">7. Relation with Reference Artifacts</h2>

<p>
The CLI should expose or emit the same main artifact family names used elsewhere in the reference workspace:
</p>

<ul>
  <li><code>frog_loaded_source</code>,</li>
  <li><code>frog_validation_result</code>,</li>
  <li><code>frog_derived_execution_ir</code>,</li>
  <li><code>frog_lowered_form</code>,</li>
  <li><code>frog_backend_contract</code>,</li>
  <li><code>frog_runtime_result</code>.</li>
</ul>

<p>
This matters because:
</p>

<ul>
  <li><code>frogc.md</code> describes the command surface,</li>
  <li><code>pipeline.md</code> describes the stage corridor,</li>
  <li><code>example-artifact-requirements.md</code> describes minimum outputs per example,</li>
  <li><code>internal-artifacts.md</code> defines the internal taxonomy.</li>
</ul>

<p>
The CLI should therefore not invent a separate competing vocabulary for stage results.
</p>

<hr/>

<h2 id="current-entry-points">8. Current Entry Points</h2>

<p>
A compact demonstration entry point may exist in this directory for early executable slices.
That is acceptable as long as it remains explicitly non-normative and does not blur ownership of the stages.
</p>

<p>
At the current published state, a practical entry point may be:
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
├── Runtime/
└── UIHost/
</code></pre>

<p>
This is the preferred direction because it preserves a simple command-line surface without turning one convenience script into accidental architecture.
</p>

<p>
The regression scripts in this directory are useful as bounded executable checks, but they should be read as support material around the main CLI and pipeline, not as the true architectural owner of stage boundaries.
</p>

<hr/>

<h2 id="design-rules">9. Design Rules</h2>

<ul>
  <li>Commands should reflect published architectural boundaries.</li>
  <li>Commands should fail explicitly rather than silently skipping invalid stages.</li>
  <li>Commands should remain implementation-oriented, not normative.</li>
  <li>Diagnostics should remain source-aligned where possible.</li>
  <li>The CLI should remain usable for inspecting intermediate stage results during bounded executable slices.</li>
  <li>Convenience wrappers must not erase the intended separation between loading, validation, derivation, lowering, contract emission, and runtime consumption.</li>
  <li>Unsupported-but-valid situations should remain explicitly diagnosable.</li>
  <li>The CLI should not imply coverage broader than the subset the reference implementation actually supports.</li>
</ul>

<hr/>

<h2 id="relation-with-examples-and-stage-results">10. Relation with Examples and Stage Results</h2>

<p>
The CLI should work directly with the published example slices.
At the current milestone, the first complete success target is:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/main.frog</code></pre>

<p>
A correct CLI should make it straightforward to:
</p>

<ul>
  <li>validate that example,</li>
  <li>derive its Execution IR,</li>
  <li>lower it for the first backend family,</li>
  <li>emit a backend contract,</li>
  <li>run it and observe both the final public output and the final UI-facing indicator result.</li>
</ul>

<p>
It should also make visible, for this first priority slice:
</p>

<ul>
  <li>the bounded loop count,</li>
  <li>the explicit state path,</li>
  <li>the distinction between natural widget value access and object-style property writes,</li>
  <li>the non-semantic status of source-persisted presentation metadata such as <code>face_template</code>.</li>
</ul>

<p>
Earlier examples such as pure addition, UI value roundtrip, UI property write, and explicit state feedback remain useful regression anchors.
However, they should now be read as supporting slices around the current first full vertical-slice closure target rather than as the sole CLI milestone.
</p>

<hr/>

<h2 id="what-this-directory-must-not-do">11. What this Directory Must Not Do</h2>

<p>
This directory must not:
</p>

<ul>
  <li>pretend that the CLI defines the language,</li>
  <li>hide stage ownership behind one opaque private command flow,</li>
  <li>replace published IR and backend boundaries with implementation shortcuts,</li>
  <li>silently jump from source directly to private execution while claiming stage fidelity,</li>
  <li>turn a convenience script into the de facto normative architecture,</li>
  <li>imply support for the entire open-ended widget ecosystem when only a bounded published subset is actually executed.</li>
</ul>

<p>
If the CLI reveals a specification gap, the fix belongs in the owning specification or implementation-layer document, not in undocumented command behavior.
</p>

<hr/>

<h2 id="summary">12. Summary</h2>

<p>
The CLI is the operational shell of the non-normative FROG reference implementation.
It exists to expose the reference pipeline clearly and explicitly, to keep stage boundaries visible, and to support executable example slices without collapsing the repository's published architecture into one opaque tool command.
</p>

<p>
At the current milestone, it is primarily the command-line path for the first complete bounded executable corridor around:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/main.frog</code></pre>

<p>
It should therefore remain aligned with:
</p>

<ul>
  <li>the stage-separated reference pipeline,</li>
  <li>the shared artifact taxonomy,</li>
  <li>the per-example artifact requirements,</li>
  <li>and the explicit distinction between the general extensible FROG model and the subset actually executed today.</li>
</ul>
