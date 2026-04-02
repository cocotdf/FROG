<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG IR Schema Posture</h1>

<p align="center">
  <strong>Normative schema posture for the canonical JSON Execution IR Document</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-document-exists">2. Why This Document Exists</a></li>
  <li><a href="#scope">3. Scope</a></li>
  <li><a href="#relation-with-other-ir-documents">4. Relation with Other IR Documents</a></li>
  <li><a href="#normative-posture">5. Normative Posture</a></li>
  <li><a href="#what-the-schema-validates">6. What the Schema Validates</a></li>
  <li><a href="#what-the-schema-does-not-validate">7. What the Schema Does Not Validate</a></li>
  <li><a href="#canonical-document-boundary">8. Canonical Document Boundary</a></li>
  <li><a href="#canonical-json-posture">9. Canonical JSON Posture</a></li>
  <li><a href="#schema-family">10. Schema Family</a></li>
  <li><a href="#top-level-document-categories">11. Top-Level Document Categories</a></li>
  <li><a href="#execution-unit-categories">12. Execution Unit Categories</a></li>
  <li><a href="#object-category-posture">13. Object Category Posture</a></li>
  <li><a href="#connection-category-posture">14. Connection Category Posture</a></li>
  <li><a href="#region-category-posture">15. Region Category Posture</a></li>
  <li><a href="#source-map-and-correspondence-posture">16. Source Map and Correspondence Posture</a></li>
  <li><a href="#identity-and-recoverability-posture">17. Identity and Recoverability Posture</a></li>
  <li><a href="#schema-validity-versus-architectural-validity">18. Schema Validity Versus Architectural Validity</a></li>
  <li><a href="#forbidden-misreadings">19. Forbidden Misreadings</a></li>
  <li><a href="#relation-with-lowering-and-backend-contract">20. Relation with Lowering and Backend Contract</a></li>
  <li><a href="#summary">21. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the schema posture for the canonical FROG Execution IR Document in base v0.1.
</p>

<p>
The Execution IR is not only an architectural layer.
It is also a canonical open artifact that a conforming implementation MUST be able to emit as JSON.
This document defines how that canonical JSON form is validated structurally.
</p>

<p>
Accordingly, the schema exists to provide:
</p>

<ul>
  <li>a machine-checkable structural boundary for canonical JSON IR emission,</li>
  <li>a stable validation surface for interchange, tooling, regression testing, and conformance reasoning,</li>
  <li>a companion to the architectural, derivation, identity, and construction law of the IR layer,</li>
  <li>a disciplined boundary between canonical open IR and later downstream specialization.</li>
</ul>

<p>
The schema is therefore part of the open IR corridor:
</p>

<pre><code>validated program meaning
   -&gt;
canonical Execution IR Document
   -&gt;
canonical JSON validation
   -&gt;
later lowering
   -&gt;
backend-facing handoff
   -&gt;
private realization</code></pre>

<p>
This document does not say that JSON schema replaces architectural law.
It says that canonical JSON IR must be machine-checkable in a way that remains aligned with architectural law.
</p>

<hr/>

<h2 id="why-this-document-exists">2. Why This Document Exists</h2>

<p>
A canonical open IR is only durable if it is:
</p>

<ul>
  <li>architecturally defined,</li>
  <li>derivable from validated meaning,</li>
  <li>recoverable and attributable,</li>
  <li>materially constructible,</li>
  <li>machine-checkable as a canonical artifact.</li>
</ul>

<p>
Without a schema posture, the canonical JSON form would drift into:
</p>

<ul>
  <li>implementation-specific payload conventions,</li>
  <li>unstated omissions,</li>
  <li>shape ambiguity,</li>
  <li>non-portable inspection tooling,</li>
  <li>backend-driven accidental formats.</li>
</ul>

<p>
This document therefore exists to ensure that:
</p>

