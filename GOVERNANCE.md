<h1 align="center">🐸 FROG Governance</h1>

<p align="center">
Governance model for the <strong>FROG</strong> specification repository<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#governance-goals">2. Governance Goals</a></li>
  <li><a href="#scope-of-governance">3. Scope of Governance</a></li>
  <li><a href="#stewardship">4. Stewardship</a></li>
  <li><a href="#open-specification-and-multiple-implementations">5. Open Specification and Multiple Implementations</a></li>
  <li><a href="#decision-model">6. Decision Model</a></li>
  <li><a href="#proposal-and-change-process">7. Proposal and Change Process</a></li>
  <li><a href="#compatibility-versioning-and-deprecation">8. Compatibility, Versioning, and Deprecation</a></li>
  <li><a href="#repository-contributions-and-licensing">9. Repository Contributions and Licensing</a></li>
  <li><a href="#commercial-implementations-and-ecosystem-participation">10. Commercial Implementations and Ecosystem Participation</a></li>
  <li><a href="#trademarks-certification-and-conformance">11. Trademarks, Certification, and Conformance</a></li>
  <li><a href="#future-governance-evolution">12. Future Governance Evolution</a></li>
  <li><a href="#non-goals">13. Non-Goals</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
FROG is an open language specification for graphical dataflow programming.
Its purpose is to define a durable, tool-independent, and vendor-independent foundation for executable graphical programs, standard primitive vocabularies, and related program representations.
</p>

<p>
This governance document defines how the specification repository is stewarded, how changes are evaluated, how architectural coherence is preserved, and how an open specification may coexist with multiple independent implementations.
</p>

<p>
This document governs the specification repository.
It does not require any implementation to be open source, and it does not limit the ability of any party to build commercial tools, runtimes, compilers, integrations, or services around the FROG specification.
</p>

<hr/>

<h2 id="governance-goals">2. Governance Goals</h2>

<p>
The governance of FROG exists to preserve the following goals:
</p>

<ul>
  <li>keep the specification open, readable, and implementable by independent parties,</li>
  <li>preserve long-term architectural coherence across the repository,</li>
  <li>avoid collapse of the language into one IDE, one runtime, one compiler, or one hardware vendor,</li>
  <li>allow responsible evolution of the specification over time,</li>
  <li>support a healthy ecosystem of open and commercial implementations.</li>
</ul>

<hr/>

<h2 id="scope-of-governance">3. Scope of Governance</h2>

<p>
This document applies to the governance of the FROG specification repository, including:
</p>

<ul>
  <li>the language specification,</li>
  <li>source-level program representation,</li>
  <li>execution-related specification layers when published,</li>
  <li>standard primitive-library specifications,</li>
  <li>IDE architecture specifications,</li>
  <li>related architectural and normative documents contained in this repository.</li>
</ul>

<p>
This document does not, by itself, define:
</p>

<ul>
  <li>commercial pricing,</li>
  <li>marketplace terms,</li>
  <li>OEM commercial agreements,</li>
  <li>trademark policy details,</li>
  <li>certification fees or business programs.</li>
</ul>

<p>
Those topics MAY be defined in separate policy documents if and when such documents are published.
</p>

<hr/>

<h2 id="stewardship">4. Stewardship</h2>

<p>
Graiphic is the initial steward of the FROG specification repository.
As steward, Graiphic is responsible for maintaining architectural coherence, reviewing proposed changes, deciding when documents are sufficiently mature for inclusion, and publishing authoritative repository revisions.
</p>

<p>
Stewardship of the repository does not mean that FROG is a vendor-locked product.
The purpose of stewardship is to keep the specification coherent while the language is still being actively defined and stabilized.
</p>

<p>
The steward SHOULD make decisions in a way that preserves:
</p>

<ul>
  <li>openness of the specification,</li>
  <li>clarity of normative wording,</li>
  <li>implementability by third parties,</li>
  <li>backward compatibility when reasonably possible,</li>
  <li>separation between the standard and any one implementation.</li>
</ul>

<hr/>

<h2 id="open-specification-and-multiple-implementations">5. Open Specification and Multiple Implementations</h2>

<p>
FROG is an open specification.
Any party MAY read, implement, validate, parse, compile, interpret, transform, or otherwise build tooling around the published FROG specification, subject to the repository license and any separately published policies.
</p>

<p>
The FROG specification is intended to support multiple independent implementations, including but not limited to:
</p>

<ul>
  <li>IDEs,</li>
  <li>validators,</li>
  <li>runtimes,</li>
  <li>compilers,</li>
  <li>bridges and interoperability layers,</li>
  <li>hardware integration libraries,</li>
  <li>testing and conformance tooling.</li>
</ul>

<p>
No implementation is automatically normative merely because it exists.
The repository documents are the normative source of the specification unless a document explicitly states otherwise.
</p>

<hr/>

<h2 id="decision-model">6. Decision Model</h2>

<p>
FROG governance currently follows a steward-led model.
Discussion is open, contributions are welcome, and architectural feedback is encouraged, but final editorial and architectural decisions for this repository are made by the steward.
</p>

<p>
In practice:
</p>

<ul>
  <li>contributors MAY propose changes, clarifications, corrections, and new specifications,</li>
  <li>maintainers review proposals for coherence, maturity, and alignment with repository direction,</li>
  <li>the steward decides whether a proposal is accepted, rejected, deferred, split, or redirected.</li>
</ul>

<p>
The steward SHOULD explain major architectural decisions when such explanation materially helps contributors understand repository direction.
</p>

