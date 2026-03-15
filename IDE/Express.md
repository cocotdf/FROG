<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG IDE Express Specification</h1>

<p align="center">
Definition of assistant-driven Express authoring entries for the FROG IDE<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Goals</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#definition">4. What an Express Entry Is</a></li>
  <li><a href="#non-goals">5. What Express Is Not</a></li>
  <li><a href="#ownership-boundaries">6. Ownership Boundaries</a></li>
  <li><a href="#express-kinds">7. Express Kinds</a></li>
  <li><a href="#configuration-model">8. Configuration Model</a></li>
  <li><a href="#configurable-vs-expandable">9. Configurable vs Expandable Parameters</a></li>
  <li><a href="#canonical-normalization">10. Canonical Normalization</a></li>
  <li><a href="#instance-model">11. Instance Model</a></li>
  <li><a href="#palette-integration">12. Palette Integration</a></li>
  <li><a href="#editing-reopen-convert">13. Edit, Reopen, Detach, and Materialize</a></li>
  <li><a href="#help-preview-doc">14. Help, Preview, and Documentation</a></li>
  <li><a href="#program-model">15. Program Model Representation</a></li>
  <li><a href="#optional-source-persistence">16. Optional Source Persistence</a></li>
  <li><a href="#validation-rules">17. Validation Rules</a></li>
  <li><a href="#examples">18. Examples</a></li>
  <li><a href="#out-of-scope">19. Out of Scope for v0.1</a></li>
  <li><a href="#summary">20. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
Express authoring is an IDE-layer capability that allows a user to insert, configure, and re-edit common programming
patterns through a guided experience rather than through raw low-level assembly alone.
</p>

<p>
Its purpose is to improve usability, speed of insertion, discoverability, and correctness for frequent tasks while
preserving the canonical FROG model.
</p>

<p>
Express is therefore an <strong>authoring presentation mechanism</strong>, not a separate language.
A conforming FROG IDE MAY expose Express entries, but any inserted Express-authored content MUST remain reducible to
canonical FROG content already owned by the active specification set.
</p>

<p>
This document defines the normative IDE-facing role of Express entries, their lifecycle, their configuration model,
their relationship to canonical source, and the minimum rules required to preserve stable round-trip authoring.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Faster authoring</strong> — common tasks SHOULD be insertable with less friction than manual low-level assembly.</li>
  <li><strong>Discoverability</strong> — users SHOULD be able to find common tasks by intent rather than only by canonical primitive name.</li>
  <li><strong>Preserved canonical identity</strong> — Express authoring MUST normalize to canonical FROG content.</li>
  <li><strong>Stable re-editability</strong> — an Express-authored instance SHOULD remain safely reconfigurable after load and reload.</li>
  <li><strong>No semantic drift</strong> — Express authoring MUST NOT create hidden language semantics.</li>
  <li><strong>Interoperability with direct authoring</strong> — users MUST remain able to work directly with canonical primitives, structures, and node insertions.</li>
  <li><strong>Tooling safety</strong> — validation, execution preparation, debugging, probes, watch, and snippets MUST remain grounded in canonical content rather than Express-private semantics.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This document complements the following specifications:
</p>

<ul>
  <li><code>IDE/Readme.md</code> — defines the architectural role of Express authoring inside the FROG IDE.</li>
  <li><code>IDE/Palette.md</code> — defines how Express entries are discovered, searched, filtered, and inserted.</li>
  <li><code>IDE/Snippet.md</code> — defines snippet transport and insertion behavior for authoring fragments.</li>
  <li><code>Expression/Readme.md</code> — defines canonical source ownership and the optional source-level <code>ide</code> section.</li>
  <li><code>Expression/Diagram.md</code> — defines canonical graph objects and standard node kinds for v0.1.</li>
  <li><code>Expression/Control structures.md</code> — defines canonical source-facing structures and the rule that authoring views do not create new canonical structure identities.</li>
  <li><code>Libraries/</code> documents — define standardized primitive identities and primitive-local semantics.</li>
  <li><code>Language/</code> documents — define cross-cutting normative execution semantics.</li>
