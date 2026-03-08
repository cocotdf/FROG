<h1 align="center">🐸 FROG Front Panel Specification</h1>

<p align="center">
Definition of the front panel (interaction layer) for <strong>.frog</strong> programs<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#design-goals">2. Design Goals</a></li>
  <li><a href="#location">3. Location in a .frog file</a></li>
  <li><a href="#relationship-with-interface-diagram-and-widget-model">4. Relationship with Interface, Diagram, and Widget Model</a></li>
  <li><a href="#front-panel-structure">5. Front Panel Structure</a></li>
  <li><a href="#canvas-and-coordinate-system">6. Canvas and Coordinate System</a></li>
  <li><a href="#widget-instances">7. Widget Instances</a></li>
  <li><a href="#bindings">8. Bindings</a></li>
  <li><a href="#layout-model">9. Layout Model</a></li>
  <li><a href="#style-system">10. Style System</a>
    <ul>
      <li><a href="#theme">10.1 Theme</a></li>
      <li><a href="#fonts">10.2 Fonts</a></li>
      <li><a href="#colors-and-variables">10.3 Colors and Variables</a></li>
      <li><a href="#style-references-and-overrides">10.4 Style References and Overrides</a></li>
    </ul>
  </li>
  <li><a href="#ui-libraries">11. UI Libraries</a></li>
  <li><a href="#validation-rules">12. Validation Rules</a></li>
  <li><a href="#examples">13. Examples</a></li>
  <li><a href="#summary">14. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <strong>front_panel</strong> section defines the graphical interaction layer of a Frog.
It describes the user-facing UI composition of the program.
</p>

<p>
The front panel is composed of <strong>widget instances</strong>.
These widgets may provide user input, display program state, organize layout, or contribute purely visual decoration.
</p>

<p>
The <code>front_panel</code> section is part of the canonical <code>.frog</code> source format.
It MUST exist, even when a Frog is executed in a headless or non-interactive context.
</p>

<p>
The front panel does <strong>not</strong> define execution logic and does <strong>not</strong> define the public contract of the Frog.
Its role is interaction, presentation, visualization, and UI organization.
</p>

<p>
Runtimes MAY ignore the front panel during execution.
Development tools, editors, and interactive runtimes MAY use it to render a user interface.
</p>

<hr/>

<h2 id="design-goals">2. Design Goals</h2>

<ul>
  <li>tool-agnostic front panel representation,</li>
  <li>stable widget serialization across implementations,</li>
  <li>clear separation between logic, public contract, and UI,</li>
  <li>explicit binding rules,</li>
  <li>consistent object-based widget composition,</li>
  <li>modular styling through themes, variables, and overrides,</li>
  <li>extensible UI composition through standard and library-defined widgets.</li>
</ul>

<hr/>

<h2 id="location">3. Location in a .frog file</h2>

<pre>{
  "spec_version": "0.1",
  "metadata": {},
  "interface": {},
  "connector": {},
  "diagram": {},
  "front_panel": {}
}</pre>

<p>
The <code>front_panel</code> section MUST exist in a canonical <code>.frog</code> source file.
It MAY be empty.
</p>

<hr/>

<h2 id="relationship-with-interface-diagram-and-widget-model">4. Relationship with Interface, Diagram, and Widget Model</h2>

<p>
FROG distinguishes the following concepts:
</p>

<ul>
  <li><strong>interface</strong> — defines the public logical contract of the Frog,</li>
  <li><strong>diagram</strong> — defines the executable dataflow logic,</li>
  <li><strong>front_panel</strong> — defines the user interaction layer,</li>
  <li><strong>widget model</strong> — defines what a widget is and how widgets behave as UI objects.</li>
</ul>

<p>
The front panel MUST NOT be interpreted as the public API of the Frog.
Controls and indicators are user-facing widgets, not public logical ports.
</p>

<p>
The front panel also does not redefine execution semantics.
It describes how widgets are arranged and how they are bound to interface ports or diagram ports.
</p>

