<h1 align="center">🐸 FROG IDE Preferences Specification</h1>

<p align="center">
Tool preference metadata for <strong>.frog</strong> programs<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#principles">2. Core principles</a></li>
  <li><a href="#location">3. Location in a .frog file</a></li>
  <li><a href="#structure">4. IDE preferences structure</a></li>
  <li><a href="#diagram-preferences">5. Diagram preferences</a></li>
  <li><a href="#front-panel-preferences">6. Front panel preferences</a></li>
  <li><a href="#execution-hints">7. Execution hints</a></li>
  <li><a href="#ui-behavior">8. UI behavior and editor workflow</a></li>
  <li><a href="#validation">9. Validation and compatibility rules</a></li>
  <li><a href="#extensibility">10. Extensibility</a></li>
  <li><a href="#examples">11. Examples</a></li>
  <li><a href="#summary">12. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <strong>ide</strong> section stores optional development-environment preferences associated with a Frog.
</p>

<p>
This section is intended for editor UX and workflow configuration:
</p>

<ul>
  <li>visual preferences (colors, grids, rulers)</li>
  <li>layout and canvas defaults</li>
  <li>editor behavior hints</li>
  <li>execution-related hints for tooling</li>
</ul>

<p>
The <code>ide</code> section <strong>MUST NOT affect execution semantics</strong>.
Runtimes MUST ignore this section completely.
</p>

<hr/>

<h2 id="principles">2. Core principles</h2>

<ul>
  <li><strong>Tool-agnostic</strong>: Preferences should not assume a specific framework.</li>
  <li><strong>Non-authoritative</strong>: Preferences never change program meaning.</li>
  <li><strong>Safe to ignore</strong>: Any tool can ignore them without breaking execution.</li>
  <li><strong>Stable diffs</strong>: Formatting tools should minimize noisy changes.</li>
</ul>

<hr/>

<h2 id="location">3. Location in a .frog file</h2>

<p>
The IDE preferences object is an optional top-level section.
</p>

<pre>{
  "spec_version": "0.1",
  "metadata": {},
  "interface": {},
  "connector": {},
  "diagram": {},
  "front_panel": {},
  "ide": { }
}</pre>

<p>
If omitted, tools MAY use their own defaults.
</p>

<hr/>

<h2 id="structure">4. IDE preferences structure</h2>

<p>
Recommended structure:
</p>

<pre>"ide": {
  "diagram": {},
  "front_panel": {},
  "execution": {},
  "workflow": {}
}</pre>

<p>
All sub-objects are optional.
</p>

<hr/>

<h2 id="diagram-preferences">5. Diagram preferences</h2>

<p>
Preferences for diagram rendering and editing.
</p>

Example:

<pre>"diagram": {
  "background_color": "#202020",
  "grid": {
    "enabled": true,
    "size": 10,
    "snap": true
  },
  "wires": {
    "style": "curved",
    "show_dots": false
  },
  "zoom": {
    "default": 1.0
  }
}</pre>

Suggested fields:

<ul>
  <li><code>background_color</code> — string color</li>
  <li><code>grid.enabled</code> — boolean</li>
  <li><code>grid.size</code> — integer</li>
  <li><code>grid.snap</code> — boolean</li>
  <li><code>wires.style</code> — string (e.g., <code>curved</code>, <code>orthogonal</code>)</li>
  <li><code>zoom.default</code> — number</li>
</ul>

<hr/>

<h2 id="front-panel-preferences">6. Front panel preferences</h2>

<p>
Preferences for front panel editing and rendering.
</p>

Example:

<pre>"front_panel": {
  "background_color": "#FFFFFF",
  "alignment_guides": {
    "enabled": true
  },
  "snap": {
    "enabled": true,
    "size": 5
  }
}</pre>

Suggested fields:

<ul>
  <li><code>background_color</code> — string color</li>
  <li><code>alignment_guides.enabled</code> — boolean</li>
  <li><code>snap.enabled</code> — boolean</li>
  <li><code>snap.size</code> — integer</li>
</ul>

