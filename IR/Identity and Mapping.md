<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG IR Identity and Mapping</h1>

<p align="center">
  <strong>Normative identity, attribution, and recoverability rules for open Execution IR</strong><br />
  FROG — Free Open Graphical Language
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
  <li><a href="#relation-with-observation">12. Relation with Observation and Debugging</a></li>
  <li><a href="#minimal-open-shape">13. Minimal Open Shape</a></li>
  <li><a href="#examples">14. Examples</a></li>
  <li><a href="#out-of-scope">15. Out of Scope</a></li>
  <li><a href="#summary">16. Summary</a></li>
</ul>

<hr />

<h2 id="overview">1. Overview</h2>

<p>
This document defines the identity and mapping rules that connect:
</p>

<ul>
  <li>source-visible identity,</li>
  <li>validated program meaning,</li>
  <li>execution-facing IR identity.</li>
</ul>

<p>
Its purpose is to ensure that open Execution IR remains:
</p>

<ul>
  <li>source-attributable,</li>
  <li>semantically grounded,</li>
  <li>recoverable for tooling and inspection,</li>
  <li>usable for lowering without becoming a private runtime form.</li>
</ul>

<p>
This document does not define semantics.
It defines how identity MUST survive projection into IR.
</p>

<pre><code>source identity
        |
        v
validated meaning
        |
        v
IR identity
        |
        v
lowering / runtime
</code></pre>

<hr />

<h2 id="boundary-contract">2. Boundary Contract</h2>

<p>
Every execution-facing IR object MUST be attributable to validated program meaning.
</p>

<p>
Every mapping MUST allow recovery of:
</p>

<ul>
  <li>its source-visible contributors,</li>
  <li>its semantic role,</li>
  <li>its derivation relation.</li>
</ul>

<p>
Identity is therefore not optional metadata.
It is part of the correctness of the IR.
</p>

<pre><code>valid IR
   =
correct execution semantics
   +
recoverable identity
</code></pre>

<hr />

<h2 id="scope">3. Scope</h2>

<p>
This document defines:
</p>

<ul>
  <li>identity layers,</li>
  <li>mapping relations,</li>
  <li>recoverability obligations,</li>
  <li>identity-safe normalization,</li>
  <li>identity-breaking forbidden transformations.</li>
</ul>

<p>
This document does not define:
</p>

<ul>
  <li>full source schema,</li>
  <li>language semantics,</li>
  <li>complete IR schema,</li>
  <li>construction algorithm,</li>
  <li>runtime identity models.</li>
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
IDENTITY + DERIVATION (this boundary)
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
runtime
</code></pre>

<p>
Identity rules apply at the derivation boundary and constrain all downstream transformations.
</p>

<hr />

<h2 id="identity-layers">5. Identity Layers</h2>

<h3>5.1 Source identity</h3>

<p>
Identity of authored elements:
</p>

<ul>
  <li>nodes (primitive, structure, subfrog),</li>
  <li>boundary nodes,</li>
  <li>widget participation,</li>
  <li>connections,</li>
  <li>relevant declarations.</li>
</ul>

<p>
Source identity reflects authored intent.
</p>

<h3>5.2 Validated semantic identity</h3>

<p>
Identity after validation:
</p>

<ul>
  <li>removes invalid constructs,</li>
  <li>resolves types and roles,</li>
  <li>stabilizes execution meaning.</li>
</ul>

<p>
This layer is authoritative for derivation.
</p>

<h3>5.3 IR identity</h3>

<p>
Identity inside one execution unit:
</p>

<ul>
  <li>unique within the unit,</li>
  <li>stable during IR lifetime,</li>
  <li>mapped to validated meaning.</li>
</ul>

<p>
IR identity is representation identity, not runtime identity.
</p>

<h3>5.4 Runtime identity</h3>

<p>
Dynamic execution identity (instances, activations).
</p>

<p>
Out of scope, but MUST remain mappable back to source identity.
</p>

<pre><code>source → semantic → IR → runtime
</code></pre>

<hr />

<h2 id="general-mapping-model">6. General Mapping Model</h2>

<p>
Allowed mapping relations:
</p>

<ul>
  <li>1 → 1 (preservation)</li>
  <li>1 → n (expansion)</li>
  <li>n → 1 (restricted support aggregation)</li>
  <li>1 → 0 (non-primary correspondence)</li>
</ul>

<p>
Rule:
</p>

<pre><code>explicitness MAY increase
recoverability MUST remain
</code></pre>

<p>
Every IR object MUST expose:
</p>

<ul>
  <li>its semantic origin,</li>
  <li>its source contributors,</li>
  <li>its mapping relation.</li>
</ul>