<ul>
  <li>the canonical JSON Execution IR form is a real public artifact,</li>
  <li>implementations can be compared at the structural JSON boundary,</li>
  <li>construction remains aligned with a machine-checkable target,</li>
  <li>schema validity is clearly separated from deeper architectural validity.</li>
</ul>

<hr/>

<h2 id="scope">3. Scope</h2>

<p>
This document defines:
</p>

<ul>
  <li>the normative posture of the canonical JSON IR schema artifacts,</li>
  <li>what structural categories the schema validates,</li>
  <li>how the canonical IR document family is framed in JSON,</li>
  <li>the required presence of the principal top-level and execution-unit categories in base v0.1,</li>
  <li>the posture of <code>source_map</code> and <code>correspondence</code> as explicit schema-validated record arrays,</li>
  <li>the distinction between schema-validity and deeper architectural validity.</li>
</ul>

<p>
This document does not define:
</p>

<ul>
  <li>validated language meaning,</li>
  <li>the full execution semantics of any object family,</li>
  <li>the full derivation law from meaning to IR,</li>
  <li>the full identity and recoverability law in isolation,</li>
  <li>the full material construction procedure for every implementation,</li>
  <li>backend-specific lowered forms,</li>
  <li>runtime-private execution artifacts.</li>
</ul>

<hr/>

<h2 id="relation-with-other-ir-documents">4. Relation with Other IR Documents</h2>

<p>
This document MUST be read together with the rest of the IR layer.
</p>

<p>
Ownership remains:
</p>

<pre><code>Execution IR.md
   -&gt; architectural identity of the canonical open IR

Derivation rules.md
   -&gt; what must correspond from validated meaning to IR content

Identity and Mapping.md
   -&gt; attribution, correspondence, and recoverability law

Construction rules.md
   -&gt; how conforming canonical IR payloads are materially built

Schema.md
   -&gt; schema posture for machine-checkable structural validation

IR/schema/
   -&gt; machine-checkable schema artifacts

Lowering.md
   -&gt; later target-oriented specialization

Backend contract.md
   -&gt; later backend-facing handoff</code></pre>

<p>
This document therefore MUST be read as a schema companion to the architectural and construction material rather than as a replacement for them.
</p>

<pre><code>Architecture
   -&gt; Execution IR.md

Derivation
   -&gt; Derivation rules.md

Identity / recoverability
   -&gt; Identity and Mapping.md

Construction
   -&gt; Construction rules.md

Schema posture
   -&gt; Schema.md

Machine-checkable schema
   -&gt; IR/schema/</code></pre>

<hr/>

<h2 id="normative-posture">5. Normative Posture</h2>

<p>
The schema artifacts published in <code>IR/schema/</code> are normative for structural validation of the canonical JSON Execution IR Document in the matching schema version.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>a conforming implementation MUST be able to emit a canonical JSON Execution IR Document that satisfies the published schema for the claimed version,</li>
  <li>a payload that fails the published schema MUST NOT be claimed as a schema-valid canonical Execution IR Document for that schema version,</li>
  <li>schema validity alone does not imply full semantic validity, derivation correctness, or architectural sufficiency,</li>
  <li>schema compliance MUST be interpreted together with the rest of the IR and Language specifications.</li>
</ul>

<p>
The schema is therefore:
</p>

<ul>
  <li>normative for structural JSON validity,</li>
  <li>non-sufficient for full architectural correctness,</li>
  <li>downstream from derivation law,</li>
  <li>upstream from lowering and backend-facing specialization.</li>
</ul>

<hr/>

<h2 id="what-the-schema-validates">6. What the Schema Validates</h2>

<p>
The schema validates the structural JSON boundary of the canonical Execution IR Document.
</p>

<p>
In base v0.1, this includes at least:
</p>

<ul>
  <li>top-level document shape,</li>
  <li>required document categories,</li>
  <li>execution-unit shape,</li>
  <li>required execution-unit arrays and records,</li>
  <li>object, connection, and region record families,</li>
  <li>identifier-bearing fields where published,</li>
  <li>source attribution and correspondence support categories,</li>
  <li>enum-style structural category restrictions where published by the schema artifacts.</li>
