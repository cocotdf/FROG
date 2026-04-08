<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Widget Realization</h1>

<p align="center">
  <strong>Normative architectural boundary for host-side widget realization, visual assets, and SVG integration</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope">2. Scope</a></li>
  <li><a href="#what-realization-means">3. What Realization Means</a></li>
  <li><a href="#why-realization-is-not-widget-law">4. Why Realization Is Not Widget Law</a></li>
  <li><a href="#host-ownership">5. Host Ownership</a></li>
  <li><a href="#runtime-ownership">6. Runtime Ownership</a></li>
  <li><a href="#svg-role">7. SVG Role</a></li>
  <li><a href="#visual-binding-model">8. Visual Binding Model</a></li>
  <li><a href="#parts-and-anchors">9. Parts and Anchors</a></li>
  <li><a href="#states-and-layers">10. States and Layers</a></li>
  <li><a href="#property-method-and-event-bindings">11. Property, Method, and Event Bindings</a></li>
  <li><a href="#host-private-hints">12. Host-Private Hints</a></li>
  <li><a href="#portability-boundary">13. Portability Boundary</a></li>
  <li><a href="#example">14. Example</a></li>
  <li><a href="#summary">15. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the architectural role of widget realization in FROG.
</p>

<p>
A widget class describes what a widget is. A realization describes how a host may realize that widget class visually and interactively.
</p>

<p>
Realization is therefore a host-facing layer that sits downstream from widget class law and upstream from concrete visual behavior on a live host.
</p>

<h2 id="scope">2. Scope</h2>

<p>
This document covers:
</p>

<ul>
  <li>host-side realization boundaries,</li>
  <li>visual asset usage,</li>
  <li>SVG integration,</li>
  <li>part-to-visual mapping,</li>
  <li>property/method/event realization bindings,</li>
  <li>portability boundaries for realization packages.</li>
</ul>

<p>
It does not redefine widget class legality and it does not replace the widget interaction model of the program.
</p>

<h2 id="what-realization-means">3. What Realization Means</h2>

<p>
Realization is the process by which a live host presents and operates a widget object using concrete visual and input surfaces.
</p>

<p>
That process may involve:
</p>

<ul>
  <li>native host controls,</li>
  <li>retained-mode scene graphs,</li>
  <li>custom draw surfaces,</li>
  <li>SVG-backed rendering,</li>
  <li>platform-specific focus models,</li>
  <li>platform-specific event dispatch.</li>
</ul>

<p>
FROG does not require all hosts to realize widgets identically at the implementation level. FROG does require that host realization not silently redefine the normative object surface of the widget.
</p>

<h2 id="why-realization-is-not-widget-law">4. Why Realization Is Not Widget Law</h2>

<p>
The same widget class may be realized:
</p>

<ul>
  <li>by a Qt control,</li>
  <li>by an HTML element,</li>
  <li>by a custom SDL surface,</li>
  <li>by an SVG template plus overlay logic,</li>
  <li>or by another host-specific mechanism.</li>
</ul>

<p>
Those realizations may differ operationally, but they do not become separate language-level widget definitions unless the class law itself differs.
</p>

<p>
This distinction is mandatory. If realization became widget law, portability would collapse into host-specific behavior.
</p>

<h2 id="host-ownership">5. Host Ownership</h2>

<p>
The host owns:
</p>

<ul>
  <li>drawing and compositing,</li>
  <li>focus management,</li>
  <li>pointer and keyboard input handling,</li>
  <li>redraw scheduling,</li>
  <li>layout execution where delegated,</li>
  <li>native visual affordances,</li>
  <li>performance optimizations.</li>
</ul>

<p>
The host does not own the normative class-level meaning of widget properties, methods, events, and parts.
</p>

<h2 id="runtime-ownership">6. Runtime Ownership</h2>

<p>
The runtime owns the interpretation bridge between class law, realization definitions, and live widget objects.
</p>

<p>
The runtime is responsible for:
</p>

<ul>
  <li>loading widget packages,</li>
  <li>instantiating widget objects,</li>
  <li>exposing legal members,</li>
  <li>connecting value participation,</li>
  <li>routing property reads and writes,</li>
  <li>routing method invocation,</li>
  <li>emitting events with normative identity and payload shape,</li>
  <li>coordinating with the host realization layer.</li>
</ul>

<h2 id="svg-role">7. SVG Role</h2>

<p>
SVG is a first-class visual asset format in FROG widget realization.
</p>

<p>
SVG may be used as:
</p>

<ul>
  <li>a face template,</li>
  <li>a layered scalable visual resource,</li>
  <li>an anchor-bearing asset,</li>
  <li>a state-aware visual composition resource.</li>
</ul>

<p>
SVG is not:
</p>

<ul>
  <li>the authoritative source of widget semantics,</li>
  <li>the authoritative source of widget member legality,</li>
  <li>a hidden executable program,</li>
  <li>the sole definition of events or methods.</li>
</ul>

<h2 id="visual-binding-model">8. Visual Binding Model</h2>

<p>
A realization package MAY bind widget properties and parts to visual elements.
</p>

<p>
Typical binding targets include:
</p>

