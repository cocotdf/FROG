<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG IR Construction Rules</h1>

<p align="center">
  <strong>Normative construction rules for building open Execution IR from validated FROG program meaning</strong><br />
  FROG — Free Open Graphical Language
</p>

<hr />

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#boundary-contract">2. Boundary Contract</a></li>
  <li><a href="#scope">3. Scope</a></li>
  <li><a href="#relation-with-other-specifications">4. Relation with Other Specifications</a></li>
  <li><a href="#construction-entry-condition">5. Construction Entry Condition</a></li>
  <li><a href="#construction-result">6. Construction Result</a></li>
  <li><a href="#construction-principles">7. Construction Principles</a></li>
  <li><a href="#conceptual-construction-pipeline">8. Conceptual Construction Pipeline</a></li>
  <li><a href="#execution-unit-construction">9. Execution Unit Construction</a></li>
  <li><a href="#primary-object-construction">10. Primary Object Construction</a></li>
  <li><a href="#port-terminal-and-connection-construction">11. Port, Terminal, and Connection Construction</a></li>
  <li><a href="#region-and-structure-construction">12. Region and Structure Construction</a></li>
  <li><a href="#boundary-and-ui-construction">13. Boundary and UI Construction</a></li>
  <li><a href="#state-and-cycle-construction">14. State and Cycle Construction</a></li>
  <li><a href="#source-attribution-and-correspondence-construction">15. Source Attribution and Correspondence Construction</a></li>
  <li><a href="#support-object-construction">16. Support Object Construction</a></li>
  <li><a href="#non-primary-correspondence-handling">17. Non-Primary Correspondence Handling</a></li>
  <li><a href="#minimal-open-payload-shape">18. Minimal Open Payload Shape</a></li>
  <li><a href="#ir-validity-checks">19. IR Validity Checks</a></li>
  <li><a href="#determinism-and-stability">20. Determinism and Stability</a></li>
  <li><a href="#out-of-scope">21. Out of Scope</a></li>
  <li><a href="#summary">22. Summary</a></li>
</ul>

<hr />

<h2 id="overview">1. Overview</h2>

<p>
This document defines how a conforming implementation constructs an open Execution IR from
<strong>validated FROG program meaning</strong> in base v0.1.
</p>

<p>
Where <code>IR/Derivation rules.md</code> defines <strong>what must correspond</strong> between validated meaning and open Execution IR,
this document defines <strong>how that corresponding IR is materially built</strong> in a way that remains conservative,
attributable, structured, portable, and recoverable.
</p>

<p>
This document does not standardize one private compiler pipeline.
It standardizes the minimum construction obligations that make a produced open Execution IR
recognizable, inspectable, recoverable, and suitable for later lowering.
</p>

<pre><code>validated program meaning
        |
        v
construction rules   &lt;-- this document
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
runtime-private realization
</code></pre>

<p>
In base v0.1, construction is intentionally conservative.
It builds:
</p>

<ul>
  <li>primary execution-facing objects for execution-relevant validated content,</li>
  <li>support objects only when they make already-validated execution-facing structure explicit,</li>
  <li>recoverable correspondence for source-visible content that does not become a primary execution object in the open IR.</li>
</ul>

<hr />

<h2 id="boundary-contract">2. Boundary Contract</h2>

<p>
Construction begins only after validated program meaning exists.
Construction does not decide validity.
Construction does not invent missing semantics.
Construction materializes an execution-facing payload from already-validated meaning.
</p>

<p>
A conforming construction result MUST therefore be:
</p>

<ul>
  <li>semantically faithful,</li>
  <li>execution-facing,</li>
  <li>explicit enough for inspection and later lowering,</li>
  <li>attributable to validated source-visible contributors,</li>
  <li>free of runtime-private semantic invention.</li>
</ul>

<p>
Construction is not:
</p>

<ul>
  <li>a validator,</li>
  <li>a lowering step,</li>
  <li>a backend contract emitter,</li>
  <li>a runtime scheduler realization.</li>
