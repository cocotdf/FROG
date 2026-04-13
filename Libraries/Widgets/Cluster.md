<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Cluster Widget</h1>

<p align="center">
  <strong>Normative baseline for the standardized cluster widget class</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#class-defined-here">2. Class Defined Here</a></li>
  <li><a href="#frogwidgetscluster">3. <code>frog.widgets.cluster</code></a></li>
  <li><a href="#child-model">4. Child Model</a></li>
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
This document defines the intrinsic standardized baseline for the cluster widget in FROG.
</p>

<p>
The cluster is the first structured aggregate widget of the extended front-panel baseline.
Its role is to expose a fixed named aggregate of child widget surfaces as one structured public object.
</p>

<p>
The cluster is therefore not merely a decorative grouping frame and not merely a runtime-private container.
It is a structured widget class with:
</p>

<ul>
  <li>a primary aggregate value posture,</li>
  <li>a minimal but real property surface,</li>
  <li>a minimal but real method surface,</li>
  <li>a minimal but real event surface,</li>
  <li>a stable public structural part model.</li>
</ul>

<p>
The intrinsic cluster baseline is intentionally conservative.
It standardizes a fixed aggregate structure, not a full dynamic form system, docking system, or arbitrary layout engine.
</p>

<hr/>

<h2 id="class-defined-here">2. Class Defined Here</h2>

<p>
This document defines the following standardized widget class:
</p>

<ul>
  <li><code>frog.widgets.cluster</code></li>
</ul>

<hr/>

<h2 id="frogwidgetscluster">3. <code>frog.widgets.cluster</code></h2>

<h3>3.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.cluster</code></li>
  <li><strong>family:</strong> <code>structured_widget</code></li>
  <li><strong>compatible roles:</strong> <code>control</code>, <code>indicator</code>, or mixed aggregate posture according to child composition</li>
</ul>

<h3>3.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>primary value kind: fixed named aggregate value</li>
  <li>natural value participation: yes</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
</ul>

<p>
The cluster value is the structured aggregate formed by its published child field set.
The intrinsic baseline assumes a fixed field inventory rather than a runtime-variable child schema.
</p>

<h3>3.3 Standard properties</h3>

<ul>
  <li><code>value</code> — readable and writable aggregate value where legal</li>
  <li><code>label.text</code> — optional readable and writable cluster label when the active class posture exposes it</li>
  <li><code>interaction.visible</code> — readable and writable</li>
  <li><code>interaction.enabled</code> — readable and writable when the active aggregate posture exposes a meaningful enabled surface</li>
</ul>

<h3>3.4 Standard methods</h3>

<ul>
  <li><code>focus_first_child()</code> when supported by the host and active realization posture</li>
  <li><code>reset_to_default()</code> when a default aggregate value exists</li>
</ul>

<h3>3.5 Standard events</h3>

<ul>
  <li><code>value_changed</code> when the aggregate value changes</li>
  <li><code>focus_gained</code> when the cluster itself exposes focus posture</li>
  <li><code>focus_lost</code> when the cluster itself exposes focus posture</li>
</ul>

<h3>3.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code> when the active class posture exposes it</li>
  <li><code>content_region</code></li>
  <li><code>frame</code> when present</li>
</ul>

<hr/>

<h2 id="child-model">4. Child Model</h2>

<p>
The intrinsic cluster baseline assumes a fixed named child field inventory.
</p>

<p>
That means:
</p>

<ul>
  <li>the cluster exposes a stable field set,</li>
  <li>each child field corresponds to a declared child widget or child surface,</li>
  <li>the aggregate value is derived from that declared child field set.</li>
</ul>

<p>
The intrinsic baseline does not standardize here:
</p>

<ul>
  <li>runtime insertion or removal of arbitrary child fields,</li>
  <li>dynamic schema mutation,</li>
  <li>full layout management semantics,</li>
  <li>container docking systems.</li>
</ul>

<p>
Those richer surfaces may be added later by higher-level structured widget families.
</p>

<hr/>

