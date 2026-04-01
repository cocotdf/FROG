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
<p>This directory defines the public conformance surface of the published FROG repository.</p>

<p>It publishes explicit cases that make the specification testable, reviewable, and comparable across independent implementations.</p>

<p>It answers three fundamental questions:</p>

<pre><code>What must be accepted?
What must be rejected?
What must be preserved?
</code></pre>

<p>This directory does not define the language by itself. It makes already-published language law operationally checkable.</p>

<p>Conformance therefore sits at the boundary between repository truth and observable implementation behavior. It turns architectural distinctions into public expectations.</p>

<p>In v0.1, that public truth surface is not limited to source acceptance or semantic rejection alone. It also includes preservation obligations across the published execution corridor:</p>

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
</code></pre>

<hr/>

<h2 id="core-purpose">2. Core Purpose</h2>
<p>The purpose of conformance is to transform specification rules into checkable public expectations.</p>

<p>The repository-level model is:</p>

<pre><code>Specification   = defines the rules
Conformance     = exposes testable cases
Implementation  = must behave accordingly
</code></pre>

<p>A conforming implementation MAY vary internally. It MUST NOT vary in published accept / reject / preserve outcomes for the same published case while still claiming conformance to the same published repository state.</p>

<p>Conformance therefore prevents the following drift:</p>

<pre><code>parseable file
        -/-> structurally valid canonical source

structurally valid canonical source
        -/-> validated meaning

validated meaning
        -/-> arbitrary execution-facing form

implementation convenience
        -/-> language truth

"it runs"
        -/-> "it is correct"
</code></pre>

<p>Conformance is therefore not a commentary layer. It is the public truth surface that makes published repository law observable, comparable, and reviewable.</p>

<hr/>

<h2 id="why-this-directory-exists">3. Why This Directory Exists</h2>
<p>FROG is specification-first and implementation-independent.</p>

<p>That creates a requirement:</p>

<pre><code>multiple independent implementations
            require
one shared public validation surface
</code></pre>

<p>This directory provides that surface.</p>

<p>It ensures that:</p>

<ul>
  <li>implementations do not silently diverge,</li>
  <li>semantic meaning is not reinterpreted implicitly,</li>
  <li>invalid constructs are rejected instead of silently repaired,</li>
  <li>critical distinctions remain visible across loadability, structural validation, semantic validation, IR derivation, IR construction, canonical JSON validation, and later specialization.</li>
</ul>

<p>Conformance is therefore not commentary. It is the public truth surface that turns specification architecture into comparable observable behavior.</p>

<hr/>

<h2 id="definition-of-conformance">4. Definition of Conformance</h2>
<p>Conformance is alignment with the published specification across the relevant architectural stages.</p>

<p>It includes:</p>

<ul>
  <li>correct rejection of malformed or non-loadable source where applicable,</li>
  <li>correct source-structure validation,</li>
  <li>correct semantic validation,</li>
  <li>correct rejection where validated meaning does not exist,</li>
  <li>correct preservation of distinctions across derivation into the canonical Execution IR Document,</li>
  <li>correct canonical-IR construction and canonical JSON compatibility where the case reaches that stage,</li>
  <li>correct preservation of required boundaries across later lowering and backend-facing handoff where applicable.</li>
</ul>

<p>Conformance therefore requires both:</p>

<ul>
  <li>accept / reject correctness, and</li>
  <li>preservation correctness.</li>
</ul>

<p>Formalized:</p>

<pre><code>Conformance =
  correct interpretation
  +
  correct preservation
  +
  correct rejection
</code></pre>

<p>A public conformance surface SHOULD make explicit whether a case is:</p>

<ul>
  <li>not loadable as source,</li>
  <li>loadable but structurally invalid as canonical source,</li>
  <li>structurally valid but semantically rejected,</li>
  <li>semantically accepted but preservation-invalid at the IR boundary,</li>
  <li>semantically accepted but canonical-IR-schema-invalid,</li>
  <li>accepted with preservation requirements.</li>
</ul>

<p>Where useful, a case MAY also make explicit whether it is:</p>

<ul>
  <li>schema-checkable at the source-shape level,</li>
  <li>structurally invalid for reasons that remain source-owned even when they exceed a minimal declarative schema artifact,</li>
  <li>semantically invalid even though canonical source shape has already been accepted,</li>
  <li>IR-schema-invalid even though semantic meaning was previously established.</li>
