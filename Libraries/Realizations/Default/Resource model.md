<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization Resource Model</h1>

<p align="center">
  <strong>Normative resource model for the official <code>Default</code> widget realization family</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#resource-purpose">2. Resource Purpose</a></li>
  <li><a href="#resource-kinds">3. Resource Kinds</a></li>
  <li><a href="#resource-identifiers">4. Resource Identifiers</a></li>
  <li><a href="#resource-record-shape">5. Resource Record Shape</a></li>
  <li><a href="#path-posture">6. Path Posture</a></li>
  <li><a href="#class-and-part-scoping">7. Class and Part Scoping</a></li>
  <li><a href="#state-scoping">8. State Scoping</a></li>
  <li><a href="#resource-examples">9. Resource Examples</a></li>
  <li><a href="#validation-posture">10. Validation Posture</a></li>
  <li><a href="#summary">11. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the resource model used by the official <code>Default</code> realization family.
</p>

<p>
The resource model provides the machine-readable posture for realization resources such as SVG assets, anchor maps, and layer maps used by state-specific and part-specific realization records.
</p>

<hr/>

<h2 id="resource-purpose">2. Resource Purpose</h2>

<p>
A realization resource exists to support visual embodiment and host-facing realization.
</p>

<p>
A resource does not own:
</p>

<ul>
  <li>widget class identity,</li>
  <li>public property legality,</li>
  <li>public method legality,</li>
  <li>public event legality,</li>
  <li>public part legality.</li>
</ul>

<hr/>

<h2 id="resource-kinds">3. Resource Kinds</h2>

<p>
The default family MAY use the following resource kinds:
</p>

<ul>
  <li><code>svg</code></li>
  <li><code>vector_template</code></li>
  <li><code>anchor_map</code></li>
  <li><code>layer_map</code></li>
  <li><code>style_token_map</code></li>
</ul>

<p>
The smallest useful baseline is <code>svg</code>.
The other resource kinds are optional support artifacts.
</p>

<hr/>

<h2 id="resource-identifiers">4. Resource Identifiers</h2>

<p>
A resource SHOULD have a stable identifier.
</p>

<p>
A recommended identifier posture is:
</p>

<pre><code>&lt;class&gt;.&lt;part&gt;.&lt;state&gt;.&lt;kind&gt;</code></pre>

<p>
Examples:
</p>

<ul>
  <li><code>button.face.pressed.svg</code></li>
  <li><code>numeric_control.increment_button.pressed.svg</code></li>
  <li><code>boolean_control.state_face.normal_true.svg</code></li>
</ul>

<hr/>

<h2 id="resource-record-shape">5. Resource Record Shape</h2>

<p>
A resource record SHOULD contain:
</p>

<ul>
  <li><code>id</code></li>
  <li><code>kind</code></li>
  <li><code>path</code></li>
  <li><code>target_class</code> when applicable</li>
  <li><code>target_part</code> when applicable</li>
  <li><code>target_state</code> when applicable</li>
</ul>

<p>
Conceptually:
</p>

<pre><code>{
  "id": "button.face.pressed.svg",
  "kind": "svg",
  "path": "./assets/button/face/pressed.svg",
  "target_class": "frog.widgets.button",
  "target_part": "face",
  "target_state": "pressed"
}</code></pre>

<hr/>

<h2 id="path-posture">6. Path Posture</h2>

<p>
Paths SHOULD remain explicit and relative to the publishing package root where practical.
</p>

<p>
The package SHOULD NOT depend on implicit filename guessing alone to resolve state-specific resources.
</p>

<hr/>

<h2 id="class-and-part-scoping">7. Class and Part Scoping</h2>

<p>
Resources SHOULD be scoped to the narrowest meaningful surface:
</p>

<ul>
  <li>widget-level resource when the whole widget surface is state-specific,</li>
  <li>part-level resource when a specific public part is state-specific,</li>
  <li>family-level shared resource only when multiple realizations intentionally reuse it.</li>
</ul>

<hr/>

<h2 id="state-scoping">8. State Scoping</h2>

<p>
State scoping SHOULD be explicit in the resource record or in the state map that references the resource.
</p>

<p>
The default family avoids making state inference depend only on filenames.
</p>

<hr/>

<h2 id="resource-examples">9. Resource Examples</h2>

<pre><code>{
  "resources": [
    {
      "id": "button.face.normal.svg",
      "kind": "svg",
      "path": "./assets/button/face/normal.svg",
      "target_class": "frog.widgets.button",
      "target_part": "face",
      "target_state": "normal"
    },
    {
      "id": "button.face.pressed.svg",
      "kind": "svg",
      "path": "./assets/button/face/pressed.svg",
      "target_class": "frog.widgets.button",
      "target_part": "face",
      "target_state": "pressed"
    },
    {
      "id": "numeric_control.increment_button.pressed.svg",
      "kind": "svg",
      "path": "./assets/numeric_control/increment_button/pressed.svg",
      "target_class": "frog.widgets.numeric_control",
      "target_part": "increment_button",
      "target_state": "pressed"
    }
  ]
}</code></pre>

<hr/>

<h2 id="validation-posture">10. Validation Posture</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>duplicate resource identifiers,</li>
  <li>unknown resource kinds,</li>
  <li>missing resource paths,</li>
  <li>target part names not declared by the target class,</li>
  <li>target states not declared by the associated realization record.</li>
</ul>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
The default realization resource model defines how official realization resources are identified, scoped, and published.
</p>

<p>
It keeps assets explicit, structured, and subordinate to the realization and class layers above them.
</p>
