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
  <li><a href="#relation-with-other-specifications">4. Relation with Other Specifications</a></li>
  <li><a href="#what-a-widget-is">5. What a Widget Is</a></li>
  <li><a href="#widget-vs-type">6. Widget Class vs Value Type</a></li>
  <li><a href="#conceptual-object-hierarchy">7. Conceptual Object Hierarchy</a></li>
  <li><a href="#widget-roles">8. Widget Roles</a></li>
  <li><a href="#common-widget-instance-fields">9. Common Widget Instance Fields</a></li>
  <li><a href="#value-carrying-widgets">10. Value-Carrying Widgets</a></li>
  <li><a href="#widget-parts">11. Widget Parts</a></li>
  <li><a href="#properties-methods-and-events">12. Properties, Methods, and Events</a></li>
  <li><a href="#property-and-method-inheritance">13. Property and Method Inheritance</a></li>
  <li><a href="#serialization-vs-runtime-reflection">14. Serialization vs Runtime Reflection</a></li>
  <li><a href="#standard-widget-classes-for-v01">15. Standard Widget Classes for v0.1</a></li>
  <li><a href="#property-and-method-addressing">16. Property and Method Addressing</a></li>
  <li><a href="#validation-rules">17. Validation Rules</a></li>
  <li><a href="#examples">18. Examples</a></li>
  <li><a href="#out-of-scope">19. Out of Scope for v0.1</a></li>
  <li><a href="#summary">20. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The FROG front panel is composed of <strong>widgets</strong>.
A widget is a user-interface object that may display data, accept user input, expose configurable properties, provide callable methods, and optionally contain attached sub-objects.
</p>

<p>
This document defines the widget model used by FROG.
It describes:
</p>

<ul>
  <li>what a widget is,</li>
  <li>how widgets are classified,</li>
  <li>how widgets relate to typed values,</li>
  <li>how widgets inherit shared behavior,</li>
  <li>how attached parts such as labels are represented,</li>
  <li>what is considered part of canonical source serialization.</li>
</ul>

<p>
A widget is not merely a visual drawing.
It is a structured UI object with identity, class, role, configurable state, and optional interaction surface.
</p>

<hr/>

<h2 id="goals">2. Goals of the Widget Model</h2>

<p>
The FROG widget model is designed to satisfy the following goals:
</p>

<ul>
  <li><strong>Object consistency</strong> — widgets must behave as structured objects rather than ad hoc visual fragments.</li>
  <li><strong>Separation of concerns</strong> — value typing, visual representation, and runtime introspection must remain distinct concepts.</li>
  <li><strong>Inheritance</strong> — common widget behavior should be shared through a conceptual hierarchy.</li>
  <li><strong>Extensibility</strong> — specialized widgets must be able to add properties, methods, parts, and visual features without redefining the common model.</li>
  <li><strong>Tool interoperability</strong> — different FROG editors and runtimes must be able to reconstruct equivalent widget behavior from the same source representation.</li>
  <li><strong>Canonical serialization</strong> — only stable, meaningful, source-relevant widget information should appear in the <code>.frog</code> file.</li>
</ul>

<hr/>

<h2 id="scope">3. Scope for v0.1</h2>

<p>
FROG v0.1 standardizes:
</p>

<ul>
  <li>the conceptual widget object model,</li>
  <li>the distinction between widget class and value type,</li>
  <li>common widget roles,</li>
  <li>the notion of widget parts,</li>
  <li>the distinction between properties, methods, and events,</li>
  <li>a minimal built-in standard widget set.</li>
</ul>

<p>
FROG v0.1 does not attempt to standardize a complete industrial UI toolkit.
The purpose of this document is to define a durable common foundation.
</p>

<hr/>

<h2 id="relation-with-other-specifications">4. Relation with Other Specifications</h2>

<p>
This document is cross-cutting and relates to other FROG specifications as follows:
</p>

<ul>
  <li><strong>Type.md</strong> defines the type system used by value-carrying widgets.</li>
  <li><strong>Front panel.md</strong> defines how widgets are placed, composed, and bound inside the <code>front_panel</code> section.</li>
  <li><strong>Diagram.md</strong> defines the execution graph that may interact with widget properties and methods through diagram-level mechanisms.</li>
  <li><strong>Interface.md</strong> defines the public contract that front panel widgets may expose or consume through bindings.</li>