</ul>

<p>
This document does not define new canonical source objects, new primitive semantics, or new structure families.
It defines how a conforming IDE MAY provide a guided authoring layer above constructs already owned elsewhere.
</p>

<hr/>

<h2 id="definition">4. What an Express Entry Is</h2>

<p>
An <strong>Express entry</strong> is an IDE-defined, assistant-driven, task-oriented authoring entry that inserts or edits
canonical FROG content through a guided configuration workflow.
</p>

<p>
An Express entry is characterized by the following properties:
</p>

<ul>
  <li>it is <strong>assistant-driven</strong>,</li>
  <li>it is <strong>instance-local</strong>,</li>
  <li>it is <strong>task-oriented</strong>,</li>
  <li>it is <strong>normalizable</strong> to canonical content,</li>
  <li>it is <strong>re-editable</strong> when the IDE preserves sufficient non-authoritative state.</li>
</ul>

<p>
An Express entry MAY represent:
</p>

<ul>
  <li>a guided configuration surface for a single canonical primitive,</li>
  <li>a guided configuration surface for a canonical sub-FROG invocation,</li>
  <li>a guided materialization process for a deterministic canonical fragment.</li>
</ul>

<p>
A conforming IDE SHOULD make the canonical target identity visible to the user somewhere in the Express experience,
entry metadata, or instance detail view.
</p>

<hr/>

<h2 id="non-goals">5. What Express Is Not</h2>

<p>
Express is not:
</p>

<ul>
  <li>a new canonical node kind,</li>
  <li>a new semantic structure family,</li>
  <li>a replacement for canonical source identity,</li>
  <li>a justification for execution-facing systems to depend on editor-private UI state,</li>
  <li>a permission to hide semantically required program content from conforming tooling.</li>
</ul>

<p>
Accordingly:
</p>

<ul>
  <li>an Express entry MUST NOT redefine primitive identity,</li>
  <li>an Express entry MUST NOT redefine language semantics,</li>
  <li>an Express entry MUST NOT require a conforming runtime to understand IDE-private Express state,</li>
  <li>an Express entry MUST NOT make canonical execution meaning ambiguous.</li>
</ul>

<hr/>

<h2 id="ownership-boundaries">6. Ownership Boundaries</h2>

<p>
Ownership boundaries remain explicit:
</p>

<ul>
  <li><code>Expression/</code> owns canonical source representation,</li>
  <li><code>Language/</code> owns normative execution meaning,</li>
  <li><code>Libraries/</code> owns primitive identity and primitive-local semantics,</li>
  <li><code>IDE/Express.md</code> owns the IDE-facing guided authoring model of Express.</li>
</ul>

<p>
Therefore:
</p>

<ul>
  <li>this document MAY describe how Express resolves to canonical content,</li>
  <li>this document MUST NOT redefine the canonical syntax of that content,</li>
  <li>this document MUST NOT replace the specifications that own the target content normatively.</li>
</ul>

<p>
If a conflict arises between Express presentation and canonical ownership, canonical ownership wins.
</p>

<hr/>

<h2 id="express-kinds">7. Express Kinds</h2>

<p>
A conforming IDE MAY support one or more of the following Express kinds.
</p>

<h3>7.1 Primitive-backed Express</h3>

<p>
A primitive-backed Express entry configures one canonical <code>primitive</code> node.
</p>

<p>
This is the most direct Express form and is appropriate when:
</p>

<ul>
  <li>the canonical primitive already exists,</li>
  <li>the primitive has meaningful configurable parameters,</li>
  <li>optional terminals may need to be exposed progressively,</li>
  <li>the guided experience mainly improves usability rather than structure creation.</li>
</ul>

<h3>7.2 Sub-FROG-backed Express</h3>

