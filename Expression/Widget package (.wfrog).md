<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Widget Package (.wfrog)</h1>

<p align="center">
  <strong>Normative package model for widget-oriented artifacts, widget class packages, front-panel packages, and bounded widget behavior publication</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-document-exists">2. Why This Document Exists</a></li>
  <li><a href="#scope">3. Scope</a></li>
  <li><a href="#relation-with-other-specifications">4. Relation with Other Specifications</a></li>
  <li><a href="#ownership-boundary">5. Ownership Boundary</a></li>
  <li><a href="#design-goals">6. Design Goals</a></li>
  <li><a href="#relationship-between-frog-and-wfrog">7. Relationship Between <code>.frog</code> and <code>.wfrog</code></a></li>
  <li><a href="#wfrog-core-principle">8. <code>.wfrog</code> Core Principle</a></li>
  <li><a href="#package-kinds">9. Package Kinds</a></li>
  <li><a href="#common-top-level-model">10. Common Top-Level Model</a></li>
  <li><a href="#package-import-model">11. Package Import Model</a></li>
  <li><a href="#widget-class-package">12. Widget Class Package</a></li>
  <li><a href="#front-panel-package">13. Front-Panel Package</a></li>
  <li><a href="#widget-class-publication-model">14. Widget Class Publication Model</a></li>
  <li><a href="#bounded-behavior-publication-model">15. Bounded Behavior Publication Model</a></li>
  <li><a href="#svg-assets-and-visual-resources">16. SVG Assets and Visual Resources</a></li>
  <li><a href="#host-bindings">17. Host Bindings</a></li>
  <li><a href="#runtime-interpretation-model">18. Runtime Interpretation Model</a></li>
  <li><a href="#developer-defined-widget-classes">19. Developer-Defined Widget Classes</a></li>
  <li><a href="#portability-and-conformance">20. Portability and Conformance</a></li>
  <li><a href="#versioning-and-ids">21. Versioning and IDs</a></li>
  <li><a href="#minimal-examples">22. Minimal Examples</a></li>
  <li><a href="#design-rules">23. Design Rules</a></li>
  <li><a href="#non-goals">24. Non-Goals</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The <code>.wfrog</code> format is the canonical widget-oriented package format of FROG.
It exists to keep widget-oriented structure explicit, inspectable, modular, and portable
without collapsing widget class publication, host realization, visual assets, and bounded widget behavior
into the canonical <code>.frog</code> program source.
</p>

<p>
A <code>.wfrog</code> artifact is a structured JSON package that MAY define:
</p>

<ul>
  <li>widget class packages,</li>
  <li>front-panel packages,</li>
  <li>visual resources and SVG references,</li>
  <li>host realization bindings,</li>
  <li>bounded portable behavior modules.</li>
</ul>

<p>
This document defines the architectural role and normative structure of that package format.
</p>

<h2 id="why-this-document-exists">2. Why This Document Exists</h2>

<p>
FROG requires a disciplined widget object system that remains open across runtimes and host implementations.
The canonical <code>.frog</code> source must remain the authoritative program source,
but it must not carry every detail of widget class law, widget packaging, host realization mapping,
visual resource binding, or portable widget behavior publication.
</p>

<p>
The <code>.wfrog</code> format therefore exists to:
</p>

<ul>
  <li>separate canonical program meaning from widget-oriented package content,</li>
  <li>support reusable widget class publication,</li>
  <li>support explicit front-panel realization packages,</li>
  <li>support developer-defined widget classes in an inspectable form,</li>
  <li>enable multi-runtime interpretation in Python, Rust, C/C++, and other environments,</li>
  <li>support SVG as a first-class visual resource without turning SVG into semantic truth,</li>
  <li>publish bounded widget behavior without collapsing the model into runtime-private code.</li>
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
  <li>how widget classes are published in machine-readable form,</li>
  <li>how bounded widget behavior is published,</li>
  <li>how runtimes interpret package content,</li>
  <li>how host-specific realization is bounded,</li>
  <li>how SVG participates in the widget system.</li>
</ul>

<p>
This document does not define the full executable semantics of diagram execution.
Those remain owned by the language, FIR, and lowering layers.
</p>

<h2 id="relation-with-other-specifications">4. Relation with Other Specifications</h2>

