<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">🐸 FROG — Heilmeier Framing</h1>

<p align="center">
  Strategic framing for the technological purpose, expected impact, ecosystem significance, and long-term program logic of FROG<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#why-this-page-exists">1. Why this Page Exists</a></li>
  <li><a href="#strategic-thesis">2. Strategic Thesis</a></li>
  <li><a href="#positioning-gap">3. Positioning Gap</a></li>
  <li><a href="#heilmeier-h1">4. Heilmeier H1 — What are you trying to do?</a></li>
  <li><a href="#heilmeier-h2">5. Heilmeier H2 — How is it done today, and what are the limits?</a></li>
  <li><a href="#heilmeier-h3">6. Heilmeier H3 — What is new, and why do we think it will work?</a></li>
  <li><a href="#heilmeier-h4">7. Heilmeier H4 — Who cares if we succeed?</a></li>
  <li><a href="#heilmeier-h5">8. Heilmeier H5 — What difference will success make?</a></li>
  <li><a href="#heilmeier-h6">9. Heilmeier H6 — What are the risks and what still needs to be proved?</a></li>
  <li><a href="#heilmeier-h7">10. Heilmeier H7 — How much will it cost?</a></li>
  <li><a href="#heilmeier-h8">11. Heilmeier H8 — How long will it take and what are the midterm and final exams?</a></li>
  <li><a href="#relation-with-strategy-roadmap-and-versioning">12. Relation with Strategy, Roadmap, and Versioning</a></li>
  <li><a href="#what-is-already-demonstrated-in-the-repository">13. What is Already Demonstrated in the Repository</a></li>
  <li><a href="#future-end-to-end-poc-direction">14. Future End-to-End POC Direction</a></li>
  <li><a href="#summary">15. Summary</a></li>
</ul>

<hr/>

<h2 id="why-this-page-exists">1. Why this Page Exists</h2>

<p>
This page explains why FROG exists as a technological program, what gap it targets, why that gap matters, what is already demonstrated, and what still needs to be proven before the full long-term compiler/runtime vision is realized.
</p>

<p>
This page is intentionally strategic.
It is not the normative language definition.
It is not the reference implementation documentation.
It is not the roadmap.
It is not the current corpus-version status surface.
It is a program-framing document that explains the problem, the opportunity, the expected impact, and the execution logic behind FROG.
</p>

<hr/>

<h2 id="strategic-thesis">2. Strategic Thesis</h2>

<p>
FROG aims to make <strong>graphical system-grade programming open, inspectable, hardware-agnostic, auditable, and deployable</strong> across heterogeneous execution targets.
</p>

<p>
The project is not only about creating another graphical language.
It is about removing structural lock-in from graphical industrial programming by opening:
</p>

<ul>
  <li>the saved program format,</li>
  <li>the execution-facing dataflow representation,</li>
  <li>the lowering path toward backend families,</li>
  <li>the contract boundary between open program semantics and downstream execution.</li>
</ul>

<p>
In practical terms, FROG seeks to combine:
</p>

<ul>
  <li>the accessibility historically associated with graphical dataflow programming,</li>
  <li>the execution seriousness required for industrial and system-grade deployment,</li>
  <li>the openness and inspectability needed for modern interoperability and portability,</li>
  <li>the auditability and structured artifacts needed for AI-assisted generation and transformation workflows,</li>
  <li>the sovereignty-preserving properties needed for long-term industrial independence from opaque vendor-controlled formats.</li>
</ul>

<p>
The strategic thesis is therefore not merely “open graphical programming”.
It is that the next generation of industrial programming infrastructure must remain:
</p>

<ul>
  <li>machine-friendly enough for AI-era tooling,</li>
  <li>human-reviewable enough for security and engineering trust,</li>
  <li>open enough for multi-vendor implementation,</li>
  <li>structured enough to preserve meaning across validation, derivation, and backend handoff,</li>
  <li>governable enough that current version posture remains explicit rather than hidden in one proprietary lifecycle.</li>
