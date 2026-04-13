<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Enum Widgets</h1>

<p align="center">
  <strong>Normative baseline for standardized enum control and enum indicator widget classes</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#classes-defined-here">2. Classes Defined Here</a></li>
  <li><a href="#common-family-posture">3. Common Family Posture</a></li>
  <li><a href="#frogwidgetsenum_control">4. <code>frog.widgets.enum_control</code></a></li>
  <li><a href="#frogwidgetsenum_indicator">5. <code>frog.widgets.enum_indicator</code></a></li>
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
This document defines the intrinsic standardized baseline for enum widgets in FROG.
</p>

<p>
The enum family provides the first discrete named-value widgets used for selecting and displaying one value from a finite declared item set.
These classes are intended to remain small, portable, inspectable, and coherent with the rest of the intrinsic widget baseline.
</p>

<p>
The standard enum family is therefore defined here as a real object surface with:
</p>

<ul>
  <li>a primary discrete value posture,</li>
  <li>a minimal but real property surface,</li>
  <li>a minimal but real method surface,</li>
  <li>a minimal but real event surface,</li>
  <li>a stable public part model for realization targeting.</li>
</ul>

<p>
This baseline is intentionally conservative.
It standardizes a finite single-selection enum widget family, not a general-purpose listbox, tree selector, or arbitrary collection-selection system.
</p>

<hr/>

<h2 id="classes-defined-here">2. Classes Defined Here</h2>

<p>
This document defines the following standardized widget classes:
</p>

<ul>
  <li><code>frog.widgets.enum_control</code></li>
  <li><code>frog.widgets.enum_indicator</code></li>
</ul>

<hr/>

<h2 id="common-family-posture">3. Common Family Posture</h2>

<p>
The enum family has the following common posture:
</p>

<ul>
  <li>family: discrete named-value widget family</li>
  <li>primary value: present</li>
  <li>primary value kind: one item from a finite declared set</li>
  <li>natural value participation: yes</li>
  <li>object-style access: yes</li>
  <li>primary value mirror property: <code>value</code></li>
  <li>common item-set property: <code>items</code></li>
  <li>common label property: <code>label.text</code></li>
  <li>common visibility property: <code>interaction.visible</code></li>
</ul>

<p>
The enum family also follows an important architectural rule:
</p>

<ul>
  <li><code>value</code> is class-owned semantic discrete data,</li>
  <li><code>items</code> defines the legal finite item inventory,</li>
  <li><code>label.text</code> is class-owned semantic label text,</li>
  <li><code>value_display</code> is a stable public dynamic part,</li>
  <li>dropdown regions, ring visuals, arrows, popup menus, and similar embodiment details belong downstream to realization.</li>
</ul>

<p>
The intrinsic baseline does not require one single realization style.
A host may realize the enum as ring-like, dropdown-like, selector-like, or another compatible single-selection embodiment, provided the public class meaning remains preserved.
</p>

<hr/>

<h2 id="frogwidgetsenum_control">4. <code>frog.widgets.enum_control</code></h2>

<h3>4.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.enum_control</code></li>
  <li><strong>family:</strong> <code>enum_widget</code></li>
  <li><strong>compatible role:</strong> <code>control</code></li>
</ul>

<h3>4.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>primary value kind: one selected item from the declared item set</li>
  <li>natural value participation: yes</li>
  <li>user-mutable: yes</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
</ul>

<h3>4.3 Standard properties</h3>

<ul>
  <li><code>value</code> — readable and writable</li>
  <li><code>items</code> — readable and writable finite item inventory</li>
  <li><code>label.text</code> — readable and writable</li>
  <li><code>interaction.enabled</code> — readable and writable</li>
  <li><code>interaction.visible</code> — readable and writable</li>
</ul>

<p>
The intrinsic baseline does not require a full item-style or presentation-style system.
If a later standardization layer adds item metadata such as display decoration, localization buckets, icons, or per-item visual styling, that belongs to an expanded class or profile rather than to the intrinsic enum core.
</p>

<h3>4.4 Standard methods</h3>

<ul>
  <li><code>focus()</code></li>
  <li><code>select_next()</code></li>
  <li><code>select_previous()</code></li>
  <li><code>reset_to_default()</code> when a default value exists</li>
</ul>

<h3>4.5 Standard events</h3>

<ul>
  <li><code>value_changed</code></li>
  <li><code>selection_opened</code> when the active class posture exposes an explicit opened-selection interaction</li>
  <li><code>selection_committed</code></li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<h3>4.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>value_display</code></li>
  <li><code>selector_face</code> when the active realization exposes a distinct selector surface</li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The <code>value_display</code> part is the public dynamic selected-value display surface.
Its semantic meaning belongs to the class through <code>value</code> and <code>items</code>.
Its visual placement and embodiment belong to realization.
</p>

<hr/>

<h2 id="frogwidgetsenum_indicator">5. <code>frog.widgets.enum_indicator</code></h2>

<h3>5.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.enum_indicator</code></li>
  <li><strong>family:</strong> <code>enum_widget</code></li>
  <li><strong>compatible role:</strong> <code>indicator</code></li>
