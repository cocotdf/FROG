<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Reference LLVM-Oriented Path</h1>

<p align="center">
  <strong>Downstream compiler-family posture for native executable closure in the non-normative FROG reference implementation</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-directory-should-exist">2. Why This Directory Should Exist</a></li>
  <li><a href="#architectural-boundary">3. Architectural Boundary</a></li>
  <li><a href="#directory-shape">4. Directory Shape</a></li>
  <li><a href="#role-of-each-file">5. Role of Each File</a></li>
  <li><a href="#target-corridor">6. Target Corridor</a></li>
  <li><a href="#what-this-directory-owns">7. What This Directory Owns</a></li>
  <li><a href="#what-this-directory-does-not-own">8. What This Directory Does Not Own</a></li>
  <li><a href="#example-facing-posture">9. Example-Facing Posture</a></li>
  <li><a href="#design-rules">10. Design Rules</a></li>
  <li><a href="#closure-status">11. LLVM Closure Status</a></li>
  <li><a href="#future-growth">12. Future Growth</a></li>
  <li><a href="#summary">13. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the downstream compiler-family posture for LLVM-oriented native executable closure in the non-normative FROG reference implementation.
Its role is to make native-path closure explicit without collapsing FROG into LLVM IR.
</p>

<hr/>

<h2 id="why-this-directory-should-exist">2. Why This Directory Should Exist</h2>

<p>
A serious example closure strategy should support two complementary downstream directions:
</p>

<ul>
  <li><strong>runtime-family consumption</strong> of backend contracts through Python, Rust, and C/C++ mini runtimes,</li>
  <li><strong>compiler-family consumption</strong> of lowered forms through an LLVM-oriented native path where a native executable is required.</li>
</ul>

<p>
This directory therefore exists to keep the compiler-family path explicit and separate from runtime-family contract consumption.
</p>

<hr/>

<h2 id="architectural-boundary">3. Architectural Boundary</h2>

<pre><code>canonical .frog source
      |
      v
validated meaning
      |
      v
FIR / execution-facing representation
      |
      v
lowering
      |
      v
compiler-facing lowered form
      |
      v
LLVM-oriented downstream path
      |
      v
native executable
</code></pre>

<p>
The key architectural rule is:
</p>

<pre><code>FIR != LLVM IR
lowering != private compiler internals
LLVM-oriented path != definition of FROG
</code></pre>

<hr/>

<h2 id="directory-shape">4. Directory Shape</h2>

<pre><code>Implementations/Reference/LLVM/
├── Readme.md
├── examples/
│   └── 05_bounded_ui_accumulator/
│       ├── Readme.md
│       ├── main.fir.json
│       ├── main.lowering.json
│       ├── module.ll
│       ├── build.sh
│       └── expected-output.json
├── bridge/
│   ├── fir_to_lowering.md
│   └── lowering_to_llvm.md
└── tools/
    └── emit_llvm_module.py
</code></pre>

<p>
The current published repository may not yet contain this full materialized shape.
The tree above is the intended useful structure for making the native-path corridor inspectable.
</p>

<hr/>

<h2 id="role-of-each-file">5. Role of Each File</h2>

<ul>
  <li><code>Readme.md</code><br/>
      Explains the LLVM-oriented compiler-family posture and the role of this directory.</li>
  <li><code>examples/&lt;example&gt;/Readme.md</code><br/>
      Example-local native-path dossier for one named example.</li>
  <li><code>examples/&lt;example&gt;/main.fir.json</code><br/>
      Example-local FIR artifact used as the execution-facing basis for the native path.</li>
  <li><code>examples/&lt;example&gt;/main.lowering.json</code><br/>
      Example-local lowered artifact used as the compiler-facing bridge.</li>
  <li><code>examples/&lt;example&gt;/module.ll</code><br/>
      LLVM-family textual module emitted for the example.</li>
  <li><code>examples/&lt;example&gt;/build.sh</code><br/>
      Native-path build command sequence for producing the executable.</li>
  <li><code>examples/&lt;example&gt;/expected-output.json</code><br/>
      Expected observable output or parity target for the native executable.</li>
  <li><code>bridge/fir_to_lowering.md</code><br/>
      Explains the bridge between FIR and lowering for the reference compiler-family path.</li>
  <li><code>bridge/lowering_to_llvm.md</code><br/>
      Explains the bridge between lowered forms and LLVM-oriented artifacts.</li>
  <li><code>tools/emit_llvm_module.py</code><br/>
      Helper tool for emitting LLVM-family module text from lowered artifacts in the reference workspace.</li>