<p>
A sub-FROG-backed Express entry configures one canonical <code>subfrog</code> node.
</p>

<p>
This form is appropriate when:
</p>

<ul>
  <li>the guided task is better represented as a reusable program unit,</li>
  <li>the underlying behavior is more complex than a single primitive,</li>
  <li>the IDE should expose a simple task-oriented entry while preserving a clean canonical diagram identity.</li>
</ul>

<h3>7.3 Fragment-backed Express</h3>

<p>
A fragment-backed Express entry deterministically materializes a canonical fragment containing multiple canonical objects.
</p>

<p>
This form SHOULD be used more conservatively because it requires stronger guarantees for:
</p>

<ul>
  <li>stable re-editability,</li>
  <li>deterministic materialization,</li>
  <li>mapping from Express instance state to owned canonical objects,</li>
  <li>safe detach or flatten behavior.</li>
</ul>

<p>
For v0.1, primitive-backed and sub-FROG-backed Express are the preferred baseline.
Fragment-backed Express MAY exist, but it SHOULD remain conservative and predictable.
</p>

<hr/>

<h2 id="configuration-model">8. Configuration Model</h2>

<p>
An Express entry SHOULD provide a guided configuration experience appropriate to the target task.
That experience MAY be implemented through:
</p>

<ul>
  <li>a modal dialog,</li>
  <li>a non-modal properties panel,</li>
  <li>an inline popover,</li>
  <li>a staged wizard,</li>
  <li>another equivalent IDE interaction surface.</li>
</ul>

<p>
The configuration experience SHOULD allow the user to:
</p>

<ul>
  <li>understand what the entry does,</li>
  <li>set configuration values,</li>
  <li>review visible optional terminals,</li>
  <li>preview the canonical target identity,</li>
  <li>confirm insertion,</li>
  <li>reopen the same configuration later when re-editing.</li>
</ul>

<p>
A conforming IDE MAY provide task-oriented wording and grouped controls that are more approachable than raw canonical
parameter names, but the mapping from those controls to canonical content MUST remain deterministic.
</p>

<hr/>

<h2 id="configurable-vs-expandable">9. Configurable vs Expandable Parameters</h2>

<p>
If Express authoring is supported, the IDE SHOULD distinguish clearly between:
</p>

<ul>
  <li><strong>configurable parameters</strong> — values or options primarily edited through the guided configuration experience,</li>
  <li><strong>expandable terminals</strong> — optional visible inputs or outputs that the user may choose to expose directly on the diagram.</li>
</ul>

<h3>9.1 Configurable Parameters</h3>

<p>
Configurable parameters typically represent:
</p>

<ul>
  <li>modes,</li>
  <li>units,</li>
  <li>defaults,</li>
  <li>policy selections,</li>
  <li>constant values,</li>
  <li>other options best edited through a guided form.</li>
</ul>

<p>
A configurable parameter MAY map to:
</p>

<ul>
  <li>a canonical constant input value,</li>
  <li>a configuration field for a sub-FROG-backed instance,</li>
  <li>a deterministic materialization choice for a fragment-backed instance.</li>
</ul>

<h3>9.2 Expandable Terminals</h3>

<p>
Expandable terminals are optional visible terminals that the user may expose or hide for authoring convenience.
</p>

<p>
The following rules apply:
</p>

<ul>
  <li>an expandable terminal MUST correspond to a port that is valid for the canonical target,</li>
  <li>an Express presentation MUST NOT invent semantically invalid terminals,</li>
  <li>an Express presentation MUST NOT hide a semantically required terminal in a way that makes the canonical model ambiguous,</li>
  <li>the mapping between instance configuration and terminal visibility SHOULD be deterministic.</li>
</ul>

<hr/>

<h2 id="canonical-normalization">10. Canonical Normalization</h2>

<p>
Canonical normalization is the process by which an Express presentation becomes ordinary canonical FROG content.
</p>

<p>
A conforming IDE MUST ensure that:
</p>

