<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">FROG Conformance</h1>

<p align="center">
  <strong>Public accept / reject / preserve truth surface for the published FROG specification</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#core-purpose">2. Core Purpose</a></li>
  <li><a href="#why-this-directory-exists">3. Why This Directory Exists</a></li>
  <li><a href="#definition-of-conformance">4. Definition of Conformance</a></li>
  <li><a href="#non-goals">5. Non-Goals</a></li>
  <li><a href="#relation-with-specification-ownership">6. Relation with Specification Ownership</a></li>
  <li><a href="#critical-boundaries">7. Critical Boundaries</a></li>
  <li><a href="#directory-structure">8. Directory Structure</a></li>
  <li><a href="#published-cases">9. Published Cases</a></li>
  <li><a href="#expected-outcomes">10. Expected Outcomes</a></li>
  <li><a href="#active-v01-conformance-focus">11. Active v0.1 Conformance Focus</a></li>
  <li><a href="#relation-with-examples-ir-profiles-and-reference-implementation">12. Relation with Examples, IR, Profiles, and Reference Implementation</a></li>
  <li><a href="#execution-ready-growth-posture">13. Execution-Ready Growth Posture</a></li>
  <li><a href="#future-growth">14. Future Growth</a></li>
  <li><a href="#summary">15. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the public conformance surface of the published FROG repository.
</p>

<p>
It publishes explicit cases that make the specification testable, reviewable, and comparable across independent implementations.
</p>

<p>
It answers three fundamental questions:
</p>

<pre>What must be accepted?
What must be rejected?
What must be preserved?</pre>

<p>
This directory does not define the language by itself. It makes already-published language law operationally checkable. Conformance therefore sits at the boundary between repository truth and observable implementation behavior. It turns architectural distinctions into public expectations.
</p>

<p>
In v0.1, that public truth surface is not limited to source acceptance or semantic rejection alone. It also includes preservation obligations across the published execution corridor:
</p>

<pre>.frog source
   -&gt;
loadability
   -&gt;
structural validity
   -&gt;
validated meaning
   -&gt;
canonical Execution IR document
   -&gt;
canonical JSON IR validation where applicable
   -&gt;
later lowering / backend-facing handoff where applicable
   -&gt;
declared backend-family consumption where applicable</pre>

<p>
Conformance therefore already matters to the compiler corridor, even when the downstream compilation route is still being consolidated. A future industrial compilation chain must remain compatible with the same public accept / reject / preserve truth surface.
</p>

<hr/>

<h2 id="core-purpose">2. Core Purpose</h2>

<p>
The purpose of conformance is to transform specification rules into checkable public expectations.
</p>

<p>
The repository-level model is:
</p>

<pre>Specification   = defines the rules
Conformance     = exposes testable cases
Implementation  = must behave accordingly</pre>

<p>
A conforming implementation MAY vary internally. It MUST NOT vary in published accept / reject / preserve outcomes for the same published case while still claiming conformance to the same published repository state.
</p>

<p>
Conformance therefore prevents the following drift:
</p>

<pre>parseable file
        -/-> structurally valid canonical source

structurally valid canonical source
        -/-> validated meaning

validated meaning
        -/-> arbitrary execution-facing form

implementation convenience
        -/-> language truth

"it runs"
        -/-> "it is correct"</pre>

<p>
Conformance is therefore not a commentary layer. It is the public truth surface that makes published repository law observable, comparable, and reviewable.
</p>

<hr/>

<h2 id="why-this-directory-exists">3. Why This Directory Exists</h2>

<p>
FROG is specification-first and implementation-independent.
</p>

<p>
That creates a requirement:
</p>

<pre>multiple independent implementations
            require
one shared public validation surface</pre>

<p>
This directory provides that surface.
</p>

<p>
It ensures that:
</p>

<ul>
  <li>implementations do not silently diverge,</li>
  <li>semantic meaning is not reinterpreted implicitly,</li>
  <li>invalid constructs are rejected instead of silently repaired,</li>
  <li>critical distinctions remain visible across loadability, structural validation, semantic validation, IR derivation, IR construction, canonical JSON validation, later lowering / backend-facing handoff, and declared backend-family consumption where applicable.</li>
