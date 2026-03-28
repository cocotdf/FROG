<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG IR Derivation Rules</h1>

<p align="center">
  <strong>Normative derivation rules from validated FROG program meaning to the canonical Execution IR Document</strong><br />
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr />

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#reading-legend">2. Reading Legend</a></li>
  <li><a href="#scope-of-this-document">3. Scope of this Document</a></li>
  <li><a href="#relation-with-other-specifications">4. Relation with Other Specifications</a></li>
  <li><a href="#derivation-boundary">5. Derivation Boundary</a></li>
  <li><a href="#inputs-and-preconditions">6. Inputs and Preconditions</a></li>
  <li><a href="#derivation-result">7. Derivation Result</a></li>
  <li><a href="#core-derivation-invariants">8. Core Derivation Invariants</a></li>
  <li><a href="#derivation-relation-shapes">9. Derivation Relation Shapes</a></li>
  <li><a href="#source-to-ir-family-mapping">10. Source-to-IR Family Mapping</a></li>
  <li><a href="#identity-and-attribution-rules">11. Identity and Attribution Rules</a></li>
  <li><a href="#connectivity-derivation">12. Connectivity Derivation</a></li>
  <li><a href="#structured-control-derivation">13. Structured Control Derivation</a></li>
  <li><a href="#interface-and-ui-derivation">14. Interface and UI Derivation</a></li>
  <li><a href="#state-and-cycle-preservation">15. State and Cycle Preservation</a></li>
  <li><a href="#allowed-normalization-during-derivation">16. Allowed Normalization During Derivation</a></li>
  <li><a href="#forbidden-derivation-outcomes">17. Forbidden Derivation Outcomes</a></li>
  <li><a href="#relation-with-construction-schema-lowering-and-backend-contract">18. Relation with Construction, Schema, Lowering, and Backend Contract</a></li>
  <li><a href="#out-of-scope-for-v01">19. Out of Scope for v0.1</a></li>
  <li><a href="#summary">20. Summary</a></li>
</ul>

<hr />

<h2 id="overview">1. Overview</h2>

<p>
This document defines the normative derivation boundary between validated FROG program meaning and the
<strong>canonical Execution IR Document</strong>.
It specifies:
</p>

<ul>
  <li>which validated execution-relevant families derive to execution-facing IR families,</li>
  <li>which source-side distinctions MUST remain recoverable at the derivation boundary,</li>
  <li>which support objects MAY be introduced to make already-validated execution structure explicit,</li>
  <li>which source-visible families do not become primary execution objects in the canonical open IR,</li>
  <li>which transformations are allowed as derivation-time normalization, and</li>
  <li>which transformations are forbidden because they would blur ownership, erase attribution, or introduce runtime-private meaning too early.</li>
</ul>

<p>
This document is intentionally about correspondence obligations.
It is not:
</p>

<ul>
  <li>the full source specification,</li>
  <li>the full language semantics specification,</li>
  <li>the complete Execution IR object-model specification,</li>
  <li>the construction algorithm for every implementation,</li>
  <li>the schema definition itself,</li>
  <li>or a runtime-private realization guide.</li>
</ul>

<p>
Compact mental model:
</p>

<pre><code>canonical source
        |
        v
validated program meaning
        |
        v
derivation rules   &lt;-- this document
        |
        v
canonical Execution IR Document
        |
        v
lowering / specialization
        |
        v
backend-facing contract
        |
        v
runtime-private realization
</code></pre>

<p>
In base v0.1, derivation is intentionally conservative.
It preserves validated meaning,
preserves recoverable identity,
preserves explicit structured control,
preserves explicit local memory,
preserves validated dependency structure,
and preserves the distinction between:
</p>

<ul>
  <li>public interface participation,</li>
  <li><code>widget_value</code> participation,</li>
  <li><code>widget_reference</code> participation,</li>
  <li>standardized UI-object primitive operation.</li>
</ul>

<hr />

<h2 id="reading-legend">2. Reading Legend</h2>

<ul>
  <li>🟦 <strong>Open specification-facing representation or layer</strong></li>
  <li>🟩 <strong>Semantic truth, attribution, recoverability, or validation result</strong></li>
  <li>🟨 <strong>Boundary, correspondence, mapping, or standardized handoff</strong></li>
  <li>🟧 <strong>Lowering, specialization, or target adaptation zone</strong></li>
  <li>🟥 <strong>Implementation-private or runtime-private realization zone</strong></li>
</ul>

<hr />

<h2 id="scope-of-this-document">3. Scope of this Document</h2>

<p>
This document defines:
</p>

<ul>
  <li>the normative entry condition for Execution IR derivation,</li>
  <li>the relation shapes permitted at the derivation boundary,</li>
  <li>the base v0.1 correspondence between validated execution-relevant families and Execution IR families,</li>
  <li>the minimum attribution and recoverability obligations that MUST survive derivation,</li>
  <li>the allowed and forbidden kinds of derivation-time explicitness and normalization,</li>
  <li>the rule that one validated FROG program derives to one canonical Execution IR Document containing one execution unit in base v0.1.</li>
</ul>

<p>
This document does not define:
</p>

<ul>
  <li>the canonical source model in full,</li>
  <li>the full normative semantics of validated FROG programs,</li>
  <li>the full Execution IR object model in complete detail,</li>
  <li>the exact material build sequence of every implementation,</li>
  <li>the JSON schema text of the canonical payload,</li>
  <li>the lowering strategy of every backend,</li>
  <li>the backend contract in full,</li>
  <li>the private scheduler, storage, or ABI policy of any runtime.</li>
