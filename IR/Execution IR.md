<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG Execution IR Specification</h1>

<p align="center">
  Open execution-facing intermediate representation for validated FROG programs<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#purpose">2. Purpose</a></li>
  <li><a href="#non-goals">3. Non-goals</a></li>
  <li><a href="#position-in-the-pipeline">4. Position in the pipeline</a></li>
  <li><a href="#construction-boundary">5. Construction boundary</a></li>
  <li><a href="#design-goals">6. Design goals</a></li>
  <li><a href="#core-invariants">7. Core invariants</a></li>
  <li><a href="#execution-ir-object-model">8. Execution IR object model</a></li>
  <li><a href="#source-attribution-and-identity">9. Source attribution and identity</a></li>
  <li><a href="#ports-values-and-connections">10. Ports, values, and connections</a></li>
  <li><a href="#regions-and-structured-control">11. Regions and structured control</a></li>
  <li><a href="#interface-and-ui-boundaries">12. Interface and UI boundaries</a></li>
  <li><a href="#state-local-memory-and-cycles">13. State, local memory, and cycles</a></li>
  <li><a href="#allowed-normalization">14. Allowed normalization</a></li>
  <li><a href="#forbidden-transformations">15. Forbidden transformations</a></li>
  <li><a href="#minimal-open-shape">16. Minimal open shape</a></li>
  <li><a href="#examples">17. Examples</a></li>
  <li><a href="#relation-with-cache">18. Relation with cache</a></li>
  <li><a href="#out-of-scope-for-v01">19. Out of scope for v0.1</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the base <strong>open execution-facing intermediate representation</strong> for FROG v0.1.
</p>

<p>
The Execution IR is a <strong>derived representation</strong> built from a validated FROG program. It is intended to support execution preparation, execution-facing analysis, normalization, inspection, optimization, lowering, and later backend consumption without confusing those concerns with:
</p>

<ul>
  <li>the canonical serialized source artifact,</li>
  <li>the IDE Program Model,</li>
  <li>the full language-semantics layer,</li>
  <li>a private runtime scheduler graph,</li>
  <li>a runtime trace or execution log.</li>
</ul>

<p>
For v0.1, the open Execution IR remains deliberately close to validated executable meaning. It is <strong>not</strong> yet a fully lowered backend contract.
</p>

<hr/>

<h2 id="purpose">2. Purpose</h2>

<p>
The purpose of the Execution IR is to provide a stable execution-facing representation that:
</p>

<ul>
  <li>preserves attribution to source-visible program objects,</li>
  <li>makes execution-relevant structure explicit,</li>
  <li>supports implementation-independent inspection,</li>
  <li>permits later normalization and lowering stages,</li>
  <li>avoids standardizing one vendor's private runtime graph as the language-level execution form.</li>
</ul>

<p>
In practical terms:
</p>

<pre>
Expression   -> what is saved
Program Model-> what is edited
Execution IR -> what is prepared for execution
Runtime      -> what is actually running
</pre>

<hr/>

<h2 id="non-goals">3. Non-goals</h2>

<p>
This document does not define:
</p>

<ul>
  <li>the canonical <code>.frog</code> source structure in full,</li>
  <li>the IDE Program Model,</li>
  <li>the complete normative semantics of all FROG execution behavior,</li>
  <li>debugger command protocols,</li>
  <li>pause/resume/step command semantics,</li>
  <li>one mandatory runtime scheduler architecture,</li>
  <li>one mandatory compiled artifact format,</li>
  <li>one mandatory target-specific lowering pipeline.</li>
</ul>

<p>
This document also does not require every implementation to expose every private internal execution form.
</p>

<hr/>

<h2 id="position-in-the-pipeline">4. Position in the pipeline</h2>

<p>
The base architectural pipeline is:
</p>

<pre>
canonical .frog source
        |
        v
Expression
        |
        v
Program Model or equivalent validated tool form
        |
        v
validated executable graph
        |
        v
Execution IR
        |
        v
lowering / compilation / runtime-specific realization
</pre>

<p>
The validated executable graph is the language-level executable meaning of the program.
The Execution IR is the execution-facing derived form built from that validated meaning.
</p>

<hr/>

<h2 id="construction-boundary">5. Construction boundary</h2>

<p>
Execution IR construction begins only after the program has been validated according to the relevant FROG specifications.
</p>

<p>
At minimum, that validation includes:
</p>

