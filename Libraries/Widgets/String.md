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
  <li><a href="#common-styling-and-skin-customization">4. Common Styling and Skin Customization</a></li>
  <li><a href="#frogwidgetsstring_control">5. <code>frog.widgets.string_control</code></a></li>
  <li><a href="#frogwidgetsstring_indicator">6. <code>frog.widgets.string_indicator</code></a></li>
  <li><a href="#common-parts">7. Common Parts</a></li>
  <li><a href="#common-behavior-expectations">8. Common Behavior Expectations</a></li>
  <li><a href="#common-realization-expectations">9. Common Realization Expectations</a></li>
  <li><a href="#diagram-interaction-posture">10. Diagram Interaction Posture</a></li>
  <li><a href="#validation-expectations">11. Validation Expectations</a></li>
  <li><a href="#summary">12. Summary</a></li>
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
  <li>primary value: present</li>
  <li>value type: <code>string</code></li>
  <li>natural value participation: yes</li>
  <li>object-style access: yes</li>
  <li>primary value mirror property: <code>value</code></li>
  <li>common label property: <code>label.text</code></li>
  <li>common visibility property: <code>interaction.visible</code></li>
</ul>

<p>
This intrinsic baseline is single-value text oriented.
It does not attempt to standardize a full rich-text, multi-line code editor, terminal-like widget, or document-layout widget surface.
</p>

<p>
The family also follows an important architectural rule:
</p>

<ul>
  <li><code>value</code> is class-owned semantic string data,</li>
  <li><code>label.text</code> is class-owned semantic label text,</li>
  <li><code>text_display</code> is a stable public dynamic part,</li>
  <li>the visual embodiment of the displayed or edited text belongs downstream to realization.</li>
</ul>

<hr/>

<h2 id="common-styling-and-skin-customization">4. Common Styling and Skin Customization</h2>

<p>
The string family is visually customizable.
However, visual customization remains subordinate to string class meaning.
</p>

<p>
Accordingly, string widgets may expose:
</p>

<ul>
  <li>portable widget-visible style properties,</li>
  <li>selection of a compatible realization family or variant,</li>
  <li>selection of a compatible skin identity,</li>
  <li>bounded realization-side resource overrides when the active publication corridor allows them.</li>
</ul>

<p>
These surfaces do not create a new widget class.
A skinned string widget remains <code>frog.widgets.string_control</code> or <code>frog.widgets.string_indicator</code>.
</p>

<p>
When exposed, the preferred portable style surfaces include:
</p>

<ul>
  <li><code>style.foreground_color</code></li>
  <li><code>style.background_color</code></li>
  <li><code>style.border_color</code></li>
  <li><code>style.opacity</code></li>
  <li><code>style.text_color</code></li>
  <li><code>style.font_family</code></li>
  <li><code>style.font_size</code></li>
  <li><code>style.font_weight</code></li>
  <li><code>style.text_alignment</code></li>
  <li><code>realization.family</code></li>
  <li><code>realization.variant</code></li>
  <li><code>realization.skin_id</code></li>
</ul>

<hr/>

<h2 id="frogwidgetsstring_control">5. <code>frog.widgets.string_control</code></h2>

<h3>5.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.string_control</code></li>
  <li><strong>category:</strong> <code>control</code></li>
  <li><strong>compatible role:</strong> <code>control</code></li>
</ul>

<h3>5.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>value type: <code>string</code></li>
  <li>natural value participation: yes</li>
  <li>user-mutable: yes</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
</ul>

<h3>5.3 Standard properties</h3>

<ul>
  <li><code>value</code></li>
  <li><code>label.text</code></li>
  <li><code>interaction.enabled</code></li>
  <li><code>interaction.visible</code></li>
  <li><code>placeholder.text</code> when supported by the realization and exposed by the class posture</li>
  <li><code>format.max_length</code> when supported by the class posture</li>
  <li>portable <code>style.*</code> surfaces when exposed by the class or active profile</li>
  <li><code>realization.family</code> when realization selection is publicly exposed</li>
  <li><code>realization.variant</code> when realization selection is publicly exposed</li>
  <li><code>realization.skin_id</code> when realization selection is publicly exposed</li>
</ul>

<h3>5.4 Standard methods</h3>

<ul>
  <li><code>focus()</code></li>
  <li><code>clear()</code></li>
  <li><code>reset_to_default()</code> when a default exists</li>
