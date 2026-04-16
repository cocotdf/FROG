<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Reference Runtime</h1>

<p align="center">
  <strong>Runtime-family consumers for the non-normative FROG reference implementation</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#status">2. Status</a></li>
  <li><a href="#reference-runtime-family">3. Reference Runtime Family</a></li>
  <li><a href="#current-published-directory-shape">4. Current Published Directory Shape</a></li>
  <li><a href="#role-of-each-file-and-subdirectory">5. Role of Each File and Subdirectory</a></li>
  <li><a href="#published-reference-contract-artifact">6. Published Reference Contract Artifact</a></li>
  <li><a href="#first-execution-posture">7. First Execution Posture</a></li>
  <li><a href="#published-demonstration-entry-points">8. Published Demonstration Entry Points</a></li>
  <li><a href="#runtime-closure-status">9. Runtime Closure Status</a></li>
  <li><a href="#multi-runtime-posture">10. Multi-Runtime Posture</a></li>
  <li><a href="#what-this-directory-owns">11. What This Directory Owns</a></li>
  <li><a href="#what-this-directory-does-not-own">12. What This Directory Does Not Own</a></li>
  <li><a href="#next-closure-targets">13. Next Closure Targets</a></li>
  <li><a href="#summary">14. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>
<p>
This directory contains runtime-family consumers of backend contracts in the non-normative FROG reference implementation.
Its role is to accept a contract for one selected backend family and realize execution privately while staying faithful to the declared contract obligations.
</p>

<p>
The runtime therefore begins downstream from canonical source, validation, semantic interpretation, FIR-target execution-facing derivation, lowering, and backend contract emission.
It consumes published backend contract artifacts.
It does not replace or absorb the layers that produced those contracts.
</p>

<p>
At the current published state, this parent directory acts as the visible coordination point for:
</p>

<ul>
  <li>shared runtime-family posture at parent level,</li>
  <li>a Python consumer family,</li>
  <li>a Rust consumer family,</li>
  <li>a C/C++ consumer family.</li>
</ul>

<hr/>

<h2 id="status">2. Status</h2>
<p>
This runtime family is non-normative.
It exists to prove that the published repository corridor is not only documentation.
</p>

<p>
At the current published structure, multi-runtime symmetry is visible at repository level:
</p>

<ul>
  <li>one Python runtime posture with contract execution, UI runtime files, CLI, and tests,</li>
  <li>one Rust runtime posture with manifest, source split, and tests,</li>
  <li>one C/C++ runtime posture with build entry, headers, and direct example execution entry point,</li>
  <li>optional shared runtime-family helpers at the parent level.</li>
</ul>

<p>
The maturity level is still not perfectly symmetrical across languages.
Python is the most operational host-facing path.
Rust is the strongest secondary parity-verification path.
C/C++ is a real narrow direct-runner posture for Example 05.
</p>

<hr/>

<h2 id="reference-runtime-family">3. Reference Runtime Family</h2>
<p>
The first published runtime family is:
</p>

<pre><code>reference_host_runtime_ui_binding</code></pre>

<p>
A useful initial shape is:
</p>

<ul>
  <li>single-process host execution,</li>
  <li>deterministic step-oriented execution,</li>
  <li>explicit handling of state and commit points,</li>
  <li>basic UI value and UI reference support where declared by the contract.</li>
</ul>

<p>
This family should be understood as a backend-family consumer posture, not as a language-definition layer.
</p>

<hr/>

<h2 id="current-published-directory-shape">4. Current Published Directory Shape</h2>
<pre><code>Implementations/Reference/Runtime/
├── Readme.md
├── accept_contract_and_execute.md
├── reference_runtime.py
├── responsibilities.md
├── run_slice05_contract.py
├── python/
│   ├── Readme.md
│   ├── cli.py
│   ├── execute_contract.py
│   ├── run_slice05_ui.py
│   ├── runtime_core.py
│   ├── ui_runtime.py
│   └── tests/
│       ├── test_slice05_contract.py
│       └── test_slice05_ui_runtime.py
├── rust/
│   ├── Readme.md
│   ├── Cargo.toml
│   ├── src/
│   │   ├── cli.rs
│   │   ├── contract.rs
│   │   ├── diagnostics.rs
│   │   ├── execute.rs
│   │   ├── lib.rs
│   │   ├── main.rs
│   │   ├── runtime.rs
│   │   └── ui.rs
│   └── tests/
│       ├── slice05_contract_smoke.rs
│       └── slice05_execution.rs
└── cpp/
    ├── Readme.md
    ├── CMakeLists.txt
    ├── include/
    │   ├── contract.hpp
    │   ├── execute.hpp
    │   ├── runtime.hpp
    │   └── ui.hpp
    └── src/
        └── main.cpp