</ul>

<p>This distinction matters because machine-checkable schema is part of the validation corridor. It is not a replacement for semantic validation. Likewise, canonical JSON IR validity is not a replacement for semantic validity or IR architectural validity.</p>

<hr/>

<h2 id="non-goals">5. Non-Goals</h2>
<p>This directory does not define:</p>

<ul>
  <li>a certification program,</li>
  <li>a universal implementation compatibility matrix,</li>
  <li>a full execution-performance suite,</li>
  <li>a debugger validation framework in full,</li>
  <li>a deployment validation system in full.</li>
</ul>

<p>It also does not introduce new language rules.</p>

<p>Rule:</p>

<pre><code>Specification defines
Conformance exposes
Implementation follows
</code></pre>

<p>Conformance must never become the place where missing language law is invented retroactively. When a case reveals ambiguity, the owning specification document must be clarified.</p>

<hr/>

<h2 id="relation-with-specification-ownership">6. Relation with Specification Ownership</h2>
<p>Conformance does not own language truth.</p>

<p>Ownership remains:</p>

<ul>
  <li><code>Expression/</code> — source structure, canonical source shape, structural validity, and source-schema posture,</li>
  <li><code>Language/</code> — semantic truth and validated meaning,</li>
  <li><code>Libraries/</code> — intrinsic primitive vocabularies and primitive-local behavioral law,</li>
  <li><code>Profiles/</code> — optional standardized capability families,</li>
  <li><code>IR/</code> — canonical execution-facing representation, derivation, identity, construction, schema posture, lowering, and backend-facing boundaries,</li>
  <li><code>IDE/</code> — tooling behavior and authoring-facing concerns.</li>
</ul>

<p>Conformance cases must always map back to these owners.</p>

<pre><code>specification
      -&gt;
conformance
      -&gt;
implementation

Never the reverse.
</code></pre>

<p>In particular:</p>

<ul>
  <li>source-shape and schema-owned rejection cases map back to <code>Expression/</code>,</li>
  <li>semantic rejection cases map back to <code>Language/</code>, <code>Libraries/</code>, or <code>Profiles/</code> as appropriate,</li>
  <li>preservation cases across derivation, identity, attribution, correspondence, construction, and canonical JSON IR validation map back to <code>IR/</code>.</li>
</ul>

<p>A case file is therefore not a second specification. It is a public executable reading of already-published ownership.</p>

<hr/>

<h2 id="critical-boundaries">7. Critical Boundaries</h2>
<p>The first critical conformance boundary is the staged progression:</p>

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

<p>Conformance must make these boundaries observable.</p>

<p>This includes verifying:</p>

<ul>
  <li>what fails before the source is even loadable,</li>
  <li>what fails at source-shape or schema-owned structural validation,</li>
  <li>what fails after canonical source shape is accepted but before semantic meaning is established,</li>
  <li>what establishes semantic meaning,</li>
  <li>what distinctions must survive validation,</li>
  <li>what distinctions must survive derivation into the canonical Execution IR Document,</li>
  <li>what identity, attribution, and correspondence carriers must remain explicit at the canonical JSON IR boundary,</li>
  <li>what distinctions must remain explicit before later lowering and backend-facing handoff.</li>
</ul>

<p>The second critical boundary is:</p>

<pre><code>validated program meaning
      |
      v
canonical Execution IR Document
</code></pre>

<p>The third critical downstream boundary is:</p>

<pre><code>canonical Execution IR Document
      |
      v
lowering / backend-facing handoff
</code></pre>

<p>Critical invariants therefore include:</p>

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
compiler-family route                    != FROG semantic truth
</code></pre>

<p>These invariants are enforced through explicit valid / invalid and preserve / reject expectations.</p>

<hr/>

<h2 id="directory-structure">8. Directory Structure</h2>
<pre><code>Conformance/
├── Readme.md
├── valid/
└── invalid/
</code></pre>

<p>Each case should define, as applicable:</p>

<ul>
  <li>expected loadability,</li>
  <li>expected structural validity,</li>
  <li>expected semantic acceptance,</li>
  <li>expected IR eligibility,</li>
  <li>expected canonical JSON IR validity where relevant,</li>
  <li>tested boundaries,</li>
  <li>preservation requirements,</li>
  <li>rejection reason if invalid.</li>