<hr/>

<h2 id="proposal-and-change-process">7. Proposal and Change Process</h2>

<p>
The normal change path for the specification is:
</p>

<ol>
  <li>identify a problem, ambiguity, inconsistency, or missing specification area,</li>
  <li>discuss the topic through repository issues, pull requests, or equivalent review channels,</li>
  <li>propose concrete wording changes or new documents,</li>
  <li>review the proposal against repository architecture and neighboring specifications,</li>
  <li>accept, revise, defer, or reject the change.</li>
</ol>

<p>
Specification changes SHOULD be:
</p>

<ul>
  <li>explicit,</li>
  <li>conservative when modifying existing normative behavior,</li>
  <li>clear about whether they are corrective, additive, or breaking,</li>
  <li>cross-checked against directly related documents.</li>
</ul>

<p>
Editorial cleanup, factual corrections, and cross-reference alignment MAY be accepted with a lighter process than major semantic changes.
Major semantic changes SHOULD be reviewed more carefully because they may affect multiple specification layers and future implementations.
</p>

<hr/>

<h2 id="compatibility-versioning-and-deprecation">8. Compatibility, Versioning, and Deprecation</h2>

<p>
The FROG specification SHOULD evolve in a way that preserves continuity whenever reasonably possible.
However, early-stage specification work may still require structural correction and architectural refinement.
</p>

<p>
Changes SHOULD be understood under three categories:
</p>

<ul>
  <li><strong>clarification</strong> — wording becomes clearer without changing intended semantics,</li>
  <li><strong>additive change</strong> — new capability is introduced without invalidating existing compliant content,</li>
  <li><strong>breaking change</strong> — previously valid content, assumptions, or interpretations may no longer remain valid.</li>
</ul>

<p>
Breaking changes SHOULD be introduced deliberately and documented clearly.
Where appropriate, the repository SHOULD describe migration direction, replacement constructs, or deprecation rationale.
</p>

<p>
A future dedicated versioning policy MAY define more precise release classes, compatibility guarantees, and conformance targets.
</p>

<hr/>

<h2 id="repository-contributions-and-licensing">9. Repository Contributions and Licensing</h2>

<p>
Repository contributions are governed by the repository license, contribution workflow, and contributor license agreement requirements published in the root of the repository.
Contributors MUST follow the contribution process in effect for this repository.
</p>

<p>
Acceptance of a pull request is not automatic.
All contributions remain subject to repository review and steward approval.
</p>

<p>
This governance document does not replace the repository license, contributor license agreement, or contribution policy.
If any conflict appears, the applicable legal and contribution documents govern their own scope.
</p>

<hr/>

<h2 id="commercial-implementations-and-ecosystem-participation">10. Commercial Implementations and Ecosystem Participation</h2>

<p>
Open specification does not imply implementation uniformity.
Open specification also does not prohibit commercial implementations.
</p>

<p>
Any party MAY build open-source or proprietary implementations around the FROG specification, including IDEs, compilers, runtimes, libraries, integration layers, deployment systems, and commercial services.
</p>

<p>
Graiphic MAY independently develop proprietary or commercial implementations, enterprise tooling, OEM integrations, plugin ecosystems, marketplaces, hosted services, support offerings, and other products around FROG.
</p>

<p>
Such implementations do not redefine the specification merely by existing.
The specification remains governed by the normative repository documents.
</p>

<hr/>

<h2 id="trademarks-certification-and-conformance">11. Trademarks, Certification, and Conformance</h2>

<p>
The openness of the FROG specification does not automatically grant trademark rights.
Names, logos, certification marks, and official compatibility claims MAY be governed by separate policies.
</p>

<p>
An implementation MAY implement the FROG specification without being an official Graiphic product.
However, terms such as <em>official</em>, <em>certified</em>, <em>endorsed</em>, or equivalent claims SHOULD only be used in accordance with any applicable trademark, certification, or conformance policies published by the steward.
</p>

<p>
A future conformance policy MAY define categories such as:
</p>

<ul>
  <li>implements the specification,</li>
  <li>conformant implementation,</li>
  <li>certified implementation.</li>
</ul>

<p>
Those categories are not fully defined by this document alone.
</p>

<hr/>

<h2 id="future-governance-evolution">12. Future Governance Evolution</h2>

<p>
The current governance model is intentionally simple and steward-led.
As the ecosystem matures, governance MAY evolve.
</p>

<p>
Possible future evolutions MAY include:
</p>

<ul>
  <li>a documented review board,</li>
  <li>formal change proposals,</li>
  <li>a conformance working group,</li>
  <li>shared editorial maintainership,</li>
  <li>an independent foundation or multi-party governance structure.</li>
</ul>

<p>
Any such change SHOULD preserve the core goals of openness, implementability, architectural coherence, and long-term ecosystem durability.
</p>

<hr/>

<h2 id="non-goals">13. Non-Goals</h2>

<p>
This document does not attempt to:
</p>

<ul>
  <li>freeze the future institutional structure of FROG,</li>
  <li>define detailed trademark law or certification contracts,</li>
  <li>mandate that implementations be open source,</li>
  <li>mandate that implementations be proprietary,</li>
  <li>select a single business model for Graiphic or for the ecosystem.</li>
</ul>

<p>
Its purpose is narrower:
to state how the specification repository is governed, how openness is preserved, and how multiple implementations may coexist without collapsing the language into a single vendor product.
</p>

<hr/>

<p align="center">
FROG — open specification, durable governance, multiple implementations
</p>
