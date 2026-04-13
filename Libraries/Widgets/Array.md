<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Array Widget</h1>

<p align="center">
  <strong>Normative baseline for the standardized array widget class</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#class-defined-here">2. Class Defined Here</a></li>
  <li><a href="#frogwidgetsarray">3. <code>frog.widgets.array</code></a></li>
  <li><a href="#element-model">4. Element Model</a></li>
  <li><a href="#standard-parts">5. Standard Parts</a></li>
  <li><a href="#behavior-expectations">6. Behavior Expectations</a></li>
  <li><a href="#realization-expectations">7. Realization Expectations</a></li>
  <li><a href="#diagram-interaction-posture">8. Diagram Interaction Posture</a></li>
  <li><a href="#validation-expectations">9. Validation Expectations</a></li>
  <li><a href="#summary">10. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the intrinsic standardized baseline for the array widget in FROG.
</p>

<p>
The array is the first collection-oriented widget of the extended front-panel baseline.
Its role is to expose an ordered repeated element surface as one structured public object.
</p>

<p>
The array is therefore not merely a decorative repeated layout pattern and not merely a runtime-private repeater.
It is a structured widget class with:
</p>

<ul>
  <li>a primary ordered collection value posture,</li>
  <li>a minimal but real property surface,</li>
  <li>a minimal but real method surface,</li>
  <li>a minimal but real event surface,</li>
  <li>a stable public structural part model.</li>
</ul>

<p>
The intrinsic array baseline is intentionally conservative.
It standardizes a one-dimensional ordered collection posture rather than a full spreadsheet, virtualized grid, or arbitrary multidimensional collection editor.
</p>

<hr/>

<h2 id="class-defined-here">2. Class Defined Here</h2>

<p>
This document defines the following standardized widget class:
</p>

<ul>
  <li><code>frog.widgets.array</code></li>
</ul>

<hr/>

<h2 id="frogwidgetsarray">3. <code>frog.widgets.array</code></h2>

<h3>3.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.array</code></li>
  <li><strong>family:</strong> <code>structured_widget</code></li>
  <li><strong>compatible roles:</strong> <code>control</code>, <code>indicator</code>, or mixed collection posture according to element composition</li>
</ul>

<h3>3.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>primary value kind: ordered collection value</li>
  <li>natural value participation: yes</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
</ul>

<p>
The array value is the ordered collection formed by its declared element type and current element sequence.
The intrinsic baseline assumes a one-dimensional ordered element sequence.
</p>

<h3>3.3 Standard properties</h3>

<ul>
  <li><code>value</code> — readable and writable collection value where legal</li>
  <li><code>length</code> — readable collection length</li>
  <li><code>label.text</code> — optional readable and writable array label when the active class posture exposes it</li>
  <li><code>interaction.visible</code> — readable and writable</li>
  <li><code>interaction.enabled</code> — readable and writable when the active aggregate posture exposes a meaningful enabled surface</li>
</ul>

<h3>3.4 Standard methods</h3>

<ul>
  <li><code>append(value)</code> when the active class posture exposes append interaction</li>
  <li><code>clear()</code></li>
  <li><code>focus_first_element()</code> when supported by the host and active realization posture</li>
  <li><code>reset_to_default()</code> when a default collection value exists</li>
</ul>

<h3>3.5 Standard events</h3>

<ul>
  <li><code>value_changed</code> when the collection value changes</li>
  <li><code>element_appended</code> when the active class posture exposes append interaction</li>
  <li><code>focus_gained</code> when the array itself exposes focus posture</li>
  <li><code>focus_lost</code> when the array itself exposes focus posture</li>
</ul>

<h3>3.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code> when the active class posture exposes it</li>
  <li><code>element_region</code></li>
  <li><code>index_display</code> when the active realization exposes an explicit current-index surface</li>
  <li><code>frame</code> when present</li>
</ul>

<hr/>

<h2 id="element-model">4. Element Model</h2>

<p>
The intrinsic array baseline assumes:
</p>

<ul>
  <li>one declared element type,</li>
  <li>one ordered element sequence,</li>
  <li>one collection value derived from that sequence.</li>
</ul>

<p>
The intrinsic baseline does not standardize here:
</p>

