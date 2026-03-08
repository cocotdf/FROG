<h1 align="center">🐸 FROG Front Panel Specification</h1>

<p align="center">
Definition of the front panel (interaction layer) for <strong>.frog</strong> programs<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Design goals</a></li>
  <li><a href="#location">3. Location in a .frog file</a></li>
  <li><a href="#relationship-with-interface-and-diagram">4. Relationship with interface and diagram</a></li>
  <li><a href="#structure">5. Front panel structure</a></li>
  <li><a href="#canvas">6. Canvas and coordinate system</a></li>
  <li><a href="#elements">7. Elements</a>
    <ul>
      <li><a href="#controls">7.1 Controls</a></li>
      <li><a href="#indicators">7.2 Indicators</a></li>
      <li><a href="#text">7.3 Text and labels</a></li>
      <li><a href="#comments">7.4 Comments</a></li>
      <li><a href="#shapes">7.5 Shapes</a></li>
      <li><a href="#images">7.6 Images</a></li>
      <li><a href="#groups">7.7 Groups</a></li>
    </ul>
  </li>
  <li><a href="#bindings">8. Bindings</a></li>
  <li><a href="#layout-model">9. Layout model</a></li>
  <li><a href="#style-system">10. Style system</a>
    <ul>
      <li><a href="#theme">10.1 Theme</a></li>
      <li><a href="#fonts">10.2 Fonts</a></li>
      <li><a href="#colors">10.3 Colors and variables</a></li>
      <li><a href="#overrides">10.4 Overrides</a></li>
    </ul>
  </li>
  <li><a href="#ui-libraries">11. UI libraries</a></li>
  <li><a href="#validation">12. Validation rules</a></li>
  <li><a href="#examples">13. Examples</a></li>
  <li><a href="#summary">14. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <strong>front_panel</strong> section defines the graphical interaction layer of a Frog.
It describes user-facing elements such as controls, indicators, text, comments, shapes, images, and groups.
</p>

<p>
The front panel is part of the canonical <code>.frog</code> source format.
The <code>front_panel</code> section MUST exist, even when a Frog is executed in a headless or non-interactive context.
</p>

<p>
The front panel does <strong>not</strong> define execution logic and does <strong>not</strong> define the public contract of the Frog.
Its role is interaction, presentation, and visualization.
</p>

<p>
Runtimes MAY ignore the front panel during execution.
Development tools, editors, and interactive runtimes MAY use it to render a user interface.
</p>

<hr/>

<h2 id="goals">2. Design goals</h2>

<ul>
  <li>tool-agnostic front panel representation</li>
  <li>stable layout across implementations</li>
  <li>clear and explicit binding rules</li>
  <li>clean separation between logic, public contract, and UI</li>
  <li>modular styling through themes, variables, and overrides</li>
  <li>composable UI through reusable libraries and components</li>
</ul>

<hr/>

<h2 id="location">3. Location in a .frog file</h2>

<pre>{
  "spec_version": "0.1",
  "metadata": {},
  "interface": {},
  "connector": {},
  "diagram": {},
  "front_panel": {}
}</pre>

<p>
The <code>front_panel</code> section MUST exist in a canonical <code>.frog</code> source file.
It MAY be empty.
</p>

<hr/>

<h2 id="relationship-with-interface-and-diagram">4. Relationship with interface and diagram</h2>

<p>
FROG distinguishes three different concepts:
</p>

<ul>
  <li><strong>interface</strong> defines the public logical contract of the Frog</li>
  <li><strong>diagram</strong> defines the executable dataflow logic</li>
  <li><strong>front_panel</strong> defines the user interaction layer</li>
</ul>

<p>
The front panel MUST NOT be interpreted as the public API of the Frog.
Controls and indicators are user-facing elements, not public logical ports.
</p>

<p>
A front panel element MAY be bound to:
</p>

<ul>
  <li>a public interface port</li>
  <li>a valid diagram node port</li>
</ul>

<p>
This allows front panels to expose the public contract of a Frog, internal state, or both, while keeping UI structure separate from execution semantics.
</p>

<p>
In short:
</p>

<ul>
  <li><strong>interface</strong> = what the Frog exposes</li>
  <li><strong>diagram</strong> = how the Frog works</li>
  <li><strong>front_panel</strong> = how users interact with the Frog</li>
</ul>

<hr/>

<h2 id="structure">5. Front panel structure</h2>

<p>
Recommended structure:
</p>

<pre>"front_panel": {
  "canvas": {},
  "elements": [],
  "bindings": [],
  "style": {},
  "ui_libraries": []
}</pre>

