<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG Profiles</h1>

<p align="center">
  Optional standardized capability families for <strong>FROG</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#purpose">2. Purpose of Profiles</a></li>
  <li><a href="#architectural-role">3. Architectural Role</a></li>
  <li><a href="#scope">4. Scope of this Directory</a></li>
  <li><a href="#capability-taxonomy">5. Capability Taxonomy</a></li>
  <li><a href="#profile-vs-runtime-boundary">6. Profile vs Runtime Boundary</a></li>
  <li><a href="#what-profiles-may-define">7. What Profiles MAY Define</a></li>
  <li><a href="#what-profiles-must-not-define">8. What Profiles MUST NOT Define</a></li>
  <li><a href="#relation-with-other-specification-layers">9. Relation with Other Specification Layers</a></li>
  <li><a href="#profile-identification-and-claims">10. Profile Identification and Claims</a></li>
  <li><a href="#current-profile-specifications">11. Current Profile Specifications</a></li>
  <li><a href="#core-conformance-profile-support-and-certification">12. Core Conformance, Profile Support, and Certification</a></li>
  <li><a href="#profile-evolution">13. Profile Evolution</a></li>
  <li><a href="#status">14. Status</a></li>
  <li><a href="#summary">15. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines <strong>optional standardized capability families</strong> for FROG.
</p>

<p>
A profile is a standardized specification layer that extends the usable capability surface of FROG
without redefining the canonical source structure of the language core, without replacing the
cross-cutting execution semantics owned by the core language architecture, and without turning one
implementation strategy into mandatory language law.
</p>

<p>
Profiles exist to standardize capability areas that matter for real ecosystems but that should not
be treated as intrinsic, always-present, mandatory parts of the minimal FROG core.
</p>

<p>
Within the current repository architecture:
</p>

<ul>
  <li><code>Expression/</code> owns canonical source representation,</li>
  <li><code>Language/</code> owns normative validated-program meaning and cross-cutting execution semantics,</li>
  <li><code>Libraries/</code> owns intrinsic standardized primitive vocabularies,</li>
  <li><code>IR/</code> owns canonical execution-facing representation, derivation, construction, lowering, and backend contracts,</li>
  <li><code>Profiles/</code> owns optional standardized capability families,</li>
  <li><code>IDE/</code> owns authoring, observability, debugging, inspection, and related tooling responsibilities,</li>
  <li><code>Implementations/</code> owns non-normative executable realization workspaces.</li>
</ul>

<p>
A profile therefore extends the <strong>standardized capability surface</strong> of FROG, but it does so
from outside the intrinsic core.
</p>

<hr/>

<h2 id="purpose">2. Purpose of Profiles</h2>

<p>
The purpose of this directory is to provide a clean architectural home for specification material that is:
</p>

<ul>
  <li>standardized,</li>
  <li>useful across multiple implementations,</li>
  <li>optional rather than mandatory for the minimal language core,</li>
  <li>sometimes dependent on broader execution assumptions, deployment assumptions, host environments, interoperability contracts, capability classes, or target-facing restrictions.</li>
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
  <li>a second hidden core-language layer,</li>
  <li>a dumping ground for implementation-specific features,</li>
  <li>a place where runtime-private realization becomes normative language truth,</li>
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

<pre><code>FROG specification architecture

Expression/        -> canonical source form
Language/          -> normative validated-program meaning
Libraries/         -> intrinsic standardized primitive vocabularies
IR/                -> canonical derived execution representation and backend-facing boundaries
Profiles/          -> optional standardized capability families
IDE/               -> authoring and observability tooling
Implementations/   -> non-normative executable realizations
</code></pre>

<p>
This model preserves a stable architectural center while allowing the ecosystem to grow through
bounded optional capability families.
</p>

<p>
Profiles are therefore part of the published FROG specification architecture, but they are
<strong>not</strong> part of the minimal intrinsic core.
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
  <li>profile-local capability assumptions,</li>
  <li>profile-local validation rules,</li>
  <li>profile-local execution constraints that remain subordinate to the core language meaning,</li>
  <li>target-facing capability classes,</li>
  <li>deployment-facing capability classes,</li>
  <li>runtime-facing capability contracts,</li>
  <li>profile-specific terminology and behavior that remain outside the minimal intrinsic language surface,</li>
  <li>optional capability claims that implementations MAY support explicitly.</li>