<p>
The object model of widgets is defined normatively by <code>Widget.md</code>.
This document does not redefine widget inheritance, widget roles, widget parts, or widget property semantics.
Instead, it defines how widget instances are composed inside the <code>front_panel</code> section.
</p>

<p>
In short:
</p>

<ul>
  <li><strong>interface</strong> = what the Frog exposes,</li>
  <li><strong>diagram</strong> = how the Frog works,</li>
  <li><strong>widget model</strong> = what UI objects are,</li>
  <li><strong>front_panel</strong> = how those UI objects are placed and bound for user interaction.</li>
</ul>

<hr/>

<h2 id="front-panel-structure">5. Front Panel Structure</h2>

<p>
Recommended structure:
</p>

<pre>"front_panel": {
  "canvas": {},
  "widgets": [],
  "bindings": [],
  "style": {},
  "ui_libraries": []
}</pre>

<p>
Fields:
</p>

<ul>
  <li><code>canvas</code> — coordinate system and visual background,</li>
  <li><code>widgets</code> — widget instances serialized according to <code>Widget.md</code>,</li>
  <li><code>bindings</code> — explicit links from widgets to interface ports or diagram ports,</li>
  <li><code>style</code> — theme, fonts, colors, variables, and reusable style definitions,</li>
  <li><code>ui_libraries</code> — references to external UI widget libraries.</li>
</ul>

<p>
All fields are optional unless otherwise constrained by validation rules.
An empty front panel is valid.
</p>

<p>
The <code>widgets</code> array is the canonical container for serialized widget instances in v0.1.
</p>

<hr/>

<h2 id="canvas-and-coordinate-system">6. Canvas and Coordinate System</h2>

<p>
The canvas defines the design-time coordinate system used by front panel widgets.
</p>

<pre>"canvas": {
  "units": "px",
  "width": 900,
  "height": 600,
  "background": {
    "color": "#FFFFFF"
  }
}</pre>

<p>
Rules:
</p>

<ul>
  <li>Units SHOULD be <code>px</code> in v0.1.</li>
  <li>Width and height SHOULD be integers.</li>
  <li>The background is purely visual and MUST NOT affect execution semantics.</li>
</ul>

<p>
The canvas provides a coordinate space only.
It does not define widget class semantics, type behavior, or execution behavior.
</p>

<hr/>

<h2 id="widget-instances">7. Widget Instances</h2>

<p>
All user-facing UI objects in the front panel are represented as widget instances.
</p>

<p>
Each entry in <code>widgets</code> MUST follow the widget instance model defined in <code>Widget.md</code>.
</p>

<p>
A widget instance typically defines:
</p>

<ul>
  <li><code>id</code>,</li>
  <li><code>role</code>,</li>
  <li><code>widget</code>,</li>
  <li><code>value_type</code> when applicable,</li>
  <li><code>layout</code>,</li>
  <li><code>props</code>,</li>
  <li><code>parts</code> when applicable.</li>
</ul>

<p>
Example widget instance:
</p>

<pre>{
  "id": "ctrl_gain",
  "role": "control",
  "widget": "frog.ui.standard.numeric_control",
  "value_type": "f64",
  "layout": { "x": 20, "y": 20, "width": 120, "height": 28 },
  "props": {
    "minimum": 0.0,
    "maximum": 10.0,
    "step": 0.1,
    "default_value": 1.0
  },
  "parts": {
    "label": {
      "class": "frog.ui.standard.label_part",
      "props": {
        "text": "Gain",
        "visible": true
      }
    }
  }
}</pre>

<p>
This document does not classify widgets by ad hoc element kinds such as “control”, “text”, or “shape” outside the widget model.
Those distinctions belong to the standardized widget roles and classes defined by <code>Widget.md</code>.
</p>

<p>
A front panel MAY contain:
</p>

