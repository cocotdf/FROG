<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
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
  <li><a href="#why-this-directory-exists">3. Why This Directory Exists</a></li>
  <li><a href="#definition-of-conformance">4. Definition of Conformance</a></li>
  <li><a href="#non-goals">5. Non-Goals</a></li>
  <li><a href="#relation-with-specification-ownership">6. Relation with Specification Ownership</a></li>
  <li><a href="#critical-boundaries">7. Critical Boundaries</a></li>
  <li><a href="#directory-structure">8. Directory Structure</a></li>
  <li><a href="#published-cases">9. Published Cases</a></li>
  <li><a href="#expected-outcomes">10. Expected Outcomes</a></li>
  <li><a href="#active-v01-conformance-focus">11. Active v0.1 Conformance Focus</a></li>
  <li><a href="#relation-with-examples-ir-profiles-and-reference-implementation">12. Relation with Examples, IR, Profiles, and Reference Implementation</a></li>
  <li><a href="#future-growth">13. Future Growth</a></li>
  <li><a href="#summary">14. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the public conformance surface of the published FROG repository.
</p>

<p>
It publishes explicit cases that make the specification testable, reviewable, and comparable across independent implementations.
</p>

<p>
It answers three fundamental questions:
</p>

<pre>What must be accepted?
What must be rejected?
What must be preserved?</pre>

<p>
This directory does not define the language by itself. It makes already-published language law operationally checkable. Conformance therefore sits at the boundary between repository truth and observable implementation behavior. It turns architectural distinctions into public expectations.
</p>

<p>
In v0.1, that public truth surface is not limited to source acceptance or semantic rejection alone. It also includes preservation obligations across the published execution corridor:
</p>

<pre>.frog source
   -&gt;
loadability
   -&gt;
structural validity
   -&gt;
validated meaning
   -&gt;
canonical Execution IR document
   -&gt;
canonical JSON IR validation where applicable
   -&gt;
later lowering / backend-facing handoff where applicable
   -&gt;
declared backend-family consumption where applicable
   -&gt;
bounded executable truth where explicitly published</pre>

<p>
Conformance therefore already matters to source law, semantic law, IR law, compiler-corridor law, and bounded executable truth where the published corpus already exposes such anchors.
</p>

<hr/>

<h2 id="core-purpose">2. Core Purpose</h2>

<p>
The purpose of conformance is to transform specification rules into checkable public expectations.
</p>

<p>
The repository-level model is:
</p>

<pre>Specification   = defines the rules
Conformance     = exposes testable cases
Implementation  = must behave accordingly</pre>

<p>
A conforming implementation MAY vary internally. It MUST NOT vary in published accept / reject / preserve outcomes for the same published case while still claiming conformance to the same published repository state.
</p>

<p>
Conformance therefore prevents the following drift:
</p>

<pre>parseable file
        -/-> structurally valid canonical source

structurally valid canonical source
        -/-> validated meaning

validated meaning
        -/-> arbitrary execution-facing form

implementation convenience
        -/-> language truth

"it runs"
        -/-> "it is correct"</pre>

<p>
Conformance is therefore not a commentary layer. It is the public truth surface that makes published repository law observable, comparable, and reviewable.
</p>

<hr/>

<h2 id="why-this-directory-exists">3. Why This Directory Exists</h2>

<p>
FROG is specification-first and implementation-independent.
</p>

<p>
That creates a requirement:
</p>

<pre>multiple independent implementations
            require
one shared public validation surface</pre>

<p>
This directory provides that surface.
</p>

<p>
It ensures that:
</p>

<ul>
  <li>implementations do not silently diverge,</li>
  <li>semantic meaning is not reinterpreted implicitly,</li>
  <li>invalid constructs are rejected instead of silently repaired,</li>
  <li>critical distinctions remain visible across loadability, structural validation, semantic validation, IR derivation, IR construction, canonical JSON validation, later lowering / backend-facing handoff, declared backend-family consumption, and bounded executable truth where published.</li>
</ul>

<p>
Conformance is therefore not commentary. It is the public truth surface that turns specification architecture into comparable observable behavior.
</p>

<hr/>

<h2 id="definition-of-conformance">4. Definition of Conformance</h2>

<p>
Conformance is alignment with the published specification across the relevant architectural stages.
</p>

<p>
It includes:
</p>

<ul>
  <li>correct rejection of malformed or non-loadable source where applicable,</li>
  <li>correct source-structure validation,</li>
  <li>correct semantic validation,</li>
  <li>correct rejection where validated meaning does not exist,</li>
  <li>correct preservation of distinctions across derivation into the canonical Execution IR document,</li>
  <li>correct canonical-IR construction and canonical JSON compatibility where the case reaches that stage,</li>
  <li>correct preservation of required boundaries across later lowering and backend-facing handoff where applicable,</li>
  <li>correct staged acceptance or rejection across declared compiler-corridor stages where applicable,</li>
  <li>correct bounded executable behavior where the published corpus already defines executable anchor truth.</li>
