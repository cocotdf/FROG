<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG IR Derivation Rules</h1>

<p align="center">
  Normative derivation rules from validated FROG program meaning to open Execution IR<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#reading-legend">2. Reading Legend</a></li>
  <li><a href="#scope">3. Scope of this Document</a></li>
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
  <li><a href="#relation-with-construction-lowering-and-backend-contract">18. Relation with Construction, Lowering, and Backend Contract</a></li>
  <li><a href="#out-of-scope-for-v01">19. Out of Scope for v0.1</a></li>
  <li><a href="#summary">20. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the <strong>normative derivation boundary</strong> between
<strong>validated FROG program meaning</strong> and the <strong>open Execution IR</strong>.
It specifies:
</p>

<ul>
  <li>which validated execution-relevant source families derive to execution-facing IR families,</li>
  <li>which source-side distinctions MUST remain recoverable at the derivation boundary,</li>
  <li>which support objects MAY be introduced to make already-validated execution structure explicit,</li>
  <li>which source-visible families do not become primary execution objects in the open IR,</li>
  <li>which transformations are allowed as derivation-time normalization, and</li>
  <li>which transformations are forbidden because they would blur ownership, erase attribution, or introduce runtime-private meaning too early.</li>
</ul>

<p>
This document is intentionally about <strong>correspondence obligations</strong>.
It is not the full source specification, not the full language semantics specification,
not the complete Execution IR object-model specification,
not the construction algorithm for every implementation,
and not a runtime-private realization guide.
</p>

<p>
Compact mental model:
</p>

<pre><code>🟦 canonical source
        |
        v
🟩 validated program meaning
        |
        v
🟨 derivation rules   &lt;-- this document
        |
        v
🟦 open Execution IR
        |
        v
🟧 lowering / specialization
        |
        v
🟨 backend-facing contract
        |
        v
🟥 runtime-private realization
</code></pre>

<p>
In base v0.1, derivation is intentionally conservative.
It preserves validated meaning,
preserves recoverable identity,
preserves explicit structured control,
preserves explicit local memory,
preserves the distinction between public interface participation and UI participation,
and preserves the distinction between
<code>widget_value</code> participation,
<code>widget_reference</code> participation,
and UI-object operations expressed as standardized primitives.
</p>

<hr/>

<h2 id="reading-legend">2. Reading Legend</h2>

<ul>
  <li>🟦 <strong>Open specification-facing representation or layer</strong></li>
  <li>🟩 <strong>Semantic truth, attribution, recoverability, or validation result</strong></li>
  <li>🟨 <strong>Boundary, correspondence, mapping, or standardized handoff</strong></li>
  <li>🟧 <strong>Lowering, specialization, or target adaptation zone</strong></li>
  <li>🟥 <strong>Implementation-private or runtime-private realization zone</strong></li>
</ul>

<hr/>

<h2 id="scope">3. Scope of this Document</h2>

<p>
This document defines:
</p>

<ul>
  <li>the normative entry condition for Execution IR derivation,</li>
  <li>the relation shapes permitted at the derivation boundary,</li>
  <li>the base v0.1 correspondence between validated execution-relevant source families and Execution IR families,</li>
  <li>the minimum attribution and recoverability obligations that must survive derivation,</li>
  <li>the allowed and forbidden kinds of derivation-time explicitness and normalization.</li>
</ul>

<p>
This document does <strong>not</strong> define:
</p>

<ul>
  <li>the canonical source model in full,</li>
  <li>the full normative semantics of validated FROG programs,</li>
  <li>the full Execution IR object model in complete detail,</li>
  <li>the exact material build sequence of every implementation,</li>
  <li>the lowering strategy of every backend,</li>
  <li>the backend contract in full,</li>
  <li>the private scheduler, storage, or ABI policy of any runtime.</li>
</ul>

<pre><code>This document defines:
🟨 what must correspond
🟩 what must remain recoverable
🟦 what may be made explicit during derivation
🟥 what derivation must not silently change

This document does not define:
🟦 canonical source in full               -&gt; Expression/
🟩 validated program meaning in full      -&gt; Language/
🟦 full open IR model                     -&gt; Execution IR.md
🟦 material payload construction          -&gt; Construction rules.md
🟩 broader cross-stage mapping            -&gt; Identity and Mapping.md
🟧 later specialization                   -&gt; Lowering.md
🟨 later consumer-facing handoff          -&gt; Backend contract.md
🟥 runtime-private realization            -&gt; future implementation/runtime layers
</code></pre>

<hr/>

<h2 id="relation-with-other-specifications">4. Relation with Other Specifications</h2>

