<h1 align="center">🐸 Contributing to FROG</h1>

<p align="center">
Contribution guidelines for the FROG specification repository<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#project-status">1. Project Status</a></li>
  <li><a href="#how-you-can-contribute">2. How You Can Contribute</a></li>
  <li><a href="#repository-architecture">3. Repository Architecture</a></li>
  <li><a href="#where-to-start">4. Where to Start</a></li>
  <li><a href="#recommended-workflow">5. Recommended Workflow</a></li>
  <li><a href="#before-you-modify-a-document">6. Before You Modify a Document</a></li>
  <li><a href="#contribution-expectations">7. Contribution Expectations</a></li>
  <li><a href="#change-categories">8. Change Categories</a></li>
  <li><a href="#cross-document-coherence">9. Cross-Document Coherence</a></li>
  <li><a href="#governance">10. Governance</a></li>
  <li><a href="#contributor-license-agreement">11. Contributor License Agreement</a></li>
  <li><a href="#licensing">12. Licensing</a></li>
  <li><a href="#community-and-collaboration">13. Community and Collaboration</a></li>
</ul>

<hr/>

<h2 id="project-status">1. Project Status</h2>

<p>
FROG is an open specification project defining a modern graphical dataflow language and its related architectural layers.
</p>

<p>
The repository is still in an active design and stabilization phase.
Many documents are already substantial, but some areas are still being clarified, split, aligned, or structurally refactored.
Contributions in the form of ideas, corrections, issue reports, specification proposals, architectural cleanup, and wording improvements are welcome.
</p>

<p>
Because this is a specification repository rather than an ordinary application repository, contributions should prioritize:
</p>

<ul>
  <li>clarity,</li>
  <li>precision,</li>
  <li>architectural coherence,</li>
  <li>durable wording,</li>
  <li>implementable semantics.</li>
</ul>

<hr/>

<h2 id="how-you-can-contribute">2. How You Can Contribute</h2>

<p>
There are several useful ways to contribute to FROG:
</p>

<ul>
  <li>improve documentation,</li>
  <li>clarify ambiguous or inconsistent specification wording,</li>
  <li>propose architectural refinements,</li>
  <li>propose new specifications or missing specification areas,</li>
  <li>identify duplication or ownership conflicts between documents,</li>
  <li>open issues to discuss design questions,</li>
  <li>submit pull requests,</li>
  <li>participate in repository-level architectural discussions.</li>
</ul>

<p>
Early contributions are especially valuable when they improve:
</p>

<ul>
  <li>cross-document consistency,</li>
  <li>terminology alignment,</li>
  <li>ownership clarity between specification layers,</li>
  <li>normative wording quality,</li>
  <li>long-term navigability of the repository.</li>
</ul>

<hr/>

<h2 id="repository-architecture">3. Repository Architecture</h2>

<p>
FROG is organized by architectural responsibility.
Contributors SHOULD understand which layer owns which topic before proposing a change.
</p>

<pre><code>FROG/
│
├── Expression/   canonical source specification
├── IDE/          authoring, observability, debugging, probes, watch, snippets
├── Language/     normative execution semantics
├── Libraries/    standard primitive-library specifications
│
├── GOVERNANCE.md
├── CLA.md
├── CONTRIBUTING.md
├── LICENSE
└── Readme.md</code></pre>

<p>
Layer ownership in summary:
</p>

<ul>
  <li><strong><code>Expression/</code></strong> — canonical source representation and source-visible program objects,</li>
  <li><strong><code>Language/</code></strong> — normative execution semantics and cross-cutting semantic rules,</li>
  <li><strong><code>Libraries/</code></strong> — standard primitive identities, ports, metadata, and library-owned primitive definitions,</li>
  <li><strong><code>IDE/</code></strong> — authoring architecture, observability, debugging, probes, watch, and snippet workflows.</li>
</ul>

<p>
If a contribution crosses multiple layers, the contributor SHOULD identify which document is the primary owner of the topic.
</p>

<hr/>

<h2 id="where-to-start">4. Where to Start</h2>

<p>
Before contributing, you SHOULD begin by reading:
</p>

<ul>
  <li><code>Readme.md</code> at the repository root,</li>
  <li>the <code>Readme.md</code> of the relevant top-level directory,</li>
  <li>the exact file you intend to modify,</li>
  <li>directly related specification files in the same semantic area,</li>
  <li>existing issues and discussions when relevant.</li>
</ul>

<p>
Typical entry points:
</p>

<ul>
  <li><code>Expression/</code> — canonical source specification</li>
  <li><code>Language/</code> — normative execution semantics</li>
  <li><code>Libraries/</code> — standard primitive-library specifications</li>
  <li><code>IDE/</code> — IDE architecture, authoring workflows, observability, debugging, and snippets</li>
</ul>

<p>
Contributors SHOULD avoid modifying a document in isolation when its topic is semantically connected to neighboring documents.
</p>

<hr/>

<h2 id="recommended-workflow">5. Recommended Workflow</h2>

<p>
The preferred contribution workflow follows the standard GitHub model using forks and pull requests.
</p>

<pre><code>Contributor
     │
     │ Fork
     ▼
Your Fork Repository
     │
     │ Create branch
     │ Commit changes
     ▼
Pull Request
     │
     │ Review by maintainers
     ▼
Graiphic / FROG main repository</code></pre>

<p>
This workflow allows maintainers to review contributions while preserving repository-wide architectural coherence.
</p>

<p>
Recommended step-by-step process:
</p>

