<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Table Widgets</h1>

<p align="center">
  <strong>Normative baseline for standardized table control and table indicator widget classes</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#classes-defined-here">2. Classes Defined Here</a></li>
  <li><a href="#common-family-posture">3. Common Family Posture</a></li>
  <li><a href="#tabular-model">4. Tabular Model</a></li>
  <li><a href="#selection-model">5. Selection Model</a></li>
  <li><a href="#frogwidgetstable_control">6. <code>frog.widgets.table_control</code></a></li>
  <li><a href="#frogwidgetstable_indicator">7. <code>frog.widgets.table_indicator</code></a></li>
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
This document defines the intrinsic standardized baseline for table widgets in FROG.
</p>

<p>
The table family provides the standard widget surfaces used for visible row-and-column presentation of finite tabular data together with an optional current-cell or current-row selection posture.
These classes are intentionally modest, portable, and sufficient for the first standardized tabular widget family in the portable front-panel ecosystem.
</p>

<p>
The standard table family is therefore defined here as a real object surface with:
</p>

<ul>
  <li>a primary tabular value posture,</li>
  <li>a visible row-and-column presentation posture,</li>
  <li>a minimal but real property surface,</li>
  <li>a minimal but real method surface,</li>
  <li>a minimal but real event surface,</li>
  <li>a stable public part model for realization targeting.</li>
</ul>

<p>
The intrinsic table baseline remains intentionally conservative.
It standardizes a flat finite table first and does not attempt to standardize tree-table behavior, spreadsheet-grade formulas, merged cells, frozen panes, virtualization contracts, or full grid-editing ecosystems in the intrinsic core.
</p>

<hr/>

<h2 id="classes-defined-here">2. Classes Defined Here</h2>

<p>
This document defines the following standardized widget classes:
</p>

<ul>
  <li><code>frog.widgets.table_control</code></li>
  <li><code>frog.widgets.table_indicator</code></li>
</ul>

<hr/>

<h2 id="common-family-posture">3. Common Family Posture</h2>

<p>
The table family has the following common posture:
</p>

<ul>
  <li>family: tabular data widget family</li>
  <li>primary value: present</li>
  <li>public value-facing surface: yes</li>
  <li>object-style access surface: yes</li>
  <li>primary value mirror property: <code>value</code></li>
  <li>selection row surface: <code>selection.row</code></li>
  <li>selection column surface: <code>selection.column</code></li>
  <li>cell value surface: <code>selection.cell_value</code></li>
  <li>column header inventory surface: <code>columns.headers</code></li>
  <li>common label property: <code>label.text</code></li>
  <li>common visibility property: <code>interaction.visible</code></li>
</ul>

<p>
The table family follows an important architectural rule:
</p>

<ul>
  <li><code>value</code> is class-owned tabular data,</li>
  <li><code>selection.row</code> and <code>selection.column</code> are class-owned current-selection metadata,</li>
  <li><code>selection.cell_value</code> is a derived public semantic surface for the currently selected cell when selection exists,</li>
  <li><code>columns.headers</code> is class-owned header metadata,</li>
  <li><code>label.text</code> is class-owned semantic label text,</li>
  <li><code>grid_region</code>, <code>header_region</code>, and <code>selection_face</code> are stable public dynamic parts,</li>
  <li>the visual embodiment of rows, columns, selection highlights, scroll posture, and grid styling belongs downstream to realization.</li>
</ul>

<p>
This means the intrinsic core standardizes one table family, not one fixed spreadsheet implementation.
Simple grid-like tables, host-native table views, and other compatible visible embodiments remain realization strategies unless promoted later into separate explicit widget classes.
</p>

<hr/>

<h2 id="tabular-model">4. Tabular Model</h2>

<h3>4.1 Baseline data posture</h3>

<p>
The intrinsic table baseline represents a finite rectangular table.
Its primary value surface is a 2-dimensional ordered data structure.
</p>

<p>
The exact element typing remains governed by the active FROG type system and profile posture.
However, the intrinsic baseline assumes that the table value remains semantically row-and-column structured.
</p>

<h3>4.2 Header posture</h3>

