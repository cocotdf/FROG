<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">🐸 FROG Widget Specification</h1>

<p align="center">
  Definition of the FROG widget object model for <strong>.frog</strong> programs<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2 id="contents">Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope">2. Scope</a></li>
  <li><a href="#goals-of-the-widget-model">3. Goals of the Widget Model</a></li>
  <li><a href="#scope-for-v01">4. Scope for v0.1</a></li>
  <li><a href="#relation-with-other-specifications">5. Relation with Other Specifications</a></li>
  <li><a href="#what-a-widget-is">6. What a Widget Is</a></li>
  <li><a href="#widget-class-vs-value-type">7. Widget Class vs Value Type</a></li>
  <li><a href="#widget-roles">8. Widget Roles</a></li>
  <li><a href="#widget-identity-and-lifecycle">9. Widget Identity and Lifecycle</a></li>
  <li><a href="#canonical-widget-instance-shape">10. Canonical Widget Instance Shape</a></li>
  <li><a href="#value-carrying-widgets">11. Value-Carrying Widgets</a></li>
  <li><a href="#widget-reference-model">12. Widget Reference Model</a></li>
  <li><a href="#widget-parts">13. Widget Parts</a></li>
  <li><a href="#properties-methods-and-events">14. Properties, Methods, and Events</a></li>
  <li><a href="#widget-behavior-model">15. Widget Behavior Model</a></li>
  <li><a href="#serialization-vs-runtime-state">16. Serialization vs Runtime State</a></li>
  <li><a href="#standard-widget-classes-for-v01">17. Standard Widget Classes for v0.1</a></li>
  <li><a href="#addressing-model">18. Addressing Model</a></li>
  <li><a href="#validation-rules">19. Validation Rules</a></li>
  <li><a href="#examples">20. Examples</a></li>
  <li><a href="#out-of-scope-for-v01">21. Out of Scope for v0.1</a></li>
  <li><a href="#summary">22. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The FROG front panel is composed of widgets.
A widget is a structured source-level UI object with stable identity, declared class, declared role,
configurable source properties, and defined interaction semantics.
</p>

<p>
A widget is not merely a graphical shape.
It is a source-level UI object that MAY:
</p>

<ul>
  <li>carry a typed primary value,</li>
  <li>accept user input,</li>
  <li>display program state,</li>
  <li>own named parts,</li>
  <li>own child widgets when it is a container,</li>
  <li>expose properties,</li>
  <li>expose methods,</li>
  <li>emit runtime events.</li>
</ul>

<p>
This document defines the widget object model used by canonical FROG source.
It standardizes widget roles, widget classes, primary-value semantics, widget parts,
and widget-level serialization rules.
</p>

<p>
FROG distinguishes two interaction paths for widgets:
</p>

<ul>
  <li><strong>Natural value path</strong> — the primary value of a value-carrying widget participates in diagram dataflow through <code>widget_value</code>.</li>
  <li><strong>Object-style path</strong> — explicit widget-member access occurs through <code>widget_reference</code> plus widget interaction primitives.</li>
</ul>

<p>
These two paths are related but distinct.
The natural value path is the canonical representation for ordinary primary value flow.
The object-style path is the canonical representation for properties, methods, parts,
and other explicit widget-object interactions.
</p>

<hr/>

<h2 id="scope">2. Scope</h2>

<p>
This document specifies:
</p>

<ul>
  <li>what a widget is in canonical source,</li>
  <li>the distinction between widget class and carried value type,</li>
  <li>widget roles, identity, and instance structure,</li>
  <li>value-carrying widget semantics,</li>
  <li>widget references, widget parts, and member concepts,</li>
  <li>source-level validation rules for widget instances.</li>
</ul>

<p>
This document does not specify:
</p>

<ul>
  <li>the public program contract,</li>
  <li>the authoritative executable graph,</li>
  <li>the full front-panel composition and layout model,</li>
  <li>the complete executable semantics of widget interaction nodes,</li>
  <li>runtime renderer internals,</li>
  <li>a complete industrial UI toolkit.</li>
