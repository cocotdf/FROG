<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — Numeric Widgets</h1>

<p align="center">
  <strong>Normative default realization posture for standardized numeric widgets</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#target-classes">2. Target Classes</a></li>
  <li><a href="#realization-variant-posture">3. Realization Variant Posture</a></li>
  <li><a href="#styling-and-skin-posture">4. Styling and Skin Posture</a></li>
  <li><a href="#realized-parts">5. Realized Parts</a></li>
  <li><a href="#standard-visual-states">6. Standard Visual States</a></li>
  <li><a href="#part-state-mapping">7. Part-State Mapping</a></li>
  <li><a href="#dynamic-surface-posture">8. Dynamic Surface Posture</a></li>
  <li><a href="#resource-posture">9. Resource Posture</a></li>
  <li><a href="#host-expectations">10. Host Expectations</a></li>
  <li><a href="#fallback-posture">11. Fallback Posture</a></li>
  <li><a href="#summary">12. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the default official realization posture for the standardized numeric widget family.
</p>

<p>
The default numeric realization provides one clean, inspectable, portable embodiment of the intrinsic numeric baseline without turning one host toolkit, one numeric editor style, one skin bundle, or one runtime-specific implementation into the semantic definition of numeric widgets.
</p>

<p>
This realization is realization-side only.
It does not redefine numeric class law, does not invent new public members, and does not replace the semantic ownership of numeric value, numeric label text, or numeric editing semantics.
Its role is to embody already-published numeric widget surfaces through stable visual states, stable structural bindings, explicit realization-side placement or rendering metadata, and bounded realization-side styling or skinning posture where supported.
</p>

<p>
The preferred realization-publication split is:
</p>

<ul>
  <li><code>state_maps</code> for state-sensitive visual embodiment,</li>
  <li><code>part_bindings</code> for stable structural correspondence,</li>
  <li>anchors or text regions for dynamic public surfaces rendered by the host,</li>
  <li>resource and style-token publication for inspectable styling and skin support.</li>
</ul>

<hr/>

<h2 id="target-classes">2. Target Classes</h2>

<ul>
  <li><code>frog.widgets.numeric_control</code></li>
  <li><code>frog.widgets.numeric_indicator</code></li>
</ul>

<p>
This realization assumes the standardized numeric posture in which:
</p>

<ul>
  <li>numeric widgets expose a primary value through <code>value</code>,</li>
  <li>numeric widgets may expose semantic label text through <code>label.text</code>,</li>
  <li>numeric controls may expose <code>increment()</code> and <code>decrement()</code> interaction according to the published class contract,</li>
  <li>portable style-facing and realization-selection surfaces may be exposed by class law or the active profile,</li>
  <li>the published public parts remain stable across realizations,</li>
  <li>the realization remains downstream from that class contract.</li>
</ul>

<p>
The realization therefore owns embodiment and placement posture for numeric widgets.
It does not become the semantic owner of the numeric value or of the label content.
</p>

<hr/>

<h2 id="realization-variant-posture">3. Realization Variant Posture</h2>

<p>
The default numeric family standardizes one numeric realization corridor, not one mandatory visible shape.
</p>

<p>
Accordingly, a conforming realization MAY choose a numeric embodiment posture such as:
</p>

<ul>
  <li>box-like numeric editor,</li>
  <li>spinbox-like numeric editor,</li>
  <li>stepper-like numeric control,</li>
  <li>compact indicator-like numeric display,</li>
  <li>another host-compatible numeric embodiment.</li>
</ul>

<p>
Those remain realization variants of the same published numeric classes.
A spinbox-like visible embodiment does not by itself define a new intrinsic widget class.
</p>

<p>
This distinction is normative:
</p>

<ul>
  <li>the class layer owns numeric value semantics, public members, methods, events, and parts,</li>
  <li>the realization layer owns how those published surfaces are visually embodied,</li>
  <li>a realization-variant identifier is not a class identifier,</li>
  <li>a runtime MUST NOT treat a spinbox-like or compact-display embodiment as if it were a distinct standard class unless a separate class contract is explicitly published elsewhere.</li>
</ul>

<p>
For that reason, differences such as visible step buttons, compact editor chrome, right-aligned value display, or raised readout framing belong here as realization strategy, not as implicit class-level semantic drift.
</p>

