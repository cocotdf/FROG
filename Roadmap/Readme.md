<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">🐸 FROG Roadmap</h1>

<p align="center">
  Non-normative planning layer for the progressive closure of FROG as a language, conformance surface, reference path, compiler corridor, runtime path, deployment path, and future IDE ecosystem<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<p align="center">
  Roadmap start date: <strong>8 March 2026</strong>
</p>

<p align="center">
  <a href="#project-map-at-a-glance">Project map</a> •
  <a href="#purpose-of-this-roadmap">Purpose</a> •
  <a href="#what-this-roadmap-is-and-is-not">What this is / is not</a> •
  <a href="#status-legend">Status legend</a> •
  <a href="#guiding-principles">Guiding principles</a> •
  <a href="#current-published-baseline">Current baseline</a> •
  <a href="#priority-order">Priority order</a> •
  <a href="#high-level-roadmap">High-level roadmap</a> •
  <a href="#phase-0">Phase 0</a> •
  <a href="#phase-1">Phase 1</a> •
  <a href="#phase-2">Phase 2</a> •
  <a href="#phase-3">Phase 3</a> •
  <a href="#phase-4">Phase 4</a> •
  <a href="#phase-5">Phase 5</a> •
  <a href="#phase-6">Phase 6</a> •
  <a href="#cross-cutting-workstreams">Cross-cutting workstreams</a> •
  <a href="#milestone-navigation">Milestone navigation</a> •
  <a href="#definition-of-success">Definition of success</a>
</p>

<hr/>

<h2 id="project-map-at-a-glance">Project map at a glance</h2>

<pre>
FROG closure sequence

canonical .frog source
        |
        v
loadability
        |
        v
structural validation
        |
        v
validated language meaning
        |
        v
standardized FROG execution IR
        |
        v
backend-specific lowering
        |
        v
backend contract / consumable handoff
        |
        v
runtime or compiler/backend realization
        |
        v
deployable artifact

in parallel

authoring
   -> Program Model
   -> graphical IDE
   -> validation feedback
   -> observability / debugging
   -> reusable industrial workflow

project logic

semantic closure
   -> schema / validation closure
   -> conformance closure
   -> reference execution proof
   -> backend credibility
   -> IDE credibility
   -> ecosystem credibility
</pre>

<p>
This roadmap explains the intended closure order.
It does not replace <code>Expression/</code>, <code>Language/</code>, <code>IR/</code>, or any other normative ownership layer.
</p>

<hr/>

<h2 id="purpose-of-this-roadmap">Purpose of this roadmap</h2>

<p>
This roadmap exists to track the planned closure path of FROG as a full long-term ecosystem effort.
It is a planning layer inside the repository, not the source of normative language truth.
</p>

<p>
Its practical purpose is to answer one project question:
</p>

<p>
<strong>What sequence of concrete closures must be completed to move from the currently published FROG baseline to a serious open graphical programming ecosystem with a credible compiler/runtime path, credible deployment depth, a serious future IDE, and a credible open industrial language position?</strong>
</p>

<p>
That distinction matters:
</p>

<ul>
  <li>the specification layers define what FROG is,</li>
  <li>the roadmap layer defines in what order the project should be closed.</li>
</ul>

<p>
The roadmap also exists to keep the project disciplined.
It helps ensure that strategic ambition does not outrun technical closure,
and that new fronts are not opened faster than the current architectural corridor is stabilized.
</p>

<hr/>

<h2 id="what-this-roadmap-is-and-is-not">What this roadmap is and is not</h2>

<h3>What it is</h3>

<ul>
  <li>a sequencing layer,</li>
  <li>a closure plan,</li>
  <li>a milestone map,</li>
  <li>a prioritization surface for technical and ecosystem work,</li>
  <li>a public statement of closure order for the repository-visible corridor.</li>
</ul>

<h3>What it is not</h3>