<hr/>

<h2 id="execution-hints">7. Execution hints</h2>

<p>
Execution hints are preferences interpreted by tools.
They may influence how an IDE configures execution, debugging, or build actions,
but they MUST NOT change the meaning of the program itself.
</p>

Example:

<pre>"execution": {
  "debug_enabled": true,
  "reentrant_hint": false,
  "preferred_profile": "core",
  "run_on_open": false,
  "auto_validate_on_save": true
}</pre>

Suggested fields:

<ul>
  <li><code>debug_enabled</code> — boolean</li>
  <li><code>reentrant_hint</code> — boolean</li>
  <li><code>preferred_profile</code> — string (e.g., core, rt, fpga)</li>
  <li><code>run_on_open</code> — boolean</li>
  <li><code>auto_validate_on_save</code> — boolean</li>
</ul>

<p>
Runtimes MUST ignore these hints.
</p>

<hr/>

<h2 id="ui-behavior">8. UI behavior and editor workflow</h2>

<p>
Workflow preferences support editor UX and user habits.
</p>

Example:

<pre>"workflow": {
  "panes": {
    "show_palette": true,
    "show_properties": true
  },
  "search": {
    "default_scope": "project"
  },
  "history": {
    "remember_window_state": true
  }
}</pre>

Suggested fields:

<ul>
  <li><code>panes.show_palette</code> — boolean</li>
  <li><code>panes.show_properties</code> — boolean</li>
  <li><code>search.default_scope</code> — string</li>
  <li><code>history.remember_window_state</code> — boolean</li>
</ul>

<hr/>

<h2 id="validation">9. Validation and compatibility rules</h2>

Implementations MUST enforce:

<ul>
  <li>If <code>ide</code> exists, it MUST be a JSON object.</li>
  <li>Unknown IDE fields MUST be safely ignored by runtimes.</li>
  <li>IDE fields MUST NOT redefine execution semantics.</li>
</ul>

<p>
Tools SHOULD preserve unknown fields to support interoperability between editors.
</p>

<hr/>

<h2 id="extensibility">10. Extensibility</h2>

<p>
The IDE preferences section is intentionally extensible.
Tools MAY add additional keys, for example:
</p>

<pre>"ide": {
  "diagram": { "background_color": "#202020" },
  "custom_tool": {
    "feature_x_enabled": true,
    "layout_profile": "compact"
  }
}</pre>

Rules:

<ul>
  <li>Unknown fields MUST NOT impact execution.</li>
  <li>Unknown fields SHOULD be preserved by formatting tools.</li>
</ul>

<hr/>

<h2 id="examples">11. Examples</h2>

<h3>11.1 Minimal IDE preferences</h3>

<pre>"ide": {
  "diagram": { "background_color": "#202020" }
}</pre>

<h3>11.2 Full IDE preferences example</h3>

<pre>"ide": {
  "diagram": {
    "background_color": "#202020",
    "grid": { "enabled": true, "size": 10, "snap": true },
    "wires": { "style": "curved", "show_dots": false },
    "zoom": { "default": 1.0 }
  },
  "front_panel": {
    "background_color": "#FFFFFF",
    "alignment_guides": { "enabled": true },
    "snap": { "enabled": true, "size": 5 }
  },
  "execution": {
    "debug_enabled": true,
    "reentrant_hint": false,
    "preferred_profile": "core",
    "run_on_open": false,
    "auto_validate_on_save": true
  },
  "workflow": {
    "panes": { "show_palette": true, "show_properties": true },
    "search": { "default_scope": "project" },
    "history": { "remember_window_state": true }
  }
}</pre>

<hr/>

<h2 id="summary">12. Summary</h2>

<p>
The <code>ide</code> section stores optional tool preferences for a Frog.
</p>

<ul>
  <li>It enables consistent editor behavior and visual defaults.</li>
  <li>It is non-authoritative and safe to ignore.</li>
  <li>Runtimes MUST ignore IDE preferences entirely.</li>
  <li>Tools MAY extend it freely while preserving compatibility.</li>
</ul>
