<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
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
  <li><a href="#strategic-scope-of-the-intrinsic-chart-baseline">3. Strategic Scope of the Intrinsic Chart Baseline</a></li>
  <li><a href="#frogwidgetswaveform_chart">4. <code>frog.widgets.waveform_chart</code></a></li>
  <li><a href="#value-and-history-posture">5. Value and History Posture</a></li>
  <li><a href="#public-object-surfaces">6. Public Object Surfaces</a></li>
  <li><a href="#standard-properties">7. Standard Properties</a></li>
  <li><a href="#standard-methods">8. Standard Methods</a></li>
  <li><a href="#standard-events">9. Standard Events</a></li>
  <li><a href="#standard-parts">10. Standard Parts</a></li>
  <li><a href="#behavior-expectations">11. Behavior Expectations</a></li>
  <li><a href="#realization-expectations">12. Realization Expectations</a></li>
  <li><a href="#diagram-interaction-posture">13. Diagram Interaction Posture</a></li>
  <li><a href="#non-goals-of-the-intrinsic-chart-baseline">14. Non-Goals of the Intrinsic Chart Baseline</a></li>
  <li><a href="#validation-expectations">15. Validation Expectations</a></li>
  <li><a href="#summary">16. Summary</a></li>
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
The intrinsic chart baseline therefore standardizes a minimal plotted-history indicator posture with:
</p>

<ul>
  <li>a stable public object surface,</li>
  <li>a stable public part model,</li>
  <li>a stable update posture,</li>
  <li>a realizable downstream embodiment.</li>
</ul>

<p>
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

<h2 id="strategic-scope-of-the-intrinsic-chart-baseline">3. Strategic Scope of the Intrinsic Chart Baseline</h2>

<p>
The intrinsic chart baseline deliberately standardizes only one minimal chart class in the primitive widget core:
</p>

<ul>
  <li><code>frog.widgets.waveform_chart</code></li>
</ul>

<p>
This is a strategic baseline decision.
It means that the first intrinsic standardized chart object is a minimal waveform-chart-style indicator with bounded visible history rather than a full family of graphing classes.
</p>

<p>
Accordingly, this document does <strong>not</strong> standardize here:
</p>

<ul>
  <li>a separate waveform graph class,</li>
  <li>a separate XY graph class,</li>
  <li>a separate intensity graph class,</li>
  <li>a complete LabVIEW-style graph ecosystem in the intrinsic core.</li>
</ul>

<p>
Those richer or more specialized chart families may be introduced later through:
</p>

<ul>
  <li>additional standardized widget classes,</li>
  <li>profiles,</li>
  <li>composite widget publication,</li>
  <li>other higher-level standardization layers.</li>
</ul>

<p>
The intrinsic core therefore adopts the following strategy:
</p>

<ul>
  <li>keep the primitive chart baseline small and portable,</li>
  <li>make its public object surface inspectable and credible,</li>
  <li>leave richer chart families for later explicit standardization rather than smuggling them into one overloaded baseline class.</li>
</ul>

<hr/>

<h2 id="frogwidgetswaveform_chart">4. <code>frog.widgets.waveform_chart</code></h2>

<h3>4.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.waveform_chart</code></li>
  <li><strong>category:</strong> <code>indicator</code></li>
  <li><strong>compatible role:</strong> <code>indicator</code></li>
</ul>

<h3>4.2 Primary value posture</h3>

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
  <li><strong>primary value:</strong> present</li>
  <li><strong>natural value participation:</strong> yes</li>
  <li><strong>user-mutable:</strong> no in the standard baseline</li>
  <li><strong>diagram-mutable:</strong> yes</li>
  <li><strong>mirrored property:</strong> <code>value</code></li>
</ul>

<hr/>

<h2 id="value-and-history-posture">5. Value and History Posture</h2>

<h3>5.1 Value posture</h3>

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

<h3>5.2 History posture</h3>

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
  <li><code>append_samples(samples)</code>, when exposed, appends a compatible ordered sample sequence,</li>
  <li><code>clear_history()</code> clears retained visible history when the chart retains it.</li>
</ul>

<h3>5.3 Axis posture</h3>