</ul>

<pre><code>validation decides:
  whether meaning exists

derivation decides:
  what must correspond

construction decides:
  how the open IR payload is materially built
</code></pre>

<hr />

<h2 id="scope">3. Scope</h2>

<p>
This document defines:
</p>

<ul>
  <li>the construction entry condition,</li>
  <li>the minimum conceptual construction stages of open Execution IR,</li>
  <li>the obligations for building execution units, primary objects, support objects, ports, terminals, connections, and regions,</li>
  <li>the obligations for building explicit source attribution and correspondence,</li>
  <li>the conditions under which support objects may be introduced,</li>
  <li>the minimum validity properties of the constructed payload.</li>
</ul>

<p>
This document does <strong>not</strong> define:
</p>

<ul>
  <li>canonical source representation,</li>
  <li>language semantics,</li>
  <li>the full cross-stage identity model,</li>
  <li>one universal mandatory wire format,</li>
  <li>backend-specific lowering,</li>
  <li>runtime-private realization.</li>
</ul>

<pre><code>This document defines:
how a conforming open IR is materially built

This document does not define:
source shape
language semantics
full cross-stage identity contract
lowering
private realization
</code></pre>

<hr />

<h2 id="relation-with-other-specifications">4. Relation with Other Specifications</h2>

<p>
Ownership remains:
</p>

<pre><code>Expression/              -&gt; source shape
Language/                -&gt; validated program meaning
IR/Derivation rules.md   -&gt; correspondence obligations
IR/Execution IR.md       -&gt; open IR architecture
IR/Construction rules.md -&gt; build obligations
IR/Identity and Mapping.md -&gt; recoverability obligations
IR/Lowering.md           -&gt; later specialization
IR/Backend contract.md   -&gt; later backend-facing handoff
</code></pre>

<p>
Accordingly:
</p>

<ul>
  <li>this document MUST NOT redefine canonical source syntax,</li>
  <li>this document MUST NOT redefine language semantics,</li>
  <li>this document MUST NOT replace derivation rules with implementation-private heuristics,</li>
  <li>this document MUST NOT replace identity and mapping rules with opaque construction shortcuts,</li>
  <li>this document MUST define how a conforming open Execution IR payload is materially built once derivation eligibility is satisfied.</li>
</ul>

<p>
This document should be read together with:
</p>

<ul>
  <li><code>Language/Expression to validated meaning.md</code>,</li>
  <li><code>IR/Derivation rules.md</code>,</li>
  <li><code>IR/Identity and Mapping.md</code>,</li>
  <li><code>IR/Execution IR.md</code>,</li>
  <li><code>Expression/Diagram.md</code>,</li>
  <li><code>Expression/Control structures.md</code>,</li>
  <li><code>Expression/State and cycles.md</code>,</li>
  <li><code>Expression/Interface.md</code>,</li>
  <li><code>Expression/Front panel.md</code>,</li>
  <li><code>Expression/Widget.md</code>,</li>
  <li><code>Expression/Widget interaction.md</code>.</li>
</ul>

<hr />

<h2 id="construction-entry-condition">5. Construction Entry Condition</h2>

<p>
Open Execution IR construction begins only after the program has <strong>validated program meaning</strong>.
Construction MUST NOT be claimed for a program that has not already satisfied the applicable validation rules.
</p>

<p>
At minimum, the following validation classes MUST already be satisfied:
</p>

<ul>
  <li>structural validation,</li>
  <li>type validation,</li>
  <li>primitive and structure-family validation,</li>
  <li>interface / diagram consistency validation,</li>
  <li>region and structure-boundary validation,</li>
  <li>widget participation validation where applicable,</li>
  <li>cycle-validity validation,</li>
  <li>all other applicable v0.1 validation rules.</li>
</ul>

<p>
An implementation MAY internally start construction from:
</p>

<ul>
  <li>canonical source plus validation results,</li>
  <li>a validated Program Model,</li>
  <li>another equivalent validated internal form.</li>
