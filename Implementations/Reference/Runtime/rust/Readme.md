<p align="center">
  <img src="../../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Reference Runtime (Rust)</h1>

<p align="center">
  <strong>Minimal Rust consumer for the reference runtime family in the non-normative FROG reference implementation</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#status">2. Status</a></li>
  <li><a href="#why-this-directory-exists">3. Why This Directory Exists</a></li>
  <li><a href="#primary-slice-target">4. Primary Slice Target</a></li>
  <li><a href="#relation-with-runtime-boundary">5. Relation to the Published Runtime Boundary</a></li>
  <li><a href="#ownership-boundary">6. Ownership Boundary</a></li>
  <li><a href="#what-this-runtime-consumes">7. What This Runtime Consumes</a></li>
  <li><a href="#what-this-runtime-produces">8. What This Runtime Produces</a></li>
  <li><a href="#minimal-supported-behavior">9. Minimal Supported Behavior</a></li>
  <li><a href="#minimal-ui-surface">10. Minimal UI Surface</a></li>
  <li><a href="#published-pipe">11. Published Pipe for Example 05</a></li>
  <li><a href="#recommended-directory-shape">12. Recommended Directory Shape</a></li>
  <li><a href="#design-rules">13. Design Rules</a></li>
  <li><a href="#explicit-non-goals">14. Explicit Non-Goals</a></li>
  <li><a href="#relationship-with-python">15. Relationship with the Python Reference Runtime</a></li>
  <li><a href="#closure-status">16. Rust Closure Status</a></li>
  <li><a href="#future-growth">17. Future Growth</a></li>
  <li><a href="#summary">18. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the minimal Rust realization of the published reference runtime boundary for the FROG reference implementation.
</p>

<p>
It is a downstream runtime consumer.
It does not redefine the language, the source model, the semantic layer, the open FIR / execution-facing layer, the lowering layer, or the backend contract boundary.
</p>

<hr/>

<h2 id="status">2. Status</h2>

<p>
This directory is non-normative.
It exists to prove that one canonical executable corridor may be consumed by more than one runtime-language realization while keeping the language and contract surfaces open and repository-visible.
</p>

<p>
At the current published state, the Rust side already proves:
</p>

<ul>
  <li>deserialization of the published example-05 contract artifact,</li>
  <li>shape validation for that contract,</li>
  <li>execution of the bounded accumulation corridor,</li>
  <li>and parity of the final observable result with the Python runtime path.</li>
</ul>

<p>
What it does not yet publish is one dedicated example-runner binary or one rendered UI host path.
</p>

<hr/>

<h2 id="why-this-directory-exists">3. Why This Directory Exists</h2>

<p>
The reference implementation already publishes a runtime boundary and a Python-side realization posture for the reference family.
This Rust directory exists to demonstrate the same architectural rule with a second runtime language:
</p>

<ul>
  <li>one canonical FROG source remains the source of truth,</li>
  <li>one validated semantic reading remains the source of truth,</li>
  <li>one open execution-facing corridor remains the source of truth,</li>
  <li>and more than one runtime language may consume the resulting backend contract.</li>
</ul>

<p>
This is therefore a modular-runtime proof point, not a second language definition.
</p>

<hr/>

<h2 id="primary-slice-target">4. Primary Slice Target</h2>

<p>
The first target for this runtime is the published example:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/
</code></pre>

<p>
That example already establishes a bounded executable corridor with:
</p>

<ul>
  <li>one numeric front-panel control,</li>
  <li>one numeric front-panel indicator,</li>
  <li>one bounded loop of exactly five iterations,</li>
  <li>one explicit local-memory path,</li>
  <li>one final public output,</li>
  <li>and a minimal object-style UI write surface through <code>frog.ui.property_write</code>.</li>
</ul>

<p>
This Rust runtime must consume that same corridor.
It must not introduce a separate source example, a parallel semantic story, or a runtime-only reinterpretation of the example.
</p>

<hr/>

<h2 id="relation-with-runtime-boundary">5. Relation to the Published Runtime Boundary</h2>

<p>
The published runtime boundary already defines the first reference runtime family as:
</p>

<pre><code>reference_host_runtime_ui_binding
</code></pre>

<p>
This Rust runtime is a consumer of that family posture.
It therefore follows the already-published runtime-side assumptions:
</p>

<ul>
  <li>single-process host execution,</li>
  <li>deterministic step execution,</li>
  <li>optional UI value binding,</li>
  <li>optional UI reference binding,</li>
  <li>explicit local-memory preservation when present,</li>
  <li>and no first-class standardized UI event execution model in this first corridor.</li>
