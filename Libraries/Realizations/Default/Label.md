<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — Label Widget</h1>

<p align="center">
  <strong>Normative default realization posture for <code>frog.widgets.label</code></strong><br/>
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
This document defines the default official realization posture for <code>frog.widgets.label</code>.
</p>

<p>
The default label realization is intended to provide one clean, inspectable, portable embodiment of the intrinsic label baseline without turning one host text primitive, one SVG text layer, or one decorative typography system into the semantic definition of the label.
</p>

<p>
This realization is realization-side only.
It does not redefine label class law, does not invent new public members, and does not replace the semantic ownership of label text.
Its job is to embody already-published label surfaces through stable visual states, stable part mappings, and realization-side placement or rendering metadata where needed.
</p>

<p>
The preferred architectural split is:
</p>

<ul>
  <li><code>state_maps</code> for state-sensitive visual embodiment,</li>
  <li><code>part_bindings</code> for stable structural correspondence,</li>
  <li>placement resources for dynamic public text rendered by the host.</li>
</ul>

<hr/>

<h2 id="target-class">2. Target Class</h2>

<ul>
  <li><strong>target class:</strong> <code>frog.widgets.label</code></li>
</ul>

<p>
This realization assumes the standardized label posture in which:
</p>

<ul>
  <li>the label is support-oriented,</li>
  <li>the label exposes a semantic text surface through <code>text</code>,</li>
  <li>the label exposes a stable <code>text_surface</code> part,</li>
  <li>the realization remains downstream from that class contract.</li>
</ul>

<p>
This realization therefore publishes embodiment and placement posture for the label.
It does not become the semantic owner of the label content.
</p>

<hr/>

<h2 id="realized-parts">3. Realized Parts</h2>

<p>
The default label realization targets the following public parts:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>text_surface</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The realization may internally use additional anchors, clipping regions, baseline helpers, decorative emphasis layers, or host-native text regions, but those remain realization-private support structures unless they are explicitly published as realization resources or placement surfaces.
</p>

<p>
The default posture is:
</p>

<ul>
  <li><code>root</code> — overall host layout region when needed,</li>
  <li><code>text_surface</code> — main dynamic semantic text-bearing part rendered through a realization-side placement surface,</li>
  <li><code>frame</code> — optional contour or emphasis surface when the realization family publishes it separately.</li>
</ul>

<hr/>

<h2 id="standard-visual-states">4. Standard Visual States</h2>

<p>
The default label realization defines at least:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code> when the active class posture or host uses disabled support-text posture</li>
  <li><code>focused</code> when the host supports focus posture for support widgets</li>
</ul>

<p>
These are realization-side visual states.
They do not redefine the semantic meaning of the label text itself.
</p>

<p>
The default family does not require pressed-like posture for the label baseline because the standardized label is not a command widget.
</p>

<hr/>

<h2 id="part-state-mapping">5. Part-State Mapping</h2>

<p>
The default family expects:
</p>

<ul>
  <li><code>text_surface</code> to remain readable across supported states,</li>
  <li><code>frame</code>, when present, to remain visually coherent with the active state.</li>
</ul>

<p>
A typical minimal mapping posture is:
</p>

<ul>
  <li><code>root</code> — global layout, clipping, and outer realization region,</li>
  <li><code>text_surface</code> — dynamic semantic text-bearing realized surface positioned through realization metadata,</li>
  <li><code>frame</code> — optional emphasis or grouping surface.</li>
</ul>

<p>
The default family SHOULD keep the mapping explicit enough that a machine-readable package can bind:
</p>

<ul>
  <li>a part to a resource layer,</li>
  <li>a part to a state-scoped resource,</li>
  <li>a part to a visual anchor, text region, or host-native region.</li>
</ul>

<hr/>

<h2 id="dynamic-surface-posture">6. Dynamic Surface Posture</h2>

<h3>6.1 Semantic text ownership versus realization ownership</h3>

<p>
The semantic label text is not owned by this realization.
It is owned by the standardized class surface through <code>text</code>.
</p>

<p>
The role of the default realization is to define where and how that semantic text is visually embodied, not to become the source of truth for the text itself.
</p>

<h3>6.2 Text-surface embodiment</h3>

<p>
The <code>text_surface</code> part is realized as a dynamic text-bearing surface.
A host interpreting this realization is expected to render or inject the current semantic label text into the realized text region at runtime.
</p>

<p>
The default realization therefore assumes a separation between:
</p>