<ul>
  <li><strong><code>Expression/Widget class contract.md</code></strong> defines the normative class-level law that a widget class package publishes in machine-readable form.</li>
  <li><strong><code>Expression/Widget.md</code></strong> defines widget instances as source-visible participants in a <code>.frog</code> program.</li>
  <li><strong><code>Expression/Front panel.md</code></strong> defines front-panel composition in canonical program source.</li>
  <li><strong><code>Expression/Widget interaction.md</code></strong> defines natural-value and object-style interaction with widget instances.</li>
  <li><strong><code>Libraries/UI.md</code></strong> defines standard UI library posture and shared cross-runtime expectations.</li>
</ul>

<p>
This document is the package-layer bridge between class-level widget law and runtime-consumable widget-oriented artifacts.
</p>

<h2 id="ownership-boundary">5. Ownership Boundary</h2>

<p>
The following ownership boundary is normative:
</p>

<ul>
  <li><strong><code>.frog</code></strong> owns canonical program source and executable graph participation.</li>
  <li><strong>Widget class contract</strong> owns class-level widget law.</li>
  <li><strong><code>.wfrog</code></strong> owns widget-oriented packages, widget class publication, front-panel package structure, bounded portable behavior publication, and visual resource packaging.</li>
  <li><strong>Runtime</strong> owns interpretation of standardized widget package content.</li>
  <li><strong>Host</strong> owns concrete rendering realization, input collection, and toolkit adaptation.</li>
  <li><strong>SVG</strong> owns visual resource content only, not executable semantic truth.</li>
</ul>

<p>
A <code>.wfrog</code> package MUST NOT replace <code>.frog</code> as the canonical source of program meaning.
One runtime implementation MUST NOT redefine the meaning of FROG widgets by private convention.
</p>

<h2 id="design-goals">6. Design Goals</h2>

<ul>
  <li>Keep the program source canonical and reviewable.</li>
  <li>Support reusable widget classes across multiple programs.</li>
  <li>Support front-panel packaging without embedding all realization detail in <code>.frog</code>.</li>
  <li>Allow modular widget systems beyond a fixed hardcoded widget list.</li>
  <li>Preserve portability across runtime families.</li>
  <li>Allow host-specific realization without semantic drift.</li>
  <li>Support SVG explicitly but safely.</li>
  <li>Support developer-defined widget classes without hiding class law in runtime-private code.</li>
  <li>Support bounded behavior publication in a form that remains inspectable and portable.</li>
</ul>

<h2 id="relationship-between-frog-and-wfrog">7. Relationship Between <code>.frog</code> and <code>.wfrog</code></h2>

<p>
The canonical <code>.frog</code> source remains the authoritative authored program source.
A <code>.frog</code> program MAY reference one or more <code>.wfrog</code> packages in order to resolve:
</p>

<ul>
  <li>widget class references,</li>
  <li>front-panel instance realization,</li>
  <li>visual resource mappings,</li>
  <li>portable bounded widget behavior,</li>
  <li>host-oriented widget configuration.</li>
</ul>

<p>
A conforming runtime MUST treat the <code>.frog</code> source as authoritative for program structure,
and MUST treat <code>.wfrog</code> packages as widget-oriented support artifacts interpreted under
published class and package rules.
</p>

<p>
A <code>.frog</code> file says that a widget instance participates in a program.
A <code>.wfrog</code> file says which widget classes exist, how they are packaged,
which visual resources are available, which bounded behaviors are portable,
and how a front panel may be materially realized without changing program meaning.
</p>

<h2 id="wfrog-core-principle">8. <code>.wfrog</code> Core Principle</h2>

<p>
The core principle of <code>.wfrog</code> is:
</p>

<blockquote>
  <p>
    Widget-oriented structure must be explicit, packageable, inspectable, and interpretable,
    but must not replace the canonical authored program source.
  </p>
</blockquote>

<p>
That principle applies equally to widget class law publication, front-panel packaging,
visual resources, and bounded behavior publication.
</p>

<h2 id="package-kinds">9. Package Kinds</h2>

<p>
A <code>.wfrog</code> package MUST declare a top-level <code>kind</code>.
In v0.1, the following kinds are defined:
</p>

<ul>
  <li><code>widget_class_package</code></li>
  <li><code>front_panel_package</code></li>
</ul>

<p>
A runtime MUST reject a package whose <code>kind</code> is unknown for the declared package schema target.
</p>

