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
  <li><a href="#current-published-directory-shape">4. Current Published Directory Shape</a></li>
  <li><a href="#target-directory-shape">5. Target Directory Shape</a></li>
  <li><a href="#role-of-each-file">6. Role of Each File</a></li>
  <li><a href="#target-corridor">7. Target Corridor</a></li>
  <li><a href="#what-this-directory-owns">8. What This Directory Owns</a></li>
  <li><a href="#what-this-directory-does-not-own">9. What This Directory Does Not Own</a></li>
  <li><a href="#example-facing-posture">10. Example-Facing Posture</a></li>
  <li><a href="#design-rules">11. Design Rules</a></li>
  <li><a href="#closure-status">12. LLVM Closure Status</a></li>
  <li><a href="#future-growth">13. Future Growth</a></li>
  <li><a href="#summary">14. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the downstream compiler-family posture for LLVM-oriented native executable closure in the non-normative FROG reference implementation.
Its role is to make native-path closure explicit without collapsing FROG into LLVM IR.
</p>

<p>
The important architectural point is that LLVM remains downstream from FROG.
It is one possible compiler-family consumer of lowered FROG artifacts.
It is not the definition of the language, not the owner of FIR, and not the owner of widget semantics.
</p>

<hr/>

<h2 id="why-this-directory-should-exist">2. Why This Directory Should Exist</h2>

<p>
A serious example closure strategy should support two complementary downstream directions:
</p>

<ul>
  <li><strong>runtime-family consumption</strong> of backend contracts through Python, Rust, and C/C++ runtime consumers,</li>
  <li><strong>compiler-family consumption</strong> of lowered forms through an LLVM-oriented native path where a native executable is required.</li>
</ul>

<p>
This directory therefore exists to keep the compiler-family path explicit and separate from runtime-family contract consumption.
That separation matters because a runtime-family corridor and a compiler-family corridor solve different downstream problems.
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

<p>
For front-panel examples, the native corridor must also make explicit how the UI host boundary is realized.
A native executable is not, by itself, proof of rendered front-panel closure.
</p>

<hr/>

<h2 id="current-published-directory-shape">4. Current Published Directory Shape</h2>

<pre><code>Implementations/Reference/LLVM/
└── Readme.md
</code></pre>

<p>
At the current published repository state, this directory is primarily a posture and architecture boundary marker.
It does not yet publish a full example-local LLVM artifact tree.
</p>

<p>
However, the Example 05 corridor already publishes two important upstream artifacts elsewhere in the repository:
</p>

<ul>
  <li><code>Examples/05_bounded_ui_accumulator/main.fir.json</code>,</li>
  <li><code>Examples/05_bounded_ui_accumulator/main.lowering.json</code>.</li>
</ul>

<p>
Accordingly, the right statement is not that FIR and lowering are absent from the repository.
The right statement is that the dedicated LLVM-oriented downstream corridor built from them is not yet materially closed in this directory.
</p>

<hr/>

<h2 id="target-directory-shape">5. Target Directory Shape</h2>

<p>
A useful future LLVM-oriented structure may look like:
</p>

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
This is a target organization for making the native-path corridor inspectable.
It should not be mistaken for a claim that the repository already publishes all of these artifacts inside this directory today.
</p>

<hr/>

<h2 id="role-of-each-file">6. Role of Each File</h2>

<ul>
  <li><code>Readme.md</code><br/>
      Explains the LLVM-oriented compiler-family posture and the role of this directory.</li>

  <li><code>examples/&lt;example&gt;/Readme.md</code><br/>
      Example-local native-path dossier for one named example.</li>

  <li><code>examples/&lt;example&gt;/main.fir.json</code><br/>
      Example-local FIR artifact used as the execution-facing basis for the native path. For Example 05, such an artifact is already published upstream in the example directory.</li>

  <li><code>examples/&lt;example&gt;/main.lowering.json</code><br/>
      Example-local lowered artifact used as the compiler-facing bridge. For Example 05, such an artifact is already published upstream in the example directory.</li>

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

<h2 id="target-corridor">7. Target Corridor</h2>

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
That means the corridor is only fully closed when a reader can inspect:
</p>

<ul>
  <li>the canonical source,</li>
  <li>the execution-facing artifact,</li>
  <li>the lowered bridge artifact,</li>
  <li>the LLVM-family emitted form,</li>
  <li>the native build command,</li>
  <li>the native observable result,</li>
  <li>and, when relevant, the front-panel host realization boundary.</li>
</ul>

<hr/>

<h2 id="what-this-directory-owns">8. What This Directory Owns</h2>

<ul>
  <li>reference compiler-family posture for LLVM-oriented native paths,</li>
  <li>example-local native-path artifact organization when this path is materialized here,</li>
  <li>bridging documentation between FIR, lowering, and LLVM-family forms,</li>
  <li>example-local build and run guidance for native closure.</li>
