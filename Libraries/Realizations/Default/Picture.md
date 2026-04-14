<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — Picture Widgets</h1>

<p align="center">
  <strong>Normative default realization posture for standardized picture widgets</strong><br/>
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
This document defines the default official realization posture for the standardized picture widget family.
</p>

<p>
The default picture realization is intended to provide one clean, inspectable, portable embodiment of the intrinsic picture baseline without turning one host image widget, one toolkit-specific canvas surface, or one runtime-private rendering engine into the semantic definition of picture widgets.
</p>

<p>
This realization is realization-side only.
It does not redefine picture class law, does not invent new public members, and does not replace the semantic ownership of picture value, viewport metadata, pointer metadata, or label text.
Its job is to embody already-published picture widget surfaces through stable visual states, stable structural bindings, and realization-side placement or rendering metadata where needed.
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
  <li><code>frog.widgets.picture_control</code></li>
  <li><code>frog.widgets.picture_indicator</code></li>
</ul>

<p>
This realization assumes the standardized picture posture in which:
</p>

<ul>
  <li>picture widgets expose visible content through <code>value</code>,</li>
  <li>picture widgets may expose viewport metadata through <code>viewport.origin</code> and <code>viewport.scale</code>,</li>
  <li>picture controls may expose pointer metadata through <code>pointer.position</code>,</li>
  <li>picture widgets may expose semantic label text through <code>label.text</code>,</li>
  <li>the published public parts remain stable across realizations,</li>
  <li>the realization remains downstream from that class contract.</li>
</ul>

<p>
The realization therefore owns embodiment and placement posture for picture widgets.
It does not become the semantic owner of picture value, viewport metadata, pointer metadata, or label content.
</p>

<hr/>

<h2 id="realization-variant-posture">3. Realization Variant Posture</h2>

<p>
The default picture family standardizes one picture realization corridor, not one mandatory visible shape.
</p>

<p>
Accordingly, a conforming realization MAY choose a picture embodiment posture such as:
</p>

<ul>
  <li>raster-like visible picture surface,</li>
  <li>vector-like visible picture surface,</li>
  <li>mixed image-and-overlay embodiment,</li>
  <li>another host-compatible visible picture embodiment.</li>
</ul>

<p>
Those remain realization variants of the same published picture classes.
A different visible rendering strategy does not by itself define a new intrinsic widget class.
</p>

<p>
This distinction is normative:
</p>

<ul>
  <li>the class layer owns picture semantics, viewport semantics, pointer semantics, public members, methods, events, and parts,</li>
  <li>the realization layer owns how those published surfaces are visually embodied,</li>
  <li>a runtime MUST NOT treat a toolkit-native image view or canvas view as if it were a distinct standard class unless a separate class contract is explicitly published elsewhere.</li>
</ul>

<hr/>

<h2 id="realized-parts">4. Realized Parts</h2>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>picture_region</code></li>
  <li><code>overlay_region</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The realization may internally use additional clipping layers, focus layers, pointer layers, zoom helpers, cached buffers, or toolkit-private rendering structures.
Those remain realization-private support structures unless they are explicitly published as realization resources or placement surfaces.
</p>

<p>
The default posture is:
</p>

<ul>
  <li><code>root</code> — overall layout, clipping, and outer realization region when needed,</li>
  <li><code>label</code> — dynamic text-bearing public part rendered through a realization-side placement surface,</li>
  <li><code>picture_region</code> — main visible picture embodiment surface,</li>
  <li><code>overlay_region</code> — visible overlay and helper surface when overlays are shown,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
A host may internally decompose the visible picture widget into content buffers, overlay layers, clipping regions, and viewport transforms.
Those remain realization-private unless explicitly published through a later realization-specific extension layer.
The stable public picture part model remains centered on <code>picture_region</code>, <code>overlay_region</code>, <code>label</code>, and optional <code>frame</code>.
</p>

<hr/>

<h2 id="standard-visual-states">5. Standard Visual States</h2>

<p>
The default picture family defines at least:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code></li>
  <li><code>focused</code></li>
</ul>

<p>
For picture controls, the family MAY also define:
</p>

