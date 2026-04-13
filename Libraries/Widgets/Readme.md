<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Widgets</h1>

<p align="center">
  <strong>Normative baseline of intrinsic standardized widget classes for portable front-panel ecosystems</strong><br/>
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
  <li><a href="#what-a-standard-widget-class-is">6. What a Standard Widget Class Is</a></li>
  <li><a href="#minimum-object-surface-rule">7. Minimum Object-Surface Rule</a></li>
  <li><a href="#baseline-widget-families">8. Baseline Widget Families</a></li>
  <li><a href="#baseline-standardization-phases">9. Baseline Standardization Phases</a></li>
  <li><a href="#shared-baseline-conventions">10. Shared Baseline Conventions</a></li>
  <li><a href="#primitive-vs-composite-posture">11. Primitive vs Composite Posture</a></li>
  <li><a href="#relation-with-frog-source">12. Relation with <code>.frog</code> Source</a></li>
  <li><a href="#relation-with-wfrog-publication">13. Relation with <code>.wfrog</code> Publication</a></li>
  <li><a href="#relation-with-frogui-primitives">14. Relation with <code>frog.ui.*</code> Primitives</a></li>
  <li><a href="#relation-with-realization-families">15. Relation with Realization Families</a></li>
  <li><a href="#portability-across-runtimes">16. Portability Across Runtimes</a></li>
  <li><a href="#conformance-posture">17. Conformance Posture</a></li>
  <li><a href="#status">18. Status</a></li>
  <li><a href="#summary">19. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the intrinsic standardized widget baseline of FROG.
</p>

<p>
Its role is to publish a small, portable, inspectable set of standard widget classes that can be reused across FROG programs, runtimes, IDEs, and realization families without forcing one private runtime implementation to become the definition of the widget system.
</p>

<p>
This baseline is intentionally modest but concrete.
It defines the first standard widget families that are sufficient to support a credible front-panel ecosystem and a first serious executable vertical slice.
</p>

<p>
The standard widget baseline does not replace the general widget architecture defined elsewhere.
Instead, it instantiates that architecture through a first published set of reusable classes with explicit public object surfaces.
</p>

<hr/>

<h2 id="why-this-directory-exists">2. Why this Directory Exists</h2>

<p>
The widget corridor is only credible if FROG can answer two different questions cleanly:
</p>

<ul>
  <li>How does the language represent widgets, widget interaction, widget class law, widget behavior, widget realization, and widget package publication?</li>
  <li>Which standard widget classes actually exist as a reusable baseline for portable programs?</li>
</ul>

<p>
The first question belongs to <code>Expression/</code> and the surrounding architecture documents.
This directory exists to answer the second question.
</p>

<p>
Without a standard widget baseline:
</p>

<ul>
  <li>every runtime would be tempted to invent its own de facto standard widgets,</li>
  <li>examples would become less portable,</li>
  <li>the front-panel corridor would remain too abstract,</li>
  <li>developer-defined widgets would have no stable standard foundation to build on.</li>
</ul>

<p>
This directory therefore publishes the first standardized reusable widget classes on top of the already-defined widget architecture.
</p>

<hr/>

<h2 id="scope">3. Scope</h2>

<p>
This directory defines:
</p>

<ul>
  <li>the first intrinsic standardized widget classes of FROG,</li>
  <li>their class identity and category,</li>
  <li>their primary value posture where applicable,</li>
  <li>their standard properties, methods, events, and parts,</li>
  <li>their minimal intrinsic behavior expectations,</li>
  <li>their minimal realization expectations,</li>
  <li>their diagram-interaction posture.</li>
</ul>

<p>
This directory does not define:
</p>

<ul>
  <li>canonical <code>.frog</code> source serialization,</li>
  <li>front-panel composition structure,</li>
  <li>the full generic widget class contract model,</li>
  <li>the full <code>.wfrog</code> package format,</li>
  <li>the general bounded behavior doctrine,</li>
  <li>the general realization doctrine,</li>
  <li>one mandatory host toolkit or one mandatory runtime architecture.</li>