<p>
The intrinsic table baseline allows an explicit column-header inventory through <code>columns.headers</code>.
</p>

<p>
This header surface is public because header meaning is often user-relevant and not only decorative.
However, the existence of visible header rows, their geometry, and their emphasis remain realization concerns unless explicitly standardized elsewhere.
</p>

<h3>4.3 Flat table posture</h3>

<p>
The intrinsic table baseline is flat.
It does not standardize:
</p>

<ul>
  <li>hierarchical row expansion,</li>
  <li>tree-style indentation,</li>
  <li>nested header groups,</li>
  <li>merged cells,</li>
  <li>formula ownership,</li>
  <li>automatic computed summary rows.</li>
</ul>

<hr/>

<h2 id="selection-model">5. Selection Model</h2>

<h3>5.1 Single-current-cell baseline</h3>

<p>
The intrinsic table baseline standardizes a single current-cell selection posture first.
At any given time, the widget exposes at most one current cell through the public selection surfaces when selection exists.
</p>

<p>
This means the intrinsic baseline does not standardize:
</p>

<ul>
  <li>multiple independent selected cells,</li>
  <li>range selection,</li>
  <li>whole-row multi-selection,</li>
  <li>whole-column multi-selection,</li>
  <li>spreadsheet-like selection blocks.</li>
</ul>

<h3>5.2 Selection surfaces</h3>

<p>
The preferred public semantic posture is:
</p>

<ul>
  <li><code>selection.row</code> — selected row index,</li>
  <li><code>selection.column</code> — selected column index,</li>
  <li><code>selection.cell_value</code> — semantic value of the current selected cell when selection exists.</li>
</ul>

<p>
This distinction is normative.
The intrinsic table baseline does not reduce the widget to a highlight-only grid.
Selection remains public and inspectable, but it does not replace the full tabular primary value.
</p>

<h3>5.3 Empty selection posture</h3>

<p>
The intrinsic baseline does not require that the widget always have a current selected cell.
A class posture or host implementation may allow the absence of current selection where that remains explicitly represented and valid.
</p>

<p>
When no cell is selected:
</p>

<ul>
  <li><code>selection.row</code> may be absent or use a documented no-selection posture,</li>
  <li><code>selection.column</code> may be absent or use a documented no-selection posture,</li>
  <li><code>selection.cell_value</code> may be absent or use a documented no-selection posture,</li>
  <li>the realization must not silently invent a hidden selection.</li>
</ul>

<hr/>

<h2 id="frogwidgetstable_control">6. <code>frog.widgets.table_control</code></h2>

<h3>6.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.table_control</code></li>
  <li><strong>family:</strong> <code>table_widget</code></li>
  <li><strong>compatible role:</strong> <code>control</code></li>
</ul>

<h3>6.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>natural value participation: yes</li>
  <li>user-mutable: yes in the standard portable posture when the active class posture allows editing</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
</ul>

<h3>6.3 Standard properties</h3>

<ul>
  <li><code>value</code> — readable and writable tabular value</li>
  <li><code>columns.headers</code> — readable and writable ordered column-header inventory</li>
  <li><code>selection.row</code> — readable and writable current selected row when selection exists</li>
  <li><code>selection.column</code> — readable and writable current selected column when selection exists</li>
  <li><code>selection.cell_value</code> — readable current selected cell value and writable where the active editing posture allows it</li>
  <li><code>label.text</code> — readable and writable</li>
  <li><code>interaction.enabled</code> — readable and writable</li>
  <li><code>interaction.visible</code> — readable and writable</li>
</ul>

<p>
These properties define the minimum public object surface of the intrinsic table control.
They do not expose realization-private scroll bars, row caches, hover layers, frozen-pane helpers, or toolkit-private grid internals as if they were public class members.
</p>

<h3>6.4 Standard methods</h3>

<ul>
  <li><code>focus()</code></li>
  <li><code>select_next_row()</code></li>
  <li><code>select_previous_row()</code></li>
  <li><code>select_next_column()</code></li>
  <li><code>select_previous_column()</code></li>
  <li><code>set_selected_cell(row, column)</code></li>
  <li><code>clear_selection()</code> when the active class posture allows no-selection state</li>
