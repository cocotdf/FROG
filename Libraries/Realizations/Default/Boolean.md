<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — Boolean Widgets</h1>

<p align="center">
  <strong>Normative default realization posture for standardized boolean widgets</strong><br/>
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
This document defines the default official realization posture for the standardized boolean widget family.
</p>

<p>
The default boolean realization provides one clean, inspectable, portable embodiment of the intrinsic boolean baseline without turning one host toolkit, one control library, or one runtime-specific implementation into the semantic definition of boolean widgets.
</p>

<p>
This realization is realization-side only.
It does not redefine boolean class law, does not invent new public members, and does not replace the semantic ownership of boolean value, boolean label text, or boolean interaction semantics.
Its role is to embody already-published boolean widget surfaces through stable visual states, stable structural bindings, and realization-side placement or rendering metadata where needed.
</p>

<p>
The preferred realization-publication split is:
</p>

<ul>
  <li><code>state_maps</code> for state-sensitive visual embodiment,</li>
  <li><code>part_bindings</code> for stable structural correspondence,</li>
  <li>anchors or text regions for dynamic public surfaces rendered by the host.</li>
</ul>

<hr/>

<h2 id="target-classes">2. Target Classes</h2>

<ul>
  <li><code>frog.widgets.boolean_control</code></li>
  <li><code>frog.widgets.boolean_indicator</code></li>
</ul>

<p>
This realization assumes the standardized boolean posture in which:
</p>

<ul>
  <li>boolean widgets expose a primary value through <code>value</code>,</li>
  <li>boolean widgets may expose semantic label text through <code>label.text</code>,</li>
  <li>boolean controls may expose interaction such as <code>toggle()</code>, <code>set_true()</code>, or <code>set_false()</code> according to the published class contract,</li>
  <li>the published public parts remain stable across realizations,</li>
  <li>the realization remains downstream from that class contract.</li>
</ul>

<p>
The realization therefore owns embodiment and placement posture for boolean widgets.
It does not become the semantic owner of the boolean value or of the label content.
</p>

<hr/>

<h2 id="realization-variant-posture">3. Realization Variant Posture</h2>

<p>
The default boolean family standardizes one boolean realization corridor, not one mandatory visible shape.
</p>

<p>
Accordingly, a conforming realization MAY choose a boolean embodiment posture such as:
</p>

<ul>
  <li>checkbox-like,</li>
  <li>switch-like,</li>
  <li>toggle-like,</li>
  <li>LED-like,</li>
  <li>another host-compatible boolean embodiment.</li>
</ul>

<p>
Those remain realization variants of the same published boolean classes.
A switch-like visible embodiment does not by itself define a new intrinsic widget class.
</p>

<p>
This distinction is normative:
</p>

<ul>
  <li>the class layer owns boolean value semantics, public members, methods, events, and parts,</li>
  <li>the realization layer owns how those published surfaces are visually embodied,</li>
  <li>a realization-variant identifier is not a class identifier,</li>
  <li>a runtime MUST NOT treat a switch-like or checkbox-like embodiment as if it were a distinct standard class unless a separate class contract is explicitly published elsewhere.</li>
</ul>

<p>
For that reason, switch-like posture belongs here as a realization strategy, not as implicit class-level semantic drift.
</p>

<hr/>

<h2 id="realized-parts">4. Realized Parts</h2>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>state_face</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The realization may internally use additional layers, glow regions, check marks, selection indicators, focus rings, icon overlays, slider thumbs, tracks, or host-native toggle structures.
Those remain realization-private support structures unless they are explicitly published as realization resources or placement surfaces.
</p>

<p>
The default posture is:
</p>

<ul>
  <li><code>root</code> — overall layout, clipping, and outer realization region when needed,</li>
  <li><code>label</code> — dynamic text-bearing public part rendered through a realization-side placement surface,</li>
  <li><code>state_face</code> — main boolean state embodiment surface,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
