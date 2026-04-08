<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Widget Behavior</h1>

<p align="center">
  <strong>Behavior model for widget classes, declarative rules, controlled expressions, and optional realization hooks</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-widget-behavior-needs-its-own-boundary">2. Why Widget Behavior Needs Its Own Boundary</a></li>
  <li><a href="#behavior-design-goal">3. Behavior Design Goal</a></li>
  <li><a href="#baseline-position">4. Baseline Position</a></li>
  <li><a href="#behavior-levels">5. Behavior Levels</a></li>
  <li><a href="#level-1-declarative">6. Level 1: Declarative</a></li>
  <li><a href="#level-2-controlled-expressions">7. Level 2: Controlled Expressions</a></li>
  <li><a href="#level-3-optional-hooks">8. Level 3: Optional Hooks</a></li>
  <li><a href="#what-is-not-allowed">9. What Is Not Allowed</a></li>
  <li><a href="#runtime-responsibility">10. Runtime Responsibility</a></li>
  <li><a href="#conformance-boundary">11. Conformance Boundary</a></li>
  <li><a href="#example">12. Example</a></li>
  <li><a href="#summary">13. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the behavior model of FROG widgets.
</p>

<p>
The goal is to allow widgets to be modular and expressive without turning widget behavior into opaque runtime-private code or hidden logic trapped inside visual assets.
</p>

<h2 id="why-widget-behavior-needs-its-own-boundary">2. Why Widget Behavior Needs Its Own Boundary</h2>

<p>
A widget class is more than a list of properties. Real widget systems often need:
</p>

<ul>
  <li>defaulting rules,</li>
  <li>constraint rules,</li>
  <li>derived presentation rules,</li>
  <li>state transitions,</li>
  <li>standard event emission rules,</li>
  <li>bounded reactions to host-side changes.</li>
</ul>

<p>
If those rules are not explicitly bounded, they tend to drift into:
</p>

<ul>
  <li>host-private code,</li>
  <li>runtime-private code,</li>
  <li>SVG-embedded logic,</li>
  <li>or undocumented assumptions.</li>
</ul>

<h2 id="behavior-design-goal">3. Behavior Design Goal</h2>

<p>
The design goal is to support:
</p>

<ul>
  <li>portable widget behavior where practical,</li>
  <li>inspectable behavior definitions,</li>
  <li>multi-runtime interpretability,</li>
  <li>bounded extensibility,</li>
  <li>clear portability degradation when optional behavior is unsupported.</li>
</ul>

<h2 id="baseline-position">4. Baseline Position</h2>

<p>
FROG adopts the following baseline position:
</p>

<ul>
  <li>widget behavior is not purely host-private,</li>
  <li>widget behavior is not unrestricted executable code,</li>
  <li>widget behavior is not hidden inside SVG,</li>
  <li>widget behavior may include declarative rules,</li>
  <li>widget behavior may include controlled expressions,</li>
  <li>widget behavior may include optional hooks, but only under explicit portability boundaries.</li>
</ul>

<h2 id="behavior-levels">5. Behavior Levels</h2>

<p>
The baseline FROG widget behavior model has three levels:
</p>

<ul>
  <li><strong>Level 1</strong> — declarative rules,</li>
  <li><strong>Level 2</strong> — controlled expressions,</li>
  <li><strong>Level 3</strong> — optional hooks.</li>
</ul>

<h2 id="level-1-declarative">6. Level 1: Declarative</h2>

<p>
Declarative behavior is the baseline portable behavior layer.
</p>

<p>
Typical declarative behavior includes:
</p>

<ul>
  <li>default values,</li>
  <li>required properties,</li>
  <li>value range constraints,</li>
  <li>visibility flags,</li>
  <li>member mutability declarations,</li>
  <li>event declaration tables,</li>
  <li>simple state mappings.</li>
</ul>

<p>
Declarative behavior MUST be directly inspectable from the package contents and MUST NOT require arbitrary code execution.
</p>

<h2 id="level-2-controlled-expressions">7. Level 2: Controlled Expressions</h2>

<p>
Controlled expressions are allowed for bounded behavior that is too expressive for simple declarative fields but does not justify arbitrary plugin code.
</p>

<p>
A controlled expression SHOULD be:
</p>

