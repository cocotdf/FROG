<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG Conformance</h1>

<p align="center">
  Early conformance cases and expected outcomes for the published FROG specification<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-directory-exists">2. Why this Directory Exists</a></li>
  <li><a href="#what-conformance-means-here">3. What Conformance Means Here</a></li>
  <li><a href="#what-this-directory-does-not-do">4. What this Directory Does Not Do</a></li>
  <li><a href="#relation-with-specification-ownership">5. Relation with Specification Ownership</a></li>
  <li><a href="#directory-structure">6. Directory Structure</a></li>
  <li><a href="#valid-and-invalid-cases">7. Valid and Invalid Cases</a></li>
  <li><a href="#expected-outcomes">8. Expected Outcomes</a></li>
  <li><a href="#early-v01-conformance-focus">9. Early v0.1 Conformance Focus</a></li>
  <li><a href="#relation-with-examples-and-reference-implementation">10. Relation with Examples and Reference Implementation</a></li>
  <li><a href="#future-growth">11. Future Growth</a></li>
  <li><a href="#summary">12. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory contains <strong>early conformance material</strong> for the published FROG specification.
Its purpose is to make expected outcomes explicit for named cases such as:
</p>

<ul>
  <li>what a conforming toolchain should accept,</li>
  <li>what a conforming toolchain should reject,</li>
  <li>what distinctions a conforming derivation or backend-facing handoff must preserve.</li>
</ul>

<p>
Conformance material is needed because a specification repository should not rely only on prose and good intentions.
It should also provide explicit cases that future validators, derivation pipelines, lowerers, and runtimes can use to check their own behavior.
</p>

<hr/>

<h2 id="why-this-directory-exists">2. Why this Directory Exists</h2>

<p>
The FROG repository is architected as a specification-first repository rather than as one product implementation.
That separation is valuable,
but it also creates a practical need:
different future implementations must have a shared way to check whether they are staying aligned with the published specification.
</p>

<p>
This directory exists to provide that shared starting point.
</p>

<p>
At minimum, conformance material should help answer questions such as:
</p>

<ul>
  <li>Should this program validate or fail?</li>
  <li>If it validates, which distinctions must still remain explicit after derivation?</li>
  <li>If it is lowered and emitted as a backend contract, which assumptions may be fixed and which may not be silently invented?</li>
  <li>If a feature is unsupported by one backend family, should it be rejected rather than reinterpreted?</li>
</ul>

<hr/>

<h2 id="what-conformance-means-here">3. What Conformance Means Here</h2>

<p>
In this directory, <strong>conformance</strong> means alignment with the published FROG specification layers and their ownership boundaries.
It includes at least:
</p>

<ul>
  <li>source validation conformance,</li>
  <li>semantic preservation conformance,</li>
  <li>derivation-boundary conformance,</li>
  <li>backend-contract conformance,</li>
  <li>rejection conformance for unsupported or invalid cases.</li>
</ul>

<p>
This is intentionally broader than just “does the tool run the program?”
A tool can run something incorrectly.
Conformance must therefore include both:
</p>

<ul>
  <li><strong>acceptance / rejection correctness</strong>, and</li>
  <li><strong>preservation correctness</strong>.</li>
</ul>

<hr/>

<h2 id="what-this-directory-does-not-do">4. What this Directory Does Not Do</h2>

<p>
This directory is <strong>not</strong>:
</p>

<ul>
  <li>a complete certification program,</li>
  <li>a frozen cross-vendor compatibility matrix,</li>
  <li>a universal deployment test suite,</li>
  <li>a replacement for the normative specification documents.</li>
</ul>

<p>
In base v0.1, this directory is only the beginning of a conformance story.
Its job is to make the first expectations explicit and durable.
</p>

<hr/>

<h2 id="relation-with-specification-ownership">5. Relation with Specification Ownership</h2>

<p>
This directory does not own language truth.
Ownership remains in the published specification layers:
</p>

<ul>
  <li><code>Expression/</code> owns canonical source structure,</li>
  <li><code>Language/</code> owns validated semantic truth,</li>
  <li><code>Libraries/</code> owns intrinsic primitive definitions,</li>
  <li><code>Profiles/</code> owns optional standardized capability families,</li>
  <li><code>IR/</code> owns execution-facing representation, derivation, construction, identity, lowering, and backend-hand-off boundaries,</li>
  <li><code>IDE/</code> owns authoring-facing and observability-facing tooling concerns.</li>
</ul>

<p>
Conformance material should therefore always point back to those owners instead of silently inventing new rules.
</p>

<hr/>

<h2 id="directory-structure">6. Directory Structure</h2>

<p>
A minimal initial structure may look like:
</p>

<pre><code>Conformance/
├── Readme.md
├── valid/
└── invalid/
</code></pre>

