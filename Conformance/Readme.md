<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Conformance</h1>

<p align="center">
  <strong>Public accept / reject / preserve truth surface for the published FROG specification</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#core-purpose">2. Core Purpose</a></li>
  <li><a href="#why-this-directory-exists">3. Why this Directory Exists</a></li>
  <li><a href="#definition-of-conformance">4. Definition of Conformance</a></li>
  <li><a href="#non-goals">5. Non-Goals</a></li>
  <li><a href="#relation-with-specification-ownership">6. Relation with Specification Ownership</a></li>
  <li><a href="#critical-boundary-expression-to-meaning">7. Critical Boundary: Expression → Meaning</a></li>
  <li><a href="#directory-structure">8. Directory Structure</a></li>
  <li><a href="#published-cases">9. Published Cases</a></li>
  <li><a href="#expected-outcomes">10. Expected Outcomes</a></li>
  <li><a href="#v01-focus">11. Active v0.1 Conformance Focus</a></li>
  <li><a href="#relation-with-examples-and-reference">12. Relation with Examples and Reference Implementation</a></li>
  <li><a href="#future-growth">13. Future Growth</a></li>
  <li><a href="#summary">14. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the <strong>public conformance surface</strong> of the FROG repository.
</p>

<p>
It publishes explicit cases that make the specification testable across implementations.
</p>

<p>
It answers three fundamental questions:
</p>

<pre><code>What must be accepted?
What must be rejected?
What must be preserved?
</code></pre>

<p>
This directory does not define the language.
It makes the language verifiable.
</p>

<hr/>

<h2 id="core-purpose">2. Core Purpose</h2>

<p>
The purpose of conformance is to transform specification rules into <strong>checkable public expectations</strong>.
</p>

<p>
The repository-level model is:
</p>

<pre><code>Specification   = defines the rules
Conformance     = exposes testable cases
Implementation  = must behave accordingly
</code></pre>

<p>
A conforming implementation may vary internally.
It must not vary in observable meaning for published cases.
</p>

<p>
Conformance prevents the following drift:
</p>

<pre><code>well-formed file
        -/-> valid meaning

implementation convenience
        -/-> language truth

"it runs"
        -/-> "it is correct"
</code></pre>

<hr/>

<h2 id="why-this-directory-exists">3. Why this Directory Exists</h2>

<p>
FROG is specification-first and implementation-independent.
</p>

<p>
This creates a requirement:
</p>

<pre><code>multiple independent implementations
            require
one shared validation surface
</code></pre>

<p>
This directory provides that surface.
</p>

<p>
It ensures that:
</p>

<ul>
  <li>implementations do not silently diverge,</li>
  <li>semantic meaning is not reinterpreted implicitly,</li>
  <li>invalid constructs are rejected instead of repaired,</li>
  <li>critical distinctions remain visible across the pipeline.</li>
</ul>

<hr/>

<h2 id="definition-of-conformance">4. Definition of Conformance</h2>

<p>
Conformance is alignment with the published specification across all architectural stages.
</p>

<p>
It includes:
</p>

<ul>
  <li>source validation correctness,</li>
  <li>semantic validation correctness,</li>
  <li>semantic preservation across derivation,</li>
  <li>boundary preservation across IR and lowering,</li>
  <li>correct rejection of invalid or unsupported cases,</li>
  <li>correct declaration of backend assumptions.</li>
</ul>

<p>
Conformance therefore requires both:
</p>

<ul>
  <li><strong>accept / reject correctness</strong>, and</li>
  <li><strong>preservation correctness</strong>.</li>
</ul>

<p>
Formalized:
</p>

<pre><code>Conformance =
  correct interpretation
  +
  correct preservation
  +
  correct rejection
</code></pre>

<hr/>

<h2 id="non-goals">5. Non-Goals</h2>

<p>
This directory does not define:
</p>

<ul>
  <li>a certification program,</li>
  <li>a universal compatibility matrix,</li>
  <li>a full execution test suite,</li>
  <li>a debugger validation framework,</li>
  <li>a deployment validation system.</li>
</ul>

<p>
It also does not introduce new language rules.
</p>

<p>
Rule:
</p>

<pre><code>Specification defines
Conformance exposes
Implementation follows
</code></pre>

<hr/>

<h2 id="relation-with-specification-ownership">6. Relation with Specification Ownership</h2>

<p>
Conformance does not own language truth.
</p>

<p>
Ownership remains:
</p>

<ul>
  <li><code>Expression/</code> — source structure,</li>
  <li><code>Language/</code> — semantic truth,</li>
  <li><code>Libraries/</code> — primitives,</li>
  <li><code>Profiles/</code> — capability families,</li>
  <li><code>IR/</code> — execution representation and lowering boundaries,</li>
  <li><code>IDE/</code> — tooling behavior.</li>
</ul>

<p>
Conformance cases must always map back to these owners.
</p>

