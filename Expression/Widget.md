<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">FROG Widget Specification</h1>

<p align="center">
  <strong>Definition of widget instances for <code>.frog</code> front panels</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals-of-the-widget-model">2. Goals of the Widget Model</a></li>
  <li><a href="#scope-for-v01">3. Scope for v0.1</a></li>
  <li><a href="#relation-with-other-specifications">4. Relation with Other Specifications</a></li>
  <li><a href="#what-a-widget-is">5. What a Widget Is</a></li>
  <li><a href="#widget-class-vs-value-type">6. Widget Class vs Value Type</a></li>
  <li><a href="#widget-roles">7. Widget Roles</a></li>
  <li><a href="#widget-identity-and-lifecycle">8. Widget Identity and Lifecycle</a></li>
  <li><a href="#canonical-widget-instance-shape">9. Canonical Widget Instance Shape</a></li>
  <li><a href="#value-carrying-widgets">10. Value-Carrying Widgets</a></li>
  <li><a href="#widget-reference-model">11. Widget Reference Model</a></li>
  <li><a href="#widget-parts">12. Widget Parts</a></li>
  <li><a href="#properties-methods-and-events">13. Properties, Methods, and Events</a></li>
  <li><a href="#widget-behavior-model">14. Widget Behavior Model</a></li>
  <li><a href="#serialization-vs-runtime-state">15. Serialization vs Runtime State</a></li>
  <li><a href="#standard-widget-classes-for-v01">16. Standard Widget Classes for v0.1</a></li>
  <li><a href="#addressing-model">17. Addressing Model</a></li>
  <li><a href="#validation-rules">18. Validation Rules</a></li>
  <li><a href="#examples">19. Examples</a></li>
  <li><a href="#out-of-scope-for-v01">20. Out of Scope for v0.1</a></li>
  <li><a href="#summary">21. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The FROG front panel is composed of widget instances. A widget is a structured UI object with stable source identity, declared class, declared role, configurable source-owned properties, and defined participation paths toward executable interaction.
</p>

<p>
A widget is not merely a graphical shape. It is a source-level UI object that MAY:
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
This document defines the widget instance model used by canonical FROG source. It standardizes widget roles, widget classes at instance level, primary value semantics, widget parts at instance level, and source-level serialization rules.
</p>

<p>
FROG distinguishes two interaction paths for widgets:
</p>

<ul>
  <li><strong>Natural value path</strong> — the primary value of a value-carrying widget participates in diagram dataflow through <code>widget_value</code>.</li>
  <li><strong>Object-style path</strong> — explicit widget-member access occurs through <code>widget_reference</code> plus widget interaction primitives.</li>
</ul>

<p>
These two paths are related but distinct. The natural value path is the canonical representation for ordinary value flow. The object-style path is the canonical representation for properties, methods, parts, and other explicit widget-object interactions.
</p>

<hr/>

<h2 id="goals-of-the-widget-model">2. Goals of the Widget Model</h2>

<p>
The widget model is designed to provide:
</p>

<ul>
  <li><strong>Object consistency</strong> — widgets behave as structured UI objects rather than ad hoc visual fragments.</li>
  <li><strong>Separation of concerns</strong> — UI composition, value typing, executable logic, public interface semantics, class-level member legality, and runtime rendering remain distinct.</li>
  <li><strong>Stable serialization</strong> — canonical source stores durable design-time information only.</li>
  <li><strong>Tool interoperability</strong> — multiple editors and runtimes can reconstruct equivalent widget meaning.</li>
  <li><strong>Extensibility</strong> — specialized widget libraries MAY extend the model without redefining its foundations.</li>
  <li><strong>Graphical durability</strong> — widget declarations remain explicit and specifiable as long-term source objects.</li>
</ul>

<hr/>

<h2 id="scope-for-v01">3. Scope for v0.1</h2>

<p>
FROG v0.1 standardizes:
</p>

