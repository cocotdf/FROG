<h1 align="center">🐸 FROG Widget Specification</h1>

<p align="center">
Definition of front panel widgets for <strong>.frog</strong> programs<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Goals of the Widget Model</a></li>
  <li><a href="#scope">3. Scope for v0.1</a></li>
  <li><a href="#relation">4. Relation with Other Specifications</a></li>
  <li><a href="#definition">5. What a Widget Is</a></li>
  <li><a href="#class-vs-type">6. Widget Class vs Value Type</a></li>
  <li><a href="#lifecycle-model">7. Widget Lifecycle Model</a></li>
  <li><a href="#hierarchy">8. Conceptual Object Hierarchy</a></li>
  <li><a href="#roles">9. Widget Roles</a></li>
  <li><a href="#fields">10. Common Widget Instance Fields</a></li>
  <li><a href="#value-widgets">11. Value-Carrying Widgets</a></li>
  <li><a href="#widget-reference">12. Widget Reference Model</a></li>
  <li><a href="#parts">13. Widget Parts</a></li>
  <li><a href="#properties">14. Properties, Methods, and Events</a></li>
  <li><a href="#behaviour-model">15. Widget Behaviour Model</a></li>
  <li><a href="#runtime-state">16. Runtime State and Rendering State</a></li>
  <li><a href="#inheritance">17. Property and Method Inheritance</a></li>
  <li><a href="#serialization">18. Serialization vs Runtime Reflection</a></li>
  <li><a href="#standard-widgets">19. Standard Widget Classes for v0.1</a></li>
  <li><a href="#addressing">20. Property and Method Addressing</a></li>
  <li><a href="#validation">21. Validation Rules</a></li>
  <li><a href="#examples">22. Examples</a></li>
  <li><a href="#out-of-scope">23. Out of Scope for v0.1</a></li>
  <li><a href="#summary">24. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The FROG front panel is composed of <strong>widgets</strong>.
A widget is a structured user-interface object capable of displaying data,
accepting user input, exposing properties, invoking methods, and emitting events.
</p>

<p>
A widget is not merely a graphical shape.
It is a living UI object with identity, class, configuration, interaction semantics,
and runtime behavior.
</p>

<p>
This document defines the widget object model used by FROG,
including widget classes, widget roles, widget parts,
value semantics, reference semantics,
and the relationship between widgets and the program diagram.
</p>

<p>
FROG adopts a model conceptually close to the object model of advanced graphical environments:
a value-carrying widget participates naturally in dataflow through its value,
while richer interactions use an explicit object reference.
</p>

<hr/>

<h2 id="goals">2. Goals of the Widget Model</h2>

<ul>
  <li><strong>Object consistency</strong> — widgets behave as structured UI objects rather than ad hoc visual fragments.</li>
  <li><strong>Separation of concerns</strong> — UI representation, value typing, runtime state, and program logic remain distinct concepts.</li>
  <li><strong>Extensibility</strong> — specialized widgets may extend the model without redefining its foundation.</li>
  <li><strong>Stable serialization</strong> — only meaningful design-time information belongs in canonical source.</li>
  <li><strong>Tool interoperability</strong> — different FROG editors and runtimes can reconstruct equivalent widget behavior.</li>
  <li><strong>Performance awareness</strong> — the model must allow efficient runtimes with explicit invalidation, batching, and partial redraw strategies.</li>
</ul>

<hr/>

<h2 id="scope">3. Scope for v0.1</h2>

<p>
FROG v0.1 standardizes:
</p>

<ul>
  <li>the widget object model,</li>
  <li>widget classes and roles,</li>
  <li>value-carrying widgets,</li>
  <li>widget references,</li>
  <li>widget parts,</li>
  <li>basic properties, methods, and events,</li>
  <li>a minimal standard widget set.</li>
</ul>

<p>
FROG v0.1 does not attempt to define a complete industrial UI toolkit.
Its purpose is to define a durable common foundation.
</p>

<hr/>

<h2 id="relation">4. Relation with Other Specifications</h2>

<ul>
  <li><strong>Type.md</strong> defines the type system used by value-carrying widgets.</li>
  <li><strong>Front panel.md</strong> defines how widget instances are placed and composed in the <code>front_panel</code> section.</li>
  <li><strong>Diagram.md</strong> defines the executable dataflow graph.</li>
  <li><strong>Interface.md</strong> defines the public program contract.</li>
