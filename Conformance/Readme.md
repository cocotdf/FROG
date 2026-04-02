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
  <li><a href="#why-this-directory-exists">3. Why This Directory Exists</a></li>
  <li><a href="#definition-of-conformance">4. Definition of Conformance</a></li>
  <li><a href="#non-goals">5. Non-Goals</a></li>
  <li><a href="#relation-with-specification-ownership">6. Relation with Specification Ownership</a></li>
  <li><a href="#critical-boundaries">7. Critical Boundaries</a></li>
  <li><a href="#directory-structure">8. Directory Structure</a></li>
  <li><a href="#published-cases">9. Published Cases</a></li>
  <li><a href="#expected-outcomes">10. Expected Outcomes</a></li>
  <li><a href="#active-v01-conformance-focus">11. Active v0.1 Conformance Focus</a></li>
  <li><a href="#relation-with-examples-ir-and-reference-implementation">12. Relation with Examples, IR, and Reference Implementation</a></li>
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

<pre><code>What must be accepted?
What must be rejected?
What must be preserved?</code></pre>

<p>
This directory does not define the language by itself. It makes already-published language law operationally checkable.
Conformance therefore sits at the boundary between repository truth and observable implementation behavior.
It turns architectural distinctions into public expectations.
</p>

<p>
In v0.1, that public truth surface is not limited to source acceptance or semantic rejection alone.
It also includes preservation obligations across the published execution corridor:
</p>

<pre><code>.frog source
   -&gt;
loadability
   -&gt;
structural validity
   -&gt;
validated meaning
   -&gt;
canonical Execution IR Document
   -&gt;
canonical JSON IR validation where applicable
   -&gt;
later lowering / backend-facing handoff where applicable
   -&gt;
declared compiler-family consumption where applicable</code></pre>

<p>
Conformance therefore already matters to the compiler corridor, even when the downstream compilation route is still being consolidated.
A future industrial compilation chain must remain compatible with the same public accept / reject / preserve truth surface.
</p>

<hr/>

<h2 id="core-purpose">2. Core Purpose</h2>

<p>
The purpose of conformance is to transform specification rules into checkable public expectations.
</p>

<p>
The repository-level model is:
</p>

<pre><code>Specification   = defines the rules
Conformance     = exposes testable cases
Implementation  = must behave accordingly</code></pre>

<p>
A conforming implementation MAY vary internally.
It MUST NOT vary in published accept / reject / preserve outcomes for the same published case while still claiming conformance to the same published repository state.
</p>

<p>
Conformance therefore prevents the following drift:
</p>

<pre><code>parseable file
        -/-&gt; structurally valid canonical source

structurally valid canonical source
        -/-&gt; validated meaning

validated meaning
        -/-&gt; arbitrary execution-facing form

implementation convenience
        -/-&gt; language truth

"it runs"
        -/-&gt; "it is correct"</code></pre>

<p>
Conformance is therefore not a commentary layer.
It is the public truth surface that makes published repository law observable, comparable, and reviewable.
</p>

<hr/>

<h2 id="why-this-directory-exists">3. Why This Directory Exists</h2>

<p>
FROG is specification-first and implementation-independent.
</p>

<p>
That creates a requirement:
</p>

<pre><code>multiple independent implementations
            require
one shared public validation surface</code></pre>

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
  <li>critical distinctions remain visible across loadability, structural validation, semantic validation, IR derivation, IR construction, canonical JSON validation, lowering, backend-facing handoff, and declared compiler-corridor consumption where applicable.</li>
</ul>

<p>
Conformance is therefore not commentary.
It is the public truth surface that turns specification architecture into comparable observable behavior.
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
  <li>correct preservation of distinctions across derivation into the canonical Execution IR Document,</li>
  <li>correct canonical-IR construction and canonical JSON compatibility where the case reaches that stage,</li>
  <li>correct preservation of required boundaries across later lowering and backend-facing handoff where applicable,</li>
  <li>correct staged acceptance or rejection across declared compiler-corridor stages where applicable.</li>
