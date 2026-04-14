<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Button Widget</h1>

<p align="center">
  <strong>Normative baseline for the standardized push button widget class</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#class-defined-here">2. Class Defined Here</a></li>
  <li><a href="#frogwidgetsbutton">3. <code>frog.widgets.button</code></a></li>
  <li><a href="#styling-and-skin-customization">4. Styling and Skin Customization</a></li>
  <li><a href="#text-model">5. Text Model</a></li>
  <li><a href="#standard-parts">6. Standard Parts</a></li>
  <li><a href="#behavior-expectations">7. Behavior Expectations</a></li>
  <li><a href="#realization-expectations">8. Realization Expectations</a></li>
  <li><a href="#diagram-interaction-posture">9. Diagram Interaction Posture</a></li>
  <li><a href="#validation-expectations">10. Validation Expectations</a></li>
  <li><a href="#summary">11. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the intrinsic standardized baseline for the push button widget of FROG.
</p>

<p>
The button is a command-oriented widget.
Its primary role is not to expose a user-edited scalar value in the same way as numeric, boolean, or string controls.
Its primary role is to expose an explicit interaction surface that may trigger methods, event observation, or command-style logic.
</p>

<p>
The standard button is therefore defined here as a stable public object surface with stable properties, methods, events, parts, and interaction expectations.
It is not defined here as a boolean-like stateful toggle widget.
</p>

<p>
This class must be read together with the shared FROG widget styling posture.
The button is an intrinsic standard widget class with a minimal but real object surface.
It is not a passive decorative control, and it is not a runtime-private host button masquerading as a standard class.
</p>

<hr/>

<h2 id="class-defined-here">2. Class Defined Here</h2>

<p>
This document defines the following standardized widget class:
</p>

<ul>
  <li><code>frog.widgets.button</code></li>
</ul>

<hr/>

<h2 id="frogwidgetsbutton">3. <code>frog.widgets.button</code></h2>

<h3>3.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.button</code></li>
  <li><strong>category:</strong> <code>command_widget</code></li>
  <li><strong>compatible role:</strong> <code>control</code></li>
</ul>

<h3>3.2 Primary value posture</h3>

<p>
The intrinsic button baseline does not define a standard persistent primary value surface.
</p>

<p>
Instead, the standard button is primarily event- and method-oriented.
It may expose transient interaction state through readable properties when the class surface allows it, but it is not standardized here as a value-carrying scalar control.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>the intrinsic button baseline does not require natural <code>widget_value</code> participation,</li>
  <li>the standard button is primarily targeted through <code>widget_reference</code>,</li>
  <li>its portable baseline is centered on object-style interaction and event observation.</li>
</ul>

<h3>3.3 Standard properties</h3>

<ul>
  <li><code>label.text</code> — user-authored semantic label text shown by the button</li>
  <li><code>interaction.enabled</code></li>
  <li><code>interaction.visible</code></li>
  <li><code>interaction.pressed</code> — readable transient interaction posture when exposed by the active class surface</li>
  <li><code>style.foreground_color</code> when exposed by the class or active profile</li>
  <li><code>style.background_color</code> when exposed by the class or active profile</li>
  <li><code>style.border_color</code> when exposed by the class or active profile</li>
  <li><code>style.opacity</code> when exposed by the class or active profile</li>
  <li><code>style.text_color</code> when exposed by the class or active profile</li>
  <li><code>style.font_family</code> when exposed by the class or active profile</li>
  <li><code>style.font_size</code> when exposed by the class or active profile</li>
  <li><code>style.font_weight</code> when exposed by the class or active profile</li>
  <li><code>style.text_alignment</code> when exposed by the class or active profile</li>
  <li><code>realization.family</code> when realization selection is exposed by the active class surface or profile</li>
  <li><code>realization.variant</code> when realization selection is exposed by the active class surface or profile</li>
  <li><code>realization.skin_id</code> when realization selection is exposed by the active class surface or profile</li>
</ul>

