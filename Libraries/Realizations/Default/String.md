<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — String Widgets</h1>

<p align="center">
  <strong>Normative default realization posture for standardized string widgets</strong><br/>
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
This document defines the default official realization posture for the standardized string widget family.
</p>

<p>
The default string realization provides one clean, inspectable, portable embodiment of the intrinsic string baseline without turning one host toolkit, one text-editor style, one skin bundle, or one runtime-specific implementation into the semantic definition of string widgets.
</p>

<p>
This realization is realization-side only.
It does not redefine string class law, does not invent new public members, and does not replace the semantic ownership of string value, string label text, or string editing semantics.
Its role is to embody already-published string widget surfaces through stable visual states, stable structural bindings, explicit realization-side placement or rendering metadata, and bounded realization-side styling or skinning posture where supported.
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
  <li><code>frog.widgets.string_control</code></li>
  <li><code>frog.widgets.string_indicator</code></li>
</ul>

<p>
This realization assumes the standardized string posture in which:
</p>

<ul>
  <li>string widgets expose a primary value through <code>value</code>,</li>
  <li>string widgets may expose semantic label text through <code>label.text</code>,</li>
  <li>string controls may expose editing-oriented behavior while string indicators remain display-oriented,</li>
  <li>portable style-facing and realization-selection surfaces may be exposed by class law or the active profile,</li>
  <li>the published public parts remain stable across realizations,</li>
  <li>the realization remains downstream from that class contract.</li>
</ul>

<p>
The realization therefore owns embodiment and placement posture for string widgets.
It does not become the semantic owner of the string value or of the label content.
</p>

<hr/>

<h2 id="realization-variant-posture">3. Realization Variant Posture</h2>

<p>
The default string family standardizes one string realization corridor, not one mandatory visible shape.
</p>

<p>
Accordingly, a conforming realization MAY choose a string embodiment posture such as:
</p>

<ul>
  <li>single-line text-field-like editor,</li>
  <li>multi-line text-area-like editor,</li>
  <li>compact read-only string display,</li>
  <li>scrollable text-view-like surface,</li>
  <li>another host-compatible string embodiment.</li>
</ul>

<p>
Those remain realization variants of the same published string classes.
A multi-line or scrollable visible embodiment does not by itself define a new intrinsic widget class.
</p>

<p>
This distinction is normative:
</p>

<ul>
  <li>the class layer owns string value semantics, public members, methods, events, and parts,</li>
  <li>the realization layer owns how those published surfaces are visually embodied,</li>
  <li>a realization-variant identifier is not a class identifier,</li>
  <li>a runtime MUST NOT treat a text-area-like, multi-line, or scrollable embodiment as if it were a distinct standard class unless a separate class contract is explicitly published elsewhere.</li>
</ul>

<p>
For that reason, differences such as single-line posture, multi-line chrome, scroll affordance, wrapping style, or compact display posture belong here as realization strategy, not as implicit class-level semantic drift.
</p>

<hr/>

<h2 id="styling-and-skin-posture">4. Styling and Skin Posture</h2>

<p>
The default string realization is customizable, but customization remains subordinate to class meaning and realization-family publication rules.
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
  <li><code>style.placeholder_color</code>,</li>
  <li><code>style.selection_color</code>,</li>
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
These surfaces do not create a new string class.
They influence how the existing string class is embodied within the allowed realization corridor.
</p>

<p>
The preferred interpretation posture is:
</p>

<ul>
  <li>public <code>style.*</code> properties influence inspectable realization-side styling parameters,</li>
  <li><code>realization.variant</code> selects among compatible published embodiment variants,</li>
  <li><code>realization.skin_id</code> selects among compatible published skin bundles or resource groups,</li>
  <li>SVG resources, host-native resources, template-driven resources, and style-token resources remain realization assets rather than semantic truth.</li>
</ul>

<p>
A skin MAY therefore change colors, borders, corner style, text-field chrome, multiline container shape, scrollbar appearance, typography defaults, placeholder styling, decorative containers, or focus emphasis.
It MUST NOT silently redefine:
</p>

<ul>
  <li>the meaning of <code>value</code>,</li>
  <li>the meaning of <code>label.text</code>,</li>
  <li>the editable-versus-indicator distinction,</li>
  <li>the public string part model,</li>
  <li>the public string method or event inventory.</li>
</ul>

<p>
A style or skin selection therefore remains realization-facing customization input.
It is not a substitute for class law and it is not a hidden semantic extension mechanism.
</p>

<hr/>

<h2 id="realized-parts">5. Realized Parts</h2>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>text_display</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The realization may internally use additional layers, clipping regions, caret surfaces, selection overlays, scroll regions, placeholder layers, viewport containers, style-token layers, or host-native text editor structures.
Those remain realization-private support structures unless they are explicitly published as realization resources or placement surfaces.
</p>

