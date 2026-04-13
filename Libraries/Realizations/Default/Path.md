<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — Path Widgets</h1>

<p align="center">
  <strong>Normative default realization posture for standardized path widgets</strong><br/>
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
This document defines the default official realization posture for the standardized path widget family.
</p>

<p>
The default path realization is intended to provide one clean, inspectable, portable embodiment of the intrinsic path baseline without turning one host file picker, browse dialog, or path-entry widget into the semantic definition of path widgets.
</p>

<p>
This realization is realization-side only.
It does not redefine path class law, does not invent new public members, and does not replace the semantic ownership of path value or path label text.
Its job is to embody already-published path widget surfaces through stable visual states, stable part mappings, and realization-side placement or rendering metadata where needed.
</p>

<hr/>

<h2 id="target-classes">2. Target Classes</h2>

<ul>
  <li><code>frog.widgets.path_control</code></li>
  <li><code>frog.widgets.path_indicator</code></li>
</ul>

<p>
This realization assumes the standardized path posture in which:
</p>

<ul>
  <li>path widgets expose a primary path value through <code>value</code>,</li>
  <li>path widgets may expose semantic label text through <code>label.text</code>,</li>
  <li>path controls may expose browse-oriented behavior while path indicators remain display-oriented,</li>
  <li>the published public parts remain stable across realizations,</li>
  <li>the realization remains downstream from that class contract.</li>
</ul>

<hr/>

<h2 id="realized-parts">3. Realized Parts</h2>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>path_display</code></li>
  <li><code>browse_button</code> when the active realization exposes it</li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The realization may internally use additional clipping regions, ellipsis helpers, path shortening helpers, browse icons, or host-native picker structures.
Those remain realization-private support structures unless they are published elsewhere as part of an explicit realization package or a future higher-level path contract.
</p>

<hr/>

<h2 id="standard-visual-states">4. Standard Visual States</h2>

<p>
The default path family defines at least:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code></li>
  <li><code>focused</code></li>
</ul>

<p>
For path controls, the default family MAY additionally define:
</p>

<ul>
  <li><code>pressed</code> for the browse button when the active realization exposes it</li>
</ul>

<p>
These are realization-side visual states.
They do not redefine the semantic meaning of path value, path mode, or path class identity.
</p>

<hr/>

<h2 id="part-state-mapping">5. Part-State Mapping</h2>

<p>
The default family expects:
</p>

<ul>
  <li><code>path_display</code> to remain readable across supported states,</li>
  <li><code>label</code> to remain readable when shown,</li>
  <li><code>browse_button</code> to provide visible browse affordance when realized,</li>
  <li><code>frame</code>, when present, to support focused posture where applicable.</li>
</ul>

<p>
A typical minimal mapping posture is:
</p>

<ul>
  <li><code>root</code> — global layout, clipping, and outer realization region,</li>
  <li><code>label</code> — dynamic text-bearing label surface,</li>
  <li><code>path_display</code> — dynamic path display or editing surface,</li>
  <li><code>browse_button</code> — optional browse interaction affordance,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
The default family SHOULD keep this mapping explicit enough that a machine-readable package can distinguish:
</p>

<ul>
  <li>state-sensitive visual resources,</li>
  <li>structural part bindings,</li>
  <li>dynamic host-rendered or host-updated path surfaces.</li>
</ul>

<hr/>

<h2 id="dynamic-surface-posture">6. Dynamic Surface Posture</h2>

<h3>6.1 Path-display posture</h3>

<p>
The <code>path_display</code> part is not just a static decorative asset surface.
It is a dynamic realization surface that reflects the current path value and, for controls, may also reflect host editing posture.
</p>

<p>
A host interpreting this realization is expected to render or update the visible path content according to the published class surface through <code>value</code> and the control-or-indicator posture of the target class.
</p>

<p>
The realization owns how the path display is visually embodied.
It does not become the semantic owner of the path value itself.
</p>

<h3>6.2 Label posture</h3>

<p>
The semantic path label text is not owned by this realization.
It is owned by the standardized class surface through <code>label.text</code>.
</p>

<p>
The role of the default realization is to define where and how that semantic label is visually embodied, not to become the source of truth for the label text itself.
</p>

<p>
The <code>label</code> part is therefore expected to be realized as a dynamic text-bearing surface.
A host interpreting this realization should render or inject the current semantic path label into the realized label region at runtime.
</p>