</ul>

<hr/>

<h2 id="positioning-gap">3. Positioning Gap</h2>

<p>
FROG targets a missing zone in the current software landscape.
</p>

<p>
At one end of the spectrum, syntax-first languages can deliver depth of control, determinism, and deployment seriousness, but they often impose substantial implementation burden on domain engineers and system integrators.
At the other end of the spectrum, accessible environments may reduce friction but often remain constrained by proprietary formats, opaque execution layers, limited backend openness, or hardware-vendor lock-in.
</p>

<p>
The gap is now even wider in the AI era.
Modern toolchains increasingly generate, rewrite, transform, or assist program structure.
That increases the need for representations that are both machine-friendly and human-reviewable.
Many current environments satisfy one side of that requirement better than the other.
</p>

<p>
FROG targets the missing zone where the following properties are combined rather than traded against one another:
</p>

<ul>
  <li>visual dataflow programming rather than syntax-heavy implementation work,</li>
  <li>system-grade execution depth rather than shallow convenience scripting only,</li>
  <li>hardware agnosticism rather than ecosystem lock-in,</li>
  <li>open and inspectable program artifacts rather than opaque saved formats,</li>
  <li>a path from rapid prototyping to deployment rather than a permanent split between prototype tooling and production tooling,</li>
  <li>structured machine-compatible source artifacts together with direct human structural review.</li>
</ul>

<p>
This is why FROG matters.
The opportunity is not merely to imitate existing graphical tools.
The opportunity is to open a missing systems capability category.
</p>

<hr/>

<h2 id="heilmeier-h1">4. Heilmeier H1 — What are you trying to do?</h2>

<p>
FROG is trying to create an open, hardware-agnostic graphical dataflow language and associated architecture that can support a serious path from canonical saved source to execution-oriented IR, backend-specific lowering, backend contract generation, and eventually real compiler/runtime backends.
</p>

<p>
In simple terms, the project is trying to make the following possible:
</p>

<ul>
  <li>save graphical programs in an open and inspectable format,</li>
  <li>validate those programs against published semantic rules,</li>
  <li>derive a standardized execution-facing FROG IR,</li>
  <li>lower that IR toward multiple backend families,</li>
  <li>run or compile those programs on heterogeneous targets without making one private vendor stack the definition of the language.</li>
</ul>

<p>
The long-term goal is not just a new editor.
It is an open language foundation that can eventually support:
</p>

<ul>
  <li>industrial automation,</li>
  <li>robotics,</li>
  <li>embedded and edge systems,</li>
  <li>AI-assisted development and transformation workflows,</li>
  <li>CPU, ARM, microcontroller, FPGA, and other backend-oriented execution paths.</li>
</ul>

<p>
More specifically, FROG is trying to make AI-era program generation more governable.
It aims to provide a language stack where:
</p>

<ul>
  <li>the saved source remains structured and machine-friendly,</li>
  <li>the program structure remains graphically reviewable by humans,</li>
  <li>the execution-facing IR remains open to inspection,</li>
  <li>downstream compilation remains separate from the normative language definition,</li>
  <li>and the repository can state its current corpus posture explicitly without forcing that truth into strategic prose.</li>
</ul>

<hr/>

<h2 id="heilmeier-h2">5. Heilmeier H2 — How is it done today, and what are the limits?</h2>

<p>
Today, the landscape is fragmented.
</p>

<ul>
  <li>Syntax-first languages provide strong execution depth but impose significant implementation friction.</li>
  <li>Graphical systems can provide accessibility but often remain proprietary, opaque, or tied to a specific vendor ecosystem.</li>
  <li>The saved program representation is often not designed as an open, durable, inspectable interoperability layer.</li>
  <li>The internal execution representation is often not designed to remain open, recoverable, or backend-neutral.</li>
</ul>

