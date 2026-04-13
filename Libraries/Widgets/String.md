<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard String Widgets</h1>

<p align="center">
  <strong>Normative baseline for standardized string control and string indicator widget classes</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#classes-defined-here">2. Classes Defined Here</a></li>
  <li><a href="#common-family-posture">3. Common Family Posture</a></li>
  <li><a href="#frogwidgetsstring_control">4. <code>frog.widgets.string_control</code></a></li>
  <li><a href="#frogwidgetsstring_indicator">5. <code>frog.widgets.string_indicator</code></a></li>
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
This document defines the intrinsic standardized baseline for string widgets in FROG.
</p>

<p>
The string family provides the first text-value widgets used for editable textual input and displayed textual output in the portable front-panel baseline.
</p>

<p>
The standard string family is therefore defined here as a real object surface with:
</p>

<ul>
  <li>a primary string value posture,</li>
  <li>a minimal but real property surface,</li>
  <li>a minimal but real method surface,</li>
  <li>a minimal but real event surface,</li>
  <li>a stable public part model for realization targeting.</li>
</ul>

<p>
This keeps the intrinsic baseline close in spirit to mature graphical systems such as LabVIEW while remaining smaller and more portable.
</p>

<p>
This intrinsic baseline is intentionally single-value text oriented.
It does not attempt to standardize a full rich-text editor, multi-line editor, code editor, terminal widget, or console-like interaction model.
</p>

<hr/>

<h2 id="classes-defined-here">2. Classes Defined Here</h2>

<p>
This document defines the following standardized widget classes:
</p>

<ul>
  <li><code>frog.widgets.string_control</code></li>
  <li><code>frog.widgets.string_indicator</code></li>
</ul>

<hr/>

<h2 id="common-family-posture">3. Common Family Posture</h2>

<p>
The string family has the following common posture:
</p>

<ul>
  <li>family: scalar text widget family</li>
  <li>primary value: present</li>
  <li>value type: <code>string</code></li>
  <li>natural value participation: yes</li>
  <li>object-style access: yes</li>
  <li>primary value mirror property: <code>value</code></li>
  <li>common label property: <code>label.text</code></li>
  <li>common visibility property: <code>interaction.visible</code></li>
</ul>

<p>
The string family also follows an important architectural rule:
</p>

<ul>
  <li><code>value</code> is class-owned semantic text data,</li>
  <li><code>label.text</code> is class-owned semantic label text,</li>
  <li><code>text_display</code> is a stable public dynamic part,</li>
  <li>placement, clipping, scrolling posture, and decorative embodiment of that part belong downstream to realization unless explicitly standardized as public class surfaces.</li>
</ul>

<hr/>

<h2 id="frogwidgetsstring_control">4. <code>frog.widgets.string_control</code></h2>

<h3>4.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.string_control</code></li>
  <li><strong>family:</strong> <code>string_widget</code></li>
  <li><strong>compatible role:</strong> <code>control</code></li>
</ul>

<h3>4.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>value type: <code>string</code></li>
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
  <li><code>placeholder.text</code> — optional readable and writable placeholder surface when the active class posture exposes it</li>
  <li><code>format.max_length</code> — optional readable and writable input-length constraint when the active class posture exposes it</li>
</ul>

<p>
These properties define the minimum public object surface of the intrinsic string control.
They do not expose realization-private anchors, text regions, scroll helpers, caret internals, or toolkit-private editor state as if they were public class members.
</p>

<h3>4.4 Standard methods</h3>

<ul>
  <li><code>focus()</code></li>
  <li><code>clear()</code></li>
  <li><code>reset_to_default()</code> when a default value exists</li>
</ul>

<p>
The baseline method surface is intentionally small.
It exists to guarantee that the string control remains a real object with a minimal action surface rather than a bare text entry field.
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
  <li><code>text_display</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The <code>text_display</code> part is a public dynamic display or editing surface.
Its semantic text meaning belongs to the class through <code>value</code>.
Its visual placement and embodiment belong to realization.
</p>

<hr/>

<h2 id="frogwidgetsstring_indicator">5. <code>frog.widgets.string_indicator</code></h2>

<h3>5.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.string_indicator</code></li>
  <li><strong>family:</strong> <code>string_widget</code></li>
  <li><strong>compatible role:</strong> <code>indicator</code></li>
