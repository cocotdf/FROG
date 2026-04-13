<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — Enum Widgets</h1>

<p align="center">
  <strong>Normative default realization posture for standardized enum widgets</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#target-classes">2. Target Classes</a></li>
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
This document defines the default official realization posture for the standardized enum widget family.
</p>

<p>
The default enum realization is intended to provide one clean, inspectable, portable embodiment of the intrinsic enum baseline without turning one host toolkit, popup implementation, or dropdown control into the semantic definition of enum widgets.
</p>

<p>
This realization is realization-side only.
It does not redefine enum class law, does not invent new public members, and does not replace the semantic ownership of enum value, enum item inventory, or enum label text.
Its job is to embody already-published enum widget surfaces through stable visual states, stable part mappings, and realization-side placement or rendering metadata where needed.
</p>

<hr/>

<h2 id="target-classes">2. Target Classes</h2>

<ul>
  <li><code>frog.widgets.enum_control</code></li>
  <li><code>frog.widgets.enum_indicator</code></li>
</ul>

<p>
This realization assumes the standardized enum posture in which:
</p>

<ul>
  <li>enum widgets expose a primary selected value through <code>value</code>,</li>
  <li>enum widgets expose a finite item inventory through <code>items</code>,</li>
  <li>enum widgets may expose semantic label text through <code>label.text</code>,</li>
  <li>the published public parts remain stable across realizations,</li>
  <li>the realization remains downstream from that class contract.</li>
</ul>

<hr/>

<h2 id="realized-parts">3. Realized Parts</h2>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>value_display</code></li>
  <li><code>selector_face</code> when the active realization exposes a distinct selector affordance</li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The realization may internally use additional popup layers, list surfaces, arrows, menus, clipping regions, or host-native selection helpers.
Those remain realization-private support structures unless they are published elsewhere as part of an explicit realization package or a future higher-level enum contract.
</p>

<hr/>

<h2 id="standard-visual-states">4. Standard Visual States</h2>

<p>
The default enum family defines at least:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code></li>
  <li><code>focused</code></li>
</ul>

<p>
For enum controls, the default family MAY additionally define:
</p>

<ul>
  <li><code>opened</code> when the active realization exposes an explicit opened-selection posture</li>
  <li><code>pressed</code> when the active realization exposes a distinct pressed selector face</li>
</ul>

<p>
These are realization-side visual states.
They do not redefine the semantic meaning of enum value, enum item legality, or enum class identity.
</p>

<hr/>

<h2 id="part-state-mapping">5. Part-State Mapping</h2>

<p>
The default family expects:
</p>

<ul>
  <li><code>value_display</code> to remain readable across supported states,</li>
  <li><code>label</code> to remain readable when shown,</li>
  <li><code>selector_face</code> to provide visible selection affordance when realized,</li>
  <li><code>frame</code>, when present, to support focused posture where applicable.</li>
</ul>

<p>
A typical minimal mapping posture is:
</p>

<ul>
  <li><code>root</code> — global layout, clipping, and outer realization region,</li>
  <li><code>label</code> — dynamic text-bearing label surface,</li>
  <li><code>value_display</code> — dynamic selected-value display surface,</li>
  <li><code>selector_face</code> — optional selector affordance surface,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
The default family SHOULD keep this mapping explicit enough that a machine-readable package can distinguish:
</p>

<ul>
  <li>state-sensitive visual resources,</li>
  <li>structural part bindings,</li>
  <li>dynamic host-rendered or host-updated enum display surfaces.</li>
</ul>

<hr/>

<h2 id="dynamic-surface-posture">6. Dynamic Surface Posture</h2>

<h3>6.1 Selected-value display posture</h3>

<p>
The <code>value_display</code> part is not just a static decorative asset surface.
It is a dynamic realization surface that reflects the currently selected enum value.
</p>

<p>
A host interpreting this realization is expected to render or update the visible selected item according to the published class surfaces through <code>value</code> and <code>items</code>.
</p>

<p>
The realization owns how the selected value is visually embodied.
It does not become the semantic owner of the selected value itself.
</p>

<h3>6.2 Label posture</h3>

<p>
The semantic enum label text is not owned by this realization.
It is owned by the standardized class surface through <code>label.text</code>.
</p>

<p>
The role of the default realization is to define where and how that semantic label is visually embodied, not to become the source of truth for the label text itself.
</p>

