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
  <li><a href="#realization-variant-posture">3. Realization Variant Posture</a></li>
  <li><a href="#styling-and-skin-posture">4. Styling and Skin Posture</a></li>
  <li><a href="#realized-parts">5. Realized Parts</a></li>
  <li><a href="#standard-visual-states">6. Standard Visual States</a></li>
  <li><a href="#part-state-mapping">7. Part-State Mapping</a></li>
  <li><a href="#text-realization-posture">8. Text Realization Posture</a></li>
  <li><a href="#resource-posture">9. Resource Posture</a></li>
  <li><a href="#host-expectations">10. Host Expectations</a></li>
  <li><a href="#fallback-posture">11. Fallback Posture</a></li>
  <li><a href="#summary">12. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the default official realization posture for <code>frog.widgets.button</code>.
</p>

<p>
Its role is to provide a clean, state-structured embodiment of the standard button without making the visual assets, skin resources, or host-native control chrome the owner of button semantics.
</p>

<p>
The default realization is realization-side only.
It does not redefine widget class law, does not invent new public members, and does not replace the semantic ownership of the button label text.
Its role is to embody already-published widget surfaces through stable visual states, stable structural bindings, explicit realization-side placement metadata, and bounded realization-side styling or skinning posture.
</p>

<p>
The preferred architectural split is:
</p>

<ul>
  <li><code>state_maps</code> for state-sensitive visual embodiment,</li>
  <li><code>part_bindings</code> for stable structural correspondence,</li>
  <li>placement resources for dynamic public parts rendered by the host,</li>
  <li>resource and style-token publication for inspectable styling and skin support.</li>
</ul>

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
  <li>portable style-facing and realization-selection surfaces may be exposed by class law or the active profile,</li>
  <li>the realization remains downstream from that class contract.</li>
</ul>

<p>
This realization therefore publishes embodiment and placement posture for the button.
It does not become the semantic owner of the label content.
</p>

<hr/>

<h2 id="realization-variant-posture">3. Realization Variant Posture</h2>

<p>
The default button realization standardizes one button realization corridor, not one mandatory visible shape.
</p>

<p>
Accordingly, a conforming realization MAY choose a button embodiment posture such as:
</p>

<ul>
  <li>flat command button,</li>
  <li>raised command button,</li>
  <li>rounded command button,</li>
  <li>host-native button chrome,</li>
  <li>another host-compatible command-button embodiment.</li>
</ul>

<p>
Those remain realization variants of the same published button class.
A rounded or host-native visible embodiment does not by itself define a new intrinsic widget class.
</p>

<p>
This distinction is normative:
</p>

<ul>
  <li>the class layer owns command semantics, public members, methods, events, and parts,</li>
  <li>the realization layer owns how those published surfaces are visually embodied,</li>
  <li>a realization-variant identifier is not a class identifier,</li>
  <li>a runtime MUST NOT treat one button embodiment variant as if it were a distinct standard class unless a separate class contract is explicitly published elsewhere.</li>
</ul>

<p>
For that reason, differences such as flatness, corner geometry, bevel posture, host-native chrome, or decorative emphasis belong here as realization strategy, not as implicit class-level semantic drift.
</p>

<hr/>

<h2 id="styling-and-skin-posture">4. Styling and Skin Posture</h2>

<p>
The default button realization is customizable, but customization remains subordinate to class meaning and realization-family publication rules.
</p>

<p>
When the relevant class or active profile exposes public styling or realization-selection surfaces, the default realization SHOULD interpret them through inspectable realization-side mechanisms rather than through runtime-private conventions.
</p>

<p>
Typical public surfaces that may influence realization include:
</p>

<ul>
  <li><code>style.foreground_color</code>,</li>
  <li><code>style.background_color</code>,</li>
  <li><code>style.border_color</code>,</li>
  <li><code>style.text_color</code>,</li>
  <li><code>style.opacity</code>,</li>
  <li><code>style.font_family</code>,</li>
  <li><code>style.font_size</code>,</li>
  <li><code>style.font_weight</code>,</li>
  <li><code>style.text_alignment</code>,</li>
  <li><code>realization.family</code>,</li>
  <li><code>realization.variant</code>,</li>
  <li><code>realization.skin_id</code>.</li>
</ul>

<p>
These surfaces do not create a new button class.
They influence how the existing button class is embodied within the allowed realization corridor.
</p>

