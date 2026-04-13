<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Tree Widgets</h1>

<p align="center">
  <strong>Normative baseline for standardized tree control and tree indicator widget classes</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#classes-defined-here">2. Classes Defined Here</a></li>
  <li><a href="#common-family-posture">3. Common Family Posture</a></li>
  <li><a href="#hierarchical-model">4. Hierarchical Model</a></li>
  <li><a href="#selection-model">5. Selection Model</a></li>
  <li><a href="#frogwidgetstree_control">6. <code>frog.widgets.tree_control</code></a></li>
  <li><a href="#frogwidgetstree_indicator">7. <code>frog.widgets.tree_indicator</code></a></li>
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
This document defines the intrinsic standardized baseline for tree widgets in FROG.
</p>

<p>
The tree family provides the standard widget surfaces used for visible hierarchical presentation of finite node structures together with optional current-node selection and expansion posture.
These classes are intentionally modest, portable, and sufficient for the first standardized hierarchical widget family in the portable front-panel ecosystem.
</p>

<p>
The standard tree family is therefore defined here as a real object surface with:
</p>

<ul>
  <li>a primary hierarchical value posture,</li>
  <li>a visible node-and-depth presentation posture,</li>
  <li>a minimal but real property surface,</li>
  <li>a minimal but real method surface,</li>
  <li>a minimal but real event surface,</li>
  <li>a stable public part model for realization targeting.</li>
</ul>

<p>
The intrinsic tree baseline remains intentionally conservative.
It standardizes a finite expandable tree first and does not attempt to standardize tree-table hybrids, drag-and-drop ownership, rich node templating, lazy remote loading contracts, or arbitrary graph navigation in the intrinsic core.
</p>

<hr/>

<h2 id="classes-defined-here">2. Classes Defined Here</h2>

<p>
This document defines the following standardized widget classes:
</p>

<ul>
  <li><code>frog.widgets.tree_control</code></li>
  <li><code>frog.widgets.tree_indicator</code></li>
</ul>

<hr/>

<h2 id="common-family-posture">3. Common Family Posture</h2>

<p>
The tree family has the following common posture:
</p>

<ul>
  <li>family: hierarchical data widget family</li>
  <li>primary value: present</li>
  <li>public value-facing surface: yes</li>
  <li>object-style access surface: yes</li>
  <li>primary value mirror property: <code>value</code></li>
  <li>selection path surface: <code>selection.path</code></li>
  <li>selection.node_value</code> surface: <code>selection.node_value</code></li>
  <li>expansion inventory surface: <code>expansion.paths</code></li>
  <li>common label property: <code>label.text</code></li>
  <li>common visibility property: <code>interaction.visible</code></li>
</ul>

<p>
The tree family follows an important architectural rule:
</p>

<ul>
  <li><code>value</code> is class-owned hierarchical data,</li>
  <li><code>selection.path</code> is class-owned current-selection metadata,</li>
  <li><code>selection.node_value</code> is a derived public semantic surface for the currently selected node when selection exists,</li>
  <li><code>expansion.paths</code> is class-owned visible expansion metadata,</li>
  <li><code>label.text</code> is class-owned semantic label text,</li>
  <li><code>node_region</code>, <code>selection_face</code>, and <code>expander_face</code> are stable public dynamic parts,</li>
  <li>the visual embodiment of node indentation, expanders, disclosure posture, selection highlight, and scroll posture belongs downstream to realization.</li>
</ul>

<p>
This means the intrinsic core standardizes one tree family, not one fixed toolkit tree implementation.
Host-native tree views and other compatible visible embodiments remain realization strategies unless promoted later into separate explicit widget classes.
</p>

<hr/>

<h2 id="hierarchical-model">4. Hierarchical Model</h2>

<h3>4.1 Baseline data posture</h3>

<p>
The intrinsic tree baseline represents a finite rooted hierarchy.
Its primary value surface is a tree-structured ordered node model rather than a flat list or flat table.
</p>

<p>
The exact node payload typing remains governed by the active FROG type system and profile posture.
However, the intrinsic baseline assumes that the tree value remains semantically hierarchical and path-addressable.
</p>

<h3>4.2 Path posture</h3>