</ul>

<pre><code>This document defines:
- what must correspond
- what must remain recoverable
- what may be made explicit during derivation
- what derivation must not silently change
- that one validated program yields one canonical IR document

This document does not define:
- canonical source in full               -&gt; Expression/
- validated program meaning in full      -&gt; Language/
- full open IR model                     -&gt; Execution IR.md
- material payload construction          -&gt; Construction rules.md
- machine-checkable schema text          -&gt; Schema.md / IR/schema/
- runtime-private realization            -&gt; outside IR ownership
</code></pre>

<hr />

<h2 id="relation-with-other-specifications">4. Relation with Other Specifications</h2>

<p>
Ownership remains:
</p>

<pre><code>Expression/                 -&gt; canonical source shape and structural validity
Language/                   -&gt; validated program meaning
IR/Execution IR.md          -&gt; canonical open Execution IR architecture
IR/Derivation rules.md      -&gt; correspondence from meaning to IR
IR/Construction rules.md    -&gt; material IR construction and canonical JSON emission
IR/Schema.md                -&gt; schema posture for canonical IR validation
IR/schema/                  -&gt; machine-checkable schema artifacts
IR/Identity and Mapping.md  -&gt; cross-layer recoverability
IR/Lowering.md              -&gt; later target-oriented specialization
IR/Backend contract.md      -&gt; later backend-facing handoff
</code></pre>

<p>
Accordingly:
</p>

<ul>
  <li>this document MUST NOT redefine what a valid <code>.frog</code> file looks like,</li>
  <li>this document MUST NOT redefine what validated meaning is,</li>
  <li>this document MUST NOT redefine the complete canonical IR schema,</li>
  <li>this document MUST NOT redefine construction as a universal procedural algorithm,</li>
  <li>this document MUST NOT redefine backend-private or runtime-private structures,</li>
  <li>this document MUST define how validated meaning becomes the canonical open Execution IR boundary artifact.</li>
</ul>

<p>
This document should be read together with:
</p>

<ul>
  <li><code>Language/Expression to validated meaning.md</code>,</li>
  <li><code>IR/Execution IR.md</code>,</li>
  <li><code>IR/Identity and Mapping.md</code>,</li>
  <li><code>IR/Construction rules.md</code>,</li>
  <li><code>IR/Schema.md</code>,</li>
  <li><code>Expression/Diagram.md</code>,</li>
  <li><code>Expression/Control structures.md</code>,</li>
  <li><code>Expression/State and cycles.md</code>,</li>
  <li><code>Expression/Interface.md</code>,</li>
  <li><code>Expression/Front panel.md</code>,</li>
  <li><code>Expression/Widget.md</code>,</li>
  <li><code>Expression/Widget interaction.md</code>,</li>
  <li><code>Language/Control structures.md</code>,</li>
  <li><code>Language/State and cycles.md</code>.</li>
</ul>

<hr />

<h2 id="derivation-boundary">5. Derivation Boundary</h2>

<p>
Derivation is the normative correspondence boundary from validated program meaning to the
<strong>canonical Execution IR Document</strong>.
</p>

<p>
This boundary does not decide whether a program is valid.
That decision has already been made upstream.
This boundary does not invent missing semantics.
It only derives execution-facing representation from already-validated meaning.
</p>

<p>
Accordingly:
</p>

<pre><code>validation decides:
  whether meaning exists

derivation decides:
  how validated meaning becomes the canonical Execution IR Document
</code></pre>

<p>
The derivation boundary MUST therefore preserve:
</p>

<ul>
  <li>semantic faithfulness,</li>
  <li>execution-facing explicitness where required,</li>
  <li>source attribution,</li>
  <li>cross-stage recoverability,</li>
  <li>freedom from runtime-private semantic invention.</li>
</ul>

<hr />

<h2 id="inputs-and-preconditions">6. Inputs and Preconditions</h2>

<p>
Execution IR derivation begins <strong>only after semantic validation has succeeded</strong>.
</p>

<p>
The derivation input is not:
</p>

<ul>
  <li>raw serialized source as such,</li>
  <li>merely loadable source,</li>
  <li>merely structurally valid source,</li>
  <li>partially edited authoring state,</li>
  <li>editor convenience state,</li>
  <li>runtime speculation,</li>
  <li>implementation-private scheduler assumptions.</li>
</ul>

<p>
The derivation input is:
</p>

<ul>
  <li>one validated FROG program meaning.</li>
</ul>

<p>
An implementation MAY internally start from canonical source,
a validated Program Model,
or another validated internal form that is semantically equivalent.
However,
the canonical Execution IR it derives MUST be grounded in validated meaning rather than in editor-only convenience or runtime-private invention.
</p>

<pre><code>raw source ------------&gt; structural validity ------------&gt; semantic validation ------------&gt; derivation
                         outside this document             outside this document              this document
</code></pre>

<p>
Derivation is therefore not the place where an implementation:
</p>

<ul>
  <li>adds hidden scheduler policy,</li>
  <li>adds hidden memory,</li>
  <li>adds opaque backend partitions,</li>
  <li>collapses structured control into private machinery,</li>
  <li>promotes presentation metadata into execution semantics.</li>
</ul>

<hr />

<h2 id="derivation-result">7. Derivation Result</h2>

<p>
The result of derivation in base v0.1 is one <strong>canonical Execution IR Document</strong> for one validated FROG program.
That document contains one <strong>execution unit</strong>.
</p>

<p>
That execution unit MUST contain enough information to represent:
</p>