<p>
Each conformance case should normally state:
</p>

<ul>
  <li>the case name,</li>
  <li>whether the case is expected to validate or fail,</li>
  <li>which specification boundaries are being exercised,</li>
  <li>which preservation obligations matter if the case is valid,</li>
  <li>which rejection reason matters if the case is invalid.</li>
</ul>

<hr/>

<h2 id="valid-and-invalid-cases">7. Valid and Invalid Cases</h2>

<h3>7.1 Valid cases</h3>

<p>
A valid case is one that a conforming toolchain should accept under the relevant base rules and active profiles.
For a valid case, the conformance note should normally state:
</p>

<ul>
  <li>why the case is valid,</li>
  <li>which constructs are being exercised,</li>
  <li>what derivation must preserve,</li>
  <li>what later lowering and backend handoff may specialize without semantic drift.</li>
</ul>

<h3>7.2 Invalid cases</h3>

<p>
An invalid case is one that a conforming toolchain should reject.
For an invalid case, the conformance note should normally state:
</p>

<ul>
  <li>why the case is invalid,</li>
  <li>which rule or boundary is being violated,</li>
  <li>why silent reinterpretation would be architecturally wrong.</li>
</ul>

<p>
A key design rule of this directory is:
</p>

<pre><code>explicit rejection
   is better than
silent semantic laundering
</code></pre>

<hr/>

<h2 id="expected-outcomes">8. Expected Outcomes</h2>

<p>
Conformance cases in this directory should express outcomes in a structured way.
At minimum, a case should make clear whether:
</p>

<ul>
  <li>validation is expected to pass or fail,</li>
  <li>derivation is allowed or forbidden,</li>
  <li>specific distinctions must remain recoverable,</li>
  <li>specific backend-family assumptions may be declared,</li>
  <li>specific unsupported situations must cause explicit rejection.</li>
</ul>

<p>
Examples of outcome language:
</p>

<ul>
  <li><strong>Expected: valid</strong></li>
  <li><strong>Expected: invalid</strong></li>
  <li><strong>Expected preservation:</strong> explicit local memory remains explicit</li>
  <li><strong>Expected preservation:</strong> <code>widget_value</code> and <code>widget_reference</code> remain distinct</li>
  <li><strong>Expected rejection:</strong> illegal feedback without explicit local memory</li>
</ul>

<hr/>

<h2 id="early-v01-conformance-focus">9. Early v0.1 Conformance Focus</h2>

<p>
For the first executable vertical slice of FROG v0.1, the most useful conformance focus is deliberately narrow.
Initial cases should concentrate on:
</p>

<ul>
  <li>basic interface participation,</li>
  <li>basic primitive execution,</li>
  <li>structured control in a small number of canonical cases,</li>
  <li>explicit local memory and legal feedback,</li>
  <li>UI value participation,</li>
  <li>UI object-style interaction through standardized primitives,</li>
  <li>correct rejection of boundary confusion and invalid cycles.</li>
</ul>

<p>
This is enough to support a first reference pipeline without pretending that all future conformance concerns are already closed.
</p>

<hr/>

<h2 id="relation-with-examples-and-reference-implementation">10. Relation with Examples and Reference Implementation</h2>

<p>
This directory should work together with:
</p>

<ul>
  <li><code>Examples/</code> — which provides named source programs,</li>
  <li><code>Implementations/Reference/</code> — which may try to process those programs through a reference pipeline.</li>
</ul>

<p>
The relationship is:
</p>

<pre><code>Examples/
   gives named source cases

Conformance/
   says what should happen

Implementations/Reference/
   tries to do it correctly
</code></pre>

<p>
A useful early pattern is:
</p>

<ul>
  <li>one example program,</li>
  <li>one conformance note describing expected behavior,</li>
  <li>one reference-implementation attempt to load, validate, derive, lower, emit a contract, and eventually run it.</li>
</ul>

<hr/>

<h2 id="future-growth">11. Future Growth</h2>

<p>
Later versions of this directory may grow toward:
</p>

<ul>
  <li>richer valid and invalid corpora,</li>
  <li>profile-specific cases,</li>
  <li>backend-family-specific compatibility cases,</li>
  <li>more explicit preservation checks,</li>
  <li>formal steward-driven certification material.</li>
</ul>

<p>
In base v0.1, that future should remain visible,
but the present directory should stay compact and useful.
</p>

<hr/>

<h2 id="summary">12. Summary</h2>

<p>
This directory contains early conformance material for the published FROG specification.
Its role is to make expected outcomes explicit:
what should validate,
what should fail,
what should be preserved,
and what should be rejected rather than silently reinterpreted.
</p>

<p>
Conformance material is downstream from the normative specification.
It does not define the language.
It helps implementations stay aligned with it.
</p>