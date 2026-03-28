<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Execution IR Schema</h1>

<p align="center">
  <strong>Schema posture and machine-checkable validation surface for the canonical FROG Execution IR Document</strong><br />
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr />

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-document-exists">2. Why this Document Exists</a></li>
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
  <li><a href="#extensibility-posture">17. Extensibility Posture</a></li>
  <li><a href="#validation-usage">18. Validation Usage</a></li>
  <li><a href="#conformance-reading-rule">19. Conformance Reading Rule</a></li>
  <li><a href="#out-of-scope">20. Out of Scope</a></li>
  <li><a href="#summary">21. Summary</a></li>
</ul>

<hr />

<h2 id="overview">1. Overview</h2>

<p>
This document defines the schema posture for the <strong>canonical FROG Execution IR Document</strong> in base v0.1.
</p>

<p>
The Execution IR is not only an architectural layer.
It is also a canonical open artifact that a conforming implementation MUST be able to emit as JSON.
This document defines how that canonical JSON form is machine-checkable.
</p>

<p>
Accordingly, the IR schema exists to provide:
</p>

<ul>
  <li>a public validation surface for the canonical Execution IR Document,</li>
  <li>a stable machine-checkable structural contract for tools and tests,</li>
  <li>a portable baseline for inspection, caching, comparison, and conformance checking,</li>
  <li>a schema boundary that remains upstream of lowering and runtime-private realization.</li>
</ul>

<pre><code>validated program meaning
      -&gt;
canonical Execution IR Document
      -&gt;
canonical JSON serialization
      -&gt;
schema validation
      -&gt;
later lowering / specialization
</code></pre>

<hr />

<h2 id="why-this-document-exists">2. Why this Document Exists</h2>

<p>
Without a schema surface, a canonical JSON requirement remains incomplete.
Tools may agree that a canonical JSON form exists while still disagreeing about:
</p>

<ul>
  <li>which top-level categories are mandatory,</li>
  <li>which category names are stable,</li>
  <li>how one execution unit is represented,</li>
  <li>how objects, connections, regions, attribution, and correspondence are carried,</li>
  <li>which structural mistakes count as invalid emitted IR.</li>
</ul>

<p>
This document exists to prevent that ambiguity.
It makes the Execution IR boundary not only architecturally defined, but also <strong>machine-checkable</strong>.
</p>

<p>
In other words:
</p>

<pre><code>Execution IR.md
   -&gt; what the canonical open IR is

Construction rules.md
   -&gt; how the canonical open IR document is built

Schema.md
   -&gt; how the canonical JSON form is validated structurally
</code></pre>

<hr />

<h2 id="scope">3. Scope</h2>

<p>
This document defines:
</p>

<ul>
  <li>the role of the IR schema in the FROG stack,</li>
  <li>the normative posture of the machine-checkable schema,</li>
  <li>the relationship between architectural IR and canonical JSON payload validation,</li>
  <li>the structural categories that a conforming canonical IR document must expose,</li>
  <li>the intended validation boundary of the schema artifacts published in <code>IR/schema/</code>.</li>
</ul>

<p>
This document does <strong>not</strong> define:
</p>

<ul>
  <li>the semantic meaning of FROG programs,</li>
  <li>the derivation obligations from source to IR,</li>
  <li>the full procedural build rules for constructing IR documents,</li>
  <li>the complete identity and mapping contract,</li>
  <li>lowering rules,</li>
  <li>backend contracts,</li>
  <li>runtime-private representations.</li>
</ul>

<hr />

<h2 id="relation-with-other-ir-documents">4. Relation with Other IR Documents</h2>

<p>
The ownership split is:
</p>

<ul>
  <li><code>Execution IR.md</code> defines the architectural identity of the canonical open IR.</li>
  <li><code>Construction rules.md</code> defines how a conforming canonical IR document is built.</li>
  <li><code>Derivation rules.md</code> defines what must correspond between validated meaning and IR content.</li>
  <li><code>Identity and Mapping.md</code> defines recoverability and cross-layer identity obligations.</li>
  <li><code>Schema.md</code> defines the posture of machine-checkable structural validation for the canonical JSON IR form.</li>
  <li><code>IR/schema/</code> contains the actual machine-checkable schema artifacts.</li>