</ul>

<p>
However, the constructed open Execution IR MUST remain grounded in validated program meaning rather than in editor-only convenience state.
</p>

<pre><code>raw or editable form
        |
        v
validated program meaning
        |
        v
construction starts here
</code></pre>

<hr />

<h2 id="construction-result">6. Construction Result</h2>

<p>
The construction result in base v0.1 is one open Execution IR payload describing one validated FROG program as one
<strong>execution unit</strong>.
</p>

<p>
That execution unit MUST contain enough constructed content to expose:
</p>

<ul>
  <li>execution-facing object identity,</li>
  <li>object-family classification,</li>
  <li>primary objects,</li>
  <li>support objects where needed,</li>
  <li>typed ports or equivalent explicit terminal interfaces,</li>
  <li>directed connections,</li>
  <li>structured regions where applicable,</li>
  <li>boundary participation,</li>
  <li>mandatory source attribution and recoverable correspondence.</li>
</ul>

<p>
A conforming implementation MAY carry additional execution-relevant metadata, provided that:
</p>

<ul>
  <li>it does not alter language meaning,</li>
  <li>it does not encode editor-only presentation semantics,</li>
  <li>it does not masquerade as runtime-private scheduler state.</li>
</ul>

<pre><code>one validated FROG
        |
        v
one execution unit
        ├── primary execution-facing objects
        ├── support objects where needed
        ├── typed ports / explicit terminals
        ├── directed connections
        ├── regions where applicable
        ├── boundary participation
        └── source attribution / correspondence
</code></pre>

<p>
The construction result is the open IR payload that later stages MAY consume.
It is not yet a lowered target-facing form and not yet a backend-facing contract artifact.
</p>

<hr />

<h2 id="construction-principles">7. Construction Principles</h2>

<p>
All conforming open Execution IR construction in base v0.1 MUST follow the following principles:
</p>

<ul>
  <li><strong>validated-first</strong> — construction starts after validation, not before it,</li>
  <li><strong>conservative</strong> — major validated families remain visible unless later documents explicitly allow stronger lowering,</li>
  <li><strong>attributable</strong> — every execution-visible constructed object remains traceable to validated source-visible contributors,</li>
  <li><strong>mapping-compatible</strong> — construction preserves enough structure and identity for later recoverable mapping,</li>
  <li><strong>structured</strong> — structured control remains explicit in the open IR,</li>
  <li><strong>portable</strong> — construction must not assume one private backend architecture,</li>
  <li><strong>execution-facing</strong> — construction may make execution-relevant facts explicit, but must not invent new semantic truth,</li>
  <li><strong>non-forcing</strong> — construction must not force non-participating source content into primary execution objects merely because it exists in source.</li>
</ul>

<pre><code>Construction principles

validated-first
attributable
mapping-compatible
structured
execution-facing
portable
non-forcing of non-primary source content

not backend-private by assumption
</code></pre>

<hr />

<h2 id="conceptual-construction-pipeline">8. Conceptual Construction Pipeline</h2>

<p>
A conforming implementation MAY organize internal construction differently,
but the resulting construction MUST be equivalent to the following conceptual pipeline:
</p>

<pre><code>validated program meaning
        |
        v
(1) create execution unit
        |
        v
(2) construct primary execution-facing objects
        |
        v
(3) construct ports and explicit terminal interfaces
        |
        v
(4) construct directed connections
        |
        v
(5) construct explicit regions and structure-owned boundaries
        |
        v
(6) construct source attribution and correspondence relations
        |
        v
(7) construct support objects where needed
        |
        v
(8) record intentional non-primary correspondence where applicable
        |
        v
(9) verify IR validity invariants
        |
        v
open Execution IR payload
</code></pre>

<p>
The order above is normative at the level of dependency, not necessarily at the level of one implementation's temporary in-memory steps.
For example, an implementation MAY resolve ports before materializing all objects, provided the final result is equivalent.
</p>