</ul>

<p>
Value-carrying widgets implicitly expose a diagram terminal corresponding to their
<code>value</code> property.
This allows them to participate directly in the FROG dataflow graph
without requiring explicit UI binding objects.
</p>

<p>
Properties, methods, parts, and events beyond the primary value interaction
are accessed conceptually through a widget reference model.
The exact diagram encoding of reference nodes, property nodes, method nodes,
and event nodes is standardized by diagram-related specifications, not by this document alone.
</p>

<hr/>

<h2 id="definition">5. What a Widget Is</h2>

<p>
A widget is an instance of a UI class.
</p>

<p>
A widget MAY:
</p>

<ul>
  <li>carry a typed value,</li>
  <li>display program state,</li>
  <li>accept user input,</li>
  <li>contain child widgets,</li>
  <li>expose configurable properties,</li>
  <li>expose callable methods,</li>
  <li>emit events,</li>
  <li>own attached parts such as labels, captions, scales, or plot areas.</li>
</ul>

<p>
A widget instance has stable identity in source form,
even if different tools render it differently.
</p>

<p>
A widget class may define both design-time configuration
and runtime behavior.
However, canonical source serialization stores only source-relevant state,
not arbitrary runtime state.
</p>

<hr/>

<h2 id="class-vs-type">6. Widget Class vs Value Type</h2>

<p>
Widget classes and value types are distinct concepts.
</p>

<h3>6.1 Widget class</h3>

<p>
A widget class defines the category of the UI object.
Examples:
</p>

<pre><code>frog.ui.standard.numeric_control
frog.ui.standard.boolean_indicator
frog.ui.standard.string_control
frog.ui.standard.panel</code></pre>

<p>
A widget class determines:
</p>

<ul>
  <li>the role of the widget,</li>
  <li>whether it carries a value,</li>
  <li>which value types are allowed,</li>
  <li>which properties are available,</li>
  <li>which methods are available,</li>
  <li>which events may exist,</li>
  <li>which parts may exist,</li>
  <li>which runtime behavior model applies.</li>
</ul>

<h3>6.2 Value type</h3>

<p>
A value type defines the data type carried by a value-carrying widget.
Examples:
</p>

<pre><code>bool
i32
f64
string
array&lt;f64&gt;</code></pre>

<p>
Value types are defined normatively by <code>Type.md</code>.
</p>

<h3>6.3 Consequence</h3>

<p>
A widget is not a type.
A type is not a widget.
</p>

<p>
For example:
</p>

<ul>
  <li><code>f64</code> is a value type,</li>
  <li><code>frog.ui.standard.numeric_control</code> is a widget class,</li>
  <li>a widget instance may be a numeric control carrying a value of type <code>f64</code>.</li>
</ul>

<hr/>

<h2 id="lifecycle-model">7. Widget Lifecycle Model</h2>

<p>
FROG distinguishes three conceptual levels for a widget:
</p>

<ul>
  <li><strong>widget class</strong> — the definition of the widget category,</li>
  <li><strong>widget instance</strong> — the serialized source-level instance inside a front panel,</li>
  <li><strong>runtime widget instance</strong> — the live object created by a runtime or editor.</li>
</ul>

<p>
Conceptually:
</p>

<pre><code>Widget Class
    ↓ instantiates
Widget Instance (source)
    ↓ realizes
Runtime Widget Instance</code></pre>

<p>
The widget class defines allowed properties, methods, events, parts,
value semantics, and behavior rules.
The source instance defines design-time configuration.
The runtime instance manages live value, internal state, invalidation state,
and rendering-related state.
</p>

<hr/>

<h2 id="hierarchy">8. Conceptual Object Hierarchy</h2>

<pre><code>UIObject
├── Widget
│   ├── ContainerWidget
│   ├── DecorationWidget
│   └── ValueWidget&lt;T&gt;
│       ├── ControlWidget&lt;T&gt;
│       └── IndicatorWidget&lt;T&gt;
└── WidgetPart</code></pre>

<p>
This hierarchy defines conceptual behavior shared by widgets.
Implementations are not required to use literal inheritance internally.
</p>

<h3>8.1 <code>UIObject</code></h3>