</ul>

<p>
This document therefore MUST be read as a schema companion to the architectural and construction material rather than as a replacement for them.
</p>

<pre><code>Architecture
   -&gt; Execution IR.md

Construction
   -&gt; Construction rules.md

Schema posture
   -&gt; Schema.md

Machine-checkable schema
   -&gt; IR/schema/
</code></pre>

<hr />

<h2 id="normative-posture">5. Normative Posture</h2>

<p>
The schema artifacts published in <code>IR/schema/</code> are <strong>normative for structural validation of the canonical JSON Execution IR Document</strong>.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>a conforming implementation MUST be able to emit a canonical JSON Execution IR Document that satisfies the published schema,</li>
  <li>a payload that fails the published schema MUST NOT be claimed as a schema-valid canonical Execution IR Document for that schema version,</li>
  <li>schema validity alone does not imply full semantic validity,</li>
  <li>schema compliance must be interpreted together with the rest of the IR and Language specifications.</li>
</ul>

<p>
The schema is therefore:
</p>

<ul>
  <li>normative for structural form,</li>
  <li>not sufficient by itself for full semantic conformance,</li>
  <li>upstream of lowering and runtime-private realization.</li>
</ul>

<hr />

<h2 id="what-the-schema-validates">6. What the Schema Validates</h2>

<p>
The IR schema validates the structural form of the canonical JSON Execution IR Document.
</p>

<p>
At minimum, that includes:
</p>

<ul>
  <li>top-level document classification,</li>
  <li>IR version presence,</li>
  <li>document identity presence,</li>
  <li>presence of exactly one execution unit category in base v0.1,</li>
  <li>presence and structural category of objects,</li>
  <li>presence and structural category of connections,</li>
  <li>presence and structural category of regions,</li>
  <li>presence and structural category of source attribution support,</li>
  <li>presence and structural category of correspondence support,</li>
  <li>basic required fields for category-level validation.</li>
</ul>

<p>
The schema may also validate selected enumerated families, required arrays, required maps, and basic identifier-bearing records where the schema layer publishes them explicitly.
</p>

<hr />

<h2 id="what-the-schema-does-not-validate">7. What the Schema Does Not Validate</h2>

<p>
The IR schema does not replace semantic validation.
Even when a payload is schema-valid, the following may still require separate validation logic:
</p>

<ul>
  <li>type meaning beyond structural encoding,</li>
  <li>primitive legality,</li>
  <li>structure-family semantic legality,</li>
  <li>cycle validity,</li>
  <li>port-type compatibility,</li>
  <li>region behavior legality,</li>
  <li>full recoverability obligations,</li>
  <li>lowering legality,</li>
  <li>backend-specific requirements.</li>
</ul>

<pre><code>schema-valid
   !=
semantically valid by itself

schema-valid
   !=
lowering-ready by itself

schema-valid
   !=
runtime-private correctness proof
</code></pre>

<hr />

<h2 id="canonical-document-boundary">8. Canonical Document Boundary</h2>

<p>
The schema validates the <strong>canonical Execution IR Document</strong> at the open IR boundary.
</p>

<p>
It does not validate:
</p>

<ul>
  <li>the canonical <code>.frog</code> source,</li>
  <li>the IDE Program Model,</li>
  <li>private in-memory compiler forms,</li>
  <li>private scheduler graphs,</li>
  <li>backend-private lowered forms,</li>
  <li>runtime-private execution artifacts.</li>
</ul>

<p>
This boundary is important.
The schema protects the open IR surface from being silently replaced by implementation-private payloads.
</p>

<hr />

<h2 id="canonical-json-posture">9. Canonical JSON Posture</h2>

<p>
The canonical open wire format of the Execution IR is JSON.
The schema published in <code>IR/schema/</code> validates that canonical JSON form.
</p>

