<p align="center">
  <img src="../FROG%20logo.svg" alt="FROG logo" width="140"/>
</p>

<h1 align="center">FROG Roadmap Milestones</h1>

<p align="center">
  <strong>Compact milestone tracking for the roadmap layer inside the FROG repository</strong>
</p>

<p align="center">
  <a href="./Readme.md">Back to Roadmap overview</a>
</p>

<hr/>

<h2>Milestone map</h2>

<pre>
M0  [x] Architectural separation established
M1  [x] First published executable slices established
M2  [x] Non-normative reference implementation posture established
M3  [x] Root repository recontextualized around the published state
M4  [x] Strategic framing layer published
M5  [~] Roadmap layer published inside the repository
M6  [ ] v0.1 foundation closed
M7  [ ] Source schema / validator closure established
M8  [ ] Stable repeatable reference execution path for the supported subset
M9  [ ] First serious backend-oriented compiler path
M10 [ ] First serious FROG IDE foundation
M11 [ ] Expanded language breadth, profile depth, and deployment depth
M12 [ ] Practical open industrial graphical ecosystem with clear structural superiority
</pre>

<hr/>

<h2>Milestone detail</h2>

<h3>M0 — Architectural separation established</h3>

<ul>
  <li><strong>Status:</strong> [x]</li>
  <li><strong>Meaning:</strong> the core ownership split exists between source, semantics, IR, libraries, profiles, and IDE.</li>
  <li><strong>Main consequence:</strong> FROG is not defined as one product implementation.</li>
</ul>

<h3>M1 — First published executable slices established</h3>

<ul>
  <li><strong>Status:</strong> [x]</li>
  <li><strong>Meaning:</strong> the repository already demonstrates early executable vertical slices.</li>
  <li><strong>Main consequence:</strong> FROG is no longer architectural prose only.</li>
</ul>

<h3>M2 — Non-normative reference implementation posture established</h3>

<ul>
  <li><strong>Status:</strong> [x]</li>
  <li><strong>Meaning:</strong> the reference path exists but is not the definition of the language.</li>
  <li><strong>Main consequence:</strong> implementation convenience remains downstream from published ownership layers.</li>
</ul>

<h3>M3 — Root repository recontextualized around the published state</h3>

<ul>
  <li><strong>Status:</strong> [x]</li>
  <li><strong>Meaning:</strong> the main landing page reflects the current architectural and repository-level reality more accurately.</li>
  <li><strong>Main consequence:</strong> the repository is easier to read as a structured language effort.</li>
</ul>

<h3>M4 — Strategic framing layer published</h3>

<ul>
  <li><strong>Status:</strong> [x]</li>
  <li><strong>Meaning:</strong> the project has an explicit strategic explanation distinct from normative ownership.</li>
  <li><strong>Main consequence:</strong> strategic positioning no longer has to leak into technical documents.</li>
</ul>

<h3>M5 — Roadmap layer published inside the repository</h3>

<ul>
  <li><strong>Status:</strong> [~]</li>
  <li><strong>Meaning:</strong> a repository-local roadmap exists as a non-normative planning layer.</li>
  <li><strong>Main consequence:</strong> sequencing can now be discussed without confusing planning and specification.</li>
  <li><strong>To close:</strong></li>
  <ul>
    <li>keep this layer aligned with the real published state after each major closure step</li>
    <li>keep milestone wording synchronized with the roadmap overview</li>
    <li>avoid letting milestone summaries drift away from specification reality</li>
  </ul>
</ul>

<h3>M6 — v0.1 foundation closed</h3>

<ul>
  <li><strong>Status:</strong> [ ]</li>
  <li><strong>Meaning:</strong> the base specification is tight enough that source truth, semantic truth, derived execution form, backend-facing handoff, and implementation workspace are no longer blurred.</li>
  <li><strong>Main consequence:</strong> later compiler, runtime, and IDE work can build on a much firmer foundation.</li>
  <li><strong>To close:</strong></li>
  <ul>
    <li>Expression ↔ Language ↔ IR correspondence tightened</li>
    <li>minimal primitive baseline clarified</li>
    <li>type / value / state ownership clarified</li>
    <li>execution-model and structure semantics tightened</li>
    <li>normative truth versus implementation convenience fully clarified</li>
    <li>architectural distinction between backend family, target profile, deployment mode, and runtime-private realization kept explicit across the relevant documents</li>
    <li>conformance around already-published boundaries strengthened</li>
  </ul>
</ul>

<h3>M7 — Source schema / validator closure established</h3>

<ul>
  <li><strong>Status:</strong> [ ]</li>
  <li><strong>Meaning:</strong> canonical source ownership is explicit enough in both normative prose and machine-checkable form that disciplined structural validation no longer depends on documentation-only interpretation or private validator folklore.</li>
  <li><strong>Main consequence:</strong> structural validation becomes more explicit, more reproducible, easier to compare across implementations, and better separated from later semantic validation and downstream derivation.</li>
  <li><strong>To close:</strong></li>
  <ul>
    <li>source-shape / schema posture published explicitly inside <code>Expression/</code></li>
    <li>a conservative machine-checkable source-schema artifact published for canonical top-level source shape</li>
    <li>conformance reading and case expectations made more explicit across loadability, structural validity, semantic acceptance, and preservation</li>
    <li>reference-validator posture aligned with the distinction between schema-assisted structural validation and later semantic validation</li>
    <li>schema posture kept aligned with canonical source ownership rather than implementation convenience</li>
    <li>the repository makes clear that schema artifacts assist structural validation but do not replace normative specification ownership</li>
  </ul>
