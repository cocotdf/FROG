<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Numeric Widgets</h1>

<p align="center">
  <strong>Normative baseline for standardized numeric control and numeric indicator widget classes</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#classes-defined-here">2. Classes Defined Here</a></li>
  <li><a href="#common-family-posture">3. Common Family Posture</a></li>
  <li><a href="#frogwidgetsnumeric_control">4. <code>frog.widgets.numeric_control</code></a></li>
  <li><a href="#frogwidgetsnumeric_indicator">5. <code>frog.widgets.numeric_indicator</code></a></li>
  <li><a href="#common-parts">6. Common Parts</a></li>
  <li><a href="#common-behavior-expectations">7. Common Behavior Expectations</a></li>
  <li><a href="#common-realization-expectations">8. Common Realization Expectations</a></li>
  <li><a href="#diagram-interaction-posture">9. Diagram Interaction Posture</a></li>
  <li><a href="#validation-expectations">10. Validation Expectations</a></li>
  <li><a href="#summary">11. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the intrinsic standardized baseline for numeric widgets in FROG.
</p>

<p>
The numeric family provides the first scalar value-carrying widgets used for editable numeric input and displayed numeric output.
These widgets are intended to be small, portable, inspectable, and sufficient for the first serious front-panel baseline.
</p>

<p>
The standard numeric family is therefore defined here as a real object surface with:
</p>

<ul>
  <li>a primary numeric value posture,</li>
  <li>a minimal but real property surface,</li>
  <li>a minimal but real method surface,</li>
  <li>a minimal but real event surface,</li>
  <li>a stable public part model for realization targeting.</li>
</ul>

<p>
This keeps the intrinsic baseline close in spirit to mature graphical systems such as LabVIEW while remaining smaller and more portable.
</p>

<hr/>

<h2 id="classes-defined-here">2. Classes Defined Here</h2>

<p>
This document defines the following standardized widget classes:
</p>

<ul>
  <li><code>frog.widgets.numeric_control</code></li>
  <li><code>frog.widgets.numeric_indicator</code></li>
</ul>

<hr/>

<h2 id="common-family-posture">3. Common Family Posture</h2>

<p>
The numeric widget family has the following common posture:
</p>

<ul>
  <li>family: scalar numeric widget family</li>
  <li>primary value: present</li>
  <li>public value-facing surface: yes</li>
  <li>object-style access surface: yes</li>
  <li>primary value mirror property: <code>value</code></li>
  <li>common label property: <code>label.text</code></li>
  <li>common visibility property: <code>interaction.visible</code></li>
</ul>

<p>
The standard numeric baseline is intended for scalar numeric values such as integers and floating-point values.
The exact allowed numeric types remain governed by the active FROG type system and profile posture.
</p>

<p>
The numeric family also follows an important architectural rule:
</p>

<ul>
  <li><code>value</code> is class-owned semantic data,</li>
  <li><code>label.text</code> is class-owned semantic text,</li>
  <li><code>value_display</code> is a stable public part,</li>
  <li>placement, rendering, and decorative embodiment of that part belong downstream to realization.</li>
</ul>

<hr/>

<h2 id="frogwidgetsnumeric_control">4. <code>frog.widgets.numeric_control</code></h2>

<h3>4.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.numeric_control</code></li>
  <li><strong>family:</strong> <code>numeric_widget</code></li>
  <li><strong>compatible role:</strong> <code>control</code></li>
</ul>

<h3>4.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>natural value participation: yes</li>
  <li>user-mutable: yes</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
</ul>

<h3>4.3 Standard properties</h3>

<ul>
  <li><code>value</code> — readable and writable</li>
  <li><code>label.text</code> — readable and writable</li>
  <li><code>interaction.enabled</code> — readable and writable</li>
  <li><code>interaction.visible</code> — readable and writable</li>
  <li><code>limits.minimum</code> — optional readable and writable bound</li>
  <li><code>limits.maximum</code> — optional readable and writable bound</li>
  <li><code>format.pattern</code> — optional readable and writable display formatting hint</li>