</ul>

<p>
The schema therefore answers questions such as:
</p>

<ul>
  <li>Is this a structurally valid canonical JSON Execution IR payload?</li>
  <li>Does the execution unit include the required major categories?</li>
  <li>Are object, connection, region, source-map, and correspondence carriers present at the required structural level?</li>
  <li>Do records satisfy the machine-checkable field and category constraints of the claimed schema version?</li>
</ul>

<hr/>

<h2 id="what-the-schema-does-not-validate">7. What the Schema Does Not Validate</h2>

<p>
The schema does not validate everything that matters.
</p>

<p>
The schema does not by itself prove:
</p>

<ul>
  <li>that semantic validation upstream was correct,</li>
  <li>that derivation preserved validated meaning correctly,</li>
  <li>that identity and mapping obligations were satisfied in the strong architectural sense,</li>
  <li>that all category distinctions remain recoverable in the way required by the IR architecture,</li>
  <li>that a schema-valid payload is suitable for every later lowering route,</li>
  <li>that a backend-facing contract derived later will be correct.</li>
</ul>

<p>
In particular:
</p>

<pre><code>schema-valid
   does not imply
semantically valid

schema-valid
   does not imply
architecturally sufficient

schema-valid
   does not imply
identity-correct in every deeper sense

schema-valid
   does not imply
lowering-correct

schema-valid
   does not imply
backend-correct</code></pre>

<p>
The schema validates structural admissibility of the canonical JSON form.
It does not replace the rest of the specification.
</p>

<hr/>

<h2 id="canonical-document-boundary">8. Canonical Document Boundary</h2>

<p>
In base v0.1, the canonical JSON IR posture is intentionally conservative:
</p>

<ul>
  <li>one canonical Execution IR Document,</li>
  <li>one execution unit inside that document,</li>
  <li>one principal open-boundary document family,</li>
  <li>one primary schema artifact rooted at the document level.</li>
</ul>

<p>
That posture exists so the open IR boundary remains:
</p>

<ul>
  <li>portable,</li>
  <li>inspectable,</li>
  <li>diffable,</li>
  <li>stable across conforming implementations.</li>
</ul>

<p>
The canonical document boundary is therefore not:
</p>

<ul>
  <li>a bag of backend-private fragments,</li>
  <li>a runtime snapshot,</li>
  <li>a private scheduler graph dump,</li>
  <li>a target-family-specific lowered artifact.</li>
</ul>

<hr/>

<h2 id="canonical-json-posture">9. Canonical JSON Posture</h2>

<p>
The preferred base v0.1 canonical posture is explicit and regular.
</p>

<p>
At the JSON boundary, the canonical Execution IR Document SHOULD expose clearly separated categories rather than relying on positional conventions or implementation-private packing.
</p>

<p>
The preferred posture is:
</p>

<pre><code>{
  "document_id": "...",
  "unit": {
    "id": "...",
    "objects": [ ... ],
    "connections": [ ... ],
    "regions": [ ... ],
    "source_map": [ ... ],
    "correspondence": [ ... ],
    "metadata": { ... }
  }
}</code></pre>

<p>
The exact schema-owned fields and constraints belong to the published JSON Schema artifacts.
The architectural posture here is that canonical JSON IR remains explicit, stable, and category-oriented.
</p>

<p>
This posture supports:
</p>

<ul>
  <li>ordinary JSON validation tools,</li>
  <li>repository diffability,</li>
  <li>portable inspection,</li>
  <li>clear separation between execution structure and attribution support structure,</li>
  <li>future lowering without forcing lowering details into the canonical open IR payload.</li>
</ul>

<hr/>

<h2 id="schema-family">10. Schema Family</h2>