</ul>

<p>
Conformance therefore requires both:
</p>

<ul>
  <li>accept / reject correctness, and</li>
  <li>preservation correctness.</li>
</ul>

<p>
Formalized:
</p>

<pre><code>Conformance =
  correct interpretation
  +
  correct preservation
  +
  correct rejection</code></pre>

<p>
A public conformance surface SHOULD make explicit whether a case is:
</p>

<ul>
  <li>not loadable as source,</li>
  <li>loadable but structurally invalid as canonical source,</li>
  <li>structurally valid but semantically rejected,</li>
  <li>semantically accepted but preservation-invalid at the IR boundary,</li>
  <li>semantically accepted but canonical-IR-schema-invalid,</li>
  <li>semantically accepted and IR-valid but rejected at a later lowering, backend-contract, or declared backend-family consumer boundary,</li>
  <li>accepted with preservation requirements.</li>
</ul>

<p>
Where useful, a case MAY also make explicit whether it is:
</p>

<ul>
  <li>schema-checkable at the source-shape level,</li>
  <li>structurally invalid for reasons that remain source-owned even when they exceed a minimal declarative schema artifact,</li>
  <li>semantically invalid even though canonical source shape has already been accepted,</li>
  <li>IR-schema-invalid even though semantic meaning was previously established,</li>
  <li>lowering-sensitive, backend-contract-sensitive, or declared-backend-consumer-sensitive after canonical IR has already been established.</li>
</ul>

<p>
This distinction matters because machine-checkable schema is part of the validation corridor.
It is not a replacement for semantic validation.
Likewise, canonical JSON IR validity is not a replacement for semantic validity or IR architectural validity.
Later backend-oriented success is not a replacement for upstream correctness either.
</p>

<hr/>

<h2 id="non-goals">5. Non-Goals</h2>

<p>
This directory does not define:
</p>

<ul>
  <li>a certification program,</li>
  <li>a universal implementation compatibility matrix,</li>
  <li>a full execution-performance suite,</li>
  <li>a debugger validation framework in full,</li>
  <li>a deployment validation system in full,</li>
  <li>a private runtime architecture,</li>
  <li>a compiler-family-specific optimization strategy.</li>
</ul>

<p>
It also does not introduce new language rules.
</p>

<p>
Rule:
</p>

<pre><code>Specification defines
Conformance exposes
Implementation follows</code></pre>

<p>
Conformance must never become the place where missing language law is invented retroactively.
When a case reveals ambiguity, the owning specification document must be clarified.
</p>

<hr/>

<h2 id="relation-with-specification-ownership">6. Relation with Specification Ownership</h2>

<p>
Conformance does not own language truth.
</p>

<p>
Ownership remains:
</p>

<ul>
  <li><code>Expression/</code> — source structure, canonical source shape, structural validity, and source-schema posture,</li>
  <li><code>Language/</code> — semantic truth and validated meaning,</li>
  <li><code>Libraries/</code> — intrinsic primitive vocabularies and primitive-local behavioral law,</li>
  <li><code>Profiles/</code> — optional standardized capability families,</li>
  <li><code>IR/</code> — canonical execution-facing representation, derivation, identity, construction, schema posture, lowering, and backend-facing boundaries,</li>
  <li><code>IDE/</code> — tooling behavior and authoring-facing concerns.</li>
</ul>

<p>
Conformance cases must always map back to these owners.
</p>

<pre><code>specification
      -&gt;
conformance
      -&gt;
implementation

Never the reverse.</code></pre>

<p>
In particular:
</p>