<p>
Base conceptual class for front panel objects that may expose properties, methods, or events.
Both widgets and attached parts inherit conceptually from <code>UIObject</code>.
</p>

<h3>8.2 <code>Widget</code></h3>

<p>
A top-level or nested front panel object that may appear in the UI composition.
</p>

<h3>8.3 <code>ContainerWidget</code></h3>

<p>
A widget that owns child widgets and defines a compositional UI area.
</p>

<h3>8.4 <code>DecorationWidget</code></h3>

<p>
A widget used primarily for presentation and not for main program value exchange.
</p>

<h3>8.5 <code>ValueWidget&lt;T&gt;</code></h3>

<p>
A widget that carries a typed primary value of type <code>T</code>.
</p>

<h3>8.6 <code>ControlWidget&lt;T&gt;</code></h3>

<p>
A value widget intended primarily for user-editable interaction.
</p>

<h3>8.7 <code>IndicatorWidget&lt;T&gt;</code></h3>

<p>
A value widget intended primarily for displaying program state.
</p>

<h3>8.8 <code>WidgetPart</code></h3>

<p>
A named attached sub-object owned by a widget.
A part is not a free-standing top-level widget instance.
</p>

<hr/>

<h2 id="roles">9. Widget Roles</h2>

<p>
Every widget instance <strong>MUST</strong> declare a role.
</p>

<p>
FROG v0.1 defines the following roles:
</p>

<ul>
  <li><code>control</code></li>
  <li><code>indicator</code></li>
  <li><code>container</code></li>
  <li><code>decoration</code></li>
</ul>

<h3>9.1 <code>control</code></h3>

<p>
A user-editable value widget.
A control normally provides data from the front panel toward the program.
</p>

<h3>9.2 <code>indicator</code></h3>

<p>
A non-user-editable value widget intended to display program state.
An indicator normally receives data from the program.
</p>

<h3>9.3 <code>container</code></h3>

<p>
A widget that owns child widgets and organizes a region of the UI.
For v0.1, standard containers are non-value widgets.
</p>

<h3>9.4 <code>decoration</code></h3>

<p>
A widget used primarily for presentation rather than program value exchange.
</p>

<hr/>

<h2 id="fields">10. Common Widget Instance Fields</h2>

<p>
A canonical widget instance in source form SHOULD follow this general shape:
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
  "props": {},
  "parts": {}
}</code></pre>

<p>
The common fields are defined below.
</p>

<h3>10.1 <code>id</code></h3>

<p>
Stable widget identifier.
</p>

<ul>
  <li><strong>MUST</strong> be a string.</li>
  <li><strong>MUST</strong> be unique within the owning front panel scope.</li>
  <li><strong>MUST</strong> remain stable enough to support references, tooling, and UI-object addressing.</li>
</ul>

<h3>10.2 <code>role</code></h3>

<p>
Declared widget role.
</p>

<ul>
  <li><strong>MUST</strong> be one of the roles defined by this specification or by a stricter active profile.</li>
</ul>

<h3>10.3 <code>widget</code></h3>

<p>
Widget class identifier.
</p>

<ul>
  <li><strong>MUST</strong> be a string.</li>
  <li><strong>MUST</strong> identify a known widget class under the active specification profile.</li>
</ul>

<p>
For standard built-in widgets defined in this document, identifiers SHOULD use the <code>frog.ui.standard.*</code> namespace.
</p>

<h3>10.4 <code>value_type</code></h3>

<p>
Declared FROG value type carried by the widget, if the widget is value-carrying.
</p>

<ul>
  <li><strong>MUST</strong> exist for value-carrying widgets.</li>
  <li><strong>MUST NOT</strong> be required for non-value widgets.</li>
  <li><strong>MUST</strong> be a valid canonical type expression according to <code>Type.md</code>.</li>
</ul>

<h3>10.5 <code>layout</code></h3>

<p>
Design-time placement and dimensions used by tools to reconstruct the front panel.
</p>

<p>
Typical fields include:
</p>

<ul>
  <li><code>x</code></li>
  <li><code>y</code></li>
  <li><code>width</code></li>
  <li><code>height</code></li>
</ul>

<p>
The exact front panel composition rules are defined by <code>Front panel.md</code>.
This document only states that widget instances may carry layout information.
</p>

<h3>10.6 <code>props</code></h3>

<p>
Serialized design-time property values for the widget instance.
</p>

