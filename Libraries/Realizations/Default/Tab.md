<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — Tab Widgets</h1>

<p align="center">
  <strong>Normative default realization posture for standardized tab widgets</strong><br/>
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
This document defines the default official realization posture for the standardized tab widget family.
</p>

<p>
The default tab realization is intended to provide one clean, inspectable, portable embodiment of the intrinsic tab baseline without turning one host tab widget, one toolkit-specific tab strip, or one runtime-private page-navigation model into the semantic definition of tab widgets.
</p>

<p>
This realization is realization-side only.
It does not redefine tab class law, does not invent new public members, and does not replace the semantic ownership of page inventory, page-title inventory, selected page value, selected-page index, or label text.
Its job is to embody already-published tab widget surfaces through stable visual states, stable structural bindings, and realization-side placement or rendering metadata where needed.
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
  <li><code>frog.widgets.tab_control</code></li>
  <li><code>frog.widgets.tab_indicator</code></li>
</ul>

<p>
This realization assumes the standardized tab posture in which:
</p>

<ul>
  <li>tab widgets expose page inventory through <code>pages</code>,</li>
  <li>tab widgets may expose page-title inventory through <code>pages.titles</code>,</li>
  <li>tab widgets expose the selected page through <code>value</code>,</li>
  <li>tab widgets expose selected-page position metadata through <code>selection.index</code>,</li>
  <li>tab widgets may expose semantic label text through <code>label.text</code>,</li>
  <li>the published public parts remain stable across realizations,</li>
  <li>the realization remains downstream from that class contract.</li>
</ul>

<p>
The realization therefore owns embodiment and placement posture for tab widgets.
It does not become the semantic owner of page inventory, title inventory, selected page value, selected-page index, or label content.
</p>

<hr/>

<h2 id="realization-variant-posture">3. Realization Variant Posture</h2>

<p>
The default tab family standardizes one tab realization corridor, not one mandatory visible shape.
</p>

<p>
Accordingly, a conforming realization MAY choose a tab embodiment posture such as:
</p>

<ul>
  <li>top-tab strip,</li>
  <li>bottom-tab strip,</li>
  <li>segmented-tab-like embodiment,</li>
  <li>another host-compatible visible page-navigation embodiment.</li>
</ul>

<p>
Those remain realization variants of the same published tab classes.
A different visible tab presentation does not by itself define a new intrinsic widget class.
</p>

<p>
This distinction is normative:
</p>

<ul>
  <li>the class layer owns page navigation semantics, public members, methods, events, and parts,</li>
  <li>the realization layer owns how those published surfaces are visually embodied,</li>
  <li>a runtime MUST NOT treat a toolkit-native tab strip as if it were a distinct standard class unless a separate class contract is explicitly published elsewhere.</li>
</ul>

<hr/>

<h2 id="realized-parts">4. Realized Parts</h2>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>tab_header_region</code></li>
  <li><code>selection_face</code></li>
  <li><code>page_region</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The realization may internally use additional hover layers, underline emphasis layers, icon adornments, clipping regions, animation helpers, page containers, or toolkit-private navigation structures.
Those remain realization-private support structures unless they are explicitly published as realization resources or placement surfaces.
</p>

<p>
The default posture is:
</p>

<ul>
  <li><code>root</code> — overall layout, clipping, and outer realization region when needed,</li>
  <li><code>label</code> — dynamic text-bearing public part rendered through a realization-side placement surface,</li>
  <li><code>tab_header_region</code> — visible page-header navigation surface,</li>
  <li><code>selection_face</code> — visible selected-tab emphasis surface,</li>
  <li><code>page_region</code> — visible selected-page embodiment surface,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
A host may internally decompose the visible tab widget into headers, selected-tab chrome, page container, viewport, and animation structures.
Those remain realization-private unless explicitly published through a later realization-specific extension layer.
The stable public tab part model remains centered on <code>tab_header_region</code>, <code>selection_face</code>, <code>page_region</code>, <code>label</code>, and optional <code>frame</code>.
</p>

<hr/>

<h2 id="standard-visual-states">5. Standard Visual States</h2>

<p>
The default tab family defines at least:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code></li>
  <li><code>focused</code></li>
</ul>

<p>
For tab controls, the family MAY also define:
</p>

<ul>
  <li><code>selection_present</code> when the active realization explicitly distinguishes a current selected page</li>
  <li><code>selection_empty</code> when the active class posture allows explicit no-page state</li>
  <li><code>pressed</code> when the active host embodiment exposes a clear press-like tab-header interaction posture.</li>
</ul>

