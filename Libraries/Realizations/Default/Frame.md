<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — Frame Widget</h1>

<p align="center">
  <strong>Normative default realization posture for <code>frog.widgets.frame</code></strong><br/>
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
This document defines the default official realization posture for <code>frog.widgets.frame</code>.
</p>

<p>
Its role is to provide a clean, state-structured embodiment of the standard frame without making decorative border assets or grouping visuals the owner of frame semantics.
</p>

<p>
The default realization is realization-side only.
It does not redefine widget class law, does not invent new public members, and does not replace the semantic ownership of frame visibility, optional title semantics, or grouping meaning.
Its job is to embody already-published widget surfaces through stable visual states, stable structural bindings, and explicit realization-side placement metadata.
</p>

<p>
The preferred architectural split is:
</p>

<ul>
  <li><code>state_maps</code> for state-sensitive visual embodiment,</li>
  <li><code>part_bindings</code> for stable structural correspondence,</li>
  <li>placement resources for optional dynamic public title surfaces rendered by the host.</li>
</ul>

<hr/>

<h2 id="target-class">2. Target Class</h2>

<ul>
  <li><strong>target class:</strong> <code>frog.widgets.frame</code></li>
</ul>

<p>
This realization assumes the standardized frame posture in which:
</p>

<ul>
  <li>the frame is support-oriented and structure-oriented,</li>
  <li>the frame exposes a stable <code>border</code> part,</li>
  <li>the frame may expose a stable <code>title_surface</code> part when the active class posture supports it,</li>
  <li>the optional semantic user-authored title text is owned by <code>title.text</code>,</li>
  <li>the realization remains downstream from that class contract.</li>
</ul>

<p>
This realization therefore publishes embodiment and placement posture for the frame.
It does not become the semantic owner of grouping meaning or optional title content.
</p>

<hr/>

<h2 id="realized-parts">3. Realized Parts</h2>

<p>
The default frame realization targets the following public parts:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>border</code></li>
  <li><code>title_surface</code> when the active class posture exposes it</li>
  <li><code>content_region</code> when the active realization exposes an explicit grouped region</li>
</ul>

<p>
The realization may internally use additional decorative lines, corners, title anchors, padding regions, grouping surfaces, or host-native group structures, but those remain realization-private support structures unless they are explicitly published as realization resources or placement surfaces.
</p>

<p>
The default posture is:
</p>

<ul>
  <li><code>root</code> — overall host layout region when needed,</li>
  <li><code>border</code> — main grouping or emphasis visual surface of the frame,</li>
  <li><code>title_surface</code> — optional dynamic text-bearing public part rendered through a realization-side placement surface,</li>
  <li><code>content_region</code> — optional grouped region associated with the frame embodiment.</li>
</ul>

<hr/>

<h2 id="standard-visual-states">4. Standard Visual States</h2>

<p>
The default frame realization defines at least:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>hidden</code> when the host models invisible support widgets through an explicit realization posture</li>
  <li><code>focused</code> when the active class posture or host uses focus-capable support grouping posture</li>
</ul>

<p>
These are realization-side visual states.
They do not redefine the semantic meaning of frame grouping or optional title semantics.
</p>

<p>
The default family does not require pressed-like posture for the frame baseline because the standardized frame is not a command widget.
</p>

<hr/>

<h2 id="part-state-mapping">5. Part-State Mapping</h2>

<p>
The default family expects:
</p>

<ul>
  <li><code>border</code> to remain visible and structurally coherent across supported states,</li>
  <li><code>title_surface</code>, when present, to remain readable,</li>
  <li><code>content_region</code>, when present, to remain structurally aligned with the grouping embodiment.</li>
</ul>

<p>
A typical minimal mapping posture is:
</p>

<ul>
  <li><code>root</code> — global layout, clipping, and outer realization region,</li>
  <li><code>border</code> — main grouping contour or emphasis surface,</li>
  <li><code>title_surface</code> — optional dynamic text-bearing realized surface positioned through realization metadata,</li>
  <li><code>content_region</code> — optional grouped layout region associated with the frame.</li>
</ul>

<p>
The default family SHOULD keep the mapping explicit enough that a machine-readable package can bind:
</p>

<ul>
  <li>a part to a resource layer,</li>
  <li>a part to a state-scoped resource,</li>
  <li>a part to a visual anchor, text region, or host-native grouping region.</li>
</ul>

<hr/>

<h2 id="dynamic-surface-posture">6. Dynamic Surface Posture</h2>

<h3>6.1 Semantic title ownership versus realization ownership</h3>

<p>
When the active class posture exposes title text, the semantic frame title is not owned by this realization.
It is owned by the standardized class surface through <code>title.text</code>.
</p>

<p>
The role of the default realization is to define where and how that semantic title is visually embodied, not to become the source of truth for the title itself.
</p>

<h3>6.2 Title-surface embodiment</h3>

<p>
The <code>title_surface</code> part, when present, is realized as a dynamic text-bearing surface.
A host interpreting this realization is expected to render or inject the current semantic frame title into the realized title region at runtime.
</p>

