<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Label Widget</h1>

<p align="center">
  <strong>Normative baseline for the standardized label widget class</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#class-defined-here">2. Class Defined Here</a></li>
  <li><a href="#frogwidgetslabel">3. <code>frog.widgets.label</code></a></li>
  <li><a href="#text-model">4. Text Model</a></li>
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
This document defines the intrinsic standardized baseline for the label widget of FROG.
</p>

<p>
The label is a support-oriented widget.
Its primary role is to expose portable semantic support text in the front panel rather than a business value intended for ordinary computational dataflow.
</p>

<p>
The standard label is therefore defined here as a stable public object surface with a minimal but real property surface, a minimal but real method surface, a minimal but real event surface, and stable public parts.
It is not defined here as a decorative SVG fragment or a realization-private text layer.
</p>

<hr/>

<h2 id="class-defined-here">2. Class Defined Here</h2>

<p>
This document defines the following standardized widget class:
</p>

<ul>
  <li><code>frog.widgets.label</code></li>
</ul>

<hr/>

<h2 id="frogwidgetslabel">3. <code>frog.widgets.label</code></h2>

<h3>3.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.label</code></li>
  <li><strong>family:</strong> <code>support_widget</code></li>
  <li><strong>compatible role:</strong> <code>support</code></li>
</ul>

<h3>3.2 Primary value posture</h3>

<p>
The intrinsic label baseline does not define a standard primary business-value surface intended for ordinary front-panel dataflow.
</p>

<p>
Instead, the standard label is primarily text-oriented and support-oriented.
Its principal public semantic surface is exposed through <code>text</code>.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>the intrinsic label baseline does not require natural <code>widget_value</code> participation,</li>
  <li>the standard label is primarily targeted through <code>widget_reference</code>,</li>
  <li>its portable baseline is centered on object-style interaction and support-text semantics.</li>
</ul>

<h3>3.3 Standard properties</h3>

<ul>
  <li><code>text</code> — semantic support text shown by the label</li>
  <li><code>interaction.visible</code></li>
  <li><code>style.text_color</code> when exposed by the class or active profile</li>
  <li><code>style.font_family</code> when exposed by the class or active profile</li>
  <li><code>style.font_size</code> when exposed by the class or active profile</li>
  <li><code>style.font_weight</code> when exposed by the class or active profile</li>
  <li><code>style.text_alignment</code> when exposed by the class or active profile</li>
</ul>

<h3>3.4 Standard methods</h3>

<ul>
  <li><code>set_text(text)</code></li>
  <li><code>reset_to_default_style()</code> when a style default exists and the active class posture exposes it</li>
</ul>

<p>
The baseline method surface is intentionally small.
It exists to guarantee that the label remains a real support object rather than a realization-private text decoration.
</p>

<h3>3.5 Standard events</h3>

<ul>
  <li><code>text_changed</code></li>
  <li><code>value_rendered</code> when the active class posture exposes visible refresh-oriented notification</li>
</ul>

<h3>3.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>text_surface</code></li>
  <li><code>frame</code> when present</li>
</ul>

<hr/>

<h2 id="text-model">4. Text Model</h2>

<h3>4.1 Semantic text ownership</h3>

<p>
The standard label exposes a semantic text-facing surface through <code>text</code>.
This property is the portable public owner of the user-authored label content in the intrinsic baseline.
</p>

<p>
The semantic label text does not belong to an SVG asset, to a realization-private skin file, or to one runtime's private host structure.
A realization may position, style, clip, anchor, or decorate the text visually, but it does not become the semantic owner of the text itself.
</p>

<h3>4.2 Text style posture</h3>

<p>
When the active profile or standardized class surface exposes text styling, those style properties remain portable widget properties rather than realization-private constants.
</p>

<p>
This means that text color, font family, font size, font weight, alignment, and related text-presentation surfaces are expected to be controlled through published widget-visible properties when supported, not hardcoded as the only source of truth inside SVG content.
</p>

<h3>4.3 Text placement posture</h3>

<p>
Text placement belongs to realization, not to public label semantics.
A realization family may define text anchors, alignment boxes, padding regions, clipping regions, or equivalent placement metadata for the <code>text_surface</code> part.
</p>

<p>
The class law only defines that <code>text_surface</code> exists as a stable public part and that <code>text</code> is the semantic text surface.
The realization layer decides where and how that text is visually placed.
</p>

<h3>4.4 SVG posture</h3>

<p>
SVG resources may provide background shapes, decorative layers, text anchor geometry, placeholder layout hints, or visual emphasis resources.
However, the SVG resource must not be the sole owner of the live user-facing label text.
</p>