</ul>

<p>
The baseline method surface is intentionally small.
It exists to guarantee that the table control remains a real tabular object with explicit action surfaces rather than a passive painted grid.
</p>

<h3>6.5 Standard events</h3>

<ul>
  <li><code>selection_changed</code></li>
  <li><code>value_changed</code></li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<p>
The baseline allows both <code>selection_changed</code> and <code>value_changed</code> because current-cell movement and actual table-data mutation are related but must remain distinguishable.
</p>

<h3>6.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>header_region</code></li>
  <li><code>grid_region</code></li>
  <li><code>selection_face</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The <code>grid_region</code> part is the public dynamic tabular embodiment surface.
The <code>selection_face</code> part is the public dynamic current-cell emphasis surface.
The <code>header_region</code> part is the public header embodiment surface when headers are shown.
Their semantic meaning belongs to the class through <code>value</code>, <code>columns.headers</code>, <code>selection.row</code>, and <code>selection.column</code>.
Their visual placement and embodiment belong to realization.
</p>

<hr/>

<h2 id="frogwidgetstable_indicator">7. <code>frog.widgets.table_indicator</code></h2>

<h3>7.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.table_indicator</code></li>
  <li><strong>family:</strong> <code>table_widget</code></li>
  <li><strong>compatible role:</strong> <code>indicator</code></li>
</ul>

<h3>7.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>natural value participation: yes</li>
  <li>user-mutable: no in the standard portable posture</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
</ul>

<h3>7.3 Standard properties</h3>

<ul>
  <li><code>value</code> — readable and writable for diagram/runtime update surfaces where legal</li>
  <li><code>columns.headers</code> — readable and writable where legal</li>
  <li><code>selection.row</code> — readable and writable where diagram/runtime selection update surfaces are legal</li>
  <li><code>selection.column</code> — readable and writable where diagram/runtime selection update surfaces are legal</li>
  <li><code>selection.cell_value</code> — readable current selected cell value</li>
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
  <li><code>set_selected_cell(row, column)</code> where diagram-side indicator update surfaces are legal</li>
  <li><code>clear_selection()</code> when the active class posture allows no-selection state</li>
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
  <li><code>header_region</code></li>
  <li><code>grid_region</code></li>
  <li><code>selection_face</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The indicator <code>header_region</code>, <code>grid_region</code>, and <code>selection_face</code> parts remain public dynamic display surfaces.
They are not merely decorative skin regions.
</p>

<hr/>

<h2 id="common-parts">8. Common Parts</h2>

<p>
The table family uses the following common stable parts:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>header_region</code></li>
  <li><code>grid_region</code></li>
  <li><code>selection_face</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
This distinction is important:
</p>

<ul>
  <li><code>header_region</code> is a public part of the class model,</li>
  <li><code>grid_region</code> is a public part of the class model,</li>
  <li><code>selection_face</code> is a public part of the class model,</li>
  <li>row separators, cell borders, hover layers, scroll bars, viewport helpers, and host-native grid containers used to embody them belong to realization unless explicitly promoted to class law.</li>
</ul>

<hr/>

<h2 id="common-behavior-expectations">9. Common Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the table family includes at least:
</p>

<ul>
  <li>the primary value remains tabular and rectangular,</li>
  <li>header inventory, when present, remains consistent with the column structure,</li>
  <li>current-cell selection, when present, remains consistent with the current table bounds,</li>
  <li>table controls accept user-originated selection changes only when enabled,</li>
  <li>table-data mutation and selection motion remain distinguishable at the public object surface,</li>
  <li>indicator realizations may emit <code>selection_rendered</code> or <code>value_rendered</code> when their visible state is refreshed.</li>
</ul>

<p>
The family also preserves the distinction between:
</p>

