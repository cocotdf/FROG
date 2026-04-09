<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Chart Widget</h1>

<p align="center">
  <strong>Normative baseline for the standardized waveform chart widget class</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#class-defined-here">2. Class Defined Here</a></li>
  <li><a href="#frogwidgetswaveform_chart">3. <code>frog.widgets.waveform_chart</code></a></li>
  <li><a href="#standard-parts">4. Standard Parts</a></li>
  <li><a href="#behavior-expectations">5. Behavior Expectations</a></li>
  <li><a href="#realization-expectations">6. Realization Expectations</a></li>
  <li><a href="#diagram-interaction-posture">7. Diagram Interaction Posture</a></li>
  <li><a href="#validation-expectations">8. Validation Expectations</a></li>
  <li><a href="#summary">9. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the intrinsic standardized baseline for a minimal waveform chart widget in FROG.
</p>

<p>
The chart baseline is intentionally conservative.
Its role is not to define a full industrial graphing ecosystem from the start.
Its role is to provide one first richer display widget that goes beyond scalar text and scalar state display while still remaining small enough to implement portably.
</p>

<hr/>

<h2 id="class-defined-here">2. Class Defined Here</h2>

<p>
This document defines the following standardized widget class:
</p>

<ul>
  <li><code>frog.widgets.waveform_chart</code></li>
</ul>

<hr/>

<h2 id="frogwidgetswaveform_chart">3. <code>frog.widgets.waveform_chart</code></h2>

<h3>3.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.waveform_chart</code></li>
  <li><strong>category:</strong> <code>indicator</code></li>
  <li><strong>compatible role:</strong> <code>indicator</code></li>
</ul>

<h3>3.2 Primary value posture</h3>

<p>
The intrinsic waveform chart baseline is an indicator-oriented class with a primary value posture representing charted data.
</p>

<p>
The exact portable value carrier MAY be:
</p>

<ul>
  <li>a sequence of numeric samples,</li>
  <li>an array of scalar numeric values,</li>
  <li>another explicitly standardized chart-compatible sample container under the active type system.</li>
</ul>

<p>
For the intrinsic baseline, the minimum required portable posture is:
</p>

<ul>
  <li>primary value: present</li>
  <li>natural value participation: yes</li>
  <li>user-mutable: no in the standard baseline</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
</ul>

<h3>3.3 Standard properties</h3>

<ul>
  <li><code>value</code></li>
  <li><code>label.text</code></li>
  <li><code>interaction.visible</code></li>
  <li><code>history.capacity</code> when the chart maintains bounded visible history</li>
  <li><code>axes.x.visible</code></li>
  <li><code>axes.y.visible</code></li>
</ul>

<h3>3.4 Standard methods</h3>

<ul>
  <li><code>append_sample(sample)</code> when the active realization and class posture expose append-style update</li>
  <li><code>clear_history()</code></li>
  <li><code>focus()</code> when supported by the host</li>
</ul>

<h3>3.5 Standard events</h3>

<ul>
  <li><code>value_rendered</code></li>
  <li><code>history_cleared</code> when exposed by the class posture</li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<h3>3.6 Standard parts</h3>

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

<h2 id="standard-parts">4. Standard Parts</h2>

<p>
The chart family uses the following stable public parts:
</p>

<ul>
  <li><code>root</code> — root widget surface</li>
  <li><code>plot_area</code> — main plotted data region</li>
  <li><code>axes</code> — aggregate axes surface when used</li>
  <li><code>x_axis</code> — horizontal axis surface</li>
  <li><code>y_axis</code> — vertical axis surface</li>
  <li><code>label</code> — optional label surface</li>
  <li><code>frame</code> — optional framing surface</li>
</ul>

<p>
These parts are intentionally minimal.
The intrinsic baseline does not attempt to standardize a full cursor, legend, marker, multi-trace, or annotation system.
</p>

<hr/>

<h2 id="behavior-expectations">5. Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the waveform chart includes at least:
</p>

<ul>
  <li>diagram-side value updates refresh the plotted visible history or visible value region,</li>
  <li><code>append_sample</code>, when supported, extends visible history according to the class posture,</li>
  <li><code>clear_history()</code> clears visible retained history when the chart retains it,</li>
  <li>visible rendering refresh may emit <code>value_rendered</code>.</li>
</ul>

<p>
The intrinsic chart baseline remains intentionally conservative.
It standardizes a minimal plotted-history posture, not a complete plotting framework.
</p>

<hr/>

<h2 id="realization-expectations">6. Realization Expectations</h2>

<p>
A conforming realization of the waveform chart SHOULD provide:
</p>

<ul>
  <li>a visible plot area,</li>
  <li>optional visible axes,</li>
  <li>reasonable visual response to value or history updates,</li>
  <li>part-to-visual mapping for the published parts.</li>
</ul>

<p>
Different runtimes MAY realize the chart differently, including:
</p>

<ul>
  <li>host-native plotting widgets,</li>
  <li>custom retained-mode plotting surfaces,</li>
  <li>SVG-assisted or vector-assisted realization layers.</li>
</ul>

<p>
Such differences are acceptable provided that the published class meaning remains preserved.
</p>

<hr/>

<h2 id="diagram-interaction-posture">7. Diagram Interaction Posture</h2>

<p>
The waveform chart supports:
</p>

<ul>
  <li>natural value participation through <code>widget_value</code>,</li>
  <li>object-style property access where legal,</li>
  <li>method invocation where legal,</li>
  <li>event observation where legal.</li>
</ul>

<p>
The natural value path remains the preferred representation for ordinary chart-data feeding in the intrinsic baseline.
</p>

<hr/>

<h2 id="validation-expectations">8. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>role/class mismatches,</li>
  <li>attempts to use unsupported chart members or parts,</li>
  <li>chart value types that are incompatible with the active chart baseline posture,</li>
  <li>attempts to treat the minimal intrinsic chart as a full unrestricted plotting system without an explicit higher-level class or profile.</li>
</ul>

<hr/>

<h2 id="summary">9. Summary</h2>

<p>
The waveform chart defines the first richer indicator-oriented display widget of the intrinsic FROG baseline:
</p>

<ul>
  <li><code>frog.widgets.waveform_chart</code></li>
</ul>

<p>
Its role is to provide a minimal but credible plotted-history widget class that can participate in serious examples and future runtime interpretation without prematurely standardizing a complete plotting ecosystem.
</p>