</ul>

<hr/>

<h2 id="ownership-boundary">6. Ownership Boundary</h2>

<h3>What this directory owns</h3>

<ul>
  <li>Rust-private loading of accepted backend contracts,</li>
  <li>Rust-private runtime state structures,</li>
  <li>Rust-private execution planning and scheduling mechanics,</li>
  <li>Rust-private UI binding helpers for the supported subset,</li>
  <li>and Rust-private result assembly for the reference family.</li>
</ul>

<h3>What this directory does not own</h3>

<ul>
  <li>the FROG language definition,</li>
  <li>the canonical <code>.frog</code> source model,</li>
  <li>the semantic acceptance boundary,</li>
  <li>the open FIR / execution-facing layer,</li>
  <li>the lowering boundary,</li>
  <li>the backend contract boundary,</li>
  <li>the normative meaning of widget classes, properties, methods, or events,</li>
  <li>and the universal definition of runtime behavior for every future host.</li>
</ul>

<p>
The key architectural rule remains:
</p>

<pre><code>validated meaning != runtime implementation
backend contract != runtime-private structures
Rust runtime != universal FROG runtime
</code></pre>

<hr/>

<h2 id="what-this-runtime-consumes">7. What This Runtime Consumes</h2>

<p>
This Rust runtime starts after source loading, structural validation, semantic validation, FIR-target derivation, and lowering have already produced an acceptable backend contract.
</p>

<p>
For the first bounded published slice, it consumes:
</p>

<ul>
  <li>one backend contract artifact from the reference contract emitter,</li>
  <li>one declared backend family equal to <code>reference_host_runtime_ui_binding</code>,</li>
  <li>one explicit bounded loop model,</li>
  <li>one explicit delay-backed state carrier,</li>
  <li>one control-input binding,</li>
  <li>one indicator/public-output publication rule,</li>
  <li>and one minimal <code>face_color</code> property-write surface.</li>
</ul>

<hr/>

<h2 id="what-this-runtime-produces">8. What This Runtime Produces</h2>

<p>
For the current bounded corridor, the Rust consumer produces runtime-visible evidence that:
</p>

<ul>
  <li>the contract was accepted,</li>
  <li>the loop ran exactly five iterations,</li>
  <li>the state started at zero,</li>
  <li>the final state for input <code>3</code> is <code>15</code>,</li>
  <li>the public output is correct,</li>
  <li>the indicator value is correct,</li>
  <li>and the minimal UI runtime state is preserved for the supported widgets.</li>
</ul>

<hr/>

<h2 id="minimal-supported-behavior">9. Minimal Supported Behavior</h2>

<p>
The current first published slice supports:
</p>

<ul>
  <li>bounded loop execution,</li>
  <li>explicit local state,</li>
  <li>u16 numeric accumulation,</li>
  <li>public input binding,</li>
  <li>public output publication,</li>
  <li>indicator publication,</li>
  <li>and bounded object-style UI property writes.</li>
</ul>

<p>
This does not imply that the Rust runtime already supports the full future FROG language surface.
It only proves that one serious named example can already be consumed in Rust without redefining the corridor.
</p>

<hr/>

<h2 id="minimal-ui-surface">10. Minimal UI Surface</h2>

<p>
The supported UI posture is intentionally narrow:
</p>

<ul>
  <li><code>widget_value</code> participation for the control,</li>
  <li><code>widget_value</code> publication for the indicator,</li>
  <li><code>widget_reference</code> resolution for both widgets,</li>
  <li><code>frog.ui.property_write</code> on member <code>face_color</code>.</li>
</ul>

<p>
This is enough to prove that the Rust consumer preserves the distinction between value participation and object-style interaction.
It is not yet a full widget object-model implementation.
</p>

<hr/>

<h2 id="published-pipe">11. Published Pipe for Example 05</h2>

<p>
At the current published state, the Rust pipe for the first serious example is test-driven:
</p>

<pre><code>cd Implementations/Reference/Runtime/rust
cargo test
</code></pre>

<p>
The relevant example-facing test files are:
</p>

<pre><code>tests/
├── slice05_contract_smoke.rs
└── slice05_execution.rs
</code></pre>

<p>
Their roles are:
</p>

<ul>
  <li><code>slice05_contract_smoke.rs</code> — verify that the published contract artifact deserializes and exposes the expected bounded shape,</li>
  <li><code>slice05_execution.rs</code> — verify that the Rust runtime executes the same published contract corridor and reaches the expected final result.</li>
</ul>

