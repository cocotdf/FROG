<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG IR Derivation Rules</h1>

<p align="center">
  Normative derivation rules from validated FROG programs to open Execution IR<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope">2. Scope of this Document</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#derivation-boundary">4. Derivation Boundary</a></li>
  <li><a href="#inputs-and-preconditions">5. Inputs and Preconditions</a></li>
  <li><a href="#derivation-result">6. Derivation Result</a></li>
  <li><a href="#core-derivation-invariants">7. Core Derivation Invariants</a></li>
  <li><a href="#primary-derivation-units">8. Primary Derivation Units</a></li>
  <li><a href="#source-to-ir-family-mapping">9. Source-to-IR Family Mapping</a></li>
  <li><a href="#identity-and-attribution-rules">10. Identity and Attribution Rules</a></li>
  <li><a href="#connectivity-derivation">11. Connectivity Derivation</a></li>
  <li><a href="#structured-control-derivation">12. Structured Control Derivation</a></li>
  <li><a href="#interface-and-ui-derivation">13. Interface and UI Derivation</a></li>
  <li><a href="#state-and-cycle-preservation">14. State and Cycle Preservation</a></li>
  <li><a href="#allowed-normalization-during-derivation">15. Allowed Normalization During Derivation</a></li>
  <li><a href="#forbidden-derivation-outcomes">16. Forbidden Derivation Outcomes</a></li>
  <li><a href="#out-of-scope-for-v01">17. Out of Scope for v0.1</a></li>
  <li><a href="#summary">18. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines how a <strong>validated</strong> FROG program is normatively related to an open Execution IR.
It specifies <strong>what must be preserved</strong>, <strong>what may be made explicit</strong>, and
<strong>what must remain recoverable</strong> when execution-facing derived representation is built.
</p>

<p>
This document does <strong>not</strong> redefine canonical source structure, language meaning,
or runtime-private realization.
It defines the derivation boundary between validated FROG program meaning and open execution-facing IR.
</p>

<p>
Compact mental model:
</p>

<pre><code>🟦 canonical source
        |
        v
🟦 validated program meaning
        |
        v
🟨 derivation rules  &lt;-- this document
        |
        v
🟦 open Execution IR
        |
        v
🟧 lowering / backend mapping / compilation
        |
        v
🟥 runtime-private realization
</code></pre>

<hr/>

<h2 id="scope">2. Scope of this Document</h2>

<p>
This document defines:
</p>

<ul>
  <li>the normative entry condition for Execution IR derivation,</li>
  <li>the minimum mapping between validated FROG source-visible families and Execution IR families,</li>
  <li>the identity and attribution obligations that make source/IR correspondence recoverable,</li>
  <li>the derivation constraints that preserve control structure, interface/UI distinction, and explicit memory,</li>
  <li>the allowed and forbidden kinds of derivation-time normalization in base v0.1.</li>
</ul>

<p>
This document is intentionally narrower than a full IR transport schema and intentionally broader than one implementation-specific build algorithm.
</p>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This document depends on the following ownership boundaries:
</p>

<ul>
  <li><code>Expression/</code> owns canonical source structure.</li>
  <li><code>Language/</code> owns normative execution meaning of validated programs.</li>
  <li><code>Libraries/</code> owns intrinsic primitive identities, primitive ports, and primitive-local behavior.</li>
  <li><code>Profiles/</code> owns optional standardized capability families.</li>
  <li><code>IR/Execution IR.md</code> owns the architectural shape and invariants of the open Execution IR.</li>
</ul>

<p>
Accordingly:
</p>

<ul>
  <li>this document MUST NOT redefine what a valid <code>.frog</code> file looks like,</li>
  <li>this document MUST NOT redefine what a validated program means,</li>
  <li>this document MUST NOT redefine private runtime scheduler internals,</li>
  <li>this document MUST define how validated program meaning becomes open execution-facing IR.</li>
</ul>

<p>
This document should be read together with:
</p>