</ul>

<p>
This document does <strong>not</strong> define the complete front panel section layout.
Instead, it defines the object model of the elements that appear inside it.
</p>

<hr/>

<h2 id="what-a-widget-is">5. What a Widget Is</h2>

<p>
A widget is an instance of a UI class.
</p>

<p>
A widget MAY:
</p>

<ul>
  <li>carry a typed value,</li>
  <li>display a value,</li>
  <li>accept user input,</li>
  <li>contain child widgets,</li>
  <li>expose configurable properties,</li>
  <li>expose callable methods,</li>
  <li>emit events,</li>
  <li>own attached parts such as labels, captions, or scales.</li>
</ul>

<p>
A widget instance is identified independently from its visual appearance.
Its identity is stable in the source representation even if tools render it differently.
</p>

<hr/>

<h2 id="widget-vs-type">6. Widget Class vs Value Type</h2>

<p>
A widget class and a value type are different concepts.
</p>

<h3>6.1 Widget class</h3>

<p>
A widget class describes the UI object category.
Examples:
</p>

<ul>
  <li><code>frog.ui.standard.numeric_control</code></li>
  <li><code>frog.ui.standard.boolean_indicator</code></li>
  <li><code>frog.ui.standard.string_control</code></li>
  <li><code>frog.ui.standard.panel</code></li>
</ul>

<p>
A widget class determines:
</p>

<ul>
  <li>the role of the widget,</li>
  <li>which properties are available,</li>
  <li>which methods are available,</li>
  <li>which events may exist,</li>
  <li>which attached parts may exist,</li>
  <li>whether the widget carries a value,</li>
  <li>which value types are allowed.</li>
</ul>

<h3>6.2 Value type</h3>

<p>
A value type describes the data carried by a value-carrying widget.
Examples:
</p>

<ul>
  <li><code>bool</code></li>
  <li><code>i32</code></li>
  <li><code>f64</code></li>
  <li><code>string</code></li>
  <li><code>array&lt;f64&gt;</code></li>
</ul>

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

<h2 id="conceptual-object-hierarchy">7. Conceptual Object Hierarchy</h2>

<p>
FROG uses a conceptual object hierarchy to define shared behavior.
This hierarchy is normative at the semantic level, but implementations are not required to use literal class inheritance internally.
</p>

<p>
The conceptual hierarchy for v0.1 is:
</p>

<pre>
UIObject
├── Widget
│   ├── ContainerWidget
│   ├── DecorationWidget
│   └── ValueWidget&lt;T&gt;
│       ├── ControlWidget&lt;T&gt;
│       └── IndicatorWidget&lt;T&gt;
└── WidgetPart
</pre>

<h3>7.1 <code>UIObject</code></h3>

<p>
Base conceptual class for any front panel object that may expose properties or methods.
Both widgets and attached parts inherit from <code>UIObject</code>.
</p>

<h3>7.2 <code>Widget</code></h3>

<p>
A top-level or nested front panel object that may appear as an element in the front panel composition.
</p>

<h3>7.3 <code>ContainerWidget</code></h3>

<p>
A widget that owns child widgets and provides a compositional UI area.
Example:
</p>

<ul>
  <li>panel</li>
</ul>

<h3>7.4 <code>DecorationWidget</code></h3>

<p>
A widget that does not primarily carry a program value but contributes to presentation.
Examples:
</p>

<ul>
  <li>text label</li>
  <li>static image</li>
  <li>separator</li>
</ul>

<h3>7.5 <code>ValueWidget&lt;T&gt;</code></h3>

<p>
A widget that exposes a typed value of type <code>T</code>.
</p>

<h3>7.6 <code>ControlWidget&lt;T&gt;</code></h3>

<p>
A value widget intended primarily for user input or user-editable state.
</p>

<h3>7.7 <code>IndicatorWidget&lt;T&gt;</code></h3>

<p>
A value widget intended primarily for displaying program state to the user.
</p>

<h3>7.8 <code>WidgetPart</code></h3>

<p>
A named attached sub-object owned by a widget.
Examples:
</p>

<ul>
  <li>label</li>
  <li>caption</li>
  <li>x_scale</li>
  <li>plot_area</li>
</ul>