<p>
Fields:
</p>

<ul>
  <li><code>canvas</code> — coordinate system and visual background</li>
  <li><code>elements</code> — UI objects such as controls, indicators, text, shapes, images, and groups</li>
  <li><code>bindings</code> — explicit links from UI elements to interface ports or diagram ports</li>
  <li><code>style</code> — theme, fonts, colors, variables, and reusable style definitions</li>
  <li><code>ui_libraries</code> — references to external UI widget libraries</li>
</ul>

<p>
All fields are optional unless otherwise constrained by the validation rules.
An empty front panel is valid.
</p>

<hr/>

<h2 id="canvas">6. Canvas and coordinate system</h2>

<p>
The canvas defines the coordinate system used by front panel elements.
</p>

<pre>"canvas": {
  "units": "px",
  "width": 900,
  "height": 600,
  "background": {
    "color": "#FFFFFF"
  }
}</pre>

<p>
Rules:
</p>

<ul>
  <li>Units SHOULD be <code>px</code> in v0.1.</li>
  <li>Width and height SHOULD be integers.</li>
  <li>The background is purely visual and MUST NOT affect execution semantics.</li>
</ul>

<hr/>

<h2 id="elements">7. Elements</h2>

<p>
All user interface objects are represented as elements.
</p>

<p>
Every element MUST define:
</p>

<ul>
  <li><code>id</code> — unique identifier</li>
  <li><code>kind</code> — element category</li>
  <li><code>layout</code> — position and size</li>
</ul>

<p>
Base element structure:
</p>

<pre>{
  "id": "el_1",
  "kind": "control",
  "type": "numeric",
  "layout": { "x": 20, "y": 20, "width": 120, "height": 28 },
  "props": {},
  "style_ref": "default.control"
}</pre>

<hr/>

<h3 id="controls">7.1 Controls</h3>

<p>
Controls provide user input.
They typically write values to interface inputs or to writable diagram ports.
</p>

<p>
Example:
</p>

<pre>{
  "id": "ctrl_gain",
  "kind": "control",
  "type": "numeric",
  "layout": { "x": 20, "y": 20, "width": 120, "height": 28 },
  "props": {
    "min": 0.0,
    "max": 10.0,
    "step": 0.1,
    "default": 1.0
  },
  "style_ref": "default.control"
}</pre>

<hr/>

<h3 id="indicators">7.2 Indicators</h3>

<p>
Indicators display values produced by the program.
They typically read from interface outputs or from readable diagram ports.
</p>

<p>
Example:
</p>

<pre>{
  "id": "ind_result",
  "kind": "indicator",
  "type": "numeric",
  "layout": { "x": 20, "y": 60, "width": 120, "height": 28 },
  "props": {
    "format": "fixed",
    "precision": 3
  },
  "style_ref": "default.indicator"
}</pre>

<hr/>

<h3 id="text">7.3 Text and labels</h3>

<p>
Text elements display static labels or textual content.
</p>

<p>
Example:
</p>

<pre>{
  "id": "txt_title",
  "kind": "text",
  "layout": { "x": 20, "y": 110, "width": 400, "height": 32 },
  "props": {
    "text": "Example Frog",
    "align": "left"
  },
  "style_ref": "default.title"
}</pre>

<hr/>

<h3 id="comments">7.4 Comments</h3>

<p>
Comments are non-executable annotations intended for users and authors.
</p>

<p>
Example:
</p>

<pre>{
  "id": "cmt_1",
  "kind": "comment",
  "layout": { "x": 20, "y": 150, "width": 500, "height": 80 },
  "props": {
    "text": "This panel demonstrates basic control and indicator binding."
  },
  "style_ref": "default.comment"
}</pre>

<hr/>

<h3 id="shapes">7.5 Shapes</h3>

<p>
Shapes are decorative or structural visual elements.
They do not define execution behavior.
</p>

<p>
Example:
</p>

<pre>{
  "id": "shape_box",
  "kind": "shape",
  "type": "rect",
  "layout": { "x": 10, "y": 10, "width": 160, "height": 90 },
  "props": {
    "radius": 8
  },
  "style_ref": "default.panel_box"
}</pre>

<hr/>

<h3 id="images">7.6 Images</h3>

<p>
Images reference an external resource or embedded vector content.
</p>

<p>
Example:
</p>

<pre>{
  "id": "img_logo",
  "kind": "image",
  "layout": { "x": 720, "y": 20, "width": 160, "height": 160 },
  "props": {
    "source": "assets/logo.svg"
  }
}</pre>

