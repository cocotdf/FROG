<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization Package</h1>

<p align="center">
  <strong>Normative machine-readable publication posture for the official <code>Default</code> widget realization family</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#purpose">2. Purpose</a></li>
  <li><a href="#relationship-with-other-layers">3. Relationship with Other Layers</a></li>
  <li><a href="#package-kind">4. Package Kind</a></li>
  <li><a href="#top-level-structure">5. Top-Level Structure</a></li>
  <li><a href="#package-identity">6. Package Identity</a></li>
  <li><a href="#target-class-declarations">7. Target Class Declarations</a></li>
  <li><a href="#realization-records">8. Realization Records</a></li>
  <li><a href="#resource-manifests">9. Resource Manifests</a></li>
  <li><a href="#state-maps">10. State Maps</a></li>
  <li><a href="#part-bindings">11. Part Bindings</a></li>
  <li><a href="#host-hints">12. Host Hints</a></li>
  <li><a href="#minimal-json-outline">13. Minimal JSON Outline</a></li>
  <li><a href="#validation-posture">14. Validation Posture</a></li>
  <li><a href="#summary">15. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the machine-readable publication posture for the official <code>Default</code> widget realization family.
</p>

<p>
Its role is to specify how the default family may be published through widget-oriented package artifacts without making those artifacts the owner of widget semantics.
</p>

<p>
The default family package publishes realization-side information such as:
</p>

<ul>
  <li>which widget classes are targeted,</li>
  <li>which parts are realized,</li>
  <li>which visual states are supported,</li>
  <li>which resources are available,</li>
  <li>how parts and states map to those resources,</li>
  <li>which host-facing hints are associated with the family.</li>
</ul>

<hr/>

<h2 id="purpose">2. Purpose</h2>

<p>
The purpose of the default realization package is to make the standard realization family explicit, inspectable, and machine-readable.
</p>

<p>
Without this layer:
</p>

<ul>
  <li>the official realization family would remain purely descriptive,</li>
  <li>state-specific resources would be hard to validate consistently,</li>
  <li>runtime families would lack a stable machine-readable realization target,</li>
  <li>assets would drift toward ad hoc organization.</li>
</ul>

<hr/>

<h2 id="relationship-with-other-layers">3. Relationship with Other Layers</h2>

<p>
The following separation is mandatory:
</p>

<pre><code>Libraries/Widgets/
    -&gt; standard widget classes

Libraries/Realizations/Default/
    -&gt; official realization-family documentation

Default realization package
    -&gt; machine-readable publication of that family

assets
    -&gt; resource files used by the package

runtime implementation
    -&gt; host execution of the package
</code></pre>

<p>
Therefore:
</p>

<ul>
  <li>the package MUST NOT redefine widget class law,</li>
  <li>the package MUST NOT create undocumented public widget members,</li>
  <li>the package MAY publish state maps, part bindings, and resource references,</li>
  <li>the runtime MAY interpret or approximate the package while preserving class meaning.</li>
</ul>

<hr/>

<h2 id="package-kind">4. Package Kind</h2>

<p>
The default realization family SHOULD be published as a <code>widget_realization_library</code> package.
</p>

<p>
That package kind is appropriate because the package publishes:
</p>

<ul>
  <li>reusable realization resources,</li>
  <li>reusable state mappings,</li>
  <li>reusable part bindings,</li>
  <li>reusable host-facing realization metadata.</li>
</ul>

<hr/>

<h2 id="top-level-structure">5. Top-Level Structure</h2>

<p>
A machine-readable package for the default family SHOULD follow this conceptual outline:
</p>

<pre><code>{
  "wfrog_version": "...",
  "package_kind": "widget_realization_library",
  "package": { ... },
  "imports": [ ... ],
  "exports": { ... },
  "targets": [ ... ],
  "realizations": [ ... ],
  "resources": [ ... ]
}
</code></pre>

<p>
The package MAY also contain:
</p>

<ul>
  <li><code>host_hints</code>,</li>
  <li><code>diagnostics</code>,</li>
  <li><code>examples</code>,</li>
  <li><code>fallbacks</code>.</li>
</ul>

<hr/>

<h2 id="package-identity">6. Package Identity</h2>

<p>
The package identity SHOULD make the realization family explicit and stable.
</p>

<p>
A typical identity posture may be:
</p>

<ul>
  <li><code>package.id</code> — <code>frog.realizations.default</code></li>
  <li><code>package.name</code> — <code>FROG Default Realization Family</code></li>
  <li><code>package.namespace</code> — <code>frog.realizations.default</code></li>
</ul>

<p>
This identity remains realization-oriented.
It does not replace widget class identity.
</p>

<hr/>

<h2 id="target-class-declarations">7. Target Class Declarations</h2>

<p>
The package SHOULD declare explicitly which standard widget classes it targets.
</p>

<p>
Typical targets include:
</p>

<ul>
  <li><code>frog.widgets.button</code></li>
  <li><code>frog.widgets.numeric_control</code></li>
  <li><code>frog.widgets.numeric_indicator</code></li>
  <li><code>frog.widgets.boolean_control</code></li>
  <li><code>frog.widgets.boolean_indicator</code></li>
  <li><code>frog.widgets.string_control</code></li>
  <li><code>frog.widgets.string_indicator</code></li>
  <li><code>frog.widgets.waveform_chart</code></li>
