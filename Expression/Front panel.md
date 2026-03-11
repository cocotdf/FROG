<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="150" />
</p>

<h1 align="center">🐸 FROG Front Panel Specification</h1>

<p align="center">
  Definition of the front panel for <strong>.frog</strong> programs<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#design-goals">2. Design Goals</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#location-in-a-frog-file">4. Location in a .frog File</a></li>
  <li><a href="#front-panel-structure">5. Front Panel Structure</a></li>
  <li><a href="#canvas-and-coordinate-system">6. Canvas and Coordinate System</a></li>
  <li><a href="#widget-instances">7. Widget Instances</a></li>
  <li><a href="#composition-and-nesting">8. Composition and Nesting</a></li>
  <li><a href="#relation-with-the-diagram">9. Relation with the Diagram</a></li>
  <li><a href="#object-style-widget-interaction">10. Object-Style Widget Interaction</a></li>
  <li><a href="#layout-model">11. Layout Model</a></li>
  <li><a href="#style-system">12. Style System</a></li>
  <li><a href="#ui-libraries">13. UI Libraries</a></li>
  <li><a href="#runtime-considerations">14. Runtime Considerations</a></li>
  <li><a href="#out-of-scope-for-v01">15. Out of Scope for v0.1</a></li>
  <li><a href="#validation-rules">16. Validation Rules</a></li>
  <li><a href="#examples">17. Examples</a></li>
  <li><a href="#summary">18. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <code>front_panel</code> section defines the graphical interaction layer of a FROG.
It describes the user-facing composition of widgets, their layout, and their visual presentation.
</p>

<p>
The front panel is composed of widget instances.
These widgets MAY:
</p>

<ul>
  <li>provide user input,</li>
  <li>display values or program state,</li>
  <li>organize visual composition,</li>
  <li>provide purely decorative or informational UI elements.</li>
</ul>

<p>
The <code>front_panel</code> section is part of the canonical <code>.frog</code> source format.
It MUST exist, even when a FROG is executed in a headless or non-interactive context.
It MAY be empty.
</p>

<p>
The front panel does not define:
</p>

<ul>
  <li>the public logical contract of the FROG,</li>
  <li>the executable graph of the FROG,</li>
  <li>the runtime scheduling model,</li>
  <li>the semantics of public interface ports.</li>
</ul>

<p>
Its role is interaction, presentation, visualization, and UI organization.
Runtimes MAY ignore the front panel during non-interactive execution.
Editors, design tools, and interactive runtimes MAY use it to render and manage a user interface.
</p>

<hr/>

<h2 id="design-goals">2. Design Goals</h2>

<ul>
  <li><strong>Tool-agnostic representation</strong> — the front panel MUST remain independent from any single editor implementation.</li>
  <li><strong>Stable widget serialization</strong> — widget instances MUST have durable source representation.</li>
  <li><strong>Separation of concerns</strong> — public contract, executable logic, widget object model, and UI composition MUST remain distinct.</li>
  <li><strong>Consistent composition</strong> — widgets MUST be composed through a structured widget model rather than ad hoc visual primitives.</li>
  <li><strong>Non-semantic presentation</strong> — layout and style MUST remain presentation concerns and MUST NOT alter execution semantics.</li>
  <li><strong>Extensibility</strong> — the model SHOULD support both standard widgets and library-defined specialized widgets.</li>
  <li><strong>Runtime compatibility</strong> — the source model SHOULD remain compatible with efficient interactive implementations.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
The front panel specification is intentionally narrow in scope and depends on other specifications for semantics it does not own.
</p>

<ul>
  <li><code>Interface.md</code> defines the public logical contract of the FROG.</li>
  <li><code>Diagram.md</code> defines the executable dataflow graph.</li>
  <li><code>Widget.md</code> defines what a widget is, including roles, value semantics, parts, properties, and methods.</li>
  <li><code>Widget interaction.md</code> defines diagram-side object-style widget access.</li>
  <li><code>Type.md</code> defines the type system used by value-carrying widgets.</li>
</ul>

