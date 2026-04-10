<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization State Mapping</h1>

<p align="center">
  <strong>Normative state and binding model for the official <code>Default</code> widget realization family</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-state-mapping-is-explicit">2. Why State Mapping Is Explicit</a></li>
  <li><a href="#state-map-purpose">3. State Map Purpose</a></li>
  <li><a href="#state-map-shape">4. State Map Shape</a></li>
  <li><a href="#part-binding-shape">5. Part Binding Shape</a></li>
  <li><a href="#state-maps-versus-structural-bindings">6. State Maps versus Structural Bindings</a></li>
  <li><a href="#widget-level-vs-part-level-maps">7. Widget-Level vs Part-Level Maps</a></li>
  <li><a href="#fallback-rules">8. Fallback Rules</a></li>
  <li><a href="#examples">9. Examples</a></li>
  <li><a href="#validation-posture">10. Validation Posture</a></li>
  <li><a href="#summary">11. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the state and binding model used by the official <code>Default</code> realization family.
</p>

<p>
The state-and-binding layer is the machine-readable realization layer that ties:
</p>

<ul>
  <li>public widget parts,</li>
  <li>published realization states,</li>
  <li>published realization resources,</li>
  <li>published anchors, text regions, or equivalent realization surfaces when needed.</li>
</ul>

<p>
Its role is to make realization correspondence explicit without redefining widget class law.
</p>

<p>
The central distinction of this document is simple:
</p>

<ul>
  <li><strong>state maps</strong> describe state-sensitive visual embodiment,</li>
  <li><strong>part bindings</strong> describe stable structural correspondence between a public part and a realization-side surface.</li>
</ul>

<hr/>

<h2 id="why-state-mapping-is-explicit">2. Why State Mapping Is Explicit</h2>

<p>
State mapping is made explicit so that:
</p>

<ul>
  <li>runtimes do not need to guess state/resource correspondence,</li>
  <li>assets do not become the only source of realization structure,</li>
  <li>validation can detect missing or ambiguous bindings,</li>
  <li>fallback posture can be inspected rather than hidden in runtime code,</li>
  <li>dynamic parts such as text-bearing parts do not get incorrectly modeled as if they were only static state assets.</li>
</ul>

<p>
The default family therefore treats state-sensitive embodiment and structural part binding as related but distinct publication concerns.
</p>

<hr/>

<h2 id="state-map-purpose">3. State Map Purpose</h2>

<p>
A state map associates:
</p>

<ul>
  <li>a target widget class,</li>
  <li>optionally a target widget part,</li>
  <li>a supported realization state,</li>
  <li>one or more resource references,</li>
  <li>optional fallback posture.</li>
</ul>

<p>
A state map answers the question:
</p>

<p>
<em>Which realization resource or resource group embodies this widget surface in this realization state?</em>
</p>

<p>
State maps are most natural for surfaces such as:
</p>

<ul>
  <li>a button face in <code>normal</code>, <code>focused</code>, or <code>pressed</code>,</li>
  <li>a button frame in <code>focused</code> or <code>disabled</code>,</li>
  <li>a boolean face in state-qualified variants,</li>
  <li>a numeric increment button in <code>pressed</code>.</li>
</ul>

<p>
State maps are generally <strong>not</strong> the preferred primary publication mechanism for dynamic public text-bearing parts whose live content is rendered by the host.
In those cases, the preferred primary mechanism is a structural binding to an anchor, text region, or equivalent placement surface.
</p>

<hr/>

<h2 id="state-map-shape">4. State Map Shape</h2>

<p>
A state map record SHOULD contain:
</p>

<ul>
  <li><code>target_class</code>,</li>
  <li><code>target_part</code> when applicable,</li>
  <li><code>state</code>,</li>
  <li><code>resource_refs</code>,</li>
  <li><code>fallback</code> when applicable.</li>
</ul>

<p>
A state map record MAY also contain:
</p>

<ul>
  <li><code>priority</code> when multiple compatible maps exist under explicit precedence rules,</li>
  <li><code>conditions</code> when the realization family publishes additional bounded selection posture,</li>
  <li><code>host_substitution</code> when a host-native fallback is explicitly declared.</li>
</ul>

<p>
Conceptually:
</p>

<pre><code>{
  "target_class": "frog.widgets.button",
  "target_part": "face",
  "state": "pressed",
  "resource_refs": [
    "button.face.pressed.svg"
  ],
  "fallback": "normal"
}</code></pre>

<p>
A state map should identify realization-side embodiment.
It should not be used to smuggle new public widget semantics into a resource-selection table.
</p>

<hr/>

<h2 id="part-binding-shape">5. Part Binding Shape</h2>

<p>
A part binding associates a public part with a realization surface.
</p>

<p>
A part binding record SHOULD contain:
</p>