<ul>
  <li><strong>MUST</strong> be an object when present.</li>
  <li><strong>MAY</strong> contain inherited and class-specific properties.</li>
  <li><strong>MUST</strong> contain only source-relevant property values.</li>
</ul>

<h3>10.7 <code>parts</code></h3>

<p>
Named attached sub-objects owned by the widget.
</p>

<ul>
  <li><strong>MUST</strong> be an object when present.</li>
  <li>Keys are stable part names such as <code>label</code> or <code>caption</code>.</li>
  <li>Values are part objects defined by this document.</li>
</ul>

<h3>10.8 <code>children</code></h3>

<p>
Container widgets MAY define child widgets.
</p>

<ul>
  <li>Container serialization is permitted.</li>
  <li>The exact ownership and layout composition rules belong to <code>Front panel.md</code>.</li>
</ul>

<p>
This field is optional and relevant only to container widgets or stricter profiles.
</p>

<hr/>

<h2 id="value-widgets">11. Value-Carrying Widgets</h2>

<p>
Controls and indicators carry typed primary values.
</p>

<h3>11.1 Required value semantics</h3>

<ul>
  <li><code>value_type</code> <strong>MUST</strong> be defined.</li>
  <li>The widget class <strong>MUST</strong> support the declared type.</li>
  <li>The widget class <strong>MUST</strong> define a primary value semantic.</li>
</ul>

<h3>11.2 Implicit diagram terminal</h3>

<p>
Every value-carrying widget implicitly exposes a diagram terminal
representing its <code>value</code> property.
</p>

<pre><code>Front Panel Widget
        │
        ▼
widget.value
        │
        ▼
Diagram Terminal</code></pre>

<p>
This terminal participates directly in the program dataflow graph.
No separate UI binding object is required in the base model.
</p>

<h3>11.3 Source value vs runtime value</h3>

<p>
Canonical source serialization SHOULD store design-time configuration and optional initial or default state,
not arbitrary runtime state snapshots.
</p>

<p>
Therefore, a source widget instance SHOULD prefer properties such as:
</p>

<ul>
  <li><code>default_value</code></li>
  <li><code>minimum</code></li>
  <li><code>maximum</code></li>
  <li><code>step</code></li>
  <li><code>format</code></li>
</ul>

<p>
rather than serializing transient runtime values.
</p>

<h3>11.4 Type compatibility</h3>

<p>
The declared <code>value_type</code> MUST follow <code>Type.md</code>.
Compatibility between widget values and program values is governed by the same FROG type system.
</p>

<hr/>

<h2 id="widget-reference">12. Widget Reference Model</h2>

<p>
A value-carrying widget exposes its primary value directly through the diagram terminal model.
However, richer object interaction requires a reference-based model.
</p>

<p>
Conceptually, every widget MAY be addressed through a widget reference.
That reference allows access to:
</p>

<ul>
  <li>properties,</li>
  <li>methods,</li>
  <li>events,</li>
  <li>attached parts.</li>
</ul>

<p>
The intended model is:
</p>

<pre><code>widget
├── implicit value terminal
└── explicit widget reference</code></pre>

<p>
This mirrors the distinction between:
</p>

<ul>
  <li>the primary dataflow path for the widget value, and</li>
  <li>the object-style access path for richer UI interaction.</li>
</ul>

<p>
The exact runtime handle representation and the exact diagram encoding of reference nodes
are outside the strict scope of this document,
but the conceptual distinction is normative.
</p>

<hr/>

<h2 id="parts">13. Widget Parts</h2>

<p>
Widgets may contain attached parts.
Parts represent structured UI sub-objects.
</p>

<h3>13.1 Purpose of parts</h3>

<p>
Parts allow widget structure to remain explicit
instead of flattening every sub-object into one large property bag.
</p>

<p>
Examples:
</p>

<ul>
  <li>a widget label,</li>
  <li>a caption,</li>
  <li>a graph plot area,</li>
  <li>a graph scale,</li>
  <li>a legend.</li>
</ul>

<h3>13.2 Example conceptual addressing</h3>

<pre><code>ctrl_gain.label.text</code></pre>

<h3>13.3 Example serialization</h3>

<pre><code>"parts": {
  "label": {
    "class": "frog.ui.standard.label_part",
    "props": {
      "text": "Gain"
    }
  }
}</code></pre>