<p>
The intrinsic tree baseline uses explicit node paths for public selection and expansion surfaces.
A path identifies one node relative to the tree root through an ordered navigation sequence.
</p>

<p>
This path posture is public because tree navigation is semantically relevant and must not be reduced to one runtime-private row index.
</p>

<h3>4.3 Expandable tree posture</h3>

<p>
The intrinsic tree baseline allows explicit visible expansion state through <code>expansion.paths</code>.
</p>

<p>
This surface is public because visible expansion meaning affects the user-observable structure of the widget and should remain inspectable rather than hidden in runtime-private view state.
</p>

<p>
The intrinsic baseline does not standardize:
</p>

<ul>
  <li>cyclic graph structures,</li>
  <li>arbitrary DAG ownership,</li>
  <li>tree-table column hybrids,</li>
  <li>automatic remote node loading,</li>
  <li>drag-and-drop reparenting contracts.</li>
</ul>

<hr/>

<h2 id="selection-model">5. Selection Model</h2>

<h3>5.1 Single-current-node baseline</h3>

<p>
The intrinsic tree baseline standardizes a single current-node selection posture first.
At any given time, the widget exposes at most one current selected node through the public selection surfaces when selection exists.
</p>

<p>
This means the intrinsic baseline does not standardize:
</p>

<ul>
  <li>multiple independent selected nodes,</li>
  <li>range selection across visible rows,</li>
  <li>checkbox-in-tree semantics,</li>
  <li>simultaneous row and subtree block selection.</li>
</ul>

<h3>5.2 Selection surfaces</h3>

<p>
The preferred public semantic posture is:
</p>

<ul>
  <li><code>selection.path</code> — selected node path,</li>
  <li><code>selection.node_value</code> — semantic value of the current selected node when selection exists.</li>
</ul>

<p>
This distinction is normative.
The intrinsic tree baseline does not reduce the widget to a visible highlight or a flat visible row index alone.
Selection remains public and inspectable, but it does not replace the full hierarchical primary value.
</p>

<h3>5.3 Empty selection posture</h3>

<p>
The intrinsic baseline does not require that the widget always have a current selected node.
A class posture or host implementation may allow the absence of current selection where that remains explicitly represented and valid.
</p>

<p>
When no node is selected:
</p>

<ul>
  <li><code>selection.path</code> may be absent or use a documented no-selection posture,</li>
  <li><code>selection.node_value</code> may be absent or use a documented no-selection posture,</li>
  <li>the realization must not silently invent a hidden selection.</li>
</ul>

<hr/>

<h2 id="frogwidgetstree_control">6. <code>frog.widgets.tree_control</code></h2>

<h3>6.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.tree_control</code></li>
  <li><strong>family:</strong> <code>tree_widget</code></li>
  <li><strong>compatible role:</strong> <code>control</code></li>
</ul>

<h3>6.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>natural value participation: yes</li>
  <li>user-mutable: yes in the standard portable posture when the active class posture allows interactive expansion and selection change</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
</ul>

<h3>6.3 Standard properties</h3>

<ul>
  <li><code>value</code> — readable and writable hierarchical value</li>
  <li><code>selection.path</code> — readable and writable current selected node path when selection exists</li>
  <li><code>selection.node_value</code> — readable current selected node value and writable where the active editing posture allows it</li>
  <li><code>expansion.paths</code> — readable and writable visible expansion inventory</li>
  <li><code>label.text</code> — readable and writable</li>
  <li><code>interaction.enabled</code> — readable and writable</li>
  <li><code>interaction.visible</code> — readable and writable</li>
</ul>

<p>
These properties define the minimum public object surface of the intrinsic tree control.
They do not expose realization-private row caches, pixel indentation offsets, scroll bars, or toolkit-private node handles as if they were public class members.
</p>

<h3>6.4 Standard methods</h3>

<ul>
  <li><code>focus()</code></li>
  <li><code>select_next_visible()</code></li>
  <li><code>select_previous_visible()</code></li>
  <li><code>set_selected_path(path)</code></li>
  <li><code>expand(path)</code></li>
  <li><code>collapse(path)</code></li>
  <li><code>toggle_expansion(path)</code></li>
  <li><code>clear_selection()</code> when the active class posture allows no-selection state</li>
