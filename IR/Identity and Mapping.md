<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG IR Identity and Mapping</h1>

<p align="center">
  Normative identity, attribution, and recoverability rules for derived execution-facing IR in FROG v0.1<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#purpose">2. Purpose</a></li>
  <li><a href="#position-in-the-pipeline">3. Position in the Pipeline</a></li>
  <li><a href="#scope-and-non-goals">4. Scope and Non-Goals</a></li>
  <li><a href="#identity-layers">5. Identity Layers</a>
    <ul>
      <li><a href="#source-identity">5.1 Source identity</a></li>
      <li><a href="#validated-semantic-identity">5.2 Validated semantic identity</a></li>
      <li><a href="#ir-identity">5.3 IR identity</a></li>
      <li><a href="#runtime-and-execution-context-identity">5.4 Runtime and execution-context identity</a></li>
    </ul>
  </li>
  <li><a href="#general-mapping-model">6. General Mapping Model</a></li>
  <li><a href="#minimum-preconditions">7. Minimum Preconditions</a></li>
  <li><a href="#required-recoverability">8. Required Recoverability</a></li>
  <li><a href="#mapping-of-ports-connections-and-regions">9. Mapping of Ports, Connections, and Regions</a></li>
  <li><a href="#allowed-normalization">10. Allowed Normalization</a></li>
  <li><a href="#forbidden-transformations">11. Forbidden Transformations</a></li>
  <li><a href="#relation-with-observation-debugging-and-inspection">12. Relation with Observation, Debugging, and Inspection</a></li>
  <li><a href="#minimal-open-shape">13. Minimal Open Shape</a></li>
  <li><a href="#examples">14. Examples</a></li>
  <li><a href="#out-of-scope-for-v01">15. Out of Scope for v0.1</a></li>
  <li><a href="#summary">16. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the normative identity and mapping rules that connect:
</p>

<ul>
  <li>canonical source-visible program objects,</li>
  <li>validated program meaning, and</li>
  <li>derived execution-facing IR objects.</li>
</ul>

<p>
Its role is to ensure that the FROG IR remains:
</p>

<ul>
  <li>source-attributable,</li>
  <li>semantically grounded,</li>
  <li>recoverable for inspection and tooling,</li>
  <li>usable for later lowering without becoming a private runtime representation.</li>
</ul>

<p>
This document does not redefine language semantics.
It defines how identity, attribution, and recoverability MUST remain stable when a validated FROG program is projected into an open execution-facing IR.
</p>

<pre><code>🟩 source-visible identity
        |
        v
🟩 validated program meaning
        |
        v
🟦 execution-facing IR identity
        |
        v
🟧 later specialization
        |
        v
🟥 private realization
</code></pre>

<p>
The normative mapping boundary owned by this document begins at the transition from validated program meaning to open Execution IR.
It does not standardize one private runtime object graph or one target-private identity model.
</p>

<hr/>

<h2 id="purpose">2. Purpose</h2>

<p>
Execution-facing normalization is useful only if implementations and tools can still answer the following questions reliably:
</p>

<ul>
  <li>Which source-visible object does this IR object come from?</li>
  <li>Which validated program meaning does it represent?</li>
  <li>Which distinctions remain recoverable after normalization?</li>
  <li>Which transformations are permitted without destroying attribution?</li>
</ul>

<p>
This document exists to make those answers stable across implementations.
</p>

<p>
In practical terms:
</p>

<pre><code>source object identity
        |
        v
validated program meaning
        |
        v
execution-facing IR identity
        |
        v
later lowering / backend-facing / private forms
</code></pre>

<p>
This document is therefore the identity-side companion of:
</p>

<pre><code>Execution IR.md
   -&gt; what the open IR is

Derivation rules.md
   -&gt; what must correspond

Construction rules.md
   -&gt; how open IR is materially built

Identity and Mapping.md
   -&gt; how attribution and recoverability survive that projection
</code></pre>

<hr/>

<h2 id="position-in-the-pipeline">3. Position in the Pipeline</h2>