</ul>

<hr/>

<h2 id="what-this-directory-does-not-own">9. What This Directory Does Not Own</h2>

<ul>
  <li>the canonical <code>.frog</code> source model,</li>
  <li>the semantic acceptance boundary,</li>
  <li>the FIR architecture,</li>
  <li>the normative lowering boundary,</li>
  <li>the universal runtime architecture,</li>
  <li>the definition of widget semantics,</li>
  <li>or the definition of FROG itself.</li>
</ul>

<p>
This directory is downstream from those layers.
It documents and organizes one compiler-family path.
It does not become the owner of upstream language truth.
</p>

<hr/>

<h2 id="example-facing-posture">10. Example-Facing Posture</h2>

<p>
The first serious target for this directory should be:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/</code></pre>

<p>
That example already publishes:
</p>

<ul>
  <li>one canonical source file,</li>
  <li>one example-local FIR artifact,</li>
  <li>one example-local lowered artifact,</li>
  <li>one widget-oriented peripheral package,</li>
  <li>one runtime-family contract corridor.</li>
</ul>

<p>
The LLVM-oriented goal is not merely to compute the right numeric result.
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

<p>
For Example 05 specifically, native closure should eventually state how the final indicator and any rendered front-panel realization are handled at the native boundary.
</p>

<hr/>

<h2 id="design-rules">11. Design Rules</h2>

<ul>
  <li>Keep FIR explicitly distinct from LLVM IR.</li>
  <li>Keep lowering explicitly distinct from private compiler internals.</li>
  <li>Keep example-local native-path artifacts attributable to named source examples.</li>
  <li>Do not claim native closure before the build and observable-result corridor is explicit.</li>
  <li>For front-panel examples, do not claim rendered closure before host realization is explicit.</li>
  <li>Do not let one compiler-family path become the semantic definition of FROG.</li>
</ul>

<hr/>

<h2 id="closure-status">12. LLVM Closure Status</h2>

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
      <td>Directory-level posture</td>
      <td>Defined</td>
      <td>Architecture and ownership boundaries are explicit.</td>
    </tr>
    <tr>
      <td>Example-local FIR artifact for Example 05</td>
      <td>Published upstream</td>
      <td><code>main.fir.json</code> already exists in <code>Examples/05_bounded_ui_accumulator/</code>, but is not yet materialized as part of a dedicated LLVM dossier here.</td>
    </tr>
    <tr>
      <td>Example-local lowered artifact for Example 05</td>
      <td>Published upstream</td>
      <td><code>main.lowering.json</code> already exists in <code>Examples/05_bounded_ui_accumulator/</code>, but is not yet materialized as part of a dedicated LLVM dossier here.</td>
    </tr>
    <tr>
      <td>LLVM-family module emission</td>
      <td>Missing</td>
      <td>No published <code>module.ll</code> is currently exposed for Example 05.</td>
    </tr>
    <tr>
      <td>Bridge documentation inside this directory</td>
      <td>Missing</td>
      <td>No dedicated <code>bridge/</code> material is currently published here.</td>
    </tr>
    <tr>
      <td>Native build path</td>
      <td>Missing</td>
      <td>No published native build and run sequence is currently exposed for Example 05.</td>
    </tr>
    <tr>
      <td>Rendered front-panel native closure</td>
      <td>Missing</td>
      <td>No native rendered front-panel host path is currently published for Example 05.</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="future-growth">13. Future Growth</h2>

<ol>
  <li>materialize one example-local LLVM dossier for Example 05 inside this directory,</li>
  <li>reuse or mirror the already-published Example 05 FIR artifact,</li>
  <li>reuse or mirror the already-published Example 05 lowered artifact,</li>
  <li>publish one LLVM-family emitted module,</li>
  <li>publish one native build and run command sequence,</li>
  <li>publish expected observable outputs or parity checks,</li>
  <li>for front-panel examples, publish the rendered host boundary explicitly.</li>
</ol>

<hr/>

<h2 id="summary">14. Summary</h2>

<p>
This directory defines the LLVM-oriented compiler-family posture for native executable closure.
Its purpose is to make native-path closure explicit while preserving the core architectural rule that LLVM remains downstream from FROG rather than becoming its definition.
</p>

<p>
The important correction at the current repository state is this:
</p>

<ul>
  <li>Example 05 FIR and lowering artifacts already exist in the repository,</li>
  <li>but the dedicated LLVM-oriented downstream corridor built from them is not yet materially published here.</li>
</ul>

<p>
That is the next closure step:
turn already-published upstream artifacts into one explicit, inspectable, example-local native path.
</p>
