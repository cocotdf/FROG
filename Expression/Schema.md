<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">FROG Source Schema</h1>

<p align="center">
  <strong>Schema posture and machine-checkable structural validation for canonical <code>.frog</code> source</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-document-exists">2. Why This Document Exists</a></li>
  <li><a href="#ownership-boundary">3. Ownership Boundary</a></li>
  <li><a href="#what-schema-means-in-frog">4. What “Schema” Means in FROG</a></li>
  <li><a href="#structural-validation-boundary">5. Structural Validation Boundary</a></li>
  <li><a href="#non-goals">6. Non-Goals</a></li>
  <li><a href="#schema-layers">7. Schema Layers</a></li>
  <li><a href="#top-level-canonical-source-shape">8. Top-Level Canonical Source Shape</a></li>
  <li><a href="#section-level-schema-ownership">9. Section-Level Schema Ownership</a></li>
  <li><a href="#cross-cutting-source-subsystems">10. Cross-Cutting Source Subsystems</a></li>
  <li><a href="#machine-checkable-schema-posture">11. Machine-Checkable Schema Posture</a></li>
  <li><a href="#schema-vs-semantic-validation">12. Schema vs Semantic Validation</a></li>
  <li><a href="#schema-vs-ir-vs-runtime">13. Schema vs IR vs Runtime</a></li>
  <li><a href="#validator-posture">14. Validator Posture</a></li>
  <li><a href="#relation-with-conformance">15. Relation with Conformance</a></li>
  <li><a href="#representation-and-evolution-rules">16. Representation and Evolution Rules</a></li>
  <li><a href="#minimum-guarantees">17. Minimum Guarantees</a></li>
  <li><a href="#reading-rule">18. Reading Rule</a></li>
  <li><a href="#status">19. Status</a></li>
  <li><a href="#license">20. License</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the schema posture of canonical FROG source.
It specifies how machine-checkable structural validation relates to the published FROG Expression specification.
</p>

<p>
In FROG, a schema is not the whole language.
A schema is the machine-checkable structural contract of canonical <code>.frog</code> source.
It exists so that source-shape validation becomes explicit, reproducible, implementation-comparable, and clearly separated from semantic validation, IR derivation, lowering, backend-facing handoff, and private runtime realization.
</p>

<p>
This document therefore sits at the following boundary:
</p>

<pre><code>canonical source prose
        +
machine-checkable structural rules
        -
validated meaning
        -
Execution IR
        -
lowering and backend contract
        -
runtime-private realization
</code></pre>

<p>
This is a source-ownership document.
It defines what schema means in FROG, what schema is allowed to own, what schema must not own, and how machine-checkable source validation must remain disciplined as the repository grows.
</p>

<hr/>

<h2 id="why-this-document-exists">2. Why This Document Exists</h2>

<p>
The repository already defines canonical source structure in <code>Expression/</code>.
However, once disciplined validators, conformance growth, and repeatable reference execution matter, structural validity must not remain prose-only or validator-folklore-only.
</p>

<p>
This document exists so that:
</p>

<ul>
  <li>canonical source ownership remains explicit,</li>
  <li>structural validation becomes machine-checkable enough to be reproducible,</li>
  <li>validator behavior can be compared against published repository law,</li>
  <li>implementations do not silently redefine structural truth through ad hoc parsing logic,</li>
  <li>the boundary between malformed source, structurally invalid source, and semantically rejected source remains stable.</li>
</ul>

<p>
The goal is not to replace the Expression specification with one technical artifact.
The goal is to make the structural contract repository-visible in both normative prose and machine-checkable form.
</p>

<hr/>

<h2 id="ownership-boundary">3. Ownership Boundary</h2>

<p>
This document belongs to <code>Expression/</code> because schema ownership is source ownership.
</p>

<pre><code>Expression/   -> canonical source structure and structural validity
Language/     -> validated program meaning
IR/           -> derived open execution-facing representation
Libraries/    -> intrinsic primitive meaning
Profiles/     -> optional capability meaning
IDE/          -> authoring, presentation, debugging, observability
</code></pre>

<p>
Accordingly:
</p>

<ul>
  <li><code>Expression/</code> owns schema posture for canonical <code>.frog</code> source.</li>
  <li><code>Expression/</code> owns what is machine-checkable as source structure.</li>
  <li><code>Expression/</code> does not own validated meaning.</li>
  <li><code>Expression/</code> does not own Execution IR shape.</li>
  <li><code>Expression/</code> does not own lowering.</li>
  <li><code>Expression/</code> does not own backend contract content.</li>
  <li><code>Expression/</code> does not own private runtime representation.</li>
