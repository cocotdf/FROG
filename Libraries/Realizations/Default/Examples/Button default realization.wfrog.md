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
  <li>part bindings,</li>
  <li>resource publication,</li>
  <li>state-to-resource mapping,</li>
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
      "button.label.normal.svg",
      "button.label.disabled.svg"
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
          "part": "face",
          "binding_kind": "resource_layer",
          "binding_target": "face"
        },
        {
          "part": "label",
          "binding_kind": "resource_layer",
          "binding_target": "label"
        },
        {
          "part": "frame",
          "binding_kind": "resource_layer",
          "binding_target": "frame"
        }
      ],
      "state_maps": [
        {
          "target_part": "face",
          "state": "normal",
          "resource_refs": [
            "button.face.normal.svg"
          ]
        },
        {
          "target_part": "face",
          "state": "disabled",
          "resource_refs": [
            "button.face.disabled.svg"
          ],
          "fallback": "normal"
        },
        {
          "target_part": "face",
          "state": "focused",
          "resource_refs": [
            "button.face.focused.svg"
          ],
          "fallback": "normal"
        },
        {
          "target_part": "face",
          "state": "pressed",
          "resource_refs": [
            "button.face.pressed.svg"
          ],
          "fallback": "normal"
        },
        {
          "target_part": "label",
          "state": "normal",
          "resource_refs": [
            "button.label.normal.svg"
          ]
        },
        {
          "target_part": "label",
          "state": "disabled",
          "resource_refs": [
            "button.label.disabled.svg"
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
      "id": "button.label.normal.svg",
      "kind": "svg",
      "path": "./assets/button/label/normal.svg",
      "target_class": "frog.widgets.button",
      "target_part": "label",
      "target_state": "normal"
    },
    {
      "id": "button.label.disabled.svg",
      "kind": "svg",
      "path": "./assets/button/label/disabled.svg",
      "target_class": "frog.widgets.button",
      "target_part": "label",
      "target_state": "disabled"
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
  <li>the SVG files remain realization resources rather than semantic truth.</li>
</ul>

<p>
The example also shows that:
</p>

<ul>
  <li><code>face</code> is the main state-driven visual part,</li>
  <li><code>label</code> has its own resource posture,</li>
  <li><code>pressed</code> and <code>focused</code> may fall back to <code>normal</code>,</li>
  <li>host hints remain hints rather than semantic law.</li>
</ul>

<hr/>

<h2 id="summary">5. Summary</h2>

<p>
This example provides a complete first machine-readable publication model for the default realization of <code>frog.widgets.button</code>.
</p>

<p>
It is suitable as a reference pattern for other widget realization packages in the same family.
</p>
