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
  <li><a href="#runtime-family">3. Reference Runtime Family</a></li>
  <li><a href="#directory-shape">4. Directory Shape</a></li>
  <li><a href="#role-of-each-file-and-subdirectory">5. Role of Each File and Subdirectory</a></li>
  <li><a href="#published-contract">6. Published Reference Contract Artifact</a></li>
  <li><a href="#execution-posture">7. First Execution Posture</a></li>
  <li><a href="#entry-points">8. Published Demonstration Entry Points</a></li>
  <li><a href="#closure-status">9. Runtime Closure Status</a></li>
  <li><a href="#multi-runtime">10. Multi-Runtime Posture</a></li>
  <li><a href="#what-this-directory-owns">11. What This Directory Owns</a></li>
  <li><a href="#what-this-directory-does-not-own">12. What This Directory Does Not Own</a></li>
  <li><a href="#next-closure">13. Next Closure Targets</a></li>
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

<hr/>

<h2 id="status">2. Status</h2>

<p>
This runtime family is non-normative.
It exists to prove that the published repository corridor is no longer only prose.
</p>

<p>
At the current intended structure, this runtime-family directory is also the place where symmetry between runtime languages should become explicit:
</p>

<ul>
  <li>one Python runtime posture,</li>
  <li>one Rust runtime posture,</li>
  <li>one C/C++ runtime posture,</li>
  <li>and optional shared runtime-family helpers at the parent level.</li>
</ul>

<hr/>

<h2 id="runtime-family">3. Reference Runtime Family</h2>

<p>
The first published runtime family is:
</p>

<pre><code>reference_host_runtime_ui_binding
</code></pre>

<p>
A useful initial shape is:
</p>

<ul>
  <li>single-process host execution,</li>
  <li>deterministic step-oriented execution,</li>
  <li>explicit handling of state and commit points,</li>
  <li>basic UI value and UI reference support where declared by the contract.</li>
</ul>

<hr/>

<h2 id="directory-shape">4. Directory Shape</h2>

<pre><code>Implementations/Reference/Runtime/
├── Readme.md
├── accept_contract_and_execute.md
├── reference_runtime.py
├── run_slice05_contract.py
├── python/
│   └── Readme.md
├── rust/
│   ├── Readme.md
│   ├── Cargo.toml
│   └── tests/
│       ├── slice05_contract_smoke.rs
│       └── slice05_execution.rs
└── cpp/
    └── Readme.md
</code></pre>

<hr/>

<h2 id="role-of-each-file-and-subdirectory">5. Role of Each File and Subdirectory</h2>

<ul>
  <li><code>Runtime/Readme.md</code><br/>
      Explains the runtime-family boundary, directory shape, and multi-runtime direction.</li>
  <li><code>accept_contract_and_execute.md</code><br/>
      Non-normative explanation of how accepted contracts are consumed and executed.</li>
  <li><code>reference_runtime.py</code><br/>
      Python-side reference runtime realization for the current bounded corridor.</li>
  <li><code>run_slice05_contract.py</code><br/>
      Python entry point that loads and executes the published contract for example 05.</li>
  <li><code>python/Readme.md</code><br/>
      Python-specific runtime posture and file-role explanation.</li>
  <li><code>rust/Readme.md</code><br/>
      Rust-specific runtime posture and file-role explanation.</li>
  <li><code>rust/Cargo.toml</code><br/>
      Rust package manifest for the Rust runtime consumer.</li>
  <li><code>rust/tests/slice05_contract_smoke.rs</code><br/>
      Contract-shape validation test against the published example-05 contract.</li>
  <li><code>rust/tests/slice05_execution.rs</code><br/>
      Execution test proving bounded accumulation behavior and parity with the Python path.</li>
  <li><code>cpp/Readme.md</code><br/>
      C/C++ runtime target posture for the same canonical corridor.</li>
</ul>

<hr/>

<h2 id="published-contract">6. Published Reference Contract Artifact</h2>

<p>
The first named executable slice has a repository-visible backend contract artifact:
</p>

<pre><code>Implementations/Reference/ContractEmitter/examples/
└── 05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json
</code></pre>

<p>
That artifact is the published handoff surface this runtime family consumes for the bounded applicative vertical slice:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/
</code></pre>

<hr/>

<h2 id="execution-posture">7. First Execution Posture</h2>

