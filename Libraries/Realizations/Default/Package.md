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
  <li><a href="#anchor-and-text-region-publication">12. Anchor and Text-Region Publication</a></li>
  <li><a href="#host-hints">13. Host Hints</a></li>
  <li><a href="#minimal-json-outline">14. Minimal JSON Outline</a></li>
  <li><a href="#validation-posture">15. Validation Posture</a></li>
  <li><a href="#summary">16. Summary</a></li>
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
  <li>which anchors, regions, or equivalent placement surfaces are published,</li>
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
  <li>assets would drift toward ad hoc organization,</li>
  <li>dynamic text-bearing parts would be at risk of collapsing into asset-only conventions.</li>
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
  <li>the package MAY publish state maps, part bindings, anchor bindings, and resource references,</li>
  <li>the runtime MAY interpret or approximate the package while preserving class meaning.</li>
</ul>

<p>
In particular, the package MAY publish where a public text-bearing part is visually placed, but it MUST NOT become the semantic owner of the text shown by that part.
</p>

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
  <li>reusable anchor and placement metadata,</li>
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

<p>
Implementations MAY choose a more structured internal encoding, but the publication posture should still make the following inspectable:
</p>

<ul>
  <li>target classes,</li>
  <li>realization identities,</li>
  <li>state sets,</li>
  <li>part sets,</li>
  <li>resource inventories,</li>
  <li>part-to-resource bindings,</li>
  <li>part-to-anchor or part-to-region bindings when relevant.</li>
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

<p>
These declarations identify realization targets.
They do not redefine the corresponding standardized classes.
</p>

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

<p>
A realization record MAY also identify:
</p>

<ul>
  <li>placement surfaces,</li>
  <li>state-specific resource groups,</li>
  <li>optional host-native substitution posture,</li>
  <li>scaling or density hints.</li>
</ul>

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
  <li><code>text_region_map</code></li>
</ul>

<p>
A resource manifest entry identifies available realization resources.
It does not, by itself, declare how a host should interpret public widget semantics.
</p>

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

<p>
State maps are realization-side publication artifacts.
They define which realization resources correspond to named visual states.
They do not define new semantic widget states beyond those already justified by the realization family.
</p>

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

<p>
For state-sensitive parts, a binding MAY also be scoped by state.
For example, a button <code>face</code> binding may vary between <code>normal</code> and <code>pressed</code>.
</p>

<p>
For dynamic text-bearing parts, a part binding SHOULD preferably target an anchor or text region rather than a resource that hardcodes the final user-visible text content.
</p>

<hr/>

<h2 id="anchor-and-text-region-publication">12. Anchor and Text-Region Publication</h2>

<p>
The default realization package SHOULD make anchor or text-region publication explicit whenever a public part is dynamically rendered by the host rather than fully baked into a single visual asset.
</p>

<p>
This is especially important for parts such as:
</p>

<ul>
  <li><code>button.label</code>,</li>
  <li>numeric text display regions,</li>
  <li>string text display regions,</li>
  <li>chart plot or axis label regions when those are realization-published.</li>
</ul>

<h3>12.1 Publication purpose</h3>

<p>
Anchor and text-region publication exists to make realization-side placement inspectable.
It defines where the host should place or render a dynamic part.
It does not redefine the semantic owner of the data shown there.
</p>

<h3>12.2 Typical anchor entry</h3>

<p>
A typical anchor-oriented publication may identify:
</p>

<ul>
  <li>the anchor identifier,</li>
  <li>the target part,</li>
  <li>the placement kind,</li>
  <li>the target resource or layer when applicable,</li>
  <li>alignment posture,</li>
  <li>padding or inset metadata,</li>
  <li>clipping posture when needed.</li>
</ul>

<p>
Conceptually:
</p>

<pre><code>{
  "id": "button.label.center",
  "part": "label",
  "kind": "text_anchor",
  "resource_ref": "button.label.anchor.json",
  "horizontal_alignment": "center",
  "vertical_alignment": "middle",
  "padding": { "left": 8, "right": 8, "top": 4, "bottom": 4 }
}
</code></pre>