<p>
The base v0.1 IR schema family is rooted in:
</p>

<ul>
  <li><code>IR/schema/frog.execution-ir.schema.json</code></li>
</ul>

<p>
That file is the primary machine-checkable schema artifact for the canonical Execution IR Document in base v0.1.
</p>

<p>
Future versions MAY introduce:
</p>

<ul>
  <li>versioned schema families,</li>
  <li>split component schemas,</li>
  <li>referenced sub-schemas,</li>
  <li>later schema bundles for future IR evolution.</li>
</ul>

<p>
For base v0.1, the posture remains conservative:
</p>

<ul>
  <li>one primary schema artifact,</li>
  <li>one canonical document family,</li>
  <li>one execution-unit model at the open boundary.</li>
</ul>

<hr/>

<h2 id="top-level-document-categories">11. Top-Level Document Categories</h2>

<p>
At the top level, the canonical JSON IR document MUST expose a document-level identity boundary and an execution-unit carrier compatible with the published schema family.
</p>

<p>
The top-level posture exists so that:
</p>

<ul>
  <li>the IR artifact is identifiable as one canonical document,</li>
  <li>the execution-bearing content is grouped as one explicit unit in base v0.1,</li>
  <li>document identity remains distinct from unit identity,</li>
  <li>later tooling can reason about the document as an artifact rather than only about anonymous arrays.</li>
</ul>

<p>
A conforming implementation MUST NOT collapse document identity and execution-unit identity into one ambiguous structural role if the published schema version keeps them distinct.
</p>

<hr/>

<h2 id="execution-unit-categories">12. Execution Unit Categories</h2>

<p>
The execution unit is the principal structural container of canonical execution-facing content.
</p>

<p>
In base v0.1, the machine-checkable posture requires that the execution unit carry explicit major categories including:
</p>

<ul>
  <li><code>objects</code>,</li>
  <li><code>connections</code>,</li>
  <li><code>regions</code>,</li>
  <li><code>source_map</code>,</li>
  <li><code>correspondence</code>.</li>
</ul>

<p>
This posture matters because it prevents accidental collapse of:
</p>

<ul>
  <li>execution-facing objects,</li>
  <li>execution-facing relations,</li>
  <li>region-owned structure,</li>
  <li>source attribution support,</li>
  <li>recoverable correspondence support.</li>
</ul>

<p>
These categories are therefore not optional conveniences.
At the schema boundary in base v0.1, they are part of the canonical structural surface.
</p>

<hr/>

<h2 id="object-category-posture">13. Object Category Posture</h2>

<p>
Objects are the primary execution-facing carriers inside the execution unit.
</p>

<p>
The schema posture for objects exists to ensure that canonical JSON IR can express:
</p>

<ul>
  <li>execution-facing identity,</li>
  <li>object family classification,</li>
  <li>typed interface or equivalent terminal structure,</li>
  <li>object-local metadata where permitted,</li>
  <li>compatibility with attribution and correspondence references where relevant.</li>
</ul>

<p>
The schema MAY validate object-level category fields, enum values, and required record structure.
</p>

<p>
However, the schema does not by itself prove that the chosen object family is semantically correct.
That remains downstream from validated meaning and derivation law.
</p>

<p>
The posture rule is:
</p>

<pre><code>object structure
   is schema-validated

object meaning
   is not created by schema</code></pre>

<hr/>

<h2 id="connection-category-posture">14. Connection Category Posture</h2>

<p>
Connections are execution-facing relation carriers.
</p>

<p>
The schema posture for connections exists so that canonical JSON IR can machine-check:
</p>

<ul>
  <li>that connection records exist explicitly,</li>
  <li>that endpoint-related structure is present in the expected schema-owned form,</li>
  <li>that connection identity and metadata posture are structurally consistent where published.</li>
</ul>

<p>
The schema does not by itself prove that every connection preserves the deeper architectural distinction between:
</p>

