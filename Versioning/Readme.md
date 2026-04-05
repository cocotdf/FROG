<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">FROG Specification Versioning</h1>

<p align="center">
  <strong>Centralized cross-version governance for the published FROG specification corpus</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-surface-exists">2. Why This Surface Exists</a></li>
  <li><a href="#scope">3. Scope</a></li>
  <li><a href="#non-goals">4. Non-Goals</a></li>
  <li><a href="#three-version-notions-that-must-remain-distinct">5. Three Version Notions That Must Remain Distinct</a></li>
  <li><a href="#specification-corpus-version">6. Specification Corpus Version</a></li>
  <li><a href="#frog-spec_version-source-compatibility-version">7. <code>.frog</code> <code>spec_version</code> Source Compatibility Version</a></li>
  <li><a href="#metadata-program_version-program-artifact-version">8. <code>metadata.program_version</code> Program Artifact Version</a></li>
  <li><a href="#governance-principles">9. Governance Principles</a></li>
  <li><a href="#version-boundary-model">10. Version Boundary Model</a></li>
  <li><a href="#stabilization-classes">11. Stabilization Classes</a></li>
  <li><a href="#cross-repository-versioning-responsibilities">12. Cross-Repository Versioning Responsibilities</a></li>
  <li><a href="#compatibility-posture">13. Compatibility Posture</a></li>
  <li><a href="#version-transition-criteria">14. Version Transition Criteria</a></li>
  <li><a href="#published-version-objectives">15. Published Version Objectives</a></li>
  <li><a href="#how-other-documents-should-reference-this-surface">16. How Other Documents Should Reference This Surface</a></li>
  <li><a href="#change-classification-guidance">17. Change Classification Guidance</a></li>
  <li><a href="#minimal-decision-table">18. Minimal Decision Table</a></li>
  <li><a href="#relationship-with-roadmap-strategy-and-conformance">19. Relationship with Roadmap, Strategy, and Conformance</a></li>
  <li><a href="#repository-wide-versioning-diagram">20. Repository-Wide Versioning Diagram</a></li>
  <li><a href="#future-expansion">21. Future Expansion</a></li>
  <li><a href="#summary">22. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>
<p>
This document is the centralized repository-visible governance surface for specification versioning across the published FROG specification corpus.
</p>

<p>
Its purpose is to define how specification versions are identified, how version-to-version closure is evaluated, what becomes normative at each published boundary, what remains draft or deferred, and how the repository should describe transition from one published specification state to the next.
</p>

<p>
This document exists so that specification-version policy does not become scattered across unrelated README files, profile files, widget files, IR files, or roadmap prose.
</p>

<hr/>

<h2 id="why-this-surface-exists">2. Why This Surface Exists</h2>
<p>
The published FROG repository already spans multiple architectural layers and repository-level support surfaces:
</p>

<ul>
  <li>canonical source representation,</li>
  <li>structural validation posture,</li>
  <li>validated language meaning,</li>
  <li>execution-facing IR,</li>
  <li>canonical JSON IR posture where applicable,</li>
  <li>lowering,</li>
  <li>backend contract,</li>
  <li>backend-family consumption,</li>
  <li>execution-start closure for bounded published cases,</li>
  <li>widget and front-panel object exposure,</li>
  <li>examples,</li>
  <li>conformance material,</li>
  <li>reference implementation workspace,</li>
  <li>strategic framing,</li>
  <li>roadmap sequencing.</li>
</ul>

<p>
Without a centralized specification-versioning surface, version intent would tend to leak into many local documents and become difficult to maintain consistently.
</p>

<p>
This document therefore serves as the single published reference point for cross-version scope, stabilization, and transition logic.
</p>

<hr/>

<h2 id="scope">3. Scope</h2>
<p>
This document governs:
</p>

<ul>
  <li>published specification corpus versions,</li>
  <li>what each specification version is intended to stabilize,</li>
  <li>what remains out of scope or explicitly deferred,</li>
  <li>how version transitions should be evaluated,</li>
  <li>how other repository documents should refer to specification-version intent.</li>
</ul>

<p>
This document does not replace normative ownership of the specification itself. Normative technical law remains owned by the relevant architectural layers such as <code>Expression/</code>, <code>Language/</code>, <code>IR/</code>, <code>Libraries/</code>, <code>Profiles/</code>, and <code>IDE/</code>.
</p>