<ul>
  <li><code>target_class</code>,</li>
  <li><code>part</code>,</li>
  <li><code>binding_kind</code>,</li>
  <li><code>binding_target</code>.</li>
</ul>

<p>
A part binding record MAY also contain:
</p>

<ul>
  <li><code>fallback</code> when the binding target can degrade gracefully,</li>
  <li><code>placement_role</code> when the target is a text anchor, clipping region, or equivalent placement surface.</li>
</ul>

<p>
Typical binding kinds include:
</p>

<ul>
  <li><code>resource_layer</code>,</li>
  <li><code>anchor</code>,</li>
  <li><code>text_region</code>,</li>
  <li><code>host_region</code>.</li>
</ul>

<p>
A part binding answers the question:
</p>

<p>
<em>Where does this public part live, visually or structurally, within the realization?</em>
</p>

<p>
Part bindings should remain stable unless the realization explicitly publishes multiple structural postures under inspectable precedence rules.
The default family therefore prefers keeping state variation in <code>state_maps</code> and keeping structural correspondence in <code>part_bindings</code>.
</p>

<hr/>

<h2 id="state-maps-versus-structural-bindings">6. State Maps versus Structural Bindings</h2>

<p>
The default family distinguishes clearly between state maps and structural bindings.
</p>

<ul>
  <li>a <strong>state map</strong> selects state-sensitive realization resources,</li>
  <li>a <strong>part binding</strong> associates a public part with a realization-side surface, region, layer, or anchor.</li>
</ul>

<p>
This distinction is important because not every public part should be modeled as a state-varying asset.
</p>

<p>
For example, in the default button posture:
</p>

<ul>
  <li><code>face</code> is naturally modeled through state maps such as <code>normal</code>, <code>disabled</code>, <code>focused</code>, and <code>pressed</code>,</li>
  <li><code>frame</code> may also be modeled through state maps when the realization family publishes frame variants,</li>
  <li><code>label</code> is naturally modeled through a structural binding to a text anchor, text region, or equivalent host-rendered placement surface.</li>
</ul>

<p>
The label may still vary stylistically across states, but its primary publication posture remains that of a dynamically rendered part bound to a placement surface rather than a semantic text string baked into a visual asset.
</p>

<p>
Therefore:
</p>

<ul>
  <li>state maps SHOULD be used for state-sensitive embodiment,</li>
  <li>part bindings SHOULD be used for stable structural correspondence,</li>
  <li>dynamic text-bearing parts SHOULD preferably bind to anchors, text regions, or host regions rather than being modeled only through state-scoped SVG files.</li>
</ul>

<p>
This rule applies more broadly than buttons.
It also matters for numeric displays, string value regions, chart titles, axis labels, and other future dynamic public surfaces.
</p>

<hr/>

<h2 id="widget-level-vs-part-level-maps">7. Widget-Level vs Part-Level Maps</h2>

<p>
The default family prefers part-level maps when a public part is explicitly realized.
</p>

<p>
Widget-level maps MAY be used when:
</p>

<ul>
  <li>the whole widget surface changes as one unit,</li>
  <li>the realization does not expose differentiated visual sub-surfaces for that state,</li>
  <li>the target class has a minimal part model.</li>
</ul>

<p>
Part-level maps are generally preferable when:
</p>

<ul>
  <li>the class exposes stable parts such as <code>face</code>, <code>label</code>, <code>frame</code>,</li>
  <li>different parts have different realization postures,</li>
  <li>only some parts are state-sensitive,</li>
  <li>the package intends to keep anchor or text-region publication inspectable.</li>
</ul>

<p>
For dynamic text-bearing parts, a part-level structural binding is usually more informative than a widget-level state map because it preserves the distinction between:
</p>

<ul>
  <li>the public semantic surface,</li>
  <li>the realization placement surface,</li>
  <li>the visual resources that may still vary elsewhere in the widget.</li>
</ul>

<hr/>

<h2 id="fallback-rules">8. Fallback Rules</h2>

<p>
A state map MAY define an explicit fallback.
</p>

<p>
Fallback SHOULD normally move toward a less specialized state rather than a more specialized one.
</p>

<p>
Examples:
</p>

<ul>
  <li><code>pressed</code> may fall back to <code>normal</code>,</li>
  <li><code>focused</code> may fall back to <code>normal</code> or to a documented host-native focus posture,</li>
  <li><code>disabled_true</code> may fall back to a host-native disabled boolean rendering preserving the true-state distinction.</li>
</ul>

<p>
A part binding MAY also define a fallback posture.
That is especially useful for dynamic placement surfaces.
</p>

<p>
Examples:
</p>

<ul>
  <li>a missing <code>text_region</code> may fall back to a host-native centered region,</li>
  <li>a missing focus-ring resource layer may fall back to a host-native focus ring,</li>
  <li>a missing anchor may fall back to a documented host-region rule.</li>
</ul>

<p>
Fallback must remain inspectable.
It must not silently collapse public part meaning into runtime-private heuristics.
</p>