<p>
The intrinsic baseline exposes only a minimal portable axis posture through:
</p>

<ul>
  <li><code>axes.x.visible</code></li>
  <li><code>axes.y.visible</code></li>
  <li><code>axes.x.label.text</code> when axis-label surfaces are exposed</li>
  <li><code>axes.y.label.text</code> when axis-label surfaces are exposed</li>
  <li><code>axes.x.auto_scale</code> when axis auto-scaling posture is exposed</li>
  <li><code>axes.y.auto_scale</code> when axis auto-scaling posture is exposed</li>
  <li><code>axes.x.minimum</code> and <code>axes.x.maximum</code> when explicit X-range posture is exposed</li>
  <li><code>axes.y.minimum</code> and <code>axes.y.maximum</code> when explicit Y-range posture is exposed</li>
</ul>

<p>
This means the intrinsic baseline recognizes that axis visibility and a small axis control surface matter to portable chart embodiment, but it still does not standardize a full axis formatting model, legend model, cursor model, or interactive plotting framework in this document.
</p>

<h3>5.4 Label posture</h3>

<p>
The chart exposes <code>label.text</code> as a semantic label-bearing public surface.
That surface belongs to class law.
Its visual placement, clipping, or styling defaults belong downstream in realization publication rather than in the intrinsic chart class itself.
</p>

<hr/>

<h2 id="public-object-surfaces">6. Public Object Surfaces</h2>

<p>
The intrinsic waveform chart baseline is intended to expose a real object surface suitable for property-style access and method-style interaction where legal.
</p>

<p>
The baseline object surface is intentionally small but structured.
It is organized around:
</p>

<ul>
  <li>the root chart object,</li>
  <li>history-related members,</li>
  <li>axis-related members,</li>
  <li>label-related members,</li>
  <li>stable public parts for realization targeting.</li>
</ul>

<p>
This gives the chart a credible property-node and method-node posture without prematurely standardizing the entire LabVIEW graph family.
</p>

<hr/>

<h2 id="standard-properties">7. Standard Properties</h2>

<p>
The intrinsic waveform chart baseline exposes the following standard properties.
Some of them are always part of the minimal baseline.
Others are part of the standardized object surface when the corresponding chart posture is active.
</p>

<h3>7.1 Root-level properties</h3>

<ul>
  <li><code>value</code></li>
  <li><code>label.text</code></li>
  <li><code>interaction.visible</code></li>
</ul>

<h3>7.2 History properties</h3>

<ul>
  <li><code>history.capacity</code> when the chart maintains bounded visible history</li>
  <li><code>history.length</code> when the active chart posture exposes retained-history length inspection</li>
</ul>

<h3>7.3 Axis properties</h3>

<ul>
  <li><code>axes.x.visible</code></li>
  <li><code>axes.y.visible</code></li>
  <li><code>axes.x.label.text</code> when axis-label exposure is active</li>
  <li><code>axes.y.label.text</code> when axis-label exposure is active</li>
  <li><code>axes.x.auto_scale</code> when auto-scaling posture is active</li>
  <li><code>axes.y.auto_scale</code> when auto-scaling posture is active</li>
  <li><code>axes.x.minimum</code> and <code>axes.x.maximum</code> when explicit X-range posture is active</li>
  <li><code>axes.y.minimum</code> and <code>axes.y.maximum</code> when explicit Y-range posture is active</li>
</ul>

<p>
The intrinsic baseline keeps these axis properties intentionally modest.
It does not standardize here a full tick, format, cursor, legend, or plot-style object surface.
</p>

<hr/>

<h2 id="standard-methods">8. Standard Methods</h2>

<p>
The intrinsic waveform chart baseline exposes the following standard methods:
</p>

<ul>
  <li><code>append_sample(sample)</code> when the active chart posture exposes append-style update</li>
  <li><code>append_samples(samples)</code> when the active chart posture exposes batched append-style update</li>
  <li><code>clear_history()</code></li>
  <li><code>autoscale_x()</code> when X-axis auto-scaling posture is exposed</li>
  <li><code>autoscale_y()</code> when Y-axis auto-scaling posture is exposed</li>
  <li><code>autoscale_all()</code> when both axes participate in explicit auto-scaling posture</li>
  <li><code>focus()</code> when supported by the host</li>