<p>
A widget part is not a free-standing top-level widget instance.
It exists through its owning widget.
</p>

<hr/>

<h2 id="widget-roles">8. Widget Roles</h2>

<p>
Every widget instance MUST declare a role.
FROG v0.1 defines the following roles:
</p>

<ul>
  <li><code>control</code></li>
  <li><code>indicator</code></li>
  <li><code>container</code></li>
  <li><code>decoration</code></li>
</ul>

<h3>8.1 <code>control</code></h3>

<p>
A user-editable value widget.
A control normally provides data from the front panel toward the program.
</p>

<h3>8.2 <code>indicator</code></h3>

<p>
A non-user-editable value widget intended to display program state.
An indicator normally receives data from the program.
</p>

<h3>8.3 <code>container</code></h3>

<p>
A widget that owns child widgets and organizes a region of the UI.
A container may or may not itself carry a value, depending on future extensions.
For v0.1, standard containers are non-value widgets.
</p>

<h3>8.4 <code>decoration</code></h3>

<p>
A widget used primarily for presentation rather than program value exchange.
</p>

<hr/>

<h2 id="common-widget-instance-fields">9. Common Widget Instance Fields</h2>

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

<h3>9.1 <code>id</code></h3>

<p>
Stable widget identifier.
</p>

<ul>
  <li>MUST be a string.</li>
  <li>MUST be unique within the owning front panel scope.</li>
  <li>MUST remain stable enough to support bindings, references, and tooling.</li>
</ul>

<h3>9.2 <code>role</code></h3>

<p>
Declared widget role.
</p>

<ul>
  <li>MUST be one of the roles defined by this specification or a stricter active profile.</li>
</ul>

<h3>9.3 <code>widget</code></h3>

<p>
Widget class identifier.
</p>

<ul>
  <li>MUST be a string.</li>
  <li>MUST identify a known widget class under the active specification profile.</li>
</ul>

<p>
For standard built-in widgets defined in this document, identifiers SHOULD use the <code>frog.ui.standard.*</code> namespace.
</p>

<h3>9.4 <code>value_type</code></h3>

<p>
Declared FROG value type carried by the widget, if the widget is value-carrying.
</p>

<ul>
  <li>MUST exist for value-carrying widgets.</li>
  <li>MUST NOT be required for non-value widgets.</li>
  <li>MUST be a valid canonical type expression according to <code>Type.md</code>.</li>
</ul>

<h3>9.5 <code>layout</code></h3>

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

<h3>9.6 <code>props</code></h3>

<p>
Serialized design-time property values for the widget instance.
</p>

<ul>
  <li>MUST be an object when present.</li>
  <li>MAY contain inherited and class-specific properties.</li>
  <li>MUST only contain source-relevant property values.</li>
</ul>

<h3>9.7 <code>parts</code></h3>

<p>
Named attached sub-objects owned by the widget.
</p>

<ul>
  <li>MUST be an object when present.</li>
  <li>Keys are stable part names such as <code>label</code> or <code>caption</code>.</li>
  <li>Values are part objects defined by this document.</li>
</ul>

<h3>9.8 <code>children</code></h3>

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

<h2 id="value-carrying-widgets">10. Value-Carrying Widgets</h2>

<p>
A value-carrying widget exposes a typed value.
This includes controls and indicators.
</p>

<h3>10.1 Required value semantics</h3>

<p>
For a value-carrying widget:
</p>

<ul>
  <li><code>value_type</code> MUST be defined,</li>
  <li>the widget class MUST be compatible with the declared type,</li>
  <li>the widget MAY expose a runtime <code>value</code> property,</li>
  <li>the serialized instance MAY expose design-time configuration related to the value.</li>
</ul>

<h3>10.2 Serialized default state vs runtime state</h3>

<p>
Canonical source serialization should store design-time configuration and optional initial/default state, not arbitrary runtime state snapshots.
</p>

<p>
Therefore, a source widget instance SHOULD prefer a property such as:
</p>

<ul>
  <li><code>default_value</code></li>
  <li><code>minimum</code></li>
  <li><code>maximum</code></li>
  <li><code>step</code></li>
</ul>

<p>
rather than serializing transient runtime values that only exist during execution.
</p>

<h3>10.3 Type compatibility</h3>

