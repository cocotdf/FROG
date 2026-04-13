<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Path Widgets</h1>

<p align="center">
  <strong>Normative baseline for standardized path control and path indicator widget classes</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#classes-defined-here">2. Classes Defined Here</a></li>
  <li><a href="#common-family-posture">3. Common Family Posture</a></li>
  <li><a href="#frogwidgetspath_control">4. <code>frog.widgets.path_control</code></a></li>
  <li><a href="#frogwidgetspath_indicator">5. <code>frog.widgets.path_indicator</code></a></li>
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
This document defines the intrinsic standardized baseline for path widgets in FROG.
</p>

<p>
The path family provides the first path-typed widgets used for editable path selection and displayed path output in the portable front-panel baseline.
These classes remain close to the string family in visible form, but they carry stronger semantic meaning than arbitrary text.
</p>

<p>
The standard path family is therefore defined here as a real object surface with:
</p>

<ul>
  <li>a primary path value posture,</li>
  <li>a minimal but real property surface,</li>
  <li>a minimal but real method surface,</li>
  <li>a minimal but real event surface,</li>
  <li>a stable public part model for realization targeting.</li>
</ul>

<p>
The intrinsic baseline does not standardize a full file-browser, filesystem API, or host dialog specification.
It standardizes a path-typed widget family with minimal interoperable behavior.
</p>

<hr/>

<h2 id="classes-defined-here">2. Classes Defined Here</h2>

<p>
This document defines the following standardized widget classes:
</p>

<ul>
  <li><code>frog.widgets.path_control</code></li>
  <li><code>frog.widgets.path_indicator</code></li>
</ul>

<hr/>

<h2 id="common-family-posture">3. Common Family Posture</h2>

<p>
The path family has the following common posture:
</p>

<ul>
  <li>family: path widget family</li>
  <li>primary value: present</li>
  <li>value type: <code>path</code></li>
  <li>natural value participation: yes</li>
  <li>object-style access: yes</li>
  <li>primary value mirror property: <code>value</code></li>
  <li>common label property: <code>label.text</code></li>
  <li>common visibility property: <code>interaction.visible</code></li>
</ul>

<p>
The path family also follows an important architectural rule:
</p>

<ul>
  <li><code>value</code> is class-owned semantic path data,</li>
  <li><code>label.text</code> is class-owned semantic label text,</li>
  <li><code>path_display</code> is a stable public dynamic part,</li>
  <li>browse buttons, host dialogs, clipping rules, ellipsis posture, and decorative embodiment belong downstream to realization unless explicitly standardized as public class surfaces.</li>
</ul>

<hr/>

<h2 id="frogwidgetspath_control">4. <code>frog.widgets.path_control</code></h2>

<h3>4.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.path_control</code></li>
  <li><strong>family:</strong> <code>path_widget</code></li>
  <li><strong>compatible role:</strong> <code>control</code></li>
</ul>

<h3>4.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>value type: <code>path</code></li>
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
  <li><code>path.mode</code> — optional readable and writable hint such as file-oriented or directory-oriented selection posture when the active class posture exposes it</li>
</ul>

<h3>4.4 Standard methods</h3>

<ul>
  <li><code>focus()</code></li>
  <li><code>browse()</code> when the active class posture exposes a host-assisted browsing interaction</li>
  <li><code>clear()</code></li>
  <li><code>reset_to_default()</code> when a default value exists</li>
</ul>

<h3>4.5 Standard events</h3>

<ul>
  <li><code>value_changed</code></li>
  <li><code>browsing_started</code> when the active class posture exposes a browse interaction</li>
  <li><code>browsing_committed</code> when the active class posture exposes a browse interaction</li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<h3>4.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>path_display</code></li>
  <li><code>browse_button</code> when the active realization exposes it</li>
  <li><code>frame</code> when present</li>
</ul>

<hr/>

<h2 id="frogwidgetspath_indicator">5. <code>frog.widgets.path_indicator</code></h2>

<h3>5.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.path_indicator</code></li>
  <li><strong>family:</strong> <code>path_widget</code></li>
  <li><strong>compatible role:</strong> <code>indicator</code></li>
</ul>