<ul>
  <li>the widget instance model,</li>
  <li>widget roles,</li>
  <li>widget instance structure in canonical source,</li>
  <li>value-carrying widgets,</li>
  <li>widget references,</li>
  <li>widget parts at instance level,</li>
  <li>basic instance-visible property, method, and event concepts,</li>
  <li>a minimal standard widget vocabulary.</li>
</ul>

<p>
FROG v0.1 does not attempt to define a complete industrial UI toolkit. Its purpose is to define a durable common baseline.
</p>

<p>
FROG v0.1 also keeps an explicit architectural split:
</p>

<ul>
  <li><code>Widget.md</code> defines widget instances as source objects,</li>
  <li><code>Widget class contract.md</code> defines class-side member contracts and member legality,</li>
  <li><code>Widget interaction.md</code> defines diagram-side executable access to widgets.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">4. Relation with Other Specifications</h2>

<ul>
  <li><code>Type.md</code> defines the type system used by value-carrying widgets and typed widget members.</li>
  <li><code>Front panel.md</code> defines how widget instances are placed, composed, styled, and serialized in the <code>front_panel</code> section.</li>
  <li><code>Widget class contract.md</code> defines class-side member contracts, part ownership, access legality, capability gating, and IDE-facing object exposure constraints.</li>
  <li><code>Diagram.md</code> defines the executable graph and the node kinds that materialize widget participation in that graph.</li>
  <li><code>Widget interaction.md</code> defines the explicit diagram-side interaction model for widget references, property reads and writes, method invocation, and optional UI sequencing.</li>
  <li><code>Interface.md</code> defines the public program contract and remains distinct from the front panel.</li>
</ul>

<p>
A value-carrying widget participates naturally in dataflow through its primary <code>value</code>. In diagram source, that participation is represented by a <code>widget_value</code> node.
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
This document defines what widget instances are. It does not redefine:
</p>

<ul>
  <li>the executable graph rules,</li>
  <li>public interface rules,</li>
  <li>front-panel composition rules,</li>
  <li>class-side member legality already owned by <code>Widget class contract.md</code>.</li>
</ul>

<hr/>

<h2 id="what-a-widget-is">5. What a Widget Is</h2>

<p>
A widget is an instance of a widget class.
</p>

<p>
A widget instance MUST have stable source identity. Different tools MAY render the same widget differently, but they MUST preserve its source meaning.
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
Canonical source serialization stores source-relevant widget configuration. It MUST NOT depend on arbitrary runtime-only state.
</p>

<p>
A widget is not a public interface port. A widget is not an executable node. A widget is a source-level UI object that may participate in execution through the diagram, but is defined independently from the graph itself.
</p>

<hr/>

<h2 id="widget-class-vs-value-type">6. Widget Class vs Value Type</h2>

<h3>6.1 Widget class</h3>

<p>
A widget class identifies the UI category of the widget instance. Examples:
</p>

<pre><code>frog.ui.standard.numeric_control
frog.ui.standard.boolean_indicator
frog.ui.standard.string_control
frog.ui.standard.panel
</code></pre>

<p>
At the widget-instance level, the declared class determines at least:
</p>

<ul>
  <li>the category of UI object the instance belongs to,</li>
  <li>the compatible roles,</li>
  <li>whether a primary value is expected,</li>
  <li>whether containment is allowed,</li>
  <li>which class-side contract applies to object-style access.</li>
</ul>

<p>
The detailed member surface of the class, including which properties, methods, events, and parts are legally exposed, belongs normatively to <code>Widget class contract.md</code>.
</p>

<h3>6.2 Value type</h3>

<p>
A value type identifies the FROG data type carried by a value-carrying widget. Examples:
</p>

<pre><code>bool
i32
f64
string
array&lt;f64&gt;
</code></pre>

<p>
Value types are defined normatively by <code>Type.md</code>.
</p>

<h3>6.3 Consequence</h3>

<p>
A widget is not a type, and a type is not a widget.
</p>

<ul>
  <li><code>f64</code> is a value type,</li>
  <li><code>frog.ui.standard.numeric_control</code> is a widget class,</li>
  <li>a widget instance may be a numeric control carrying a value of type <code>f64</code>.</li>