<ul>
  <li>execution-facing object identity,</li>
  <li>object-family classification,</li>
  <li>typed ports or equivalent explicit terminal interfaces,</li>
  <li>directed connectivity,</li>
  <li>structured regions where applicable,</li>
  <li>public boundary participation and UI participation where applicable,</li>
  <li>support objects where needed to make already-validated execution structure explicit,</li>
  <li>mandatory attribution to validated source-visible execution content.</li>
</ul>

<p>
The derivation result MUST be:
</p>

<ul>
  <li>semantically equivalent to validated meaning,</li>
  <li>mapping-compatible,</li>
  <li>inspectable,</li>
  <li>compatible with <code>IR/Execution IR.md</code>,</li>
  <li>constructible into the canonical JSON form defined by the IR layer.</li>
</ul>

<pre><code>one validated FROG
        |
        v
one Execution IR Document
        └── one execution unit
            ├── execution-facing objects
            ├── typed ports / explicit terminals
            ├── directed connections
            ├── explicit regions where applicable
            ├── explicit boundary participation
            ├── support objects where required
            └── source attribution
</code></pre>

<p>
The derivation result is not yet:
</p>

<ul>
  <li>a lowered target-facing form,</li>
  <li>a backend-facing contract artifact,</li>
  <li>a runtime-private artifact.</li>
</ul>

<hr />

<h2 id="core-derivation-invariants">8. Core Derivation Invariants</h2>

<p>
All conforming derivations in base v0.1 MUST satisfy the following invariants:
</p>

<ul>
  <li>Derivation MUST preserve validated language meaning.</li>
  <li>Derivation MUST preserve attribution to validated execution-visible source content.</li>
  <li>Derivation MUST preserve enough structure and identity for later recoverable mapping.</li>
  <li>Derivation MUST preserve explicit memory as explicit memory.</li>
  <li>Derivation MUST preserve structured control as structured control.</li>
  <li>Derivation MUST preserve validated dependency structure.</li>
  <li>Derivation MUST preserve the distinction between public interface participation and UI participation.</li>
  <li>Derivation MUST preserve the distinction between <code>widget_value</code> participation and <code>widget_reference</code> participation.</li>
  <li>Derivation MUST preserve the distinction between <code>widget_reference</code> participation and standardized UI-object primitive operation.</li>
  <li>Derivation MUST preserve the distinction between <code>widget_value</code> participation and property-based access to a widget member named <code>value</code>.</li>
  <li>Derivation MUST produce content compatible with one canonical Execution IR Document for one validated program.</li>
  <li>Derivation MUST NOT reinterpret non-execution source content as execution semantics merely because it exists in canonical source.</li>
  <li>Derivation MUST NOT import editor-only geometry, styling, annotation placement, or similar presentation state as execution semantics.</li>
  <li>Derivation MUST NOT standardize one runtime-private scheduler policy as though it were the open IR.</li>
</ul>

<pre><code>Core invariants

preserve semantic truth
preserve source attribution
preserve recoverable identity
preserve explicit memory
preserve structured control
preserve validated dependencies
preserve interface / UI distinction
preserve widget_value / widget_reference distinction
preserve widget_reference / UI-primitive distinction
preserve canonical-document compatibility

do not promote non-execution source content
do not import editor-only state
do not standardize private scheduler policy
</code></pre>

<hr />

<h2 id="derivation-relation-shapes">9. Derivation Relation Shapes</h2>

<p>
Base v0.1 distinguishes four broad derivation relation shapes:
</p>

<ul>
  <li><strong>1 -&gt; 1 direct preservation</strong> — one validated execution-relevant contributor derives to one primary IR object,</li>
  <li><strong>1 -&gt; n expansion</strong> — one validated contributor derives to one primary IR object plus one or more support objects,</li>
  <li><strong>n -&gt; 1 restricted aggregation</strong> — multiple validated contributors derive to one support object, but only when all contributors remain explicitly attributable,</li>
  <li><strong>1 -&gt; 0 non-primary derivation</strong> — one source-visible family remains relevant to validation, attribution, or correspondence, but does not become a primary execution object.</li>
</ul>

<p>
The first three shapes apply to execution-facing derived content.
The fourth applies to content that remains respected at the boundary without becoming a primary execution object.
</p>

<p>
Examples:
</p>

<ul>
  <li>a <code>primitive</code> node commonly derives by 1 -&gt; 1 direct preservation,</li>
  <li>a <code>structure</code> node commonly derives by 1 -&gt; n expansion,</li>
  <li>a validated interface declaration may derive as support-only correspondence rather than as a primary execution object,</li>
  <li>a non-participating widget declaration is typically 1 -&gt; 0 with respect to primary execution objects.</li>
</ul>

<pre><code>direct:
  source object A
      |
      v
  IR object A'

expanded:
  source object B
      |
      +------&gt; IR primary object B'
      |
      +------&gt; IR support object B1'
      |
      +------&gt; IR support object B2'

restricted aggregated support:
  source object C -----\
                        +----&gt; IR support object Cx'
  source object D -----/
  with explicit contributor attribution to C and D

non-primary:
  source object E
      |
      +----&gt; no primary execution object
      |
      +----&gt; obligations may still survive through attribution
             or boundary correspondence
</code></pre>

<hr />

<h2 id="source-to-ir-family-mapping">10. Source-to-IR Family Mapping</h2>

<p>
The rules below define the base v0.1 normative correspondence between validated families and canonical Execution IR families.
They are about <strong>execution-facing derivation</strong>.
They do not imply that every source-visible family becomes a primary execution object.
</p>