<p>
The relevant architectural pipeline is:
</p>

<pre><code>canonical .frog source
        |
        v
Expression/
        |
        v
Program Model or equivalent validated tool form
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
runtime-specific realization
</code></pre>

<p>
Identity and mapping rules apply first at the transition between validated program meaning and Execution IR.
They also constrain what later stages must remain able to recover when specialization continues downstream.
</p>

<p>
An implementation MAY derive IR from canonical source plus validation results, from a validated Program Model, or from another equivalent validated internal form.
However, the resulting IR MUST remain attributable to validated FROG program meaning rather than to editor-only convenience state.
</p>

<pre><code>🟦 raw or editable form
        |
        v
🟩 validated program meaning
        |
        v
🟨 identity and mapping boundary starts here
        |
        v
🟦 open Execution IR
        |
        v
🟧 lowering
        |
        v
🟨 backend-facing contract
        |
        v
🟥 private realization
</code></pre>

<p>
This document is upstream of lowering and backend contract.
It exists so that later stages can still recover source-aligned identity rather than receiving one opaque execution artifact.
</p>

<hr/>

<h2 id="scope-and-non-goals">4. Scope and Non-Goals</h2>

<p>
This document defines:
</p>

<ul>
  <li>identity layers relevant to source-aligned IR,</li>
  <li>allowed mapping relations between those layers,</li>
  <li>mandatory recoverability requirements,</li>
  <li>identity-related normalization rules,</li>
  <li>identity-related forbidden transformations.</li>
</ul>

<p>
This document does not define:
</p>

<ul>
  <li>the full canonical <code>.frog</code> source schema,</li>
  <li>the full language semantics of execution behavior,</li>
  <li>the full open IR object model in isolation,</li>
  <li>the material payload-construction procedure in full,</li>
  <li>a mandatory runtime scheduler architecture,</li>
  <li>a mandatory debugger protocol,</li>
  <li>a mandatory target-lowering format,</li>
  <li>a mandatory backend-private identity model.</li>
</ul>

<pre><code>This document defines:
🟩 identity continuity
🟩 attribution continuity
🟩 recoverability obligations

This document does not define:
🟦 full source schema
🟩 language semantics
🟦 full IR object model
🟨 construction procedure
🟧 lowering format
🟥 private runtime identity
</code></pre>

<hr/>

<h2 id="identity-layers">5. Identity Layers</h2>

<h3 id="source-identity">5.1 Source identity</h3>

<p>
A source identity is the stable identity of a source-visible program object as defined by the relevant source-facing specifications.
</p>

<p>
Examples of source-visible object families include:
</p>

<ul>
  <li>primitive nodes,</li>
  <li>structure objects,</li>
  <li>sub-FROG invocation objects,</li>
  <li>interface boundary objects,</li>
  <li>widget-value participation objects,</li>
  <li>widget-reference participation objects,</li>
  <li>source-visible connections where applicable.</li>
</ul>

<p>
A source identity MUST refer to an object that remains meaningful from the perspective of canonical authored content, not merely from the perspective of one implementation.
</p>

<h3 id="validated-semantic-identity">5.2 Validated semantic identity</h3>

<p>
A validated semantic identity is the identity of an executable meaning unit after all applicable validation has succeeded.
</p>

<p>
This identity layer exists because:
</p>

<ul>
  <li>a source object may expand into multiple execution-relevant derived objects,</li>
  <li>some execution-relevant distinctions become explicit only after validation,</li>
  <li>some invalid source distinctions disappear because they were never semantically valid.</li>
</ul>

<p>
In v0.1, validated semantic identity MAY remain implicit in a conforming implementation, but the implementation MUST behave as though such an identity layer exists whenever it is needed to preserve recoverability.
</p>

<h3 id="ir-identity">5.3 IR identity</h3>

<p>
An IR identity is the stable identity of an object inside one execution-facing IR unit.
</p>

<p>
IR identities:
</p>