<h3>13.4 Ownership</h3>

<p>
A part belongs to exactly one widget instance.
It is not serialized as an independent top-level widget entry.
</p>

<hr/>

<h2 id="properties">14. Properties, Methods, and Events</h2>

<p>
Widgets and widget parts may expose:
</p>

<ul>
  <li><strong>properties</strong> — readable or writable object state,</li>
  <li><strong>methods</strong> — callable actions,</li>
  <li><strong>events</strong> — emitted notifications.</li>
</ul>

<h3>14.1 Properties</h3>

<p>
Properties describe object state or configuration.
Examples:
</p>

<pre><code>ctrl_gain.visible
ctrl_gain.enabled
ctrl_gain.minimum
ctrl_gain.maximum
ctrl_gain.label.text</code></pre>

<h3>14.2 Methods</h3>

<p>
Methods represent actions that are not best expressed as plain state assignment.
Examples:
</p>

<pre><code>ctrl_gain.focus()
ctrl_gain.reset_to_default()
ctrl_gain.show()
ctrl_gain.hide()</code></pre>

<h3>14.3 Events</h3>

<p>
Events represent notifications emitted by a widget or widget part.
Examples:
</p>

<pre><code>value_changed
focus_changed
clicked</code></pre>

<p>
Event semantics are acknowledged by the widget model,
but full event scheduling and event-loop behavior remain outside the strict scope of v0.1.
</p>

<hr/>

<h2 id="behaviour-model">15. Widget Behaviour Model</h2>

<p>
A widget class MAY define runtime behavior beyond static rendering.
This behavior may include:
</p>

<ul>
  <li>value normalization,</li>
  <li>clamping or validation,</li>
  <li>state transitions,</li>
  <li>event emission,</li>
  <li>visual invalidation rules.</li>
</ul>

<p>
Conceptually, a widget behaves like a living UI object.
However, FROG separates:
</p>

<ul>
  <li>the widget class behavior contract,</li>
  <li>the serialized source instance,</li>
  <li>the live runtime state.</li>
</ul>

<p>
For performance and determinism reasons,
widget behavior SHOULD be explicit, schedulable, and optimizable.
The source serialization does not require embedding arbitrary opaque runtime callbacks.
</p>

<p>
Future FROG profiles MAY standardize richer behavior descriptions,
including graph-based or declarative widget behavior definitions.
</p>

<hr/>

<h2 id="runtime-state">16. Runtime State and Rendering State</h2>

<p>
A live widget instance may maintain several categories of state.
These categories are conceptually distinct:
</p>

<ul>
  <li><strong>primary value</strong> — the typed program-facing value,</li>
  <li><strong>internal state</strong> — editing state, hover state, cursor position, selection state, and similar UI logic state,</li>
  <li><strong>rendering state</strong> — caches, dirty flags, invalidation state, layout state, and similar rendering-oriented data.</li>
</ul>

<p>
These categories <strong>MUST NOT</strong> be conflated in canonical source serialization.
</p>

<p>
In particular:
</p>

<ul>
  <li>the primary value may participate in dataflow,</li>
  <li>internal state belongs to runtime behavior,</li>
  <li>rendering state belongs to the renderer and runtime implementation.</li>
</ul>

<p>
This distinction is important for performance, portability, and stable source representation.
</p>

<hr/>

<h2 id="inheritance">17. Property and Method Inheritance</h2>

<p>
Widgets inherit behavior from conceptual base classes.
</p>

<p>
Example hierarchy:
</p>

<pre><code>UIObject
  └── Widget
      └── ValueWidget
          └── NumericControl</code></pre>

<p>
A specialized widget class may:
</p>

<ul>
  <li>inherit existing properties unchanged,</li>
  <li>specialize inherited properties with narrower constraints,</li>
  <li>add new properties,</li>
  <li>add new parts,</li>
  <li>add new methods,</li>
  <li>add new events.</li>
</ul>

<hr/>

<h2 id="serialization">18. Serialization vs Runtime Reflection</h2>

<p>
FROG distinguishes:
</p>

<ul>
  <li><strong>serialized source properties</strong> — stable design-time values relevant to canonical source,</li>
  <li><strong>runtime reflection metadata</strong> — implementation-level or runtime-level information used only during execution or editing.</li>
</ul>

<h3>18.1 Serialized source properties</h3>