<hr/>

<h2 id="styling-and-skin-posture">4. Styling and Skin Posture</h2>

<p>
The default numeric realization is customizable, but customization remains subordinate to class meaning and realization-family publication rules.
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
These surfaces do not create a new numeric class.
They influence how the existing numeric class is embodied within the allowed realization corridor.
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
A skin MAY therefore change colors, borders, corner style, value-field chrome, step-button appearance, typography defaults, decorative containers, or focus emphasis.
It MUST NOT silently redefine:
</p>

<ul>
  <li>the meaning of <code>value</code>,</li>
  <li>the meaning of <code>label.text</code>,</li>
  <li>the editable-versus-indicator distinction,</li>
  <li>the public numeric part model,</li>
  <li>the public numeric method or event inventory.</li>
</ul>

<hr/>

<h2 id="realized-parts">5. Realized Parts</h2>

<p>
The default numeric realization targets the following parts:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>value_display</code></li>
  <li><code>increment_button</code> when the control realization exposes it</li>
  <li><code>decrement_button</code> when the control realization exposes it</li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The realization may internally use additional layers, clipping regions, caret surfaces, selection surfaces, editing guides, cursor helpers, separators, style-token layers, or host-native editor structures.
Those remain realization-private support structures unless they are explicitly published as realization resources or placement surfaces.
</p>

<p>
The default posture is:
</p>

<ul>
  <li><code>root</code> — overall layout, clipping, and outer realization region when needed,</li>
  <li><code>label</code> — dynamic text-bearing public part rendered through a realization-side placement surface,</li>
  <li><code>value_display</code> — dynamic numeric display or editing surface,</li>
  <li><code>increment_button</code> — optional state-sensitive step-up interaction surface,</li>
  <li><code>decrement_button</code> — optional state-sensitive step-down interaction surface,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
A spinbox-like realization MAY internally decompose the visible embodiment into editor field, arrows, separators, and other toolkit-native structures.
Those remain realization-private unless explicitly published through a later realization-specific extension layer.
The stable public numeric part model remains centered on <code>value_display</code>, <code>label</code>, optional step buttons, and optional <code>frame</code>.
</p>

<hr/>

<h2 id="standard-visual-states">6. Standard Visual States</h2>

<p>
The default numeric family defines at least:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code></li>
  <li><code>focused</code></li>
</ul>

<p>
For increment and decrement button parts, the default family additionally defines:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>pressed</code></li>
</ul>

<p>
The host MAY also support richer transient posture such as hovered editor chrome, caret emphasis, or selection emphasis, but such additions are not required in the minimal default realization posture.
</p>

<p>
These are realization-side visual states.
They do not redefine the semantic meaning of numeric value, numeric editing legality, or numeric class identity.
</p>

<p>
A spinbox-like or compact-display embodiment may use different geometry, spacing, or emphasis for these states, but it still remains bound to the same published numeric state vocabulary unless an extended realization family explicitly publishes more specialized realization-only states.
</p>

<hr/>

<h2 id="part-state-mapping">7. Part-State Mapping</h2>

<p>
The default family expects:
</p>

<ul>
  <li><code>value_display</code> to remain readable across supported states,</li>
  <li><code>label</code> to remain readable when shown,</li>
  <li><code>increment_button</code> to support state distinction between <code>normal</code> and <code>pressed</code> when realized,</li>
  <li><code>decrement_button</code> to support state distinction between <code>normal</code> and <code>pressed</code> when realized,</li>
  <li><code>frame</code>, when present, to support focused posture where applicable.</li>
</ul>

<p>
A typical minimal mapping posture is:
</p>

<ul>
  <li><code>root</code> — global layout, clipping, and outer realization region,</li>
  <li><code>label</code> — dynamic text-bearing label surface,</li>
  <li><code>value_display</code> — dynamic numeric display or editing surface,</li>
  <li><code>increment_button</code> — optional state-sensitive step-up interaction surface,</li>
  <li><code>decrement_button</code> — optional state-sensitive step-down interaction surface,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
The preferred machine-readable split is:
</p>

