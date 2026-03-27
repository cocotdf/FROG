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
  <li><a href="#critical-boundaries">7. Critical Boundaries</a></li>
  <li><a href="#directory-structure">8. Directory Structure</a></li>
  <li><a href="#published-cases">9. Published Cases</a></li>
  <li><a href="#expected-outcomes">10. Expected Outcomes</a></li>
  <li><a href="#v01-focus">11. Active v0.1 Conformance Focus</a></li>
  <li><a href="#relation-with-examples-ir-and-reference-implementation">12. Relation with Examples, IR, and Reference Implementation</a></li>
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
It makes the published language testable and publicly checkable.
</p>

<p>
Conformance therefore belongs at the boundary between published repository law and observable implementation behavior.
It turns architectural distinctions into explicit public expectations.
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
A conforming implementation MAY vary internally.
It MUST NOT vary in published accept / reject / preserve outcomes for the same published case while still claiming conformance to the same published repository state.
</p>

<p>
Conformance therefore prevents the following drift:
</p>

<pre><code>parseable file
        -/-> structurally valid canonical source

structurally valid canonical source
        -/-> validated meaning

validated meaning
        -/-> arbitrary IR

implementation convenience
        -/-> language truth

"it runs"
        -/-> "it is correct"
</code></pre>

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
one shared public validation surface
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
  <li>invalid constructs are rejected instead of silently repaired,</li>
  <li>critical distinctions remain visible across loadability, structural validation, semantic validation, IR derivation, and later specialization.</li>
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
  <li>correct preservation of distinctions across derivation into open Execution IR,</li>
  <li>correct preservation of required boundaries across later lowering and backend-facing handoff where applicable.</li>
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

<p>
A public conformance surface SHOULD make explicit whether a case is:
</p>

<ul>
  <li>not loadable as source,</li>
  <li>loadable but structurally invalid as canonical source,</li>
  <li>structurally valid but semantically rejected,</li>
  <li>accepted with preservation requirements.</li>
</ul>

<p>
Where useful, a case MAY also make explicit whether it is:
</p>

<ul>
  <li>schema-checkable at the source-shape level,</li>
  <li>structurally valid only after rules that exceed a purely declarative schema artifact,</li>
  <li>semantically invalid even though canonical source shape has already been accepted.</li>
</ul>

<p>
This distinction matters because machine-checkable source schema is part of the structural validation corridor.
It is not a replacement for semantic validation.
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
  <li>a deployment validation system in full.</li>
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
  <li><code>Libraries/</code> — intrinsic primitive vocabularies,</li>
  <li><code>Profiles/</code> — optional standardized capability families,</li>
  <li><code>IR/</code> — execution-facing representation, derivation, construction, lowering, and backend-facing boundaries,</li>
  <li><code>IDE/</code> — tooling behavior and authoring-facing concerns.</li>
</ul>

<p>
Conformance cases must always map back to these owners.
</p>

<pre><code>specification
      ->
conformance
      ->
implementation
</code></pre>

<p>
Never the reverse.
</p>

<p>
In particular:
</p>

<ul>
  <li>source-shape and schema-owned rejection cases map back to <code>Expression/</code>,</li>
  <li>semantic rejection cases map back to <code>Language/</code>, <code>Libraries/</code>, or <code>Profiles/</code> as appropriate,</li>
  <li>preservation cases across derivation and lowering map back to <code>IR/</code>.</li>
</ul>

<hr/>

<h2 id="critical-boundaries">7. Critical Boundaries</h2>

<p>
The first critical conformance boundary is not merely raw source to meaning.
It is the staged progression:
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
validated program meaning
</code></pre>

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
  <li>what distinctions must survive derivation into open Execution IR,</li>
  <li>what distinctions must remain explicit before later lowering and backend-facing handoff.</li>
</ul>

<p>
The second critical boundary is:
</p>

<pre><code>validated program meaning
      |
      v
open Execution IR
</code></pre>

<p>
The third critical downstream boundary is:
</p>

<pre><code>open Execution IR
      |
      v
lowering / backend-facing handoff
</code></pre>

<p>
Critical invariants therefore include:
</p>

