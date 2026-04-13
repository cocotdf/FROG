<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Listbox Widgets</h1>

<p align="center">
  <strong>Normative baseline for standardized listbox control and listbox indicator widget classes</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#classes-defined-here">2. Classes Defined Here</a></li>
  <li><a href="#common-family-posture">3. Common Family Posture</a></li>
  <li><a href="#selection-model">4. Selection Model</a></li>
  <li><a href="#frogwidgetslistbox_control">5. <code>frog.widgets.listbox_control</code></a></li>
  <li><a href="#frogwidgetslistbox_indicator">6. <code>frog.widgets.listbox_indicator</code></a></li>
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
This document defines the intrinsic standardized baseline for listbox widgets in FROG.
</p>

<p>
The listbox family provides the standard widget surfaces used for explicit selection from an ordered finite item inventory through a persistent visible item list.
These classes are intentionally modest, portable, and sufficient for the first standardized discrete-selection widget family beyond enum.
</p>

<p>
The standard listbox family is therefore defined here as a real object surface with:
</p>

<ul>
  <li>a primary selection value posture,</li>
  <li>a finite ordered item inventory,</li>
  <li>a minimal but real property surface,</li>
  <li>a minimal but real method surface,</li>
  <li>a minimal but real event surface,</li>
  <li>a stable public part model for realization targeting.</li>
</ul>

<p>
The intrinsic listbox baseline remains intentionally conservative.
It standardizes a single-selection model first and does not attempt to standardize multi-selection, tree-like hierarchy, tabular selection, or virtualized mega-list behavior in the intrinsic core.
</p>

<hr/>

<h2 id="classes-defined-here">2. Classes Defined Here</h2>

<p>
This document defines the following standardized widget classes:
</p>

<ul>
  <li><code>frog.widgets.listbox_control</code></li>
  <li><code>frog.widgets.listbox_indicator</code></li>
</ul>

<hr/>

<h2 id="common-family-posture">3. Common Family Posture</h2>

<p>
The listbox family has the following common posture:
</p>

<ul>
  <li>family: discrete selection widget family</li>
  <li>primary value: present</li>
  <li>public value-facing surface: yes</li>
  <li>object-style access surface: yes</li>
  <li>primary value mirror property: <code>value</code></li>
  <li>selection index surface: <code>selection.index</code></li>
  <li>item inventory surface: <code>items</code></li>
  <li>common label property: <code>label.text</code></li>
  <li>common visibility property: <code>interaction.visible</code></li>
</ul>

<p>
The listbox family follows an important architectural rule:
</p>

<ul>
  <li><code>items</code> is class-owned item inventory data,</li>
  <li><code>value</code> is class-owned semantic selected value,</li>
  <li><code>selection.index</code> is class-owned selection-position metadata,</li>
  <li><code>label.text</code> is class-owned semantic label text,</li>
  <li><code>item_region</code> and <code>selection_face</code> are stable public dynamic parts,</li>
  <li>the visual embodiment of rows, focus, highlight, or scroll posture belongs downstream to realization.</li>
</ul>

<p>
This means the intrinsic core standardizes one listbox family, not one fixed host widget shape.
Single-column list embodiments, flat menu-like list embodiments, and other compatible visible embodiments remain realization strategies unless promoted later into separate explicit widget classes.
</p>

<hr/>

<h2 id="selection-model">4. Selection Model</h2>

<h3>4.1 Single-selection baseline</h3>

<p>
The intrinsic listbox baseline is single-selection.
At any given time, the widget exposes at most one selected item in its public selection surface.
</p>

<p>
This means the intrinsic baseline does not standardize:
</p>

<ul>
  <li>multiple simultaneous selected items,</li>
  <li>range selection,</li>
  <li>checkbox-in-list semantics,</li>
  <li>hierarchical expansion semantics,</li>
  <li>table-like row/column selection.</li>
</ul>

<h3>4.2 Value versus selection index</h3>

<p>
The preferred public semantic posture is:
</p>

<ul>
  <li><code>value</code> — the semantic selected value,</li>
  <li><code>selection.index</code> — the selected item position in the current ordered item inventory,</li>
  <li><code>items</code> — the ordered item inventory from which the selection is made.</li>
</ul>

<p>
This distinction is normative.
The intrinsic listbox baseline does not reduce the widget to an integer index alone.
The index remains important and public, but it is auxiliary to the semantic selection value rather than replacing it.
</p>

<h3>4.3 Empty selection posture</h3>

<p>
The intrinsic baseline does not require that the widget always have a selected item.
A class posture or host implementation may allow the absence of current selection where that remains explicitly represented and valid.
</p>

<p>
When no item is selected:
</p>

