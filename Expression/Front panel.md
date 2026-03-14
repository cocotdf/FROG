<h1 align="center">🐸 FROG Front Panel Specification</h1>

<p align="center">
Definition of the optional front-panel section of <strong>.frog</strong> programs<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
<li><a href="#overview">1. Overview</a></li>
<li><a href="#scope">2. Scope</a></li>
<li><a href="#relation">3. Relation with Other Specifications</a></li>
<li><a href="#location">4. Location in a <code>.frog</code> File</a></li>
<li><a href="#structure">5. Front Panel Structure</a></li>
<li><a href="#widgets">6. Widget Instances</a></li>
<li><a href="#composition">7. Composition and Nesting</a></li>
<li><a href="#diagram-relation">8. Relation with the Diagram</a></li>
<li><a href="#validation">9. Validation Rules</a></li>
<li><a href="#examples">10. Examples</a></li>
<li><a href="#summary">11. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <code>front_panel</code> section describes the optional graphical interaction layer of a FROG program.
</p>

<p>
It declares user-facing widget instances and their composition.
</p>

<p>
A FROG MAY include a front panel, but it is not required.
Programs may be purely diagram-based without any user-facing interface.
</p>

<p>
The front panel defines:
</p>

<ul>
<li>widget instances,</li>
<li>visual composition of widgets,</li>
<li>optional layout information.</li>
</ul>

<p>
The front panel does <strong>not</strong> define:
</p>

<ul>
<li>the public interface of the FROG,</li>
<li>the executable dataflow graph,</li>
<li>runtime scheduling semantics.</li>
</ul>

<p>
Those responsibilities belong respectively to:
</p>

<ul>
<li><code>Interface.md</code></li>
<li><code>Diagram.md</code></li>
<li>the normative execution semantics defined in <code>Language/</code></li>
</ul>

<hr/>

<h2 id="scope">2. Scope</h2>

<p>
This document defines the canonical source representation of the <code>front_panel</code> section when it appears in a <code>.frog</code> file.
</p>

<p>
It specifies:
</p>

<ul>
<li>how widgets are declared,</li>
<li>how widgets are composed into a widget tree,</li>
<li>the structural validation rules for the section.</li>
</ul>

<p>
It intentionally does not standardize a complete UI toolkit.
Widget classes, parts, and styling systems are defined by UI libraries.
</p>

<hr/>

<h2 id="relation">3. Relation with Other Specifications</h2>

<ul>
<li><code>Widget.md</code> defines the widget object model.</li>
<li><code>Widget interaction.md</code> defines diagram-side interaction with widgets.</li>
<li><code>Diagram.md</code> defines the executable graph.</li>
<li><code>Interface.md</code> defines the public contract of the FROG.</li>
</ul>

<p>
Accordingly:
</p>

<ul>
<li><strong>interface</strong> defines public program inputs and outputs,</li>
<li><strong>diagram</strong> defines executable behavior,</li>
<li><strong>widget model</strong> defines UI object semantics,</li>
<li><strong>front_panel</strong> declares the visual composition of widget instances.</li>
</ul>

<hr/>

<h2 id="location">4. Location in a <code>.frog</code> File</h2>

<p>
When present, the front panel appears as a top-level section of a <code>.frog</code> file.
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
</p>

<p>
When absent, the FROG is interpreted as a diagram-only program with no serialized UI composition.
</p>

<hr/>

<h2 id="structure">5. Front Panel Structure</h2>

<p>
The canonical structure of the front panel object is:
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
<li><code>canvas</code> — optional design-time coordinate space.</li>
<li><code>widgets</code> — top-level widget instances.</li>
<li><code>ui_libraries</code> — UI libraries used by the panel.</li>
</ul>

<p>
All fields are optional.
If present they MUST follow the defined structure.
</p>

<hr/>

<h2 id="widgets">6. Widget Instances</h2>

<p>
Widgets are declared as instances following the widget model defined in <code>Widget.md</code>.
</p>

<p>
Typical widget fields include:
</p>

<ul>
<li><code>id</code></li>
<li><code>widget</code> (widget class)</li>
<li><code>role</code></li>
<li><code>value_type</code> when applicable</li>
<li><code>layout</code></li>
<li><code>props</code></li>
<li><code>parts</code></li>
<li><code>children</code></li>
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
}</code></pre>

<hr/>

<h2 id="composition">7. Composition and Nesting</h2>

<p>
The front panel defines a widget tree.
</p>

<p>
Top-level widgets appear in <code>front_panel.widgets</code>.
Container widgets may define child widgets using the <code>children</code> field.
</p>

<p>
Rules:
</p>

<ul>
<li>widget identifiers MUST be unique across the full widget tree,</li>
<li>a widget MUST belong to exactly one container,</li>
<li>container ownership MUST be explicit in source.</li>
</ul>

<hr/>

<h2 id="diagram-relation">8. Relation with the Diagram</h2>

<p>
The front panel does not define executable behavior.
</p>

<p>
Widget participation in program execution is expressed in the diagram.
</p>

<p>
The canonical diagram interaction mechanisms are:
</p>

<ul>
<li><code>widget_value</code> nodes — natural access to a widget primary value,</li>
<li><code>widget_reference</code> nodes — object reference access.</li>
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
These mechanisms are defined in <code>Widget interaction.md</code>.
</p>

<hr/>

<h2 id="validation">9. Validation Rules</h2>

<p>
If the <code>front_panel</code> section exists, validators MUST ensure:
</p>

<ul>
<li>the section is an object,</li>
<li><code>widgets</code> is an array when present,</li>
<li>widget identifiers are unique across the full widget tree,</li>
<li>all widget instances conform to <code>Widget.md</code>,</li>
<li>child widgets appear only under valid container ownership.</li>
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
<li>language execution semantics.</li>
</ul>

<hr/>

<h2 id="examples">10. Examples</h2>

<h3>Minimal front panel</h3>

<pre><code>"front_panel": {
"widgets": []
}</code></pre>

<h3>Front panel with widgets</h3>

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
}</code></pre>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
The <code>front_panel</code> section defines the optional UI composition of a FROG program.
</p>

<ul>
<li>It declares widget instances and their composition.</li>
<li>It is independent from the public interface.</li>
<li>It is independent from the executable diagram.</li>
<li>Execution semantics remain defined by the diagram and the language specification.</li>
</ul>

<p>
This separation allows FROG programs to be either UI-driven or purely computational while preserving a consistent canonical source format.
</p>
