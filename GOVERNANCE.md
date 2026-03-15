<p align="center">
  <img src="FROG logo.svg" alt="FROG logo" width="140" />
</p>

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
  <li><a href="#commercial-vs-non-commercial-certification-direction">12. Commercial vs Non-Commercial Certification Direction</a></li>
  <li><a href="#future-governance-evolution">13. Future Governance Evolution</a></li>
  <li><a href="#non-goals">14. Non-Goals</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
FROG is an open language specification for graphical dataflow programming.
Its purpose is to define a durable, tool-independent, and vendor-independent foundation for executable graphical programs, intrinsic primitive vocabularies, optional standardized capability profiles, and related program representations.
</p>

<p>
This governance document defines how the specification repository is stewarded, how changes are evaluated, how architectural coherence is preserved, and how an open specification may coexist with multiple independent implementations.
</p>

<p>
This document governs the specification repository.
It does not require any implementation to be open source, and it does not prohibit any party from building commercial tools, runtimes, compilers, integrations, services, or full IDE platforms around the FROG specification.
</p>

<hr/>

<h2 id="governance-goals">2. Governance Goals</h2>

<p>
The governance of FROG exists to preserve the following goals:
</p>

<ul>
  <li>keep the specification open, readable, and implementable by independent parties,</li>
  <li>preserve long-term architectural coherence across the repository,</li>
  <li>avoid collapse of the language into one IDE, one runtime, one compiler, one profile implementation, or one hardware vendor,</li>
  <li>allow responsible evolution of the specification over time,</li>
  <li>support a healthy ecosystem of open and commercial implementations,</li>
  <li>keep a clean distinction between the core language, optional standardized profiles, and implementation-specific extensions,</li>
  <li>protect the integrity of official FROG branding, certification, and compatibility claims.</li>
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
  <li>intrinsic standard primitive-library specifications,</li>
  <li>optional standardized profile specifications,</li>
  <li>IDE architecture specifications,</li>
  <li>related architectural and normative documents contained in this repository.</li>
</ul>

<p>
This document does not, by itself, fully define:
</p>

<ul>
  <li>detailed commercial pricing,</li>
  <li>marketplace terms,</li>
  <li>OEM commercial agreements,</li>
  <li>detailed trademark law,</li>
  <li>detailed certification contracts,</li>
  <li>all future certification program procedures.</li>
</ul>

<p>
Those topics MAY be defined more precisely in separate policy documents if and when such documents are published.
</p>

<hr/>

<h2 id="stewardship">4. Stewardship</h2>

<p>
Graiphic is the initial steward of the FROG specification repository.
As steward, Graiphic is responsible for maintaining architectural coherence, reviewing proposed changes, deciding when documents are sufficiently mature for inclusion, and publishing authoritative repository revisions.
</p>

<p>
Stewardship of the repository does not mean that FROG is a vendor-locked product.
The purpose of stewardship is to keep the specification coherent while the language is still being actively defined, cleaned up, and stabilized.
</p>

<p>
The steward SHOULD make decisions in a way that preserves:
</p>

<ul>
  <li>openness of the specification,</li>
  <li>clarity of normative wording,</li>
  <li>implementability by third parties,</li>
  <li>backward compatibility when reasonably possible,</li>
  <li>separation between the standard and any one implementation,</li>
  <li>clear boundaries between intrinsic libraries, profiles, and implementation-specific extensions.</li>
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
  <li>profile-supporting execution environments,</li>
  <li>testing and conformance tooling.</li>
</ul>

<p>
No implementation is automatically normative merely because it exists.
The repository documents are the normative source of the specification unless a document explicitly states otherwise.
</p>

<p>
An implementation MAY support:
</p>

<ul>
  <li>core FROG only,</li>
  <li>core FROG plus one or more standardized profiles,</li>
  <li>core FROG plus profiles plus additional proprietary or open extensions.</li>
</ul>

<p>
Support for optional profiles is not automatically required for core language support unless a future policy explicitly defines a stricter conformance target.
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
  <li>the steward decides whether a proposal is accepted, rejected, deferred, split, redirected, or accepted in a narrower form.</li>
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
  <li>review the proposal against repository architecture and directly related specifications,</li>
  <li>accept, revise, defer, split, redirect, or reject the change.</li>
</ol>

<p>
Specification changes SHOULD be:
</p>

