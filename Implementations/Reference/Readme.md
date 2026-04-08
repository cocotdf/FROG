<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Reference Implementation Workspace</h1>

<p align="center">
  <strong>Non-normative executable workspace for inspecting and exercising the published FROG corridor from source to contract to runtime and native-path consumption</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#non-normative-status">2. Non-Normative Status</a></li>
  <li><a href="#why-this-directory-exists">3. Why This Directory Exists</a></li>
  <li><a href="#architectural-position">4. Architectural Position</a></li>
  <li><a href="#published-workspace-shape">5. Published Workspace Shape</a></li>
  <li><a href="#useful-file-tree">6. Useful File Tree</a></li>
  <li><a href="#file-responsibilities">7. File Responsibilities</a></li>
  <li><a href="#first-bounded-executable-corridor">8. First Bounded Executable Corridor</a></li>
  <li><a href="#what-this-workspace-owns">9. What This Workspace Owns</a></li>
  <li><a href="#what-this-workspace-does-not-own">10. What This Workspace Does Not Own</a></li>
  <li><a href="#stage-separation-discipline">11. Stage-Separation Discipline</a></li>
  <li><a href="#example-contract-runtime-reading">12. Example → Contract → Runtime Reading</a></li>
  <li><a href="#multi-runtime-posture">13. Multi-Runtime Posture</a></li>
  <li><a href="#native-path-posture">14. Native Path Posture</a></li>
  <li><a href="#design-rules">15. Design Rules</a></li>
  <li><a href="#summary">16. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory contains the non-normative reference implementation workspace for FROG.
It exists to make selected repository-visible corridors executable and inspectable without turning implementation convenience into normative language law.
</p>

<p>
The workspace is intentionally stage-separated.
It is not a monolithic hidden compiler/runtime product.
It is a repository-visible execution workspace that consumes the published specification layers through explicit intermediate boundaries.
</p>

<hr/>

<h2 id="non-normative-status">2. Non-Normative Status</h2>

<p>
This workspace is <strong>non-normative</strong>.
It is not the definition of FROG.
It is not the owner of source law, semantic law, FIR law, lowering law, or backend-contract law.
</p>

<p>
Its role is to demonstrate that the published repository can already support bounded executable corridors through inspectable reference-family components.
</p>

<hr/>

<h2 id="why-this-directory-exists">3. Why This Directory Exists</h2>

<p>
A serious open language repository should be able to expose more than prose-only architecture.
It should also be able to show that at least one bounded slice can be carried through executable downstream stages without collapsing the language into one private implementation.
</p>

<p>
This workspace therefore exists to:
</p>

<ul>
  <li>load canonical source artifacts where relevant,</li>
  <li>exercise structural and semantic checks in reference form where relevant,</li>
  <li>derive or consume execution-facing representations in reference form,</li>
  <li>lower into backend-facing reference-family forms,</li>
  <li>emit consumer-facing backend contracts,</li>
  <li>execute selected bounded slices through explicit runtime consumers,</li>
  <li>and prepare native compiler-oriented downstream paths where declared.</li>
</ul>

<hr/>

<h2 id="architectural-position">4. Architectural Position</h2>

<pre><code>canonical .frog source
      |
      v
published structural + semantic boundaries
      |
      v
published FIR / execution-facing posture
      |
      v
published lowering posture
      |
      v
reference implementation stages
      |
      +-- Loader/
      +-- Validator/
      +-- Deriver/
      +-- Lowerer/
      +-- ContractEmitter/
      +-- Runtime/
      \-- LLVM/
</code></pre>

<p>
The key rule is that this workspace follows the published corridor.
It does not silently replace it.
</p>

<hr/>

<h2 id="published-workspace-shape">5. Published Workspace Shape</h2>

<p>
The reference workspace is organized as explicit stage-separated areas, including:
</p>

<ul>
  <li><code>ContractEmitter/</code></li>
  <li><code>Runtime/</code></li>
  <li><code>LLVM/</code></li>
</ul>

