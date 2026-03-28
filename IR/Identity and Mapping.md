<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG IR Identity and Mapping</h1>

<p align="center">
  <strong>Normative identity, attribution, and recoverability rules for the canonical Execution IR Document</strong><br />
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr />

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#boundary-contract">2. Boundary Contract</a></li>
  <li><a href="#scope-of-this-document">3. Scope of this Document</a></li>
  <li><a href="#position-in-the-pipeline">4. Position in the Pipeline</a></li>
  <li><a href="#identity-layers">5. Identity Layers</a></li>
  <li><a href="#general-mapping-model">6. General Mapping Model</a></li>
  <li><a href="#preconditions">7. Preconditions</a></li>
  <li><a href="#required-recoverability">8. Required Recoverability</a></li>
  <li><a href="#mapping-rules">9. Mapping Rules</a></li>
  <li><a href="#document-unit-and-object-identity">10. Document, Unit, and Object Identity</a></li>
  <li><a href="#ports-terminals-connections-and-regions">11. Ports, Terminals, Connections, and Regions</a></li>
  <li><a href="#attribution-and-correspondence-records">12. Attribution and Correspondence Records</a></li>
  <li><a href="#allowed-normalization">13. Allowed Normalization</a></li>
  <li><a href="#forbidden-transformations">14. Forbidden Transformations</a></li>
  <li><a href="#relation-with-schema-construction-lowering-and-backend-contract">15. Relation with Schema, Construction, Lowering, and Backend Contract</a></li>
  <li><a href="#relation-with-observation-and-debugging">16. Relation with Observation and Debugging</a></li>
  <li><a href="#canonical-json-shape-posture">17. Canonical JSON Shape Posture</a></li>
  <li><a href="#examples">18. Examples</a></li>
  <li><a href="#out-of-scope-for-v01">19. Out of Scope for v0.1</a></li>
  <li><a href="#summary">20. Summary</a></li>
</ul>

<hr />

<h2 id="overview">1. Overview</h2>

<p>
This document defines the identity and mapping rules that connect:
</p>

<ul>
  <li>validated source-visible contributors,</li>
  <li>validated program meaning,</li>
  <li>the canonical Execution IR Document,</li>
  <li>execution-facing IR identities inside that document.</li>
</ul>

<p>
Its purpose is to ensure that the canonical open Execution IR remains:
</p>

<ul>
  <li>source-attributable,</li>
  <li>semantically grounded,</li>
  <li>recoverable for inspection and tooling,</li>
  <li>usable for lowering without collapsing into private runtime form.</li>
</ul>

<p>
This document does not define semantic truth.
It defines how identity, attribution, and recoverability MUST survive projection into the canonical Execution IR Document.
</p>

<pre><code>validated source-visible contributors
                |
                v
validated program meaning
                |
                v
canonical Execution IR Document
                |
                v
execution-facing IR identity
                |
                v
lowering / backend contract / private realization
</code></pre>

<hr />

<h2 id="boundary-contract">2. Boundary Contract</h2>

<p>
Every execution-facing IR object MUST be attributable to validated program meaning.
</p>

<p>
Every conforming mapping MUST allow recovery of:
</p>

<ul>
  <li>its validated source-visible contributor or contributors,</li>
  <li>its semantic role,</li>
  <li>its derivation relation,</li>
  <li>its object-family classification where relevant,</li>
  <li>its place inside the canonical Execution IR Document.</li>
</ul>

<p>
Identity is therefore not optional metadata.
It is part of the correctness of the canonical open Execution IR.
</p>

<pre><code>valid canonical IR
   =
correct execution-facing correspondence
   +
recoverable identity
   +
recoverable attribution
</code></pre>

<p>
A conforming implementation MUST NOT treat identity as disposable convenience data that may be dropped once derivation succeeds.
</p>

<hr />

<h2 id="scope-of-this-document">3. Scope of this Document</h2>

<p>
This document defines:
</p>

<ul>
  <li>identity layers relevant to the canonical Execution IR Document,</li>
  <li>mapping relations between validated meaning and IR objects,</li>
  <li>recoverability obligations that MUST survive derivation and construction,</li>
  <li>identity-safe normalization,</li>
  <li>identity-breaking forbidden transformations.</li>
</ul>

<p>
This document does not define:
</p>

