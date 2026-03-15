<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG Profiles</h1>

<p align="center">
  Optional standardized capability families for FROG<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#purpose">2. Purpose of Profiles</a></li>
  <li><a href="#architectural-role">3. Architectural Role</a></li>
  <li><a href="#scope">4. Scope of this Directory</a></li>
  <li><a href="#what-profiles-may-define">5. What Profiles MAY Define</a></li>
  <li><a href="#what-profiles-must-not-define">6. What Profiles MUST NOT Define</a></li>
  <li><a href="#relation-with-other-specifications">7. Relation with Other Specifications</a></li>
  <li><a href="#current-profile-specifications">8. Current Profile Specifications</a></li>
  <li><a href="#profile-identification-and-claims">9. Profile Identification and Claims</a></li>
  <li><a href="#core-conformance-profile-support-and-certification">10. Core Conformance, Profile Support, and Certification</a></li>
  <li><a href="#profile-evolution">11. Profile Evolution</a></li>
  <li><a href="#status">12. Status</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines <strong>optional standardized capability families</strong> for FROG.
</p>

<p>
A profile is a standardized specification layer that extends the usable capability surface of FROG
without changing the canonical source structure of the language core and without redefining the
cross-cutting execution semantics owned by the core language specification.
</p>

<p>
Profiles exist to standardize capability areas that are important for practical ecosystems but that
should not be treated as intrinsic, always-present, mandatory parts of the minimal FROG core.
</p>

<p>
Within the current repository architecture:
</p>

<ul>
  <li><code>Expression/</code> owns canonical source representation.</li>
  <li><code>Language/</code> owns normative execution semantics.</li>
  <li><code>Libraries/</code> owns intrinsic standard primitive vocabularies.</li>
  <li><code>Profiles/</code> owns optional standardized capability families.</li>
  <li><code>IDE/</code> owns authoring, observability, debugging, inspection, and related tooling responsibilities.</li>
</ul>

<hr/>

<h2 id="purpose">2. Purpose of Profiles</h2>

<p>
The purpose of this directory is to provide a clean architectural home for specification material that is:
</p>

<ul>
  <li>standardized,</li>
  <li>useful across multiple implementations,</li>
  <li>optional rather than mandatory for the language core,</li>
  <li>sometimes dependent on external runtimes, host environments, protocols, services, deployment assumptions, or ecosystem contracts.</li>
</ul>

<p>
This separation keeps the FROG core small, stable, portable, and durable while still allowing the
standard to define broader capability surfaces where justified.
</p>

<p>
A profile is therefore neither:
</p>

<ul>
  <li>a replacement for the language core,</li>
  <li>a dumping ground for implementation-specific features,</li>
  <li>nor an excuse to move core language meaning into optional documents.</li>
</ul>

<hr/>

<h2 id="architectural-role">3. Architectural Role</h2>

<p>
Profiles occupy a distinct architectural role between the minimal core standard and purely
implementation-specific extensions.
</p>

<p>
They are intended to standardize capability families that are broader than one vendor-specific
extension but narrower than the mandatory language core.
</p>

<pre>FROG specification architecture

Expression/   - canonical source form
Language/     - normative execution semantics
Libraries/    - intrinsic standard primitive vocabularies
Profiles/     - optional standardized capability families
IDE/          - authoring, observability, debugging, inspection

Implementations MAY support:
- core only
- core + one or more profiles
- core + profiles + additional proprietary or open extensions
</pre>

<p>
This model preserves a stable architectural center while allowing the ecosystem to grow through
bounded optional capability families.
</p>

<hr/>

<h2 id="scope">4. Scope of this Directory</h2>

<p>
This directory is the normative home of optional profile specifications.
</p>

<p>
A profile specification MAY define:
</p>

<ul>
  <li>an optional primitive namespace or namespace family,</li>
  <li>additional primitive catalogs and port models,</li>
  <li>profile-local validation rules,</li>
  <li>profile-local capability assumptions,</li>
  <li>profile-local execution or target constraints,</li>
  <li>profile-specific terminology and behavior that remain outside the minimal intrinsic language surface,</li>
  <li>optional capability contracts that implementations MAY claim explicitly.</li>
</ul>

<p>
A profile specification MUST remain subordinate to the core language architecture.
</p>

<hr/>

<h2 id="what-profiles-may-define">5. What Profiles MAY Define</h2>

<p>
A profile specification MAY define one or more of the following:
</p>

<ul>
  <li>optional executable primitive families,</li>
  <li>optional interoperability surfaces,</li>
  <li>optional runtime-facing or deployment-facing capability contracts,</li>
  <li>optional environment assumptions,</li>
  <li>optional stricter validation rules for that capability family,</li>
  <li>optional support requirements for implementations that choose to claim that profile.</li>
</ul>

<p>
Examples of areas that MAY be appropriate for profiles include:
</p>

<ul>
  <li>interop with external runtimes or managed platforms,</li>
  <li>runtime-oriented capability families,</li>
  <li>deployment-oriented capability contracts,</li>
  <li>hardware-facing capability families,</li>
  <li>other standardized optional families that are not intrinsic to the minimal core language.</li>
</ul>

<p>
The presence of a profile in the repository does not imply that every conforming FROG implementation
must support that profile.
</p>

<hr/>

<h2 id="what-profiles-must-not-define">6. What Profiles MUST NOT Define</h2>

<p>
Profiles MUST NOT redefine the core ownership boundaries of the repository.
</p>

<p>
In particular, a profile specification MUST NOT:
</p>