<p>
The preferred interpretation posture is:
</p>

<ul>
  <li>public <code>style.*</code> properties influence inspectable realization-side styling parameters,</li>
  <li><code>realization.variant</code> selects among compatible published embodiment variants,</li>
  <li><code>realization.skin_id</code> selects among compatible published skin bundles or resource groups,</li>
  <li>SVG resources, host-native resources, and style-token resources remain realization assets rather than semantic truth.</li>
</ul>

<p>
A skin MAY therefore change colors, borders, corner style, highlight posture, typography defaults, decorative containers, shadow posture, or other visual embodiment details.
It MUST NOT silently redefine:
</p>

<ul>
  <li>the meaning of <code>label.text</code>,</li>
  <li>the command-oriented meaning of the button,</li>
  <li>the public button part model,</li>
  <li>the public button method or event inventory.</li>
</ul>

<hr/>

<h2 id="realized-parts">5. Realized Parts</h2>

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
The realization may internally use additional layers, anchors, clipping regions, decorative containers, style-token layers, or host-native regions, but those remain realization-private support structures unless they are explicitly published as realization resources or placement surfaces.
</p>

<p>
The default posture is:
</p>

<ul>
  <li><code>root</code> — overall host layout region when needed,</li>
  <li><code>face</code> — main actionable visual body of the button,</li>
  <li><code>label</code> — dynamic text-bearing public part rendered through a realization-side placement surface,</li>
  <li><code>frame</code> — optional contour or emphasis layer when the realization family publishes it separately.</li>
</ul>

<hr/>

<h2 id="standard-visual-states">6. Standard Visual States</h2>

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

<p>
A flat, raised, rounded, or host-native embodiment may use different geometry, chrome, or emphasis for these states, but it still remains bound to the same published button state vocabulary unless an extended realization family explicitly publishes more specialized realization-only states.
</p>

<hr/>

<h2 id="part-state-mapping">7. Part-State Mapping</h2>

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
The preferred machine-readable split is:
</p>

<ul>
  <li><code>face</code> published through <code>part_bindings</code> plus <code>state_maps</code>,</li>
  <li><code>frame</code>, when present, published through <code>part_bindings</code> plus optional <code>state_maps</code>,</li>
  <li><code>label</code> published primarily through a <code>part_binding</code> to an anchor, text region, or equivalent placement surface,</li>
  <li>styling and skin differences published through resource inventories, style-token resources, variant identifiers, or compatible resource groups.</li>
</ul>

<p>
This means that the default family SHOULD keep the mapping explicit enough that a machine-readable package can bind:
</p>

<ul>
  <li>a part to a resource layer,</li>
  <li>a part to a state-scoped resource,</li>
  <li>a part to a visual anchor, text region, or host-native region,</li>
  <li>a compatible styling or skin selection to an inspectable realization resource group.</li>
</ul>

<p>
The label may still vary stylistically across states, but that does not change its primary publication posture as a dynamic public text-bearing part.
</p>

<hr/>

<h2 id="text-realization-posture">8. Text Realization Posture</h2>

<h3>8.1 Semantic ownership versus realization ownership</h3>

<p>
The semantic button label text is not owned by this realization.
It is owned by the standardized class surface through <code>label.text</code>.
</p>

<p>
The role of the default realization is to define where and how that semantic text is visually embodied, not to become the source of truth for the text itself.
</p>

<h3>8.2 Label embodiment</h3>

<p>
The <code>label</code> part is realized as a dynamic text-bearing surface.
A host interpreting this realization is expected to render or inject the current semantic label text into the realized label surface at runtime.
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

<h3>8.3 Text anchors and placement metadata</h3>

<p>
The default family SHOULD publish an explicit placement surface for <code>label</code>.
That placement surface may take the form of:
</p>

<ul>
  <li>a named <code>text_anchor</code>,</li>
  <li>a published anchor entry backed by an <code>anchor_map</code> resource,</li>
  <li>a published <code>text_region</code> entry backed by a <code>text_region_map</code> resource,</li>
  <li>a host-native text region under explicit binding posture,</li>
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

<h3>8.4 SVG posture</h3>

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

<h3>8.5 State interaction with text</h3>

<p>
The default realization MAY vary text appearance across states such as <code>normal</code> and <code>disabled</code>, for example through color, opacity, contrast, emphasis, or host-native styling changes.
</p>