<ul>
  <li>the full source schema,</li>
  <li>language semantics in full,</li>
  <li>the complete Execution IR schema text,</li>
  <li>the construction algorithm in full,</li>
  <li>runtime-private identity models.</li>
</ul>

<pre><code>This document defines:
- identity layers relevant to the canonical Execution IR Document
- mapping relations between validated meaning and IR objects
- recoverability obligations
- identity-safe normalization
- forbidden identity-breaking transformations

This document does not define:
- source shape
- language semantics
- the full canonical IR schema text
- construction in full
- runtime-private identity models
</code></pre>

<hr />

<h2 id="position-in-the-pipeline">4. Position in the Pipeline</h2>

<pre><code>source
  |
  v
validation
  |
  v
validated meaning
  |
  v
identity + derivation constraints
  |
  v
canonical Execution IR Document
  |
  v
lowering
  |
  v
backend contract
  |
  v
runtime / backend-private realization
</code></pre>

<p>
Identity rules apply at the derivation boundary and constrain all downstream transformations that still claim semantic faithfulness or source-aligned recoverability.
</p>

<p>
This means:
</p>

<ul>
  <li>derivation MUST establish recoverable open-IR identity,</li>
  <li>construction MUST materialize that identity explicitly enough for canonical open-IR validity,</li>
  <li>schema validation MUST validate the structural carriers of that identity where published,</li>
  <li>lowering MUST preserve required recoverability where later layers still depend on it,</li>
  <li>backend-facing consumption MUST NOT erase required attribution while still claiming faithful consumption.</li>
</ul>

<hr />

<h2 id="identity-layers">5. Identity Layers</h2>

<h3>5.1 Source-visible identity</h3>

<p>
This is the identity of authored or source-owned contributors that participate in validation or later recoverability.
Examples include:
</p>

<ul>
  <li>primitive nodes,</li>
  <li>structure nodes,</li>
  <li>sub-FROG invocation nodes,</li>
  <li>public boundary participation nodes,</li>
  <li>widget participation nodes,</li>
  <li>diagram edges,</li>
  <li>relevant declarations whose identity must remain recoverable.</li>
</ul>

<p>
Source-visible identity reflects authored structure and authored intent as accepted by validation.
</p>

<h3>5.2 Validated semantic identity</h3>

<p>
This is the identity of accepted contributors after validation:
</p>

<ul>
  <li>invalid constructs are excluded,</li>
  <li>roles are resolved,</li>
  <li>type commitments are resolved to the degree required for semantic acceptance,</li>
  <li>execution-relevant distinctions become authoritative.</li>
</ul>

<p>
This layer is authoritative for derivation.
A conforming derivation MUST be grounded in validated identity, not in pre-validation ambiguity.
</p>

<h3>5.3 Canonical Execution IR document identity</h3>

<p>
This is the identity of the top-level canonical Execution IR artifact for one validated FROG program.
</p>

<p>
In base v0.1:
</p>

<ul>
  <li>one validated FROG program yields one canonical Execution IR Document,</li>
  <li>that document carries its own identity,</li>
  <li>that document contains one execution unit.</li>
</ul>

<p>
Document identity is distinct from source identity and distinct from execution-object identity.
It identifies the open IR artifact itself.
</p>

<h3>5.4 Open Execution IR unit and object identity</h3>

<p>
This is the identity of the execution unit and of the objects inside it:
</p>

<ul>
  <li>unique within the relevant document or unit scope,</li>
  <li>stable for the lifetime of that IR instance,</li>
  <li>mapped to validated meaning through explicit correspondence.</li>
</ul>

<p>
IR identity is execution-facing representation identity.
It is not yet runtime activation identity.
</p>

<h3>5.5 Lowered identity</h3>

<p>
Lowering may later introduce additional identities or refined object partitions.
That lowered identity remains downstream from this document, but it MUST respect recoverability obligations inherited from the canonical open IR where later stages still claim faithful mapping.
</p>

<h3>5.6 Runtime or backend-private identity</h3>

<p>
Dynamic execution identity such as activations, instances, handles, retained state cells, or backend-private objects is downstream and out of scope here.
However, when later stages claim source-aligned diagnosability, their private identity models MUST still remain mappable back to the relevant open-IR and source-facing identities.
</p>

<pre><code>source-visible
      -&gt;
validated semantic
      -&gt;
canonical IR document
      -&gt;
execution unit / object identity
      -&gt;
lowered
      -&gt;