<p>
Construction stops at the open IR boundary.
Lowering, backend-contract shaping, scheduling, partitioning, or runtime realization belong to later stages.
</p>

<hr />

<h2 id="execution-unit-construction">9. Execution Unit Construction</h2>

<p>
Construction MUST begin by creating one execution unit for the validated FROG program being constructed.
</p>

<p>
The execution unit MUST provide the owning scope for:
</p>

<ul>
  <li>all constructed primary execution-facing objects,</li>
  <li>all constructed support objects that belong to the open IR payload,</li>
  <li>all constructed connections,</li>
  <li>all region objects,</li>
  <li>all explicit source-attribution records,</li>
  <li>all explicit correspondence records.</li>
</ul>

<p>
The execution unit MUST carry a stable unit identity within the payload.
That identity does not require one globally fixed syntax, but it MUST be stable enough for inspection, diagnostics, cross-record reference, and recoverable mapping inside the payload.
</p>

<p>
In base v0.1, one validated FROG program MUST construct to one execution unit.
The open IR does not yet standardize multi-unit partitioning, distributed unit packaging, or backend-sharded unit construction.
</p>

<pre><code>execution unit
   owns:
   - primary objects
   - support objects
   - connections
   - regions
   - source attribution
   - correspondence records

Rule:
one validated FROG
   -&gt;
one execution unit
</code></pre>

<hr />

<h2 id="primary-object-construction">10. Primary Object Construction</h2>

<p>
Primary execution-facing objects MUST be constructed from validated executable or boundary-participating content according to the derivation rules.
</p>

<p>
In base v0.1, construction SHOULD preserve recognizable primary object families corresponding to:
</p>

<ul>
  <li>primitive execution objects,</li>
  <li>structured execution objects,</li>
  <li>sub-FROG invocation objects,</li>
  <li>public interface boundary objects,</li>
  <li>widget-value participation objects,</li>
  <li>widget-reference participation objects,</li>
  <li>explicit local-memory execution objects where validated meaning requires them.</li>
</ul>

<p>
Each constructed primary object MUST contain at minimum:
</p>

<ul>
  <li>a local IR object identity,</li>
  <li>an object family or equivalent classification field,</li>
  <li>its explicit port or terminal interface,</li>
  <li>its source attribution relation,</li>
  <li>its validated semantic correspondence,</li>
  <li>execution-relevant metadata required for faithful interpretation, when applicable.</li>
</ul>

<p>
Construction MUST NOT produce anonymous execution-visible objects whose role cannot be classified or attributed.
Construction MUST NOT merge multiple independently attributable primary validated objects into one opaque generated object.
</p>

<pre><code>Primary object requirements

local IR identity
family classification
explicit port / terminal interface
source attribution
semantic correspondence
required execution-facing metadata

Forbidden:
anonymous execution-visible objects
opaque unattributable primary merging
</code></pre>

<hr />

<h2 id="port-terminal-and-connection-construction">11. Port, Terminal, and Connection Construction</h2>

<p>
Execution-relevant connectivity MUST be constructed explicitly.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>every constructed execution-facing object MUST expose explicit ports or an equivalent explicit terminal interface,</li>
  <li>port direction MUST be explicit,</li>
  <li>port type MUST be explicit once validation has resolved it,</li>
  <li>directed connections MUST be constructed explicitly,</li>
  <li>connection endpoints MUST resolve to attributable execution-facing objects and attributable ports or terminals.</li>
</ul>

<p>
At minimum, each constructed connection MUST identify:
</p>

<ul>
  <li>its source endpoint,</li>
  <li>its destination endpoint,</li>
  <li>its local identity or equivalent stable payload handle,</li>
  <li>its source attribution relation when the connection itself is represented as a first-class attributable record.</li>
</ul>

<p>
Construction MAY make already-resolved details explicit, including:
</p>

<ul>
  <li>resolved port type,</li>
  <li>resolved port direction,</li>
  <li>resolved structure-terminal classification,</li>
  <li>resolved public-boundary role,</li>
  <li>resolved widget participation role,</li>
  <li>resolved structure-boundary ownership.</li>
