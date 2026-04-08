<p align="center">
  <img src="../../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Reference Runtime (C/C++)</h1>

<p align="center">
  <strong>Target C/C++ consumer for the reference runtime family in the non-normative FROG reference implementation</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-directory-should-exist">2. Why This Directory Should Exist</a></li>
  <li><a href="#directory-shape">3. Directory Shape</a></li>
  <li><a href="#role-of-each-file">4. Role of Each File</a></li>
  <li><a href="#primary-slice-target">5. Primary Slice Target</a></li>
  <li><a href="#relation-with-runtime-boundary">6. Relation to the Runtime Boundary</a></li>
  <li><a href="#what-this-runtime-should-consume">7. What This Runtime Should Consume</a></li>
  <li><a href="#what-this-runtime-should-produce">8. What This Runtime Should Produce</a></li>
  <li><a href="#target-pipe">9. Target Pipe for Example 05</a></li>
  <li><a href="#design-rules">10. Design Rules</a></li>
  <li><a href="#relationship-with-python-and-rust">11. Relationship with Python and Rust Consumers</a></li>
  <li><a href="#closure-status">12. C/C++ Closure Status</a></li>
  <li><a href="#future-growth">13. Future Growth</a></li>
  <li><a href="#summary">14. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the target C/C++ realization of the published reference runtime boundary for the FROG reference implementation.
It is a downstream runtime consumer.
Its role is to prove that the same canonical example corridor can be consumed in C or C++ without changing the language definition.
</p>

<hr/>

<h2 id="why-this-directory-should-exist">2. Why This Directory Should Exist</h2>

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

<hr/>

<h2 id="directory-shape">3. Directory Shape</h2>

<pre><code>Implementations/Reference/Runtime/cpp/
├── Readme.md
├── CMakeLists.txt
├── include/
│   ├── contract.hpp
│   ├── runtime.hpp
│   ├── execute.hpp
│   └── ui.hpp
├── src/
│   ├── main.cpp
│   ├── contract.cpp
│   ├── runtime.cpp
│   ├── execute.cpp
│   └── ui.cpp
└── tests/
    ├── slice05_contract_smoke.cpp
    └── slice05_execution.cpp
</code></pre>

<hr/>

<h2 id="role-of-each-file">4. Role of Each File</h2>

<ul>
  <li><code>Readme.md</code><br/>
      Explains the C/C++-side runtime posture and the role of this directory.</li>
  <li><code>CMakeLists.txt</code><br/>
      Build-system entry point for the C/C++ mini runtime and example consumers.</li>
  <li><code>include/contract.hpp</code><br/>
      Contract-loading declarations and data structures.</li>
  <li><code>include/runtime.hpp</code><br/>
      Runtime state declarations.</li>
  <li><code>include/execute.hpp</code><br/>
      Execution interface for accepted contracts.</li>
  <li><code>include/ui.hpp</code><br/>
      UI binding declarations for the supported subset.</li>
  <li><code>src/main.cpp</code><br/>
      Direct example runner entry point for bounded contract execution.</li>
  <li><code>src/contract.cpp</code><br/>
      Contract loading and contract-shape logic.</li>
  <li><code>src/runtime.cpp</code><br/>
      Runtime state and scheduling logic.</li>
  <li><code>src/execute.cpp</code><br/>
      Bounded execution logic for accepted contracts.</li>
  <li><code>src/ui.cpp</code><br/>
      Minimal widget-value and widget-reference handling for the supported subset.</li>
  <li><code>tests/slice05_contract_smoke.cpp</code><br/>
      Contract-shape validation test for the example-05 contract artifact.</li>
  <li><code>tests/slice05_execution.cpp</code><br/>
      Execution test proving bounded accumulation behavior and parity with Python and Rust.</li>
</ul>

<hr/>

<h2 id="primary-slice-target">5. Primary Slice Target</h2>

<p>
The first target for this runtime should be the published example:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/</code></pre>