<p>
This document depends on the following ownership boundaries:
</p>

<ul>
  <li><code>Expression/</code> owns canonical source structure.</li>
  <li><code>Language/</code> owns normative execution meaning of validated programs.</li>
  <li><code>Libraries/</code> owns intrinsic primitive identities, primitive-local behavior, and primitive-port contracts.</li>
  <li><code>Profiles/</code> owns optional standardized capability families.</li>
  <li><code>IR/Execution IR.md</code> owns the architectural shape and invariants of the open Execution IR.</li>
  <li><code>IR/Identity and Mapping.md</code> owns broader recoverable cross-layer identity obligations.</li>
  <li><code>IR/Construction rules.md</code> owns the material construction of conforming open IR payloads.</li>
  <li><code>IR/Lowering.md</code> owns later target-oriented specialization.</li>
  <li><code>IR/Backend contract.md</code> owns the later backend-facing standardized handoff boundary.</li>
</ul>

<p>
Accordingly:
</p>

<ul>
  <li>this document MUST NOT redefine what a valid <code>.frog</code> file looks like,</li>
  <li>this document MUST NOT redefine what a validated program means,</li>
  <li>this document MUST NOT redefine the full Execution IR schema,</li>
  <li>this document MUST NOT redefine construction as a procedural algorithm,</li>
  <li>this document MUST NOT redefine backend-private or runtime-private structures,</li>
  <li>this document MUST define how validated program meaning becomes open execution-facing IR at the derivation boundary.</li>
</ul>

<p>
This document should be read together with:
</p>

<ul>
  <li><code>IR/Execution IR.md</code> — what the open Execution IR is and what it must preserve,</li>
  <li><code>IR/Identity and Mapping.md</code> — how recoverability survives across boundaries,</li>
  <li><code>IR/Construction rules.md</code> — how corresponding IR content is materially built,</li>
  <li><code>Expression/Diagram.md</code> — executable source graph families,</li>
  <li><code>Expression/Control structures.md</code> — source-facing structure families, regions, and terminals,</li>
  <li><code>Expression/State and cycles.md</code> — source-facing explicit memory and cycle constraints,</li>
  <li><code>Expression/Interface.md</code> — public interface declarations and interface connection policies,</li>
  <li><code>Expression/Front panel.md</code>, <code>Expression/Widget.md</code>, and <code>Expression/Widget interaction.md</code> — front-panel ownership, widget declaration, widget-value participation, widget-reference participation, and standardized UI-object primitives,</li>
  <li><code>Language/Control structures.md</code> and <code>Language/State and cycles.md</code> — semantics that derivation must preserve.</li>
</ul>

<pre><code>🟦 Expression/        -&gt; source shape
🟩 Language/          -&gt; semantic truth
🟦 Execution IR       -&gt; open IR model
🟨 Derivation         -&gt; correspondence obligations
🟦 Construction       -&gt; material build obligations
🟩 Identity/Mapping   -&gt; recoverable cross-layer identity
🟧 Lowering           -&gt; later specialization
🟨 Backend contract   -&gt; later standardized handoff
🟥 Runtime            -&gt; private realization
</code></pre>

<hr/>

<h2 id="derivation-boundary">5. Derivation Boundary</h2>

<p>
Execution IR derivation begins <strong>after validation</strong>.
The derivation input is not merely raw serialized source,
not merely editor convenience state,
and not merely partially edited authoring state.
The derivation input is the <strong>validated program meaning</strong> of one FROG program.
</p>

<p>
An implementation MAY internally start from:
</p>

<ul>
  <li>canonical source,</li>
  <li>a validated Program Model,</li>
  <li>another validated internal representation that is semantically equivalent.</li>
</ul>

<p>
However, the resulting open Execution IR MUST be grounded in validated program meaning rather than in editor-only convenience state,
partially edited transient state,
or runtime-private speculation.
</p>

<p>
Derivation is therefore not the place where an implementation invents hidden scheduler policy,
implied memory,
opaque backend partitions,
or runtime-private execution artifacts.
</p>

<pre><code>raw source -----------&gt; validation -----------&gt; derivation
                      outside this document      this document
</code></pre>

<pre><code>🟦 raw or editable form
        |
        v
🟩 validated program meaning
        |
        v
🟨 derivation boundary starts here
</code></pre>

<p>
This document does not require every implementation to expose the same pre-IR validation machinery.
It requires that, whatever internal route is used,
the produced open Execution IR be derivable from validated program meaning and faithful to it.
</p>

<hr/>

<h2 id="inputs-and-preconditions">6. Inputs and Preconditions</h2>