</ul>

<p>
A validator may consume a schema.
A schema does not become the owner of the language.
The published specification remains the owner of the language.
</p>

<hr/>

<h2 id="what-schema-means-in-frog">4. What “Schema” Means in FROG</h2>

<p>
In FROG, “schema” means the machine-checkable description of canonical source shape that is appropriate to structural validation.
</p>

<p>
It may cover, for example:
</p>

<ul>
  <li>top-level object shape,</li>
  <li>required versus optional top-level sections,</li>
  <li>section type constraints,</li>
  <li>required object properties for structurally defined source objects,</li>
  <li>allowed structural discriminators,</li>
  <li>container kinds such as object, array, and scalar where structurally relevant,</li>
  <li>forbidden malformed placements that can be rejected without semantic interpretation.</li>
</ul>

<p>
It does not automatically cover every rule that can be stated in prose.
Some structural rules may remain validator logic rather than pure declarative schema when they clearly belong to source structure but are awkward to encode declaratively without reducing clarity or recoverability.
</p>

<p>
Therefore, “schema” in FROG is:
</p>

<ul>
  <li>broader than one serialization technology,</li>
  <li>broader than one validator implementation,</li>
  <li>narrower than the whole language,</li>
  <li>strictly upstream from semantic validation and IR work.</li>
</ul>

<hr/>

<h2 id="structural-validation-boundary">5. Structural Validation Boundary</h2>

<p>
Structural validation is the stage after loadability and before semantic validation.
</p>

<pre><code>bytes / text
    -> loadable JSON source
    -> structurally valid canonical source
    -> validated program meaning
    -> open execution-facing derivation
    -> lowering / backend-facing handoff
    -> private realization
</code></pre>

<p>
This document governs the second step only.
</p>

<ul>
  <li>not malformed bytes,</li>
  <li>not parser failure,</li>
  <li>not semantic legality,</li>
  <li>not execution correctness,</li>
  <li>not backend suitability,</li>
  <li>not deployment readiness.</li>
</ul>

<p>
A source file may therefore be:
</p>

<ul>
  <li>not loadable,</li>
  <li>loadable but structurally invalid,</li>
  <li>structurally valid but semantically invalid,</li>
  <li>semantically valid but unsupported by a given implementation subset.</li>
</ul>

<p>
These states MUST NOT be collapsed.
A structural rejection is not a semantic rejection.
A semantic rejection is not malformed source.
An implementation subset limitation is not specification invalidity.
</p>

<hr/>

<h2 id="non-goals">6. Non-Goals</h2>

<p>
This document does not define:
</p>

<ul>
  <li>the complete semantic interpretation of nodes, edges, structures, widgets, or state,</li>
  <li>the complete legality of type and value combinations,</li>
  <li>the full primitive catalog,</li>
  <li>profile-owned optional capability semantics,</li>
  <li>Execution IR construction,</li>
  <li>lowering strategy,</li>
  <li>backend contract content,</li>
  <li>runtime scheduling choices,</li>
  <li>private debug state,</li>
  <li>IDE Program Model details.</li>
</ul>

<p>
This document also does not require one mandatory schema technology.
A JSON Schema artifact may be used.
Other machine-checkable validator-support artifacts may also exist.
The normative requirement is the published structural contract, not one implementation convenience format.
</p>

<hr/>

<h2 id="schema-layers">7. Schema Layers</h2>

<p>
FROG source-schema posture has three layers.
</p>

<h3>7.1 Normative structural prose</h3>

<p>
The primary owner remains the published specification text in <code>Expression/</code>.
If a machine artifact and the published prose disagree, the prose wins until the repository is corrected and republished coherently.
</p>

<h3>7.2 Repository-visible machine-checkable schema artifacts</h3>

<p>
The repository MAY publish machine-checkable artifacts such as:
</p>

<ul>
  <li>JSON Schema documents,</li>
  <li>section-local schema fragments,</li>
  <li>validator-facing structural rule tables,</li>
  <li>generated schema bundles whose ownership remains traceable to published source documents.</li>
</ul>

<p>
These artifacts make structural validation more reproducible.
They do not replace the normative specification layer.
</p>

<h3>7.3 Implementation validator logic</h3>

<p>
Implementations MAY contain validator logic that applies the published schema posture.
That logic is downstream.
It must align with the published source contract.
It must not silently expand language law.
</p>