<ul>
  <li>arbitrary multidimensional collection editing,</li>
  <li>virtualized large-grid semantics,</li>
  <li>spreadsheet-like cell systems,</li>
  <li>full structural editing policy for every possible child type.</li>
</ul>

<p>
Those richer surfaces may be added later through higher-level collection-oriented widget families.
</p>

<hr/>

<h2 id="standard-parts">5. Standard Parts</h2>

<p>
The array uses the following common stable parts:
</p>

<ul>
  <li><code>root</code> — root widget surface</li>
  <li><code>label</code> — optional array label surface</li>
  <li><code>element_region</code> — region in which array elements are visually embodied</li>
  <li><code>index_display</code> — optional current-index display or navigation support surface</li>
  <li><code>frame</code> — optional outer framing surface</li>
</ul>

<p>
This distinction is important:
</p>

<ul>
  <li><code>element_region</code> is a public structural part,</li>
  <li>scroll helpers, virtualization helpers, clipping regions, repeated cell decorations, and decorative grid layers belong to realization unless explicitly promoted to class law.</li>
</ul>

<hr/>

<h2 id="behavior-expectations">6. Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the array includes at least:
</p>

<ul>
  <li>the array value reflects the current ordered element sequence,</li>
  <li>collection mutation, when exposed, may produce <code>value_changed</code>,</li>
  <li>append interaction, when exposed, may produce <code>element_appended</code>,</li>
  <li>the array remains a structured collection object rather than a decorative repeated layout shell.</li>
</ul>

<p>
The intrinsic baseline does not require one universal editing policy for every possible element family.
It requires only that the public collection contract remain inspectable and portable.
</p>

<hr/>

<h2 id="realization-expectations">7. Realization Expectations</h2>

<p>
A conforming realization of the array SHOULD provide:
</p>

<ul>
  <li>a visible element region for element embodiment,</li>
  <li>optional visible label support,</li>
  <li>optional current-index support when the active realization exposes it,</li>
  <li>part-to-visual mapping for the published parts.</li>
</ul>

<p>
The realization MAY use host-native repeated controls, repeated element views, framed grid-like embodiment, or another compatible collection visualization, provided the published public class surface remains preserved.
</p>

<p>
In particular:
</p>

<ul>
  <li>realization MAY define repeated-cell visuals, layout helpers, clipping helpers, or navigation affordances,</li>
  <li>realization MUST NOT redefine the semantic owner of the array collection value,</li>
  <li>realization MUST NOT turn repeated layout-only structures into the only source of array meaning.</li>
</ul>

<hr/>

<h2 id="diagram-interaction-posture">8. Diagram Interaction Posture</h2>

<p>
The array supports:
</p>

<ul>
  <li>natural value participation through <code>widget_value</code>,</li>
  <li>property access through <code>frog.ui.property_read</code> and <code>frog.ui.property_write</code>,</li>
  <li>method invocation where legal,</li>
  <li>event observation where legal.</li>
</ul>

<p>
When the program intent is ordinary collection-value dataflow, the natural value path SHOULD be preferred.
Object-style access remains available for richer structured widget interaction.
</p>

<p>
Typical legal object-style surfaces include:
</p>

<ul>
  <li><code>value</code></li>
  <li><code>length</code></li>
  <li><code>label.text</code> when exposed</li>
  <li><code>interaction.visible</code></li>
  <li><code>interaction.enabled</code> when exposed</li>
</ul>

<p>
Realization-only scroll helpers, clipping helpers, virtualization layers, and decorative repeated-cell layers remain outside the public array class surface unless explicitly standardized elsewhere.
</p>

<hr/>

<h2 id="validation-expectations">9. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>array values whose element type does not match the declared element type posture,</li>
  <li>unknown array members or parts,</li>
  <li>attempts to treat realization-only repeated layout helpers as semantic collection members,</li>
  <li>attempts to treat realization-only scroll or virtualization helpers as public class members by default.</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The array widget defines the intrinsic standardized ordered-collection widget baseline of FROG:
</p>

<ul>
  <li><code>frog.widgets.array</code></li>
</ul>

<p>
It provides the first standard collection-oriented widget surface of the extended baseline.
It exposes a real minimal object surface with properties, methods, events, and parts while keeping realization ownership and runtime-private embodiment clearly separated from class meaning.
</p>