<p>
These are realization-side visual states.
They do not replace the public class meaning of <code>pages</code>, <code>pages.titles</code>, <code>value</code>, or <code>selection.index</code>.
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
  <li><code>tab_header_region</code> to provide a visible ordered page-header posture,</li>
  <li><code>selection_face</code> to distinguish the current selected tab clearly,</li>
  <li><code>page_region</code> to provide a visible selected-page surface,</li>
  <li><code>label</code> to remain readable across supported states,</li>
  <li><code>frame</code>, when present, to support focused posture where applicable.</li>
</ul>

<p>
A typical minimal mapping posture is:
</p>

<ul>
  <li><code>root</code> — global layout, clipping, and outer realization region,</li>
  <li><code>label</code> — dynamic text-bearing label surface,</li>
  <li><code>tab_header_region</code> — visible page-header navigation surface,</li>
  <li><code>selection_face</code> — selected-tab emphasis surface,</li>
  <li><code>page_region</code> — visible selected-page surface,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
The preferred machine-readable split is:
</p>

<ul>
  <li><code>tab_header_region</code> published through <code>part_bindings</code> plus optional state-sensitive <code>state_maps</code>,</li>
  <li><code>selection_face</code> published through <code>part_bindings</code> plus selection-sensitive <code>state_maps</code>,</li>
  <li><code>page_region</code> published through <code>part_bindings</code> plus optional state-sensitive <code>state_maps</code>,</li>
  <li><code>label</code> published primarily through a <code>part_binding</code> to an anchor, text region, or equivalent placement surface,</li>
  <li><code>frame</code>, when present, published through <code>part_bindings</code> plus optional <code>state_maps</code>.</li>
</ul>

<p>
The default family SHOULD keep this mapping explicit enough that a machine-readable package can distinguish:
</p>

<ul>
  <li>state-sensitive visual resources,</li>
  <li>structural part bindings,</li>
  <li>dynamic host-rendered or host-updated tab surfaces.</li>
</ul>

<hr/>

<h2 id="dynamic-surface-posture">7. Dynamic Surface Posture</h2>

<h3>7.1 Tab-header-region posture</h3>

<p>
The <code>tab_header_region</code> part is the main dynamic visible navigation surface of the tab family.
It is expected to reflect the ordered page inventory and associated visible titles rather than through runtime-private semantics hidden from inspection.
</p>

<p>
A host interpreting this realization is expected to embody the current page inventory visibly through <code>tab_header_region</code>.
The realization owns how the visible tab headers are embodied.
It does not become the semantic owner of page inventory or title inventory themselves.
</p>

<h3>7.2 Selection-face posture</h3>

<p>
The <code>selection_face</code> part is the main dynamic selected-tab emphasis surface.
It is expected to reflect the current selected page value and selected-page index.
</p>

<p>
The realization owns how the current selected tab is visually emphasized.
It does not become the semantic owner of selected page value or selected-page index themselves.
</p>

<h3>7.3 Page-region posture</h3>

<p>
The <code>page_region</code> part is the main dynamic selected-page embodiment surface.
It is expected to reflect the currently active page rather than through runtime-private semantics hidden from inspection.
</p>

<p>
The realization owns how the selected page is visually embodied.
It does not become the semantic owner of the selected page value itself.
</p>

<h3>7.4 Label posture</h3>

<p>
The semantic tab label text is not owned by this realization.
It is owned by the standardized class surface through <code>label.text</code>.
</p>

<p>
The role of the default realization is to define where and how that semantic label is visually embodied, not to become the source of truth for the label text itself.
</p>

<p>
The <code>label</code> part is therefore expected to be realized as a dynamic text-bearing surface.
A host interpreting this realization should render or inject the current semantic tab label into the realized label region at runtime.
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
A tab resource file MAY include placeholder page titles, decorative header guides, preview selected-tab emphasis, or design-time scaffolding.
However, a conforming realization family must not require that those asset-baked elements become the only path by which live page inventory, live page-title inventory, live selected-page value, live selected-page index, or live semantic label text is shown.
</p>

<p>
Likewise, selected-tab emphasis posture and focus posture must remain distinguishable from the semantic selected page itself.
</p>

<hr/>

<h2 id="resource-posture">8. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>tab_control/
  tab_header_region/
    normal
    disabled
    focused
    selection_present
    selection_empty
  selection_face/
    normal
    focused
    pressed
  page_region/
    normal
    disabled
    focused
  frame/
    normal
    focused
  anchors/
    label