<p>
This is already a real downstream consumer pipe.
What is still missing is one dedicated Rust runner binary comparable to the Python entry point.
</p>

<hr/>

<h2 id="recommended-directory-shape">12. Recommended Directory Shape</h2>

<pre><code>Implementations/Reference/Runtime/rust/
├── Readme.md
├── Cargo.toml
├── src/
│   ├── main.rs
│   ├── lib.rs
│   ├── cli.rs
│   ├── contract.rs
│   ├── diagnostics.rs
│   ├── runtime.rs
│   ├── execute.rs
│   └── ui.rs
└── tests/
    ├── slice05_contract_smoke.rs
    └── slice05_execution.rs
</code></pre>

<p>
This shape is only a recommended first skeleton.
It should remain small until the published corridor requires more.
</p>

<hr/>

<h2 id="design-rules">13. Design Rules</h2>

<ul>
  <li>Accept or reject contracts explicitly.</li>
  <li>Do not silently reinterpret undeclared assumptions.</li>
  <li>Keep explicit local-memory meaning visible in runtime execution.</li>
  <li>Keep loop iteration count explicit where the contract declares it.</li>
  <li>Keep runtime-private helper structures downstream from the published backend contract.</li>
  <li>Reject unsupported widget-reference or property-write operations explicitly.</li>
  <li>Keep diagnostics attributable when the consumed contract carries source-aligned anchors.</li>
</ul>

<hr/>

<h2 id="explicit-non-goals">14. Explicit Non-Goals</h2>

<ul>
  <li>This directory does not define the language.</li>
  <li>This directory does not define the canonical source format.</li>
  <li>This directory does not define the FIR architecture.</li>
  <li>This directory does not define lowering law.</li>
  <li>This directory does not define the backend contract boundary.</li>
  <li>This directory does not define a universal host UI.</li>
  <li>This directory does not yet define a native executable LLVM corridor.</li>
</ul>

<hr/>

<h2 id="relationship-with-python">15. Relationship with the Python Reference Runtime</h2>

<p>
The Python and Rust runtimes are parallel consumers of the same published contract corridor.
They may differ in private structures, packaging, and host mechanics, but they should stay aligned on:
</p>

<ul>
  <li>acceptance criteria,</li>
  <li>loop meaning,</li>
  <li>explicit-state meaning,</li>
  <li>UI binding obligations,</li>
  <li>and final public behavior.</li>
</ul>

<p>
The Python runtime currently provides the clearest direct execution entry point.
The Rust runtime currently provides the strongest second-language parity proof through tests.
</p>

<hr/>

<h2 id="closure-status">16. Rust Closure Status</h2>

<table>
  <thead>
    <tr>
      <th>Rust-side surface</th>
      <th>Status</th>
      <th>Published posture</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contract loading</td>
      <td>Closed</td>
      <td>Published contract artifact is consumed successfully.</td>
    </tr>
    <tr>
      <td>Contract shape proof</td>
      <td>Closed</td>
      <td><code>slice05_contract_smoke.rs</code> exists.</td>
    </tr>
    <tr>
      <td>Execution proof</td>
      <td>Closed enough for the first slice</td>
      <td><code>slice05_execution.rs</code> proves bounded execution and final result parity.</td>
    </tr>
    <tr>
      <td>Dedicated example runner</td>
      <td>Missing</td>
      <td>No dedicated <code>cargo run</code> example pipe is published yet.</td>
    </tr>
    <tr>
      <td>Rendered UI host</td>
      <td>Missing</td>
      <td>Runtime-visible UI state exists, but no rendered Rust host UI is published yet.</td>
    </tr>
    <tr>
      <td>Native LLVM corridor</td>
      <td>Missing</td>
      <td>No Rust-side native executable closure is published yet for this example.</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="future-growth">17. Future Growth</h2>

<ol>
  <li>add one dedicated Rust CLI runner for the example contract,</li>
  <li>add one C/C++ sibling consumer for full three-language modularity,</li>
  <li>add one peripheral UI object realization file contract for rendered hosts,</li>
  <li>and later participate in a native FIR → lowering → LLVM-oriented path where applicable.</li>
</ol>

<hr/>

<h2 id="summary">18. Summary</h2>

<p>
This Rust directory is already a real downstream consumer of the first published executable corridor.
It proves that the repository is not locked to one runtime language.
</p>

<p>
What is still missing is not a new semantic story.
What is still missing is the next layer of closure:
a dedicated Rust runner, a C/C++ peer runtime, a rendered UI host path, and a native executable corridor.
</p>