</ul>

<p>
A profile specification MUST remain subordinate to the core repository architecture.
</p>

<p>
This means that a profile may add an optional capability layer, but it MUST do so without collapsing
the ownership boundaries of <code>Expression/</code>, <code>Language/</code>, <code>Libraries/</code>,
<code>IR/</code>, or <code>IDE/</code>.
</p>

<hr/>

<h2 id="capability-taxonomy">5. Capability Taxonomy</h2>

<p>
To keep the architecture explicit, FROG distinguishes several different concepts that are related but
must not be conflated.
</p>

<h3>5.1 Optional capability profiles</h3>

<p>
An <strong>optional capability profile</strong> is the top-level object standardized in this directory.
It defines one bounded optional capability family that implementations may claim explicitly.
</p>

<p>
A profile is not automatically:
</p>

<ul>
  <li>a target profile,</li>
  <li>a deployment mode,</li>
  <li>a backend family,</li>
  <li>a runtime module.</li>
</ul>

<p>
A profile MAY define one or more of those related capability classes or constraints when that is part
of its bounded scope.
</p>

<h3>5.2 Target profiles</h3>

<p>
A <strong>target profile</strong> is a standardized class of execution assumptions, constraints, and
capabilities that a program, implementation, backend path, or deployment may explicitly target.
</p>

<p>
A target profile is not a single machine model, not a private runtime module, and not a backend
implementation by itself.
It is a standardized capability class.
</p>

<p>
Examples of target-profile families that MAY later be specified include:
</p>

<ul>
  <li><code>desktop_ui</code>,</li>
  <li><code>desktop_headless</code>,</li>
  <li><code>embedded</code>,</li>
  <li><code>real_time</code>,</li>
  <li><code>accelerated</code>,</li>
  <li><code>microcontroller</code>.</li>
</ul>

<h3>5.3 Deployment modes</h3>

<p>
A <strong>deployment mode</strong> is a standardized class of packaging, observability, distribution,
or execution-environment assumptions applied when preparing an executable artifact.
</p>

<p>
A deployment mode is not itself the language meaning of the program and is not itself a backend
family.
It characterizes how execution is packaged or exposed.
</p>

<p>
Examples of deployment-mode families that MAY later be specified include:
</p>

<ul>
  <li><code>dev</code>,</li>
  <li><code>debug</code>,</li>
  <li><code>release</code>,</li>
  <li><code>self_contained</code>,</li>
  <li><code>runtime_shared</code>,</li>
  <li><code>restricted</code>.</li>
</ul>

<h3>5.4 Runtime-facing capability contracts</h3>

<p>
A profile MAY define <strong>runtime-facing capability contracts</strong>.
These describe what classes of runtime service availability, execution support, platform support,
or host-service availability are assumed or required for that profile.
</p>

<p>
Such contracts do <strong>not</strong> standardize one universal runtime implementation.
They standardize capability expectations, not one mandatory runtime-private realization.
</p>

<h3>5.5 Backend families</h3>

<p>
A <strong>backend family</strong> is a downstream execution-consumption family reached after
validated FROG meaning and canonical FROG Execution IR have already been established.
</p>

<p>
Backend families are primarily a <strong>backend-contract-facing</strong> and
<strong>realization-facing</strong> classification.
They are not owned by <code>Profiles/</code> as such, even when a profile constrains which backend
families are viable.
</p>

<h3>5.6 Runtime modules</h3>

<p>
A <strong>runtime module</strong> is an implementation-side executable service bundle such as UI
support, observability support, interoperability support, or constrained-target support.
</p>

<p>
Runtime modules are generally an <strong>implementation realization concern</strong>, not a normative
profile identity.
Profiles may define runtime-facing capability contracts, but they do not by themselves standardize one
mandatory monolithic runtime.
</p>

<p>
This distinction is essential.
FROG profiles may define optional capability classes that influence runtime needs, but they MUST NOT
cause one implementation runtime layout to become hidden language law.
</p>

<h3>5.7 Relationship summary</h3>

<pre><code>validated program meaning
    ->
canonical Execution IR
    ->
lowering
    ->
backend contract
    ->
backend family consumption
    ->
deployment bundle realization
    ->
runtime services available on target