</ul>

<p>
Conformance therefore requires both:
</p>

<pre>correct accept / reject decisions
and
correct preservation of required distinctions</pre>

<p>
A conforming implementation is not merely an implementation that “does something plausible”. It is an implementation that behaves compatibly with the published public truth surface.
</p>

<hr/>

<h2 id="non-goals">5. Non-Goals</h2>

<p>
This directory is not:
</p>

<ul>
  <li>a replacement for the language specification,</li>
  <li>a replacement for Expression, Language, Libraries, IR, Profiles, or IDE ownership,</li>
  <li>a private implementation test folder,</li>
  <li>a benchmark suite,</li>
  <li>a repository for examples presented as hidden law,</li>
  <li>a place where backend convenience replaces published architecture,</li>
  <li>a place where execution success alone is treated as proof of correctness.</li>
</ul>

<p>
Conformance is public truth, not implementation folklore.
</p>

<hr/>

<h2 id="relation-with-specification-ownership">6. Relation with Specification Ownership</h2>

<p>
This directory depends on the rest of the specification but does not replace it.
</p>

<p>
The intended ownership model remains:
</p>

<pre>Expression/
   owns canonical source representation

Language/
   owns validated meaning

Libraries/
   own intrinsic primitive law

IR/
   owns canonical execution-facing representation,
   derivation,
   schema posture,
   lowering,
   backend contract

Profiles/
   own optional capability corridors
   and any bounded profile-level execution contracts

Conformance/
   exposes public cases that test the published rules</pre>

<p>
Conformance therefore reads the specification. It does not silently redefine it.
</p>

<hr/>

<h2 id="critical-boundaries">7. Critical Boundaries</h2>

<p>
Conformance must preserve the repository-wide distinctions that the published architecture depends on.
</p>

<p>
These include, at minimum:
</p>

<ul>
  <li>loadable source vs structurally valid canonical source,</li>
  <li>structurally valid source vs semantically accepted program,</li>
  <li>validated meaning vs canonical Execution IR,</li>
  <li>open IR vs lowered form,</li>
  <li>lowered form vs backend contract,</li>
  <li>backend contract vs backend-family consumption,</li>
  <li>backend-family consumability vs bounded executable truth,</li>
  <li>profile validity vs execution-contract satisfaction where a published profile-level execution contract exists,</li>
  <li>examples vs normative law,</li>
  <li>reference implementation behavior vs normative truth.</li>
</ul>

<p>
Compactly:
</p>

<pre>accepted upstream
does not automatically imply
accepted downstream

backend-consumable
does not automatically imply
execution-ready
unless the published conformance corpus says so explicitly</pre>

<hr/>

<h2 id="directory-structure">8. Directory Structure</h2>

<p>
The current published directory structure is layered rather than uniform.
</p>

<p>
At top level:
</p>

<pre>Conformance/
├── Readme.md
├── valid/
└── invalid/</pre>

<p>
Inside <code>valid/</code>, the published corpus currently combines:
</p>

<ul>
  <li>a top-level historical block of valid source-shape, architectural, IR-sensitive, and executable-anchor cases,</li>
  <li>a dedicated <code>compiler/</code> family,</li>
  <li>a dedicated <code>executable/</code> family.</li>
</ul>

<p>
This means the published positive corpus is already hybrid:
</p>

<pre>top-level historical valid cases
   +
valid/compiler/
   +
valid/executable/</pre>

<p>
The key architectural rule is therefore not “every case must already fit one uniform subtree”.
The key rule is:
</p>

<pre>the published corpus may grow by structured subfamilies
without erasing earlier top-level anchors</pre>

<hr/>

<h2 id="published-cases">9. Published Cases</h2>

<p>
The currently published conformance corpus is staged rather than monolithic.
</p>

<h3>9.1 Published top-level valid anchors</h3>

<p>
The published positive corpus already contains a top-level historical block under <code>Conformance/valid/</code> that includes:
</p>

<ul>
  <li>minimal canonical source-shape cases,</li>
  <li>optional-section validity cases,</li>
  <li>front-panel and connector structure cases,</li>
  <li>named executable anchors,</li>
  <li>architectural distinction cases tied to canonical Execution IR correspondence discipline.</li>
</ul>

<p>
This top-level block remains part of the published truth surface and must not be retroactively described as though it had been replaced already.
</p>

<h3>9.2 Early executable anchor cases</h3>

