<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Example 05 — Bounded UI Accumulator</h1>

<p align="center">
  <strong>Operational A-to-Z dossier for a bounded source → UI object package → FIR → lowering → contract → multi-runtime execution slice</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#expected-behavior">2. Expected Behavior</a></li>
  <li><a href="#closure-status">3. Closure Status</a></li>
  <li><a href="#useful-file-tree">4. Useful File Tree</a></li>
  <li><a href="#file-responsibilities">5. File Responsibilities</a></li>
  <li><a href="#shared-corridor">6. Shared Canonical Corridor</a></li>
  <li><a href="#source-posture">7. Canonical Source Posture</a></li>
  <li><a href="#ui-posture">8. UI Object and Front-Panel Posture</a></li>
  <li><a href="#fir-posture">9. FIR / Execution-Facing Posture</a></li>
  <li><a href="#lowering-posture">10. Lowering and Backend-Contract Posture</a></li>
  <li><a href="#python-pipe">11. Python Runtime Pipe</a></li>
  <li><a href="#rust-pipe">12. Rust Runtime Pipe</a></li>
  <li><a href="#cpp-pipe">13. C/C++ Runtime Pipe</a></li>
  <li><a href="#llvm-path">14. LLVM-Oriented Native Path</a></li>
  <li><a href="#observable-parity">15. Observable Parity Across Runtime Families</a></li>
  <li><a href="#published-gaps">16. Published Gaps Still To Close</a></li>
  <li><a href="#next-steps">17. Next Steps for Full Closure</a></li>
  <li><a href="#summary">18. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This example is the first bounded vertical slice in the FROG repository that crosses a real execution boundary while remaining fully inspectable.
</p>

<p>
It combines:
</p>

<ul>
  <li>one canonical <code>.frog</code> source file (program semantics),</li>
  <li>one bounded counted loop,</li>
  <li>one explicit state path via <code>frog.core.delay</code>,</li>
  <li>two widgets (control + indicator),</li>
  <li>one peripheral UI object file (host realization layer),</li>
  <li>one example-local FIR artifact,</li>
  <li>one example-local lowered artifact,</li>
  <li>one backend contract artifact,</li>
  <li>one Python runtime execution path,</li>
  <li>one Rust runtime validation path.</li>
</ul>

<p>
The objective is not completeness, but <strong>corridor readability</strong>:
the reader must be able to follow the entire chain from source semantics to runtime execution.
</p>

<hr/>

<h2 id="expected-behavior">2. Expected Behavior</h2>

<ul>
  <li><code>ctrl_input</code> provides a <code>u16</code> input value <code>x</code>,</li>
  <li>state starts at <code>0</code>,</li>
  <li>loop executes exactly <code>5</code> iterations,</li>
  <li>each iteration: <code>state = state + x</code>,</li>
  <li>final state is exposed as:</li>
  <ul>
    <li>public output <code>result</code>,</li>
    <li>indicator <code>ind_result</code>,</li>
  </ul>
  <li>UI object-style writes update <code>face_color</code>.</li>
</ul>

<p>
Example:
</p>

<pre><code>input  = 3
result = 15
</code></pre>

<hr/>

<h2 id="closure-status">3. Closure Status</h2>

<table>
<thead>
<tr>
<th>Surface</th>
<th>Status</th>
<th>Comment</th>
</tr>
</thead>
<tbody>

<tr>
<td>Source (.frog)</td>
<td>Closed</td>
<td>Canonical semantics defined</td>
</tr>

<tr>
<td>UI object layer</td>
<td>Transitional</td>
<td><code>front_panel.objects.json</code> exists → will evolve toward <code>.wfrog</code></td>
</tr>

<tr>
<td>FIR</td>
<td>Closed (example-local)</td>
<td>Execution-facing artifact visible</td>
</tr>

<tr>
<td>Lowering</td>
<td>Closed (example-local)</td>
<td>Bridge toward runtime/LLVM</td>
</tr>

<tr>
<td>Backend contract</td>
<td>Closed</td>
<td>Runtime consumption boundary defined</td>
</tr>

<tr>
<td>Python runtime</td>
<td>Closed</td>
<td>Executable path exists</td>
</tr>

<tr>
<td>Rust runtime</td>
<td>Partial</td>
<td>Validated via tests, no runner binary</td>
</tr>

<tr>
<td>C/C++ runtime</td>
<td>Missing</td>
<td>No consumer yet</td>
</tr>

<tr>
<td>Rendered UI</td>
<td>Missing</td>
<td>No host rendering pipeline</td>
</tr>

<tr>
<td>LLVM native path</td>
<td>Missing</td>
<td>No executable generation yet</td>
</tr>

</tbody>
</table>

<hr/>

<h2 id="useful-file-tree">4. Useful File Tree</h2>

<pre><code>Examples/
└── 05_bounded_ui_accumulator/
    ├── Readme.md
    ├── main.frog
    ├── front_panel.objects.json   # → future .wfrog
    ├── main.fir.json
    └── main.lowering.json
</code></pre>

<hr/>

<h2 id="file-responsibilities">5. File Responsibilities</h2>