<ul>
  <li>not the normative language definition,</li>
  <li>not the source of semantic truth,</li>
  <li>not a substitute for <code>Expression/</code>, <code>Language/</code>, <code>IR/</code>, or <code>Profiles/</code>,</li>
  <li>not a place where implementation convenience becomes language law,</li>
  <li>not a place where strategy prose silently replaces technical closure,</li>
  <li>not a claim that all future phases are already stabilized.</li>
</ul>

<hr/>

<h2 id="status-legend">Status legend</h2>

<ul>
  <li><strong>[x]</strong> completed or already established in the published baseline</li>
  <li><strong>[~]</strong> partially established, active, or not yet fully closed</li>
  <li><strong>[ ]</strong> planned future work</li>
</ul>

<hr/>

<h2 id="guiding-principles">Guiding principles</h2>

<ul>
  <li>Keep the architectural boundaries explicit.</li>
  <li>Prefer small coherent closures over large speculative rewrites.</li>
  <li>Do not let reference implementation convenience become hidden language law.</li>
  <li>Do not collapse open FROG IR into one backend-specific or runtime-private form.</li>
  <li>Do not confuse backend family, target profile, deployment mode, and runtime-private realization.</li>
  <li>Do not confuse roadmap planning with normative ownership.</li>
  <li>Keep the path from canonical <code>.frog</code> source to deployable execution explicit and inspectable.</li>
  <li>Use conformance as a public truth surface, not as commentary only.</li>
  <li>Keep source-shape/schema closure distinct from later semantic validation.</li>
  <li>Only widen the ecosystem after enough closure exists to support that widening cleanly.</li>
  <li>Keep strategic claims aligned with repository-visible proof.</li>
  <li>Keep AI-era auditability claims tied to real architectural closure rather than slogans.</li>
</ul>

<p>
What the project must preserve:
</p>

<pre>
saved source           -> Expression
validated meaning      -> Language
derived execution form -> IR
backend specialization -> Lowering
consumable handoff     -> Backend contract
private realization    -> Runtime / backend
authoring + debugging  -> IDE
closure sequencing     -> Roadmap
strategic purpose      -> Strategy
</pre>

<hr/>

<h2 id="current-published-baseline">Current published baseline</h2>

<p>
The project is no longer only conceptual.
A meaningful public foundation already exists.
</p>

<h3>Already established</h3>

<ul>
  <li>[x] FROG is explicitly structured as an open graphical dataflow language rather than a product-bound environment.</li>
  <li>[x] The six core specification families exist: <code>Expression</code>, <code>Language</code>, <code>IR</code>, <code>Libraries</code>, <code>Profiles</code>, <code>IDE</code>.</li>
  <li>[x] The repository contains support areas: <code>Examples/</code>, <code>Conformance/</code>, and <code>Implementations/Reference/</code>.</li>
  <li>[x] The first published executable slices already exist: <code>01_pure_addition</code>, <code>02_ui_value_roundtrip</code>, <code>03_ui_property_write</code>, <code>04_stateful_feedback_delay</code>.</li>
  <li>[x] The reference implementation posture is explicitly non-normative.</li>
  <li>[x] The distinction between public interface, front panel, and diagram is already explicit.</li>
  <li>[x] The distinction between <code>widget_value</code> and <code>widget_reference</code> is already explicit.</li>
  <li>[x] The strategic framing layer already exists through <code>Strategy/Heilmeier/</code>.</li>
  <li>[x] The roadmap layer already exists as a non-normative planning surface distinct from both strategy and specification.</li>
  <li>[x] The long-term chain remains explicit: <code>.frog source -&gt; loadability -&gt; structural validation -&gt; validated meaning -&gt; FROG execution IR -&gt; lowering -&gt; backend contract -&gt; backend/runtime</code>.</li>
  <li>[x] The distinction between backend family, target profile, deployment mode, and runtime-private realization is explicit at the architectural level.</li>
  <li>[x] Source-shape/schema posture has an explicit normative home inside <code>Expression/</code>.</li>
  <li>[x] A conservative machine-checkable schema artifact exists for canonical top-level source shape.</li>
  <li>[x] The conformance layer reads explicitly through <code>loadability -&gt; structural validity -&gt; semantic acceptance -&gt; preservation</code>.</li>
  <li>[x] The reference implementation posture describes staged validation rather than a blurred validator story.</li>
  <li>[x] The repository now already supports an explicit argument around open source, inspectable IR, and downstream compiler/backend separation.</li>