</ul>

<h3>5.5 Standard events</h3>

<ul>
  <li><code>value_changed</code></li>
  <li><code>editing_started</code></li>
  <li><code>editing_committed</code></li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<h3>5.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>text_display</code></li>
  <li><code>frame</code></li>
</ul>

<hr/>

<h2 id="frogwidgetsstring_indicator">6. <code>frog.widgets.string_indicator</code></a></h2>

<h3>6.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.string_indicator</code></li>
  <li><strong>category:</strong> <code>indicator</code></li>
  <li><strong>compatible role:</strong> <code>indicator</code></li>
</ul>

<h3>6.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>value type: <code>string</code></li>
  <li>natural value participation: yes</li>
  <li>user-mutable: no in the standard portable posture</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
</ul>

<h3>6.3 Standard properties</h3>

<ul>
  <li><code>value</code></li>
  <li><code>label.text</code></li>
  <li><code>interaction.visible</code></li>
  <li>portable <code>style.*</code> surfaces when exposed by the class or active profile</li>
  <li><code>realization.family</code> when realization selection is publicly exposed</li>
  <li><code>realization.variant</code> when realization selection is publicly exposed</li>
  <li><code>realization.skin_id</code> when realization selection is publicly exposed</li>
</ul>

<h3>6.4 Standard methods</h3>

<ul>
  <li><code>focus()</code> when supported by the host</li>
  <li><code>reset_to_default_style()</code> when a style default exists</li>
</ul>

<h3>6.5 Standard events</h3>

<ul>
  <li><code>value_rendered</code></li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<h3>6.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>text_display</code></li>
  <li><code>frame</code></li>
</ul>

<hr/>

<h2 id="common-parts">7. Common Parts</h2>

<p>
The string family uses the following common stable parts:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>text_display</code></li>
  <li><code>frame</code></li>
</ul>

<p>
The <code>text_display</code> part is especially important because it preserves the distinction between:
</p>

<ul>
  <li>semantic string value owned by <code>value</code>,</li>
  <li>portable style preferences that affect visible text presentation,</li>
  <li>placement and editing embodiment owned by realization.</li>
</ul>

<hr/>

<h2 id="common-behavior-expectations">8. Common Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the string family includes at least:
</p>

<ul>
  <li>the primary value remains of type <code>string</code>,</li>
  <li>string controls accept user editing only when enabled,</li>
  <li>control-side value edits may emit <code>value_changed</code> and <code>editing_committed</code>,</li>
  <li>indicator-side visual refresh may emit <code>value_rendered</code>,</li>
  <li>placeholder presentation, when supported, remains realization-facing and does not replace the actual primary value.</li>
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

<hr/>

<h2 id="common-realization-expectations">9. Common Realization Expectations</h2>

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
In particular:
</p>

<ul>
  <li>realization MAY define where string text is rendered,</li>
  <li>realization MAY define borders, frames, anchors, or text regions,</li>
  <li>realization MAY define compatible family, variant, or skin identities,</li>
  <li>realization MUST NOT redefine the public owner of <code>value</code> or <code>label.text</code>,</li>
  <li>realization MUST NOT make asset-baked strings the only semantic source of visible text meaning.</li>
</ul>

<hr/>

<h2 id="diagram-interaction-posture">10. Diagram Interaction Posture</h2>

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
Typical legal object-style surfaces include:
</p>

<ul>
  <li><code>value</code></li>
  <li><code>label.text</code></li>
  <li><code>interaction.enabled</code></li>
  <li><code>interaction.visible</code></li>
  <li><code>placeholder.text</code> when exposed</li>
  <li><code>format.max_length</code> when exposed</li>
  <li>portable <code>style.*</code> properties when publicly exposed</li>
  <li>realization-selection members when publicly exposed</li>
</ul>

<hr/>

<h2 id="validation-expectations">11. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>non-string <code>value_type</code> on string widgets,</li>
  <li>role/class mismatches,</li>
  <li>attempts to use unsupported members,</li>
  <li>attempts to treat placeholder presentation as the actual primary value,</li>
  <li>attempts to address realization-only anchors, text regions, selection internals, or caret internals through <code>frog.ui.*</code> as if they were public members,</li>
  <li>attempts to use styling or skin-selection surfaces to imply a distinct string class contract without explicit class publication.</li>
</ul>

<hr/>

<h2 id="summary">12. Summary</h2>

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
