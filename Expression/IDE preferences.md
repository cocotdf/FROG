<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG IDE Preferences Specification</h1>

<p align="center">
IDE-facing preferences and recoverability metadata for <strong>.frog</strong> programs<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#principles">2. Core Principles</a></li>
  <li><a href="#location">3. Location in a .frog File</a></li>
  <li><a href="#scope-boundary">4. Scope and Boundary of the <code>ide</code> Section</a></li>
  <li><a href="#structure">5. Recommended Structure</a></li>
  <li><a href="#diagram-preferences">6. Diagram Preferences</a></li>
  <li><a href="#front-panel-preferences">7. Front Panel Preferences</a></li>
  <li><a href="#execution-hints">8. Execution Hints</a></li>
  <li><a href="#workflow-preferences">9. Workflow Preferences</a></li>
  <li><a href="#recoverability-metadata">10. Recoverability Metadata</a></li>
  <li><a href="#validation">11. Validation and Compatibility Rules</a></li>
  <li><a href="#extensibility">12. Extensibility</a></li>
  <li><a href="#examples">13. Examples</a></li>
  <li><a href="#summary">14. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The top-level <code>ide</code> section stores optional IDE-facing metadata associated with a FROG.
</p>

<p>
This metadata exists to support a better authoring experience without changing the meaning of the program.
It MAY contain:
</p>

<ul>
  <li>editor preferences,</li>
  <li>visual defaults,</li>
  <li>workflow preferences,</li>
  <li>tool-interpreted execution hints,</li>
  <li>non-authoritative recoverability metadata that helps an IDE restore authoring state.</li>
</ul>

<p>
The <code>ide</code> section <strong>MUST NOT affect execution semantics</strong>.
Runtimes and execution-facing systems MUST ignore this section completely when determining canonical executable meaning.
</p>

<p>
This section belongs to the FROG Expression because a FROG is a durable editable program unit.
A source file MAY therefore carry IDE-facing preferences and recoverability aids together with its canonical program content,
provided that such metadata remains non-authoritative for execution.
</p>

<hr/>

<h2 id="principles">2. Core Principles</h2>

<ul>
  <li><strong>Tool-agnostic</strong> — IDE metadata SHOULD NOT assume one specific editor framework or UI toolkit.</li>
  <li><strong>Non-authoritative</strong> — IDE metadata MUST NEVER change canonical program meaning.</li>
  <li><strong>Safe to ignore</strong> — a conforming runtime or execution-facing tool MUST be able to ignore the entire <code>ide</code> section safely.</li>
  <li><strong>Recoverable but optional</strong> — IDE metadata MAY help an IDE reopen or restore authoring state, but it MUST NOT be required to interpret the program canonically.</li>
  <li><strong>Stable diffs</strong> — formatting and tooling SHOULD minimize noisy changes in this section.</li>
  <li><strong>Inter-tool survivability</strong> — tools SHOULD preserve unknown fields whenever practical.</li>
</ul>

<hr/>

<h2 id="location">3. Location in a .frog File</h2>

<p>
The <code>ide</code> object is an optional top-level section of a <code>.frog</code> file.
</p>

<pre><code>{
  "spec_version": "0.1",
  "metadata": {},
  "interface": {},
  "connector": {},
  "diagram": {},
  "front_panel": {},
  "ide": {}
}</code></pre>

<p>
If omitted, tools MAY use their own defaults and MAY operate without recoverability metadata.
</p>

<hr/>

<h2 id="scope-boundary">4. Scope and Boundary of the <code>ide</code> Section</h2>

<p>
The <code>ide</code> section is the source-level home for metadata that is meaningful to editors and other authoring tools,
but not authoritative for execution.
</p>

<p>
It MAY contain:
</p>

<ul>
  <li>diagram editing preferences,</li>
  <li>front-panel editing preferences,</li>
  <li>workflow preferences,</li>
  <li>execution-related hints for tools,</li>
  <li>non-authoritative recoverability metadata for re-openable authoring features such as guided editing flows.</li>
</ul>

<p>
It MUST NOT contain:
</p>

<ul>
  <li>canonical executable structure,</li>
  <li>runtime-required semantic data,</li>
  <li>hidden information needed to understand the meaning of the diagram,</li>
  <li>data that redefines primitive identity, structure identity, or language semantics.</li>
</ul>

<p>
If a conflict exists between canonical source sections and <code>ide</code> metadata, canonical source sections win.
</p>

<hr/>

<h2 id="structure">5. Recommended Structure</h2>

<p>
The exact structure of the <code>ide</code> object is extensible.
The following shape is recommended for the standardized v0.1 baseline:
</p>

