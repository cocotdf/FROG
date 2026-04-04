<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">🐸 FROG Strategy</h1>

<p align="center">
  Non-normative strategic framing layer for the long-term purpose, positioning, and ecosystem logic of FROG<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#why-this-directory-exists">1. Why this Directory Exists</a></li>
  <li><a href="#what-strategy-owns">2. What Strategy Owns</a></li>
  <li><a href="#what-strategy-does-not-own">3. What Strategy Does Not Own</a></li>
  <li><a href="#why-frog-needs-a-strategic-layer">4. Why FROG Needs a Strategic Layer</a></li>
  <li><a href="#frog-in-the-ai-era">5. FROG in the AI Era</a></li>
  <li><a href="#industrial-security-and-technological-sovereignty">6. Industrial Security and Technological Sovereignty</a></li>
  <li><a href="#relation-with-the-rest-of-the-repository">7. Relation with the Rest of the Repository</a></li>
  <li><a href="#current-strategic-entry-point">8. Current Strategic Entry Point</a></li>
  <li><a href="#strategic-boundaries-to-preserve">9. Strategic Boundaries to Preserve</a></li>
  <li><a href="#summary">10. Summary</a></li>
</ul>

<hr/>

<h2 id="why-this-directory-exists">1. Why this Directory Exists</h2>

<p>
This directory exists to hold the <strong>strategic framing layer</strong> of FROG.
It explains why the project matters, what category gap it targets, why that gap is important now, and what long-term ecosystem consequences would follow if FROG succeeds.
</p>

<p>
This layer is intentionally <strong>non-normative</strong>.
It does not define language truth.
It does not define source validity.
It does not define execution semantics.
It does not define IR derivation rules.
</p>

<p>
Its purpose is to make the larger logic of the project explicit:
why an open graphical language matters,
why the repository is structured the way it is,
why the project should be understood as more than a local tooling exercise,
and why the category itself needs to change.
</p>

<hr/>

<h2 id="what-strategy-owns">2. What Strategy Owns</h2>

<p>
The Strategy layer owns repository-visible documents whose role is to explain:
</p>

<ul>
  <li>the strategic problem FROG addresses,</li>
  <li>the ecosystem gap FROG targets,</li>
  <li>the expected impact of success,</li>
  <li>the relevance of openness, inspectability, and portability,</li>
  <li>the long-term industrial and technological significance of the project,</li>
  <li>the framing used for external explanation, funding logic, ecosystem communication, or mission-level positioning.</li>
</ul>

<p>
This is the layer where FROG can explain not only <strong>what it is</strong>, but also <strong>why it matters</strong>.
</p>

<hr/>

<h2 id="what-strategy-does-not-own">3. What Strategy Does Not Own</h2>

<p>
The Strategy layer does <strong>not</strong> own:
</p>

<ul>
  <li>canonical source representation,</li>
  <li>source-shape/schema posture,</li>
  <li>structural validity,</li>
  <li>validated language meaning,</li>
  <li>intrinsic primitive behavior,</li>
  <li>profile-owned capability behavior,</li>
  <li>canonical execution-facing IR definition,</li>
  <li>lowering rules,</li>
  <li>backend contract rules,</li>
  <li>conformance expectations,</li>
  <li>reference implementation behavior,</li>
  <li>roadmap sequencing.</li>
</ul>

<p>
Those ownership boundaries remain elsewhere in the repository:
</p>

<pre>
Expression/                 -> canonical source and structural validity
Language/                   -> validated program meaning
Libraries/                  -> intrinsic primitive surface
Profiles/                   -> optional standardized capability families
IR/                         -> canonical open execution-facing representation
Conformance/                -> public accept / reject / preserve expectations
Implementations/Reference/  -> non-normative executable workspace
Roadmap/                    -> sequencing and closure order
</pre>

<p>
Strategy may explain why those layers matter,
but it must not silently replace them.
</p>

<hr/>

<h2 id="why-frog-needs-a-strategic-layer">4. Why FROG Needs a Strategic Layer</h2>

<p>
FROG is not merely a technical document set.
It is an attempt to open a category that has historically remained fragmented, opaque, and too tightly coupled to proprietary execution ecosystems.
</p>

<p>
A strategic layer is therefore needed because the project has to explain more than local technical design choices.
It has to explain:
</p>

<ul>
  <li>why open graphical programming matters,</li>
  <li>why graphical system programming should not remain vendor-bound by default,</li>
  <li>why inspectable source and inspectable execution-facing artifacts matter,</li>
  <li>why the repository is built as a layered language stack rather than as one monolithic product,</li>
  <li>why the ecosystem significance of FROG is larger than one implementation.</li>
</ul>

<p>
Without this strategic framing, the repository could be misread as:
</p>

<ul>
  <li>just another graphical editor idea,</li>
  <li>just a runtime experiment,</li>
  <li>just an implementation workspace,</li>
  <li>just a niche format proposal.</li>
</ul>

<p>
That would be an incomplete reading.
FROG is trying to establish an open language basis for graphical system programming that can support future validators, IDEs, runtimes, compilers, profiles, conformance growth, and industrial ecosystem participation.
</p>

<hr/>

<h2 id="frog-in-the-ai-era">5. FROG in the AI Era</h2>

<p>
FROG matters even more in the AI era than it would have in a purely manual-programming era.
</p>

<p>
Software artifacts are increasingly:
</p>

<ul>
  <li>generated,</li>
  <li>rewritten,</li>
  <li>transformed,</li>
  <li>assisted,</li>
  <li>refactored,</li>
  <li>explained,</li>
  <li>reviewed,</li>
  <li>validated</li>