<p>
Useful reading rule:
</p>

<pre><code>published prose
    owns structural truth

machine-checkable artifact
    assists structural reproducibility

implementation validator
    consumes the published contract
</code></pre>

<hr/>

<h2 id="top-level-canonical-source-shape">8. Top-Level Canonical Source Shape</h2>

<p>
At the top level, a canonical <code>.frog</code> source file MUST satisfy the following structural posture:
</p>

<ul>
  <li>the root MUST be a JSON object,</li>
  <li>the root MUST contain <code>spec_version</code>, <code>metadata</code>, <code>interface</code>, and <code>diagram</code>,</li>
  <li>the root MAY contain <code>connector</code>, <code>front_panel</code>, <code>icon</code>, <code>ide</code>, and <code>cache</code>,</li>
  <li>required and optional sections MUST appear at the top level only,</li>
  <li>top-level section names MUST follow the canonical section vocabulary defined by <code>Expression/</code>,</li>
  <li>top-level section values MUST have the structural kind required by their owning section specification,</li>
  <li>unexpected top-level sections MUST be rejected as structurally invalid canonical source.</li>
</ul>

<p>
This document does not restate every section rule in full.
Section-specific structural detail remains owned by the corresponding specification document.
</p>

<hr/>

<h2 id="section-level-schema-ownership">9. Section-Level Schema Ownership</h2>

<p>
Section-level schema ownership remains local and explicit.
</p>

<pre><code>Metadata.md           -> shape of metadata section
Interface.md          -> shape of interface section
Connector.md          -> shape of connector section
Diagram.md            -> shape of diagram section
Front panel.md        -> shape of front_panel section
Icon.md               -> shape of icon section
IDE preferences.md    -> shape of ide section
Cache.md              -> shape of cache section
</code></pre>

<p>
This file does not centralize every sub-object definition into one giant prose table.
Instead, it defines the posture under which those section-owned source rules may be rendered into machine-checkable structural artifacts.
</p>

<p>
A useful ownership rule is:
</p>

<ul>
  <li>root-level section presence is governed here and in <code>Expression/Readme.md</code>,</li>
  <li>section-local structural object shape is governed by the owning section document,</li>
  <li>cross-section semantic consistency is not automatically a schema concern.</li>
</ul>

<p>
This avoids one of the main failure modes of growing schema systems:
a central artifact silently becoming the hidden owner of many local section rules that it no longer explains well.
</p>

<hr/>

<h2 id="cross-cutting-source-subsystems">10. Cross-Cutting Source Subsystems</h2>

<p>
Some source subsystems are cross-cutting rather than top-level sections.
Examples include:
</p>

<ul>
  <li>type expressions,</li>
  <li>widget model,</li>
  <li>widget interaction source objects,</li>
  <li>control-structure source representation,</li>
  <li>explicit local-memory source representation.</li>
</ul>

<p>
These subsystems may contribute machine-checkable structural rules when they affect canonical source shape.
However, their semantic consequences remain outside the schema layer when they belong to validated meaning.
</p>

<p>
Example distinction:
</p>

<ul>
  <li>“this object MUST contain a <code>kind</code> discriminator and an array named <code>ports</code>” may be schema-level,</li>
  <li>“this structure is semantically legal only when its selector type matches all branch expectations” is not automatically schema-level.</li>
</ul>

<p>
Schema growth across cross-cutting subsystems should therefore remain selective and boundary-aware:
encode structural shape where useful, but do not drag semantic legality upstream into source-shape validation.
</p>

<hr/>

<h2 id="machine-checkable-schema-posture">11. Machine-Checkable Schema Posture</h2>

<p>
A repository-visible machine-checkable schema artifact SHOULD aim to capture the parts of structural validity that are:
</p>

<ul>
  <li>source-owned,</li>
  <li>stable enough to encode,</li>
  <li>implementation-independent,</li>
  <li>useful for reproducible validator behavior.</li>
</ul>

<p>
It SHOULD NOT attempt to force every meaningful rule into one declarative format when that would:
</p>

<ul>
  <li>blur the structural versus semantic boundary,</li>
  <li>smuggle execution meaning into source schema,</li>
  <li>encode implementation-specific convenience as if it were repository law,</li>
  <li>make published ownership harder to understand,</li>
  <li>reduce recoverability of why a rule exists and where it is owned.</li>
</ul>

<p>
Accordingly, the machine-checkable schema posture in FROG is intentionally conservative:
</p>

