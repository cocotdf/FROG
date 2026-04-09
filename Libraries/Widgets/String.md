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
</ul>

<p>
This intrinsic baseline is single-value text oriented.
It does not attempt to standardize a full rich-text, multi-line editor, code editor, or terminal-like widget surface.
Those may be standardized later or introduced through other families or profiles.
</p>

<hr/>

<h2 id="frogwidgetsstring_control">4. <code>frog.widgets.string_control</code></h2>

<h3>4.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.string_control</code></li>
  <li><strong>category:</strong> <code>control</code></li>
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
  <li><code>value</code></li>
  <li><code>label.text</code></li>
  <li><code>interaction.enabled</code></li>
  <li><code>interaction.visible</code></li>
  <li><code>placeholder.text</code> when supported by the realization</li>
  <li><code>format.max_length</code> when supported by the class posture</li>
</ul>

<h3>4.4 Standard methods</h3>

<ul>
  <li><code>focus()</code></li>
  <li><code>clear()</code></li>
  <li><code>reset_to_default()</code> when a default exists</li>
</ul>

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
  <li><code>frame</code></li>
</ul>

<hr/>

<h2 id="frogwidgetsstring_indicator">5. <code>frog.widgets.string_indicator</code></h2>

<h3>5.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.string_indicator</code></li>
  <li><strong>category:</strong> <code>indicator</code></li>
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
  <li><code>value</code></li>
  <li><code>label.text</code></li>
  <li><code>interaction.visible</code></li>
</ul>

<h3>5.4 Standard methods</h3>

<ul>
  <li><code>focus()</code> when supported by the host</li>
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
  <li><code>frame</code></li>
</ul>

<hr/>

<h2 id="common-parts">6. Common Parts</h2>

<p>
The string family uses the following common stable parts:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>text_display</code></li>
  <li><code>frame</code></li>
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
  <li>indicator-side visual refresh may emit <code>value_rendered</code>,</li>
  <li>placeholder presentation, when supported, remains realization-facing and does not replace the actual primary value.</li>
</ul>

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

<hr/>

<h2 id="validation-expectations">10. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>non-string <code>value_type</code> on string widgets,</li>
  <li>role/class mismatches,</li>
  <li>attempts to use unsupported members,</li>
  <li>attempts to treat placeholder presentation as the actual primary value.</li>
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
</p>