</ul>

<p>
Construction MUST preserve the validated dependency structure of the executable graph.
It MUST NOT silently bypass a structure boundary or region wall that exists in validated meaning.
</p>

<pre><code>Connectivity construction

explicit ports / terminals
explicit direction
explicit port type
explicit directed connections
attributable endpoints
preserved validated dependencies

Forbidden:
hidden cross-boundary bypass
</code></pre>

<hr />

<h2 id="region-and-structure-construction">12. Region and Structure Construction</h2>

<p>
Structured control remains explicit in the base open Execution IR.
Therefore, construction of a validated structure MUST produce:
</p>

<ul>
  <li>one structured execution object,</li>
  <li>explicit owned regions,</li>
  <li>explicit boundary inputs and outputs or equivalent structured ports,</li>
  <li>explicit structure terminals where applicable.</li>
</ul>

<p>
For base v0.1:
</p>

<ul>
  <li><code>case</code> MUST be constructed as a structured object with explicit region ownership and explicit selector participation,</li>
  <li><code>for_loop</code> MUST be constructed as a structured object with explicit counted-iteration semantics and explicit loop-intrinsic terminals where applicable,</li>
  <li><code>while_loop</code> MUST be constructed as a structured object with explicit continuation semantics and explicit loop-intrinsic terminals where applicable.</li>
</ul>

<p>
Each constructed region MUST remain explicitly owned by its parent structured execution object.
A region MUST NOT exist in the payload without a recoverable ownership relation.
</p>

<p>
Each region MUST contain or reference the execution-facing objects and connectivity that belong to that region.
A conforming payload MAY represent region-local membership directly or indirectly,
but region-local content MUST remain recoverable.
</p>

<p>
Boundary crossings MUST remain explicit.
Construction MUST NOT flatten structured control so aggressively that:
</p>

<ul>
  <li>structure family identity becomes unrecoverable,</li>
  <li>region ownership becomes unrecoverable,</li>
  <li>boundary-terminal correspondence becomes unrecoverable,</li>
  <li>structure-terminal roles become unrecoverable.</li>
</ul>

<pre><code>structured execution object
        ├── explicit owned regions
        ├── explicit structure-boundary participation
        ├── explicit structure terminals where applicable
        └── recoverable region-local content

Forbidden:
unrecoverable structural flattening
</code></pre>

<hr />

<h2 id="boundary-and-ui-construction">13. Boundary and UI Construction</h2>

<p>
Construction MUST preserve the distinction between:
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
  <li><code>interface_input</code> and <code>interface_output</code> MUST construct to explicit public boundary participation in the IR,</li>
  <li><code>widget_value</code> MUST construct to explicit widget-value participation when that widget participates in validated meaning,</li>
  <li><code>widget_reference</code> MUST construct to explicit widget-reference participation when object-style widget interaction is part of validated meaning.</li>
</ul>

<p>
Construction MUST NOT collapse those families into one untyped generic endpoint concept without preserving their distinct semantic roles.
</p>

<p>
Additional rules:
</p>

<ul>
  <li>public interface declarations and diagram-side interface participation MUST remain coherently related in the constructed IR,</li>
  <li>widgets that do not participate in validated meaning MUST NOT be forced into primary execution-facing IR objects merely because they exist in source,</li>
  <li>widget declarations that do participate through <code>widget_value</code> or <code>widget_reference</code> MUST remain recoverably related to the constructed participation objects,</li>
  <li>widget-reference-based interaction used with <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, or <code>frog.ui.method_invoke</code> MUST remain distinguishable from ordinary valueflow participation.</li>
</ul>

<pre><code>Boundary construction

public interface participation
   !=
widget primary-value participation
   !=
widget object-style reference participation

Forbidden:
one untyped generic endpoint role
</code></pre>

<hr />

<h2 id="state-and-cycle-construction">14. State and Cycle Construction</h2>