<ul>
  <li>an Express entry normalizes to content already valid in the active specification set,</li>
  <li>normalization preserves the intended source-level meaning,</li>
  <li>execution-facing systems can operate on normalized canonical content without depending on Express UI state.</li>
</ul>

<p>
Canonical normalization MAY target:
</p>

<ul>
  <li>a canonical <code>primitive</code> node,</li>
  <li>a canonical <code>subfrog</code> node,</li>
  <li>a deterministic canonical fragment whose owned objects are all valid under the active specification set.</li>
</ul>

<p>
The normalization process MUST NOT:
</p>

<ul>
  <li>create a hidden semantic family,</li>
  <li>introduce runtime-required editor-private data,</li>
  <li>change canonical meaning depending on transient editor UI state alone.</li>
</ul>

<hr/>

<h2 id="instance-model">11. Instance Model</h2>

<p>
Each Express-authored instance SHOULD have a stable IDE-level identity while the user edits the program.
</p>

<p>
A conforming IDE SHOULD be able to associate the following conceptual elements with an Express-authored instance:
</p>

<ul>
  <li><strong>instance identity</strong> — the IDE-side identity of the Express-authored occurrence,</li>
  <li><strong>express identity</strong> — the Express entry definition used to create or edit the instance,</li>
  <li><strong>canonical target identity</strong> — the primitive, sub-FROG, or fragment target to which the instance resolves,</li>
  <li><strong>configuration state</strong> — non-authoritative IDE state sufficient to reopen guided editing,</li>
  <li><strong>visible optional terminals</strong> — the current authoring-facing terminal exposure state,</li>
  <li><strong>owned canonical objects</strong> — the canonical object or objects created or edited by the instance.</li>
</ul>

<p>
This instance model is an IDE concern.
It MUST remain reducible to canonical content for execution-facing purposes.
</p>

<hr/>

<h2 id="palette-integration">12. Palette Integration</h2>

<p>
Express entries integrate with the palette as guided insertion entries.
They MAY appear in:
</p>

<ul>
  <li>primary intent-first browsing,</li>
  <li>search results,</li>
  <li>context-aware insertion results,</li>
  <li>a dedicated guided or Express lens.</li>
</ul>

<p>
A conforming IDE SHOULD:
</p>

<ul>
  <li>make Express entries visually distinguishable from direct primitive, structure, and node-insertion entries,</li>
  <li>disclose canonical target identity in entry metadata or detail view,</li>
  <li>allow the user to reach the corresponding direct canonical entry where that improves transparency.</li>
</ul>

<p>
Express entries SHOULD remain especially useful for task-oriented workflows such as:
</p>

<ul>
  <li>common I/O tasks,</li>
  <li>common signal-processing tasks,</li>
  <li>common connectivity tasks,</li>
  <li>other repetitive workflows where guided configuration materially improves usability.</li>
</ul>

<hr/>

<h2 id="editing-reopen-convert">13. Edit, Reopen, Detach, and Materialize</h2>

<p>
A conforming IDE SHOULD support the following lifecycle operations for Express-authored instances where Express is available:
</p>

<ul>
  <li><strong>insert and configure</strong> — create the initial canonical target through a guided workflow,</li>
  <li><strong>reopen configuration</strong> — reopen guided editing for a previously inserted instance,</li>
  <li><strong>reconfigure</strong> — change configuration and update canonical content deterministically,</li>
  <li><strong>detach or discard Express presentation</strong> — remove the guided layer while preserving valid canonical content,</li>
  <li><strong>materialize</strong> — when supported, convert the guided instance into plain canonical content with no remaining guided editing contract.</li>
</ul>

<h3>13.1 Reopen</h3>

<p>
Reopening configuration SHOULD restore enough guided state to allow meaningful continued editing without reconstructing
the instance from guesswork alone.
</p>

<h3>13.2 Detach</h3>

<p>
Detach removes the Express presentation while leaving the underlying canonical object model intact.
After detach:
</p>