</code></pre>

<p>
This matters because the runtime-family posture is materially visible in the published tree rather than only described abstractly.
</p>

<hr/>

<h2 id="role-of-each-file-and-subdirectory">5. Role of Each File and Subdirectory</h2>
<ul>
  <li><code>Runtime/Readme.md</code><br/>
      Explains the runtime-family boundary, directory shape, and multi-runtime posture.</li>

  <li><code>accept_contract_and_execute.md</code><br/>
      Non-normative explanation of how accepted contracts are consumed and executed.</li>

  <li><code>reference_runtime.py</code><br/>
      Parent-level Python-side reference runtime realization for the current bounded corridor.</li>

  <li><code>responsibilities.md</code><br/>
      Parent-level runtime-family responsibility clarification surface.</li>

  <li><code>run_slice05_contract.py</code><br/>
      Python entry point that loads and executes the published contract for Example 05.</li>

  <li><code>python/</code><br/>
      Python-specific runtime posture with runtime core, contract execution helpers, rendered UI runner, CLI, and Python-side tests.</li>

  <li><code>rust/</code><br/>
      Rust-specific runtime posture with Cargo manifest, explicit <code>src/</code> split, and test-driven corridor verification.</li>

  <li><code>cpp/</code><br/>
      C/C++ runtime posture with CMake entry, header surfaces, and direct source entry point for the same canonical corridor.</li>
</ul>

<p>
The important parent-level point is that this directory holds both:
</p>

<ul>
  <li>shared runtime-family material,</li>
  <li>parallel language-specific runtime consumers.</li>
</ul>

<hr/>

<h2 id="published-reference-contract-artifact">6. Published Reference Contract Artifact</h2>
<p>
The first named executable slice has a repository-visible backend contract artifact:
</p>

<pre><code>Implementations/Reference/ContractEmitter/examples/
└── 05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json
</code></pre>

<p>
That artifact is the published handoff surface this runtime family consumes for the bounded vertical slice:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/</code></pre>

<p>
The runtime-family posture should therefore be read as:
</p>

<pre><code>canonical source
  -&gt; validation and semantic acceptance
  -&gt; FIR
  -&gt; lowering
  -&gt; backend-family contract
  -&gt; runtime-family consumer
</code></pre>

<hr/>

<h2 id="first-execution-posture">7. First Execution Posture</h2>
<p>
The first execution posture is intentionally bounded.
It is designed for the first named vertical slice, not for the full future FROG runtime surface.
</p>

<p>
The current bounded corridor supports:
</p>

<ul>
  <li>one public input value sampled from the control binding,</li>
  <li>one bounded loop of exactly five iterations,</li>
  <li>one explicit state cell initialized to zero,</li>
  <li>one final public result publication,</li>
  <li>one indicator publication path,</li>
  <li>bounded object-style UI property writes for <code>foreground_color</code>.</li>
</ul>

<p>
For Example 05, the strongest rendered-host proof path currently exists on the Python side, while Rust and C/C++ provide additional contract-faithful execution proof paths with different closure styles.
</p>

<hr/>

<h2 id="published-demonstration-entry-points">8. Published Demonstration Entry Points</h2>
<p>
This directory already contains repository-visible entry points that exercise the published contract artifact directly rather than through a private simplified schema.
</p>

<pre><code>Python direct contract execution
python -m Implementations.Reference.Runtime.run_slice05_contract 3
</code></pre>

<pre><code>Python rendered UI execution
python Implementations/Reference/Runtime/python/run_slice05_ui.py 3 --autorun
</code></pre>

<pre><code>Rust verification
cd Implementations/Reference/Runtime/rust
cargo test
</code></pre>

<pre><code>C/C++ direct example execution
cmake -S Implementations/Reference/Runtime/cpp -B build/frog_runtime_cpp
cmake --build build/frog_runtime_cpp
build/frog_runtime_cpp/frog_runtime_cpp_example05 3
</code></pre>

<p>
The intended long-term symmetry is:
</p>

<pre><code>Python
   -&gt; direct example runner
   -&gt; rendered UI runner

Rust
   -&gt; direct runner posture and tests

C/C++
   -&gt; direct runner posture and tests where useful
</code></pre>

<p>
At the current published state, Python remains the most operational host-facing path, Rust is the strongest secondary parity-verification path, and C/C++ is a real narrow operational proof path for Example 05 rather than only a structural placeholder.
</p>

<hr/>

