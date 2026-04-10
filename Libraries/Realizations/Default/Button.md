<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — Button</h1>

<p align="center">
  <strong>Normative default realization posture for <code>frog.widgets.button</code></strong><br/>
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
  <li><a href="#text-realization-posture">6. Text Realization Posture</a></li>
  <li><a href="#resource-posture">7. Resource Posture</a></li>
  <li><a href="#host-expectations">8. Host Expectations</a></li>
  <li><a href="#fallback-posture">9. Fallback Posture</a></li>
  <li><a href="#summary">10. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the default official realization posture for <code>frog.widgets.button</code>.
</p>

<p>
Its role is to provide a clean, state-structured embodiment of the standard button without making the visual assets the owner of button semantics.
</p>

<p>
The default realization is realization-side only.
It does not redefine widget class law, does not invent new public members, and does not replace the semantic ownership of the button label text.
Its job is to embody already-published widget surfaces through stable visual states, stable part mappings, and explicit realization-side placement metadata.
</p>

<hr/>

<h2 id="target-class">2. Target Class</h2>

<ul>
  <li><strong>target class:</strong> <code>frog.widgets.button</code></li>
</ul>

<p>
This realization assumes the standardized button posture in which:
</p>

<ul>
  <li>the button is command-oriented,</li>
  <li>the button exposes a stable <code>label</code> part,</li>
  <li>the semantic user-authored label text is owned by <code>label.text</code>,</li>
  <li>the realization remains downstream from that class contract.</li>
</ul>

<hr/>

<h2 id="realized-parts">3. Realized Parts</h2>

<p>
The default button realization targets the following public parts:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>face</code></li>
  <li><code>label</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The realization may internally use additional layers, anchors, or host-native regions, but those remain realization-private support structures.
They do not become new public widget parts unless published elsewhere as part of widget class law.
</p>

<hr/>

<h2 id="standard-visual-states">4. Standard Visual States</h2>

<p>
The default button realization defines the following standard visual states:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code></li>
  <li><code>focused</code></li>
  <li><code>pressed</code></li>
</ul>

<p>
The host MAY also support <code>hovered</code>, but it is not required in the minimal default realization posture.
</p>

<p>
These states are realization-side visual states.
They do not redefine the semantic contract of the button and they do not create persistent button-owned source state by themselves.
</p>

<hr/>

<h2 id="part-state-mapping">5. Part-State Mapping</h2>

<p>
The default family expects at least:
</p>

<ul>
  <li><code>face</code> to vary across <code>normal</code>, <code>disabled</code>, <code>focused</code>, and <code>pressed</code>,</li>
  <li><code>label</code> to remain readable in all supported states,</li>
  <li><code>frame</code>, when present, to remain visually consistent with the current state.</li>
</ul>

<p>
A typical minimal mapping posture is:
</p>

<ul>
  <li><code>root</code> — global host layout region and clipping boundary when needed,</li>
  <li><code>face</code> — state-sensitive visual body of the button,</li>
  <li><code>label</code> — dynamic text-bearing realized surface positioned through realization metadata,</li>
  <li><code>frame</code> — optional contour or outer emphasis layer.</li>
</ul>

<p>
The default family SHOULD keep the mapping explicit enough that a machine-readable package can bind:
</p>

<ul>
  <li>a part to a resource layer,</li>
  <li>a part to a state-scoped resource,</li>
  <li>a part to a visual anchor or host-native region.</li>
</ul>

<hr/>

<h2 id="text-realization-posture">6. Text Realization Posture</h2>

<h3>6.1 Semantic ownership versus realization ownership</h3>

<p>
The semantic button label text is not owned by this realization.
It is owned by the standardized class surface through <code>label.text</code>.
</p>

<p>
The role of the default realization is to define where and how that semantic text is visually embodied, not to become the source of truth for the text itself.
</p>

<h3>6.2 Label embodiment</h3>

<p>
The <code>label</code> part is realized as a dynamic text-bearing surface.
A host interpreting this realization is expected to render or inject the current semantic label text into the realized label region at runtime.
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
The default family SHOULD publish an explicit placement surface for <code>label</code>.
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
Those realization-side structures do not change the public meaning of <code>label.text</code>.
They only specify where the host should visually place the text.
</p>