</ul>

<h3>Partially formed but not yet fully closed</h3>

<ul>
  <li>[~] Expression ↔ Language ↔ IR correspondence</li>
  <li>[~] minimal primitive baseline closure</li>
  <li>[~] type / value / state semantic closure</li>
  <li>[~] execution-model and structure closure</li>
  <li>[~] source-shape / schema and validator closure as a fully stable repository-level asset</li>
  <li>[~] conformance breadth and public completeness</li>
  <li>[~] repeatable reference execution path for a clearly bounded supported subset</li>
  <li>[~] explicit target-profile taxonomy beyond the now-established architectural distinction</li>
  <li>[~] explicit deployment-mode taxonomy beyond the now-established architectural distinction</li>
  <li>[~] first serious backend-family taxonomies and first reusable contract families</li>
  <li>[~] explicit strategic articulation of AI-era auditability and sovereignty across all top-level repository entry points</li>
</ul>

<h3>Still future work</h3>

<ul>
  <li>[ ] a fully closed v0.1 foundation</li>
  <li>[ ] a fully stable schema / validator closure</li>
  <li>[ ] a first serious backend-oriented compiler path</li>
  <li>[ ] a serious FROG IDE foundation</li>
  <li>[ ] broader target-profile and deployment depth</li>
  <li>[ ] a mature conformance / certification / ecosystem layer</li>
  <li>[ ] a repository-wide strategic alignment where openness, auditability, industrial security, and technological sovereignty are stated consistently without displacing normative ownership</li>
</ul>

<h3>Interpretation of the current state</h3>

<pre>
FROG today
   +-- strong architectural base
   +-- early semantic and IR structure
   +-- first public executable reference slices
   +-- explicit conformance posture
   +-- explicit non-normative reference path
   +-- explicit profile / backend / runtime separation
   +-- explicit source-schema posture
   +-- conservative machine-checkable top-level schema support
   +-- explicit staged conformance reading
   +-- stronger AI-era relevance than a purely pre-GenAI framing
   +-- no final production compiler stack yet
   +-- no serious full IDE yet
   +-- no mature deployment ecosystem yet
</pre>

<hr/>

<h2 id="priority-order">Priority order</h2>

<p>
Not all future work is equally urgent.
The project currently benefits most from the following closure order.
</p>

<ol>
  <li>close Expression ↔ Language ↔ IR correspondence more explicitly,</li>
  <li>close the minimal primitive baseline,</li>
  <li>close type / value / state semantic ownership more tightly,</li>
  <li>close execution-model and structure semantics more tightly,</li>
  <li>stabilize source-shape/schema and validator posture as a stable repository-level closure,</li>
  <li>expand conformance in a disciplined way,</li>
  <li>strengthen the repeatable reference execution path,</li>
  <li>prepare the first serious backend contract and lowering family,</li>
  <li>stabilize the first serious backend-family-oriented compiler corridor,</li>
  <li>only then widen toward broader execution profiles, deployment models, and richer ecosystem growth,</li>
  <li>keep strategic communication aligned with the real published proof surface at each step.</li>
</ol>

<p>
This order is intentional.
It keeps the project grounded in repository-visible closure rather than jumping too early into broad ecosystem claims.
</p>

<hr/>

<h2 id="high-level-roadmap">High-level roadmap</h2>