<hr/>

<h3 id="groups">7.7 Groups</h3>

<p>
Groups allow multiple elements to be organized and manipulated as a unit.
A group may contain children elements by reference.
</p>

<p>
Example:
</p>

<pre>{
  "id": "group_1",
  "kind": "group",
  "layout": { "x": 0, "y": 0, "width": 0, "height": 0 },
  "props": {
    "children": ["shape_box", "ctrl_gain", "ind_result"]
  }
}</pre>

<hr/>

<h2 id="bindings">8. Bindings</h2>

<p>
Bindings connect UI elements to interface ports or diagram ports.
Bindings MUST be explicit.
</p>

<p>
Recommended binding structure:
</p>

<pre>"bindings": [
  {
    "element": "ctrl_gain",
    "mode": "write",
    "target": {
      "scope": "interface",
      "port": "gain"
    }
  },
  {
    "element": "ind_result",
    "mode": "read",
    "target": {
      "scope": "interface",
      "port": "result"
    }
  },
  {
    "element": "ind_internal",
    "mode": "read",
    "target": {
      "scope": "diagram",
      "node": "compute_sum",
      "port": "value"
    }
  }
]</pre>

<p>
Fields:
</p>

<ul>
  <li><code>element</code> — identifier of the bound front panel element</li>
  <li><code>mode</code> — interaction mode, such as <code>write</code> or <code>read</code></li>
  <li><code>target</code> — binding destination in the interface or diagram space</li>
</ul>

<p>
Target forms:
</p>

<ul>
  <li><strong>Interface target</strong>: <code>{ "scope": "interface", "port": "name" }</code></li>
  <li><strong>Diagram target</strong>: <code>{ "scope": "diagram", "node": "node_id", "port": "port_name" }</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>Each binding MUST reference an existing element id.</li>
  <li>Each binding MUST reference a valid target according to its scope.</li>
  <li>Bindings MUST be type-compatible.</li>
  <li>Controls SHOULD use <code>write</code> bindings.</li>
  <li>Indicators SHOULD use <code>read</code> bindings.</li>
</ul>

<p>
The binding model defines interaction wiring only.
It MUST NOT introduce additional execution semantics.
</p>

<hr/>

<h2 id="layout-model">9. Layout model</h2>

<p>
Layout defines element geometry and visual ordering.
</p>

<p>
Layout fields:
</p>

<ul>
  <li><code>x</code>, <code>y</code> — position</li>
  <li><code>width</code>, <code>height</code> — size</li>
  <li><code>z</code> (optional) — drawing order</li>
  <li><code>anchor</code> (optional) — responsive behavior hint</li>
</ul>

<p>
Example:
</p>

<pre>"layout": {
  "x": 20,
  "y": 20,
  "width": 120,
  "height": 28,
  "z": 10,
  "anchor": "top_left"
}</pre>

<hr/>

<h2 id="style-system">10. Style system</h2>

<p>
The style system provides modular visual definitions:
</p>

<ul>
  <li>themes</li>
  <li>fonts</li>
  <li>color palettes</li>
  <li>style references</li>
  <li>local overrides</li>
</ul>

<h3 id="theme">10.1 Theme</h3>

<pre>"style": {
  "theme": "default"
}</pre>

<h3 id="fonts">10.2 Fonts</h3>

<pre>"style": {
  "fonts": {
    "default": { "family": "Inter", "size": 12, "weight": 400 },
    "title": { "family": "Inter", "size": 20, "weight": 700 }
  }
}</pre>

<h3 id="colors">10.3 Colors and variables</h3>

<pre>"style": {
  "colors": {
    "bg": "#FFFFFF",
    "fg": "#111111",
    "accent": "#2ECC71"
  }
}</pre>

<h3 id="overrides">10.4 Overrides</h3>

<p>
Elements MAY override style locally.
</p>

<pre>{
  "id": "ctrl_gain",
  "kind": "control",
  "type": "numeric",
  "layout": { "x": 20, "y": 20, "width": 120, "height": 28 },
  "props": { "default": 1.0 },
  "style_ref": "default.control",
  "style_override": { "colors": { "accent": "#FF6600" } }
}</pre>

<p>
Style information is non-semantic and MUST NOT affect execution behavior.
</p>

<hr/>

<h2 id="ui-libraries">11. UI libraries</h2>

<p>
FROG front panels MAY reference external UI widget libraries.
This enables modular and standardized control and indicator sets.
</p>

<p>
Example:
</p>

