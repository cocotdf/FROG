<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Profiles</h1>

<p align="center">
  <strong>Optional standardized capability families for FROG</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#purpose-of-profiles">2. Purpose of Profiles</a></li>
  <li><a href="#architectural-role">3. Architectural Role</a></li>
  <li><a href="#scope-of-this-directory">4. Scope of this Directory</a></li>
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
This directory defines optional standardized capability families for FROG.
</p>

<p>
A profile is a standardized specification layer that extends the usable capability surface of FROG without redefining the canonical source structure of the language core, without replacing the cross-cutting execution semantics owned by the core language architecture, and without turning one implementation strategy into mandatory language law.
</p>

<p>
Profiles exist to standardize capability areas that matter for real ecosystems but that should not be treated as intrinsic, always-present, mandatory parts of the minimal FROG core.
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
A profile therefore extends the standardized capability surface of FROG, but it does so from outside the intrinsic core.
</p>

<hr/>

<h2 id="purpose-of-profiles">2. Purpose of Profiles</h2>

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
This separation keeps the FROG core small, stable, portable, and durable while still allowing the standard to define broader capability surfaces where justified.
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
Profiles occupy a distinct architectural role between the minimal core standard and purely implementation-specific extensions.
</p>

<p>
They are intended to standardize capability families that are broader than one vendor-specific extension but narrower than the mandatory language core.
</p>

<pre><code>FROG specification architecture
Expression/        -&gt; canonical source form
Language/          -&gt; normative validated-program meaning
Libraries/         -&gt; intrinsic standardized primitive vocabularies
IR/                -&gt; canonical derived execution representation and backend-facing boundaries
Profiles/          -&gt; optional standardized capability families
IDE/               -&gt; authoring and observability tooling
Implementations/   -&gt; non-normative executable realizations</code></pre>

<p>
This model preserves a stable architectural center while allowing the ecosystem to grow through bounded optional capability families.
</p>

<p>
Profiles are therefore part of the published FROG specification architecture, but they are not part of the minimal intrinsic core.
</p>

<hr/>

<h2 id="scope-of-this-directory">4. Scope of this Directory</h2>

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
This means that a profile may add an optional capability layer, but it MUST do so without collapsing the ownership boundaries of <code>Expression/</code>, <code>Language/</code>, <code>Libraries/</code>, <code>IR/</code>, or <code>IDE/</code>.
</p>

<hr/>

<h2 id="capability-taxonomy">5. Capability Taxonomy</h2>

<p>
To keep the architecture explicit, FROG distinguishes several different concepts that are related but must not be conflated.
</p>

<h3>5.1 Optional capability profiles</h3>

<p>
An optional capability profile is the top-level object standardized in this directory.
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
A profile MAY define one or more of those related capability classes or constraints when that is part of its bounded scope.
</p>

<h3>5.2 Target profiles</h3>

<p>
A target profile is a standardized class of execution assumptions, constraints, and capabilities that a program, implementation, backend path, or deployment may explicitly target.
</p>

<p>
A target profile is not a single machine model, not a private runtime module, and not a backend implementation by itself.
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
A deployment mode is a standardized class of packaging, observability, distribution, or execution-environment assumptions applied when preparing an executable artifact.
</p>

<p>
A deployment mode may constrain how a compiled or prepared program is delivered or executed.
It is not the same thing as:
</p>

<ul>
  <li>language semantics,</li>
  <li>core IR structure,</li>
  <li>backend family identity.</li>
</ul>

<h3>5.4 Backend families</h3>

<p>
A backend family is a class of downstream execution consumers or compiler consumers.
Backend families remain downstream from the canonical FROG Execution IR.
</p>

<p>
Examples of backend-family postures that MAY exist include:
</p>

<ul>
  <li>native-code-oriented families,</li>
  <li>LLVM-oriented native families,</li>
  <li>VM-oriented families,</li>
  <li>interpreter-oriented families,</li>
  <li>accelerator-oriented families.</li>
</ul>

<p>
A backend family is not a profile by itself, although a profile MAY define compatibility with one or more backend families.
</p>

<h3>5.5 Runtime-facing capability contracts</h3>

<p>
A runtime-facing capability contract is a standardized statement about assumptions, services, or guarantees expected at a runtime boundary.
</p>

<p>
It is not identical to:
</p>

<ul>
  <li>canonical open IR,</li>
  <li>backend contract ownership in <code>IR/</code>,</li>
  <li>private runtime realization.</li>
</ul>

<p>
A profile MAY define runtime-facing capability expectations where justified, but those expectations MUST remain subordinate to the repository-wide separation between open IR, lowering, backend handoff, and private realization.
</p>