<h3>10.1 Execution-relevant families</h3>

<table>
  <thead>
    <tr>
      <th>Validated family</th>
      <th>Derivation shape</th>
      <th>Primary IR result</th>
      <th>Permitted support objects</th>
      <th>What MUST remain recoverable</th>
      <th>What derivation MUST NOT do</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Whole validated FROG</td>
      <td>1 -&gt; 1</td>
      <td>One Execution IR Document containing one execution unit</td>
      <td>Document-level attribution and classification records; unit-level attribution and classification records</td>
      <td>Program identity, document identity, and execution-unit identity relation</td>
      <td>Split one validated FROG into multiple competing canonical documents or multiple independent execution units in base v0.1</td>
    </tr>
    <tr>
      <td>Top-level executable diagram</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Top-level execution graph content of the execution unit</td>
      <td>Explicit top-level graph scope records if needed</td>
      <td>Top-level scope identity and contained-object attribution</td>
      <td>Hide top-level graph ownership or reinterpret it as opaque backend-only graph material</td>
    </tr>
    <tr>
      <td><code>primitive</code> node</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Primitive execution object</td>
      <td>Resolved port descriptors, attribution records, execution-facing classification records</td>
      <td>Primitive identity, resolved ports, execution-relevant metadata, source correspondence</td>
      <td>Replace the primitive with opaque runtime-private machinery or erase primitive identity in the open IR</td>
    </tr>
    <tr>
      <td>Standardized UI-object primitive (<code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, <code>frog.ui.method_invoke</code>)</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>UI-primitive execution object</td>
      <td>Resolved UI-port descriptors, resolved member or method descriptors, UI-operation classification records, source-map records</td>
      <td>Primitive identity, UI-operation family, referenced member or method semantics, required <code>widget_reference</code> participation, source correspondence</td>
      <td>Absorb the primitive into the widget-reference object itself or reinterpret it as unrestricted generic object execution</td>
    </tr>
    <tr>
      <td><code>subfrog</code> node</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Sub-FROG invocation object</td>
      <td>Resolved invocation-boundary descriptors, source-map records</td>
      <td>Referenced FROG identity, invocation identity, invocation boundary, resolved ports</td>
      <td>Inline or flatten invocation so aggressively that invocation identity becomes non-recoverable in the base open IR</td>
    </tr>
    <tr>
      <td><code>interface_input</code> node</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Public interface entry boundary object</td>
      <td>Resolved interface-port descriptors, unit-boundary classification records, support-only policy metadata where execution-relevant</td>
      <td>Public API role, referenced interface input, value direction, source correspondence</td>
      <td>Merge it into an undifferentiated endpoint concept together with widget participation</td>
    </tr>
    <tr>
      <td><code>interface_output</code> node</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Public interface exit boundary object</td>
      <td>Resolved interface-port descriptors, unit-boundary classification records</td>
      <td>Public API role, referenced interface output, value direction, source correspondence</td>
      <td>Merge it into an undifferentiated endpoint concept together with widget participation</td>
    </tr>
    <tr>
      <td><code>widget_value</code> node</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Widget-value participation object</td>
      <td>Resolved widget-value descriptors, widget-role classification records</td>
      <td>Referenced widget identity, primary-value participation role, control/indicator directionality, source correspondence</td>
      <td>Collapse it with public interface participation, reinterpret it as object-style reference participation, or normalize it into property access on member <code>value</code></td>
    </tr>
    <tr>
      <td><code>widget_reference</code> node</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Widget-reference participation object</td>
      <td>Resolved widget-reference descriptors, object-style access classification records</td>
      <td>Referenced widget identity, object-style access role, source correspondence</td>
      <td>Collapse it into ordinary valueflow participation, reinterpret it as unrestricted general-purpose storage, or absorb all standardized UI-object operations into the reference object itself</td>
    </tr>
    <tr>
      <td><code>structure</code> node</td>
      <td>1 -&gt; n</td>
      <td>Structured execution object</td>
      <td>Explicit region objects, boundary-terminal records, structure-terminal records, structured-port descriptors, source-map records</td>
      <td>Structure family, owned regions, boundary crossing, structure-terminal roles, source correspondence</td>
      <td>Flatten it immediately into backend-shaped opaque control machinery in a way that makes family identity or region ownership unrecoverable</td>
    </tr>
    <tr>
      <td>Structure region</td>
      <td>1 -&gt; 1</td>
      <td>Region object</td>
      <td>Region-local attribution records, region classification records</td>
      <td>Region identity, owning structure, source-region identity, region-local graph ownership</td>
      <td>Hide region ownership or allow region-local content to lose source-region attribution</td>
    </tr>
    <tr>
      <td>Structure boundary input/output entry</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Explicit boundary terminal or equivalent structured boundary-port form</td>
      <td>Terminal descriptors, attribution records, structured-boundary records</td>
      <td>Boundary crossing role, type, owning structure, source-side identity</td>
      <td>Allow cross-scope communication to bypass the structure wall implicitly</td>
    </tr>
    <tr>
      <td>Structure terminal entry</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Explicit structure terminal or equivalent structured terminal-port form</td>
      <td>Terminal descriptors, structure-terminal classification records</td>
      <td>Terminal role, type, owning structure, visibility relation, standardized terminal distinction</td>
      <td>Erase distinctions such as selector, loop count, loop condition, iteration index, or equivalent standardized terminal roles</td>
    </tr>
    <tr>
      <td>Diagram edge</td>
      <td>1 -&gt; 1</td>
      <td>Directed connection</td>
      <td>Resolved endpoint descriptors if needed</td>
      <td>Endpoint attribution, endpoint direction, validated dependency relation</td>
      <td>Detach connections from attributable objects or silently redirect connectivity through hidden scheduler-private objects</td>
    </tr>
    <tr>
      <td>Explicit local-memory primitive</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Attributable stateful execution object</td>
      <td>Resolved state descriptors, explicit initialization records, source-map records</td>
      <td>Explicit memory identity, explicit initial state, cycle-legality role, source correspondence</td>
      <td>Legalize a cycle by inserting hidden implicit memory or erase the attribution of explicit memory</td>
    </tr>
  </tbody>