<h3>12.3 Button-specific posture</h3>

<p>
For <code>frog.widgets.button</code>, the package SHOULD make it possible to express the following distinction cleanly:
</p>

<ul>
  <li><code>face</code> binds to state-sensitive visual resources,</li>
  <li><code>label</code> binds to a text anchor, text region, or equivalent placement surface,</li>
  <li>the host dynamically renders the current semantic <code>label.text</code> into that surface.</li>
</ul>

<p>
That publication posture helps preserve the architectural separation between:
</p>

<ul>
  <li>class-owned semantic label text,</li>
  <li>widget-visible style properties when supported,</li>
  <li>realization-owned placement metadata,</li>
  <li>asset-owned decorative visual content.</li>
</ul>

<hr/>

<h2 id="host-hints">13. Host Hints</h2>

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

<h2 id="minimal-json-outline">14. Minimal JSON Outline</h2>

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
          "state": "normal",
          "resource_ref": "button.face.normal.svg"
        },
        {
          "part": "face",
          "state": "disabled",
          "resource_ref": "button.face.disabled.svg"
        },
        {
          "part": "face",
          "state": "focused",
          "resource_ref": "button.face.focused.svg"
        },
        {
          "part": "face",
          "state": "pressed",
          "resource_ref": "button.face.pressed.svg"
        },
        {
          "part": "label",
          "binding_kind": "text_anchor",
          "anchor_ref": "button.label.center"
        }
      ],
      "fallbacks": {
        "focused": "host_native_focus_ring",
        "pressed": "host_native_pressed_posture",
        "label": "host_centered_text_region"
      }
    }
  ],
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
      "id": "button.face.disabled.svg",
      "kind": "svg",
      "path": "./assets/button/face/disabled.svg",
      "target_class": "frog.widgets.button",
      "target_part": "face",
      "target_state": "disabled"
    },
    {
      "id": "button.face.focused.svg",
      "kind": "svg",
      "path": "./assets/button/face/focused.svg",
      "target_class": "frog.widgets.button",
      "target_part": "face",
      "target_state": "focused"
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
      "id": "button.label.anchor.json",
      "kind": "anchor_map",
      "path": "./assets/button/anchors/label.json",
      "target_class": "frog.widgets.button",
      "target_part": "label"
    }
  ],
  "anchors": [
    {
      "id": "button.label.center",
      "target_class": "frog.widgets.button",
      "target_part": "label",
      "kind": "text_anchor",
      "resource_ref": "button.label.anchor.json",
      "horizontal_alignment": "center",
      "vertical_alignment": "middle",
      "padding": {
        "left": 8,
        "right": 8,
        "top": 4,
        "bottom": 4
      }
    }
  ]
}</code></pre>

<hr/>

<h2 id="validation-posture">15. Validation Posture</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>unknown target class identifiers,</li>
  <li>bindings to undeclared widget parts,</li>
  <li>state mappings to undeclared realization states,</li>
  <li>resource references that do not resolve,</li>
  <li>attempts to use the package to redefine public class law,</li>
  <li>ambiguous duplicate bindings for the same class, part, and state without explicit precedence rules,</li>
  <li>anchor or text-region bindings that reference undeclared parts,</li>
  <li>resource entries that imply asset-baked semantic text as the only realization path for a dynamic public text-bearing part.</li>
</ul>

<p>
Validators MAY also diagnose realization records that omit an inspectable placement path for dynamic text-bearing parts when the corresponding realization family claims to support them.
</p>

<hr/>

<h2 id="summary">16. Summary</h2>

<p>
The default realization package is the machine-readable publication surface for the official <code>Default</code> realization family.
</p>

<p>
It publishes target classes, realization records, state maps, part bindings, anchors, and resources while remaining subordinate to published widget class law.
</p>

<p>
Its main purpose is to make the official realization family inspectable and portable without collapsing widget semantics into assets or into one runtime-specific implementation.
</p>
