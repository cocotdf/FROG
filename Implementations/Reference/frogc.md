<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">frogc Command Surface</h1>

<p align="center">
  <strong>Reference CLI surface for the bounded executable corridors exercised by the FROG reference implementation</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#status-and-boundary">2. Status and Boundary</a></li>
  <li><a href="#design-goals">3. Design Goals</a></li>
  <li><a href="#current-priority-slice">4. Current Priority Slice</a></li>
  <li><a href="#command-family">5. Command Family</a></li>
  <li><a href="#shared-options">6. Shared Options</a></li>
  <li><a href="#validate-command">7. <code>validate</code> Command</a></li>
  <li><a href="#derive-ir-command">8. <code>derive-ir</code> Command</a></li>
  <li><a href="#lower-command">9. <code>lower</code> Command</a></li>
  <li><a href="#emit-contract-command">10. <code>emit-contract</code> Command</a></li>
  <li><a href="#run-command">11. <code>run</code> Command</a></li>
  <li><a href="#stage-separation-rule">12. Stage Separation Rule</a></li>
  <li><a href="#subset-honesty-rule">13. Subset Honesty Rule</a></li>
  <li><a href="#example-session">14. Example Session</a></li>
  <li><a href="#summary">15. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document records the intended command surface for the FROG reference implementation CLI.
</p>

<p>
It is an implementation-side document.
It does not redefine the language.
Its purpose is to make the reference pipeline visible and stage-separated through a small command family that mirrors the published architecture rather than bypassing it.
</p>

<p>
The reference CLI should therefore let a user perform, explicitly and separately:
</p>

<ul>
  <li>validation,</li>
  <li>Execution IR derivation,</li>
  <li>lowering,</li>
  <li>backend contract emission,</li>
  <li>and runtime-side execution.</li>
</ul>

<hr/>

<h2 id="status-and-boundary">2. Status and Boundary</h2>

<p>
This command surface is non-normative.
It belongs to the reference implementation workspace.
</p>

<p>
It does not own:
</p>

<ul>
  <li>canonical source shape,</li>
  <li>validated semantic meaning,</li>
  <li>canonical Execution IR law,</li>
  <li>lowering law,</li>
  <li>backend contract law.</li>
</ul>

<p>
It only exposes a practical way to consume those published repository surfaces for the supported reference subset.
</p>

<hr/>

<h2 id="design-goals">3. Design Goals</h2>

<p>
The command surface should satisfy the following goals:
</p>

<ul>
  <li><strong>stage visibility</strong> — each major pipeline stage should remain explicit,</li>
  <li><strong>artifact visibility</strong> — each command should emit a recognizable artifact kind,</li>
  <li><strong>subset honesty</strong> — unsupported-but-valid situations should be reported explicitly,</li>
  <li><strong>slice-first usefulness</strong> — the first complete vertical slice should be directly runnable through this CLI,</li>
  <li><strong>no hidden semantic shortcuts</strong> — <code>run</code> should not pretend to bypass validation, derivation, lowering, and contract emission conceptually, even if the implementation internally pipelines them.</li>
</ul>

<hr/>

<h2 id="current-priority-slice">4. Current Priority Slice</h2>

<p>
The current reference priority is the first complete executable vertical slice:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/main.frog</code></pre>

<p>
The command surface should therefore be sufficient to make this slice observable through:
</p>

<ul>
  <li>successful validation of the supported subset,</li>
  <li>visible Execution IR derivation,</li>
  <li>visible lowering,</li>
  <li>visible backend contract emission,</li>
  <li>visible runtime-side outputs and UI effects.</li>
</ul>

<p>
This slice remains the first success target.
The CLI should not imply that every richer future widget family is already supported just because the underlying architectural model is open-ended.
</p>

<hr/>

<h2 id="command-family">5. Command Family</h2>

<p>
The reference command family is intentionally small:
</p>

<pre><code>frogc validate &lt;file.frog&gt;
frogc derive-ir &lt;file.frog&gt;
frogc lower &lt;file.frog&gt;
frogc emit-contract &lt;file.frog&gt;
frogc run &lt;file.frog&gt;
</code></pre>

<p>
A future implementation MAY add additional helper commands.
However, the core stage family above SHOULD remain recognizable because it mirrors the published repository corridor.
</p>

<hr/>

<h2 id="shared-options">6. Shared Options</h2>

<p>
The exact option set may evolve, but the following shared options are useful and aligned with the current reference posture:
</p>

<pre><code>--backend-family &lt;family_id&gt;
--output &lt;path&gt;
--format json
--strict-subset
--example-id &lt;example_id&gt;
</code></pre>

<p>
Intended meanings:
</p>

<ul>
  <li><code>--backend-family</code> selects the backend family used by <code>lower</code>, <code>emit-contract</code>, or <code>run</code>.</li>
  <li><code>--output</code> writes the resulting artifact to a file.</li>
  <li><code>--format json</code> requests a JSON artifact surface when applicable.</li>
  <li><code>--strict-subset</code> rejects unsupported-but-valid source instead of allowing best-effort continuation.</li>
  <li><code>--example-id</code> makes the intended bounded reference slice explicit in diagnostics or logs.</li>