<ul>
  <li><code>pointer_present</code> when the active realization explicitly distinguishes a current pointer posture</li>
  <li><code>pointer_absent</code> when the active realization explicitly distinguishes a no-pointer posture</li>
  <li><code>pressed</code> when the active host embodiment exposes a clear press-like picture interaction posture.</li>
</ul>

<p>
These are realization-side visual states.
They do not replace the public class meaning of <code>value</code>, <code>viewport.origin</code>, <code>viewport.scale</code>, or <code>pointer.position</code>.
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
  <li><code>picture_region</code> to provide a visible drawable picture posture,</li>
  <li><code>overlay_region</code> to provide visible helper or emphasis posture when overlays are used,</li>
  <li><code>label</code> to remain readable across supported states,</li>
  <li><code>frame</code>, when present, to support focused posture where applicable.</li>
</ul>

<p>
A typical minimal mapping posture is:
</p>

<ul>
  <li><code>root</code> — global layout, clipping, and outer realization region,</li>
  <li><code>label</code> — dynamic text-bearing label surface,</li>
  <li><code>picture_region</code> — main visible picture surface,</li>
  <li><code>overlay_region</code> — visible overlay and emphasis surface,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
The preferred machine-readable split is:
</p>

<ul>
  <li><code>picture_region</code> published through <code>part_bindings</code> plus optional state-sensitive <code>state_maps</code>,</li>
  <li><code>overlay_region</code> published through <code>part_bindings</code> plus optional interaction-sensitive <code>state_maps</code>,</li>
  <li><code>label</code> published primarily through a <code>part_binding</code> to an anchor, text region, or equivalent placement surface,</li>
  <li><code>frame</code>, when present, published through <code>part_bindings</code> plus optional <code>state_maps</code>.</li>
</ul>

<p>
The default family SHOULD keep this mapping explicit enough that a machine-readable package can distinguish:
</p>

<ul>
  <li>state-sensitive visual resources,</li>
  <li>structural part bindings,</li>
  <li>dynamic host-rendered or host-updated picture surfaces.</li>
</ul>

<hr/>

<h2 id="dynamic-surface-posture">7. Dynamic Surface Posture</h2>

<h3>7.1 Picture-region posture</h3>

<p>
The <code>picture_region</code> part is the main dynamic visible surface of the picture family.
It is expected to reflect the current picture value visibly rather than through runtime-private semantics hidden from inspection.
</p>

<p>
A host interpreting this realization is expected to embody the current picture value visibly through <code>picture_region</code>.
The realization owns how the visible picture surface is embodied.
It does not become the semantic owner of the picture value itself.
</p>

<h3>7.2 Overlay-region posture</h3>

<p>
The <code>overlay_region</code> part is the public visible helper and emphasis surface.
It is expected to reflect visible focus posture, pointer emphasis, or bounded helper marks when the active realization uses them.
</p>

<p>
The realization owns how overlays are visually embodied.
It does not become the semantic owner of picture content, viewport metadata, or pointer metadata themselves.
</p>

<h3>7.3 Label posture</h3>

<p>
The semantic picture label text is not owned by this realization.
It is owned by the standardized class surface through <code>label.text</code>.
</p>

<p>
The role of the default realization is to define where and how that semantic label is visually embodied, not to become the source of truth for the label text itself.
</p>

<p>
The <code>label</code> part is therefore expected to be realized as a dynamic text-bearing surface.
A host interpreting this realization should render or inject the current semantic picture label into the realized label region at runtime.
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
A picture resource file MAY include placeholder imagery, decorative guides, preview overlays, or design-time scaffolding.
However, a conforming realization family must not require that those asset-baked elements become the only path by which live picture value, live viewport metadata, live pointer metadata, or live semantic label text is shown.
</p>

<p>
Likewise, overlay emphasis posture and focus posture must remain distinguishable from the semantic picture value itself.
</p>

<hr/>

<h2 id="resource-posture">8. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>picture_control/
  picture_region/
    normal
    disabled
    focused
  overlay_region/
    normal
    pointer_present
    pressed
  frame/
    normal
    focused
  anchors/
    label