<ul>
  <li>value-carrying widgets such as controls and indicators,</li>
  <li>container widgets,</li>
  <li>decoration widgets,</li>
  <li>library-defined specialized widgets allowed by the active profile.</li>
</ul>

<hr/>

<h2 id="bindings">8. Bindings</h2>

<p>
Bindings connect widget instances to interface ports or diagram ports.
Bindings MUST be explicit.
</p>

<p>
Recommended binding structure:
</p>

<pre>"bindings": [
  {
    "widget": "ctrl_gain",
    "mode": "write",
    "target": {
      "scope": "interface",
      "port": "gain"
    }
  },
  {
    "widget": "ind_result",
    "mode": "read",
    "target": {
      "scope": "interface",
      "port": "result"
    }
  },
  {
    "widget": "ind_internal",
    "mode": "read",
    "target": {
      "scope": "diagram",
      "node": "compute_sum",
      "port": "value"
    }
  }
]</pre>

<p>
Fields:
</p>

<ul>
  <li><code>widget</code> — identifier of the bound widget instance,</li>
  <li><code>mode</code> — interaction mode such as <code>read</code> or <code>write</code>,</li>
  <li><code>target</code> — binding destination in interface space or diagram space.</li>
</ul>

<p>
Target forms:
</p>

<ul>
  <li><strong>Interface target</strong>: <code>{ "scope": "interface", "port": "name" }</code></li>
  <li><strong>Diagram target</strong>: <code>{ "scope": "diagram", "node": "node_id", "port": "port_name" }</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>Each binding MUST reference an existing widget id.</li>
  <li>Each binding MUST reference a valid target according to its scope.</li>
  <li>Bindings MUST be type-compatible.</li>
  <li>Controls SHOULD use <code>write</code> bindings when they provide values to the program.</li>
  <li>Indicators SHOULD use <code>read</code> bindings when they display values from the program.</li>
</ul>

<p>
The binding model defines interaction wiring only.
It MUST NOT introduce additional execution semantics.
</p>

<p>
This document defines widget-to-port bindings.
It does not yet standardize the full diagram encoding of widget property nodes, widget method nodes, or event nodes.
Those remain outside the strict scope of v0.1 front panel serialization.
</p>

<hr/>

<h2 id="layout-model">9. Layout Model</h2>

<p>
Layout defines widget geometry and visual ordering.
</p>

<p>
Typical layout fields include:
</p>

<ul>
  <li><code>x</code>, <code>y</code> — position,</li>
  <li><code>width</code>, <code>height</code> — size,</li>
  <li><code>z</code> (optional) — drawing order,</li>
  <li><code>anchor</code> (optional) — responsive behavior hint.</li>
</ul>

<p>
Example:
</p>

<pre>"layout": {
  "x": 20,
  "y": 20,
  "width": 120,
  "height": 28,
  "z": 10,
  "anchor": "top_left"
}</pre>

<p>
Layout fields are design-time and rendering-oriented.
They MUST NOT affect execution semantics, scheduling, type rules, or public interface behavior.
</p>

<hr/>

<h2 id="style-system">10. Style System</h2>

<p>
The style system provides modular visual definitions:
</p>

<ul>
  <li>themes,</li>
  <li>fonts,</li>
  <li>color palettes,</li>
  <li>style references,</li>
  <li>local overrides.</li>
</ul>

<h3 id="theme">10.1 Theme</h3>

<pre>"style": {
  "theme": "default"
}</pre>

<h3 id="fonts">10.2 Fonts</h3>

<pre>"style": {
  "fonts": {
    "default": { "family": "Inter", "size": 12, "weight": 400 },
    "title": { "family": "Inter", "size": 20, "weight": 700 }
  }
}</pre>

<h3 id="colors-and-variables">10.3 Colors and Variables</h3>

<pre>"style": {
  "colors": {
    "bg": "#FFFFFF",
    "fg": "#111111",
    "accent": "#2ECC71"
  }
}</pre>