<p>
Before Execution IR derivation begins,
the program MUST already satisfy all applicable validation rules of base v0.1 and of all active standardized profiles.
</p>

<p>
At minimum, that includes:
</p>

<ul>
  <li>structural validation,</li>
  <li>type validation,</li>
  <li>primitive and structure-family validation,</li>
  <li>interface/diagram consistency validation,</li>
  <li>region and structure-boundary validation,</li>
  <li>structure-terminal validation,</li>
  <li>widget declaration and participation validation where applicable,</li>
  <li>UI primitive usage validation where applicable,</li>
  <li>cycle-validity validation,</li>
  <li>all other applicable source and semantic validation rules.</li>
</ul>

<p>
If those preconditions are not satisfied,
a conforming implementation MUST NOT claim to have produced a valid open Execution IR for that program.
</p>

<pre><code>Preconditions for derivation

🟩 validated structure
🟩 validated types
🟩 validated primitive usage
🟩 validated structure regions / terminals
🟩 validated interface consistency
🟩 validated widget participation
🟩 validated UI primitive usage
🟩 validated cycle legality

No validation
   -&gt;
No conforming open Execution IR
</code></pre>

<hr/>

<h2 id="derivation-result">7. Derivation Result</h2>

<p>
The result of derivation in base v0.1 is an <strong>Execution IR</strong> describing one validated FROG as one <strong>execution unit</strong>.
</p>

<p>
That execution unit MUST contain enough information to represent:
</p>

<ul>
  <li>execution-facing object identity,</li>
  <li>object family classification,</li>
  <li>typed ports or equivalent explicit terminal interfaces,</li>
  <li>directed connections,</li>
  <li>structured regions where applicable,</li>
  <li>boundary participation for public interface and UI participation,</li>
  <li>support objects where required to make already-validated execution structure explicit,</li>
  <li>mandatory attribution to validated source-visible execution content.</li>
</ul>

<p>
This document does not require one frozen mandatory wire format.
It requires a derivation result that is semantically equivalent,
attributable,
inspectable,
mapping-compatible,
and compatible with the invariants defined by <code>Execution IR.md</code>.
</p>

<pre><code>🟩 one validated FROG
        |
        v
🟦 one execution unit
        ├── 🟦 execution-facing objects
        ├── 🟦 typed ports / explicit terminals
        ├── 🟦 directed connections
        ├── 🟦 explicit regions where applicable
        ├── 🟨 explicit boundary participation
        ├── 🟦 support objects where required
        └── 🟩 source attribution
</code></pre>

<p>
The derivation result is the open IR layer input to later stages.
It is not yet a lowered target-facing form,
not yet a backend-facing contract artifact,
and not yet a runtime-private artifact.
</p>

<hr/>

<h2 id="core-derivation-invariants">8. Core Derivation Invariants</h2>

<p>
The following invariants apply to all conforming derivations in base v0.1:
</p>

<ul>
  <li>Derivation MUST preserve validated language meaning.</li>
  <li>Derivation MUST preserve attribution to validated source-visible execution content.</li>
  <li>Derivation MUST preserve enough structure and identity to satisfy later recoverable mapping obligations.</li>
  <li>Derivation MUST preserve explicit memory as explicit memory.</li>
  <li>Derivation MUST preserve structured control as structured control in the open IR.</li>
  <li>Derivation MUST preserve the distinction between public interface participation, widget-value participation, and widget-reference participation.</li>
  <li>Derivation MUST preserve the distinction between widget-reference participation and standardized UI-object primitives that consume widget references.</li>
  <li>Derivation MUST preserve the distinction between <code>widget_value</code> participation and property-based access to a widget member named <code>value</code>.</li>
  <li>Derivation MUST preserve the validated dependency structure of the executable graph.</li>
  <li>Derivation MUST NOT reinterpret non-execution source content as execution semantics merely because it exists in canonical source.</li>
  <li>Derivation MUST NOT import editor-only geometry, styling, annotation placement, or other presentation state as execution semantics.</li>
  <li>Derivation MUST NOT standardize one runtime-private scheduler strategy as if it were the open IR.</li>
</ul>

<pre><code>Core derivation invariants

🟩 preserve semantic truth
🟩 preserve source attribution
🟩 preserve recoverable identity
🟩 preserve explicit memory
🟩 preserve structured control
🟩 preserve interface / UI distinction
🟩 preserve widget-value / widget-reference distinction
🟩 preserve widget-reference / UI-primitive distinction
🟩 preserve validated dependencies
🟥 do not promote non-execution source content
🟥 do not import editor-only state
🟥 do not standardize private scheduler policy
</code></pre>