<hr/>

<h2 id="profile-vs-runtime-boundary">6. Profile vs Runtime Boundary</h2>

<p>
A profile may constrain or classify runtime-facing expectations, but it does not own one runtime implementation and does not replace the architectural runtime boundary.
</p>

<p>
This distinction matters especially for advanced capability surfaces.
</p>

<pre><code>profile
   may define
capability assumptions

profile
   does not define
one private runtime realization</code></pre>

<p>
Likewise:
</p>

<pre><code>profile
   may define
target-facing or deployment-facing classes

profile
   does not redefine
canonical open IR
or
backend contract ownership</code></pre>

<p>
Profiles therefore remain optional specification layers, not hidden runtime specifications.
</p>

<hr/>

<h2 id="what-profiles-may-define">7. What Profiles MAY Define</h2>

<p>
A profile MAY define any bounded optional capability family that remains architecturally subordinate to the rest of the repository.
</p>

<p>
Examples include:
</p>

<ul>
  <li>interoperability surfaces,</li>
  <li>restricted target classes,</li>
  <li>native compilation corridors,</li>
  <li>deployment classes,</li>
  <li>runtime-service capability surfaces,</li>
  <li>specialized validation restrictions for an optional capability family,</li>
  <li>bounded profile-specific execution assumptions.</li>
</ul>

<p>
A profile MAY therefore state:
</p>

<ul>
  <li>what optional capability claim exists,</li>
  <li>what assumptions that claim requires,</li>
  <li>what subset or bounded capability class it applies to,</li>
  <li>what explicit rejection conditions apply when those assumptions are not met.</li>
</ul>

<hr/>

<h2 id="what-profiles-must-not-define">8. What Profiles MUST NOT Define</h2>

<p>
A profile MUST NOT:
</p>

<ul>
  <li>redefine canonical source structure,</li>
  <li>redefine core validated-program meaning,</li>
  <li>move intrinsic language truth out of the core architecture,</li>
  <li>replace the ownership of <code>Libraries/</code> for intrinsic primitives,</li>
  <li>replace the ownership of <code>IR/</code> for canonical execution representation, derivation, lowering, or backend contract,</li>
  <li>turn one implementation strategy into mandatory language law,</li>
  <li>present one private runtime design as though it were the only conforming meaning of the capability family,</li>
  <li>collapse backend family, target profile, deployment mode, and runtime realization into one ambiguous concept.</li>
</ul>

<p>
Profiles are optional architectural extensions.
They are not ownership shortcuts.
</p>

<hr/>

<h2 id="relation-with-other-specification-layers">9. Relation with Other Specification Layers</h2>

<p>
Profiles must remain readable relative to the rest of the repository.
</p>

<p>
The intended reading model is:
</p>

<pre><code>Expression/
   defines canonical source structure

Language/
   defines validated meaning

Libraries/
   define intrinsic primitives

IR/
   defines canonical execution-facing representation,
   derivation,
   construction,
   schema posture,
   lowering,
   backend contract

Profiles/
   define optional standardized capability families
   that remain subordinate to all of the above

IDE/
   defines authoring and observability concerns

Implementations/
   provide non-normative executable workspaces</code></pre>

<p>
A profile may depend on these layers.
It must not absorb them.
</p>

<hr/>

<h2 id="profile-identification-and-claims">10. Profile Identification and Claims</h2>

<p>
Profiles are intended to be claimable.
</p>

<p>
An implementation MAY state that it supports:
</p>

<ul>
  <li>the core language only,</li>
  <li>the core language plus one or more published profiles,</li>
  <li>different subsets or maturity levels of profile support, provided those claims are explicit and not misleading.</li>
</ul>

<p>
A program, toolchain, or deployment path MAY also declare that it targets a given profile when that is meaningful and explicitly defined by the relevant profile specification.
</p>

<p>
A profile claim MUST remain precise.
For example:
</p>

<ul>
  <li><code>interop</code> means support for the published interoperability profile, not generic foreign-function support of unknown scope,</li>
  <li><code>native_cpu_llvm</code> means support for the published optional native CPU LLVM-oriented compilation profile, not a claim that LLVM defines FROG or that every valid FROG program is automatically compatible with that corridor.</li>
</ul>

<p>
Vague claims such as “supports all advanced features” are not profile claims.
Explicit profile naming is preferred.
</p>

<hr/>

<h2 id="current-profile-specifications">11. Current Profile Specifications</h2>

<p>
The currently published profile specifications are:
</p>

<ul>
  <li><code>Interop.md</code> — optional interoperability capability profile,</li>
  <li><code>Native CPU LLVM.md</code> — optional native CPU compilation profile for LLVM-oriented backend families.</li>