<p>
The default realization therefore assumes a separation between:
</p>

<ul>
  <li>semantic title text owned by the widget class,</li>
  <li>title styling owned by published widget-visible properties when supported,</li>
  <li>title placement owned by realization,</li>
  <li>decorative grouping visuals owned by the asset layer.</li>
</ul>

<h3>6.3 Title anchors and placement metadata</h3>

<p>
The default family SHOULD publish an explicit placement surface for <code>title_surface</code> when that part exists.
That placement surface may take the form of:
</p>

<ul>
  <li>a named <code>text_anchor</code>,</li>
  <li>an anchor map entry,</li>
  <li>a host-native title region,</li>
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
Those realization-side structures do not change the public meaning of <code>title.text</code>.
They only specify where the host should visually place the title.
</p>

<h3>6.4 Border and grouping posture</h3>

<p>
The <code>border</code> and <code>content_region</code> parts are realization-side grouping and embodiment surfaces.
They provide the visible grouping posture of the frame without becoming the semantic owner of the frame's support meaning.
</p>

<h3>6.5 SVG posture</h3>

<p>
SVG-backed resources MAY provide:
</p>

<ul>
  <li>border geometry,</li>
  <li>decorative corners or emphasis lines,</li>
  <li>title anchor geometry or placement hints,</li>
  <li>content-region guidance surfaces.</li>
</ul>

<p>
However, the SVG resource must not be the sole owner of the live user-visible frame title when title support exists.
Placeholder title text, decorative outlines, or preview text may appear in design resources, but a conforming host must remain able to render the actual semantic title dynamically.
</p>

<hr/>

<h2 id="resource-posture">7. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>frame/
  border/
    normal
    hidden
    focused
  title_surface/
    normal
    focused
  content_region/
    normal
  anchors/
    title_surface
</code></pre>

<p>
An equivalent package-oriented posture may publish resources such as:
</p>

<ul>
  <li><code>frame.border.normal.svg</code></li>
  <li><code>frame.border.focused.svg</code></li>
  <li><code>frame.title_surface.normal.svg</code> when the family uses a separate title-support layer</li>
  <li><code>frame.content_region.normal.svg</code> when the family publishes explicit grouped-region guidance</li>
  <li><code>frame.title_surface.anchor.json</code> or another explicit anchor-map artifact</li>
</ul>

<p>
Resources MAY be SVG-backed, host-native, or toolkit-driven.
The default family standardizes the state posture, part posture, and realization-side binding posture, not one mandatory file format.
</p>

<p>
In particular, the optional title-bearing part SHOULD preferably bind to a placement surface such as an anchor or text region rather than to a resource that hardcodes the final user-facing title content.
</p>

<hr/>

<h2 id="host-expectations">8. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a clearly perceivable grouping or emphasis surface,</li>
  <li>visible hidden or focused posture where the host supports it,</li>
  <li>dynamic rendering or injection of <code>title.text</code> into the realized title surface when title support exists,</li>
  <li>state-consistent readability of the optional title across supported visual states.</li>
</ul>

<p>
A host MAY approximate the realization when exact resources are unavailable, but it should preserve:
</p>

<ul>
  <li>the grouping identity of the frame,</li>
  <li>the stable meaning of the public parts,</li>
  <li>the separation between semantic support meaning and decorative assets.</li>
</ul>

<hr/>

<h2 id="fallback-posture">9. Fallback Posture</h2>

<p>
If a specialized resource is unavailable:
</p>

<ul>
  <li><code>focused</code> MAY fall back to a host-native emphasis posture,</li>
  <li><code>hidden</code> MAY fall back to host-managed visibility suppression,</li>
  <li><code>title_surface</code>, when present, MUST remain dynamically renderable even when a dedicated anchor asset is unavailable.</li>
</ul>

<p>
If no explicit title anchor is available, the host MAY fall back to a reasonable default title region or another stable host-native placement rule, provided that:
</p>

<ul>
  <li>the title remains readable,</li>
  <li>the grouping posture remains clear,</li>
  <li>the fallback does not turn asset-baked title text into semantic truth.</li>
</ul>

<p>
If no explicit content-region guidance is available, the host MAY fall back to a generic grouped region compatible with the frame posture, provided that the frame remains visibly structural and support-oriented.
</p>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The default frame realization defines one official state-structured embodiment of <code>frog.widgets.frame</code> with stable parts and stable grouping posture.
</p>

<p>
It realizes:
</p>

<ul>
  <li><code>border</code> as the main grouping or emphasis surface,</li>
  <li><code>title_surface</code> as an optional dynamically rendered text-bearing surface,</li>
  <li><code>content_region</code> as an optional grouped-region support surface.</li>
</ul>

<p>
Its resources may provide geometry, grouping visuals, and anchors.
Its package publication may provide state maps and part bindings.
Its host implementation may approximate the visuals when needed.
But the realization never becomes the semantic owner of optional frame title text or of frame support meaning.
</p>