<ul>
  <li>structural validation,</li>
  <li>type validation,</li>
  <li>primitive and structure-family validation,</li>
  <li>cycle-validity validation,</li>
  <li>all other applicable v0.1 validation rules.</li>
</ul>

<p>
An implementation MAY internally derive Execution IR from:
</p>

<ul>
  <li>canonical source plus validation results,</li>
  <li>a validated Program Model,</li>
  <li>another equivalent validated internal form.</li>
</ul>

<p>
However, the resulting Execution IR MUST remain semantically grounded in the validated FROG program rather than in editor-only convenience state.
</p>

<hr/>

<h2 id="design-goals">6. Design goals</h2>

<p>
The base Execution IR for v0.1 SHOULD be:
</p>

<ul>
  <li>execution-facing,</li>
  <li>source-attributable,</li>
  <li>inspectable,</li>
  <li>portable across implementations,</li>
  <li>stable enough to support future tooling,</li>
  <li>strict enough to support later lowering,</li>
  <li>conservative enough to avoid freezing one private compiler design too early.</li>
</ul>

<hr/>

<h2 id="core-invariants">7. Core invariants</h2>

<p>
The following invariants apply to the base Execution IR of v0.1:
</p>

<ul>
  <li>Every Execution IR object MUST be attributable to validated program meaning.</li>
  <li>The Execution IR MUST remain source-aligned at the level of attributable executable objects.</li>
  <li>The Execution IR MUST NOT silently change the normative language meaning of the validated program.</li>
  <li>The Execution IR MUST NOT replace explicit local memory with hidden implicit state.</li>
  <li>The Execution IR MUST NOT encode editor-only presentation state as if that state were execution semantics.</li>
  <li>The Execution IR MUST NOT be treated as a runtime history, event trace, or debugger session log.</li>
</ul>

<hr/>

<h2 id="execution-ir-object-model">8. Execution IR object model</h2>

<p>
The base Execution IR represents one validated FROG as one <strong>execution unit</strong> containing execution-facing objects and their relationships.
</p>

<p>
Conceptually:
</p>

<pre>
Execution IR
└── execution unit
    ├── interface boundary objects
    ├── executable objects
    ├── region objects
    ├── typed ports
    ├── directed connections
    └── source attribution
</pre>

<p>
In base v0.1, the Execution IR SHOULD preserve the major validated object families rather than aggressively lowering them away. Those families include:
</p>

<ul>
  <li>primitive executable objects,</li>
  <li>structured-control executable objects,</li>
  <li>sub-FROG invocation objects,</li>
  <li>public interface boundary objects,</li>
  <li>widget-value participation objects,</li>
  <li>widget-reference participation objects where applicable.</li>
</ul>

<p>
This conservative model keeps the open IR readable and attributable while still making execution-facing structure explicit.
</p>

<hr/>

<h2 id="source-attribution-and-identity">9. Source attribution and identity</h2>

<p>
Source attribution is mandatory.
</p>

<p>
Each execution-facing object in the IR MUST preserve enough information to identify the source-visible object or objects from which it was derived.
</p>

<p>
At minimum:
</p>

<ul>
  <li>a directly preserved object SHOULD carry one stable source identity,</li>
  <li>a normalized object derived from multiple source-visible objects MUST preserve an explicit attribution relation to all relevant source-visible contributors,</li>
  <li>an implementation MUST NOT collapse multiple independently attributable source-visible objects into one opaque generated object without preserving traceable attribution.</li>
</ul>

<p>
The goal is not to force one specific identifier syntax. The goal is to preserve stable cross-layer attribution for:
</p>

<ul>
  <li>inspection,</li>
  <li>validation reporting,</li>
  <li>debugging and observability integration,</li>
  <li>toolchain diagnostics,</li>
  <li>future source/IR/runtime correspondence.</li>
</ul>

<hr/>

<h2 id="ports-values-and-connections">10. Ports, values, and connections</h2>

<p>
The Execution IR MUST represent execution-relevant connectivity explicitly.
</p>

<p>
At minimum:
</p>

<ul>
  <li>execution-facing objects MUST expose typed ports,</li>
  <li>port direction MUST be explicit,</li>
  <li>directed connections between ports MUST be explicit,</li>
  <li>the resulting IR graph MUST preserve the validated dependency structure of the program,</li>
  <li>connection endpoints MUST remain attributable to validated executable objects and validated ports.</li>