<hr/>

<h2 id="derivation-relation-shapes">9. Derivation Relation Shapes</h2>

<p>
Base v0.1 distinguishes four broad derivation relation shapes:
</p>

<ul>
  <li><strong>1 -&gt; 1 direct preservation</strong> — one validated source-visible execution-relevant object derives to one primary IR object,</li>
  <li><strong>1 -&gt; n expansion</strong> — one validated source-visible execution-relevant object derives to one primary IR object plus one or more support objects,</li>
  <li><strong>n -&gt; 1 restricted aggregation</strong> — multiple validated source-visible contributors derive to one generated support object, but only when all contributors remain explicitly attributable,</li>
  <li><strong>1 -&gt; 0 non-deriving source content</strong> — one source-visible object or record remains relevant to validation, attribution, or correspondence, but does not become a primary execution object in the open IR.</li>
</ul>

<p>
The first three shapes apply to execution-facing derived content.
The fourth shape applies to source-visible content that must remain respected at the boundary without being converted into a primary execution object.
</p>

<p>
Examples:
</p>

<ul>
  <li>a <code>primitive</code> node commonly derives by 1 -&gt; 1 direct preservation,</li>
  <li>a <code>structure</code> node commonly derives by 1 -&gt; n expansion because explicit regions or terminal support objects may be introduced,</li>
  <li>a validated interface declaration may derive support-only correspondence without becoming a standalone primary execution object,</li>
  <li>a non-participating widget declaration is typically 1 -&gt; 0 with respect to primary execution objects.</li>
</ul>

<pre><code>direct:
  🟩 source object A
      |
      v
  🟦 IR object A'

expanded:
  🟩 source object B
      |
      +------&gt; 🟦 IR primary object B'
      |
      +------&gt; 🟦 IR support object B1'
      |
      +------&gt; 🟦 IR support object B2'

restricted aggregated support:
  🟩 source object C -----\
                           +----&gt; 🟦 IR support object Cx'
  🟩 source object D -----/
  with explicit contributor attribution to C and D

non-deriving source content:
  🟩 source object E
      |
      +----&gt; no primary IR object
      |
      +----&gt; obligations may still survive through attribution,
             resolved metadata,
             or boundary correspondence
</code></pre>

<hr/>

<h2 id="source-to-ir-family-mapping">10. Source-to-IR Family Mapping</h2>

<p>
The following tables define the base v0.1 normative correspondence between validated source families and open Execution IR families.
These tables are about <strong>execution-facing derivation</strong>.
They do not imply that every source-visible family must become a primary execution object.
</p>

<h3>10.1 Execution-relevant source families</h3>

