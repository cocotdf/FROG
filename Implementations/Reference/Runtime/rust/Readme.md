<p align="center">
  <img src="../../../../FROG logo.svg" alt="FROG logo" width="200" />
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
  <li><a href="#relation-to-the-published-runtime-boundary">5. Relation to the Published Runtime Boundary</a></li>
  <li><a href="#ownership-boundary">6. Ownership Boundary</a></li>
  <li><a href="#what-this-runtime-consumes">7. What This Runtime Consumes</a></li>
  <li><a href="#what-this-runtime-produces">8. What This Runtime Produces</a></li>
  <li><a href="#minimal-supported-behavior">9. Minimal Supported Behavior</a></li>
  <li><a href="#minimal-ui-surface">10. Minimal UI Surface</a></li>
  <li><a href="#execution-shape">11. Execution Shape</a></li>
  <li><a href="#recommended-directory-shape">12. Recommended Directory Shape</a></li>
  <li><a href="#design-rules">13. Design Rules</a></li>
  <li><a href="#explicit-non-goals">14. Explicit Non-Goals</a></li>
  <li><a href="#relationship-with-the-python-reference-runtime">15. Relationship with the Python Reference Runtime</a></li>
  <li><a href="#future-growth">16. Future Growth</a></li>
  <li><a href="#summary">17. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the minimal Rust realization of the published reference runtime boundary for the FROG reference implementation.
</p>

<p>
It is a <strong>downstream runtime consumer</strong>. It does not redefine the language, the source model, the semantic layer, the Execution IR, the lowering layer, or the backend contract boundary.
</p>

<hr/>

<h2 id="status">2. Status</h2>

<p>
This directory is <strong>non-normative</strong>.
</p>

<p>
It exists to prove that one canonical executable corridor may be consumed by more than one runtime family realization while keeping the language and contract surfaces open and repository-visible.
</p>

<hr/>

<h2 id="why-this-directory-exists">3. Why This Directory Exists</h2>

<p>
The reference implementation already publishes a runtime boundary and a first Python-side realization posture for the reference family.
This Rust directory exists to demonstrate the same architectural rule with a second runtime language:
</p>

<ul>
  <li>one canonical FROG source remains the source of truth,</li>
  <li>one validated semantic reading remains the source of truth,</li>
  <li>one open execution-facing corridor remains the source of truth,</li>
  <li>and more than one runtime may consume the resulting backend contract.</li>
</ul>

<p>
This is therefore a modular-runtime proof point, not a second language definition.
</p>

<hr/>

<h2 id="primary-slice-target">4. Primary Slice Target</h2>

<p>
The first target for this runtime is the published example:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/</code></pre>

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
This Rust runtime must consume <strong>that same corridor</strong>.
It must not introduce a separate source example, a parallel semantic story, or a runtime-only reinterpretation of the example.
</p>

<hr/>

<h2 id="relation-to-the-published-runtime-boundary">5. Relation to the Published Runtime Boundary</h2>

<p>
The published runtime boundary already defines the first reference runtime family as:
</p>

<pre><code>reference_host_runtime_ui_binding</code></pre>

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

<p>
This runtime must remain compatible with the published distinction between:
</p>

<ul>
  <li>contract rejection,</li>
  <li>accepted execution,</li>
  <li>and accepted-but-failed execution.</li>
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
  <li>the open Execution IR,</li>
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
Rust runtime != universal FROG runtime</code></pre>

<hr/>

<h2 id="what-this-runtime-consumes">7. What This Runtime Consumes</h2>

<p>
This runtime consumes a successful backend contract artifact for the published reference runtime family.
Conceptually, it consumes a payload compatible with the already-published runtime contract corridor:
</p>

<pre><code>{
  "artifact_kind": "frog_backend_contract",
  "artifact_version": "0.1",
  "backend_family": "reference_host_runtime_ui_binding",
  "producer": "...",
  "compatibility": "family_specific",
  "source_ref": { ... },
  "assumptions": { ... },
  "units": [ ... ],
  "unsupported": [],
  "diagnostics": []
}</code></pre>

<p>
This Rust runtime therefore starts <strong>after</strong> source loading, structural validation, semantic validation, Execution IR derivation, and lowering have already produced an acceptable backend contract.
</p>

<p>
It must not silently accept:
</p>

<ul>
  <li>the wrong backend family,</li>
  <li>missing required assumptions,</li>
  <li>unsupported declarations that it claims not to handle,</li>
  <li>or malformed contract entries for state, loop, widget, or property-write obligations.</li>
</ul>

<hr/>

<h2 id="what-this-runtime-produces">8. What This Runtime Produces</h2>

<p>
On successful execution, this runtime returns a runtime result artifact compatible with the published runtime result posture.
Conceptually:
</p>

<pre><code>{
  "artifact_kind": "frog_runtime_result",
  "artifact_version": "0.1-dev",
  "backend_family": "reference_host_runtime_ui_binding",
  "contract_ref": {
    "unit_ids": ["main"]
  },
  "status": "ok",
  "execution_summary": {
    "mode": "deterministic_step_execution",
    "state_initialized": true,
    "ui_bound": true
  },
  "outputs": {
    "public": { ... },
    "ui": { ... }
  },
  "diagnostics": []
}</code></pre>

<p>
On rejection or failure, it returns an explicit error-shaped runtime result rather than silently degrading execution meaning.
</p>

<hr/>

<h2 id="minimal-supported-behavior">9. Minimal Supported Behavior</h2>

<p>
For the first executable slice, this runtime only needs to support the smallest sufficient behavior required by <code>Examples/05_bounded_ui_accumulator</code>.
</p>