</ul>

<hr/>

<h2 id="goals-of-the-widget-model">3. Goals of the Widget Model</h2>

<p>
The widget model is designed to provide:
</p>

<ul>
  <li><strong>Object consistency</strong> — widgets behave as structured UI objects rather than ad hoc visual fragments.</li>
  <li><strong>Separation of concerns</strong> — UI composition, value typing, executable logic, public interface semantics, and runtime rendering remain distinct.</li>
  <li><strong>Stable serialization</strong> — canonical source stores durable design-time information only.</li>
  <li><strong>Tool interoperability</strong> — multiple editors and runtimes can reconstruct equivalent widget meaning.</li>
  <li><strong>Extensibility</strong> — specialized widget libraries MAY extend the model without redefining its foundations.</li>
  <li><strong>Graphical durability</strong> — widget declarations remain explicit and specifiable as long-term source objects.</li>
</ul>

<hr/>

<h2 id="scope-for-v01">4. Scope for v0.1</h2>

<p>
FROG v0.1 standardizes:
</p>

<ul>
  <li>the widget object model,</li>
  <li>widget roles,</li>
  <li>widget instance structure in canonical source,</li>
  <li>value-carrying widgets,</li>
  <li>widget references,</li>
  <li>widget parts,</li>
  <li>basic property and method concepts,</li>
  <li>a minimal standard widget vocabulary.</li>
</ul>

<p>
FROG v0.1 does not attempt to define a complete industrial UI toolkit.
Its purpose is to define a durable common baseline.
</p>

<hr/>

<h2 id="relation-with-other-specifications">5. Relation with Other Specifications</h2>

<ul>
  <li><code>Type.md</code> defines the value type system used by value-carrying widgets.</li>
  <li><code>Front panel.md</code> defines how widget instances are placed, composed, styled, and serialized in the <code>front_panel</code> section.</li>
  <li><code>Diagram.md</code> defines the executable graph and the node kinds that materialize widget participation in that graph.</li>
  <li><code>Widget interaction.md</code> defines the explicit diagram-side interaction model for widget references, property reads and writes, method invocation, and optional UI sequencing.</li>
  <li><code>Interface.md</code> defines the public program contract and remains distinct from the front panel.</li>
</ul>

<p>
Ownership boundary:
</p>

<pre>Widget.md owns:
- widget object model
- widget class / role model
- widget instance semantics
- primary value concept
- widget reference concept
- widget parts and member concepts

Widget.md does not own:
- public interface semantics
- executable graph semantics
- full front-panel composition/layout rules
- value type system
- executable interaction node forms</pre>

<p>
A value-carrying widget participates naturally in dataflow through its primary <code>value</code>.
In diagram source, that participation is represented by a <code>widget_value</code> node.
</p>

<p>
Richer access to a widget object is represented through a <code>widget_reference</code> node together with widget interaction primitives such as:
</p>

<ul>
  <li><code>frog.ui.property_read</code>,</li>
  <li><code>frog.ui.property_write</code>,</li>
  <li><code>frog.ui.method_invoke</code>.</li>
</ul>

<p>
This document defines what widgets are.
It does not redefine executable graph rules, public interface rules, or front-panel composition rules owned by the dedicated specifications above.
</p>

<hr/>

<h2 id="what-a-widget-is">6. What a Widget Is</h2>

<p>
A widget is an instance of a widget class.
</p>

<p>
A widget instance MUST have stable source identity.
Different tools MAY render the same widget differently, but they MUST preserve its semantic meaning.
</p>

<p>
A widget MAY:
</p>

<ul>
  <li>carry a typed primary value,</li>
  <li>accept or display data,</li>
  <li>own child widgets if it is a container,</li>
  <li>own named parts,</li>
  <li>expose configurable properties,</li>
  <li>expose callable methods,</li>
  <li>emit runtime events.</li>
