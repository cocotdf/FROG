<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Picture Widgets</h1>

<p align="center">
  <strong>Normative baseline for standardized picture control and picture indicator widget classes</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#classes-defined-here">2. Classes Defined Here</a></li>
  <li><a href="#common-family-posture">3. Common Family Posture</a></li>
  <li><a href="#picture-model">4. Picture Model</a></li>
  <li><a href="#interaction-model">5. Interaction Model</a></li>
  <li><a href="#frogwidgetspicture_control">6. <code>frog.widgets.picture_control</code></a></li>
  <li><a href="#frogwidgetspicture_indicator">7. <code>frog.widgets.picture_indicator</code></a></li>
  <li><a href="#common-parts">8. Common Parts</a></li>
  <li><a href="#common-behavior-expectations">9. Common Behavior Expectations</a></li>
  <li><a href="#common-realization-expectations">10. Common Realization Expectations</a></li>
  <li><a href="#diagram-interaction-posture">11. Diagram Interaction Posture</a></li>
  <li><a href="#validation-expectations">12. Validation Expectations</a></li>
  <li><a href="#summary">13. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the intrinsic standardized baseline for picture widgets in FROG.
</p>

<p>
The picture family provides the standard widget surfaces used for visible display of image-like or drawable visual content together with optional pointing, focus, and bounded interaction posture.
These classes are intentionally modest, portable, and sufficient for the first standardized free-form visual surface beyond chart, table, tree, and tab families.
</p>

<p>
The standard picture family is therefore defined here as a real object surface with:
</p>

<ul>
  <li>a primary picture value posture,</li>
  <li>a visible drawable surface posture,</li>
  <li>a minimal but real property surface,</li>
  <li>a minimal but real method surface,</li>
  <li>a minimal but real event surface,</li>
  <li>a stable public part model for realization targeting.</li>
</ul>

<p>
The intrinsic picture baseline remains intentionally conservative.
It standardizes a bounded visible picture surface first and does not attempt to standardize a full retained-scene editor, arbitrary vector authoring suite, GPU canvas API, or unrestricted drawing-program contract in the intrinsic core.
</p>

<hr/>

<h2 id="classes-defined-here">2. Classes Defined Here</h2>

<p>
This document defines the following standardized widget classes:
</p>

<ul>
  <li><code>frog.widgets.picture_control</code></li>
  <li><code>frog.widgets.picture_indicator</code></li>
</ul>

<hr/>

<h2 id="common-family-posture">3. Common Family Posture</h2>

<p>
The picture family has the following common posture:
</p>

<ul>
  <li>family: picture widget family</li>
  <li>primary value: present</li>
  <li>public value-facing surface: yes</li>
  <li>object-style access surface: yes</li>
  <li>primary value mirror property: <code>value</code></li>
  <li>viewport position surface: <code>viewport.origin</code></li>
  <li>viewport scale surface: <code>viewport.scale</code></li>
  <li>pointer position surface: <code>pointer.position</code></li>
  <li>common label property: <code>label.text</code></li>
  <li>common visibility property: <code>interaction.visible</code></li>
</ul>

<p>
The picture family follows an important architectural rule:
</p>

<ul>
  <li><code>value</code> is class-owned picture content data,</li>
  <li><code>viewport.origin</code> and <code>viewport.scale</code> are class-owned viewport metadata when the active class posture supports them,</li>
  <li><code>pointer.position</code> is class-owned transient interaction metadata when the active class posture exposes it,</li>
  <li><code>label.text</code> is class-owned semantic label text,</li>
  <li><code>picture_region</code>, <code>overlay_region</code>, and <code>frame</code> are stable public dynamic parts,</li>
  <li>the visual embodiment of raster content, vector content, overlays, pointer emphasis, clipping, and zoom posture belongs downstream to realization.</li>
</ul>

<p>
This means the intrinsic core standardizes one picture family, not one fixed drawing engine or one fixed image toolkit.
Raster-like, vector-like, or host-native mixed embodiments remain realization strategies unless promoted later into separate explicit widget classes.
</p>

