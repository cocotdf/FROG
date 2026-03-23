<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140">
</p>

<h1 align="center">FROG Expression to Validated Meaning</h1>

<p align="center">
  <strong>Normative boundary from canonical <code>.frog</code> source to validated program meaning</strong><br>
  FROG — Free Open Graphical Language
</p>

<hr>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#boundary-contract">2. Boundary Contract</a></li>
  <li><a href="#scope">3. Scope</a></li>
  <li><a href="#relation">4. Relation with Other Specifications</a></li>
  <li><a href="#validation-inputs">5. Validation Inputs</a></li>
  <li><a href="#validation-output">6. Validation Output</a></li>
  <li><a href="#semantic-closure">7. Semantic Closure Guarantees</a></li>
  <li><a href="#source-families">8. Source Families and Semantic Ownership</a></li>
  <li><a href="#execution-relevance">9. Execution-Relevant Content</a></li>
  <li><a href="#non-semantic">10. Non-Semantic Content</a></li>
  <li><a href="#critical-distinctions">11. Critical Distinctions Preserved</a></li>
  <li><a href="#state-structures">12. Structures, State, and Cycles</a></li>
  <li><a href="#type-value">13. Type, Value, and State Commitments</a></li>
  <li><a href="#attribution">14. Attribution and Recoverability</a></li>
  <li><a href="#forbidden">15. Forbidden Boundary Collapses</a></li>
  <li><a href="#ir-contract">16. Contract with IR Derivation</a></li>
  <li><a href="#out-of-scope">17. Out of Scope</a></li>
  <li><a href="#summary">18. Summary</a></li>
</ul>

<hr>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the normative transition from canonical <code>.frog</code> source
to validated program meaning.
</p>

<p>
It establishes what must be true before any Execution IR may be derived.
</p>

<pre><code>Expression/  →  Language/  →  IR/
   source         meaning      execution
</code></pre>

<p>
This document governs the transition:
</p>

<pre><code>.frog source → validated program meaning
</code></pre>

<hr>

<h2 id="boundary-contract">2. Boundary Contract</h2>

<p>
This boundary produces exactly one of two outcomes:
</p>

<ul>
  <li>a valid, semantically closed program meaning, or</li>
  <li>a rejection (no meaning exists).</li>
</ul>

<p>
No conforming system may derive IR without validated meaning.
</p>

<p>
The output of this boundary is:
</p>

<ul>
  <li>semantically complete,</li>
  <li>execution-relevant,</li>
  <li>non-ambiguous,</li>
  <li>attributable.</li>
</ul>

<p>
It is not:
</p>

<ul>
  <li>an IR,</li>
  <li>a runtime representation,</li>
  <li>a lowered form.</li>
</ul>

<hr>

<h2 id="scope">3. Scope</h2>

<p>This document defines:</p>

<ul>
  <li>what validation must establish,</li>
  <li>what becomes semantic meaning,</li>
  <li>what must remain recoverable,</li>
  <li>what must NOT influence semantics.</li>
</ul>

<p>This document does NOT define:</p>

<ul>
  <li>source serialization format,</li>
  <li>primitive implementation,</li>
  <li>IR structure,</li>
  <li>runtime behavior.</li>
</ul>

<hr>

<h2 id="relation">4. Relation with Other Specifications</h2>

<pre><code>Expression/   → source shape
Language/     → semantic truth (this document)
IR/           → execution representation
</code></pre>

<p>
This document is upstream of <code>IR/Derivation rules.md</code>.
</p>

<hr>

<h2 id="validation-inputs">5. Validation Inputs</h2>

<p>
Validation MUST consider:
</p>

<ul>
  <li>source structure,</li>
  <li>interface,</li>
  <li>diagram,</li>
  <li>types,</li>
  <li>primitives,</li>
  <li>structures,</li>
  <li>state and cycles,</li>
  <li>UI participation where applicable.</li>
</ul>

<p>
Validation is cross-layer.
Its result is owned here.
</p>

<hr>

<h2 id="validation-output">6. Validation Output</h2>

<p>
Validated meaning MUST fully define:
</p>

<ul>
  <li>public interface boundary,</li>
  <li>executable graph participation,</li>
  <li>structure semantics,</li>
  <li>state legality,</li>
  <li>typed value flow,</li>
  <li>UI participation where execution-relevant.</li>
</ul>

<p>
After this stage, no ambiguity remains for IR derivation.
</p>

<hr>