<hr />

<h2 id="preconditions">7. Preconditions</h2>

<p>
Identity-preserving IR requires:
</p>

<ul>
  <li>complete validation,</li>
  <li>type correctness,</li>
  <li>structure correctness,</li>
  <li>cycle legality,</li>
  <li>boundary consistency.</li>
</ul>

<pre><code>no validation → no valid identity-preserving IR
</code></pre>

<hr />

<h2 id="required-recoverability">8. Required Recoverability</h2>

<p>
The following MUST remain recoverable:
</p>

<ul>
  <li>interface_input vs interface_output,</li>
  <li>widget_value vs widget_reference,</li>
  <li>UI primitive vs widget reference,</li>
  <li>interface vs UI participation,</li>
  <li>structure families,</li>
  <li>regions and boundaries,</li>
  <li>structure terminals,</li>
  <li>explicit memory,</li>
  <li>invocation boundaries,</li>
  <li>primary vs support vs non-primary roles.</li>
</ul>

<pre><code>recoverability set = minimal invariant surface
</code></pre>

<hr />

<h2 id="mapping-rules">9. Mapping Rules</h2>

<h3>Objects</h3>
<ul>
  <li>Primary objects → directly attributable</li>
  <li>Support objects → attributable to contributors</li>
</ul>

<h3>Ports / terminals</h3>
<ul>
  <li>Must map to owning object</li>
  <li>Must preserve role (boundary, structure, etc.)</li>
</ul>

<h3>Connections</h3>
<ul>
  <li>Must preserve dependency meaning</li>
  <li>Must preserve attribution</li>
</ul>

<h3>Regions</h3>
<ul>
  <li>Must preserve ownership</li>
  <li>Must preserve structure linkage</li>
</ul>

<hr />

<h2 id="allowed-normalization">10. Allowed Normalization</h2>

<ul>
  <li>explicit ports/types/directions</li>
  <li>explicit regions and terminals</li>
  <li>support objects</li>
  <li>canonical IR identifiers</li>
  <li>expansion of objects</li>
</ul>

<p>
Conditions:
</p>

<ul>
  <li>semantic equivalence preserved</li>
  <li>attribution preserved</li>
  <li>distinctions preserved</li>
</ul>

<hr />

<h2 id="forbidden-transformations">11. Forbidden Transformations</h2>

<ul>
  <li>loss of attribution</li>
  <li>opaque object collapse</li>
  <li>hidden memory insertion</li>
  <li>interface/UI merge</li>
  <li>structure flattening without recovery</li>
  <li>editor-state semantics</li>
  <li>forced execution of non-execution content</li>
</ul>

<pre><code>forbidden = anything that breaks traceability
</code></pre>

<hr />

<h2 id="relation-with-observation">12. Relation with Observation and Debugging</h2>

<p>
Open IR is not:
</p>

<ul>
  <li>a trace,</li>
  <li>a log,</li>
  <li>a runtime snapshot.</li>
</ul>

<p>
But it MUST enable:
</p>

<ul>
  <li>source-aligned debugging,</li>
  <li>structure-aware inspection,</li>
  <li>state inspection.</li>
</ul>

<hr />

<h2 id="minimal-open-shape">13. Minimal Open Shape</h2>

<p>
A conforming IR SHOULD expose:
</p>

<ul>
  <li>IR identity</li>
  <li>object classification</li>
  <li>mapping relation</li>
  <li>semantic identity</li>
  <li>source attribution</li>
</ul>

<pre><code>{
  ir_id,
  kind,
  role,
  mapping_relation,
  semantic_identity,
  source_attribution
}
</code></pre>

<hr />

<h2 id="examples">14. Examples</h2>

<h3>1 → 1</h3>
<pre><code>primitive → primitive IR object
</code></pre>

<h3>1 → n</h3>
<pre><code>structure → structure + regions + terminals
</code></pre>

<h3>n → 1</h3>
<pre><code>contributors → support object (with attribution)
</code></pre>

<h3>1 → 0</h3>
<pre><code>non-participating widget → no IR object
</code></pre>

<hr />

<h2 id="out-of-scope">15. Out of Scope</h2>

<ul>
  <li>global identity system</li>
  <li>runtime identity</li>
  <li>debug protocol</li>
  <li>lowering identity</li>
</ul>

<hr />

<h2 id="summary">16. Summary</h2>

<p>
A valid open Execution IR MUST:
</p>

<ul>
  <li>preserve meaning,</li>
  <li>preserve attribution,</li>
  <li>preserve recoverability.</li>
</ul>

<pre><code>validated meaning
        |
        v
recoverable IR identity
        |
        v
safe specialization
</code></pre>