</ul>

<hr/>

<h2 id="target-corridor">6. Target Corridor</h2>

<p>
The target corridor for a serious native example is:
</p>

<pre><code>example-local canonical .frog source
      |
      v
example-local FIR artifact
      |
      v
example-local lowered artifact
      |
      v
LLVM-family module
      |
      v
native executable
      |
      v
expected observable behavior
</code></pre>

<p>
For examples with a front panel, this path must also state how the rendered UI host is realized at the native boundary.
</p>

<hr/>

<h2 id="what-this-directory-owns">7. What This Directory Owns</h2>

<ul>
  <li>reference compiler-family posture for LLVM-oriented native paths,</li>
  <li>example-local native-path artifact organization,</li>
  <li>bridging documentation between FIR, lowering, and LLVM-family forms,</li>
  <li>and example-local build/run guidance for native closure.</li>
</ul>

<hr/>

<h2 id="what-this-directory-does-not-own">8. What This Directory Does Not Own</h2>

<ul>
  <li>the canonical <code>.frog</code> source model,</li>
  <li>the semantic acceptance boundary,</li>
  <li>the FIR architecture,</li>
  <li>the normative lowering boundary,</li>
  <li>the universal runtime architecture,</li>
  <li>or the definition of FROG itself.</li>
</ul>

<hr/>

<h2 id="example-facing-posture">9. Example-Facing Posture</h2>

<p>
The first serious target for this directory should be:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/</code></pre>

<p>
The native-path goal is not merely to compute the right numeric result.
It is to prove that one reader can inspect:
</p>

<ul>
  <li>the canonical source,</li>
  <li>the execution-facing basis,</li>
  <li>the lowering bridge,</li>
  <li>the LLVM-family artifact,</li>
  <li>the build command,</li>
  <li>and the final observable result.</li>
</ul>

<hr/>

<h2 id="design-rules">10. Design Rules</h2>

<ul>
  <li>Keep FIR explicitly distinct from LLVM IR.</li>
  <li>Keep lowering explicitly distinct from private compiler internals.</li>
  <li>Keep example-local native-path artifacts attributable to named source examples.</li>
  <li>Do not claim native closure before the build and observable-result corridor is explicit.</li>
  <li>For front-panel examples, do not claim rendered closure before host realization is explicit.</li>
</ul>

<hr/>

<h2 id="closure-status">11. LLVM Closure Status</h2>

<table>
  <thead>
    <tr>
      <th>LLVM-oriented surface</th>
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
      <td>Example-local FIR artifact</td>
      <td>Missing</td>
      <td>Not yet published for example 05.</td>
    </tr>
    <tr>
      <td>Example-local lowered artifact</td>
      <td>Missing</td>
      <td>Not yet published for example 05.</td>
    </tr>
    <tr>
      <td>LLVM-family module emission</td>
      <td>Missing</td>
      <td>Not yet published for example 05.</td>
    </tr>
    <tr>
      <td>Native build path</td>
      <td>Missing</td>
      <td>Not yet published for example 05.</td>
    </tr>
    <tr>
      <td>Rendered front-panel native closure</td>
      <td>Missing</td>
      <td>Not yet published for example 05.</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="future-growth">12. Future Growth</h2>

<ol>
  <li>publish one example-local FIR artifact for example 05,</li>
  <li>publish one example-local lowered artifact for example 05,</li>
  <li>publish one LLVM-family emitted module,</li>
  <li>publish one native build and run command sequence,</li>
  <li>publish expected observable outputs or parity checks,</li>
  <li>and, for front-panel examples, publish the rendered host boundary explicitly.</li>
</ol>

<hr/>

<h2 id="summary">13. Summary</h2>

<p>
This directory defines the LLVM-oriented compiler-family posture for native executable closure.
Its purpose is to make native-path closure explicit while preserving the core architectural rule that LLVM remains downstream from FROG rather than becoming its definition.
</p>
