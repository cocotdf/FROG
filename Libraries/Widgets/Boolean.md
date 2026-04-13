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

<p>
The standard boolean family is therefore defined here as a real object surface with:
</p>

<ul>
  <li>a primary boolean value posture,</li>
  <li>a minimal but real property surface,</li>
  <li>a minimal but real method surface,</li>
  <li>a minimal but real event surface,</li>
  <li>a stable public part model for realization targeting.</li>
</ul>

<p>
This keeps the intrinsic baseline close in spirit to mature graphical systems such as LabVIEW while remaining smaller and more portable.
</p>

<p>
The intrinsic boolean baseline is strictly true/false.
It does not standardize a tri-state boolean model in the intrinsic core.
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
  <li>family: scalar boolean widget family</li>
  <li>primary value: present</li>
  <li>value type: <code>bool</code></li>
  <li>public value-facing surface: yes</li>
  <li>object-style access surface: yes</li>
  <li>primary value mirror property: <code>value</code></li>
  <li>common label property: <code>label.text</code></li>
  <li>common visibility property: <code>interaction.visible</code></li>
</ul>

<p>
The boolean family also follows an important architectural rule:
</p>

<ul>
  <li><code>value</code> is class-owned semantic boolean data,</li>
  <li><code>label.text</code> is class-owned semantic label text,</li>
  <li><code>state_face</code> is a stable public dynamic part,</li>
  <li>the visual embodiment of true, false, focus, or press posture belongs downstream to realization.</li>
</ul>

<p>
This means the intrinsic core standardizes one boolean family, not one fixed visual embodiment.
Checkbox-like, switch-like, LED-like, and similar host embodiments are realization strategies unless promoted later into separate explicit widget classes.
</p>

<hr/>

<h2 id="frogwidgetsboolean_control">4. <code>frog.widgets.boolean_control</code></h2>

<h3>4.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.boolean_control</code></li>
  <li><strong>family:</strong> <code>boolean_widget</code></li>
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
  <li><code>value</code> — readable and writable</li>
  <li><code>label.text</code> — readable and writable</li>
  <li><code>interaction.enabled</code> — readable and writable</li>
  <li><code>interaction.visible</code> — readable and writable</li>
</ul>

<p>
These properties define the minimum public object surface of the intrinsic boolean control.
They do not expose realization-private anchors, state maps, skin layers, glow helpers, or toolkit-private interaction internals as if they were public class members.
</p>

<h3>4.4 Standard methods</h3>

<ul>
  <li><code>focus()</code></li>
  <li><code>toggle()</code></li>
  <li><code>set_true()</code></li>
  <li><code>set_false()</code></li>
</ul>

<p>
The baseline method surface is intentionally small.
It exists to guarantee that the boolean control remains a real object with a minimal action surface rather than a bare true/false glyph.
</p>

<h3>4.5 Standard events</h3>

<ul>
  <li><code>value_changed</code></li>
  <li><code>pressed</code> when supported by the active class posture</li>
  <li><code>released</code> when supported by the active class posture</li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<p>
The <code>pressed</code> and <code>released</code> events are interaction events.
They do not redefine the semantic boolean value itself.
</p>

<h3>4.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>state_face</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The <code>state_face</code> part is the public dynamic boolean embodiment surface.
Its semantic meaning belongs to the class through <code>value</code>.
Its visual placement and embodiment belong to realization.
</p>

<hr/>

<h2 id="frogwidgetsboolean_indicator">5. <code>frog.widgets.boolean_indicator</code></h2>

<h3>5.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.boolean_indicator</code></li>
  <li><strong>family:</strong> <code>boolean_widget</code></li>
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
  <li><code>reset_to_default()</code> when a default boolean value exists and the active class posture exposes it</li>
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

<p>
The indicator <code>state_face</code> part remains a public dynamic display surface.
It is not merely a decorative skin region.
</p>

<hr/>

<h2 id="common-parts">6. Common Parts</h2>

<p>
The boolean family uses the following common stable parts:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>state_face</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
This distinction is important:
</p>

<ul>
  <li><code>state_face</code> is a public part of the class model,</li>
  <li>state-specific assets, anchors, layer maps, glow helpers, and visual state composition used to embody it belong to realization unless explicitly promoted to class law.</li>
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

<p>
The family also preserves the distinction between:
</p>

<ul>
  <li>semantic boolean value owned by <code>value</code>,</li>
  <li>semantic label text owned by <code>label.text</code>,</li>
  <li>dynamic public state surface exposed through <code>state_face</code>,</li>
  <li>downstream visual embodiment owned by realization.</li>
</ul>

<p>
Pressed posture, focus posture, and host activation feedback remain interaction and realization concerns unless explicitly promoted to additional public class surfaces.
They do not automatically redefine the boolean value itself.
</p>

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

<p>
In particular:
</p>

<ul>
  <li>realization MAY define composed visual states such as normal_true or pressed_false,</li>
  <li>realization MAY define decorative frames, state assets, skins, or focus layers,</li>
  <li>realization MUST NOT redefine the semantic owner of <code>value</code> or <code>label.text</code>,</li>
  <li>realization MUST NOT make baked check marks, host-private LED state, or decorative assets the only semantic source of visible boolean meaning.</li>
</ul>

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

<p>
When the program intent is ordinary boolean dataflow, the natural value path SHOULD be preferred.
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
</ul>

<p>
Realization-only anchors, state maps, resource layers, focus helpers, and asset helpers remain outside the public boolean class surface unless explicitly standardized elsewhere.
</p>

<hr/>

<h2 id="validation-expectations">10. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>non-boolean <code>value_type</code> on boolean widgets,</li>
  <li>role/class mismatches,</li>
  <li>attempts to write user-edit surfaces on indicator-only classes where forbidden,</li>
  <li>unknown boolean family members or parts,</li>
  <li>attempts to treat realization-only state composition or placement surfaces as public class members by default.</li>
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
They expose a real minimal object surface with properties, methods, events, and parts while keeping realization ownership and runtime-private embodiment clearly separated from class meaning.
</p>