</ul>

<p>In practice, the directory serves three public roles:</p>

<ul>
  <li>accept — what must validate and remain correct,</li>
  <li>reject — what must fail explicitly,</li>
  <li>preserve — what distinctions must remain explicit across later stages.</li>
</ul>

<p>For v0.1, published cases SHOULD remain small, sharply owned, and explicit about the stage at which acceptance or rejection occurs.</p>

<p>Where useful, cases SHOULD also be written so that the reader can tell whether the failure belongs to:</p>

<ul>
  <li>non-loadable source,</li>
  <li>schema-owned or source-shape-owned structural invalidity,</li>
  <li>semantic invalidity after structural acceptance,</li>
  <li>IR preservation failure after semantic acceptance,</li>
  <li>canonical JSON IR schema failure after otherwise valid IR construction intent.</li>
</ul>

<p>Recommended reading corridor:</p>

<pre><code>loadability
   -&gt;
source-shape / structural validity
   -&gt;
semantic acceptance
   -&gt;
IR derivation / identity / construction preservation
   -&gt;
canonical JSON IR validation where relevant
</code></pre>

<hr/>

<h2 id="published-cases">9. Published Cases</h2>
<p>The current published set combines:</p>

<ul>
  <li>an explicit top-level source-shape valid / invalid block,</li>
  <li>early positive executable anchor cases,</li>
  <li>a mirrored valid / invalid architectural boundary progression,</li>
  <li>additional standalone invalid architectural rejection cases,</li>
  <li>an extended IR recoverability and correspondence-disentanglement progression.</li>
</ul>

<h3>9.1 Published top-level source-shape block</h3>
<p>The published top-level source-shape block currently includes:</p>

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
08_connector_references_unknown_interface_port
</code></pre>

<p>This block matters because it makes the first public structural corridor explicit:</p>

<pre><code>loadable JSON
   -&gt;
canonical top-level source shape
   -&gt;
later semantic validation
</code></pre>

<p>These cases should be read primarily as <code>Expression/</code>-owned conformance around canonical source shape and structural validity.</p>

<h3>9.2 Early valid executable anchor cases</h3>
<pre><code>01_pure_addition
02_ui_value_roundtrip
03_ui_property_write
04_stateful_feedback_delay
</code></pre>

<p>These anchor cases show that conformance is not only about abstract rejection. It also covers minimal positive executable slices that the published architecture is expected to support.</p>

<h3>9.3 Mirrored architectural boundary progression</h3>
<p>The published mirrored progression begins with the foundational distinction families:</p>

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
47 / 48   open execution IR observation surface != private runtime debug state
49 / 50   intentional non-primary correspondence != disguised identity loss
51 / 52   primary execution object must keep recoverable source attribution
53 / 54   schema-valid canonical IR shape != IR architectural validity
55 / 56   semantic acceptance != canonical IR schema validity
57 / 58   region ownership must remain recoverable
59 / 60   structure-boundary terminal recoverability must remain explicit
61 / 62   structure terminal roles must remain recoverable / must not be lost
</code></pre>

<p>This pairing strategy is intentional:</p>

<pre><code>acceptance alone is insufficient
rejection alone is insufficient
both define truth
</code></pre>

<h3>9.4 Extended IR recoverability and correspondence-disentanglement progression</h3>
<p>The published conformance set now also extends the IR-side progression through additional families such as:</p>

<ul>
  <li>multi-contributor attribution,</li>
  <li>declaration reference versus primary execution identity,</li>
  <li>explicit memory identity recoverability,</li>
  <li>structure-family identity recoverability,</li>
  <li>correspondence-category recoverability,</li>
  <li>primary / non-primary / contributor correspondence separation,</li>
  <li>public-interface-boundary versus UI-side correspondence,</li>
  <li>UI-side correspondence disentanglement,</li>
  <li>explicit UI sequencing versus other execution-side categories,</li>
  <li>primary and multi-contributor attribution versus public-boundary, state, structure, and ordinary-connectivity categories.</li>
</ul>

<p>These later families matter because conformance in v0.1 no longer stops at “accepted meaning exists.” It also checks whether canonical Execution IR remains architecturally readable, attributable, and category-safe after derivation.</p>

<h3>9.5 Additional standalone invalid architectural rejection cases</h3>
<p>The published invalid set also contains additional non-mirrored rejection cases such as:</p>

