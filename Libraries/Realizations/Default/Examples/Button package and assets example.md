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
  <li>an anchor map.</li>
</ul>

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
        │   ├── layer_map.json
        │   └── anchor_map.json
        ├── label/
        │   ├── normal.svg
        │   └── disabled.svg
        └── frame/
            ├── normal.svg
            └── focused.svg
</code></pre>

<hr/>

<h2 id="files-included">4. Files Included</h2>

<ul>
  <li><code>default_button_realization.wfrog.json</code></li>
  <li><code>asset_manifest.json</code></li>
  <li><code>layer_map.json</code></li>
  <li><code>anchor_map.json</code></li>
</ul>

<p>
The SVG files are represented here as paths and placeholders only.
Their visual drawing content is intentionally left out at this stage.
</p>

<hr/>

<h2 id="reading-notes">5. Reading Notes</h2>

<p>
This example is intentionally conservative:
</p>

<ul>
  <li>the package targets one class,</li>
  <li>the assets are scoped by public part,</li>
  <li>the state mapping is explicit,</li>
  <li>fallback remains explicit,</li>
  <li>the maps remain realization support, not semantic truth.</li>
</ul>

<hr/>

<h2 id="summary">6. Summary</h2>

<p>
This example is the first complete publication block for a standard widget realization package in the default family.
</p>

<p>
It is designed to serve as the reference pattern for the next families such as numeric, boolean, string, and chart.
</p>