<p>
Examples of values that may belong in canonical source:
</p>

<ul>
  <li>widget class,</li>
  <li>role,</li>
  <li>layout,</li>
  <li>visibility,</li>
  <li>default value,</li>
  <li>minimum and maximum constraints,</li>
  <li>label text.</li>
</ul>

<h3>18.2 Runtime reflection metadata</h3>

<p>
Examples of values that should generally <strong>not</strong> appear in canonical source:
</p>

<ul>
  <li>runtime handles,</li>
  <li>resolved owner objects,</li>
  <li>internal class IDs,</li>
  <li>editor-private caches,</li>
  <li>render caches,</li>
  <li>dirty flags,</li>
  <li>runtime reference tables.</li>
</ul>

<p>
Runtime metadata <strong>MUST NOT</strong> be required for canonical source validity.
</p>

<hr/>

<h2 id="standard-widgets">19. Standard Widget Classes for v0.1</h2>

<p>
FROG v0.1 defines a minimal standard widget vocabulary.
These classes form the recommended built-in baseline.
</p>

<h3>19.1 Containers</h3>

<pre><code>frog.ui.standard.panel</code></pre>

<h3>19.2 Decoration widgets</h3>

<pre><code>frog.ui.standard.text_label</code></pre>

<h3>19.3 Value widgets</h3>

<pre><code>frog.ui.standard.numeric_control
frog.ui.standard.numeric_indicator
frog.ui.standard.boolean_control
frog.ui.standard.boolean_indicator
frog.ui.standard.string_control
frog.ui.standard.string_indicator</code></pre>

<h3>19.4 Common parts</h3>

<p>
Common standard parts include:
</p>

<ul>
  <li><code>label</code></li>
  <li><code>caption</code></li>
</ul>

<h3>19.5 Type constraints</h3>

<p>
Recommended compatibility:
</p>

<ul>
  <li><code>numeric_control</code> and <code>numeric_indicator</code> — numeric FROG types only,</li>
  <li><code>boolean_control</code> and <code>boolean_indicator</code> — <code>bool</code> only,</li>
  <li><code>string_control</code> and <code>string_indicator</code> — <code>string</code> only.</li>
</ul>

<hr/>

<h2 id="addressing">20. Property and Method Addressing</h2>

<p>
A widget reference must be able to target:
</p>

<ul>
  <li>the widget itself, or</li>
  <li>a named part of the widget.</li>
</ul>

<p>
Examples:
</p>

<pre><code>ctrl_gain.value
ctrl_gain.visible
ctrl_gain.label.text
ctrl_gain.focus()
ctrl_gain.reset_to_default()</code></pre>

<p>
The <code>value</code> property has special semantics because it participates directly
in diagram dataflow through the implicit terminal model.
Other properties, methods, and parts use the widget-reference conceptual path.
</p>

<hr/>

<h2 id="validation">21. Validation Rules</h2>

<p>
Implementations MUST enforce the following rules for standardized widget instances:
</p>

<ul>
  <li>every widget <strong>MUST</strong> define <code>id</code>,</li>
  <li>every widget <strong>MUST</strong> define <code>role</code>,</li>
  <li>every widget <strong>MUST</strong> define <code>widget</code>,</li>
  <li>widget ids <strong>MUST</strong> be unique within the owning front panel scope,</li>
  <li>value widgets <strong>MUST</strong> declare <code>value_type</code>,</li>
  <li>the widget role <strong>MUST</strong> match the widget class,</li>
  <li>serialized properties <strong>MUST</strong> be valid for the widget class or active profile,</li>
  <li>serialized parts <strong>MUST</strong> use valid part names for the widget class or active profile,</li>
  <li>a part <strong>MUST NOT</strong> exist independently from an owning widget,</li>
  <li>runtime-only reflection metadata <strong>MUST NOT</strong> be required for canonical source validity.</li>
</ul>

<p>
For standard widget classes:
</p>

<ul>
  <li><code>numeric_control</code> and <code>numeric_indicator</code> <strong>MUST</strong> use numeric value types only,</li>
  <li><code>boolean_control</code> and <code>boolean_indicator</code> <strong>MUST</strong> use <code>bool</code>,</li>
  <li><code>string_control</code> and <code>string_indicator</code> <strong>MUST</strong> use <code>string</code>.</li>