</table>

<h3>10.2 Source-visible families that do not become primary execution objects by themselves</h3>

<p>
The following source-visible families may matter for source durability,
validation,
authoring,
or correspondence,
but do <strong>not</strong> become primary execution objects merely because they exist.
</p>

<table>
  <thead>
    <tr>
      <th>Source-visible family</th>
      <th>Default derivation shape</th>
      <th>Open-IR consequence</th>
      <th>What MUST remain respected</th>
      <th>What derivation MUST NOT do</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Interface declaration entry in <code>interface.inputs</code> / <code>interface.outputs</code></td>
      <td>1 -&gt; 0 or support-only</td>
      <td>No standalone primary execution object is required merely for the declaration record itself</td>
      <td>Public-port identity, type, connection-policy meaning where execution-relevant after validation, and consistency with interface-boundary participation</td>
      <td>Drop interface-port correspondence or invent independent execution meaning unrelated to interface participation</td>
    </tr>
    <tr>
      <td>Input default or interface-side connection-policy metadata</td>
      <td>1 -&gt; 0 or support-only</td>
      <td>No standalone primary execution object is required merely for the metadata record itself</td>
      <td>Its validated relation to interface participation and boundary semantics where applicable</td>
      <td>Invent runtime-private semantics not justified by validated meaning or silently erase required execution-relevant boundary metadata</td>
    </tr>
    <tr>
      <td><code>front_panel</code> container</td>
      <td>1 -&gt; 0 or support-only</td>
      <td>No primary execution object is required for the source container itself</td>
      <td>Its ownership relation to widget declarations and its distinction from executable diagram content</td>
      <td>Promote the front-panel container itself to a primary execution object merely because the source owns widgets</td>
    </tr>
    <tr>
      <td>Front-panel widget declaration with no validated execution participation</td>
      <td>1 -&gt; 0</td>
      <td>No primary execution object is required</td>
      <td>Its non-participation must not be misread as execution semantics</td>
      <td>Force every widget into execution-facing IR merely because it exists in source</td>
    </tr>
    <tr>
      <td>Front-panel widget declaration later referenced through <code>widget_value</code> or <code>widget_reference</code></td>
      <td>1 -&gt; 0 or support-only</td>
      <td>The widget declaration itself need not become a primary execution object; its identity may be referenced by derived UI participation objects</td>
      <td>Referenced widget identity and correspondence between declaration and participation</td>
      <td>Collapse declaration identity or confuse declaration identity with participation identity</td>
    </tr>
    <tr>
      <td>Layout, geometry, styling, and annotation placement records</td>
      <td>1 -&gt; 0</td>
      <td>No execution-facing object</td>
      <td>Authoring information may remain in source-oriented tooling layers</td>
      <td>Promote editor-only presentation state into execution semantics</td>
    </tr>
    <tr>
      <td>Icon, documentation, tags, and other non-execution descriptive records</td>
      <td>1 -&gt; 0</td>
      <td>No execution-facing object</td>
      <td>Non-execution descriptive meaning remains in its owning source or documentation layer</td>
      <td>Convert descriptive metadata into execution-visible semantics without separate normative authorization</td>
    </tr>
    <tr>
      <td>Editor-only preferences, cache, or transient tooling records</td>
      <td>1 -&gt; 0</td>
      <td>No execution-facing object</td>
      <td>Their absence from open IR must not change validated execution meaning</td>
      <td>Treat editor or cache state as part of validated execution truth</td>
    </tr>
  </tbody>
</table>

<p>
The absence of a family from the execution-relevant table does not make it execution-relevant.
Conversely,
a family that does not derive to a primary execution object may still matter for validation,
attribution,
or boundary correspondence.
</p>

<hr />

<h2 id="identity-and-attribution-rules">11. Identity and Attribution Rules</h2>

<p>
Source attribution is mandatory.
Every execution-visible IR object MUST preserve enough information to identify the validated source-visible contributor or contributors from which it was derived.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>a directly preserved object SHOULD carry one stable source-identity relation,</li>
  <li>a 1 -&gt; n derivation MUST preserve which support objects belong to which primary contributor,</li>
  <li>an n -&gt; 1 restricted aggregation MUST preserve explicit contributor attribution,</li>
  <li>a 1 -&gt; 0 omission is allowed only for content that does not become a primary execution object,</li>
  <li>a conforming implementation MUST NOT collapse multiple independently attributable execution-visible contributors into one opaque generated object.</li>
</ul>

<p>
At minimum,
base v0.1 requires recoverability of the following distinctions whenever they are present:
</p>

<ul>
  <li>document identity versus execution-unit identity,</li>
  <li><code>interface_input</code> versus <code>interface_output</code>,</li>
  <li><code>widget_value</code> versus <code>widget_reference</code>,</li>
  <li><code>widget_reference</code> participation versus standardized UI-object primitive operation,</li>
  <li>public interface participation versus UI participation,</li>
  <li><code>widget_value</code> participation versus property-based access to member <code>value</code>,</li>
  <li>structured family identity,</li>
  <li>owned region identity,</li>
  <li>structure-boundary participation,</li>
  <li>explicit structure-terminal roles,</li>
  <li>explicit local-memory identity,</li>
  <li>sub-FROG invocation identity.</li>
