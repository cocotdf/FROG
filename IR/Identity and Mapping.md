<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG IR Identity and Mapping</h1>

<p align="center">
  <strong>Normative identity, attribution, and recoverability rules for open Execution IR</strong><br />
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr />

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#boundary-contract">2. Boundary Contract</a></li>
  <li><a href="#scope">3. Scope</a></li>
  <li><a href="#position-in-the-pipeline">4. Position in the Pipeline</a></li>
  <li><a href="#identity-layers">5. Identity Layers</a></li>
  <li><a href="#general-mapping-model">6. General Mapping Model</a></li>
  <li><a href="#preconditions">7. Preconditions</a></li>
  <li><a href="#required-recoverability">8. Required Recoverability</a></li>
  <li><a href="#mapping-rules">9. Mapping Rules</a></li>
  <li><a href="#allowed-normalization">10. Allowed Normalization</a></li>
  <li><a href="#forbidden-transformations">11. Forbidden Transformations</a></li>
  <li><a href="#relation-with-lowering-and-backend-contract">12. Relation with Lowering and Backend Contract</a></li>
  <li><a href="#relation-with-observation-and-debugging">13. Relation with Observation and Debugging</a></li>
  <li><a href="#minimal-open-shape">14. Minimal Open Shape</a></li>
  <li><a href="#examples">15. Examples</a></li>
  <li><a href="#out-of-scope">16. Out of Scope</a></li>
  <li><a href="#summary">17. Summary</a></li>
</ul>

<hr />

<h2 id="overview">1. Overview</h2>

<p>
This document defines the identity and mapping rules that connect:
</p>

<ul>
  <li>validated source-visible contributors,</li>
  <li>validated program meaning,</li>
  <li>execution-facing IR identity.</li>
</ul>

<p>
Its purpose is to ensure that open Execution IR remains:
</p>

<ul>
  <li>source-attributable,</li>
  <li>semantically grounded,</li>
  <li>recoverable for inspection and tooling,</li>
  <li>usable for lowering without collapsing into private runtime form.</li>
</ul>

<p>
This document does not define semantic truth.
It defines how identity, attribution, and recoverability MUST survive projection into open Execution IR.
</p>

<pre><code>validated source-visible contributors
                |
                v
validated program meaning
                |
                v
open Execution IR identity
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
  <li>its object-family classification where relevant.</li>
</ul>

<p>
Identity is therefore not optional metadata.
It is part of the correctness of open Execution IR.
</p>

<pre><code>valid IR
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

<h2 id="scope">3. Scope</h2>

<p>
This document defines:
</p>

<ul>
  <li>identity layers relevant to open Execution IR,</li>
  <li>mapping relations between validated meaning and IR objects,</li>
  <li>recoverability obligations that MUST survive derivation,</li>
  <li>identity-safe normalization,</li>
  <li>identity-breaking forbidden transformations.</li>
</ul>

<p>
This document does not define:
</p>

<ul>
  <li>the full source schema,</li>
  <li>language semantics in full,</li>
  <li>the complete Execution IR schema,</li>
  <li>the construction algorithm in full,</li>
  <li>runtime-private identity models.</li>
</ul>

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
open Execution IR
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

<h3>5.3 Open Execution IR identity</h3>

<p>
This is the identity of objects inside one execution unit:
</p>

<ul>
  <li>unique within the relevant unit scope,</li>
  <li>stable for the lifetime of that IR instance,</li>
  <li>mapped to validated meaning through explicit correspondence.</li>
</ul>

<p>
IR identity is execution-facing representation identity.
It is not yet runtime activation identity.
</p>

<h3>5.4 Lowered identity</h3>

<p>
Lowering may later introduce additional identities or refined object partitions.
That lowered identity remains downstream from this document, but it MUST respect recoverability obligations inherited from open Execution IR where later stages still claim faithful mapping.
</p>

<h3>5.5 Runtime or backend-private identity</h3>

<p>
Dynamic execution identity such as activations, instances, handles, retained state cells, or backend-private objects is downstream and out of scope here.
However, when later stages claim source-aligned diagnosability, their private identity models MUST still remain mappable back to the relevant open-IR and source-facing identities.
</p>

<pre><code>source-visible
      -&gt;
validated semantic
      -&gt;
open IR
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
  <li>its object-family role where relevant.</li>
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
Identity-preserving open Execution IR requires:
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
no conforming identity-preserving open Execution IR
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
  <li><code>interface_input</code> versus <code>interface_output</code>,</li>
  <li><code>widget_value</code> versus <code>widget_reference</code>,</li>
  <li>standardized UI-object primitive versus widget-reference participation,</li>
  <li>public interface participation versus UI participation,</li>
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
for open Execution IR correspondence
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

<h2 id="allowed-normalization">10. Allowed Normalization</h2>