<ul>
  <li><code>main.frog</code> → program semantics (authoritative)</li>
  <li><code>front_panel.objects.json</code> → UI realization (host layer, non-authoritative)</li>
  <li><code>main.fir.json</code> → execution-facing normalized representation</li>
  <li><code>main.lowering.json</code> → backend bridge layer</li>
</ul>

<p>
Key rule:
</p>

<pre><code>.frog  = semantics
UI file = realization
FIR     = execution reading
lowering = backend bridge
</code></pre>

<hr/>

<h2 id="shared-corridor">6. Shared Canonical Corridor</h2>

<pre><code>.frog
  ↓
UI object layer
  ↓
FIR
  ↓
lowering
  ↓
contract
  ↓
runtime (Python / Rust / C++)
  ↓
(optional) LLVM native executable
</code></pre>

<hr/>

<h2 id="source-posture">7. Canonical Source Posture</h2>

<p>
The source defines:
</p>

<ul>
  <li>dataflow (add + delay),</li>
  <li>loop semantics,</li>
  <li>widget identity,</li>
  <li>UI interactions (property_write).</li>
</ul>

<p>
The source does NOT define:
</p>

<ul>
  <li>rendering,</li>
  <li>widget visuals,</li>
  <li>host runtime behavior.</li>
</ul>

<hr/>

<h2 id="ui-posture">8. UI Object and Front-Panel Posture</h2>

<p>
Two layers must remain strictly separated:
</p>

<ul>
  <li><strong>source layer (.frog)</strong> → identity + semantics</li>
  <li><strong>UI object layer (.wfrog / json)</strong> → realization + rendering</li>
</ul>

<p>
Important constraint:
</p>

<pre><code>UI layer MUST NOT redefine program semantics
</code></pre>

<hr/>

<h2 id="fir-posture">9. FIR / Execution-Facing Posture</h2>

<p>
FIR exposes:
</p>

<ul>
  <li>explicit state</li>
  <li>loop structure</li>
  <li>input/output bindings</li>
  <li>UI interaction surface</li>
</ul>

<p>
FIR is the first form that is:
</p>

<ul>
  <li>runtime-consumable</li>
  <li>compiler-consumable</li>
</ul>

<hr/>

<h2 id="lowering-posture">10. Lowering and Backend-Contract Posture</h2>

<p>
Lowering transforms FIR into:
</p>

<ul>
  <li>runtime-ready structure</li>
  <li>future LLVM bridge</li>
</ul>

<p>
Contract = stable boundary for runtimes.
</p>

<hr/>

<h2 id="python-pipe">11. Python Runtime Pipe</h2>

<pre><code>python Implementations/Reference/Runtime/run_slice05_contract.py 3
</code></pre>

<p>
Pipeline:
</p>

<ol>
  <li>load contract</li>
  <li>instantiate runtime</li>
  <li>execute loop</li>
  <li>apply UI writes</li>
  <li>emit result</li>
</ol>

<hr/>

<h2 id="rust-pipe">12. Rust Runtime Pipe</h2>

<pre><code>cargo test
</code></pre>

<p>
Confirms:
</p>

<ul>
  <li>contract validity</li>
  <li>execution correctness</li>
</ul>

<hr/>

<h2 id="cpp-pipe">13. C/C++ Runtime Pipe</h2>

<p>
Not implemented yet.
</p>

<p>
Target:
</p>

<ul>
  <li>minimal interpreter</li>
  <li>same contract consumption</li>
</ul>

<hr/>

<h2 id="llvm-path">14. LLVM-Oriented Native Path</h2>

<p>
Missing today.
</p>

<p>
Target architecture:
</p>

<pre><code>lowering → LLVM IR → native executable
</code></pre>

<hr/>

<h2 id="observable-parity">15. Observable Parity Across Runtime Families</h2>

<table>
<thead>
<tr><th>Observable</th><th>Value</th></tr>
</thead>
<tbody>
<tr><td>Iterations</td><td>5</td></tr>
<tr><td>Initial state</td><td>0</td></tr>
<tr><td>Final result</td><td>15</td></tr>
</tbody>
</table>

<hr/>

<h2 id="published-gaps">16. Published Gaps Still To Close</h2>

<ol>
  <li>C/C++ runtime</li>
  <li>Rust runner binary</li>
  <li>real UI renderer</li>
  <li>LLVM backend</li>
</ol>

<hr/>

<h2 id="next-steps">17. Next Steps for Full Closure</h2>

<p>
To reach full A→Z closure:
</p>

<ul>
  <li>introduce <code>.wfrog</code> formally (replace json file)</li>
  <li>add minimal UI renderer</li>
  <li>add C++ runtime</li>
  <li>add LLVM backend</li>
  <li>produce native executable demo</li>
</ul>

<hr/>

<h2 id="summary">18. Summary</h2>

<pre><code>source           : closed
UI object layer  : transitional
FIR              : closed
lowering         : closed
multi-runtime    : partial
native exec      : missing
UI rendering     : missing
</code></pre>

<p>
This example proves that FROG can define a stable execution corridor across multiple runtimes.
</p>

<p>
It does not yet prove full native or UI closure.
</p>