<ul>
  <li><code>IR/Execution IR.md</code> — what the open Execution IR must preserve,</li>
  <li><code>Expression/Diagram.md</code> — executable source graph families,</li>
  <li><code>Expression/Control structures.md</code> — source-facing structure boundaries, terminals, and regions,</li>
  <li><code>Expression/State and cycles.md</code> — source-facing explicit memory and cycle constraints,</li>
  <li><code>Language/Control structures.md</code> and <code>Language/State and cycles.md</code> — execution semantics that derivation must preserve.</li>
</ul>

<hr/>

<h2 id="derivation-boundary">4. Derivation Boundary</h2>

<p>
Execution IR derivation begins <strong>after validation</strong>.
The derivation input is not merely a raw serialized file.
The derivation input is the <strong>validated executable meaning</strong> of one FROG program.
</p>

<p>
An implementation MAY internally start from:
</p>

<ul>
  <li>canonical source,</li>
  <li>a validated Program Model,</li>
  <li>another validated internal form that is semantically equivalent.</li>
</ul>

<p>
However, the resulting Execution IR MUST be grounded in validated FROG meaning rather than in editor-only convenience state.
</p>

<p>
Derivation therefore begins at the following boundary:
</p>

<pre><code>raw source --------------------&gt; validation --------------------&gt; derivation
                               (outside this doc)                (this doc)
</code></pre>

<hr/>

<h2 id="inputs-and-preconditions">5. Inputs and Preconditions</h2>

<p>
Before Execution IR derivation begins, the program MUST already satisfy all applicable validation rules of base v0.1 and of all active standardized profiles.
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
  <li>widget participation validation where applicable,</li>
  <li>cycle-validity validation,</li>
  <li>all other applicable source and semantic validation rules.</li>
</ul>

<p>
If those preconditions are not satisfied, a conforming implementation MUST NOT claim to have produced a valid open Execution IR for that program.
</p>

<hr/>

<h2 id="derivation-result">6. Derivation Result</h2>

<p>
The result of derivation in base v0.1 is an <strong>Execution IR</strong> describing one validated FROG as one <strong>execution unit</strong>.
</p>

<p>
That execution unit MUST contain enough information to represent:
</p>

<ul>
  <li>execution-facing object identity,</li>
  <li>object family classification,</li>
  <li>typed ports,</li>
  <li>directed connections,</li>
  <li>structured regions where applicable,</li>
  <li>boundary participation for public interface and UI participation,</li>
  <li>mandatory source attribution.</li>
</ul>

<p>
This document does not require one frozen mandatory wire format.
It requires a derivation result that is semantically equivalent, attributable, inspectable, and compatible with the Execution IR invariants defined elsewhere.
</p>

<hr/>

<h2 id="core-derivation-invariants">7. Core Derivation Invariants</h2>

<p>
The following invariants apply to all conforming derivations in base v0.1:
</p>

<ul>
  <li>Derivation MUST preserve validated language meaning.</li>
  <li>Derivation MUST preserve attribution to validated source-visible execution content.</li>
  <li>Derivation MUST preserve explicit memory as explicit memory.</li>
  <li>Derivation MUST preserve structured control as structured control in the open IR.</li>
  <li>Derivation MUST preserve the distinction between public interface participation and UI participation.</li>
  <li>Derivation MUST preserve the validated dependency structure of the executable graph.</li>
  <li>Derivation MUST NOT import editor-only geometry, styling, or presentation state as execution semantics.</li>
  <li>Derivation MUST NOT standardize one runtime-private scheduler strategy as if it were the open IR.</li>
</ul>

<hr/>

<h2 id="primary-derivation-units">8. Primary Derivation Units</h2>

<p>
Base v0.1 distinguishes two broad categories of derived IR content:
</p>

<ul>
  <li><strong>primary derived objects</strong> — execution-facing objects corresponding directly to validated executable or boundary participation,</li>
  <li><strong>support objects</strong> — explicit IR-side helper objects introduced only to make already-validated execution-relevant structure more explicit.</li>
</ul>

