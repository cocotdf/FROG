<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Conformance — Invalid Compiler Corridor Cases</h1>

<p align="center">
  <strong>Negative compiler-corridor conformance cases for published FROG execution paths</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-subdirectory-exists">2. Why This Subdirectory Exists</a></li>
  <li><a href="#position-in-the-conformance-corridor">3. Position in the Conformance Corridor</a></li>
  <li><a href="#what-invalid-compiler-corridor-means">4. What Invalid Compiler-Corridor Means</a></li>
  <li><a href="#four-primary-failure-classes">5. Four Primary Failure Classes</a></li>
  <li><a href="#what-these-cases-test">6. What These Cases Test</a></li>
  <li><a href="#what-these-cases-do-not-claim">7. What These Cases Do Not Claim</a></li>
  <li><a href="#relation-with-native_cpu_llvm">8. Relation with <code>native_cpu_llvm</code></a></li>
  <li><a href="#expected-case-structure">9. Expected Case Structure</a></li>
  <li><a href="#expected-outcome-classes">10. Expected Outcome Classes</a></li>
  <li><a href="#recommended-case-growth-order">11. Recommended Case Growth Order</a></li>
  <li><a href="#initial-v01-case-families">12. Initial v0.1 Case Families</a></li>
  <li><a href="#relation-with-valid-compiler-corridor-cases">13. Relation with Valid Compiler-Corridor Cases</a></li>
  <li><a href="#summary">14. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This subdirectory defines negative conformance cases for the compiler corridor of published FROG.
</p>

<p>
These cases are not generic invalid-language cases.
They are public rejection anchors for situations where a program or derived artifact may still be valid at one upstream stage, but must be rejected at a later compiler-corridor stage.
</p>

<p>
The relevant corridor is:
</p>

<pre><code>.frog
   -&gt;
structural validity
   -&gt;
semantic acceptance
   -&gt;
canonical Execution IR derivation
   -&gt;
canonical JSON IR validation where applicable
   -&gt;
lowering eligibility
   -&gt;
backend-contract eligibility
   -&gt;
declared backend-family consumability</code></pre>

<p>
This directory exists so that failures in the compiler corridor become explicit public truth rather than implicit implementation drift.
</p>

<hr/>

<h2 id="why-this-subdirectory-exists">2. Why This Subdirectory Exists</h2>

<p>
Once the repository recognizes a serious compiler-oriented corridor, it is no longer enough to publish only:
</p>

<ul>
  <li>ordinary source invalidity,</li>
  <li>ordinary semantic invalidity,</li>
  <li>ordinary IR-preservation invalidity.</li>
</ul>

<p>
It also becomes necessary to publish failures that occur later in the corridor.
</p>

<p>
This subdirectory therefore exists to expose cases where the repository can say:
</p>

<pre><code>this program slice
is not acceptable
for the declared compiler corridor stage

even if
some upstream stage was still accepted</code></pre>

<p>
That distinction is essential for industrial compilation work because otherwise implementations will silently disagree about where rejection belongs.
</p>

<hr/>

<h2 id="position-in-the-conformance-corridor">3. Position in the Conformance Corridor</h2>

<p>
These cases sit downstream from ordinary source and semantic validity and make later rejection boundaries public.
</p>

<p>
They belong to the following staged reading:
</p>

<pre><code>language-valid
   -&gt;
IR-derivable
   -&gt;
IR-schema-valid where applicable
   -&gt;
lowerable
   -&gt;
backend-contract-emittable
   -&gt;
backend-family-consumable</code></pre>

<p>
A compiler-corridor invalid case makes explicit where this staged progression must stop.
</p>

<hr/>

<h2 id="what-invalid-compiler-corridor-means">4. What Invalid Compiler-Corridor Means</h2>

<p>
An invalid compiler-corridor case is a published case that must be rejected at a declared downstream stage of the compiler corridor.
</p>

<p>
This means that the repository explicitly distinguishes:
</p>

<ul>
  <li>language invalidity,</li>
  <li>IR invalidity,</li>
  <li>lowering invalidity,</li>
  <li>backend-contract invalidity,</li>
  <li>backend-family consumer invalidity.</li>
</ul>

<p>
These are not interchangeable.
</p>

<p>
A key rule is:
</p>

<pre><code>upstream acceptance
   does not imply
downstream compiler-corridor acceptance</code></pre>

<p>
A program may therefore be:
</p>

<ul>
  <li>language-valid but profile-rejected,</li>
  <li>IR-derivable but not lowerable,</li>
  <li>lowerable but not backend-contract-emittable,</li>
  <li>contract-emittable but rejected by the declared backend-family consumer.</li>