<p>
The practical limits of the current situation are structural rather than cosmetic:
</p>

<ul>
  <li>vendor lock-in,</li>
  <li>difficulty of porting graphical system logic across hardware ecosystems,</li>
  <li>difficulty of integrating modern AI tooling with opaque graphical formats,</li>
  <li>difficulty of building an open multi-vendor ecosystem around system-grade graphical execution,</li>
  <li>difficulty of cleanly separating source truth, execution-facing IR, backend lowering, and runtime realization,</li>
  <li>difficulty of keeping version posture explicit rather than burying it in one vendor release logic.</li>
</ul>

<p>
There is also a reviewability problem.
Textual languages can certainly be audited, but structural understanding is often indirect:
reviewers reconstruct system architecture from syntax, coding conventions, build context, and analysis tooling.
In closed graphical systems, the problem is different but equally serious:
the structure may be visual, yet the saved format and execution path remain opaque or vendor-bound.
</p>

<p>
The issue is therefore not merely “better usability”.
The issue is that graphical industrial programming has historically lacked a sufficiently open and standardized architectural foundation,
and AI-era software generation is making the cost of opaque or weakly reviewable representations even higher.
</p>

<hr/>

<h2 id="heilmeier-h3">6. Heilmeier H3 — What is new, and why do we think it will work?</h2>

<p>
What is new is not just the idea of drawing dataflow graphs.
What is new is the combination of the following architectural commitments inside one coherent open system:
</p>

<ul>
  <li>an open canonical <code>.frog</code> source representation,</li>
  <li>a canonical source model that is structured JSON rather than a private opaque file format,</li>
  <li>an explicit separation between saved source, validated semantics, derived IR, lowering, backend contract, and runtime realization,</li>
  <li>a standardized execution-facing FROG IR that remains inspectable and recoverable,</li>
  <li>a backend-family-oriented lowering path rather than one hidden private execution pipeline,</li>
  <li>a future path toward known backend/compiler targets without making those targets the definition of the language,</li>
  <li>a centralized repository-visible versioning surface rather than scattered implicit version claims.</li>
</ul>

<p>
The project can work because the repository has already begun to demonstrate the architecture in small executable slices rather than relying only on abstract claims.
The current slices already show that the published boundaries are not merely conceptual:
</p>

<ul>
  <li>public input/output dataflow,</li>
  <li>natural widget-value participation,</li>
  <li>object-style UI interaction,</li>
  <li>explicit local memory and valid feedback through delay.</li>
</ul>

<p>
The architectural argument is especially strong in the AI era:
FROG does not offer only a machine-friendly source representation.
It also offers a human-reviewable primary program structure and an open execution-facing IR.
That combination is precisely what reduces the auditability gap between generated artifacts and deployed behavior.
</p>

<p>
That does not yet prove the full compiler story.
But it does provide technical evidence that the architecture is capable of sustaining a real execution path without collapsing all layers into one implementation shortcut.
</p>

<p>
A particularly strong future demonstration would be to show that standardized FROG IR can be lowered toward a known CPU compiler pipeline such as LLVM, while keeping LLVM clearly downstream from FROG rather than letting LLVM become the normative language definition.
</p>

<hr/>

<h2 id="heilmeier-h4">7. Heilmeier H4 — Who cares if we succeed?</h2>

<p>
If FROG succeeds, multiple groups should care.
</p>

<ul>
  <li><strong>Industrial users and integrators</strong> gain an open graphical programming foundation that is not structurally locked to one hardware vendor.</li>
  <li><strong>Hardware vendors</strong> gain a path to expose serious industrial capabilities through a shared open graphical execution model rather than through isolated proprietary stacks.</li>
  <li><strong>System builders</strong> gain a cleaner way to target CPUs, embedded systems, edge devices, and future hardware families through one architectural language stack.</li>
  <li><strong>AI and tooling ecosystems</strong> gain structured source and open IR artifacts rather than opaque graphical artifacts.</li>
  <li><strong>Security and assurance stakeholders</strong> gain a more direct way to inspect generated or transformed logic across source and execution-facing layers.</li>
  <li><strong>The broader engineering community</strong> gains an alternative model for graphical programming that is open, portable, and structurally modern.</li>
  <li><strong>States, sovereign industrial actors, and strategic technology programs</strong> gain a path away from dependence on opaque vendor-controlled graphical programming infrastructure.</li>