<pre><code>specification → conformance → implementation
</code></pre>

<p>
Never the reverse.
</p>

<hr/>

<h2 id="critical-boundary-expression-to-meaning">7. Critical Boundary: Expression → Meaning</h2>

<p>
The most critical conformance boundary is:
</p>

<pre><code>.frog source
      |
      v
validated program meaning
</code></pre>

<p>
Conformance must make this boundary observable.
</p>

<p>
This includes verifying:
</p>

<ul>
  <li>what establishes semantic meaning,</li>
  <li>what fails before meaning exists,</li>
  <li>what distinctions must survive validation and derivation.</li>
</ul>

<p>
Critical invariants:
</p>

<pre><code>front panel            != public interface
widget_value           != widget_reference
layout                 != execution
adjacency              != dependency
visual order           != execution order
feedback shape         != state
default inference      != explicit initialization
</code></pre>

<p>
These are enforced through mirrored valid / invalid cases.
</p>

<hr/>

<h2 id="directory-structure">8. Directory Structure</h2>

<pre><code>Conformance/
├── Readme.md
├── valid/
└── invalid/
</code></pre>

<p>
Each case should define:
</p>

<ul>
  <li>expected validity,</li>
  <li>tested boundaries,</li>
  <li>preservation requirements,</li>
  <li>rejection reason if invalid.</li>
</ul>

<hr/>

<h2 id="published-cases">9. Published Cases</h2>

<p>
The current published set follows a mirrored pattern:
</p>

<pre><code>valid case   → defines allowed behavior
invalid case → defines forbidden behavior
pair         → defines boundary
</code></pre>

<p>
These pairs define core invariants such as:
</p>

<pre><code>public interface       != widget participation
widget_reference       != widget_value
execution meaning      != UI presence
connectivity           != evaluation order
structure              != layout grouping
state                  != inferred feedback
</code></pre>

<p>
This pairing strategy is intentional:
</p>

<pre><code>acceptance alone is insufficient
rejection alone is insufficient
both define truth
</code></pre>

<hr/>

<h2 id="expected-outcomes">10. Expected Outcomes</h2>

<p>
Each case expresses structured expectations:
</p>

<ul>
  <li><strong>Expected:</strong> valid | invalid</li>
  <li><strong>Expected meaning:</strong> established | not established</li>
  <li><strong>Expected preservation:</strong> required distinctions remain explicit</li>
  <li><strong>Expected rejection:</strong> explicit failure reason</li>
</ul>

<p>
Examples:
</p>

<pre><code>Expected: valid
Expected preservation:
  explicit state remains explicit

Expected: invalid
Expected rejection:
  illegal feedback without explicit memory
</code></pre>

<hr/>

<h2 id="v01-focus">11. Active v0.1 Conformance Focus</h2>

<p>
v0.1 focuses on architectural correctness, not feature coverage.
</p>

<p>
Priorities:
</p>

<pre><code>1. source validity
2. semantic validity
3. preservation of distinctions
4. explicit rejection of violations
</code></pre>

<p>
Key enforced separations:
</p>

<ul>
  <li>interface vs widget,</li>
  <li>value vs reference,</li>
  <li>state vs feedback,</li>
  <li>execution vs layout,</li>
  <li>connectivity vs order.</li>
</ul>

<p>
Rule:
</p>

<pre><code>no implicit meaning
no silent repair
no hidden interpretation
</code></pre>

<hr/>

<h2 id="relation-with-examples-and-reference">12. Relation with Examples and Reference Implementation</h2>

<pre><code>Examples/                   → illustrate
Conformance/                → define expectations
Implementations/Reference/  → execute
</code></pre>

<p>
These roles must remain strictly separated.
</p>

<p>
An implementation passing a case does not redefine the language.
</p>

<hr/>

<h2 id="future-growth">13. Future Growth</h2>

<p>
Growth must remain controlled and architecture-driven.
</p>

<p>
Preferred pattern:
</p>

<pre><code>small case
→ clear boundary
→ clear expectation
→ clear ownership
</code></pre>

<p>
Future expansion areas:
</p>

<ul>
  <li>type and value legality,</li>
  <li>state semantics and timing,</li>
  <li>structure legality,</li>
  <li>profile-dependent behavior,</li>
  <li>backend-family rejection cases.</li>
</ul>

<hr/>

<h2 id="summary">14. Summary</h2>

<p>
This directory is the public truth surface of FROG conformance.
</p>

<p>
It defines:
</p>

<ul>
  <li>what must be accepted,</li>
  <li>what must be rejected,</li>
  <li>what must be preserved.</li>
</ul>

<p>
Core rule:
</p>

<pre><code>Specification defines truth
Conformance exposes truth
Implementations must align
</code></pre>

<p>
Or more directly:
</p>

<pre><code>rules are written
cases make them testable
tools must follow
</code></pre>
