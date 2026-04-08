<p align="center">
  <img src="../../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Reference Runtime (C/C++)</h1>

<p align="center">
  <strong>Early C/C++ consumer for the reference runtime family in the non-normative FROG reference implementation</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#status">2. Status</a></li>
  <li><a href="#why-this-directory-should-exist">3. Why This Directory Should Exist</a></li>
  <li><a href="#directory-shape">4. Directory Shape</a></li>
  <li><a href="#role-of-each-file">5. Role of Each File</a></li>
  <li><a href="#primary-slice-target">6. Primary Slice Target</a></li>
  <li><a href="#relation-to-the-runtime-boundary">7. Relation to the Runtime Boundary</a></li>
  <li><a href="#ownership-boundary">8. Ownership Boundary</a></li>
  <li><a href="#what-this-runtime-consumes">9. What This Runtime Consumes</a></li>
  <li><a href="#what-this-runtime-produces">10. What This Runtime Produces</a></li>
  <li><a href="#minimal-supported-behavior">11. Minimal Supported Behavior</a></li>
  <li><a href="#minimal-ui-surface">12. Minimal UI Surface</a></li>
  <li><a href="#published-pipe-for-example-05">13. Published Pipe for Example 05</a></li>
  <li><a href="#design-rules">14. Design Rules</a></li>
  <li><a href="#relationship-with-python-and-rust">15. Relationship with Python and Rust Consumers</a></li>
  <li><a href="#closure-status">16. C/C++ Closure Status</a></li>
  <li><a href="#future-growth">17. Future Growth</a></li>
  <li><a href="#summary">18. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the early C/C++ realization of the published reference runtime boundary for the FROG reference implementation.
It is a downstream runtime consumer.
Its role is to prove that the same canonical example corridor can be consumed in C or C++ without changing the language definition.
</p>

<p>
This directory must remain read as a runtime-family consumer layer, not as a language-definition layer.
It is downstream from canonical source, downstream from FIR, downstream from lowering, and downstream from the published backend-family contract posture.
</p>

<hr/>

<h2 id="status">2. Status</h2>

<p>
This directory is non-normative.
It is repository-visible and structurally real, but it is not yet closed at the same operational confidence level as the Python path.
</p>

<p>
At the current stage, the correct posture is:
</p>

<ul>
  <li>the C/C++ consumer family is no longer hypothetical at directory level,</li>
  <li>the build surface and source split are visible,</li>
  <li>the example-05 A-to-Z proof is not yet documented and demonstrated as strongly as Python,</li>
  <li>rendered host closure is not yet published here as a completed proof path.</li>
</ul>

<hr/>

<h2 id="why-this-directory-should-exist">3. Why This Directory Should Exist</h2>

<p>
A serious modular-runtime posture should not stop at Python plus Rust.
For repository-visible proof of implementation freedom, the same corridor should also be consumable through a C/C++ mini runtime.
</p>

<p>
This directory therefore exists to make the third runtime language explicit and symmetric with:
</p>

<ul>
  <li><code>Runtime/python/</code>,</li>
  <li><code>Runtime/rust/</code>,</li>
  <li>and the same canonical example corridor.</li>
</ul>

<p>
That matters because FROG is not trying to say “one reference implementation language is enough”.
It is trying to prove that runtime-family consumption remains open and portable across implementation languages.
</p>

<hr/>

<h2 id="directory-shape">4. Directory Shape</h2>

<pre><code>Implementations/Reference/Runtime/cpp/
├── Readme.md
├── CMakeLists.txt
├── include/
│   ├── contract.hpp
│   ├── runtime.hpp
│   ├── execute.hpp
│   └── ui.hpp
└── src/
    └── main.cpp
</code></pre>

<p>
This current repository-visible shape already matters because it separates:
</p>

<ul>
  <li>build entry,</li>
  <li>contract-facing declarations,</li>
  <li>runtime-facing declarations,</li>
  <li>execution-facing declarations,</li>
  <li>UI binding declarations,</li>
  <li>and one direct C/C++ entry point.</li>
</ul>

<p>
Additional <code>.cpp</code> implementation files and dedicated tests may be added later, but they should remain downstream from the same published corridor.
</p>

<hr/>

<h2 id="role-of-each-file">5. Role of Each File</h2>

<ul>
  <li><code>Readme.md</code><br/>
      Explains the C/C++-side runtime posture and the role of this directory.</li>

  <li><code>CMakeLists.txt</code><br/>
      Build-system entry point for the C/C++ mini runtime and example consumers.</li>

  <li><code>include/contract.hpp</code><br/>
      Contract-loading declarations and contract-shape data structures.</li>

  <li><code>include/runtime.hpp</code><br/>
      Runtime state declarations and runtime-private orchestration boundaries.</li>

  <li><code>include/execute.hpp</code><br/>
      Execution interface for accepted contracts.</li>

  <li><code>include/ui.hpp</code><br/>
      UI binding declarations for the supported subset.</li>

  <li><code>src/main.cpp</code><br/>
      Direct example-runner entry surface for bounded contract execution posture.</li>
