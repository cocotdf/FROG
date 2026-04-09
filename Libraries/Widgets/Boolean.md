<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Boolean Widgets</h1>

<p align="center">
  <strong>Normative baseline for standardized boolean control and boolean indicator widget classes</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#classes-defined-here">2. Classes Defined Here</a></li>
  <li><a href="#common-family-posture">3. Common Family Posture</a></li>
  <li><a href="#frogwidgetsboolean_control">4. <code>frog.widgets.boolean_control</code></a></li>
  <li><a href="#frogwidgetsboolean_indicator">5. <code>frog.widgets.boolean_indicator</code></a></li>
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
This document defines the intrinsic standardized baseline for boolean widgets in FROG.
</p>

<p>
The boolean family provides the standard widget surfaces used for logical true/false interaction and true/false display.
These classes are intentionally simple, portable, and sufficient for the minimal reusable front-panel baseline.
</p>

<hr/>

<h2 id="classes-defined-here">2. Classes Defined Here</h2>

<p>
This document defines the following standardized widget classes:
</p>

<ul>
  <li><code>frog.widgets.boolean_control</code></li>
  <li><code>frog.widgets.boolean_indicator</code></li>
</ul>

<hr/>

<h2 id="common-family-posture">3. Common Family Posture</h2>

<p>
The boolean family has the following common posture:
</p>

<ul>
  <li>primary value: present</li>
  <li>value type: <code>bool</code></li>
  <li>public value-facing surface: yes</li>
  <li>object-style access surface: yes</li>
  <li>compatible roles: according to class identity</li>
</ul>

<p>
The boolean family is not a tri-state baseline in the intrinsic core.
It is a true/false baseline.
Future profile-owned or extended classes MAY add richer logical-state surfaces, but this document remains limited to the portable intrinsic boolean case.
</p>

<hr/>

<h2 id="frogwidgetsboolean_control">4. <code>frog.widgets.boolean_control</code></h2>

<h3>4.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.boolean_control</code></li>
  <li><strong>category:</strong> <code>control</code></li>
  <li><strong>compatible role:</strong> <code>control</code></li>
</ul>

<h3>4.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>value type: <code>bool</code></li>
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
  <li><code>style.on_color</code> when supported by the standard family realization posture</li>
  <li><code>style.off_color</code> when supported by the standard family realization posture</li>
</ul>

<h3>4.4 Standard methods</h3>

<ul>
  <li><code>focus()</code></li>
  <li><code>toggle()</code></li>
  <li><code>set_true()</code></li>
  <li><code>set_false()</code></li>
</ul>

<h3>4.5 Standard events</h3>

<ul>
  <li><code>value_changed</code></li>
  <li><code>pressed</code> when supported by the active realization posture</li>
  <li><code>released</code> when supported by the active realization posture</li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<h3>4.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>state_face</code></li>
  <li><code>frame</code> when present</li>
</ul>

<hr/>

<h2 id="frogwidgetsboolean_indicator">5. <code>frog.widgets.boolean_indicator</code></h2>

<h3>5.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.boolean_indicator</code></li>
  <li><strong>category:</strong> <code>indicator</code></li>
  <li><strong>compatible role:</strong> <code>indicator</code></li>
</ul>

<h3>5.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>value type: <code>bool</code></li>
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
  <li><code>style.on_color</code> when supported</li>
  <li><code>style.off_color</code> when supported</li>
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
  <li><code>state_face</code></li>
  <li><code>frame</code> when present</li>
</ul>

<hr/>

<h2 id="common-parts">6. Common Parts</h2>

<p>
The boolean family uses the following common stable parts:
</p>

<ul>
  <li><code>root</code> — owning widget root</li>
  <li><code>label</code> — optional label surface</li>
  <li><code>state_face</code> — visual state surface representing true/false posture</li>
  <li><code>frame</code> — optional framing surface</li>
</ul>

<hr/>

<h2 id="common-behavior-expectations">7. Common Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the boolean family includes at least:
</p>

<ul>
  <li>the primary value remains boolean,</li>
  <li>boolean controls accept user-originated toggling only when enabled,</li>
  <li>boolean value transitions may emit <code>value_changed</code>,</li>
  <li>indicator realizations may emit <code>value_rendered</code> when their visible state is refreshed,</li>
  <li>the visual state surface follows the current boolean value posture.</li>
</ul>

<hr/>

<h2 id="common-realization-expectations">8. Common Realization Expectations</h2>

<p>
A conforming realization of the boolean family SHOULD provide:
</p>

<ul>
  <li>a visible distinction between true and false states,</li>
  <li>optional visible label support,</li>
  <li>state-specific visual feedback for controls where appropriate,</li>
  <li>part-to-visual mapping for the published parts.</li>
</ul>

<p>
The realization MAY be checkbox-like, switch-like, LED-like, or another host-compatible boolean embodiment, provided that the published public class surface remains preserved.
</p>

<hr/>

<h2 id="diagram-interaction-posture">9. Diagram Interaction Posture</h2>

<p>
The boolean family supports:
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
  <li>non-boolean <code>value_type</code> on boolean widgets,</li>
  <li>role/class mismatches,</li>
  <li>attempts to write user-edit surfaces on indicator-only classes where forbidden,</li>
  <li>unknown boolean family members or parts.</li>
</ul>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
The boolean widget family defines the intrinsic standardized true/false widget baseline of FROG:
</p>

<ul>
  <li><code>frog.widgets.boolean_control</code></li>
  <li><code>frog.widgets.boolean_indicator</code></li>
</ul>

<p>
These classes provide the standard portable boolean interaction and display surfaces of the minimal widget core.
</p>