<h2 id="semantic-closure">7. Semantic Closure Guarantees</h2>

<p>
Validation MUST guarantee:
</p>

<ul>
  <li>no missing execution-relevant information,</li>
  <li>no implicit execution dependency,</li>
  <li>no implicit memory,</li>
  <li>no reliance on layout,</li>
  <li>no reliance on runtime behavior.</li>
</ul>

<pre><code>validated meaning must be:
✔ explicit
✔ complete
✔ deterministic at the dependency level
✔ independent of runtime policy
</code></pre>

<hr>

<h2 id="source-families">8. Source Families and Semantic Ownership</h2>

<h3>8.1 Semantic families</h3>

<ul>
  <li>interface</li>
  <li>diagram</li>
  <li>structures</li>
  <li>explicit state</li>
  <li>primitive usage</li>
  <li>execution-relevant widget participation</li>
</ul>

<h3>8.2 Support families</h3>

<ul>
  <li>connector</li>
  <li>front panel (non-participating)</li>
  <li>icon</li>
  <li>ide</li>
  <li>cache</li>
</ul>

<hr>

<h2 id="execution-relevance">9. Execution-Relevant Content</h2>

<p>
Execution-relevant content includes:
</p>

<ul>
  <li>nodes,</li>
  <li>edges,</li>
  <li>structure boundaries,</li>
  <li>state,</li>
  <li>typed values,</li>
  <li>interface participation,</li>
  <li>widget_value,</li>
  <li>widget_reference.</li>
</ul>

<hr>

<h2 id="non-semantic">10. Non-Semantic Content</h2>

<p>
The following MUST NOT influence semantics:
</p>

<ul>
  <li>layout,</li>
  <li>geometry,</li>
  <li>styling,</li>
  <li>editor metadata,</li>
  <li>cache.</li>
</ul>

<hr>

<h2 id="critical-distinctions">11. Critical Distinctions Preserved</h2>

<p>Validation MUST preserve:</p>

<ul>
  <li><code>interface_input</code> vs <code>interface_output</code></li>
  <li><code>widget_value</code> vs <code>widget_reference</code></li>
  <li>interface vs UI</li>
  <li>structure vs layout</li>
  <li>explicit state vs inferred state</li>
</ul>

<hr>

<h2 id="state-structures">12. Structures, State, and Cycles</h2>

<ul>
  <li>structures MUST be valid and explicit</li>
  <li>state MUST be explicit</li>
  <li>cycles MUST be validated</li>
</ul>

<pre><code>loop != state
explicit memory → valid state
</code></pre>

<hr>

<h2 id="type-value">13. Type, Value, and State Commitments</h2>

<p>Validation MUST guarantee:</p>

<ul>
  <li>type correctness,</li>
  <li>value compatibility,</li>
  <li>state legality.</li>
</ul>

<hr>

<h2 id="attribution">14. Attribution and Recoverability</h2>

<p>
All execution-relevant elements MUST remain attributable:
</p>

<ul>
  <li>nodes,</li>
  <li>structures,</li>
  <li>state,</li>
  <li>UI participation.</li>
</ul>

<hr>

<h2 id="forbidden">15. Forbidden Boundary Collapses</h2>

<pre><code>source        -/-> IR
validator     -/-> language law
front panel   -/-> interface
connector     -/-> interface
runtime       -/-> semantics
IDE/cache     -/-> semantics
</code></pre>

<hr>

<h2 id="ir-contract">16. Contract with IR Derivation</h2>

<p>
This document guarantees that IR derivation:
</p>

<ul>
  <li>does not need to infer meaning,</li>
  <li>does not need to resolve ambiguity,</li>
  <li>only transforms validated meaning into IR.</li>
</ul>

<pre><code>this document answers:
"What must be true before IR exists?"

IR/Derivation rules.md answers:
"How meaning becomes IR?"
</code></pre>

<hr>

<h2 id="out-of-scope">17. Out of Scope</h2>

<ul>
  <li>validator implementation,</li>
  <li>internal representation,</li>
  <li>IR format,</li>
  <li>runtime.</li>
</ul>

<hr>

<h2 id="summary">18. Summary</h2>

<p>
Validated program meaning is:
</p>

<ul>
  <li>the first semantic truth,</li>
  <li>fully explicit,</li>
  <li>non-ambiguous,</li>
  <li>ready for IR derivation.</li>
</ul>

<pre><code>Expression → Language → IR

write      → meaning     → execution
</code></pre>