<h3>6.3 Browse-button posture</h3>

<p>
The <code>browse_button</code> part is an optional realization-side interaction affordance.
When present, it may be embodied through:
</p>

<ul>
  <li>an SVG-backed button layer,</li>
  <li>a host-native browse button,</li>
  <li>a toolkit-native picker affordance,</li>
  <li>another compatible host interaction mechanism.</li>
</ul>

<p>
Its presence does not redefine the semantic path value.
It only supports the visible browse posture of the realization.
</p>

<h3>6.4 Asset limitation rule</h3>

<p>
A path resource file MAY include placeholder paths, decorative path text, preview text, or design-time scaffolding.
However, a conforming realization family must not require that those asset-baked strings become the only path by which live path value or live semantic label text is shown.
</p>

<hr/>

<h2 id="resource-posture">7. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>path_control/
  path_display/
    normal
    disabled
    focused
  browse_button/
    normal
    pressed
  frame/
    normal
    focused
  anchors/
    label
    path_display

path_indicator/
  path_display/
    normal
    focused
  frame/
    normal
    focused
  anchors/
    label
    path_display
</code></pre>

<p>
An equivalent package-oriented posture may publish resources such as:
</p>

<ul>
  <li><code>path_control.path_display.normal.svg</code></li>
  <li><code>path_control.path_display.focused.svg</code></li>
  <li><code>path_control.browse_button.pressed.svg</code></li>
  <li><code>path_control.label.anchor.json</code></li>
  <li><code>path_control.path_display.region.json</code> or another explicit placement artifact</li>
  <li><code>path_indicator.path_display.normal.svg</code></li>
</ul>

<p>
Resources MAY be SVG-backed, host-native, toolkit-driven, or mixed.
The default family standardizes the part posture, state posture, and realization-side binding posture, not one mandatory file picker or one mandatory file format.
</p>

<hr/>

<h2 id="host-expectations">8. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a clearly readable path display surface,</li>
  <li>a visible disabled posture when interaction is suppressed,</li>
  <li>a visible focus posture where host focus is supported,</li>
  <li>visible browse-button feedback when the browse part is realized,</li>
  <li>dynamic rendering of visible path value and label text.</li>
</ul>

<p>
A host SHOULD also preserve the distinction between:
</p>

<ul>
  <li>the semantic path value owned by the class,</li>
  <li>the path label text owned by <code>label.text</code>,</li>
  <li>the realization-side embodiment of label, path display, browse button, and frame.</li>
</ul>

<p>
A host MAY approximate the realization when exact resources are unavailable, but it should preserve:
</p>

<ul>
  <li>the editable-versus-indicator distinction,</li>
  <li>the stable meaning of the published public parts,</li>
  <li>the separation between semantic path data and realization resources.</li>
</ul>

<hr/>

<h2 id="fallback-posture">9. Fallback Posture</h2>

<p>
If browse-button-specific resources are unavailable, a runtime MAY:
</p>

<ul>
  <li>use a host-native browse affordance,</li>
  <li>omit a visible browse button while preserving path editing capability,</li>
  <li>reuse generic button-state posture for the browse button.</li>
</ul>

<p>
If dedicated label or path-display placement resources are unavailable, a host MAY fall back to:
</p>

<ul>
  <li>a host-native text region,</li>
  <li>a generic text-entry or text-display region,</li>
  <li>another documented compatible placement rule.</li>
</ul>

<p>
Any fallback MUST preserve the published path class law and the meaning of the public parts when those parts are exposed.
Fallback must not turn asset-baked path text or label text into semantic truth.
</p>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The default path realization defines one official embodiment of the path widget family, including optional browse-button realization.
</p>

<p>
It realizes:
</p>

<ul>
  <li><code>path_display</code> as the main dynamic path display or editing surface,</li>
  <li><code>label</code> as a dynamically rendered text-bearing surface,</li>
  <li><code>browse_button</code> as an optional browse interaction surface,</li>
  <li><code>frame</code> as an optional supporting outer surface.</li>
</ul>

<p>
Its resources may provide skins, layers, regions, and anchors.
Its package publication may provide state maps and bindings.
Its host implementation may approximate the visuals when needed.
But the realization never becomes the semantic owner of path value, path label text, or path class meaning.
</p>
