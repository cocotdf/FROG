<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">02 — IR-Derivable but Not Lowerable</h1>

<p align="center">
  <strong>Negative compiler-corridor case where canonical IR exists but faithful lowering is unavailable under the declared corridor</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Case Identifier</h2>

<pre><code>invalid/compiler/02_ir_derivable_but_not_lowerable</code></pre>

<hr/>

<h2>Purpose</h2>

<p>
This case verifies that canonical FROG Execution IR derivation does not automatically imply lowerability for a declared compilation corridor.
</p>

<p>
The protected distinction is:
</p>

<pre><code>IR-derivable
   !=
lowerable</code></pre>

<hr/>

<h2>Why this Case Exists</h2>

<p>
The repository now explicitly separates:
</p>

<ul>
  <li>validated meaning,</li>
  <li>canonical open IR,</li>
  <li>lowering,</li>
  <li>backend contract.</li>
</ul>

<p>
That architecture is only real if the repo can publish cases where:
</p>

<ul>
  <li>semantic acceptance succeeds,</li>
  <li>IR derivation succeeds,</li>
  <li>but lowering must still reject.</li>
</ul>

<hr/>

<h2>Source Scenario</h2>

<p>
The program is assumed to be:
</p>

<ul>
  <li>structurally valid,</li>
  <li>semantically accepted,</li>
  <li>derivable to canonical FROG Execution IR,</li>
  <li>but dependent on a semantically valid construct whose faithful lowering path is not yet available under the declared corridor.</li>
</ul>

<p>
Illustrative examples may include:
</p>

<ul>
  <li>a structured construct whose semantics cannot yet be lowered faithfully under the declared profile,</li>
  <li>a state-sensitive pattern whose explicit semantics cannot yet be preserved by the implementation’s lowering corridor,</li>
  <li>another accepted IR-level form lacking a coherent lowered representation.</li>
</ul>

<hr/>

<h2>Expected Loadability</h2>

<pre><code>Expected loadability: loadable</code></pre>

<hr/>

<h2>Expected Structural Validity</h2>

<pre><code>Expected structural validity: valid</code></pre>

<hr/>

<h2>Expected Semantic Acceptance</h2>

<pre><code>Expected semantic acceptance: accepted</code></pre>

<hr/>

<h2>Expected IR Derivation</h2>

<pre><code>Expected IR derivation: derivable</code></pre>

<p>
The case must derive to canonical Execution IR without loss of required distinctions.
</p>

<hr/>

<h2>Expected Canonical JSON IR Result</h2>

<pre><code>Expected IR schema result: schema-valid</code></pre>

<hr/>

<h2>Declared Profile Scope</h2>

<pre><code>Declared profile scope: native_cpu_llvm</code></pre>

<hr/>

<h2>Expected Lowering Result</h2>

<pre><code>Expected lowering result: rejected</code></pre>

<p>
The expected reason is not semantic invalidity.
The expected reason is the absence of a faithful lowering path for the declared corridor.
</p>

<hr/>

<h2>Expected Backend-Contract Result</h2>

<pre><code>Expected backend-contract result: not emittable</code></pre>

<p>
No backend contract should be emitted after lowering rejection.
</p>

<hr/>

<h2>Expected Backend-Family Consumption</h2>

<pre><code>Expected backend-family consumption: not applicable</code></pre>

<hr/>

<h2>Expected Rejection Stage</h2>

<pre><code>Expected rejection stage: lowering</code></pre>

<hr/>

<h2>Expected Rejection Reason</h2>

<pre><code>Expected rejection reason:
canonical IR exists,
but faithful lowering under native_cpu_llvm is unavailable
without semantic loss or illicit invention</code></pre>

<hr/>

<h2>Required Preserved Distinctions</h2>

<ul>
  <li>semantic acceptance remains distinct from lowerability,</li>
  <li>canonical IR existence remains distinct from lowered-form availability,</li>
  <li>lowering rejection remains distinct from IR invalidity.</li>
</ul>

<hr/>

<h2>Case Classification</h2>

<pre><code>Case classification:
- negative
- compiler corridor
- IR-derivable
- lowering-rejected
- native_cpu_llvm boundary case</code></pre>

<hr/>

<h2>Summary</h2>

<p>
This case proves that the compiler corridor preserves a real lowering boundary.
A conforming implementation must reject here rather than silently flattening, inventing, or erasing semantics.
</p>