<p>
The published top-level positive corpus includes the following early valid executable anchor cases:
</p>

<pre>01_pure_addition.md
02_ui_value_roundtrip.md
03_ui_property_write.md
04_stateful_feedback_delay.md</pre>

<p>
These anchors are important because they already expose bounded executable truth across four distinct axes:
</p>

<ul>
  <li>pure dataflow computation,</li>
  <li>natural <code>widget_value</code> participation,</li>
  <li><code>widget_reference</code> object-operation participation,</li>
  <li>explicit state through feedback and delay.</li>
</ul>

<p>
They therefore already constrain future compiler and runtime growth, even before the entire executable corpus becomes fully normalized under one subtree.
</p>

<h3>9.3 Additional top-level architectural distinction cases</h3>

<p>
The same published top-level positive corpus also includes additional cases such as:
</p>

<pre>05_public_interface_and_widget_participation_distinct.md
07_widget_reference_remains_distinct_from_widget_value.md</pre>

<p>
and later correspondence-sensitive cases with higher numbering that protect canonical Execution IR boundary distinctions.
</p>

<p>
This means the top-level positive corpus is not only “early examples”.
It is already part of the published architectural truth surface.
</p>

<h3>9.4 Compiler-corridor families</h3>

<p>
The conformance tree also opens a dedicated compiler-corridor family:
</p>

<pre>valid/compiler/
invalid/compiler/</pre>

<p>
These families extend the public truth surface beyond ordinary language validity and IR correctness by making later corridor stages readable and testable:
</p>

<pre>semantic acceptance
   -&gt;
IR derivation
   -&gt;
canonical JSON IR validity where applicable
   -&gt;
lowering eligibility
   -&gt;
backend-contract eligibility
   -&gt;
declared backend-family consumability</pre>

<p>
The positive side currently names the first three published corridor anchors:
</p>

<pre>valid/compiler/01_pure_arithmetic_is_consumable
valid/compiler/02_structured_control_is_consumable
valid/compiler/03_explicit_state_is_consumable</pre>

<p>
The negative side currently names staged rejection anchors along the downstream corridor.
</p>

<h3>9.5 Executable subfamily posture</h3>

<p>
The published positive tree also already contains a dedicated <code>valid/executable/</code> subtree.
</p>

<p>
That means the repository has already opened a structural place for executable-family growth.
</p>

<p>
However, the top-level executable anchors still remain published at the root of <code>valid/</code>.
The correct reading is therefore:
</p>

<pre>top-level executable anchors
   remain published historical anchors

valid/executable/
   provides structured executable-family growth

the two are not mutually exclusive</pre>

<hr/>

<h2 id="expected-outcomes">10. Expected Outcomes</h2>

<p>
Each case expresses structured expectations such as:
</p>

<ul>
  <li>Expected loadability: <code>loadable</code> | <code>not loadable</code></li>
  <li>Expected structural validity: <code>valid</code> | <code>invalid</code></li>
  <li>Expected meaning: <code>established</code> | <code>not established</code></li>
  <li>Expected IR result: <code>derivable</code> | <code>not derivable</code></li>
  <li>Expected IR schema result: <code>schema-valid</code> | <code>not schema-valid</code></li>
  <li>Expected lowering result: <code>lowerable</code> | <code>rejected</code> | <code>not applicable</code></li>
  <li>Expected backend-contract result: <code>emittable</code> | <code>not emittable</code> | <code>not applicable</code></li>
  <li>Expected backend-family result: <code>consumable</code> | <code>rejected</code> | <code>not applicable</code></li>
  <li>Expected executable result where already published: bounded positive executable truth for the named anchor or executable-family case</li>
</ul>

<p>
The expected question is therefore not only:
</p>

<pre>Did the tool run?</pre>

<p>
but also:
</p>

<pre>Did it accept or reject at the correct stage?
Did it preserve the correct distinctions?
Did it avoid inventing meaning that the specification does not grant?
Did it match the published executable truth where executable anchors already exist?</pre>

<hr/>

<h2 id="active-v01-conformance-focus">11. Active v0.1 Conformance Focus</h2>

<p>
The active v0.1 conformance focus is now multi-layered.
</p>

<p>
The published corpus already contains:
</p>

<ul>
  <li>top-level source-shape truth,</li>
  <li>top-level architectural distinction truth,</li>
  <li>top-level early executable anchors,</li>
  <li>a dedicated compiler-corridor family,</li>
  <li>a dedicated executable subtree for structured future executable growth.</li>
</ul>

<p>
This is already a substantial closure step.
</p>

<p>
It means the repository no longer treats downstream execution as future-only strategy. It already exposes:
</p>