</ul>

<hr/>

<h2 id="widget-roles">7. Widget Roles</h2>

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

<h3>7.1 <code>control</code></h3>

<p>
A <code>control</code> is a value-carrying widget intended primarily for user-editable interaction. Its primary value normally flows from the front panel toward executable logic.
</p>

<h3>7.2 <code>indicator</code></h3>

<p>
An <code>indicator</code> is a value-carrying widget intended primarily to display program state. Its primary value normally flows from executable logic toward the front panel.
</p>

<h3>7.3 <code>container</code></h3>

<p>
A <code>container</code> owns child widgets and defines a compositional UI region. In v0.1, standard containers are non-value widgets unless a stricter active profile defines otherwise.
</p>

<h3>7.4 <code>decoration</code></h3>

<p>
A <code>decoration</code> is used primarily for presentation rather than primary program value exchange.
</p>

<h3>7.5 Role compatibility</h3>

<p>
The declared role MUST be compatible with the declared widget class. A tool MUST NOT accept an arbitrary role/class combination unless the active profile explicitly defines it as valid.
</p>

<p>
The legality of a role/class combination is a class-side constraint and therefore depends on the corresponding widget class contract.
</p>

<hr/>

<h2 id="widget-identity-and-lifecycle">8. Widget Identity and Lifecycle</h2>

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

<pre><code>Widget Class
    ↓ instantiates
Widget Instance (source)
    ↓ realizes
Runtime Widget Instance
</code></pre>

<p>
The source instance defines design-time configuration. The runtime instance manages live value, internal UI state, and rendering-related state.
</p>

<p>
Widget identifiers MUST remain unique across the entire recursive front-panel widget tree. This guarantees that diagram-level widget references remain unambiguous.
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

<h2 id="canonical-widget-instance-shape">9. Canonical Widget Instance Shape</h2>

<p>
A canonical widget instance in source form SHOULD follow this general structure:
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
}
</code></pre>

<p>
Common fields are defined below.
</p>

<h3>9.1 <code>id</code></h3>

<ul>
  <li>MUST be a string.</li>
  <li>MUST be unique across the full recursive front-panel widget tree.</li>
  <li>MUST remain stable enough to support source tracking, diagram references, and tool interoperability.</li>
</ul>

<h3>9.2 <code>role</code></h3>

<ul>
  <li>MUST be a valid widget role under the active specification profile.</li>
  <li>MUST be compatible with the declared widget class.</li>
</ul>

<h3>9.3 <code>widget</code></h3>

<ul>
  <li>MUST be a string.</li>
  <li>MUST identify a known widget class under the active specification profile.</li>
</ul>

<p>
For standard built-in widgets defined by this document, identifiers SHOULD use the <code>frog.ui.standard.*</code> namespace.
</p>

<h3>9.4 <code>value_type</code></h3>

<ul>
  <li>MUST exist for value-carrying widgets.</li>
  <li>MUST NOT be required for non-value widgets.</li>
  <li>MUST be a valid canonical FROG type expression according to <code>Type.md</code>.</li>
</ul>

<h3>9.5 <code>layout</code></h3>

<p>
<code>layout</code> stores design-time placement and size information. Its detailed interpretation belongs normatively to <code>Front panel.md</code>.
</p>

<h3>9.6 <code>props</code></h3>

<ul>
  <li>MUST be an object when present.</li>
  <li>MUST contain only source-relevant property values.</li>
  <li>MAY contain inherited and class-specific source-owned properties.</li>
</ul>

<p>
Whether a property is legal, readable, writable, design-time-owned, runtime-owned, or profile-gated depends on the corresponding widget class contract.
</p>

<h3>9.7 <code>parts</code></h3>

<ul>
  <li>MUST be an object when present.</li>
  <li>Keys MUST be stable part names.</li>
  <li>Values MUST be valid part objects for the owning widget class or active profile.</li>
</ul>

<p>
The available part surface and part-member legality belong normatively to the corresponding widget class contract.
</p>