<p>
This does <strong>not</strong> mean that implementations must use JSON internally.
It means that:
</p>

<ul>
  <li>the open conformance-visible emitted form is canonical JSON,</li>
  <li>the schema validates that emitted form,</li>
  <li>private internal forms remain allowed but non-normative at the open IR boundary.</li>
</ul>

<pre><code>internal implementation form
      MAY differ

canonical open IR form
      MUST be JSON

IR/schema/
      validates that canonical JSON form
</code></pre>

<hr />

<h2 id="schema-family">10. Schema Family</h2>

<p>
The base v0.1 IR schema family is rooted in:
</p>

<ul>
  <li><code>IR/schema/frog.execution-ir.schema.json</code></li>
</ul>

<p>
That file is the primary machine-checkable schema artifact for the canonical Execution IR Document in base v0.1.
Future versions MAY add:
</p>

<ul>
  <li>versioned schema families,</li>
  <li>split component schemas,</li>
  <li>referenced sub-schemas,</li>
  <li>future schema bundles for later IR evolution.</li>
</ul>

<p>
For base v0.1, the preferred posture is conservative:
</p>

<ul>
  <li>one primary schema artifact,</li>
  <li>one canonical document family,</li>
  <li>one execution-unit model at the open boundary.</li>
</ul>

<hr />

<h2 id="top-level-document-categories">11. Top-Level Document Categories</h2>

<p>
At the top level, the schema MUST validate a document equivalent in category to:
</p>

<ul>
  <li><code>ir_version</code></li>
  <li><code>kind</code></li>
  <li><code>document_id</code></li>
  <li><code>unit</code></li>
</ul>

<p>
These categories exist to guarantee that the payload is clearly:
</p>

<ul>
  <li>identified as IR,</li>
  <li>versioned,</li>
  <li>document-addressable,</li>
  <li>rooted in a single execution-unit container.</li>
</ul>

<p>
A payload lacking those top-level categories MUST NOT be treated as a conforming canonical Execution IR Document for base v0.1.
</p>

<hr />

<h2 id="execution-unit-categories">12. Execution Unit Categories</h2>

<p>
Within the top-level document, the schema MUST validate one execution unit category containing at minimum:
</p>

<ul>
  <li><code>id</code></li>
  <li><code>objects</code></li>
  <li><code>connections</code></li>
  <li><code>regions</code></li>
  <li><code>source_map</code></li>
  <li><code>correspondence</code></li>
</ul>

<p>
Those categories define the minimum published structural surface of the open Execution IR in base v0.1.
</p>

<p>
Equivalent richer shapes may exist only if they remain compatible with the schema family and do not erase those structural responsibilities.
</p>

<hr />

<h2 id="object-category-posture">13. Object Category Posture</h2>

<p>
The schema MUST validate that the execution unit contains an <code>objects</code> array.
Each object record must be machine-checkable as an identifiable execution-facing object record.
</p>

<p>
At minimum, object validation is expected to cover:
</p>

<ul>
  <li>record identity presence,</li>
  <li>family classification presence,</li>
  <li>port category presence,</li>
  <li>attribution category presence,</li>
  <li>distinguishability of primary versus support role where the schema publishes that distinction.</li>
</ul>

<p>
The schema does not need to flatten all object-family semantics into one file-level prose rule.
Its role is to guarantee stable structural expectations for object records.
</p>

<hr />

<h2 id="connection-category-posture">14. Connection Category Posture</h2>

<p>
The schema MUST validate that the execution unit contains a <code>connections</code> array.
Each connection record must be machine-checkable as an explicit directed connectivity record.
</p>

<p>
At minimum, connection validation is expected to cover:
</p>

<ul>
  <li>connection identity presence,</li>
  <li>source endpoint presence,</li>
  <li>destination endpoint presence,</li>
  <li>basic endpoint structural shape.</li>
</ul>

<p>
This keeps the open IR aligned with the rule that execution-relevant connectivity must remain explicit and inspectable.
</p>

<hr />

<h2 id="region-category-posture">15. Region Category Posture</h2>