</ul>

<p>
through AI-assisted tooling or AI-adjacent pipelines.
</p>

<p>
That changes the strategic value of representation.
A serious language infrastructure now needs to be:
</p>

<ul>
  <li>structured enough for machine generation and transformation,</li>
  <li>explicit enough for human review,</li>
  <li>open enough for independent tooling,</li>
  <li>layered enough to preserve meaning across derivation and backend handoff.</li>
</ul>

<p>
FROG is well aligned with that requirement because:
</p>

<ul>
  <li>the canonical <code>.frog</code> source is structured JSON,</li>
  <li>the primary program structure is graphically reviewable,</li>
  <li>the execution-facing IR remains open and inspectable,</li>
  <li>the backend/compiler path remains downstream rather than becoming hidden language truth.</li>
</ul>

<p>
This does not mean that textual languages cannot be audited.
It means that FROG is designed to make structural review more direct by keeping the executable graph explicit across the language stack.
</p>

<p>
That is a strategic advantage, not just a cosmetic one.
It reduces the auditability gap between:
</p>

<ul>
  <li>what was generated,</li>
  <li>what was saved,</li>
  <li>what was validated,</li>
  <li>what was derived,</li>
  <li>what is handed downstream.</li>
</ul>

<hr/>

<h2 id="industrial-security-and-technological-sovereignty">6. Industrial Security and Technological Sovereignty</h2>

<p>
FROG is also strategically relevant because industrial systems increasingly depend on software that must remain:
</p>

<ul>
  <li>reviewable,</li>
  <li>portable,</li>
  <li>traceable,</li>
  <li>durable,</li>
  <li>vendor-independent enough to remain governable over time.</li>
</ul>

<p>
That matters for industrial security.
Critical logic should not have to disappear into opaque saved formats, opaque private execution layers, or one vendor-defined tooling stack in order to remain usable.
</p>

<p>
That also matters for technological sovereignty.
A language ecosystem is more sovereign when:
</p>

<ul>
  <li>the source representation is open,</li>
  <li>the execution-facing representation remains inspectable,</li>
  <li>multiple actors can implement compatible tooling,</li>
  <li>compiler, runtime, IDE, and backend paths are not collapsed into one private authority.</li>
</ul>

<p>
FROG therefore has strategic significance beyond developer ergonomics.
It can support an open, inspectable, and portable programming foundation for industrial and strategic software ecosystems.
</p>

<hr/>

<h2 id="relation-with-the-rest-of-the-repository">7. Relation with the Rest of the Repository</h2>

<p>
The Strategy layer should be read together with, but distinctly from, the other repository layers.
</p>

<pre>
Readme.md                   -> repository-wide architectural entry point
Strategy/                   -> why the project matters
Roadmap/                    -> in what order closure should happen
Expression/                 -> what is saved and structurally valid
Language/                   -> what validated programs mean
IR/                         -> what validated meaning becomes in execution-facing form
Conformance/                -> what should be accepted, rejected, and preserved
Implementations/Reference/  -> how a bounded subset is currently exercised
</pre>

<p>
This separation matters because FROG needs:
</p>

<ul>
  <li>architecture,</li>
  <li>strategy,</li>
  <li>roadmap,</li>
  <li>conformance,</li>
  <li>reference proof</li>
</ul>

<p>
without allowing any one of those layers to silently replace the others.
</p>

<hr/>

<h2 id="current-strategic-entry-point">8. Current Strategic Entry Point</h2>

<p>
At the current published repository state, the main strategic framing document is:
</p>

<pre><code>Strategy/Heilmeier/Readme.md</code></pre>

<p>
That document explains the technological purpose, gap, expected impact, and long-term program logic of FROG in a structured mission-oriented form.
</p>

<p>
The role of this directory-level <code>Readme.md</code> is different.
It serves as the strategic entry point for the <code>Strategy/</code> layer as a whole and clarifies how strategic framing should coexist with the normative specification and the roadmap.
</p>

<hr/>

<h2 id="strategic-boundaries-to-preserve">9. Strategic Boundaries to Preserve</h2>

<p>
The Strategy layer should preserve the following distinctions:
</p>

<ul>
  <li>strategy vs normative specification,</li>
  <li>strategy vs roadmap sequencing,</li>
  <li>strategic motivation vs semantic ownership,</li>
  <li>AI compatibility vs AI dependence,</li>
  <li>auditability improvement vs exaggerated security claims,</li>
  <li>open language vs one implementation,</li>
  <li>technological sovereignty vs branding control.</li>
</ul>

<p>
In particular:
</p>

<ul>
  <li>FROG should not claim that graphical form automatically guarantees security,</li>
  <li>FROG should not claim that textual languages cannot be reviewed,</li>
  <li>FROG should claim, more narrowly and more credibly, that its architecture reduces opacity by combining structured source, explicit graph reviewability, and inspectable execution-facing representation.</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The <code>Strategy/</code> layer exists to explain why FROG matters as a long-term technological program.
</p>

<p>
Its role is to make explicit that FROG is not only:
</p>

<ul>
  <li>an open graphical language,</li>
  <li>a dataflow architecture,</li>
  <li>a compiler/runtime preparation effort.</li>
</ul>

<p>
It is also:
</p>

<ul>
  <li>a response to opaque graphical ecosystems,</li>
  <li>a response to AI-era auditability needs,</li>
  <li>a response to industrial reviewability requirements,</li>
  <li>a response to technological sovereignty concerns in strategic software systems.</li>
</ul>

<p>
That is why the Strategy layer exists, and why it must remain explicit, non-normative, and clearly separated from both the specification layers and the roadmap.
</p>