<ul>
  <li><code>value_display</code> published primarily through a <code>part_binding</code> to a text region, anchor, or equivalent dynamic display surface,</li>
  <li><code>label</code> published primarily through a <code>part_binding</code> to an anchor, text region, or equivalent placement surface,</li>
  <li><code>increment_button</code> and <code>decrement_button</code>, when exposed, published through <code>part_bindings</code> plus <code>state_maps</code>,</li>
  <li><code>frame</code>, when present, published through <code>part_bindings</code> plus optional <code>state_maps</code>,</li>
  <li>styling and skin differences published through resource inventories, style-token resources, variant identifiers, or compatible resource groups.</li>
</ul>

<p>
The default family SHOULD keep this mapping explicit enough that a machine-readable package can distinguish:
</p>

<ul>
  <li>state-sensitive visual resources,</li>
  <li>structural part bindings,</li>
  <li>dynamic host-rendered or host-updated numeric surfaces.</li>
</ul>

<p>
This distinction is important because <code>value_display</code> is not merely decorative.
It is the realized surface through which the current semantic numeric value becomes visible and, for controls, may become editable.
</p>

<p>
In a spinbox-like realization, any internal sub-embodiment such as editor field chrome, arrow cluster, or separator remains subordinate to the published <code>value_display</code>, <code>increment_button</code>, and <code>decrement_button</code> binding posture.
It does not create new public parts by implication alone.
</p>

<hr/>

<h2 id="dynamic-surface-posture">8. Dynamic Surface Posture</h2>

<h3>8.1 Value display posture</h3>

<p>
The <code>value_display</code> part is not just a static decorative asset surface.
It is a dynamic realization surface that reflects the current numeric value and, for controls, may also reflect host editing posture.
</p>

<p>
A host interpreting this realization is expected to render or update the visible numeric content according to the published class surface through <code>value</code>, formatting hints such as <code>format.pattern</code> when supported, and the control-or-indicator posture of the target class.
</p>

<p>
The realization owns how the value display is visually embodied.
It does not become the semantic owner of the numeric value itself.
</p>

<h3>8.2 Label posture</h3>

<p>
The semantic numeric label text is not owned by this realization.
It is owned by the standardized class surface through <code>label.text</code>.
</p>

<p>
The role of the default realization is to define where and how that semantic label is visually embodied, not to become the source of truth for the label text itself.
</p>

<p>
The <code>label</code> part is therefore expected to be realized as a dynamic text-bearing surface.
A host interpreting this realization should render or inject the current semantic numeric label into the realized label region at runtime.
</p>

<h3>8.3 Placement posture</h3>

<p>
The default family SHOULD publish explicit placement surfaces for both <code>label</code> and <code>value_display</code> whenever host-rendered numeric content is used.
Those placement surfaces may take the form of:
</p>

<ul>
  <li>a named <code>text_anchor</code>,</li>
  <li>a published anchor entry backed by an <code>anchor_map</code> resource,</li>
  <li>a published <code>text_region</code> entry backed by a <code>text_region_map</code> resource,</li>
  <li>a host-native region under explicit binding posture,</li>
  <li>an equivalent explicitly published placement binding.</li>
</ul>

<p>
This placement metadata may define:
</p>

<ul>
  <li>alignment box or region bounds,</li>
  <li>horizontal and vertical alignment,</li>
  <li>padding or inset region,</li>
  <li>clipping posture,</li>
  <li>numeric-text alignment or right-justification posture when the realization chooses to expose it.</li>
</ul>

<p>
Those realization-side structures do not change the public meaning of <code>value</code> or <code>label.text</code>.
They only specify where the host should visually place or edit the rendered content.
</p>

<h3>8.4 Step-button posture</h3>

<p>
The <code>increment_button</code> and <code>decrement_button</code> parts are standard only when the active realization exposes step-style interaction.
When exposed, they are realization-side interaction surfaces corresponding to already-published control-side behavior such as <code>increment()</code> and <code>decrement()</code>.
</p>

<p>
These parts may be embodied through:
</p>

<ul>
  <li>SVG-backed button layers,</li>
  <li>host-native spin controls,</li>
  <li>toolkit-native stepper surfaces,</li>
  <li>another compatible host interaction mechanism.</li>
</ul>

<p>
The realization may choose whether those parts are visibly separate.
However, when they are published as exposed parts, their meaning must remain inspectable and compatible with the standardized control contract.
</p>