</ul>

<hr/>

<h2 id="primary-slice-target">6. Primary Slice Target</h2>

<p>
The first target for this runtime is the published example:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/</code></pre>

<p>
This C/C++ runtime must consume the same corridor already consumed by the Python and Rust paths.
It must not introduce a separate source example, a parallel semantic story, or a runtime-only reinterpretation of the example.
</p>

<p>
The intended corridor remains:
</p>

<pre><code>main.frog
  -&gt; main.fir.json
  -&gt; main.lowering.json
  -&gt; reference runtime-family contract
  -&gt; C/C++ consumer
</code></pre>

<hr/>

<h2 id="relation-to-the-runtime-boundary">7. Relation to the Runtime Boundary</h2>

<p>
The published runtime family is:
</p>

<pre><code>reference_host_runtime_ui_binding
</code></pre>

<p>
This C/C++ runtime is one consumer of that family posture.
It should follow the same runtime-side assumptions as the Python and Rust consumers:
</p>

<ul>
  <li>single-process host execution,</li>
  <li>deterministic step execution,</li>
  <li>optional UI value binding,</li>
  <li>optional UI reference binding,</li>
  <li>explicit local-memory preservation when present,</li>
  <li>no first-class standardized asynchronous UI event execution model in this first corridor.</li>
</ul>

<hr/>

<h2 id="ownership-boundary">8. Ownership Boundary</h2>

<h3>What this directory owns</h3>

<ul>
  <li>C/C++-private loading of accepted backend contracts,</li>
  <li>C/C++-private runtime state structures,</li>
  <li>C/C++-private execution mechanics,</li>
  <li>C/C++-private UI binding helpers for the supported subset,</li>
  <li>C/C++-private result assembly for the reference family.</li>
</ul>

<h3>What this directory does not own</h3>

<ul>
  <li>the FROG language definition,</li>
  <li>the canonical <code>.frog</code> source model,</li>
  <li>the semantic acceptance boundary,</li>
  <li>the FIR architecture,</li>
  <li>the lowering boundary,</li>
  <li>the backend contract boundary,</li>
  <li>the normative meaning of widget classes, properties, methods, or events,</li>
  <li>the universal definition of runtime behavior for every future host.</li>
</ul>

<p>
The core rule remains:
</p>

<pre><code>published contract truth
    !=
C/C++-private implementation structure
</code></pre>

<hr/>

<h2 id="what-this-runtime-consumes">9. What This Runtime Consumes</h2>

<p>
This C/C++ runtime starts after source loading, structural validation, semantic validation, FIR-target derivation, and lowering have already produced an acceptable backend contract.
</p>

<p>
For the first bounded published slice, it should consume:
</p>

<ul>
  <li>one backend contract artifact from the reference contract emitter,</li>
  <li>one declared backend family equal to <code>reference_host_runtime_ui_binding</code>,</li>
  <li>one explicit bounded loop model,</li>
  <li>one explicit delay-backed state carrier,</li>
  <li>one control-input binding,</li>
  <li>one indicator and public-output publication rule,</li>
  <li>one minimal <code>foreground_color</code> property-write surface.</li>
</ul>

<hr/>

<h2 id="what-this-runtime-produces">10. What This Runtime Produces</h2>

<p>
For the same bounded corridor, the C/C++ consumer should produce runtime-visible evidence that:
</p>

<ul>
  <li>the contract was accepted,</li>
  <li>the loop ran exactly five iterations,</li>
  <li>the state started at zero,</li>
  <li>the final state for input <code>3</code> is <code>15</code>,</li>
  <li>the public output is correct,</li>
  <li>the indicator value is correct,</li>
  <li>the minimal UI runtime state is preserved for the supported widgets.</li>
</ul>

<p>
At the current repository stage, this remains the target observable posture for Example 05,
not yet a fully documented published proof path at the same level as Python.
</p>

<hr/>

<h2 id="minimal-supported-behavior">11. Minimal Supported Behavior</h2>

<p>
The intended first published slice supports:
</p>

<ul>
  <li>bounded loop execution,</li>
  <li>explicit local state,</li>
  <li><code>u16</code> numeric accumulation,</li>
  <li>public input binding,</li>
  <li>public output publication,</li>
  <li>indicator publication,</li>
  <li>bounded object-style UI property writes.</li>
</ul>

<hr/>

<h2 id="minimal-ui-surface">12. Minimal UI Surface</h2>

<p>
The intended UI posture is intentionally narrow:
</p>

<ul>
  <li><code>widget_value</code> participation for the control,</li>
  <li><code>widget_value</code> publication for the indicator,</li>
  <li><code>widget_reference</code> resolution for both widgets,</li>
  <li><code>frog.ui.property_write</code> on member <code>foreground_color</code>.</li>
</ul>

