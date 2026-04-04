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
Conformance therefore already matters to the compiler corridor and already contains early executable truth anchors, even while broader execution-ready structuring remains a later consolidation step.
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
  <li>correct bounded executable behavior where the repository has already published executable anchor truth.</li>
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
The current published directory structure is:
</p>

<pre>Conformance/
├── Readme.md
├── valid/
│   └── compiler/
└── invalid/
    └── compiler/</pre>

<p>
The root <code>valid/</code> and <code>invalid/</code> directories remain the primary home of the published conformance corpus.
</p>

<p>
The nested <code>compiler/</code> families extend that corpus along a later compiler-corridor reading without replacing the root valid / invalid structure.
</p>

<p>
This means the published conformance tree currently mixes:
</p>

<ul>
  <li>top-level source-shape and architectural cases,</li>
  <li>top-level early positive executable anchor cases,</li>
  <li>nested compiler-corridor families.</li>
</ul>

<p>
That mixed structure is intentional in the current published state. It already exposes executable truth anchors without yet requiring a fully separated <code>valid/executable/</code> or <code>invalid/executable/</code> family.
</p>

<hr/>

<h2 id="published-cases">9. Published Cases</h2>

<p>
The currently published conformance corpus is staged rather than monolithic.
</p>

<h3>9.1 Published top-level source-shape block</h3>

<p>
The published top-level source-shape block currently includes root valid / invalid material that keeps loadability, structural validity, and early semantic accept / reject behavior visible at the top level of the corpus.
</p>

<h3>9.2 Early valid executable anchor cases</h3>

<p>
The published corpus also already contains four early positive executable anchor cases:
</p>

<pre>01_pure_addition
02_ui_value_roundtrip
03_ui_property_write
04_stateful_feedback_delay</pre>

<p>
These anchor cases show that conformance is not only about abstract rejection. It already covers minimal positive executable slices that the published architecture is expected to support.
</p>

<p>
These cases are especially important because they already span:
</p>

<ul>
  <li>a pure dataflow slice,</li>
  <li>a UI value path slice,</li>
  <li>a UI object-operation slice,</li>
  <li>an explicit state / delay slice.</li>
</ul>

<p>
Together they already constrain the future execution and compilation corridor by proving that the repository truth surface is not limited to syntax or abstract semantics alone.
</p>

<h3>9.3 Architectural boundary progression</h3>

<p>
The published corpus also includes top-level material that makes architectural boundary mistakes publicly visible, including cases where source validity, semantic validity, IR derivability, and preservation obligations must not be silently collapsed.
</p>

<h3>9.4 Additional standalone invalid architectural cases</h3>

<p>
The top-level negative corpus also includes standalone rejection cases that remain useful independently of the later nested compiler-corridor families.
</p>

<h3>9.5 IR recoverability and correspondence-sensitive cases</h3>

<p>
The published corpus already includes cases that materially constrain IR identity, recoverability, and correspondence discipline.
</p>

<p>
This is one of the most important current published areas for the future compiler corridor, because a serious backend cannot be allowed to consume an IR that has already lost attribution, ownership, or distinction boundaries.
</p>

<h3>9.6 Compiler-corridor families</h3>

<p>
The conformance tree now also opens two nested compiler-corridor families:
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
The negative side currently names the first four staged rejection anchors:
</p>

<pre>invalid/compiler/01_language_valid_but_profile_rejected
invalid/compiler/02_ir_derivable_but_not_lowerable
invalid/compiler/03_lowerable_but_not_backend_contract_emittable
invalid/compiler/04_contract_emittable_but_consumer_rejected</pre>

<p>
These two mirrored families are intentionally ordered along the downstream corridor:
</p>

<ul>
  <li>pure computation,</li>
  <li>structured control,</li>
  <li>explicit state</li>
</ul>

<p>
on the positive side, and:
</p>

<ul>
  <li>profile rejection,</li>
  <li>lowering rejection,</li>
  <li>backend-contract rejection,</li>
  <li>backend-family consumer rejection</li>
</ul>

<p>
on the negative side.
</p>

<p>
For v0.1, the first intended downstream profile target for these families is the conservative subset of <code>native_cpu_llvm</code>.
</p>

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
  <li>Expected executable result where already published at top level: bounded positive executable truth for the named anchor case</li>
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
The active v0.1 conformance focus is now two-part.
</p>

<p>
First, the repository already publishes top-level executable anchors that prove conformance is not limited to rejection or abstract preservation.
</p>

<p>
Second, the repository now also publishes a named compiler corridor through the nested <code>valid/compiler/</code> and <code>invalid/compiler/</code> families.
</p>

<p>
More precisely, the current public truth surface concentrates on:
</p>

<pre>top-level source and architectural correctness
   +
top-level early executable anchors
   +
named compiler-corridor staged consumability</pre>

<p>
This is already a substantial closure step.
</p>

<p>
It means the repository no longer treats the downstream corridor as future-only strategy. It already exposes:
</p>

<ul>
  <li>source-shape truth,</li>
  <li>semantic truth,</li>
  <li>IR-sensitive truth,</li>
  <li>early executable truth,</li>
  <li>compiler-corridor truth.</li>
</ul>

<p>
However, the current published focus remains conservative:
</p>

<ul>
  <li>the root valid / invalid corpus remains primary,</li>
  <li>the compiler-corridor families extend rather than replace that root corpus,</li>
  <li>broader executable family normalization may still come later,</li>
  <li>future executable structuring should not erase or misdescribe the already-published top-level executable anchors.</li>
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
early executable anchor preservation
   -&gt;
named compiler-corridor family closure
   -&gt;
later executable-family normalization where justified
   -&gt;
later corridor expansion</pre>

<p>
That means future executable growth may later introduce more explicit structuring such as dedicated executable subfamilies.
</p>

<p>
But if that happens, the growth should:
</p>

<ul>
  <li>remain compatible with the already-published top-level executable anchors,</li>
  <li>avoid pretending those anchors never existed,</li>
  <li>avoid claiming a new executable family is already published before it actually exists in the tree,</li>
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
  <li>a named valid / invalid compiler-corridor family for declared downstream compilation routes.</li>
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