Profiles/
    may constrain or classify some of these assumptions
    but do not replace IR/, backend contracts, or runtime realization
</code></pre>

<hr/>

<h2 id="profile-vs-runtime-boundary">6. Profile vs Runtime Boundary</h2>

<p>
Profiles are an important architectural preparation layer for future compiler/runtime work, but they
are not themselves the runtime layer.
</p>

<p>
A profile may say:
</p>

<ul>
  <li>what capability class is being targeted,</li>
  <li>what deployment-style assumptions apply,</li>
  <li>what runtime-facing services must be available in principle,</li>
  <li>what remains optional or implementation-defined.</li>
</ul>

<p>
A profile must <strong>not</strong> say:
</p>

<ul>
  <li>the exact internal runtime object model,</li>
  <li>the exact private scheduler design,</li>
  <li>the exact host framework,</li>
  <li>the exact GUI toolkit,</li>
  <li>the exact logging substrate,</li>
  <li>the exact process model,</li>
  <li>the exact packaging trick used by one implementation.</li>
</ul>

<p>
This distinction is especially important for UI-capable or interop-capable profiles.
A profile may standardize that a capability family assumes some class of UI service, host interop,
or environment support.
It must not standardize one private realization of that service as if it were the meaning of FROG.
</p>

<pre><code>Profiles/
    standardize capability classes and contracts

IR/
    standardizes canonical derived execution-facing representation,
    lowering boundaries, and backend-facing contracts

Implementations/
    realize those capabilities through private runtime layouts and executable service bundles
</code></pre>

<p>
In short:
</p>

<pre><code>profile
    != runtime implementation

profile
    != backend family

profile
    != deployment bundle

profile
    may constrain
    target / deployment / runtime-facing capability expectations
</code></pre>

<hr/>

<h2 id="what-profiles-may-define">7. What Profiles MAY Define</h2>

<p>
A profile specification MAY define one or more of the following:
</p>

<ul>
  <li>optional executable primitive families,</li>
  <li>optional interoperability surfaces,</li>
  <li>optional target-profile capability classes,</li>
  <li>optional deployment-facing capability classes,</li>
  <li>optional runtime-facing capability contracts,</li>
  <li>optional environment assumptions,</li>
  <li>optional stricter validation rules for that capability family,</li>
  <li>optional support requirements for implementations that choose to claim that profile.</li>
</ul>

<p>
Examples of areas that MAY be appropriate for profiles include:
</p>

<ul>
  <li>interop with external runtimes or managed platforms,</li>
  <li>deployment-oriented capability contracts,</li>
  <li>target-profile capability classes,</li>
  <li>hardware-facing capability families,</li>
  <li>runtime-facing capability classes that remain standardized at the contract level rather than the private implementation level,</li>
  <li>other optional capability families that are not intrinsic to the minimal core language.</li>
</ul>

<p>
The presence of a profile in the repository does not imply that every conforming FROG implementation
must support that profile.
</p>

<hr/>

<h2 id="what-profiles-must-not-define">8. What Profiles MUST NOT Define</h2>

<p>
Profiles MUST NOT redefine the core ownership boundaries of the repository.
</p>

<p>
In particular, a profile specification MUST NOT:
</p>

<ul>
  <li>redefine the canonical <code>.frog</code> source file structure owned by <code>Expression/</code>,</li>
  <li>replace, weaken, or contradict validated-program meaning owned by <code>Language/</code>,</li>
  <li>replace, weaken, or contradict canonical derivation responsibilities owned by <code>IR/</code>,</li>
  <li>reclassify profile-local behavior as unconditional language-core behavior,</li>
  <li>absorb intrinsic primitive vocabularies that belong in <code>Libraries/</code>,</li>
  <li>turn <code>Libraries/</code> into a catch-all bucket for ecosystem-specific capability growth,</li>
  <li>treat one vendor, runtime, operating system, database engine, host framework, or deployment model as the mandatory baseline for FROG itself,</li>
  <li>standardize one private runtime layout as though it were the language definition,</li>
  <li>collapse target profiles, deployment modes, backend families, backend-contract assumptions, and runtime modules into one undifferentiated concept,</li>
  <li>use optional capability support as a hidden requirement for core language conformance.</li>
</ul>