<p>
Examples of primary derived objects include:
</p>

<ul>
  <li>primitive execution objects,</li>
  <li>structured execution objects,</li>
  <li>sub-FROG invocation objects,</li>
  <li>public interface boundary objects,</li>
  <li>widget-value participation objects,</li>
  <li>widget-reference participation objects.</li>
</ul>

<p>
Examples of support objects include:
</p>

<ul>
  <li>explicit region objects,</li>
  <li>explicit structure-boundary terminal objects,</li>
  <li>resolved port descriptors,</li>
  <li>explicit source-map entries,</li>
  <li>other execution-facing classification records that do not alter meaning.</li>
</ul>

<p>
Support objects MUST NOT be used as a loophole for semantic transformation.
They MAY make meaning more explicit.
They MUST NOT replace meaning with runtime-private policy.
</p>

<hr/>

<h2 id="source-to-ir-family-mapping">9. Source-to-IR Family Mapping</h2>

<p>
The minimum source-to-IR mapping for base v0.1 is as follows.
</p>

<table>
  <thead>
    <tr>
      <th>Validated source family</th>
      <th>Primary IR result</th>
      <th>What MUST remain recoverable</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Whole validated FROG</td>
      <td>One execution unit</td>
      <td>Program identity and execution-unit identity relation</td>
      <td>One validated FROG -&gt; one execution unit in base open IR</td>
    </tr>
    <tr>
      <td>Top-level executable diagram</td>
      <td>Top-level execution graph content of the execution unit</td>
      <td>Top-level graph scope and contained object attribution</td>
      <td>The root graph MAY be represented directly by the unit rather than as an ordinary nested region object</td>
    </tr>
    <tr>
      <td><code>primitive</code> node</td>
      <td>Primitive execution object</td>
      <td>Primitive identity, resolved ports, execution-relevant metadata</td>
      <td>Includes intrinsic and profile-defined primitives</td>
    </tr>
    <tr>
      <td><code>subfrog</code> node</td>
      <td>Sub-FROG invocation object</td>
      <td>Referenced FROG identity, invocation boundary, resolved ports</td>
      <td>Base open IR SHOULD preserve invocation rather than inline it away</td>
    </tr>
    <tr>
      <td><code>interface_input</code> node</td>
      <td>Public interface entry boundary object</td>
      <td>Public API role, referenced interface input, value direction</td>
      <td>MUST remain distinct from widget-originated value participation</td>
    </tr>
    <tr>
      <td><code>interface_output</code> node</td>
      <td>Public interface exit boundary object</td>
      <td>Public API role, referenced interface output, value direction</td>
      <td>MUST remain distinct from widget-facing indicator participation</td>
    </tr>
    <tr>
      <td><code>widget_value</code> node</td>
      <td>Widget-value participation object</td>
      <td>Referenced widget identity, primary-value participation, control/indicator directionality</td>
      <td>Only widgets that actually participate in validated executable content need such IR objects</td>
    </tr>
    <tr>
      <td><code>widget_reference</code> node</td>
      <td>Widget-reference participation object</td>
      <td>Referenced widget identity, object-style access role</td>
      <td>MUST remain distinct from ordinary valueflow participation</td>
    </tr>
    <tr>
      <td><code>structure</code> node</td>
      <td>Structured execution object</td>
      <td>Structure family, explicit regions, explicit boundary terminals, source correspondence</td>
      <td>Base v0.1 preserves <code>case</code>, <code>for_loop</code>, and <code>while_loop</code> as explicit structured families</td>
    </tr>
    <tr>
      <td>Structure region entry</td>
      <td>Region object</td>
      <td>Owned region identity, structure ownership, source region identity</td>
      <td>Region-local executable content remains attributable to region-local source content</td>
    </tr>
    <tr>
      <td>Structure boundary input/output entry</td>
      <td>Explicit boundary terminal or equivalent support object</td>
      <td>Boundary crossing role, type, owning structure, source-side identity</td>
      <td>May be materialized as explicit terminal objects or explicit structured ports</td>
    </tr>
    <tr>
      <td>Structure terminal entry</td>
      <td>Explicit structure terminal or equivalent support object</td>
      <td>Role, type, visibility relation, owning structure</td>
      <td>Selector, loop count, loop condition, iteration index, and equivalent standardized terminals remain distinguishable</td>
    </tr>
    <tr>
      <td>Diagram edge</td>
      <td>Directed connection</td>
      <td>Endpoint attribution and validated dependency direction</td>
      <td>Connection endpoints MUST attach to attributable validated objects and ports</td>
    </tr>
  </tbody>