</ul>

<p>
The broader strategic consequence is large:
FROG could help transform graphical system programming from a closed vendor capability into an open ecosystem capability.
</p>

<hr/>

<h2 id="heilmeier-h5">8. Heilmeier H5 — What difference will success make?</h2>

<p>
If successful, FROG would change more than one tool.
It would change the structure of the category.
</p>

<ul>
  <li>Graphical programs would no longer need to live inside opaque saved formats.</li>
  <li>The saved source could remain open, structured, machine-friendly, and durable.</li>
  <li>Execution-facing representations could become inspectable, standardizable, and portable.</li>
  <li>Graphical industrial programming could become hardware-agnostic by design rather than vendor-limited by default.</li>
  <li>Multiple hardware manufacturers could participate in one open language ecosystem instead of forcing users into mutually isolated stacks.</li>
  <li>AI-assisted tooling could operate on open source and open IR artifacts rather than reverse-engineering closed graphical representations.</li>
  <li>Critical generated logic could become easier to review visually and structurally rather than only through indirect reconstruction.</li>
  <li>Specification-corpus version posture could remain publicly readable and governable rather than hidden in one product lifecycle.</li>
</ul>

<p>
The long-term difference would therefore be structural:
FROG could shift graphical system-grade programming from vendor-controlled lock-in toward open, multi-vendor, inspectable infrastructure.
</p>

<p>
That difference is not only technical.
It is also strategic.
In industrial and security-sensitive domains, the ability to inspect, attribute, govern, and port logic matters for trust, resilience, and technological sovereignty.
</p>

<hr/>

<h2 id="heilmeier-h6">9. Heilmeier H6 — What are the risks and what still needs to be proved?</h2>

<p>
Several important things still need to be proved.
</p>

<ul>
  <li>The standardized FROG execution IR must be stabilized more fully.</li>
  <li>The lowering model toward backend families must be specified more deeply.</li>
  <li>A future backend/compiler-oriented path must be demonstrated more concretely.</li>
  <li>Real deployable targets must be shown beyond the current minimal reference path.</li>
  <li>Backend diversity must be demonstrated without collapsing the architecture into one backend-specific truth.</li>
  <li>The relationship between open IR, backend contracts, compiler backends, runtime realization, and deployment artifacts must be shown end to end.</li>
  <li>The claimed auditability advantage must remain disciplined and credible rather than overstated.</li>
  <li>The distinction between strategy, roadmap sequencing, and current version truth must remain explicit.</li>
</ul>

<p>
The key risk is not that the idea is meaningless.
The key risk is that the project could stop too early at the “interesting prototype” stage without closing the future standardized IR and backend/compiler story strongly enough.
</p>

<p>
Another risk is strategic overclaim.
FROG should not claim that graphical representation automatically guarantees security or that textual languages cannot be reviewed.
Its real claim is narrower and stronger:
it can reduce structural opacity by combining machine-friendly source, direct graphical reviewability, open execution-facing representation, and explicit repository-visible version governance.
</p>

<hr/>

<h2 id="heilmeier-h7">10. Heilmeier H7 — How much will it cost?</h2>

<p>
At the current repository stage, the project should be understood as an architecture-building and proof-building effort rather than as a finalized program budget.
</p>

<p>
The cost profile should eventually separate into at least four layers:
</p>

<ul>
  <li>normative specification work,</li>
  <li>reference implementation and executable slice closure,</li>
  <li>future backend/compiler/runtime proof of concept work,</li>
  <li>future IDE and ecosystem-enablement work.</li>
