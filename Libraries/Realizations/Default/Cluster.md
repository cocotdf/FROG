<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — Cluster Widget</h1>

<p align="center">
  <strong>Normative default realization posture for <code>frog.widgets.cluster</code></strong><br/>
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
This document defines the default official realization posture for <code>frog.widgets.cluster</code>.
</p>

<p>
The default cluster realization is intended to provide one clean, inspectable, portable embodiment of the intrinsic cluster baseline without turning one layout engine, group-box widget, or container implementation into the semantic definition of the cluster.
</p>

<p>
This realization is realization-side only.
It does not redefine cluster class law, does not invent new public members, and does not replace the semantic ownership of cluster aggregate value or optional cluster label text.
Its job is to embody already-published cluster surfaces through stable visual states, stable part mappings, and realization-side structural placement metadata where needed.
</p>

<hr/>

<h2 id="target-class">2. Target Class</h2>

<ul>
  <li><strong>target class:</strong> <code>frog.widgets.cluster</code></li>
</ul>

<p>
This realization assumes the standardized cluster posture in which:
</p>

<ul>
  <li>the cluster exposes a fixed aggregate value through <code>value</code>,</li>
  <li>the cluster may expose semantic label text through <code>label.text</code>,</li>
  <li>the cluster exposes stable public parts such as <code>content_region</code>,</li>
  <li>the realization remains downstream from that class contract.</li>
</ul>

<hr/>

<h2 id="realized-parts">3. Realized Parts</h2>

<ul>
  <li><code>root</code></li>
  <li><code>label</code> when the active class posture exposes it</li>
  <li><code>content_region</code></li>
  <li><code>frame</code> when present</li>
</ul>

<p>
The realization may internally use additional layout guides, padding regions, grouping visuals, or host-native container structures.
Those remain realization-private support structures unless they are published elsewhere as part of an explicit realization package or a future higher-level cluster contract.
</p>

<hr/>

<h2 id="standard-visual-states">4. Standard Visual States</h2>

<p>
The default cluster realization defines at least:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code> when the active class posture exposes a meaningful disabled aggregate embodiment</li>
  <li><code>focused</code> when the host supports cluster-level focus posture</li>
</ul>

<p>
These are realization-side visual states.
They do not create new persistent cluster-owned source state by themselves.
</p>

<hr/>

<h2 id="part-state-mapping">5. Part-State Mapping</h2>

<p>
The default family expects:
</p>

<ul>
  <li><code>content_region</code> to provide the main aggregate child embodiment region,</li>
  <li><code>label</code> to remain readable when the label is shown,</li>
  <li><code>frame</code>, when present, to support focused posture where applicable.</li>
</ul>

<p>
A typical minimal mapping posture is:
</p>

<ul>
  <li><code>root</code> — global layout, clipping, and outer realization region,</li>
  <li><code>label</code> — optional dynamic text-bearing cluster label surface,</li>
  <li><code>content_region</code> — structural child embodiment region,</li>
  <li><code>frame</code> — optional grouping border or focus-emphasis surface.</li>
</ul>

<p>
The default family SHOULD keep this mapping explicit enough that a machine-readable package can distinguish:
</p>

<ul>
  <li>state-sensitive visual resources,</li>
  <li>structural part bindings,</li>
  <li>child-containment or layout-support surfaces.</li>
</ul>

<hr/>

<h2 id="dynamic-surface-posture">6. Dynamic Surface Posture</h2>

<h3>6.1 Content-region posture</h3>

<p>
The <code>content_region</code> part is not just a decorative grouping box.
It is the main structural realization surface through which child widgets are visually embodied as part of the cluster.
</p>

<p>
A host interpreting this realization is expected to place and realize the declared child field set inside that region according to the published cluster structure and the active front-panel layout posture.
</p>

<p>
The realization owns how that structural region is visually embodied.
It does not become the semantic owner of the cluster aggregate value itself.
</p>

<h3>6.2 Label posture</h3>

<p>
The semantic cluster label text is not owned by this realization.
It is owned by the standardized class surface through <code>label.text</code> when that surface exists.
</p>

<p>
The role of the default realization is to define where and how that semantic label is visually embodied, not to become the source of truth for the label text itself.
</p>

<h3>6.3 Asset limitation rule</h3>

<p>
A cluster resource file MAY include decorative grouping titles, guide text, or design-time scaffolding.
However, a conforming realization family must not require that those asset-baked elements become the only path by which the live cluster aggregate structure or live semantic label text is shown.
</p>

<hr/>

<h2 id="resource-posture">7. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>cluster/
  content_region/
    normal
    disabled
    focused
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
  <li><code>cluster.content_region.normal.svg</code></li>
  <li><code>cluster.content_region.focused.svg</code></li>
  <li><code>cluster.frame.focused.svg</code></li>
  <li><code>cluster.label.anchor.json</code> or another explicit placement artifact</li>
</ul>

<p>
Resources MAY be SVG-backed, host-native, toolkit-driven, or mixed.
The default family standardizes the part posture, state posture, and realization-side binding posture, not one mandatory layout engine or one mandatory file format.
</p>

<hr/>

<h2 id="host-expectations">8. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a visible child content region,</li>
  <li>readable optional cluster label when shown,</li>
  <li>reasonable grouping or frame posture when the frame is present,</li>
  <li>host-compatible focus indication where supported.</li>
</ul>

<p>
A host SHOULD also preserve the distinction between:
</p>

<ul>
  <li>the semantic cluster aggregate value owned by the class,</li>
  <li>the optional cluster label text owned by <code>label.text</code>,</li>
  <li>the realization-side embodiment of label, content region, and frame.</li>
</ul>

<p>
A host MAY approximate the realization when exact resources are unavailable, but it should preserve:
</p>

<ul>
  <li>the structured aggregate identity of the cluster,</li>
  <li>the stable meaning of the published public parts,</li>
  <li>the separation between semantic structured value and realization resources.</li>
</ul>

<hr/>

<h2 id="fallback-posture">9. Fallback Posture</h2>

<p>
If specialized grouping or frame resources are unavailable, a runtime MAY use:
</p>

<ul>
  <li>a host-native grouping container,</li>
  <li>a simplified framed region,</li>
  <li>a reduced but compatible aggregate embodiment preserving the published parts.</li>
</ul>

<p>
If specialized label placement resources are unavailable, a host MAY fall back to:
</p>

<ul>
  <li>a host-native text region,</li>
  <li>a generic heading placement rule,</li>
  <li>another documented compatible placement surface.</li>
</ul>

<p>
Fallback is acceptable only if:
</p>

<ul>
  <li>the cluster remains visibly aggregate and structured,</li>
  <li>published public parts remain interpretable,</li>
  <li>layout-only grouping assets do not become the semantic owner of cluster meaning.</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The default cluster realization defines one official minimal embodiment of <code>frog.widgets.cluster</code> centered on label, content region, and frame parts.
</p>

<p>
It realizes:
</p>

<ul>
  <li><code>content_region</code> as the main structural child embodiment surface,</li>
  <li><code>label</code> as an optional dynamically rendered text-bearing cluster label surface,</li>
  <li><code>frame</code> as an optional supporting grouping surface.</li>
</ul>

<p>
Its resources may provide grouping visuals, layout-support surfaces, and anchors.
Its package publication may provide state maps and bindings.
Its host implementation may approximate the visuals when needed.
But the realization never becomes the semantic owner of cluster aggregate value, cluster label text, or cluster class meaning.
</p>
