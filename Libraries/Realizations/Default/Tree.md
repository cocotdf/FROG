<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — Tree Widgets</h1>

<p align="center">
  <strong>Normative default realization posture for standardized tree widgets</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#target-classes">2. Target Classes</a></li>
  <li><a href="#realization-variant-posture">3. Realization Variant Posture</a></li>
  <li><a href="#realized-parts">4. Realized Parts</a></li>
  <li><a href="#standard-visual-states">5. Standard Visual States</a></li>
  <li><a href="#part-state-mapping">6. Part-State Mapping</a></li>
  <li><a href="#dynamic-surface-posture">7. Dynamic Surface Posture</a></li>
  <li><a href="#resource-posture">8. Resource Posture</a></li>
  <li><a href="#host-expectations">9. Host Expectations</a></li>
  <li><a href="#fallback-posture">10. Fallback Posture</a></li>
  <li><a href="#summary">11. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the default official realization posture for the standardized tree widget family.
</p>

<p>
The default tree realization is intended to provide one clean, inspectable, portable embodiment of the intrinsic tree baseline without turning one host tree widget, one toolkit-specific hierarchical view, or one runtime-private disclosure model into the semantic definition of tree widgets.
</p>

<p>
This realization is realization-side only.
It does not redefine tree class law, does not invent new public members, and does not replace the semantic ownership of hierarchical value, current-node selection metadata, selected-node semantic value, visible expansion metadata, or label text.
Its job is to embody already-published tree widget surfaces through stable visual states, stable structural bindings, and realization-side placement or rendering metadata where needed.
</p>

<p>
The preferred architectural split is:
</p>

<ul>
  <li><code>state_maps</code> for state-sensitive visual embodiment,</li>
  <li><code>part_bindings</code> for stable structural correspondence,</li>
  <li>anchors or text regions for dynamic public surfaces rendered by the host.</li>
</ul>

<hr/>

<h2 id="target-classes">2. Target Classes</h2>

<ul>
  <li><code>frog.widgets.tree_control</code></li>
  <li><code>frog.widgets.tree_indicator</code></li>
</ul>

<p>
This realization assumes the standardized tree posture in which:
</p>

<ul>
  <li>tree widgets expose hierarchical data through <code>value</code>,</li>
  <li>tree widgets may expose current-node selection metadata through <code>selection.path</code>,</li>
  <li>tree widgets may expose derived current selected-node semantic value through <code>selection.node_value</code>,</li>
  <li>tree widgets may expose visible expansion metadata through <code>expansion.paths</code>,</li>
  <li>tree widgets may expose semantic label text through <code>label.text</code>,</li>
  <li>the published public parts remain stable across realizations,</li>
  <li>the realization remains downstream from that class contract.</li>
</ul>

<p>
The realization therefore owns embodiment and placement posture for tree widgets.
It does not become the semantic owner of hierarchical value, selection metadata, selected-node semantic value, visible expansion metadata, or label content.
</p>

<hr/>

<h2 id="realization-variant-posture">3. Realization Variant Posture</h2>

<p>
The default tree family standardizes one tree realization corridor, not one mandatory visible shape.
</p>

<p>
Accordingly, a conforming realization MAY choose a tree embodiment posture such as:
</p>

<ul>
  <li>flat outline-like tree,</li>
  <li>host-native tree-view-like embodiment,</li>
  <li>connector-line-emphasized tree,</li>
  <li>another host-compatible visible hierarchical embodiment.</li>
</ul>

<p>
Those remain realization variants of the same published tree classes.
A different visible hierarchical presentation does not by itself define a new intrinsic widget class.
</p>

<p>
This distinction is normative:
</p>

<ul>
  <li>the class layer owns hierarchical semantics, selection semantics, expansion semantics, public members, methods, events, and parts,</li>
  <li>the realization layer owns how those published surfaces are visually embodied,</li>
  <li>a runtime MUST NOT treat a toolkit-native hierarchical view as if it were a distinct standard class unless a separate class contract is explicitly published elsewhere.</li>
</ul>

<hr/>

<h2 id="realized-parts">4. Realized Parts</h2>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>node_region</code></li>
  <li><code>selection_face</code></li>
  <li><code>expander_face</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The realization may internally use additional indentation guides, connector lines, disclosure icons, row separators, scroll regions, viewport helpers, clipping regions, hover layers, host-native row views, or toolkit-private hierarchical containers.
