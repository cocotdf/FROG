<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">FROG Version Matrix</h1>

<p align="center">
  <strong>Centralized current-status table for the published FROG specification corpus</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#how-to-read-this-matrix">2. How to Read This Matrix</a></li>
  <li><a href="#current-repository-wide-values">3. Current Repository-Wide Values</a></li>
  <li><a href="#current-surface-matrix">4. Current Surface Matrix</a></li>
  <li><a href="#version-status-legend">5. Version Status Legend</a></li>
  <li><a href="#cross-version-handling-summary">6. Cross-Version Handling Summary</a></li>
  <li><a href="#maintenance-rule">7. Maintenance Rule</a></li>
  <li><a href="#summary">8. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>
<p>
This document is the centralized detailed status table for the current published FROG specification corpus.
</p>

<p>
It complements <code>Versioning/Readme.md</code> by giving a compact matrix view of:
</p>

<ul>
  <li>the current repository-wide version posture,</li>
  <li>the current scope and status of each major repository surface,</li>
  <li>the difference between stabilized, bounded, draft, deferred, and framing areas,</li>
  <li>the current next closure target where that is useful to state explicitly.</li>
</ul>

<p>
This matrix is a governance and visibility surface. It does not replace the normative ownership of the technical documents themselves.
</p>

<hr/>

<h2 id="how-to-read-this-matrix">2. How to Read This Matrix</h2>
<p>
Each row should be interpreted as the current repository-visible posture of one surface, not as a promise that every detail inside that surface is equally complete.
</p>

<p>
The main columns are:
</p>

<ul>
  <li><strong>Surface</strong> — repository area or cross-cutting closure surface,</li>
  <li><strong>Current scope version</strong> — current declared bounded version scope for that surface,</li>
  <li><strong>Status</strong> — stabilization posture for that surface,</li>
  <li><strong>Primary role</strong> — what architectural responsibility that surface owns,</li>
  <li><strong>Current posture</strong> — compact description of what is currently true,</li>
  <li><strong>Next coherent closure step</strong> — the smallest next step that would improve coherence.</li>
</ul>

<hr/>

<h2 id="current-repository-wide-values">3. Current Repository-Wide Values</h2>
<table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Current value</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Specification corpus version</td>
      <td><code>0.1-draft</code></td>
      <td>Current repository-wide published posture under consolidation</td>
    </tr>
    <tr>
      <td>Reference source-format target</td>
      <td><code>.frog spec_version = 0.1</code></td>
      <td>Bounded source compatibility target for the current published subset</td>
    </tr>
    <tr>
      <td>Current repository-wide status</td>
      <td>Bounded published closure under consolidation</td>
      <td>The repository already exposes a real end-to-end corridor but not all surfaces are equally stabilized</td>
    </tr>
    <tr>
      <td>Versioning doctrine</td>
      <td>Additive by default, explicit degraded readability, preservable when safe</td>
      <td>Governed centrally in <code>Versioning/Readme.md</code></td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="current-surface-matrix">4. Current Surface Matrix</h2>