A switch-like realization MAY internally decompose the visible embodiment into structures such as track and thumb.
Those remain realization-private unless explicitly published through a later realization-specific extension layer.
The stable public boolean part model remains centered on <code>state_face</code>, <code>label</code>, and optional <code>frame</code>.
</p>

<hr/>

<h2 id="standard-visual-states">5. Standard Visual States</h2>

<p>
The default boolean family defines at least:
</p>

<ul>
  <li><code>normal_false</code></li>
  <li><code>normal_true</code></li>
  <li><code>disabled_false</code></li>
  <li><code>disabled_true</code></li>
</ul>

<p>
For boolean controls, the family MAY also define:
</p>

<ul>
  <li><code>focused_false</code></li>
  <li><code>focused_true</code></li>
  <li><code>pressed_false</code></li>
  <li><code>pressed_true</code></li>
</ul>

<p>
These are realization-side composed visual states.
They combine a realization posture such as <code>normal</code>, <code>disabled</code>, <code>focused</code>, or <code>pressed</code> with the public boolean value posture <code>true</code> or <code>false</code>.
</p>

<p>
This composed-state vocabulary belongs to the realization family.
It does not replace the public class meaning of the boolean <code>value</code> surface itself.
</p>

<p>
A switch-like embodiment may use different geometry, motion, or emphasis for these states, but it still remains bound to the same published boolean state vocabulary unless an extended realization family explicitly publishes more specialized realization-only states.
</p>

<hr/>

<h2 id="part-state-mapping">6. Part-State Mapping</h2>

<p>
The default family expects:
</p>

<ul>
  <li><code>state_face</code> to distinguish true and false posture clearly,</li>
  <li><code>state_face</code> to distinguish enabled and disabled posture clearly,</li>
  <li><code>label</code> to remain readable across supported states,</li>
  <li><code>frame</code>, when present, to support focused posture where applicable.</li>
</ul>

<p>
A typical minimal mapping posture is:
</p>

<ul>
  <li><code>root</code> — global layout, clipping, and outer realization region,</li>
  <li><code>label</code> — dynamic text-bearing label surface,</li>
  <li><code>state_face</code> — main boolean state embodiment surface,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
The preferred machine-readable split is:
</p>

<ul>
  <li><code>state_face</code> published through <code>part_bindings</code> plus composed-value <code>state_maps</code>,</li>
  <li><code>label</code> published primarily through a <code>part_binding</code> to an anchor, text region, or equivalent placement surface,</li>
  <li><code>frame</code>, when present, published through <code>part_bindings</code> plus optional <code>state_maps</code>.</li>
</ul>

<p>
The default family SHOULD keep this mapping explicit enough that a machine-readable package can distinguish:
</p>

<ul>
  <li>state-sensitive visual resources,</li>
  <li>structural part bindings,</li>
  <li>dynamic host-rendered or host-updated boolean surfaces.</li>
</ul>

<p>
This distinction is important because <code>state_face</code> is the main embodiment surface of the boolean value, but it is not the semantic owner of the boolean value itself.
</p>

<p>
In a switch-like realization, any internal sub-embodiment such as track or thumb remains subordinate to the published <code>state_face</code> binding posture.
It does not create new public parts by implication alone.
</p>

<hr/>

<h2 id="dynamic-surface-posture">7. Dynamic Surface Posture</h2>

<h3>7.1 State-face posture</h3>

<p>
The <code>state_face</code> part is the main dynamic realization surface of the boolean family.
It is expected to reflect the public boolean value and, where applicable, additional realization-side interaction posture such as focus or press feedback.
</p>

<p>
A host interpreting this realization is expected to embody the current boolean value visibly through <code>state_face</code> rather than through runtime-private semantics hidden from inspection.
</p>

<p>
The realization owns how the boolean state is visually embodied.
It does not become the semantic owner of the boolean value itself.
</p>

<h3>7.2 Label posture</h3>

<p>
The semantic boolean label text is not owned by this realization.
It is owned by the standardized class surface through <code>label.text</code>.
</p>

<p>
The role of the default realization is to define where and how that semantic label is visually embodied, not to become the source of truth for the label text itself.
</p>