</ul>

<pre><code>Recoverability obligations

document / execution-unit relation remains explicit
interface_input / interface_output remain distinct
widget_value / widget_reference remain distinct
widget_reference / UI-object primitive remain distinct
public interface / UI participation remain distinct
widget_value / property(value) remain distinct
structure family remains distinct
regions remain attributable
structure terminals remain classifiable
explicit memory remains explicit
invocation identity remains recoverable
</code></pre>

<p>
This document does not freeze one identifier syntax.
It requires recoverable cross-layer identity at the derivation boundary.
Broader cross-stage identity architecture remains owned by <code>IR/Identity and Mapping.md</code>.
</p>

<hr />

<h2 id="connectivity-derivation">12. Connectivity Derivation</h2>

<p>
Execution-relevant connectivity MUST be explicit in the derived IR.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>every derived execution-facing object MUST expose explicit typed ports or equivalent explicit terminal interfaces,</li>
  <li>port direction MUST be explicit,</li>
  <li>directed connections MUST be explicit,</li>
  <li>connection endpoints MUST resolve to attributable execution-facing objects and attributable ports or terminals,</li>
  <li>the derived connectivity graph MUST preserve the validated dependency structure of the program.</li>
</ul>

<p>
Derivation MAY make the following already-validated facts explicit:
</p>

<ul>
  <li>resolved port type,</li>
  <li>resolved port direction,</li>
  <li>resolved boundary-terminal classification,</li>
  <li>resolved interface-boundary role,</li>
  <li>resolved widget participation role,</li>
  <li>resolved structured-boundary ownership,</li>
  <li>resolved standardized UI-object primitive role.</li>
</ul>

<p>
Cross-scope communication MUST remain explicit.
A region-local connection MUST NOT silently bypass the structure boundary.
A connection involving structure-boundary participation MUST preserve which side of the structured boundary it belongs to.
A connection involving standardized UI-object primitives MUST remain attributable both to the primitive operation and to the participating widget-reference path.
</p>

<pre><code>validated dependency structure
        |
        v
explicit ports / terminals
explicit direction
explicit directed connections
attributable endpoints

Cross-scope rule:
region-local content
   MUST NOT
silently bypass structure boundary
</code></pre>

<hr />

<h2 id="structured-control-derivation">13. Structured Control Derivation</h2>

<p>
Structured control remains explicit in the base open Execution IR.
</p>

<p>
A validated <code>structure</code> node MUST derive to one structured execution object that preserves:
</p>

<ul>
  <li>the standardized structure family,</li>
  <li>owned executable regions,</li>
  <li>structure-boundary inputs and outputs,</li>
  <li>structure terminals where applicable,</li>
  <li>source attribution for region-local execution content.</li>
</ul>

<p>
For base v0.1:
</p>

<ul>
  <li><code>case</code> MUST remain distinguishable as a structured region-selection object,</li>
  <li><code>for_loop</code> MUST remain distinguishable as a counted-iteration object,</li>
  <li><code>while_loop</code> MUST remain distinguishable as a condition-governed iteration object.</li>
</ul>

<p>
The open IR MUST NOT flatten those structure families into target-specific branch graphs,
generic CFG nodes,
or backend-private loop machinery in a way that makes family identity,
region correspondence,
or structure-terminal correspondence non-recoverable.
</p>

<p>
For structures with region-specific metadata,
the derived IR MUST preserve enough information to recover:
</p>

<ul>
  <li>which regions belong to which structure,</li>
  <li>which boundary terminals cross the structure wall,</li>
  <li>which terminals are structure-intrinsic rather than ordinary boundary values,</li>
  <li>which region-local graph content belongs to which source region.</li>
</ul>

<p>
Base v0.1 does not require one universal nested-region encoding.
It requires explicit structured ownership and semantic recoverability compatible with the canonical IR document model.
</p>

<pre><code>validated structure family
        |
        v
structured execution object
        ├── explicit owned regions
        ├── explicit boundary terminals or equivalent structured ports
        ├── explicit structure terminals where applicable
        └── region-local attribution

Allowed:
explicit structured IR
support objects that clarify regions or terminals

Forbidden:
opaque backend-shaped flattening
</code></pre>

<hr />

<h2 id="interface-and-ui-derivation">14. Interface and UI Derivation</h2>

<p>
The open Execution IR MUST preserve the distinction between:
</p>

<ul>
  <li>public interface participation,</li>
  <li>widget primary-value participation,</li>
  <li>widget object-style reference participation,</li>
  <li>standardized UI-object primitive operation performed through a widget reference.</li>
</ul>

<p>
Therefore:
</p>

<ul>
  <li><code>interface_input</code> and <code>interface_output</code> MUST remain recognizable as public boundary participation,</li>
  <li><code>widget_value</code> MUST remain recognizable as front-panel primary-value participation,</li>
  <li><code>widget_reference</code> MUST remain recognizable as object-style widget access participation,</li>
  <li><code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code> MUST remain recognizable as primitive execution objects rather than being absorbed into reference participation,</li>
  <li>derivation MUST NOT merge those families into one undifferentiated endpoint or generic object-access model without preserving their distinct semantic roles.</li>
</ul>

<p>
Additional rules:
</p>