<ul>
  <li>semantic tabular data owned by <code>value</code>,</li>
  <li>semantic header metadata owned by <code>columns.headers</code>,</li>
  <li>selection metadata owned by <code>selection.row</code> and <code>selection.column</code>,</li>
  <li>derived selected-cell semantic value exposed through <code>selection.cell_value</code>,</li>
  <li>semantic label text owned by <code>label.text</code>,</li>
  <li>dynamic public tabular surfaces exposed through <code>header_region</code>, <code>grid_region</code>, and <code>selection_face</code>,</li>
  <li>downstream visual embodiment owned by realization.</li>
</ul>

<p>
Scroll posture, hover posture, column resizing, row resizing, and spreadsheet-like editing feedback remain realization concerns unless explicitly promoted to additional public class surfaces.
</p>

<hr/>

<h2 id="common-realization-expectations">10. Common Realization Expectations</h2>

<p>
A conforming realization of the table family SHOULD provide:
</p>

<ul>
  <li>a visible row-and-column grid,</li>
  <li>a visible distinction for the current selected cell when selection exists,</li>
  <li>visible header support when headers are shown,</li>
  <li>optional visible label support,</li>
  <li>reasonable focus indication for controls where appropriate,</li>
  <li>part-to-visual mapping for the published parts.</li>
</ul>

<p>
The realization MAY be grid-like, table-view-like, or another host-compatible tabular embodiment, provided that the published public class surface remains preserved.
</p>

<p>
In particular:
</p>

<ul>
  <li>realization MAY define cell-border assets, header assets, selection-highlight assets, focus layers, or scroll affordances,</li>
  <li>realization MUST NOT redefine the semantic owner of <code>value</code>, <code>columns.headers</code>, <code>selection.row</code>, <code>selection.column</code>, <code>selection.cell_value</code>, or <code>label.text</code>,</li>
  <li>realization MUST NOT make baked cell text, header text, host-private row caches, or decorative assets the only semantic source of visible table meaning.</li>
</ul>

<hr/>

<h2 id="diagram-interaction-posture">11. Diagram Interaction Posture</h2>

<p>
The table family supports:
</p>

<ul>
  <li>natural value participation through <code>widget_value</code>,</li>
  <li>property access through <code>frog.ui.property_read</code> and <code>frog.ui.property_write</code>,</li>
  <li>method invocation where legal,</li>
  <li>event observation where legal.</li>
</ul>

<p>
When the program intent is ordinary tabular dataflow, the natural value path SHOULD be preferred.
Object-style access remains available for richer widget interaction.
</p>

<p>
Typical legal object-style surfaces include:
</p>

<ul>
  <li><code>value</code></li>
  <li><code>columns.headers</code></li>
  <li><code>selection.row</code></li>
  <li><code>selection.column</code></li>
  <li><code>selection.cell_value</code></li>
  <li><code>label.text</code></li>
  <li><code>interaction.enabled</code></li>
  <li><code>interaction.visible</code></li>
</ul>

<p>
Realization-only row layouts, column widths, scroll bars, hover layers, viewport helpers, and asset helpers remain outside the public table class surface unless explicitly standardized elsewhere.
</p>

<hr/>

<h2 id="validation-expectations">12. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>role/class mismatches,</li>
  <li>attempts to use unsupported multi-cell or range-selection semantics in the intrinsic baseline,</li>
  <li>selection indices outside the valid row or column range,</li>
  <li>inconsistent selection posture between <code>selection.row</code>, <code>selection.column</code>, and <code>selection.cell_value</code>,</li>
  <li>header inventories inconsistent with the current column structure,</li>
  <li>attempts to write user-edit surfaces on indicator-only classes where forbidden,</li>
  <li>unknown table family members or parts,</li>
  <li>attempts to treat realization-only row, column, scroll, or placement surfaces as public class members by default.</li>
</ul>

<hr/>

<h2 id="summary">13. Summary</h2>

<p>
The table widget family defines the intrinsic standardized flat tabular widget baseline of FROG:
</p>

<ul>
  <li><code>frog.widgets.table_control</code></li>
  <li><code>frog.widgets.table_indicator</code></li>
</ul>

<p>
These classes provide the first standard portable visible row-and-column data surfaces beyond listbox.
They expose a real minimal object surface with properties, methods, events, and parts while keeping realization ownership and runtime-private embodiment clearly separated from class meaning.
</p>