<h2 id="standard-parts">5. Standard Parts</h2>

<p>
The cluster uses the following common stable parts:
</p>

<ul>
  <li><code>root</code> — root widget surface</li>
  <li><code>label</code> — optional cluster label surface</li>
  <li><code>content_region</code> — aggregate child layout and containment region</li>
  <li><code>frame</code> — optional outer framing surface</li>
</ul>

<p>
The child field set is part of the structural contract of the cluster, but individual child widgets remain child objects rather than decorative realization layers.
</p>

<p>
This distinction is important:
</p>

<ul>
  <li><code>content_region</code> is a public structural part,</li>
  <li>layout guides, spacing grids, clipping helpers, and decorative grouping assets belong to realization unless explicitly promoted to class law.</li>
</ul>

<hr/>

<h2 id="behavior-expectations">6. Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the cluster includes at least:
</p>

<ul>
  <li>the cluster aggregate value reflects the current values of its declared child field set,</li>
  <li>when any child field changes, the aggregate value may produce <code>value_changed</code>,</li>
  <li>cluster-level enabled or visible posture, when exposed, propagates compatibly to the aggregate embodiment,</li>
  <li>the cluster remains a structured value object rather than a purely decorative group.</li>
</ul>

<p>
The intrinsic baseline does not require the cluster to define one universal propagation algorithm for every future child family.
It requires only that the aggregate contract remain inspectable and portable.
</p>

<hr/>

<h2 id="realization-expectations">7. Realization Expectations</h2>

<p>
A conforming realization of the cluster SHOULD provide:
</p>

<ul>
  <li>a visible content region for child embodiment,</li>
  <li>optional visible label support,</li>
  <li>optional outer frame or grouping surface,</li>
  <li>part-to-visual mapping for the published parts.</li>
</ul>

<p>
The realization MAY use group-box-like, framed, flat, or host-native aggregate embodiment, provided the published public class surface remains preserved.
</p>

<p>
In particular:
</p>

<ul>
  <li>realization MAY define grouping visuals, padding regions, or layout helpers,</li>
  <li>realization MUST NOT redefine the semantic owner of the cluster aggregate value,</li>
  <li>realization MUST NOT turn layout-only grouping structures into the only source of cluster meaning.</li>
</ul>

<hr/>

<h2 id="diagram-interaction-posture">8. Diagram Interaction Posture</h2>

<p>
The cluster supports:
</p>

<ul>
  <li>natural value participation through <code>widget_value</code>,</li>
  <li>property access through <code>frog.ui.property_read</code> and <code>frog.ui.property_write</code>,</li>
  <li>method invocation where legal,</li>
  <li>event observation where legal.</li>
</ul>

<p>
When the program intent is ordinary aggregate-value dataflow, the natural value path SHOULD be preferred.
Object-style access remains available for richer structured widget interaction.
</p>

<p>
Typical legal object-style surfaces include:
</p>

<ul>
  <li><code>value</code></li>
  <li><code>label.text</code> when exposed</li>
  <li><code>interaction.visible</code></li>
  <li><code>interaction.enabled</code> when exposed</li>
</ul>

<p>
Realization-only layout guides, clipping helpers, and decorative grouping layers remain outside the public cluster class surface unless explicitly standardized elsewhere.
</p>

<hr/>

<h2 id="validation-expectations">9. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>cluster values whose shape does not match the declared child field inventory,</li>
  <li>unknown cluster members or parts,</li>
  <li>attempts to treat decorative grouping layers as semantic child fields,</li>
  <li>attempts to treat realization-only layout helpers as public class members by default.</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The cluster widget defines the intrinsic standardized fixed-aggregate structured widget baseline of FROG:
</p>

<ul>
  <li><code>frog.widgets.cluster</code></li>
</ul>

<p>
It provides the first standard structured aggregate widget surface of the extended baseline.
It exposes a real minimal object surface with properties, methods, events, and parts while keeping realization ownership and runtime-private embodiment clearly separated from class meaning.
</p>
