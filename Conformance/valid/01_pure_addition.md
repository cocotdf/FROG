<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 Conformance Case — 01 Pure Addition</h1>

<p align="center">
  Valid conformance case for minimal public-interface arithmetic in FROG v0.1<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#case-overview">1. Case Overview</a></li>
  <li><a href="#status">2. Expected Status</a></li>
  <li><a href="#source-target">3. Source Target</a></li>
  <li><a href="#boundaries-exercised">4. Boundaries Exercised</a></li>
  <li><a href="#why-this-case-is-valid">5. Why this Case Is Valid</a></li>
  <li><a href="#expected-validation-outcome">6. Expected Validation Outcome</a></li>
  <li><a href="#expected-derivation-preservation">7. Expected Derivation Preservation</a></li>
  <li><a href="#expected-backend-contract-preservation">8. Expected Backend Contract Preservation</a></li>
  <li><a href="#what-must-not-happen">9. What Must Not Happen</a></li>
  <li><a href="#summary">10. Summary</a></li>
</ul>

<hr/>

<h2 id="case-overview">1. Case Overview</h2>

<p>
This case covers the smallest useful executable FROG program with:
</p>

<ul>
  <li>two public inputs,</li>
  <li>one core arithmetic primitive,</li>
  <li>one public output.</li>
</ul>

<p>
The case is intentionally free of UI participation, structured control, and explicit memory.
</p>

<hr/>

<h2 id="status">2. Expected Status</h2>

<p><strong>Expected: valid</strong></p>

<hr/>

<h2 id="source-target">3. Source Target</h2>

<p>
Expected source target:
</p>

<pre><code>Examples/01_pure_addition/main.frog</code></pre>

<hr/>

<h2 id="boundaries-exercised">4. Boundaries Exercised</h2>

<ul>
  <li>canonical source loading,</li>
  <li>public interface declaration,</li>
  <li>diagram-side <code>interface_input</code> and <code>interface_output</code> participation,</li>
  <li>primitive execution through <code>frog.core.add</code>,</li>
  <li>basic edge validity,</li>
  <li>basic Execution IR derivation,</li>
  <li>basic backend-contract emission for a callable execution unit.</li>
</ul>

<hr/>

<h2 id="why-this-case-is-valid">5. Why this Case Is Valid</h2>

<p>
This case is valid because it expresses a simple acyclic executable graph with:
</p>

<ul>
  <li>well-formed public interface declarations,</li>
  <li>valid diagram-side boundary participation,</li>
  <li>a valid intrinsic primitive reference,</li>
  <li>type-compatible edges.</li>
</ul>

<p>
No additional profile capability is required for this case.
</p>

<hr/>

<h2 id="expected-validation-outcome">6. Expected Validation Outcome</h2>

<p>
A conforming validator should accept the case.
It should confirm at minimum that:
</p>

<ul>
  <li>the file is structurally valid canonical source,</li>
  <li>the interface port declarations are well formed,</li>
  <li>the <code>frog.core.add</code> primitive usage is valid,</li>
  <li>the primitive input and output edges are correctly connected,</li>
  <li>no illegal cycle is present.</li>
</ul>

<hr/>

<h2 id="expected-derivation-preservation">7. Expected Derivation Preservation</h2>

<p>
Execution IR derivation should preserve explicitly:
</p>

<ul>
  <li>one execution unit for the whole validated FROG,</li>
  <li>public entry participation for the first input,</li>
  <li>public entry participation for the second input,</li>
  <li>primitive execution identity for <code>frog.core.add</code>,</li>
  <li>public exit participation for the output,</li>
  <li>the validated dependency edges between those objects.</li>
</ul>

<p>
The derivation should not introduce:
</p>

<ul>
  <li>UI participation,</li>
  <li>widget references,</li>
  <li>structured regions,</li>
  <li>explicit memory objects.</li>
</ul>

<hr/>

<h2 id="expected-backend-contract-preservation">8. Expected Backend Contract Preservation</h2>

<p>
If this case is lowered and emitted as a backend contract, the contract should still make clear that:
</p>

<ul>
  <li>one consumable execution unit is offered,</li>
  <li>the unit has two public inputs and one public output,</li>
  <li>the computation is ordinary arithmetic addition,</li>
  <li>no UI participation is required,</li>
  <li>no explicit local-memory semantics are required.</li>
</ul>

<hr/>

<h2 id="what-must-not-happen">9. What Must Not Happen</h2>

<ul>
  <li>The case must not be rejected as if UI support were required.</li>
  <li>The case must not be rewritten into a hidden runtime-private callable form with lost public-boundary attribution.</li>
  <li>The case must not gain implicit state or scheduler-private semantics.</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
This is the baseline valid conformance case for minimal public-interface arithmetic in FROG v0.1.
A conforming toolchain should accept it,
derive it cleanly,
and preserve its public-boundary and primitive-execution meaning through backend handoff.
</p>
