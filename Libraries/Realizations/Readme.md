<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Realizations</h1>

<p align="center">
  <strong>Normative baseline for official realization families of intrinsic standardized widget classes</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-directory-exists">2. Why this Directory Exists</a></li>
  <li><a href="#scope">3. Scope</a></li>
  <li><a href="#architectural-position">4. Architectural Position</a></li>
  <li><a href="#ownership-boundary">5. Ownership Boundary</a></li>
  <li><a href="#what-a-standard-realization-family-is">6. What a Standard Realization Family Is</a></li>
  <li><a href="#current-standard-family">7. Current Standard Family</a></li>
  <li><a href="#relationship-with-widgets">8. Relationship with Standard Widget Classes</a></li>
  <li><a href="#relationship-with-wfrog-and-assets">9. Relationship with <code>.wfrog</code> and Assets</a></li>
  <li><a href="#state-and-resource-mapping">10. State and Resource Mapping</a></li>
  <li><a href="#portability">11. Portability</a></li>
  <li><a href="#status">12. Status</a></li>
  <li><a href="#summary">13. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the first official realization families for the intrinsic standardized widget classes of FROG.
</p>

<p>
A realization family specifies how already-published widget classes may be embodied visually and interactively while remaining subordinate to class law, bounded behavior law, and the source-level widget model.
</p>

<p>
A realization family is not the owner of widget semantics.
It is the official publication surface for:
</p>

<ul>
  <li>state-oriented visual posture,</li>
  <li>part-to-visual mapping,</li>
  <li>layout posture inside a class realization,</li>
  <li>recommended resource organization,</li>
  <li>host-facing realization expectations.</li>
</ul>

<hr/>

<h2 id="why-this-directory-exists">2. Why this Directory Exists</h2>

<p>
Once standard widget classes exist, the next architectural need is to define how an official realization family may embody them without collapsing semantics into skins or into one runtime-private toolkit mapping.
</p>

<p>
Without a realization layer:
</p>

<ul>
  <li>the standard widget baseline remains too abstract for serious front-panel publication,</li>
  <li>each runtime is tempted to invent its own de facto visual standard,</li>
  <li>SVG and host assets drift toward semantic ownership,</li>
  <li>state-specific skins become ad hoc rather than structured.</li>
</ul>

<p>
This directory exists to prevent that drift.
</p>

<hr/>

<h2 id="scope">3. Scope</h2>

<p>
This directory defines:
</p>

<ul>
  <li>official realization families for standard widgets,</li>
  <li>their state posture,</li>
  <li>their part-to-visual posture,</li>
  <li>their resource-organization posture,</li>
  <li>their host-facing realization expectations.</li>
</ul>

<p>
This directory does not define:
</p>

<ul>
  <li>widget class identity,</li>
  <li>widget properties, methods, events, or parts as public law,</li>
  <li>the generic realization doctrine of the language,</li>
  <li>the generic <code>.wfrog</code> package format,</li>
  <li>one mandatory toolkit-specific implementation.</li>
</ul>

<hr/>

<h2 id="architectural-position">4. Architectural Position</h2>

<p>
The standard realization layer occupies the following position:
</p>

<pre><code>Libraries/Widgets/      -&gt; intrinsic standardized class law baseline
Libraries/Realizations/ -&gt; official realization families for those classes
Expression/             -&gt; source model and generic realization boundary
.wfrog publication      -&gt; machine-readable publication of realization artifacts
Implementations/        -&gt; runtime and host execution of realization families
</code></pre>

<p>
This means:
</p>

<ul>
  <li>class identity is upstream from realization,</li>
  <li>realization is upstream from host-private rendering details,</li>
  <li>runtime-private implementation remains downstream from published realization posture.</li>
</ul>

<hr/>

<h2 id="ownership-boundary">5. Ownership Boundary</h2>

<p>
The following ownership boundary is normative:
</p>

<ul>
  <li><strong><code>Libraries/Widgets/</code></strong> owns which standard classes exist.</li>
  <li><strong><code>Libraries/Realizations/</code></strong> owns official realization-family posture for those classes.</li>
  <li><strong><code>Expression/Widget realization.md</code></strong> owns the generic realization doctrine.</li>
  <li><strong><code>Expression/Widget package (.wfrog).md</code></strong> owns the widget-oriented publication format.</li>
  <li><strong>SVG and other visual assets</strong> remain resources, not semantic truth.</li>
</ul>

<p>
Therefore:
</p>

<ul>
  <li>a realization family MUST NOT invent public widget semantics,</li>
  <li>a realization family MUST NOT redefine class identity,</li>
  <li>a realization family MAY define visual states, state-to-resource mappings, and part bindings,</li>
  <li>a runtime MAY realize the same family differently internally while preserving its published posture.</li>
