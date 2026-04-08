<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Front Panel</h1>

<p align="center">
  <strong>Normative source model for front-panel composition, widget instances, placement, and source-owned presentation references</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope">2. Scope</a></li>
  <li><a href="#architectural-position">3. Architectural Position</a></li>
  <li><a href="#ownership-boundary">4. Ownership Boundary</a></li>
  <li><a href="#location-in-a-frog-file">5. Location in a <code>.frog</code> File</a></li>
  <li><a href="#front-panel-structure">6. Front-Panel Structure</a></li>
  <li><a href="#widget-instances">7. Widget Instances</a></li>
  <li><a href="#composition-and-nesting">8. Composition and Nesting</a></li>
  <li><a href="#canvas-metadata">9. Canvas Metadata</a></li>
  <li><a href="#source-persisted-presentation-metadata">10. Source-Persisted Presentation Metadata</a></li>
  <li><a href="#widget-asset-references">11. Widget Asset References</a></li>
  <li><a href="#svg-visual-posture">12. SVG Visual Posture</a></li>
  <li><a href="#relation-with-the-diagram">13. Relation with the Diagram</a></li>
  <li><a href="#relation-with-widget-class-law">14. Relation with Widget Class Law</a></li>
  <li><a href="#relation-with-wfrog-packages">15. Relation with <code>.wfrog</code> Packages</a></li>
  <li><a href="#validation-rules">16. Validation Rules</a></li>
  <li><a href="#minimal-v01-posture">17. Minimal v0.1 Posture</a></li>
  <li><a href="#example">18. Example</a></li>
  <li><a href="#summary">19. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <code>front_panel</code> section defines the canonical source-level declaration of the user-facing widget composition of a FROG.
It is the source home of the serialized widget tree, placement metadata, canvas metadata, and source-owned presentation references associated with widget instances.
</p>

<p>
The front panel may declare:
</p>

<ul>
  <li>which widget instances exist,</li>
  <li>where they are placed,</li>
  <li>how they are nested,</li>
  <li>which source-owned instance properties are persisted,</li>
  <li>which widget-oriented assets are referenced by those instances.</li>
</ul>

<p>
The front panel does not define executable graph semantics.
The diagram remains the authoritative executable graph of the FROG.
</p>

<p>
The front panel also does not define full widget class law and does not define host rendering internals.
Those concerns belong to distinct specification layers.
</p>

<hr/>

<h2 id="scope">2. Scope</h2>

<p>
This document standardizes:
</p>

<ul>
  <li>the top-level source shape of the <code>front_panel</code> section,</li>
  <li>source ownership of widget composition,</li>
  <li>source ownership of widget containment and placement,</li>
  <li>canvas metadata,</li>
  <li>the source-persistence posture of instance-level presentation properties,</li>
  <li>the source-level posture of widget-oriented asset references,</li>
  <li>the architectural boundary between front-panel serialization and execution semantics.</li>
</ul>

<p>
This document does not standardize:
</p>

<ul>
  <li>public interface semantics,</li>
  <li>diagram execution semantics,</li>
  <li>the full class-level legality of widget properties, methods, events, and parts,</li>
  <li>diagram-side UI interaction primitive semantics,</li>
  <li>one mandatory rendering toolkit,</li>
  <li>pixel-identical rendering across hosts.</li>
</ul>

<hr/>

<h2 id="architectural-position">3. Architectural Position</h2>

<p>
The front panel is a source-owned composition layer.
It sits beside, but not above, the diagram.
</p>

<p>
The required architectural distinction is:
</p>

<pre><code>front_panel serialization
    !=
widget class law
    !=
diagram executable interaction
    !=
runtime-private live widget structures
    !=
host rendering strategy
</code></pre>

<p>
This distinction is mandatory.
If these layers are blurred, source persistence, object legality, runtime interpretation, and rendering portability become difficult to reason about and difficult to validate.
</p>

<hr/>

<h2 id="ownership-boundary">4. Ownership Boundary</h2>

<p>
<code>Front panel.md</code> owns:
</p>

<ul>
  <li>source-level panel composition,</li>
  <li>source-level widget containment,</li>
  <li>source-level placement and canvas metadata,</li>
  <li>source-persisted instance metadata when allowed by the widget class contract,</li>
  <li>source-visible references to widget-oriented assets.</li>