<h3>9.8 <code>children</code></h3>

<ul>
  <li>MAY appear on container widgets.</li>
  <li>MUST be an array when present.</li>
  <li>MUST contain valid child widget instances.</li>
</ul>

<p>
Ownership, nesting, and composition rules belong normatively to <code>Front panel.md</code>.
</p>

<h3>9.9 <code>style_ref</code> and <code>style_override</code></h3>

<p>
Widget instances MAY include visual style references and visual style overrides. These fields remain presentation-related and MUST NOT alter widget semantics, public interface semantics, class-side member legality, or executable graph semantics.
</p>

<hr/>

<h2 id="value-carrying-widgets">10. Value-Carrying Widgets</h2>

<p>
Controls and indicators are value-carrying widgets.
</p>

<h3>10.1 Required value semantics</h3>

<ul>
  <li><code>value_type</code> MUST be defined.</li>
  <li>The widget class MUST support the declared type.</li>
  <li>The widget class MUST define a primary value semantic.</li>
</ul>

<h3>10.2 Primary value path</h3>

<p>
Every value-carrying widget conceptually exposes a primary <code>value</code> member. That primary value is the natural dataflow path between the front panel and the diagram.
</p>

<pre><code>Front Panel Widget
        │
        ▼
widget.value
        │
        ▼
widget_value.value
</code></pre>

<p>
In diagram source, this participation is represented by a <code>widget_value</code> node.
</p>

<h3>10.3 Directional intent</h3>

<ul>
  <li>a control normally provides a value to the diagram,</li>
  <li>an indicator normally receives a value from the diagram.</li>
</ul>

<p>
This directional intent does not redefine executable semantics by itself. The diagram remains authoritative.
</p>

<h3>10.4 Access to <code>value</code> through the object model</h3>

<p>
The primary value MAY also be read or written through the object-style interaction path when the widget class exposes <code>value</code> as a readable or writable property.
</p>

<p>
That legality belongs to the widget class contract and MUST NOT be inferred solely from the fact that the widget is value-carrying.
</p>

<h3>10.5 Distinction that MUST remain explicit</h3>

<pre><code>widget_value access
    !=
object-style property access to value
</code></pre>

<p>
They may refer to related semantics, but they are not the same abstraction layer.
</p>

<hr/>

<h2 id="widget-reference-model">11. Widget Reference Model</h2>

<p>
A widget reference is the object-style access anchor used by the diagram to target a widget as an object rather than only as a natural value source or sink.
</p>

<p>
Conceptually:
</p>

<pre><code>widget_reference
    ↓
widget object
    ├── property read / write
    ├── method invocation
    └── part-scoped access
</code></pre>

<p>
A <code>widget_reference</code> node identifies one widget instance by stable source identity.
</p>

<p>
A widget reference does not by itself define which members are legal. It only anchors object-style access. Member legality depends on the widget class contract, and executable access rules depend on <code>Widget interaction.md</code>.
</p>

<hr/>

<h2 id="widget-parts">12. Widget Parts</h2>

<p>
A widget MAY expose named parts.
</p>

<p>
A part is a named object-owned sub-surface of a widget, such as:
</p>

<ul>
  <li>a label,</li>
  <li>an axis,</li>
  <li>a legend,</li>
  <li>a cursor,</li>
  <li>an increment button,</li>
  <li>a decrement button.</li>
</ul>

<p>
At instance level, parts allow canonical source to attach source-relevant data to sub-surfaces owned by the widget.
</p>

<p>
However:
</p>

<ul>
  <li>the existence of a part for a given class,</li>
  <li>the cardinality of that part,</li>
  <li>the members exposed by that part,</li>
  <li>the legality of part-scoped access</li>
</ul>

<p>
belong normatively to the corresponding widget class contract.
</p>

<p>
A part is not automatically an independent top-level widget. It remains owned by its parent widget unless another specification explicitly states otherwise.
</p>

<hr/>

<h2 id="properties-methods-and-events">13. Properties, Methods, and Events</h2>