<ul>
  <li>the resulting content MUST remain valid canonical FROG content,</li>
  <li>execution-facing behavior MUST remain grounded in canonical meaning,</li>
  <li>the user MAY continue editing the resulting content directly.</li>
</ul>

<h3>13.3 Materialize</h3>

<p>
Materialize is especially relevant for fragment-backed Express.
When materialization is supported:
</p>

<ul>
  <li>the resulting canonical fragment MUST be deterministic,</li>
  <li>the IDE SHOULD make clear that future reconfiguration may no longer use the original guided contract,</li>
  <li>materialization MUST NOT produce semantically hidden required content.</li>
</ul>

<hr/>

<h2 id="help-preview-doc">14. Help, Preview, and Documentation</h2>

<p>
A conforming IDE SHOULD provide user-facing help for Express entries.
Useful capabilities include:
</p>

<ul>
  <li>a short task-oriented description,</li>
  <li>a canonical target disclosure,</li>
  <li>a preview of key configurable parameters,</li>
  <li>a preview of optional expandable terminals,</li>
  <li>links or references to the underlying canonical primitive, sub-FROG, or related specification entry.</li>
</ul>

<p>
An Express entry MAY describe the task in more human terms than the canonical primitive name.
However, the IDE SHOULD still preserve a path back to the canonical identity.
</p>

<hr/>

<h2 id="program-model">15. Program Model Representation</h2>

<p>
The FROG Program Model MAY preserve non-authoritative Express-related state in memory during editing.
That state SHOULD be sufficient to support:
</p>

<ul>
  <li>stable mapping from Express instance to owned canonical objects,</li>
  <li>reopen and reconfigure workflows,</li>
  <li>deterministic terminal visibility,</li>
  <li>safe detach or materialize operations,</li>
  <li>round-trip editing without semantic drift.</li>
</ul>

<p>
Typical IDE-side Program Model concerns include:
</p>

<ul>
  <li>preferred guided presentation,</li>
  <li>configuration state,</li>
  <li>per-instance editor hints,</li>
  <li>optional terminal visibility state,</li>
  <li>mapping to canonical target identity.</li>
</ul>

<p>
This state remains IDE-owned and non-authoritative for execution semantics.
</p>

<hr/>

<h2 id="optional-source-persistence">16. Optional Source Persistence</h2>

<p>
The FROG source format MAY optionally persist IDE-facing recoverability aids through the source-level <code>ide</code> section
owned by the Expression layer.
</p>

<p>
If Express-related state is persisted there:
</p>

<ul>
  <li>it MUST remain non-authoritative for execution semantics,</li>
  <li>it MUST NOT be required to determine canonical executable meaning,</li>
  <li>it SHOULD support stable reopen and re-edit workflows,</li>
  <li>it SHOULD remain safely ignorable by runtimes and other execution-facing systems.</li>
</ul>

<p>
Examples of persistable Express-related IDE state MAY include:
</p>

<ul>
  <li>Express entry identity,</li>
  <li>guided presentation preferences,</li>
  <li>recoverable configuration values,</li>
  <li>optional terminal visibility state,</li>
  <li>mapping from Express instance identity to owned canonical objects.</li>
</ul>

<p>
A conforming runtime MUST NOT require this state in order to execute the program.
</p>

<hr/>

<h2 id="validation-rules">17. Validation Rules</h2>

<p>
A conforming IDE MUST validate Express behavior against canonical ownership and canonical validity.
</p>

<p>
At minimum:
</p>

<ul>
  <li>an Express entry MUST resolve to valid canonical content,</li>
  <li>the disclosed canonical target identity MUST match the actual normalized target,</li>
  <li>expandable terminals MUST correspond to ports valid for the canonical target,</li>
  <li>reconfiguration MUST update canonical content deterministically,</li>
  <li>detach or materialize MUST leave valid canonical content,</li>
  <li>execution-facing systems MUST be able to ignore Express-private presentation state.</li>
