<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — Listbox Widgets</h1>

<p align="center">
  <strong>Normative default realization posture for standardized listbox widgets</strong><br/>
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
This document defines the default official realization posture for the standardized listbox widget family.
</p>

<p>
The default listbox realization is intended to provide one clean, inspectable, portable embodiment of the intrinsic listbox baseline without turning one host list widget, one toolkit-specific scroll container, or one runtime-private row model into the semantic definition of listbox widgets.
</p>

<p>
This realization is realization-side only.
It does not redefine listbox class law, does not invent new public members, and does not replace the semantic ownership of item inventory, selected value, selection index, or label text.
Its job is to embody already-published listbox widget surfaces through stable visual states, stable structural bindings, and realization-side placement or rendering metadata where needed.
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
  <li><code>frog.widgets.listbox_control</code></li>
  <li><code>frog.widgets.listbox_indicator</code></li>
</ul>

<p>
This realization assumes the standardized listbox posture in which:
</p>

<ul>
  <li>listbox widgets expose an ordered item inventory through <code>items</code>,</li>
  <li>listbox widgets expose a semantic selected value through <code>value</code>,</li>
  <li>listbox widgets expose selection position metadata through <code>selection.index</code>,</li>
  <li>listbox widgets may expose semantic label text through <code>label.text</code>,</li>
  <li>the published public parts remain stable across realizations,</li>
  <li>the realization remains downstream from that class contract.</li>
</ul>

<p>
The realization therefore owns embodiment and placement posture for listbox widgets.
It does not become the semantic owner of the item inventory, the selected value, the selection index, or the label content.
</p>

<hr/>

<h2 id="realization-variant-posture">3. Realization Variant Posture</h2>

<p>
The default listbox family standardizes one listbox realization corridor, not one mandatory visible shape.
</p>

<p>
Accordingly, a conforming realization MAY choose a listbox embodiment posture such as:
</p>

<ul>
  <li>flat bordered list,</li>
  <li>menu-like visible list,</li>
  <li>host-native single-column selector list,</li>
  <li>another host-compatible persistent visible selection list.</li>
</ul>

<p>
Those remain realization variants of the same published listbox classes.
A different visible list presentation does not by itself define a new intrinsic widget class.
</p>

<p>
This distinction is normative:
</p>

<ul>
  <li>the class layer owns item inventory semantics, selection semantics, public members, methods, events, and parts,</li>
  <li>the realization layer owns how those published surfaces are visually embodied,</li>
  <li>a runtime MUST NOT treat a menu-like or toolkit-native embodiment as if it were a distinct standard class unless a separate class contract is explicitly published elsewhere.</li>
</ul>

<hr/>

<h2 id="realized-parts">4. Realized Parts</h2>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>item_region</code></li>
  <li><code>selection_face</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The realization may internally use additional row backgrounds, separators, scroll regions, hover layers, clipping regions, host-native row views, or toolkit-private list structures.
Those remain realization-private support structures unless they are explicitly published as realization resources or placement surfaces.
</p>

<p>
The default posture is:
</p>

<ul>
  <li><code>root</code> — overall layout, clipping, and outer realization region when needed,</li>
  <li><code>label</code> — dynamic text-bearing public part rendered through a realization-side placement surface,</li>
  <li><code>item_region</code> — main visible item-list embodiment surface,</li>
  <li><code>selection_face</code> — main selected-item emphasis surface,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
A host may internally decompose the list embodiment into rows, viewport, and scroll structures.
Those remain realization-private unless explicitly published through a later realization-specific extension layer.
The stable public listbox part model remains centered on <code>item_region</code>, <code>selection_face</code>, <code>label</code>, and optional <code>frame</code>.
</p>

<hr/>

<h2 id="standard-visual-states">5. Standard Visual States</h2>

<p>
The default listbox family defines at least:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code></li>
  <li><code>focused</code></li>
</ul>

<p>
For listbox controls, the family MAY also define:
</p>