<ul>
  <li>source-shape and schema-owned rejection cases map back to <code>Expression/</code>,</li>
  <li>semantic rejection cases map back to <code>Language/</code>, <code>Libraries/</code>, or <code>Profiles/</code> as appropriate,</li>
  <li>preservation cases across derivation, identity, attribution, correspondence, construction, and canonical JSON IR validation map back to <code>IR/</code>,</li>
  <li>compiler-corridor-sensitive cases must still map back first to <code>IR/</code> and to any declared profile surface before they map to a downstream consumer family.</li>
</ul>

<p>
A case file is therefore not a second specification.
It is a public executable reading of already-published ownership.
</p>

<hr/>

<h2 id="critical-boundaries">7. Critical Boundaries</h2>

<p>
The first critical conformance boundary is the staged progression:
</p>

<pre><code>.frog source
      |
      v
loadable source
      |
      v
structurally valid canonical source
      |
      v
validated program meaning</code></pre>

<p>
Conformance must make these boundaries observable.
</p>

<p>
This includes verifying:
</p>

<ul>
  <li>what fails before the source is even loadable,</li>
  <li>what fails at source-shape or schema-owned structural validation,</li>
  <li>what fails after canonical source shape is accepted but before semantic meaning is established,</li>
  <li>what establishes semantic meaning,</li>
  <li>what distinctions must survive validation,</li>
  <li>what distinctions must survive derivation into the canonical Execution IR Document,</li>
  <li>what identity, attribution, and correspondence carriers must remain explicit at the canonical JSON IR boundary,</li>
  <li>what distinctions must remain explicit before later lowering and backend-facing handoff,</li>
  <li>what later-stage rejection boundaries remain explicit once a compiler corridor is declared.</li>
</ul>

<p>
The second critical boundary is:
</p>

<pre><code>validated program meaning
      |
      v
canonical Execution IR Document</code></pre>

<p>
The third critical downstream boundary is:
</p>

<pre><code>canonical Execution IR Document
      |
      v
lowering / backend-facing handoff</code></pre>

<p>
The fourth critical downstream boundary, where declared by a case, is:
</p>

<pre><code>backend-facing handoff
      |
      v
declared backend-family consumption</code></pre>

<p>
Critical invariants therefore include:
</p>

<pre><code>front panel                              != public interface
widget_value                             != widget_reference
widget reference                         != UI-object operation
property read                            != property write
method invocation                        != property write
property read                            != method invocation
ui_in                                    != ui_out
layout                                   != execution
adjacency                                != dependency
visual order                             != execution order
feedback shape                           != state
default inference                        != explicit initialization
structural validity                      != semantic acceptance
schema acceptance                        != semantic acceptance
validated meaning                        != canonical Execution IR
canonical Execution IR                   != private runtime realization
source_map presence                      != semantic validity by itself
correspondence presence                  != semantic validity by itself
intentional non-primary                  != accidental identity loss
primary source attribution               != public-interface participation
primary source attribution               != ordinary connectivity
primary source attribution               != structure-boundary participation
primary source attribution               != explicit state participation
multi-contributor attribution            != public-interface participation
multi-contributor attribution            != ordinary connectivity
ordinary connectivity                    != public-interface participation
ordinary connectivity                    != structure-boundary participation
explicit UI sequencing                   != ordinary connectivity
explicit UI sequencing                   != structure-boundary participation
explicit UI sequencing                   != explicit state participation
explicit UI sequencing                   != public-interface participation
backend contract                         != private runtime structure
backend family                           != target profile
deployment mode                          != runtime-private realization
compiler-family route                    != FROG semantic truth</code></pre>

<p>
These invariants are enforced through explicit valid / invalid and preserve / reject expectations.
</p>

<hr/>

<h2 id="directory-structure">8. Directory Structure</h2>

<pre><code>Conformance/
├── Readme.md
├── valid/
│   └── compiler/
└── invalid/
    └── compiler/</code></pre>

<p>
The root valid / invalid directories remain the primary home of the published conformance corpus.
The nested <code>compiler/</code> families extend that corpus along a later compiler-corridor reading without replacing the root valid / invalid structure.
</p>

