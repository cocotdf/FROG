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
  <li><a href="#resource-posture">6. Resource Posture</a></li>
  <li><a href="#host-expectations">7. Host Expectations</a></li>
  <li><a href="#fallback-posture">8. Fallback Posture</a></li>
  <li><a href="#summary">9. Summary</a></li>
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

<hr/>

<h2 id="target-class">2. Target Class</h2>

<ul>
  <li><strong>target class:</strong> <code>frog.widgets.waveform_chart</code></li>
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
  <li><code>frame</code></li>
</ul>

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

<hr/>

<h2 id="part-state-mapping">5. Part-State Mapping</h2>

<p>
The default family expects:
</p>

<ul>
  <li><code>plot_area</code> to provide the main plotted display region,</li>
  <li><code>x_axis</code> and <code>y_axis</code> to provide visible axis surfaces when enabled,</li>
  <li><code>label</code> to remain readable,</li>
  <li><code>frame</code> to support focused posture where applicable.</li>
</ul>

<hr/>

<h2 id="resource-posture">6. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>waveform_chart/
  plot_area/
    normal
    focused
  x_axis/
    normal
  y_axis/
    normal
  frame/
    normal
    focused
</code></pre>

<hr/>

<h2 id="host-expectations">7. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a visible plotting region,</li>
  <li>reasonable axis presentation when enabled,</li>
  <li>visible update response when chart data changes,</li>
  <li>host-compatible focus indication where supported.</li>
</ul>

<hr/>

<h2 id="fallback-posture">8. Fallback Posture</h2>

<p>
If specialized plot resources are unavailable, a runtime MAY use:
</p>

<ul>
  <li>a host-native chart or graph surface,</li>
  <li>a simplified retained-mode plotting surface,</li>
  <li>a reduced but compatible plotting embodiment preserving the published parts.</li>
</ul>

<hr/>

<h2 id="summary">9. Summary</h2>

<p>
The default waveform chart realization defines one official minimal embodiment of <code>frog.widgets.waveform_chart</code> centered on plot, axis, label, and frame parts.
</p>