<ul>
  <li>ordinary connectivity,</li>
  <li>public-interface-boundary participation,</li>
  <li>structure-boundary participation,</li>
  <li>explicit state participation,</li>
  <li>explicit UI sequencing.</li>
</ul>

<p>
That distinction remains governed by derivation and identity law.
The schema only validates the structural carrier boundary that makes such distinctions expressible and inspectable.
</p>

<hr/>

<h2 id="region-category-posture">15. Region Category Posture</h2>

<p>
Regions are explicit structural carriers needed for structured execution forms.
</p>

<p>
The schema posture for regions exists so that canonical JSON IR can machine-check:
</p>

<ul>
  <li>the existence of explicit region records,</li>
  <li>their identity-bearing structure,</li>
  <li>their place inside the execution unit,</li>
  <li>their compatibility with structure-owned execution families.</li>
</ul>

<p>
The schema does not by itself prove that structure ownership, boundary roles, or terminal roles are semantically correct.
Those remain governed by validated meaning, derivation rules, and recoverability law.
</p>

<p>
The posture rule is:
</p>

<pre><code>region record presence
   is schema-checkable

correct structured-control meaning
   is not created by schema alone</code></pre>

<hr/>

<h2 id="source-map-and-correspondence-posture">16. Source Map and Correspondence Posture</h2>

<p>
The schema MUST validate explicit categories for attribution and recoverable correspondence support.
</p>

<p>
In base v0.1, these appear as:
</p>

<ul>
  <li><code>source_map</code></li>
  <li><code>correspondence</code></li>
</ul>

<p>
The preferred base v0.1 posture is explicit record arrays for both categories.
That keeps the canonical JSON form:
</p>

<ul>
  <li>simple,</li>
  <li>portable,</li>
  <li>diffable,</li>
  <li>straightforward to inspect with ordinary JSON tooling.</li>
</ul>

<p>
This posture also prevents a common failure mode:
</p>

<pre><code>execution objects exist
but
attribution and non-primary correspondence are only implicit
or
buried in implementation-private conventions</code></pre>

<p>
The schema therefore supports a canonical JSON IR where attribution and correspondence are visible as first-class structural categories rather than inferred after the fact.
</p>

<hr/>

<h2 id="identity-and-recoverability-posture">17. Identity and Recoverability Posture</h2>

<p>
Schema posture must remain compatible with the stronger identity and recoverability law of the IR layer.
</p>

<p>
This means the schema-owned JSON boundary SHOULD support explicit or equivalent structural carriers for:
</p>

<ul>
  <li>document identity,</li>
  <li>execution-unit identity,</li>
  <li>object identity,</li>
  <li>connection identity where published,</li>
  <li>region identity where published,</li>
  <li>source attribution records,</li>
  <li>correspondence records.</li>
</ul>

<p>
The schema does not need to encode every semantic explanation.
It does need to keep the canonical JSON form structurally capable of carrying the recoverability surface required by the open IR boundary.
</p>

<p>
Accordingly, a schema evolution MUST NOT simplify the JSON form by erasing the structural possibility of:
</p>

<ul>
  <li>attribution,</li>
  <li>non-primary correspondence,</li>
  <li>document-versus-unit identity,</li>
  <li>explicit object / connection / region categorization.</li>
</ul>

<hr/>

<h2 id="schema-validity-versus-architectural-validity">18. Schema Validity Versus Architectural Validity</h2>

<p>
This distinction is critical.
</p>

<p>
A payload may be:
</p>

<ul>
  <li>schema-valid but architecturally insufficient,</li>
  <li>schema-valid but derivation-wrong,</li>
  <li>schema-valid but attribution-poor in ways that only deeper specification checks can detect,</li>
  <li>schema-valid but not acceptable for a later backend corridor because upstream distinctions were already lost.</li>
</ul>

<p>
Conversely, a conceptually intended IR may be architecturally plausible but still fail the canonical JSON schema if required structural carriers are missing.
</p>