<p>
Other stage names such as <code>Loader/</code>, <code>Validator/</code>, <code>Deriver/</code>, and <code>Lowerer/</code> remain part of the intended reference corridor vocabulary even when repository-visible material is not yet equally developed for each one.
</p>

<hr/>

<h2 id="useful-file-tree">6. Useful File Tree</h2>

<pre><code>Implementations/
└── Reference/
    ├── Readme.md
    ├── ContractEmitter/
    │   ├── Readme.md
    │   └── examples/
    │       └── 05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json
    ├── Runtime/
    │   ├── Readme.md
    │   ├── reference_runtime.py
    │   ├── run_slice05_contract.py
    │   ├── python/
    │   │   └── Readme.md
    │   ├── rust/
    │   │   ├── Readme.md
    │   │   ├── Cargo.toml
    │   │   └── tests/
    │   │       ├── slice05_contract_smoke.rs
    │   │       └── slice05_execution.rs
    │   └── cpp/
    │       └── Readme.md
    └── LLVM/
        └── Readme.md
</code></pre>

<hr/>

<h2 id="file-responsibilities">7. File Responsibilities</h2>

<ul>
  <li><code>Implementations/Reference/Readme.md</code><br/>
      Directory-level entry point for the non-normative reference workspace.</li>
  <li><code>Implementations/Reference/ContractEmitter/</code><br/>
      Reference-family backend handoff materialization surface for emitted contracts.</li>
  <li><code>Implementations/Reference/ContractEmitter/examples/...</code><br/>
      Published backend-family contract artifacts attributable to named examples.</li>
  <li><code>Implementations/Reference/Runtime/</code><br/>
      Shared runtime-family surface for downstream runtime consumers.</li>
  <li><code>Implementations/Reference/Runtime/python/</code><br/>
      Dedicated Python mini-runtime posture and future implementation home.</li>
  <li><code>Implementations/Reference/Runtime/rust/</code><br/>
      Rust mini-runtime consumer posture and published Rust-side test-driven proof.</li>
  <li><code>Implementations/Reference/Runtime/cpp/</code><br/>
      Planned C/C++ mini-runtime consumer posture for parity with Python and Rust.</li>
  <li><code>Implementations/Reference/LLVM/</code><br/>
      LLVM-oriented native executable path posture, kept distinct from runtime families.</li>
</ul>

<hr/>

<h2 id="first-bounded-executable-corridor">8. First Bounded Executable Corridor</h2>

<p>
The first repository-visible bounded executable corridor is centered on:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/</code></pre>

<p>
The corresponding repository-visible reference-family backend contract artifact is:
</p>

<pre><code>Implementations/Reference/ContractEmitter/examples/
└── 05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json</code></pre>

<p>
That contract is then consumed downstream by the reference runtime family under:
</p>

<pre><code>Implementations/Reference/Runtime/</code></pre>

<p>
This makes the first bounded executable corridor inspectable as:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/
      |
      v
ContractEmitter/examples/
05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json
      |
      +------------------------------+------------------------------+------------------------------+
      |                              |                              |
      v                              v                              v
Runtime/python/                Runtime/rust/                 Runtime/cpp/
      |
      \----------------------------------------- LLVM/ ------------------------------------------&gt;
</code></pre>

<hr/>

<h2 id="what-this-workspace-owns">9. What This Workspace Owns</h2>

<ul>
  <li>reference-family executable staging,</li>
  <li>reference-family loading, validation, derivation, lowering, and contract-emission mechanics where implemented,</li>
  <li>reference-family runtime consumption of accepted backend contracts,</li>
  <li>reference-family native compiler-oriented downstream experiments,</li>
  <li>and repository-visible executable artifacts used to exercise selected named slices.</li>
</ul>

<hr/>

<h2 id="what-this-workspace-does-not-own">10. What This Workspace Does Not Own</h2>

<ul>
  <li>the canonical <code>.frog</code> source model,</li>
  <li>the normative structural-validation boundary,</li>
  <li>the normative semantic-acceptance boundary,</li>
  <li>the normative FIR boundary,</li>
  <li>the normative backend-contract boundary,</li>
  <li>the universal runtime architecture for all future implementations,</li>
  <li>the universal native compiler path for all future implementations,</li>
  <li>or the universal UI toolkit/object model for all future hosts.</li>
