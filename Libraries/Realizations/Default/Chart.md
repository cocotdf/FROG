<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — Waveform Chart</h1>

<p align="center">
  <strong>Normative default realization posture for <code>frog.widgets.waveform_chart</code></strong><br/>
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
This document defines the default official realization posture for <code>frog.widgets.waveform_chart</code>.
</p>

<p>
The default chart realization is intended to be minimal but credible.
It provides a standard visual embodiment of the published chart parts without prematurely standardizing a complete plotting framework.
</p>

<p>
This realization is realization-side only.
It does not redefine chart class law, does not invent new public chart members, and does not replace the semantic ownership of chart value, chart label text, or chart-visible history posture.
Its job is to embody already-published chart surfaces through stable visual states, stable part mappings, and realization-side placement or rendering metadata where needed.
</p>

<hr/>

<h2 id="target-class">2. Target Class</h2>

<ul>
  <li><strong>target class:</strong> <code>frog.widgets.waveform_chart</code></li>
</ul>

<p>
This realization assumes the standardized chart posture in which:
</p>

<ul>
  <li>the chart is indicator-oriented,</li>
  <li>the chart exposes a primary value through <code>value</code>,</li>
  <li>the chart may expose bounded visible history through <code>history.capacity</code> when that surface is active,</li>
  <li>the chart exposes stable public parts such as <code>plot_area</code>, <code>x_axis</code>, <code>y_axis</code>, and <code>label</code>,</li>
  <li>the realization remains downstream from that class contract.</li>
</ul>

<hr/>

<h2 id="realized-parts">3. Realized Parts</h2>

<ul>
  <li><code>root</code></li>
  <li><code>plot_area</code></li>
  <li><code>axes</code></li>
  <li><code>x_axis</code></li>
  <li><code>y_axis</code></li>
  <li><code>label</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The realization may internally use additional layers, guides, clipping regions, grid surfaces, plot traces, or host-native plotting structures.
Those remain realization-private support structures unless they are published elsewhere as part of an explicit realization package or a future higher-level chart contract.
</p>

<hr/>

<h2 id="standard-visual-states">4. Standard Visual States</h2>

<p>
The default chart realization defines at least:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code> when the host supports disabled posture for display widgets</li>
  <li><code>focused</code> when the host supports focus posture</li>
</ul>

<p>
These are realization-side visual states.
They do not create new persistent chart-owned source state by themselves.
</p>

<p>
The default family does not require a pressed-like posture for the chart baseline because the standardized chart is not a command-style control in the intrinsic baseline.
</p>

<hr/>

<h2 id="part-state-mapping">5. Part-State Mapping</h2>

<p>
The default family expects:
</p>

<ul>
  <li><code>plot_area</code> to provide the main plotted display region,</li>
  <li><code>x_axis</code> and <code>y_axis</code> to provide visible axis surfaces when the corresponding axis visibility posture is enabled,</li>
  <li><code>axes</code> to remain the aggregate axes realization surface when the host or package uses one,</li>
  <li><code>label</code> to remain readable when the label is shown,</li>
  <li><code>frame</code>, when present, to support focused posture where applicable.</li>
</ul>

<p>
A typical minimal mapping posture is:
</p>

<ul>
  <li><code>root</code> — global layout, clipping, and outer realization region,</li>
  <li><code>plot_area</code> — plotted data region and associated visual background,</li>
  <li><code>axes</code> — aggregate axis support surface when published as one realization-side grouping,</li>
  <li><code>x_axis</code> — horizontal axis embodiment,</li>
  <li><code>y_axis</code> — vertical axis embodiment,</li>
  <li><code>label</code> — dynamic text-bearing chart label surface,</li>
  <li><code>frame</code> — optional border or focus-emphasis surface.</li>
</ul>

<p>
The default family SHOULD keep this mapping explicit enough that a machine-readable package can distinguish:
</p>

<ul>
  <li>state-sensitive visual resources,</li>
  <li>structural part bindings,</li>
  <li>dynamic host-rendered or host-updated chart surfaces.</li>
</ul>

<hr/>

<h2 id="dynamic-surface-posture">6. Dynamic Surface Posture</h2>

<h3>6.1 Plot surface posture</h3>

<p>
The <code>plot_area</code> part is not just a static decorative asset surface.
It is a dynamic realization surface that reflects chart value and visible history updates.
</p>

<p>
A host interpreting this realization is expected to update the plotted display according to the published chart value and history posture.
That update may be implemented through:
</p>

<ul>
  <li>a host-native plotting widget,</li>
  <li>a retained-mode vector or canvas plot surface,</li>
  <li>a custom rendering layer backed by realization resources.</li>
</ul>

<p>
The realization owns how plotted history is visually embodied.
It does not become the semantic owner of the chart value itself.
</p>

<h3>6.2 Axis posture</h3>

<p>
The chart class owns the public existence of axis visibility surfaces such as <code>axes.x.visible</code> and <code>axes.y.visible</code>.
The default realization owns how those axes are visually embodied when they are shown.
</p>