picture_indicator/
  picture_region/
    normal
    disabled
    focused
  overlay_region/
    normal
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
  <li><code>picture_control.picture_region.normal.svg</code></li>
  <li><code>picture_control.overlay_region.pointer_present.svg</code></li>
  <li><code>picture_control.frame.focused.svg</code></li>
  <li><code>picture_control.label.anchor_map</code> backed by <code>./assets/picture_control/anchors/label.json</code></li>
  <li><code>picture_indicator.picture_region.normal.svg</code></li>
  <li><code>picture_indicator.overlay_region.normal.svg</code></li>
  <li><code>picture_indicator.frame.focused.svg</code></li>
  <li><code>picture_indicator.label.anchor_map</code> backed by <code>./assets/picture_indicator/anchors/label.json</code></li>
</ul>

<p>
Resources MAY be SVG-backed, raster-backed, host-native, toolkit-driven, or mixed.
The default family standardizes the part posture, state posture, and realization-side binding posture, not one mandatory rendering engine and not one mandatory file format.
</p>

<p>
In particular:
</p>

<ul>
  <li><code>picture_region</code> is the natural candidate for content-sensitive visible resources,</li>
  <li><code>overlay_region</code> is the natural candidate for helper and emphasis resources,</li>
  <li><code>label</code> is naturally a placement-bound dynamic text surface,</li>
  <li><code>frame</code>, when present, is a natural candidate for optional state-sensitive supporting resources.</li>
</ul>

<hr/>

<h2 id="host-expectations">9. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a clearly visible picture surface,</li>
  <li>a visible overlay or emphasis posture when overlays are used,</li>
  <li>clear visible distinction between enabled and disabled posture,</li>
  <li>reasonable focus indication for controls,</li>
  <li>dynamic rendering of visible picture label text.</li>
</ul>

<p>
A host SHOULD also preserve the distinction between:
</p>

<ul>
  <li>the semantic picture value owned by the class,</li>
  <li>the viewport metadata owned by <code>viewport.origin</code> and <code>viewport.scale</code>,</li>
  <li>the pointer metadata owned by <code>pointer.position</code>,</li>
  <li>the picture label text owned by <code>label.text</code>,</li>
  <li>the realization-side embodiment of <code>picture_region</code>, <code>overlay_region</code>, <code>label</code>, and <code>frame</code>.</li>
</ul>

<p>
A host MAY approximate the realization when exact resources are unavailable, but it should preserve:
</p>

<ul>
  <li>the interactive-versus-indicator distinction,</li>
  <li>the stable meaning of the published public parts,</li>
  <li>the separation between semantic picture data and realization resources.</li>
</ul>

<hr/>

<h2 id="fallback-posture">10. Fallback Posture</h2>

<p>
If state-specific resources are unavailable, a runtime MAY use host-native picture widgets or generic visible picture rendering, provided the visible picture posture remains preserved.
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
If overlay-region-specific resources are unavailable, a host MAY fall back to host-native helper or focus posture provided that the visible emphasis remains clear where supported.
</p>

<p>
If picture-region-specific resources are unavailable, a host MAY fall back to another compatible visible picture embodiment provided that picture meaning remains visible.
</p>

<p>
Any fallback MUST preserve the published picture class law and the meaning of the public parts when those parts are exposed.
Fallback must not turn asset-baked imagery, overlay marks, or label text into semantic truth.
</p>

<p>
Fallback must remain inspectable at the realization-publication layer.
It must not become a purely runtime-private convention.
</p>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
The default picture realization defines one official state-structured embodiment for picture controls and picture indicators, centered on the public <code>picture_region</code> and <code>overlay_region</code> parts.
</p>

<p>
It realizes:
</p>

<ul>
  <li><code>picture_region</code> as the main visible picture surface,</li>
  <li><code>overlay_region</code> as the dynamic overlay and emphasis surface,</li>
  <li><code>label</code> as a dynamically rendered text-bearing surface,</li>
  <li><code>frame</code> as an optional supporting outer surface.</li>
</ul>

<p>
Its resources may provide skins, layers, regions, and anchors.
Its package publication may provide <code>state_maps</code> and <code>part_bindings</code>.
Its host implementation may approximate the visuals when needed.
But the realization never becomes the semantic owner of picture value, viewport metadata, pointer metadata, label text, or picture class meaning.
</p>