<p>
Future package kinds MAY be introduced by later published specification work,
but they are not implied by this document unless explicitly standardized.
</p>

<h2 id="common-top-level-model">10. Common Top-Level Model</h2>

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

<p>
The following top-level fields are optional but recommended:
</p>

<ul>
  <li><code>imports</code> — package dependencies and imported class domains,</li>
  <li><code>metadata</code> — descriptive metadata that does not redefine semantics,</li>
  <li><code>extensions</code> — explicitly marked extension surfaces.</li>
</ul>

<h2 id="package-import-model">11. Package Import Model</h2>

<p>
A <code>.wfrog</code> package MAY import other packages.
Imports exist to allow reusable class libraries, shared visual resources, shared themes,
and shared bounded behavior modules.
</p>

<p>
An import declaration SHOULD identify:
</p>

<ul>
  <li>the imported package reference,</li>
  <li>the expected compatibility range,</li>
  <li>an optional alias,</li>
  <li>whether the import is required or optional.</li>
</ul>

<p>
Imported content MUST NOT silently override already-resolved class identities.
If import conflict resolution is supported by a runtime, the conflict rules MUST be explicit and inspectable.
</p>

<h2 id="widget-class-package">12. Widget Class Package</h2>

<p>
A <code>widget_class_package</code> defines one or more widget classes.
It is the package-level surface used to publish reusable widget class descriptions
in a machine-readable form that conforms to the widget class contract.
</p>

<p>
A widget class package MAY contain:
</p>

<ul>
  <li><code>widget_classes</code>,</li>
  <li><code>svg_assets</code>,</li>
  <li><code>visual_resources</code>,</li>
  <li><code>host_bindings</code>,</li>
  <li><code>behavior_modules</code>.</li>
</ul>

<p>
The class package does not replace the widget class contract.
Rather, it publishes one or more concrete class definitions under that contract.
</p>

<p>
A widget class package SHOULD be the primary publication mechanism for:
</p>

<ul>
  <li>stable <code>class_id</code> definitions,</li>
  <li>primary value posture,</li>
  <li>property, method, event, and part inventories,</li>
  <li>portable behavior modules attached to published classes,</li>
  <li>visual resource references used by those classes.</li>
</ul>

<h2 id="front-panel-package">13. Front-Panel Package</h2>

<p>
A <code>front_panel_package</code> defines one or more front-panel realizations.
It is used to describe concrete widget instance realization, layout, initial visual configuration,
front-panel resources, panel-level theming, and package-level realization metadata.
</p>

<p>
A front-panel package MAY contain:
</p>

<ul>
  <li><code>front_panels</code>,</li>
  <li><code>svg_assets</code>,</li>
  <li><code>visual_resources</code>,</li>
  <li><code>host_bindings</code>,</li>
  <li><code>themes</code>,</li>
  <li><code>resources</code>.</li>
</ul>

<p>
A front-panel package MUST NOT redefine the class-level law of a widget class.
It may configure and realize widget instances, but it does not become the source of class semantics.
</p>

<p>
A front-panel package SHOULD focus on:
</p>

<ul>
  <li>panel identity,</li>
  <li>panel layout and composition,</li>
  <li>widget instance realization metadata,</li>
  <li>resource references,</li>
  <li>panel-level host binding hints.</li>
</ul>

<h2 id="widget-class-publication-model">14. Widget Class Publication Model</h2>

<p>
A widget class published in a <code>widget_class_package</code> MUST publish the stable semantic surfaces
required by the widget class contract.
</p>

<p>
A class publication SHOULD therefore include:
</p>

<ul>
  <li><code>class_id</code>,</li>
  <li><code>category</code>,</li>
  <li><code>primary_value</code>,</li>
  <li><code>properties</code>,</li>
  <li><code>methods</code>,</li>
  <li><code>events</code>,</li>
  <li><code>parts</code>,</li>
  <li><code>behavior_refs</code> or embedded behavior declarations,</li>
  <li>optional visual resource references,</li>
  <li>optional host binding references.</li>
</ul>

<p>
A class publication MUST be sufficient for a conforming runtime to determine:
</p>

<ul>
  <li>what the class is,</li>
  <li>which members are portable,</li>
  <li>which members are mutable or persistent,</li>
  <li>which parts are addressable,</li>
  <li>which portable behavior surfaces are attached to the class.</li>