<p>
The declared <code>value_type</code> MUST follow <code>Type.md</code>.
Compatibility between widget values and program values is governed by the same FROG type system.
</p>

<hr/>

<h2 id="widget-parts">11. Widget Parts</h2>

<p>
A widget MAY own attached parts.
A part is a named sub-object with its own properties and, optionally, methods.
</p>

<h3>11.1 Purpose of parts</h3>

<p>
Parts allow structured UI sub-objects to be represented explicitly instead of flattening all widget details into one large property set.
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

<h3>11.2 Common part model</h3>

<p>
A widget part SHOULD follow this general shape:
</p>

<pre><code>{
  "class": "frog.ui.standard.label_part",
  "props": {
    "text": "Gain",
    "visible": true
  }
}</code></pre>

<h3>11.3 Part naming</h3>

<p>
Part names are stable identifiers chosen by the widget class definition.
Examples:
</p>

<ul>
  <li><code>label</code></li>
  <li><code>caption</code></li>
  <li><code>x_scale</code></li>
  <li><code>y_scale</code></li>
  <li><code>plot_area</code></li>
</ul>

<h3>11.4 Ownership</h3>

<p>
A part belongs to exactly one widget instance.
It is not serialized as an independent top-level widget entry.
</p>

<h3>11.5 Visibility of parts</h3>

<p>
A part MAY have properties such as visibility, text, style, or geometry, depending on its class.
</p>

<hr/>

<h2 id="properties-methods-and-events">12. Properties, Methods, and Events</h2>

<p>
Widgets and parts may expose:
</p>

<ul>
  <li><strong>properties</strong> — readable or writable object state,</li>
  <li><strong>methods</strong> — callable actions,</li>
  <li><strong>events</strong> — emitted notifications.</li>
</ul>

<h3>12.1 Properties</h3>

<p>
A property describes object state or configuration.
Examples:
</p>

<ul>
  <li><code>visible</code></li>
  <li><code>enabled</code></li>
  <li><code>text</code></li>
  <li><code>minimum</code></li>
  <li><code>maximum</code></li>
  <li><code>default_value</code></li>
</ul>

<p>
Properties may be:
</p>

<ul>
  <li>inherited,</li>
  <li>class-specific,</li>
  <li>part-specific,</li>
  <li>read-only, write-only, or read/write.</li>
</ul>

<h3>12.2 Methods</h3>

<p>
A method performs an action that is not best represented as plain state assignment.
Examples:
</p>

<ul>
  <li><code>focus()</code></li>
  <li><code>reset_to_default()</code></li>
  <li><code>show()</code></li>
  <li><code>hide()</code></li>
</ul>

<p>
Methods may be inherited or class-specific.
</p>

<h3>12.3 Events</h3>

<p>
An event represents a notification emitted by a widget or part.
Examples:
</p>

<ul>
  <li><code>value_changed</code></li>
  <li><code>focus_changed</code></li>
  <li><code>clicked</code></li>
</ul>

<p>
Event semantics are acknowledged by this object model, but full event scheduling and event-loop behavior are outside the scope of v0.1.
</p>

<hr/>

<h2 id="property-and-method-inheritance">13. Property and Method Inheritance</h2>

<p>
Widgets inherit common behavior from their conceptual ancestors.
</p>

<p>
For example:
</p>

<ul>
  <li>all widgets inherit core object identity,</li>
  <li>visual widgets may share properties such as visibility and geometry,</li>
  <li>all value widgets may share value-related properties,</li>
  <li>specific widget classes may add specialized properties.</li>
</ul>

<p>
A specialized class may:
</p>

<ul>
  <li>inherit a property unchanged,</li>
  <li>specialize a property with narrower constraints,</li>
  <li>add new properties,</li>
  <li>add new parts,</li>
  <li>add new methods or events.</li>
</ul>

<p>
Example conceptual progression:
</p>

<pre>
UIObject
  └── Widget
        └── ValueWidget&lt;T&gt;
              └── ControlWidget&lt;f64&gt;
                    └── NumericControl
</pre>

<p>
In this example:
</p>

<ul>
  <li><code>UIObject</code> may define identity-level semantics,</li>
  <li><code>Widget</code> may define visibility and layout-related semantics,</li>
  <li><code>ValueWidget&lt;T&gt;</code> may define value-related semantics,</li>
  <li><code>NumericControl</code> may add <code>minimum</code>, <code>maximum</code>, <code>step</code>, and numeric formatting properties.</li>
