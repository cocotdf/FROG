<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG — Heilmeier Framing</h1>

<p align="center">
  Strategic framing for the technological purpose, expected impact, and program logic of FROG<br/>
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
  <li><a href="#what-is-already-demonstrated-in-the-repository">12. What is Already Demonstrated in the Repository</a></li>
  <li><a href="#future-end-to-end-poc-direction">13. Future End-to-End POC Direction</a></li>
  <li><a href="#summary">14. Summary</a></li>
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
It is a program-framing document that explains the problem, the opportunity, the expected impact, and the execution logic behind FROG.
</p>

<hr/>

<h2 id="strategic-thesis">2. Strategic Thesis</h2>

<p>
FROG aims to make <strong>graphical system-grade programming open, inspectable, hardware-agnostic, and deployable</strong> across heterogeneous execution targets.
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
  <li>the openness and inspectability needed for modern interoperability, portability, and AI-assisted tooling.</li>
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
FROG targets the missing zone where the following properties are combined rather than traded against one another:
</p>

<ul>
  <li>visual dataflow programming rather than syntax-heavy implementation work,</li>
  <li>system-grade execution depth rather than shallow convenience scripting only,</li>
  <li>hardware agnosticism rather than ecosystem lock-in,</li>
  <li>open and inspectable program artifacts rather than opaque saved formats,</li>
  <li>a path from rapid prototyping to deployment rather than a permanent split between prototype tooling and production tooling.</li>
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
  <li>difficulty of cleanly separating source truth, execution-facing IR, backend lowering, and runtime realization.</li>
</ul>

<p>
The issue is therefore not merely “better usability”.
The issue is that graphical industrial programming has historically lacked a sufficiently open and standardized architectural foundation.
</p>

<hr/>

<h2 id="heilmeier-h3">6. Heilmeier H3 — What is new, and why do we think it will work?</h2>

<p>
What is new is not just the idea of drawing dataflow graphs.
What is new is the combination of the following architectural commitments inside one coherent open system:
</p>

<ul>
  <li>an open canonical <code>.frog</code> source representation,</li>
  <li>an explicit separation between saved source, validated semantics, derived IR, lowering, backend contract, and runtime realization,</li>
  <li>a future standardized execution-facing FROG IR that remains inspectable and recoverable,</li>
  <li>a backend-family-oriented lowering path rather than one hidden private execution pipeline,</li>
  <li>a future path toward known backend/compiler targets without making those targets the definition of the language.</li>
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
  <li><strong>AI and tooling ecosystems</strong> gain a readable and inspectable program representation rather than opaque graphical artifacts.</li>
  <li><strong>The broader engineering community</strong> gains an alternative model for graphical programming that is open, portable, and structurally modern.</li>
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
  <li>Execution-facing representations could become inspectable, standardizable, and portable.</li>
  <li>Graphical industrial programming could become hardware-agnostic by design rather than vendor-limited by default.</li>
  <li>Multiple hardware manufacturers could participate in one open language ecosystem instead of forcing users into mutually isolated stacks.</li>
  <li>AI-assisted tooling could operate on open source and open IR artifacts rather than reverse-engineering closed graphical representations.</li>
</ul>

<p>
The long-term difference would therefore be structural:
FROG could shift graphical system-grade programming from vendor-controlled lock-in toward open, multi-vendor, inspectable infrastructure.
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
</ul>

<p>
The key risk is not that the idea is meaningless.
The key risk is that the project could stop too early at the “interesting prototype” stage without closing the future standardized IR and backend/compiler story strongly enough.
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

<hr/>

<h2 id="what-is-already-demonstrated-in-the-repository">12. What is Already Demonstrated in the Repository</h2>

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

<hr/>

<h2 id="future-end-to-end-poc-direction">13. Future End-to-End POC Direction</h2>

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

<hr/>

<h2 id="summary">14. Summary</h2>

<p>
FROG is trying to open a missing category: accessible graphical programming with a serious path to system-grade execution, hardware agnosticism, and future deployable backend/compiler integration.
</p>

<p>
The repository already demonstrates meaningful parts of this architecture through executable reference slices, but it does not yet claim that the final industrial compiler/runtime story is complete.
</p>

<p>
The strategic case for FROG is therefore clear:
</p>

<ul>
  <li>open the saved source format,</li>
  <li>open and standardize the execution-facing dataflow representation,</li>
  <li>separate language truth from runtime-private realization,</li>
  <li>prepare a future path toward known compiler/runtime backends,</li>
  <li>enable an open, multi-vendor, industrial graphical programming ecosystem.</li>
</ul>

<p>
That is the long-term significance of the project.
</p>