</ul>

<h3>M8 — Stable repeatable reference execution path</h3>

<ul>
  <li><strong>Status:</strong> [ ]</li>
  <li><strong>Meaning:</strong> the supported subset can be processed end to end repeatedly through the same explicit stages.</li>
  <li><strong>Main consequence:</strong> the reference path becomes a reliable proof surface rather than a one-off demonstration.</li>
  <li><strong>To close:</strong></li>
  <ul>
    <li>supported subset explicitly bounded</li>
    <li>intermediate artifacts standardized</li>
    <li>CLI execution path made easy to run and inspect</li>
    <li>end-to-end repeatability demonstrated</li>
    <li>development and execution postures shown to support different runtime-service bundles without changing language meaning</li>
  </ul>
</ul>

<h3>M9 — First serious backend-oriented compiler path</h3>

<ul>
  <li><strong>Status:</strong> [ ]</li>
  <li><strong>Meaning:</strong> FROG can feed a real backend-oriented path without collapsing its own IR and architectural stages into one private downstream technology.</li>
  <li><strong>Main consequence:</strong> the project gains real compiler/runtime credibility beyond the early reference path.</li>
  <li><strong>To close:</strong></li>
  <ul>
    <li>first compilation-oriented IR subset stabilized</li>
    <li>first backend-family strategy defined</li>
    <li>backend contract family prepared</li>
    <li>known downstream backend demonstrated without collapsing FROG into it</li>
    <li>target-profile and deployment-mode assumptions made explicit where they materially affect backend consumption</li>
  </ul>
</ul>

<h3>M10 — First serious FROG IDE foundation</h3>

<ul>
  <li><strong>Status:</strong> [ ]</li>
  <li><strong>Meaning:</strong> FROG gains a real graphical authoring and debugging foundation rather than only static documents and early execution demos.</li>
  <li><strong>Main consequence:</strong> the project becomes materially more usable for real authoring, validation, inspection, and execution workflows.</li>
  <li><strong>To close:</strong></li>
  <ul>
    <li>Program Model stabilized</li>
    <li>diagram + interface + front-panel authoring supported</li>
    <li>validation feedback integrated</li>
    <li>debugging, probes, and watch surfaces established</li>
    <li>deployment selection can target different backend families, target profiles, and deployment modes without blurring their distinction</li>
  </ul>
</ul>

<h3>M11 — Expanded language breadth, profile depth, and deployment depth</h3>

<ul>
  <li><strong>Status:</strong> [ ]</li>
  <li><strong>Meaning:</strong> the project expands beyond the minimal serious base toward broader computation, stronger reuse, and more realistic deployment depth.</li>
  <li><strong>Main consequence:</strong> FROG becomes much closer to a genuinely useful industrial programming environment rather than a narrow proof surface.</li>
  <li><strong>To close:</strong></li>
  <ul>
    <li>broader primitive coverage</li>
    <li>stronger structure and memory semantics</li>
    <li>profile growth</li>
    <li>packaging and deployment preparation</li>
    <li>named target-profile families expanded where needed</li>
    <li>runtime-module strategies for development, debug, release, self-contained, and constrained deployment postures clarified without creating one monolithic universal runtime</li>
  </ul>
</ul>

<h3>M12 — Practical open industrial graphical ecosystem</h3>

<ul>
  <li><strong>Status:</strong> [ ]</li>
  <li><strong>Meaning:</strong> FROG becomes a credible open industrial graphical ecosystem with serious technical depth, explicit boundaries, and real implementation potential.</li>
  <li><strong>Main consequence:</strong> the project can credibly rival and surpass the historical proprietary model on both openness and technical structure.</li>
  <li><strong>To close:</strong></li>
  <ul>
    <li>serious IDE</li>
    <li>serious backend path</li>
    <li>clear conformance boundary</li>
    <li>usable governance / certification / branding layer</li>
    <li>credible industrial adoption path</li>
    <li>explicit separation between language, IDE, runtime, backend, deployment, and ecosystem participation remains durable at scale</li>
  </ul>
</ul>

<hr/>

<h2>Suggested near-term execution order</h2>

<pre>
1. correspondence closure
2. primitive baseline closure
3. type / value / state closure
4. execution-model and structure closure
5. source schema / validator closure
6. conformance growth
7. reference-path hardening
8. backend-contract preparation
9. target-profile and deployment-mode depth where it materially improves backend and deployment clarity
</pre>

<hr/>

<p align="center">
  <strong>Milestones guide the closure sequence.</strong><br/>
  They do not replace specification ownership.
</p>