</ul>

<p>
Canonical source serialization stores source-relevant widget configuration.
It MUST NOT depend on arbitrary runtime-only state.
</p>

<p>
A widget is not a public interface port.
A widget is not an executable node.
A widget is a source-level UI object that may participate in execution through the diagram,
but is defined independently from the graph itself.
</p>

<hr/>

<h2 id="widget-class-vs-value-type">7. Widget Class vs Value Type</h2>

<h3 id="widget-class">7.1 Widget Class</h3>

<p>
A widget class identifies the UI category of the widget.
Examples:
</p>

<pre>frog.ui.standard.numeric_control
frog.ui.standard.boolean_indicator
frog.ui.standard.string_control
frog.ui.standard.panel</pre>

<p>
A widget class determines:
</p>

<ul>
  <li>the allowed widget roles,</li>
  <li>whether the widget carries a primary value,</li>
  <li>which value types are allowed,</li>
  <li>which properties are available,</li>
  <li>which methods are available,</li>
  <li>which parts are available,</li>
  <li>which behavior model applies.</li>
</ul>

<h3 id="value-type">7.2 Value Type</h3>

<p>
A value type identifies the FROG data type carried by a value-carrying widget.
Examples:
</p>

<pre>bool
i32
f64
string
array&lt;f64&gt;</pre>

<p>
Value types are defined normatively by <code>Type.md</code>.
</p>

<h3 id="consequence">7.3 Consequence</h3>

<p>
A widget is not a type, and a type is not a widget.
</p>

<ul>
  <li><code>f64</code> is a value type,</li>
  <li><code>frog.ui.standard.numeric_control</code> is a widget class,</li>
  <li>a widget instance may be a numeric control carrying a value of type <code>f64</code>.</li>
</ul>

<hr/>

<h2 id="widget-roles">8. Widget Roles</h2>

<p>
Every widget instance MUST declare a role.
</p>

<p>
FROG v0.1 defines the following standard roles:
</p>

<ul>
  <li><code>control</code></li>
  <li><code>indicator</code></li>
  <li><code>container</code></li>
  <li><code>decoration</code></li>
</ul>

<h3 id="role-control">8.1 <code>control</code></h3>

<p>
A <code>control</code> is a value-carrying widget intended primarily for user-editable interaction.
Its primary value normally flows from the front panel toward executable logic.
</p>

<h3 id="role-indicator">8.2 <code>indicator</code></h3>

<p>
An <code>indicator</code> is a value-carrying widget intended primarily to display program state.
Its primary value normally flows from executable logic toward the front panel.
</p>

<h3 id="role-container">8.3 <code>container</code></h3>

<p>
A <code>container</code> owns child widgets and defines a compositional UI region.
In v0.1, standard containers are non-value widgets unless a stricter active profile explicitly defines otherwise.
</p>

<h3 id="role-decoration">8.4 <code>decoration</code></h3>

<p>
A <code>decoration</code> is used primarily for presentation rather than primary program value exchange.
</p>

<h3 id="role-compatibility">8.5 Role Compatibility</h3>

<p>
The declared role MUST be compatible with the declared widget class.
A tool MUST NOT accept an arbitrary role/class combination unless the active profile explicitly defines it as valid.
</p>

<hr/>

<h2 id="widget-identity-and-lifecycle">9. Widget Identity and Lifecycle</h2>

<p>
FROG distinguishes three conceptual levels:
</p>

<ul>
  <li>widget class — the category definition,</li>
  <li>widget instance — the serialized source instance in the front panel,</li>
  <li>runtime widget instance — the live object created by an editor or runtime.</li>
</ul>

<p>
Conceptually:
</p>

<pre>Widget Class
    |
    +-- instantiates -->
Widget Instance (source)
    |
    +-- realizes ----->
Runtime Widget Instance</pre>

