<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Frame Widget</h1>

<p align="center">
  <strong>Normative baseline for the standardized frame widget class</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#class-defined-here">2. Class Defined Here</a></li>
  <li><a href="#frogwidgetsframe">3. <code>frog.widgets.frame</code></a></li>
  <li><a href="#title-model">4. Title Model</a></li>
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
This document defines the intrinsic standardized baseline for the frame widget of FROG.
</p>

<p>
The frame is a support-oriented structural widget.
Its primary role is to expose a portable grouping or emphasis surface in the front panel rather than a business value intended for ordinary computational dataflow.
</p>

<p>
The standard frame is therefore defined here as a stable public object surface with a minimal but real property surface, a minimal but real method surface, a minimal but real event surface, and stable public parts.
It is not defined here as a realization-private border fragment or a host-only grouping primitive.
</p>

<hr/>

<h2 id="class-defined-here">2. Class Defined Here</h2>

<p>
This document defines the following standardized widget class:
</p>

<ul>
  <li><code>frog.widgets.frame</code></li>
</ul>

<hr/>

<h2 id="frogwidgetsframe">3. <code>frog.widgets.frame</code></h2>

<h3>3.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.frame</code></li>
  <li><strong>family:</strong> <code>support_widget</code></li>
  <li><strong>compatible role:</strong> <code>support</code></li>
</ul>

<h3>3.2 Primary value posture</h3>

<p>
The intrinsic frame baseline does not define a standard primary business-value surface intended for ordinary front-panel dataflow.
</p>

<p>
Instead, the standard frame is primarily structure-oriented and support-oriented.
Its principal public semantic surfaces are grouping visibility and, when exposed, optional title text.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>the intrinsic frame baseline does not require natural <code>widget_value</code> participation,</li>
  <li>the standard frame is primarily targeted through <code>widget_reference</code>,</li>
  <li>its portable baseline is centered on object-style interaction and structural grouping semantics.</li>
</ul>

<h3>3.3 Standard properties</h3>

<ul>
  <li><code>interaction.visible</code></li>
  <li><code>title.text</code> when the active class posture exposes an explicit title surface</li>
  <li><code>style.border_visible</code> when exposed by the class or active profile</li>
  <li><code>style.border_thickness</code> when exposed by the class or active profile</li>
  <li><code>style.corner_radius</code> when exposed by the class or active profile</li>
</ul>

<h3>3.4 Standard methods</h3>

<ul>
  <li><code>show()</code></li>
  <li><code>hide()</code></li>
  <li><code>reset_to_default_style()</code> when a style default exists and the active class posture exposes it</li>
</ul>

<p>
The baseline method surface is intentionally small.
It exists to guarantee that the frame remains a real structural support object rather than a realization-private border decoration.
</p>

<h3>3.5 Standard events</h3>

<ul>
  <li><code>visibility_changed</code></li>
  <li><code>value_rendered</code> when the active class posture exposes visible refresh-oriented notification</li>
</ul>

<h3>3.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>border</code></li>
  <li><code>title_surface</code> when the active class posture exposes it</li>
  <li><code>content_region</code> when the active realization exposes a contained grouping region</li>
</ul>

<hr/>

<h2 id="title-model">4. Title Model</h2>

<h3>4.1 Semantic title ownership</h3>

<p>
When the active class posture exposes title text, the standard frame exposes a semantic text-facing surface through <code>title.text</code>.
This property is the portable public owner of the user-authored frame title in the intrinsic baseline.
</p>

<p>
The semantic title text does not belong to an SVG asset, to a realization-private skin file, or to one runtime's private host structure.
A realization may position, style, clip, anchor, or decorate the title visually, but it does not become the semantic owner of the title itself.
</p>

<h3>4.2 Title posture</h3>

<p>
The intrinsic standardized frame baseline does not require title text in every embodiment.
The title surface is optional and only exists when the active class posture exposes it.
</p>

<p>
When exposed, the title remains a portable public property rather than realization-private static decoration.
</p>

<h3>4.3 Title placement posture</h3>

<p>
Title placement belongs to realization, not to public frame semantics.
A realization family may define title anchors, alignment boxes, padding regions, clipping regions, or equivalent placement metadata for the <code>title_surface</code> part.
</p>

<p>
The class law only defines that <code>title_surface</code> may exist as a stable public part and that <code>title.text</code> is the semantic title surface when exposed.
The realization layer decides where and how that title is visually placed.
</p>

<hr/>

<h2 id="standard-parts">5. Standard Parts</h2>

