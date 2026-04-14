<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Tab Widgets</h1>

<p align="center">
  <strong>Normative baseline for standardized tab control and tab indicator widget classes</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#classes-defined-here">2. Classes Defined Here</a></li>
  <li><a href="#common-family-posture">3. Common Family Posture</a></li>
  <li><a href="#page-model">4. Page Model</a></li>
  <li><a href="#selection-model">5. Selection Model</a></li>
  <li><a href="#frogwidgetstab_control">6. <code>frog.widgets.tab_control</code></a></li>
  <li><a href="#frogwidgetstab_indicator">7. <code>frog.widgets.tab_indicator</code></a></li>
  <li><a href="#common-parts">8. Common Parts</a></li>
  <li><a href="#common-behavior-expectations">9. Common Behavior Expectations</a></li>
  <li><a href="#common-realization-expectations">10. Common Realization Expectations</a></li>
  <li><a href="#diagram-interaction-posture">11. Diagram Interaction Posture</a></li>
  <li><a href="#validation-expectations">12. Validation Expectations</a></li>
  <li><a href="#summary">13. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the intrinsic standardized baseline for tab widgets in FROG.
</p>

<p>
The tab family provides the standard widget surfaces used for visible page navigation among a finite ordered set of named pages together with one current selected page posture.
These classes are intentionally modest, portable, and sufficient for the first standardized page-navigation widget family in the portable front-panel ecosystem.
</p>

<p>
The standard tab family is therefore defined here as a real object surface with:
</p>

<ul>
  <li>a primary page-selection value posture,</li>
  <li>a visible page-header navigation posture,</li>
  <li>a minimal but real property surface,</li>
  <li>a minimal but real method surface,</li>
  <li>a minimal but real event surface,</li>
  <li>a stable public part model for realization targeting.</li>
</ul>

<p>
The intrinsic tab baseline remains intentionally conservative.
It standardizes finite page selection first and does not attempt to standardize detachable tabs, draggable reorder contracts, closable tabs, nested tab-management systems, or browser-like session models in the intrinsic core.
</p>

<hr/>

<h2 id="classes-defined-here">2. Classes Defined Here</h2>

<p>
This document defines the following standardized widget classes:
</p>

<ul>
  <li><code>frog.widgets.tab_control</code></li>
  <li><code>frog.widgets.tab_indicator</code></li>
</ul>

<hr/>

<h2 id="common-family-posture">3. Common Family Posture</h2>

<p>
The tab family has the following common posture:
</p>

<ul>
  <li>family: page navigation widget family</li>
  <li>primary value: present</li>
  <li>public value-facing surface: yes</li>
  <li>object-style access surface: yes</li>
  <li>primary value mirror property: <code>value</code></li>
  <li>selection index surface: <code>selection.index</code></li>
  <li>page inventory surface: <code>pages</code></li>
  <li>page title inventory surface: <code>pages.titles</code></li>
  <li>common label property: <code>label.text</code></li>
  <li>common visibility property: <code>interaction.visible</code></li>
</ul>

<p>
The tab family follows an important architectural rule:
</p>

<ul>
  <li><code>pages</code> is class-owned page inventory data,</li>
  <li><code>pages.titles</code> is class-owned page-title metadata,</li>
  <li><code>value</code> is class-owned semantic selected page value,</li>
  <li><code>selection.index</code> is class-owned current selected-page position metadata,</li>
  <li><code>label.text</code> is class-owned semantic label text,</li>
  <li><code>tab_header_region</code>, <code>page_region</code>, and <code>selection_face</code> are stable public dynamic parts,</li>
  <li>the visual embodiment of tabs, selected tab emphasis, page chrome, and navigation posture belongs downstream to realization.</li>
</ul>

<p>
This means the intrinsic core standardizes one tab family, not one fixed host tab-strip implementation.
Top tabs, bottom tabs, segmented-tab embodiments, and other compatible visible embodiments remain realization strategies unless promoted later into separate explicit widget classes.
</p>

<hr/>

<h2 id="page-model">4. Page Model</h2>

<h3>4.1 Baseline page posture</h3>

<p>
The intrinsic tab baseline represents a finite ordered page family.
Its primary value surface corresponds to the currently selected page rather than to all visible page content flattened into one scalar field.
</p>