<ol>
  <li>Fork the repository.</li>
  <li>Create a branch for your change.</li>
  <li>Re-read the current version of the target document and its directly related documents.</li>
  <li>Commit your modifications.</li>
  <li>Open a Pull Request.</li>
  <li>Discuss the proposal with maintainers if clarification is needed.</li>
</ol>

<hr/>

<h2 id="before-you-modify-a-document">6. Before You Modify a Document</h2>

<p>
Because FROG is a specification repository, contributors MUST work from the current repository state rather than from memory,
assumption, or older draft wording.
</p>

<p>
Before modifying a document, you SHOULD:
</p>

<ul>
  <li>start from the current version of the target file,</li>
  <li>read the relevant top-level <code>Readme.md</code>,</li>
  <li>read directly related files in the same semantic area,</li>
  <li>identify whether the target document is the primary owner of the topic,</li>
  <li>identify any cross-document conflict before rewriting.</li>
</ul>

<p>
Contributors SHOULD NOT:
</p>

<ul>
  <li>rewrite a document from scratch without taking the current content into account,</li>
  <li>invent repository structure, file names, or ownership assumptions that are not present in the repository,</li>
  <li>move semantic ownership casually from one layer to another without clearly explaining the architectural reason,</li>
  <li>remove useful existing content merely because a shorter formulation is possible.</li>
</ul>

<hr/>

<h2 id="contribution-expectations">7. Contribution Expectations</h2>

<p>
FROG documents are specification documents.
Contributions SHOULD therefore aim for wording that is:
</p>

<ul>
  <li>explicit,</li>
  <li>stable over time,</li>
  <li>architecturally coherent,</li>
  <li>implementable,</li>
  <li>clear about ownership and scope.</li>
</ul>

<p>
Contributors SHOULD:
</p>

<ul>
  <li>preserve useful existing content when possible,</li>
  <li>prefer conservative rewrites when editing an existing specification,</li>
  <li>improve the document rather than merely shorten it,</li>
  <li>distinguish clearly between current published state and proposed architectural direction when that distinction matters,</li>
  <li>use explicit normative wording when the document is intended to be normative.</li>
</ul>

<p>
Contributors SHOULD call out:
</p>

<ul>
  <li>ownership conflicts,</li>
  <li>duplication between documents,</li>
  <li>ambiguous terminology,</li>
  <li>under-specified behavior,</li>
  <li>outdated references or obsolete repository assumptions.</li>
</ul>

<hr/>

<h2 id="change-categories">8. Change Categories</h2>

<p>
When proposing a change, contributors SHOULD make clear which category the change belongs to:
</p>

<ul>
  <li><strong>clarification</strong> — wording becomes clearer without changing intended semantics,</li>
  <li><strong>editorial cleanup</strong> — formatting, cross-references, navigation, or readability improve without changing intended meaning,</li>
  <li><strong>additive change</strong> — new capability or new specification area is added without invalidating current compliant content,</li>
  <li><strong>architectural refactor</strong> — ownership, layering, or document boundaries are reorganized for coherence,</li>
  <li><strong>breaking change</strong> — previously valid content, assumptions, or interpretations may no longer remain valid.</li>
</ul>

<p>
Major semantic or architectural changes SHOULD explain:
</p>

<ul>
  <li>what problem they solve,</li>
  <li>which neighboring documents are affected,</li>
  <li>whether migration or follow-up cleanup is required.</li>
</ul>

<hr/>

<h2 id="cross-document-coherence">9. Cross-Document Coherence</h2>

<p>
A contribution is stronger when it respects repository-wide coherence rather than improving one file locally while creating
inconsistency elsewhere.
</p>

<p>
Contributors SHOULD therefore cross-check:
</p>

<ul>
  <li>top-level ownership boundaries,</li>
  <li>terminology consistency,</li>
  <li>duplicate topic coverage,</li>
  <li>references between layers,</li>
  <li>examples that may have become stale after an architectural change.</li>
</ul>

<p>
If a contributor identifies a conflict but only proposes a local change, the Pull Request SHOULD still explain the broader conflict.
</p>

<hr/>

<h2 id="governance">10. Governance</h2>

<p>
FROG is an open specification project with repository-level governance.
Contributors SHOULD remain consistent with the governance model and the current architectural direction of the specification.
</p>

<p>
See:
</p>

<p>
<code>GOVERNANCE.md</code>
</p>

<hr/>

<h2 id="contributor-license-agreement">11. Contributor License Agreement</h2>

<p>
By submitting a contribution, you agree to the Contributor License Agreement.
</p>

<p>
See:
</p>

<p>
<code>CLA.md</code>
</p>

<p>
If CLA signing is required for your Pull Request, the repository workflow may prompt you through the configured CLA process.
</p>

<hr/>

<h2 id="licensing">12. Licensing</h2>

<p>
Repository content is governed by the repository license.
Contributors are responsible for ensuring that they have the legal right to submit their work under the licensing terms used by this repository.
</p>

<p>
See:
</p>

<p>
<code>LICENSE</code>
</p>

<hr/>

<h2 id="community-and-collaboration">13. Community and Collaboration</h2>

<p>
FROG aims to build an open ecosystem around graphical dataflow programming.
Constructive discussions, careful specification proposals, editorial cleanup, and serious architectural reasoning are encouraged.
</p>

<p>
The goal is not only to add more content.
The goal is to build a coherent, durable, and implementable specification that can support multiple independent implementations over time.
</p>