</table>

<p>
The absence of a source family from this table does not automatically mean it is execution-relevant.
Non-execution source content MUST NOT be converted into execution objects merely because it exists in source.
</p>

<hr/>

<h2 id="identity-and-attribution-rules">10. Identity and Attribution Rules</h2>

<p>
Source attribution is mandatory.
Every execution-visible IR object MUST preserve enough information to identify the validated source-visible object or objects from which it was derived.
</p>

<p>
Base v0.1 recognizes the following derivation relation shapes:
</p>

<ul>
  <li><strong>1 -&gt; 1 direct preservation</strong> — one source-visible object derives to one primary IR object,</li>
  <li><strong>1 -&gt; n expansion</strong> — one source-visible object derives to one primary IR object plus one or more support objects,</li>
  <li><strong>n -&gt; 1 restricted aggregation</strong> — multiple source-visible objects contribute to one generated support object, but only when all contributors remain explicitly attributable.</li>
</ul>

<p>
Accordingly:
</p>

<ul>
  <li>a directly preserved object SHOULD carry one stable source identity relation,</li>
  <li>a 1 -&gt; n derivation MUST preserve which support objects belong to which primary source-visible contributor,</li>
  <li>an n -&gt; 1 derivation MUST preserve explicit contributor attribution,</li>
  <li>a conforming implementation MUST NOT collapse multiple independently attributable primary source-visible execution objects into one opaque generated object.</li>
</ul>

<p>
Conceptually:
</p>

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
</code></pre>

<p>
This document does not freeze one identifier syntax.
It requires recoverable cross-layer identity.
</p>

<hr/>

<h2 id="connectivity-derivation">11. Connectivity Derivation</h2>

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
  <li>resolved widget participation role.</li>
</ul>

<p>
Cross-scope communication MUST remain explicit.
A region-local connection MUST NOT silently bypass the structure boundary.
</p>

<hr/>

<h2 id="structured-control-derivation">12. Structured Control Derivation</h2>

<p>
Structured control remains explicit in the base open Execution IR.
</p>

<p>
A validated structure node MUST derive to one structured execution object that preserves:
</p>

<ul>
  <li>the standardized structure family,</li>
  <li>owned executable regions,</li>
  <li>boundary inputs and outputs,</li>
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
The open IR MUST NOT immediately flatten those structure families into target-specific branch graphs, generic CFG nodes, or backend-private loop machinery in a way that makes family identity or region correspondence non-recoverable.
</p>

<p>
For structures with region-specific metadata, the derived IR MUST preserve enough information to recover:
</p>

<ul>
  <li>which regions belong to which structure,</li>
  <li>which boundary terminals cross the structure wall,</li>
  <li>which terminals are structure-intrinsic rather than ordinary boundary values,</li>
  <li>which region-local graph content belongs to which source region.</li>
</ul>

<p>
Base v0.1 does not require one universal low-level nested-region encoding.
It requires semantic recoverability and explicit structured ownership.
</p>

<hr/>

<h2 id="interface-and-ui-derivation">13. Interface and UI Derivation</h2>

<p>
The open Execution IR MUST preserve the distinction between:
</p>

<ul>
  <li>public interface participation,</li>
  <li>widget primary-value participation,</li>
  <li>widget object-style reference participation.</li>
</ul>

<p>
Therefore:
</p>

