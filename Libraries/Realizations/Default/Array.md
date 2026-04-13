<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — Array Widget</h1>

<p align="center">
  <strong>Normative default realization posture for <code>frog.widgets.array</code></strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#target-class">2. Target Class</a></li>
  <li><a href="#realized-parts">3. Realized Parts</a></li>
  <li><a href="#standard-visual-states">4. Standard Visual States</a></li>
  <li><a href="#part-state-mapping">5. Part-State Mapping</a></li>
  <li><a href="#dynamic-surface-posture">6. Dynamic Surface Posture</a></li>
  <li><a href="#resource-posture">7. Resource Posture</a></li>
  <li><a href="#host-expectations">8. Host Expectations</a></li>
  <li><a href="#fallback-posture">9. Fallback Posture</a></li>
  <li><a href="#summary">10. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the default official realization posture for <code>frog.widgets.array</code>.
</p>

<p>
The default array realization is intended to provide one clean, inspectable, portable embodiment of the intrinsic array baseline without turning one repeated-layout engine, grid widget, or virtualization strategy into the semantic definition of the array.
</p>

<p>
This realization is realization-side only.
It does not redefine array class law, does not invent new public members, and does not replace the semantic ownership of array collection value or optional array label text.
Its job is to embody already-published array surfaces through stable visual states, stable part mappings, and realization-side structural placement metadata where needed.
</p>

<hr/>

<h2 id="target-class">2. Target Class</h2>

<ul>
  <li><strong>target class:</strong> <code>frog.widgets.array</code></li>
</ul>

<p>
This realization assumes the standardized array posture in which:
</p>

<ul>
  <li>the array exposes an ordered collection value through <code>value</code>,</li>
  <li>the array exposes collection length through <code>length</code>,</li>
  <li>the array may expose semantic label text through <code>label.text</code>,</li>
  <li>the array exposes stable public parts such as <code>element_region</code>,</li>
  <li>the realization remains downstream from that class contract.</li>
</ul>

<hr/>

<h2 id="realized-parts">3. Realized Parts</h2>

<ul>
  <li><code>root</code></li>
  <li><code>label</code> when the active class posture exposes it</li>
  <li><code>element_region</code></li>
  <li><code>index_display</code> when the active realization exposes an explicit current-index surface</li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The realization may internally use additional clipping regions, scroll helpers, repeated-cell guides, or host-native repeated-element structures.
Those remain realization-private support structures unless they are published elsewhere as part of an explicit realization package or a future higher-level array contract.
</p>

<hr/>

<h2 id="standard-visual-states">4. Standard Visual States</h2>

<p>
The default array realization defines at least:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code> when the active class posture exposes a meaningful disabled aggregate embodiment</li>
  <li><code>focused</code> when the host supports array-level focus posture</li>
</ul>

<p>
These are realization-side visual states.
They do not create new persistent array-owned source state by themselves.
</p>

<hr/>

<h2 id="part-state-mapping">5. Part-State Mapping</h2>

<p>
The default family expects:
</p>

<ul>
  <li><code>element_region</code> to provide the main repeated-element embodiment region,</li>
  <li><code>label</code> to remain readable when the label is shown,</li>
  <li><code>index_display</code>, when present, to remain readable and structurally consistent with the active realization,</li>
  <li><code>frame</code>, when present, to support focused posture where applicable.</li>
</ul>

<p>
A typical minimal mapping posture is:
</p>

<ul>
  <li><code>root</code> — global layout, clipping, and outer realization region,</li>
  <li><code>label</code> — optional dynamic text-bearing array label surface,</li>
  <li><code>element_region</code> — repeated-element embodiment region,</li>
  <li><code>index_display</code> — optional visible current-index or navigation support surface,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
The default family SHOULD keep this mapping explicit enough that a machine-readable package can distinguish:
</p>

<ul>
  <li>state-sensitive visual resources,</li>
  <li>structural part bindings,</li>
  <li>collection-support or navigation-support surfaces.</li>
</ul>

<hr/>

<h2 id="dynamic-surface-posture">6. Dynamic Surface Posture</h2>

<h3>6.1 Element-region posture</h3>

<p>
The <code>element_region</code> part is not just a decorative repeated grid.
It is the main structural realization surface through which array elements are visually embodied as part of the array.
</p>