<hr/>

<h2 id="non-goals">4. Non-Goals</h2>
<p>
This document does not:
</p>

<ul>
  <li>define one product release train,</li>
  <li>define vendor-specific shipping schedules,</li>
  <li>replace roadmap milestone tracking,</li>
  <li>replace strategic justification,</li>
  <li>replace conformance expectations,</li>
  <li>define one required implementation,</li>
  <li>act as a hidden source of technical semantics.</li>
</ul>

<p>
Versioning governance is not a substitute for technical specification. It is the repository-level policy that organizes stabilization across the already-separated technical ownership layers.
</p>

<hr/>

<h2 id="three-version-notions-that-must-remain-distinct">5. Three Version Notions That Must Remain Distinct</h2>
<p>
FROG requires three different notions of version to remain explicit and non-collapsed:
</p>

<table>
  <thead>
    <tr>
      <th>Version notion</th>
      <th>What it versions</th>
      <th>Where it belongs</th>
      <th>What it must not be confused with</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Specification corpus version</td>
      <td>The published FROG specification corpus as a whole</td>
      <td>This document and repository-wide version governance</td>
      <td>Source-format compatibility or one program's artifact version</td>
    </tr>
    <tr>
      <td><code>.frog</code> <code>spec_version</code></td>
      <td>The source-format / compatibility target declared by a FROG source file</td>
      <td>Canonical source payload</td>
      <td>The repository's publication state or one program release number</td>
    </tr>
    <tr>
      <td><code>metadata.program_version</code></td>
      <td>One particular program artifact revision chosen by the author</td>
      <td>Program metadata</td>
      <td>Specification version or source-format compatibility law</td>
    </tr>
  </tbody>
</table>

<p>
These three notions are related but not interchangeable.
</p>

<hr/>

<h2 id="specification-corpus-version">6. Specification Corpus Version</h2>
<p>
The specification corpus version is the version of the published FROG specification repository considered as a public specification corpus.
</p>

<p>
It answers questions such as:
</p>

<ul>
  <li>Which architectural surfaces are already considered published and stabilized enough to be referenced together?</li>
  <li>Which closures are required before the next corpus version can be declared?</li>
  <li>Which areas remain draft, provisional, partial, or deferred?</li>
  <li>Which public distinctions are now considered repository-wide policy?</li>
</ul>

<p>
The specification corpus version is a repository-governance notion. It is not embedded as the version of an individual FROG program artifact.
</p>

<hr/>

<h2 id="frog-spec_version-source-compatibility-version">7. <code>.frog</code> <code>spec_version</code> Source Compatibility Version</h2>
<p>
The <code>spec_version</code> field in a <code>.frog</code> file identifies the source-format / compatibility version expected by that source artifact.
</p>

<p>
It answers questions such as:
</p>

<ul>
  <li>What canonical source shape is expected?</li>
  <li>Which source-level constructs are admitted?</li>
  <li>Which structural validation rules apply?</li>
  <li>Which source-visible distinctions are required for that file to be accepted as canonical source?</li>
</ul>

<p>
A repository may publish multiple documents that discuss future source-model growth, while a concrete <code>.frog</code> file still declares one source-compatibility target through <code>spec_version</code>.
</p>

<p>
Therefore:
</p>

<ul>
  <li>the repository can evolve beyond one source version,</li>
  <li>a source file can target a specific compatibility boundary,</li>
  <li>the published corpus version and the source file's <code>spec_version</code> remain distinct.</li>
</ul>

<hr/>

<h2 id="metadata-program_version-program-artifact-version">8. <code>metadata.program_version</code> Program Artifact Version</h2>
<p>
The <code>metadata.program_version</code> field versions one particular FROG program artifact as chosen by its author, maintainer, or governing process.
</p>

<p>
It answers questions such as:
</p>

<ul>
  <li>Is this program artifact revision 1.2.0 or 2.0.0?</li>
  <li>Has this authored graph changed from one release of the program to another?</li>
  <li>How should downstream tooling or users distinguish one application-level revision from another?</li>
</ul>

<p>
It does not define specification law, source compatibility law, or repository publication state.
</p>

<hr/>

<h2 id="governance-principles">9. Governance Principles</h2>
<p>
The following principles apply to specification-version governance across the published repository:
</p>