runtime / backend-private
</code></pre>

<hr />

<h2 id="general-mapping-model">6. General Mapping Model</h2>

<p>
Base v0.1 allows the following mapping relations:
</p>

<ul>
  <li><strong>1 -&gt; 1</strong> — direct preservation,</li>
  <li><strong>1 -&gt; n</strong> — expansion into one primary object plus support objects,</li>
  <li><strong>n -&gt; 1</strong> — restricted support aggregation with explicit contributor attribution,</li>
  <li><strong>1 -&gt; 0</strong> — non-primary correspondence.</li>
</ul>

<p>
The governing rule is:
</p>

<pre><code>execution-facing explicitness MAY increase
recoverability MUST remain
</code></pre>

<p>
Every execution-facing IR object MUST expose or imply, in a recoverable way:
</p>

<ul>
  <li>its semantic origin,</li>
  <li>its validated source-visible contributor or contributors,</li>
  <li>its mapping relation,</li>
  <li>its object-family role where relevant,</li>
  <li>its owning document and unit relation where relevant.</li>
</ul>

<p>
Restricted aggregation is permitted only when:
</p>

<ul>
  <li>the result is a support object rather than an opaque semantic replacement,</li>
  <li>all contributors remain explicitly attributable,</li>
  <li>the aggregation does not destroy required boundary distinctions.</li>
</ul>

<hr />

<h2 id="preconditions">7. Preconditions</h2>

<p>
Identity-preserving canonical Execution IR requires:
</p>

<ul>
  <li>complete validation for the accepted subset,</li>
  <li>type correctness under the accepted semantic rules,</li>
  <li>structure correctness,</li>
  <li>cycle legality,</li>
  <li>boundary consistency,</li>
  <li>resolved execution-relevant distinctions at the semantic boundary.</li>
</ul>

<pre><code>no validation
    -&gt;
no conforming identity-preserving canonical Execution IR
</code></pre>

<p>
A conforming implementation MUST NOT use open-IR identity to compensate for missing semantic validation upstream.
</p>

<hr />

<h2 id="required-recoverability">8. Required Recoverability</h2>

<p>
The following distinctions MUST remain recoverable whenever present and relevant:
</p>

<ul>
  <li>document identity versus execution-unit identity,</li>
  <li><code>interface_input</code> versus <code>interface_output</code>,</li>
  <li><code>widget_value</code> versus <code>widget_reference</code>,</li>
  <li>standardized UI-object primitive versus widget-reference participation,</li>
  <li>public interface participation versus UI participation,</li>
  <li><code>widget_value</code> participation versus property-based access to member <code>value</code>,</li>
  <li>structure family identity,</li>
  <li>regions and structure-owned boundaries,</li>
  <li>structure-terminal roles,</li>
  <li>explicit local memory identity,</li>
  <li>sub-FROG invocation identity and callable boundary,</li>
  <li>primary versus support versus non-primary roles.</li>
</ul>

<pre><code>recoverability set
    =
minimal invariant surface
for canonical Execution IR correspondence
</code></pre>

<p>
These recoverability requirements are the minimum architectural surface that later lowering, observability, conformance reasoning, and fault attribution must not silently destroy.
</p>

<hr />

<h2 id="mapping-rules">9. Mapping Rules</h2>

<h3>9.1 Objects</h3>

<ul>
  <li>Primary execution-facing objects MUST be directly attributable to validated contributors or validated contributor groups allowed by this specification.</li>
  <li>Support objects MUST be attributable to their contributing validated objects.</li>
  <li>Non-primary source-visible contributors MAY remain outside the set of primary execution objects, but their correspondence obligations MUST remain recoverable where relevant.</li>
</ul>

<h3>9.2 Ports and terminals</h3>

<ul>
  <li>Every explicit port or terminal MUST map to an owning execution-facing object.</li>
  <li>Where relevant, ports and terminals MUST preserve role distinctions such as public boundary, structure boundary, or structure-intrinsic terminal role.</li>
  <li>Support descriptors MAY refine port or terminal classification, but they MUST NOT erase required distinctions.</li>
</ul>

<h3>9.3 Connections</h3>

<ul>
  <li>Directed connections MUST preserve validated dependency meaning.</li>
  <li>Connection attribution MUST remain recoverable through attributable endpoints and, where needed, explicit connection identity.</li>
  <li>Cross-boundary connections MUST preserve enough information to recover the relevant boundary relation.</li>
