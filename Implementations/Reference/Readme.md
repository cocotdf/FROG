<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG Reference Implementation</h1>

<p align="center">
  Non-normative reference implementation workspace for early FROG toolchain experiments<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-directory-exists">2. Why this Directory Exists</a></li>
  <li><a href="#status-and-normative-boundary">3. Status and Normative Boundary</a></li>
  <li><a href="#architectural-position">4. Architectural Position</a></li>
  <li><a href="#scope-of-the-reference-implementation">5. Scope of the Reference Implementation</a></li>
  <li><a href="#first-target-family">6. First Target Family</a></li>
  <li><a href="#planned-subdirectories">7. Planned Subdirectories</a></li>
  <li><a href="#toolchain-intent">8. Toolchain Intent</a></li>
  <li><a href="#ui-handling-in-the-first-reference-runtime">9. UI Handling in the First Reference Runtime</a></li>
  <li><a href="#relation-with-examples-and-conformance">10. Relation with Examples and Conformance</a></li>
  <li><a href="#what-this-directory-must-not-do">11. What this Directory Must Not Do</a></li>
  <li><a href="#status-in-v01">12. Status in v0.1</a></li>
  <li><a href="#summary">13. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory is the home of a future <strong>reference implementation</strong> for the published FROG specification.
Its role is to provide a practical implementation workspace for early end-to-end experiments such as:
</p>

<ul>
  <li>loading canonical <code>.frog</code> source,</li>
  <li>validating source against published rules,</li>
  <li>deriving open Execution IR,</li>
  <li>performing controlled lowering,</li>
  <li>emitting a backend contract,</li>
  <li>running that result through a first reference runtime family.</li>
</ul>

<p>
This directory is intentionally practical.
It exists to make the specification executable.
It does not replace the specification itself.
</p>

<hr/>

<h2 id="why-this-directory-exists">2. Why this Directory Exists</h2>

<p>
The repository defines an open language specification and its surrounding layers,
not one mandatory product implementation.
That architectural separation is essential.
However, once the core specification boundaries become coherent enough,
it becomes valuable to test them with a reference pipeline.
</p>

<p>
This directory exists to support that next step.
It should provide:
</p>

<ul>
  <li>a concrete place to experiment with a first FROG toolchain,</li>
  <li>a practical consumer of the published derivation and backend-contract boundaries,</li>
  <li>a compact proving ground for examples and early conformance cases,</li>
  <li>a non-normative implementation baseline that can reveal specification gaps without becoming the owner of language truth.</li>
</ul>

<hr/>

<h2 id="status-and-normative-boundary">3. Status and Normative Boundary</h2>

<p>
This directory is <strong>non-normative</strong>.
It is part of the repository,
but it does not own the language.
</p>

<p>
Normative ownership remains in the published specification layers:
</p>

<ul>
  <li><code>Expression/</code> — canonical source structure,</li>
  <li><code>Language/</code> — validated semantic truth,</li>
  <li><code>Libraries/</code> — intrinsic primitive identities and primitive-local contracts,</li>
  <li><code>Profiles/</code> — optional standardized capability families,</li>
  <li><code>IR/</code> — execution-facing representation, derivation, construction, identity, lowering, and backend handoff boundaries,</li>
  <li><code>IDE/</code> — authoring-facing and observability-facing tooling concerns.</li>
</ul>

<p>
The reference implementation may expose ambiguities or missing pieces in those layers.
When that happens,
the fix belongs in the owning specification document,
not in private implementation folklore.
</p>

<hr/>

<h2 id="architectural-position">4. Architectural Position</h2>

<p>
The reference implementation should be understood as a <strong>consumer-side implementation workspace</strong> downstream from the published specification:
</p>

<pre><code>canonical source
      |
      v
validated program meaning
      |
      v
Execution IR
      |
      v
lowering
      |
      v
backend contract
      |
      v
reference implementation consumption
</code></pre>

<p>
In other words:
</p>

<ul>
  <li>this directory is not the owner of canonical source,</li>
  <li>this directory is not the owner of validated semantic truth,</li>
  <li>this directory is not the owner of the open IR architecture,</li>
  <li>this directory is a consumer and experimenter of those published boundaries.</li>
</ul>

<hr/>

<h2 id="scope-of-the-reference-implementation">5. Scope of the Reference Implementation</h2>

<p>
The first reference implementation should aim for a <strong>small vertical slice</strong>, not for a complete industrial runtime.
Its initial scope should include:
</p>

<ul>
  <li>loader behavior for canonical source,</li>
  <li>validation behavior for the selected MVP constructs,</li>
  <li>Execution IR derivation according to the published derivation boundary,</li>
  <li>controlled lowering for a first backend family,</li>
  <li>backend contract emission for that family,</li>
  <li>a first runtime capable of consuming the contract and executing a compact set of examples.</li>
</ul>

<p>
The initial goal is not maximal coverage.
The initial goal is architectural coherence.
</p>

<hr/>

<h2 id="first-target-family">6. First Target Family</h2>

<p>
The recommended first backend family for the reference implementation is a compact host-oriented family such as:
</p>

<pre><code>reference_host_runtime_ui_binding
</code></pre>

<p>
This family is intended to remain simple enough for early experimentation while still covering an important vertical slice:
</p>

<ul>
  <li>ordinary executable primitives,</li>
  <li>public interface boundaries,</li>
  <li>explicit local memory,</li>
  <li>basic UI value participation,</li>
  <li>basic UI object-style interaction through standardized UI primitives.</li>