<p>
The default posture is:
</p>

<ul>
  <li><code>root</code> — overall layout, clipping, and outer realization region when needed,</li>
  <li><code>label</code> — dynamic text-bearing public part rendered through a realization-side placement surface,</li>
  <li><code>text_display</code> — dynamic text display or editing surface,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
A multi-line or scrollable realization MAY internally decompose the visible embodiment into editor field, inner viewport, scrollbar affordances, placeholder layer, and other toolkit-native structures.
Those remain realization-private unless explicitly published through a later realization-specific extension layer.
The stable public string part model remains centered on <code>text_display</code>, <code>label</code>, and optional <code>frame</code>.
</p>

<hr/>

<h2 id="standard-visual-states">6. Standard Visual States</h2>

<p>
The default string family defines at least:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code></li>
  <li><code>focused</code></li>
</ul>

<p>
The host MAY also support richer transient posture such as hovered chrome, selection emphasis, placeholder emphasis, or scroll affordances, but such additions are not required in the minimal default realization posture.
</p>

<p>
These are realization-side visual states.
They do not redefine the semantic meaning of string value, string editing legality, or string class identity.
</p>

<p>
A single-line, multi-line, compact, or scrollable embodiment may use different geometry, spacing, clipping, or emphasis for these states, but it still remains bound to the same published string state vocabulary unless an extended realization family explicitly publishes more specialized realization-only states.
</p>

<hr/>

<h2 id="part-state-mapping">7. Part-State Mapping</h2>

<p>
The default family expects:
</p>

<ul>
  <li><code>text_display</code> to remain readable in all supported states,</li>
  <li><code>label</code> to remain readable when shown,</li>
  <li><code>frame</code>, when present, to support a focused posture where applicable.</li>
</ul>

<p>
A typical minimal mapping posture is:
</p>

<ul>
  <li><code>root</code> — global layout, clipping, and outer realization region,</li>
  <li><code>label</code> — dynamic text-bearing label surface,</li>
  <li><code>text_display</code> — dynamic text display or editing surface,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
The preferred machine-readable split is:
</p>

<ul>
  <li><code>text_display</code> published primarily through a <code>part_binding</code> to a text region, anchor, or equivalent dynamic text surface,</li>
  <li><code>label</code> published primarily through a <code>part_binding</code> to an anchor, text region, or equivalent placement surface,</li>
  <li><code>frame</code>, when present, published through <code>part_bindings</code> plus optional <code>state_maps</code>,</li>
  <li>styling and skin differences published through resource inventories, style-token resources, variant identifiers, or compatible resource groups.</li>
</ul>

<p>
The default family SHOULD keep this mapping explicit enough that a machine-readable package can distinguish:
</p>

<ul>
  <li>state-sensitive visual resources,</li>
  <li>structural part bindings,</li>
  <li>dynamic host-rendered or host-updated text surfaces,</li>
  <li>bounded styling or skin-selection posture.</li>
</ul>

<p>
This distinction is important because <code>text_display</code> is not merely decorative.
It is the realized surface through which the current semantic string value becomes visible and, for controls, may become editable.
</p>

<p>
In a multi-line or scrollable realization, any internal sub-embodiment such as inner viewport, placeholder layer, or scroll chrome remains subordinate to the published <code>text_display</code> binding posture.
It does not create new public parts by implication alone.
</p>

<hr/>

<h2 id="dynamic-surface-posture">8. Dynamic Surface Posture</h2>

<h3>8.1 Text display posture</h3>

<p>
The <code>text_display</code> part is not just a static decorative asset surface.
It is a dynamic realization surface that reflects the current string value and, for controls, may also reflect host editing posture such as caret position, selection, scrolling, or text input focus.
</p>

<p>
A host interpreting this realization is expected to render or update the visible text content according to the published class surface through <code>value</code> and the control-or-indicator posture of the target class.
</p>

<p>
The realization owns how the text display is visually embodied.
It does not become the semantic owner of the string value itself.
</p>

<h3>8.2 Label posture</h3>

<p>
The semantic string label text is not owned by this realization.
It is owned by the standardized class surface through <code>label.text</code>.
</p>

<p>
The role of the default realization is to define where and how that semantic label is visually embodied, not to become the source of truth for the label text itself.
</p>

<p>
The <code>label</code> part is therefore expected to be realized as a dynamic text-bearing surface.
A host interpreting this realization should render or inject the current semantic string label into the realized label region at runtime.
</p>

<h3>8.3 Placement posture</h3>