<ol>
  <li><strong>Centralization:</strong> version-transition policy should be maintained here rather than duplicated across many files.</li>
  <li><strong>Explicitness:</strong> what is stabilized, draft, deferred, or out of scope must be stated explicitly.</li>
  <li><strong>Layer preservation:</strong> versioning must not collapse architectural ownership boundaries.</li>
  <li><strong>Non-substitution:</strong> roadmap, strategy, examples, conformance, and reference implementation do not replace specification version governance.</li>
  <li><strong>Repository coherence:</strong> a version claim should refer to a coherent repository-visible state, not one isolated local rewrite.</li>
  <li><strong>Bounded closure before expansion:</strong> a version should close a coherent corridor before broadening into new unfinished fronts.</li>
  <li><strong>No hidden semantic law:</strong> runtime-private implementation convenience must not silently define version semantics.</li>
</ol>

<hr/>

<h2 id="version-boundary-model">10. Version Boundary Model</h2>
<p>
A specification version boundary is the public point at which the repository declares that a specific closure target has become coherent enough to be treated as a stabilized published corpus state.
</p>

<p>
A version boundary should not be declared solely because:
</p>

<ul>
  <li>many files changed,</li>
  <li>one implementation can run one shortcut path,</li>
  <li>a strategy document became stronger,</li>
  <li>a roadmap milestone was renamed,</li>
  <li>one example happened to work in one environment.</li>
</ul>

<p>
A version boundary should instead correspond to a coherent published closure across the relevant layers of the repository.
</p>

<p>
For example:
</p>

<pre><code>source representation
    -&gt; structural validity posture
    -&gt; validated meaning
    -&gt; execution-facing IR posture
    -&gt; lowering / handoff posture
    -&gt; bounded conformance / example / reference coherence
</code></pre>

<p>
Where a version objective includes execution-start closure or widget-object closure, the required repository-visible corridor must be coherent at those boundaries too.
</p>

<hr/>

<h2 id="stabilization-classes">11. Stabilization Classes</h2>
<p>
Each major topic discussed in the repository should be readable through one of the following stabilization classes:
</p>

<table>
  <thead>
    <tr>
      <th>Class</th>
      <th>Meaning</th>
      <th>Expected wording posture</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Normative and stabilized for current version scope</td>
      <td>Part of the current published technical law or repository-wide version boundary</td>
      <td>Clear, direct, architecture-bound, non-speculative</td>
    </tr>
    <tr>
      <td>Normative but still narrow in scope</td>
      <td>Published and binding, but only for a bounded subset</td>
      <td>Explicitly bounded and non-overclaimed</td>
    </tr>
    <tr>
      <td>Published draft</td>
      <td>Visible in the repository, but not yet treated as stabilized version boundary law</td>
      <td>Clearly marked as draft, provisional, exploratory, or subject to closure</td>
    </tr>
    <tr>
      <td>Deferred</td>
      <td>Intentionally not closed for the target version</td>
      <td>Explicitly postponed without ambiguity</td>
    </tr>
    <tr>
      <td>Out of scope</td>
      <td>Not part of the target version objective</td>
      <td>Explicitly excluded</td>
    </tr>
  </tbody>
</table>

<p>
This classification is repository-governance guidance. Technical meaning remains owned by the relevant technical documents.
</p>

<hr/>

<h2 id="cross-repository-versioning-responsibilities">12. Cross-Repository Versioning Responsibilities</h2>
<p>
Version governance must preserve the published ownership boundaries of the repository.
</p>

