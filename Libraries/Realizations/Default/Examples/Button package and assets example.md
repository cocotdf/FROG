<p align="center">
  <img src="../../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Example — Default Button Package and Asset Tree</h1>

<p align="center">
  <strong>Complete illustrative example of a default button realization package together with a simulated asset tree</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#purpose">2. Purpose</a></li>
  <li><a href="#simulated-tree">3. Simulated Tree</a></li>
  <li><a href="#files-included">4. Files Included</a></li>
  <li><a href="#reading-notes">5. Reading Notes</a></li>
  <li><a href="#summary">6. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document provides a complete illustrative example for the default realization of <code>frog.widgets.button</code>.
</p>

<p>
It combines:
</p>

<ul>
  <li>a machine-readable <code>.wfrog</code> realization package,</li>
  <li>a normalized asset tree,</li>
  <li>a resource manifest,</li>
  <li>a layer map,</li>
  <li>an anchor publication resource for dynamic label placement.</li>
</ul>

<p>
The example is intentionally small, but it is structured to preserve the doctrinal split between widget semantic law, realization publication, asset resources, and runtime rendering responsibility.
</p>

<hr/>

<h2 id="purpose">2. Purpose</h2>

<p>
The purpose of this example is to show one coherent end-to-end publication unit for a standard widget realization without confusing:
</p>

<ul>
  <li>class law,</li>
  <li>realization-family posture,</li>
  <li>package publication,</li>
  <li>asset files,</li>
  <li>runtime implementation.</li>
</ul>

<p>
In particular, this example preserves the distinction between:
</p>

<ul>
  <li>the semantic button label owned by the widget class through <code>label.text</code>,</li>
  <li>the realization-side placement surface used to display that text,</li>
  <li>the state-sensitive visual resources used for the button face,</li>
  <li>optional decorative or structural layers such as a frame,</li>
  <li>the runtime-side responsibility for drawing live text into the published placement surface.</li>
</ul>

<hr/>

<h2 id="simulated-tree">3. Simulated Tree</h2>

<pre><code>Libraries/Realizations/Default/Examples/ButtonPackage/
├── default_button_realization.wfrog.json
└── assets/
    └── button/
        ├── asset_manifest.json
        ├── face/
        │   ├── normal.svg
        │   ├── disabled.svg
        │   ├── focused.svg
        │   ├── pressed.svg
        │   └── layer_map.json
        ├── anchors/
        │   └── label.json
        └── frame/
            ├── normal.svg
            └── focused.svg
</code></pre>

<p>
This tree intentionally does <strong>not</strong> publish state-specific SVG assets for <code>label</code>.
The button label remains a dynamic public surface, so the realization publishes a placement surface for that label rather than baking final text ownership into SVG files.
</p>

<hr/>

<h2 id="files-included">4. Files Included</h2>

<ul>
  <li><code>default_button_realization.wfrog.json</code></li>
  <li><code>asset_manifest.json</code></li>
  <li><code>layer_map.json</code></li>
  <li><code>label.json</code> under <code>anchors/</code></li>
</ul>

<p>
The SVG files are represented here as paths and placeholders only.
Their visual drawing content is intentionally left out at this stage.
</p>

<p>
The expected role of each file is as follows:
</p>

<ul>
  <li><code>default_button_realization.wfrog.json</code> publishes the machine-readable realization package, including target class, parts, bindings, state maps, and fallbacks,</li>
  <li><code>asset_manifest.json</code> provides a compact inventory of the resources shipped with this example package,</li>
  <li><code>layer_map.json</code> describes how visual face layers are composed or interpreted when the runtime loads face resources,</li>
  <li><code>anchors/label.json</code> publishes the placement surface used by the runtime to render live <code>label.text</code>.</li>
</ul>

<hr/>

<h2 id="reading-notes">5. Reading Notes</h2>

<p>
This example is intentionally conservative:
</p>

<ul>
  <li>the package targets one class,</li>
  <li>the assets are scoped by structural realization role,</li>
  <li>the state mapping is explicit for the main state-driven visual part,</li>
  <li>fallback remains explicit,</li>
  <li>the maps remain realization support, not semantic truth.</li>
</ul>

<p>
The most important architectural point is that <code>face</code> and <code>label</code> do not follow the same publication posture:
</p>

<ul>
  <li><code>face</code> is a state-driven visual part, so it is represented through state-sensitive SVG resources,</li>
  <li><code>label</code> is a semantic public text-bearing part, so it is represented through a placement resource rather than through baked final text assets.</li>
</ul>

<p>
This means that:
</p>

<ul>
  <li>the widget class remains the owner of the semantic text surface,</li>
  <li>the realization remains the owner of the placement geometry and visual embodiment,</li>
  <li>the runtime remains responsible for rendering the live text using the published placement surface,</li>
  <li>the asset tree does not silently become the owner of button-text semantics.</li>
</ul>

<p>
The optional <code>frame/</code> subtree is shown here to illustrate that a realization family may publish additional visual layers without changing widget-class meaning.
Whether a given runtime chooses to materialize <code>frame</code> as a distinct host layer or flatten it into a composed drawing pipeline remains an implementation matter, provided that the published realization contract is respected.
</p>

<hr/>

<h2 id="summary">6. Summary</h2>

<p>
This example provides a complete first publication block for a standard widget realization package in the default family.
</p>

<p>
It demonstrates a coherent asset-publication posture in which:
</p>

<ul>
  <li>state-sensitive SVG resources are used for the button face,</li>
  <li>dynamic label placement is published through an anchor resource,</li>
  <li>machine-readable package publication and concrete assets remain aligned,</li>
  <li>semantic ownership does not collapse into the asset tree.</li>
</ul>

<p>
It is designed to serve as the reference pattern for the next families such as numeric, boolean, string, and chart, especially when those widgets also expose dynamic public text or other dynamic public surfaces that must remain portable across runtimes.
</p>