<table>
  <thead>
    <tr>
      <th>Validated source family</th>
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
      <td>One execution unit</td>
      <td>Unit-level attribution and classification records</td>
      <td>Program identity and execution-unit identity relation</td>
      <td>Split one validated FROG into multiple independent open-IR execution units in base v0.1</td>
    </tr>
    <tr>
      <td>Top-level executable diagram</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Top-level execution graph content of the execution unit</td>
      <td>Explicit top-level graph scope records if needed</td>
      <td>Top-level scope identity and contained-object attribution</td>
      <td>Hide top-level graph ownership or reinterpret it as an opaque backend-only graph</td>
    </tr>
    <tr>
      <td><code>primitive</code> node</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Primitive execution object</td>
      <td>Resolved port descriptors, explicit attribution records, explicit execution-facing classification records</td>
      <td>Primitive identity, resolved ports, execution-relevant metadata, source correspondence</td>
      <td>Replace the primitive with opaque runtime-private machinery or erase primitive identity in the base open IR</td>
    </tr>
    <tr>
      <td>Standardized UI object primitive (<code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, <code>frog.ui.method_invoke</code>)</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Primitive execution object of the standardized UI-object primitive family</td>
      <td>Resolved UI-port descriptors, resolved member or method descriptors, explicit UI-operation classification records, explicit source-map records</td>
      <td>Primitive identity, standardized UI-operation family, referenced member or method semantics, required <code>widget_reference</code> participation, source correspondence</td>
      <td>Absorb the primitive into the widget-reference object itself, or reinterpret the operation as generic unrestricted object execution outside the standardized primitive model</td>
    </tr>
    <tr>
      <td><code>subfrog</code> node</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Sub-FROG invocation object</td>
      <td>Resolved invocation-boundary descriptors, explicit source-map records</td>
      <td>Referenced FROG identity, invocation identity, invocation boundary, resolved ports</td>
      <td>Inline or flatten invocation so aggressively that invocation identity becomes non-recoverable in the base open IR</td>
    </tr>
    <tr>
      <td><code>interface_input</code> node</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Public interface entry boundary object</td>
      <td>Resolved interface-port descriptors, unit-boundary classification records, support-only policy/default metadata records where execution-relevant</td>
      <td>Public API role, referenced interface input, value direction, source correspondence</td>
      <td>Merge into a generic undifferentiated endpoint concept together with widget participation</td>
    </tr>
    <tr>
      <td><code>interface_output</code> node</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Public interface exit boundary object</td>
      <td>Resolved interface-port descriptors, unit-boundary classification records</td>
      <td>Public API role, referenced interface output, value direction, source correspondence</td>
      <td>Merge into a generic undifferentiated endpoint concept together with widget participation</td>
    </tr>
    <tr>
      <td><code>widget_value</code> node</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Widget-value participation object</td>
      <td>Resolved widget-value descriptors, widget role classification records</td>
      <td>Referenced widget identity, primary-value participation role, control/indicator directionality, source correspondence</td>
      <td>Collapse with public interface participation, reinterpret as object-style reference participation, or normalize into property access on a member named <code>value</code></td>
    </tr>
    <tr>
      <td><code>widget_reference</code> node</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Widget-reference participation object</td>
      <td>Resolved widget-reference descriptors, object-style access classification records</td>
      <td>Referenced widget identity, object-style access role, source correspondence</td>
      <td>Collapse into ordinary valueflow participation, reinterpret as unrestricted general-purpose storage, or absorb all standardized UI-object operations into the reference object itself</td>
    </tr>
    <tr>
      <td><code>structure</code> node</td>
      <td>1 -&gt; n</td>
      <td>Structured execution object</td>
      <td>Explicit region objects, explicit boundary-terminal records, explicit structure-terminal records, explicit structured-port descriptors, source-map records</td>
      <td>Structure family, owned regions, boundary crossing, structure-terminal roles, source correspondence</td>
      <td>Flatten immediately into backend-shaped opaque control machinery in a way that makes family identity or region ownership unrecoverable</td>
    </tr>
    <tr>
      <td>Structure region entry</td>
      <td>1 -&gt; 1</td>
      <td>Region object</td>
      <td>Region-local attribution records, explicit region classification records</td>
      <td>Region identity, owning structure, source-region identity, region-local graph ownership</td>
      <td>Hide region ownership or allow region-local content to lose source-region attribution</td>
    </tr>
    <tr>
      <td>Structure boundary input/output entry</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Explicit boundary terminal or explicit structured boundary-port form</td>
      <td>Terminal descriptors, attribution records, structured-boundary records</td>
      <td>Boundary crossing role, type, owning structure, source-side identity</td>
      <td>Allow cross-scope communication to bypass the structure wall implicitly</td>
    </tr>
    <tr>
      <td>Structure terminal entry</td>
      <td>1 -&gt; 1 or 1 -&gt; n</td>
      <td>Explicit structure terminal or explicit structured terminal-port form</td>
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

<h3>10.2 Source-visible families that do not derive to primary execution objects by themselves</h3>

<p>
The following kinds of source-visible content are relevant to source,
validation,
authoring,
or correspondence,
but do <strong>not</strong> derive to primary execution objects merely because they exist in source.
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
      <td>1 -&gt; 0 or 1 -&gt; n support-only</td>
      <td>No standalone primary execution object is required merely for the declaration record itself</td>
      <td>Public port identity, type, connection-policy meaning where execution-relevant after validation, and consistency with interface boundary participation</td>
      <td>Drop interface-port correspondence or invent independent execution meaning unrelated to public interface participation</td>
    </tr>
    <tr>
      <td>Input default or interface-side connection-policy metadata</td>
      <td>1 -&gt; 0 or support-only</td>
      <td>No standalone primary execution object is required merely for the metadata record itself</td>
      <td>Its validated relation to interface participation and boundary semantics where applicable</td>
      <td>Invent runtime-private semantics not justified by validated program meaning, or silently erase required execution-relevant boundary metadata</td>
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
      <td>Collapse declaration identity or confuse declaration identity with participation object identity</td>
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
      <td>Non-execution descriptive meaning belongs to its owning source or documentation layer</td>
      <td>Convert descriptive metadata into execution-visible semantics without a separate normative specification</td>
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
The absence of a source-visible family from the execution-relevant table does not automatically make it execution-relevant.
Conversely,
a family that does not derive to a primary execution object may still matter for validation,
source attribution,
or boundary correspondence.
</p>

<pre><code>Family mapping principle

🟩 validated execution-relevant source family
        |
        v