</ul>

<p>
A later roadmap phase should convert this strategic framing into explicit work packages, milestones, cost ranges, and resource assumptions.
The current corpus-version posture and current detailed repository-surface status remain governed centrally in <code>Versioning/</code>, not in this strategic framing.
</p>

<hr/>

<h2 id="heilmeier-h8">11. Heilmeier H8 — How long will it take and what are the midterm and final exams?</h2>

<p>
The project should be judged by successive proof points rather than by one monolithic promise.
</p>

<p>
Natural milestone categories are:
</p>

<ul>
  <li><strong>Early exam</strong> — prove executable architectural slices from canonical source through runtime consumption.</li>
  <li><strong>Midterm exam</strong> — stabilize the execution-facing FROG IR and the backend-lowering story more fully.</li>
  <li><strong>Advanced exam</strong> — demonstrate an end-to-end backend/compiler proof of concept, ideally including a known backend family such as LLVM for CPU-oriented execution.</li>
  <li><strong>Long-term exam</strong> — demonstrate a credible path toward a serious IDE, a broader primitive base, stronger structures, richer memory semantics, and multi-target deployment.</li>
</ul>

<p>
The important point is that each stage should be auditable, explicit, and grounded in repository-visible artifacts rather than in vague aspiration.
</p>

<p>
In the AI-era framing, a particularly important exam is whether FROG can demonstrate the full review loop:
</p>

<ul>
  <li>structured source generation,</li>
  <li>human graphical review,</li>
  <li>semantic validation,</li>
  <li>inspectable IR derivation,</li>
  <li>backend handoff without loss of architectural traceability.</li>
</ul>

<p>
The ordering of those proofs belongs to the roadmap layer.
The current published version posture of the corpus belongs to the versioning layer.
This document explains why those proof points matter strategically.
</p>

<hr/>

<h2 id="relation-with-strategy-roadmap-and-versioning">12. Relation with Strategy, Roadmap, and Versioning</h2>

<p>
The repository now contains three distinct repository-wide framing and governance surfaces that answer three different questions:
</p>

<table>
  <thead>
    <tr>
      <th>Surface</th>
      <th>Primary question</th>
      <th>What it must not replace</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>Strategy/</code></td>
      <td>Why does FROG matter?</td>
      <td>Normative technical ownership, closure sequencing, or current corpus-version truth</td>
    </tr>
    <tr>
      <td><code>Roadmap/</code></td>
      <td>In what order should FROG be closed?</td>
      <td>Normative technical ownership, strategic rationale, or current corpus-version truth</td>
    </tr>
    <tr>
      <td><code>Versioning/</code></td>
      <td>What is the current published specification corpus version, what doctrine governs version evolution, and what is the current detailed per-surface status?</td>
      <td>Normative technical ownership, strategic rationale, or milestone sequencing</td>
    </tr>
  </tbody>
</table>

<p>
This means:
</p>

<ul>
  <li>Strategy explains the <strong>why</strong>,</li>
  <li>Roadmap explains the <strong>next</strong>,</li>
  <li>Versioning explains the <strong>current published corpus posture</strong>.</li>
</ul>

<p>
This Heilmeier framing belongs to the strategic layer.
It may refer to the current baseline of the project, but it must not become the authoritative place where the repository declares its current version state or detailed surface-by-surface status.
When that information is needed, the authoritative repository-visible entry points are:
</p>

<ul>
  <li><code>Versioning/Readme.md</code>,</li>
  <li><code>Versioning/Matrix.md</code>.</li>
</ul>

<hr/>

<h2 id="what-is-already-demonstrated-in-the-repository">13. What is Already Demonstrated in the Repository</h2>

<p>
The repository already demonstrates a minimal executable reference path through a sequence of small vertical slices.
</p>