<h3>8.5 Editor-style posture as realization choice</h3>

<p>
A numeric editor style such as box-like editor, spinbox-like editor, or compact readout remains an embodiment choice within the default numeric family.
Such a realization may use:
</p>

<ul>
  <li>separate editor chrome,</li>
  <li>embedded arrows,</li>
  <li>right-aligned or centered numeric text,</li>
  <li>compact readout framing,</li>
  <li>host-native numeric field affordance conventions.</li>
</ul>

<p>
However, those embodiment choices remain realization-owned.
They do not, by themselves, introduce:
</p>

<ul>
  <li>a distinct intrinsic widget class,</li>
  <li>new public numeric semantics,</li>
  <li>new mandatory public properties,</li>
  <li>new mandatory public methods,</li>
  <li>new mandatory public events.</li>
</ul>

<p>
If a future specification standardizes a numerically distinct class with genuinely different public behavior, that class would need its own explicit class law.
Until then, editor-style differences remain realization variants of <code>frog.widgets.numeric_control</code> or <code>frog.widgets.numeric_indicator</code>.
</p>

<h3>8.6 Asset limitation rule</h3>

<p>
A numeric resource file MAY include placeholder digits, decorative guides, preview values, or design-time scaffolding.
However, a conforming realization family must not require that those asset-baked values become the only path by which live numeric value or live semantic label text is shown.
</p>

<p>
Likewise, state-sensitive styling of rendered numeric text must remain distinguishable from semantic ownership of the numeric value itself.
</p>

<hr/>

<h2 id="resource-posture">9. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>numeric_control/
  variants/
    spinbox/
      value_display/
        normal
        disabled
        focused
      increment_button/
        normal
        pressed
      decrement_button/
        normal
        pressed
      frame/
        normal
        focused
      anchors/
        label
      text_regions/
        value
    compact/
      value_display/
        normal
        disabled
        focused
      frame/
        normal
        focused
      anchors/
        label
      text_regions/
        value

numeric_indicator/
  variants/
    standard/
      value_display/
        normal
        focused
      frame/
        normal
        focused
      anchors/
        label
      text_regions/
        value
</code></pre>

<p>
An equivalent package-oriented posture may publish resources such as:
</p>

<ul>
  <li><code>numeric_control.value_display.normal.svg</code></li>
  <li><code>numeric_control.value_display.focused.svg</code></li>
  <li><code>numeric_control.increment_button.pressed.svg</code></li>
  <li><code>numeric_control.decrement_button.pressed.svg</code></li>
  <li><code>numeric_control.label.anchor_map</code> backed by <code>./assets/numeric_control/anchors/label.json</code></li>
  <li><code>numeric_control.value.text_region_map</code> backed by <code>./assets/numeric_control/text_regions/value.json</code></li>
  <li><code>numeric_indicator.value_display.normal.svg</code></li>
  <li><code>numeric_indicator.label.anchor_map</code> backed by <code>./assets/numeric_indicator/anchors/label.json</code></li>
  <li><code>numeric_indicator.value.text_region_map</code> backed by <code>./assets/numeric_indicator/text_regions/value.json</code></li>
</ul>

<p>
Resources MAY be SVG-backed, host-native, toolkit-driven, or mixed.
The default family standardizes the part posture, state posture, and realization-side binding posture, not one mandatory editor implementation and not one mandatory file format.
</p>

<p>
In particular:
</p>

<ul>
  <li><code>increment_button</code>, <code>decrement_button</code>, and <code>frame</code> are natural candidates for state-sensitive visual resources,</li>
  <li><code>label</code> is naturally a placement-bound dynamic text surface,</li>
  <li><code>value_display</code> is naturally a placement-bound dynamic numeric surface, even when decorative visual resources also exist around it.</li>
</ul>

<p>
A spinbox-like, compact, skinned, or host-native embodiment may still publish its resources under the same numeric realization corridor, as long as the published part meaning and state vocabulary remain preserved.
</p>

<hr/>

<h2 id="host-expectations">10. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a clearly readable numeric display,</li>
  <li>a visible disabled posture when interaction is suppressed,</li>
  <li>a visible focus posture where host focus is supported,</li>
  <li>visible step-button feedback when increment and decrement parts are realized,</li>
  <li>dynamic rendering of visible numeric value and label text.</li>