<p>
Each case should define, as applicable:
</p>

<ul>
  <li>expected loadability,</li>
  <li>expected structural validity,</li>
  <li>expected semantic acceptance,</li>
  <li>expected IR eligibility,</li>
  <li>expected canonical JSON IR validity where relevant,</li>
  <li>tested boundaries,</li>
  <li>preservation requirements,</li>
  <li>rejection reason if invalid,</li>
  <li>downstream sensitivity if the case materially constrains lowering, backend-facing handoff, or declared backend-family consumption.</li>
</ul>

<p>
In practice, the directory serves three public roles:
</p>

<ul>
  <li>accept — what must validate and remain correct,</li>
  <li>reject — what must fail explicitly,</li>
  <li>preserve — what distinctions must remain explicit across later stages.</li>
</ul>

<p>
For v0.1, published cases SHOULD remain small, sharply owned, and explicit about the stage at which acceptance or rejection occurs.
</p>

<p>
Where useful, cases SHOULD also be written so that the reader can tell whether the failure belongs to:
</p>

<ul>
  <li>non-loadable source,</li>
  <li>schema-owned or source-shape-owned structural invalidity,</li>
  <li>semantic invalidity after structural acceptance,</li>
  <li>IR preservation failure after semantic acceptance,</li>
  <li>canonical JSON IR schema failure after otherwise valid IR construction intent,</li>
  <li>lowering failure after canonical IR acceptance,</li>
  <li>backend-contract failure after lowering eligibility,</li>
  <li>declared backend-family consumer rejection after contract emission.</li>
</ul>

<p>
Recommended reading corridor:
</p>

<pre><code>loadability
   -&gt;
source-shape / structural validity
   -&gt;
semantic acceptance
   -&gt;
IR derivation / identity / construction preservation
   -&gt;
canonical JSON IR validation where relevant
   -&gt;
later lowering / backend-facing handoff where relevant
   -&gt;
declared backend-family consumption where relevant</code></pre>

<hr/>

<h2 id="published-cases">9. Published Cases</h2>

<p>
The current published and newly-opened conformance set combines:
</p>

<ul>
  <li>an explicit top-level source-shape valid / invalid block,</li>
  <li>early positive executable anchor cases,</li>
  <li>a mirrored valid / invalid architectural boundary progression,</li>
  <li>additional standalone invalid architectural rejection cases,</li>
  <li>an extended IR recoverability and correspondence-disentanglement progression,</li>
  <li>a newly-opened valid / invalid compiler-corridor family for downstream compilation-stage reading.</li>
</ul>

<h3>9.1 Published top-level source-shape block</h3>

<p>
The published top-level source-shape block currently includes:
</p>

<pre><code>valid/
01_minimal_canonical_frog
02_optional_sections_absent_is_still_valid
03_optional_front_panel_absent_is_still_valid
04_optional_connector_absent_is_still_valid
05_optional_icon_absent_is_still_valid
06_optional_ide_absent_is_still_valid
07_optional_cache_absent_is_still_valid
08_optional_connector_present_and_consistent
09_optional_front_panel_present_and_structurally_valid
10_distinct_source_identifiers_are_valid

invalid/
01_missing_required_section
02_wrong_top_level_section_type
03_connector_defines_logical_ports
04_malformed_front_panel_structure
05_duplicate_source_identifier
06_invalid_top_level_root_shape
07_invalid_section_placement
08_connector_references_unknown_interface_port</code></pre>

<p>
This block matters because it makes the first public structural corridor explicit:
</p>

<pre><code>loadable JSON
   -&gt;
canonical top-level source shape
   -&gt;
later semantic validation</code></pre>

<p>
These cases should be read primarily as <code>Expression/</code>-owned conformance around canonical source shape and structural validity.
They are upstream of IR derivation and therefore upstream of any serious compilation route.
</p>