<p>
The <code>label</code> part is therefore expected to be realized as a dynamic text-bearing surface.
A host interpreting this realization should render or inject the current semantic boolean label into the realized label region at runtime.
</p>

<h3>7.3 Placement posture</h3>

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
This placement metadata may define:
</p>

<ul>
  <li>alignment box or region bounds,</li>
  <li>horizontal and vertical alignment,</li>
  <li>padding or inset region,</li>
  <li>clipping posture,</li>
  <li>the visual relation between the label and the state face when the realization chooses to expose it.</li>
</ul>

<p>
Those realization-side structures do not change the public meaning of <code>label.text</code>.
They only specify where the host should visually place the text.
</p>

<h3>7.4 Control versus indicator posture</h3>

<p>
The default realization may embody boolean controls and boolean indicators differently internally.
For example, a control may use a host-native checkbox, switch, or toggle button, while an indicator may use a simpler retained display surface.
</p>

<p>
Those internal differences are acceptable provided that:
</p>

<ul>
  <li>the published class identity remains preserved,</li>
  <li>the public parts remain interpretable,</li>
  <li>the difference between interactive and non-interactive posture remains compatible with the standardized class contract.</li>
</ul>

<p>
A runtime may internally flatten or decompose the visible boolean embodiment into toolkit-native layers, but the published realization contract should still make the meaning of <code>state_face</code>, <code>label</code>, and optional <code>frame</code> inspectable.
</p>

<h3>7.5 Switch-like posture as realization choice</h3>

<p>
A switch-like realization is an allowed embodiment choice within the default boolean family.
Such a realization may use:
</p>

<ul>
  <li>a sliding thumb,</li>
  <li>a track-like background,</li>
  <li>animated position shift between false and true posture,</li>
  <li>different ON and OFF emphasis zones,</li>
  <li>host-native switch affordance conventions.</li>
</ul>

<p>
However, those embodiment choices remain realization-owned.
They do not, by themselves, introduce:
</p>

<ul>
  <li>a distinct intrinsic widget class,</li>
  <li>new public boolean semantics,</li>
  <li>new mandatory public properties,</li>
  <li>new mandatory public methods,</li>
  <li>new mandatory public events.</li>
</ul>

<p>
If a future specification standardizes a switch-specific class, that class would need its own explicit class law.
Until then, switch-like posture remains a realization variant of <code>frog.widgets.boolean_control</code>.
</p>

<h3>7.6 Asset limitation rule</h3>

<p>
A boolean resource file MAY include placeholder marks, decorative indicators, preview labels, or design-time scaffolding.
However, a conforming realization family must not require that those asset-baked elements become the only path by which live boolean value or live semantic label text is shown.
</p>

<p>
Likewise, composed visual states such as <code>pressed_true</code> or <code>focused_false</code> must remain distinguishable from the semantic boolean value itself.
</p>

<hr/>

<h2 id="resource-posture">8. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>boolean_control/
  state_face/
    normal_false
    normal_true
    disabled_false
    disabled_true
    focused_false
    focused_true
    pressed_false
    pressed_true
  frame/
    normal_false
    normal_true
    focused_false
    focused_true
  anchors/
    label

boolean_indicator/
  state_face/
    normal_false
    normal_true
    disabled_false
    disabled_true
  frame/
    normal_false
    normal_true
  anchors/
    label
</code></pre>

<p>
An equivalent package-oriented posture may publish resources such as:
</p>

<ul>
  <li><code>boolean_control.state_face.normal_false.svg</code></li>
  <li><code>boolean_control.state_face.normal_true.svg</code></li>
  <li><code>boolean_control.state_face.pressed_true.svg</code></li>
  <li><code>boolean_control.state_face.focused_false.svg</code></li>
  <li><code>boolean_control.label.anchor_map</code> backed by <code>./assets/boolean_control/anchors/label.json</code></li>
  <li><code>boolean_indicator.state_face.normal_true.svg</code></li>
  <li><code>boolean_indicator.label.anchor_map</code> backed by <code>./assets/boolean_indicator/anchors/label.json</code></li>