<p>
This is enough to preserve the bounded Example 05 corridor without pretending that the full future widget system is already closed.
</p>

<hr/>

<h2 id="published-pipe-for-example-05">13. Published Pipe for Example 05</h2>

<p>
The current repository already exposes the structural ingredients for a C/C++ build corridor through <code>CMakeLists.txt</code> and <code>src/main.cpp</code>.
However, the README should stay precise:
</p>

<ul>
  <li>the directory-level build posture exists,</li>
  <li>the example-level end-to-end proof posture still needs to be made explicit and demonstrated,</li>
  <li>the commands below are the intended operational corridor once the C/C++ example path is fully closed.</li>
</ul>

<pre><code>cmake -S Implementations/Reference/Runtime/cpp -B build/frog_runtime_cpp
cmake --build build/frog_runtime_cpp
build/frog_runtime_cpp/frog_runtime_cpp_example05 3
</code></pre>

<p>
A future test posture may take a form such as:
</p>

<pre><code>ctest --test-dir build/frog_runtime_cpp
</code></pre>

<p>
These commands describe the intended operational posture for this directory.
They should be treated as fully published example proof commands only once the C/C++ consumer path is completed and verified.
</p>

<hr/>

<h2 id="design-rules">14. Design Rules</h2>

<ul>
  <li>Accept or reject contracts explicitly.</li>
  <li>Do not silently reinterpret undeclared assumptions.</li>
  <li>Keep explicit local-memory meaning visible in runtime execution.</li>
  <li>Keep loop iteration count explicit where the contract declares it.</li>
  <li>Keep runtime-private helper structures downstream from the published backend contract.</li>
  <li>Reject unsupported widget-reference, property-write, method, or event operations explicitly.</li>
  <li>Do not let low-level implementation convenience become semantic law.</li>
</ul>

<hr/>

<h2 id="relationship-with-python-and-rust">15. Relationship with Python and Rust Consumers</h2>

<p>
The C/C++ runtime is not a separate language definition.
It is a third runtime-language realization of the same runtime family.
It must remain aligned with:
</p>

<ul>
  <li>the Python consumer,</li>
  <li>the Rust consumer,</li>
  <li>and the same canonical example corridor.</li>
</ul>

<p>
All three consumers may differ in private implementation details,
but they should converge on:
</p>

<ul>
  <li>acceptance criteria,</li>
  <li>loop meaning,</li>
  <li>explicit-state meaning,</li>
  <li>UI binding obligations,</li>
  <li>final public behavior.</li>
</ul>

<hr/>

<h2 id="closure-status">16. C/C++ Closure Status</h2>

<table>
  <thead>
    <tr>
      <th>C/C++-side surface</th>
      <th>Status</th>
      <th>Posture</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Directory-level runtime posture</td>
      <td>Defined</td>
      <td>Architecture and file-role expectations are explicit and backed by a real directory structure.</td>
    </tr>
    <tr>
      <td>Build entry</td>
      <td>Structured</td>
      <td><code>CMakeLists.txt</code> is present.</td>
    </tr>
    <tr>
      <td>Direct example entry surface</td>
      <td>Structured</td>
      <td><code>src/main.cpp</code> is present.</td>
    </tr>
    <tr>
      <td>Contract loading</td>
      <td>Partial repository posture</td>
      <td>Contract-facing header surface exists, but full documented example proof remains to be closed.</td>
    </tr>
    <tr>
      <td>Direct example runner proof</td>
      <td>Not yet closed</td>
      <td>The corridor is structurally visible, but the README-level operational proof is not yet at Python parity.</td>
    </tr>
    <tr>
      <td>Parity with Python and Rust</td>
      <td>Not yet closed</td>
      <td>The target is clear, but observable example-05 parity still needs to be demonstrated.</td>
    </tr>
    <tr>
      <td>Rendered UI host</td>
      <td>Missing as published proof path</td>
      <td>No rendered C/C++ host UI is published yet.</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="future-growth">17. Future Growth</h2>

<ol>
  <li>close contract loading and bounded execution for Example 05 explicitly,</li>
  <li>publish one direct example runner command and one verified run posture,</li>
  <li>add one test suite for contract shape and execution parity,</li>
  <li>align parity checks with Python and Rust,</li>
  <li>integrate with peripheral UI object realization and optional rendered-host work,</li>
  <li>remain clearly separate from LLVM-oriented compiler-family native paths.</li>
</ol>

<hr/>

<h2 id="summary">18. Summary</h2>

<p>
This directory defines the early C/C++ runtime posture for the reference runtime family.
Its purpose is to make implementation freedom repository-visible by proving that the same canonical corridor can be consumed in C or C++ without changing the definition of FROG.
</p>

<p>
The important correction is that this directory is no longer just a theoretical target.
It already has a real repository-visible structure.
What is still missing is the next layer of closure:
a fully documented Example 05 run path, explicit observable parity, and later an optional rendered host path.
</p>