<p>
The intrinsic baseline keeps this property surface intentionally small.
These properties define legal public object surfaces.
They do not expose realization-private anchors, text regions, asset layers, SVG element identifiers, or toolkit-private handles as if they were public button members.
</p>

<h3>3.4 Standard methods</h3>

<ul>
  <li><code>focus()</code></li>
  <li><code>press()</code> when allowed by the active interaction posture</li>
  <li><code>release()</code> when allowed by the active interaction posture</li>
  <li><code>activate()</code> when the active profile or standardized class surface exposes an explicit activation method</li>
</ul>

<p>
The baseline method surface is intentionally minimal.
It exists to guarantee that the button remains a real object with a small action surface rather than a visual-only command glyph.
</p>

<h3>3.5 Standard events</h3>

<ul>
  <li><code>pressed</code></li>
  <li><code>released</code></li>
  <li><code>clicked</code></li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<p>
These events define the minimum observable interaction posture of the intrinsic standard button.
They do not imply a richer toggle or multistate command model.
</p>

<h3>3.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>face</code></li>
  <li><code>label</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
These parts are stable public realization targets.
They do not force one host toolkit structure or one asset decomposition.
</p>

<hr/>

<h2 id="styling-and-skin-customization">4. Styling and Skin Customization</h2>

<h3>4.1 Styling posture</h3>

<p>
The standard button is visually customizable.
However, visual customization remains subordinate to class meaning.
</p>

<p>
This means the button may support:
</p>

<ul>
  <li>portable widget-visible style properties,</li>
  <li>selection of a compatible realization family or realization variant,</li>
  <li>selection of a compatible skin identity,</li>
  <li>bounded realization-side resource overrides when allowed by the active publication corridor.</li>
</ul>

<p>
Those customization surfaces do not, by themselves, create a new widget class.
A skinned button remains <code>frog.widgets.button</code> unless a distinct class contract is explicitly published elsewhere.
</p>

<h3>4.2 Portable style surface</h3>

<p>
When exposed, the button may support a small portable style surface through <code>style.*</code> properties.
</p>

<p>
Typical portable style intent includes:
</p>

<ul>
  <li>text color and typography,</li>
  <li>foreground and background emphasis,</li>
  <li>border emphasis,</li>
  <li>overall opacity,</li>
  <li>text alignment.</li>
</ul>

<p>
These style surfaces are public and portable.
They are suitable for source-level widget configuration and for object-style access through <code>frog.ui.property_read</code> and <code>frog.ui.property_write</code> where legal.
</p>

<h3>4.3 Realization-selection surface</h3>

<p>
When exposed, the button may also support realization-selection surfaces such as:
</p>

<ul>
  <li><code>realization.family</code></li>
  <li><code>realization.variant</code></li>
  <li><code>realization.skin_id</code></li>
</ul>

<p>
These surfaces choose a compatible embodiment posture.
They do not redefine:
</p>

<ul>
  <li>the command-oriented class identity of the button,</li>
  <li>the ownership of <code>label.text</code>,</li>
  <li>the public method and event surfaces of the button.</li>
</ul>

<h3>4.4 Resource-override posture</h3>

<p>
A higher-level publication corridor may allow bounded resource overrides for the button realization.
Typical examples include replacing face or frame SVG resources with compatible published alternatives.
</p>

<p>
Such overrides remain realization-oriented.
They must not:
</p>

<ul>
  <li>replace the semantic owner of the button label,</li>
  <li>invent new public parts,</li>
  <li>smuggle new public semantics into a skin substitution.</li>
</ul>

<h3>4.5 Styling versus realization ownership</h3>

<p>
The button class may expose portable visual preferences.
The realization still owns:
</p>

<ul>
  <li>text placement,</li>
  <li>anchor or text-region geometry,</li>
  <li>state-specific face resources,</li>
  <li>frame resources,</li>
  <li>layer composition.</li>
</ul>

<hr/>

<h2 id="text-model">5. Text Model</h2>