<p>
The exact page payload typing remains governed by the active FROG type system and profile posture.
However, the intrinsic baseline assumes that the selected page remains semantically identifiable through ordered page inventory and selected-page metadata.
</p>

<h3>4.2 Title posture</h3>

<p>
The intrinsic tab baseline allows an explicit page-title inventory through <code>pages.titles</code>.
</p>

<p>
This title surface is public because page-title meaning is user-relevant and must not be reduced to realization-only decorative text.
However, the geometry, visual placement, truncation behavior, and selected-tab emphasis of those titles remain realization concerns unless explicitly standardized elsewhere.
</p>

<h3>4.3 Finite-page posture</h3>

<p>
The intrinsic tab baseline is finite and ordered.
It does not standardize:
</p>

<ul>
  <li>runtime-created ad hoc page sessions,</li>
  <li>detachable floating tabs,</li>
  <li>page drag reorder ownership,</li>
  <li>close buttons or pinned-page semantics,</li>
  <li>browser-like tab history models.</li>
</ul>

<hr/>

<h2 id="selection-model">5. Selection Model</h2>

<h3>5.1 Single-current-page baseline</h3>

<p>
The intrinsic tab baseline standardizes a single current-page selection posture first.
At any given time, the widget exposes exactly one current selected page when the page inventory is non-empty.
</p>

<p>
This means the intrinsic baseline does not standardize:
</p>

<ul>
  <li>multiple simultaneously active pages,</li>
  <li>split-view tab activation,</li>
  <li>multi-selection of tab headers,</li>
  <li>partial selection across page subsets.</li>
</ul>

<h3>5.2 Value versus selection index</h3>

<p>
The preferred public semantic posture is:
</p>

<ul>
  <li><code>value</code> — the semantic selected page value,</li>
  <li><code>selection.index</code> — the selected page position in the ordered page inventory,</li>
  <li><code>pages</code> — the ordered page inventory,</li>
  <li><code>pages.titles</code> — the ordered public title inventory associated with visible page navigation.</li>
</ul>

<p>
This distinction is normative.
The intrinsic tab baseline does not reduce the widget to an integer index alone.
The index remains important and public, but it is auxiliary to the semantic selected page value rather than replacing it.
</p>

<h3>5.3 Empty-page posture</h3>

<p>
The intrinsic baseline does not require that a tab widget always carry a non-empty page inventory.
A class posture or host implementation may allow an empty page family where that remains explicitly represented and valid.
</p>

<p>
When no page exists:
</p>

<ul>
  <li><code>selection.index</code> may be absent or use a documented no-page posture,</li>
  <li><code>value</code> may be absent or use a documented no-page posture,</li>
  <li>the realization must not silently invent a hidden selected page.</li>
</ul>

<hr/>

<h2 id="frogwidgetstab_control">6. <code>frog.widgets.tab_control</code></h2>

<h3>6.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.tab_control</code></li>
  <li><strong>family:</strong> <code>tab_widget</code></li>
  <li><strong>compatible role:</strong> <code>control</code></li>
</ul>

<h3>6.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>natural value participation: yes</li>
  <li>user-mutable: yes</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
  <li>selection index mirror property: <code>selection.index</code></li>
</ul>

<h3>6.3 Standard properties</h3>

<ul>
  <li><code>pages</code> — readable and writable ordered page inventory</li>
  <li><code>pages.titles</code> — readable and writable ordered page-title inventory</li>
  <li><code>value</code> — readable and writable semantic selected page value</li>
  <li><code>selection.index</code> — readable and writable selected page index when selection exists</li>
  <li><code>label.text</code> — readable and writable</li>
  <li><code>interaction.enabled</code> — readable and writable</li>
  <li><code>interaction.visible</code> — readable and writable</li>
</ul>

<p>
These properties define the minimum public object surface of the intrinsic tab control.
They do not expose realization-private hover layers, close icons, animation helpers, layout caches, or toolkit-private page handles as if they were public class members.
</p>

<h3>6.4 Standard methods</h3>

<ul>
  <li><code>focus()</code></li>
  <li><code>select_next()</code></li>
  <li><code>select_previous()</code></li>
  <li><code>set_selected_index(index)</code></li>
  <li><code>clear_selection()</code> when the active class posture allows no-page state</li>