</ul>

<hr/>

<h2 id="serialization-vs-runtime-reflection">14. Serialization vs Runtime Reflection</h2>

<p>
Not every object property visible at runtime belongs in the canonical source file.
</p>

<p>
FROG distinguishes:
</p>

<ul>
  <li><strong>serialized source properties</strong> — stable, meaningful, source-relevant configuration values,</li>
  <li><strong>runtime reflection metadata</strong> — implementation-level or runtime-level information derived during execution or editing.</li>
</ul>

<h3>14.1 Serialized source properties</h3>

<p>
Examples of values that may belong in canonical source:
</p>

<ul>
  <li>widget class,</li>
  <li>role,</li>
  <li>layout,</li>
  <li>visibility,</li>
  <li>default value,</li>
  <li>text,</li>
  <li>minimum and maximum constraints,</li>
  <li>attached label text.</li>
</ul>

<h3>14.2 Runtime reflection metadata</h3>

<p>
Examples of values that should generally <strong>not</strong> be required in canonical source:
</p>

<ul>
  <li>runtime reference handles,</li>
  <li>internal class IDs,</li>
  <li>resolved owner objects,</li>
  <li>owning process or owning runtime instance,</li>
  <li>implementation-private reflection data.</li>
</ul>

<h3>14.3 Principle</h3>

<p>
If a field is needed only for runtime introspection, internal references, or implementation-private object management, it should not be part of the mandatory FROG Expression unless standardized explicitly by a future specification revision.
</p>

<hr/>

<h2 id="standard-widget-classes-for-v01">15. Standard Widget Classes for v0.1</h2>

<p>
FROG v0.1 defines a minimal standard widget vocabulary.
These classes form the recommended built-in baseline.
</p>

<h3>15.1 Standard container widgets</h3>

<ul>
  <li><code>frog.ui.standard.panel</code></li>
</ul>

<p>
Role:
</p>

<ul>
  <li><code>container</code></li>
</ul>

<p>
Purpose:
</p>

<ul>
  <li>owns or groups child widgets.</li>
</ul>

<h3>15.2 Standard decoration widgets</h3>

<ul>
  <li><code>frog.ui.standard.text_label</code></li>
</ul>

<p>
Role:
</p>

<ul>
  <li><code>decoration</code></li>
</ul>

<p>
Purpose:
</p>

<ul>
  <li>displays static text or presentation-only text.</li>
</ul>

<h3>15.3 Standard value widgets</h3>

<ul>
  <li><code>frog.ui.standard.numeric_control</code></li>
  <li><code>frog.ui.standard.numeric_indicator</code></li>
  <li><code>frog.ui.standard.boolean_control</code></li>
  <li><code>frog.ui.standard.boolean_indicator</code></li>
  <li><code>frog.ui.standard.string_control</code></li>
  <li><code>frog.ui.standard.string_indicator</code></li>
</ul>

<h3>15.4 Type constraints for standard value widgets</h3>

<p>
Recommended compatibility:
</p>

<ul>
  <li><code>numeric_control</code> / <code>numeric_indicator</code> — numeric FROG types only</li>
  <li><code>boolean_control</code> / <code>boolean_indicator</code> — <code>bool</code> only</li>
  <li><code>string_control</code> / <code>string_indicator</code> — <code>string</code> only</li>
</ul>

<h3>15.5 Standard common parts</h3>

<p>
The following parts are commonly supported by standard widgets when relevant:
</p>

<ul>
  <li><code>label</code></li>
  <li><code>caption</code></li>
</ul>

<p>
Future widget families may define additional specialized parts such as scales, plot areas, legends, or embedded text regions.
</p>

<hr/>

<h2 id="property-and-method-addressing">16. Property and Method Addressing</h2>

<p>
Property and method access must be able to target:
</p>

<ul>
  <li>a widget itself, or</li>
  <li>a named part of a widget.</li>
</ul>

<p>
This document defines the conceptual addressing model, even if the exact diagram encoding is standardized elsewhere.
</p>

<h3>16.1 Widget-level addressing</h3>

<p>
Examples:
</p>