<table>
  <thead>
    <tr>
      <th>Surface</th>
      <th>Current scope version</th>
      <th>Status</th>
      <th>Primary role</th>
      <th>Current posture</th>
      <th>Next coherent closure step</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>Readme.md</code> (root)</td>
      <td><code>0.1-draft</code></td>
      <td>Published, broad framing, mostly aligned</td>
      <td>Repository-level entry point and top-level architecture framing</td>
      <td>Describes the current multi-layer repository posture and the bounded end-to-end corridor</td>
      <td>Add a short introduction of <code>Versioning/</code> as a distinct repository-level governance surface</td>
    </tr>
    <tr>
      <td><code>Expression/</code></td>
      <td><code>0.1</code></td>
      <td>Normative, bounded published scope</td>
      <td>Canonical source representation and source-visible boundaries</td>
      <td>Owns canonical source shape for the currently published subset</td>
      <td>Keep source-level extensibility points and version-facing guidance aligned with the centralized versioning doctrine</td>
    </tr>
    <tr>
      <td><code>Language/</code></td>
      <td><code>0.1</code></td>
      <td>Normative, bounded published scope</td>
      <td>Validated meaning of accepted programs</td>
      <td>Provides semantic law for the currently published subset</td>
      <td>Continue tightening semantic closure only where needed by currently published executable and widget corridors</td>
    </tr>
    <tr>
      <td><code>IR/</code></td>
      <td><code>0.1</code></td>
      <td>Normative, bounded published scope</td>
      <td>Execution-facing normalized representation and downstream corridor staging</td>
      <td>Already carries execution IR, derivation, schema, lowering, backend contract, and related corridor material</td>
      <td>Keep IR corridor language tightly aligned with the currently bounded executable and backend-family claims</td>
    </tr>
    <tr>
      <td><code>Libraries/</code></td>
      <td><code>0.1</code></td>
      <td>Normative, bounded published scope</td>
      <td>Intrinsic primitive catalog law</td>
      <td>Owns primitive namespaces and primitive-local semantics for the bounded published subset</td>
      <td>Keep intrinsic-library scope clearly separated from profile-owned capability growth</td>
    </tr>
    <tr>
      <td><code>Profiles/</code></td>
      <td><code>0.1-draft</code></td>
      <td>Bounded published closure with active growth fronts</td>
      <td>Optional capability-family and profile-level closure</td>
      <td>Already includes Native CPU LLVM and UI widget class surfaces, but remains a high-leverage growth area</td>
      <td>Keep Native CPU LLVM and widget-related profiles coherent before widening to additional families</td>
    </tr>
    <tr>
      <td><code>IDE/</code></td>
      <td><code>0.1-draft</code></td>
      <td>Published draft / bounded architecture surface</td>
      <td>Authoring, observability, inspection, debugging, Program Model</td>
      <td>Published and meaningful, but not yet a fully frozen ecosystem-wide law surface</td>
      <td>Keep IDE-facing boundaries explicit without turning one future IDE behavior into hidden semantic law</td>
    </tr>
    <tr>
      <td><code>Examples/</code></td>
      <td><code>0.1</code></td>
      <td>Published, bounded, aligned support surface</td>
      <td>Named illustrative slices</td>
      <td>Provides named examples for the bounded published corridor</td>
      <td>Maintain strict alignment with conformance and executable reference slices</td>
    </tr>
    <tr>
      <td><code>Conformance/</code></td>
      <td><code>0.1</code></td>
      <td>Published, bounded, high-priority truth surface</td>
      <td>Public accept / reject / preserve expectations</td>
      <td>Already acts as a major repository-visible truth surface for the bounded published subset</td>
      <td>Keep numbering, mirroring, and corridor-family coverage aligned with the actual published claims</td>
    </tr>
    <tr>
      <td><code>Implementations/Reference/</code></td>
      <td><code>0.1-draft</code></td>
      <td>Published non-normative bounded executable workspace</td>
      <td>Reference path exercise without normative ownership</td>
      <td>Exercises a real reference corridor from loading toward bounded execution path</td>
      <td>Keep it aligned with published contracts without allowing it to become hidden normative law</td>
    </tr>
    <tr>
      <td><code>Roadmap/</code></td>
      <td>n/a</td>
      <td>Published non-normative framing</td>
      <td>Closure sequencing and milestone posture</td>
      <td>Helps sequence work but does not define current version truth</td>
      <td>Keep roadmap intent distinct from centralized version-state reporting</td>
    </tr>
    <tr>
      <td><code>Strategy/</code></td>
      <td>n/a</td>
      <td>Published non-normative framing</td>
      <td>Rationale, positioning, and broader justification</td>
      <td>Explains why FROG matters but does not define current version truth</td>
      <td>Keep strategy language distinct from normative version governance</td>
    </tr>
    <tr>
      <td><code>Versioning/Readme.md</code></td>
      <td><code>0.1-draft</code></td>
      <td>Draft-to-add centralized governance surface</td>
      <td>Specification-version governance entry point</td>
      <td>Should centralize doctrine, current corpus version, and transition logic</td>
      <td>Publish and then lightly reference it from the root README and nearby repository-level surfaces</td>
    </tr>
    <tr>
      <td><code>Versioning/Matrix.md</code></td>
      <td><code>0.1-draft</code></td>
      <td>Draft-to-add centralized status matrix</td>
      <td>Detailed current-state matrix for repository surfaces</td>
      <td>Should centralize the current per-surface status table</td>
      <td>Publish and keep it maintained as the single detailed current-status table</td>
    </tr>
    <tr>
      <td>Bounded executable corridor</td>
      <td><code>0.1</code></td>
      <td>Published bounded closure</td>
      <td>Repository-visible source-to-execution corridor for the first bounded slice</td>
      <td>Already present across root framing, IR, Profiles, Examples, Conformance, and Reference workspace</td>
      <td>Preserve coherence before broadening to additional backend families or runtime families</td>
    </tr>
    <tr>
      <td>Widget-object corridor</td>
      <td><code>0.1-draft</code></td>
      <td>Published bounded closure with active growth</td>
      <td>Source-visible widget declaration, interaction, class contract, and profile-level class modeling</td>
      <td>Already serious and repository-visible, but still a likely growth front</td>
      <td>Keep ownership and object-surface distinctions aligned across Expression, Libraries, and Profiles</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="version-status-legend">5. Version Status Legend</h2>