</ul>

<p>
Conformance is therefore not commentary. It is the public truth surface that turns specification architecture into comparable observable behavior.
</p>

<hr/>

<h2 id="definition-of-conformance">4. Definition of Conformance</h2>

<p>
Conformance is alignment with the published specification across the relevant architectural stages.
</p>

<p>
It includes:
</p>

<ul>
  <li>correct rejection of malformed or non-loadable source where applicable,</li>
  <li>correct source-structure validation,</li>
  <li>correct semantic validation,</li>
  <li>correct rejection where validated meaning does not exist,</li>
  <li>correct preservation of distinctions across derivation into the canonical Execution IR document,</li>
  <li>correct canonical-IR construction and canonical JSON compatibility where the case reaches that stage,</li>
  <li>correct preservation of required boundaries across later lowering and backend-facing handoff where applicable,</li>
  <li>correct staged acceptance or rejection across declared compiler-corridor stages where applicable.</li>
</ul>

<p>
Conformance therefore requires both:
</p>

<pre>correct accept / reject decisions
and
correct preservation of required distinctions</pre>

<p>
A conforming implementation is not merely an implementation that “does something plausible”. It is an implementation that behaves compatibly with the published public truth surface.
</p>

<hr/>

<h2 id="non-goals">5. Non-Goals</h2>

<p>
This directory is not:
</p>

<ul>
  <li>a replacement for the language specification,</li>
  <li>a replacement for Expression, Language, Libraries, IR, Profiles, or IDE ownership,</li>
  <li>a private implementation test folder,</li>
  <li>a benchmark suite,</li>
  <li>a repository for examples presented as hidden law,</li>
  <li>a place where backend convenience replaces published architecture,</li>
  <li>a place where execution success alone is treated as proof of correctness.</li>
</ul>

<p>
Conformance is public truth, not implementation folklore.
</p>

<hr/>

<h2 id="relation-with-specification-ownership">6. Relation with Specification Ownership</h2>

<p>
This directory depends on the rest of the specification but does not replace it.
</p>

<p>
The intended ownership model remains:
</p>

<pre>Expression/
   owns canonical source representation

Language/
   owns validated meaning

Libraries/
   own intrinsic primitive law

IR/
   owns canonical execution-facing representation,
   derivation,
   schema posture,
   lowering,
   backend contract

Profiles/
   own optional capability corridors
   and any bounded profile-level execution contracts

Conformance/
   exposes public cases that test the published rules</pre>

<p>
Conformance therefore reads the specification. It does not silently redefine it.
</p>

<hr/>

<h2 id="critical-boundaries">7. Critical Boundaries</h2>

<p>
Conformance must preserve the repository-wide distinctions that the published architecture depends on.
</p>

<p>
These include, at minimum:
</p>

<ul>
  <li>loadable source vs structurally valid canonical source,</li>
  <li>structurally valid source vs semantically accepted program,</li>
  <li>validated meaning vs canonical Execution IR,</li>
  <li>open IR vs lowered form,</li>
  <li>lowered form vs backend contract,</li>
  <li>backend contract vs backend-family consumption,</li>
  <li>backend-family consumability vs execution-start readiness,</li>
  <li>profile validity vs execution-contract satisfaction where a profile-level execution contract exists,</li>
  <li>examples vs normative law,</li>
  <li>reference implementation behavior vs normative truth.</li>
</ul>

<p>
Compactly:
</p>

<pre>accepted upstream
does not automatically imply
accepted downstream

backend-consumable
does not automatically imply
execution-start-ready</pre>

<p>
That distinction matters even before an execution-ready conformance family is fully published.
</p>

<hr/>

<h2 id="directory-structure">8. Directory Structure</h2>

<p>
The directory structure is:
</p>

<pre>Conformance/
├── valid/
│   └── compiler/
│       ├── 01_pure_arithmetic_is_consumable/
│       ├── 02_structured_control_is_consumable/
│       └── 03_explicit_state_is_consumable/
├── invalid/
│   └── compiler/
│       ├── 01_language_valid_but_profile_invalid/
│       ├── 02_ir_valid_but_not_lowerable/
│       ├── 03_lowerable_but_backend_contract_invalid/
│       └── 04_backend_contract_valid_but_consumer_rejected/
└── Readme.md</pre>