Those remain realization-private support structures unless they are explicitly published as realization resources or placement surfaces.
</p>

<p>
The default posture is:
</p>

<ul>
  <li><code>root</code> — overall layout, clipping, and outer realization region when needed,</li>
  <li><code>label</code> — dynamic text-bearing public part rendered through a realization-side placement surface,</li>
  <li><code>node_region</code> — main visible hierarchical embodiment surface,</li>
  <li><code>selection_face</code> — main current-node emphasis surface,</li>
  <li><code>expander_face</code> — main visible disclosure and expansion-control surface,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
A host may internally decompose the visible tree into visible rows, indentation layers, expander glyphs, viewport, and scroll structures.
Those remain realization-private unless explicitly published through a later realization-specific extension layer.
The stable public tree part model remains centered on <code>node_region</code>, <code>selection_face</code>, <code>expander_face</code>, <code>label</code>, and optional <code>frame</code>.
</p>

<hr/>

<h2 id="standard-visual-states">5. Standard Visual States</h2>

<p>
The default tree family defines at least:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code></li>
  <li><code>focused</code></li>
</ul>

<p>
For tree controls, the family MAY also define:
</p>

<ul>
  <li><code>selection_present</code> when the active realization explicitly distinguishes a current selected node</li>
  <li><code>selection_empty</code> when the active class posture allows explicit no-selection state</li>
  <li><code>expanded</code> and <code>collapsed</code> as realization-side disclosure states for nodes represented through visible expander posture</li>
  <li><code>pressed</code> when the active host embodiment exposes a clear press-like node or expander interaction posture.</li>
</ul>

<p>
These are realization-side visual states.
They do not replace the public class meaning of <code>value</code>, <code>selection.path</code>, <code>selection.node_value</code>, or <code>expansion.paths</code>.
</p>

<p>
The default family prefers explicit state publication over implicit toolkit conventions.
</p>

<hr/>

<h2 id="part-state-mapping">6. Part-State Mapping</h2>

<p>
The default family expects:
</p>

<ul>
  <li><code>node_region</code> to provide a visible hierarchical node posture,</li>
  <li><code>selection_face</code> to distinguish the current selected node clearly when selection exists,</li>
  <li><code>expander_face</code> to distinguish expanded and collapsed posture where visible expansion is shown,</li>
  <li><code>label</code> to remain readable across supported states,</li>
  <li><code>frame</code>, when present, to support focused posture where applicable.</li>
</ul>

<p>
A typical minimal mapping posture is:
</p>

<ul>
  <li><code>root</code> — global layout, clipping, and outer realization region,</li>
  <li><code>label</code> — dynamic text-bearing label surface,</li>
  <li><code>node_region</code> — main visible tree embodiment surface,</li>
  <li><code>selection_face</code> — current-node emphasis surface,</li>
  <li><code>expander_face</code> — visible disclosure and expansion surface,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
The preferred machine-readable split is:
</p>

<ul>
  <li><code>node_region</code> published through <code>part_bindings</code> plus optional state-sensitive <code>state_maps</code>,</li>
  <li><code>selection_face</code> published through <code>part_bindings</code> plus selection-sensitive <code>state_maps</code>,</li>
  <li><code>expander_face</code> published through <code>part_bindings</code> plus expansion-sensitive <code>state_maps</code>,</li>
  <li><code>label</code> published primarily through a <code>part_binding</code> to an anchor, text region, or equivalent placement surface,</li>
  <li><code>frame</code>, when present, published through <code>part_bindings</code> plus optional <code>state_maps</code>.</li>
</ul>

<p>
The default family SHOULD keep this mapping explicit enough that a machine-readable package can distinguish:
</p>

<ul>
  <li>state-sensitive visual resources,</li>
  <li>structural part bindings,</li>
  <li>dynamic host-rendered or host-updated tree surfaces.</li>
</ul>

<hr/>

<h2 id="dynamic-surface-posture">7. Dynamic Surface Posture</h2>

<h3>7.1 Node-region posture</h3>

<p>
The <code>node_region</code> part is the main dynamic realization surface of the tree family.
It is expected to reflect the visible hierarchical structure rather than through runtime-private semantics hidden from inspection.
</p>