<ul>
  <li>interface declarations and diagram-side interface nodes MUST remain coherently related,</li>
  <li>front-panel widgets that do not participate in validated meaning MUST NOT be forced into primary execution-facing IR objects merely because they exist in source,</li>
  <li>the <code>front_panel</code> source container itself MUST NOT become a primary execution-facing object merely because it owns widget declarations,</li>
  <li>widget declarations referenced by validated participation MUST remain recoverably linked to their participation objects,</li>
  <li>widget references used together with <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, or <code>frog.ui.method_invoke</code> MUST remain distinguishable from ordinary dataflow values,</li>
  <li>the base widget-reference token MUST NOT be reinterpreted as unrestricted general-purpose storage or computation unless a future specification explicitly standardizes that meaning,</li>
  <li><code>widget_value</code> MUST NOT be normalized into property-based access to member <code>value</code>,</li>
  <li>property-based access to member <code>value</code> MUST NOT be normalized into <code>widget_value</code> participation.</li>
</ul>

<pre><code>public interface participation
   !=
widget primary-value participation
   !=
widget object-style reference participation
   !=
standardized UI-object primitive operation
</code></pre>

<hr />

<h2 id="state-and-cycle-preservation">15. State and Cycle Preservation</h2>

<p>
Explicit local memory remains explicit in derivation.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>a validated local-memory primitive such as <code>frog.core.delay</code> MUST derive to an explicit attributable execution-facing object,</li>
  <li>required execution-relevant configuration such as mandatory explicit initial state MUST remain recoverable,</li>
  <li>a valid feedback path remains valid in the IR only because explicit memory remains present,</li>
  <li>derivation MUST NOT legalize an otherwise invalid combinational cycle by silently inserting hidden implicit memory,</li>
  <li>derivation MUST NOT erase the attribution of explicit memory in a valid stateful cycle.</li>
</ul>

<p>
The open IR inherits validated cycle legality from the language-level rules.
It does not invent a new cycle-validity rule.
</p>

<pre><code>valid feedback
   requires
explicit local memory

therefore

derived IR
   must preserve
explicit memory identity
explicit initial-state recoverability

Forbidden:
hidden implicit memory legalization
</code></pre>

<hr />

<h2 id="allowed-normalization-during-derivation">16. Allowed Normalization During Derivation</h2>

<p>
Derivation MAY normalize validated meaning in execution-facing ways that do not change semantic truth.
</p>

<p>
Allowed normalization includes:
</p>

<ul>
  <li>making resolved port types explicit,</li>
  <li>making resolved port directions explicit,</li>
  <li>making structure-boundary terminals explicit,</li>
  <li>making structure-terminal roles explicit,</li>
  <li>making region ownership explicit,</li>
  <li>materializing support objects for execution-facing classification,</li>
  <li>adding explicit source-attribution records,</li>
  <li>adding contributor records for permitted restricted aggregations,</li>
  <li>normalizing equivalent validated source spellings into one execution-facing canonical representation,</li>
  <li>carrying validated execution-relevant metadata in normalized explicit form,</li>
  <li>normalizing derivation output so that it is compatible with the canonical document and canonical JSON schema surface.</li>
</ul>

<p>
Allowed normalization is subject to all of the following conditions:
</p>

<ul>
  <li>semantic equivalence MUST be preserved,</li>
  <li>source attribution MUST remain recoverable,</li>
  <li>explicit memory MUST remain explicit,</li>
  <li>structured control MUST remain structurally recoverable,</li>
  <li>public interface participation and UI participation MUST remain distinguishable,</li>
  <li><code>widget_value</code> participation and property-based member access MUST remain distinguishable,</li>
  <li><code>widget_reference</code> participation and standardized UI-object primitives MUST remain distinguishable,</li>
  <li>support objects MUST NOT be used as a loophole for semantic transformation.</li>
</ul>

<pre><code>Allowed normalization

make already-validated facts explicit
add explicit support objects
add attribution structure
add contributor structure where permitted
normalize equivalent validated spellings
normalize toward canonical document compatibility

Only if:
meaning preserved
attribution preserved
explicit memory preserved
structured control recoverable
interface / UI distinction preserved
widget_value / property(value) distinction preserved
widget_reference / UI-primitive distinction preserved
</code></pre>

<hr />

<h2 id="forbidden-derivation-outcomes">17. Forbidden Derivation Outcomes</h2>

<p>
The following outcomes are forbidden in the base open Execution IR of v0.1:
</p>

<ul>
  <li>changing validated execution meaning,</li>
  <li>removing attribution for execution-visible objects,</li>
  <li>collapsing multiple independently attributable execution-visible contributors into one opaque unattributable generated object,</li>
  <li>replacing explicit memory with hidden scheduler-private state,</li>
  <li>flattening structured control so aggressively that family identity, region correspondence, or boundary-terminal correspondence is no longer recoverable,</li>
  <li>collapsing public interface participation, widget-value participation, widget-reference participation, and standardized UI-object primitive operation into one undifferentiated concept,</li>
  <li>normalizing <code>widget_value</code> participation into property access to member <code>value</code>,</li>
  <li>normalizing property access to member <code>value</code> into <code>widget_value</code> participation,</li>
  <li>forcing non-participating source families into primary execution objects merely because they exist in canonical source,</li>
  <li>promoting layout, styling, annotation placement, or similar authoring convenience state into execution semantics,</li>
  <li>treating the open IR as a debugger trace, runtime history log, or event stream,</li>
  <li>hard-coding one private runtime scheduling strategy as though it were the standardized open IR,</li>
  <li>deriving multiple competing canonical Execution IR Documents for one validated program at the same open IR boundary.</li>
