<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">FROG Front Panel Specification</h1>

<p align="center">
  <strong>Definition of the optional <code>front_panel</code> section of <code>.frog</code> programs</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope">2. Scope</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#location-in-a-frog-file">4. Location in a <code>.frog</code> File</a></li>
  <li><a href="#front-panel-ownership">5. Front Panel Ownership</a></li>
  <li><a href="#front-panel-structure">6. Front Panel Structure</a></li>
  <li><a href="#widget-instances">7. Widget Instances</a></li>
  <li><a href="#composition-and-nesting">8. Composition and Nesting</a></li>
  <li><a href="#layout-and-canvas">9. Layout and Canvas</a></li>
  <li><a href="#relation-with-the-diagram">10. Relation with the Diagram</a></li>
  <li><a href="#relation-with-the-public-interface">11. Relation with the Public Interface</a></li>
  <li><a href="#validation-rules">12. Validation Rules</a></li>
  <li><a href="#examples">13. Examples</a></li>
  <li><a href="#summary">14. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <code>front_panel</code> section defines the optional user-facing interaction surface of a FROG program.
</p>

<p>
It declares widget instances and their visual composition in canonical source. A FROG MAY include a front panel, but it is not required. A program MAY therefore be purely diagram-based with no serialized user-facing UI composition.
</p>

<p>
The front panel defines:
</p>

<ul>
  <li>widget instances,</li>
  <li>their containment structure,</li>
  <li>their visual composition,</li>
  <li>their design-time layout information.</li>
</ul>

<p>
The front panel does not define:
</p>

<ul>
  <li>the public interface of the FROG,</li>
  <li>the authoritative executable dataflow graph,</li>
  <li>runtime scheduling semantics,</li>
  <li>the general language execution semantics,</li>
  <li>the full widget class contract,</li>
  <li>the full executable interaction model for widgets.</li>
</ul>

<p>
Those responsibilities belong respectively to:
</p>

<ul>
  <li><code>Interface.md</code>,</li>
  <li><code>Diagram.md</code>,</li>
  <li>the normative execution semantics defined in <code>Language/</code>,</li>
  <li><code>Widget class contract.md</code>,</li>
  <li><code>Widget interaction.md</code>.</li>
</ul>

<p>
This document also does not define repository-wide version policy. Top-level <code>spec_version</code> identifies the source-format compatibility target of the containing <code>.frog</code> file, while the published specification corpus version remains governed centrally in <code>Versioning/Readme.md</code>.
</p>

<hr/>

<h2 id="scope">2. Scope</h2>

<p>
This document defines the canonical source representation of the <code>front_panel</code> section when it appears in a <code>.frog</code> file.
</p>

<p>
It specifies:
</p>

<ul>
  <li>how widget instances are declared in the front panel,</li>
  <li>how those widget instances are composed into a widget tree,</li>
  <li>how design-time layout and panel-level composition data are serialized,</li>
  <li>the structural validation rules for the section.</li>
</ul>

<p>
This document intentionally does not standardize:
</p>

<ul>
  <li>the full widget object model,</li>
  <li>the full class-level widget contract,</li>
  <li>the full executable interaction model for widgets,</li>
  <li>a complete UI toolkit,</li>
  <li>a complete theme or styling system,</li>
  <li>pixel-perfect cross-runtime rendering,</li>
  <li>the repository-wide version-transition doctrine.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<ul>
  <li><code>Widget.md</code> defines the widget instance model, including roles, value-carrying behavior, parts, properties, methods, events, and widget identity.</li>
  <li><code>Widget class contract.md</code> defines the class-level widget contract, including members, part ownership, member legality, access modes, and IDE-facing object exposure constraints.</li>
  <li><code>Widget interaction.md</code> defines diagram-side object-style interaction with widgets.</li>
  <li><code>Diagram.md</code> defines the authoritative executable graph.</li>
  <li><code>Interface.md</code> defines the public contract of the FROG.</li>
  <li><code>Type.md</code> defines the value type system used by value-carrying widgets and typed widget members.</li>
  <li><code>Versioning/Readme.md</code> defines the centralized distinction between specification corpus version, top-level <code>spec_version</code>, and program artifact versioning.</li>
</ul>

<p>
Accordingly:
</p>

<ul>
  <li>interface defines public program inputs and outputs,</li>
  <li>diagram defines executable behavior,</li>
  <li>widget model defines instance-side widget-object shape,</li>
  <li>widget class contract defines class-side member legality and object exposure,</li>
  <li>front_panel defines UI composition and serialized widget placement,</li>
  <li>the centralized versioning surface defines repository-wide version-transition doctrine.</li>
</ul>

<p>
Ownership boundary:
</p>

<pre><code>Front panel.md owns:
- optional UI composition
- widget tree serialization
- panel-level layout/canvas structure
- source-level containment of widgets

Front panel.md does not own:
- public interface semantics
- executable graph semantics
- widget instance-object semantics
- widget class member-contract semantics
- widget interaction primitive semantics
- general language execution semantics
- repository-wide version-transition law
</code></pre>

<hr/>

<h2 id="location-in-a-frog-file">4. Location in a <code>.frog</code> File</h2>

<p>
When present, the front panel appears as an optional top-level section of a <code>.frog</code> file.
</p>

<pre><code>{
  "spec_version": "0.1",
  "metadata": {},
  "interface": {},
  "diagram": {},
  "front_panel": {}
}
</code></pre>

<p>
The <code>front_panel</code> section is optional.
</p>

<p>
When absent, the FROG is interpreted as having no serialized front-panel composition. This does not affect the validity of the program as an executable FROG.
</p>

<p>
In this source shape:
</p>

<ul>
  <li>top-level <code>spec_version</code> identifies the source-format compatibility target of the file,</li>
  <li><code>front_panel</code> defines optional UI composition only,</li>
  <li>the published specification corpus version remains governed centrally in <code>Versioning/Readme.md</code>.</li>
</ul>

<hr/>

<h2 id="front-panel-ownership">5. Front Panel Ownership</h2>

<p>
The <code>front_panel</code> section owns the source-level declaration of the user-facing widget composition. It is the canonical source home for the widget tree of the user-facing panel.
</p>

<p>
However, the <code>front_panel</code> section is not authoritative for:
</p>

<ul>
  <li>program execution,</li>
  <li>public API definition,</li>
  <li>type-system definition,</li>
  <li>widget-object interaction semantics,</li>
  <li>class-side widget member legality.</li>
</ul>

<p>
A practical interpretation rule is:
</p>

<pre><code>If the question is:
- What is displayed and how widgets are composed? -> Front panel.md
- What is the widget as an instance-side object?  -> Widget.md
- What members does the class expose legally?     -> Widget class contract.md
- How does execution use the widget?              -> Diagram.md / Widget interaction.md
- What is the public API of the FROG?             -> Interface.md
</code></pre>

<hr/>

<h2 id="front-panel-structure">6. Front Panel Structure</h2>

<p>
The canonical structure of the front panel object is:
</p>

<pre><code>"front_panel": {
  "canvas": {},
  "widgets": [],
  "ui_libraries": []
}
</code></pre>

<p>
Fields:
</p>

<ul>
  <li><code>canvas</code> — optional design-time panel or coordinate-space metadata.</li>
  <li><code>widgets</code> — top-level widget instances of the front panel.</li>
  <li><code>ui_libraries</code> — optional list of UI libraries or namespaces referenced by the panel.</li>
</ul>

<p>
All fields are optional. If present, they MUST follow the declared structure.
</p>

<p>
The absence of a field does not transfer its responsibility elsewhere. It only means the corresponding information is omitted from source.
</p>

<hr/>

<h2 id="widget-instances">7. Widget Instances</h2>

<p>
Widgets are declared as instances following the widget model defined in <code>Widget.md</code>.
</p>

<p>
Typical widget fields include:
</p>

<ul>
  <li><code>id</code>,</li>
  <li><code>widget</code> (widget class),</li>
  <li><code>role</code>,</li>
  <li><code>value_type</code> when applicable,</li>
  <li><code>layout</code>,</li>
  <li><code>props</code>,</li>
  <li><code>parts</code>,</li>
  <li><code>children</code>.</li>
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
  }
}
</code></pre>

<p>
The front panel serializes widget instances as source objects. It does not redefine widget class semantics, member legality, member accessibility, or class-side part contracts already owned by <code>Widget.md</code> and <code>Widget class contract.md</code>.
</p>

<hr/>

<h2 id="composition-and-nesting">8. Composition and Nesting</h2>

<p>
The front panel defines a widget tree.
</p>

<p>
Top-level widgets appear in <code>front_panel.widgets</code>. Container widgets MAY define child widgets using the <code>children</code> field.
</p>

<p>
Rules:
</p>

<ul>
  <li>widget identifiers MUST be unique across the full recursive widget tree,</li>
  <li>a widget MUST belong to exactly one container position in the serialized tree,</li>
  <li>container ownership MUST be explicit in source,</li>
  <li>child widgets MUST appear only under widgets whose class and role permit containment.</li>
</ul>

<p>
Conceptually:
</p>

<pre><code>front_panel
   |
   +-- widgets[]
         |
         +-- widget
         |     |
         |     +-- children[]
         |             |
         |             +-- child widget
         |
         +-- widget
         |
         +-- widget
</code></pre>

<p>
The front panel therefore owns the composition tree, while individual widget semantics remain owned by the widget model and class-side member legality remains owned by the widget class contract.
</p>

<hr/>

<h2 id="layout-and-canvas">9. Layout and Canvas</h2>

<p>
The <code>front_panel</code> section MAY include panel-level and widget-level design-time layout information.
</p>

<p>
Typical responsibilities include:
</p>

<ul>
  <li>panel coordinate-space metadata,</li>
  <li>widget positions,</li>
  <li>widget dimensions,</li>
  <li>containment-based placement context.</li>
</ul>

<p>
This information is design-time composition data. It MUST NOT redefine execution semantics, widget-object semantics, widget class member semantics, or public interface semantics.
</p>

<p>
The front panel does not require every implementation to render identically. The serialized meaning is structural and compositional, not pixel-perfect renderer identity.
</p>

<hr/>

<h2 id="relation-with-the-diagram">10. Relation with the Diagram</h2>

<p>
The front panel does not define executable behavior. The diagram remains the authoritative executable graph of the FROG.
</p>

<p>
Widget participation in program execution is expressed in the diagram, not in the front panel itself.
</p>

<p>
The canonical diagram interaction mechanisms are:
</p>

<ul>
  <li><code>widget_value</code> nodes — natural access to a widget primary value,</li>
  <li><code>widget_reference</code> nodes — object-style widget access anchors.</li>
</ul>

<p>
Object-style interaction occurs through standardized primitives such as:
</p>

<ul>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
</ul>

<p>
These mechanisms are defined in <code>Widget interaction.md</code> together with the relevant widget and library specifications. Their legality against a given widget class depends on the corresponding class contract.
</p>

<p>
The relationship can be summarized as:
</p>

<pre><code>front_panel
   |
   +-- declares widget instance
            |
            +-- diagram may reference it through widget_value
            |
            +-- diagram may reference it through widget_reference
                     |
                     +-- frog.ui.property_read
                     +-- frog.ui.property_write
                     +-- frog.ui.method_invoke

front_panel declares UI composition
diagram declares executable interaction
widget class contract constrains legal object access
</code></pre>

<hr/>

<h2 id="relation-with-the-public-interface">11. Relation with the Public Interface</h2>

<p>
The front panel is independent from the public interface of the FROG.
</p>

<p>
A widget does not become a public API port merely because it exists in the front panel. Likewise, a public interface port does not require a corresponding widget.
</p>

<p>
This means:
</p>

<ul>
  <li>a FROG MAY have public interface ports with no serialized front-panel widgets,</li>
  <li>a FROG MAY have front-panel widgets that do not correspond to public interface ports,</li>
  <li>the public contract remains defined canonically by <code>interface</code> and by its executable materialization in the diagram.</li>