<h2 id="runtime-closure-status">9. Runtime Closure Status</h2>
<table>
  <thead>
    <tr>
      <th>Runtime family surface</th>
      <th>Status</th>
      <th>Published posture</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Family definition posture</td>
      <td>Closed enough for the first slice</td>
      <td><code>reference_host_runtime_ui_binding</code> is explicit.</td>
    </tr>
    <tr>
      <td>Python consumer</td>
      <td>Most operational</td>
      <td>Contract runner, rendered UI runner, runtime core, CLI, and tests are published.</td>
    </tr>
    <tr>
      <td>Rust consumer</td>
      <td>Structured and partially closed</td>
      <td>Manifest, source split, and test-driven execution proof are published.</td>
    </tr>
    <tr>
      <td>C/C++ consumer</td>
      <td>Narrow direct runner posture</td>
      <td>Build entry, headers, and source entry point are published and support the direct Example 05 run corridor.</td>
    </tr>
    <tr>
      <td>Rendered host UI</td>
      <td>Partially closed</td>
      <td>A rendered host path exists on Python for the bounded Example 05 subset.</td>
    </tr>
    <tr>
      <td>LLVM-oriented native path</td>
      <td>Downstream and separate</td>
      <td>Belongs to a compiler-family corridor, not to the runtime-family definition itself.</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="multi-runtime-posture">10. Multi-Runtime Posture</h2>
<p>
This directory defines a runtime-family boundary, not a single mandatory runtime language.
</p>

<p>
Where the reference implementation publishes multiple runtime realizations, such as:
</p>

<ul>
  <li>a Python realization,</li>
  <li>a Rust realization,</li>
  <li>a C/C++ realization,</li>
</ul>

<p>
those runtimes must be understood as parallel consumers of the same published corridor.
They may differ in private structures and host mechanics, but they should remain aligned on:
</p>

<ul>
  <li>contract acceptance criteria,</li>
  <li>explicit-state meaning,</li>
  <li>bounded loop meaning,</li>
  <li>UI binding obligations declared by the contract,</li>
  <li>public result publication obligations.</li>
</ul>

<p>
The parent directory exists precisely to make that parallel-consumer posture explicit.
</p>

<hr/>

<h2 id="what-this-directory-owns">11. What This Directory Owns</h2>
<ul>
  <li>private execution realization of accepted backend contracts,</li>
  <li>state management for the reference family,</li>
  <li>family-specific runtime objects,</li>
  <li>family-specific scheduling mechanics,</li>
  <li>runtime-private UI binding helpers for the accepted subset,</li>
  <li>runtime-private success and failure reporting,</li>
  <li>parent-level coordination of parallel runtime-language consumers.</li>
</ul>

<hr/>

<h2 id="what-this-directory-does-not-own">12. What This Directory Does Not Own</h2>
<ul>
  <li>the language,</li>
  <li>the canonical <code>.frog</code> source model,</li>
  <li>the semantic acceptance boundary,</li>
  <li>the FIR layer,</li>
  <li>the lowering boundary,</li>
  <li>the backend contract boundary,</li>
  <li>the normative meaning of UI constructs,</li>
  <li>the structural-validation boundary.</li>
</ul>

<pre><code>validated meaning != runtime implementation
backend contract != runtime-private structures
reference runtime != universal FROG runtime
</code></pre>

<hr/>

<h2 id="next-closure-targets">13. Next Closure Targets</h2>
<ol>
  <li>publish one clearer direct Rust runner posture in addition to the tests,</li>
  <li>tighten the relation between the Python rendered path and the contract-driven path,</li>
  <li>add C/C++ test posture where useful for parity automation,</li>
  <li>keep runtime-family consumers aligned with the same example-local artifact set,</li>
  <li>maintain clean separation from the downstream LLVM-oriented native executable corridor.</li>
</ol>

<hr/>

<h2 id="summary">14. Summary</h2>
<p>
The reference runtime is the first private consumer-side realization of the reference backend family.
It proves executability, but it does not become the language definition.
</p>

<p>
The important correction at the current published state is that the multi-runtime posture is no longer only an aspiration.
It is already visible in the repository tree through Python, Rust, and C/C++ consumer directories with distinct but real closure levels.
</p>

<p>
The current closure direction is therefore:
</p>

<ul>
  <li>keep the same canonical example corridor consumable through several runtime languages,</li>
  <li>raise Rust toward a stronger direct-runner posture while keeping C/C++ aligned,</li>
  <li>preserve the architectural rule that runtime families remain downstream from source, meaning, FIR, lowering, and backend handoff.</li>
</ul>