tab_indicator/
  tab_header_region/
    normal
    disabled
    focused
    selection_present
    selection_empty
  selection_face/
    normal
    focused
  page_region/
    normal
    disabled
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
  <li><code>tab_control.tab_header_region.normal.svg</code></li>
  <li><code>tab_control.selection_face.focused.svg</code></li>
  <li><code>tab_control.page_region.normal.svg</code></li>
  <li><code>tab_control.label.anchor_map</code> backed by <code>./assets/tab_control/anchors/label.json</code></li>
  <li><code>tab_indicator.tab_header_region.normal.svg</code></li>
  <li><code>tab_indicator.selection_face.normal.svg</code></li>
  <li><code>tab_indicator.page_region.normal.svg</code></li>
  <li><code>tab_indicator.label.anchor_map</code> backed by <code>./assets/tab_indicator/anchors/label.json</code></li>
</ul>

<p>
Resources MAY be SVG-backed, host-native, toolkit-driven, or mixed.
The default family standardizes the part posture, state posture, and realization-side binding posture, not one mandatory tab implementation and not one mandatory file format.
</p>

<p>
In particular:
</p>

<ul>
  <li><code>tab_header_region</code> is the natural candidate for navigation-sensitive visible resources,</li>
  <li><code>selection_face</code> is the natural candidate for selected-tab emphasis resources,</li>
  <li><code>page_region</code> is the natural candidate for selected-page visible resources,</li>
  <li><code>label</code> is naturally a placement-bound dynamic text surface,</li>
  <li><code>frame</code>, when present, is a natural candidate for optional state-sensitive supporting resources.</li>
</ul>

<hr/>

<h2 id="host-expectations">9. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a clearly visible ordered page-header navigation surface,</li>
  <li>a clear visible distinction for the current selected tab,</li>
  <li>a clear visible selected-page region,</li>
  <li>clear visible distinction between enabled and disabled posture,</li>
  <li>reasonable focus indication for controls,</li>
  <li>dynamic rendering of visible tab label text.</li>
</ul>

<p>
A host SHOULD also preserve the distinction between:
</p>

<ul>
  <li>the semantic page inventory owned by the class,</li>
  <li>the semantic page-title inventory owned by <code>pages.titles</code>,</li>
  <li>the selected-page value owned by <code>value</code>,</li>
  <li>the selected-page index owned by <code>selection.index</code>,</li>
  <li>the tab label text owned by <code>label.text</code>,</li>
  <li>the realization-side embodiment of <code>tab_header_region</code>, <code>selection_face</code>, <code>page_region</code>, <code>label</code>, and <code>frame</code>.</li>
</ul>

<p>
A host MAY approximate the realization when exact resources are unavailable, but it should preserve:
</p>

<ul>
  <li>the interactive-versus-indicator distinction,</li>
  <li>the stable meaning of the published public parts,</li>
  <li>the separation between semantic tab data and realization resources.</li>
</ul>

<hr/>

<h2 id="fallback-posture">10. Fallback Posture</h2>

<p>
If state-specific resources are unavailable, a runtime MAY use host-native tab widgets or generic page-navigation rendering, provided the visible navigation posture and selected-page distinction remain preserved.
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
If selection-face-specific resources are unavailable, a host MAY fall back to host-native selected-tab emphasis posture provided that the selected-tab distinction remains visible and the page-navigation embodiment remains clear.
</p>

<p>
If page-region-specific resources are unavailable, a host MAY fall back to host-native selected-page rendering provided that selected-page posture remains visible.
</p>

<p>
Any fallback MUST preserve the published tab class law and the meaning of the public parts when those parts are exposed.
Fallback must not turn asset-baked page titles, selected-tab marks, page chrome, or label text into semantic truth.
</p>

<p>
Fallback must remain inspectable at the realization-publication layer.
It must not become a purely runtime-private convention.
</p>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
The default tab realization defines one official state-structured embodiment for tab controls and tab indicators, centered on the public <code>tab_header_region</code>, <code>selection_face</code>, and <code>page_region</code> parts.
</p>

<p>
It realizes:
</p>

<ul>
  <li><code>tab_header_region</code> as the main visible page-navigation surface,</li>
  <li><code>selection_face</code> as the dynamic selected-tab emphasis surface,</li>
  <li><code>page_region</code> as the dynamic selected-page visible surface,</li>
  <li><code>label</code> as a dynamically rendered text-bearing surface,</li>
  <li><code>frame</code> as an optional supporting outer surface.</li>
</ul>

<p>
Its resources may provide skins, layers, regions, and anchors.
Its package publication may provide <code>state_maps</code> and <code>part_bindings</code>.
Its host implementation may approximate the visuals when needed.
But the realization never becomes the semantic owner of page inventory, page-title inventory, selected-page value, selected-page index, label text, or tab class meaning.
</p>
