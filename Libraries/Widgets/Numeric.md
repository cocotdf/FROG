<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Numeric Widgets</h1>

<p align="center">
  <strong>Normative baseline for the currently published numeric control and numeric indicator classes</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Navigation</h2>

<ul>
  <li><a href="./Readme.md">Widgets index</a></li>
  <li><a href="../../Expression/Widget.md">Expression widget instances</a></li>
  <li><a href="../../Expression/Widget interaction.md">Expression widget interaction</a></li>
  <li><a href="../../Libraries/UI.md">Executable UI primitives</a></li>
  <li><a href="../../Examples/05_bounded_ui_accumulator/Readme.md">Example 05 corridor</a></li>
  <li><a href="../../Examples/05_bounded_ui_accumulator/ui/accumulator_panel.wfrog">Example 05 published <code>.wfrog</code></a></li>
  <li><a href="../../Profiles/UI%20Widget%20Classes.md">Profile posture for widget-class adoption</a></li>
</ul>

<hr/>

<h2>1. Overview</h2>

<p>
This document defines the currently published intrinsic numeric widget baseline used by the first executable UI slice.
</p>

<p>
The active published numeric classes are:
</p>

<ul>
  <li><code>frog.widgets.numeric_control</code></li>
  <li><code>frog.widgets.numeric_indicator</code></li>
</ul>

<p>
These class identifiers match the canonical source, the published Example 05 <code>.wfrog</code> package, the emitted runtime-family contract, and the published reference runtimes.
</p>

<hr/>

<h2>2. Ownership boundary</h2>

<ul>
  <li><code>Expression/</code> owns widget instances in canonical source.</li>
  <li><code>Libraries/UI.md</code> owns executable interaction primitives such as <code>frog.ui.property_write</code>.</li>
  <li><code>Libraries/Widgets/</code> owns the portable public law of intrinsic standardized widget classes.</li>
  <li><code>.wfrog</code> packages publish concrete class, panel, asset, and host-binding material for specific corridors.</li>
  <li>runtimes consume those published artifacts; they do not redefine the class law.</li>
</ul>

<p>
Therefore, this file defines the portable public surface of the numeric classes. It does not define host-private handles, toolkit-private structures, or skin-private layer maps.
</p>

<hr/>

<h2>3. Common numeric-family posture</h2>

<ul>
  <li>class family: scalar numeric widgets,</li>
  <li>primary semantic value property: <code>value</code>,</li>
  <li>shared text label property: <code>label</code>,</li>
  <li>shared visibility property: <code>visible</code>,</li>
  <li>shared enablement property: <code>enabled</code>,</li>
  <li>shared portable presentation property for the first slice: <code>foreground_color</code>,</li>
  <li>stable public parts: <code>root</code>, <code>label</code>, <code>value_display</code>.</li>
</ul>

<p>
The currently published baseline uses <strong>flat public property names</strong>.
The active published portable surface is therefore <code>label</code>, not <code>label.text</code>; <code>visible</code>, not <code>interaction.visible</code>; and <code>foreground_color</code>, not <code>style.foreground_color</code>.
</p>

<p>
Nested property namespaces may be standardized later, but they are not the active portable baseline of the currently published slice.
</p>

<hr/>

<h2>4. <code>frog.widgets.numeric_control</code></h2>

<h3>4.1 Identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.numeric_control</code></li>
  <li><strong>compatible role:</strong> <code>control</code></li>
  <li><strong>primary value participation:</strong> editable numeric value</li>
</ul>

<h3>4.2 Portable public properties</h3>

<ul>
  <li><code>value</code> — readable and writable numeric primary value</li>
  <li><code>label</code> — readable and writable string label</li>
  <li><code>visible</code> — readable and writable boolean visibility</li>
  <li><code>enabled</code> — readable and writable boolean enablement</li>
  <li><code>foreground_color</code> — readable and writable portable presentation color token of type <code>frog.color.rgba8</code></li>
</ul>

<h3>4.3 Portable public methods</h3>