<p>
Therefore:
</p>

<pre><code>architectural law
   is broader than
schema law

schema law
   is stricter than
informal JSON convenience

schema-valid
   is necessary
but not sufficient
for full canonical IR correctness</code></pre>

<p>
This section must remain explicit because the repository now already uses conformance material to distinguish not only semantic rejection, but also IR architectural preservation and schema-valid versus architecturally valid outcomes.
</p>

<hr/>

<h2 id="forbidden-misreadings">19. Forbidden Misreadings</h2>

<p>
The following interpretations are forbidden:
</p>

<ul>
  <li>“If the JSON validates, the IR is automatically correct in every deeper sense.”</li>
  <li>“The schema replaces derivation law.”</li>
  <li>“The schema replaces identity and mapping law.”</li>
  <li>“The schema may erase attribution and correspondence as long as objects still exist.”</li>
  <li>“The schema may be specialized around one backend family and still define canonical open IR.”</li>
  <li>“The canonical JSON schema may collapse the open IR boundary into a lowered or runtime-private form.”</li>
</ul>

<p>
The correct reading is:
</p>

<pre><code>schema
   validates canonical JSON structure

it does not replace
validated meaning
or derivation
or identity / recoverability
or lowering boundaries</code></pre>

<hr/>

<h2 id="relation-with-lowering-and-backend-contract">20. Relation with Lowering and Backend Contract</h2>

<p>
The schema boundary is upstream from lowering and backend-facing handoff.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>the canonical JSON IR must remain an open IR artifact,</li>
  <li>it must not be prematurely shaped around one backend family,</li>
  <li>it must not encode runtime-private realization as though that were canonical open IR truth,</li>
  <li>it must remain suitable as the machine-checkable output of the canonical IR stage before later specialization.</li>
</ul>

<p>
This matters directly to a future industrial compiler corridor.
A later LLVM-oriented route remains valid only if it starts from a canonical IR boundary that:
</p>

<ul>
  <li>is schema-valid,</li>
  <li>is architecturally valid,</li>
  <li>preserves attribution and recoverability,</li>
  <li>has not already collapsed into backend-private assumptions.</li>
</ul>

<p>
The schema therefore supports the compiler corridor indirectly:
</p>

<pre><code>validated meaning
   -&gt;
canonical open IR
   -&gt;
canonical JSON schema-valid artifact
   -&gt;
later lowering
   -&gt;
backend-facing contract
   -&gt;
LLVM-oriented or other downstream consumer</code></pre>

<p>
The schema does not define LLVM.
It protects the open IR JSON boundary that LLVM-oriented lowering must remain downstream from.
</p>

<hr/>

<h2 id="summary">21. Summary</h2>

<p>
This document defines the schema posture for the canonical JSON Execution IR Document in base v0.1.
</p>

<p>
Its core rules are:
</p>

<ul>
  <li>the published schema artifacts are normative for structural JSON validity,</li>
  <li>the canonical JSON IR boundary remains explicit and category-oriented,</li>
  <li>the execution unit carries explicit structural categories including objects, connections, regions, source_map, and correspondence,</li>
  <li>schema validity is necessary but not sufficient for full canonical IR correctness,</li>
  <li>schema posture must remain aligned with derivation, identity, recoverability, construction, and later lowering boundaries.</li>
</ul>

<p>
The canonical JSON Execution IR is therefore a real public artifact:
</p>

<ul>
  <li>machine-checkable,</li>
  <li>portable,</li>
  <li>inspectable,</li>
  <li>stable enough for conformance and tooling,</li>
  <li>still distinct from lowered form and backend-private realization.</li>
</ul>

<p>
As the repository moves toward a more industrial compilation corridor, this document keeps the structural JSON boundary honest.
A future LLVM-oriented route may be downstream.
It must still begin from a canonical IR artifact whose JSON shape remains faithful to the open FROG IR boundary.
</p>