</ul>

<pre><code>example source != emitted contract
emitted contract != runtime-private realization
runtime-family consumer != universal FROG runtime
LLVM-native path != definition of FROG
</code></pre>

<hr/>

<h2 id="stage-separation-discipline">11. Stage-Separation Discipline</h2>

<p>
Each stage in this workspace should remain explicit about its ownership boundary.
</p>

<ul>
  <li><strong>ContractEmitter</strong> materializes backend contract artifacts.</li>
  <li><strong>Runtime</strong> privately consumes accepted contract artifacts through runtime families.</li>
  <li><strong>LLVM</strong> explores native compiler-oriented downstream consumption.</li>
</ul>

<p>
That separation keeps the corridor attributable.
It also makes it easier to inspect where a failure belongs:
source problem,
validation problem,
derivation problem,
lowering problem,
contract-emission problem,
runtime-consumption problem,
or native-compilation problem.
</p>

<hr/>

<h2 id="example-contract-runtime-reading">12. Example → Contract → Runtime Reading</h2>

<p>
For the first bounded executable slice, the recommended reading order is:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/
      |
      v
Implementations/Reference/ContractEmitter/examples/
05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json
      |
      v
Implementations/Reference/Runtime/
      |
      +-- python/
      +-- rust/
      \-- cpp/
      |
      \-- Implementations/Reference/LLVM/
</code></pre>

<hr/>

<h2 id="multi-runtime-posture">13. Multi-Runtime Posture</h2>

<p>
This workspace supports the intended rule that one runtime must not become the definition of FROG.
</p>

<p>
Within the reference family, multiple runtime language realizations may coexist, for example:
</p>

<ul>
  <li>a Python realization,</li>
  <li>a Rust realization,</li>
  <li>a C/C++ realization.</li>
</ul>

<p>
Those runtimes should remain parallel consumers of the same emitted contract family for the same named slice.
They may differ in private structures or host mechanics,
but they should stay aligned on declared contract obligations.
</p>

<hr/>

<h2 id="native-path-posture">14. Native Path Posture</h2>

<p>
The reference workspace also needs to preserve a distinct downstream path for native compiler-oriented closure.
That path should remain separate from runtime-family consumers.
</p>

<p>
Its intended reading is:
</p>

<pre><code>canonical example corridor
   -&gt; FIR posture
   -&gt; lowering posture
   -&gt; compiler-facing lowered artifact
   -&gt; LLVM-oriented downstream compilation
   -&gt; native executable
</code></pre>

<p>
That corridor is not yet fully closed in the published repository for example 05.
The architectural distinction nevertheless needs to remain visible now.
</p>

<hr/>

<h2 id="design-rules">15. Design Rules</h2>

<ul>
  <li>Keep stage boundaries explicit.</li>
  <li>Do not hide undeclared assumptions across stages.</li>
  <li>Do not erase loop, state, or UI-participation meaning when the bounded corridor depends on them.</li>
  <li>Do not treat runtime-private convenience as normative specification truth.</li>
  <li>Keep emitted artifacts attributable to named example slices.</li>
  <li>Keep runtime families parallel rather than hierarchical.</li>
  <li>Keep LLVM-native work downstream from FROG rather than redefining it.</li>
</ul>

<hr/>

<h2 id="summary">16. Summary</h2>

<p>
This directory is the non-normative executable workspace for the FROG reference family.
Its purpose is to exercise bounded published corridors through explicit reference stages without collapsing the language into one implementation.
</p>

<p>
The first repository-visible executable corridor is now materially readable across:
</p>

<ul>
  <li><code>Examples/05_bounded_ui_accumulator/</code>,</li>
  <li><code>Implementations/Reference/ContractEmitter/examples/05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json</code>,</li>
  <li><code>Implementations/Reference/Runtime/</code>,</li>
  <li><code>Implementations/Reference/LLVM/</code> as native-path direction.</li>
</ul>