<hr/>

<h2 id="picture-model">4. Picture Model</h2>

<h3>4.1 Baseline content posture</h3>

<p>
The intrinsic picture baseline represents a finite visible picture surface.
Its primary value surface is a picture payload rather than a scalar number, boolean, string, or selection index.
</p>

<p>
The exact picture payload typing remains governed by the active FROG type system and profile posture.
However, the intrinsic baseline assumes that the picture value remains semantically drawable or displayable as one visible picture surface.
</p>

<h3>4.2 Drawable-surface posture</h3>

<p>
The intrinsic picture baseline standardizes a visible picture surface rather than a full drawing-program model.
</p>

<p>
This means the intrinsic baseline does not standardize:
</p>

<ul>
  <li>arbitrary retained scene graph editing,</li>
  <li>layer authoring ownership,</li>
  <li>unbounded brush systems,</li>
  <li>general animation timelines,</li>
  <li>full CAD-like editing contracts.</li>
</ul>

<h3>4.3 Viewport posture</h3>

<p>
The intrinsic picture baseline allows a bounded viewport posture through public surfaces such as <code>viewport.origin</code> and <code>viewport.scale</code> when the active class posture exposes them.
</p>

<p>
These surfaces are public because visible framing, zoom posture, or panning posture may be semantically relevant and should not be forced into runtime-private view state.
</p>

<hr/>

<h2 id="interaction-model">5. Interaction Model</h2>

<h3>5.1 Pointer-oriented baseline</h3>

<p>
The intrinsic picture baseline allows bounded pointer-oriented interaction.
</p>

<p>
This means the intrinsic baseline may expose:
</p>

<ul>
  <li>current pointer position,</li>
  <li>focus posture,</li>
  <li>click or press events,</li>
  <li>bounded viewport changes when the class posture allows them.</li>
</ul>

<p>
This does not standardize a full freehand editing system, arbitrary drag toolchain, or generic drawing-command language.
</p>

<h3>5.2 Indicator versus control</h3>

<p>
The picture indicator is display-oriented.
The picture control may expose bounded interactive surfaces such as click observation, pointer tracking, or viewport adjustment when the active class posture allows them.
</p>

<p>
Those control-side interaction surfaces remain intentionally modest in the intrinsic baseline.
</p>

<hr/>

<h2 id="frogwidgetspicture_control">6. <code>frog.widgets.picture_control</code></h2>

<h3>6.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.picture_control</code></li>
  <li><strong>family:</strong> <code>picture_widget</code></li>
  <li><strong>compatible role:</strong> <code>control</code></li>
</ul>

<h3>6.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>natural value participation: yes</li>
  <li>user-mutable: yes in the standard portable posture when the active class posture allows bounded interactive updates</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
</ul>

<h3>6.3 Standard properties</h3>

<ul>
  <li><code>value</code> — readable and writable picture value</li>
  <li><code>viewport.origin</code> — readable and writable viewport origin when supported</li>
  <li><code>viewport.scale</code> — readable and writable viewport scale when supported</li>
  <li><code>pointer.position</code> — readable current pointer position when available</li>
  <li><code>label.text</code> — readable and writable</li>
  <li><code>interaction.enabled</code> — readable and writable</li>
  <li><code>interaction.visible</code> — readable and writable</li>
</ul>

<p>
These properties define the minimum public object surface of the intrinsic picture control.
They do not expose realization-private GPU buffers, host-native scene handles, private overlay caches, or toolkit-private image objects as if they were public class members.
</p>

<h3>6.4 Standard methods</h3>

<ul>
  <li><code>focus()</code></li>
  <li><code>set_viewport_origin(origin)</code> when viewport origin is supported</li>
  <li><code>set_viewport_scale(scale)</code> when viewport scale is supported</li>
  <li><code>reset_viewport()</code> when viewport posture is supported</li>
</ul>

<p>
The baseline method surface is intentionally small.
It exists to guarantee that the picture control remains a real visual object with bounded interaction and viewport action surfaces rather than a passive painted bitmap shell.
</p>