<p>
A host interpreting this realization is expected to embody the current tree value visibly through <code>node_region</code>.
The realization owns how the visible hierarchy is embodied.
It does not become the semantic owner of the hierarchical value itself.
</p>

<h3>7.2 Selection-face posture</h3>

<p>
The <code>selection_face</code> part is the main dynamic current-node emphasis surface.
It is expected to reflect the current selected path and current selected-node semantic value when selection exists.
</p>

<p>
The realization owns how the current selected node is visually emphasized.
It does not become the semantic owner of selection metadata or selected-node semantic value themselves.
</p>

<h3>7.3 Expander-face posture</h3>

<p>
The <code>expander_face</code> part is the main dynamic disclosure and expansion-control surface.
It is expected to reflect visible expanded and collapsed posture where the active realization chooses to show explicit disclosure affordances.
</p>

<p>
The realization owns how disclosure posture is visually embodied.
It does not become the semantic owner of visible expansion metadata itself.
</p>

<h3>7.4 Label posture</h3>

<p>
The semantic tree label text is not owned by this realization.
It is owned by the standardized class surface through <code>label.text</code>.
</p>

<p>
The role of the default realization is to define where and how that semantic label is visually embodied, not to become the source of truth for the label text itself.
</p>

<p>
The <code>label</code> part is therefore expected to be realized as a dynamic text-bearing surface.
A host interpreting this realization should render or inject the current semantic tree label into the realized label region at runtime.
</p>

<h3>7.5 Placement posture</h3>

<p>
The default family SHOULD publish an explicit placement surface for <code>label</code> whenever host-rendered text is used.
That placement surface may take the form of:
</p>

<ul>
  <li>a named <code>text_anchor</code>,</li>
  <li>a published anchor entry backed by an <code>anchor_map</code> resource,</li>
  <li>a published <code>text_region</code> entry backed by a <code>text_region_map</code> resource,</li>
  <li>a host-native region under explicit binding posture,</li>
  <li>an equivalent explicitly published placement binding.</li>
</ul>

<p>
Those realization-side structures do not change the public meaning of <code>label.text</code>.
They only specify where the host should visually place the text.
</p>

<h3>7.6 Asset limitation rule</h3>

<p>
A tree resource file MAY include placeholder node labels, decorative connector lines, preview disclosure marks, preview selection emphasis, or design-time scaffolding.
However, a conforming realization family must not require that those asset-baked elements become the only path by which live hierarchical value, live selection metadata, live selected-node semantic value, live expansion metadata, or live semantic label text is shown.
</p>

<p>
Likewise, selection highlight posture and disclosure posture must remain distinguishable from the semantic hierarchical value itself.
</p>

<hr/>

<h2 id="resource-posture">8. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>tree_control/
  node_region/
    normal
    disabled
    focused
    selection_present
    selection_empty
  selection_face/
    normal
    focused
    pressed
  expander_face/
    expanded
    collapsed
    disabled
  frame/
    normal
    focused
  anchors/
    label

tree_indicator/
  node_region/
    normal
    disabled
    focused
    selection_present
    selection_empty
  selection_face/
    normal
    focused
  expander_face/
    expanded
    collapsed
    disabled
  frame/
    normal
    focused
  anchors/
    label
</code></pre>

<p>
An equivalent package-oriented posture may publish resources such as:
</p>

<ul>
  <li><code>tree_control.node_region.normal.svg</code></li>
  <li><code>tree_control.selection_face.focused.svg</code></li>
  <li><code>tree_control.expander_face.expanded.svg</code></li>
  <li><code>tree_control.expander_face.collapsed.svg</code></li>
  <li><code>tree_control.label.anchor_map</code> backed by <code>./assets/tree_control/anchors/label.json</code></li>
  <li><code>tree_indicator.node_region.normal.svg</code></li>
  <li><code>tree_indicator.selection_face.normal.svg</code></li>
  <li><code>tree_indicator.expander_face.collapsed.svg</code></li>
  <li><code>tree_indicator.label.anchor_map</code> backed by <code>./assets/tree_indicator/anchors/label.json</code></li>
</ul>