<h3>9.2 Early valid executable anchor cases</h3>

<pre><code>01_pure_addition
02_ui_value_roundtrip
03_ui_property_write
04_stateful_feedback_delay</code></pre>

<p>
These anchor cases show that conformance is not only about abstract rejection.
It also covers minimal positive executable slices that the published architecture is expected to support.
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
Together they already constrain the future compilation corridor by proving that the repository truth surface is not limited to syntax or abstract semantics alone.
</p>

<h3>9.3 Mirrored architectural boundary progression</h3>

<p>
The published mirrored progression begins with the foundational distinction families:
</p>

<pre><code>05 / 06   public interface participation != widget participation
07 / 08   widget_reference != widget_value
09 / 10   front-panel presence != execution meaning
11 / 12   public interface declaration does not require widget existence
13 / 14   explicit diagram participation != layout or adjacency
15 / 16   explicit connectivity != inferred evaluation order
17 / 18   explicit structure boundary != layout grouping or apparent nesting
19 / 20   explicit structure terminals != inferred region crossing by layout
21 / 22   explicit structure-owned state != inferred persistent value by feedback shape
23 / 24   explicit state initialization != inferred default initial value
25 / 26   explicit state read timing != inferred scheduler order
27 / 28   explicit state write visibility != inferred runtime flush order
29 / 30   explicit state snapshot boundary != inferred runtime observation point
31 / 32   explicit state version boundary != inferred runtime update epoch
33 / 34   explicit state merge boundary != inferred runtime reconciliation pass
35 / 36   explicit state commit boundary != inferred stabilization phase
37 / 38   source attribution must remain recoverable
39 / 40   canonical Execution IR != private runtime realization
41 / 42   backend contract != private runtime structure
43 / 44   target profile != backend family
45 / 46   deployment mode != runtime-private scheduling structure
47 / 48   open execution IR observation surface != private runtime debug state</code></pre>

<p>
This progression matters because it forces a public mirrored reading:
</p>

<pre><code>valid case
   -&gt; explicit accepted distinction

invalid case
   -&gt; explicit rejected collapse of that distinction</code></pre>

<p>
These cases are not decorative.
They prevent execution-side categories from collapsing into convenience-driven implementation shortcuts.
That matters directly for IR correctness, later lowering discipline, and any credible LLVM-oriented downstream path.
</p>

<h3>9.4 Additional standalone invalid architectural rejections</h3>

<p>
The published set also includes standalone invalid cases that reinforce architectural boundaries outside the simplest mirrored progression.
These cases should be read as focused rejection anchors for category collapse, illicit inference, missing explicit carriers, or ownership confusion.
</p>

<h3>9.5 Extended IR recoverability and correspondence-disentanglement progression</h3>

<p>
The published set also extends into recoverability and correspondence discipline at the IR boundary.
This matters because canonical IR is not just an execution-facing graph.
It is an open, attributable, recoverable representation with explicit category discipline.
</p>

<p>
That progression should be read as enforcing at least the following public expectations:
</p>

<ul>
  <li>source attribution remains recoverable after semantic acceptance,</li>
  <li>primary attribution does not collapse into ordinary connectivity or boundary participation,</li>
  <li>multi-contributor correspondence does not erase category ownership,</li>
  <li>canonical JSON shape alone is not enough when architectural distinction has already been lost,</li>
  <li>recoverability obligations remain in force before later lowering and backend-facing handoff.</li>
</ul>

<p>
This is one of the most important current published areas for the future compiler corridor, because a serious backend cannot be allowed to consume an IR that has already lost attribution, ownership, or distinction boundaries.
</p>

<h3>9.6 Compiler-corridor families</h3>

<p>
The conformance tree now also opens two nested compiler-corridor families:
</p>

<pre><code>valid/compiler/
invalid/compiler/</code></pre>

<p>
These families extend the public truth surface beyond ordinary language validity and IR correctness by making later corridor stages readable and testable:
</p>