</ul>

<p>
<code>Front panel.md</code> does not own:
</p>

<ul>
  <li>public interface meaning,</li>
  <li>diagram executable semantics,</li>
  <li>complete widget class legality,</li>
  <li>object-style interaction primitive law,</li>
  <li>runtime-private live object structure,</li>
  <li>host-private rendering internals.</li>
</ul>

<hr/>

<h2 id="location-in-a-frog-file">5. Location in a <code>.frog</code> File</h2>

<p>
When present, the front panel appears as an optional top-level section of a <code>.frog</code> file.
</p>

<pre><code>{
  "spec_version": "0.1",
  "metadata": {},
  "interface": {},
  "diagram": {},
  "front_panel": {}
}</code></pre>

<p>
The <code>front_panel</code> section is optional.
When absent, the FROG is interpreted as having no serialized front-panel composition.
This does not affect the validity of the FROG as an executable program.
</p>

<hr/>

<h2 id="front-panel-structure">6. Front-Panel Structure</h2>

<p>
The canonical source shape of the front panel object is:
</p>

<pre><code>"front_panel": {
  "canvas": {},
  "widgets": [],
  "ui_libraries": []
}</code></pre>

<p>
Fields:
</p>

<ul>
  <li><code>canvas</code> — optional design-time panel or coordinate-space metadata,</li>
  <li><code>widgets</code> — top-level widget instances of the panel,</li>
  <li><code>ui_libraries</code> — optional list of UI libraries, package families, or namespaces referenced by the panel.</li>
</ul>

<p>
All fields are optional.
If present, they MUST follow the declared structure.
Widget instance metadata belongs inside widget instances, not in a separate front-panel semantic layer.
</p>

<hr/>

<h2 id="widget-instances">7. Widget Instances</h2>

<p>
Widgets are serialized as source-level instances following the widget instance model defined in <code>Widget.md</code>.
</p>

<p>
Typical widget instance fields include:
</p>

<ul>
  <li><code>id</code>,</li>
  <li><code>role</code>,</li>
  <li><code>class_ref</code>,</li>
  <li><code>value_type</code> when applicable,</li>
  <li><code>layout</code>,</li>
  <li><code>props</code>,</li>
  <li><code>parts</code>,</li>
  <li><code>children</code>,</li>
  <li><code>widget_assets</code>.</li>
</ul>

<p>
Example:
</p>

<pre><code>{
  "id": "ctrl_count",
  "role": "control",
  "class_ref": "frog.ui.standard.numeric_control",
  "value_type": "u16",
  "layout": {
    "x": 20,
    "y": 24,
    "width": 140,
    "height": 32
  },
  "props": {
    "caption": "Count",
    "face_color": "#D0D0D0"
  },
  "widget_assets": {
    "class_package": "./ui/classes/standard-numeric.wfrog",
    "realization_package": "./ui/realizations/default-theme.wfrog"
  }
}</code></pre>

<p>
The front panel serializes widget instances as source objects.
It does not redefine widget class semantics, member legality, member accessibility, or class-side part contracts.
</p>

<hr/>

<h2 id="composition-and-nesting">8. Composition and Nesting</h2>

<p>
The front panel defines a widget tree.
Top-level widgets appear in <code>front_panel.widgets</code>.
Container widgets MAY define child widgets through <code>children</code>.
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
A runtime or host MAY realize the same source composition using a different internal rendering structure, but that does not change source-owned containment.
</p>

<hr/>

<h2 id="canvas-metadata">9. Canvas Metadata</h2>

<p>
The optional <code>canvas</code> object carries design-time panel geometry or coordinate-space metadata.
</p>

<p>
Example:
</p>

<pre><code>"canvas": {
  "width": 460,
  "height": 170
}</code></pre>

<p>
Canvas metadata:
</p>

<ul>
  <li>MAY guide designer layout,</li>
  <li>MAY guide preview sizing,</li>
  <li>MAY guide initial host window sizing,</li>
  <li>MUST NOT define execution semantics by itself.</li>
</ul>

<hr/>

<h2 id="source-persisted-presentation-metadata">10. Source-Persisted Presentation Metadata</h2>

<p>
A widget instance MAY contain source-persisted presentation metadata when the active widget class contract allows it.
</p>