<p>
Resources MAY be SVG-backed, host-native, toolkit-driven, or mixed.
The default family standardizes the part posture, state posture, and realization-side binding posture, not one mandatory tree implementation and not one mandatory file format.
</p>

<p>
In particular:
</p>

<ul>
  <li><code>node_region</code> is the natural candidate for hierarchy-sensitive visible resources,</li>
  <li><code>selection_face</code> is the natural candidate for selection-sensitive emphasis resources,</li>
  <li><code>expander_face</code> is the natural candidate for disclosure-sensitive resources,</li>
  <li><code>label</code> is naturally a placement-bound dynamic text surface,</li>
  <li><code>frame</code>, when present, is a natural candidate for optional state-sensitive supporting resources.</li>
</ul>

<hr/>

<h2 id="host-expectations">9. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a clearly visible hierarchical node structure,</li>
  <li>a clear visible distinction for the current selected node when selection exists,</li>
  <li>a clear visible distinction between expanded and collapsed nodes where expansion is shown,</li>
  <li>clear visible distinction between enabled and disabled posture,</li>
  <li>reasonable focus indication for controls,</li>
  <li>dynamic rendering of visible tree label text.</li>
</ul>

<p>
A host SHOULD also preserve the distinction between:
</p>

<ul>
  <li>the semantic tree value owned by the class,</li>
  <li>the selection metadata owned by <code>selection.path</code>,</li>
  <li>the selected-node semantic value owned by <code>selection.node_value</code>,</li>
  <li>the visible expansion metadata owned by <code>expansion.paths</code>,</li>
  <li>the tree label text owned by <code>label.text</code>,</li>
  <li>the realization-side embodiment of <code>node_region</code>, <code>selection_face</code>, <code>expander_face</code>, <code>label</code>, and <code>frame</code>.</li>
</ul>

<p>
A host MAY approximate the realization when exact resources are unavailable, but it should preserve:
</p>

<ul>
  <li>the interactive-versus-indicator distinction,</li>
  <li>the stable meaning of the published public parts,</li>
  <li>the separation between semantic tree data and realization resources.</li>
</ul>

<hr/>

<h2 id="fallback-posture">10. Fallback Posture</h2>

<p>
If state-specific resources are unavailable, a runtime MAY use host-native tree widgets or generic hierarchical rendering, provided the visible hierarchical posture and current-node distinction remain preserved.
</p>

<p>
If dedicated label placement resources are unavailable, a host MAY fall back to:
</p>

<ul>
  <li>a host-native text region,</li>
  <li>a generic compatible label placement rule,</li>
  <li>another documented compatible placement surface.</li>
</ul>

<p>
If selection-face-specific resources are unavailable, a host MAY fall back to host-native current-node emphasis posture provided that the selected-node distinction remains visible and the hierarchical embodiment remains clear.
</p>

<p>
If expander-face-specific resources are unavailable, a host MAY fall back to host-native disclosure rendering provided that expanded-versus-collapsed posture remains visible where expansion is shown.
</p>

<p>
Any fallback MUST preserve the published tree class law and the meaning of the public parts when those parts are exposed.
Fallback must not turn asset-baked node labels, connector lines, disclosure icons, highlight marks, or label text into semantic truth.
</p>

<p>
Fallback must remain inspectable at the realization-publication layer.
It must not become a purely runtime-private convention.
</p>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
The default tree realization defines one official state-structured embodiment for tree controls and tree indicators, centered on the public <code>node_region</code>, <code>selection_face</code>, and <code>expander_face</code> parts.
</p>

<p>
It realizes:
</p>

<ul>
  <li><code>node_region</code> as the main dynamic visible hierarchical surface,</li>
  <li><code>selection_face</code> as the dynamic current-node emphasis surface,</li>
  <li><code>expander_face</code> as the visible disclosure and expansion surface,</li>
  <li><code>label</code> as a dynamically rendered text-bearing surface,</li>
  <li><code>frame</code> as an optional supporting outer surface.</li>
</ul>

<p>
Its resources may provide skins, layers, regions, and anchors.
Its package publication may provide <code>state_maps</code> and <code>part_bindings</code>.
Its host implementation may approximate the visuals when needed.
But the realization never becomes the semantic owner of hierarchical value, selection metadata, selected-node semantic value, expansion metadata, label text, or tree class meaning.
</p>