<table>
  <thead>
    <tr>
      <th>Repository area</th>
      <th>Primary role</th>
      <th>Versioning responsibility</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>Expression/</code></td>
      <td>Canonical source representation and source-structural posture</td>
      <td>State source-visible rules that correspond to a source compatibility target</td>
    </tr>
    <tr>
      <td><code>Language/</code></td>
      <td>Validated program meaning</td>
      <td>Stabilize semantic law for the target scope</td>
    </tr>
    <tr>
      <td><code>IR/</code></td>
      <td>Execution-facing normalized representation and downstream corridor staging</td>
      <td>Stabilize the published open IR corridor relevant to the target version</td>
    </tr>
    <tr>
      <td><code>Libraries/</code></td>
      <td>Intrinsic primitive catalog law</td>
      <td>Stabilize primitive identities and primitive-local semantics for the target scope</td>
    </tr>
    <tr>
      <td><code>Profiles/</code></td>
      <td>Optional capability-family and bounded backend-family closure</td>
      <td>State which profile-level closures are in scope for a given version</td>
    </tr>
    <tr>
      <td><code>IDE/</code></td>
      <td>Authoring, observability, debugging, inspection, Program Model</td>
      <td>State published IDE-facing boundaries without collapsing into language law</td>
    </tr>
    <tr>
      <td><code>Examples/</code></td>
      <td>Illustrative named slices</td>
      <td>Demonstrate repository-visible bounded slices without becoming semantic law</td>
    </tr>
    <tr>
      <td><code>Conformance/</code></td>
      <td>Public accept / reject / preserve truth surface</td>
      <td>Reflect the public acceptance posture of the stabilized subset</td>
    </tr>
    <tr>
      <td><code>Implementations/Reference/</code></td>
      <td>Non-normative executable workspace</td>
      <td>Exercise bounded reference paths without becoming hidden normative truth</td>
    </tr>
    <tr>
      <td><code>Roadmap/</code></td>
      <td>Non-normative sequencing</td>
      <td>Track intended closure order, not specification law</td>
    </tr>
    <tr>
      <td><code>Strategy/</code></td>
      <td>Non-normative rationale and positioning</td>
      <td>Explain why the program matters, not what version law is</td>
    </tr>
    <tr>
      <td><code>Versioning/</code></td>
      <td>Centralized specification-version governance</td>
      <td>State corpus-level stabilization and transition policy</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="compatibility-posture">13. Compatibility Posture</h2>
<p>
Compatibility claims should be made carefully and at the correct layer.
</p>

<p>
The repository should distinguish at least the following:
</p>

<ul>
  <li><strong>source compatibility</strong> — whether a <code>.frog</code> artifact conforms to the expected source-format boundary,</li>
  <li><strong>semantic compatibility</strong> — whether the validated meaning remains equivalent across specification evolution,</li>
  <li><strong>IR compatibility</strong> — whether the published execution-facing representation remains acceptable for the relevant version scope,</li>
  <li><strong>backend-handoff compatibility</strong> — whether downstream consumer-facing contracts remain stable enough for the targeted profile boundary,</li>
  <li><strong>example / conformance alignment compatibility</strong> — whether repository-visible examples and conformance material still match the intended published subset.</li>
</ul>

<p>
A compatibility statement should therefore identify:
</p>

<ul>
  <li>the layer concerned,</li>
  <li>the target scope,</li>
  <li>whether the statement is normative, bounded, draft, or deferred.</li>
</ul>

<hr/>

<h2 id="version-transition-criteria">14. Version Transition Criteria</h2>
<p>
A transition from one specification corpus version to the next should be considered only when the repository shows a coherent closure across the relevant target boundary.
</p>

<p>
The exact criteria depend on the intended version objective, but should generally include:
</p>

<ol>
  <li>the target scope is explicitly stated,</li>
  <li>the relevant ownership layers are mutually aligned,</li>
  <li>draft-only ambiguity has been reduced to an acceptable bounded level,</li>
  <li>examples and conformance material are aligned where they materially reflect the target subset,</li>
  <li>reference implementation material is not contradicting the published corridor,</li>
  <li>the new version does not silently collapse architectural boundaries.</li>
</ol>

<p>
Where the target version claims bounded executable closure, transition criteria should also include:
</p>

<ul>
  <li>an explicit execution-start contract for the bounded profile family,</li>
  <li>a repository-visible path from source to observable execution for the declared subset,</li>
  <li>clear distinction between public contract and runtime-private realization.</li>
</ul>

<p>
Where the target version claims richer widget-object closure, transition criteria should also include:
</p>

<ul>
  <li>alignment between widget declaration, widget interaction, widget class contract, UI library surface, and relevant profile-level class modeling,</li>
  <li>clear ownership of property read, property write, method invocation, and event exposure,</li>
  <li>preservation of the distinction between source declaration and IDE-synthesized node surfaces.</li>
</ul>

<hr/>

<h2 id="published-version-objectives">15. Published Version Objectives</h2>
<p>
This section centralizes the current published version objectives at a repository-governance level.
</p>

<h3>15.1 Current published closure baseline</h3>
<p>
At the current published stage of the repository, the visible closure direction is already beyond architecture-only prose.
</p>