</ul>

<pre><code>Forbidden outcomes

semantic drift
lost attribution
opaque unattributable aggregation
hidden scheduler-private memory
unrecoverable control flattening
collapsed interface / UI roles
collapsed widget_reference / UI-primitive roles
widget_value / property(value) collapse
forced executionization of non-participating source content
editor-state semantics
runtime trace substitution
private scheduler policy as open IR
multiple competing canonical IR documents
</code></pre>

<hr />

<h2 id="relation-with-construction-schema-lowering-and-backend-contract">18. Relation with Construction, Schema, Lowering, and Backend Contract</h2>

<p>
The output of derivation is the <strong>canonical Execution IR Document boundary result</strong>.
It is not yet a lowered form and not yet a backend-facing contract artifact.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>derivation MUST stop at the open IR boundary defined by <code>IR/Execution IR.md</code>,</li>
  <li>material build procedure and canonical JSON emission belong to <code>IR/Construction rules.md</code>,</li>
  <li>machine-checkable payload validation belongs to <code>IR/Schema.md</code> and <code>IR/schema/</code>,</li>
  <li>later target-oriented specialization belongs to <code>IR/Lowering.md</code>,</li>
  <li>later consumer-facing assumptions belong to <code>IR/Backend contract.md</code>,</li>
  <li>derivation MUST NOT prematurely encode backend-private scheduling, partitioning, storage layout, target-profile assumptions, deployment-mode assumptions, or target ABI policy as if those belonged to the base open IR.</li>
</ul>

<p>
Later layers MAY consume support metadata,
classification records,
or source-attribution records introduced during derivation,
but those later consumer expectations do not belong to this document.
</p>

<pre><code>validated program meaning
        |
        v
derivation
        |
        v
canonical Execution IR boundary result
        |
        +-- construction materializes canonical JSON payload
        |
        +-- schema validates canonical JSON payload
        |
        v
lowering
        |
        v
backend contract
        |
        v
private realization
</code></pre>

<p>
This separation matters because:
</p>

<ul>
  <li>derivation is about correspondence,</li>
  <li>construction is about material build,</li>
  <li>schema is about machine-checkable structural validation,</li>
  <li>lowering is about specialization,</li>
  <li>backend contract is about later standardized consumer expectations.</li>
</ul>

<p>
Those layers MUST NOT be collapsed into one another.
</p>

<hr />

<h2 id="out-of-scope-for-v01">19. Out of Scope for v0.1</h2>

<p>
The following topics are out of scope for this document in base v0.1:
</p>

<ul>
  <li>the exact procedural construction order used by every implementation,</li>
  <li>the full JSON schema text,</li>
  <li>mandatory SSA conversion,</li>
  <li>mandatory aggressive flattening of structured control,</li>
  <li>lowering to backend-facing contracts,</li>
  <li>runtime-private scheduler structures,</li>
  <li>compiled artifact formats,</li>
  <li>deployment packaging,</li>
  <li>debugger transport, eventing, or live observability protocols.</li>
</ul>

<p>
Those concerns belong to construction,
schema,
identity and mapping,
lowering,
backend contract,
runtime,
or IDE-facing specifications.
</p>

<p>
What is <strong>not</strong> out of scope anymore is:
</p>

<ul>
  <li>the rule that one validated program derives to one canonical Execution IR Document,</li>
  <li>the rule that the derivation result must be compatible with the canonical JSON open IR surface,</li>
  <li>the rule that derivation must preserve the distinctions needed by the published schema-visible IR categories.</li>
</ul>

<hr />

<h2 id="summary">20. Summary</h2>

<p>
Execution IR derivation in FROG v0.1 is conservative by design.
It starts from <strong>validated program meaning</strong>, not from raw source convenience.
It produces <strong>one canonical Execution IR Document per validated FROG</strong>, with <strong>one execution unit</strong>.
It preserves:
</p>

<ul>
  <li>validated executable meaning,</li>
  <li>source attribution,</li>
  <li>recoverable identity,</li>
  <li>structured control,</li>
  <li>explicit memory,</li>
  <li>validated dependency structure,</li>
  <li>the distinction between interface participation and UI participation,</li>
  <li>the distinction between <code>widget_value</code> and <code>widget_reference</code>,</li>
  <li>the distinction between <code>widget_reference</code> and standardized UI-object primitive operation.</li>
</ul>

<p>
It allows execution-facing explicitness and normalization,
but it forbids:
</p>

<ul>
  <li>semantic drift,</li>
  <li>opaque collapse,</li>
  <li>loss of attribution,</li>
  <li>runtime-private leakage.</li>
</ul>

<p>
It also fixes an important boundary in base v0.1:
not every source-visible family becomes a primary execution object.
Some families derive directly,
some derive with support objects,
and some remain source-visible but non-primary at the open-IR boundary.
That is true for front-panel ownership,
widget declarations,
and interface-side metadata as well.
</p>

<pre><code>validated FROG
   |
   +-- preserve executable meaning
   +-- preserve source attribution
   +-- preserve recoverable identity
   +-- preserve explicit memory
   +-- preserve structured control
   +-- preserve validated dependencies
   +-- preserve interface / UI distinction
   +-- preserve widget_value / widget_reference distinction
   +-- preserve widget_reference / UI-primitive distinction
   +-- do not executionize non-execution source content
   +-- derive one canonical IR document with one execution unit
   |
   v
canonical Execution IR Document
</code></pre>