<p>
The following are allowed when semantic equivalence and recoverability are preserved:
</p>

<ul>
  <li>making ports, types, and directions explicit,</li>
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

<h2 id="forbidden-transformations">11. Forbidden Transformations</h2>

<p>
The following transformations are forbidden:
</p>

<ul>
  <li>loss of attribution for execution-facing objects,</li>
  <li>opaque object collapse that destroys contributor recoverability,</li>
  <li>hidden memory insertion presented as though it had validated source origin,</li>
  <li>collapse of interface participation and UI participation into one undifferentiated identity class,</li>
  <li>structure flattening that destroys family, region, or terminal recoverability,</li>
  <li>promotion of editor-only state into execution-facing identity,</li>
  <li>forced executionization of non-execution source content merely because it exists in source,</li>
  <li>rewriting support objects as though they were independently authored semantic truth,</li>
  <li>treating one runtime-private identity model as though it were the open IR identity model.</li>
</ul>

<pre><code>forbidden
    =
anything that breaks semantic traceability
or destroys required recoverability
</code></pre>

<hr />

<h2 id="relation-with-lowering-and-backend-contract">12. Relation with Lowering and Backend Contract</h2>

<p>
This document defines recoverability obligations at the open-IR boundary.
Lowering and backend contract remain downstream.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>lowering MAY refine or expand identity,</li>
  <li>backend contract MAY carry consumer-facing identity anchors,</li>
  <li>runtime or backend-private realization MAY introduce private handles or activation identities,</li>
  <li>but none of those stages may erase required recoverability while still claiming faithful downstream correspondence.</li>
</ul>

<p>
In particular:
</p>

<ul>
  <li>backend-family orientation is not itself an open-IR identity class,</li>
  <li>target-profile assumptions are not themselves a substitute for source-attributable object identity,</li>
  <li>deployment-mode assumptions are not themselves a substitute for semantic identity,</li>
  <li>runtime-private realization identity is not the normative identity model of open Execution IR.</li>
</ul>

<pre><code>open IR identity
      constrains
safe lowering

safe lowering
      constrains
faithful backend contract

faithful backend contract
      constrains
later diagnosable realization
</code></pre>

<hr />

<h2 id="relation-with-observation-and-debugging">13. Relation with Observation and Debugging</h2>

<p>
Open Execution IR is not:
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

<h2 id="minimal-open-shape">14. Minimal Open Shape</h2>

<p>
A conforming execution-facing IR object SHOULD expose or imply information equivalent to:
</p>

<ul>
  <li>IR identity,</li>
  <li>object classification,</li>
  <li>mapping relation,</li>
  <li>semantic origin identity,</li>
  <li>source attribution.</li>
</ul>

<pre><code>{
  "ir_id": "...",
  "kind": "...",
  "role": "...",
  "mapping_relation": "...",
  "semantic_identity": "...",
  "source_attribution": [...]
}
</code></pre>

<p>
The exact field names are illustrative only.
What matters is the recoverable presence of equivalent information.
</p>

<hr />

<h2 id="examples">15. Examples</h2>

<h3>15.1 1 -&gt; 1</h3>

<pre><code>validated primitive contributor
    -&gt;
primitive execution object
</code></pre>

<h3>15.2 1 -&gt; n</h3>

<pre><code>validated structure contributor
    -&gt;
structured execution object
    + region objects
    + terminal support objects
</code></pre>

<h3>15.3 n -&gt; 1</h3>

<pre><code>multiple contributors
    -&gt;
one support object
with explicit contributor attribution
</code></pre>

<h3>15.4 1 -&gt; 0</h3>

<pre><code>non-participating widget declaration
    -&gt;
no primary execution object
but declaration correspondence may still remain recoverable
</code></pre>

<h3>15.5 Distinction preservation</h3>

<pre><code>widget_reference contributor
    !=
frog.ui.property_write contributor

both may be related
but they do not share one undifferentiated identity
</code></pre>

<hr />

<h2 id="out-of-scope">16. Out of Scope</h2>

<ul>
  <li>a global cross-repository identifier system for every artifact class,</li>
  <li>runtime activation identity in full,</li>
  <li>debug transport or debugger protocol,</li>
  <li>lowered-identity schema in full,</li>
  <li>backend-private handle systems,</li>
  <li>deployment identity and package identity systems.</li>
</ul>

<hr />

<h2 id="summary">17. Summary</h2>

<p>
A conforming open Execution IR MUST:
</p>

<ul>
  <li>preserve validated execution-facing meaning,</li>
  <li>preserve attribution,</li>
  <li>preserve recoverability.</li>
</ul>

<p>
Its identity model exists so that open Execution IR remains:
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
recoverable open IR identity
        |
        v
safe specialization
        |
        v
later diagnosable realization
</code></pre>
