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
<li><a href="#hierarchy">7. Conceptual Object Hierarchy</a></li>
<li><a href="#roles">8. Widget Roles</a></li>
<li><a href="#fields">9. Common Widget Instance Fields</a></li>
<li><a href="#value-widgets">10. Value-Carrying Widgets</a></li>
<li><a href="#parts">11. Widget Parts</a></li>
<li><a href="#properties">12. Properties, Methods, and Events</a></li>
<li><a href="#inheritance">13. Property and Method Inheritance</a></li>
<li><a href="#serialization">14. Serialization vs Runtime Reflection</a></li>
<li><a href="#standard-widgets">15. Standard Widget Classes for v0.1</a></li>
<li><a href="#addressing">16. Property and Method Addressing</a></li>
<li><a href="#validation">17. Validation Rules</a></li>
<li><a href="#examples">18. Examples</a></li>
<li><a href="#out-of-scope">19. Out of Scope</a></li>
<li><a href="#summary">20. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The FROG front panel is composed of <strong>widgets</strong>.
A widget is a structured user-interface object capable of displaying data,
accepting user input, exposing properties, invoking methods, and emitting events.
</p>

<p>
Widgets are not merely graphical shapes.
They are structured UI objects with identity, behavior, and interaction semantics.
</p>

<p>
This document defines the widget object model used by FROG,
including widget classes, widget roles, widget parts,
and how widgets interact with the program diagram.
</p>

<hr/>

<h2 id="goals">2. Goals of the Widget Model</h2>

<ul>
<li><strong>Object consistency</strong> — widgets behave as structured objects.</li>
<li><strong>Separation of concerns</strong> — UI representation, value typing, and program logic remain independent.</li>
<li><strong>Extensibility</strong> — specialized widgets can extend the model.</li>
<li><strong>Stable serialization</strong> — only meaningful design-time data appears in the source file.</li>
<li><strong>Tool interoperability</strong> — different editors can reconstruct equivalent widget behavior.</li>
</ul>

<hr/>

<h2 id="scope">3. Scope for v0.1</h2>

<p>
FROG v0.1 standardizes:
</p>

<ul>
<li>the widget object model</li>
<li>widget classes and roles</li>
<li>value-carrying widgets</li>
<li>widget parts</li>
<li>basic properties and methods</li>
<li>a minimal standard widget set</li>
</ul>

<p>
FROG v0.1 does not attempt to define a complete industrial UI toolkit.
</p>

<hr/>

<h2 id="relation">4. Relation with Other Specifications</h2>

<ul>
<li><strong>Type.md</strong> defines the type system used by value-carrying widgets.</li>
<li><strong>FrontPanel.md</strong> defines how widget instances are placed and composed.</li>
<li><strong>Diagram.md</strong> defines the executable dataflow graph.</li>
<li><strong>Interface.md</strong> defines the public program contract.</li>
</ul>

<p>
Value-carrying widgets implicitly expose a diagram terminal corresponding
to their <code>value</code> property.
</p>

<p>
This allows widgets to participate directly in the dataflow graph
without requiring explicit UI binding objects.
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
<li>carry a typed value</li>
<li>display program state</li>
<li>accept user input</li>
<li>contain child widgets</li>
<li>expose configurable properties</li>
<li>expose callable methods</li>
<li>emit events</li>
<li>own attached parts such as labels or captions</li>
</ul>

<hr/>

<h2 id="class-vs-type">6. Widget Class vs Value Type</h2>

<p>
Widget classes and value types are distinct concepts.
</p>

<h3>Widget class</h3>

<p>
Defines the UI object category.
</p>

<pre>
frog.ui.standard.numeric_control
frog.ui.standard.boolean_indicator
frog.ui.standard.string_control
frog.ui.standard.panel
</pre>

<h3>Value type</h3>

<p>
Defines the data type carried by the widget.
</p>

<pre>
bool
i32
f64
string
array&lt;f64&gt;
</pre>

<hr/>

<h2 id="hierarchy">7. Conceptual Object Hierarchy</h2>

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

<p>
This hierarchy defines conceptual behavior shared by widgets.
Implementations are not required to use literal inheritance.
</p>

<hr/>

<h2 id="roles">8. Widget Roles</h2>

<p>
Every widget instance MUST declare a role.
</p>

<ul>
<li><code>control</code></li>
<li><code>indicator</code></li>
<li><code>container</code></li>
<li><code>decoration</code></li>
</ul>

<hr/>

<h2 id="fields">9. Common Widget Instance Fields</h2>

Example widget instance:

<pre><code>{
"id": "ctrl_gain",
"role": "control",
"widget": "frog.ui.standard.numeric_control",
"value_type": "f64",
"layout": { "x":20, "y":20, "width":120, "height":28 },
"props": {},
"parts": {}
}</code></pre>