<p>
The first execution posture is intentionally bounded.
It is designed for the first named applicative vertical slice, not for the full future FROG runtime surface.
</p>

<p>
The current bounded corridor already supports:
</p>

<ul>
  <li>one public input value sampled from the control binding,</li>
  <li>one bounded loop of exactly five iterations,</li>
  <li>one explicit state cell initialized to zero,</li>
  <li>one final public result publication,</li>
  <li>one indicator publication path,</li>
  <li>and minimal object-style UI property writes for <code>face_color</code>.</li>
</ul>

<hr/>

<h2 id="entry-points">8. Published Demonstration Entry Points</h2>

<p>
This directory already contains repository-visible entry points that exercise the published contract artifact directly rather than through a private simplified schema.
</p>

<pre><code>Python direct execution
python -m Implementations.Reference.Runtime.run_slice05_contract 3
</code></pre>

<pre><code>Rust verification
cd Implementations/Reference/Runtime/rust
cargo test
</code></pre>

<p>
The intended future symmetry is:
</p>

<pre><code>Python
   -> direct example runner

Rust
   -> direct example runner plus tests

C/C++
   -> direct example runner plus tests where useful
</code></pre>

<hr/>

<h2 id="closure-status">9. Runtime Closure Status</h2>

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
      <td>Closed</td>
      <td>Runnable entry point is published.</td>
    </tr>
    <tr>
      <td>Rust consumer</td>
      <td>Partial-to-closed</td>
      <td>Execution proof exists through tests, but not yet through one dedicated example runner binary.</td>
    </tr>
    <tr>
      <td>C/C++ consumer</td>
      <td>Missing</td>
      <td>No published consumer exists yet.</td>
    </tr>
    <tr>
      <td>Rendered host UI</td>
      <td>Missing</td>
      <td>UI runtime state is exposed in output artifacts, but no rendered host UI exists yet.</td>
    </tr>
    <tr>
      <td>LLVM-oriented native path</td>
      <td>Downstream and separate</td>
      <td>Belongs to a compiler-family corridor, not to the runtime-family definition itself.</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="multi-runtime">10. Multi-Runtime Posture</h2>

<p>
This directory defines a runtime-family boundary, not a single mandatory runtime language.
</p>

<p>
Where the reference implementation publishes multiple runtime realizations, such as:
</p>

<ul>
  <li>a Python realization,</li>
  <li>a Rust realization,</li>
  <li>and later a C/C++ realization,</li>
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
  <li>and public result publication obligations.</li>
</ul>

<hr/>

<h2 id="what-this-directory-owns">11. What This Directory Owns</h2>

<ul>
  <li>private execution realization of accepted backend contracts,</li>
  <li>state management for the reference family,</li>
  <li>family-specific runtime objects,</li>
  <li>family-specific scheduling mechanics,</li>
  <li>runtime-private UI binding helpers for the accepted subset,</li>
  <li>and runtime-private success / failure reporting.</li>
</ul>

<hr/>

<h2 id="what-this-directory-does-not-own">12. What This Directory Does Not Own</h2>

<ul>
  <li>the language,</li>
  <li>the canonical <code>.frog</code> source model,</li>
  <li>the semantic acceptance boundary,</li>
  <li>the FIR / execution-facing layer,</li>
  <li>the lowering boundary,</li>
  <li>the backend contract boundary,</li>
  <li>the normative meaning of UI constructs,</li>
  <li>or the structural-validation boundary.</li>
</ul>

<pre><code>validated meaning != runtime implementation
backend contract != runtime-private structures
reference runtime != universal FROG runtime
</code></pre>

<hr/>

<h2 id="next-closure">13. Next Closure Targets</h2>

<ol>
  <li>publish one explicit C/C++ consumer for the same example corridor,</li>
  <li>publish one dedicated Rust runner command in addition to the tests,</li>
  <li>publish one distinct peripheral UI object realization file,</li>
  <li>publish one rendered front-panel host path,</li>
  <li>and align runtime-family consumption with an optional downstream LLVM-oriented native executable corridor.</li>
</ol>

<hr/>

<h2 id="summary">14. Summary</h2>

<p>
The reference runtime is the first private consumer-side realization of the reference backend family.
It proves executability, but it does not become the language definition.
</p>

<p>
The current closure direction is to make the same canonical example corridor visibly consumable through Python, Rust, and C/C++ while preserving that runtime families remain downstream from source, meaning, FIR, lowering, and backend handoff.
</p>