<p>
The default family SHOULD publish explicit placement surfaces for both <code>label</code> and <code>text_display</code> whenever host-rendered text content is used.
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
  <li>multiline posture, wrapping posture, or scroll interaction region when the realization chooses to expose them.</li>
</ul>

<p>
Those realization-side structures do not change the public meaning of <code>value</code> or <code>label.text</code>.
They only specify where the host should visually place, render, or edit the text.
</p>

<h3>8.4 Control versus indicator posture</h3>

<p>
The default realization may embody string controls and string indicators differently internally.
For example, a control may use a host-native text entry field while an indicator may use a simpler retained display surface.
</p>

<p>
Those internal differences are acceptable provided that:
</p>

<ul>
  <li>the published class identity remains preserved,</li>
  <li>the public parts remain interpretable,</li>
  <li>the difference between editable and non-editable posture remains compatible with the standardized class contract.</li>
</ul>

<p>
Caret position, text selection, insertion mode, scrolling, and similar host editing details remain host-side editing posture unless explicitly standardized elsewhere.
They do not become new public widget semantics merely because a given runtime exposes them visually.
</p>

<h3>8.5 Editor-style posture as realization choice</h3>

<p>
A string editor style such as single-line field, multi-line area, scrollable viewer, or compact readout remains an embodiment choice within the default string family.
Such a realization may use:
</p>

<ul>
  <li>single-line editor chrome,</li>
  <li>multi-line clipping regions,</li>
  <li>scrollable inner viewport,</li>
  <li>placeholder or hint presentation,</li>
  <li>host-native text-field affordance conventions.</li>
</ul>

<p>
However, those embodiment choices remain realization-owned.
They do not, by themselves, introduce:
</p>

<ul>
  <li>a distinct intrinsic widget class,</li>
  <li>new public string semantics,</li>
  <li>new mandatory public properties,</li>
  <li>new mandatory public methods,</li>
  <li>new mandatory public events.</li>
</ul>

<p>
If a future specification standardizes a text-widget class with genuinely different public behavior, that class would need its own explicit class law.
Until then, editor-style differences remain realization variants of <code>frog.widgets.string_control</code> or <code>frog.widgets.string_indicator</code>.
</p>

<h3>8.6 Styling and skin application posture</h3>

<p>
A string realization MAY apply portable style surfaces or skin selection in several ways, including:
</p>

<ul>
  <li>substituting one compatible visual resource group for another,</li>
  <li>injecting style-token values into a vector template or rendering layer,</li>
  <li>mapping public color, typography, placeholder, or selection surfaces to host-native toolkit styling parameters,</li>
  <li>switching among compatible realization variants under the same class contract.</li>
</ul>

<p>
Such realization-side adaptation remains valid only if:
</p>

<ul>
  <li>the published string state vocabulary remains preserved,</li>
  <li>the public part meaning remains preserved,</li>
  <li>the chosen embodiment remains inspectable through realization publication,</li>
  <li>styling or skinning does not silently become a new public semantic contract.</li>
</ul>

<h3>8.7 Asset limitation rule</h3>

<p>
A string resource file MAY include placeholder text, decorative guides, preview content, or design-time scaffolding.
However, a conforming realization family must not require that those asset-baked strings become the only path by which live string value or live semantic label text is shown.
</p>

<p>
Likewise, state-sensitive styling of rendered text must remain distinguishable from semantic ownership of the string value itself.
</p>

<hr/>

<h2 id="resource-posture">9. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>string_control/
  variants/
    single_line/
      text_display/
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
    multiline/
      text_display/
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

string_indicator/
  variants/
    standard/
      text_display/
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
  <li><code>string_control.text_display.normal.svg</code></li>
  <li><code>string_control.text_display.focused.svg</code></li>
  <li><code>string_control.label.anchor_map</code> backed by <code>./assets/string_control/anchors/label.json</code></li>
  <li><code>string_control.value.text_region_map</code> backed by <code>./assets/string_control/text_regions/value.json</code></li>
  <li><code>string_indicator.text_display.normal.svg</code></li>
  <li><code>string_indicator.label.anchor_map</code> backed by <code>./assets/string_indicator/anchors/label.json</code></li>
  <li><code>string_indicator.value.text_region_map</code> backed by <code>./assets/string_indicator/text_regions/value.json</code></li>
</ul>

<p>
Resources MAY be SVG-backed, host-native, toolkit-driven, template-driven, or mixed.
The default family standardizes the part posture, state posture, and realization-side binding posture, not one mandatory text-editor implementation and not one mandatory file format.
</p>

<p>
In particular:
</p>