</ul>

<p>
Those ownerships remain defined elsewhere in the repository.
This directory publishes standard reusable widget classes inside those already-established boundaries.
</p>

<hr/>

<h2 id="architectural-position">4. Architectural Position</h2>

<p>
The standardized widget baseline occupies the following architectural position:
</p>

<pre><code>Expression/                 - widget source model and widget architecture
Libraries/Widgets/          - intrinsic standardized widget classes
Libraries/UI.md             - intrinsic executable UI interaction primitives
Libraries/Realizations/     - official realization families for standardized classes
.wfrog publication          - machine-readable publication of widget and realization artifacts
Implementations/            - runtime families and host realization
</code></pre>

<p>
This separation is intentional:
</p>

<pre><code>frog.widgets.*   - class identities and public class surfaces
frog.ui.*        - executable interaction primitives
realization      - official embodiment posture for published classes
</code></pre>

<p>
The standardized widget layer is therefore upstream from realization families and upstream from runtime-private embodiment details.
</p>

<hr/>

<h2 id="ownership-boundary">5. Ownership Boundary</h2>

<p>
The following ownership boundary is normative:
</p>

<ul>
  <li><code>Expression/Widget.md</code> owns widget instances in canonical source.</li>
  <li><code>Expression/Widget class contract.md</code> owns the general class-law model.</li>
  <li><code>Expression/Widget behavior.md</code> owns the bounded behavior doctrine.</li>
  <li><code>Expression/Widget realization.md</code> owns the generic realization doctrine.</li>
  <li><code>Expression/Widget package (.wfrog).md</code> owns widget-oriented package publication format.</li>
  <li><code>Libraries/UI.md</code> owns executable widget interaction primitives.</li>
  <li><code>Libraries/Widgets/</code> owns the intrinsic standardized baseline widget classes themselves.</li>
  <li><code>Libraries/Realizations/</code> owns official realization-family posture for those classes.</li>
</ul>

<p>
Therefore:
</p>

<ul>
  <li>this directory defines which standard classes exist,</li>
  <li>this directory defines the portable public surface of those classes,</li>
  <li>it does not redefine the generic widget architecture,</li>
  <li>it does not replace <code>.wfrog</code> as the widget-oriented publication family,</li>
  <li>it does not make one runtime the owner of the class law,</li>
  <li>it does not delegate public class meaning to realization assets.</li>
</ul>

<hr/>

<h2 id="what-a-standard-widget-class-is">6. What a Standard Widget Class Is</h2>

<p>
A standard widget class in this directory is a reusable, portable, intrinsic class published as part of the FROG baseline.
</p>

<p>
A standard class defines, at minimum:
</p>

<ul>
  <li>a stable <code>class_id</code>,</li>
  <li>a category and role posture,</li>
  <li>a primary value posture where applicable,</li>
  <li>a stable public property inventory,</li>
  <li>a stable public method inventory,</li>
  <li>a stable public event inventory,</li>
  <li>a stable public part model,</li>
  <li>minimal behavior expectations,</li>
  <li>minimal realization expectations.</li>
</ul>

<p>
A standard class is therefore more than an abstract name and more than a visual control template.
It is a published portable object surface that runtimes may implement and programs may rely on.
</p>

<p>
That public surface may include semantic label-bearing or value-bearing members such as <code>label.text</code>, <code>value</code>, <code>value_display</code>, <code>text_display</code>, or chart-related public surfaces when the class requires them.
However, the existence of such members does not mean that realization-side placement, styling defaults, anchors, text regions, or decorative assets become part of the intrinsic class law unless explicitly published here.
</p>

<p>
The standard widget class therefore owns:
</p>

<ul>
  <li>what public members exist,</li>
  <li>what those members mean,</li>
  <li>which methods and events are legal,</li>
  <li>which public parts are stable realization targets.</li>
</ul>

<p>
Downstream realization publication owns:
</p>