</ul>

<p>
These options are implementation-side convenience.
They do not replace the architectural stage boundaries.
</p>

<hr/>

<h2 id="validate-command">7. <code>validate</code> Command</h2>

<h3>7.1 Surface</h3>

<pre><code>frogc validate &lt;file.frog&gt; [--format json] [--output &lt;path&gt;] [--strict-subset]</code></pre>

<h3>7.2 Intent</h3>

<p>
The <code>validate</code> command checks the input file against the supported published reference subset and distinguishes:
</p>

<ul>
  <li>load failure,</li>
  <li>structural invalidity,</li>
  <li>semantic rejection,</li>
  <li>unsupported-but-valid situations,</li>
  <li>successful validation.</li>
</ul>

<h3>7.3 Minimum artifact posture</h3>

<p>
When <code>--format json</code> is used, the result SHOULD include at least:
</p>

<ul>
  <li><code>artifact_kind</code>,</li>
  <li><code>status</code>,</li>
  <li><code>source_ref</code>,</li>
  <li><code>validated_subset</code>,</li>
  <li><code>validated_program</code> when successful.</li>
</ul>

<h3>7.4 Example</h3>

<pre><code>frogc validate Examples/05_bounded_ui_accumulator/main.frog --format json</code></pre>

<hr/>

<h2 id="derive-ir-command">8. <code>derive-ir</code> Command</h2>

<h3>8.1 Surface</h3>

<pre><code>frogc derive-ir &lt;file.frog&gt; [--format json] [--output &lt;path&gt;] [--strict-subset]</code></pre>

<h3>8.2 Intent</h3>

<p>
The <code>derive-ir</code> command produces an execution-facing derived artifact from a successfully validated source program.
</p>

<p>
It SHOULD preserve:
</p>

<ul>
  <li>source attribution,</li>
  <li>execution-unit identity,</li>
  <li>boundary objects,</li>
  <li>explicit state when present,</li>
  <li>the distinction between semantic state and presentation-only metadata.</li>
</ul>

<h3>8.3 Minimum artifact posture</h3>

<p>
When <code>--format json</code> is used, the result SHOULD include at least:
</p>

<ul>
  <li><code>artifact_kind</code>,</li>
  <li><code>execution_unit</code> or equivalent attributable root object,</li>
  <li><code>objects</code>,</li>
  <li><code>connections</code>.</li>
</ul>

<h3>8.4 Example</h3>

<pre><code>frogc derive-ir Examples/05_bounded_ui_accumulator/main.frog --format json</code></pre>

<hr/>

<h2 id="lower-command">9. <code>lower</code> Command</h2>

<h3>9.1 Surface</h3>

<pre><code>frogc lower &lt;file.frog&gt; [--backend-family &lt;family_id&gt;] [--format json] [--output &lt;path&gt;]</code></pre>

<h3>9.2 Intent</h3>

<p>
The <code>lower</code> command specializes the derived open Execution IR for a selected backend family.
</p>

<p>
It SHOULD keep explicit:
</p>

<ul>
  <li>the selected backend family,</li>
  <li>the lowered unit set,</li>
  <li>the assumptions introduced by specialization,</li>
  <li>and the fact that the lowered form is downstream from canonical FROG IR.</li>
</ul>

<h3>9.3 Minimum artifact posture</h3>

<p>
When <code>--format json</code> is used, the result SHOULD include at least:
</p>

<ul>
  <li><code>artifact_kind</code>,</li>
  <li><code>backend_family</code>,</li>
  <li><code>assumptions</code>,</li>
  <li><code>units</code>.</li>
</ul>

<h3>9.4 Example</h3>

<pre><code>frogc lower Examples/05_bounded_ui_accumulator/main.frog \
  --backend-family reference_host_runtime_ui_binding \
  --format json</code></pre>

<hr/>

<h2 id="emit-contract-command">10. <code>emit-contract</code> Command</h2>

<h3>10.1 Surface</h3>

<pre><code>frogc emit-contract &lt;file.frog&gt; [--backend-family &lt;family_id&gt;] [--format json] [--output &lt;path&gt;]</code></pre>

<h3>10.2 Intent</h3>

<p>
The <code>emit-contract</code> command produces the backend contract artifact consumed by the selected runtime or backend-side consumer.
</p>

<p>
It SHOULD make visible:
</p>

<ul>
  <li>unit identities,</li>
  <li>boundary obligations,</li>
  <li>state-cell obligations when present,</li>
  <li>UI bindings when present,</li>
  <li>unsupported surfaces that are preserved only as non-semantic metadata.</li>
</ul>

<h3>10.3 Minimum artifact posture</h3>

<p>
When <code>--format json</code> is used, the result SHOULD include at least:
</p>

<ul>
  <li><code>artifact_kind</code>,</li>
  <li><code>backend_family</code>,</li>
  <li><code>assumptions</code>,</li>
  <li><code>units</code>,</li>
  <li><code>unsupported</code>.</li>
</ul>

<h3>10.4 Example</h3>