<p>
Implementations MAY support additional style variables or token systems under stricter profiles.
</p>

<h3 id="style-references-and-overrides">10.4 Style References and Overrides</h3>

<p>
Widget instances MAY reference shared style definitions and MAY override them locally.
</p>

<pre>{
  "id": "ctrl_gain",
  "role": "control",
  "widget": "frog.ui.standard.numeric_control",
  "value_type": "f64",
  "layout": { "x": 20, "y": 20, "width": 120, "height": 28 },
  "props": {
    "default_value": 1.0
  },
  "style_ref": "default.control",
  "style_override": {
    "colors": {
      "accent": "#FF6600"
    }
  }
}</pre>

<p>
Style information is non-semantic and MUST NOT affect execution behavior.
</p>

<hr/>

<h2 id="ui-libraries">11. UI Libraries</h2>

<p>
FROG front panels MAY reference external UI widget libraries.
This enables modular and standardized widget sets beyond the minimal built-in vocabulary.
</p>

<p>
Example:
</p>

<pre>"ui_libraries": [
  {
    "name": "frog.ui.standard",
    "version": "0.1.0"
  }
]</pre>

<p>
Rules:
</p>

<ul>
  <li>UI libraries MAY define additional widget classes, parts, and styling systems.</li>
  <li>Widgets serialized in the front panel SHOULD be resolvable against the active built-in set or declared UI libraries.</li>
  <li>Runtimes MAY ignore UI libraries for pure execution.</li>
  <li>Editors and interactive runtimes MAY use UI libraries to reconstruct specialized visual behavior.</li>
</ul>

<hr/>

<h2 id="validation-rules">12. Validation Rules</h2>

<p>
Implementations MUST enforce:
</p>

<ul>
  <li><code>front_panel</code> MUST exist in a canonical <code>.frog</code> file,</li>
  <li>if present, <code>widgets</code> MUST be an array,</li>
  <li>widget identifiers MUST be unique within the front panel scope,</li>
  <li>all widget instances MUST be valid according to <code>Widget.md</code>,</li>
  <li>all bindings MUST reference valid widget ids,</li>
  <li>all bindings MUST reference valid targets according to their declared scope,</li>
  <li>widget layouts MUST contain valid numeric coordinates when layout is present,</li>
  <li>bindings MUST be type-compatible with their targets,</li>
  <li>unknown front panel properties MUST NOT affect execution semantics.</li>
</ul>

<p>
Additionally:
</p>

<ul>
  <li>an empty <code>front_panel</code> section is valid,</li>
  <li>style and UI library information MUST remain non-authoritative for execution,</li>
  <li>tools MAY warn when a control uses a read-only target or an indicator uses a write-only target.</li>
</ul>

<hr/>

<h2 id="examples">13. Examples</h2>

<h3>13.1 Minimal front panel</h3>

<pre>"front_panel": {
  "canvas": {
    "units": "px",
    "width": 600,
    "height": 400,
    "background": { "color": "#FFFFFF" }
  },
  "widgets": [],
  "bindings": [],
  "style": {},
  "ui_libraries": []
}</pre>

<h3>13.2 Control and indicator bound to the public interface</h3>