<pre>"ui_libraries": [
  {
    "name": "frog.ui.standard",
    "version": "0.1.0"
  }
]</pre>

<p>
Tools MAY resolve these libraries from local or remote registries.
Runtimes MUST ignore UI libraries for execution.
</p>

<hr/>

<h2 id="validation">12. Validation rules</h2>

<p>
Implementations MUST enforce:
</p>

<ul>
  <li>Element identifiers MUST be unique.</li>
  <li>Group children MUST reference existing elements.</li>
  <li>All bindings MUST reference valid elements.</li>
  <li>All bindings MUST reference valid targets according to their declared scope.</li>
  <li>Element layouts MUST contain valid numeric coordinates.</li>
  <li>Bindings MUST be type-compatible with their targets.</li>
  <li>Unknown front panel properties MUST NOT affect execution.</li>
</ul>

<p>
Additionally:
</p>

<ul>
  <li>an empty <code>front_panel</code> section is valid</li>
  <li>style and UI library information MUST remain non-authoritative for execution</li>
  <li>tools MAY warn when a control uses a read-only target or an indicator uses a write-only target</li>
</ul>

<hr/>

<h2 id="examples">13. Examples</h2>

<h3>Minimal front panel</h3>

<pre>"front_panel": {
  "canvas": { "units": "px", "width": 600, "height": 400, "background": { "color": "#FFFFFF" } },
  "elements": [],
  "bindings": [],
  "style": {},
  "ui_libraries": []
}</pre>

<h3>Control and indicator bound to the public interface</h3>

<pre>"front_panel": {
  "canvas": { "units": "px", "width": 900, "height": 600, "background": { "color": "#FFFFFF" } },
  "elements": [
    {
      "id": "ctrl_gain",
      "kind": "control",
      "type": "numeric",
      "layout": { "x": 20, "y": 20, "width": 120, "height": 28 },
      "props": { "min": 0.0, "max": 10.0, "step": 0.1, "default": 1.0 },
      "style_ref": "default.control"
    },
    {
      "id": "ind_result",
      "kind": "indicator",
      "type": "numeric",
      "layout": { "x": 20, "y": 60, "width": 120, "height": 28 },
      "props": { "format": "fixed", "precision": 3 },
      "style_ref": "default.indicator"
    },
    {
      "id": "txt_title",
      "kind": "text",
      "layout": { "x": 20, "y": 110, "width": 400, "height": 32 },
      "props": { "text": "Example Frog", "align": "left" },
      "style_ref": "default.title"
    }
  ],
  "bindings": [
    {
      "element": "ctrl_gain",
      "mode": "write",
      "target": { "scope": "interface", "port": "gain" }
    },
    {
      "element": "ind_result",
      "mode": "read",
      "target": { "scope": "interface", "port": "result" }
    }
  ],
  "style": {
    "theme": "default",
    "fonts": {
      "default": { "family": "Inter", "size": 12, "weight": 400 },
      "title": { "family": "Inter", "size": 20, "weight": 700 }
    },
    "colors": {
      "bg": "#FFFFFF",
      "fg": "#111111",
      "accent": "#2ECC71"
    }
  },
  "ui_libraries": [
    { "name": "frog.ui.standard", "version": "0.1.0" }
  ]
}</pre>

<h3>Indicator bound to an internal diagram node</h3>

<pre>"front_panel": {
  "elements": [
    {
      "id": "ind_internal",
      "kind": "indicator",
      "type": "numeric",
      "layout": { "x": 20, "y": 20, "width": 120, "height": 28 },
      "props": {},
      "style_ref": "default.indicator"
    }
  ],
  "bindings": [
    {
      "element": "ind_internal",
      "mode": "read",
      "target": {
        "scope": "diagram",
        "node": "compute_sum",
        "port": "value"
      }
    }
  ]
}</pre>

<hr/>

<h2 id="summary">14. Summary</h2>

<p>
The front panel defines the interaction layer of a Frog through a modular model:
</p>

<ul>
  <li>elements — controls, indicators, text, comments, shapes, images, groups</li>
  <li>bindings — explicit links to interface ports or diagram ports</li>
  <li>layout — geometry and visual ordering</li>
  <li>style — themes, fonts, colors, overrides</li>
  <li>ui libraries — reusable widget sets</li>
</ul>

<p>
The front panel is part of the canonical source format, but it is not the public contract and not the execution logic of the Frog.
</p>

<p>
It exists to define how users see and interact with a Frog, while remaining cleanly separated from interface semantics and dataflow execution.
</p>