<p>
Construction MUST preserve explicit local memory as explicit attributable execution-facing content.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>a validated local-memory primitive such as <code>frog.core.delay</code> MUST construct to an explicit attributable IR object,</li>
  <li>execution-relevant initialization data required by validated meaning MUST remain recoverable,</li>
  <li>stateful feedback validity MUST remain grounded in explicit memory already present in validated meaning,</li>
  <li>construction MUST NOT legalize an otherwise invalid combinational cycle by injecting hidden implicit memory,</li>
  <li>construction MUST NOT erase attribution of explicit memory in a valid feedback path.</li>
</ul>

<p>
If the implementation chooses to classify some constructed objects as state-bearing execution objects,
that classification MAY be added as execution-facing metadata.
It MUST NOT change the rule that valid feedback depends on explicit memory rather than hidden runtime policy.
</p>

<pre><code>Cycle construction rule

valid feedback
   requires
explicit local memory

therefore

constructed IR
   must preserve
explicit memory identity
explicit initial-state recoverability

Forbidden:
hidden implicit-memory legalization
</code></pre>

<hr />

<h2 id="source-attribution-and-correspondence-construction">15. Source Attribution and Correspondence Construction</h2>

<p>
Source attribution is mandatory.
Construction MUST produce explicit attribution information sufficient to recover the relation between constructed execution-facing objects and validated source-visible contributors.
</p>

<p>
At minimum, the constructed payload MUST support:
</p>

<ul>
  <li>direct attribution for directly preserved objects,</li>
  <li>multi-contributor attribution for support objects derived from more than one validated contributor,</li>
  <li>stable attribution references for inspection, validation reporting, diagnostics, and later mapping-aware tooling,</li>
  <li>recoverable correspondence between declarations and participation where v0.1 requires it.</li>
</ul>

<p>
A conforming implementation MAY represent attribution and correspondence:
</p>

<ul>
  <li>inline on each object,</li>
  <li>through a dedicated source map table,</li>
  <li>through a dedicated correspondence table,</li>
  <li>through an equivalent explicit mechanism.</li>
</ul>

<p>
Whatever representation is used, attribution MUST remain explicit and recoverable.
Construction MUST NOT rely on unstated positional assumptions or undocumented ordering conventions as the sole attribution mechanism.
</p>

<pre><code>Source attribution construction

direct attribution
multi-contributor attribution where needed
declaration-to-participation correspondence where needed
stable diagnostic references

Allowed representations:
- inline attribution
- source_map table
- correspondence table
- equivalent explicit mechanism

Forbidden:
implicit undocumented positional attribution only
</code></pre>

<p>
This document does not require one universal attribution encoding.
It requires a construction result that remains compatible with the recoverability obligations defined elsewhere in the IR layer.
</p>

<hr />

<h2 id="support-object-construction">16. Support Object Construction</h2>

<p>
Construction MAY introduce support objects when doing so makes validated execution-facing structure more explicit without changing semantic meaning.
</p>

<p>
Examples include:
</p>

<ul>
  <li>explicit region records,</li>
  <li>explicit structure-boundary terminal records,</li>
  <li>explicit structure-terminal records,</li>
  <li>explicit port descriptors,</li>
  <li>explicit source-map records,</li>
  <li>explicit classification records needed for inspection or later lowering.</li>
</ul>

<p>
Support-object construction is permitted only if all of the following remain true:
</p>

<ul>
  <li>the support object serves a real execution-facing or attribution-facing purpose,</li>
  <li>validated meaning remains unchanged,</li>
  <li>source-visible contributors remain recoverable,</li>
  <li>the support object does not smuggle in runtime-private scheduler policy.</li>
</ul>

<p>
A support object MUST NOT replace a primary source-visible execution object.
It may clarify it.
It may accompany it.
It MUST NOT erase it.
</p>

<pre><code>Support objects

Allowed:
clarify
classify
expose explicit structure
carry attribution / correspondence

Forbidden:
replace primary meaning
erase primary contributors
smuggle runtime-private policy
</code></pre>