<p>
The default realization may therefore publish:
</p>

<ul>
  <li>axis layers,</li>
  <li>axis region bindings,</li>
  <li>axis label regions,</li>
  <li>grid or tick support surfaces when the family uses them.</li>
</ul>

<p>
However, the intrinsic default posture does not require a full standardized axis formatting system in this document.
</p>

<h3>6.3 Label posture</h3>

<p>
The semantic chart label text is not owned by this realization.
It is owned by the standardized class surface through <code>label.text</code>.
</p>

<p>
The role of the default realization is to define where and how that semantic label is visually embodied, not to become the source of truth for the label text itself.
</p>

<p>
The <code>label</code> part is therefore expected to be realized as a dynamic text-bearing surface.
A host interpreting this realization should render or inject the current semantic chart label into the realized label region at runtime.
</p>

<p>
The default family may publish that label region through:
</p>

<ul>
  <li>a text anchor,</li>
  <li>a text region,</li>
  <li>a host-native region,</li>
  <li>another explicitly published realization-side placement surface.</li>
</ul>

<h3>6.4 Asset limitation rule</h3>

<p>
A chart resource file MAY include decorative guides, placeholder text, preview traces, or design-time visual scaffolding.
However, a conforming realization family must not require that those asset-baked elements become the only path by which live chart data or live semantic chart label text is shown.
</p>

<hr/>

<h2 id="resource-posture">7. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>waveform_chart/
  plot_area/
    normal
    focused
    disabled
  x_axis/
    normal
  y_axis/
    normal
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
  <li><code>waveform_chart.plot_area.normal.svg</code></li>
  <li><code>waveform_chart.plot_area.focused.svg</code></li>
  <li><code>waveform_chart.plot_area.disabled.svg</code></li>
  <li><code>waveform_chart.x_axis.normal.svg</code> when the family uses an SVG-backed axis layer</li>
  <li><code>waveform_chart.y_axis.normal.svg</code> when the family uses an SVG-backed axis layer</li>
  <li><code>waveform_chart.frame.focused.svg</code> when focused posture is realized through a separate frame surface</li>
  <li><code>waveform_chart.label.anchor.json</code> or another explicit placement artifact for the chart label</li>
</ul>

<p>
Resources MAY be SVG-backed, host-native, toolkit-driven, or mixed.
The default family standardizes the part posture, state posture, and realization-side binding posture, not one mandatory plotting engine or one mandatory file format.
</p>

<hr/>

<h2 id="host-expectations">8. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a visible plotting region,</li>
  <li>reasonable axis presentation when enabled,</li>
  <li>visible update response when chart data changes,</li>
  <li>a readable chart label when the label is shown,</li>
  <li>host-compatible focus indication where supported.</li>
</ul>

<p>
A host SHOULD also preserve the distinction between:
</p>

<ul>
  <li>the semantic chart value owned by the class,</li>
  <li>the chart label text owned by <code>label.text</code>,</li>
  <li>the realization-side embodiment of plot, axes, label, and frame.</li>
</ul>

<p>
A host MAY approximate the realization when exact resources are unavailable, but it should preserve:
</p>

<ul>
  <li>the indicator-oriented chart identity,</li>
  <li>the stable meaning of the published public parts,</li>
  <li>the separation between semantic chart data and realization resources.</li>
</ul>

<hr/>

<h2 id="fallback-posture">9. Fallback Posture</h2>

<p>
If specialized plot resources are unavailable, a runtime MAY use:
</p>

<ul>
  <li>a host-native chart or graph surface,</li>
  <li>a simplified retained-mode plotting surface,</li>
  <li>a reduced but compatible plotting embodiment preserving the published parts.</li>
</ul>

<p>
If specialized axis or label resources are unavailable, a host MAY fall back to:
</p>

<ul>
  <li>a host-native axis rendering,</li>
  <li>a generic axis region compatible with the published visibility posture,</li>
  <li>a host-native text region or documented generic label placement rule.</li>
</ul>

<p>
Fallback is acceptable only if:
</p>

<ul>
  <li>the plot remains visibly chart-like,</li>
  <li>published public parts remain interpretable,</li>
  <li>asset omission does not turn asset-baked data or asset-baked label text into semantic truth.</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The default waveform chart realization defines one official minimal embodiment of <code>frog.widgets.waveform_chart</code> centered on plot, axis, label, and frame parts.
</p>

<p>
It realizes:
</p>

<ul>
  <li><code>plot_area</code> as the main dynamic plotted display surface,</li>
  <li><code>x_axis</code> and <code>y_axis</code> as the default axis embodiment surfaces when shown,</li>
  <li><code>label</code> as a dynamically rendered text-bearing chart label surface,</li>
  <li><code>frame</code> as an optional supporting outer surface.</li>
</ul>

<p>
Its resources may provide geometry, skins, layers, and anchors.
Its package publication may provide state maps and bindings.
Its host implementation may approximate the visuals when needed.
But the realization never becomes the semantic owner of chart value, chart label text, or chart class meaning. 
</p>