<pre>"front_panel": {
  "canvas": {
    "units": "px",
    "width": 900,
    "height": 600,
    "background": { "color": "#FFFFFF" }
  },
  "widgets": [
    {
      "id": "ctrl_gain",
      "role": "control",
      "widget": "frog.ui.standard.numeric_control",
      "value_type": "f64",
      "layout": { "x": 20, "y": 20, "width": 120, "height": 28 },
      "props": {
        "minimum": 0.0,
        "maximum": 10.0,
        "step": 0.1,
        "default_value": 1.0
      },
      "parts": {
        "label": {
          "class": "frog.ui.standard.label_part",
          "props": {
            "text": "Gain",
            "visible": true
          }
        }
      },
      "style_ref": "default.control"
    },
    {
      "id": "ind_result",
      "role": "indicator",
      "widget": "frog.ui.standard.numeric_indicator",
      "value_type": "f64",
      "layout": { "x": 20, "y": 60, "width": 120, "height": 28 },
      "props": {
        "visible": true
      },
      "parts": {
        "label": {
          "class": "frog.ui.standard.label_part",
          "props": {
            "text": "Result",
            "visible": true
          }
        }
      },
      "style_ref": "default.indicator"
    },
    {
      "id": "title_1",
      "role": "decoration",
      "widget": "frog.ui.standard.text_label",
      "layout": { "x": 20, "y": 110, "width": 240, "height": 28 },
      "props": {
        "text": "Example Frog",
        "visible": true
      },
      "style_ref": "default.title"
    }
  ],
  "bindings": [
    {
      "widget": "ctrl_gain",
      "mode": "write",
      "target": { "scope": "interface", "port": "gain" }
    },
    {
      "widget": "ind_result",
      "mode": "read",
      "target": { "scope": "interface", "port": "result" }
    }
  ],
  "style": {
    "theme": "default",
    "fonts": {
      "default": { "family": "Inter", "size": 12, "weight": 400 },
      "title": { "family": "Inter", "size": 20, "weight": 700 }
    },
    "colors": {
      "bg": "#FFFFFF",
      "fg": "#111111",
      "accent": "#2ECC71"
    }
  },
  "ui_libraries": [
    { "name": "frog.ui.standard", "version": "0.1.0" }
  ]
}</pre>

<h3>13.3 Indicator bound to an internal diagram node</h3>

<pre>"front_panel": {
  "widgets": [
    {
      "id": "ind_internal",
      "role": "indicator",
      "widget": "frog.ui.standard.numeric_indicator",
      "value_type": "f64",
      "layout": { "x": 20, "y": 20, "width": 120, "height": 28 },
      "props": {},
      "parts": {
        "label": {
          "class": "frog.ui.standard.label_part",
          "props": {
            "text": "Internal sum",
            "visible": true
          }
        }
      }
    }
  ],
  "bindings": [
    {
      "widget": "ind_internal",
      "mode": "read",
      "target": {
        "scope": "diagram",
        "node": "compute_sum",
        "port": "value"
      }
    }
  ]
}</pre>

<h3>13.4 Container widget with child widgets</h3>

<pre>"front_panel": {
  "widgets": [
    {
      "id": "main_panel",
      "role": "container",
      "widget": "frog.ui.standard.panel",
      "layout": { "x": 0, "y": 0, "width": 500, "height": 300 },
      "props": {
        "visible": true
      },
      "children": [
        {
          "id": "ctrl_name",
          "role": "control",
          "widget": "frog.ui.standard.string_control",
          "value_type": "string",
          "layout": { "x": 20, "y": 20, "width": 180, "height": 28 },
          "props": {
            "default_value": "operator_1"
          },
          "parts": {
            "label": {
              "class": "frog.ui.standard.label_part",
              "props": {
                "text": "Operator",
                "visible": true
              }
            }
          }
        }
      ]
    }
  ]
}</pre>

<hr/>

<h2 id="summary">14. Summary</h2>

<p>
The front panel defines the interaction layer of a Frog through a structured widget-based model:
</p>

<ul>
  <li><strong>widgets</strong> — serialized widget instances defined by <code>Widget.md</code>,</li>
  <li><strong>bindings</strong> — explicit links to interface ports or diagram ports,</li>
  <li><strong>layout</strong> — geometry and visual ordering,</li>
  <li><strong>style</strong> — themes, fonts, colors, references, and overrides,</li>
  <li><strong>ui_libraries</strong> — reusable widget vocabularies.</li>
</ul>

<p>
The front panel is part of the canonical source format, but it is not the public contract and not the execution logic of the Frog.
</p>

<p>
It exists to define how users see and interact with a Frog, while remaining cleanly separated from interface semantics, widget semantics, and dataflow execution.
</p>