</ul>

<h3>9.4 Regions</h3>

<ul>
  <li>Region objects MUST preserve ownership by their structure object.</li>
  <li>Region-local content MUST preserve its region relation.</li>
  <li>A conforming derivation MUST NOT allow region-local content to become detached from region identity when region identity remains relevant to semantics or later diagnostics.</li>
</ul>

<h3>9.5 State-bearing objects</h3>

<ul>
  <li>Explicit state-bearing contributors MUST map to attributable explicit state-bearing IR identity.</li>
  <li>Required explicit initialization MUST remain recoverable.</li>
  <li>State-bearing identity MUST remain distinguishable from ordinary transient dataflow identity.</li>
</ul>

<h3>9.6 UI participation</h3>

<ul>
  <li>UI-related participation objects MUST preserve their semantic role distinctions.</li>
  <li>Widget declarations referenced by participation objects MUST remain recoverably linked to those participation objects.</li>
  <li>Standardized UI-object primitive operations MUST remain distinct from both widget declaration identity and widget-reference participation identity.</li>
</ul>

<hr />

<h2 id="document-unit-and-object-identity">10. Document, Unit, and Object Identity</h2>

<p>
The canonical Execution IR identity model in base v0.1 has at least three open-IR levels:
</p>

<ul>
  <li><strong>document identity</strong> — the identity of the canonical Execution IR Document,</li>
  <li><strong>unit identity</strong> — the identity of the single execution unit contained in that document,</li>
  <li><strong>object identity</strong> — the identity of execution-facing objects inside that unit.</li>
</ul>

<p>
Accordingly:
</p>

<ul>
  <li>every canonical Execution IR Document MUST carry a document identity,</li>
  <li>every execution unit MUST carry a unit identity,</li>
  <li>every execution-visible object MUST carry an object identity unique within the owning execution unit,</li>
  <li>support objects MUST remain distinguishable from primary objects by recoverable identity-bearing classification,</li>
  <li>document identity MUST NOT be reused as a substitute for unit or object identity,</li>
  <li>unit identity MUST NOT be reused as a substitute for object identity.</li>
</ul>

<pre><code>canonical Execution IR Document
└── document identity
    └── execution unit identity
        ├── object identity
        ├── connection identity
        ├── region identity
        └── attribution / correspondence record identity where applicable
</code></pre>

<p>
This layered identity model exists so that tools can answer different questions without ambiguity:
</p>

<ul>
  <li>Which canonical IR artifact is this?</li>
  <li>Which execution unit does this record belong to?</li>
  <li>Which execution-facing object is this?</li>
  <li>Is this object primary, support, or only referenced through correspondence?</li>
</ul>

<hr />

<h2 id="ports-terminals-connections-and-regions">11. Ports, Terminals, Connections, and Regions</h2>

<p>
Identity obligations do not stop at object level.
Where those categories are made explicit in the canonical IR, they MUST also remain recoverable as structured identity-bearing records or equivalent explicit references.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>every explicit port or terminal MUST remain attached to an owning execution-facing object,</li>
  <li>every explicit connection MUST remain attached to attributable source and destination endpoints,</li>
  <li>every explicit region MUST remain attached to an owning structure object,</li>
  <li>where structure-boundary terminals are materialized explicitly, they MUST remain distinguishable from ordinary ports,</li>
  <li>where structure terminals are materialized explicitly, their structure-intrinsic role MUST remain recoverable.</li>
</ul>

<p>
If a conforming implementation chooses not to materialize a given helper category as a first-class record, equivalent recoverability MUST still remain possible through explicit references or explicit structured membership.
</p>

<pre><code>object
  ├── ports / terminals
  ├── region membership where applicable
  └── attributable connectivity

structure
  ├── owned regions
  ├── boundary roles
  └── structure-terminal roles
</code></pre>

<hr />

<h2 id="attribution-and-correspondence-records">12. Attribution and Correspondence Records</h2>

<p>
Attribution and correspondence are not merely diagnostic conveniences.
They are part of the canonical open IR boundary.
</p>

<p>
At minimum, a conforming canonical Execution IR representation MUST support:
</p>

<ul>
  <li><strong>attribution</strong> — which validated contributor or contributors gave rise to this IR-side record,</li>
  <li><strong>correspondence</strong> — how a validated source-visible contributor relates to primary objects, support objects, or intentional non-primary outcomes.</li>