<ul>
  <li>capture source shape first,</li>
  <li>capture top-level section presence rules,</li>
  <li>capture obvious structural object requirements,</li>
  <li>leave semantic interpretation to later validation stages,</li>
  <li>leave IR construction to the IR corridor,</li>
  <li>leave runtime choices to implementations.</li>
</ul>

<p>
At the current repository stage, the published machine-checkable posture may therefore be partial without being weak.
Partial machine-checkability is acceptable when:
</p>

<ul>
  <li>its limits are explicit,</li>
  <li>ownership remains attributable,</li>
  <li>structural versus semantic boundaries remain clear,</li>
  <li>implementations are not forced to guess silently.</li>
</ul>

<p>
The important rule is not “encode everything”.
The important rule is:
</p>

<pre><code>encode what is structurally stable
publish what remains prose-owned
do not blur the boundary
</code></pre>

<hr/>

<h2 id="schema-vs-semantic-validation">12. Schema vs Semantic Validation</h2>

<p>
Schema validation and semantic validation are related but distinct.
</p>

<h3>12.1 Schema validation asks</h3>

<ul>
  <li>Is the source loadable as JSON?</li>
  <li>Is the root shape correct?</li>
  <li>Are required sections present?</li>
  <li>Are optional sections placed correctly?</li>
  <li>Do section values have the expected structural kind?</li>
  <li>Are structurally required identifiers or discriminators present where the source model requires them?</li>
</ul>

<h3>12.2 Semantic validation asks</h3>

<ul>
  <li>Does the diagram mean something legal in the language?</li>
  <li>Are types compatible where meaning requires compatibility?</li>
  <li>Are structures used legally?</li>
  <li>Are cycles legal only through explicit local memory?</li>
  <li>Are primitive invocations valid with respect to their library definition?</li>
  <li>Are profile-owned capabilities used only where allowed?</li>
</ul>

<p>
A key FROG rule is therefore:
</p>

<pre><code>schema-valid
does not mean
semantically valid
</code></pre>

<p>
And the inverse is equally important:
</p>

<pre><code>semantic rejection
must not be mislabeled
as malformed source
</code></pre>

<p>
Likewise:
</p>

<pre><code>unsupported by one implementation subset
does not mean
invalid by repository law
</code></pre>

<hr/>

<h2 id="schema-vs-ir-vs-runtime">13. Schema vs IR vs Runtime</h2>

<p>
The schema layer must remain upstream from the IR corridor.
</p>

<pre><code>.frog source
    -> source schema / structural validation
    -> validated meaning
    -> Execution IR
    -> lowering
    -> backend contract
    -> backend-family consumption
    -> deployment realization
    -> runtime services on target
</code></pre>

<p>
Therefore, the schema layer MUST NOT:
</p>

<ul>
  <li>define Execution IR node identities,</li>
  <li>define derivation results as if they were source shape,</li>
  <li>define lowering-time specialization,</li>
  <li>define backend-family assumptions,</li>
  <li>define runtime module composition,</li>
  <li>define private scheduling order,</li>
  <li>define private observation state.</li>
</ul>

<p>
The schema layer only guarantees that canonical source is structurally well-formed enough to proceed to later stages.
It does not guarantee semantic acceptance.
It does not guarantee successful execution.
It does not guarantee support in one implementation stack.
</p>

<hr/>

<h2 id="validator-posture">14. Validator Posture</h2>

<p>
A FROG validator is a downstream consumer of the published structural contract.
It may be split internally into stages such as:
</p>

<pre><code>loader
    -> source-shape checker
    -> structural validator
    -> semantic validator
</code></pre>

<p>
That split is encouraged because it keeps rejection reasons explicit.
</p>

<p>
A validator SHOULD report at least:
</p>

<ul>
  <li>loadability failures,</li>
  <li>structural validation failures,</li>
  <li>semantic validation failures,</li>
  <li>unsupported-but-valid situations when an implementation subset is narrower than repository law.</li>
</ul>

<p>
A validator MAY use repository-visible machine-checkable artifacts to support structural validation.
However:
</p>

<ul>
  <li>a machine-checkable artifact does not override normative prose,</li>
  <li>implementation convenience does not override published ownership,</li>
  <li>a passed validator run does not redefine the language.</li>
</ul>

<p>
A validator MUST NOT:
</p>

<ul>
  <li>silently repair malformed canonical source,</li>
  <li>quietly reinterpret structurally invalid source into some private acceptable form,</li>
  <li>treat implementation convenience as if it were specification truth,</li>
  <li>collapse source validation, semantic validation, and runtime support into one blurred rejection category.</li>