<p>
This C/C++ runtime should consume the same corridor already consumed by the Python and Rust paths.
It must not introduce a separate source example, a parallel semantic story, or a runtime-only reinterpretation of the example.
</p>

<hr/>

<h2 id="relation-with-runtime-boundary">6. Relation to the Runtime Boundary</h2>

<p>
The published runtime family is:
</p>

<pre><code>reference_host_runtime_ui_binding
</code></pre>

<p>
This C/C++ runtime should be one consumer of that family posture.
It should follow the same runtime-side assumptions as the Python and Rust consumers.
</p>

<hr/>

<h2 id="what-this-runtime-should-consume">7. What This Runtime Should Consume</h2>

<p>
This C/C++ runtime should start after source loading, structural validation, semantic validation, FIR-target derivation, and lowering have already produced an acceptable backend contract.
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
  <li>one indicator/public-output publication rule,</li>
  <li>and one minimal <code>face_color</code> property-write surface.</li>
</ul>

<hr/>

<h2 id="what-this-runtime-should-produce">8. What This Runtime Should Produce</h2>

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
  <li>and the minimal UI runtime state is preserved for the supported widgets.</li>
</ul>

<hr/>

<h2 id="target-pipe">9. Target Pipe for Example 05</h2>

<p>
The target direct build-and-run posture is:
</p>

<pre><code>cmake -S Implementations/Reference/Runtime/cpp -B build/frog_runtime_cpp
cmake --build build/frog_runtime_cpp
build/frog_runtime_cpp/frog_runtime_cpp_example05 3
</code></pre>

<p>
The target test posture is:
</p>

<pre><code>ctest --test-dir build/frog_runtime_cpp
</code></pre>

<p>
These commands are target posture for the directory.
They become materially valid once the C/C++ consumer is implemented.
</p>

<hr/>

<h2 id="design-rules">10. Design Rules</h2>

<ul>
  <li>Accept or reject contracts explicitly.</li>
  <li>Do not silently reinterpret undeclared assumptions.</li>
  <li>Keep explicit local-memory meaning visible in runtime execution.</li>
  <li>Keep loop iteration count explicit where the contract declares it.</li>
  <li>Keep runtime-private helper structures downstream from the published backend contract.</li>
  <li>Reject unsupported widget-reference or property-write operations explicitly.</li>
  <li>Do not let low-level implementation convenience become semantic law.</li>
</ul>

<hr/>

<h2 id="relationship-with-python-and-rust">11. Relationship with Python and Rust Consumers</h2>

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

<hr/>

<h2 id="closure-status">12. C/C++ Closure Status</h2>

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
      <td>Directory-level target posture</td>
      <td>Defined here</td>
      <td>Architecture and file-role expectations are explicit.</td>
    </tr>
    <tr>
      <td>Contract loading</td>
      <td>Missing</td>
      <td>Implementation not yet published.</td>
    </tr>
    <tr>
      <td>Direct example runner</td>
      <td>Missing</td>
      <td>Implementation not yet published.</td>
    </tr>
    <tr>
      <td>Parity with Python and Rust</td>
      <td>Missing</td>
      <td>Will be achieved when the same corridor is consumed successfully.</td>
    </tr>
    <tr>
      <td>Rendered UI host</td>
      <td>Missing</td>
      <td>No rendered C/C++ host UI is published yet.</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="future-growth">13. Future Growth</h2>

<ol>
  <li>implement contract loading and bounded execution for example 05,</li>
  <li>add one direct example runner and one test suite,</li>
  <li>align parity checks with Python and Rust,</li>
  <li>integrate with peripheral UI object realization and optional rendered host work,</li>
  <li>and remain clearly separate from LLVM-oriented compiler-family native paths.</li>
</ol>

<hr/>

<h2 id="summary">14. Summary</h2>

<p>
This directory defines the target C/C++ runtime posture for the reference runtime family.
Its purpose is to make implementation freedom repository-visible by proving that the same canonical corridor can be consumed in C or C++ without changing the definition of FROG.
</p>