</ul>

<p>
These properties define the minimum public object surface of the intrinsic numeric control.
They do not expose realization-private anchors, text regions, skin layers, or toolkit-private editing machinery as if they were public class members.
</p>

<h3>4.4 Standard methods</h3>

<ul>
  <li><code>focus()</code></li>
  <li><code>increment()</code> when the active class posture exposes step-style increment interaction</li>
  <li><code>decrement()</code> when the active class posture exposes step-style decrement interaction</li>
  <li><code>reset_to_default()</code> when a default value exists</li>
</ul>

<p>
The baseline method surface is intentionally small.
It exists to guarantee that the numeric control remains a real object with a minimal action surface rather than a bare scalar input field.
</p>

<h3>4.5 Standard events</h3>

<ul>
  <li><code>value_changed</code></li>
  <li><code>editing_started</code></li>
  <li><code>editing_committed</code></li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<h3>4.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>value_display</code></li>
  <li><code>increment_button</code> when the active realization exposes it</li>
  <li><code>decrement_button</code> when the active realization exposes it</li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The <code>value_display</code> part is a public dynamic display or editing surface.
Its semantic numeric meaning belongs to the class through <code>value</code>.
Its visual placement and embodiment belong to realization.
</p>

<hr/>

<h2 id="frogwidgetsnumeric_indicator">5. <code>frog.widgets.numeric_indicator</code></a></h2>

<h3>5.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.numeric_indicator</code></li>
  <li><strong>family:</strong> <code>numeric_widget</code></li>
  <li><strong>compatible role:</strong> <code>indicator</code></li>
</ul>

<h3>5.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>natural value participation: yes</li>
  <li>user-mutable: no in the standard portable posture</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
</ul>

<h3>5.3 Standard properties</h3>

<ul>
  <li><code>value</code> — readable and writable for diagram/runtime update surfaces where legal</li>
  <li><code>label.text</code> — readable and writable</li>
  <li><code>interaction.visible</code> — readable and writable</li>
  <li><code>format.pattern</code> — optional readable and writable display formatting hint</li>
</ul>

<p>
The indicator remains a real object even though it is display-oriented.
Its public surface is intentionally smaller than that of the control.
</p>

<h3>5.4 Standard methods</h3>

<ul>
  <li><code>focus()</code> when supported by the host</li>
  <li><code>reset_to_default()</code> when a default value exists and the active class posture exposes it</li>
</ul>

<p>
The intrinsic indicator baseline keeps its method surface modest.
It should not be overloaded with style-reset or toolkit-facing methods that belong more naturally to realization or runtime policy.
</p>

<h3>5.5 Standard events</h3>

<ul>
  <li><code>value_rendered</code></li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<h3>5.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>value_display</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The indicator <code>value_display</code> part remains a public dynamic display surface.
It is not merely a decorative skin region.
</p>

<hr/>

<h2 id="common-parts">6. Common Parts</h2>

<p>
The numeric family uses the following common stable part model:
</p>

<ul>
  <li><code>root</code> — owning widget root surface</li>
  <li><code>label</code> — label surface when present</li>
  <li><code>value_display</code> — rendered numeric display surface</li>
  <li><code>frame</code> — outer visual framing surface when present</li>
</ul>

<p>
The increment and decrement button parts are standard for realizations that expose step-style interaction, but a runtime MAY realize the numeric control without visible increment and decrement parts if it still preserves the published public contract.
</p>

<p>
This distinction is important:
</p>

<ul>
  <li><code>value_display</code> is a public part of the class model,</li>
  <li>anchors, text regions, clipping boxes, and skin layers used to embody it belong to realization unless explicitly promoted to class law.</li>
</ul>

<hr/>

<h2 id="common-behavior-expectations">7. Common Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the numeric family includes at least:
</p>