<ul>
  <li>where dynamic public surfaces are placed,</li>
  <li>how visual states are embodied,</li>
  <li>which anchors, text regions, or resource layers are used,</li>
  <li>which assets or host-native layers provide the embodiment.</li>
</ul>

<hr/>

<h2 id="minimum-object-surface-rule">7. Minimum Object-Surface Rule</h2>

<p>
The intrinsic widget baseline follows a strict minimum object-surface rule.
</p>

<p>
A standard widget in the intrinsic baseline must not collapse into a passive value plus a runtime-private visual shell.
Instead, each intrinsic baseline widget is expected to expose a minimal but real public object surface.
</p>

<p>
At minimum, this means:
</p>

<ul>
  <li>a meaningful public property surface,</li>
  <li>a meaningful public method surface when the class is interactive, stateful, or structurally significant,</li>
  <li>a meaningful public event surface when the class produces observable interaction or visible update,</li>
  <li>a stable public part model for realization targeting.</li>
</ul>

<p>
This rule is intentionally close in spirit to mature graphical object systems such as LabVIEW:
the intrinsic baseline remains small, but standard widgets still have a real minimum of property-node, method-node, and event-observation usefulness.
</p>

<p>
At the same time, this rule does not justify overloading the intrinsic core with every possible surface.
The baseline remains minimal, disciplined, and portable.
</p>

<hr/>

<h2 id="baseline-widget-families">8. Baseline Widget Families</h2>

<p>
The initial intrinsic standardized baseline is organized into the following families:
</p>

<ul>
  <li><code>Numeric.md</code> — numeric control and numeric indicator</li>
  <li><code>Boolean.md</code> — boolean control and boolean indicator</li>
  <li><code>String.md</code> — string control and string indicator</li>
  <li><code>Button.md</code> — push button</li>
  <li><code>Chart.md</code> — minimal waveform chart baseline</li>
</ul>

<p>
These families intentionally form a small but credible front-panel core:
</p>

<ul>
  <li>typed editable values,</li>
  <li>typed displayed values,</li>
  <li>basic command interaction,</li>
  <li>a first structured visual history widget.</li>
</ul>

<p>
The chart strategy is intentionally conservative:
the intrinsic core standardizes one minimal waveform-chart-style baseline rather than trying to standardize, all at once, the full family of waveform graph, XY graph, intensity graph, legend, cursor, and annotation systems.
</p>

<hr/>

<h2 id="baseline-standardization-phases">9. Baseline Standardization Phases</h2>

<p>
The intrinsic widget baseline should remain intentionally phased.
This helps preserve a credible v1 core while keeping the path open for later expansion.
</p>

<h3>9.1 Intrinsic baseline v1</h3>

<p>
The recommended intrinsic baseline v1 consists of:
</p>

<ul>
  <li><code>frog.widgets.numeric_control</code></li>
  <li><code>frog.widgets.numeric_indicator</code></li>
  <li><code>frog.widgets.boolean_control</code></li>
  <li><code>frog.widgets.boolean_indicator</code></li>
  <li><code>frog.widgets.string_control</code></li>
  <li><code>frog.widgets.string_indicator</code></li>
  <li><code>frog.widgets.button</code></li>
  <li><code>frog.widgets.waveform_chart</code></li>
</ul>

<p>
This v1 core is the smallest serious portable widget set that still supports:
</p>

<ul>
  <li>scalar editable values,</li>
  <li>scalar displayed values,</li>
  <li>command-oriented interaction,</li>
  <li>a first bounded history-oriented visualization surface.</li>
</ul>

<h3>9.2 Standardized support widgets outside intrinsic baseline v1</h3>

<p>
The following support widgets may be standardized and fully documented without being treated as part of the intrinsic baseline v1 core:
</p>

<ul>
  <li><code>frog.widgets.label</code></li>
  <li><code>frog.widgets.frame</code></li>
</ul>