<p>
The repository already exposes a first bounded end-to-end corridor where a controlled subset can be:
</p>

<ul>
  <li>loaded,</li>
  <li>distinguished by loadability,</li>
  <li>structurally validated,</li>
  <li>semantically validated,</li>
  <li>derived into a published execution-facing IR posture,</li>
  <li>lowered toward a backend family,</li>
  <li>emitted as a backend-facing handoff,</li>
  <li>brought to a bounded execution-start contract for a first native CPU LLVM family,</li>
  <li>and exercised through repository-visible example, conformance, and reference-path material.</li>
</ul>

<p>
The repository also already exposes a serious widget-object closure direction through source-visible widget representation, interaction surfaces, class-contract discussion, and profile-level widget class modeling.
</p>

<h3>15.2 Near-term version objective</h3>
<p>
The near-term version objective is to consolidate the first coherent published corpus version around:
</p>

<ul>
  <li>canonical source posture,</li>
  <li>structural validation posture,</li>
  <li>validated semantic posture for the bounded subset,</li>
  <li>open execution-facing IR posture,</li>
  <li>canonical JSON IR posture where published,</li>
  <li>lowering and backend contract posture,</li>
  <li>bounded Native CPU LLVM execution-start closure,</li>
  <li>bounded observable executable slices,</li>
  <li>coherent widget-object exposure for the currently published UI corridor,</li>
  <li>repository-visible conformance / examples / reference alignment.</li>
</ul>

<h3>15.3 Explicitly not yet implied by this baseline</h3>
<p>
The current near-term version objective does not automatically imply:
</p>

<ul>
  <li>all possible backend families are stabilized,</li>
  <li>all runtime families are standardized,</li>
  <li>all future widget systems are closed,</li>
  <li>all IDE behaviors are frozen,</li>
  <li>all profile families are complete,</li>
  <li>all interoperability surfaces are final.</li>
</ul>

<p>
Those areas may remain draft, partial, or deferred even if one bounded corpus version is considered coherently stabilized.
</p>

<hr/>

<h2 id="how-other-documents-should-reference-this-surface">16. How Other Documents Should Reference This Surface</h2>
<p>
When another repository document needs versioning guidance, it should keep that guidance short and point back to this document rather than restating full transition policy.
</p>

<p>
Recommended pattern:
</p>

<pre><code>This document participates in the current published FROG specification corpus scope.
Cross-version stabilization targets and transition policy are governed centrally in `Versioning/Readme.md`.
</code></pre>

<p>
Other documents should not duplicate:
</p>

<ul>
  <li>full version-transition criteria,</li>
  <li>repository-wide stabilization taxonomy,</li>
  <li>cross-version compatibility doctrine,</li>
  <li>multi-version governance policy.</li>
</ul>

<hr/>

<h2 id="change-classification-guidance">17. Change Classification Guidance</h2>
<p>
A proposed repository change should be classified before version claims are made.
</p>

<table>
  <thead>
    <tr>
      <th>Change class</th>
      <th>Typical effect</th>
      <th>Versioning concern</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Clarification</td>
      <td>Makes existing intent more explicit without changing target law</td>
      <td>Usually does not require redefining version scope, but may help close ambiguity</td>
    </tr>
    <tr>
      <td>Additive bounded closure</td>
      <td>Adds a new explicitly bounded published capability or corridor segment</td>
      <td>May expand version scope if cross-layer coherence is reached</td>
    </tr>
    <tr>
      <td>Breaking source-visible change</td>
      <td>Changes canonical source acceptance or required source distinctions</td>
      <td>Must be evaluated against <code>.frog</code> <code>spec_version</code> implications</td>
    </tr>
    <tr>
      <td>Breaking semantic change</td>
      <td>Changes validated meaning for existing accepted constructs</td>
      <td>Requires careful corpus-level transition review</td>
    </tr>
    <tr>
      <td>Downstream corridor clarification</td>
      <td>Clarifies IR, lowering, backend contract, or execution-start boundaries</td>
      <td>May affect corpus-level stabilization without changing source compatibility</td>
    </tr>
    <tr>
      <td>Implementation-only change</td>
      <td>Changes a reference or experimental implementation without changing published law</td>
      <td>Does not by itself change specification version scope</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="minimal-decision-table">18. Minimal Decision Table</h2>