<p>
Typical examples include:
</p>

<ul>
  <li><code>caption</code>,</li>
  <li><code>face_color</code>,</li>
  <li><code>border_color</code>,</li>
  <li><code>text_color</code>,</li>
  <li>other instance-level presentation members explicitly allowed by the widget class.</li>
</ul>

<p>
For baseline source serialization, such metadata SHOULD normally appear inside <code>props</code>.
</p>

<p>
Presentation metadata:
</p>

<ul>
  <li>MUST remain source-owned instance metadata,</li>
  <li>MUST remain subordinate to widget class legality,</li>
  <li>MUST remain distinct from diagram executable interaction,</li>
  <li>MUST NOT create execution semantics by mere presence in source.</li>
</ul>

<p>
The following distinction MUST remain explicit:
</p>

<pre><code>widget primary value
    !=
presentation property
    !=
widget-oriented asset reference
</code></pre>

<hr/>

<h2 id="widget-asset-references">11. Widget Asset References</h2>

<p>
A widget instance MAY reference widget-oriented assets through a source-visible field such as <code>widget_assets</code>.
</p>

<p>
Such references are source-owned declarations pointing to artifacts that may define class law, realization information, or both.
They are not themselves executable graph operations.
</p>

<p>
Typical references include:
</p>

<ul>
  <li>a class package reference,</li>
  <li>a realization package reference,</li>
  <li>other future widget-oriented package references defined by later specifications.</li>
</ul>

<p>
Example:
</p>