<pre><code>"ide": {
  "diagram": {},
  "front_panel": {},
  "execution": {},
  "workflow": {},
  "recoverability": {}
}</code></pre>

<p>
All sub-objects are optional.
Tools MAY omit any sub-object they do not use.
Tools MAY add additional keys as long as they preserve the non-authoritative status of this section.
</p>

<hr/>

<h2 id="diagram-preferences">6. Diagram Preferences</h2>

<p>
The <code>diagram</code> sub-object stores preferences for diagram rendering and editing.
</p>

<p>
Example:
</p>

<pre><code>"diagram": {
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
}</code></pre>

<p>
Suggested fields include:
</p>

<ul>
  <li><code>background_color</code> — string color</li>
  <li><code>grid.enabled</code> — boolean</li>
  <li><code>grid.size</code> — integer</li>
  <li><code>grid.snap</code> — boolean</li>
  <li><code>wires.style</code> — string such as <code>curved</code> or <code>orthogonal</code></li>
  <li><code>wires.show_dots</code> — boolean</li>
  <li><code>zoom.default</code> — number</li>
</ul>

<p>
These preferences affect authoring presentation only.
They MUST NOT affect canonical diagram meaning.
</p>

<hr/>

<h2 id="front-panel-preferences">7. Front Panel Preferences</h2>

<p>
The <code>front_panel</code> sub-object stores preferences for front panel editing and rendering.
</p>

<p>
Example:
</p>

<pre><code>"front_panel": {
  "background_color": "#FFFFFF",
  "alignment_guides": {
    "enabled": true
  },
  "snap": {
    "enabled": true,
    "size": 5
  }
}</code></pre>

<p>
Suggested fields include:
</p>

<ul>
  <li><code>background_color</code> — string color</li>
  <li><code>alignment_guides.enabled</code> — boolean</li>
  <li><code>snap.enabled</code> — boolean</li>
  <li><code>snap.size</code> — integer</li>
</ul>

<p>
These preferences affect editor UX only.
They MUST NOT redefine widget behavior or public interface meaning.
</p>

<hr/>

<h2 id="execution-hints">8. Execution Hints</h2>

<p>
The <code>execution</code> sub-object stores execution-related hints interpreted by tools.
These hints MAY influence how an IDE configures execution, debugging, validation, or build actions,
but they MUST NOT change the meaning of the program itself.
</p>

<p>
Example:
</p>

<pre><code>"execution": {
  "debug_enabled": true,
  "reentrant_hint": false,
  "preferred_profile": "core",
  "run_on_open": false,
  "auto_validate_on_save": true
}</code></pre>

<p>
Suggested fields include:
</p>

<ul>
  <li><code>debug_enabled</code> — boolean</li>
  <li><code>reentrant_hint</code> — boolean</li>
  <li><code>preferred_profile</code> — string such as <code>core</code>, <code>rt</code>, or <code>fpga</code></li>
  <li><code>run_on_open</code> — boolean</li>
  <li><code>auto_validate_on_save</code> — boolean</li>
</ul>

<p>
Runtimes MUST ignore these hints when determining execution semantics.
</p>

<hr/>

<h2 id="workflow-preferences">9. Workflow Preferences</h2>

<p>
The <code>workflow</code> sub-object stores editor UX and workflow preferences.
</p>

<p>
Example:
</p>

<pre><code>"workflow": {
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
}</code></pre>

<p>
Suggested fields include:
</p>

<ul>
  <li><code>panes.show_palette</code> — boolean</li>
  <li><code>panes.show_properties</code> — boolean</li>
  <li><code>search.default_scope</code> — string</li>
  <li><code>history.remember_window_state</code> — boolean</li>
</ul>

<p>
These fields are editor conveniences only.
They MUST NOT affect canonical source meaning.
</p>

<hr/>

<h2 id="recoverability-metadata">10. Recoverability Metadata</h2>

<p>
The <code>recoverability</code> sub-object stores non-authoritative IDE metadata that helps an editor restore or reopen
authoring state that would otherwise be inconvenient to reconstruct from canonical source alone.
</p>

<p>
Recoverability metadata MAY support:
</p>

<ul>
  <li>guided authoring re-open workflows,</li>
  <li>presentation-state restoration,</li>
  <li>stable mapping between IDE-level instances and owned canonical objects,</li>
  <li>other authoring-layer recoverability needs that remain non-authoritative for execution.</li>
</ul>

<p>
Recoverability metadata MUST obey all of the following:
</p>