<p>
Widgets may expose properties, methods, and runtime events.
</p>

<ul>
  <li>A <strong>property</strong> is a named readable and/or writable member.</li>
  <li>A <strong>method</strong> is a named invocable operation.</li>
  <li>An <strong>event</strong> is a named observable occurrence emitted by the widget or one of its parts.</li>
</ul>

<p>
At the widget-instance level, these concepts exist so that canonical source and diagram interaction can refer to stable object-surface members.
</p>

<p>
This document does not fully define the legality of every property, method, and event on every class. That responsibility belongs to <code>Widget class contract.md</code>.
</p>

<p>
Accordingly:
</p>

<ul>
  <li><code>Widget.md</code> defines that widgets may expose such members,</li>
  <li><code>Widget class contract.md</code> defines which members a class actually exposes and under which access conditions,</li>
  <li><code>Widget interaction.md</code> defines how diagram-side executable access uses those members.</li>
</ul>

<hr/>

<h2 id="widget-behavior-model">14. Widget Behavior Model</h2>

<p>
A widget instance has two related but distinct behavioral viewpoints:
</p>

<ul>
  <li><strong>source-side behavior</strong> — the declared object surface and source-owned configuration recorded in canonical source,</li>
  <li><strong>runtime-side behavior</strong> — the live behavior realized by an IDE or runtime host.</li>
</ul>

<p>
Canonical source standardizes the first viewpoint. It does not serialize arbitrary live runtime state.
</p>

<p>
The source-side behavior model therefore includes:
</p>

<ul>
  <li>class identity,</li>
  <li>role,</li>
  <li>value-carrying status,</li>
  <li>source-owned configuration,</li>
  <li>source-visible parts,</li>
  <li>stable object-surface naming needed for interaction.</li>
</ul>

<p>
The runtime realization MAY include richer internal behavior, but that richness MUST NOT become the hidden source of normative truth for canonical source validity.
</p>

<hr/>

<h2 id="serialization-vs-runtime-state">15. Serialization vs Runtime State</h2>

<p>
Canonical widget serialization stores source-relevant information only.
</p>

<p>
Examples of source-relevant information include:
</p>

<ul>
  <li>widget identity,</li>
  <li>declared class,</li>
  <li>role,</li>
  <li>value type,</li>
  <li>source-owned property defaults,</li>
  <li>layout,</li>
  <li>source-visible part configuration,</li>
  <li>child-widget composition.</li>
</ul>

<p>
Examples of runtime-only information include:
</p>

<ul>
  <li>current focus ownership,</li>
  <li>live repaint handles,</li>
  <li>host-specific control handles,</li>
  <li>temporary hover state,</li>
  <li>renderer-private caches.</li>
</ul>

<p>
Canonical source MUST NOT depend on runtime-only data for validity.
</p>

<p>
The design-time versus runtime-owned boundary of individual members is defined more precisely by the corresponding widget class contract.
</p>

<hr/>

<h2 id="standard-widget-classes-for-v01">16. Standard Widget Classes for v0.1</h2>

<p>
FROG v0.1 defines a minimal baseline vocabulary of standard widget classes. Typical standardized examples include:
</p>

<ul>
  <li><code>frog.ui.standard.numeric_control</code></li>
  <li><code>frog.ui.standard.numeric_indicator</code></li>
  <li><code>frog.ui.standard.boolean_control</code></li>
  <li><code>frog.ui.standard.boolean_indicator</code></li>
  <li><code>frog.ui.standard.string_control</code></li>
  <li><code>frog.ui.standard.string_indicator</code></li>
  <li><code>frog.ui.standard.panel</code></li>
  <li><code>frog.ui.standard.label</code></li>
</ul>

<p>
This baseline exists to guarantee a small portable common core.
</p>

<p>
Profiles MAY define additional widget classes or richer widget vocabularies. Such extensions MUST remain compatible with the widget instance model defined here and with the class-side contract model defined in <code>Widget class contract.md</code>.
</p>

<hr/>