<p>
Therefore:
</p>

<ul>
  <li><code>interface</code> = what the FROG exposes publicly,</li>
  <li><code>diagram</code> = how the FROG executes,</li>
  <li><code>widget model</code> = what UI objects are,</li>
  <li><code>front_panel</code> = how those UI objects are declared, composed, and presented.</li>
</ul>

<p>
The front panel MUST NOT be interpreted as the public API of the FROG.
Controls and indicators are user-facing widgets, not public logical interface ports.
</p>

<p>
Likewise, the front panel does not redefine execution semantics.
It declares widget instances and presentation-related information only.
</p>

<hr/>

<h2 id="location-in-a-frog-file">4. Location in a .frog File</h2>

<p>
The <code>front_panel</code> section appears as a top-level object in the canonical <code>.frog</code> source file.
</p>

<pre><code>{
  "spec_version": "0.1",
  "metadata": {},
  "interface": {},
  "connector": {},
  "diagram": {},
  "front_panel": {}
}</code></pre>

<p>
The <code>front_panel</code> section MUST exist in a canonical <code>.frog</code> source file.
It MAY be empty.
</p>

<hr/>

<h2 id="front-panel-structure">5. Front Panel Structure</h2>

<p>
The canonical front-panel object SHOULD use the following structure:
</p>

<pre><code>"front_panel": {
  "canvas": {},
  "widgets": [],
  "style": {},
  "ui_libraries": []
}</code></pre>

<p>
Field meaning:
</p>

<ul>
  <li><code>canvas</code> — design-time coordinate system and optional visual background,</li>
  <li><code>widgets</code> — top-level widget instances,</li>
  <li><code>style</code> — visual theme, typography, palettes, variables, and reusable style definitions,</li>
  <li><code>ui_libraries</code> — declarations of external UI widget vocabularies used by the front panel.</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li><code>front_panel</code> MUST be an object,</li>
  <li><code>widgets</code> MUST be an array when present,</li>
  <li><code>canvas</code> MUST be an object when present,</li>
  <li><code>style</code> MUST be an object when present,</li>
  <li><code>ui_libraries</code> MUST be an array when present.</li>
</ul>

<p>
The <code>widgets</code> array is the canonical container for top-level widget instances in v0.1.
Nested widgets, when used, are owned through the <code>children</code> field of container widgets.
</p>

<hr/>

<h2 id="canvas-and-coordinate-system">6. Canvas and Coordinate System</h2>

<p>
The <code>canvas</code> object defines the design-time coordinate space used by top-level widgets.
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
  <li><code>units</code> SHOULD be <code>"px"</code> in base v0.1,</li>
  <li><code>width</code> and <code>height</code> SHOULD be integers,</li>
  <li><code>background</code> is visual only and MUST NOT affect execution semantics.</li>
</ul>

<p>
The canvas provides a coordinate space only.
It does not define widget semantics, value semantics, or execution behavior.
</p>

<p>
Top-level widgets use the canvas coordinate system.
Child widgets of a container use the local content coordinate system of their parent container unless a stricter profile defines additional composition rules.
</p>

<hr/>

<h2 id="widget-instances">7. Widget Instances</h2>

<p>
All user-facing UI objects in the front panel are represented as widget instances.
Each entry in <code>widgets</code> MUST follow the widget instance model defined by <code>Widget.md</code>.
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
  <li><code>children</code> when applicable,</li>
  <li><code>style_ref</code> when applicable,</li>
  <li><code>style_override</code> when applicable.</li>
</ul>

<p>
Example:
</p>