<p>
This structure intentionally mirrors the currently published compiler-corridor truth surface.
</p>

<p>
It is staged rather than monolithic:
</p>

<pre>valid/
   publishes
accepted corridor slices

invalid/
   publishes
explicit rejection slices</pre>

<hr/>

<h2 id="published-cases">9. Published Cases</h2>

<p>
The currently published cases focus on compiler-corridor closure for a conservative native compilation path.
</p>

<p>
The positive published cases currently state that:
</p>

<ul>
  <li>pure arithmetic can remain consumable across the corridor,</li>
  <li>structured control can remain consumable across the corridor,</li>
  <li>explicit state can remain consumable across the corridor.</li>
</ul>

<p>
The negative published cases currently distinguish that a case may be:
</p>

<ul>
  <li>language-valid but profile-invalid,</li>
  <li>IR-valid but not lowerable,</li>
  <li>lowerable but backend-contract-invalid,</li>
  <li>backend-contract-valid but consumer-rejected.</li>
</ul>

<p>
This staged publication is deliberate.
</p>

<p>
It turns the compiler corridor into explicit public truth instead of leaving it as implied architectural prose.
</p>

<hr/>

<h2 id="expected-outcomes">10. Expected Outcomes</h2>

<p>
For each published case, a conforming implementation is expected to produce outcomes consistent with the case definition.
</p>

<p>
Those outcomes may include:
</p>

<ul>
  <li>acceptance,</li>
  <li>rejection,</li>
  <li>preserved identity and structure,</li>
  <li>preserved IR distinctions,</li>
  <li>preserved lowering eligibility,</li>
  <li>preserved backend-contract eligibility,</li>
  <li>explicit declared backend-family acceptance or rejection.</li>
</ul>

<p>
The expected question is therefore not only:
</p>

<pre>Did the tool run?</pre>

<p>
but also:
</p>

<pre>Did it accept or reject at the correct stage?
Did it preserve the correct distinctions?
Did it avoid inventing meaning that the specification does not grant?</pre>

<hr/>

<h2 id="active-v01-conformance-focus">11. Active v0.1 Conformance Focus</h2>

<p>
The active v0.1 focus is the published compiler corridor.
</p>

<p>
More precisely, the public truth surface currently concentrates on:
</p>

<pre>validated meaning
   -&gt;
canonical Execution IR
   -&gt;
canonical JSON IR validity where applicable
   -&gt;
lowering eligibility
   -&gt;
backend-contract eligibility
   -&gt;
declared backend-family consumability</pre>

<p>
This is already a substantial closure step.
</p>

<p>
It means the repository no longer treats the compiler corridor as future-only strategy. It already exposes a staged public truth surface for that corridor.
</p>

<p>
However, the current published focus remains conservative:
</p>

<ul>
  <li>it closes consumability before broader execution readiness,</li>
  <li>it closes backend-family acceptance before richer runtime guarantees,</li>
  <li>it keeps UI-heavy and broader runtime-mediated execution outside the first published executable promise.</li>
</ul>

<hr/>

<h2 id="relation-with-examples-ir-profiles-and-reference-implementation">12. Relation with Examples, IR, Profiles, and Reference Implementation</h2>

<p>
Conformance must be read in relation to nearby repository surfaces without collapsing them.
</p>

<h3>12.1 Relation with Examples</h3>

<p>
Examples may illustrate patterns, but they do not become hidden law merely by existing.
</p>

<p>
A conformance case is different:
</p>

<pre>example
   illustrates

conformance case
   binds public accept / reject / preserve expectations</pre>

<h3>12.2 Relation with IR</h3>

<p>
The conformance corridor depends directly on the published IR architecture.
</p>

<p>
In particular, conformance reads and depends on:
</p>

<ul>
  <li>IR derivation,</li>
  <li>IR construction,</li>
  <li>schema posture,</li>
  <li>lowering,</li>
  <li>backend contract.</li>
</ul>

<p>
Conformance therefore checks whether implementations remain aligned with the open execution-facing corridor defined by <code>IR/</code>. It does not move IR ownership into <code>Conformance/</code>.
</p>