<ul>
  <li>SVG attributes,</li>
  <li>text nodes,</li>
  <li>visibility states,</li>
  <li>style classes,</li>
  <li>native control configuration fields,</li>
  <li>scene-graph node properties.</li>
</ul>

<p>
These bindings are realization mappings. They do not replace the widget object surface itself.
</p>

<h2 id="parts-and-anchors">9. Parts and Anchors</h2>

<p>
A class-level widget definition may expose parts. A realization package may map those parts to visual anchors.
</p>

<p>
An anchor is a named visual attachment point or named visual node in the realization asset.
</p>

<p>
For example:
</p>

<ul>
  <li>a <code>label</code> part may bind to <code>label_anchor</code>,</li>
  <li>an <code>editor</code> part may bind to <code>editor_anchor</code>,</li>
  <li>a <code>root</code> anchor may identify the top visual node.</li>
</ul>

<p>
Part ownership remains class-side. Anchor ownership remains realization-side.
</p>

<h2 id="states-and-layers">10. States and Layers</h2>

<p>
A realization package MAY define visual states and layer sets.
</p>

<p>
Typical visual states include:
</p>

<ul>
  <li>normal,</li>
  <li>focused,</li>
  <li>disabled,</li>
  <li>pressed,</li>
  <li>hovered,</li>
  <li>alarm.</li>
</ul>

<p>
Layer sets are host-facing visual composition tools. They do not themselves redefine event or property semantics.
</p>

<h2 id="property-method-and-event-bindings">11. Property, Method, and Event Bindings</h2>

<p>
A realization package MAY define:
</p>

<ul>
  <li><strong>property bindings</strong> — map widget properties to visual or native host surfaces,</li>
  <li><strong>method bindings</strong> — map widget methods to host actions,</li>
  <li><strong>event bindings</strong> — map host signals to widget events.</li>
</ul>

<p>
These bindings must preserve normative widget identity.
</p>

<p>
A host-native signal may be the origin of a standardized event, but the standardized event identity remains the FROG-owned event identity.
</p>

<h2 id="host-private-hints">12. Host-Private Hints</h2>

<p>
A realization package MAY contain bounded host-private hints.
</p>

<p>
Examples include:
</p>

<ul>
  <li>preferred native control classes,</li>
  <li>preferred text rendering mode,</li>
  <li>platform-specific composition hints,</li>
  <li>optional acceleration hints.</li>
</ul>

<p>
Host-private hints:
</p>

<ul>
  <li>MUST NOT redefine class law,</li>
  <li>MUST NOT be treated as mandatory for class-level validity,</li>
  <li>SHOULD degrade safely when unsupported.</li>
</ul>

<h2 id="portability-boundary">13. Portability Boundary</h2>

<p>
A realization package is portable only to the extent that the target runtime and host support the relevant realization features.
</p>

<p>
However, portability of class law is broader than portability of realization.
</p>

<p>
This means:
</p>

<ul>
  <li>class-level object legality should remain broadly portable,</li>
  <li>visual realization may be narrower,</li>
  <li>host-private realization hints are narrower still.</li>
</ul>

<p>
A runtime may therefore support a class package without supporting every realization package for that class.
</p>

<h2 id="example">14. Example</h2>

<pre><code>{
  "wfrog_version": "0.1",
  "kind": "widget_realization_package",
  "package": {
    "name": "frog.ui.theme.default",
    "version": "0.1.0",
    "namespace": "frog.ui.theme.default"
  },
  "targets": [
    {
      "class_id": "frog.ui.standard.numeric_control",
      "host_family": "generic_svg_host",
      "visual": {
        "mode": "svg_template",
        "svg_asset": "./assets/numeric_control.svg",
        "anchors": {
          "root": "root",
          "label": "label_anchor",
          "editor": "editor_anchor"
        },
        "state_layers": {
          "normal": ["base", "label", "editor"],
          "focused": ["base", "focus_ring", "label", "editor"]
        }
      },
      "part_bindings": [
        {
          "part": "label",
          "visual_node": "label_anchor",
          "property_bindings": {
            "text": "textContent",
            "visible": "visibility"
          }
        }
      ],
      "property_bindings": {
        "face_color": {
          "binding_kind": "svg_attribute",
          "target": "base_fill",
          "attribute": "fill"
        }
      },
      "method_bindings": {
        "focus": {
          "binding_kind": "host_action",
          "action": "focus_editor"
        }
      },
      "event_bindings": {
        "value_changed": {
          "binding_kind": "host_signal",
          "signal": "editor_value_changed"
        }
      }
    }
  ]
}</code></pre>

<h2 id="summary">15. Summary</h2>

<p>
Widget realization is a mandatory architectural layer, but it is not the owner of widget law.
</p>

<p>
It provides the bounded bridge between:
</p>

<ul>
  <li>class-owned member surfaces,</li>
  <li>runtime-owned interpretation,</li>
  <li>host-owned rendering and interaction,</li>
  <li>and visual assets such as SVG.</li>
</ul>

<p>
That boundary is what allows FROG to support rich UI objects without collapsing the language into one runtime or one rendering stack.
</p>