<p>
A profile MAY add optional capability contracts.
A profile MUST NOT mutate the meaning of the FROG core.
</p>

<hr/>

<h2 id="relation-with-other-specification-layers">9. Relation with Other Specification Layers</h2>

<p>
Profile specifications are used together with the rest of the FROG specification.
</p>

<ul>
  <li><code>Expression/</code> defines canonical source representation and remains authoritative for source structure.</li>
  <li><code>Language/</code> defines validated-program meaning and cross-cutting execution semantics that remain authoritative across both core and profile-owned capabilities.</li>
  <li><code>Libraries/</code> remains the home of intrinsic standardized primitive vocabularies and MUST remain distinct from optional profile families.</li>
  <li><code>IR/</code> defines the canonical derived execution-oriented representation, lowering boundaries, and backend contracts, and MUST remain distinct from both target-profile claims and runtime-private realization.</li>
  <li><code>IDE/</code> MAY surface supported profiles in palette organization, authoring assistance, validation feedback, deployment targeting, and observability tooling, but IDE presentation does not replace normative profile specifications.</li>
  <li><code>Implementations/</code> MAY realize profile support through one or more runtime modules, backend selections, deployment bundles, or private optimization strategies, but such realization choices do not by themselves define the profile normatively.</li>
  <li><code>GOVERNANCE.md</code> defines governance-facing distinctions such as core support, profile support, conformance, certification, and branding policy.</li>
</ul>

<p>
These relationships can be summarized as follows:
</p>

<pre><code>Expression/        -> source representation
Language/          -> validated-program meaning
Libraries/         -> intrinsic primitive vocabularies
IR/                -> canonical derived execution representation and backend-facing boundaries
Profiles/          -> optional standardized capability families
IDE/               -> tooling and deployment surface
Implementations/   -> executable realization
</code></pre>

<p>
Profile documents complement the rest of the specification.
They do not replace repository ownership boundaries established elsewhere.
</p>

<hr/>

<h2 id="profile-identification-and-claims">10. Profile Identification and Claims</h2>

<p>
Each profile specification SHOULD define a stable profile identity and a clear capability boundary.
</p>

<p>
When an implementation claims support for a profile, that claim SHOULD identify the profile explicitly
rather than implying that all optional capability families in the repository are universally supported.
</p>

<p>
Profiles that define target-profile classes, deployment-mode classes, or runtime-facing capability
contracts SHOULD also state clearly:
</p>

<ul>
  <li>what is being claimed,</li>
  <li>what remains optional,</li>
  <li>what execution assumptions are required,</li>
  <li>what is still implementation-defined.</li>
</ul>

<p>
Examples of acceptable claim styles include:
</p>

<ul>
  <li><code>core FROG support only</code></li>
  <li><code>core FROG + Interop profile</code></li>
  <li><code>core FROG + desktop_ui target-profile support</code></li>
  <li><code>core FROG + Interop profile + embedded target-profile support</code></li>
  <li><code>core FROG + Interop profile + additional vendor extensions</code></li>
</ul>

<p>
Such claims are architectural capability claims.
They do not automatically imply official certification, endorsement, or trademark permission.
</p>

<hr/>

<h2 id="current-profile-specifications">11. Current Profile Specifications</h2>

<p>
This directory currently contains the following documents:
</p>

<ul>
  <li><code>Readme.md</code> — overview of the Profiles layer and its architectural role.</li>
  <li><code>Interop.md</code> — the Interop profile, defining the first standardized optional interoperability capability family for <code>frog.connectivity.*</code>.</li>
</ul>

<p>
Accordingly, the authoritative normative home of <code>frog.connectivity.*</code> is:
</p>

<pre><code>Profiles/Interop.md</code></pre>

<p>
The presence of <code>Libraries/Connectivity.md</code> elsewhere in the repository does not create a second
normative home.
That file remains only as a transition and continuity note.
</p>

<p>
Additional profile specifications MAY be added as sibling documents when their scope is sufficiently
clear, architecturally justified, and bounded well enough to remain distinct from both the language
core and implementation-specific extensions.
</p>

<p>
The taxonomy introduced in this document does not itself mean that all of the following already exist
as standalone published profile specifications:
</p>

<ul>
  <li>target-profile specifications,</li>
  <li>deployment-mode specifications,</li>
  <li>runtime-facing capability-profile specifications.</li>