</ul>

<h3>5.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>primary value kind: one selected item from the declared item set</li>
  <li>natural value participation: yes</li>
  <li>user-mutable: no in the standard portable posture</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
</ul>

<h3>5.3 Standard properties</h3>

<ul>
  <li><code>value</code> — readable and writable for diagram/runtime update surfaces where legal</li>
  <li><code>items</code> — readable and writable finite item inventory</li>
  <li><code>label.text</code> — readable and writable</li>
  <li><code>interaction.visible</code> — readable and writable</li>
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
  <li><code>value_display</code></li>
  <li><code>frame</code> when present</li>
</ul>

<hr/>

<h2 id="common-parts">6. Common Parts</h2>

<p>
The enum family uses the following common stable parts:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>value_display</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The optional <code>selector_face</code> part may exist in a realization that needs a distinct visible selection affordance.
However, the intrinsic class law does not require one mandatory selector embodiment.
</p>

<p>
This distinction is important:
</p>

<ul>
  <li><code>value_display</code> is a public part of the class model,</li>
  <li>popup regions, list layers, ring visuals, arrows, and realization-specific selection helpers belong to realization unless explicitly promoted to class law.</li>
</ul>

<hr/>

<h2 id="common-behavior-expectations">7. Common Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the enum family includes at least:
</p>

<ul>
  <li>the primary value always belongs to the declared item set,</li>
  <li>enum controls accept user-originated selection change only when enabled,</li>
  <li>selection change may emit <code>value_changed</code>,</li>
  <li>selection commit may emit <code>selection_committed</code>,</li>
  <li>indicator-side visual refresh may emit <code>value_rendered</code>.</li>
</ul>

<p>
The family also preserves the distinction between:
</p>

<ul>
  <li>semantic selected value owned by <code>value</code>,</li>
  <li>semantic item inventory owned by <code>items</code>,</li>
  <li>semantic label text owned by <code>label.text</code>,</li>
  <li>dynamic public display surface exposed through <code>value_display</code>,</li>
  <li>downstream visual embodiment owned by realization.</li>
</ul>

<hr/>

<h2 id="common-realization-expectations">8. Common Realization Expectations</h2>

<p>
A conforming realization of the enum family SHOULD provide:
</p>

<ul>
  <li>a visible selected-value display surface,</li>
  <li>optional visible label support,</li>
  <li>reasonable visual distinction between control and indicator posture,</li>
  <li>part-to-visual mapping for the published parts.</li>
</ul>

<p>
The realization MAY be ring-like, dropdown-like, selector-like, or another host-compatible single-selection embodiment, provided the published public class surface remains preserved.
</p>

<p>
In particular:
</p>

<ul>
  <li>realization MAY define popup or selector-specific visual surfaces,</li>
  <li>realization MAY define decorative frames, arrows, state assets, or skins,</li>
  <li>realization MUST NOT redefine the semantic owner of <code>value</code>, <code>items</code>, or <code>label.text</code>,</li>
  <li>realization MUST NOT make popup-private state or baked presentation text the only semantic source of visible enum meaning.</li>
</ul>

<hr/>

<h2 id="diagram-interaction-posture">9. Diagram Interaction Posture</h2>

<p>
The enum family supports:
</p>

<ul>
  <li>natural value participation through <code>widget_value</code>,</li>
  <li>property access through <code>frog.ui.property_read</code> and <code>frog.ui.property_write</code>,</li>
  <li>method invocation where legal,</li>
  <li>event observation where legal.</li>
</ul>

<p>
When the program intent is ordinary discrete-value dataflow, the natural value path SHOULD be preferred.
Object-style access remains available for richer widget interaction.
</p>

<p>
Typical legal object-style surfaces include:
</p>

<ul>
  <li><code>value</code></li>
  <li><code>items</code></li>
  <li><code>label.text</code></li>
  <li><code>interaction.enabled</code></li>
  <li><code>interaction.visible</code></li>
</ul>

<p>
Realization-only popup layers, selector helpers, anchors, resource layers, and asset helpers remain outside the public enum class surface unless explicitly standardized elsewhere.
</p>

<hr/>

<h2 id="validation-expectations">10. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>enum values that do not belong to the declared item set,</li>
  <li>role/class mismatches,</li>
  <li>attempts to write user-edit surfaces on indicator-only classes where forbidden,</li>
  <li>unknown enum family members or parts,</li>
  <li>duplicate item identifiers in the same enum item set,</li>
  <li>attempts to treat realization-only selection helpers or popup-private structures as public class members by default.</li>
</ul>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
The enum widget family defines the intrinsic standardized discrete named-value widget baseline of FROG:
</p>

<ul>
  <li><code>frog.widgets.enum_control</code></li>
  <li><code>frog.widgets.enum_indicator</code></li>
</ul>

<p>
These classes provide the first standard portable single-selection discrete-value surfaces of the extended widget baseline.
They expose a real minimal object surface with properties, methods, events, and parts while keeping realization ownership and runtime-private embodiment clearly separated from class meaning.
</p>