</ul>

<p>
Accordingly:
</p>

<ul>
  <li>a directly preserved object SHOULD expose direct attribution,</li>
  <li>a support object derived from multiple contributors MUST expose explicit contributor attribution,</li>
  <li>intentional non-primary outcomes MUST remain distinguishable from accidental identity loss,</li>
  <li>declaration-reference relations MUST remain distinguishable from primary execution-object identity,</li>
  <li>attribution and correspondence MAY be inline, table-based, or represented through equivalent explicit records.</li>
</ul>

<pre><code>primary object
   -&gt; direct attribution

support object
   -&gt; contributor attribution

non-primary source-visible contributor
   -&gt; correspondence without forced primary execution identity
</code></pre>

<p>
A conforming implementation MUST NOT rely on undocumented ordering conventions or positional coincidence as the only mapping mechanism.
</p>

<hr />

<h2 id="allowed-normalization">13. Allowed Normalization</h2>

<p>
The following are allowed when semantic equivalence and recoverability are preserved:
</p>

<ul>
  <li>making ports, types, and directions explicit,</li>
  <li>making document and unit identity explicit,</li>
  <li>making regions and terminals explicit,</li>
  <li>adding support objects,</li>
  <li>introducing canonical IR identifiers,</li>
  <li>expanding one validated contributor into multiple attributable IR-side support objects,</li>
  <li>normalizing equivalent validated forms into one canonical execution-facing representation.</li>
</ul>

<p>
These normalizations are allowed only if all of the following remain true:
</p>

<ul>
  <li>semantic equivalence is preserved,</li>
  <li>attribution is preserved,</li>
  <li>required distinctions are preserved,</li>
  <li>explicit memory remains explicit,</li>
  <li>structured control remains recoverable.</li>
</ul>

<p>
Canonicalization of identifier syntax is permitted.
Loss of identity relation is not.
</p>

<hr />

<h2 id="forbidden-transformations">14. Forbidden Transformations</h2>

<p>
The following transformations are forbidden:
</p>

<ul>
  <li>loss of attribution for execution-facing objects,</li>
  <li>opaque object collapse that destroys contributor recoverability,</li>
  <li>hidden memory insertion presented as though it had validated source origin,</li>
  <li>collapse of interface participation and UI participation into one undifferentiated identity class,</li>
  <li>collapse of <code>widget_value</code> participation and property-based access to member <code>value</code> into one undifferentiated identity class,</li>
  <li>collapse of document identity, unit identity, and object identity into one ambiguous identifier role,</li>
  <li>structure flattening that destroys family, region, or terminal recoverability,</li>
  <li>promotion of editor-only state into execution-facing identity,</li>
  <li>forced executionization of non-execution source content merely because it exists in source,</li>
  <li>rewriting support objects as though they were independently authored semantic truth,</li>
  <li>treating one runtime-private identity model as though it were the canonical open IR identity model.</li>
</ul>

<pre><code>forbidden
    =
anything that breaks semantic traceability
or destroys required recoverability
</code></pre>

<hr />

<h2 id="relation-with-schema-construction-lowering-and-backend-contract">15. Relation with Schema, Construction, Lowering, and Backend Contract</h2>

<p>
This document defines recoverability obligations at the canonical open-IR boundary.
Schema, construction, lowering, and backend contract remain distinct concerns.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>construction MUST materialize the required identity and mapping carriers,</li>
  <li>schema MAY validate the structural presence of those carriers where published,</li>
  <li>lowering MAY refine or expand identity,</li>
  <li>backend contract MAY carry consumer-facing identity anchors,</li>
  <li>runtime or backend-private realization MAY introduce private handles or activation identities,</li>
  <li>but none of those stages may erase required recoverability while still claiming faithful downstream correspondence.</li>
</ul>

<p>
In particular:
</p>

<ul>
  <li>backend-family orientation is not itself a canonical open-IR identity class,</li>
  <li>target-profile assumptions are not themselves a substitute for source-attributable object identity,</li>
  <li>deployment-mode assumptions are not themselves a substitute for semantic identity,</li>
  <li>runtime-private realization identity is not the normative identity model of the canonical Execution IR Document.</li>
</ul>

<pre><code>open IR identity
      constrains
safe construction

safe construction
      constrains
schema-valid canonical payloads

schema-valid canonical payloads
      constrain
safe lowering