<pre><code>illegal_feedback_without_explicit_memory
interface_widget_role_confusion
ui_reference_without_ui_primitive
</code></pre>

<p>These exist because some architectural failures are important enough to publish even when they are not yet part of one large mirrored numbering progression.</p>

<h3>9.6 Reading rule for published cases</h3>
<p>A published case defines public truth for the published repository state. A session draft that is not yet published does not.</p>

<p>A case SHOULD also be read with stage discipline:</p>

<pre><code>loadability
   -&gt;
source-shape / schema-owned structural validity
   -&gt;
semantic acceptance
   -&gt;
IR preservation expectations
   -&gt;
canonical JSON IR expectations where relevant
</code></pre>

<p>A case SHOULD NOT blur:</p>

<ul>
  <li>schema-owned failure into semantic rejection,</li>
  <li>semantic rejection into source malformedness,</li>
  <li>IR preservation failure into source invalidity,</li>
  <li>implementation subset limitations into specification invalidity.</li>
</ul>

<hr/>

<h2 id="expected-outcomes">10. Expected Outcomes</h2>
<p>Each case expresses structured expectations such as:</p>

<ul>
  <li>Expected loadability: loadable | not loadable</li>
  <li>Expected structural validity: valid | invalid</li>
  <li>Expected meaning: established | not established</li>
  <li>Expected IR result: derivable | not derivable</li>
  <li>Expected IR schema result: schema-valid | not schema-valid</li>
  <li>Expected preservation: required distinctions remain explicit</li>
  <li>Expected rejection: explicit failure reason</li>
</ul>

<p>Examples:</p>

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
</code></pre>

<p>For later-stage-sensitive cases, expectations may also include:</p>

<ul>
  <li>required IR-side recoverability,</li>
  <li>required attribution and correspondence category preservation,</li>
  <li>required distinction between primary and non-primary relations,</li>
  <li>required preservation of execution-side category boundaries before lowering.</li>
</ul>

<p>A useful discipline rule is:</p>

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
</code></pre>

<hr/>

<h2 id="active-v01-conformance-focus">11. Active v0.1 Conformance Focus</h2>
<p>v0.1 focuses on architectural correctness, not broad feature coverage.</p>

<p>Priorities are:</p>

<pre><code>1. source loadability and structural validity
2. semantic validity
3. preservation of distinctions
4. explicit rejection of violations
5. conservative correctness across the IR corridor
6. canonical JSON IR carrier discipline where published
</code></pre>

<p>The active public truth surface therefore emphasizes:</p>

<ul>
  <li>source structure versus semantic acceptance,</li>
  <li>schema-owned source shape versus later semantic legality,</li>
  <li>interface versus widget participation,</li>
  <li>value versus reference participation,</li>
  <li>state versus inferred feedback,</li>
  <li>execution versus layout,</li>
  <li>connectivity versus order,</li>
  <li>explicit state-family boundaries,</li>
  <li>the fact that validated meaning, canonical Execution IR, lowering, and backend-facing handoff are distinct stages rather than one blurred implementation pipeline,</li>
  <li>the fact that explicit <code>source_map[]</code> and <code>correspondence[]</code> carriers belong to the canonical IR boundary rather than to implementation folklore when that published IR posture is in scope,</li>
  <li>the fact that intentional non-primary correspondence is not the same thing as accidental identity loss,</li>
  <li>the fact that open execution IR observation surface is not the same thing as private runtime debug state,</li>
  <li>the fact that schema-valid canonical IR shape is not the same thing as IR architectural validity,</li>
  <li>the fact that semantic acceptance by itself does not establish schema-valid canonical IR,</li>
  <li>the fact that region ownership, terminal recoverability, role recoverability, attribution recoverability, and correspondence-category recoverability all belong to the canonical IR preservation surface,</li>
  <li>the fact that UI-side sequencing, UI-object operations, public-interface participation, ordinary connectivity, control-structure boundaries, and state boundaries are not interchangeable correspondence families.</li>
</ul>

<p>Rule:</p>

<pre><code>no implicit meaning
no silent repair
no hidden interpretation
no silent stage collapse
</code></pre>

<hr/>