🟦 corresponding execution-facing IR family
        |
        +--&gt; 🟩 recoverable attribution
        +--&gt; 🟦 possible support objects

non-execution or non-primary source family
        |
        v
no primary execution object
        |
        +--&gt; may still matter for attribution,
             boundary correspondence,
             or support-only metadata
</code></pre>

<hr/>

<h2 id="identity-and-attribution-rules">11. Identity and Attribution Rules</h2>

<p>
Source attribution is mandatory.
Every execution-visible IR object MUST preserve enough information to identify the validated source-visible object or objects from which it was derived.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>a directly preserved object SHOULD carry one stable source-identity relation,</li>
  <li>a 1 -&gt; n derivation MUST preserve which support objects belong to which primary source-visible contributor,</li>
  <li>an n -&gt; 1 restricted aggregation MUST preserve explicit contributor attribution,</li>
  <li>a 1 -&gt; 0 omission is allowed only for content that does not become a primary execution object in the open IR,</li>
  <li>a conforming implementation MUST NOT collapse multiple independently attributable primary source-visible execution objects into one opaque generated object.</li>
</ul>

<p>
At minimum,
base v0.1 requires recoverability of the following distinctions whenever they are present in validated meaning:
</p>

<ul>
  <li><code>interface_input</code> versus <code>interface_output</code>,</li>
  <li><code>widget_value</code> versus <code>widget_reference</code>,</li>
  <li>widget-reference participation versus standardized UI-object primitive operation,</li>
  <li>public interface participation versus UI participation,</li>
  <li><code>widget_value</code> participation versus property-based access to a widget member named <code>value</code>,</li>
  <li>structured family identity,</li>
  <li>owned region identity,</li>
  <li>structure-boundary participation,</li>
  <li>explicit structure-terminal roles,</li>
  <li>explicit local-memory identity,</li>
  <li>sub-FROG invocation identity.</li>
</ul>

<pre><code>Recoverability obligations

🟩 interface_input / interface_output remain distinct
🟩 widget_value / widget_reference remain distinct
🟩 widget_reference / UI-object primitive remain distinct
🟩 public interface / UI participation remain distinct
🟩 widget_value / property(value) remain distinct
🟩 structure family remains distinct
🟩 regions remain attributable
🟩 structure terminals remain classifiable
🟩 explicit memory remains explicit
🟩 invocation identity remains recoverable
</code></pre>

<p>
This document does not freeze one identifier syntax.
It requires recoverable cross-layer identity at the derivation boundary.
Broader cross-stage identity architecture remains owned by <code>Identity and Mapping.md</code>.
</p>

<hr/>

<h2 id="connectivity-derivation">12. Connectivity Derivation</h2>

<p>
Execution-relevant connectivity MUST be explicit in the derived IR.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>every derived execution-facing object MUST expose explicit typed ports or an equivalent explicit terminal interface,</li>
  <li>port direction MUST be explicit in the IR,</li>
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
A connection involving standardized UI-object primitives MUST remain attributable to both the primitive operation and the participating widget-reference path.
</p>

<pre><code>Connectivity derivation

🟩 validated dependency structure
        |
        v
🟦 explicit ports / terminals
🟦 explicit direction
🟦 explicit directed connections
🟩 attributable endpoints

Cross-scope rule:
region-local content
   MUST NOT
silently bypass structure boundary
</code></pre>

<hr/>

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
  <li>source attribution for region-local executable content.</li>
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
Base v0.1 does not require one universal low-level nested-region encoding.
It requires explicit structured ownership and semantic recoverability.
</p>

<pre><code>🟩 validated structure family
        |
        v
🟦 structured execution object
        ├── 🟦 explicit owned regions
        ├── 🟨 explicit boundary terminals or equivalent structured ports
        ├── 🟨 explicit structure terminals where applicable
        └── 🟩 region-local attribution

Allowed:
🟦 explicit structured IR
🟦 support objects that clarify regions or terminals

Forbidden:
🟥 opaque backend-shaped flattening
</code></pre>

<hr/>

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
  <li>derivation MUST NOT merge those families into one undifferentiated generic endpoint or generic object-access model without preserving their recoverable semantic roles.</li>
</ul>

<p>
Additional rules:
</p>