<pre>source truth
   +
meaning truth
   +
IR-sensitive truth
   +
early executable truth
   +
compiler-corridor truth
   +
room for structured executable-family growth</pre>

<p>
However, the current published focus remains conservative:
</p>

<ul>
  <li>the top-level valid corpus remains important,</li>
  <li>structured subfamilies extend rather than erase earlier anchors,</li>
  <li>future executable normalization should not rewrite history by pretending the top-level executable anchors never existed.</li>
</ul>

<hr/>

<h2 id="relation-with-examples-ir-profiles-and-reference-implementation">12. Relation with Examples, IR, Profiles, and Reference Implementation</h2>

<p>
This directory must be read together with nearby repository areas, but without ownership collapse.
</p>

<ul>
  <li><code>Examples/</code> provides illustrative named slices. Examples do not become hidden language law.</li>
  <li><code>IR/</code> owns canonical execution-facing representation, derivation, identity, construction, schema posture, lowering, and backend-facing boundaries.</li>
  <li><code>Profiles/</code> owns optional capability corridors such as <code>native_cpu_llvm</code>, and may later own bounded execution-contract companion documents where published.</li>
  <li><code>Implementations/Reference/</code> is a non-normative executable workspace. It does not become hidden semantic truth.</li>
</ul>

<p>
The practical relation is:
</p>

<pre>Examples
   -&gt; illustrate

Conformance
   -&gt; expose public expectations

IR
   -&gt; define canonical execution-facing law

Profiles
   -&gt; bound optional downstream corridors

Reference implementation
   -&gt; consume the published layers without owning them</pre>

<p>
Where a case materially constrains IR derivation, identity, recoverability, lowering, or backend-facing handoff, the reader should cross-check:
</p>

<ul>
  <li><code>IR/Readme.md</code>,</li>
  <li><code>IR/Execution IR.md</code>,</li>
  <li><code>IR/Derivation rules.md</code>,</li>
  <li><code>IR/Identity and Mapping.md</code>,</li>
  <li><code>IR/Construction rules.md</code>,</li>
  <li><code>IR/Schema.md</code>,</li>
  <li><code>IR/Lowering.md</code>,</li>
  <li><code>IR/Backend contract.md</code>.</li>
</ul>

<p>
Where a case materially constrains later compiler-corridor stages, the reader should also cross-check:
</p>

<ul>
  <li><code>Profiles/Readme.md</code>,</li>
  <li><code>Profiles/Native CPU LLVM.md</code>,</li>
  <li>and any published Native CPU LLVM companion execution-contract document, if and when such a document is actually published.</li>
</ul>

<hr/>

<h2 id="future-growth">13. Future Growth</h2>

<p>
Future growth should remain conservative and corridor-oriented.
</p>

<p>
A good growth rule is:
</p>

<pre>close one public corridor fully
before opening many half-closed fronts</pre>

<p>
The preferred near-term growth order is therefore:
</p>

<pre>top-level source-shape and architectural closure
   -&gt;
top-level executable anchor preservation
   -&gt;
named compiler-corridor family closure
   -&gt;
structured executable-family growth
   -&gt;
later corridor expansion</pre>

<p>
That means future executable growth should:
</p>

<ul>
  <li>remain compatible with the already-published top-level executable anchors,</li>
  <li>avoid pretending those anchors never existed,</li>
  <li>treat <code>valid/executable/</code> as structured growth rather than retroactive erasure,</li>
  <li>keep the distinction explicit between backend-family consumability and broader execution-side closure.</li>
</ul>

<p>
Conformance growth should therefore follow publication maturity, not wishful scope expansion.
</p>

<hr/>

<h2 id="summary">14. Summary</h2>

<p>
This directory defines the public conformance surface of the published FROG specification.
</p>

<p>
It answers:
</p>

<pre>What must be accepted?
What must be rejected?
What must be preserved?</pre>

<p>
In v0.1, the active published conformance surface already includes:
</p>

<ul>
  <li>top-level source-shape and architectural truth,</li>
  <li>top-level early executable anchor cases,</li>
  <li>a named valid / invalid compiler-corridor family,</li>
  <li>a structured executable subtree for further executable-family growth.</li>
</ul>

<p>
It should therefore be read as a public truth surface for the full published corridor:
</p>

<pre>source
   -&gt;
meaning
   -&gt;
IR
   -&gt;
lowering
   -&gt;
backend handoff
   -&gt;
backend-family consumability
   -&gt;
bounded executable truth where already published</pre>

<p>
This keeps the repository disciplined:
</p>

<pre>specification defines

conformance checks

implementation must align</pre>

<p>
That is the intended role of <code>Conformance/</code> in FROG v0.1.
</p>
