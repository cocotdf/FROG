<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Widget Package (.wfrog)</h1>

<p align="center">
  <strong>Normative package model for widget-oriented artifacts, widget class packages, and front-panel packages</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-document-exists">2. Why This Document Exists</a></li>
  <li><a href="#scope">3. Scope</a></li>
  <li><a href="#ownership-boundary">4. Ownership Boundary</a></li>
  <li><a href="#design-goals">5. Design Goals</a></li>
  <li><a href="#relationship-between-frog-and-wfrog">6. Relationship Between <code>.frog</code> and <code>.wfrog</code></a></li>
  <li><a href="#wfrog-core-principle">7. <code>.wfrog</code> Core Principle</a></li>
  <li><a href="#package-kinds">8. Package Kinds</a></li>
  <li><a href="#common-top-level-model">9. Common Top-Level Model</a></li>
  <li><a href="#widget-class-package">10. Widget Class Package</a></li>
  <li><a href="#front-panel-package">11. Front-Panel Package</a></li>
  <li><a href="#svg-assets">12. SVG Assets</a></li>
  <li><a href="#host-bindings">13. Host Bindings</a></li>
  <li><a href="#behavior-model">14. Behavior Model</a></li>
  <li><a href="#runtime-interpretation-model">15. Runtime Interpretation Model</a></li>
  <li><a href="#portability-and-conformance">16. Portability and Conformance</a></li>
  <li><a href="#versioning-and-ids">17. Versioning and IDs</a></li>
  <li><a href="#minimal-example">18. Minimal Example</a></li>
  <li><a href="#design-rules">19. Design Rules</a></li>
  <li><a href="#non-goals">20. Non-Goals</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <code>.wfrog</code> format is the canonical widget-oriented package format of FROG.
It exists to keep widget-oriented structure explicit, inspectable, modular, and portable
without collapsing widget definition, host rendering, and program logic into the canonical
<code>.frog</code> source file.
</p>

<p>
A <code>.wfrog</code> artifact is a structured JSON package that MAY define:
</p>

<ul>
  <li>widget class packages,</li>
  <li>front-panel packages,</li>
  <li>visual resources and SVG references,</li>
  <li>host realization bindings,</li>
  <li>controlled behavior declarations.</li>
</ul>

<p>
This document defines the architectural role and normative structure of that package format.
</p>

<h2 id="why-this-document-exists">2. Why This Document Exists</h2>

<p>
FROG requires a disciplined widget object system that remains open across runtimes and host
implementations. The canonical <code>.frog</code> source must remain the authoritative program source,
but it must not carry every detail of widget class law, host realization, or visual asset mapping.
</p>

<p>
The <code>.wfrog</code> format therefore exists to:
</p>

<ul>
  <li>separate canonical program meaning from widget-oriented package content,</li>
  <li>support reusable widget class definitions,</li>
  <li>support explicit front-panel realization packages,</li>
  <li>enable multi-runtime interpretation in Python, Rust, C/C++, and other environments,</li>
  <li>support SVG as a first-class visual resource without turning SVG into semantic truth.</li>
</ul>

<h2 id="scope">3. Scope</h2>

<p>
This document defines:
</p>

<ul>
  <li>what <code>.wfrog</code> is,</li>
  <li>which package kinds are allowed,</li>
  <li>how <code>.wfrog</code> relates to <code>.frog</code>,</li>
  <li>which sections belong in a widget package,</li>
  <li>how runtimes interpret package content,</li>
  <li>how host-specific realization is bounded,</li>
  <li>how SVG participates in the widget system.</li>
</ul>

<p>
This document does not define the full executable semantics of diagram execution. Those remain owned
by the language and IR layers.
</p>

<h2 id="ownership-boundary">4. Ownership Boundary</h2>

<p>
The following ownership boundary is normative:
</p>

<ul>
  <li><strong><code>.frog</code></strong> owns canonical program source and executable graph participation.</li>
  <li><strong>Widget class contract</strong> owns class-level widget law.</li>
  <li><strong><code>.wfrog</code></strong> owns widget-oriented packages and front-panel package structure.</li>
  <li><strong>Runtime</strong> owns interpretation of standardized widget package content.</li>
  <li><strong>Host</strong> owns concrete rendering realization and toolkit adaptation.</li>
  <li><strong>SVG</strong> owns visual resource content, not executable semantic truth.</li>
</ul>

<p>
One runtime implementation MUST NOT redefine the meaning of FROG widgets.
</p>

<h2 id="design-goals">5. Design Goals</h2>