<h3>5.1 Semantic text ownership</h3>

<p>
The standard button exposes a semantic text-facing surface through <code>label.text</code>.
This property is the portable public owner of the user-authored button label in the intrinsic baseline.
</p>

<p>
The semantic label text does not belong to an SVG asset, to a realization-private skin file, or to one runtime's private host structure.
A realization may position, style, clip, anchor, or decorate the label visually, but it does not become the semantic owner of the label text.
</p>

<h3>5.2 Baseline text posture</h3>

<p>
The intrinsic standardized button baseline supports a single semantic label text through <code>label.text</code>.
That baseline is intentionally small and portable.
</p>

<p>
The intrinsic standardized button baseline does not define:
</p>

<ul>
  <li><code>label.text_on</code>,</li>
  <li><code>label.text_off</code>,</li>
  <li>intrinsic state-to-text switching as part of the public baseline class law.</li>
</ul>

<p>
Those surfaces may be introduced later by a separate standardized boolean-like button class, a toggle-oriented class, or a bounded composite class built on top of the primitive button baseline.
They are not part of <code>frog.widgets.button</code> itself.
</p>

<h3>5.3 Text style posture</h3>

<p>
When the active profile or standardized class surface exposes text styling, those style properties remain portable widget properties rather than realization-private constants.
</p>

<p>
This means that text color, font family, font size, font weight, alignment, and related text-presentation surfaces are expected to be controlled through published widget-visible properties when supported, not hardcoded as the only source of truth inside SVG content.
</p>

<h3>5.4 Text placement posture</h3>

<p>
Text placement belongs to realization, not to public button semantics.
A realization family may define text anchors, alignment boxes, padding regions, clipping regions, or equivalent placement metadata for the <code>label</code> part.
</p>

<p>
The class law only defines that <code>label</code> exists as a stable public part and that <code>label.text</code> is the semantic text surface.
The realization layer decides where and how that text is visually placed.
</p>

<h3>5.5 SVG posture</h3>

<p>
SVG resources may provide background shapes, decorative layers, text anchor geometry, placeholder layout hints, or visual state resources.
However, the SVG resource must not be the sole owner of the live user-facing button text.
</p>

<p>
A host runtime interpreting the button is expected to render or inject the current semantic label text dynamically according to the published class surface and the active realization mapping.
</p>

<hr/>

<h2 id="standard-parts">6. Standard Parts</h2>

<p>
The button family uses the following common stable parts:
</p>

<ul>
  <li><code>root</code> — root widget surface</li>
  <li><code>face</code> — the main clickable visual face of the button</li>
  <li><code>label</code> — the semantic and visible label surface realized by the host</li>
  <li><code>frame</code> — optional outer frame surface</li>
</ul>

<p>
The <code>label</code> part is especially important because it preserves the distinction between:
</p>

<ul>
  <li>semantic label text owned by <code>label.text</code>,</li>
  <li>text styling exposed through widget-visible style surfaces where supported,</li>
  <li>text placement owned by realization,</li>
  <li>decorative or placeholder visual text content that may appear in assets.</li>
</ul>

<hr/>

<h2 id="behavior-expectations">7. Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the button includes at least:
</p>

<ul>
  <li>user-originated activation is suppressed when the button is disabled,</li>
  <li>press interaction may emit <code>pressed</code>,</li>
  <li>release interaction may emit <code>released</code>,</li>
  <li>a completed button activation may emit <code>clicked</code>,</li>
  <li>runtime interaction state such as pressed posture, when exposed, remains transient rather than canonical program state.</li>
</ul>

<p>
The intrinsic button baseline does not require public state-dependent label switching.
If such switching exists in an extended class or composite posture, it must be published explicitly by that higher-level contract rather than inferred from realization assets.
</p>

<hr/>

<h2 id="realization-expectations">8. Realization Expectations</h2>

<p>
A conforming realization of the button SHOULD provide:
</p>