<p>
A host interpreting this realization is expected to place and realize the current ordered element sequence inside that region according to the published array structure and the active front-panel layout posture.
</p>

<p>
The realization owns how that repeated-element region is visually embodied.
It does not become the semantic owner of the array collection value itself.
</p>

<h3>6.2 Label posture</h3>

<p>
The semantic array label text is not owned by this realization.
It is owned by the standardized class surface through <code>label.text</code> when that surface exists.
</p>

<p>
The role of the default realization is to define where and how that semantic label is visually embodied, not to become the source of truth for the label text itself.
</p>

<h3>6.3 Index-display posture</h3>

<p>
The <code>index_display</code> part is an optional realization-side support surface.
When present, it may display or support navigation of the current visible index without redefining array value semantics.
</p>

<p>
Its presence does not change the semantic owner of collection value.
It only supports the visible navigation posture of the realization.
</p>

<h3>6.4 Asset limitation rule</h3>

<p>
An array resource file MAY include placeholder cells, decorative repeated slots, preview values, or design-time scaffolding.
However, a conforming realization family must not require that those asset-baked structures become the only path by which live array collection value or live semantic label text is shown.
</p>

<hr/>

<h2 id="resource-posture">7. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>array/
  element_region/
    normal
    disabled
    focused
  index_display/
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
  <li><code>array.element_region.normal.svg</code></li>
  <li><code>array.element_region.focused.svg</code></li>
  <li><code>array.index_display.normal.svg</code> when the realization uses a distinct index surface</li>
  <li><code>array.frame.focused.svg</code></li>
  <li><code>array.label.anchor.json</code> or another explicit placement artifact</li>
</ul>

<p>
Resources MAY be SVG-backed, host-native, toolkit-driven, or mixed.
The default family standardizes the part posture, state posture, and realization-side binding posture, not one mandatory repeated-layout engine or one mandatory file format.
</p>

<hr/>

<h2 id="host-expectations">8. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a visible repeated-element region,</li>
  <li>readable optional array label when shown,</li>
  <li>reasonable array framing or grouping posture when the frame is present,</li>
  <li>host-compatible focus indication where supported.</li>
</ul>

<p>
A host SHOULD also preserve the distinction between:
</p>

<ul>
  <li>the semantic array collection value owned by the class,</li>
  <li>the optional array label text owned by <code>label.text</code>,</li>
  <li>the realization-side embodiment of label, element region, index display, and frame.</li>
</ul>

<p>
A host MAY approximate the realization when exact resources are unavailable, but it should preserve:
</p>

<ul>
  <li>the ordered collection identity of the array,</li>
  <li>the stable meaning of the published public parts,</li>
  <li>the separation between semantic collection value and realization resources.</li>
</ul>

<hr/>

<h2 id="fallback-posture">9. Fallback Posture</h2>

<p>
If specialized repeated-element or frame resources are unavailable, a runtime MAY use:
</p>

<ul>
  <li>a host-native repeated-element embodiment,</li>
  <li>a simplified framed region,</li>
  <li>a reduced but compatible collection embodiment preserving the published parts.</li>
</ul>

<p>
If specialized label or index-display placement resources are unavailable, a host MAY fall back to:
</p>

<ul>
  <li>a host-native text region,</li>
  <li>a generic index placement rule,</li>
  <li>another documented compatible placement surface.</li>
</ul>

<p>
Fallback is acceptable only if:
</p>

<ul>
  <li>the array remains visibly ordered and collection-like,</li>
  <li>published public parts remain interpretable,</li>
  <li>repeated layout helpers do not become the semantic owner of array meaning.</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The default array realization defines one official minimal embodiment of <code>frog.widgets.array</code> centered on label, element region, optional index display, and frame parts.
</p>

<p>
It realizes:
</p>

<ul>
  <li><code>element_region</code> as the main repeated-element embodiment surface,</li>
  <li><code>label</code> as an optional dynamically rendered text-bearing array label surface,</li>
  <li><code>index_display</code> as an optional array navigation or index-support surface,</li>
  <li><code>frame</code> as an optional supporting outer surface.</li>
</ul>

<p>
Its resources may provide repeated-layout visuals, navigation-support surfaces, and anchors.
Its package publication may provide state maps and bindings.
Its host implementation may approximate the visuals when needed.
But the realization never becomes the semantic owner of array collection value, array label text, or array class meaning.
</p>