<table>
  <thead>
    <tr>
      <th>Question</th>
      <th>If yes</th>
      <th>If no</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Does the change alter canonical source acceptance?</td>
      <td>Review <code>.frog</code> <code>spec_version</code> implications explicitly</td>
      <td>Do not claim source-compatibility impact</td>
    </tr>
    <tr>
      <td>Does the change alter validated semantic meaning?</td>
      <td>Treat as corpus-level semantic transition matter</td>
      <td>Keep semantic version claims narrow</td>
    </tr>
    <tr>
      <td>Does the change only clarify already-intended law?</td>
      <td>Classify as clarification unless another layer is affected</td>
      <td>Assess whether it is additive or breaking</td>
    </tr>
    <tr>
      <td>Does the change widen the bounded executable corridor?</td>
      <td>Check examples, conformance, profiles, and reference path alignment</td>
      <td>Do not overclaim execution closure</td>
    </tr>
    <tr>
      <td>Does the change widen widget-object closure?</td>
      <td>Check Expression / Libraries / Profiles alignment</td>
      <td>Do not imply richer UI-object law than published</td>
    </tr>
    <tr>
      <td>Does the change only affect roadmap or strategy?</td>
      <td>Keep it outside specification-version law</td>
      <td>Evaluate its technical layer implications separately</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="relationship-with-roadmap-strategy-and-conformance">19. Relationship with Roadmap, Strategy, and Conformance</h2>
<p>
This document must remain distinct from three nearby repository-wide surfaces:
</p>

<table>
  <thead>
    <tr>
      <th>Surface</th>
      <th>Question it answers</th>
      <th>What it must not replace</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>Strategy/</code></td>
      <td>Why FROG matters</td>
      <td>Normative ownership or version-transition law</td>
    </tr>
    <tr>
      <td><code>Roadmap/</code></td>
      <td>In what order closure is intended</td>
      <td>Normative ownership or centralized version policy</td>
    </tr>
    <tr>
      <td><code>Conformance/</code></td>
      <td>What is accepted, rejected, or preserved in public repository-visible truth surfaces</td>
      <td>Cross-version governance policy</td>
    </tr>
  </tbody>
</table>

<p>
Versioning governance sits adjacent to those surfaces, but it is not reducible to any of them.
</p>

<hr/>

<h2 id="repository-wide-versioning-diagram">20. Repository-Wide Versioning Diagram</h2>
<pre><code>published FROG repository
    |
    +-- technical ownership layers
    |      |
    |      +-- Expression/
    |      +-- Language/
    |      +-- IR/
    |      +-- Libraries/
    |      +-- Profiles/
    |      +-- IDE/
    |
    +-- support and inspection surfaces
    |      |
    |      +-- Examples/
    |      +-- Conformance/
    |      +-- Implementations/Reference/
    |
    +-- framing surfaces
    |      |
    |      +-- Strategy/
    |      +-- Roadmap/
    |
    +-- centralized version governance
           |
           +-- Versioning/Readme.md

version notions that must remain distinct:
    specification corpus version
        != .frog spec_version
        != metadata.program_version
</code></pre>

<hr/>

<h2 id="future-expansion">21. Future Expansion</h2>
<p>
This document may later be expanded with:
</p>

<ul>
  <li>a compact version history table,</li>
  <li>explicit version identifiers for successive published corpus states,</li>
  <li>migration notes between corpus versions,</li>
  <li>source-compatibility mapping tables,</li>
  <li>release-bound stabilization checklists for major closure fronts.</li>
</ul>

<p>
Such additions should remain centralized here unless a strong repository-architecture reason requires a separate dedicated subdocument set.
</p>

<hr/>

<h2 id="summary">22. Summary</h2>
<p>
FROG needs centralized specification-version governance because the repository now spans multiple technical ownership layers, executable reference slices, conformance material, profile-level closure, widget-object closure, and framing layers.
</p>

<p>
This document provides the single repository-visible place where the published specification corpus can state:
</p>

<ul>
  <li>what specification version means,</li>
  <li>how it differs from <code>.frog</code> source compatibility versioning,</li>
  <li>how it differs from program artifact versioning,</li>
  <li>what the current published closure target is,</li>
  <li>and how transition to future specification versions should be governed.</li>
</ul>

<p>
All other repository documents should keep version references lightweight and point back here instead of re-scattering cross-version policy.
</p>