<ul>
  <li><code>focus()</code> — requests focus on the control when the active host can realize focus transfer</li>
</ul>

<h3>4.4 Portable public events</h3>

<ul>
  <li><code>value_changed</code> — runtime-observable event carrying the current numeric value</li>
</ul>

<h3>4.5 Public parts</h3>

<ul>
  <li><code>root</code> — widget root container</li>
  <li><code>label</code> — label presentation target</li>
  <li><code>value_display</code> — realized numeric editing or display face</li>
</ul>

<hr/>

<h2>5. <code>frog.widgets.numeric_indicator</code></h2>

<h3>5.1 Identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.numeric_indicator</code></li>
  <li><strong>compatible role:</strong> <code>indicator</code></li>
  <li><strong>primary value participation:</strong> diagram-published numeric result</li>
</ul>

<h3>5.2 Portable public properties</h3>

<ul>
  <li><code>value</code> — readable and writable numeric primary value</li>
  <li><code>label</code> — readable and writable string label</li>
  <li><code>visible</code> — readable and writable boolean visibility</li>
  <li><code>enabled</code> — readable and writable boolean enablement</li>
  <li><code>foreground_color</code> — readable and writable portable presentation color token of type <code>frog.color.rgba8</code></li>
</ul>

<h3>5.3 Portable public methods</h3>

<ul>
  <li><code>reset_to_default_style()</code> — restores the indicator instance to the default style values published by the active panel package</li>
</ul>

<h3>5.4 Portable public events</h3>

<ul>
  <li><code>value_rendered</code> — runtime-observable event carrying the realized display text</li>
</ul>

<h3>5.5 Public parts</h3>

<ul>
  <li><code>root</code> — widget root container</li>
  <li><code>label</code> — label presentation target</li>
  <li><code>value_display</code> — realized numeric display face</li>
</ul>

<hr/>

<h2>6. Diagram interaction posture</h2>

<p>
The numeric baseline participates in diagrams through the already-published interaction architecture.
</p>

<ul>
  <li><code>widget_value(...)</code> exposes the primary numeric value as natural diagram data.</li>
  <li><code>widget_reference(...)</code> exposes object-style access for portable member interaction.</li>
  <li><code>frog.ui.property_write</code> may target portable writable members such as <code>foreground_color</code>.</li>
  <li>method invocation remains object-style and member-specific; it does not replace value participation.</li>
</ul>

<p>
Example 05 is the current corridor anchor for this posture. It uses <code>widget_value</code> for the control and indicator value path, <code>widget_reference</code> for object access, and <code>frog.ui.property_write</code> for <code>foreground_color</code> writes.
</p>

<hr/>

<h2>7. Realization posture</h2>

<p>
The numeric classes are semantic and portable. Realization remains downstream.
</p>

<ul>
  <li>default SVG assets may be published by a corridor package,</li>
  <li>host bindings may require windowing, value binding, reference binding, and property writes,</li>
  <li>skins and visual assets may change without changing the class identity or the public property law.</li>
</ul>

<p>
Therefore, a change of skin or rendered face does not create a new numeric class.
</p>

<hr/>

<h2>8. Current slice commitments</h2>

<p>
A runtime, package, or profile that claims conformance to the current published Example 05 numeric slice must support at least the following portable public members for these classes:
</p>

<ul>
  <li><code>value</code></li>
  <li><code>label</code></li>
  <li><code>visible</code></li>
  <li><code>enabled</code></li>
  <li><code>foreground_color</code></li>
  <li><code>focus()</code> for <code>frog.widgets.numeric_control</code></li>
  <li><code>reset_to_default_style()</code> for <code>frog.widgets.numeric_indicator</code></li>
</ul>

<hr/>

<h2>9. Summary</h2>

<p>
The active published numeric baseline is intentionally narrow but real.
It uses the <code>frog.widgets.*</code> class identifiers, flat property names, portable member interaction through <code>widget_reference</code> and <code>frog.ui.*</code>, and a realization layer that stays downstream from class meaning.
</p>