</ul>

<hr/>

<h2 id="four-primary-failure-classes">5. Four Primary Failure Classes</h2>

<p>
This directory should treat the following four classes as the foundational mirrored rejection surface of the compiler corridor.
</p>

<h3>5.1 Language-valid but profile-rejected</h3>

<p>
The program is:
</p>

<ul>
  <li>structurally valid,</li>
  <li>semantically accepted by FROG,</li>
  <li>but outside the declared compilation profile surface.</li>
</ul>

<p>
Typical reason:
</p>

<ul>
  <li>the program exceeds the conservative accepted subset of the declared compilation profile.</li>
</ul>

<h3>5.2 IR-derivable but not lowerable</h3>

<p>
The program is:
</p>

<ul>
  <li>language-valid,</li>
  <li>derivable to canonical FROG Execution IR,</li>
  <li>but not lowerable under the declared corridor without semantic loss or illicit invention.</li>
</ul>

<p>
Typical reason:
</p>

<ul>
  <li>the implementation lacks a faithful lowering path for a semantically accepted construct under the declared corridor.</li>
</ul>

<h3>5.3 Lowerable but not backend-contract-emittable</h3>

<p>
The program or lowered form is:
</p>

<ul>
  <li>language-valid,</li>
  <li>IR-derivable,</li>
  <li>lowerable,</li>
  <li>but still cannot be emitted as a consumer-safe backend contract without ambiguity or hidden assumptions.</li>
</ul>

<p>
Typical reason:
</p>

<ul>
  <li>the required backend-facing assumptions cannot yet be stated explicitly enough.</li>
</ul>

<h3>5.4 Contract-emittable but consumer-rejected</h3>

<p>
The program and lowered form are:
</p>

<ul>
  <li>language-valid,</li>
  <li>IR-derivable,</li>
  <li>lowerable,</li>
  <li>backend-contract-emittable,</li>
  <li>but rejected by the declared backend-family consumer because the consumer cannot honor the declared assumptions.</li>
</ul>

<p>
Typical reason:
</p>

<ul>
  <li>consumer capability mismatch, unsupported contract version, or unsupported lowered commitments.</li>
</ul>

<hr/>

<h2 id="what-these-cases-test">6. What These Cases Test</h2>

<p>
These cases test the negative edges of the compiler corridor.
</p>

<p>
They may test, for example:
</p>

<ul>
  <li>that a valid FROG program is correctly rejected by a bounded profile claim,</li>
  <li>that explicit state is not silently compiled through an unfaithful lowering path,</li>
  <li>that structured control is not silently flattened when faithful lowering is unavailable,</li>
  <li>that a backend contract is rejected rather than emitted with hidden assumptions,</li>
  <li>that a backend-family consumer rejects unsupported contract content rather than silently reinterpreting it.</li>
</ul>

<p>
These cases therefore protect the corridor from false positives.
</p>

<hr/>

<h2 id="what-these-cases-do-not-claim">7. What These Cases Do Not Claim</h2>

<p>
These cases do not claim:
</p>

<ul>
  <li>that upstream validity disappears when a downstream stage rejects,</li>
  <li>that every rejection is a language error,</li>
  <li>that every backend-family consumer must reject for the same reason,</li>
  <li>that LLVM-oriented rejection becomes language truth,</li>
  <li>that profile rejection means semantic invalidity.</li>
</ul>

<p>
A downstream corridor rejection must remain staged and explicit.
</p>

<hr/>

<h2 id="relation-with-native_cpu_llvm">8. Relation with <code>native_cpu_llvm</code></h2>

<p>
For v0.1, the first intended downstream compilation corridor is the optional profile:
</p>

<pre><code>native_cpu_llvm</code></pre>

<p>
Accordingly, the first invalid compiler-corridor cases SHOULD preferentially target rejection boundaries relevant to that profile.
</p>

<p>
This means the first published negative cases SHOULD focus on situations such as:
</p>

<ul>
  <li>language-valid but outside the accepted conservative Native CPU LLVM subset,</li>
  <li>IR-derivable but not lowerable without semantic distortion,</li>
  <li>lowerable but not contract-emittable because required commitments remain ambiguous,</li>
  <li>contract-emittable but rejected by the LLVM-oriented native CPU consumer family for explicit capability reasons.</li>
</ul>

<hr/>

<h2 id="expected-case-structure">9. Expected Case Structure</h2>

<p>
Each invalid compiler-corridor case SHOULD state, as applicable:
</p>