<ul>
  <li><code>selection.index</code> may be absent or use a documented no-selection posture,</li>
  <li><code>value</code> may be absent or use a documented no-selection posture,</li>
  <li>the realization must not silently invent a hidden selection.</li>
</ul>

<p>
Validators and implementations must keep this posture explicit.
</p>

<hr/>

<h2 id="frogwidgetslistbox_control">5. <code>frog.widgets.listbox_control</code></h2>

<h3>5.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.listbox_control</code></li>
  <li><strong>family:</strong> <code>listbox_widget</code></li>
  <li><strong>compatible role:</strong> <code>control</code></li>
</ul>

<h3>5.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>natural value participation: yes</li>
  <li>user-mutable: yes</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
  <li>selection index mirror property: <code>selection.index</code></li>
</ul>

<h3>5.3 Standard properties</h3>

<ul>
  <li><code>items</code> — readable and writable ordered item inventory</li>
  <li><code>value</code> — readable and writable semantic selected value</li>
  <li><code>selection.index</code> — readable and writable selected index when selection exists</li>
  <li><code>label.text</code> — readable and writable</li>
  <li><code>interaction.enabled</code> — readable and writable</li>
  <li><code>interaction.visible</code> — readable and writable</li>
</ul>

<p>
These properties define the minimum public object surface of the intrinsic listbox control.
They do not expose realization-private scroll bars, row caches, host-native item views, or toolkit-private selection helpers as if they were public class members.
</p>

<h3>5.4 Standard methods</h3>

<ul>
  <li><code>focus()</code></li>
  <li><code>select_next()</code></li>
  <li><code>select_previous()</code></li>
  <li><code>set_selected_index(index)</code></li>
  <li><code>clear_selection()</code> when the active class posture allows no-selection state</li>
</ul>

<p>
The baseline method surface is intentionally small.
It exists to guarantee that the listbox control remains a real selection object with explicit action surfaces rather than a passive rendered item list.
</p>

<h3>5.5 Standard events</h3>

<ul>
  <li><code>selection_changed</code></li>
  <li><code>value_changed</code></li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<p>
The baseline allows both <code>selection_changed</code> and <code>value_changed</code> because selection movement and semantic selected-value change are closely related but should remain distinguishable at the object surface.
</p>

<h3>5.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>item_region</code></li>
  <li><code>selection_face</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The <code>item_region</code> part is the public dynamic item-list embodiment surface.
The <code>selection_face</code> part is the public dynamic selected-item emphasis surface.
Their semantic meaning belongs to the class through <code>items</code>, <code>value</code>, and <code>selection.index</code>.
Their visual placement and embodiment belong to realization.
</p>

<hr/>

<h2 id="frogwidgetslistbox_indicator">6. <code>frog.widgets.listbox_indicator</code></h2>

<h3>6.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.listbox_indicator</code></li>
  <li><strong>family:</strong> <code>listbox_widget</code></li>
  <li><strong>compatible role:</strong> <code>indicator</code></li>
</ul>

<h3>6.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>natural value participation: yes</li>
  <li>user-mutable: no in the standard portable posture</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
  <li>selection index mirror property: <code>selection.index</code></li>
</ul>

<h3>6.3 Standard properties</h3>

<ul>
  <li><code>items</code> — readable and writable ordered item inventory where legal</li>
  <li><code>value</code> — readable and writable for diagram/runtime update surfaces where legal</li>
  <li><code>selection.index</code> — readable and writable for diagram/runtime update surfaces where legal</li>
  <li><code>label.text</code> — readable and writable</li>
  <li><code>interaction.visible</code> — readable and writable</li>
</ul>

<p>
The indicator remains a real object even though it is display-oriented.
Its public surface is intentionally smaller than that of the control.
</p>

<h3>6.4 Standard methods</h3>

<ul>
  <li><code>focus()</code> when supported by the host</li>
  <li><code>set_selected_index(index)</code> where diagram-side indicator update surfaces are legal</li>
  <li><code>clear_selection()</code> when the active class posture allows no-selection state</li>
</ul>

<h3>6.5 Standard events</h3>

<ul>
  <li><code>selection_rendered</code></li>
  <li><code>value_rendered</code></li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<h3>6.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>item_region</code></li>
  <li><code>selection_face</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The indicator <code>item_region</code> and <code>selection_face</code> parts remain public dynamic display surfaces.
They are not merely decorative skin regions.
</p>

<hr/>

<h2 id="common-parts">7. Common Parts</h2>

<p>
The listbox family uses the following common stable parts:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>item_region</code></li>
  <li><code>selection_face</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
This distinction is important:
</p>