<pre>
Phase 0  -> establish open language architecture
Phase 1  -> establish canonical source posture and semantic baseline
Phase 2  -> establish repository-visible reference path and conformance posture
Phase 3  -> stabilize open execution-facing IR and compiler corridor boundaries
Phase 4  -> demonstrate a serious backend-oriented path
Phase 5  -> build serious IDE and observability foundations
Phase 6  -> widen ecosystem, deployment, and certification depth
</pre>

<p>
The roadmap is cumulative.
Later phases do not replace earlier ones.
They depend on them.
</p>

<hr/>

<h2 id="phase-0">Phase 0</h2>

<h3>Architectural establishment</h3>

<ul>
  <li>[x] establish FROG as an open graphical language rather than a product-bound environment</li>
  <li>[x] separate language, runtime, IDE, and hardware concerns</li>
  <li>[x] establish the six core architectural specification families</li>
  <li>[x] establish a repository-visible strategic layer and roadmap layer distinct from normative ownership</li>
</ul>

<p>
Phase 0 should be read as established at the architectural level.
Its purpose was to create the correct ownership model before deeper closure work.
</p>

<hr/>

<h2 id="phase-1">Phase 1</h2>

<h3>Canonical source and semantic baseline</h3>

<ul>
  <li>[x] establish canonical <code>.frog</code> source ownership</li>
  <li>[x] establish source-shape/schema posture inside <code>Expression/</code></li>
  <li>[~] close the minimal structural source model more fully</li>
  <li>[~] close core type, value, control, and state semantics more fully</li>
  <li>[~] align source-owned and semantic-owned responsibilities more tightly</li>
</ul>

<p>
This phase is where FROG becomes more than a general architectural idea.
It becomes a language with a serious saved form and a serious semantic baseline.
</p>

<hr/>

<h2 id="phase-2">Phase 2</h2>

<h3>Repository-visible reference path and conformance posture</h3>

<ul>
  <li>[x] publish first example slices</li>
  <li>[x] publish conformance as a public truth surface</li>
  <li>[x] publish a non-normative reference implementation workspace</li>
  <li>[~] expand conformance breadth coherently</li>
  <li>[~] make the bounded supported subset more explicit and repeatable</li>
  <li>[~] keep examples, conformance, and reference implementation aligned without letting them become hidden semantic law</li>
</ul>

<p>
This phase is critical because it turns the repository into a visible proof surface rather than leaving it as architecture prose only.
</p>

<hr/>

<h2 id="phase-3">Phase 3</h2>

<h3>IR stabilization and compiler corridor closure</h3>

<ul>
  <li>[x] publish an explicit IR layer</li>
  <li>[x] publish derivation, construction, identity, schema, lowering, and backend contract surfaces</li>
  <li>[~] stabilize Expression ↔ Language ↔ IR correspondence</li>
  <li>[~] stabilize canonical JSON IR posture as a durable machine-checkable layer</li>
  <li>[~] keep lowering explicitly downstream from open IR</li>
  <li>[~] keep backend contract explicitly distinct from private runtime realization</li>
</ul>

<p>
This phase is where FROG becomes credible as more than an authoring format.
It becomes credible as a language stack with a real execution-facing middle.
</p>

<hr/>

<h2 id="phase-4">Phase 4</h2>

<h3>First serious backend-oriented proof</h3>

<ul>
  <li>[ ] define the first reusable backend-family corridor more concretely</li>
  <li>[ ] demonstrate lowering toward a serious backend path</li>
  <li>[ ] demonstrate consumable backend handoff for a bounded subset</li>
  <li>[ ] keep LLVM or any comparable compiler family clearly downstream from FROG</li>
  <li>[ ] prove that the open IR can feed a serious compilation path without becoming that compiler family’s private truth model</li>
</ul>

<p>
This phase is one of the most important future exams of the whole project.
It is where backend credibility becomes real.
</p>