<pre><code>semantic acceptance
   -&gt;
IR derivation
   -&gt;
canonical JSON IR validity where applicable
   -&gt;
lowering eligibility
   -&gt;
backend-contract eligibility
   -&gt;
declared backend-family consumability</code></pre>

<p>
The positive side exists to publish cases that are not only language-valid, but also lowerable and handoff-ready for a declared compilation corridor.
The negative side exists to publish staged rejections such as:
</p>

<ul>
  <li>language-valid but profile-rejected,</li>
  <li>IR-derivable but not lowerable,</li>
  <li>lowerable but not backend-contract-emittable,</li>
  <li>contract-emittable but rejected by the declared backend-family consumer.</li>
</ul>

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
  <li>Expected backend-family consumption: <code>consumable</code> | <code>rejected</code> | <code>not applicable</code></li>
  <li>Expected preservation: required distinctions remain explicit</li>
  <li>Expected rejection: explicit failure reason</li>
</ul>

<p>
Examples:
</p>

<pre><code>Expected loadability: loadable
Expected structural validity: valid
Expected meaning: established
Expected IR result: derivable
Expected preservation:
  explicit state remains explicit

Expected loadability: loadable
Expected structural validity: invalid
Expected meaning: not established
Expected rejection:
  missing required source section

Expected loadability: loadable
Expected structural validity: valid
Expected meaning: not established
Expected rejection:
  illegal feedback without explicit memory

Expected loadability: loadable
Expected structural validity: valid
Expected meaning: established
Expected IR result: derivable
Expected IR schema result: not schema-valid
Expected rejection:
  canonical IR omitted required correspondence carrier

Expected loadability: loadable
Expected structural validity: valid
Expected meaning: established
Expected IR result: derivable
Expected lowering result: rejected
Expected rejection:
  faithful lowering unavailable for declared profile

Expected loadability: loadable
Expected structural validity: valid
Expected meaning: established
Expected IR result: derivable
Expected lowering result: lowerable
Expected backend-contract result: emittable
Expected backend-family consumption: rejected
Expected rejection:
  declared backend-family consumer cannot honor required capabilities</code></pre>

<p>
A useful discipline rule is:
</p>

<pre><code>loadable
does not imply
structurally valid

structurally valid
does not imply
semantically accepted

accepted meaning
does not imply
arbitrary IR shape

schema-valid IR
does not imply
semantic correctness by itself

lowerable
does not imply
backend-contract-emittable

backend-contract-emittable
does not imply
backend-family consumable</code></pre>

<hr/>

<h2 id="active-v01-conformance-focus">11. Active v0.1 Conformance Focus</h2>

<p>
The active v0.1 conformance focus is now split across two tightly related fronts:
</p>

<ul>
  <li>maintaining coherence of the already-published source / semantic / IR truth surface,</li>
  <li>opening the first explicit compiler-corridor reading without collapsing FROG into a backend-private model.</li>
</ul>

<p>
Near-term focus therefore remains:
</p>

<ul>
  <li>top-level source-shape validity and invalidity,</li>
  <li>semantic rejection clarity,</li>
  <li>IR preservation, attribution, and correspondence discipline,</li>
  <li>canonical JSON IR validity versus deeper architectural validity,</li>
  <li>first compiler-corridor positive and negative family structure.</li>
</ul>

<p>
For v0.1, compiler-corridor work should remain conservative and preferentially target the first bounded compilation profile:
</p>

<pre><code>native_cpu_llvm</code></pre>

<p>
That means the active compiler-corridor focus is not “all compilation”.
It is:
</p>

<pre><code>close one serious conservative downstream route first</code></pre>

<p>
The preferred growth order is therefore:
</p>

<pre><code>source-shape closure
   -&gt;
semantic rejection closure
   -&gt;
IR preservation closure
   -&gt;
canonical JSON IR validation closure
   -&gt;