</ul>

<p>
It means that the architectural distinction is explicit and available for future profile work.
</p>

<hr/>

<h2 id="core-conformance-profile-support-and-certification">12. Core Conformance, Profile Support, and Certification</h2>

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

<h2 id="profile-evolution">13. Profile Evolution</h2>

<p>
Profiles SHOULD be introduced conservatively.
</p>

<p>
A new profile is justified when all of the following are true:
</p>

<ul>
  <li>the capability area is broader than one implementation-specific extension,</li>
  <li>the capability area should not be mandatory for the language core,</li>
  <li>standardization improves interoperability, portability of meaning, deployment clarity, or conformance clarity,</li>
  <li>the added material can be specified without destabilizing the core architecture,</li>
  <li>the capability family is bounded enough to avoid becoming a generic optional-feature dump.</li>
</ul>

<p>
Profiles SHOULD remain well-scoped.
When a capability family grows too large, it MAY later be split into multiple sibling profile specifications.
</p>

<p>
A capability area SHOULD NOT be placed in <code>Profiles/</code> merely because it is useful.
It belongs here only when optional standardization is architecturally justified.
</p>

<p>
Likewise, an implementation convenience SHOULD NOT be standardized as a profile merely because it is
widely reused.
If it is only a private runtime layout, packaging trick, private ABI choice, private scheduler shape,
or implementation bundling choice, it does not by itself justify a normative profile.
</p>

<hr/>

<h2 id="status">14. Status</h2>

<p>
This directory defines an architectural layer intended to keep the FROG specification modular,
portable, durable, and explicit as the ecosystem grows.
</p>

<p>
At the current repository stage, the Profiles layer is no longer only a placeholder category.
It already contains a first concrete profile specification and already serves as the normative home
for optional standardized capability families that do not belong to the intrinsic library core.
</p>

<p>
This document also makes explicit that FROG distinguishes:
</p>

<ul>
  <li>optional standardized profiles,</li>
  <li>target-profile capability classes,</li>
  <li>deployment-mode capability classes,</li>
  <li>runtime-facing capability contracts,</li>
  <li>backend families,</li>
  <li>implementation runtime modules.</li>
</ul>

<p>
This distinction is important for long-term compiler/runtime preparation.
A compiled FROG artifact does not imply one universal runtime shape.
Different target profiles and deployment modes may legitimately require different runtime-service
bundles, while still preserving the same validated meaning and the same architectural stage boundaries.
</p>

<p>
The long-term objective is to maintain a clean distinction between:
</p>

<ul>
  <li>the FROG core language,</li>
  <li>intrinsic standardized libraries,</li>
  <li>optional standardized capability profiles,</li>
  <li>canonical derived execution representation,</li>
  <li>backend-facing execution consumption paths,</li>
  <li>implementation-specific runtime realization,</li>
  <li>future conformance, certification, and ecosystem participation models.</li>
</ul>

<p>
In short:
</p>

<pre><code>Profiles/ should stay:
- optional
- standardized
- bounded
- explicitly claimed
- architecturally subordinate to the core
- distinct from backend-private realization
- distinct from runtime-private layout

Profiles/ should not become:
- a second core
- an extension dump
- a vendor bucket
- a hidden conformance trap
- a synonym for runtime implementation
- a synonym for backend family
</code></pre>

<hr/>

<h2 id="summary">15. Summary</h2>

<p>
<code>Profiles/</code> is the architectural home of optional standardized capability families in FROG.
</p>

<p>
It exists to make optional capability growth explicit without corrupting the ownership boundaries of:
</p>

<ul>
  <li><code>Expression/</code>,</li>
  <li><code>Language/</code>,</li>
  <li><code>Libraries/</code>,</li>
  <li><code>IR/</code>,</li>
  <li><code>IDE/</code>.</li>
</ul>

<p>
Profiles may standardize bounded optional capability classes.
They may constrain target, deployment, or runtime-facing expectations.
They may influence lowering viability and backend compatibility.
They do not redefine validated meaning, canonical IR, backend contracts, or private runtime realization.
</p>

<pre><code>core language
    stays core

intrinsic libraries
    stay intrinsic

profiles
    stay optional

IR
    stays the canonical execution-facing bridge

runtime realization
    stays implementation-private
</code></pre>