<hr/>

<h2 id="phase-5">Phase 5</h2>

<h3>Serious IDE and observability foundation</h3>

<ul>
  <li>[ ] stabilize the Program Model architecture more deeply</li>
  <li>[ ] define coherent IDE responsibilities across editing, validation feedback, and execution preparation</li>
  <li>[ ] define strong observability, debugging, probes, and watch foundations</li>
  <li>[ ] demonstrate that the language can support a serious future graphical development environment without collapsing the language into that IDE</li>
</ul>

<p>
This phase matters because FROG is not only a compiler corridor.
It is also intended to support a serious graphical engineering workflow.
</p>

<hr/>

<h2 id="phase-6">Phase 6</h2>

<h3>Ecosystem widening, deployment, and certification depth</h3>

<ul>
  <li>[ ] refine target-profile taxonomies</li>
  <li>[ ] refine deployment-mode distinctions</li>
  <li>[ ] widen conformance breadth and certification logic</li>
  <li>[ ] support broader implementation diversity</li>
  <li>[ ] support richer industrial ecosystem participation</li>
  <li>[ ] support long-term hardware and software ecosystem adoption</li>
</ul>

<p>
This phase should come after enough technical closure exists to support it cleanly.
Premature ecosystem widening would create ambiguity rather than credibility.
</p>

<hr/>

<h2 id="cross-cutting-workstreams">Cross-cutting workstreams</h2>

<p>
Some workstreams cut across multiple phases and should be treated as continuous concerns:
</p>

<ul>
  <li><strong>Ownership clarity</strong> — keep strategy, roadmap, conformance, specification, and reference implementation distinct.</li>
  <li><strong>Repository-visible proof</strong> — prefer published artifacts over abstract claims.</li>
  <li><strong>AI-era auditability</strong> — keep the source, graph structure, and execution-facing representation aligned with reviewability goals.</li>
  <li><strong>Industrial credibility</strong> — keep execution seriousness and portability central.</li>
  <li><strong>Technological sovereignty</strong> — keep the language open, multi-implementable, and separable from one vendor stack.</li>
  <li><strong>Conservative closure discipline</strong> — close one corridor coherently before widening unrelated fronts.</li>
</ul>

<hr/>

<h2 id="milestone-navigation">Milestone navigation</h2>

<p>
Milestone tracking should remain compact and subordinate to the roadmap narrative.
The detailed milestone surface is maintained in:
</p>

<pre><code>Roadmap/Milestones.md</code></pre>

<p>
This separation helps keep the roadmap readable while still allowing explicit tracking.
</p>

<hr/>

<h2 id="definition-of-success">Definition of success</h2>

<p>
The roadmap should be considered successful when the repository can credibly demonstrate all of the following together:
</p>

<ul>
  <li>a stable canonical <code>.frog</code> source posture,</li>
  <li>a clear structural validation boundary,</li>
  <li>a coherent validated semantic layer,</li>
  <li>a serious open execution-facing IR,</li>
  <li>explicit lowering and backend handoff boundaries,</li>
  <li>a credible backend/compiler corridor,</li>
  <li>a serious future IDE foundation,</li>
  <li>a public conformance growth path,</li>
  <li>a reference path that remains non-normative but useful,</li>
  <li>a coherent strategic position as an open, inspectable, industrially credible language foundation.</li>
</ul>

<p>
In the current era, success also includes one more condition:
FROG should become credibly understandable as a language infrastructure that remains governable when software creation is increasingly AI-assisted.
</p>

<p>
That means:
</p>

<ul>
  <li>structured source,</li>
  <li>graphically reviewable logic,</li>
  <li>inspectable execution-facing derivation,</li>
  <li>clear downstream handoff boundaries,</li>
  <li>an ecosystem architecture compatible with long-term industrial security and technological sovereignty.</li>
</ul>

<p>
That is the long-term closure target of the roadmap.
</p>