<h3>5.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>value type: <code>path</code></li>
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
  <li><code>path.mode</code> — optional readable and writable path-kind hint when the active class posture exposes it</li>
</ul>

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
  <li><code>path_display</code></li>
  <li><code>frame</code> when present</li>
</ul>

<hr/>

<h2 id="common-parts">6. Common Parts</h2>

<p>
The path family uses the following common stable parts:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>path_display</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The optional <code>browse_button</code> part may exist in realizations that expose explicit browse affordance, but the intrinsic class law does not require one mandatory browse embodiment.
</p>

<p>
This distinction is important:
</p>

<ul>
  <li><code>path_display</code> is a public part of the class model,</li>
  <li>browse dialogs, popup pickers, clipping helpers, ellipsis posture, and decorative assets belong to realization unless explicitly promoted to class law.</li>
</ul>

<hr/>

<h2 id="common-behavior-expectations">7. Common Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the path family includes at least:
</p>

<ul>
  <li>the primary value remains of type <code>path</code>,</li>
  <li>path controls accept user-originated editing or path selection only when enabled,</li>
  <li>path changes may emit <code>value_changed</code>,</li>
  <li>host-assisted browsing, when exposed, may emit <code>browsing_started</code> and <code>browsing_committed</code>,</li>
  <li>indicator-side visual refresh may emit <code>value_rendered</code>.</li>
</ul>

<p>
The family also preserves the distinction between:
</p>

<ul>
  <li>semantic path value owned by <code>value</code>,</li>
  <li>semantic label text owned by <code>label.text</code>,</li>
  <li>dynamic public display surface exposed through <code>path_display</code>,</li>
  <li>downstream visual embodiment owned by realization.</li>
</ul>

<hr/>

<h2 id="common-realization-expectations">8. Common Realization Expectations</h2>

<p>
A conforming realization of the path family SHOULD provide:
</p>

<ul>
  <li>a visible path display surface,</li>
  <li>optional visible label support,</li>
  <li>reasonable visual distinction between control and indicator posture,</li>
  <li>part-to-visual mapping for the published parts.</li>
</ul>

<p>
The realization MAY be text-entry-like, browse-assisted, or another host-compatible path embodiment, provided the published public class surface remains preserved.
</p>

<p>
In particular:
</p>

<ul>
  <li>realization MAY define browse buttons, clipping helpers, path shortening rules, or decorative frames,</li>
  <li>realization MUST NOT redefine the semantic owner of <code>value</code> or <code>label.text</code>,</li>
  <li>realization MUST NOT make placeholder path text, preview text, or host-private browse state the only semantic source of visible path meaning.</li>
</ul>

<hr/>

<h2 id="diagram-interaction-posture">9. Diagram Interaction Posture</h2>

<p>
The path family supports:
</p>

<ul>
  <li>natural value participation through <code>widget_value</code>,</li>
  <li>property access through <code>frog.ui.property_read</code> and <code>frog.ui.property_write</code>,</li>
  <li>method invocation where legal,</li>
  <li>event observation where legal.</li>
</ul>

<p>
When the program intent is ordinary path dataflow, the natural value path SHOULD be preferred.
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
  <li><code>path.mode</code> when exposed</li>
</ul>

<p>
Realization-only browse helpers, popup pickers, resource layers, and asset helpers remain outside the public path class surface unless explicitly standardized elsewhere.
</p>

<hr/>

<h2 id="validation-expectations">10. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>non-path <code>value_type</code> on path widgets,</li>
  <li>role/class mismatches,</li>
  <li>attempts to write user-edit surfaces on indicator-only classes where forbidden,</li>
  <li>unknown path family members or parts,</li>
  <li>attempts to treat realization-only browse helpers or host-private picker structures as public class members by default.</li>
</ul>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
The path widget family defines the intrinsic standardized path-value widget baseline of FROG:
</p>

<ul>
  <li><code>frog.widgets.path_control</code></li>
  <li><code>frog.widgets.path_indicator</code></li>
</ul>

<p>
These classes provide the first standard portable path interaction and display surfaces of the extended widget baseline.
They expose a real minimal object surface with properties, methods, events, and parts while keeping realization ownership and runtime-private embodiment clearly separated from class meaning.
</p>
