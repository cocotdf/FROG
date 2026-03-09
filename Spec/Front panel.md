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
  <li><a href="#value-participation-in-the-diagram">8. Value Participation in the Diagram</a></li>
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
  <li><a href="#runtime-considerations">12. Runtime Considerations</a></li>
  <li><a href="#out-of-scope">13. Out of Scope for v0.1</a></li>
  <li><a href="#validation-rules">14. Validation Rules</a></li>
  <li><a href="#examples">15. Examples</a></li>
  <li><a href="#summary">16. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <strong>front_panel</strong> section defines the graphical interaction layer of a FROG program.
It describes the user-facing UI composition of the program.
</p>

<p>
The front panel is composed of <strong>widget instances</strong>.
These widgets may provide user input, display program state, organize layout,
or contribute purely visual decoration.
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
  <li>consistent object-based widget composition,</li>
  <li>modular styling through themes, variables, shared styles, and overrides,</li>
  <li>extensible UI composition through standard and library-defined widgets,</li>
  <li>compatibility with efficient runtimes and partial redraw strategies.</li>
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
It describes how widgets are arranged, configured, composed, and styled.
</p>

<p>
The object model of widgets is defined normatively by <code>Widget.md</code>.
This document does not redefine widget inheritance, widget roles, widget parts,
widget references, or widget property semantics.
Instead, it defines how widget instances are composed inside the <code>front_panel</code> section.
</p>

<p>
Value-carrying widgets participate in the diagram through the implicit terminal model defined by <code>Widget.md</code>.
This means the front panel does not need a separate binding section for base value interaction.
</p>

<p>
In short:
</p>

<ul>
  <li><strong>interface</strong> = what the FROG exposes,</li>
  <li><strong>diagram</strong> = how the FROG works,</li>
  <li><strong>widget model</strong> = what UI objects are,</li>
  <li><strong>front_panel</strong> = how those UI objects are placed, configured, and presented.</li>
</ul>

<hr/>

<h2 id="front-panel-structure">5. Front Panel Structure</h2>

<p>
Recommended structure:
</p>

<pre><code>"front_panel": {
  "canvas": {},
  "widgets": [],
  "style": {},
  "ui_libraries": []
}</code></pre>

<p>
Fields:
</p>

<ul>
  <li><code>canvas</code> — coordinate system and visual background,</li>
  <li><code>widgets</code> — widget instances serialized according to <code>Widget.md</code>,</li>
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
Child widgets of a container use the local content coordinate system of their parent container,
unless a stricter profile defines additional composition rules.
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
Canonical source serialization SHOULD store design-time configuration and optional initial or default state,
not arbitrary runtime state snapshots.
</p>

<hr/>

<h2 id="value-participation-in-the-diagram">8. Value Participation in the Diagram</h2>

<p>
Value-carrying widgets participate in the executable diagram through the implicit terminal model defined in <code>Widget.md</code>.
</p>

<p>
Conceptually:
</p>

<pre><code>Front panel widget
        │
        ▼
widget.value
        │
        ▼
diagram terminal</code></pre>

<p>
This means:
</p>

<ul>
  <li>a control may provide a value to the diagram through its implicit <code>value</code> terminal,</li>
  <li>an indicator may receive a value from the diagram through its implicit <code>value</code> terminal,</li>
  <li>the front panel itself does not need to serialize separate base value bindings.</li>
</ul>

<p>
If a FROG author wants a widget value to influence public interface behavior,
that relationship is expressed in the diagram by wiring widget terminals and interface terminals,
not by a front panel binding object.
</p>

<p>
Likewise, if a widget must reflect an internal computed value,
that relationship is also expressed in the diagram.
</p>

<p>
Richer widget interactions such as property access, method calls, part access,
or event handling belong to the widget-reference and diagram mechanisms,
not to the base <code>front_panel</code> serialization model.
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
They <strong>MUST NOT</strong> affect execution semantics, scheduling, type rules,
or public interface behavior.
</p>

<p>
For top-level widgets, coordinates are interpreted in canvas space.
For child widgets, coordinates are interpreted in parent-local space.
The exact clipping, padding, and advanced responsive layout behavior are implementation-defined
unless standardized by a stricter profile.
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