<ul>
  <li>MUST be unique within the containing execution unit,</li>
  <li>MUST remain stable for the lifetime of that IR unit,</li>
  <li>MUST remain attributable to validated program meaning,</li>
  <li>MUST NOT be treated as if they were automatically equal to runtime instance identities.</li>
</ul>

<p>
IR identity is therefore an <strong>open representation identity</strong>, not a live runtime activation identity.
</p>

<h3 id="runtime-and-execution-context-identity">5.4 Runtime and execution-context identity</h3>

<p>
Runtime object identity, live activation identity, and execution-context identity belong to later stages than the base open IR.
</p>

<p>
However, this document imposes one important requirement:
</p>

<ul>
  <li>nothing in the IR identity model MAY make later source-visible runtime attribution impossible.</li>
</ul>

<p>
Accordingly, when a later layer needs to expose source-visible observation, pause, debug-stop, or fault attribution, it MUST remain able to relate dynamic execution contexts back to stable source-visible identity.
</p>

<pre><code>identity layers

🟩 source identity
        |
        v
🟩 validated semantic identity
        |
        v
🟦 IR identity
        |
        v
🟥 runtime / execution-context identity
</code></pre>

<hr/>

<h2 id="general-mapping-model">6. General Mapping Model</h2>

<p>
Every execution-facing IR object MUST be connected to validated program meaning through an explicit or recoverable mapping relation.
</p>

<p>
The base mapping relations are:
</p>

<ul>
  <li><strong>1→1 preservation</strong> — one source-visible object remains one attributable IR object,</li>
  <li><strong>1→n expansion</strong> — one source-visible object yields multiple attributable IR objects,</li>
  <li><strong>n→1 restricted aggregation</strong> — multiple source-visible contributors yield one IR support object, but all relevant contributors remain recoverable,</li>
  <li><strong>derived support object</strong> — an IR object is introduced by normalization but remains attributable to one or more validated source-visible contributors.</li>
</ul>

<p>
The mapping model can be summarized as:
</p>

<pre><code>source-visible object(s)
        |
        | validation and semantic resolution
        v
validated program meaning
        |
        | conservative execution-facing projection
        v
IR object(s)
</code></pre>

<p>
For every IR object, an implementation MUST preserve enough information to determine:
</p>

<ul>
  <li>which validated meaning it represents,</li>
  <li>which source-visible object or objects contributed to it,</li>
  <li>whether it is preserved, expanded, restrictedly aggregated, or introduced as a derived support object.</li>
</ul>

<p>
When multiple source-visible contributors exist, an implementation MAY designate one contributor as primary for convenience, but all semantically relevant contributors MUST remain recoverable.
</p>

<pre><code>mapping relations

1 → 1   preserved object
1 → n   expanded object family
n → 1   restricted support aggregation only
n → n   allowed only if contributor attribution remains recoverable
</code></pre>

<p>
The guiding rule is simple:
</p>

<pre><code>normalization MAY increase explicitness
normalization MUST NOT destroy recoverability
</code></pre>

<hr/>

<h2 id="minimum-preconditions">7. Minimum Preconditions</h2>

<p>
Identity-preserving IR construction begins only after the program has been validated according to the applicable FROG specifications.
</p>

<p>
At minimum, that includes:
</p>

<ul>
  <li>structural validation,</li>
  <li>type validation,</li>
  <li>primitive and structure-family validation,</li>
  <li>cycle-validity validation,</li>
  <li>all other applicable v0.1 validation rules.</li>
</ul>

<p>
No implementation may justify identity loss by claiming that missing validation made attribution impossible.
If validation has not completed, the object is not yet part of the standardized Execution IR boundary.
</p>

<pre><code>No completed validation
        |
        v
No conforming identity-preserving open IR claim
</code></pre>

<hr/>

<h2 id="required-recoverability">8. Required Recoverability</h2>

<p>
The following distinctions MUST remain recoverable from the base open IR of v0.1.
</p>

<h3>8.1 Public interface boundaries</h3>