</ul>

<p>
The IR MAY make port details more explicit than the source representation when such details are already determined by validation or intrinsic primitive definitions.
</p>

<p>
Examples of permitted explicitness include:
</p>

<ul>
  <li>resolved port direction,</li>
  <li>resolved port type,</li>
  <li>resolved structure terminal classification,</li>
  <li>resolved interface-boundary port role.</li>
</ul>

<hr/>

<h2 id="regions-and-structured-control">11. Regions and structured control</h2>

<p>
Structured control remains explicit in the base Execution IR.
</p>

<p>
For v0.1, control structures such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code> SHOULD remain represented as structured execution objects with explicit regions and explicit boundary terminals rather than being immediately flattened into target-specific branch or loop machinery.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>a structured execution object MUST identify its standardized structure family,</li>
  <li>owned execution regions MUST remain explicit,</li>
  <li>boundary terminals crossing the structure boundary MUST remain explicit,</li>
  <li>region-local execution content MUST remain attributable to source-level region content.</li>
</ul>

<p>
This preserves a clean distinction between:
</p>

<ul>
  <li>open execution IR, and</li>
  <li>later lowering into backend-oriented branch and loop realizations.</li>
</ul>

<hr/>

<h2 id="interface-and-ui-boundaries">12. Interface and UI boundaries</h2>

<p>
The Execution IR MUST preserve the distinction between public interface participation and UI participation.
</p>

<p>
Therefore:
</p>

<ul>
  <li>public interface entry and exit semantics MUST remain represented explicitly,</li>
  <li>widget primary-value participation MUST remain distinguishable from public interface participation,</li>
  <li>widget-reference object access MUST remain distinguishable from ordinary valueflow participation,</li>
  <li>the IR MUST NOT collapse public API boundaries and front-panel value boundaries into one undifferentiated concept.</li>
</ul>

<p>
In base v0.1, a source-aligned implementation SHOULD preserve recognizable boundary families corresponding to:
</p>

<ul>
  <li><code>interface_input</code>,</li>
  <li><code>interface_output</code>,</li>
  <li><code>widget_value</code>,</li>
  <li><code>widget_reference</code>.</li>
</ul>

<p>
More aggressive normalization is permitted only if source attribution and semantic distinction remain recoverable.
</p>

<hr/>

<h2 id="state-local-memory-and-cycles">13. State, local memory, and cycles</h2>

<p>
Explicit local memory remains explicit in the base Execution IR.
</p>

<p>
This is a hard requirement of the architectural model.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>the IR MUST preserve the presence of local-memory primitives such as <code>frog.core.delay</code>,</li>
  <li>the IR MUST NOT legalize an otherwise invalid combinational cycle by introducing hidden implicit memory,</li>
  <li>the IR MUST NOT erase explicit memory attribution in a valid stateful feedback path,</li>
  <li>cycles represented in the IR MUST remain consistent with validated cycle rules.</li>
</ul>

<p>
The open Execution IR is allowed to classify explicit memory-bearing objects as execution-relevant state objects, but it MUST remain faithful to the validated FROG rule that valid feedback depends on explicit local memory.
</p>

<hr/>

<h2 id="allowed-normalization">14. Allowed normalization</h2>

<p>
The base Execution IR MAY normalize validated program meaning in execution-facing ways that do not change semantic truth.
</p>

<p>
Examples of allowed normalization include:
</p>

<ul>
  <li>making resolved port direction explicit,</li>
  <li>making resolved port type explicit,</li>
  <li>making structure boundary terminals explicit,</li>
  <li>making region ownership explicit,</li>
  <li>materializing validated object classification needed for execution-facing analysis,</li>
  <li>adding explicit source-attribution maps,</li>
  <li>normalizing equivalent source spellings into one execution-facing canonical form.</li>
</ul>

<p>
Such normalization is acceptable only when the resulting IR remains semantically equivalent to the validated program.
</p>

<hr/>

<h2 id="forbidden-transformations">15. Forbidden transformations</h2>

<p>
The following transformations are forbidden in the base open Execution IR of v0.1:
</p>