<p>
The schema MUST validate that the execution unit contains a <code>regions</code> array.
Each region record must be machine-checkable as a region-bearing record suitable for structured control ownership.
</p>

<p>
At minimum, region validation is expected to cover:
</p>

<ul>
  <li>region identity presence,</li>
  <li>owner reference presence,</li>
  <li>basic membership or equivalent region-local content support.</li>
</ul>

<p>
This protects the rule that structured control remains structured in the open IR rather than being silently flattened away.
</p>

<hr />

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
The schema does not by itself define the full semantics of those records.
It defines the required structural presence of explicit machine-checkable categories so that attribution and non-primary correspondence are not left to undocumented convention.
</p>

<hr />

<h2 id="extensibility-posture">17. Extensibility Posture</h2>

<p>
The schema MAY allow conservative extension points.
However, extensibility must remain subordinate to the canonical open IR boundary.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>extensions MUST NOT remove required canonical categories,</li>
  <li>extensions MUST NOT redefine language meaning,</li>
  <li>extensions MUST NOT smuggle runtime-private scheduler policy into the canonical open surface,</li>
  <li>extensions SHOULD remain additive and execution-relevant,</li>
  <li>extensions SHOULD remain stable enough to preserve inspection and conformance usefulness.</li>
</ul>

<p>
The base schema should therefore remain strict on required structure and conservative on extension freedom.
</p>

<hr />

<h2 id="validation-usage">18. Validation Usage</h2>

<p>
The schema is intended to be used by:
</p>

<ul>
  <li>emitters of canonical Execution IR Documents,</li>
  <li>validators,</li>
  <li>conformance tooling,</li>
  <li>inspection tooling,</li>
  <li>cache integrity tooling,</li>
  <li>future lowering-entry tooling.</li>
</ul>

<p>
Typical use is:
</p>

<pre><code>validated program meaning
      -&gt;
construct canonical Execution IR Document
      -&gt;
emit canonical JSON
      -&gt;
validate against IR schema
      -&gt;
claim schema-valid canonical IR document
</code></pre>

<hr />

<h2 id="conformance-reading-rule">19. Conformance Reading Rule</h2>

<p>
Conformance must be read in layers.
</p>

<ul>
  <li><strong>Schema-valid</strong> means the emitted canonical JSON matches the published machine-checkable structural contract.</li>
  <li><strong>IR-valid</strong> means the document also satisfies the architectural and construction rules of the IR layer.</li>
  <li><strong>Semantically valid</strong> means the program meaning itself satisfies the Language layer.</li>
</ul>

<p>
Therefore:
</p>

<pre><code>semantic validity
   remains owned by Language/

IR architectural validity
   remains owned by IR/Execution IR.md
   and IR/Construction rules.md

schema validity
   is owned by IR/schema/
</code></pre>

<p>
A tool MUST NOT claim that schema validity alone replaces the rest of specification conformance.
</p>

<hr />

<h2 id="out-of-scope">20. Out of Scope</h2>

<p>
The following remain out of scope for this document:
</p>

<ul>
  <li>the full prose semantics of all IR records,</li>
  <li>all future IR versions beyond base v0.1,</li>
  <li>lowering schemas,</li>
  <li>backend contract schemas,</li>
  <li>runtime-private schemas,</li>
  <li>trace, debug, or observability payload schemas.</li>
</ul>

<hr />

<h2 id="summary">21. Summary</h2>

<p>
The FROG IR schema layer makes the canonical Execution IR Document machine-checkable.
It gives the open IR boundary a public structural validation surface that is:
</p>

<ul>
  <li>canonical,</li>
  <li>JSON-based,</li>
  <li>portable,</li>
  <li>conformance-friendly,</li>
  <li>upstream of lowering and runtime-private realization.</li>
</ul>

<p>
Its role is not to replace semantic validation.
Its role is to ensure that the canonical JSON IR artifact has a stable public structural contract.
</p>

<pre><code>architectural IR
      -&gt;
canonical JSON IR document
      -&gt;
machine-checkable schema validation
      -&gt;
portable open IR surface
</code></pre>