safe lowering
      constrains
faithful backend contract

faithful backend contract
      constrains
later diagnosable realization
</code></pre>

<hr />

<h2 id="relation-with-observation-and-debugging">16. Relation with Observation and Debugging</h2>

<p>
The canonical Execution IR is not:
</p>

<ul>
  <li>a runtime trace,</li>
  <li>a log,</li>
  <li>a runtime snapshot,</li>
  <li>a debugger event stream.</li>
</ul>

<p>
However, its identity and mapping rules MUST support later layers that need:
</p>

<ul>
  <li>source-aligned debugging,</li>
  <li>structure-aware inspection,</li>
  <li>state inspection,</li>
  <li>fault attribution,</li>
  <li>recoverable mapping from lowered or runtime-private activity back to meaningful source-facing contributors.</li>
</ul>

<p>
This document therefore supports observation indirectly by preserving the identity surface that later observation layers depend on.
</p>

<hr />

<h2 id="canonical-json-shape-posture">17. Canonical JSON Shape Posture</h2>

<p>
The canonical JSON Execution IR form SHOULD expose or imply information equivalent to:
</p>

<ul>
  <li>document identity,</li>
  <li>unit identity,</li>
  <li>IR-side object identity,</li>
  <li>object classification,</li>
  <li>mapping relation,</li>
  <li>semantic origin identity,</li>
  <li>source attribution,</li>
  <li>correspondence where needed.</li>
</ul>

<pre><code>{
  "document_id": "...",
  "unit": {
    "id": "...",
    "objects": [
      {
        "id": "...",
        "family": "...",
        "role": "...",
        "attribution": { ... },
        "correspondence_refs": [ ... ]
      }
    ],
    "source_map": [ ... ],
    "correspondence": [ ... ]
  }
}
</code></pre>

<p>
The exact field names above are illustrative only.
What matters here is the recoverable presence of equivalent information.
The machine-checkable schema layer owns the exact published payload validation surface.
</p>

<hr />

<h2 id="examples">18. Examples</h2>

<h3>18.1 1 -&gt; 1</h3>

<pre><code>validated primitive contributor
    -&gt;
primitive execution object
with direct attribution
</code></pre>

<h3>18.2 1 -&gt; n</h3>

<pre><code>validated structure contributor
    -&gt;
structured execution object
    + region objects
    + terminal support objects
with recoverable ownership and attribution
</code></pre>

<h3>18.3 n -&gt; 1</h3>

<pre><code>multiple contributors
    -&gt;
one support object
with explicit contributor attribution
</code></pre>

<h3>18.4 1 -&gt; 0</h3>

<pre><code>non-participating widget declaration
    -&gt;
no primary execution object
but declaration correspondence may still remain recoverable
</code></pre>

<h3>18.5 Distinction preservation</h3>

<pre><code>widget_reference contributor
    !=
frog.ui.property_write contributor

both may be related
but they do not share one undifferentiated identity
</code></pre>

<h3>18.6 Document versus unit versus object</h3>

<pre><code>validated FROG
   -&gt; Execution IR Document D
      -&gt; execution unit U
         -&gt; object O1
         -&gt; object O2

D != U
U != O1
O1 != O2
</code></pre>

<hr />

<h2 id="out-of-scope-for-v01">19. Out of Scope for v0.1</h2>

<ul>
  <li>a global cross-repository identifier system for every artifact class,</li>
  <li>runtime activation identity in full,</li>
  <li>debug transport or debugger protocol,</li>
  <li>lowered-identity schema in full,</li>
  <li>backend-private handle systems,</li>
  <li>deployment identity and package identity systems.</li>
</ul>

<hr />

<h2 id="summary">20. Summary</h2>

<p>
A conforming canonical Execution IR MUST:
</p>

<ul>
  <li>preserve validated execution-facing meaning,</li>
  <li>preserve attribution,</li>
  <li>preserve recoverability.</li>
</ul>

<p>
Its identity model exists so that the canonical Execution IR Document remains:
</p>

<ul>
  <li>semantically grounded,</li>
  <li>inspectable,</li>
  <li>source-aligned,</li>
  <li>safe to lower without collapsing into private execution truth.</li>
</ul>

<pre><code>validated meaning
        |
        v
recoverable canonical IR identity
        |
        v
safe construction and schema validation
        |
        v
safe specialization
        |
        v
later diagnosable realization
</code></pre>