compiler-corridor valid / invalid family closure
   -&gt;
later corridor expansion</code></pre>

<hr/>

<h2 id="relation-with-examples-ir-and-reference-implementation">12. Relation with Examples, IR, and Reference Implementation</h2>

<p>
This directory must be read together with nearby repository areas, but without ownership collapse.
</p>

<ul>
  <li><code>Examples/</code> provides illustrative named slices. Examples do not become hidden language law.</li>
  <li><code>IR/</code> owns canonical execution-facing representation, derivation, identity, construction, schema posture, lowering, and backend-facing boundaries.</li>
  <li><code>Implementations/Reference/</code> is a non-normative executable workspace. It does not become hidden semantic truth.</li>
</ul>

<p>
The practical relation is:
</p>

<pre><code>Examples
   -&gt; illustrate

Conformance
   -&gt; expose public expectations

IR
   -&gt; define canonical execution-facing law

Reference implementation
   -&gt; consume the published layers without owning them</code></pre>

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
Where a case materially constrains a declared compilation profile or backend-family route, the reader should also cross-check:
</p>

<ul>
  <li><code>Profiles/Readme.md</code>,</li>
  <li><code>Profiles/Native CPU LLVM.md</code> where relevant.</li>
</ul>

<p>
Where a case materially constrains executable reference slices, the reader should also cross-check <code>Implementations/Reference/Readme.md</code> and the reference pipeline staging.
</p>

<hr/>

<h2 id="future-growth">13. Future Growth</h2>

<p>
Future growth should remain disciplined.
This directory SHOULD expand by closing coherent corridors rather than by accumulating disconnected examples.
</p>

<p>
Near-term growth should prioritize:
</p>

<ul>
  <li>continued alignment with the real published case set,</li>
  <li>stronger read-across to IR identity, derivation, and recoverability law,</li>
  <li>explicit distinction between canonical IR validity and later backend-facing success,</li>
  <li>mirrored compiler-corridor-sensitive cases as lowering and backend contract continue to consolidate.</li>
</ul>

<p>
A useful growth order is:
</p>

<pre><code>source-shape closure
   -&gt;
semantic rejection closure
   -&gt;
IR preservation closure
   -&gt;
canonical JSON IR validation closure
   -&gt;
compiler-corridor positive closure
   -&gt;
compiler-corridor mirrored rejection closure
   -&gt;
later profile-specific corridor growth</code></pre>

<p>
That order preserves the architecture:
</p>

<pre><code>upstream truth first
downstream specialization second</code></pre>

<hr/>

<h2 id="summary">14. Summary</h2>

<p>
<code>Conformance/</code> is the public accept / reject / preserve truth surface of the published FROG repository.
</p>

<p>
It does not replace specification ownership.
It exposes it.
</p>

<p>
Its current published and newly-opened corpus covers:
</p>

<ul>
  <li>top-level canonical source-shape acceptance and rejection,</li>
  <li>positive executable anchor slices,</li>
  <li>architectural distinction preservation,</li>
  <li>IR recoverability and correspondence discipline,</li>
  <li>downstream-sensitive boundaries relevant to lowering and backend-facing handoff,</li>
  <li>first valid / invalid compiler-corridor family structure for declared downstream compilation routes.</li>
</ul>

<p>
It should therefore be read as a public truth surface for the full published corridor:
</p>

<pre><code>.frog source
   -&gt;
loadability
   -&gt;
structural validity
   -&gt;
validated meaning
   -&gt;
canonical Execution IR Document
   -&gt;
canonical JSON IR validation where applicable
   -&gt;
later lowering / backend-facing handoff where applicable
   -&gt;
declared backend-family consumption where applicable</code></pre>

<p>
As the repository moves toward a more industrial compiler corridor, this directory remains one of the key public anchors.
A future LLVM-oriented route may be downstream.
It must still remain faithful to the same published conformance truth.
</p>