<pre><code>front panel                    != public interface
widget_value                   != widget_reference
layout                         != execution
adjacency                      != dependency
visual order                   != execution order
feedback shape                 != state
default inference              != explicit initialization
structural validity            != semantic acceptance
schema acceptance              != semantic acceptance
validated meaning              != open Execution IR
open Execution IR              != private runtime realization
backend family                 != target profile
deployment mode                != runtime-private realization
</code></pre>

<p>
These invariants are enforced through explicit valid / invalid and preserve / reject expectations.
</p>

<hr/>

<h2 id="directory-structure">8. Directory Structure</h2>

<pre><code>Conformance/
├── Readme.md
├── valid/
└── invalid/
</code></pre>

<p>
Each case should define, as applicable:
</p>

<ul>
  <li>expected loadability,</li>
  <li>expected structural validity,</li>
  <li>expected semantic acceptance,</li>
  <li>tested boundaries,</li>
  <li>preservation requirements,</li>
  <li>rejection reason if invalid.</li>
</ul>

<p>
In practice, the directory serves three public roles:
</p>

<ul>
  <li><strong>accept</strong> — what must validate and remain correct,</li>
  <li><strong>reject</strong> — what must fail explicitly,</li>
  <li><strong>preserve</strong> — what distinctions must remain explicit across later stages.</li>
</ul>

<p>
For v0.1, published cases SHOULD remain small, sharply-owned, and explicit about the stage at which acceptance or rejection occurs.
</p>

<p>
Where useful, cases SHOULD also be written so that the reader can tell whether the failure belongs to:
</p>

<ul>
  <li>non-loadable source,</li>
  <li>schema-owned or source-shape-owned structural invalidity,</li>
  <li>semantic invalidity after structural acceptance,</li>
  <li>preservation failure in later stages.</li>
</ul>

<hr/>

<h2 id="published-cases">9. Published Cases</h2>

<p>
The current published set combines:
</p>

<ul>
  <li>early positive executable anchor cases,</li>
  <li>a mirrored valid / invalid boundary progression,</li>
  <li>additional invalid architectural rejection cases.</li>
</ul>

<h3>9.1 Early valid executable anchor cases</h3>

<pre><code>01_pure_addition
02_ui_value_roundtrip
03_ui_property_write
04_stateful_feedback_delay
</code></pre>

<p>
These anchor cases show that conformance is not only about abstract rejection.
It also covers minimal positive executable slices that the published architecture is expected to support.
</p>

<h3>9.2 Mirrored boundary progression</h3>

<p>
The published mirrored progression currently includes:
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
</code></pre>

<p>
This pairing strategy is intentional:
</p>

<pre><code>acceptance alone is insufficient
rejection alone is insufficient
both define truth
</code></pre>

<h3>9.3 Additional invalid architectural rejection cases</h3>

<p>
The published invalid set also contains additional non-mirrored rejection cases such as:
</p>

<pre><code>illegal_feedback_without_explicit_memory
interface_widget_role_confusion
ui_reference_without_ui_primitive
</code></pre>

<p>
These exist because some architectural failures are important enough to publish even when they are not yet part of one large mirrored numbering progression.
</p>

<h3>9.4 Reading rule for published cases</h3>

<p>
A published case defines public truth for the published repository state.
A session draft that is not yet published does not.
</p>

<p>
A case SHOULD also be read with stage discipline:
</p>

<pre><code>loadability
   ->
source-shape / schema-owned structural validity
   ->
semantic acceptance
   ->
preservation expectations
</code></pre>

<p>
A case SHOULD NOT blur:
</p>

<ul>
  <li>schema-owned failure into semantic rejection,</li>
  <li>semantic rejection into source malformedness,</li>
  <li>implementation subset limitations into specification invalidity.</li>
</ul>

<hr/>

<h2 id="expected-outcomes">10. Expected Outcomes</h2>

<p>
Each case expresses structured expectations such as:
</p>

<ul>
  <li><strong>Expected loadability:</strong> loadable | not loadable</li>
  <li><strong>Expected structural validity:</strong> valid | invalid</li>
  <li><strong>Expected meaning:</strong> established | not established</li>
  <li><strong>Expected preservation:</strong> required distinctions remain explicit</li>
  <li><strong>Expected rejection:</strong> explicit failure reason</li>
</ul>

<p>
Examples:
</p>

<pre><code>Expected loadability: loadable
Expected structural validity: valid
Expected meaning: established
Expected preservation:
  explicit state remains explicit