<ul>
  <li>interface declarations and diagram-side interface nodes MUST remain coherently related,</li>
  <li>front-panel widgets that do not participate in validated program meaning MUST NOT be forced into primary execution-facing IR objects merely because they exist in source,</li>
  <li>the <code>front_panel</code> source container itself MUST NOT become a primary execution-facing object merely because it owns widget declarations,</li>
  <li>widget declarations that are referenced by validated diagram participation MUST remain recoverably linked to their participation objects,</li>
  <li>widget references used together with <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, or <code>frog.ui.method_invoke</code> MUST remain distinguishable from ordinary dataflow values,</li>
  <li>the base widget-reference token MUST NOT be reinterpreted by derivation as an unrestricted general-purpose storage or computation value unless a future specification explicitly standardizes that meaning,</li>
  <li><code>widget_value</code> MUST NOT be normalized into property-based access to member <code>value</code>,</li>
  <li>property-based access to member <code>value</code> MUST NOT be normalized into <code>widget_value</code> participation.</li>
</ul>

<pre><code>Boundary distinction

🟨 public interface participation
   !=
🟦 widget primary-value participation
   !=
🟦 widget object-style reference participation
   !=
🟦 standardized UI-object primitive operation
</code></pre>

<hr/>

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
For cycle handling,
the open IR inherits validated cycle legality from the language-level rules.
It does not invent a new cycle-validity rule.
</p>

<pre><code>Cycle preservation rule

🟩 valid feedback
   requires
🟩 explicit local memory

therefore

🟦 derived IR
   must preserve
🟩 explicit memory identity
🟩 explicit initial-state recoverability

Forbidden:
🟥 hidden implicit memory legalization
</code></pre>

<hr/>

<h2 id="allowed-normalization-during-derivation">16. Allowed Normalization During Derivation</h2>

<p>
Derivation MAY normalize validated program meaning in execution-facing ways that do not change semantic truth.
</p>

<p>
Examples of allowed normalization include:
</p>

<ul>
  <li>making resolved port types explicit,</li>
  <li>making resolved port directions explicit,</li>
  <li>making structure-boundary terminals explicit,</li>
  <li>making structure-terminal roles explicit,</li>
  <li>making region ownership explicit,</li>
  <li>materializing support objects for execution-facing classification,</li>
  <li>adding explicit source-attribution records,</li>
  <li>adding explicit contributor records for permitted restricted aggregations,</li>
  <li>normalizing equivalent validated source spellings into one execution-facing canonical representation,</li>
  <li>carrying validated execution-relevant metadata in normalized explicit form.</li>
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
  <li>widget-reference participation and standardized UI-object primitives MUST remain distinguishable,</li>
  <li>support objects MUST NOT be used as a loophole for semantic transformation.</li>
</ul>

<pre><code>Allowed normalization

✔ make already-validated facts explicit
✔ add explicit support objects
✔ add attribution structure
✔ add contributor structure where permitted
✔ normalize equivalent validated spellings

Only if:
🟩 meaning preserved
🟩 attribution preserved
🟩 explicit memory preserved
🟩 structured control recoverable
🟩 interface / UI distinction preserved
🟩 widget-value / property(value) distinction preserved
🟩 widget-reference / UI-primitive distinction preserved
</code></pre>

<hr/>

<h2 id="forbidden-derivation-outcomes">17. Forbidden Derivation Outcomes</h2>

<p>
The following outcomes are forbidden in the base open Execution IR of v0.1:
</p>

<ul>
  <li>changing validated language-level execution meaning,</li>
  <li>removing attribution for execution-visible objects,</li>
  <li>collapsing multiple primary source-visible execution objects into one opaque unattributable generated object,</li>
  <li>replacing explicit memory with hidden scheduler-private state,</li>
  <li>flattening structured control so aggressively that family identity, region correspondence, or boundary-terminal correspondence is no longer recoverable,</li>
  <li>collapsing public interface participation, widget-value participation, widget-reference participation, and standardized UI-object primitive operation into one untyped undifferentiated concept,</li>
  <li>normalizing <code>widget_value</code> participation into property access to member <code>value</code>,</li>
  <li>normalizing property access to member <code>value</code> into <code>widget_value</code> participation,</li>
  <li>forcing non-participating source families into primary execution objects merely because they exist in canonical source,</li>
  <li>promoting editor-only layout, styling, annotation placement, or other authoring convenience state into execution semantics,</li>
  <li>treating the open IR as a debugger trace, runtime history log, or event stream,</li>
  <li>hard-coding one private runtime scheduling strategy as if it were the standardized open IR.</li>
</ul>

<pre><code>Forbidden outcomes

🟥 semantic drift
🟥 lost attribution
🟥 opaque unattributable aggregation
🟥 hidden scheduler-private memory
🟥 unrecoverable control flattening
🟥 collapsed interface / UI roles
🟥 collapsed widget-reference / UI-primitive roles
🟥 widget_value / property(value) collapse
🟥 forced executionization of non-participating source content
🟥 editor-state semantics
🟥 runtime trace substitution
🟥 private scheduler policy as open IR
</code></pre>