<ul>
  <li>numeric value updates remain type-compatible with the declared numeric type,</li>
  <li>minimum and maximum bounds, when present, constrain accepted values,</li>
  <li>control-side user editing may produce <code>value_changed</code> and <code>editing_committed</code>,</li>
  <li>indicator-side visual refresh may produce <code>value_rendered</code> when the class contract exposes it,</li>
  <li>disabled numeric controls suppress user-originated editing.</li>
</ul>

<p>
The family also preserves the distinction between:
</p>

<ul>
  <li>semantic numeric value owned by <code>value</code>,</li>
  <li>semantic label text owned by <code>label.text</code>,</li>
  <li>dynamic public display surface exposed through <code>value_display</code>,</li>
  <li>downstream visual embodiment owned by realization.</li>
</ul>

<hr/>

<h2 id="common-realization-expectations">8. Common Realization Expectations</h2>

<p>
A conforming realization of the numeric family SHOULD provide:
</p>

<ul>
  <li>a visible numeric display surface,</li>
  <li>optional label surface,</li>
  <li>reasonable visual distinction between editable control and display-only indicator postures,</li>
  <li>part-to-visual mapping for published parts,</li>
  <li>support for standard interaction states such as enabled, disabled, focused, and value update response.</li>
</ul>

<p>
The realization MAY be SVG-backed, host-native, or toolkit-driven.
It MUST NOT change the published class meaning.
</p>

<p>
In particular:
</p>

<ul>
  <li>realization MAY define anchors or text regions for numeric text placement,</li>
  <li>realization MAY define decorative frames, skins, or step-button assets,</li>
  <li>realization MUST NOT redefine the semantic owner of <code>value</code> or <code>label.text</code>,</li>
  <li>realization MUST NOT make placeholder digits or baked asset text the only semantic source of visible numeric content.</li>
</ul>

<hr/>

<h2 id="diagram-interaction-posture">9. Diagram Interaction Posture</h2>

<p>
The numeric family supports:
</p>

<ul>
  <li>natural value participation through <code>widget_value</code>,</li>
  <li>object-style property access through <code>frog.ui.property_read</code> and <code>frog.ui.property_write</code>,</li>
  <li>method invocation through <code>frog.ui.method_invoke</code> where legal,</li>
  <li>event observation through <code>frog.ui.event_observe</code> where legal.</li>
</ul>

<p>
When the program intent is ordinary numeric dataflow, the natural value path SHOULD be preferred.
Object-style access remains available for richer widget interaction.
</p>

<p>
Typical legal object-style surfaces include:
</p>

<ul>
  <li><code>value</code></li>
  <li><code>label.text</code></li>
  <li><code>interaction.enabled</code></li>
  <li><code>interaction.visible</code></li>
  <li><code>limits.minimum</code></li>
  <li><code>limits.maximum</code></li>
  <li><code>format.pattern</code></li>
</ul>

<p>
Realization-only anchors, text regions, resource layers, and asset helpers remain outside the public numeric class surface unless explicitly standardized elsewhere.
</p>

<hr/>

<h2 id="validation-expectations">10. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>non-numeric <code>value_type</code> on numeric widgets,</li>
  <li>use of indicator role with <code>frog.widgets.numeric_control</code>,</li>
  <li>use of control role with <code>frog.widgets.numeric_indicator</code>,</li>
  <li>access to unknown numeric family members,</li>
  <li>attempts to write control-only or indicator-only surfaces where forbidden,</li>
  <li>inconsistent bound declarations such as minimum greater than maximum,</li>
  <li>attempts to treat realization-only placement surfaces as public numeric class members by default.</li>
</ul>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
The numeric widget family defines the intrinsic standardized scalar numeric baseline of FROG:
</p>

<ul>
  <li><code>frog.widgets.numeric_control</code></li>
  <li><code>frog.widgets.numeric_indicator</code></li>
</ul>

<p>
These classes provide the first standard numeric value-carrying widget surfaces for portable front panels.
They expose a real minimal object surface with properties, methods, events, and parts while keeping realization ownership and runtime-private embodiment clearly separated from class meaning.
</p>