<ul>
  <li>a clearly perceivable actionable face surface,</li>
  <li>standard visual states such as enabled, disabled, pressed, and focused where supported by the host,</li>
  <li>stable part-to-visual mapping for <code>face</code> and <code>label</code>,</li>
  <li>text placement metadata or equivalent realization support for the <code>label</code> part,</li>
  <li>reasonable visible feedback on user activation.</li>
</ul>

<p>
The button is a particularly important example of the realization split:
multiple SVG resources or other realization assets MAY exist for different interaction states, but those assets do not define the semantics of the button.
They only realize already-published class surfaces and interaction states.
</p>

<p>
In particular:
</p>

<ul>
  <li>realization MAY define where button text is drawn,</li>
  <li>realization MAY define visual style defaults or fallbacks,</li>
  <li>realization MAY define decorative or skinned text containers,</li>
  <li>realization MAY define anchors, text regions, layer maps, or equivalent placement-support structures,</li>
  <li>realization MAY expose compatible family, variant, or skin identities,</li>
  <li>realization MUST NOT redefine the public owner of the label text,</li>
  <li>realization MUST NOT make hardcoded asset text the only semantic label source.</li>
</ul>

<hr/>

<h2 id="diagram-interaction-posture">9. Diagram Interaction Posture</h2>

<p>
The button supports:
</p>

<ul>
  <li>object-style property access where legal,</li>
  <li>method invocation where legal,</li>
  <li>event observation through <code>frog.ui.event_observe</code>,</li>
  <li>widget reference targeting through <code>widget_reference</code>.</li>
</ul>

<p>
The intrinsic button baseline is primarily event-oriented and command-oriented.
It is not standardized here as a natural value-path widget.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>the button is normally addressed through <code>widget_reference</code>,</li>
  <li><code>label.text</code>, <code>interaction.visible</code>, and portable style members may be accessed through <code>frog.ui.property_read</code> and <code>frog.ui.property_write</code> when legal,</li>
  <li>realization-selection members may be accessed through <code>frog.ui.property_read</code> and <code>frog.ui.property_write</code> only when the active class surface or profile exposes them publicly,</li>
  <li><code>focus()</code>, <code>press()</code>, <code>release()</code>, or <code>activate()</code> may be accessed through <code>frog.ui.method_invoke</code> when legal,</li>
  <li><code>pressed</code>, <code>released</code>, and <code>clicked</code> may be observed through <code>frog.ui.event_observe</code>.</li>
</ul>

<hr/>

<h2 id="validation-expectations">10. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>attempts to treat the button as a required scalar value-carrying widget in the intrinsic baseline,</li>
  <li>access to unknown members or parts,</li>
  <li>use of role/class combinations incompatible with <code>frog.widgets.button</code>,</li>
  <li>attempts to interpret transient pressed state as canonical persistent source-owned state by default,</li>
  <li>attempts to treat realization-private text placement or SVG-baked text as the public semantic owner of the button label,</li>
  <li>attempts to use <code>label.text_on</code> or <code>label.text_off</code> as if they were intrinsic baseline members of <code>frog.widgets.button</code>,</li>
  <li>attempts to address realization-only anchors, text regions, or asset layers through <code>frog.ui.*</code> as if they were public button members by default,</li>
  <li>attempts to use styling or skin-selection surfaces to imply a distinct class contract without explicit class publication.</li>
</ul>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
The standardized button defines the intrinsic command-oriented action widget of the FROG baseline:
</p>

<ul>
  <li><code>frog.widgets.button</code></li>
</ul>

<p>
It is primarily an event- and method-oriented control surface with stable properties, methods, events, parts, and portable executable observation through the widget interaction corridor.
</p>

<p>
Its semantic label text is owned by <code>label.text</code>.
Its portable style surfaces, when exposed, remain widget-visible and portable.
Its compatible skin and realization choices remain realization-oriented rather than class-defining.
Its text placement belongs to realization.
Its assets may decorate and anchor the button face, but they do not become the semantic owner of the button label.
</p>