<p>
The <code>label</code> part is therefore expected to be realized as a dynamic text-bearing surface.
A host interpreting this realization should render or inject the current semantic enum label into the realized label region at runtime.
</p>

<h3>6.3 Selector-face posture</h3>

<p>
The <code>selector_face</code> part is an optional realization-side affordance surface.
It may represent an arrow, a dropdown cue, a ring indicator, or another compatible embodiment of single-selection interaction.
</p>

<p>
Its presence does not redefine enum semantics.
It only supports the visible interaction posture of the realization.
</p>

<h3>6.4 Asset limitation rule</h3>

<p>
An enum resource file MAY include placeholder item text, preview values, decorative list hints, or design-time scaffolding.
However, a conforming realization family must not require that those asset-baked strings become the only path by which the live selected value or live semantic label text is shown.
</p>

<hr/>

<h2 id="resource-posture">7. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>enum_control/
  value_display/
    normal
    disabled
    focused
    opened
  selector_face/
    normal
    pressed
    opened
  frame/
    normal
    focused
  anchors/
    label
    value_display

enum_indicator/
  value_display/
    normal
    focused
  frame/
    normal
    focused
  anchors/
    label
    value_display
</code></pre>

<p>
An equivalent package-oriented posture may publish resources such as:
</p>

<ul>
  <li><code>enum_control.value_display.normal.svg</code></li>
  <li><code>enum_control.value_display.opened.svg</code></li>
  <li><code>enum_control.selector_face.pressed.svg</code></li>
  <li><code>enum_control.label.anchor.json</code></li>
  <li><code>enum_control.value_display.region.json</code> or another explicit placement artifact</li>
  <li><code>enum_indicator.value_display.normal.svg</code></li>
</ul>

<p>
Resources MAY be SVG-backed, host-native, toolkit-driven, or mixed.
The default family standardizes the part posture, state posture, and realization-side binding posture, not one mandatory popup engine or one mandatory file format.
</p>

<hr/>

<h2 id="host-expectations">8. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a clearly readable selected-value surface,</li>
  <li>a visible disabled posture when interaction is suppressed,</li>
  <li>a visible focus posture where host focus is supported,</li>
  <li>a visible selector affordance when the realization exposes one,</li>
  <li>dynamic rendering of visible selected value and label text.</li>
</ul>

<p>
A host SHOULD also preserve the distinction between:
</p>

<ul>
  <li>the semantic selected value owned by the class,</li>
  <li>the semantic item inventory owned by <code>items</code>,</li>
  <li>the enum label text owned by <code>label.text</code>,</li>
  <li>the realization-side embodiment of label, value display, selector face, and frame.</li>
</ul>

<p>
A host MAY approximate the realization when exact resources are unavailable, but it should preserve:
</p>

<ul>
  <li>the control-versus-indicator distinction,</li>
  <li>the stable meaning of the published public parts,</li>
  <li>the separation between semantic enum data and realization resources.</li>
</ul>

<hr/>

<h2 id="fallback-posture">9. Fallback Posture</h2>

<p>
If selector-face-specific resources are unavailable, a runtime MAY:
</p>

<ul>
  <li>use a host-native single-selection control embodiment,</li>
  <li>omit a visible selector affordance while preserving selection capability,</li>
  <li>reuse generic focused or normal posture for the selector face.</li>
</ul>

<p>
If dedicated label or selected-value placement resources are unavailable, a host MAY fall back to:
</p>

<ul>
  <li>a host-native text region,</li>
  <li>a generic single-line display region,</li>
  <li>another documented compatible placement rule.</li>
</ul>

<p>
Any fallback MUST preserve the published enum class law and the meaning of the public parts when those parts are exposed.
Fallback must not turn asset-baked item text or label text into semantic truth.
</p>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The default enum realization defines one official embodiment of the enum widget family, including optional selector-face realization.
</p>

<p>
It realizes:
</p>

<ul>
  <li><code>value_display</code> as the main dynamic selected-value surface,</li>
  <li><code>label</code> as a dynamically rendered text-bearing surface,</li>
  <li><code>selector_face</code> as an optional visible selection affordance,</li>
  <li><code>frame</code> as an optional supporting outer surface.</li>
</ul>

<p>
Its resources may provide skins, layers, regions, and anchors.
Its package publication may provide state maps and bindings.
Its host implementation may approximate the visuals when needed.
But the realization never becomes the semantic owner of enum value, enum item inventory, enum label text, or enum class meaning.
</p>