<p>
The source instance defines design-time configuration.
The runtime instance manages live value, internal UI state, and rendering-related state.
</p>

<p>
Widget identifiers MUST remain unique across the entire recursive front-panel widget tree.
This guarantees that diagram-level widget references remain unambiguous.
</p>

<p>
The source identity of a widget MUST remain stable enough to support:
</p>

<ul>
  <li>diagram-side <code>widget_value</code> references,</li>
  <li>diagram-side <code>widget_reference</code> references,</li>
  <li>editor tracking,</li>
  <li>tool interoperability,</li>
  <li>canonical source diffs and merges.</li>
</ul>

<hr/>

<h2 id="canonical-widget-instance-shape">10. Canonical Widget Instance Shape</h2>

<p>
A canonical widget instance in source form SHOULD follow this general structure:
</p>

<pre>{
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
}</pre>

<p>
Common fields are defined below.
</p>

<h3 id="field-id">10.1 <code>id</code></h3>

<ul>
  <li>MUST be a string.</li>
  <li>MUST be unique across the full recursive front-panel widget tree.</li>
  <li>MUST remain stable enough to support source tracking, diagram references, and tool interoperability.</li>
</ul>

<h3 id="field-role">10.2 <code>role</code></h3>

<ul>
  <li>MUST be a valid widget role under the active specification profile.</li>
  <li>MUST be compatible with the declared widget class.</li>
</ul>

<h3 id="field-widget">10.3 <code>widget</code></h3>

<ul>
  <li>MUST be a string.</li>
  <li>MUST identify a known widget class under the active specification profile.</li>
</ul>

<p>
For standard built-in widgets defined by this document, identifiers SHOULD use the <code>frog.ui.standard.*</code> namespace.
</p>

<h3 id="field-value-type">10.4 <code>value_type</code></h3>

<ul>
  <li>MUST exist for value-carrying widgets.</li>
  <li>MUST NOT be required for non-value widgets.</li>
  <li>MUST be a valid canonical FROG type expression according to <code>Type.md</code>.</li>
</ul>

<h3 id="field-layout">10.5 <code>layout</code></h3>

<p>
<code>layout</code> stores design-time placement and size information.
Its detailed interpretation belongs normatively to <code>Front panel.md</code>.
</p>

<h3 id="field-props">10.6 <code>props</code></h3>

<ul>
  <li>MUST be an object when present.</li>
  <li>MUST contain only source-relevant property values.</li>
  <li>MAY contain inherited and class-specific properties.</li>
</ul>

<h3 id="field-parts">10.7 <code>parts</code></h3>

<ul>
  <li>MUST be an object when present.</li>
  <li>Keys MUST be stable part names.</li>
  <li>Values MUST be valid part objects for the owning widget class or active profile.</li>
</ul>

<h3 id="field-children">10.8 <code>children</code></h3>

<ul>
  <li>MAY appear on container widgets.</li>
  <li>MUST be an array when present.</li>
  <li>MUST contain valid child widget instances.</li>
</ul>

<p>
Ownership, nesting, and composition rules belong normatively to <code>Front panel.md</code>.
</p>

<h3 id="field-style">10.9 <code>style_ref</code> and <code>style_override</code></h3>

<p>
Widget instances MAY include visual style references and visual style overrides.
These fields remain presentation-related and MUST NOT alter widget semantics,
public interface semantics, or executable graph semantics.
</p>

<hr/>

<h2 id="value-carrying-widgets">11. Value-Carrying Widgets</h2>

<p>
Controls and indicators are value-carrying widgets in base v0.1.
</p>

<h3 id="required-value-semantics">11.1 Required Value Semantics</h3>

<ul>
  <li><code>value_type</code> MUST be defined.</li>
  <li>The widget class MUST support the declared type.</li>
  <li>The widget class MUST define a primary value semantic.</li>
</ul>

<h3 id="primary-value-path">11.2 Primary Value Path</h3>