</ul>

<p>
A conforming IDE SHOULD also detect and report:
</p>

<ul>
  <li>broken mappings between Express instances and canonical targets,</li>
  <li>configuration states that no longer match the active specification set,</li>
  <li>profile mismatches that would make the target entry unavailable or invalid,</li>
  <li>stale recoverability state that cannot safely be reapplied.</li>
</ul>

<hr/>

<h2 id="examples">18. Examples</h2>

<h3>18.1 Primitive-backed Express example</h3>

<p>
A guided numeric filter entry MAY configure one canonical primitive or one canonical sub-FROG target.
The guided UI may expose:
</p>

<ul>
  <li>filter family,</li>
  <li>cutoff value,</li>
  <li>units,</li>
  <li>optional error terminals.</li>
</ul>

<p>
After insertion, the canonical target remains an ordinary canonical object known to the active specification set.
</p>

<h3>18.2 Sub-FROG-backed Express example</h3>

<p>
A task-oriented file reading entry such as <em>Read Text File</em> MAY configure one canonical <code>subfrog</code> node whose
public contract is easier to present through guided wording than through raw low-level assembly.
</p>

<h3>18.3 Fragment-backed Express example</h3>

<p>
A guided acquisition or connectivity workflow MAY materialize a deterministic fragment containing several canonical objects.
If so, the IDE MUST preserve deterministic mapping between the Express instance and that fragment for as long as guided
re-editing is supported.
</p>

<h3>18.4 Conceptual persisted IDE metadata example</h3>

<pre><code>{
  "ide": {
    "express_bindings": [
      {
        "instance_id": "expr_001",
        "express_id": "frog.ide.express.read_text_file",
        "canonical_target_kind": "subfrog",
        "canonical_target_ref": "frog.io.read_text_file.basic",
        "visible_optional_terminals": ["error_in", "error_out"],
        "config": {
          "encoding": "utf8",
          "line_endings": "auto"
        }
      }
    ]
  }
}</code></pre>

<p>
This example is conceptual.
It illustrates the kind of non-authoritative recoverability state an IDE MAY preserve.
It does not redefine canonical execution meaning.
</p>

<hr/>

<h2 id="out-of-scope">19. Out of Scope for v0.1</h2>

<ul>
  <li>turning Express into a new canonical node kind,</li>
  <li>requiring runtimes to interpret Express-private presentation state,</li>
  <li>opaque Express systems whose canonical target cannot be determined by a conforming IDE,</li>
  <li>automatic hidden semantic transformation beyond deterministic canonical normalization,</li>
  <li>marketplace-specific Express UX or commercial distribution workflows,</li>
  <li>cloud-hosted Express catalogs,</li>
  <li>a requirement that every primitive family already provide Express entries,</li>
  <li>full standardization of fragment-backed Express lifecycle semantics across all future profiles,</li>
  <li>execution-private helper content that cannot be represented as canonical FROG content.</li>
</ul>

<hr/>

<h2 id="summary">20. Summary</h2>

<p>
Express authoring gives the FROG IDE a guided, assistant-driven insertion model for common tasks without creating a separate language.
</p>

<ul>
  <li>Express entries belong to the IDE layer.</li>
  <li>They MUST normalize to canonical FROG content.</li>
  <li>They MUST NOT become new semantic node kinds or structure families.</li>
  <li>They SHOULD disclose canonical target identity.</li>
  <li>They MAY preserve non-authoritative recoverability state in the Program Model and, optionally, in the source-level <code>ide</code> section.</li>
  <li>They SHOULD support insert, configure, reopen, reconfigure, and safe detach workflows.</li>
  <li>Execution-facing systems MUST remain grounded in canonicalized content rather than Express UI state.</li>
</ul>

<p>
This gives FROG a modern guided-authoring model inspired by practical IDE workflows while preserving an open, durable,
canonical graphical language representation.
</p>