Expected loadability: loadable
Expected structural validity: invalid
Expected meaning: not established
Expected rejection:
  missing required source section

Expected loadability: loadable
Expected structural validity: invalid
Expected meaning: not established
Expected rejection:
  top-level source shape violates canonical schema posture

Expected loadability: loadable
Expected structural validity: valid
Expected meaning: not established
Expected rejection:
  illegal feedback without explicit memory
</code></pre>

<p>
For later-stage-sensitive cases, expectations may also include:
</p>

<ul>
  <li>required IR-side recoverability,</li>
  <li>required lowering-side distinction preservation,</li>
  <li>required backend-facing explicitness where applicable.</li>
</ul>

<hr/>

<h2 id="v01-focus">11. Active v0.1 Conformance Focus</h2>

<p>
v0.1 focuses on architectural correctness, not broad feature coverage.
</p>

<p>
Priorities are:
</p>

<pre><code>1. source loadability and structural validity
2. semantic validity
3. preservation of distinctions
4. explicit rejection of violations
5. conservative correctness across the IR corridor
</code></pre>

<p>
The active public truth surface therefore emphasizes:
</p>

<ul>
  <li>source structure versus semantic acceptance,</li>
  <li>schema-owned source shape versus later semantic legality,</li>
  <li>interface versus widget participation,</li>
  <li>value versus reference participation,</li>
  <li>state versus inferred feedback,</li>
  <li>execution versus layout,</li>
  <li>connectivity versus order,</li>
  <li>explicit state-family boundaries,</li>
  <li>the fact that validated meaning, Execution IR, lowering, and backend-facing handoff are distinct stages rather than one blurred implementation pipeline.</li>
</ul>

<p>
Rule:
</p>

<pre><code>no implicit meaning
no silent repair
no hidden interpretation
no silent stage collapse
</code></pre>

<hr/>

<h2 id="relation-with-examples-ir-and-reference-implementation">12. Relation with Examples, IR, and Reference Implementation</h2>

<pre><code>Examples/                   -> illustrate and anchor named programs
Conformance/                -> define public expectations
Implementations/Reference/  -> try to execute correctly
</code></pre>

<p>
These roles must remain strictly separated.
</p>

<p>
Likewise, the relation with the specification corridor is:
</p>

<pre><code>Expression/
   defines canonical source structure, source-schema posture, and structural validity

Language/
   defines semantic truth

IR/
   defines derivation, identity, construction, lowering, and backend-facing boundaries

Conformance/
   tests whether those published boundaries are being respected
</code></pre>

<p>
An implementation passing a case does not redefine the language.
It only demonstrates alignment with the published conformance surface.
</p>

<p>
A machine-checkable schema artifact may assist source-structure validation.
It does not replace the ownership boundary above.
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
-> clear boundary
-> clear expectation
-> clear ownership
</code></pre>

<p>
Near-term future expansion areas include:
</p>

<ul>
  <li>source-shape and schema rejection cases,</li>
  <li>type and value legality,</li>
  <li>state semantics and timing,</li>
  <li>structure legality,</li>
  <li>validated meaning to open-IR preservation,</li>
  <li>profile-dependent behavior,</li>
  <li>backend-family and target-profile rejection cases where applicable.</li>
</ul>

<p>
Growth should continue to prefer:
</p>

<ul>
  <li>small sharply-owned boundary cases,</li>
  <li>mirrored valid / invalid pairs where they clarify truth,</li>
  <li>additional standalone invalid cases where architecture requires them,</li>
  <li>explicit published expectations rather than implementation folklore.</li>
</ul>

<p>
As source-schema closure grows, conformance SHOULD increasingly distinguish:
</p>

<ul>
  <li>malformed source,</li>
  <li>schema-level structural failure,</li>
  <li>structural failure that exceeds a minimal declarative schema artifact but still belongs to <code>Expression/</code>,</li>
  <li>semantic rejection after structural acceptance.</li>
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

<p>
In v0.1, conformance is intentionally conservative and architecture-first.
It exists to keep the most important public boundaries explicit:
</p>

<pre><code>.frog source
   ->
loadable source
   ->
source-shape / schema-owned structural validity
   ->
validated meaning
   ->
open Execution IR
   ->
lowering / backend-facing handoff
   ->
private realization

Conformance checks:
accept
reject
preserve
</code></pre>