<p>
Every value-carrying widget conceptually exposes a primary <code>value</code> member.
That primary value is the natural dataflow path between the front panel and the diagram.
</p>

<pre>Front Panel Widget
        |
        v
widget.value
        |
        v
widget_value</pre>

<p>
In diagram source, this participation is represented by a <code>widget_value</code> node.
</p>

<h3 id="directional-intent">11.3 Directional Intent</h3>

<ul>
  <li>a control normally provides a value to the diagram,</li>
  <li>an indicator normally receives a value from the diagram.</li>
</ul>

<p>
This directional intent does not redefine executable semantics by itself.
The diagram remains authoritative.
</p>

<h3 id="access-to-value-through-object-model">11.4 Access to <code>value</code> Through the Object Model</h3>

<p>
The primary value MAY also be read or written through the object-style interaction path when the widget class exposes <code>value</code> as a readable or writable property.
</p>

<p>
However, when the intent is ordinary primary-value wiring, tools SHOULD prefer the natural <code>widget_value</code> representation.
</p>

<h3 id="non-value-widgets">11.5 Non-Value Widgets</h3>

<p>
Container and decoration widgets are normally non-value widgets in base v0.1.
They do not expose a natural <code>widget_value</code> path unless a stricter active profile explicitly defines otherwise.
</p>

<hr/>

<h2 id="widget-reference-model">12. Widget Reference Model</h2>

<p>
A widget reference represents explicit object-style access to a widget.
</p>

<p>
This path is used when the diagram needs access to widget members beyond ordinary primary-value dataflow, such as:
</p>

<ul>
  <li>non-primary properties,</li>
  <li>methods,</li>
  <li>attached parts,</li>
  <li>other object-level behavior supported by the active profile.</li>
</ul>

<p>
Conceptually:
</p>

<pre>widget instance
      |
      v
widget_reference
      |
      v
widget member access</pre>

<p>
In diagram source, the reference is represented by a <code>widget_reference</code> node.
That reference is then consumed by widget interaction primitives.
</p>

<p>
The widget reference model does not replace the primary value path.
It complements it.
</p>

<p>
In v0.1, the widget reference token is opaque and interaction-oriented.
It is not standardized here as a general-purpose first-class value for arbitrary storage, transport, or computation.
</p>

<hr/>

<h2 id="widget-parts">13. Widget Parts</h2>

<p>
Widgets MAY contain attached parts.
A part is a structured UI sub-object owned by exactly one widget.
</p>

<p>
Parts allow widget structure to remain explicit instead of flattening all sub-objects into one large property bag.
</p>

<p>
Examples of parts include:
</p>

<ul>
  <li>a widget label,</li>
  <li>a caption,</li>
  <li>a graph scale,</li>
  <li>a plot area,</li>
  <li>a legend.</li>
</ul>

<h3 id="example-conceptual-addressing">13.1 Example Conceptual Addressing</h3>

<pre>ctrl_gain.label.text</pre>

<h3 id="example-serialization">13.2 Example Serialization</h3>

<pre>"parts": {
  "label": {
    "class": "frog.ui.standard.label_part",
    "props": {
      "text": "Gain"
    }
  }
}</pre>

<h3 id="ownership-rules">13.3 Ownership Rules</h3>

<ul>
  <li>A part belongs to exactly one widget instance.</li>
  <li>A part MUST NOT be serialized as an independent top-level widget.</li>
  <li>A part name MUST be valid for the owning widget class or active profile.</li>
</ul>

<h3 id="part-identity">13.4 Part Identity</h3>

<p>
A part is identified locally by its owning widget plus its stable part name.
It does not require a separate top-level widget identifier in canonical v0.1 source.
</p>

<hr/>

<h2 id="properties-methods-and-events">14. Properties, Methods, and Events</h2>

<h3 id="properties">14.1 Properties</h3>