</ul>

<p>
A host SHOULD also preserve the distinction between:
</p>

<ul>
  <li>the semantic numeric value owned by the class,</li>
  <li>the numeric label text owned by <code>label.text</code>,</li>
  <li>the realization-side embodiment of label, value display, step buttons, and frame.</li>
</ul>

<p>
For controls, the host should also preserve the difference between:
</p>

<ul>
  <li>display posture,</li>
  <li>editing posture,</li>
  <li>step-style interaction posture when exposed.</li>
</ul>

<p>
A host MAY approximate the realization when exact resources are unavailable, but it should preserve:
</p>

<ul>
  <li>the editable-versus-indicator distinction,</li>
  <li>the stable meaning of the published public parts,</li>
  <li>the separation between semantic numeric data and realization resources.</li>
</ul>

<p>
A host MAY choose a box-like, spinbox-like, compact, skinned, or other compatible numeric embodiment strategy.
That choice is acceptable only if the public numeric class meaning remains unchanged and the realization contract remains inspectable.
</p>

<hr/>

<h2 id="fallback-posture">11. Fallback Posture</h2>

<p>
If step-button-specific resources are unavailable, a runtime MAY:
</p>

<ul>
  <li>use host-native increment and decrement controls,</li>
  <li>omit visible step buttons while preserving numeric editing capability when the host still provides compatible editing posture,</li>
  <li>reuse generic button-state posture for increment and decrement parts.</li>
</ul>

<p>
If dedicated label or value-display placement resources are unavailable, a host MAY fall back to:
</p>

<ul>
  <li>a host-native text region,</li>
  <li>a generic numeric editor or display region,</li>
  <li>another documented compatible placement rule.</li>
</ul>

<p>
If focused or disabled frame-specific resources are unavailable, a host MAY fall back to host-native focus or disabled posture provided that the distinction remains visible.
</p>

<p>
If one numeric embodiment variant cannot be realized exactly, a host MAY fall back to another compatible numeric embodiment such as box-like, spinbox-like, or compact posture, provided that:
</p>

<ul>
  <li>the published numeric class meaning remains unchanged,</li>
  <li>the readable numeric display remains clear,</li>
  <li>the editable-versus-indicator distinction remains preserved,</li>
  <li>the fallback does not imply a new class-level contract.</li>
</ul>

<p>
If a requested skin, variant, or style-token resource is unavailable, a host MAY fall back to:
</p>

<ul>
  <li>the default skin of the selected realization corridor,</li>
  <li>another compatible published numeric variant,</li>
  <li>a host-native compatible numeric embodiment preserving the published state vocabulary and part meaning.</li>
</ul>

<p>
Any fallback MUST preserve the published numeric class law and the meaning of the public parts when those parts are exposed.
Fallback must not turn asset-baked digits or asset-baked label text into semantic truth.
</p>

<p>
Fallback must remain inspectable at the realization-publication layer.
It must not become a purely runtime-private convention.
</p>

<hr/>

<h2 id="summary">12. Summary</h2>

<p>
The default numeric realization defines one official embodiment of the numeric widget family, including optional stateful increment and decrement part realization.
</p>

<p>
It realizes:
</p>

<ul>
  <li><code>value_display</code> as the main dynamic numeric display or editing surface,</li>
  <li><code>label</code> as a dynamically rendered text-bearing surface,</li>
  <li><code>increment_button</code> and <code>decrement_button</code> as optional step-style interaction surfaces,</li>
  <li><code>frame</code> as an optional supporting outer surface,</li>
  <li>bounded styling and skin selection as realization-side customization posture rather than class-level semantic drift.</li>
</ul>

<p>
Its resources may provide skins, layers, regions, anchors, style-token support, and compatible embodiment variants.
Its package publication may provide <code>state_maps</code>, <code>part_bindings</code>, variant identifiers, and inspectable fallback posture.
Its host implementation may approximate the visuals when needed.
But the realization never becomes the semantic owner of numeric value, numeric label text, or numeric class meaning.
</p>

<p>
In this realization family, box-like, spinbox-like, compact, and similar visible embodiments remain realization variants unless a future specification publishes a distinct class with genuinely distinct public semantics.
</p>