</ul>

<p>
The baseline method surface is intentionally small.
It exists to guarantee that the tab control remains a real navigation object with explicit action surfaces rather than a passive painted header strip.
</p>

<h3>6.5 Standard events</h3>

<ul>
  <li><code>selection_changed</code></li>
  <li><code>value_changed</code></li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<p>
The baseline allows both <code>selection_changed</code> and <code>value_changed</code> because selected-page movement and semantic selected-page value change are closely related but should remain distinguishable at the object surface.
</p>

<h3>6.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>tab_header_region</code></li>
  <li><code>selection_face</code></li>
  <li><code>page_region</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The <code>tab_header_region</code> part is the public dynamic page-navigation header surface.
The <code>selection_face</code> part is the public dynamic selected-tab emphasis surface.
The <code>page_region</code> part is the public dynamic visible selected-page embodiment surface.
Their semantic meaning belongs to the class through <code>pages</code>, <code>pages.titles</code>, <code>value</code>, and <code>selection.index</code>.
Their visual placement and embodiment belong to realization.
</p>

<hr/>

<h2 id="frogwidgetstab_indicator">7. <code>frog.widgets.tab_indicator</code></h2>

<h3>7.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.tab_indicator</code></li>
  <li><strong>family:</strong> <code>tab_widget</code></li>
  <li><strong>compatible role:</strong> <code>indicator</code></li>
</ul>

<h3>7.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>natural value participation: yes</li>
  <li>user-mutable: no in the standard portable posture</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
  <li>selection index mirror property: <code>selection.index</code></li>
</ul>

<h3>7.3 Standard properties</h3>

<ul>
  <li><code>pages</code> — readable and writable ordered page inventory where legal</li>
  <li><code>pages.titles</code> — readable and writable ordered page-title inventory where legal</li>
  <li><code>value</code> — readable and writable for diagram/runtime update surfaces where legal</li>
  <li><code>selection.index</code> — readable and writable for diagram/runtime update surfaces where legal</li>
  <li><code>label.text</code> — readable and writable</li>
  <li><code>interaction.visible</code> — readable and writable</li>
</ul>

<p>
The indicator remains a real object even though it is display-oriented.
Its public surface is intentionally smaller than that of the control.
</p>

<h3>7.4 Standard methods</h3>

<ul>
  <li><code>focus()</code> when supported by the host</li>
  <li><code>set_selected_index(index)</code> where diagram-side indicator update surfaces are legal</li>
  <li><code>clear_selection()</code> when the active class posture allows no-page state</li>
</ul>

<h3>7.5 Standard events</h3>

<ul>
  <li><code>selection_rendered</code></li>
  <li><code>value_rendered</code></li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<h3>7.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>tab_header_region</code></li>
  <li><code>selection_face</code></li>
  <li><code>page_region</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The indicator <code>tab_header_region</code>, <code>selection_face</code>, and <code>page_region</code> parts remain public dynamic display surfaces.
They are not merely decorative skin regions.
</p>

<hr/>

<h2 id="common-parts">8. Common Parts</h2>

<p>
The tab family uses the following common stable parts:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>tab_header_region</code></li>
  <li><code>selection_face</code></li>
  <li><code>page_region</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
This distinction is important:
</p>

<ul>
  <li><code>tab_header_region</code> is a public part of the class model,</li>
  <li><code>selection_face</code> is a public part of the class model,</li>
  <li><code>page_region</code> is a public part of the class model,</li>
  <li>tab chrome, underline emphasis, hover layers, icon adornments, animation helpers, and toolkit-private containers used to embody them belong to realization unless explicitly promoted to class law.</li>
</ul>

<hr/>

<h2 id="common-behavior-expectations">9. Common Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the tab family includes at least:
</p>

<ul>
  <li>selected-page posture remains consistent with the current page inventory,</li>
  <li>page-title inventory, when present, remains consistent with the ordered page structure,</li>
  <li>tab controls accept user-originated page selection changes only when enabled,</li>
  <li>selected-page transitions may emit <code>selection_changed</code> or <code>value_changed</code>,</li>
  <li>indicator realizations may emit <code>selection_rendered</code> or <code>value_rendered</code> when their visible state is refreshed.</li>
