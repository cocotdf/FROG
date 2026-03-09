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
  <li><a href="#location">3. Location in a <code>.frog</code> File</a></li>
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
      <li><a href="#shared-styles">10.4 Shared Styles, References, and Overrides</a></li>
    </ul>
  </li>
  <li><a href="#ui-libraries">11. UI Libraries</a></li>
  <li><a href="#out-of-scope">12. Out of Scope for v0.1</a></li>
  <li><a href="#validation-rules">13. Validation Rules</a></li>
  <li><a href="#examples">14. Examples</a></li>
  <li><a href="#summary">15. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <strong>front_panel</strong> section defines the graphical interaction layer of a FROG program.
It describes the user-facing UI composition of the program.
</p>

<p>
The front panel is composed of <strong>widget instances</strong>.
These widgets may provide user input, display program state, organize layout, or contribute purely visual decoration.
</p>

<p>
The <code>front_panel</code> section is part of the canonical <code>.frog</code> source format.
It <strong>MUST</strong> exist, even when a FROG is executed in a headless or non-interactive context.
</p>

<p>
The front panel does <strong>not</strong> define execution logic and does <strong>not</strong> define the public contract of the FROG.
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
  <li>explicit and auditable binding rules,</li>
  <li>consistent object-based widget composition,</li>
  <li>modular styling through themes, variables, shared styles, and overrides,</li>
  <li>extensible UI composition through standard and library-defined widgets.</li>
</ul>

<hr/>

<h2 id="location">3. Location in a <code>.frog</code> File</h2>

<pre><code>{
  "spec_version": "0.1",
  "metadata": {},
  "interface": {},
  "connector": {},
  "diagram": {},
  "front_panel": {}
}</code></pre>

<p>
The <code>front_panel</code> section <strong>MUST</strong> exist in a canonical <code>.frog</code> source file.
It MAY be empty.
</p>

<hr/>

<h2 id="relationship-with-interface-diagram-and-widget-model">4. Relationship with Interface, Diagram, and Widget Model</h2>

<p>
FROG distinguishes the following concepts:
</p>

<ul>
  <li><strong>interface</strong> — defines the public logical contract of the FROG,</li>
  <li><strong>diagram</strong> — defines the executable dataflow logic,</li>
  <li><strong>front_panel</strong> — defines the user interaction layer,</li>
  <li><strong>widget model</strong> — defines what a widget is and how widgets behave as UI objects.</li>
</ul>

<p>
The front panel <strong>MUST NOT</strong> be interpreted as the public API of the FROG.
Controls and indicators are user-facing widgets, not public logical ports.
</p>

<p>
The front panel also does not redefine execution semantics.
It describes how widgets are arranged and how their primary value interaction is bound to interface ports or diagram targets.
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
  <li><strong>interface</strong> = what the FROG exposes,</li>
  <li><strong>diagram</strong> = how the FROG works,</li>
  <li><strong>widget model</strong> = what UI objects are,</li>
  <li><strong>front_panel</strong> = how those UI objects are placed and bound for user interaction.</li>
</ul>

<hr/>

<h2 id="front-panel-structure">5. Front Panel Structure</h2>

<p>
Recommended structure:
</p>

<pre><code>"front_panel": {
  "canvas": {},
  "widgets": [],
  "bindings": [],
  "style": {},
  "ui_libraries": []
}</code></pre>

<p>
Fields:
</p>

<ul>
  <li><code>canvas</code> — coordinate system and visual background,</li>
  <li><code>widgets</code> — widget instances serialized according to <code>Widget.md</code>,</li>
  <li><code>bindings</code> — explicit value bindings from widgets to interface or diagram targets,</li>
  <li><code>style</code> — theme, fonts, colors, variables, and reusable style definitions,</li>
  <li><code>ui_libraries</code> — references to external UI widget libraries.</li>
</ul>

<p>
All fields are optional unless otherwise constrained by validation rules.
An empty front panel is valid.
</p>

<p>
The <code>widgets</code> array is the canonical container for top-level widget instances in v0.1.
Nested widgets, when used, are owned through the <code>children</code> field of container widgets.
</p>