<ul>
  <li><code>ctrl_gain.value</code></li>
  <li><code>ctrl_gain.visible</code></li>
  <li><code>led_ready.value</code></li>
</ul>

<h3>16.2 Part-level addressing</h3>

<p>
Examples:
</p>

<ul>
  <li><code>ctrl_gain.label.text</code></li>
  <li><code>ctrl_gain.label.visible</code></li>
</ul>

<h3>16.3 Method addressing</h3>

<p>
Examples:
</p>

<ul>
  <li><code>ctrl_gain.focus()</code></li>
  <li><code>ctrl_gain.reset_to_default()</code></li>
</ul>

<p>
If a future widget class defines nested specialized parts, the same principle applies recursively.
</p>

<hr/>

<h2 id="validation-rules">17. Validation Rules</h2>

<p>
Implementations MUST enforce the following rules for standardized widget instances:
</p>

<ul>
  <li>every widget instance MUST define an <code>id</code>,</li>
  <li>every widget instance MUST define a <code>role</code>,</li>
  <li>every widget instance MUST define a <code>widget</code> class identifier,</li>
  <li>widget identifiers MUST be unique within the owning front panel scope,</li>
  <li>if the widget is value-carrying, <code>value_type</code> MUST exist and MUST be a valid FROG type expression,</li>
  <li>the widget role MUST be compatible with the widget class,</li>
  <li>serialized properties MUST be valid for the widget class or active profile,</li>
  <li>serialized parts MUST use valid part names for the widget class or active profile,</li>
  <li>a part MUST NOT exist independently from an owning widget,</li>
  <li>runtime-only reflection metadata MUST NOT be required for canonical source validity.</li>
</ul>

<p>
For standard widget classes:
</p>

<ul>
  <li><code>numeric_control</code> and <code>numeric_indicator</code> MUST use numeric value types only,</li>
  <li><code>boolean_control</code> and <code>boolean_indicator</code> MUST use <code>bool</code>,</li>
  <li><code>string_control</code> and <code>string_indicator</code> MUST use <code>string</code>.</li>
</ul>

<hr/>

<h2 id="examples">18. Examples</h2>

<h3>18.1 Numeric control with label part</h3>

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

<h3>18.2 Boolean indicator</h3>

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

<h3>18.3 String control</h3>

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

<h3>18.4 Static text label</h3>

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

<h3>18.5 Panel container</h3>

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

<h3>18.6 Conceptual property access examples</h3>

<pre><code>ctrl_gain.value
ctrl_gain.visible
ctrl_gain.label.text
led_ready.value
ctrl_name.focus()
ctrl_name.reset_to_default()</code></pre>

<h3>18.7 Specialized future-style widget with advanced parts</h3>

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

<p>
This example shows how specialized widgets may expose richer attached object structures while still following the same core model.
</p>

<hr/>

<h2 id="out-of-scope">19. Out of Scope for v0.1</h2>

<p>
The following topics are not fully standardized by this document in v0.1:
</p>

<ul>
  <li>complete event-loop behavior,</li>
  <li>all possible specialized widget families,</li>
  <li>advanced graph/chart widget semantics,</li>
  <li>the exact diagram encoding of property nodes and method nodes,</li>
  <li>runtime object references and reflection APIs,</li>
  <li>style system standardization beyond basic serialized properties,</li>
  <li>container layout engines and automatic layout policies,</li>
  <li>full accessibility metadata model,</li>
  <li>animation, transitions, and visual effects.</li>
</ul>

<hr/>

<h2 id="summary">20. Summary</h2>

<p>
A FROG widget is a structured UI object, not merely a visual drawing.
</p>

<p>
This specification establishes that:
</p>

<ul>
  <li>the front panel is composed of widget instances,</li>
  <li>widget classes and value types are distinct concepts,</li>
  <li>widgets follow a conceptual inheritance model,</li>
  <li>widgets may expose properties, methods, events, and attached parts,</li>
  <li>only stable source-relevant information belongs in canonical serialization,</li>
  <li>a minimal standard widget set exists for v0.1.</li>
</ul>

<p>
This widget model provides the foundation needed to define richer front panel behavior, property access, method invocation, and future widget families in a coherent and extensible way.
</p>

<hr/>

<p align="center">
End of FROG Widget Specification
</p>