<ul>
  <li><code>frame</code> is a natural candidate for state-sensitive visual resources,</li>
  <li><code>label</code> is naturally a placement-bound dynamic text surface,</li>
  <li><code>text_display</code> is naturally a placement-bound dynamic string surface, even when decorative visual resources also exist around it,</li>
  <li>variant-specific or skin-specific resource groups MAY coexist as long as the published part meaning and state vocabulary remain preserved.</li>
</ul>

<p>
A single-line, multi-line, scrollable, skinned, or host-native embodiment may still publish its resources under the same string realization corridor, as long as the published part meaning and state vocabulary remain preserved.
</p>

<hr/>

<h2 id="host-expectations">10. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a clearly readable text value surface,</li>
  <li>a visible disabled posture when interaction is suppressed,</li>
  <li>a visible focus posture for controls where supported by the host,</li>
  <li>dynamic rendering of visible string value and label text.</li>
</ul>

<p>
A host SHOULD also preserve the distinction between:
</p>

<ul>
  <li>the semantic string value owned by the class,</li>
  <li>the string label text owned by <code>label.text</code>,</li>
  <li>the realization-side embodiment of label, text display, and frame.</li>
</ul>

<p>
For controls, the host should also preserve the difference between:
</p>

<ul>
  <li>display posture,</li>
  <li>editing posture,</li>
  <li>indicator-style read-only posture.</li>
</ul>

<p>
A host MAY approximate the realization when exact resources are unavailable, but it should preserve:
</p>

<ul>
  <li>the editable-versus-indicator distinction,</li>
  <li>the stable meaning of the published public parts,</li>
  <li>the separation between semantic string data and realization resources.</li>
</ul>

<p>
A host MAY choose a single-line, multi-line, scrollable, compact, skinned, or other compatible string embodiment strategy.
That choice is acceptable only if the public string class meaning remains unchanged and the realization contract remains inspectable.
</p>

<p>
When public styling or skin-selection surfaces are exposed, the host SHOULD apply them through the published realization contract rather than through hidden runtime-specific conventions.
</p>

<hr/>

<h2 id="fallback-posture">11. Fallback Posture</h2>

<p>
If specialized text-display resources are unavailable, a runtime MAY use host-native text entry or text display surfaces provided the published part structure and interaction meaning remain preserved.
</p>

<p>
If dedicated label or text-display placement resources are unavailable, a host MAY fall back to:
</p>

<ul>
  <li>a host-native text region,</li>
  <li>a generic text editor or display region,</li>
  <li>another documented compatible placement rule.</li>
</ul>

<p>
If focused or disabled frame-specific resources are unavailable, a host MAY fall back to host-native focus or disabled posture provided that the distinction remains visible.
</p>

<p>
If one string embodiment variant cannot be realized exactly, a host MAY fall back to another compatible string embodiment such as single-line, multi-line, scrollable, or compact posture, provided that:
</p>

<ul>
  <li>the published string class meaning remains unchanged,</li>
  <li>the readable text display remains clear,</li>
  <li>the editable-versus-indicator distinction remains preserved,</li>
  <li>the fallback does not imply a new class-level contract.</li>
</ul>

<p>
If a requested skin, variant, or style-token resource is unavailable, a host MAY fall back to:
</p>

<ul>
  <li>the default skin of the selected realization corridor,</li>
  <li>another compatible published string variant,</li>
  <li>a host-native compatible string embodiment preserving the published state vocabulary and part meaning.</li>
</ul>

<p>
Any fallback MUST preserve the published string class law and the meaning of the public parts when those parts are exposed.
Fallback must not turn asset-baked strings or asset-baked label text into semantic truth.
</p>

<p>
Fallback must remain inspectable at the realization-publication layer.
It must not become a purely runtime-private convention.
</p>

<hr/>

<h2 id="summary">12. Summary</h2>

<p>
The default string realization defines one official embodiment for string controls and string indicators centered on the public <code>text_display</code> part.
</p>

<p>
It realizes:
</p>

<ul>
  <li><code>text_display</code> as the main dynamic text display or editing surface,</li>
  <li><code>label</code> as a dynamically rendered text-bearing surface,</li>
  <li><code>frame</code> as an optional supporting outer surface,</li>
  <li>bounded styling and skin selection as realization-side customization posture rather than class-level semantic drift.</li>
</ul>

<p>
Its resources may provide skins, layers, regions, anchors, style-token support, and compatible embodiment variants.
Its package publication may provide <code>state_maps</code>, <code>part_bindings</code>, variant identifiers, and inspectable fallback posture.
Its host implementation may approximate the visuals when needed.
But the realization never becomes the semantic owner of string value, string label text, or string class meaning.
</p>

<p>
In this realization family, single-line, multi-line, scrollable, compact, and similar visible embodiments remain realization variants unless a future specification publishes a distinct class with genuinely distinct public semantics.
</p>