<pre><code>{
  "widget_assets": {
    "class_package": "./ui/classes/standard-numeric.wfrog",
    "realization_package": "./ui/realizations/default-theme.wfrog"
  }
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li>asset references MUST remain source-visible and inspectable,</li>
  <li>asset references MUST NOT by themselves redefine class identity,</li>
  <li>asset references MUST NOT create hidden executable behavior,</li>
  <li>unsupported asset families MAY be ignored or diagnosed by a host or runtime according to profile and capability claims.</li>
</ul>

<hr/>

<h2 id="svg-visual-posture">12. SVG Visual Posture</h2>

<p>
When a widget realization package or another permitted widget-oriented asset references SVG content, that SVG is a visual resource, not executable truth.
</p>

<p>
Accordingly, SVG-backed realization content:
</p>

<ul>
  <li>MAY provide a designer preview or host skin,</li>
  <li>MAY define named visual layers or anchors,</li>
  <li>MAY support scalable visual rendering,</li>
  <li>MUST NOT define hidden methods, events, or dataflow meaning,</li>
  <li>MUST NOT replace widget class law as the normative owner of widget behavior.</li>
</ul>

<p>
The required distinction remains:
</p>

<pre><code>front_panel composition
    !=
source-persisted presentation metadata
    !=
widget class law
    !=
SVG visual resource content
</code></pre>

<p>
A host MAY:
</p>

<ul>
  <li>render SVG-backed realization faithfully,</li>
  <li>substitute a compatible native realization,</li>
  <li>ignore unsupported SVG-specific details,</li>
  <li>or ignore an unsupported realization package entirely,</li>
  <li>but it MUST preserve the source-owned meaning of the widget instance.</li>
</ul>

<hr/>

<h2 id="relation-with-the-diagram">13. Relation with the Diagram</h2>

<p>
The front panel does not define executable behavior.
The diagram remains the authoritative executable graph of the FROG.
</p>

<p>
Widget participation in execution is expressed in the diagram, not in the front panel itself.
Canonical diagram interaction mechanisms include:
</p>

<ul>
  <li><code>widget_value</code> — natural access to a widget primary value,</li>
  <li><code>widget_reference</code> — object-style access anchor,</li>
  <li><code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, and <code>frog.ui.method_invoke</code> — executable UI interaction primitives when allowed.</li>
</ul>

<p>
A source-persisted asset reference or presentation property does not become executable interaction merely because it appears in source.
</p>

<hr/>

<h2 id="relation-with-widget-class-law">14. Relation with Widget Class Law</h2>

<p>
The front panel serializes widget instances.
The widget class contract defines which members and behaviors are legal for the class referenced by each instance.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>the front panel may persist only instance-side members allowed by the relevant class law,</li>
  <li>the front panel does not invent new properties, methods, events, or parts,</li>
  <li>the front panel does not redefine addressing legality or mutability boundaries.</li>
</ul>

<hr/>

<h2 id="relation-with-wfrog-packages">15. Relation with <code>.wfrog</code> Packages</h2>

<p>
The front panel MAY reference one or more <code>.wfrog</code> packages through widget instances.
</p>

<p>
Typical package roles include:
</p>

<ul>
  <li><code>widget_class_package</code> — machine-readable class law,</li>
  <li><code>widget_realization_package</code> — host-facing realization definitions,</li>
  <li><code>widget_bundle_package</code> — combined packaging form.</li>
</ul>

<p>
The front panel references these packages but does not absorb their ownership.
</p>

<hr/>

<h2 id="validation-rules">16. Validation Rules</h2>

<p>
Validators MUST verify at least that:
</p>

<ul>
  <li><code>front_panel</code>, when present, follows the canonical object shape,</li>
  <li><code>widgets</code>, when present, is an array,</li>
  <li>widget identifiers are unique across the full widget tree,</li>
  <li>each widget instance is structurally valid,</li>
  <li>persisted instance metadata is recognized by the active widget class contract when such validation is available,</li>
  <li>widget-oriented asset references follow the published source shape,</li>
  <li>source-persisted presentation metadata is not misinterpreted as executable semantics.</li>
</ul>

<p>
Validators SHOULD additionally diagnose:
</p>

<ul>
  <li>unsupported package families under the active profile,</li>
  <li>structurally valid but unsupported realization references under the active host claim,</li>
  <li>attempts to blur source presentation with executable behavior.</li>
</ul>

<hr/>

<h2 id="minimal-v01-posture">17. Minimal v0.1 Posture</h2>

<p>
A minimal v0.1 front panel MAY contain:
</p>

<ul>
  <li>one top-level numeric control widget,</li>
  <li>one top-level numeric indicator widget,</li>
  <li>one canvas object,</li>
  <li>source-persisted instance properties in <code>props</code>,</li>
  <li>source-visible references to widget-oriented packages where needed.</li>
</ul>

<p>
For that posture:
</p>

<ul>
  <li>the front panel remains a serious but bounded source composition layer,</li>
  <li>widget class law remains externalized and inspectable,</li>
  <li>realization remains host-facing,</li>
  <li>the diagram remains the sole owner of executable graph semantics.</li>
</ul>

<hr/>

<h2 id="example">18. Example</h2>

<pre><code>{
  "front_panel": {
    "canvas": {
      "width": 460,
      "height": 170
    },
    "widgets": [
      {
        "id": "ctrl_count",
        "role": "control",
        "class_ref": "frog.ui.standard.numeric_control",
        "value_type": "u16",
        "layout": {
          "x": 20,
          "y": 24,
          "width": 140,
          "height": 32
        },
        "props": {
          "caption": "Count",
          "face_color": "#D0D0D0"
        },
        "widget_assets": {
          "class_package": "./ui/classes/standard-numeric.wfrog",
          "realization_package": "./ui/realizations/default-theme.wfrog"
        }
      },
      {
        "id": "ind_total",
        "role": "indicator",
        "class_ref": "frog.ui.standard.numeric_indicator",
        "value_type": "u16",
        "layout": {
          "x": 220,
          "y": 24,
          "width": 140,
          "height": 32
        },
        "props": {
          "caption": "Total",
          "face_color": "#E0E0E0"
        },
        "widget_assets": {
          "class_package": "./ui/classes/standard-numeric.wfrog",
          "realization_package": "./ui/realizations/default-theme.wfrog"
        }
      }
    ]
  }
}</code></pre>

<hr/>

<h2 id="summary">19. Summary</h2>

<p>
This document defines the canonical source model for front-panel composition.
</p>

<p>
It stabilizes:
</p>

<ul>
  <li>source-owned widget composition,</li>
  <li>source-owned placement and canvas metadata,</li>
  <li>source-persisted instance presentation metadata,</li>
  <li>source-visible widget-oriented asset references,</li>
  <li>and a strict separation between front-panel serialization and executable graph meaning.</li>
</ul>

<p>
This allows a FROG program to persist a credible front face in canonical source while preserving the architectural rule that the diagram remains the authoritative executable graph.
</p>