<table>
  <thead>
    <tr>
      <th>Status label</th>
      <th>Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Normative, bounded published scope</td>
      <td>Published and binding for the currently declared bounded subset</td>
    </tr>
    <tr>
      <td>Published, bounded, aligned support surface</td>
      <td>Published support area aligned with the bounded published corridor, but not itself the sole source of normative law</td>
    </tr>
    <tr>
      <td>Published non-normative bounded executable workspace</td>
      <td>Published and useful, but non-normative by design</td>
    </tr>
    <tr>
      <td>Published draft</td>
      <td>Published and important, but not yet treated as fully stabilized repository-wide closure law</td>
    </tr>
    <tr>
      <td>Draft-to-add</td>
      <td>Proposed new published surface not yet present in the currently published repository tree</td>
    </tr>
    <tr>
      <td>Non-normative framing</td>
      <td>Published rationale or sequencing surface that must remain distinct from specification law</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="cross-version-handling-summary">6. Cross-Version Handling Summary</h2>
<p>
The current repository-wide versioning doctrine is:
</p>

<pre><code>open if possible
inspect what is known
preserve what is unknown when safe
refuse unsafe semantic or executable claims
never silently misinterpret
</code></pre>

<p>
This doctrine applies across the matrix as a repository-wide governance rule. Detailed policy remains centralized in <code>Versioning/Readme.md</code>.
</p>

<hr/>

<h2 id="maintenance-rule">7. Maintenance Rule</h2>
<p>
This matrix should be updated whenever one of the following changes:
</p>

<ul>
  <li>the declared specification corpus version,</li>
  <li>the bounded published source target,</li>
  <li>the stabilization status of a major repository surface,</li>
  <li>the declared next closure target of a major repository surface,</li>
  <li>the repository adds or removes a major top-level specification or support surface.</li>
</ul>

<p>
This file should remain compact, current, and centralized. Other documents should reference it rather than re-creating competing status tables.
</p>

<hr/>

<h2 id="summary">8. Summary</h2>
<p>
This file is the central detailed version-status table for the published FROG specification corpus.
</p>

<p>
It should answer, in one place:
</p>

<ul>
  <li>what the current repository-wide specification version is,</li>
  <li>which surfaces are currently bounded and stabilized,</li>
  <li>which surfaces remain draft or framing-only,</li>
  <li>which cross-cutting corridors are already real,</li>
  <li>and what the next smallest coherent closure steps are.</li>
</ul>