<ul>
  <li>redefine the canonical <code>.frog</code> source file structure owned by <code>Expression/</code>,</li>
  <li>replace, weaken, or contradict execution semantics owned by <code>Language/</code>,</li>
  <li>reclassify profile-local behavior as unconditional language-core behavior,</li>
  <li>turn <code>Libraries/</code> into a catch-all bucket for ecosystem-specific capability growth,</li>
  <li>treat one vendor, runtime, operating system, database engine, or framework as the mandatory baseline for FROG itself,</li>
  <li>use optional capability support as a hidden requirement for core language conformance.</li>
</ul>

<p>
A profile MAY add optional capability contracts.
A profile MUST NOT mutate the meaning of the FROG core.
</p>

<hr/>

<h2 id="relation-with-other-specifications">7. Relation with Other Specifications</h2>

<p>
Profile specifications are used together with the rest of the FROG specification.
</p>

<ul>
  <li><code>Expression/Diagram.md</code> defines how profile-owned primitives appear as executable diagram nodes.</li>
  <li><code>Expression/Type.md</code> defines the ordinary type-system baseline unless a profile explicitly introduces additional profile-local rules that remain compatible with the core model.</li>
  <li><code>Language/</code> defines cross-cutting execution semantics that remain authoritative across both core and profile-owned capabilities.</li>
  <li><code>Libraries/</code> remains the home of intrinsic standard primitive vocabularies and MUST remain distinct from optional profile families.</li>
  <li><code>IDE/</code> MAY surface supported profiles in palette organization, authoring assistance, validation feedback, and observability tooling, but IDE presentation does not replace normative profile specifications.</li>
  <li><code>GOVERNANCE.md</code> defines governance-facing distinctions such as core support, profile support, conformance, certification, and branding policy.</li>
</ul>

<p>
Profile documents complement the rest of the specification.
They do not replace repository ownership boundaries established elsewhere.
</p>

<hr/>

<h2 id="current-profile-specifications">8. Current Profile Specifications</h2>

<p>
This directory currently contains the following documents:
</p>

<ul>
  <li><code>Readme.md</code> — overview of the Profiles layer and its architectural role.</li>
  <li><code>Interop.md</code> — the Interop profile, defining the first standardized optional interoperability capability family for <code>frog.connectivity.*</code>.</li>
</ul>

<p>
Additional profile specifications MAY be added as sibling documents when their scope is sufficiently
clear, architecturally justified, and bounded well enough to remain distinct from both the language
core and implementation-specific extensions.
</p>

<hr/>

<h2 id="profile-identification-and-claims">9. Profile Identification and Claims</h2>

<p>
Each profile specification SHOULD define a stable profile identity and a clear capability boundary.
</p>

<p>
When an implementation claims support for a profile, that claim SHOULD identify the profile explicitly
rather than implying that all optional capability families in the repository are universally supported.
</p>

<p>
Examples of acceptable claim styles include:
</p>

<ul>
  <li><code>core FROG support only</code></li>
  <li><code>core FROG + Interop profile</code></li>
  <li><code>core FROG + Interop profile + additional vendor extensions</code></li>
</ul>

<p>
Such claims are architectural capability claims.
They do not automatically imply official certification, endorsement, or trademark permission.
</p>

<hr/>

<h2 id="core-conformance-profile-support-and-certification">10. Core Conformance, Profile Support, and Certification</h2>

<p>
Core language conformance, profile support, and certification-related claims are related but distinct.
</p>

<ul>
  <li>A core-conforming implementation MUST satisfy the core language specification.</li>
  <li>A core-conforming implementation MAY support zero, one, or multiple optional profiles.</li>
  <li>An implementation claiming support for a profile MUST satisfy the normative requirements of that profile.</li>
  <li>Lack of support for a profile MUST NOT, by itself, be treated as failure of core language conformance.</li>
  <li>Support for one profile MUST NOT, by itself, be interpreted as support for all profiles.</li>
  <li>Claims such as <code>official</code>, <code>certified</code>, or trademark-bearing compatibility claims are governed separately from simple architectural support claims.</li>
</ul>

<p>
This distinction is essential for long-term modularity, portability, ecosystem growth, and future
conformance or certification policies.
</p>

<hr/>

<h2 id="profile-evolution">11. Profile Evolution</h2>

<p>
Profiles SHOULD be introduced conservatively.
</p>

<p>
A new profile is justified when all of the following are true:
</p>

<ul>
  <li>the capability area is broader than one implementation-specific extension,</li>
  <li>the capability area should not be mandatory for the language core,</li>
  <li>standardization improves interoperability, portability of meaning, or conformance clarity,</li>
  <li>the added material can be specified without destabilizing the core architecture,</li>
  <li>the capability family is bounded enough to avoid becoming a generic optional-feature dump.</li>
</ul>

<p>
Profiles SHOULD remain well-scoped.
When a capability family grows too large, it MAY later be split into multiple sibling profile specifications.
</p>

<hr/>

<h2 id="status">12. Status</h2>

<p>
This directory defines an architectural layer intended to keep the FROG specification modular,
portable, and durable as the ecosystem grows.
</p>

<p>
At the current repository stage, the Profiles layer is no longer only a placeholder category.
It already contains a first concrete profile specification and establishes the normative home for
optional standardized capability families that do not belong to the intrinsic library core.
</p>

<p>
The long-term objective is to maintain a clean distinction between:
</p>

<ul>
  <li>the FROG core language,</li>
  <li>intrinsic standard libraries,</li>
  <li>optional standardized capability profiles,</li>
  <li>implementation-specific extensions,</li>
  <li>future conformance, certification, and ecosystem participation models.</li>
</ul>