<table>
<tr><th>Field</th><th>Description</th></tr>
<tr><td>id</td><td>stable widget identifier</td></tr>
<tr><td>role</td><td>widget role</td></tr>
<tr><td>widget</td><td>widget class identifier</td></tr>
<tr><td>value_type</td><td>value type carried by widget</td></tr>
<tr><td>layout</td><td>design-time geometry</td></tr>
<tr><td>props</td><td>serialized properties</td></tr>
<tr><td>parts</td><td>attached sub-objects</td></tr>
</table>

<hr/>

<h2 id="value-widgets">10. Value-Carrying Widgets</h2>

<p>
Controls and indicators carry typed values.
</p>

Rules:

<ul>
<li><code>value_type</code> MUST be defined.</li>
<li>The widget class MUST support the declared type.</li>
</ul>

<h3>Diagram terminal</h3>

<p>
Every value-carrying widget implicitly exposes a diagram terminal
representing its <code>value</code> property.
</p>

<pre>
Front Panel Widget
        │
        ▼
widget.value
        │
        ▼
Diagram Terminal
</pre>

<p>
This terminal participates in the program dataflow graph.
</p>

<hr/>

<h2 id="parts">11. Widget Parts</h2>

<p>
Widgets may contain attached parts.
Parts represent structured UI sub-objects.
</p>

Example:

<pre>
ctrl_gain.label.text
</pre>

Example serialization:

<pre><code>
"parts": {
 "label": {
  "class": "frog.ui.standard.label_part",
  "props": {
   "text": "Gain"
  }
 }
}
</code></pre>

<hr/>

<h2 id="properties">12. Properties, Methods, and Events</h2>

Widgets expose:

<ul>
<li><strong>properties</strong></li>
<li><strong>methods</strong></li>
<li><strong>events</strong></li>
</ul>

Examples:

<pre>
ctrl_gain.visible
ctrl_gain.enabled
ctrl_gain.focus()
ctrl_gain.reset_to_default()
</pre>

<hr/>

<h2 id="inheritance">13. Property and Method Inheritance</h2>

Widgets inherit behavior from conceptual base classes.

Example hierarchy:

<pre>
UIObject
  └ Widget
      └ ValueWidget
          └ NumericControl
</pre>

<hr/>

<h2 id="serialization">14. Serialization vs Runtime Reflection</h2>

FROG distinguishes:

<ul>
<li><strong>serialized source properties</strong></li>
<li><strong>runtime reflection metadata</strong></li>
</ul>

Runtime metadata MUST NOT appear in canonical source.

<hr/>

<h2 id="standard-widgets">15. Standard Widget Classes for v0.1</h2>

<h3>Containers</h3>

<pre>
frog.ui.standard.panel
</pre>

<h3>Decoration widgets</h3>

<pre>
frog.ui.standard.text_label
</pre>

<h3>Value widgets</h3>

<pre>
frog.ui.standard.numeric_control
frog.ui.standard.numeric_indicator
frog.ui.standard.boolean_control
frog.ui.standard.boolean_indicator
frog.ui.standard.string_control
frog.ui.standard.string_indicator
</pre>

<hr/>

<h2 id="addressing">16. Property and Method Addressing</h2>

Examples:

<pre>
ctrl_gain.value
ctrl_gain.visible
ctrl_gain.label.text
ctrl_gain.focus()
</pre>

<p>
The <code>value</code> property has special semantics because it participates
in diagram dataflow.
</p>

<hr/>

<h2 id="validation">17. Validation Rules</h2>

<ul>
<li>every widget MUST define <code>id</code></li>
<li>widget ids MUST be unique</li>
<li>value widgets MUST declare <code>value_type</code></li>
<li>widget role MUST match widget class</li>
</ul>

<hr/>

<h2 id="examples">18. Examples</h2>

<h3>Numeric control</h3>

<pre><code>{
"id":"ctrl_gain",
"role":"control",
"widget":"frog.ui.standard.numeric_control",
"value_type":"f64",
"props":{
 "default_value":1.0,
 "minimum":0,
 "maximum":10
}
}</code></pre>

<h3>Boolean indicator</h3>

<pre><code>{
"id":"led_ready",
"role":"indicator",
"widget":"frog.ui.standard.boolean_indicator",
"value_type":"bool"
}</code></pre>

<hr/>

<h2 id="out-of-scope">19. Out of Scope</h2>

<ul>
<li>complete UI toolkit</li>
<li>advanced graph widgets</li>
<li>event loop scheduling</li>
<li>animation systems</li>
</ul>

<hr/>

<h2 id="summary">20. Summary</h2>

<p>
Widgets are structured UI objects capable of carrying values,
exposing properties and methods,
and participating in the program dataflow graph
through implicit value terminals.
</p>

<p>
This widget model forms the foundation of the FROG front panel system.
</p>

<hr/>

<p align="center">
End of FROG Widget Specification
</p>