</ul>

<h3>5.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>value type: <code>string</code></li>
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
  <li><code>text_display</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The indicator <code>text_display</code> part remains a public dynamic display surface.
It is not merely a decorative skin region.
</p>

<hr/>

<h2 id="common-parts">6. Common Parts</h2>

<p>
The string family uses the following common stable parts:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>text_display</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
This distinction is important:
</p>

<ul>
  <li><code>text_display</code> is a public part of the class model,</li>
  <li>anchors, text regions, clipping boxes, placeholder placement, and skin layers used to embody it belong to realization unless explicitly promoted to class law.</li>
</ul>

<hr/>

<h2 id="common-behavior-expectations">7. Common Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the string family includes at least:
</p>

<ul>
  <li>the primary value remains of type <code>string</code>,</li>
  <li>string controls accept user editing only when enabled,</li>
  <li>control-side value edits may emit <code>value_changed</code> and <code>editing_committed</code>,</li>
  <li>indicator-side visual refresh may emit <code>value_rendered</code> when the class contract exposes it,</li>
  <li>placeholder presentation, when exposed, remains a public display aid and does not replace the actual primary value.</li>
</ul>

<p>
The family also preserves the distinction between:
</p>

<ul>
  <li>semantic string value owned by <code>value</code>,</li>
  <li>semantic label text owned by <code>label.text</code>,</li>
  <li>dynamic public display surface exposed through <code>text_display</code>,</li>
  <li>downstream visual embodiment owned by realization.</li>
</ul>

<p>
Caret state, text selection, scrolling posture, insertion mode, and similar host editing details remain runtime-facing editing posture unless explicitly standardized elsewhere.
They do not automatically become intrinsic public string-widget semantics.
</p>

<hr/>

<h2 id="common-realization-expectations">8. Common Realization Expectations</h2>

<p>
A conforming realization of the string family SHOULD provide:
</p>

<ul>
  <li>a visible text surface for the current value,</li>
  <li>optional label presentation,</li>
  <li>visual distinction between control and indicator postures,</li>
  <li>part-to-visual mapping for the published parts.</li>
</ul>

<p>
The realization MAY be SVG-backed, host-native, or toolkit-driven.
It MUST NOT change the published class meaning.
</p>

<p>
In particular:
</p>

<ul>
  <li>realization MAY define anchors or text regions for string text placement,</li>
  <li>realization MAY define placeholder placement, clipping regions, skins, or decorative frames,</li>
  <li>realization MUST NOT redefine the semantic owner of <code>value</code> or <code>label.text</code>,</li>
  <li>realization MUST NOT make placeholder text, preview strings, or baked asset text the only semantic source of visible string content.</li>
</ul>

<hr/>

<h2 id="diagram-interaction-posture">9. Diagram Interaction Posture</h2>

<p>
The string family supports:
</p>

<ul>
  <li>natural value participation through <code>widget_value</code>,</li>
  <li>property access through <code>frog.ui.property_read</code> and <code>frog.ui.property_write</code>,</li>
  <li>method invocation where legal,</li>
  <li>event observation where legal.</li>
</ul>

<p>
When the program intent is ordinary text dataflow, the natural value path SHOULD be preferred.
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
  <li><code>placeholder.text</code> when exposed</li>
  <li><code>format.max_length</code> when exposed</li>
</ul>

<p>
Realization-only anchors, text regions, clipping helpers, resource layers, and asset helpers remain outside the public string class surface unless explicitly standardized elsewhere.
</p>

<hr/>

<h2 id="validation-expectations">10. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>non-string <code>value_type</code> on string widgets,</li>
  <li>role/class mismatches,</li>
  <li>attempts to use unsupported members,</li>
  <li>attempts to treat placeholder presentation as the actual primary value,</li>
  <li>attempts to treat realization-only placement or clipping surfaces as public class members by default.</li>
</ul>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
The string widget family defines the intrinsic standardized text-value baseline of FROG:
</p>

<ul>
  <li><code>frog.widgets.string_control</code></li>
  <li><code>frog.widgets.string_indicator</code></li>
</ul>

<p>
These classes provide the first standard textual value widgets of the portable front-panel baseline.
They expose a real minimal object surface with properties, methods, events, and parts while keeping realization ownership and runtime-private embodiment clearly separated from class meaning.
</p>