</ul>

<hr/>

<h2 id="examples">22. Examples</h2>

<h3>22.1 Numeric control</h3>

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
    "visible": true,
    "enabled": true,
    "default_value": 1.0,
    "minimum": 0.0,
    "maximum": 10.0,
    "step": 0.1
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

<h3>22.2 Boolean indicator</h3>

<pre><code>{
  "id": "led_ready",
  "role": "indicator",
  "widget": "frog.ui.standard.boolean_indicator",
  "value_type": "bool",
  "layout": {
    "x": 180,
    "y": 20,
    "width": 22,
    "height": 22
  },
  "props": {
    "visible": true,
    "enabled": true
  },
  "parts": {
    "label": {
      "class": "frog.ui.standard.label_part",
      "props": {
        "text": "Ready",
        "visible": true
      }
    }
  }
}</code></pre>

<h3>22.3 String control</h3>

<pre><code>{
  "id": "ctrl_name",
  "role": "control",
  "widget": "frog.ui.standard.string_control",
  "value_type": "string",
  "layout": {
    "x": 20,
    "y": 70,
    "width": 220,
    "height": 28
  },
  "props": {
    "visible": true,
    "enabled": true,
    "default_value": "operator_1",
    "multiline": false
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
}</code></pre>

<h3>22.4 Static text label</h3>

<pre><code>{
  "id": "title_1",
  "role": "decoration",
  "widget": "frog.ui.standard.text_label",
  "layout": {
    "x": 20,
    "y": 120,
    "width": 180,
    "height": 24
  },
  "props": {
    "text": "System Status",
    "visible": true
  }
}</code></pre>

<h3>22.5 Panel container</h3>

<pre><code>{
  "id": "main_panel",
  "role": "container",
  "widget": "frog.ui.standard.panel",
  "layout": {
    "x": 0,
    "y": 0,
    "width": 800,
    "height": 600
  },
  "props": {
    "visible": true
  }
}</code></pre>

<h3>22.6 Conceptual access examples</h3>

<pre><code>ctrl_gain.value
ctrl_gain.visible
ctrl_gain.label.text
led_ready.value
ctrl_name.focus()
ctrl_name.reset_to_default()</code></pre>

<h3>22.7 Extended future-style widget</h3>

<p>
The following example is illustrative only and not part of the standardized v0.1 minimum set:
</p>

<pre><code>{
  "id": "graph_1",
  "role": "indicator",
  "widget": "frog.ui.extended.waveform_graph",
  "value_type": "array&lt;f64&gt;",
  "layout": {
    "x": 20,
    "y": 160,
    "width": 420,
    "height": 240
  },
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
    },
    "plot_area": {
      "class": "frog.ui.extended.plot_area_part",
      "props": {
        "visible": true
      }
    }
  }
}</code></pre>

<hr/>

<h2 id="out-of-scope">23. Out of Scope for v0.1</h2>

<ul>
  <li>complete industrial UI toolkit standardization,</li>
  <li>advanced graph and chart semantics,</li>
  <li>full event-loop scheduling behavior,</li>
  <li>the exact diagram encoding of property nodes, method nodes, reference nodes, and event nodes,</li>
  <li>runtime object handle representations,</li>
  <li>advanced behavior-graph standardization,</li>
  <li>animation systems and visual effects,</li>
  <li>full accessibility metadata,</li>
  <li>container layout engines and automatic layout policies.</li>
</ul>

<hr/>

<h2 id="summary">24. Summary</h2>

<p>
Widgets are structured UI objects capable of carrying values,
exposing properties, methods, events, and attached parts,
and participating in the program dataflow graph
through implicit value terminals.
</p>

<p>
This specification establishes that:
</p>

<ul>
  <li>widget classes and value types are distinct concepts,</li>
  <li>value widgets expose an implicit <code>value</code> terminal for diagram dataflow,</li>
  <li>richer interactions use a widget-reference conceptual model,</li>
  <li>runtime internal state and rendering state are distinct from canonical source serialization,</li>
  <li>a minimal standard widget set exists for v0.1.</li>
</ul>

<p>
This widget model provides the foundation needed to define richer front panel behavior,
property access, method invocation, future widget families,
and efficient runtime implementations in a coherent and extensible way.
</p>

<hr/>

<p align="center">
End of FROG Widget Specification
</p>