</ul>

<p>
These methods are intentionally limited to operations that are portable, inspectable, and useful in the minimal baseline.
The intrinsic baseline does not standardize here a full chart-editing, plot-management, cursor-management, or annotation-management API.
</p>

<hr/>

<h2 id="standard-events">9. Standard Events</h2>

<p>
The intrinsic waveform chart baseline may expose the following standard events:
</p>

<ul>
  <li><code>value_rendered</code></li>
  <li><code>history_cleared</code> when exposed by the class posture</li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<p>
These events remain intentionally modest.
The intrinsic baseline does not standardize here a rich event system for cursors, annotations, plot hit-testing, or advanced user interaction.
</p>

<hr/>

<h2 id="standard-parts">10. Standard Parts</h2>

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

<h2 id="behavior-expectations">11. Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the waveform chart includes at least:
</p>

<ul>
  <li>diagram-side value updates refresh the plotted visible history or visible value region,</li>
  <li><code>append_sample(sample)</code>, when supported, extends visible history according to the class posture,</li>
  <li><code>append_samples(samples)</code>, when supported, appends an ordered batch in a compatible way,</li>
  <li><code>clear_history()</code> clears visible retained history when the chart retains it,</li>
  <li><code>autoscale_x()</code>, <code>autoscale_y()</code>, and <code>autoscale_all()</code>, when exposed, update visible axis range posture compatibly,</li>
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

<h2 id="realization-expectations">12. Realization Expectations</h2>

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
  <li>the chart class owns the semantic presence of <code>value</code>, <code>label.text</code>, axis visibility posture, and the published public parts,</li>
  <li>the realization family owns how <code>plot_area</code>, axes, label, and frame are visually embodied,</li>
  <li>assets and host widgets remain realization resources rather than semantic truth.</li>
</ul>

<hr/>

<h2 id="diagram-interaction-posture">13. Diagram Interaction Posture</h2>

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
Object-style members such as <code>history.capacity</code>, axis visibility members, or axis-range members may be accessed where the active class posture exposes them, but the intrinsic baseline does not require that ordinary chart feeding abandon the natural value path.
</p>

<p>
This gives the chart a property-node and method-node posture similar in spirit to mature graphical systems while keeping the intrinsic baseline small and portable.
</p>

<hr/>

<h2 id="non-goals-of-the-intrinsic-chart-baseline">14. Non-Goals of the Intrinsic Chart Baseline</h2>

<p>
The following are intentionally outside the scope of <code>frog.widgets.waveform_chart</code> in the intrinsic baseline:
</p>

<ul>
  <li>a full multi-plot object model,</li>
  <li>a full legend object model,</li>
  <li>a full cursor system,</li>
  <li>a full annotation system,</li>
  <li>XY graph semantics,</li>
  <li>intensity graph semantics,</li>
  <li>one mandatory plotting engine,</li>
  <li>one mandatory host interaction model for advanced plotting.</li>
</ul>

<p>
Those features may become standardized later through additional widget classes, profiles, or composite publication.
They are not part of the minimal intrinsic chart baseline defined here.
</p>

<hr/>

<h2 id="validation-expectations">15. Validation Expectations</h2>

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

<p>
Validators MAY also diagnose:
</p>

<ul>
  <li>attempts to use graph-family features such as explicit plot collections, cursors, legends, or annotations without a higher-level standardized class,</li>
  <li>confusion between indicator-oriented waveform-chart posture and richer graph-family semantics that are not yet standardized in the intrinsic core.</li>
</ul>

<hr/>

<h2 id="summary">16. Summary</h2>

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
It standardizes:
</p>

<ul>
  <li>a portable value-bearing indicator posture,</li>
  <li>a small but credible property and method surface,</li>
  <li>stable public parts,</li>
  <li>minimal history and axis posture,</li>
  <li>clear separation between class meaning and downstream realization.</li>
</ul>

<p>
Richer chart families such as waveform graphs, XY graphs, or intensity graphs remain outside the intrinsic chart core until they are explicitly standardized elsewhere.
</p>