</ul>

<p>
The first reference implementation should stay deliberately conservative:
</p>

<ul>
  <li>single process,</li>
  <li>host runtime,</li>
  <li>deterministic step-oriented execution,</li>
  <li>no first-class standardized event execution model in base v0.1,</li>
  <li>no requirement to define one universal runtime-private architecture for all future implementations.</li>
</ul>

<hr/>

<h2 id="planned-subdirectories">7. Planned Subdirectories</h2>

<p>
A useful initial structure is:
</p>

<pre><code>Implementations/Reference/
├── CLI/
├── Loader/
├── Validator/
├── Deriver/
├── Lowerer/
├── ContractEmitter/
├── Runtime/
└── UIHost/
</code></pre>

<p>
These subdirectories are not separate language layers.
They are implementation-facing work areas for one reference pipeline.
</p>

<ul>
  <li><code>CLI/</code> — user-facing command entry points for the reference toolchain,</li>
  <li><code>Loader/</code> — source loading and structural intake,</li>
  <li><code>Validator/</code> — MVP validation logic,</li>
  <li><code>Deriver/</code> — consumption of the published derivation boundary,</li>
  <li><code>Lowerer/</code> — controlled specialization for the first target family,</li>
  <li><code>ContractEmitter/</code> — backend contract emission,</li>
  <li><code>Runtime/</code> — runtime-side contract consumption and execution,</li>
  <li><code>UIHost/</code> — host-side UI binding for the first reference family.</li>
</ul>

<hr/>

<h2 id="toolchain-intent">8. Toolchain Intent</h2>

<p>
The first reference toolchain should support a compact sequence of operations such as:
</p>

<pre><code>validate
derive-ir
lower
emit-contract
run
</code></pre>

<p>
A useful mental model is:
</p>

<pre><code>frogc validate file.frog
frogc derive-ir file.frog
frogc lower file.frog
frogc emit-contract file.frog
frogc run file.frog
</code></pre>

<p>
This is only a conceptual starting point.
The exact command-line surface may evolve.
What matters is that the implementation reflects the already published boundaries instead of skipping over them.
</p>

<hr/>

<h2 id="ui-handling-in-the-first-reference-runtime">9. UI Handling in the First Reference Runtime</h2>

<p>
The first reference runtime may support a minimal published UI slice, but it should remain intentionally narrow.
The initial UI scope should cover:
</p>

<ul>
  <li><code>widget_value</code> participation,</li>
  <li><code>widget_reference</code> participation,</li>
  <li><code>frog.ui.property_read</code>,</li>
  <li><code>frog.ui.property_write</code>,</li>
  <li><code>frog.ui.method_invoke</code>.</li>
</ul>

<p>
The first reference runtime should not silently expand this into a fully standardized event system.
Instead, it should remain compatible with a conservative model such as:
</p>

<ul>
  <li>value binding,</li>
  <li>reference binding,</li>
  <li>deterministic host-managed UI update points,</li>
  <li>explicit runtime-side handling of standardized UI primitives.</li>
</ul>

<p>
This keeps the implementation aligned with the current published scope while still making the vertical slice executable.
</p>

<hr/>

<h2 id="relation-with-examples-and-conformance">10. Relation with Examples and Conformance</h2>

<p>
This directory should work together with:
</p>

<ul>
  <li><code>Examples/</code> — which provides named source programs,</li>
  <li><code>Conformance/</code> — which states expected acceptance, rejection, and preservation behavior.</li>
</ul>

<p>
The intended relationship is:
</p>

<pre><code>Examples/
   gives the source cases

Conformance/
   says what should happen

Implementations/Reference/
   tries to do it correctly
</code></pre>

<p>
The first reference implementation should therefore focus on the first named example slices rather than trying to support the whole language at once.
</p>

<hr/>

<h2 id="what-this-directory-must-not-do">11. What this Directory Must Not Do</h2>

<p>
This directory must not:
</p>

<ul>
  <li>pretend that one implementation automatically becomes the language definition,</li>
  <li>silently redefine source structure,</li>
  <li>silently redefine semantic truth,</li>
  <li>silently replace the published IR boundaries with private shortcuts,</li>
  <li>hide unsupported features behind silent reinterpretation,</li>
  <li>claim that one runtime-private architecture is the universal FROG runtime.</li>
</ul>

<p>
If a private shortcut becomes attractive but conflicts with the published architecture,
the specification should be clarified first rather than overwritten by implementation habit.
</p>

<hr/>

<h2 id="status-in-v01">12. Status in v0.1</h2>

<p>
In base v0.1, this directory should remain compact and disciplined.
The first goal is not to produce a feature-complete industrial platform.
The first goal is to prove that the published boundaries are strong enough to support a coherent end-to-end slice.
</p>

<p>
A good first success condition is:
</p>

<ul>
  <li>load a small <code>.frog</code> example,</li>
  <li>validate it,</li>
  <li>derive an open execution-facing IR,</li>
  <li>lower it for the first backend family,</li>
  <li>emit a backend contract,</li>
  <li>run it through the first reference runtime.</li>
</ul>

<hr/>

<h2 id="summary">13. Summary</h2>

<p>
This directory is the home of a future non-normative reference implementation for FROG.
Its role is to make the published specification executable through a disciplined vertical slice:
source,
validation,
IR derivation,
lowering,
backend contract emission,
and reference-family runtime consumption.
</p>

<p>
It is practical by design,
but it does not own the language.
It is a consumer of the published architecture,
not a replacement for it.
</p>