<ul>
  <li><code>interface_input</code> participation MUST remain distinguishable from all other boundary families.</li>
  <li><code>interface_output</code> participation MUST remain distinguishable from all other boundary families.</li>
  <li>Public API boundaries MUST NOT be collapsed into generic data ingress/egress objects with no recoverable source meaning.</li>
</ul>

<h3>8.2 Front-panel value vs object access</h3>

<ul>
  <li><code>widget_value</code> participation MUST remain distinguishable from public interface participation.</li>
  <li><code>widget_reference</code> participation MUST remain distinguishable from ordinary valueflow participation.</li>
  <li>Object-style widget interaction through <code>frog.ui.*</code> MUST remain recoverable as object-style interaction.</li>
</ul>

<h3>8.3 Structured control</h3>

<ul>
  <li>Structure family identity MUST remain recoverable.</li>
  <li>Region ownership MUST remain recoverable.</li>
  <li>Boundary terminals introduced by structured control MAY be made more explicit, but structure correspondence MUST remain traceable.</li>
</ul>

<h3>8.4 Explicit local memory and cycles</h3>

<ul>
  <li>Explicit local-memory primitives such as <code>frog.core.delay</code> MUST remain explicitly attributable.</li>
  <li>A valid stateful feedback path MUST remain recoverable as an explicitly stateful path.</li>
  <li>An invalid combinational cycle MUST NOT become indistinguishable from a valid stateful cycle through IR rewriting.</li>
</ul>

<h3>8.5 Invocation boundaries</h3>

<ul>
  <li>Sub-FROG invocation identity MUST remain recoverable as invocation identity.</li>
  <li>An invocation MUST NOT be flattened so aggressively that cross-boundary provenance becomes unrecoverable in the base open IR.</li>
</ul>

<pre><code>Required recoverability

🟨 interface_input / interface_output remain distinct
🟦 widget_value / widget_reference remain distinct
🟦 structure family and regions remain distinct
🟩 explicit memory remains explicit
🟦 invocation identity remains recoverable
</code></pre>

<hr/>

<h2 id="mapping-of-ports-connections-and-regions">9. Mapping of Ports, Connections, and Regions</h2>

<p>
Identity and attribution rules apply not only to executable objects but also to execution-relevant relationships.
</p>

<h3>9.1 Ports</h3>

<ul>
  <li>An IR port MUST remain attributable to the validated executable object that owns it.</li>
  <li>If validation resolves direction or type information, the IR MAY make that information explicit.</li>
  <li>A normalized IR port MUST remain connected to the source-visible or semantically validated port role from which it originates.</li>
</ul>

<h3>9.2 Connections</h3>

<ul>
  <li>An IR connection MUST remain attributable to validated dependency meaning.</li>
  <li>Connection normalization MAY rewrite representation details, but MUST NOT silently reverse dependency meaning or erase relevant source correspondence.</li>
  <li>When multiple source-visible elements contribute to one normalized dependency relation, their contribution MUST remain recoverable.</li>
</ul>

<h3>9.3 Regions</h3>

<ul>
  <li>Region objects MAY be introduced or made more explicit in the IR.</li>
  <li>Every region object MUST remain attributable to the structure and region semantics from which it was derived.</li>
  <li>Region identity MUST remain sufficient to support structure-aware inspection and later safe observation semantics.</li>
</ul>

<pre><code>relationship mapping

object
  ├── port ownership remains recoverable
  ├── connection meaning remains recoverable
  └── region ownership remains recoverable
</code></pre>

<hr/>

<h2 id="allowed-normalization">10. Allowed Normalization</h2>

<p>
The following transformations are allowed in the base open IR, provided that attribution and recoverability remain intact:
</p>

<ul>
  <li>making resolved port direction explicit,</li>
  <li>making resolved port type explicit,</li>
  <li>making region ownership explicit,</li>
  <li>making structure boundary terminals explicit,</li>
  <li>materializing execution-relevant helper objects,</li>
  <li>using implementation-specific IR identifiers instead of source identifiers,</li>
  <li>canonicalizing equivalent execution-facing spellings,</li>
  <li>separating one source-visible object into multiple attributable IR objects when needed for analysis or later lowering.</li>