</ul>

<h2 id="bounded-behavior-publication-model">15. Bounded Behavior Publication Model</h2>

<p>
FROG supports extensible widget behavior only if that behavior remains bounded and inspectable.
For that reason, <code>.wfrog</code> MAY publish behavior modules in a standardized form.
</p>

<p>
Portable behavior publication is divided into three categories:
</p>

<ul>
  <li><strong>declarative behavior</strong> — mappings, constraints, triggers, value projections, derived state rules, and other machine-readable behavior declarations,</li>
  <li><strong>bounded pure expressions</strong> — portable expressions without host side effects,</li>
  <li><strong>host-private hooks</strong> — explicitly non-portable integration points for runtime or host adaptation.</li>
</ul>

<p>
A <code>behavior_module</code> SHOULD declare:
</p>

<ul>
  <li><code>behavior_id</code>,</li>
  <li><code>kind</code>,</li>
  <li>declared inputs and outputs,</li>
  <li>trigger conditions when applicable,</li>
  <li>portability posture,</li>
  <li>scope of attachment, such as class-level, part-level, or panel-level.</li>
</ul>

<p>
Portable behavior MUST NOT be defined only inside runtime-private code if the behavior changes
the portable interpretation of widget members.
</p>

<p>
Host-private hooks are allowed, but they MUST be explicitly marked as non-portable and MUST NOT redefine
published class law.
</p>

<h2 id="svg-assets-and-visual-resources">16. SVG Assets and Visual Resources</h2>

<p>
SVG is a first-class visual resource in FROG widget packaging.
A package MAY reference SVG assets for:
</p>

<ul>
  <li>widget face templates,</li>
  <li>layered visual skins,</li>
  <li>part anchoring,</li>
  <li>scalable visual composition,</li>
  <li>decorative panel assets.</li>
</ul>

<p>
Visual resources MAY also include non-SVG assets where supported by published package rules,
but SVG remains the preferred explicit scalable vector resource model.
</p>

<p>
SVG content MUST NOT become hidden executable truth.
No runtime may infer class law from arbitrary SVG structure.
SVG MUST NOT own:
</p>

<ul>
  <li>dynamic widget values,</li>
  <li>portable method law,</li>
  <li>portable event law,</li>
  <li>widget class identity,</li>
  <li>bounded behavior semantics.</li>
</ul>

<p>
SVG may support visual anchoring, named visual layers, and other rendering-oriented mappings,
but those mappings remain subordinate to published widget semantics.
</p>

<h2 id="host-bindings">17. Host Bindings</h2>

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
  <li>host adapter mapping hints,</li>
  <li>resource binding hints,</li>
  <li>non-portable integration identifiers.</li>
</ul>

<p>
Host bindings MUST NOT change widget semantic law.
They may inform realization, but they do not redefine class members, primary value semantics,
or portable event and method meaning.
</p>

<h2 id="runtime-interpretation-model">18. Runtime Interpretation Model</h2>

<p>
A conforming runtime that consumes <code>.wfrog</code> packages MUST be able to:
</p>

<ul>
  <li>load package metadata,</li>
  <li>resolve imports,</li>
  <li>resolve widget classes,</li>
  <li>instantiate declared widget instances or class realizations,</li>
  <li>apply property values,</li>
  <li>support property reads and writes,</li>
  <li>invoke declared methods,</li>
  <li>emit or observe declared events,</li>
  <li>resolve part-local members,</li>
  <li>bind portable behavior modules,</li>
  <li>connect widget instances to host realization,</li>
  <li>bind visual assets and front-panel resources.</li>
</ul>

<p>
A runtime MUST interpret standardized package content rather than rely exclusively on a closed,
hardcoded widget inventory.
</p>

<p>
A runtime MAY internally optimize, cache, lower, or precompile package content,
but such internal strategies do not replace the published package model.
</p>

<h2 id="developer-defined-widget-classes">19. Developer-Defined Widget Classes</h2>

<p>
FROG is intended to support developer-defined widget classes.
The <code>.wfrog</code> package model is the normative publication mechanism that allows those classes
to remain inspectable and portable across runtimes.
</p>

<p>
A developer-defined class is portable only if its class law is published through a <code>widget_class_package</code>
in a form that conforms to the widget class contract.
</p>