<h3>12.3 Relation with Profiles</h3>

<p>
The currently published compiler-corridor cases are read relative to published profile material, especially the Native CPU LLVM corridor.
</p>

<p>
That means conformance may already depend on distinctions such as:
</p>

<ul>
  <li>language-valid but profile-invalid,</li>
  <li>profile-valid and backend-consumable,</li>
  <li>profile-valid but still rejected later in the corridor.</li>
</ul>

<p>
Where a profile later publishes a companion execution contract, conformance growth may also distinguish:
</p>

<ul>
  <li>backend-contract-valid but execution-contract-invalid,</li>
  <li>execution-contract-valid and execution-start-ready.</li>
</ul>

<p>
That extension remains compatible with the current staged architecture:
</p>

<pre>profile validity
   is not always the same as
execution-start readiness</pre>

<h3>12.4 Relation with Reference Implementation</h3>

<p>
A reference implementation may help exercise the published cases, but it does not become the hidden owner of language truth.
</p>

<p>
The correct direction remains:
</p>

<pre>published specification
   -&gt;
published conformance
   -&gt;
implementation behavior</pre>

<p>
not:
</p>

<pre>implementation behavior
   -&gt;
retroactive language law</pre>

<hr/>

<h2 id="execution-ready-growth-posture">13. Execution-Ready Growth Posture</h2>

<p>
The current published conformance focus stops conservatively at declared backend-family consumability.
</p>

<p>
That is a deliberate staging boundary, not a denial that execution-ready conformance matters.
</p>

<p>
The next coherent extension after the current compiler-corridor truth surface is:
</p>

<pre>backend-contract-valid
   -&gt;
execution-contract satisfaction where published
   -&gt;
execution-start readiness where published</pre>

<p>
Accordingly, future execution-ready conformance growth should remain disciplined and explicit.
</p>

<p>
It should distinguish at least:
</p>

<ul>
  <li>backend-consumable but not execution-contract-ready,</li>
  <li>execution-contract-ready but startup-faulting under explicit published fault conditions,</li>
  <li>execution-ready and observably correct under the published bounded corridor.</li>
</ul>

<p>
This directory therefore already leaves room for a later executable conformance family without pretending that this family is already fully published today.
</p>

<hr/>

<h2 id="future-growth">14. Future Growth</h2>

<p>
Future growth should remain conservative and corridor-oriented.
</p>

<p>
Good future growth directions include:
</p>

<ul>
  <li>more valid compiler cases,</li>
  <li>more invalid compiler cases,</li>
  <li>richer profile-rejection distinctions,</li>
  <li>execution-contract-aware cases where a published profile companion exists,</li>
  <li>bounded executable cases once execution-start closure is publicly anchored,</li>
  <li>later target-specific conformance families where the published specification justifies them.</li>
</ul>

<p>
A good growth rule is:
</p>

<pre>close one public corridor fully
before opening many half-closed fronts</pre>

<p>
Conformance growth should therefore follow publication maturity, not wishful scope expansion.
</p>

<hr/>

<h2 id="summary">15. Summary</h2>

<p>
This directory defines the public conformance surface of the published FROG specification.
</p>

<p>
It answers:
</p>

<pre>What must be accepted?
What must be rejected?
What must be preserved?</pre>

<p>
In v0.1, the active published focus already includes the compiler corridor up to declared backend-family consumability.
</p>

<p>
That means conformance already spans:
</p>

<ul>
  <li>source acceptance and rejection,</li>
  <li>semantic acceptance and rejection,</li>
  <li>IR preservation,</li>
  <li>canonical JSON validation where applicable,</li>
  <li>lowering eligibility,</li>
  <li>backend-contract eligibility,</li>
  <li>declared backend-family acceptance or rejection.</li>
</ul>

<p>
And it already leaves a clean next extension point:
</p>

<pre>execution-contract-aware
and later
execution-ready conformance growth</pre>

<p>
This keeps the repository disciplined:
</p>

<pre>specification defines

conformance checks

implementation must align</pre>

<p>
That is the intended role of <code>Conformance/</code> in FROG v0.1.
</p>