</ul>

<h3>11.1 Interop</h3>

<p>
<code>Interop.md</code> is the normative home for the optional interoperability capability surface, including the standardized home for capability families that should not remain in the intrinsic core library layer.
</p>

<h3>11.2 Native CPU LLVM</h3>

<p>
<code>Native CPU LLVM.md</code> defines a first optional compilation-oriented profile for a conservative v0.1 subset capable of traveling through:
</p>

<pre><code>validated meaning
   -&gt;
canonical FROG Execution IR
   -&gt;
lowering
   -&gt;
backend contract
   -&gt;
LLVM-oriented native CPU backend family</code></pre>

<p>
This profile exists to close one serious industrial compilation corridor without collapsing the language into LLVM and without redefining IR ownership inside <code>Profiles/</code>.
</p>

<p>
It should be read as:
</p>

<ul>
  <li>a bounded optional capability claim,</li>
  <li>a target-facing native compilation profile,</li>
  <li>a backend-family-oriented downstream compatibility claim,</li>
  <li>not a replacement for the core language or core IR stack.</li>
</ul>

<hr/>

<h2 id="core-conformance-profile-support-and-certification">12. Core Conformance, Profile Support, and Certification</h2>

<p>
Core conformance and profile support are related but not identical.
</p>

<p>
An implementation may:
</p>

<ul>
  <li>conform to the core language and support no optional profiles,</li>
  <li>conform to the core language and support one optional profile,</li>
  <li>conform to the core language and support multiple optional profiles.</li>
</ul>

<p>
Profile support therefore extends the supported capability surface.
It does not replace core conformance.
</p>

<p>
Likewise:
</p>

<pre><code>core conformance
   != profile support breadth

profile support breadth
   != certification breadth</code></pre>

<p>
Certification, if defined more explicitly later, remains a separate question from the existence of profiles themselves.
</p>

<hr/>

<h2 id="profile-evolution">13. Profile Evolution</h2>

<p>
Profiles should evolve conservatively.
</p>

<p>
A good profile evolution pattern is:
</p>

<ul>
  <li>identify a bounded optional capability family,</li>
  <li>define its assumptions clearly,</li>
  <li>define what it adds without redefining the core,</li>
  <li>define what it does not promise,</li>
  <li>keep its relation with other layers explicit,</li>
  <li>add conformance material when the profile becomes mature enough for public accept / reject expectations.</li>
</ul>

<p>
Profiles should not become a catch-all zone for unresolved architectural ideas.
</p>

<p>
In particular, future profile growth SHOULD prefer:
</p>

<ul>
  <li>small coherent capability families,</li>
  <li>clear target-facing or deployment-facing classes,</li>
  <li>explicit rejection conditions,</li>
  <li>clean separation from backend-private and runtime-private realization.</li>
</ul>

<hr/>

<h2 id="status">14. Status</h2>

<p>
In the current published repository posture:
</p>

<ul>
  <li><code>Profiles/</code> is already a normative specification layer,</li>
  <li>the directory already distinguishes optional profiles from core intrinsic language ownership,</li>
  <li>the directory now publishes both an interoperability profile and a first native compilation profile,</li>
  <li>the broader profile surface remains intentionally limited and conservative.</li>
</ul>

<p>
That is the intended status for v0.1:
</p>

<ul>
  <li>a stable architectural home exists,</li>
  <li>a small number of bounded optional capability families are published,</li>
  <li>the repository remains free to grow later without collapsing the core architecture.</li>
</ul>

<hr/>

<h2 id="summary">15. Summary</h2>

<p>
This directory defines optional standardized capability families for FROG.
</p>

<p>
A profile:
</p>

<ul>
  <li>extends the standardized capability surface,</li>
  <li>remains optional rather than intrinsic,</li>
  <li>stays subordinate to the core repository architecture,</li>
  <li>may define bounded target-facing, deployment-facing, interoperability, runtime-facing, or compilation-oriented capability classes,</li>
  <li>must not redefine the language core, canonical IR ownership, or private runtime truth.</li>
</ul>

<p>
The current published profile set includes:
</p>

<ul>
  <li><code>Interop.md</code> for interoperability capability,</li>
  <li><code>Native CPU LLVM.md</code> for a first native CPU LLVM-oriented compilation corridor.</li>
</ul>

<p>
This keeps the architecture explicit:
</p>

<pre><code>core language stays core

IR stays IR

profiles stay optional

backend families stay downstream

private realization stays private</code></pre>

<p>
That is the intended role of <code>Profiles/</code> in FROG v0.1.
</p>