<ul>
  <li>it MUST remain optional,</li>
  <li>it MUST remain non-authoritative for execution semantics,</li>
  <li>it MUST NOT be required to determine canonical executable meaning,</li>
  <li>it MUST be safely ignorable by runtimes, compilers, and other execution-facing systems,</li>
  <li>it SHOULD be preserved by IDEs and formatting tools whenever practical.</li>
</ul>

<p>
At the current repository stage, one important use case is Express authoring recoverability.
For example, an IDE MAY preserve enough state to reopen a guided Express configuration, restore optional terminal visibility,
or keep a stable mapping between an Express-authored instance and its canonical target.
</p>

<p>
Example:
</p>

<pre><code>"recoverability": {
  "express_bindings": [
    {
      "instance_id": "expr_001",
      "express_id": "frog.ide.express.read_text_file",
      "canonical_target_kind": "subfrog",
      "canonical_target_ref": "frog.io.read_text_file.basic",
      "visible_optional_terminals": ["error_in", "error_out"],
      "config": {
        "encoding": "utf8",
        "line_endings": "auto"
      }
    }
  ]
}</code></pre>

<p>
This example is conceptual.
It illustrates the class of source-level recoverability aids that MAY be stored in <code>ide</code>.
It does not define canonical execution meaning.
</p>

<hr/>

<h2 id="validation">11. Validation and Compatibility Rules</h2>

<p>
Implementations MUST enforce the following rules:
</p>

<ul>
  <li>If <code>ide</code> exists, it MUST be a JSON object.</li>
  <li>If present, each known sub-object such as <code>diagram</code>, <code>front_panel</code>, <code>execution</code>, <code>workflow</code>, or <code>recoverability</code> MUST be a JSON object of the expected shape for that tool.</li>
  <li>IDE metadata MUST NOT redefine execution semantics.</li>
  <li>Unknown IDE fields MUST be safely ignored by runtimes and execution-facing systems.</li>
  <li>Recoverability metadata MUST remain optional and non-authoritative.</li>
</ul>

<p>
Tools SHOULD preserve unknown fields to support interoperability between editors and future extensions of the <code>ide</code> model.
</p>

<hr/>

<h2 id="extensibility">12. Extensibility</h2>

<p>
The <code>ide</code> section is intentionally extensible.
Tools MAY add additional keys, for example:
</p>

<pre><code>"ide": {
  "diagram": {
    "background_color": "#202020"
  },
  "recoverability": {
    "custom_editor_state": {
      "feature_x_enabled": true
    }
  },
  "custom_tool": {
    "layout_profile": "compact"
  }
}</code></pre>

<p>
The following extensibility rules apply:
</p>

<ul>
  <li>unknown fields MUST NOT impact execution semantics,</li>
  <li>unknown fields SHOULD be preserved by formatting tools and IDEs whenever practical,</li>
  <li>vendor-specific or tool-specific fields SHOULD be namespaced or clearly grouped when that improves interoperability,</li>
  <li>recoverability-oriented extensions MUST remain non-authoritative for execution.</li>
</ul>

<hr/>

<h2 id="examples">13. Examples</h2>

<h3>13.1 Minimal IDE metadata</h3>

<pre><code>"ide": {
  "diagram": {
    "background_color": "#202020"
  }
}</code></pre>

<h3>13.2 Preferences-focused example</h3>

<pre><code>"ide": {
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
}</code></pre>

<h3>13.3 Preferences plus recoverability example</h3>

<pre><code>"ide": {
  "diagram": {
    "background_color": "#202020",
    "grid": { "enabled": true, "size": 10, "snap": true }
  },
  "workflow": {
    "panes": { "show_palette": true, "show_properties": true }
  },
  "recoverability": {
    "express_bindings": [
      {
        "instance_id": "expr_001",
        "express_id": "frog.ide.express.read_text_file",
        "canonical_target_kind": "subfrog",
        "canonical_target_ref": "frog.io.read_text_file.basic",
        "visible_optional_terminals": ["error_in", "error_out"],
        "config": {
          "encoding": "utf8"
        }
      }
    ]
  }
}</code></pre>

<hr/>

<h2 id="summary">14. Summary</h2>

<p>
The <code>ide</code> section stores optional IDE-facing metadata for a FROG.
</p>

<ul>
  <li>It MAY store editor preferences, execution hints for tools, workflow preferences, and recoverability aids.</li>
  <li>It is non-authoritative and safe to ignore for execution.</li>
  <li>Runtimes and execution-facing systems MUST ignore it completely for semantic interpretation.</li>
  <li>Tools SHOULD preserve unknown fields to support interoperability and future extensions.</li>
  <li>Recoverability metadata MAY help reopen guided authoring flows such as Express, but it MUST NOT become required to understand canonical program meaning.</li>
</ul>