<h3>6.4 SVG posture</h3>

<p>
SVG-backed resources MAY provide:
</p>

<ul>
  <li>button background and frame geometry,</li>
  <li>state-specific face visuals,</li>
  <li>decorative label containers,</li>
  <li>anchor geometry or placement hints for text.</li>
</ul>

<p>
However, the SVG resource must not be the sole owner of the live user-visible button text.
Placeholder text, decorative outlines, or preview text may appear in design resources, but a conforming host must remain able to render the actual semantic label dynamically.
</p>

<h3>6.5 State interaction with text</h3>

<p>
The default realization MAY vary text appearance across states such as <code>normal</code> and <code>disabled</code>, for example through color, opacity, contrast, or host-native emphasis changes.
</p>

<p>
However, the default realization does not define intrinsic state-dependent semantic text switching.
It does not introduce <code>label.text_on</code> or <code>label.text_off</code>, and it does not infer alternate text semantics from face-state assets alone.
</p>

<hr/>

<h2 id="resource-posture">7. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>button/
  face/
    normal
    disabled
    focused
    pressed
  frame/
    normal
    disabled
    focused
    pressed
  anchors/
    label
</code></pre>

<p>
An equivalent package-oriented posture may publish resources such as:
</p>

<ul>
  <li><code>button.face.normal.svg</code></li>
  <li><code>button.face.disabled.svg</code></li>
  <li><code>button.face.focused.svg</code></li>
  <li><code>button.face.pressed.svg</code></li>
  <li><code>button.frame.normal.svg</code> when the family uses a separate frame layer</li>
  <li><code>button.label.anchor.json</code> or another explicit anchor-map artifact</li>
</ul>

<p>
Resources MAY be SVG-backed, host-native, or toolkit-driven.
The default family standardizes the state posture, part posture, and realization-side binding posture, not one mandatory file format.
</p>

<p>
In particular, the label part SHOULD preferably bind to a placement surface such as an anchor or text region rather than to a resource that hardcodes the final user-facing text content.
</p>

<hr/>

<h2 id="host-expectations">8. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a clearly actionable face,</li>
  <li>a visible pressed posture during activation,</li>
  <li>a visible disabled posture when interaction is suppressed,</li>
  <li>a visible focus posture where host focus is supported,</li>
  <li>dynamic rendering or injection of <code>label.text</code> into the realized label surface,</li>
  <li>state-consistent readability of the label across supported visual states.</li>
</ul>

<p>
A host MAY approximate the realization when exact resources are unavailable, but it should preserve:
</p>

<ul>
  <li>the action-oriented button identity,</li>
  <li>the stable meaning of the public parts,</li>
  <li>the separation between semantic text and decorative assets.</li>
</ul>

<hr/>

<h2 id="fallback-posture">9. Fallback Posture</h2>

<p>
If a specialized resource is unavailable:
</p>

<ul>
  <li><code>pressed</code> MAY fall back to a host-native pressed embodiment,</li>
  <li><code>focused</code> MAY fall back to a host-native focus ring or equivalent indicator,</li>
  <li><code>disabled</code> MUST remain visually distinguishable from <code>normal</code>,</li>
  <li><code>label</code> MUST remain dynamically renderable even when a dedicated anchor asset is unavailable.</li>
</ul>

<p>
If no explicit label anchor is available, the host MAY fall back to a reasonable centered text region or another stable host-native placement rule, provided that:
</p>

<ul>
  <li>the text remains readable,</li>
  <li>the face remains clearly actionable,</li>
  <li>the fallback does not turn asset-baked text into semantic truth.</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The default button realization defines one official state-structured embodiment of <code>frog.widgets.button</code> with stable parts and stable visual states.
</p>

<p>
It realizes:
</p>

<ul>
  <li><code>face</code> as the main actionable visual body,</li>
  <li><code>label</code> as a dynamically rendered text-bearing surface,</li>
  <li><code>frame</code> as an optional supporting outer surface.</li>
</ul>

<p>
Its resources may provide geometry, skins, and anchors.
Its package publication may provide state maps and part bindings.
Its host implementation may approximate the visuals when needed.
But the realization never becomes the semantic owner of the button label text.
</p>