<ul>
  <li><code>selection_present</code> when the active realization explicitly distinguishes a currently selected state,</li>
  <li><code>selection_empty</code> when the active class posture allows explicit no-selection state,</li>
  <li><code>pressed</code> when the active host embodiment exposes a clear press-like item activation posture.</li>
</ul>

<p>
These are realization-side visual states.
They do not replace the public class meaning of <code>items</code>, <code>value</code>, or <code>selection.index</code>.
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
  <li><code>item_region</code> to provide a visible ordered item-list posture,</li>
  <li><code>selection_face</code> to distinguish the current selection clearly when selection exists,</li>
  <li><code>label</code> to remain readable across supported states,</li>
  <li><code>frame</code>, when present, to support focused posture where applicable.</li>
</ul>

<p>
A typical minimal mapping posture is:
</p>

<ul>
  <li><code>root</code> — global layout, clipping, and outer realization region,</li>
  <li><code>label</code> — dynamic text-bearing label surface,</li>
  <li><code>item_region</code> — main item-list embodiment surface,</li>
  <li><code>selection_face</code> — selected-item emphasis surface,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
The preferred machine-readable split is:
</p>

<ul>
  <li><code>item_region</code> published through <code>part_bindings</code> plus optional state-sensitive <code>state_maps</code>,</li>
  <li><code>selection_face</code> published through <code>part_bindings</code> plus selection-sensitive <code>state_maps</code>,</li>
  <li><code>label</code> published primarily through a <code>part_binding</code> to an anchor, text region, or equivalent placement surface,</li>
  <li><code>frame</code>, when present, published through <code>part_bindings</code> plus optional <code>state_maps</code>.</li>
</ul>

<p>
The default family SHOULD keep this mapping explicit enough that a machine-readable package can distinguish:
</p>

<ul>
  <li>state-sensitive visual resources,</li>
  <li>structural part bindings,</li>
  <li>dynamic host-rendered or host-updated listbox surfaces.</li>
</ul>

<hr/>

<h2 id="dynamic-surface-posture">7. Dynamic Surface Posture</h2>

<h3>7.1 Item-region posture</h3>

<p>
The <code>item_region</code> part is the main dynamic realization surface of the listbox family.
It is expected to reflect the ordered item inventory visibly rather than through runtime-private semantics hidden from inspection.
</p>

<p>
A host interpreting this realization is expected to embody the current item inventory visibly through <code>item_region</code>.
</p>

<p>
The realization owns how the visible item list is embodied.
It does not become the semantic owner of the item inventory itself.
</p>

<h3>7.2 Selection-face posture</h3>

<p>
The <code>selection_face</code> part is the main dynamic selected-item emphasis surface.
It is expected to reflect the current selected value and current selection index when selection exists.
</p>

<p>
The realization owns how the current selection is visually emphasized.
It does not become the semantic owner of the selection value or selection index themselves.
</p>

<h3>7.3 Label posture</h3>

<p>
The semantic listbox label text is not owned by this realization.
It is owned by the standardized class surface through <code>label.text</code>.
</p>

<p>
The role of the default realization is to define where and how that semantic label is visually embodied, not to become the source of truth for the label text itself.
</p>

<p>
The <code>label</code> part is therefore expected to be realized as a dynamic text-bearing surface.
A host interpreting this realization should render or inject the current semantic listbox label into the realized label region at runtime.
</p>

<h3>7.4 Placement posture</h3>

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

<h3>7.5 Asset limitation rule</h3>

<p>
A listbox resource file MAY include placeholder row text, decorative row guides, preview selection emphasis, or design-time scaffolding.
However, a conforming realization family must not require that those asset-baked elements become the only path by which live item inventory, live selected value, live selection index, or live semantic label text is shown.
</p>

<p>
Likewise, selection highlight posture and focus posture must remain distinguishable from the semantic selection value itself.
</p>

<hr/>

<h2 id="resource-posture">8. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>listbox_control/
  item_region/
    normal
    disabled
    focused
    selection_present
    selection_empty
  selection_face/
    normal
    focused
    pressed
  frame/
    normal
    focused
  anchors/
    label