<ul>
  <li>Keep the program source canonical and reviewable.</li>
  <li>Support reusable widget classes across multiple programs.</li>
  <li>Support front-panel packaging without embedding all realization detail in <code>.frog</code>.</li>
  <li>Allow modular widget systems beyond a fixed hardcoded widget list.</li>
  <li>Preserve portability across runtime families.</li>
  <li>Allow host-specific realization without semantic drift.</li>
  <li>Support SVG explicitly but safely.</li>
</ul>

<h2 id="relationship-between-frog-and-wfrog">6. Relationship Between <code>.frog</code> and <code>.wfrog</code></h2>

<p>
The canonical <code>.frog</code> source remains the authoritative authored program source.
A <code>.frog</code> program MAY reference one or more <code>.wfrog</code> packages in order to resolve:
</p>

<ul>
  <li>widget class references,</li>
  <li>front-panel instance realization,</li>
  <li>visual resource mappings,</li>
  <li>host-oriented widget configuration.</li>
</ul>

<p>
A conforming runtime MUST treat the <code>.frog</code> source as authoritative for program structure,
and MUST treat <code>.wfrog</code> packages as widget-oriented support artifacts interpreted under
published class and package rules.
</p>

<h2 id="wfrog-core-principle">7. <code>.wfrog</code> Core Principle</h2>

<p>
The core principle of <code>.wfrog</code> is:
</p>

<blockquote>
  <p>
    Widget-oriented structure must be explicit, packageable, inspectable, and interpretable,
    but must not replace the canonical authored program source.
  </p>
</blockquote>

<h2 id="package-kinds">8. Package Kinds</h2>

<p>
A <code>.wfrog</code> package MUST declare a top-level <code>kind</code>.
In v0.1, the following kinds are defined:
</p>

<ul>
  <li><code>widget_class_package</code></li>
  <li><code>front_panel_package</code></li>
</ul>

<p>
A runtime MUST reject a package whose <code>kind</code> is unknown for the declared package schema version.
</p>

<h2 id="common-top-level-model">9. Common Top-Level Model</h2>

<p>
All <code>.wfrog</code> packages share the following top-level structure:
</p>

<pre><code>{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:frog:expression:schema:frog.widget-package:0.1",
  "format": "frog.wfrog",
  "spec_version": "0.1",
  "kind": "widget_class_package",
  "package": {
    "name": "frog.widgets.core",
    "version": "0.1.0"
  },
  "imports": [],
  "metadata": {},
  "extensions": []
}</code></pre>

<p>
The following top-level fields are normative:
</p>

<ul>
  <li><code>format</code> — MUST be <code>frog.wfrog</code>.</li>
  <li><code>spec_version</code> — widget-package compatibility target.</li>
  <li><code>kind</code> — package category.</li>
  <li><code>package.name</code> — package identity.</li>
  <li><code>package.version</code> — package content version.</li>
</ul>

<h2 id="widget-class-package">10. Widget Class Package</h2>

<p>
A <code>widget_class_package</code> defines one or more widget classes. It is the package-level surface
used to publish reusable widget class descriptions.
</p>

<p>
A widget class package MAY contain:
</p>

<ul>
  <li><code>widget_classes</code></li>
  <li><code>svg_assets</code></li>
  <li><code>host_bindings</code></li>
  <li><code>behavior_modules</code></li>
</ul>

<p>
The class package does not replace the widget class contract. Rather, it instantiates that contract
in a machine-readable package format.
</p>

<h2 id="front-panel-package">11. Front-Panel Package</h2>

<p>
A <code>front_panel_package</code> defines one or more front-panel realizations.
It is used to describe concrete widget instances, layout, initial visual configuration,
front-panel resources, and package-level realization metadata.
</p>

<p>
A front-panel package MAY contain:
</p>

<ul>
  <li><code>front_panels</code></li>
  <li><code>svg_assets</code></li>
  <li><code>host_bindings</code></li>
  <li><code>themes</code></li>
  <li><code>resources</code></li>
</ul>

<p>
A front-panel package MUST NOT redefine the class-level law of a widget class.
</p>

<h2 id="svg-assets">12. SVG Assets</h2>

<p>
SVG is a first-class visual resource in FROG widget packaging.
A package MAY reference SVG assets for:
</p>

<ul>
  <li>widget face templates,</li>
  <li>layered visual skins,</li>
  <li>part anchoring,</li>
  <li>scalable visual composition.</li>
</ul>