</ul>

<hr/>

<h2 id="relation-with-conformance">15. Relation with Conformance</h2>

<p>
This document defines schema posture.
<code>Conformance/</code> defines public testable expectations against that posture.
</p>

<pre><code>Expression/                  -> structural contract is written
Conformance/                 -> structural contract is tested
Implementations/Reference/   -> structural contract is consumed
</code></pre>

<p>
Accordingly:
</p>

<ul>
  <li>schema-owned rejection cases belong naturally in <code>Conformance/invalid/</code>,</li>
  <li>schema-owned acceptance cases belong naturally in <code>Conformance/valid/</code>,</li>
  <li>conformance expectations SHOULD distinguish loadability, structural validity, semantic acceptance, and preservation.</li>
</ul>

<p>
Conformance does not redefine schema ownership.
It makes it inspectable.
A case passing in one implementation does not turn implementation behavior into repository law.
</p>

<hr/>

<h2 id="representation-and-evolution-rules">16. Representation and Evolution Rules</h2>

<p>
The schema posture of FROG must remain evolvable without becoming unstable.
</p>

<p>
Therefore:
</p>

<ul>
  <li>schema artifacts SHOULD be derived from published source ownership rather than invented independently,</li>
  <li>schema artifacts SHOULD be version-aware where <code>spec_version</code> materially affects allowed source structure,</li>
  <li>new schema constraints SHOULD be introduced conservatively,</li>
  <li>schema growth SHOULD prefer explicit ownership and recoverability over compact cleverness,</li>
  <li>schema changes MUST NOT silently move semantic, IR, or runtime ownership into <code>Expression/</code>.</li>
</ul>

<p>
A repository-visible schema artifact MAY be incomplete relative to all structural prose if its limits are explicit.
Partial machine-checkability is acceptable.
Silent ambiguity is not.
</p>

<p>
Preferred growth pattern:
</p>

<pre><code>published ownership
    -> explicit structural rule
    -> repository-visible machine-checkable form
    -> conformance case
    -> implementation alignment
</code></pre>

<hr/>

<h2 id="minimum-guarantees">17. Minimum Guarantees</h2>

<p>
At minimum, the FROG source-schema posture MUST preserve the following guarantees:
</p>

<ul>
  <li>canonical <code>.frog</code> source has an explicit top-level object shape,</li>
  <li>required top-level sections are explicit,</li>
  <li>optional top-level sections are explicit,</li>
  <li>section placement rules are explicit,</li>
  <li>unexpected top-level sections are structurally rejectable,</li>
  <li>section-local structural ownership remains attributable,</li>
  <li>structural validity remains distinct from semantic validity,</li>
  <li>schema artifacts remain downstream from normative prose,</li>
  <li>validators remain downstream from published repository law.</li>
</ul>

<hr/>

<h2 id="reading-rule">18. Reading Rule</h2>

<p>
Use the following reading rule when deciding whether a question belongs to source schema.
</p>

<pre><code>If the question is:
- "Can this be rejected without semantic interpretation?"          -> likely schema / structural validity
- "Is this the correct top-level source shape?"                    -> schema / structural validity
- "Is this source object missing structurally required fields?"    -> schema / structural validity
- "What does this validated program mean?"                         -> Language/
- "What does this primitive do?"                                   -> Libraries/
- "What does this optional capability mean?"                       -> Profiles/
- "What does the open execution-facing form look like?"            -> IR/
- "How does one runtime realize it privately?"                     -> implementation, not schema
</code></pre>

<p>
Companion rule:
</p>

<pre><code>reject early when the source shape is wrong
but do not use schema
to answer semantic questions
</code></pre>

<hr/>

<h2 id="status">19. Status</h2>

<p>
This document establishes the published schema posture of canonical FROG source.
It does not by itself close every section-local machine-checkable rule.
It defines the ownership model under which that closure can proceed without architectural blur.
</p>

<p>
At the current repository stage, machine-checkable support is intentionally conservative.
That conservatism is deliberate:
it improves structural reproducibility without pretending that all structural prose has already been fully rendered into one artifact.
</p>

<p>
Immediate consequence:
</p>

<pre><code>source shape
can now be discussed
tested
and made machine-checkable
as a first-class published concern
inside Expression/
rather than as implementation folklore
</code></pre>

<hr/>

<h2 id="license">20. License</h2>

<p>
This document is part of the FROG repository and is covered by the repository license.
See the root <code>LICENSE</code> file for details.
</p>