listbox_indicator/
  item_region/
    normal
    disabled
    focused
    selection_present
    selection_empty
  selection_face/
    normal
    focused
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
  <li><code>listbox_control.item_region.normal.svg</code></li>
  <li><code>listbox_control.item_region.selection_present.svg</code></li>
  <li><code>listbox_control.selection_face.focused.svg</code></li>
  <li><code>listbox_control.label.anchor_map</code> backed by <code>./assets/listbox_control/anchors/label.json</code></li>
  <li><code>listbox_indicator.item_region.normal.svg</code></li>
  <li><code>listbox_indicator.selection_face.normal.svg</code></li>
  <li><code>listbox_indicator.label.anchor_map</code> backed by <code>./assets/listbox_indicator/anchors/label.json</code></li>
</ul>

<p>
Resources MAY be SVG-backed, host-native, toolkit-driven, or mixed.
The default family standardizes the part posture, state posture, and realization-side binding posture, not one mandatory scroll-container implementation and not one mandatory file format.
</p>

<p>
In particular:
</p>

<ul>
  <li><code>item_region</code> is the natural candidate for inventory-sensitive visible resources,</li>
  <li><code>selection_face</code> is the natural candidate for selection-sensitive emphasis resources,</li>
  <li><code>label</code> is naturally a placement-bound dynamic text surface,</li>
  <li><code>frame</code>, when present, is a natural candidate for optional state-sensitive supporting resources.</li>
</ul>

<hr/>

<h2 id="host-expectations">9. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a clearly visible ordered item list,</li>
  <li>a clear visible distinction for the current selection when selection exists,</li>
  <li>clear visible distinction between enabled and disabled posture,</li>
  <li>reasonable focus indication for controls,</li>
  <li>dynamic rendering of visible listbox label text.</li>
</ul>

<p>
A host SHOULD also preserve the distinction between:
</p>

<ul>
  <li>the semantic item inventory owned by the class,</li>
  <li>the semantic selected value owned by <code>value</code>,</li>
  <li>the selection position metadata owned by <code>selection.index</code>,</li>
  <li>the listbox label text owned by <code>label.text</code>,</li>
  <li>the realization-side embodiment of <code>item_region</code>, <code>selection_face</code>, <code>label</code>, and <code>frame</code>.</li>
</ul>

<p>
A host MAY approximate the realization when exact resources are unavailable, but it should preserve:
</p>

<ul>
  <li>the interactive-versus-indicator distinction,</li>
  <li>the stable meaning of the published public parts,</li>
  <li>the separation between semantic listbox data and realization resources.</li>
</ul>

<hr/>

<h2 id="fallback-posture">10. Fallback Posture</h2>

<p>
If state-specific resources are unavailable, a runtime MAY use host-native list widgets or generic selection rendering, provided the ordered item posture and selected-item distinction remain preserved.
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
If selection-face-specific resources are unavailable, a host MAY fall back to host-native selection emphasis posture provided that the selected-item distinction remains visible and the inventory-sensitive embodiment remains clear.
</p>

<p>
Any fallback MUST preserve the published listbox class law and the meaning of the public parts when those parts are exposed.
Fallback must not turn asset-baked row text, highlight marks, or label text into semantic truth.
</p>

<p>
Fallback must remain inspectable at the realization-publication layer.
It must not become a purely runtime-private convention.
</p>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
The default listbox realization defines one official state-structured embodiment for listbox controls and listbox indicators, centered on the public <code>item_region</code> and <code>selection_face</code> parts.
</p>

<p>
It realizes:
</p>

<ul>
  <li><code>item_region</code> as the main dynamic visible item-list surface,</li>
  <li><code>selection_face</code> as the dynamic selected-item emphasis surface,</li>
  <li><code>label</code> as a dynamically rendered text-bearing surface,</li>
  <li><code>frame</code> as an optional supporting outer surface.</li>
</ul>

<p>
Its resources may provide skins, layers, regions, and anchors.
Its package publication may provide <code>state_maps</code> and <code>part_bindings</code>.
Its host implementation may approximate the visuals when needed.
But the realization never becomes the semantic owner of item inventory, selected value, selection index, label text, or listbox class meaning.
</p>