<p>
This posture is intentional.
It allows support widgets to exist as real standardized classes with disciplined public contracts while keeping the intrinsic v1 core small and centered on the most essential reusable value, command, and chart surfaces.
</p>

<h3>9.3 Near-core standardized candidates</h3>

<p>
The following classes are strong near-core candidates, but do not need to enter the intrinsic baseline before the core above is fully stabilized:
</p>

<ul>
  <li>enum</li>
  <li>path</li>
  <li>cluster</li>
  <li>array</li>
</ul>

<h3>9.4 Deferred standardization</h3>

<p>
The following families should generally be deferred until after the intrinsic v1 core is stabilized:
</p>

<ul>
  <li>listbox</li>
  <li>switch</li>
  <li>table</li>
  <li>tree</li>
  <li>tab</li>
  <li>waveform graph</li>
  <li>XY graph</li>
  <li>intensity graph</li>
  <li>picture-rich or canvas-like widget families</li>
</ul>

<p>
This phased posture is not a rejection of those classes.
It is a discipline rule intended to keep the intrinsic baseline coherent.
</p>

<p>
In particular, a class such as <code>switch</code> should not be introduced merely because one realization family supports a switch-like visual embodiment.
A distinct class should only be standardized when it contributes distinct public semantics rather than only a different visible embodiment.
</p>

<hr/>

<h2 id="shared-baseline-conventions">10. Shared Baseline Conventions</h2>

<p>
The baseline families in this directory follow a shared normalization posture.
</p>

<p>
At minimum:
</p>

<ul>
  <li>standard class identifiers use the <code>frog.widgets.*</code> namespace,</li>
  <li>value-carrying classes expose a primary value mirrored as property <code>value</code>,</li>
  <li>label-bearing classes use property <code>label.text</code> where label-bearing posture is part of public class meaning,</li>
  <li>visibility uses property <code>interaction.visible</code>,</li>
  <li>interactive classes use property <code>interaction.enabled</code> where applicable,</li>
  <li>the root part is named <code>root</code>,</li>
  <li>the outer framing part, when present, is named <code>frame</code>,</li>
  <li>controls typically emit <code>value_changed</code> for primary value mutation,</li>
  <li>indicators typically emit <code>value_rendered</code> for visible refresh-oriented notification.</li>
</ul>

<p>
This normalization keeps the baseline coherent while leaving room for richer families and richer realization-specific surfaces later.
</p>

<p>
The baseline deliberately avoids pushing realization-heavy appearance structure into every class.
Portable semantic surfaces may still be standardized when they belong to public class meaning, but realization-specific anchors, text regions, skin layers, placement maps, and most visual-theme machinery belong downstream in realization publication.
</p>

<hr/>

<h2 id="primitive-vs-composite-posture">11. Primitive vs Composite Posture</h2>

<p>
The classes defined in this directory are the initial standardized primitive baseline.
</p>

<p>
They are intended to serve as:
</p>

<ul>
  <li>a portable reusable widget core,</li>
  <li>a foundation for serious examples,</li>
  <li>a foundation for future standardized or developer-defined composite widgets.</li>
</ul>

<p>
Composite widgets are expected to be published through the widget package corridor and to remain compatible with the standard primitive classes defined here.
This means the primitive baseline should remain small, clear, and stable rather than absorbing every higher-level interaction pattern into the intrinsic core.
</p>

<hr/>

<h2 id="relation-with-frog-source">12. Relation with <code>.frog</code> Source</h2>

<p>
Canonical <code>.frog</code> source instantiates widgets through widget instances in <code>front_panel</code>.
Those widget instances may reference the standard classes defined in this directory.
</p>

<p>
For example, a widget instance may declare a class reference such as:
</p>

<pre><code>frog.widgets.numeric_control
frog.widgets.boolean_indicator
frog.widgets.string_control
frog.widgets.button
frog.widgets.waveform_chart
</code></pre>

<p>
This directory does not define the instance serialization itself.
It defines the published classes that such instances may target.
</p>

