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
  <li><a href="#widget-level-vs-part-level-maps">6. Widget-Level vs Part-Level Maps</a></li>
  <li><a href="#fallback-rules">7. Fallback Rules</a></li>
  <li><a href="#examples">8. Examples</a></li>
  <li><a href="#validation-posture">9. Validation Posture</a></li>
  <li><a href="#summary">10. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the state and binding model used by the official <code>Default</code> realization family.
</p>

<p>
The state map is the machine-readable layer that ties:
</p>

<ul>
  <li>public widget parts,</li>
  <li>published realization states,</li>
  <li>published realization resources.</li>
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
  <li>fallback posture can be inspected rather than hidden in runtime code.</li>
</ul>

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

<hr/>

<h2 id="state-map-shape">4. State Map Shape</h2>

<p>
A state map record SHOULD contain:
</p>

<ul>
  <li><code>target_class</code></li>
  <li><code>target_part</code> when applicable</li>
  <li><code>state</code></li>
  <li><code>resource_refs</code></li>
  <li><code>fallback</code> when applicable</li>
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

<hr/>

<h2 id="part-binding-shape">5. Part Binding Shape</h2>

<p>
A part binding associates a public part with a realization surface.
</p>

<p>
A part binding record SHOULD contain:
</p>

<ul>
  <li><code>target_class</code></li>
  <li><code>part</code></li>
  <li><code>binding_kind</code></li>
  <li><code>binding_target</code></li>
</ul>

<p>
Typical binding kinds include:
</p>

<ul>
  <li><code>resource_layer</code></li>
  <li><code>anchor</code></li>
  <li><code>host_region</code></li>
</ul>

<hr/>

<h2 id="widget-level-vs-part-level-maps">6. Widget-Level vs Part-Level Maps</h2>

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

<hr/>

<h2 id="fallback-rules">7. Fallback Rules</h2>

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
  <li><code>focused</code> may fall back to host-native focus posture,</li>
  <li><code>disabled_true</code> may fall back to a host-native disabled boolean rendering preserving the true state distinction.</li>
</ul>

<hr/>

<h2 id="examples">8. Examples</h2>

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
      "state": "pressed",
      "resource_refs": [
        "button.face.pressed.svg"
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
      "target_class": "frog.widgets.numeric_control",
      "part": "value_display",
      "binding_kind": "host_region",
      "binding_target": "value_display"
    }
  ]
}</code></pre>

<hr/>

<h2 id="validation-posture">9. Validation Posture</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>state maps referencing undeclared classes, parts, or states,</li>
  <li>missing resource references,</li>
  <li>ambiguous duplicate state bindings without explicit precedence,</li>
  <li>fallback chains that resolve to unknown states,</li>
  <li>part bindings that target undeclared public parts.</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The default realization state map makes realization binding explicit.
</p>

<p>
It is the correct layer for part/state/resource correspondence and for fallback rules, while remaining fully subordinate to widget class law and realization-family posture.
</p>