<hr />

<h2 id="non-primary-correspondence-handling">17. Non-Primary Correspondence Handling</h2>

<p>
Some source-visible content does not become a primary execution object in the open IR of base v0.1.
Construction MUST handle that fact explicitly rather than by accidental omission.
</p>

<p>
Typical examples include:
</p>

<ul>
  <li>interface declaration entries that correspond to public boundary participation but do not need a second independent primary execution object,</li>
  <li>widget declarations that are referenced by participation objects but are not themselves primary execution objects,</li>
  <li>widget declarations that do not participate in validated meaning at all,</li>
  <li>non-execution descriptive or presentational records.</li>
</ul>

<p>
When such content matters to recoverability, construction MUST preserve enough information to distinguish:
</p>

<ul>
  <li>intentional non-primary correspondence,</li>
  <li>referenced declaration correspondence,</li>
  <li>true non-participation,</li>
  <li>forbidden attribution loss.</li>
</ul>

<p>
A conforming implementation MAY represent this through:
</p>

<ul>
  <li>explicit non-primary correspondence records,</li>
  <li>declaration references carried by primary or support objects,</li>
  <li>another equivalent explicit mechanism.</li>
</ul>

<p>
Construction MUST NOT use absence alone as the only signal when absence would make required correspondence ambiguous.
</p>

<pre><code>Non-primary correspondence

Allowed:
declaration referenced by a primary participation object
intentional non-participation recorded explicitly where needed
no primary object when v0.1 does not require one

Forbidden:
accidental silent omission of required correspondence
</code></pre>

<hr />

<h2 id="minimal-open-payload-shape">18. Minimal Open Payload Shape</h2>

<p>
This document does not freeze one mandatory universal JSON wire format for every implementation.
However, a conforming open payload SHOULD be representable in a broadly equivalent open shape such as:
</p>

<pre><code>{
  "ir_version": "0.1",
  "kind": "execution_ir",
  "unit": {
    "id": "main",
    "objects": [],
    "connections": [],
    "regions": [],
    "source_map": {},
    "correspondence": {}
  }
}
</code></pre>

<p>
This example is an <strong>illustrative minimal open payload skeleton</strong>, not a claim that every conforming implementation must emit this exact JSON syntax.
</p>

<p>
In a minimally open payload:
</p>

<ul>
  <li><code>ir_version</code> SHOULD identify the IR schema or version family being emitted,</li>
  <li><code>kind</code> SHOULD classify the payload as open execution IR,</li>
  <li><code>unit</code> MUST identify the execution unit being described,</li>
  <li><code>objects</code> MUST carry primary execution-facing objects and support objects, with clear classification,</li>
  <li><code>connections</code> MUST carry explicit directed connectivity,</li>
  <li><code>regions</code> MUST carry explicit structured region information where applicable,</li>
  <li><code>source_map</code> or an equivalent mechanism MUST carry recoverable attribution,</li>
  <li><code>correspondence</code> or an equivalent mechanism MAY carry declaration linkage and intentional non-primary correspondence where needed.</li>
</ul>

<p>
An implementation MAY extend this shape with additional execution-relevant metadata,
provided that such metadata does not redefine language semantics or freeze runtime-private realization details as though they were open IR standard.
</p>

<pre><code>Minimal open payload intent

unit
├── objects
├── connections
├── regions
├── source attribution
└── correspondence where needed
</code></pre>

<hr />

<h2 id="ir-validity-checks">19. IR Validity Checks</h2>

<p>
Before a constructed payload is claimed to be a valid open Execution IR,
it MUST satisfy the following minimum checks:
</p>