<h2 id="relation-with-examples-ir-and-reference-implementation">12. Relation with Examples, IR, and Reference Implementation</h2>
<pre><code>Examples/                   -&gt; illustrate and anchor named programs
Conformance/                -&gt; define public expectations
Implementations/Reference/  -&gt; try to execute correctly
</code></pre>

<p>These roles must remain strictly separated.</p>

<p>Likewise, the relation with the specification corridor is:</p>

<pre><code>Expression/
   defines canonical source structure, source-schema posture, and structural validity

Language/
   defines semantic truth

IR/
   defines the canonical execution-facing artifact, derivation, identity,
   construction, schema posture, lowering, and backend-facing boundaries

Conformance/
   tests whether those published boundaries are being respected
</code></pre>

<p>An implementation passing a case does not redefine the language. It only demonstrates alignment with the published conformance surface.</p>

<p>A machine-checkable schema artifact may assist source-structure validation. It does not replace the ownership boundary above. Likewise, a machine-checkable IR schema artifact may assist canonical JSON IR validation. It does not replace the ownership of semantic truth or IR architectural validity.</p>

<p>The reference implementation therefore remains a downstream consumer of published conformance expectations. It is useful as a proof surface. It is not the owner of conformance truth.</p>

<hr/>

<h2 id="future-growth">13. Future Growth</h2>
<p>Growth must remain controlled and architecture-driven.</p>

<p>Preferred pattern:</p>

<pre><code>small case
-&gt; clear boundary
-&gt; clear expectation
-&gt; clear ownership
</code></pre>

<p>Near-term future expansion areas include:</p>

<ul>
  <li>remaining correspondence disentanglement families,</li>
  <li>source-shape and schema rejection cases,</li>
  <li>type and value legality,</li>
  <li>state semantics and timing,</li>
  <li>structure legality,</li>
  <li>validated meaning to canonical-IR preservation,</li>
  <li>IR identity, attribution, and correspondence carrier discipline,</li>
  <li>IR canonical JSON schema-valid versus non-schema-valid cases,</li>
  <li>profile-dependent behavior,</li>
  <li>backend-family and target-profile rejection cases where applicable.</li>
</ul>

<p>Growth should continue to prefer:</p>

<ul>
  <li>small sharply owned boundary cases,</li>
  <li>mirrored valid / invalid pairs where they clarify truth,</li>
  <li>additional standalone invalid cases where architecture requires them,</li>
  <li>explicit published expectations rather than implementation folklore.</li>
</ul>

<p>As source-schema closure grows, conformance SHOULD increasingly distinguish:</p>

<ul>
  <li>malformed source,</li>
  <li>schema-level structural failure,</li>
  <li>structural failure that exceeds a minimal declarative schema artifact but still belongs to <code>Expression/</code>,</li>
  <li>semantic rejection after structural acceptance.</li>
</ul>

<p>As IR closure grows, conformance SHOULD also increasingly distinguish:</p>

<ul>
  <li>semantically accepted programs that derive to valid canonical IR,</li>
  <li>IR preservation failures,</li>
  <li>canonical JSON IR schema failures,</li>
  <li>valid intentional non-primary correspondence,</li>
  <li>invalid attribution loss disguised as omission,</li>
  <li>valid recoverable correspondence categories,</li>
  <li>invalid category collapse across attribution, boundary, connectivity, state, structure, and UI-side relation families.</li>
</ul>

<hr/>

<h2 id="summary">14. Summary</h2>
<p>This directory is the public truth surface of FROG conformance.</p>

<p>It defines:</p>

<ul>
  <li>what must be accepted,</li>
  <li>what must be rejected,</li>
  <li>what must be preserved.</li>
</ul>

<p>Core rule:</p>

<pre><code>Specification defines truth
Conformance exposes truth
Implementations must align
</code></pre>

<p>Or more directly:</p>

<pre><code>rules are written
cases make them testable
tools must follow
</code></pre>

<p>In v0.1, conformance is intentionally conservative and architecture-first. It exists to keep the most important public boundaries explicit:</p>

<pre><code>.frog source
   -&gt;
loadable source
   -&gt;
source-shape / schema-owned structural validity
   -&gt;
validated meaning
   -&gt;
canonical Execution IR
   -&gt;
canonical JSON IR validation where relevant
   -&gt;
lowering / backend-facing handoff
   -&gt;
private realization
</code></pre>

<p>Conformance checks:</p>

<pre><code>accept
reject
preserve
</code></pre>