</ul>

<p>
Allowed normalization does not remove the obligation to preserve attribution.
</p>

<pre><code>Allowed normalization

✔ make already-validated distinctions explicit
✔ introduce attributable support objects
✔ use implementation-local IR identifiers
✔ expand one source object into several attributable IR objects

Only if:
🟩 contributor attribution remains recoverable
🟩 validated meaning remains preserved
🟩 critical distinctions remain recoverable
</code></pre>

<hr/>

<h2 id="forbidden-transformations">11. Forbidden Transformations</h2>

<p>
The following transformations are forbidden in the base open IR of v0.1:
</p>

<ul>
  <li>removing source attribution for execution-visible objects,</li>
  <li>collapsing multiple independently attributable source-visible primary execution objects into one opaque generated object,</li>
  <li>converting explicit local memory into hidden implicit scheduler state,</li>
  <li>erasing the distinction between public interface boundaries and front-panel value boundaries,</li>
  <li>erasing the distinction between widget-value participation and widget-reference participation,</li>
  <li>flattening structured control so aggressively that structure family, region attribution, or semantic correspondence is no longer recoverable,</li>
  <li>turning editor-only layout or presentation choices into identity-bearing execution semantics,</li>
  <li>treating one private runtime object graph as the normative meaning of the open IR.</li>
</ul>

<pre><code>Forbidden identity loss

🟥 lost attribution
🟥 opaque primary-object collapse
🟥 hidden implicit memory
🟥 collapsed interface / UI roles
🟥 unrecoverable structured flattening
🟥 editor-only execution identity
🟥 private runtime graph as open IR
</code></pre>

<hr/>

<h2 id="relation-with-observation-debugging-and-inspection">12. Relation with Observation, Debugging, and Inspection</h2>

<p>
This document does not define debugger commands or live runtime protocols.
</p>

<p>
However, identity and mapping rules are intentionally written so that later observation and debugging layers can remain source-faithful.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>source-visible observation MUST remain relatable to stable source-visible identity,</li>
  <li>when dynamic disambiguation is required, later layers MUST be able to relate a live execution context back to stable source-visible identity,</li>
  <li>IR normalization MUST NOT destroy the information needed for structure-aware inspection, local-memory inspection, or boundary-aware observation.</li>
</ul>

<p>
The base open IR is therefore not a debugger trace, but it MUST remain suitable as an attribution foundation for later inspection-facing projections.
</p>

<pre><code>🟦 open IR
   is not
🟥 debugger trace

🟦 open IR
   must remain usable as
🟩 attribution foundation
for later observability and debugging layers
</code></pre>

<hr/>

<h2 id="minimal-open-shape">13. Minimal Open Shape</h2>

<p>
This document does not freeze one mandatory transport schema for all implementations.
</p>

<p>
However, a conforming base open IR representation SHOULD preserve information equivalent to the following conceptual shape:
</p>

<pre><code>{
  "execution_unit_id": "main",
  "objects": [
    {
      "ir_id": "obj_001",
      "kind": "primitive",
      "mapping_relation": "1_to_1",
      "semantic_identity": {
        "kind": "validated_object",
        "id": "sem.mul_1"
      },
      "source_attribution": {
        "primary": [
          { "layer": "diagram", "object_id": "mul_1" }
        ],
        "contributors": []
      }
    }
  ]
}
</code></pre>

<p>
For v0.1, the exact field names are illustrative rather than mandatory.
</p>

<p>
What is mandatory is the presence of information equivalent to:
</p>

<ul>
  <li>a stable IR identity,</li>
  <li>object classification,</li>
  <li>mapping relation category,</li>
  <li>validated semantic correspondence,</li>
  <li>recoverable source attribution.</li>
</ul>

<pre><code>Minimal identity intent