<pre><code>{
  "id": "ctrl_gain",
  "role": "control",
  "widget": "frog.ui.standard.numeric_control",
  "value_type": "f64",
  "layout": {
    "x": 20,
    "y": 20,
    "width": 120,
    "height": 28
  },
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
A front panel MAY contain:
</p>

<ul>
  <li>value-carrying widgets such as controls and indicators,</li>
  <li>container widgets,</li>
  <li>decoration widgets,</li>
  <li>library-defined specialized widgets allowed by the active profile.</li>
</ul>

<p>
Canonical source serialization SHOULD store design-time configuration and optional default state,
not arbitrary runtime state snapshots.
</p>

<hr/>

<h2 id="composition-and-nesting">8. Composition and Nesting</h2>

<p>
The front panel is a widget tree.
</p>

<p>
Top-level widgets are stored in <code>front_panel.widgets</code>.
Container widgets MAY own child widgets through a <code>children</code> array.
</p>

<p>
Example:
</p>

<pre><code>{
  "id": "main_panel",
  "role": "container",
  "widget": "frog.ui.standard.panel",
  "layout": {
    "x": 0,
    "y": 0,
    "width": 500,
    "height": 300
  },
  "props": {
    "visible": true
  },
  "children": [
    {
      "id": "ctrl_name",
      "role": "control",
      "widget": "frog.ui.standard.string_control",
      "value_type": "string",
      "layout": {
        "x": 20,
        "y": 20,
        "width": 180,
        "height": 28
      },
      "props": {
        "default_value": "operator_1"
      }
    }
  ]
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li>all widget identifiers MUST be unique across the full recursive front-panel widget tree,</li>
  <li>a child widget belongs to exactly one parent container,</li>
  <li>non-container widgets MUST NOT own children unless a stricter profile explicitly allows it,</li>
  <li>ownership and composition MUST remain explicit in source.</li>
</ul>

<hr/>

<h2 id="relation-with-the-diagram">9. Relation with the Diagram</h2>

<p>
The front panel does not contain executable bindings.
The diagram is the authoritative place where widget participation becomes part of program behavior.
</p>

<p>
For ordinary primary-value wiring:
</p>

<ul>
  <li>a control MAY provide its primary value to the diagram,</li>
  <li>an indicator MAY receive its primary value from the diagram,</li>
  <li>that participation is represented canonically by <code>widget_value</code> nodes in the diagram.</li>
</ul>

<p>
Conceptually:
</p>

<pre><code>Front panel widget
        │
        ▼
widget.value
        │
        ▼
widget_value node
        │
        ▼
diagram dataflow</code></pre>

<p>
Therefore:
</p>

<ul>
  <li>the front panel does not need a separate base-value binding section,</li>
  <li>relationships between widget values and public interface behavior are expressed in the diagram,</li>
  <li>relationships between widget values and internal computed values are also expressed in the diagram.</li>
</ul>

<p>
The front panel declares widget objects.
The diagram decides whether the program uses their primary values, their object references, or both.
</p>

<hr/>

<h2 id="object-style-widget-interaction">10. Object-Style Widget Interaction</h2>

<p>
Richer widget interactions do not belong to the base <code>front_panel</code> serialization model.
They belong to the diagram-level widget interaction model.
</p>

<p>
This includes:
</p>

<ul>
  <li>property reads,</li>
  <li>property writes,</li>
  <li>method invocation,</li>
  <li>widget-part access,</li>
  <li>future event-related interaction.</li>
</ul>

<p>
In particular:
</p>

<ul>
  <li><code>widget_value</code> is the natural path for the primary widget value,</li>
  <li><code>widget_reference</code> is the explicit object-style path,</li>
  <li><code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code> are diagram-side primitives, not front-panel serialization constructs.</li>
</ul>

<p>
A widget MAY expose its primary value both naturally through <code>widget_value</code> and as a property through the object-style path when the widget class allows it.
</p>

<hr/>

<h2 id="layout-model">11. Layout Model</h2>

<p>
Layout defines widget geometry and visual ordering.
It is a design-time and rendering-oriented concern.
</p>

<p>
Typical layout fields include:
</p>

<ul>
  <li><code>x</code>, <code>y</code> — position,</li>
  <li><code>width</code>, <code>height</code> — size,</li>
  <li><code>z</code> — optional drawing order among siblings,</li>
  <li><code>anchor</code> — optional responsive behavior hint.</li>
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
Rules:
</p>

<ul>
  <li>layout fields, when present, SHOULD use numeric coordinates and dimensions appropriate for the active UI profile,</li>
  <li>layout MUST NOT affect execution semantics, scheduling, type rules, or public interface behavior,</li>
  <li>top-level widget coordinates are interpreted in canvas space,</li>
  <li>child widget coordinates are interpreted in parent-local space.</li>
</ul>

<p>
Advanced clipping, docking, constraint solving, and responsive layout behavior remain outside base v0.1 unless standardized by a stricter profile.
</p>

<hr/>

<h2 id="style-system">12. Style System</h2>

<p>
The style system provides modular visual definitions for front-panel rendering.
Style information is non-semantic and MUST NOT affect execution behavior.
</p>

<p>
The <code>style</code> object MAY define:
</p>

<ul>
  <li>themes,</li>
  <li>font presets,</li>
  <li>color palettes,</li>
  <li>style variables,</li>
  <li>shared named styles,</li>
  <li>local overrides.</li>
</ul>

<h3>12.1 Theme</h3>

<pre><code>"style": {
  "theme": "default"
}</code></pre>

<p>
A theme identifies a coherent visual preset.
Theme selection is visual only.
</p>

<h3>12.2 Fonts</h3>

<pre><code>"style": {
  "fonts": {
    "default": { "family": "Inter", "size": 12, "weight": 400 },
    "title": { "family": "Inter", "size": 20, "weight": 700 }
  }
}</code></pre>

<p>
Fonts define reusable typography presets for front-panel rendering.
</p>

<h3>12.3 Colors and Variables</h3>

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

<h3>12.4 Shared Styles, References, and Overrides</h3>

<p>
The <code>style</code> object MAY define reusable named styles.
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
Rules:
</p>

<ul>
  <li><code>style_ref</code> MUST reference an existing named shared style when present,</li>
  <li><code>style_override</code> MUST remain visual only,</li>
  <li>style inheritance or merging strategy MAY be profile-defined, but MUST NOT alter widget semantics.</li>
</ul>

<hr/>

<h2 id="ui-libraries">13. UI Libraries</h2>

<p>
Front panels MAY reference external UI widget libraries.
This enables modular widget vocabularies beyond the minimal built-in set.
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
  <li>UI libraries MAY define additional widget classes, parts, and styling systems,</li>
  <li>widgets serialized in the front panel SHOULD be resolvable against the active built-in set or declared UI libraries,</li>
  <li>runtimes MAY ignore UI libraries for pure non-interactive execution,</li>
  <li>editors and interactive runtimes MAY use UI libraries to reconstruct specialized visual behavior.</li>
</ul>

<p>
This document does not standardize package discovery, remote fetching, or compatibility resolution between UI library versions.
</p>

<hr/>

<h2 id="runtime-considerations">14. Runtime Considerations</h2>

<p>
Although <code>front_panel</code> is a source-level UI description, it is intended to remain compatible with efficient interactive runtime implementations.
</p>

<p>
Implementations MAY use:
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
They are implementation concerns enabled by the separation between:
</p>

<ul>
  <li>design-time widget description,</li>
  <li>runtime widget state,</li>
  <li>rendering state.</li>
</ul>

<hr/>

<h2 id="out-of-scope-for-v01">15. Out of Scope for v0.1</h2>

<p>
The following topics are outside the strict scope of the base v0.1 front-panel serialization model:
</p>

<ul>
  <li>full industrial UI toolkit standardization,</li>
  <li>event-structure serialization for widget events,</li>
  <li>general-purpose property-node and method-node serialization inside <code>front_panel</code>,</li>
  <li>arbitrary runtime UI state snapshotting,</li>
  <li>advanced responsive layout systems, docking systems, or constraint solvers,</li>
  <li>full accessibility standardization,</li>
  <li>animation and visual effect systems.</li>
</ul>

<p>
These features MAY be defined later by the diagram model, by dedicated UI interaction specifications, or by stricter profiles.
</p>

<hr/>

<h2 id="validation-rules">16. Validation Rules</h2>

<p>
Implementations MUST enforce the following base rules:
</p>

<ul>
  <li><code>front_panel</code> MUST exist in a canonical <code>.frog</code> file,</li>
  <li>if present, <code>widgets</code> MUST be an array,</li>
  <li>all widget identifiers MUST be unique across the full recursive front-panel widget tree,</li>
  <li>all widget instances MUST be valid according to <code>Widget.md</code>,</li>
  <li>if present, <code>canvas</code> MUST be an object,</li>
  <li>if present, <code>style</code> MUST be an object,</li>
  <li>if present, <code>ui_libraries</code> MUST be an array,</li>
  <li>widget layouts MUST contain valid numeric coordinates when layout is present,</li>
  <li>child widgets MUST appear only under valid container ownership unless a stricter profile explicitly allows otherwise,</li>
  <li>serialized parts MUST use valid part names and valid part classes for the owning widget class or active profile,</li>
  <li><code>style_ref</code> MUST reference an existing named style when present,</li>
  <li><code>style_override</code> MUST remain visual only,</li>
  <li>front-panel serialization MUST NOT be used to redefine public interface semantics, diagram semantics, or widget interaction semantics.</li>
</ul>

<p>
Validators SHOULD diagnose at least the following error classes:
</p>

<ul>
  <li>duplicate widget identifier,</li>
  <li>unknown widget class,</li>
  <li>invalid role for widget class,</li>
  <li>missing <code>value_type</code> on a value-carrying widget,</li>
  <li>invalid child ownership,</li>
  <li>unknown part name,</li>
  <li>invalid part class,</li>
  <li>invalid layout geometry,</li>
  <li>unknown style reference,</li>
  <li>invalid non-object <code>props</code>, <code>parts</code>, or <code>style_override</code>.</li>
</ul>

<hr/>

<h2 id="examples">17. Examples</h2>

<h3>17.1 Minimal front panel</h3>

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

<h3>17.2 Front panel with control, indicator, and decoration widgets</h3>

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

<h3>17.3 Container widget with child widgets</h3>

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

<h3>17.4 Specialized widget from an external UI library</h3>

<pre><code>"front_panel": {
  "widgets": [
    {
      "id": "graph_1",
      "role": "indicator",
      "widget": "frog.ui.extended.waveform_graph",
      "value_type": "array&lt;f64&gt;",
      "layout": { "x": 20, "y": 160, "width": 420, "height": 240 },
      "parts": {
        "label": {
          "class": "frog.ui.standard.label_part",
          "props": {
            "text": "Signal",
            "visible": true
          }
        },
        "x_scale": {
          "class": "frog.ui.extended.scale_part",
          "props": {
            "visible": true
          }
        },
        "y_scale": {
          "class": "frog.ui.extended.scale_part",
          "props": {
            "visible": true
          }
        }
      }
    }
  ],
  "ui_libraries": [
    { "name": "frog.ui.standard", "version": "0.1.0" },
    { "name": "frog.ui.extended", "version": "0.1.0" }
  ]
}</code></pre>

<hr/>

<h2 id="summary">18. Summary</h2>

<p>
The front panel defines the interaction layer of a FROG through a structured widget-based model.
</p>

<ul>
  <li>Widgets are declared as widget instances defined by <code>Widget.md</code>.</li>
  <li>Composition is expressed through top-level widgets and container-owned children.</li>
  <li>Layout defines geometry and visual ordering only.</li>
  <li>Style defines themes, fonts, colors, variables, shared styles, and overrides.</li>
  <li>UI libraries allow reusable widget vocabularies beyond the minimal built-in set.</li>
  <li>Ordinary widget value participation is represented canonically in the diagram through <code>widget_value</code>.</li>
  <li>Object-style widget access is represented canonically in the diagram through <code>widget_reference</code> and <code>frog.ui.*</code> primitives.</li>
  <li>The front panel does not define the public API and does not define executable bindings.</li>
</ul>

<p>
This keeps the UI model explicit, durable, and editor-friendly while preserving a clean separation from interface semantics and execution semantics.
</p>