<ul>
  <li><code>item_region</code> is a public part of the class model,</li>
  <li><code>selection_face</code> is a public part of the class model,</li>
  <li>row layouts, scroll helpers, row separators, hover emphasis, and host-native list containers used to embody them belong to realization unless explicitly promoted to class law.</li>
</ul>

<hr/>

<h2 id="common-behavior-expectations">8. Common Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the listbox family includes at least:
</p>

<ul>
  <li>selection remains constrained to the published ordered item inventory,</li>
  <li>selection index, when present, remains consistent with the current item inventory,</li>
  <li>listbox controls accept user-originated selection changes only when enabled,</li>
  <li>selection transitions may emit <code>selection_changed</code> or <code>value_changed</code>,</li>
  <li>indicator realizations may emit <code>selection_rendered</code> or <code>value_rendered</code> when their visible state is refreshed.</li>
</ul>

<p>
The family also preserves the distinction between:
</p>

<ul>
  <li>semantic selected value owned by <code>value</code>,</li>
  <li>selection position metadata owned by <code>selection.index</code>,</li>
  <li>semantic label text owned by <code>label.text</code>,</li>
  <li>dynamic public item and selection surfaces exposed through <code>item_region</code> and <code>selection_face</code>,</li>
  <li>downstream visual embodiment owned by realization.</li>
</ul>

<p>
Scroll posture, row hover posture, visible row virtualization, and host navigation feedback remain realization concerns unless explicitly promoted to additional public class surfaces.
</p>

<hr/>

<h2 id="common-realization-expectations">9. Common Realization Expectations</h2>

<p>
A conforming realization of the listbox family SHOULD provide:
</p>

<ul>
  <li>a visible ordered item list,</li>
  <li>a visible distinction for the currently selected item when selection exists,</li>
  <li>optional visible label support,</li>
  <li>reasonable focus indication for controls where appropriate,</li>
  <li>part-to-visual mapping for the published parts.</li>
</ul>

<p>
The realization MAY be flat-list-like, menu-list-like, or another host-compatible list embodiment, provided that the published public class surface remains preserved.
</p>

<p>
In particular:
</p>

<ul>
  <li>realization MAY define item-row assets, selection highlight assets, focus layers, or scroll affordances,</li>
  <li>realization MUST NOT redefine the semantic owner of <code>items</code>, <code>value</code>, <code>selection.index</code>, or <code>label.text</code>,</li>
  <li>realization MUST NOT make baked row text, host-private row caches, or decorative assets the only semantic source of visible selection meaning.</li>
</ul>

<hr/>

<h2 id="diagram-interaction-posture">10. Diagram Interaction Posture</h2>

<p>
The listbox family supports:
</p>

<ul>
  <li>natural value participation through <code>widget_value</code>,</li>
  <li>property access through <code>frog.ui.property_read</code> and <code>frog.ui.property_write</code>,</li>
  <li>method invocation where legal,</li>
  <li>event observation where legal.</li>
</ul>

<p>
When the program intent is ordinary selected-value dataflow, the natural value path SHOULD be preferred.
Object-style access remains available for richer widget interaction.
</p>

<p>
Typical legal object-style surfaces include:
</p>

<ul>
  <li><code>items</code></li>
  <li><code>value</code></li>
  <li><code>selection.index</code></li>
  <li><code>label.text</code></li>
  <li><code>interaction.enabled</code></li>
  <li><code>interaction.visible</code></li>
</ul>

<p>
Realization-only row layouts, hover layers, scroll bars, focus helpers, and asset helpers remain outside the public listbox class surface unless explicitly standardized elsewhere.
</p>

<hr/>

<h2 id="validation-expectations">11. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>role/class mismatches,</li>
  <li>attempts to use unsupported multi-selection semantics in the intrinsic baseline,</li>
  <li>selection indices outside the valid item range,</li>
  <li>inconsistent selection posture between <code>value</code> and <code>selection.index</code>,</li>
  <li>attempts to write user-edit surfaces on indicator-only classes where forbidden,</li>
  <li>unknown listbox family members or parts,</li>
  <li>attempts to treat realization-only row, scroll, or placement surfaces as public class members by default.</li>
</ul>

<hr/>

<h2 id="summary">12. Summary</h2>

<p>
The listbox widget family defines the intrinsic standardized single-selection list widget baseline of FROG:
</p>

<ul>
  <li><code>frog.widgets.listbox_control</code></li>
  <li><code>frog.widgets.listbox_indicator</code></li>
</ul>

<p>
These classes provide the first standard portable persistent-item-list selection surfaces beyond enum.
They expose a real minimal object surface with properties, methods, events, and parts while keeping realization ownership and runtime-private embodiment clearly separated from class meaning.
</p>