</ul>

<p>
Resources MAY be SVG-backed, host-native, toolkit-driven, or mixed.
The default family standardizes the part posture, state posture, and realization-side binding posture, not one mandatory checkbox, switch, or toggle implementation and not one mandatory file format.
</p>

<p>
In particular:
</p>

<ul>
  <li><code>state_face</code> is the natural candidate for composed value-sensitive visual resources,</li>
  <li><code>label</code> is naturally a placement-bound dynamic text surface,</li>
  <li><code>frame</code>, when present, is a natural candidate for optional state-sensitive supporting resources.</li>
</ul>

<p>
A switch-like embodiment may still publish its resources under the same boolean realization corridor, as long as the published part meaning and state vocabulary remain preserved.
</p>

<hr/>

<h2 id="host-expectations">9. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>clear visible distinction between true and false,</li>
  <li>clear visible distinction between enabled and disabled,</li>
  <li>reasonable focus indication for controls,</li>
  <li>reasonable activation feedback for controls,</li>
  <li>dynamic rendering of visible boolean label text.</li>
</ul>

<p>
A host SHOULD also preserve the distinction between:
</p>

<ul>
  <li>the semantic boolean value owned by the class,</li>
  <li>the boolean label text owned by <code>label.text</code>,</li>
  <li>the realization-side embodiment of <code>state_face</code>, <code>label</code>, and <code>frame</code>.</li>
</ul>

<p>
A host MAY approximate the realization when exact resources are unavailable, but it should preserve:
</p>

<ul>
  <li>the interactive-versus-indicator distinction,</li>
  <li>the stable meaning of the published public parts,</li>
  <li>the separation between semantic boolean data and realization resources.</li>
</ul>

<p>
A host MAY choose a checkbox-like or switch-like embodiment strategy.
That choice is acceptable only if the public boolean class meaning remains unchanged and the realization contract remains inspectable.
</p>

<hr/>

<h2 id="fallback-posture">10. Fallback Posture</h2>

<p>
If state-specific resources are unavailable, a runtime MAY use host-native boolean widgets or generic state rendering, provided the true/false and enabled/disabled distinctions remain preserved.
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
If focused or pressed state-specific resources are unavailable, a host MAY fall back to host-native focus or activation posture provided that the distinction remains visible and the value-sensitive embodiment remains clear.
</p>

<p>
If a switch-like embodiment cannot be realized exactly, a host MAY fall back to another compatible boolean embodiment such as checkbox-like or generic toggle-like posture, provided that:
</p>

<ul>
  <li>the published boolean class meaning remains unchanged,</li>
  <li>the true/false and enabled/disabled distinctions remain clear,</li>
  <li>the fallback does not imply a new class-level contract.</li>
</ul>

<p>
Any fallback MUST preserve the published boolean class law and the meaning of the public parts when those parts are exposed.
Fallback must not turn asset-baked boolean marks or asset-baked label text into semantic truth.
</p>

<p>
Fallback must remain inspectable at the realization-publication layer.
It must not become a purely runtime-private convention.
</p>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
The default boolean realization defines one official state-structured embodiment for boolean controls and boolean indicators, centered on the public <code>state_face</code> part.
</p>

<p>
It realizes:
</p>

<ul>
  <li><code>state_face</code> as the main dynamic boolean state embodiment surface,</li>
  <li><code>label</code> as a dynamically rendered text-bearing surface,</li>
  <li><code>frame</code> as an optional supporting outer surface.</li>
</ul>

<p>
Its resources may provide skins, layers, regions, and anchors.
Its package publication may provide <code>state_maps</code> and <code>part_bindings</code>.
Its host implementation may approximate the visuals when needed.
But the realization never becomes the semantic owner of boolean value, boolean label text, or boolean class meaning.
</p>

<p>
In this realization family, checkbox-like, switch-like, and similar visible embodiments remain realization variants unless a future specification publishes a distinct class with genuinely distinct public semantics.
</p>