</ul>

<hr/>

<h2 id="realization-records">8. Realization Records</h2>

<p>
Each target class SHOULD have a realization record.
</p>

<p>
A realization record SHOULD identify:
</p>

<ul>
  <li>the target class,</li>
  <li>the supported parts,</li>
  <li>the supported visual states,</li>
  <li>the supported bindings,</li>
  <li>the supported host hints,</li>
  <li>the fallback posture.</li>
</ul>

<p>
Conceptually:
</p>

<pre><code>{
  "target_class": "frog.widgets.button",
  "family": "default",
  "parts": [ ... ],
  "states": [ ... ],
  "bindings": [ ... ],
  "fallbacks": { ... }
}
</code></pre>

<hr/>

<h2 id="resource-manifests">9. Resource Manifests</h2>

<p>
The package SHOULD publish explicit resource manifests.
</p>

<p>
Each resource manifest entry SHOULD identify:
</p>

<ul>
  <li>a stable resource identifier,</li>
  <li>the resource kind,</li>
  <li>the path,</li>
  <li>the target widget class or part when applicable,</li>
  <li>the target state when applicable.</li>
</ul>

<p>
Typical resource kinds include:
</p>

<ul>
  <li><code>svg</code></li>
  <li><code>vector_template</code></li>
  <li><code>layer_map</code></li>
  <li><code>anchor_map</code></li>
</ul>

<hr/>

<h2 id="state-maps">10. State Maps</h2>

<p>
The package SHOULD define explicit state maps rather than relying on filename conventions alone.
</p>

<p>
A state map associates:
</p>

<ul>
  <li>a widget class or widget part,</li>
  <li>a named state,</li>
  <li>one or more realization resources.</li>
</ul>

<p>
Examples:
</p>

<ul>
  <li><code>button.face.pressed</code></li>
  <li><code>numeric_control.increment_button.pressed</code></li>
  <li><code>boolean_control.state_face.normal_true</code></li>
</ul>

<hr/>

<h2 id="part-bindings">11. Part Bindings</h2>

<p>
The package SHOULD define explicit part bindings.
</p>

<p>
A part binding associates a public widget part with:
</p>

<ul>
  <li>a named resource layer,</li>
  <li>a named visual anchor,</li>
  <li>a host-native visual region,</li>
  <li>or another explicitly published realization surface.</li>
</ul>

<p>
Part bindings remain downstream from widget class law.
They must reference already-published parts.
</p>

<hr/>

<h2 id="host-hints">12. Host Hints</h2>

<p>
The package MAY define host-facing hints.
</p>

<p>
Typical host hints include:
</p>

<ul>
  <li>preferred focus ring style,</li>
  <li>preferred scaling posture,</li>
  <li>preferred density buckets,</li>
  <li>optional accessibility hints,</li>
  <li>preferred host-native substitution posture.</li>
</ul>

<p>
Such hints remain non-authoritative with respect to public widget law.
</p>

<hr/>

<h2 id="minimal-json-outline">13. Minimal JSON Outline</h2>

<pre><code>{
  "wfrog_version": "1",
  "package_kind": "widget_realization_library",
  "package": {
    "id": "frog.realizations.default",
    "name": "FROG Default Realization Family",
    "namespace": "frog.realizations.default"
  },
  "imports": [],
  "exports": {
    "realizations": [
      "frog.realizations.default.button",
      "frog.realizations.default.numeric_control",
      "frog.realizations.default.boolean_control"
    ]
  },
  "targets": [
    { "class_id": "frog.widgets.button" },
    { "class_id": "frog.widgets.numeric_control" },
    { "class_id": "frog.widgets.boolean_control" }
  ],
  "realizations": [
    {
      "id": "frog.realizations.default.button",
      "target_class": "frog.widgets.button",
      "states": [
        "normal",
        "disabled",
        "focused",
        "pressed"
      ],
      "parts": [
        "root",
        "face",
        "label",
        "frame"
      ],
      "bindings": [
        {
          "part": "face",
          "state": "pressed",
          "resource_ref": "button.face.pressed.svg"
        }
      ]
    }
  ],
  "resources": [
    {
      "id": "button.face.pressed.svg",
      "kind": "svg",
      "path": "./assets/button/face/pressed.svg"
    }
  ]
}</code></pre>

<hr/>

<h2 id="validation-posture">14. Validation Posture</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>unknown target class identifiers,</li>
  <li>bindings to undeclared widget parts,</li>
  <li>state mappings to undeclared realization states,</li>
  <li>resource references that do not resolve,</li>
  <li>attempts to use the package to redefine public class law,</li>
  <li>ambiguous duplicate bindings for the same class, part, and state without explicit precedence rules.</li>
</ul>

<hr/>

<h2 id="summary">15. Summary</h2>

<p>
The default realization package is the machine-readable publication surface for the official <code>Default</code> realization family.
</p>

<p>
It publishes target classes, realization records, state maps, part bindings, and resources while remaining subordinate to published widget class law.
</p>