<h2 id="addressing-model">17. Addressing Model</h2>

<p>
Widget interaction requires stable addressing.
</p>

<p>
At minimum, addressing distinguishes:
</p>

<ul>
  <li>the widget instance itself,</li>
  <li>the primary value path of value-carrying widgets,</li>
  <li>part-scoped access,</li>
  <li>member-scoped object access.</li>
</ul>

<p>
Conceptually:
</p>

<pre><code>widget
widget.value
widget.part
widget.part.member
widget.member
</code></pre>

<p>
The precise legality of a given member path depends on the widget class contract. The executable form of such access belongs to <code>Widget interaction.md</code>.
</p>

<hr/>

<h2 id="validation-rules">18. Validation Rules</h2>

<p>
Validators MUST enforce at least the following rules:
</p>

<ul>
  <li>a widget instance MUST have a stable <code>id</code>,</li>
  <li>a widget instance MUST declare a known <code>widget</code> class,</li>
  <li>a widget instance MUST declare a compatible <code>role</code>,</li>
  <li>a value-carrying widget MUST declare a valid <code>value_type</code>,</li>
  <li><code>props</code> MUST be an object when present,</li>
  <li><code>parts</code> MUST be an object when present,</li>
  <li><code>children</code> MUST be an array when present,</li>
  <li>widget identifiers MUST be unique across the full recursive widget tree.</li>
</ul>

<p>
Validators SHOULD additionally diagnose at least:
</p>

<ul>
  <li>unknown widget class,</li>
  <li>invalid role/class combination,</li>
  <li>missing <code>value_type</code> on a value-carrying widget,</li>
  <li>illegal <code>value_type</code> for the class,</li>
  <li>invalid source-owned property shape,</li>
  <li>unknown or invalid part instance shape.</li>
</ul>

<p>
Detailed legality of class members, part members, access modes, profile gates, and host gates belongs to the corresponding widget class contract and to the relevant interaction validation.
</p>

<hr/>

<h2 id="examples">19. Examples</h2>

<h3>19.1 Numeric control widget instance</h3>

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
    "caption": "Gain"
  }
}
</code></pre>

<h3>19.2 Boolean indicator widget instance</h3>

<pre><code>{
  "id": "ind_ready",
  "role": "indicator",
  "widget": "frog.ui.standard.boolean_indicator",
  "value_type": "bool",
  "layout": {
    "x": 20,
    "y": 70,
    "width": 120,
    "height": 28
  },
  "props": {
    "caption": "Ready"
  }
}
</code></pre>

<h3>19.3 Container widget instance</h3>

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
  "children": [
    {
      "id": "ctrl_gain",
      "role": "control",
      "widget": "frog.ui.standard.numeric_control",
      "value_type": "f64"
    }
  ]
}
</code></pre>

<hr/>

<h2 id="out-of-scope-for-v01">20. Out of Scope for v0.1</h2>

<p>
The following are intentionally out of scope for this document in v0.1:
</p>

<ul>
  <li>a full industrial widget catalog,</li>
  <li>pixel-perfect rendering identity across runtimes,</li>
  <li>one mandatory theme system,</li>
  <li>one mandatory runtime object model,</li>
  <li>the full class-side contract surface for every widget class,</li>
  <li>the full executable semantics of widget interaction primitives,</li>
  <li>a complete UI event-loop specification.</li>
</ul>

<hr/>

<h2 id="summary">21. Summary</h2>

<p>
A FROG widget is a structured source-level UI object with stable identity, declared class, declared role, optional primary value, optional parts, and explicit participation paths toward executable interaction.
</p>

<p>
This document defines widget instances as they exist in canonical source.
</p>

<p>
It does not define:
</p>

<ul>
  <li>front-panel composition ownership,</li>
  <li>class-side member legality,</li>
  <li>diagram-side executable widget interaction semantics,</li>
  <li>general language execution semantics.</li>
</ul>

<p>
That separation allows FROG to support rich widget objects without collapsing source instance shape, class contract, executable access, one IDE, and one runtime into the same layer.
</p>