<p>
Widgets and widget parts MAY expose properties.
Properties are named members whose values describe configuration or state.
</p>

<p>
Examples of common source-relevant properties include:
</p>

<ul>
  <li><code>visible</code>,</li>
  <li><code>enabled</code>,</li>
  <li><code>default_value</code>,</li>
  <li><code>minimum</code>,</li>
  <li><code>maximum</code>,</li>
  <li><code>step</code>,</li>
  <li><code>text</code>,</li>
  <li><code>multiline</code>.</li>
</ul>

<h3 id="methods">14.2 Methods</h3>

<p>
Widgets MAY expose methods representing imperative UI actions.
Examples of common conceptual methods include:
</p>

<ul>
  <li><code>focus()</code>,</li>
  <li><code>reset_to_default()</code>.</li>
</ul>

<h3 id="events">14.3 Events</h3>

<p>
Widgets MAY emit runtime events.
Examples include value-change or focus-related events.
</p>

<p>
The widget object model recognizes the existence of events.
However, event-specific executable interaction is not standardized as a first-class base mechanism in v0.1.
</p>

<h3 id="diagram-side-standardization">14.4 Diagram-Side Standardization</h3>

<p>
In v0.1, explicit property reads, property writes, and method invocation are standardized in diagram-related specifications through:
</p>

<ul>
  <li><code>frog.ui.property_read</code>,</li>
  <li><code>frog.ui.property_write</code>,</li>
  <li><code>frog.ui.method_invoke</code>.</li>
</ul>

<p>
This document does not redefine those executable forms.
It defines the widget-side object model to which they apply.
</p>

<hr/>

<h2 id="widget-behavior-model">15. Widget Behavior Model</h2>

<p>
A widget class MAY define both design-time configuration and runtime behavior.
</p>

<p>
Examples of behavior differences include:
</p>

<ul>
  <li>a numeric control may validate edits against numeric constraints,</li>
  <li>a string control may support multiline editing,</li>
  <li>a boolean indicator may render state without accepting user edits,</li>
  <li>a container may propagate visibility or clipping behavior to children,</li>
  <li>a decoration widget may affect presentation only.</li>
</ul>

<p>
This specification standardizes semantic categories and source structure.
It does not require identical visual rendering across implementations.
</p>

<p>
Behavior compatibility across tools MUST be evaluated at the semantic level defined by the widget class and active profile, not at the pixel-perfect rendering level.
</p>

<hr/>

<h2 id="serialization-vs-runtime-state">16. Serialization vs Runtime State</h2>

<p>
FROG distinguishes between serialized source properties and runtime-only state.
</p>

<h3 id="serialized-source-properties">16.1 Serialized Source Properties</h3>

<p>
Examples of values that MAY belong in canonical source include:
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

<h3 id="runtime-only-state">16.2 Runtime-Only State</h3>

<p>
Examples of values that SHOULD NOT appear in canonical source include:
</p>

<ul>
  <li>runtime object handles,</li>
  <li>resolved owner objects,</li>
  <li>internal runtime IDs,</li>
  <li>editor-private caches,</li>
  <li>render caches,</li>
  <li>dirty flags,</li>
  <li>transient hover or cursor state,</li>
  <li>runtime reference tables.</li>
</ul>

<p>
Runtime-only metadata MUST NOT be required for canonical source validity.
</p>

<h3 id="internal-state-vs-rendering-state">16.3 Internal State vs Rendering State</h3>

<p>
A live widget instance MAY maintain several conceptual categories of state:
</p>

<ul>
  <li>primary value — the typed program-facing value,</li>
  <li>internal UI state — edit state, selection, cursor state, hover state, and similar logic state,</li>
  <li>rendering state — layout caches, invalidation state, dirty flags, and similar renderer-oriented data.</li>
</ul>

<p>
These categories are conceptually distinct.
Only source-relevant state belongs in canonical source.
</p>

<hr/>

<h2 id="standard-widget-classes-for-v01">17. Standard Widget Classes for v0.1</h2>

