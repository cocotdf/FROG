<p align="center">
  <img src="../../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Example — Default Button Realization Package</h1>

<p align="center">
  <strong>Illustrative machine-readable <code>.wfrog</code> publication example for the default realization of <code>frog.widgets.button</code></strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#purpose-of-this-example">2. Purpose of this Example</a></li>
  <li><a href="#example-json">3. Example JSON</a></li>
  <li><a href="#reading-notes">4. Reading Notes</a></li>
  <li><a href="#summary">5. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document provides an illustrative machine-readable <code>.wfrog</code> publication example for the default realization of <code>frog.widgets.button</code>.
</p>

<p>
It is intentionally simple, but already complete enough to demonstrate:
</p>

<ul>
  <li>package identity,</li>
  <li>target-class declaration,</li>
  <li>realization declaration,</li>
  <li>state inventory,</li>
  <li>structural part bindings,</li>
  <li>resource publication,</li>
  <li>state-to-resource mapping,</li>
  <li>anchor publication for dynamic text placement,</li>
  <li>fallback posture.</li>
</ul>

<hr/>

<h2 id="purpose-of-this-example">2. Purpose of this Example</h2>

<p>
This example is not the generic <code>.wfrog</code> specification.
It is a concrete publication example built on top of the realization-package posture already defined elsewhere.
</p>

<p>
Its purpose is to show how the default official realization family may publish one standard widget embodiment in a machine-readable way without collapsing class law, realization publication, resources, and runtime implementation into the same layer.
</p>

<p>
In particular, this example preserves the architectural split between:
</p>

<ul>
  <li>the semantic button label owned by the widget class through <code>label.text</code>,</li>
  <li>the realization-side placement surface used to display that text,</li>
  <li>the state-sensitive visual resources used for the button face,</li>
  <li>the runtime-side responsibility for rendering live text into the published placement surface.</li>
</ul>

<hr/>

<h2 id="example-json">3. Example JSON</h2>

<pre><code>{
  "wfrog_version": "1",
  "package_kind": "widget_realization_library",
  "package": {
    "id": "frog.realizations.default.button",
    "name": "FROG Default Button Realization",
    "namespace": "frog.realizations.default",
    "publisher": "FROG",
    "summary": "Default official realization for frog.widgets.button"
  },
  "imports": [],
  "exports": {
    "realizations": [
      "frog.realizations.default.button"
    ],
    "resources": [
      "button.face.normal.svg",
      "button.face.disabled.svg",
      "button.face.focused.svg",
      "button.face.pressed.svg",
      "button.label.anchor_map"
    ],
    "anchors": [
      "button.label.center"
    ]
  },
  "targets": [
    {
      "class_id": "frog.widgets.button"
    }
  ],
  "realizations": [
    {
      "id": "frog.realizations.default.button",
      "family": "default",
      "target_class": "frog.widgets.button",
      "parts": [
        "root",
        "face",
        "label",
        "frame"
      ],
      "states": [
        "normal",
        "disabled",
        "focused",
        "pressed"
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
        }
      ],
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
          "fallback": "normal"
        },
        {
          "target_class": "frog.widgets.button",
          "target_part": "face",
          "state": "pressed",
          "resource_refs": [
            "button.face.pressed.svg"
          ],
          "fallback": "normal"
        }
      ],
      "fallbacks": {
        "focused": "normal",
        "pressed": "normal",
        "disabled": "normal"
      },
      "host_hints": {
        "supports_host_focus_ring": true,
        "supports_host_pressed_feedback": true,
        "preferred_scaling": "uniform"
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
      "id": "button.label.anchor_map",
      "kind": "anchor_map",
      "path": "./assets/button/anchors/label.json",
      "target_class": "frog.widgets.button",
      "target_part": "label",
      "role": "text_anchor"
    }
  ],
  "anchors": [
    {
      "id": "button.label.center",
      "target_class": "frog.widgets.button",
      "target_part": "label",
      "source_resource": "button.label.anchor_map",
      "anchor_kind": "text_anchor",
      "horizontal_alignment": "center",
      "vertical_alignment": "center",
      "padding": {
        "left": 10,
        "right": 10,
        "top": 6,
        "bottom": 6
      }
    }
  ]
}</code></pre>

<hr/>

<h2 id="reading-notes">4. Reading Notes</h2>

<p>
This example shows a clean four-layer split:
</p>

<ul>
  <li>the widget class already exists in <code>Libraries/Widgets/Button.md</code>,</li>
  <li>the default realization family already exists in <code>Libraries/Realizations/Default/Button.md</code>,</li>
  <li>this package publishes a machine-readable realization of that family,</li>
  <li>the assets remain realization resources rather than semantic truth.</li>
</ul>

<p>
The example also shows that:
</p>

<ul>
  <li><code>face</code> is the main state-driven visual part and therefore uses state maps,</li>
  <li><code>label</code> is not published as baked final text inside state-specific SVG assets,</li>
  <li><code>label</code> is structurally bound to a published anchor so that the runtime can render live <code>label.text</code>,</li>
  <li><code>pressed</code> and <code>focused</code> may fall back to <code>normal</code>,</li>
  <li>host hints remain hints rather than semantic law.</li>
</ul>

<p>
This distinction is important because the standard button class defines <code>label.text</code> as a portable semantic surface.
The realization may define where that text is placed, clipped, aligned, or decorated, but it does not become the semantic owner of the label content itself.
</p>

<hr/>

<h2 id="summary">5. Summary</h2>

<p>
This example provides a complete first machine-readable publication model for the default realization of <code>frog.widgets.button</code> using:
</p>

<ul>
  <li>state-sensitive visual resources for <code>face</code>,</li>
  <li>a published anchor map for <code>label</code>,</li>
  <li>explicit structural bindings,</li>
  <li>inspectable fallback posture.</li>
</ul>

<p>
It is suitable as a reference pattern for other widget realization packages in the same family, especially when a realization must preserve the distinction between public semantic text and realization-side visual placement.
</p>