<p>
The conservative supported reading is:
</p>

<ol>
  <li>accept one successful contract for the family <code>reference_host_runtime_ui_binding</code>,</li>
  <li>prepare one host-side execution session,</li>
  <li>bind the numeric control value once for the run,</li>
  <li>apply the declared minimal UI property writes supported by this runtime,</li>
  <li>initialize the explicit state to <code>0</code>,</li>
  <li>execute exactly five iterations,</li>
  <li>compute <code>state_next = state_current + input_value</code> at each iteration,</li>
  <li>commit state explicitly at the required commit point,</li>
  <li>publish the final state to the numeric indicator,</li>
  <li>publish the same final state to the public output surface,</li>
  <li>and report success or explicit failure.</li>
</ol>

<p>
Even if the mathematical outcome is equivalent to <code>5 * input</code>, this runtime must preserve the explicit loop-and-state reading of the slice.
It must not treat the example as a narrative shortcut.
</p>

<hr/>

<h2 id="minimal-ui-surface">10. Minimal UI Surface</h2>

<p>
The first Rust runtime surface is intentionally small.
</p>

<p>
For the initial slice, the required UI posture is:
</p>

<ul>
  <li>one numeric control value binding,</li>
  <li>one numeric indicator value publication,</li>
  <li>minimal widget-reference support where the contract explicitly declares it,</li>
  <li>and support for the small property-write surface actually exercised by the published slice.</li>
</ul>

<p>
For the initial example, the explicitly exercised property-write surface is currently limited to:
</p>

<pre><code>face_color</code></pre>

<p>
Accordingly, the first Rust runtime may conservatively reject unsupported property writes outside that bounded surface.
</p>

<p>
This bounded support is sufficient for the first executable proof.
It is not a statement that the long-term widget object model is limited to that property.
</p>

<hr/>

<h2 id="execution-shape">11. Execution Shape</h2>

<p>
The recommended execution shape for the first Rust runtime is:
</p>

<pre><code>accepted backend contract
        |
        v
family compatibility check
        |
        v
assumption / unsupported check
        |
        v
host-side execution session creation
        |
        v
UI value binding + UI reference preparation
        |
        v
explicit state initialization
        |
        v
deterministic counted-loop execution
        |
        v
indicator publication + public output collection
        |
        v
runtime result artifact</code></pre>

<p>
This execution shape remains:
</p>

<ul>
  <li>host-oriented,</li>
  <li>deterministic,</li>
  <li>bounded,</li>
  <li>single-run,</li>
  <li>and intentionally free of event-loop-heavy requirements for the first slice.</li>
</ul>

<hr/>

<h2 id="recommended-directory-shape">12. Recommended Directory Shape</h2>

<p>
A conservative directory shape for this runtime family is:
</p>

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
    └── slice05_execution.rs</code></pre>

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
  <li>Do not promote Rust-private implementation convenience into normative language law.</li>
</ul>

<hr/>

<h2 id="explicit-non-goals">14. Explicit Non-Goals</h2>

<p>
The first Rust runtime does not need to provide:
</p>

<ul>
  <li>a universal FROG runtime architecture,</li>
  <li>direct execution from raw <code>.frog</code> source,</li>
  <li>a complete widget toolkit,</li>
  <li>a full property / method / event object system,</li>
  <li>continuous interactive re-execution,</li>
  <li>hidden persistence between runs,</li>
  <li>pixel-identical rendering across hosts,</li>
  <li>or direct LLVM ownership or LLVM-private runtime coupling.</li>
</ul>

<p>
LLVM remains a downstream backend-family topic, not the definition of this runtime and not the definition of FROG.
</p>

<hr/>

<h2 id="relationship-with-the-python-reference-runtime">15. Relationship with the Python Reference Runtime</h2>

<p>
The Python reference runtime and the Rust reference runtime must be understood as <strong>parallel consumers of the same published corridor</strong>.
</p>

<p>
They should aim to agree on:
</p>

<ul>
  <li>family acceptance criteria,</li>
  <li>explicit-state preservation,</li>
  <li>counted-loop behavior for the supported slice,</li>
  <li>bounded UI property-write support for the supported slice,</li>
  <li>public output publication,</li>
  <li>and result / error-shape expectations.</li>
</ul>

<p>
They do not need to share identical internal data structures, helper APIs, or host-specific execution mechanics.
</p>

<hr/>

<h2 id="future-growth">16. Future Growth</h2>

<p>
If the published corridor grows, this runtime may later expand in carefully bounded steps, for example:
</p>

<ul>
  <li>additional supported widget properties,</li>
  <li>additional supported widget classes,</li>
  <li>broader counted-loop and state forms,</li>
  <li>broader public interface binding,</li>
  <li>richer diagnostics and attribution preservation,</li>
  <li>or a stronger test matrix shared with the Python reference runtime.</li>
</ul>

<p>
Such growth must remain downstream from the language-owned specification surfaces and must stay aligned with published examples, conformance material, and backend-contract expectations.
</p>

<hr/>

<h2 id="summary">17. Summary</h2>

<p>
This directory defines the first minimal Rust runtime consumer for the published reference runtime family.
</p>

<p>
Its purpose is not to redefine FROG.
Its purpose is to prove that one canonical executable slice can remain language-owned and contract-owned while being consumed by more than one runtime language.
</p>

<p>
For the first closure target, this runtime is intentionally narrow:
one accepted backend contract family,
one bounded host-side execution posture,
one explicit-state counted-loop example,
one minimal UI write surface,
and one final observable result.
</p>