<ul>
  <li>side-effect bounded,</li>
  <li>deterministic,</li>
  <li>evaluable by multiple runtimes,</li>
  <li>limited to an allowed expression subset.</li>
</ul>

<p>
Typical uses include:
</p>

<ul>
  <li>derived visual states,</li>
  <li>clamped values,</li>
  <li>simple enable/disable logic,</li>
  <li>simple event trigger conditions.</li>
</ul>

<p>
Example:
</p>

<pre><code>{
  "kind": "constraint",
  "target": "value",
  "expression": "clamp(value, min, max)"
}</code></pre>

<p>
A runtime that claims support for controlled expressions MUST document which expression subset it supports for the relevant conformance profile.
</p>

<h2 id="level-3-optional-hooks">8. Level 3: Optional Hooks</h2>

<p>
Optional hooks are allowed for realization-side or host-side enrichment that cannot reasonably be standardized at the portable expression level.
</p>

<p>
Examples include:
</p>

<ul>
  <li>specialized host animations,</li>
  <li>native accessibility integration helpers,</li>
  <li>high-performance editing surfaces,</li>
  <li>host-native composition optimizations.</li>
</ul>

<p>
Hooks MUST be explicitly marked as optional and non-portable unless standardized by a future profile or package family.
</p>

<p>
Hooks MUST NOT:
</p>

<ul>
  <li>silently redefine class law,</li>
  <li>replace the declared normative member surface,</li>
  <li>be required to understand basic object legality,</li>
  <li>be treated as the only source of widget behavior truth.</li>
</ul>

<h2 id="what-is-not-allowed">9. What Is Not Allowed</h2>

<p>
The following behavior patterns are not valid as baseline FROG widget behavior:
</p>

<ul>
  <li>arbitrary hidden code execution embedded in visual assets,</li>
  <li>undocumented host-private behavior that changes public widget meaning,</li>
  <li>undeclared properties, methods, or events that only exist in one runtime,</li>
  <li>behavior rules that cannot be inspected without reading one implementation's source code.</li>
</ul>

<h2 id="runtime-responsibility">10. Runtime Responsibility</h2>

<p>
A runtime that interprets widget behavior is responsible for:
</p>

<ul>
  <li>loading behavior definitions,</li>
  <li>evaluating portable declarative and expression rules where supported,</li>
  <li>keeping object state consistent with declared constraints,</li>
  <li>degrading safely when unsupported optional hooks are encountered.</li>
</ul>

<p>
A runtime is not allowed to treat its own private convenience code as the authoritative meaning of the widget.
</p>

<h2 id="conformance-boundary">11. Conformance Boundary</h2>

<p>
Conformance for widget behavior is layered.
</p>

<ul>
  <li>Level 1 declarative behavior SHOULD be the broadest portability baseline.</li>
  <li>Level 2 controlled expressions MAY be supported by conforming runtimes that claim that capability.</li>
  <li>Level 3 optional hooks remain narrower and SHOULD degrade explicitly.</li>
</ul>

<p>
This layered model allows extensibility without pretending that every enrichment is universally portable.
</p>

<h2 id="example">12. Example</h2>

<pre><code>{
  "behavior": {
    "mode": "declarative_plus_expressions",
    "rules": [
      {
        "kind": "constraint",
        "target": "value",
        "expression": "clamp(value, min, max)"
      },
      {
        "kind": "derived_property",
        "target": "alarm_visible",
        "expression": "value > alarm_threshold"
      },
      {
        "kind": "event_rule",
        "event": "value_changed",
        "when": "value != previous(value)"
      }
    ],
    "optional_hooks": [
      {
        "id": "qt6.numeric_editor.animation",
        "kind": "host_plugin",
        "required": false
      }
    ]
  }
}</code></pre>

<h2 id="summary">13. Summary</h2>

<p>
FROG widget behavior is neither frozen to a tiny fixed declarative subset nor opened to uncontrolled arbitrary code.
</p>

<p>
Instead, it is layered:
</p>

<ul>
  <li>declarative where possible,</li>
  <li>expression-based where useful,</li>
  <li>hook-based only where explicitly bounded.</li>
</ul>

<p>
This is the behavior model required for rich widgets that remain inspectable, portable, and multi-runtime credible.
</p>