<p>
FROG v0.1 defines a minimal standard widget vocabulary.
These classes form the recommended built-in baseline.
</p>

<h3 id="containers">17.1 Containers</h3>

<pre>frog.ui.standard.panel</pre>

<h3 id="decoration-widgets">17.2 Decoration Widgets</h3>

<pre>frog.ui.standard.text_label</pre>

<h3 id="value-widgets">17.3 Value Widgets</h3>

<pre>frog.ui.standard.numeric_control
frog.ui.standard.numeric_indicator
frog.ui.standard.boolean_control
frog.ui.standard.boolean_indicator
frog.ui.standard.string_control
frog.ui.standard.string_indicator</pre>

<h3 id="common-parts">17.4 Common Parts</h3>

<p>
Common standard parts include:
</p>

<ul>
  <li><code>label</code></li>
  <li><code>caption</code></li>
</ul>

<h3 id="type-constraints">17.5 Type Constraints</h3>

<ul>
  <li><code>frog.ui.standard.numeric_control</code> and <code>frog.ui.standard.numeric_indicator</code> MUST use numeric FROG types only,</li>
  <li><code>frog.ui.standard.boolean_control</code> and <code>frog.ui.standard.boolean_indicator</code> MUST use <code>bool</code>,</li>
  <li><code>frog.ui.standard.string_control</code> and <code>frog.ui.standard.string_indicator</code> MUST use <code>string</code>.</li>
</ul>

<p>
Library-defined widget classes MAY extend this vocabulary under stricter profiles or external UI libraries.
</p>

<hr/>

<h2 id="addressing-model">18. Addressing Model</h2>

<p>
Widget member access MUST be able to target:
</p>

<ul>
  <li>the widget itself, or</li>
  <li>a named part of the widget.</li>
</ul>

<p>
Examples:
</p>

<pre>ctrl_gain.value
ctrl_gain.visible
ctrl_gain.label.text
ctrl_gain.focus()
ctrl_gain.reset_to_default()</pre>

<p>
The <code>value</code> member has special semantics because it also participates in diagram dataflow through the <code>widget_value</code> path.
Other properties, methods, and parts normally use the widget-reference path.
</p>

<p>
In conceptual canonical diagram representation:
</p>

<ul>
  <li>the target widget identity is carried by <code>widget_reference</code>,</li>
  <li>member selection targets a widget or one of its parts,</li>
  <li>property and method operations are then materialized by the widget interaction primitives.</li>
</ul>

<p>
This document defines the object model behind such addressing.
The executable node forms themselves are standardized by <code>Widget interaction.md</code>.
</p>

<hr/>

<h2 id="validation-rules">19. Validation Rules</h2>

<p>
Implementations MUST enforce the following rules for standardized widget instances:
</p>

<ul>
  <li>every widget MUST define <code>id</code>,</li>
  <li>every widget MUST define <code>role</code>,</li>
  <li>every widget MUST define <code>widget</code>,</li>
  <li>widget identifiers MUST be unique across the full recursive front-panel widget tree,</li>
  <li>value-carrying widgets MUST declare <code>value_type</code>,</li>
  <li>non-value widgets MUST NOT require <code>value_type</code>,</li>
  <li>the widget role MUST be compatible with the widget class,</li>
  <li>serialized properties MUST be valid for the widget class or active profile,</li>
  <li>serialized parts MUST use valid part names and valid part classes for the owning widget class or active profile,</li>
  <li>a part MUST NOT exist independently from an owning widget,</li>
  <li>runtime-only reflection metadata MUST NOT be required for canonical source validity.</li>
</ul>

<p>
For standard widget classes:
</p>

