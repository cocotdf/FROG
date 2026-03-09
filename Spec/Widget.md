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
  <li><a href="#standard-widget-classes">15. Standard Widget Classes for v0.1</a></li>
  <li><a href="#property-and-method-addressing">16. Property and Method Addressing</a></li>
  <li><a href="#validation-rules">17. Validation Rules</a></li>
  <li><a href="#examples">18. Examples</a></li>
  <li><a href="#out-of-scope">19. Out of Scope</a></li>
  <li><a href="#summary">20. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The FROG front panel is composed of <strong>widgets</strong>.
A widget is a structured user interface object capable of displaying data,
accepting user input, exposing properties, invoking methods, and emitting events.
</p>

<p>
Widgets are not merely visual elements.
They are fully defined UI objects with identity, class, behavior,
and interaction semantics.
</p>

<p>
This document defines the widget object model used by FROG,
including the conceptual hierarchy of widgets, their relationship to typed values,
their serialization model, and their interaction with the program diagram.
</p>

<hr/>

<h2 id="goals">2. Goals of the Widget Model</h2>

<ul>
<li><strong>Object consistency</strong> — widgets behave as structured objects rather than graphical fragments.</li>
<li><strong>Separation of concerns</strong> — UI representation, data typing, and program logic remain independent.</li>
<li><strong>Extensibility</strong> — specialized widgets can extend the model without redefining it.</li>
<li><strong>Stable serialization</strong> — only meaningful source information appears in the .frog file.</li>
<li><strong>Tool interoperability</strong> — different editors and runtimes can reconstruct equivalent widget behavior.</li>
</ul>

<hr/>

<h2 id="scope">3. Scope for v0.1</h2>

<p>
FROG v0.1 standardizes:
</p>

<ul>
<li>the widget object model</li>
<li>the distinction between widget classes and value types</li>
<li>common widget roles</li>
<li>widget parts</li>
<li>basic properties, methods, and events</li>
<li>a minimal standard widget vocabulary</li>
</ul>

<p>
FROG v0.1 does not attempt to define a full UI toolkit.
</p>

<hr/>

<h2 id="relation-with-other-specifications">4. Relation with Other Specifications</h2>

<ul>
<li><strong>Type.md</strong> defines the type system used by value-carrying widgets.</li>
<li><strong>FrontPanel.md</strong> defines how widget instances are arranged and composed.</li>
<li><strong>Diagram.md</strong> defines the executable dataflow graph.</li>
<li><strong>Interface.md</strong> defines the public program contract.</li>
</ul>

<p>
Value-carrying widgets implicitly expose a diagram terminal corresponding
to their <code>value</code> property.
</p>

<p>
This allows widgets to participate directly in the dataflow graph.
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
<li>carry a typed value</li>
<li>display program state</li>
<li>accept user input</li>
<li>expose properties</li>
<li>expose callable methods</li>
<li>emit events</li>
<li>contain child widgets</li>
<li>own attached parts</li>
</ul>

<hr/>

<h2 id="widget-vs-type">6. Widget Class vs Value Type</h2>

<p>
A widget class and a value type are distinct concepts.
</p>

<h3>Widget class</h3>

<p>
Defines the UI object category.
</p>

Examples:
