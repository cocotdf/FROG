<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">FROG Front Panel</h1>

<p align="center">
  <strong>Normative source model for front-panel composition, widget placement, and source-persisted presentation metadata</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope">2. Scope</a></li>
  <li><a href="#ownership-boundary">3. Ownership Boundary</a></li>
  <li><a href="#location-in-a-frog-file">4. Location in a <code>.frog</code> File</a></li>
  <li><a href="#front-panel-structure">5. Front Panel Structure</a></li>
  <li><a href="#widget-instances">6. Widget Instances</a></li>
  <li><a href="#composition-and-nesting">7. Composition and Nesting</a></li>
  <li><a href="#canvas-metadata">8. Canvas Metadata</a></li>
  <li><a href="#presentation-metadata-boundary">9. Presentation Metadata Boundary</a></li>
  <li><a href="#face-template-reference">10. Face Template Reference</a></li>
  <li><a href="#svg-template-posture">11. SVG Template Posture</a></li>
  <li><a href="#relation-with-the-diagram">12. Relation with the Diagram</a></li>
  <li><a href="#validation-rules">13. Validation Rules</a></li>
  <li><a href="#minimal-v01-front-panel-posture-for-the-first-executable-slice">14. Minimal v0.1 Front-Panel Posture for the First Executable Slice</a></li>
  <li><a href="#summary">15. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <code>front_panel</code> section defines the source-level declaration of the user-facing widget composition of a FROG.
It is the canonical source home of the serialized widget tree.
</p>

<p>
The front panel may include:
</p>

<ul>
  <li>canvas metadata,</li>
  <li>widget instances,</li>
  <li>source-persisted presentation metadata associated with those widget instances,</li>
  <li>optional UI library references.</li>
</ul>

<p>
The front panel does not define executable graph semantics.
The diagram remains the authoritative executable graph of the FROG.
</p>

<hr/>

<h2 id="scope">2. Scope</h2>

<p>
This document standardizes:
</p>

<ul>
  <li>the top-level source shape of the <code>front_panel</code> section,</li>
  <li>widget-tree ownership at source level,</li>
  <li>canvas and placement metadata,</li>
  <li>the boundary between composition metadata and executable meaning,</li>
  <li>the source-persistence posture of presentation members such as <code>face_color</code> and <code>face_template</code>.</li>
</ul>

<p>
This document does not standardize:
</p>

<ul>
  <li>public interface semantics,</li>
  <li>diagram executable semantics,</li>
  <li>widget class member legality,</li>
  <li>diagram-side interaction primitive semantics,</li>
  <li>one mandatory rendering toolkit.</li>
</ul>

<hr/>

<h2 id="ownership-boundary">3. Ownership Boundary</h2>

<p>
<code>Front panel.md</code> owns:
</p>

<ul>
  <li>source-level panel composition,</li>
  <li>source-level widget containment,</li>
  <li>source-level placement and canvas metadata,</li>
  <li>source-persisted presentation metadata carried by widget instances when the class contract allows it.</li>
</ul>

<p>
<code>Front panel.md</code> does not own:
</p>

<ul>
  <li>public interface semantics,</li>
  <li>executable graph semantics,</li>
  <li>widget instance-object semantics beyond source serialization,</li>
  <li>widget class member-contract semantics,</li>
  <li>widget interaction primitive semantics,</li>
  <li>general language execution semantics,</li>
  <li>repository-wide version-transition law.</li>
</ul>

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
When absent, the FROG is interpreted as having no serialized front-panel composition.
This does not affect the validity of the program as an executable FROG.
</p>

<hr/>

<h2 id="front-panel-structure">5. Front Panel Structure</h2>

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
  <li><code>canvas</code> — optional design-time panel or coordinate-space metadata,</li>
  <li><code>widgets</code> — top-level widget instances of the front panel,</li>
  <li><code>ui_libraries</code> — optional list of UI libraries or namespaces referenced by the panel.</li>
</ul>

<p>
All fields are optional.
If present, they MUST follow the declared structure.
Presentation metadata for a widget instance belongs inside that widget instance, typically under source-owned instance fields such as <code>props</code>, not as a separate top-level front-panel semantic layer.
</p>

<hr/>

<h2 id="widget-instances">6. Widget Instances</h2>

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
  "id": "ctrl_count",
  "role": "control",
  "widget": "frog.ui.standard.numeric_control",
  "value_type": "u16",
  "layout": {
    "x": 20,
    "y": 24,
    "width": 140,
    "height": 32
  },
  "props": {
    "caption": "Count",
    "face_color": "#D0D0D0",
    "face_template": {
      "kind": "resource",
      "family": "svg_static_template_v1",
      "path": "./assets/widgets/u16_numeric_control_face.svg"
    }
  }
}
</code></pre>

<p>
The front panel serializes widget instances as source objects.
It does not redefine widget class semantics, member legality, member accessibility, or class-side part contracts already owned by <code>Widget.md</code> and <code>Widget class contract.md</code>.
</p>

<hr/>

<h2 id="composition-and-nesting">7. Composition and Nesting</h2>

<p>
The front panel defines a widget tree.
</p>

<p>
Top-level widgets appear in <code>front_panel.widgets</code>.
Container widgets MAY define child widgets using the <code>children</code> field.
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
The first executable slice does not require nesting.
It uses two top-level widgets only.
</p>

<hr/>

<h2 id="canvas-metadata">8. Canvas Metadata</h2>

<p>
The optional <code>canvas</code> object carries design-time panel geometry or coordinate-space metadata.
</p>

<p>
Example:
</p>

<pre><code>"canvas": {
  "width": 460,
  "height": 180
}
</code></pre>

<p>
Canvas metadata:
</p>

<ul>
  <li>MAY guide designer layout,</li>
  <li>MAY guide host window sizing or preview sizing,</li>
  <li>MUST NOT by itself define execution semantics.</li>
</ul>

<hr/>

<h2 id="presentation-metadata-boundary">9. Presentation Metadata Boundary</h2>

<p>
A widget instance MAY contain source-persisted presentation metadata when its widget class contract allows it.
</p>

<p>
Typical examples include:
</p>

<ul>
  <li><code>caption</code>,</li>
  <li><code>face_color</code>,</li>
  <li><code>border_color</code>,</li>
  <li><code>text_color</code>,</li>
  <li><code>face_template</code>.</li>
</ul>

<p>
For the first executable slice, such metadata SHOULD normally be serialized inside <code>props</code>.
</p>

<p>
Presentation metadata:
</p>

<ul>
  <li>MUST remain source-owned composition or presentation metadata,</li>
  <li>MUST remain subordinate to widget class legality,</li>
  <li>MUST remain distinct from diagram-side executable interaction,</li>
  <li>MUST NOT by itself create execution semantics.</li>
</ul>

<hr/>

<h2 id="face-template-reference">10. Face Template Reference</h2>

<p>
A widget class MAY support a persisted presentation-template reference such as <code>face_template</code>.
</p>

<p>
When present in source, such a member:
</p>

<ul>
  <li>MUST be treated as source-persisted presentation metadata,</li>
  <li>SHOULD be design-time-visible,</li>
  <li>MUST NOT by itself create executable semantics,</li>
  <li>MUST NOT change the widget role, primary value contract, or class identity,</li>
  <li>and MAY be ignored by a host that does not support the referenced template family.</li>
</ul>

<p>
For the minimal executable widget family, a face-template reference is carried as:
</p>

<pre><code>{
  "face_template": {
    "kind": "resource",
    "family": "svg_static_template_v1",
    "path": "./assets/widgets/u16_numeric_control_face.svg"
  }
}
</code></pre>

<p>
The <code>family</code> field identifies the expected template interpretation family.
For the first executable slice, the recommended family is <code>svg_static_template_v1</code>.
</p>

<hr/>

<h2 id="svg-template-posture">11. SVG Template Posture</h2>

<p>
When <code>face_template</code> references an SVG resource, that SVG is a presentation asset, not executable truth.
</p>

<p>
Accordingly, an SVG face template:
</p>

<ul>
  <li>MAY provide a designer preview or host skin,</li>
  <li>MAY define stable named visual layers or anchors for rendering-oriented tooling,</li>
  <li>MUST NOT define widget executable semantics,</li>
  <li>MUST NOT create hidden methods, events, or dataflow meaning,</li>
  <li>MUST NOT replace the widget class contract as the normative owner of widget behavior.</li>
</ul>

<p>
The following distinction MUST remain explicit:
</p>

<pre><code>front_panel composition
    !=
widget executable interaction
    !=
presentation metadata
</code></pre>

<hr/>

<h2 id="relation-with-the-diagram">12. Relation with the Diagram</h2>

<p>
The front panel does not define executable behavior.
The diagram remains the authoritative executable graph of the FROG.
</p>

<p>
Widget participation in program execution is expressed in the diagram, not in the front panel itself.
The canonical diagram interaction mechanisms are:
</p>

<ul>
  <li><code>widget_value</code> nodes — natural access to a widget primary value,</li>
  <li><code>widget_reference</code> nodes — object-style access anchor,</li>
  <li><code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code> — executable interaction primitives when standardized and allowed.</li>
</ul>

<p>
A source-persisted member such as <code>face_template</code> does not become executable interaction merely because it is present in the widget instance source.
</p>

<hr/>

<h2 id="validation-rules">13. Validation Rules</h2>

<p>
Validators MUST verify at least that:
</p>

<ul>
  <li><code>front_panel</code>, when present, follows the canonical object shape,</li>
  <li><code>widgets</code>, when present, is an array,</li>
  <li>widget identifiers are unique across the full widget tree,</li>
  <li>each widget instance is structurally valid,</li>
  <li>persisted presentation metadata is recognized by the active widget class contract,</li>
  <li><code>face_template</code> values, when present, follow the published template-reference source shape,</li>
  <li>presentation metadata is not misinterpreted as executable semantics.</li>
</ul>

<hr/>

<h2 id="minimal-v01-front-panel-posture-for-the-first-executable-slice">14. Minimal v0.1 Front-Panel Posture for the First Executable Slice</h2>

<p>
The first executable slice uses one minimal front panel containing:
</p>

<ul>
  <li>one top-level numeric control widget,</li>
  <li>one top-level numeric indicator widget,</li>
  <li>one canvas object,</li>
  <li>and source-persisted presentation metadata in <code>props</code>.</li>
</ul>

<p>
The required presentation properties for that slice are:
</p>

<ul>
  <li><code>caption</code>,</li>
  <li><code>face_color</code>,</li>
  <li><code>face_template</code>.</li>
</ul>

<p>
The front panel therefore provides a serious but bounded face-plate corridor suitable for:
</p>

<ul>
  <li>designer visibility,</li>
  <li>host realization,</li>
  <li>and example portability across the source-to-execution corridor,</li>
</ul>

<p>
without allowing the serialized face to redefine execution semantics.
</p>

<hr/>

<h2 id="summary">15. Summary</h2>

<p>
This document defines the canonical source model for front-panel composition.
</p>

<p>
For the first executable slice, it stabilizes:
</p>

<ul>
  <li>one two-widget panel composition,</li>
  <li>one bounded source-owned presentation metadata posture,</li>
  <li>one explicit SVG-backed <code>face_template</code> resource shape,</li>
  <li>and one strict separation between front-panel persistence and executable graph meaning.</li>
</ul>
