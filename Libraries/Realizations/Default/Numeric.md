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
This document defines the default official realization posture for the standardized numeric widget family.
</p>

<p>
The default numeric realization is intended to provide one clean, inspectable, portable embodiment of the intrinsic numeric baseline without turning one host toolkit or one runtime-specific editor into the semantic definition of numeric widgets.
</p>

<p>
This realization is realization-side only.
It does not redefine numeric class law, does not invent new public members, and does not replace the semantic ownership of numeric value, numeric label text, or numeric editing semantics.
Its job is to embody already-published numeric widget surfaces through stable visual states, stable part mappings, and realization-side placement or rendering metadata where needed.
</p>

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
  <li>numeric controls may expose <code>increment()</code> and <code>decrement()</code> interaction when the active realization supports it,</li>
  <li>the published public parts remain stable across realizations,</li>
  <li>the realization remains downstream from that class contract.</li>
</ul>

<hr/>

<h2 id="realized-parts">3. Realized Parts</h2>

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
The realization may internally use additional layers, clipping regions, caret surfaces, editing guides, or host-native editor structures.
Those remain realization-private support structures unless they are published elsewhere as part of an explicit realization package or a future higher-level numeric contract.
</p>

<hr/>

<h2 id="standard-visual-states">4. Standard Visual States</h2>

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
These are realization-side visual states.
They do not redefine the semantic meaning of numeric value, numeric editing legality, or numeric class identity.
</p>

<hr/>

<h2 id="part-state-mapping">5. Part-State Mapping</h2>

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
The default family SHOULD keep this mapping explicit enough that a machine-readable package can distinguish:
</p>

<ul>
  <li>state-sensitive visual resources,</li>
  <li>structural part bindings,</li>
  <li>dynamic host-rendered or host-updated numeric surfaces.</li>
</ul>

<hr/>

<h2 id="dynamic-surface-posture">6. Dynamic Surface Posture</h2>

<h3>6.1 Value display posture</h3>

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

<h3>6.2 Label posture</h3>

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

<h3>6.3 Step-button posture</h3>

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

<h3>6.4 Asset limitation rule</h3>

<p>
A numeric resource file MAY include placeholder digits, decorative guides, preview values, or design-time scaffolding.
However, a conforming realization family must not require that those asset-baked values become the only path by which live numeric value or live semantic label text is shown.
</p>

<hr/>

<h2 id="resource-posture">7. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>numeric_control/
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
  anchors/
    label
    value_display

numeric_indicator/
  value_display/
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
  <li><code>numeric_control.value_display.normal.svg</code></li>
  <li><code>numeric_control.value_display.focused.svg</code></li>
  <li><code>numeric_control.increment_button.pressed.svg</code></li>
  <li><code>numeric_control.decrement_button.pressed.svg</code></li>
  <li><code>numeric_control.label.anchor.json</code></li>
  <li><code>numeric_control.value_display.region.json</code> or another explicit placement artifact</li>
  <li><code>numeric_indicator.value_display.normal.svg</code></li>
</ul>

<p>
Resources MAY be SVG-backed, host-native, toolkit-driven, or mixed.
The default family standardizes the part posture, state posture, and realization-side binding posture, not one mandatory editor implementation or one mandatory file format.
</p>

<hr/>

<h2 id="host-expectations">8. Host Expectations</h2>

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
A host MAY approximate the realization when exact resources are unavailable, but it should preserve:
</p>

<ul>
  <li>the editable-versus-indicator distinction,</li>
  <li>the stable meaning of the published public parts,</li>
  <li>the separation between semantic numeric data and realization resources.</li>
</ul>

<hr/>

<h2 id="fallback-posture">9. Fallback Posture</h2>

<p>
If step-button-specific resources are unavailable, a runtime MAY:
</p>

<ul>
  <li>use host-native increment and decrement controls,</li>
  <li>omit visible step buttons while preserving numeric editing capability,</li>
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
Any fallback MUST preserve the published numeric class law and the meaning of the public parts when those parts are exposed.
Fallback must not turn asset-baked digits or asset-baked label text into semantic truth.
</p>

<hr/>

<h2 id="summary">10. Summary</h2>

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
  <li><code>frame</code> as an optional supporting outer surface.</li>
</ul>

<p>
Its resources may provide skins, layers, regions, and anchors.
Its package publication may provide state maps and bindings.
Its host implementation may approximate the visuals when needed.
But the realization never becomes the semantic owner of numeric value, numeric label text, or numeric class meaning.
</p>