</ul>

<p>
The family also preserves the distinction between:
</p>

<ul>
  <li>semantic selected page owned by <code>value</code>,</li>
  <li>selection position metadata owned by <code>selection.index</code>,</li>
  <li>page inventory owned by <code>pages</code>,</li>
  <li>page-title inventory owned by <code>pages.titles</code>,</li>
  <li>semantic label text owned by <code>label.text</code>,</li>
  <li>dynamic public page-navigation surfaces exposed through <code>tab_header_region</code>, <code>selection_face</code>, and <code>page_region</code>,</li>
  <li>downstream visual embodiment owned by realization.</li>
</ul>

<p>
Hover posture, animated transitions, page-close affordances, and tab-strip overflow behavior remain realization concerns unless explicitly promoted to additional public class surfaces.
</p>

<hr/>

<h2 id="common-realization-expectations">10. Common Realization Expectations</h2>

<p>
A conforming realization of the tab family SHOULD provide:
</p>

<ul>
  <li>a visible ordered page-header navigation surface,</li>
  <li>a visible distinction for the currently selected page,</li>
  <li>a visible selected-page content region,</li>
  <li>optional visible label support,</li>
  <li>reasonable focus indication for controls where appropriate,</li>
  <li>part-to-visual mapping for the published parts.</li>
</ul>

<p>
The realization MAY be top-tab-like, bottom-tab-like, segmented-tab-like, or another host-compatible page-navigation embodiment, provided that the published public class surface remains preserved.
</p>

<p>
In particular:
</p>

<ul>
  <li>realization MAY define tab-header assets, selection-emphasis assets, page-surface assets, focus layers, or overflow affordances,</li>
  <li>realization MUST NOT redefine the semantic owner of <code>pages</code>, <code>pages.titles</code>, <code>value</code>, <code>selection.index</code>, or <code>label.text</code>,</li>
  <li>realization MUST NOT make baked tab titles, host-private layout caches, or decorative assets the only semantic source of visible tab meaning.</li>
</ul>

<hr/>

<h2 id="diagram-interaction-posture">11. Diagram Interaction Posture</h2>

<p>
The tab family supports:
</p>

<ul>
  <li>natural value participation through <code>widget_value</code>,</li>
  <li>property access through <code>frog.ui.property_read</code> and <code>frog.ui.property_write</code>,</li>
  <li>method invocation where legal,</li>
  <li>event observation where legal.</li>
</ul>

<p>
When the program intent is ordinary selected-page dataflow, the natural value path SHOULD be preferred.
Object-style access remains available for richer widget interaction.
</p>

<p>
Typical legal object-style surfaces include:
</p>

<ul>
  <li><code>pages</code></li>
  <li><code>pages.titles</code></li>
  <li><code>value</code></li>
  <li><code>selection.index</code></li>
  <li><code>label.text</code></li>
  <li><code>interaction.enabled</code></li>
  <li><code>interaction.visible</code></li>
</ul>

<p>
Realization-only hover layers, close icons, overflow mechanics, animation helpers, and asset helpers remain outside the public tab class surface unless explicitly standardized elsewhere.
</p>

<hr/>

<h2 id="validation-expectations">12. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>role/class mismatches,</li>
  <li>selection indices outside the valid page range,</li>
  <li>inconsistent selection posture between <code>value</code> and <code>selection.index</code>,</li>
  <li>page-title inventories inconsistent with the current page inventory,</li>
  <li>attempts to write user-edit surfaces on indicator-only classes where forbidden,</li>
  <li>unknown tab family members or parts,</li>
  <li>attempts to treat realization-only header, hover, overflow, animation, or placement surfaces as public class members by default.</li>
</ul>

<hr/>

<h2 id="summary">13. Summary</h2>

<p>
The tab widget family defines the intrinsic standardized page-navigation widget baseline of FROG:
</p>

<ul>
  <li><code>frog.widgets.tab_control</code></li>
  <li><code>frog.widgets.tab_indicator</code></li>
</ul>

<p>
These classes provide the first standard portable visible page-navigation surfaces.
They expose a real minimal object surface with properties, methods, events, and parts while keeping realization ownership and runtime-private embodiment clearly separated from class meaning.
</p>