<ul>
  <li><code>interface_input</code> and <code>interface_output</code> MUST remain recognizable as public boundary participation,</li>
  <li><code>widget_value</code> MUST remain recognizable as front-panel primary-value participation,</li>
  <li><code>widget_reference</code> MUST remain recognizable as object-style widget access participation,</li>
  <li>derivation MUST NOT merge those families into one undifferentiated generic endpoint model without preserving recoverable semantic roles.</li>
</ul>

<p>
Additional rules:
</p>

<ul>
  <li>interface declarations and diagram-side interface nodes MUST remain coherently related,</li>
  <li>front-panel widgets that do not participate in validated executable content MUST NOT be forced into execution-facing IR objects merely because they exist in source,</li>
  <li>widget references used together with <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, or <code>frog.ui.method_invoke</code> MUST remain distinguishable from ordinary dataflow values,</li>
  <li>the base widget reference token MUST NOT be reinterpreted by derivation as an unrestricted general-purpose storage or computation value unless a future specification explicitly standardizes that meaning.</li>
</ul>

<hr/>

<h2 id="state-and-cycle-preservation">14. State and Cycle Preservation</h2>

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
For cycle handling, the open IR inherits validated cycle legality from the language-level rules.
It does not invent a new cycle-validity rule.
</p>

<hr/>

<h2 id="allowed-normalization-during-derivation">15. Allowed Normalization During Derivation</h2>

<p>
Derivation MAY normalize validated program meaning in execution-facing ways that do not change semantic truth.
</p>

<p>
Examples of allowed normalization include:
</p>

<ul>
  <li>making resolved port types explicit,</li>
  <li>making resolved port directions explicit,</li>
  <li>making structure boundary terminals explicit,</li>
  <li>making region ownership explicit,</li>
  <li>materializing explicit support objects for execution-facing classification,</li>
  <li>adding explicit source-attribution records,</li>
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
  <li>public interface participation and UI participation MUST remain distinguishable.</li>
</ul>

<hr/>

<h2 id="forbidden-derivation-outcomes">16. Forbidden Derivation Outcomes</h2>

<p>
The following outcomes are forbidden in the base open Execution IR of v0.1:
</p>

<ul>
  <li>changing validated language-level execution meaning,</li>
  <li>removing attribution for execution-visible objects,</li>
  <li>collapsing multiple primary source-visible execution objects into one opaque unattributable generated object,</li>
  <li>replacing explicit memory with hidden scheduler-private state,</li>
  <li>flattening structured control so aggressively that family identity, region correspondence, or boundary-terminal correspondence is no longer recoverable,</li>
  <li>collapsing public interface, widget-value participation, and widget-reference participation into one untyped undifferentiated concept,</li>
  <li>promoting editor-only layout, styling, annotation placement, or other authoring convenience state into execution semantics,</li>
  <li>treating the open IR as a debugger trace, runtime history log, or event stream,</li>
  <li>hard-coding one private runtime scheduling strategy as if it were the standardized open IR.</li>
</ul>

<hr/>

<h2 id="out-of-scope-for-v01">17. Out of Scope for v0.1</h2>

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
Those concerns belong to later documents such as construction, lowering, backend contract, runtime, or IDE-facing specifications.
</p>

<hr/>

<h2 id="summary">18. Summary</h2>

<p>
Execution IR derivation in FROG v0.1 is conservative by design.
It starts from <strong>validated meaning</strong>, not from raw source convenience.
It produces <strong>one execution unit per validated FROG</strong>.
It preserves <strong>source attribution</strong>, <strong>structured control</strong>, <strong>explicit memory</strong>, and the distinction between <strong>public interface</strong> and <strong>UI participation</strong>.
It allows explicit execution-facing normalization, but it forbids semantic drift and runtime-private leakage.
</p>

<p>
In compact form:
</p>

<pre><code>validated FROG
   |
   +-- preserve executable meaning
   +-- preserve source attribution
   +-- preserve explicit memory
   +-- preserve structured control
   +-- preserve interface/UI distinction
   |
   v
open Execution IR
</code></pre>