<ul>
  <li>semantic text owned by the widget class,</li>
  <li>text styling owned by published widget-visible properties when supported,</li>
  <li>text placement owned by realization,</li>
  <li>decorative visual content owned by the asset layer.</li>
</ul>

<h3>6.3 Text anchors and placement metadata</h3>

<p>
The default family SHOULD publish an explicit placement surface for <code>text_surface</code>.
That placement surface may take the form of:
</p>

<ul>
  <li>a named <code>text_anchor</code>,</li>
  <li>an anchor map entry,</li>
  <li>a host-native text region,</li>
  <li>an equivalent explicitly published placement binding.</li>
</ul>

<p>
That placement metadata may define:
</p>

<ul>
  <li>alignment box or anchor point,</li>
  <li>horizontal and vertical alignment,</li>
  <li>padding or inset region,</li>
  <li>clipping region,</li>
  <li>baseline or center alignment posture.</li>
</ul>

<p>
Those realization-side structures do not change the public meaning of <code>text</code>.
They only specify where the host should visually place the text.
</p>

<h3>6.4 SVG posture</h3>

<p>
SVG-backed resources MAY provide:
</p>

<ul>
  <li>decorative emphasis geometry,</li>
  <li>support-text background shapes,</li>
  <li>anchor geometry or placement hints for text,</li>
  <li>optional frame or underline visuals.</li>
</ul>

<p>
However, the SVG resource must not be the sole owner of the live user-visible label text.
Placeholder text, decorative outlines, or preview text may appear in design resources, but a conforming host must remain able to render the actual semantic text dynamically.
</p>

<hr/>

<h2 id="resource-posture">7. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>label/
  text_surface/
    normal
    disabled
    focused
  frame/
    normal
    focused
  anchors/
    text_surface
</code></pre>

<p>
An equivalent package-oriented posture may publish resources such as:
</p>

<ul>
  <li><code>label.text_surface.normal.svg</code></li>
  <li><code>label.text_surface.disabled.svg</code></li>
  <li><code>label.text_surface.focused.svg</code></li>
  <li><code>label.frame.normal.svg</code> when the family uses a separate frame layer</li>
  <li><code>label.text_surface.anchor.json</code> or another explicit anchor-map artifact</li>
</ul>

<p>
Resources MAY be SVG-backed, host-native, or toolkit-driven.
The default family standardizes the state posture, part posture, and realization-side binding posture, not one mandatory file format.
</p>

<p>
In particular, the text-bearing part SHOULD preferably bind to a placement surface such as an anchor or text region rather than to a resource that hardcodes the final user-facing text content.
</p>

<hr/>

<h2 id="host-expectations">8. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a clearly readable text surface,</li>
  <li>visible disabled posture where the host supports it,</li>
  <li>visible focus posture where the host supports it,</li>
  <li>dynamic rendering or injection of <code>text</code> into the realized text surface,</li>
  <li>state-consistent readability across supported visual states.</li>
</ul>

<p>
A host MAY approximate the realization when exact resources are unavailable, but it should preserve:
</p>

<ul>
  <li>the support-text identity of the label,</li>
  <li>the stable meaning of the public parts,</li>
  <li>the separation between semantic text and decorative assets.</li>
</ul>

<hr/>

<h2 id="fallback-posture">9. Fallback Posture</h2>

<p>
If a specialized resource is unavailable:
</p>

<ul>
  <li><code>focused</code> MAY fall back to a host-native emphasis posture,</li>
  <li><code>disabled</code> MAY fall back to a host-native disabled text embodiment,</li>
  <li><code>text_surface</code> MUST remain dynamically renderable even when a dedicated anchor asset is unavailable.</li>
</ul>

<p>
If no explicit text anchor is available, the host MAY fall back to a reasonable default text region or another stable host-native placement rule, provided that:
</p>

<ul>
  <li>the text remains readable,</li>
  <li>the support-text posture remains clear,</li>
  <li>the fallback does not turn asset-baked text into semantic truth.</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The default label realization defines one official state-structured embodiment of <code>frog.widgets.label</code> with stable parts and stable support-text posture.
</p>

<p>
It realizes:
</p>

<ul>
  <li><code>text_surface</code> as the main dynamically rendered text-bearing surface,</li>
  <li><code>frame</code> as an optional supporting emphasis surface.</li>
</ul>

<p>
Its resources may provide geometry, skins, and anchors.
Its package publication may provide state maps and part bindings.
Its host implementation may approximate the visuals when needed.
But the realization never becomes the semantic owner of the label text.
</p>