<p>
Canonical source owns the instance.
This directory owns the standardized class being instantiated.
</p>

<hr/>

<h2 id="relation-with-wfrog-publication">13. Relation with <code>.wfrog</code> Publication</h2>

<p>
The classes defined in this directory are intrinsic standardized classes.
They may be published, mirrored, or accompanied by official widget-oriented package artifacts through the <code>.wfrog</code> corridor.
</p>

<p>
That means:
</p>

<ul>
  <li>this directory defines the normative class baseline,</li>
  <li><code>.wfrog</code> provides the machine-readable widget-oriented publication family,</li>
  <li>realization resources, realization mappings, bounded composite publication, and related artifacts may be published through <code>.wfrog</code> artifacts associated with these classes.</li>
</ul>

<p>
The governing distinction remains:
</p>

<pre><code>published class law
    !=
widget-oriented package publication
    !=
realization-family publication
    !=
visual asset
    !=
runtime-private implementation
</code></pre>

<hr/>

<h2 id="relation-with-frogui-primitives">14. Relation with <code>frog.ui.*</code> Primitives</h2>

<p>
The executable object-style interaction surface for widgets is defined by <code>frog.ui.*</code> primitives.
Those primitives operate on widget classes defined by this directory and on compatible developer-defined classes published elsewhere.
</p>

<p>
This means:
</p>

<ul>
  <li><code>Libraries/Widgets/</code> defines which standard widget classes exist and what public surfaces they expose,</li>
  <li><code>Libraries/UI.md</code> defines how executable diagrams may read properties, write properties, invoke methods, and observe events on those classes when allowed.</li>
</ul>

<pre><code>class law
    - what exists

frog.ui.*
    - how execution accesses what exists
</code></pre>

<p>
This distinction is especially important for members such as <code>value</code>.
A class may expose <code>value</code> as a legal public property, while the execution layer still preserves the distinction between:
</p>

<ul>
  <li>natural <code>widget_value</code> participation,</li>
  <li>object-style property access to member <code>value</code> through <code>frog.ui.property_read</code> or <code>frog.ui.property_write</code>.</li>
</ul>

<p>
Likewise, if a class exposes members such as <code>label.text</code>, axis properties, history members, or methods such as <code>append_sample(sample)</code> or <code>clear_history()</code>, this directory owns their legality and meaning, while <code>frog.ui.*</code> owns the executable primitive vocabulary used to access them.
</p>

<hr/>

<h2 id="relation-with-realization-families">15. Relation with Realization Families</h2>

<p>
The classes defined here are not identical to one skin and are not identical to one realization resource family.
</p>

<p>
A standard widget class may later be accompanied by:
</p>

<ul>
  <li>one or more official realization families,</li>
  <li>one or more machine-readable realization packages,</li>
  <li>state-sensitive resource maps,</li>
  <li>structural part bindings,</li>
  <li>anchor or text-region publication for dynamic public parts.</li>
</ul>

<p>
Those realization layers remain subordinate to the class law.
</p>

<p>
For example:
</p>

<ul>
  <li>a button may expose semantic label text through <code>label.text</code>,</li>
  <li>a numeric widget may expose a dynamic <code>value_display</code> surface,</li>
  <li>a string widget may expose a dynamic <code>text_display</code> surface,</li>
  <li>a chart may expose <code>plot_area</code>, axis surfaces, and <code>label.text</code>,</li>
  <li>the corresponding realization family may publish where those surfaces are placed or how they are visually embodied,</li>
  <li>an associated asset may provide geometry, decoration, anchor support, or text-region support,</li>
  <li>a runtime may render the final result through its own host toolkit.</li>
</ul>

<p>
But the existence of those realization layers does not mean that the realization owns the semantics of the class.
The class remains primary.
The realization remains subordinate.
</p>

<p>
A realization family may also publish several compatible embodiment variants for the same class.
That does not, by itself, create several classes.
A distinct standardized class should only appear when a distinct public contract is explicitly published.
</p>