<h3>6.5 Standard events</h3>

<ul>
  <li><code>value_changed</code></li>
  <li><code>pointer_moved</code></li>
  <li><code>clicked</code></li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<p>
The baseline allows both value and pointer-oriented events because visible content mutation and pointer interaction are related but must remain distinguishable.
</p>

<h3>6.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>picture_region</code></li>
  <li><code>overlay_region</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The <code>picture_region</code> part is the public dynamic visible picture surface.
The <code>overlay_region</code> part is the public dynamic surface for bounded host-visible overlays such as focus emphasis, pointer emphasis, or helper marks when the active realization uses them.
Their semantic meaning belongs to the class through <code>value</code>, <code>viewport.*</code>, and <code>pointer.position</code>.
Their visual placement and embodiment belong to realization.
</p>

<hr/>

<h2 id="frogwidgetspicture_indicator">7. <code>frog.widgets.picture_indicator</code></h2>

<h3>7.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.picture_indicator</code></li>
  <li><strong>family:</strong> <code>picture_widget</code></li>
  <li><strong>compatible role:</strong> <code>indicator</code></li>
</ul>

<h3>7.2 Primary value posture</h3>

<ul>
  <li>primary value: present</li>
  <li>natural value participation: yes</li>
  <li>user-mutable: no in the standard portable posture</li>
  <li>diagram-mutable: yes</li>
  <li>mirrored property: <code>value</code></li>
</ul>

<h3>7.3 Standard properties</h3>

<ul>
  <li><code>value</code> — readable and writable for diagram/runtime update surfaces where legal</li>
  <li><code>viewport.origin</code> — readable and writable where legal and supported</li>
  <li><code>viewport.scale</code> — readable and writable where legal and supported</li>
  <li><code>label.text</code> — readable and writable</li>
  <li><code>interaction.visible</code> — readable and writable</li>
</ul>

<p>
The indicator remains a real object even though it is display-oriented.
Its public surface is intentionally smaller than that of the control.
</p>

<h3>7.4 Standard methods</h3>

<ul>
  <li><code>focus()</code> when supported by the host</li>
  <li><code>set_viewport_origin(origin)</code> where diagram-side indicator update surfaces are legal</li>
  <li><code>set_viewport_scale(scale)</code> where diagram-side indicator update surfaces are legal</li>
  <li><code>reset_viewport()</code> when viewport posture is supported</li>
</ul>

<h3>7.5 Standard events</h3>

<ul>
  <li><code>value_rendered</code></li>
  <li><code>viewport_rendered</code></li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<h3>7.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>picture_region</code></li>
  <li><code>overlay_region</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The indicator <code>picture_region</code> and <code>overlay_region</code> parts remain public dynamic display surfaces.
They are not merely decorative skin regions.
</p>

<hr/>

<h2 id="common-parts">8. Common Parts</h2>

<p>
The picture family uses the following common stable parts:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>picture_region</code></li>
  <li><code>overlay_region</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
This distinction is important:
</p>

<ul>
  <li><code>picture_region</code> is a public part of the class model,</li>
  <li><code>overlay_region</code> is a public part of the class model,</li>
  <li>private helper layers, raster buffers, clipping paths, pointer cursors, zoom helpers, and toolkit-native rendering containers used to embody them belong to realization unless explicitly promoted to class law.</li>
</ul>

<hr/>

<h2 id="common-behavior-expectations">9. Common Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the picture family includes at least:
</p>

<ul>
  <li>the primary value remains displayable as a visible picture surface,</li>
  <li>viewport posture, when present, remains consistent with the current picture value and visible bounds,</li>
  <li>picture controls accept user-originated pointer interaction only when enabled,</li>
  <li>visible content mutation and viewport changes remain distinguishable at the public object surface,</li>
  <li>indicator realizations may emit <code>value_rendered</code> or <code>viewport_rendered</code> when their visible state is refreshed.</li>
</ul>