</ul>

<p>
The baseline method surface is intentionally small.
It exists to guarantee that the tree control remains a real hierarchical object with explicit navigation and expansion action surfaces rather than a passive painted outline.
</p>

<h3>6.5 Standard events</h3>

<ul>
  <li><code>selection_changed</code></li>
  <li><code>expansion_changed</code></li>
  <li><code>value_changed</code></li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<p>
The baseline allows <code>selection_changed</code>, <code>expansion_changed</code>, and <code>value_changed</code> because selection motion, visible structural expansion, and actual hierarchical-data mutation are related but must remain distinguishable.
</p>

<h3>6.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>node_region</code></li>
  <li><code>selection_face</code></li>
  <li><code>expander_face</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The <code>node_region</code> part is the public dynamic hierarchical embodiment surface.
The <code>selection_face</code> part is the public dynamic current-node emphasis surface.
The <code>expander_face</code> part is the public dynamic disclosure and expansion-control surface when visible expansion posture is supported.
Their semantic meaning belongs to the class through <code>value</code>, <code>selection.path</code>, and <code>expansion.paths</code>.
Their visual placement and embodiment belong to realization.
</p>

<hr/>

<h2 id="frogwidgetstree_indicator">7. <code>frog.widgets.tree_indicator</code></h2>

<h3>7.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.tree_indicator</code></li>
  <li><strong>family:</strong> <code>tree_widget</code></li>
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
  <li><code>selection.path</code> — readable and writable where diagram/runtime selection update surfaces are legal</li>
  <li><code>selection.node_value</code> — readable current selected node value</li>
  <li><code>expansion.paths</code> — readable and writable where diagram/runtime visible expansion update surfaces are legal</li>
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
  <li><code>set_selected_path(path)</code> where diagram-side indicator update surfaces are legal</li>
  <li><code>expand(path)</code> where diagram-side visible expansion update surfaces are legal</li>
  <li><code>collapse(path)</code> where diagram-side visible expansion update surfaces are legal</li>
  <li><code>clear_selection()</code> when the active class posture allows no-selection state</li>
</ul>

<h3>7.5 Standard events</h3>

<ul>
  <li><code>selection_rendered</code></li>
  <li><code>expansion_rendered</code></li>
  <li><code>value_rendered</code></li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<h3>7.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>node_region</code></li>
  <li><code>selection_face</code></li>
  <li><code>expander_face</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The indicator <code>node_region</code>, <code>selection_face</code>, and <code>expander_face</code> parts remain public dynamic display surfaces.
They are not merely decorative skin regions.
</p>

<hr/>

<h2 id="common-parts">8. Common Parts</h2>

<p>
The tree family uses the following common stable parts:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>node_region</code></li>
  <li><code>selection_face</code></li>
  <li><code>expander_face</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
This distinction is important:
</p>

<ul>
  <li><code>node_region</code> is a public part of the class model,</li>
  <li><code>selection_face</code> is a public part of the class model,</li>
  <li><code>expander_face</code> is a public part of the class model,</li>
  <li>indent guides, connector lines, disclosure arrows, hover layers, scroll bars, viewport helpers, and host-native tree containers used to embody them belong to realization unless explicitly promoted to class law.</li>
</ul>

<hr/>

<h2 id="common-behavior-expectations">9. Common Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the tree family includes at least:
</p>

<ul>
  <li>the primary value remains hierarchical and path-addressable,</li>
  <li>visible expansion state remains consistent with the current tree value,</li>
  <li>selected-node path, when present, remains consistent with the current tree bounds,</li>
  <li>tree controls accept user-originated selection and expansion changes only when enabled,</li>
  <li>visible structural expansion and current-node selection remain distinguishable at the public object surface,</li>
  <li>indicator realizations may emit <code>selection_rendered</code>, <code>expansion_rendered</code>, or <code>value_rendered</code> when their visible state is refreshed.</li>
</ul>

<p>
The family also preserves the distinction between:
</p>