<pre><code>frogc emit-contract Examples/05_bounded_ui_accumulator/main.frog \
  --backend-family reference_host_runtime_ui_binding \
  --format json</code></pre>

<hr/>

<h2 id="run-command">11. <code>run</code> Command</h2>

<h3>11.1 Surface</h3>

<pre><code>frogc run &lt;file.frog&gt; [--backend-family &lt;family_id&gt;] [--format json] [--output &lt;path&gt;]</code></pre>

<h3>11.2 Intent</h3>

<p>
The <code>run</code> command executes the selected supported corridor through the reference runtime family.
</p>

<p>
Conceptually, it still depends on:
</p>

<ul>
  <li>validation,</li>
  <li>Execution IR derivation,</li>
  <li>lowering,</li>
  <li>backend contract emission.</li>
</ul>

<p>
An implementation MAY internally pipeline those stages for convenience.
However, it MUST remain possible to understand the command as runtime-side consumption of a bounded validated corridor rather than as a hidden direct source-to-execution shortcut.
</p>

<h3>11.3 Minimum artifact posture</h3>

<p>
When <code>--format json</code> is used, the result SHOULD include at least:
</p>

<ul>
  <li><code>artifact_kind</code>,</li>
  <li><code>status</code>,</li>
  <li><code>contract_ref</code>,</li>
  <li><code>execution_summary</code>,</li>
  <li><code>outputs</code>.</li>
</ul>

<h3>11.4 Example</h3>

<pre><code>frogc run Examples/05_bounded_ui_accumulator/main.frog \
  --backend-family reference_host_runtime_ui_binding \
  --format json</code></pre>

<h3>11.5 Expected observable facts for the first priority slice</h3>

<p>
For the current bounded UI accumulator slice, a successful <code>run</code> SHOULD make it possible to observe at least:
</p>

<ul>
  <li>the final public output value,</li>
  <li>the final indicator value,</li>
  <li>the counted loop execution summary,</li>
  <li>the explicit state surface,</li>
  <li>minimal UI property-write effects such as <code>face_color</code> writes.</li>
</ul>

<hr/>

<h2 id="stage-separation-rule">12. Stage Separation Rule</h2>

<p>
The CLI surface MUST preserve the conceptual distinction between stages:
</p>

<pre><code>validate
    !=
derive-ir
    !=
lower
    !=
emit-contract
    !=
run
</code></pre>

<p>
This means:
</p>

<ul>
  <li><code>derive-ir</code> MUST NOT pretend to succeed when validation failed,</li>
  <li><code>lower</code> MUST NOT pretend to succeed when no valid execution-facing artifact exists,</li>
  <li><code>emit-contract</code> MUST NOT pretend to succeed when no valid lowered form exists,</li>
  <li><code>run</code> MUST NOT claim success without a conceptually valid contract path.</li>
</ul>

<hr/>

<h2 id="subset-honesty-rule">13. Subset Honesty Rule</h2>

<p>
The CLI MUST remain explicit about the difference between:
</p>

<ul>
  <li>the general extensible FROG model published by the repository,</li>
  <li>the bounded subset currently supported by the reference implementation,</li>
  <li>implementation-private convenience behavior.</li>
</ul>

<p>
Accordingly:
</p>

<ul>
  <li>unsupported-but-valid situations SHOULD be reported explicitly,</li>
  <li>the CLI SHOULD identify the selected backend family when relevant,</li>
  <li>the CLI SHOULD avoid implying support for all future widget families, profiles, or runtime forms unless such support is actually implemented and claimed.</li>
</ul>

<hr/>

<h2 id="example-session">14. Example Session</h2>

<p>
A typical first-priority bounded slice session may look like:
</p>

<pre><code>frogc validate Examples/05_bounded_ui_accumulator/main.frog --format json
frogc derive-ir Examples/05_bounded_ui_accumulator/main.frog --format json
frogc lower Examples/05_bounded_ui_accumulator/main.frog --backend-family reference_host_runtime_ui_binding --format json
frogc emit-contract Examples/05_bounded_ui_accumulator/main.frog --backend-family reference_host_runtime_ui_binding --format json
frogc run Examples/05_bounded_ui_accumulator/main.frog --backend-family reference_host_runtime_ui_binding --format json
</code></pre>

<p>
This sequence is intentionally small.
Its purpose is to make one bounded published corridor inspectable from source to runtime-visible outcome.
</p>

<hr/>

<h2 id="summary">15. Summary</h2>

<p>
The <code>frogc</code> command surface is the small reference CLI that mirrors the published FROG architecture through explicit stages:
</p>

<ul>
  <li><code>validate</code>,</li>
  <li><code>derive-ir</code>,</li>
  <li><code>lower</code>,</li>
  <li><code>emit-contract</code>,</li>
  <li><code>run</code>.</li>
</ul>

<p>
Its current mission is to help the reference implementation prove one complete bounded executable corridor, especially the first priority UI-bearing accumulator slice, while remaining explicit about:
</p>

<ul>
  <li>stage boundaries,</li>
  <li>artifact boundaries,</li>
  <li>backend-family selection,</li>
  <li>and supported-subset boundaries.</li>
</ul>