</ul>

<p>
The front panel is therefore optional UI composition, not API definition.
</p>

<hr/>

<h2 id="validation-rules">12. Validation Rules</h2>

<p>
If the <code>front_panel</code> section exists, validators MUST ensure:
</p>

<ul>
  <li>the section is a JSON object,</li>
  <li><code>widgets</code> is an array when present,</li>
  <li><code>canvas</code> is an object when present,</li>
  <li><code>ui_libraries</code> is an array when present,</li>
  <li>widget identifiers are unique across the full recursive widget tree,</li>
  <li>all widget instances conform to <code>Widget.md</code>,</li>
  <li>child widgets appear only under valid container ownership,</li>
  <li>a widget appears at exactly one place in the serialized tree.</li>
</ul>

<p>
Optional fields MUST follow their declared structure when present.
</p>

<p>
The front panel MUST NOT redefine:
</p>

<ul>
  <li>public interface semantics,</li>
  <li>diagram semantics,</li>
  <li>class-side widget member legality,</li>
  <li>language execution semantics.</li>
</ul>

<p>
Validators SHOULD diagnose at least the following error classes:
</p>

<ul>
  <li>duplicate widget identifier,</li>
  <li>invalid widget structure,</li>
  <li>invalid container ownership,</li>
  <li>unknown widget class under the active profile,</li>
  <li>invalid child placement under a non-container widget.</li>
</ul>

<p>
These checks validate optional UI-composition structure.
They do not, by themselves, redefine top-level <code>spec_version</code> policy or repository-wide corpus-version governance.
</p>

<hr/>

<h2 id="examples">13. Examples</h2>

<h3>13.1 Minimal Front Panel</h3>

<pre><code>"front_panel": {
  "widgets": []
}
</code></pre>

<h3>13.2 Front Panel with One Widget</h3>

<pre><code>"front_panel": {
  "widgets": [
    {
      "id": "ctrl_gain",
      "role": "control",
      "widget": "frog.ui.standard.numeric_control",
      "value_type": "f64",
      "layout": {
        "x": 20,
        "y": 20,
        "width": 120,
        "height": 28
      }
    }
  ]
}
</code></pre>

<h3>13.3 Front Panel with Container and Children</h3>

<pre><code>"front_panel": {
  "canvas": {
    "width": 800,
    "height": 600
  },
  "widgets": [
    {
      "id": "main_panel",
      "role": "container",
      "widget": "frog.ui.standard.panel",
      "layout": {
        "x": 0,
        "y": 0,
        "width": 800,
        "height": 600
      },
      "children": [
        {
          "id": "ctrl_gain",
          "role": "control",
          "widget": "frog.ui.standard.numeric_control",
          "value_type": "f64",
          "layout": {
            "x": 20,
            "y": 20,
            "width": 120,
            "height": 28
          }
        },
        {
          "id": "ind_ready",
          "role": "indicator",
          "widget": "frog.ui.standard.boolean_indicator",
          "value_type": "bool",
          "layout": {
            "x": 20,
            "y": 70,
            "width": 120,
            "height": 28
          }
        }
      ]
    }
  ]
}
</code></pre>

<hr/>

<h2 id="summary">14. Summary</h2>

<p>
The <code>front_panel</code> section is the optional canonical source home of user-facing widget composition in a FROG program.
</p>

<p>
It defines:
</p>

<ul>
  <li>which widget instances exist on the panel,</li>
  <li>how they are serialized,</li>
  <li>how they are nested,</li>
  <li>how their design-time layout is represented.</li>
</ul>

<p>
It does not define:
</p>

<ul>
  <li>the public interface,</li>
  <li>the authoritative executable graph,</li>
  <li>the class-side widget contract,</li>
  <li>the executable widget interaction model,</li>
  <li>general language execution semantics,</li>
  <li>source-format compatibility law,</li>
  <li>published specification corpus versioning.</li>
</ul>

<p>
Keeping that boundary explicit allows FROG to support rich panel composition without turning UI layout, one IDE, or one runtime into the hidden source of execution truth.
</p>