<hr/>

<h2 id="portability-across-runtimes">16. Portability Across Runtimes</h2>

<p>
The standard classes defined here are intended to be portable across runtime families such as Python, Rust, and C/C++ implementations.
</p>

<p>
Portability does not require:
</p>

<ul>
  <li>identical host toolkit choice,</li>
  <li>identical rendering internals,</li>
  <li>identical pixel output in every case.</li>
</ul>

<p>
Portability does require:
</p>

<ul>
  <li>stable class identity,</li>
  <li>stable public properties, methods, events, and parts,</li>
  <li>stable primary value posture,</li>
  <li>stable behavior meaning,</li>
  <li>stable diagram-interaction meaning.</li>
</ul>

<p>
Where a class exposes semantic text-bearing or value-bearing public surfaces, portability also requires that runtimes preserve their public meaning even if the visual embodiment differs.
</p>

<hr/>

<h2 id="conformance-posture">17. Conformance Posture</h2>

<p>
A runtime claiming support for one of the standard classes defined here MUST preserve the published portable class surface of that class for the surfaces it claims to implement.
</p>

<p>
Partial support is allowed.
However, a runtime claiming partial support SHOULD identify which surfaces it supports and which it does not.
</p>

<p>
A runtime MUST NOT:
</p>

<ul>
  <li>invent undocumented public members while claiming conformance,</li>
  <li>silently redefine the meaning of standard parts,</li>
  <li>silently redefine standard events,</li>
  <li>use one private realization strategy as if it were the standard class law itself.</li>
</ul>

<p>
A runtime also MUST NOT silently transfer semantic ownership of dynamic public text or value-bearing surfaces into realization assets, anchors, text regions, or toolkit-private layers.
Those structures may embody, place, or render the surface.
They do not redefine its class meaning.
</p>

<hr/>

<h2 id="status">18. Status</h2>

<p>
This directory defines the first intrinsic standardized widget baseline of FROG.
</p>

<p>
Its closure direction is:
</p>

<ul>
  <li>a small but credible standard widget core,</li>
  <li>clear reusable class publication,</li>
  <li>clean alignment with <code>frog.ui.*</code> interaction primitives,</li>
  <li>clean downstream alignment with official realization families,</li>
  <li>future growth through composite widgets and realization publication without architectural drift.</li>
</ul>

<p>
The immediate closure direction is:
</p>

<ul>
  <li>stabilize the intrinsic v1 widget core,</li>
  <li>stabilize the status of standardized support widgets relative to that core,</li>
  <li>avoid premature expansion into heavier structured and graphing families,</li>
  <li>preserve the minimum object-surface rule across all intrinsic baseline widgets,</li>
  <li>add near-core classes only after the intrinsic core is fully coherent.</li>
</ul>

<hr/>

<h2 id="summary">19. Summary</h2>

<p>
This directory publishes the first intrinsic standardized widget classes of FROG.
</p>

<p>
It exists so that the widget corridor is not only architecturally well separated, but also concretely instantiated through a portable reusable baseline.
</p>

<p>
In short:
</p>

<ul>
  <li><code>Expression/</code> defines how widgets exist in the language architecture,</li>
  <li><code>Libraries/Widgets/</code> defines which standard widget classes exist in the intrinsic baseline and what their public surfaces mean,</li>
  <li><code>Libraries/UI.md</code> defines how execution interacts with those classes,</li>
  <li><code>Libraries/Realizations/</code> defines how official realization families embody them,</li>
  <li><code>.wfrog</code> artifacts publish machine-readable widget and realization artifacts without collapsing those ownership layers.</li>
</ul>

<p>
The next most coherent file to handle after this rewrite is:
</p>

<ul>
  <li><code>Libraries/Widgets/Listbox.md</code></li>
</ul>

<p>
That file is the next good candidate because the boolean switch question is now architecturally contained as a realization matter, while listbox remains the next meaningful deferred selection-family class to evaluate on its own merits.
</p>