<p>
The family also preserves the distinction between:
</p>

<ul>
  <li>semantic picture value owned by <code>value</code>,</li>
  <li>viewport metadata owned by <code>viewport.origin</code> and <code>viewport.scale</code>,</li>
  <li>pointer metadata owned by <code>pointer.position</code> when exposed,</li>
  <li>semantic label text owned by <code>label.text</code>,</li>
  <li>dynamic public picture surfaces exposed through <code>picture_region</code> and <code>overlay_region</code>,</li>
  <li>downstream visual embodiment owned by realization.</li>
</ul>

<p>
Hover posture, arbitrary drawing tools, freehand editing, scene layering, and animation systems remain realization or higher-level extension concerns unless explicitly promoted to additional public class surfaces.
</p>

<hr/>

<h2 id="common-realization-expectations">10. Common Realization Expectations</h2>

<p>
A conforming realization of the picture family SHOULD provide:
</p>

<ul>
  <li>a visible drawable picture surface,</li>
  <li>bounded visible overlay support when overlays are used,</li>
  <li>optional visible label support,</li>
  <li>reasonable focus indication for controls where appropriate,</li>
  <li>part-to-visual mapping for the published parts.</li>
</ul>

<p>
The realization MAY be raster-backed, vector-backed, mixed, or host-native, provided that the published public class surface remains preserved.
</p>

<p>
In particular:
</p>

<ul>
  <li>realization MAY define picture assets, overlay assets, focus layers, clipping layers, or zoom affordances,</li>
  <li>realization MUST NOT redefine the semantic owner of <code>value</code>, <code>viewport.origin</code>, <code>viewport.scale</code>, <code>pointer.position</code>, or <code>label.text</code>,</li>
  <li>realization MUST NOT make baked images, host-private buffers, or decorative assets the only semantic source of visible picture meaning.</li>
</ul>

<hr/>

<h2 id="diagram-interaction-posture">11. Diagram Interaction Posture</h2>

<p>
The picture family supports:
</p>

<ul>
  <li>natural value participation through <code>widget_value</code>,</li>
  <li>property access through <code>frog.ui.property_read</code> and <code>frog.ui.property_write</code>,</li>
  <li>method invocation where legal,</li>
  <li>event observation where legal.</li>
</ul>

<p>
When the program intent is ordinary picture dataflow, the natural value path SHOULD be preferred.
Object-style access remains available for richer widget interaction.
</p>

<p>
Typical legal object-style surfaces include:
</p>

<ul>
  <li><code>value</code></li>
  <li><code>viewport.origin</code></li>
  <li><code>viewport.scale</code></li>
  <li><code>pointer.position</code></li>
  <li><code>label.text</code></li>
  <li><code>interaction.enabled</code></li>
  <li><code>interaction.visible</code></li>
</ul>

<p>
Realization-only hover layers, private scene handles, GPU helpers, clipping helpers, and asset helpers remain outside the public picture class surface unless explicitly standardized elsewhere.
</p>

<hr/>

<h2 id="validation-expectations">12. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>role/class mismatches,</li>
  <li>invalid viewport surfaces when the active class posture does not support viewport behavior,</li>
  <li>attempts to write user-edit surfaces on indicator-only classes where forbidden,</li>
  <li>unknown picture family members or parts,</li>
  <li>attempts to treat realization-only overlay, clipping, pointer-helper, zoom-helper, or placement surfaces as public class members by default.</li>
</ul>

<hr/>

<h2 id="summary">13. Summary</h2>

<p>
The picture widget family defines the intrinsic standardized visible picture-surface widget baseline of FROG:
</p>

<ul>
  <li><code>frog.widgets.picture_control</code></li>
  <li><code>frog.widgets.picture_indicator</code></li>
</ul>

<p>
These classes provide the first standard portable visible generic picture surfaces beyond chart and structured navigation widgets.
They expose a real minimal object surface with properties, methods, events, and parts while keeping realization ownership and runtime-private embodiment clearly separated from class meaning.
</p>