<ul>
  <li><strong>01_pure_addition</strong> — end-to-end public-input/public-output arithmetic path.</li>
  <li><strong>02_ui_value_roundtrip</strong> — natural widget-value path without object-style UI collapse.</li>
  <li><strong>03_ui_property_write</strong> — first explicit object-style UI interaction path.</li>
  <li><strong>04_stateful_feedback_delay</strong> — first explicit-memory and valid-feedback path.</li>
</ul>

<p>
These slices matter because they show that the architecture already supports real execution exercises without requiring the final full compiler pipeline to exist yet.
</p>

<p>
They should be understood as proof of architectural viability, not as proof that all long-term execution targets are already closed.
</p>

<p>
They also matter strategically because they keep the project grounded in inspectable repository-visible artifacts.
The strategic argument for openness, auditability, and downstream seriousness is stronger when each stage is already exercised in public slices.
The authoritative current repository-wide version posture of those published surfaces remains centralized in <code>Versioning/</code>.
</p>

<hr/>

<h2 id="future-end-to-end-poc-direction">14. Future End-to-End POC Direction</h2>

<p>
A future end-to-end proof of concept should demonstrate the full chain more explicitly and more convincingly.
</p>

<p>
The ideal future demonstration path is:
</p>

<pre><code>.frog canonical source
    |
    v
validation
    |
    v
standardized FROG execution IR
    |
    v
backend-specific lowering
    |
    v
backend contract / backend-oriented IR
    |
    v
known compiler/runtime backend
    |
    v
deployable artifact
</code></pre>

<p>
For CPU-oriented execution, a future LLVM-oriented demonstration would be especially meaningful.
It would show that FROG is not merely a saved graphical representation or a toy runtime, but a language architecture capable of targeting serious industrial compilation paths while preserving its own open upstream boundaries.
</p>

<p>
For hardware-oriented targets, the same logic should later extend toward backend families appropriate for embedded systems, microcontrollers, and FPGA-oriented flows.
</p>

<p>
A particularly convincing future proof point would be an AI-assisted generation scenario in which:
</p>

<ul>
  <li>a valid canonical <code>.frog</code> source artifact is produced,</li>
  <li>its structure is reviewed graphically by a human,</li>
  <li>its validated meaning is derived into inspectable FROG IR,</li>
  <li>that IR is lowered toward a serious backend path,</li>
  <li>the end-to-end chain remains attributable and auditable.</li>
</ul>

<p>
The strategic importance of that proof belongs here.
The ordering of the work belongs to <code>Roadmap/</code>.
The current corpus-version truth and detailed surface status belong to <code>Versioning/</code>.
</p>

<hr/>

<h2 id="summary">15. Summary</h2>

<p>
FROG is trying to open a missing category:
accessible graphical programming with a serious path to system-grade execution, hardware agnosticism, inspectable intermediate representation, and future deployable backend/compiler integration.
</p>

<p>
The repository already demonstrates meaningful parts of this architecture through executable reference slices, but it does not yet claim that the final industrial compiler/runtime story is complete.
</p>

<p>
The strategic case for FROG is therefore clear:
</p>

<ul>
  <li>open the saved source format,</li>
  <li>keep that source structured and machine-friendly,</li>
  <li>make program structure graphically reviewable by humans,</li>
  <li>open and standardize the execution-facing dataflow representation,</li>
  <li>separate language truth from runtime-private realization,</li>
  <li>prepare a future path toward known compiler/runtime backends,</li>
  <li>enable an open, multi-vendor, industrial graphical programming ecosystem,</li>
  <li>reduce the auditability gap introduced by increasingly AI-assisted software generation,</li>
  <li>support industrial security and technological sovereignty through open, inspectable, and governable program artifacts.</li>
</ul>

<p>
That is the long-term significance of the project.
This document explains <strong>why</strong> that significance matters.
It does not replace the roadmap’s sequencing role, and it does not replace the versioning layer’s role as the centralized source for current published corpus-version truth.
</p>