🟦 IR identity
🟦 object classification
🟩 semantic correspondence
🟩 source attribution
</code></pre>

<hr/>

<h2 id="examples">14. Examples</h2>

<h3>14.1 Direct preservation</h3>

<p>
A validated <code>interface_input</code> object may remain one recognizable IR boundary object.
</p>

<pre><code>source:
  interface_input("a")

validated meaning:
  public input boundary for interface port "a"

IR:
  boundary_object(kind="interface_input", source="a-node")
</code></pre>

<p>
This is a 1→1 preservation relation.
</p>

<h3>14.2 One source object expanded into several IR objects</h3>

<p>
A structured-control object may be projected into:
</p>

<ul>
  <li>one structure object,</li>
  <li>one or more region objects,</li>
  <li>explicit structure-boundary terminal objects.</li>
</ul>

<pre><code>source:
  for_loop(loop_1)

IR:
  structure(loop_1)
  region(loop_1.body)
  boundary_input(loop_1.N)
  boundary_output(loop_1.result)
</code></pre>

<p>
This is a 1→n expansion relation.
All derived objects MUST remain attributable to the original validated structure meaning.
</p>

<h3>14.3 Derived support object</h3>

<p>
An implementation may introduce an explicit helper object to make a validated boundary rule execution-facing.
</p>

<p>
Such an object is allowed only if:
</p>

<ul>
  <li>it remains attributable,</li>
  <li>it does not become opaque,</li>
  <li>it does not silently replace the semantic identity of the validated object it supports.</li>
</ul>

<h3>14.4 Restricted aggregation</h3>

<p>
Multiple validated contributors MAY feed one derived support object when that support object exists only to make already-validated execution-facing structure explicit.
</p>

<pre><code>source contributors:
  structure(loop_1)
  region(loop_1.body)

IR support object:
  region_membership_record(loop_1.body.membership)

Requirement:
  contributors to both loop_1 and loop_1.body remain recoverable
</code></pre>

<p>
This is not permission to collapse multiple primary execution-visible objects into one opaque replacement object.
</p>

<hr/>

<h2 id="out-of-scope-for-v01">15. Out of Scope for v0.1</h2>

<p>
The following topics remain out of scope for this document in v0.1:
</p>

<ul>
  <li>a mandatory serialized semantic-identity schema,</li>
  <li>a mandatory global identity namespace across all future IR families,</li>
  <li>a mandatory runtime execution-context schema,</li>
  <li>a mandatory debugger-stop attribution payload format,</li>
  <li>a mandatory target-lowering identity contract,</li>
  <li>a mandatory backend-private identity model.</li>
</ul>

<p>
Those topics may be refined later by stricter IR, lowering, backend-contract, observability, or conformance documents.
</p>

<pre><code>Out of scope in v0.1

🟨 one mandatory serialized semantic-identity schema
🟨 one mandatory global cross-family namespace
🟥 one mandatory runtime execution-context schema
🟨 one mandatory debugger-stop attribution payload
🟧 one mandatory lowering identity contract
🟥 one mandatory backend-private identity model
</code></pre>

<hr/>

<h2 id="summary">16. Summary</h2>

<p>
FROG v0.1 requires identity-preserving open IR.
A conforming open Execution IR MUST remain able to answer:
</p>

<ul>
  <li>which source-visible contributors are involved,</li>
  <li>which validated program meaning is represented,</li>
  <li>which IR object now carries that execution-facing role,</li>
  <li>which distinctions remain recoverable after normalization.</li>
</ul>

<p>
This document therefore preserves the attribution foundation needed by:
</p>

<ul>
  <li>open Execution IR inspection,</li>
  <li>safe later lowering,</li>
  <li>source-aligned observability,</li>
  <li>future debugging and diagnostics.</li>
</ul>

<pre><code>🟩 source-visible identity
        |
        v
🟩 validated program meaning
        |
        v
🟦 recoverable execution-facing IR identity
        |
        v
🟧 later specialization without attribution loss
</code></pre>