<p>
However, the default realization does not define intrinsic state-dependent semantic text switching.
It does not introduce <code>label.text_on</code> or <code>label.text_off</code>, and it does not infer alternate text semantics from face-state assets alone.
</p>

<p>
More generally, state-sensitive styling of the rendered label must remain distinguishable from semantic text ownership.
</p>

<hr/>

<h2 id="resource-posture">9. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>button/
  variants/
    flat/
      face/
        normal
        disabled
        focused
        pressed
      frame/
        normal
        focused
      anchors/
        label
    raised/
      face/
        normal
        disabled
        focused
        pressed
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
  <li><code>button.face.normal.svg</code></li>
  <li><code>button.face.disabled.svg</code></li>
  <li><code>button.face.focused.svg</code></li>
  <li><code>button.face.pressed.svg</code></li>
  <li><code>button.frame.normal.svg</code> when the family uses a separate frame layer</li>
  <li><code>button.frame.focused.svg</code> when a focused frame variant exists</li>
  <li><code>button.label.anchor_map</code> backed by <code>./assets/button/anchors/label.json</code></li>
</ul>

<p>
Resources MAY be SVG-backed, host-native, template-driven, or toolkit-driven.
The default family standardizes the state posture, part posture, and realization-side binding posture, not one mandatory file format.
</p>

<p>
In particular, the <code>label</code> part SHOULD preferably bind to a placement surface such as an anchor or text region rather than to a resource that hardcodes the final user-facing text content.
</p>

<p>
Variant-specific and skin-specific resource groups MAY coexist within the same button realization corridor, provided that the published button part meaning and state vocabulary remain preserved.
</p>

<hr/>

<h2 id="host-expectations">10. Host Expectations</h2>

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

<p>
The host may use:
</p>

<ul>
  <li>published <code>state_maps</code> to choose visual embodiment resources,</li>
  <li>published <code>part_bindings</code> to locate realized parts structurally,</li>
  <li>published anchors or text regions to render live text into the correct surface,</li>
  <li>published variant, skin, or style-token posture to select a compatible visual embodiment without semantic drift.</li>
</ul>

<hr/>

<h2 id="fallback-posture">11. Fallback Posture</h2>

<p>
If a specialized resource is unavailable:
</p>

<ul>
  <li><code>pressed</code> MAY fall back to a host-native pressed embodiment or to <code>normal</code>,</li>
  <li><code>focused</code> MAY fall back to a host-native focus ring or equivalent indicator,</li>
  <li><code>disabled</code> MUST remain visually distinguishable from <code>normal</code>,</li>
  <li><code>label</code> MUST remain dynamically renderable even when a dedicated anchor or text-region resource is unavailable.</li>
</ul>

<p>
If no explicit label placement surface is available, the host MAY fall back to a reasonable centered text region or another stable host-native placement rule, provided that:
</p>

<ul>
  <li>the text remains readable,</li>
  <li>the face remains clearly actionable,</li>
  <li>the fallback does not turn asset-baked text into semantic truth.</li>
</ul>

<p>
If a requested skin, variant, or style-token resource is unavailable, a host MAY fall back to:
</p>

<ul>
  <li>the default skin of the selected realization corridor,</li>
  <li>another compatible published button variant,</li>
  <li>a host-native compatible command-button embodiment preserving the published state vocabulary and part meaning.</li>
</ul>

<p>
Fallback must remain inspectable at the realization-publication layer.
It must not become a purely runtime-private convention.
</p>

<hr/>

<h2 id="summary">12. Summary</h2>

<p>
The default button realization defines one official state-structured embodiment of <code>frog.widgets.button</code> with stable parts and stable visual states.
</p>

<p>
It realizes:
</p>

<ul>
  <li><code>face</code> as the main actionable visual body,</li>
  <li><code>label</code> as a dynamically rendered text-bearing surface,</li>
  <li><code>frame</code> as an optional supporting outer surface,</li>
  <li>bounded styling and skin selection as realization-side customization posture rather than class-level semantic drift.</li>
</ul>

<p>
Its resources may provide geometry, skins, placement metadata, style-token support, and compatible embodiment variants.
Its package publication may provide <code>state_maps</code>, <code>part_bindings</code>, variant identifiers, and inspectable fallback posture.
Its host implementation may approximate the visuals when needed.
But the realization never becomes the semantic owner of the button label text.
</p>