<p>
SVG content MUST NOT become hidden executable truth.
No runtime may infer class law from arbitrary SVG structure.
</p>

<h2 id="host-bindings">13. Host Bindings</h2>

<p>
A package MAY publish host binding declarations to indicate how a host may realize a widget family
or front-panel package.
</p>

<p>
Host bindings MAY define:
</p>

<ul>
  <li>required host capabilities,</li>
  <li>optional host capabilities,</li>
  <li>preferred rendering families,</li>
  <li>host adapter mapping hints.</li>
</ul>

<p>
Host bindings MUST NOT change widget semantic law.
</p>

<h2 id="behavior-model">14. Behavior Model</h2>

<p>
The FROG widget system is designed to support extensibility without uncontrolled semantic ambiguity.
The behavior posture for v0.1 is:
</p>

<ul>
  <li>declarative behavior — normative and preferred,</li>
  <li>controlled pure expressions — allowed for bounded state derivation,</li>
  <li>host-private plugin hooks — allowed only as non-portable extensions.</li>
</ul>

<p>
Portable widget behavior MUST remain inspectable and bounded by the package model.
</p>

<h2 id="runtime-interpretation-model">15. Runtime Interpretation Model</h2>

<p>
A conforming runtime that consumes <code>.wfrog</code> packages MUST be able to:
</p>

<ul>
  <li>load package metadata,</li>
  <li>resolve imports,</li>
  <li>resolve widget classes,</li>
  <li>instantiate declared widget instances,</li>
  <li>apply property values,</li>
  <li>support property reads and writes,</li>
  <li>invoke declared methods,</li>
  <li>emit declared events,</li>
  <li>connect widget instances to host realization,</li>
  <li>bind visual assets and front-panel resources.</li>
</ul>

<p>
A runtime MUST interpret standardized package content rather than rely exclusively on a closed,
hardcoded widget inventory.
</p>

<h2 id="portability-and-conformance">16. Portability and Conformance</h2>

<p>
The widget system supports portability through explicit contracts and bounded extension points.
A package or package section is portable only to the extent that it stays inside:
</p>

<ul>
  <li>published class law,</li>
  <li>published package structure,</li>
  <li>published type system and access rules,</li>
  <li>published host-binding boundaries.</li>
</ul>

<p>
Host-private extensions MUST be marked explicitly.
</p>

<h2 id="versioning-and-ids">17. Versioning and IDs</h2>

<p>
A <code>.wfrog</code> package MUST declare a package-level <code>spec_version</code>.
This version is distinct from:
</p>

<ul>
  <li>the repository specification corpus version,</li>
  <li>the <code>.frog</code> source file <code>spec_version</code>,</li>
  <li>the authored program version.</li>
</ul>

<p>
Schema identifiers SHOULD use stable FROG URN identifiers.
For example:
</p>

<pre><code>"$id": "urn:frog:expression:schema:frog.widget-package:0.1"</code></pre>

<h2 id="minimal-example">18. Minimal Example</h2>

<pre><code>{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:frog:expression:schema:frog.widget-package:0.1",
  "format": "frog.wfrog",
  "spec_version": "0.1",
  "kind": "front_panel_package",
  "package": {
    "name": "frog.examples.accumulator.ui",
    "version": "0.1.0"
  },
  "imports": [
    {
      "package_ref": "frog.widgets.core"
    }
  ],
  "front_panels": [
    {
      "panel_id": "main_panel",
      "title": "Accumulator",
      "widgets": [
        {
          "instance_id": "count_indicator",
          "class_ref": "frog.widgets.numeric_indicator"
        }
      ]
    }
  ]
}</code></pre>

<h2 id="design-rules">19. Design Rules</h2>

<ul>
  <li><code>.frog</code> remains the canonical program source.</li>
  <li><code>.wfrog</code> packages remain widget-oriented support artifacts.</li>
  <li>Class law remains explicit and inspectable.</li>
  <li>Runtime interpretation remains bounded by published contracts.</li>
  <li>Host realization remains separate from semantic ownership.</li>
  <li>SVG remains visual, not semantic truth.</li>
</ul>

<h2 id="non-goals">20. Non-Goals</h2>

<ul>
  <li>Defining one mandatory host toolkit for all FROG implementations.</li>
  <li>Collapsing widget behavior into arbitrary runtime-private code.</li>
  <li>Using SVG as hidden widget logic.</li>
  <li>Forcing all widget realization content into <code>.frog</code>.</li>
  <li>Equating one runtime implementation with the FROG widget standard.</li>
</ul>