<p>
The frame family uses the following common stable parts:
</p>

<ul>
  <li><code>root</code> — root widget surface</li>
  <li><code>border</code> — the main visible grouping or emphasis border surface</li>
  <li><code>title_surface</code> — optional visible title surface realized by the host</li>
  <li><code>content_region</code> — optional grouping region associated with the frame embodiment</li>
</ul>

<p>
These parts are especially important because they preserve the distinction between:
</p>

<ul>
  <li>semantic support structure owned by the frame class,</li>
  <li>optional semantic title text owned by <code>title.text</code>,</li>
  <li>title placement and grouping visuals owned by realization,</li>
  <li>decorative borders or placeholder title text that may appear in assets.</li>
</ul>

<hr/>

<h2 id="behavior-expectations">6. Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the frame includes at least:
</p>

<ul>
  <li>visibility changes may emit <code>visibility_changed</code>,</li>
  <li>visible refresh may emit <code>value_rendered</code> when the class posture exposes it,</li>
  <li>runtime-private layout or grouping caches do not become public class state.</li>
</ul>

<p>
The intrinsic frame baseline does not require focus behavior, command behavior, natural primary-value semantics, or mandatory child-container semantics in the class law itself.
If such surfaces exist in an extended class or composite posture, they must be published explicitly by that higher-level contract rather than inferred from realization assets.
</p>

<hr/>

<h2 id="realization-expectations">7. Realization Expectations</h2>

<p>
A conforming realization of the frame SHOULD provide:
</p>

<ul>
  <li>a clearly perceivable grouping or emphasis border surface,</li>
  <li>stable part-to-visual mapping for <code>border</code>,</li>
  <li>title placement metadata or equivalent realization support for the <code>title_surface</code> part when exposed,</li>
  <li>reasonable visible grouping posture where the active realization uses one.</li>
</ul>

<p>
The frame is a particularly important example of the realization split:
multiple SVG resources or other realization assets MAY exist for different grouping styles,
but those assets do not define the semantics of the frame.
They only realize already-published class surfaces.
</p>

<p>
In particular:
</p>

<ul>
  <li>realization MAY define where frame title text is drawn,</li>
  <li>realization MAY define visual border defaults or fallbacks,</li>
  <li>realization MAY define decorative containers, emphasis lines, or grouping surfaces,</li>
  <li>realization MUST NOT redefine the public owner of <code>title.text</code> when exposed,</li>
  <li>realization MUST NOT make hardcoded asset title text the only semantic title source.</li>
</ul>

<hr/>

<h2 id="diagram-interaction-posture">8. Diagram Interaction Posture</h2>

<p>
The frame supports:
</p>

<ul>
  <li>object-style property access where legal,</li>
  <li>method invocation where legal,</li>
  <li>event observation through <code>frog.ui.event_observe</code>,</li>
  <li>widget reference targeting through <code>widget_reference</code>.</li>
</ul>

<p>
The intrinsic frame baseline is primarily structure-oriented and support-oriented.
It is not standardized here as a natural value-path widget.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>the frame is normally addressed through <code>widget_reference</code>,</li>
  <li><code>interaction.visible</code> and <code>title.text</code> when exposed may be accessed through <code>frog.ui.property_read</code> and <code>frog.ui.property_write</code> when legal,</li>
  <li><code>show()</code> and <code>hide()</code> may be accessed through <code>frog.ui.method_invoke</code> when legal,</li>
  <li><code>visibility_changed</code> may be observed through <code>frog.ui.event_observe</code>.</li>
</ul>

<hr/>

<h2 id="validation-expectations">9. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>attempts to treat the frame as a required scalar value-carrying widget in the intrinsic baseline,</li>
  <li>access to unknown members or parts,</li>
  <li>use of role/class combinations incompatible with <code>frog.widgets.frame</code>,</li>
  <li>attempts to treat realization-private title placement or SVG-baked title text as the public semantic owner of the frame title,</li>
  <li>attempts to address realization-only anchors, title regions, or asset layers through <code>frog.ui.*</code> as if they were public frame members by default.</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The standardized frame defines the intrinsic support-oriented grouping widget of the FROG baseline:
</p>

<ul>
  <li><code>frog.widgets.frame</code></li>
</ul>

<p>
It is primarily a structural support object surface with stable properties, methods, events, and parts.
Its optional semantic title is owned by <code>title.text</code> when exposed.
Its title placement and grouping visuals belong to realization.
Its assets may decorate and support grouping, but they do not become the semantic owner of frame meaning.
</p>