<p>
A host runtime interpreting the label is expected to render or inject the current semantic text dynamically according to the published class surface and the active realization mapping.
</p>

<hr/>

<h2 id="standard-parts">5. Standard Parts</h2>

<p>
The label family uses the following common stable parts:
</p>

<ul>
  <li><code>root</code> — root widget surface</li>
  <li><code>text_surface</code> — the visible semantic text surface realized by the host</li>
  <li><code>frame</code> — optional outer emphasis or grouping surface</li>
</ul>

<p>
The <code>text_surface</code> part is especially important because it preserves the distinction between:
</p>

<ul>
  <li>semantic support text owned by <code>text</code>,</li>
  <li>text styling exposed through widget-visible style surfaces where supported,</li>
  <li>text placement owned by realization,</li>
  <li>decorative or placeholder visual text content that may appear in assets.</li>
</ul>

<hr/>

<h2 id="behavior-expectations">6. Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the label includes at least:
</p>

<ul>
  <li>text updates may emit <code>text_changed</code>,</li>
  <li>visible refresh may emit <code>value_rendered</code> when the class posture exposes it,</li>
  <li>runtime-private styling or rendering caches do not become public class state.</li>
</ul>

<p>
The intrinsic label baseline does not require focus behavior, command behavior, or natural primary-value semantics.
If such surfaces exist in an extended class or composite posture, they must be published explicitly by that higher-level contract rather than inferred from realization assets.
</p>

<hr/>

<h2 id="realization-expectations">7. Realization Expectations</h2>

<p>
A conforming realization of the label SHOULD provide:
</p>

<ul>
  <li>a clearly readable text surface,</li>
  <li>stable part-to-visual mapping for <code>text_surface</code>,</li>
  <li>text placement metadata or equivalent realization support for the <code>text_surface</code> part,</li>
  <li>reasonable visible support styling where the active realization uses one.</li>
</ul>

<p>
The label is a particularly important example of the realization split:
multiple SVG resources or other realization assets MAY exist for different visual styles,
but those assets do not define the semantics of the label.
They only realize already-published class surfaces.
</p>

<p>
In particular:
</p>

<ul>
  <li>realization MAY define where label text is drawn,</li>
  <li>realization MAY define visual style defaults or fallbacks,</li>
  <li>realization MAY define decorative containers or emphasis surfaces,</li>
  <li>realization MUST NOT redefine the public owner of the text,</li>
  <li>realization MUST NOT make hardcoded asset text the only semantic text source.</li>
</ul>

<hr/>

<h2 id="diagram-interaction-posture">8. Diagram Interaction Posture</h2>

<p>
The label supports:
</p>

<ul>
  <li>object-style property access where legal,</li>
  <li>method invocation where legal,</li>
  <li>event observation through <code>frog.ui.event_observe</code>,</li>
  <li>widget reference targeting through <code>widget_reference</code>.</li>
</ul>

<p>
The intrinsic label baseline is primarily support-oriented.
It is not standardized here as a natural value-path widget.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>the label is normally addressed through <code>widget_reference</code>,</li>
  <li><code>text</code> and <code>interaction.visible</code> may be accessed through <code>frog.ui.property_read</code> and <code>frog.ui.property_write</code> when legal,</li>
  <li><code>set_text(text)</code> may be accessed through <code>frog.ui.method_invoke</code> when legal,</li>
  <li><code>text_changed</code> may be observed through <code>frog.ui.event_observe</code>.</li>
</ul>

<hr/>

<h2 id="validation-expectations">9. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>attempts to treat the label as a required scalar value-carrying widget in the intrinsic baseline,</li>
  <li>access to unknown members or parts,</li>
  <li>use of role/class combinations incompatible with <code>frog.widgets.label</code>,</li>
  <li>attempts to treat realization-private text placement or SVG-baked text as the public semantic owner of the label text,</li>
  <li>attempts to address realization-only anchors, text regions, or asset layers through <code>frog.ui.*</code> as if they were public label members by default.</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The standardized label defines the intrinsic support-oriented text widget of the FROG baseline:
</p>

<ul>
  <li><code>frog.widgets.label</code></li>
</ul>

<p>
It is primarily a support-text object surface with stable properties, methods, events, and parts.
Its semantic text is owned by <code>text</code>.
Its text styling, when exposed, remains widget-visible and portable.
Its text placement belongs to realization.
Its assets may decorate and anchor the text surface, but they do not become the semantic owner of the label content.
</p>