<ul>
  <li>the source scope,</li>
  <li>the semantic scope,</li>
  <li>the canonical IR expectation,</li>
  <li>the canonical JSON IR expectation where relevant,</li>
  <li>the lowering expectation,</li>
  <li>the backend-contract expectation,</li>
  <li>the declared profile scope,</li>
  <li>the declared backend-family scope,</li>
  <li>the exact rejection stage,</li>
  <li>the exact rejection reason.</li>
</ul>

<p>
A useful pattern is:
</p>

<pre><code>Expected loadability:
Expected structural validity:
Expected semantic acceptance:
Expected IR derivation:
Expected IR schema result:
Expected lowering result:
Expected backend-contract result:
Expected backend-family consumption:
Declared profile scope:
Declared backend-family scope:
Expected rejection stage:
Expected rejection reason:</code></pre>

<hr/>

<h2 id="expected-outcome-classes">10. Expected Outcome Classes</h2>

<p>
Negative compiler-corridor cases will typically use outcome declarations such as:
</p>

<ul>
  <li><code>Expected structural validity: valid</code></li>
  <li><code>Expected semantic acceptance: accepted</code></li>
  <li><code>Expected IR derivation: derivable</code></li>
  <li><code>Expected lowering result: rejected</code></li>
  <li><code>Expected backend-contract result: not emittable</code></li>
  <li><code>Expected backend-family consumption: rejected</code></li>
</ul>

<p>
The key discipline is that the rejection stage must be explicit.
</p>

<p>
For example:
</p>

<pre><code>language-valid
+
IR-derivable
+
lowering-rejected</code></pre>

<p>
is not the same thing as:
</p>

<pre><code>language-valid
+
lowerable
+
backend-consumer-rejected</code></pre>

<hr/>

<h2 id="recommended-case-growth-order">11. Recommended Case Growth Order</h2>

<p>
Growth in this directory SHOULD remain disciplined and mirrored against the positive compiler corridor.
</p>

<p>
The recommended order is:
</p>

<pre><code>profile rejection
   -&gt;
lowering rejection
   -&gt;
backend-contract rejection
   -&gt;
backend-family consumer rejection</code></pre>

<p>
This order mirrors the downstream corridor in the cleanest way.
</p>

<hr/>

<h2 id="initial-v01-case-families">12. Initial v0.1 Case Families</h2>

<p>
The first coherent negative case families for this directory SHOULD be:
</p>

<h3>12.1 Language-valid but Native CPU LLVM profile-rejected</h3>

<ul>
  <li>programs accepted by core FROG but outside the conservative first compiled subset,</li>
  <li>programs that depend on surfaces intentionally excluded from the first compiled corridor.</li>
</ul>

<h3>12.2 IR-derivable but not lowerable</h3>

<ul>
  <li>programs whose semantics survive into canonical IR but for which no faithful lowering path is yet available under the declared profile.</li>
</ul>

<h3>12.3 Lowerable but not backend-contract-emittable</h3>

<ul>
  <li>programs where lowering can proceed conceptually, but the producer cannot state a consumer-safe handoff without ambiguity.</li>
</ul>

<h3>12.4 Contract-emittable but consumer-rejected</h3>

<ul>
  <li>programs whose contract is structurally valid and explicit, but whose declared backend-family consumer cannot honor it.</li>
</ul>

<p>
These four families are enough to make the downstream rejection story explicit and usable.
</p>

<hr/>

<h2 id="relation-with-valid-compiler-corridor-cases">13. Relation with Valid Compiler-Corridor Cases</h2>

<p>
This directory must be read together with the positive side:
</p>

<ul>
  <li><code>Conformance/valid/compiler/</code></li>
</ul>

<p>
The two directories should eventually form a mirrored public truth surface for the first compiler corridor.
</p>

<p>
The positive side says:
</p>

<pre><code>this corridor stage is accepted</code></pre>

<p>
The negative side says:
</p>

<pre><code>this corridor stage must reject here
and for this reason</code></pre>

<p>
Both are required for serious public compiler-corridor discipline.
</p>

<hr/>

<h2 id="summary">14. Summary</h2>

<p>
This subdirectory defines negative conformance cases for the published FROG compiler corridor.
</p>

<p>
Its role is to make downstream rejection boundaries explicit after ordinary language validity has already been established where applicable.
</p>

<p>
The four foundational failure classes are:
</p>

<ul>
  <li>language-valid but profile-rejected,</li>
  <li>IR-derivable but not lowerable,</li>
  <li>lowerable but not backend-contract-emittable,</li>
  <li>contract-emittable but consumer-rejected.</li>
</ul>

<p>
For v0.1, the first intended target is the conservative subset of the optional <code>native_cpu_llvm</code> profile.
</p>

<p>
This keeps the compiler corridor explicit not only on the success path, but also on the rejection path.
</p>