<ul>
  <li>explicit,</li>
  <li>conservative when modifying existing normative behavior,</li>
  <li>clear about whether they are corrective, additive, or breaking,</li>
  <li>cross-checked against directly related documents,</li>
  <li>clear about whether they affect the core language, an intrinsic library, a profile, or only an IDE-facing concern.</li>
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
A future dedicated versioning policy MAY define more precise release classes, compatibility guarantees, profile-version compatibility rules, and conformance targets.
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
Any party MAY build open-source or proprietary implementations around the FROG specification, including IDEs, compilers, runtimes, libraries, profiles, integration layers, deployment systems, and commercial services.
</p>

<p>
Graiphic MAY independently develop proprietary or commercial implementations, enterprise tooling, OEM integrations, plugin ecosystems, marketplaces, hosted services, support offerings, certification programs, and other products around FROG.
</p>

<p>
Such implementations do not redefine the specification merely by existing.
The specification remains governed by the normative repository documents.
</p>

<hr/>

<h2 id="trademarks-certification-and-conformance">11. Trademarks, Certification, and Conformance</h2>

<p>
The openness of the FROG specification does not automatically grant trademark rights.
Names, logos, certification marks, and official compatibility claims are governed by the steward and MAY be subject to separate policies.
</p>

<p>
An implementation MAY implement the FROG specification without being an official Graiphic product.
However, terms such as <em>official</em>, <em>certified</em>, <em>endorsed</em>, <em>FROG-certified</em>, or equivalent claims SHOULD only be used in accordance with applicable trademark, certification, or conformance policies published by the steward.
</p>

<p>
A future conformance policy SHOULD distinguish at least the following categories:
</p>

<ul>
  <li><strong>implements core FROG</strong> — the implementation claims support for the core language surface only,</li>
  <li><strong>implements core FROG + named profiles</strong> — the implementation claims support for the core language plus one or more explicitly identified standardized profiles,</li>
  <li><strong>conformant implementation</strong> — the implementation satisfies the requirements of the claimed conformance target under an applicable conformance policy,</li>
  <li><strong>certified implementation</strong> — the implementation has been verified and approved under an applicable certification or branding policy.</li>
</ul>

<p>
A claim of profile support SHOULD identify the supported profile explicitly rather than implying universal support for all optional capability families in the repository.
</p>

<p>
Support for a profile MUST NOT, by itself, be treated as support for all profiles.
Likewise, lack of support for a profile MUST NOT, by itself, be treated as failure of core language support unless the claimed target explicitly includes that profile.
</p>

<hr/>

<h2 id="commercial-vs-non-commercial-certification-direction">12. Commercial vs Non-Commercial Certification Direction</h2>

<p>
The steward MAY define a certification and branding program for implementations that wish to use official FROG certification, official compatibility branding, or equivalent steward-controlled marks.
</p>

<p>
The intended direction is:
</p>

<ul>
  <li>commercial implementations that seek official certification, official branding, or equivalent steward-controlled compatibility recognition MAY be subject to paid verification, licensing, or program fees,</li>
  <li>non-commercial implementations MAY be verified and certified free of charge or at minimal cost, subject to steward review and applicable policy,</li>
  <li>the specification itself remains open regardless of whether an implementation participates in any certification or branding program.</li>
</ul>

<p>
This distinction exists to preserve openness of the language specification while allowing the steward to govern the FROG name, branding integrity, and certification responsibility over time.
</p>

<p>
More detailed rules, procedures, fee schedules, eligibility conditions, and branding requirements MAY be defined later in separate policy documents.
</p>

<hr/>

<h2 id="future-governance-evolution">13. Future Governance Evolution</h2>

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
Any such change SHOULD preserve the core goals of openness, implementability, architectural coherence, branding clarity, and long-term ecosystem durability.
</p>

<hr/>

<h2 id="non-goals">14. Non-Goals</h2>

<p>
This document does not attempt to:
</p>

<ul>
  <li>freeze the future institutional structure of FROG,</li>
  <li>define detailed trademark law or certification contracts,</li>
  <li>mandate that implementations be open source,</li>
  <li>mandate that implementations be proprietary,</li>
  <li>select a single business model for Graiphic or for the ecosystem,</li>
  <li>force all implementations to support the same optional profiles.</li>
</ul>

<p>
Its purpose is narrower:
to state how the specification repository is governed, how openness is preserved, how branding and certification authority are separated from the open language itself, and how multiple implementations may coexist without collapsing the language into a single vendor product.
</p>

<hr/>

<p align="center">
FROG — open specification, durable governance, multiple implementations
</p>