<hr/>

<h2 id="canvas-and-coordinate-system">6. Canvas and Coordinate System</h2>

<p>
The canvas defines the design-time coordinate system used by front panel widgets.
</p>

<pre><code>"canvas": {
  "units": "px",
  "width": 900,
  "height": 600,
  "background": {
    "color": "#FFFFFF"
  }
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>units</code> SHOULD be <code>px</code> in v0.1.</li>
  <li><code>width</code> and <code>height</code> SHOULD be integers.</li>
  <li>The background is purely visual and <strong>MUST NOT</strong> affect execution semantics.</li>
</ul>

<p>
The canvas provides a coordinate space only.
It does not define widget class semantics, type behavior, or execution behavior.
</p>

<p>
Top-level widgets use the canvas coordinate system.
Child widgets of a container use the local content coordinate system of their parent container unless a stricter profile defines additional composition rules.
</p>

<hr/>

<h2 id="widget-instances">7. Widget Instances</h2>

<p>
All user-facing UI objects in the front panel are represented as widget instances.
</p>

<p>
Each entry in <code>widgets</code> <strong>MUST</strong> follow the widget instance model defined in <code>Widget.md</code>.
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
  <li><code>parts</code> when applicable,</li>
  <li><code>children</code> when applicable.</li>
</ul>

<p>
Example widget instance:
</p>

<pre><code>{
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
}</code></pre>

<p>
This document does not classify widgets by ad hoc element kinds outside the widget model.
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

<p>
Canonical source serialization SHOULD store design-time configuration and optional initial/default state, not arbitrary runtime state snapshots.
</p>

<hr/>

<h2 id="bindings">8. Bindings</h2>

<p>
Bindings connect widget instances to interface ports or diagram targets.
Bindings <strong>MUST</strong> be explicit.
</p>

<p>
In v0.1, a front panel binding represents a <strong>primary value binding</strong>.
It binds the main value channel of a value-carrying widget to a program-facing target.
It does not standardize arbitrary widget property, part, method, or event binding.
</p>

<p>
Recommended binding structure:
</p>

<pre><code>"bindings": [
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
]</code></pre>

<p>
Fields:
</p>

<ul>
  <li><code>widget</code> — identifier of the bound widget instance,</li>
  <li><code>mode</code> — value interaction mode such as <code>read</code> or <code>write</code>,</li>
  <li><code>target</code> — binding destination in interface space or diagram space.</li>
</ul>

<p>
Target forms:
</p>

<ul>
  <li><strong>Interface target</strong>: <code>{ "scope": "interface", "port": "name" }</code></li>
  <li><strong>Diagram target</strong>: <code>{ "scope": "diagram", "node": "node_id", "port": "port_name" }</code></li>
</ul>

<h3>8.1 Binding semantics</h3>

<p>
A front panel binding is defined at the level of the widget's primary value interaction:
</p>

<ul>
  <li>for a control, this is normally the user-editable value flowing from UI toward the program,</li>
  <li>for an indicator, this is normally the displayed value flowing from the program toward the UI.</li>
</ul>

<p>
This document deliberately does not require a literal serialized member name such as <code>value</code> in front panel bindings.
The binding is semantic rather than reflective.
</p>

<p>
If an implementation needs explicit property-level access such as reading or writing <code>value</code>, <code>label.text</code>, or invoking widget methods, those interactions belong to the diagram-level mechanisms and not to the base front panel binding model of v0.1.
</p>

<h3>8.2 Binding mode</h3>

<p>
Allowed binding modes in v0.1 are:
</p>

<ul>
  <li><code>read</code></li>
  <li><code>write</code></li>
</ul>

<p>
Interpretation:
</p>

<ul>
  <li><code>read</code> means the widget receives a value from the bound target for presentation,</li>
  <li><code>write</code> means the widget provides a value to the bound target.</li>
</ul>

<p>
A stricter profile MAY introduce additional modes such as bidirectional synchronization, but such behavior is outside the base specification in v0.1.
</p>

<h3>8.3 Binding rules</h3>

<ul>
  <li>Each binding <strong>MUST</strong> reference an existing widget id.</li>
  <li>Each binding <strong>MUST</strong> reference a valid target according to its scope.</li>
  <li>Bindings <strong>MUST</strong> be type-compatible.</li>
  <li>Only value-carrying widgets SHOULD participate in primary value bindings.</li>
  <li>Controls SHOULD use <code>write</code> bindings when they provide values to the program.</li>
  <li>Indicators SHOULD use <code>read</code> bindings when they display values from the program.</li>
  <li>Decoration widgets SHOULD NOT use primary value bindings.</li>
  <li>Container widgets SHOULD NOT use primary value bindings in v0.1 unless a stricter profile explicitly defines such behavior.</li>
</ul>

<h3>8.4 Multiple bindings</h3>

<p>
In v0.1, a value-carrying widget SHOULD have at most one primary value binding.
Multiple bindings targeting the same widget primary value channel are invalid unless a stricter profile explicitly defines their semantics.
</p>

<p>
The binding model defines interaction wiring only.
It <strong>MUST NOT</strong> introduce additional execution semantics.
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
  <li><code>z</code> (optional) — drawing order among siblings,</li>
  <li><code>anchor</code> (optional) — responsive behavior hint.</li>
</ul>

<p>
Example:
</p>

<pre><code>"layout": {
  "x": 20,
  "y": 20,
  "width": 120,
  "height": 28,
  "z": 10,
  "anchor": "top_left"
}</code></pre>

<p>
Layout fields are design-time and rendering-oriented.
They <strong>MUST NOT</strong> affect execution semantics, scheduling, type rules, or public interface behavior.
</p>

<p>
For top-level widgets, coordinates are interpreted in canvas space.
For child widgets, coordinates are interpreted in parent-local space.
The exact clipping, padding, and advanced responsive layout behavior are implementation-defined unless standardized by a stricter profile.
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
  <li>style variables,</li>
  <li>shared named styles,</li>
  <li>local overrides.</li>
</ul>

<h3 id="theme">10.1 Theme</h3>

<pre><code>"style": {
  "theme": "default"
}</code></pre>

<p>
A theme identifies a coherent visual preset.
Theme selection is visual only and <strong>MUST NOT</strong> affect program semantics.
</p>

<h3 id="fonts">10.2 Fonts</h3>

<pre><code>"style": {
  "fonts": {
    "default": { "family": "Inter", "size": 12, "weight": 400 },
    "title": { "family": "Inter", "size": 20, "weight": 700 }
  }
}</code></pre>

<p>
Fonts define reusable typography presets for front panel rendering.
</p>

<h3 id="colors-and-variables">10.3 Colors and Variables</h3>

<pre><code>"style": {
  "colors": {
    "bg": "#FFFFFF",
    "fg": "#111111",
    "accent": "#2ECC71"
  },
  "variables": {
    "corner_radius": 4,
    "control_height": 28
  }
}</code></pre>

<p>
Implementations MAY support additional style variables or token systems under stricter profiles.
</p>

<h3 id="shared-styles">10.4 Shared Styles, References, and Overrides</h3>

<p>
The style object MAY define reusable named styles.
Widget instances MAY reference shared style definitions and MAY override them locally.
</p>

<pre><code>"style": {
  "theme": "default",
  "styles": {
    "default.control": {
      "colors": {
        "accent": "#2ECC71"
      }
    },
    "default.title": {
      "font": "title"
    }
  }
}</code></pre>

<p>
Example widget using a shared style:
</p>

<pre><code>{
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
}</code></pre>

<p>
Style information is non-semantic and <strong>MUST NOT</strong> affect execution behavior.
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

<pre><code>"ui_libraries": [
  {
    "name": "frog.ui.standard",
    "version": "0.1.0"
  }
]</code></pre>

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

<h2 id="out-of-scope">12. Out of Scope for v0.1</h2>

<p>
The following topics are outside the strict scope of the base v0.1 front panel serialization model:
</p>

<ul>
  <li>full industrial UI toolkit standardization,</li>
  <li>event structure serialization for widget events,</li>
  <li>general-purpose property node and method node serialization inside <code>front_panel</code>,</li>
  <li>arbitrary runtime UI state snapshotting,</li>
  <li>advanced responsive layout systems, docking systems, or constraint solvers,</li>
  <li>bidirectional synchronization semantics beyond the basic <code>read</code> and <code>write</code> binding model.</li>
</ul>

<p>
These features MAY be defined later by the diagram model, by dedicated UI interaction specifications, or by stricter profiles.
</p>

<hr/>

<h2 id="validation-rules">13. Validation Rules</h2>

<p>
Implementations <strong>MUST</strong> enforce:
</p>

<ul>
  <li><code>front_panel</code> <strong>MUST</strong> exist in a canonical <code>.frog</code> file,</li>
  <li>if present, <code>widgets</code> <strong>MUST</strong> be an array,</li>
  <li>widget identifiers <strong>MUST</strong> be unique within the front panel scope,</li>
  <li>all widget instances <strong>MUST</strong> be valid according to <code>Widget.md</code>,</li>
  <li>all bindings <strong>MUST</strong> reference valid widget ids,</li>
  <li>all bindings <strong>MUST</strong> reference valid targets according to their declared scope,</li>
  <li>bindings <strong>MUST</strong> be type-compatible with their targets,</li>
  <li>if present, <code>canvas</code> <strong>MUST</strong> be an object,</li>
  <li>if present, <code>style</code> <strong>MUST</strong> be an object,</li>
  <li>if present, <code>ui_libraries</code> <strong>MUST</strong> be an array,</li>
  <li>widget layouts <strong>MUST</strong> contain valid numeric coordinates when layout is present,</li>
  <li>unknown front panel properties <strong>MUST NOT</strong> affect execution semantics.</li>
</ul>

<p>
Additionally:
</p>

<ul>
  <li>an empty <code>front_panel</code> section is valid,</li>
  <li>style and UI library information <strong>MUST</strong> remain non-authoritative for execution,</li>
  <li>tools MAY warn when a control uses a <code>read</code> binding,</li>
  <li>tools MAY warn when an indicator uses a <code>write</code> binding,</li>
  <li>tools MAY warn when a decoration or container widget participates in a primary value binding.</li>
</ul>

<hr/>

<h2 id="examples">14. Examples</h2>

<h3>14.1 Minimal front panel</h3>

<pre><code>"front_panel": {
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
}</code></pre>

<h3>14.2 Control and indicator bound to the public interface</h3>

<pre><code>"front_panel": {
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
        "text": "Example FROG",
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
    },
    "styles": {
      "default.control": {},
      "default.indicator": {},
      "default.title": { "font": "title" }
    }
  },
  "ui_libraries": [
    { "name": "frog.ui.standard", "version": "0.1.0" }
  ]
}</code></pre>

<h3>14.3 Indicator bound to an internal diagram target</h3>

<pre><code>"front_panel": {
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
}</code></pre>

<h3>14.4 Container widget with child widgets</h3>

<pre><code>"front_panel": {
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
}</code></pre>

<hr/>

<h2 id="summary">15. Summary</h2>

<p>
The front panel defines the interaction layer of a FROG through a structured widget-based model:
</p>

<ul>
  <li><strong>widgets</strong> — serialized widget instances defined by <code>Widget.md</code>,</li>
  <li><strong>bindings</strong> — explicit primary value links to interface ports or diagram targets,</li>
  <li><strong>layout</strong> — geometry and visual ordering,</li>
  <li><strong>style</strong> — themes, fonts, colors, variables, shared styles, references, and overrides,</li>
  <li><strong>ui_libraries</strong> — reusable widget vocabularies.</li>
</ul>

<p>
The front panel is part of the canonical source format, but it is not the public contract and not the execution logic of the FROG.
</p>

<p>
It exists to define how users see and interact with a FROG, while remaining cleanly separated from interface semantics, widget semantics, and dataflow execution.
</p>