</ul>

<hr/>

<h2 id="what-a-standard-realization-family-is">6. What a Standard Realization Family Is</h2>

<p>
A standard realization family is an official published realization posture associated with one or more standard widget classes.
</p>

<p>
A realization family SHOULD define:
</p>

<ul>
  <li>family identity,</li>
  <li>target widget classes,</li>
  <li>state inventory,</li>
  <li>part-to-visual mapping posture,</li>
  <li>resource naming posture,</li>
  <li>host-facing realization expectations,</li>
  <li>fallback posture when a resource or host feature is unavailable.</li>
</ul>

<p>
A realization family is allowed to have multiple state-specific assets for the same widget or widget part.
That does not make the asset the source of semantic truth.
It only makes the realization explicit and inspectable.
</p>

<hr/>

<h2 id="current-standard-family">7. Current Standard Family</h2>

<p>
The first official realization family published here is:
</p>

<ul>
  <li><code>Default/</code> — the default standard realization family for the intrinsic widget baseline.</li>
</ul>

<p>
This family exists to provide:
</p>

<ul>
  <li>a first coherent official embodiment of the standard widget baseline,</li>
  <li>a stable reference target for examples,</li>
  <li>a concrete realization posture that runtimes may interpret faithfully or approximate compatibly.</li>
</ul>

<hr/>

<h2 id="relationship-with-widgets">8. Relationship with Standard Widget Classes</h2>

<p>
Every realization family document in this directory is downstream from one or more standard widget class documents in <code>Libraries/Widgets/</code>.
</p>

<p>
This means:
</p>

<ul>
  <li>the widget class defines which parts and states matter semantically,</li>
  <li>the realization family defines how those parts and states are embodied visually,</li>
  <li>the runtime interprets the resulting realization posture without becoming its semantic owner.</li>
</ul>

<hr/>

<h2 id="relationship-with-wfrog-and-assets">9. Relationship with <code>.wfrog</code> and Assets</h2>

<p>
This directory defines the normative documentation posture of realization families.
</p>

<p>
Machine-readable publication may later be carried through:
</p>

<ul>
  <li><code>.wfrog</code> realization libraries,</li>
  <li>resource manifests,</li>
  <li>SVG and other visual assets,</li>
  <li>part-binding maps,</li>
  <li>state-to-resource maps.</li>
</ul>

<p>
The governing rule remains:
</p>

<pre><code>published class law
    !=
published realization family
    !=
machine-readable realization package
    !=
visual asset
    !=
runtime-private rendering implementation
</code></pre>

<hr/>

<h2 id="state-and-resource-mapping">10. State and Resource Mapping</h2>

<p>
A realization family MAY define:
</p>

<ul>
  <li>widget-level states such as <code>normal</code>, <code>disabled</code>, <code>focused</code>, or <code>pressed</code>,</li>
  <li>part-level states such as <code>increment_button.pressed</code>,</li>
  <li>resource maps that assign state-specific assets to widget parts,</li>
  <li>fallback rules when a specialized state resource is unavailable.</li>
</ul>

<p>
This layer is the correct place for multiple SVG skins or state-specific SVG fragments.
It is not the correct place to redefine widget law.
</p>

<hr/>

<h2 id="portability">11. Portability</h2>

<p>
A standard realization family is portable if:
</p>

<ul>
  <li>its target class law remains preserved,</li>
  <li>its parts remain recognizable,</li>
  <li>its published state posture remains preserved,</li>
  <li>its host-specific substitutions do not change the public interaction meaning.</li>
</ul>

<p>
Pixel-identical rendering is not required.
Semantic and realization-structure compatibility is required.
</p>

<hr/>

<h2 id="status">12. Status</h2>

<p>
This directory defines the official realization-family layer for the intrinsic standard widget baseline.
</p>

<p>
Its closure direction is:
</p>

<ul>
  <li>explicit official realization families,</li>
  <li>clean separation between class law and skin resources,</li>
  <li>state-structured resource publication,</li>
  <li>multi-runtime realizability without semantic drift.</li>
</ul>

<hr/>

<h2 id="summary">13. Summary</h2>

<p>
This directory defines how official realization families may embody the intrinsic standard widget classes of FROG.
</p>

<p>
In short:
</p>

<ul>
  <li><code>Libraries/Widgets/</code> defines what the widget is,</li>
  <li><code>Libraries/Realizations/</code> defines how an official standard family embodies it,</li>
  <li>assets and <code>.wfrog</code> publication may later materialize that family,</li>
  <li>runtimes interpret the family without becoming the owner of its meaning.</li>
</ul>