<p>
A developer-defined widget class publication SHOULD therefore include:
</p>

<ul>
  <li>a stable <code>class_id</code>,</li>
  <li>its category,</li>
  <li>its primary value posture,</li>
  <li>its member inventories,</li>
  <li>its addressable parts,</li>
  <li>its bounded portable behavior surfaces,</li>
  <li>its visual resource references where needed,</li>
  <li>its explicitly marked non-portable hooks where needed.</li>
</ul>

<p>
A runtime may choose not to implement a given developer-defined class,
but it MUST NOT reinterpret that class arbitrarily while claiming conformance.
</p>

<h2 id="portability-and-conformance">20. Portability and Conformance</h2>

<p>
The widget system supports portability through explicit contracts and bounded extension points.
A package or package section is portable only to the extent that it stays inside:
</p>

<ul>
  <li>published class law,</li>
  <li>published package structure,</li>
  <li>published type system and access rules,</li>
  <li>published behavior publication rules,</li>
  <li>published host-binding boundaries.</li>
</ul>

<p>
Host-private extensions MUST be marked explicitly.
A package MUST NOT claim portability for behavior or realization content that depends on hidden host-private semantics.
</p>

<h2 id="versioning-and-ids">21. Versioning and IDs</h2>

<p>
A <code>.wfrog</code> package MUST declare a package-level <code>spec_version</code>.
This version is distinct from:
</p>

<ul>
  <li>the repository specification corpus version,</li>
  <li>the <code>.frog</code> source file <code>spec_version</code>,</li>
  <li>the authored program version,</li>
  <li>the package content version.</li>
</ul>

<p>
Package content versioning belongs in <code>package.version</code>.
Compatibility with the <code>.wfrog</code> specification model belongs in <code>spec_version</code>.
</p>

<p>
Schema identifiers SHOULD use stable FROG URN identifiers.
For example:
</p>

<pre><code>"$id": "urn:frog:expression:schema:frog.widget-package:0.1"</code></pre>

<p>
Package, class, panel, behavior, and resource identifiers SHOULD be stable within their declared package scope.
</p>

<h2 id="minimal-examples">22. Minimal Examples</h2>

<p>
Minimal widget class package example:
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
  "widget_classes": [
    {
      "class_id": "frog.widgets.numeric_indicator",
      "category": "indicator",
      "primary_value": {
        "present": true,
        "type": "float64",
        "access": "read_write"
      },
      "properties": [
        {
          "name": "value",
          "type": "float64",
          "access": "read_write"
        },
        {
          "name": "foreground_color",
          "type": "frog.color.rgba8",
          "access": "read_write"
        }
      ],
      "methods": [],
      "events": [],
      "parts": [
        {
          "part_id": "root",
          "kind": "container"
        }
      ],
      "behavior_refs": []
    }
  ]
}</code></pre>

<p>
Minimal front-panel package example:
</p>

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
          "instance_id": "input_control",
          "class_ref": "frog.widgets.numeric_control"
        },
        {
          "instance_id": "count_indicator",
          "class_ref": "frog.widgets.numeric_indicator"
        }
      ]
    }
  ]
}</code></pre>

<h2 id="design-rules">23. Design Rules</h2>

<ul>
  <li><code>.frog</code> remains the canonical program source.</li>
  <li><code>.wfrog</code> packages remain widget-oriented support artifacts.</li>
  <li>Class law remains explicit and inspectable.</li>
  <li>Portable behavior remains bounded and publishable.</li>
  <li>Runtime interpretation remains bounded by published contracts.</li>
  <li>Host realization remains separate from semantic ownership.</li>
  <li>SVG remains visual, not semantic truth.</li>
  <li>Developer-defined widget classes must be publishable without making one runtime implementation the language definition.</li>
</ul>

<h2 id="non-goals">24. Non-Goals</h2>

<ul>
  <li>Defining one mandatory host toolkit for all FROG implementations.</li>
  <li>Collapsing widget behavior into arbitrary runtime-private code.</li>
  <li>Using SVG as hidden widget logic.</li>
  <li>Forcing all widget realization content into <code>.frog</code>.</li>
  <li>Equating one runtime implementation with the FROG widget standard.</li>
  <li>Making <code>.wfrog</code> the canonical owner of program meaning.</li>
</ul>