<hr/>

<h2 id="relation-with-construction-lowering-and-backend-contract">18. Relation with Construction, Lowering, and Backend Contract</h2>

<p>
The output of derivation is the <strong>open Execution IR</strong>.
It is not yet a lowered form and not yet a backend-facing contract artifact.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>derivation MUST stop at the open IR boundary defined by <code>Execution IR.md</code>,</li>
  <li>material build procedure belongs to <code>Construction rules.md</code>,</li>
  <li>later target-oriented specialization belongs to <code>Lowering.md</code>,</li>
  <li>later consumer-facing assumptions belong to <code>Backend contract.md</code>,</li>
  <li>derivation MUST NOT prematurely encode backend-private scheduling, partitioning, storage layout, or target ABI policy as if those belonged to the base open IR.</li>
</ul>

<p>
Later layers MAY consume support metadata,
support classification records,
or source-attribution records that were introduced during derivation,
but those later consumer expectations do not belong to this document.
</p>

<pre><code>🟩 validated program meaning
        |
        v
🟨 derivation
        |
        v
🟦 open Execution IR
        |
        +--&gt; 🟦 construction materializes conforming payloads
        |
        v
🟧 lowering
        |
        v
🟨 backend contract
        |
        v
🟥 private realization
</code></pre>

<p>
This separation matters because the derivation boundary is about <strong>correspondence</strong>.
Construction is about <strong>material build</strong>.
Lowering is about <strong>specialization</strong>.
Backend contract is about <strong>later standardized consumer expectations</strong>.
Those layers MUST NOT be collapsed into one another.
</p>

<hr/>

<h2 id="out-of-scope-for-v01">19. Out of Scope for v0.1</h2>

<p>
The following topics are out of scope for this document in base v0.1:
</p>

<ul>
  <li>one mandatory universal JSON transport schema for all implementations,</li>
  <li>the exact procedural construction order used by every implementation,</li>
  <li>mandatory SSA conversion,</li>
  <li>mandatory aggressive flattening of structured control,</li>
  <li>lowering to backend-facing contracts,</li>
  <li>runtime-private scheduler structures,</li>
  <li>compiled artifact formats,</li>
  <li>deployment packaging,</li>
  <li>debugger transport, eventing, or live observability protocols.</li>
</ul>

<p>
Those concerns belong to later documents such as construction,
identity and mapping,
lowering,
backend contract,
runtime,
or IDE-facing specifications.
</p>

<pre><code>Out of scope in v0.1

🟨 universal transport schema
🟦 exact construction procedure
🟥 mandatory SSA
🟥 mandatory aggressive flattening
🟧 backend-facing lowering contract
🟥 runtime-private scheduler structures
🟥 compiled artifact formats
🟥 deployment packaging
🟨 debugger / observability transport protocols
</code></pre>

<hr/>

<h2 id="summary">20. Summary</h2>

<p>
Execution IR derivation in FROG v0.1 is conservative by design.
It starts from <strong>validated program meaning</strong>, not from raw source convenience.
It produces <strong>one execution unit per validated FROG</strong>.
It preserves <strong>source attribution</strong>,
<strong>recoverable identity</strong>,
<strong>structured control</strong>,
<strong>explicit memory</strong>,
and the distinction between
<strong>public interface participation</strong>,
<strong>widget primary-value participation</strong>,
<strong>widget object-style reference participation</strong>,
and <strong>standardized UI-object primitive operation</strong>.
It allows execution-facing explicitness and normalization,
but it forbids semantic drift,
opaque collapse,
and runtime-private leakage.
</p>

<p>
This document also fixes an important boundary in base v0.1:
not every source-visible family becomes a primary execution object.
Some families derive directly,
some derive with support objects,
and some remain source-visible but non-primary at the open-IR boundary.
The same is true for front-panel ownership,
widget declarations,
and interface-side metadata:
they may remain relevant to attribution or boundary correspondence
without becoming primary execution objects.
</p>

<p>
In compact form:
</p>

<pre><code>🟩 validated FROG
   |
   +-- preserve executable meaning
   +-- preserve source attribution
   +-- preserve recoverable identity
   +-- preserve explicit memory
   +-- preserve structured control
   +-- preserve interface / UI distinction
   +-- preserve widget_value / widget_reference distinction
   +-- preserve widget_reference / UI-primitive distinction
   +-- do not executionize non-execution source content
   |
   v
🟦 open Execution IR
</code></pre>