<ul>
  <li>semantic hierarchical data owned by <code>value</code>,</li>
  <li>selection metadata owned by <code>selection.path</code>,</li>
  <li>derived selected-node semantic value exposed through <code>selection.node_value</code>,</li>
  <li>visible expansion metadata owned by <code>expansion.paths</code>,</li>
  <li>semantic label text owned by <code>label.text</code>,</li>
  <li>dynamic public hierarchical surfaces exposed through <code>node_region</code>, <code>selection_face</code>, and <code>expander_face</code>,</li>
  <li>downstream visual embodiment owned by realization.</li>
</ul>

<p>
Scroll posture, hover posture, animated expand-collapse posture, and toolkit-native disclosure behavior remain realization concerns unless explicitly promoted to additional public class surfaces.
</p>

<hr/>

<h2 id="common-realization-expectations">10. Common Realization Expectations</h2>

<p>
A conforming realization of the tree family SHOULD provide:
</p>

<ul>
  <li>a visible hierarchical node structure,</li>
  <li>a visible distinction for the current selected node when selection exists,</li>
  <li>a visible distinction between expanded and collapsed nodes where expansion is shown,</li>
  <li>optional visible label support,</li>
  <li>reasonable focus indication for controls where appropriate,</li>
  <li>part-to-visual mapping for the published parts.</li>
</ul>

<p>
The realization MAY be tree-view-like or another host-compatible hierarchical embodiment, provided that the published public class surface remains preserved.
</p>

<p>
In particular:
</p>

<ul>
  <li>realization MAY define indentation assets, disclosure assets, selection-highlight assets, focus layers, or scroll affordances,</li>
  <li>realization MUST NOT redefine the semantic owner of <code>value</code>, <code>selection.path</code>, <code>selection.node_value</code>, <code>expansion.paths</code>, or <code>label.text</code>,</li>
  <li>realization MUST NOT make baked node labels, host-private row caches, or decorative assets the only semantic source of visible tree meaning.</li>
</ul>

<hr/>

<h2 id="diagram-interaction-posture">11. Diagram Interaction Posture</h2>

<p>
The tree family supports:
</p>

<ul>
  <li>natural value participation through <code>widget_value</code>,</li>
  <li>property access through <code>frog.ui.property_read</code> and <code>frog.ui.property_write</code>,</li>
  <li>method invocation where legal,</li>
  <li>event observation where legal.</li>
</ul>

<p>
When the program intent is ordinary hierarchical dataflow, the natural value path SHOULD be preferred.
Object-style access remains available for richer widget interaction.
</p>

<p>
Typical legal object-style surfaces include:
</p>

<ul>
  <li><code>value</code></li>
  <li><code>selection.path</code></li>
  <li><code>selection.node_value</code></li>
  <li><code>expansion.paths</code></li>
  <li><code>label.text</code></li>
  <li><code>interaction.enabled</code></li>
  <li><code>interaction.visible</code></li>
</ul>

<p>
Realization-only row layouts, indentation metrics, disclosure icons, scroll bars, viewport helpers, and asset helpers remain outside the public tree class surface unless explicitly standardized elsewhere.
</p>

<hr/>

<h2 id="validation-expectations">12. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>role/class mismatches,</li>
  <li>attempts to use unsupported multi-selection semantics in the intrinsic baseline,</li>
  <li>selection paths outside the valid tree bounds,</li>
  <li>expansion paths outside the valid tree bounds,</li>
  <li>inconsistent selection posture between <code>selection.path</code> and <code>selection.node_value</code>,</li>
  <li>attempts to write user-edit surfaces on indicator-only classes where forbidden,</li>
  <li>unknown tree family members or parts,</li>
  <li>attempts to treat realization-only row, indentation, disclosure, scroll, or placement surfaces as public class members by default.</li>
</ul>

<hr/>

<h2 id="summary">13. Summary</h2>

<p>
The tree widget family defines the intrinsic standardized hierarchical widget baseline of FROG:
</p>

<ul>
  <li><code>frog.widgets.tree_control</code></li>
  <li><code>frog.widgets.tree_indicator</code></li>
</ul>

<p>
These classes provide the first standard portable visible hierarchical data surfaces beyond listbox and table.
They expose a real minimal object surface with properties, methods, events, and parts while keeping realization ownership and runtime-private embodiment clearly separated from class meaning.
</p>
