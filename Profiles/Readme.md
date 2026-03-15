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
  <li><a href="#scope">3. Scope of this Directory</a></li>
  <li><a href="#role">4. Role of Profiles in FROG Architecture</a></li>
  <li><a href="#what-profiles-may-define">5. What Profiles MAY Define</a></li>
  <li><a href="#what-profiles-must-not-define">6. What Profiles MUST NOT Define</a></li>
  <li><a href="#relation-with-other-specifications">7. Relation with Other Specifications</a></li>
  <li><a href="#current-documents">8. Current Documents</a></li>
  <li><a href="#profile-identification-and-claims">9. Profile Identification and Claims</a></li>
  <li><a href="#core-conformance-vs-profile-support">10. Core Conformance vs Profile Support</a></li>
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
core execution semantics owned by the language itself.
</p>

<p>
Profiles exist to standardize capability areas that are important for practical ecosystems but that
should not be treated as intrinsic, always-present, core language libraries.
</p>

<p>
Accordingly:
</p>

<ul>
  <li><code>Expression/</code> owns canonical source representation.</li>
  <li><code>Language/</code> owns cross-cutting execution semantics.</li>
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
  <li>sometimes dependent on external runtimes, host environments, protocols, services, or ecosystems.</li>
</ul>

<p>
This separation keeps the FROG core small, stable, portable, and durable while still allowing the
standard to define broader capability surfaces where justified.
</p>

<hr/>

<h2 id="scope">3. Scope of this Directory</h2>

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
  <li>profile-local constraints on execution environments or target support,</li>
  <li>profile-specific terminology and behavior that remains outside the minimal core language surface.</li>
</ul>

<p>
A profile specification MUST remain subordinate to the core language architecture.
</p>

<hr/>

<h2 id="role">4. Role of Profiles in FROG Architecture</h2>

<p>
Profiles occupy a distinct architectural role between the minimal core standard and concrete
implementation-specific extensions.
</p>

<p>
They are intended to standardize capability families that are broader than one vendor implementation
but narrower than the mandatory language core.
</p>

<pre>FROG standard architecture

Expression/   -> canonical source form
Language/     -> normative execution semantics
Libraries/    -> intrinsic standard primitive vocabularies
Profiles/     -> optional standardized capability families
IDE/          -> authoring, observability, debugging, inspection

Implementations MAY support:
- core only
- core + one or more profiles
- core + profiles + additional proprietary or open extensions
</pre>

<p>
This model allows the standard to remain modular while preserving a stable center.
</p>

<hr/>

<h2 id="what-profiles-may-define">5. What Profiles MAY Define</h2>

<p>
A profile specification MAY define one or more of the following:
</p>

<ul>
  <li>optional executable primitive families,</li>
  <li>optional interoperability surfaces,</li>
  <li>optional target-facing capability contracts,</li>
  <li>optional environment assumptions,</li>
  <li>optional stricter validation rules for that capability family,</li>
  <li>optional additional observability or inspection objects in stricter execution environments.</li>
</ul>

<p>
Examples of areas that may be appropriate for profiles include:
</p>

<ul>
  <li>interop with external runtimes or managed platforms,</li>
  <li>deployment-facing capability contracts,</li>
  <li>runtime-oriented execution profiles,</li>
  <li>hardware-facing capability families,</li>
  <li>domain-specific standardized capability sets.</li>
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
  <li>replace or contradict core execution semantics owned by <code>Language/</code>,</li>
  <li>reclassify profile-local behavior as unconditional language-core behavior,</li>
  <li>turn <code>Libraries/</code> into a catch-all bucket for ecosystem-specific capability growth,</li>
  <li>treat one vendor, runtime, operating system, database engine, or framework as the mandatory baseline for FROG itself.</li>
</ul>

<p>
A profile MAY add optional capability contracts.
A profile MUST NOT mutate the meaning of the language core.
</p>

<hr/>

<h2 id="relation-with-other-specifications">7. Relation with Other Specifications</h2>

<p>
Profile specifications are used together with the rest of the FROG specification.
</p>

<ul>
  <li><code>Expression/Diagram.md</code> defines how profile-owned primitives appear as executable diagram nodes.</li>
  <li><code>Expression/Type.md</code> defines the ordinary type system baseline used unless a profile explicitly introduces additional profile-local rules compatible with the core type model.</li>
  <li><code>Language/</code> defines cross-cutting execution semantics that remain authoritative across both core and profile-owned capabilities.</li>
  <li><code>Libraries/</code> remains the home of intrinsic standard primitive vocabularies and MUST remain distinct from optional profile families.</li>
  <li><code>IDE/</code> MAY surface supported profiles in palette organization, authoring assistance, validation feedback, and observability tooling, but IDE presentation does not replace normative profile specifications.</li>
</ul>

<hr/>

<h2 id="current-documents">8. Current Documents</h2>

<p>
This directory currently contains the following documents:
</p>

<ul>
  <li><code>Readme.md</code> — overview of the Profiles layer and its architectural role.</li>
</ul>

<p>
Additional profile specifications MAY be added as sibling documents when their scope is sufficiently
clear and architecturally justified.
</p>

<p>
A first expected example is an interoperability-oriented profile that standardizes optional capability
surfaces for interaction with external runtimes or services without treating those capabilities as
part of the minimal intrinsic library core.
</p>

<hr/>

<h2 id="profile-identification-and-claims">9. Profile Identification and Claims</h2>

<p>
Each profile specification SHOULD define a stable profile identity and a clear capability boundary.
</p>

<p>
When an implementation claims support for a profile, that claim SHOULD identify the profile explicitly
rather than implying that all optional repository capability families are universally supported.
</p>

<p>
Examples of acceptable future claim styles include:
</p>

<ul>
  <li><code>core FROG support only</code></li>
  <li><code>core FROG + Interop profile</code></li>
  <li><code>core FROG + Interop profile + deployment profile</code></li>
</ul>

<p>
Such claims are architectural capability claims.
They do not automatically imply official certification, endorsement, or trademark permission.
</p>

<hr/>

<h2 id="core-conformance-vs-profile-support">10. Core Conformance vs Profile Support</h2>

<p>
Core FROG conformance and profile support are related but distinct.
</p>

<ul>
  <li>A core-conforming implementation MUST satisfy the core language specification.</li>
  <li>A core-conforming implementation MAY support zero, one, or multiple optional profiles.</li>
  <li>An implementation claiming support for a profile MUST satisfy the normative requirements of that profile.</li>
  <li>The absence of support for a profile MUST NOT by itself be treated as failure of core language conformance.</li>
</ul>

<p>
This distinction is essential for long-term modularity, portability, and multi-implementation ecosystem growth.
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
  <li>the added material can be specified without destabilizing the core architecture.</li>
</ul>

<p>
Profiles SHOULD remain well-bounded.
A profile SHOULD NOT become a generic dumping ground for unrelated optional features.
</p>

<p>
When a capability area grows large enough, it MAY later be split into multiple sibling profile specifications.
</p>

<hr/>

<h2 id="status">12. Status</h2>

<p>
This directory defines an architectural layer that is intended to keep the FROG specification modular,
portable, and durable as the ecosystem grows.
</p>

<p>
At the current stage, the Profiles layer is being established to prevent optional capability families
from being conflated with the minimal intrinsic standard library surface.
</p>

<p>
The long-term objective is to support a clean distinction between:
</p>

<ul>
  <li>the FROG core language,</li>
  <li>optional standardized capability profiles,</li>
  <li>implementation-specific extensions,</li>
  <li>future conformance, certification, and ecosystem participation models.</li>
</ul>