<ul>
  <li>changing language-level execution meaning,</li>
  <li>removing source attribution for execution-visible objects,</li>
  <li>converting explicit local memory into hidden implicit scheduler state,</li>
  <li>treating editor-only annotations or presentation choices as execution semantics,</li>
  <li>hard-coding one private runtime scheduling strategy as if it were the open IR standard,</li>
  <li>flattening structured control so aggressively that structure identity, region attribution, or semantic correspondence is no longer recoverable,</li>
  <li>merging public interface boundaries, widget boundaries, and object-style widget access into one untyped generic edge model without preserving their semantic roles.</li>
</ul>

<hr/>

<h2 id="minimal-open-shape">16. Minimal open shape</h2>

<p>
This document does not yet freeze one mandatory JSON wire format for all implementations.
</p>

<p>
However, an open Execution IR payload SHOULD be representable in a shape broadly equivalent to:
</p>

<pre>
{
  "ir_version": "0.1",
  "kind": "execution_ir",
  "unit": {
    "id": "main",
    "objects": [],
    "connections": [],
    "regions": [],
    "source_map": {}
  }
}
</pre>

<p>
At minimum, such a representation SHOULD be capable of carrying:
</p>

<ul>
  <li>execution-facing object identity,</li>
  <li>object kind classification,</li>
  <li>typed ports,</li>
  <li>directed connections,</li>
  <li>structured regions where applicable,</li>
  <li>source attribution,</li>
  <li>validated execution-relevant metadata where applicable.</li>
</ul>

<p>
The exact transport schema MAY be defined more strictly in later documents.
</p>

<hr/>

<h2 id="examples">17. Examples</h2>

<h3>17.1 Basic interface-aligned arithmetic graph</h3>

<pre>
Source-facing idea
------------------
interface_input(a) ----\
                        +--> frog.core.add --> interface_output(result)
interface_input(b) ----/

Possible execution-facing IR view
---------------------------------
public_input[a] ----\
                     +--> primitive[frog.core.add] --> public_output[result]
public_input[b] ----/
</pre>

<p>
This example illustrates that the Execution IR MAY normalize naming while preserving:
</p>

<ul>
  <li>boundary role,</li>
  <li>primitive identity,</li>
  <li>dependency direction,</li>
  <li>source attribution.</li>
</ul>

<h3>17.2 Explicit local memory in feedback</h3>

<pre>
validated source-aligned meaning
--------------------------------
            +----------------------+
            |                      |
            v                      |
      [ frog.core.delay ] --> [ frog.core.add ] --> next_value
</pre>

<p>
In the Execution IR:
</p>

<ul>
  <li>the feedback path MAY remain a directed cycle,</li>
  <li>the delay MUST remain explicit as local memory,</li>
  <li>the IR MUST NOT replace the delay with hidden runtime-only state while pretending that no explicit memory object exists.</li>
</ul>

<h3>17.3 Structured control remains structured</h3>

<pre>
Source-facing idea
------------------
case(selector)
  ├── region "true"
  └── region "false"

Execution IR principle
----------------------
structure[case]
  ├── region[true]
  └── region[false]
</pre>

<p>
The open Execution IR keeps the structured form explicit. Backend-oriented branch lowering belongs later.
</p>

<hr/>

<h2 id="relation-with-cache">18. Relation with cache</h2>

<p>
A tool MAY serialize an Execution IR artifact inside a cache entry such as <code>frog.ir</code>.
</p>

<p>
However:
</p>

<ul>
  <li>the cache container does not own the meaning of Execution IR,</li>
  <li>cache metadata does not affect program semantics,</li>
  <li>cache absence does not invalidate the canonical source artifact,</li>
  <li>cache presence does not make the cached artifact the canonical source of truth.</li>
</ul>

<p>
This document owns the architectural meaning of the Execution IR itself.
Cache specifications only define how such derived artifacts may be stored or associated.
</p>

<hr/>

<h2 id="out-of-scope-for-v01">19. Out of scope for v0.1</h2>

<p>
The following topics remain out of scope for this document in v0.1:
</p>

<ul>
  <li>a fully frozen transport schema for every implementation,</li>
  <li>one mandatory SSA-style form,</li>
  <li>one mandatory scheduler graph,</li>
  <li>one mandatory target-lowering contract,</li>
  <li>distributed execution IR,</li>
  <li>asynchronous execution IR beyond the baseline language model,</li>
  <li>one mandatory runtime state snapshot format,</li>
  <li>one mandatory trace or observability event protocol.</li>
</ul>

<p>
The purpose of v0.1 is narrower:
</p>

<pre>
define an open execution-facing representation
without collapsing FROG into one private implementation pipeline
</pre>
