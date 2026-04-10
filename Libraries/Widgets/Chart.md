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
  <li><a href="#value-and-history-posture">4. Value and History Posture</a></li>
  <li><a href="#standard-parts">5. Standard Parts</a></li>
  <li><a href="#behavior-expectations">6. Behavior Expectations</a></li>
  <li><a href="#realization-expectations">7. Realization Expectations</a></li>
  <li><a href="#diagram-interaction-posture">8. Diagram Interaction Posture</a></li>
  <li><a href="#validation-expectations">9. Validation Expectations</a></li>
  <li><a href="#summary">10. Summary</a></li>
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

<p>
The intrinsic chart baseline therefore standardizes a minimal plotted-history indicator posture with a stable public part model, a stable update posture, and a realizable downstream embodiment.
It does not attempt to standardize a full legend, cursor, annotation, multi-trace, or analysis surface in the intrinsic core.
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
The exact active type used by a program may depend on the active type system and on higher-level normalization elsewhere in the repository.
However, the intrinsic standardized baseline assumes a chart-compatible ordered numeric sample sequence rather than an unrestricted plotting payload.
</p>

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
  <li><code>append_sample(sample)</code> when the active chart posture exposes append-style update</li>
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
  <li><code>frame</code> when present</li>
</ul>

<hr/>

<h2 id="value-and-history-posture">4. Value and History Posture</h2>

<h3>4.1 Value posture</h3>

<p>
The intrinsic chart baseline is a value-carrying indicator, but not a general-purpose graph object model.
Its public <code>value</code> surface represents charted numeric history or chart-compatible numeric sequence content.
</p>

<p>
The intrinsic baseline deliberately does not standardize here:
</p>

<ul>
  <li>multiple named plots,</li>
  <li>independent plot styles,</li>
  <li>explicit cursor collections,</li>
  <li>legend management,</li>
  <li>annotation collections,</li>
  <li>arbitrary mixed trace payloads.</li>
</ul>

<p>
Those richer surfaces may be introduced later through higher-level standardized classes, profiles, or composite publication.
They are not part of <code>frog.widgets.waveform_chart</code> itself.
</p>

<h3>4.2 History posture</h3>

<p>
The intrinsic chart baseline may operate in a visible-history posture.
When such posture is active, <code>history.capacity</code> defines the bounded retained visible history surface of the class when that surface is exposed.
</p>

<p>
The intrinsic baseline does not require one universal internal history algorithm.
It requires only that bounded history behavior, when exposed, remain portable enough that:
</p>

<ul>
  <li>diagram-side updates produce a compatible visible chart update,</li>
  <li><code>append_sample(sample)</code> behaves as an append-oriented update when exposed,</li>
  <li><code>clear_history()</code> clears retained visible history when the chart retains it.</li>
</ul>

<h3>4.3 Axis posture</h3>

<p>
The intrinsic baseline exposes only a minimal portable axis posture through:
</p>

<ul>
  <li><code>axes.x.visible</code></li>
  <li><code>axes.y.visible</code></li>
</ul>

<p>
This means the intrinsic baseline recognizes that axis visibility matters to portable chart embodiment, but it does not yet standardize a full axis configuration model for scaling, ticks, labels, formatting, or interaction.
Those richer surfaces remain downstream from the intrinsic core unless standardized elsewhere.
</p>

<h3>4.4 Label posture</h3>

<p>
The chart exposes <code>label.text</code> as a semantic label-bearing public surface.
That surface belongs to class law.
Its visual placement, clipping, or styling defaults belong downstream in realization publication rather than in the intrinsic chart class itself.
</p>

<hr/>

<h2 id="standard-parts">5. Standard Parts</h2>

<p>
The chart family uses the following stable public parts:
</p>

<ul>
  <li><code>root</code> — root widget surface</li>
  <li><code>plot_area</code> — main plotted data region</li>
  <li><code>axes</code> — aggregate axes surface when used</li>
  <li><code>x_axis</code> — horizontal axis surface</li>
  <li><code>y_axis</code> — vertical axis surface</li>
  <li><code>label</code> — optional semantic label surface</li>
  <li><code>frame</code> — optional framing surface</li>
</ul>

<p>
These parts are intentionally minimal.
The intrinsic baseline does not attempt to standardize a full cursor, legend, marker, multi-trace, or annotation system.
</p>

<p>
The presence of these parts means the standardized class exposes stable public realization targets.
It does not mean that every host must realize them pixel-identically or through the same toolkit structure.
</p>

<hr/>

<h2 id="behavior-expectations">6. Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the waveform chart includes at least:
</p>

<ul>
  <li>diagram-side value updates refresh the plotted visible history or visible value region,</li>
  <li><code>append_sample(sample)</code>, when supported, extends visible history according to the class posture,</li>
  <li><code>clear_history()</code> clears visible retained history when the chart retains it,</li>
  <li>visible rendering refresh may emit <code>value_rendered</code>.</li>
</ul>

<p>
The intrinsic chart baseline remains intentionally conservative.
It standardizes a minimal plotted-history posture, not a complete plotting framework.
</p>

<p>
The intrinsic baseline also does not require user-originated data editing.
The chart is indicator-oriented in the standardized baseline, even though a host may still expose focus posture or host-native navigation affordances.
</p>

<hr/>

<h2 id="realization-expectations">7. Realization Expectations</h2>

<p>
A conforming realization of the waveform chart SHOULD provide:
</p>

<ul>
  <li>a visible plot area,</li>
  <li>optional visible axes,</li>
  <li>a readable label surface when the label is shown,</li>
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

<p>
In particular:
</p>

<ul>
  <li>the chart class owns the semantic presence of <code>value</code>, <code>label.text</code>, and the published public parts,</li>
  <li>the realization family owns how <code>plot_area</code>, axes, label, and frame are visually embodied,</li>
  <li>assets and host widgets remain realization resources rather than semantic truth.</li>
</ul>

<hr/>

<h2 id="diagram-interaction-posture">8. Diagram Interaction Posture</h2>

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

<p>
Object-style members such as <code>history.capacity</code> or axis visibility members may be accessed where the active class posture exposes them, but the intrinsic baseline does not require that ordinary chart feeding abandon the natural value path.
</p>

<hr/>

<h2 id="validation-expectations">9. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>role/class mismatches,</li>
  <li>attempts to use unsupported chart members or parts,</li>
  <li>chart value types that are incompatible with the active chart baseline posture,</li>
  <li>attempts to treat the minimal intrinsic chart as a full unrestricted plotting system without an explicit higher-level class or profile,</li>
  <li>attempts to treat realization-private chart surfaces as if they were intrinsic public class members by default.</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The waveform chart defines the first richer indicator-oriented display widget of the intrinsic FROG baseline:
</p>

<ul>
  <li><code>frog.widgets.waveform_chart</code></li>
</ul>

<p>
Its role is to provide a minimal but credible plotted-history widget class that can participate in serious examples and future runtime interpretation without prematurely standardizing a complete plotting ecosystem.
</p>

<p>
It standardizes a portable value-bearing indicator with stable public parts and minimal history posture, while leaving detailed chart embodiment, placement, and styling machinery downstream in realization publication.
</p>