<ul>
  <li><code>frog.ui.standard.numeric_control</code> and <code>frog.ui.standard.numeric_indicator</code> MUST use numeric value types only,</li>
  <li><code>frog.ui.standard.boolean_control</code> and <code>frog.ui.standard.boolean_indicator</code> MUST use <code>bool</code>,</li>
  <li><code>frog.ui.standard.string_control</code> and <code>frog.ui.standard.string_indicator</code> MUST use <code>string</code>.</li>
</ul>

<p>
For interaction consistency:
</p>

<ul>
  <li>a <code>widget_value</code> node MUST reference an existing value-carrying widget,</li>
  <li>a <code>widget_reference</code> node MUST reference an existing widget,</li>
  <li>object-style access to a part MUST target a valid part name on the referenced widget,</li>
  <li>reading or writing <code>value</code> through the object model remains valid only when the widget class exposes that member with the required access mode.</li>
</ul>

<p>
Validators SHOULD diagnose at least the following error classes:
</p>

<ul>
  <li>unknown widget class,</li>
  <li>unknown widget role,</li>
  <li>role/class incompatibility,</li>
  <li>missing <code>value_type</code> on a value-carrying widget,</li>
  <li>invalid value type for widget class,</li>
  <li>duplicate widget identifier,</li>
  <li>unknown part name,</li>
  <li>invalid part class,</li>
  <li>invalid source-only versus runtime-only property usage.</li>
</ul>

<hr/>

<h2 id="examples">20. Examples</h2>

<h3 id="numeric-control-example">20.1 Numeric Control</h3>

<pre>{
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
}</pre>

<h3 id="boolean-indicator-example">20.2 Boolean Indicator</h3>

<pre>{
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
}</pre>

<h3 id="string-control-example">20.3 String Control</h3>

<pre>{
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
        "text": "Name",
        "visible": true
      }
    }
  }
}</pre>

<h3 id="text-label-decoration-example">20.4 Text Label Decoration</h3>

<pre>{
  "id": "title_label",
  "role": "decoration",
  "widget": "frog.ui.standard.text_label",
  "layout": {
    "x": 20,
    "y": 120,
    "width": 240,
    "height": 24
  },
  "props": {
    "text": "System status",
    "visible": true
  }
}</pre>

<h3 id="panel-container-example">20.5 Panel Container</h3>

<pre>{
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
}</pre>

<h3 id="conceptual-access-examples">20.6 Conceptual Access Examples</h3>

<pre>ctrl_gain.value
ctrl_gain.visible
ctrl_gain.label.text
led_ready.value
ctrl_name.focus()
ctrl_name.reset_to_default()</pre>

<h3 id="extended-widget-example">20.7 Extended Widget Example</h3>

<pre>{
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
    }
  }
}</pre>

<hr/>

<h2 id="out-of-scope-for-v01">21. Out of Scope for v0.1</h2>

<ul>
  <li>a full industrial UI widget catalog,</li>
  <li>pixel-perfect cross-runtime rendering equivalence,</li>
  <li>a standardized first-class event structure for executable event handling,</li>
  <li>a generalized widget reference value type for arbitrary storage or transport,</li>
  <li>complete theme and style systems,</li>
  <li>advanced accessibility semantics,</li>
  <li>advanced responsive layout behavior,</li>
  <li>editor-private runtime reflection models.</li>
</ul>

<hr/>

<h2 id="summary">22. Summary</h2>

<p>
The FROG widget model defines widgets as structured source-level UI objects with stable identity,
declared class, declared role, optional typed primary value, named parts, properties, methods,
and runtime behavior categories.
</p>

<p>
For v0.1:
</p>

<ul>
  <li>the natural primary-value path is represented by <code>widget_value</code>,</li>
  <li>the object-style path is represented by <code>widget_reference</code> plus diagram-side widget interaction primitives,</li>
  <li>widgets remain distinct from public interface ports and from executable nodes,</li>
  <li>canonical source stores design-time widget meaning, not runtime-only implementation state.</li>
</ul>

<p>
This gives FROG a durable and explicit widget foundation suitable for long-term graphical language specification.
</p>