<p>
The preferred pattern is:
</p>

<ul>
  <li><code>state_maps</code> publish visual-state fallback,</li>
  <li><code>part_bindings</code> publish structural or placement fallback.</li>
</ul>

<hr/>

<h2 id="examples">9. Examples</h2>

<pre><code>{
  "state_maps": [
    {
      "target_class": "frog.widgets.button",
      "target_part": "face",
      "state": "normal",
      "resource_refs": [
        "button.face.normal.svg"
      ]
    },
    {
      "target_class": "frog.widgets.button",
      "target_part": "face",
      "state": "disabled",
      "resource_refs": [
        "button.face.disabled.svg"
      ],
      "fallback": "normal"
    },
    {
      "target_class": "frog.widgets.button",
      "target_part": "face",
      "state": "focused",
      "resource_refs": [
        "button.face.focused.svg"
      ],
      "fallback": "host_native_focus_ring"
    },
    {
      "target_class": "frog.widgets.button",
      "target_part": "face",
      "state": "pressed",
      "resource_refs": [
        "button.face.pressed.svg"
      ],
      "fallback": "normal"
    },
    {
      "target_class": "frog.widgets.button",
      "target_part": "frame",
      "state": "focused",
      "resource_refs": [
        "button.frame.focused.svg"
      ],
      "fallback": "normal"
    },
    {
      "target_class": "frog.widgets.numeric_control",
      "target_part": "increment_button",
      "state": "pressed",
      "resource_refs": [
        "numeric_control.increment_button.pressed.svg"
      ],
      "fallback": "normal"
    }
  ],
  "part_bindings": [
    {
      "target_class": "frog.widgets.button",
      "part": "face",
      "binding_kind": "resource_layer",
      "binding_target": "face"
    },
    {
      "target_class": "frog.widgets.button",
      "part": "label",
      "binding_kind": "anchor",
      "binding_target": "button.label.center",
      "placement_role": "text_anchor",
      "fallback": "host_centered_text_region"
    },
    {
      "target_class": "frog.widgets.button",
      "part": "frame",
      "binding_kind": "resource_layer",
      "binding_target": "frame"
    },
    {
      "target_class": "frog.widgets.numeric_control",
      "part": "value_display",
      "binding_kind": "text_region",
      "binding_target": "numeric_control.value.center",
      "placement_role": "text_region",
      "fallback": "host_value_region"
    }
  ]
}</code></pre>

<p>
In this example:
</p>

<ul>
  <li>the button <code>face</code> is realized through state-sensitive resources,</li>
  <li>the button <code>frame</code> may expose additional state-sensitive embodiment,</li>
  <li>the button <code>label</code> is realized through a structural binding to a published placement surface,</li>
  <li>the package remains explicit about fallback posture for both state-sensitive embodiment and dynamic placement.</li>
</ul>

<hr/>

<h2 id="validation-posture">10. Validation Posture</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>state maps referencing undeclared classes, parts, or states,</li>
  <li>missing resource references,</li>
  <li>ambiguous duplicate state bindings without explicit precedence,</li>
  <li>fallback chains that resolve to unknown states or undocumented host substitutions,</li>
  <li>part bindings that target undeclared public parts,</li>
  <li>part bindings whose binding kinds are unknown or incompatible with the referenced binding target,</li>
  <li>dynamic public text-bearing parts modeled only as asset-baked state resources when the realization family claims explicit anchor or text-region support.</li>
</ul>

<p>
Validators MAY also diagnose:
</p>

<ul>
  <li>needlessly coarse widget-level mappings when a stable part-level posture is already published,</li>
  <li>overlapping bindings for the same class and part without explicit precedence,</li>
  <li>state maps that attempt to encode public widget semantics instead of realization-side embodiment,</li>
  <li>examples in which a dynamic public text-bearing part is simultaneously treated as anchor-bound and as the semantic owner of state-scoped SVG label resources without an explicit dual-layer realization contract.</li>
</ul>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
The default realization state-and-binding model makes realization correspondence explicit.
</p>

<p>
It is the correct layer for:
</p>

<ul>
  <li>part/state/resource correspondence,</li>
  <li>structural part bindings,</li>
  <li>fallback rules for state-sensitive embodiment and dynamic placement.</li>
</ul>

<p>
Its preferred architecture is:
</p>

<ul>
  <li><code>state_maps</code> for state-sensitive visual embodiment,</li>
  <li><code>part_bindings</code> for stable structural correspondence,</li>
  <li>placement surfaces for dynamic public parts rendered by the host,</li>
  <li>clear separation between realization-side embodiment and widget-class meaning.</li>
</ul>

<p>
It remains fully subordinate to widget class law and realization-family posture.
Its main architectural rule is that state-sensitive visual embodiment and stable structural part binding must remain distinguishable, inspectable, and portable.
</p>