<ul>
  <li>all execution-visible objects are classifiable,</li>
  <li>all execution-visible objects are attributable,</li>
  <li>all primary objects are distinguishable from support objects,</li>
  <li>all connection endpoints resolve to valid explicit ports or terminals,</li>
  <li>all structured regions have valid ownership relations,</li>
  <li>all explicit public / interface / UI distinctions required by v0.1 remain recoverable,</li>
  <li>all explicit local-memory objects remain explicit and attributable,</li>
  <li>required declaration-to-participation correspondence remains recoverable where applicable,</li>
  <li>intentional non-primary correspondence is not confused with accidental identity loss,</li>
  <li>the payload does not contain editor-only presentation state as execution semantics,</li>
  <li>the payload does not require hidden undocumented runtime policy to be interpreted as open IR.</li>
</ul>

<p>
If those checks are not satisfied, the implementation MUST NOT claim that the emitted payload is a conforming open Execution IR for base v0.1.
</p>

<pre><code>IR validity checks

classifiable objects
attributable objects
primary / support distinction
valid endpoint resolution
valid region ownership
recoverable interface / UI distinctions
explicit attributable memory
recoverable declaration correspondence where required
non-primary correspondence not confused with identity loss

no editor-only execution semantics
no hidden runtime-policy dependency
</code></pre>

<hr />

<h2 id="determinism-and-stability">20. Determinism and Stability</h2>

<p>
Construction SHOULD be stable for semantically identical validated inputs under the same implementation configuration.
</p>

<p>
This does not require identical payload byte layout across all tools.
It does require that the emitted open IR remain:
</p>

<ul>
  <li>structurally coherent,</li>
  <li>attribution-stable,</li>
  <li>semantically equivalent,</li>
  <li>sufficiently predictable for inspection, diagnostics, caching, and future lowering.</li>
</ul>

<p>
Implementation-defined ordering choices MAY exist.
However, a conforming implementation SHOULD avoid unnecessary instability in:
</p>

<ul>
  <li>object identity assignment,</li>
  <li>region identity assignment,</li>
  <li>connection identity assignment,</li>
  <li>source-attribution representation,</li>
  <li>support-object classification,</li>
  <li>non-primary correspondence representation.</li>
</ul>

<pre><code>Construction stability

Required:
structural coherence
attribution stability
semantic equivalence
predictable inspection-friendly shape

Not required:
identical byte-for-byte payload across all tools
</code></pre>

<hr />

<h2 id="out-of-scope">21. Out of Scope</h2>

<p>
The following are out of scope for this document in base v0.1:
</p>

<ul>
  <li>one universally mandatory procedural build algorithm,</li>
  <li>one universally mandatory binary or JSON transport syntax,</li>
  <li>mandatory SSA construction,</li>
  <li>mandatory CFG flattening of structured control,</li>
  <li>backend-specific lowering rules,</li>
  <li>compiled artifact formats,</li>
  <li>runtime-private scheduler graph construction,</li>
  <li>distributed or multi-unit execution packaging,</li>
  <li>debugger event streams, trace payloads, or observability protocols.</li>
</ul>

<p>
Those concerns belong to later documents such as lowering, backend contract, runtime, deployment, and IDE-facing observability specifications.
</p>

<hr />

<h2 id="summary">22. Summary</h2>

<p>
Open Execution IR construction in FROG v0.1 is intentionally conservative.
It starts from <strong>validated program meaning</strong>, creates <strong>one execution unit</strong>, constructs
<strong>primary execution-facing objects</strong>, <strong>typed ports</strong>, <strong>directed connections</strong>,
<strong>structured regions</strong>, <strong>support objects where justified</strong>, and
<strong>mandatory source attribution and correspondence</strong>,
then verifies that the resulting payload remains structured, attributable, portable, and free from runtime-private leakage.
</p>

<p>
It is also intentionally upstream of later stages:
construction closes the material build boundary for open Execution IR,
while lowering, backend-facing contracts, and private realization remain later concerns.
</p>

<pre><code>validated program meaning
   |
   +-- construct execution unit
   +-- construct primary objects
   +-- construct ports and connections
   +-- construct regions and boundaries
   +-- construct attribution and support objects
   +-- record non-primary correspondence where needed
   +-- verify invariants
   |
   v
open Execution IR
</code></pre>