<h2 id="runtime-considerations">12. Runtime Considerations</h2>

<p>
Although <code>front_panel</code> is a source-level UI description,
it is intended to remain compatible with efficient runtime implementations.
</p>

<p>
In particular, implementations MAY use:
</p>

<ul>
  <li>retained widget trees,</li>
  <li>incremental layout updates,</li>
  <li>dirty-region rendering,</li>
  <li>batched visual invalidation,</li>
  <li>cached text and graphics resources.</li>
</ul>

<p>
These runtime strategies do not change source semantics.
They are implementation concerns enabled by the clear separation between:
</p>

<ul>
  <li>design-time widget description,</li>
  <li>runtime widget state,</li>
  <li>rendering state.</li>
</ul>

<hr/>

<h2 id="out-of-scope">13. Out of Scope for v0.1</h2>

<p>
The following topics are outside the strict scope of the base v0.1 front panel serialization model:
</p>

<ul>
  <li>full industrial UI toolkit standardization,</li>
  <li>event structure serialization for widget events,</li>
  <li>general-purpose property node and method node serialization inside <code>front_panel</code>,</li>
  <li>arbitrary runtime UI state snapshotting,</li>
  <li>advanced responsive layout systems, docking systems, or constraint solvers,</li>
  <li>full accessibility standardization,</li>
  <li>animation and visual effect systems.</li>
</ul>

<p>
These features MAY be defined later by the diagram model,
by dedicated UI interaction specifications,
or by stricter profiles.
</p>

<hr/>

<h2 id="validation-rules">14. Validation Rules</h2>

<p>
Implementations <strong>MUST</strong> enforce:
</p>

<ul>
  <li><code>front_panel</code> <strong>MUST</strong> exist in a canonical <code>.frog</code> file,</li>
  <li>if present, <code>widgets</code> <strong>MUST</strong> be an array,</li>
  <li>widget identifiers <strong>MUST</strong> be unique within the front panel scope,</li>
  <li>all widget instances <strong>MUST</strong> be valid according to <code>Widget.md</code>,</li>
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
  <li>a value-carrying widget MAY exist in the front panel even if it is not wired in the diagram, subject to tool diagnostics,</li>
  <li>tools MAY warn when a control or indicator appears unused in the diagram,</li>
  <li>tools MAY warn when a decoration widget carries unexpected value-related fields.</li>
</ul>

<hr/>

<h2 id="examples">15. Examples</h2>

<h3>15.1 Minimal front panel</h3>

<pre><code>"front_panel": {
  "canvas": {
    "units": "px",
    "width": 600,
    "height": 400,
    "background": { "color": "#FFFFFF" }
  },
  "widgets": [],
  "style": {},
  "ui_libraries": []
}</code></pre>

<h3>15.2 Front panel with control, indicator, and decoration widgets</h3>

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

<h3>15.3 Container widget with child widgets</h3>

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

<h3>15.4 Note about diagram participation</h3>

<p>
The following relationships are not serialized in <code>front_panel</code> itself,
but are expressed in the diagram:
</p>

<pre><code>ctrl_gain.value  → internal node input
internal result  → ind_result.value
ctrl_gain.value  → interface input path
interface output path → ind_result.value</code></pre>

<hr/>

<h2 id="summary">16. Summary</h2>

<p>
The front panel defines the interaction layer of a FROG through a structured widget-based model:
</p>

<ul>
  <li><strong>widgets</strong> — serialized widget instances defined by <code>Widget.md</code>,</li>
  <li><strong>layout</strong> — geometry and visual ordering,</li>
  <li><strong>style</strong> — themes, fonts, colors, variables, shared styles, references, and overrides,</li>
  <li><strong>ui_libraries</strong> — reusable widget vocabularies.</li>
</ul>

<p>
The front panel is part of the canonical source format,
but it is not the public contract and not the execution logic of the FROG.
</p>

<p>
It defines how users see and interact with a FROG,
while remaining cleanly separated from interface semantics,
widget semantics,
and dataflow execution.
</p>

<p>
In the base model, value interaction is achieved through the implicit widget terminal model,
not through explicit front panel binding objects.
</p>
