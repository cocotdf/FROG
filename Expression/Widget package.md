<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Widget Package</h1>

<p align="center">
  <strong>Canonical architectural definition of the <code>.wfrog</code> widget-oriented artifact family</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-document-exists">2. Why This Document Exists</a></li>
  <li><a href="#design-objective">3. Design Objective</a></li>
  <li><a href="#core-architectural-decision">4. Core Architectural Decision</a></li>
  <li><a href="#what-wfrog-is">5. What <code>.wfrog</code> Is</a></li>
  <li><a href="#package-kinds">6. Package Kinds</a></li>
  <li><a href="#relation-between-frog-and-wfrog">7. Relation Between <code>.frog</code> and <code>.wfrog</code></a></li>
  <li><a href="#ownership-boundary">8. Ownership Boundary</a></li>
  <li><a href="#minimal-top-level-shape">9. Minimal Top-Level Shape</a></li>
  <li><a href="#widget-class-package">10. Widget Class Package</a></li>
  <li><a href="#widget-realization-package">11. Widget Realization Package</a></li>
  <li><a href="#widget-bundle-package">12. Widget Bundle Package</a></li>
  <li><a href="#versioning-posture">13. Versioning Posture</a></li>
  <li><a href="#portability-and-conformance">14. Portability and Conformance</a></li>
  <li><a href="#example-minimal-class-package">15. Example: Minimal Class Package</a></li>
  <li><a href="#example-minimal-realization-package">16. Example: Minimal Realization Package</a></li>
  <li><a href="#summary">17. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the architectural role of the <code>.wfrog</code> file family in FROG.
</p>

<p>
A canonical <code>.frog</code> file remains the authoritative source file for the program itself. A <code>.wfrog</code> file is a widget-oriented artifact used to describe widget classes, widget realization information, or both, without collapsing those concerns into the canonical program source.
</p>

<p>
The purpose of this separation is to keep the language inspectable, portable, and multi-runtime compatible while still allowing a rich widget object system.
</p>

<h2 id="why-this-document-exists">2. Why This Document Exists</h2>

<p>
FROG already distinguishes:
</p>

<ul>
  <li>the executable diagram,</li>
  <li>the optional front panel,</li>
  <li>widget instances,</li>
  <li>object-style widget access,</li>
  <li>and class-level widget legality.</li>
</ul>

<p>
That distinction is necessary, but by itself it is not sufficient to support a long-term widget ecosystem across multiple runtimes and hosts.
</p>

<p>
Without a dedicated widget-oriented artifact family, toolchains would tend to fall into one of two bad outcomes:
</p>

<ul>
  <li>too much widget law gets pushed into the canonical <code>.frog</code> source, or</li>
  <li>too much widget law gets pushed into runtime-private implementation code.</li>
</ul>

<p>
The <code>.wfrog</code> family exists to prevent both failures.
</p>

<h2 id="design-objective">3. Design Objective</h2>

<p>
The design objective is to support a disciplined widget object model that:
</p>

<ul>
  <li>works across Python, Rust, C/C++, and other runtimes,</li>
  <li>supports standard and future widget families,</li>
  <li>supports host-specific realization without turning host behavior into language truth,</li>
  <li>supports SVG as a first-class visual asset format,</li>
  <li>remains inspectable and reviewable,</li>
  <li>does not trap FROG in one runtime-owned hardcoded widget list.</li>
</ul>

<h2 id="core-architectural-decision">4. Core Architectural Decision</h2>

<p>
FROG adopts the following architectural decision:
</p>

<ul>
  <li><code>.frog</code> remains the canonical program source,</li>
  <li><code>.wfrog</code> is introduced as the widget-oriented artifact family,</li>
  <li><code>.wfrog</code> packages are typed by an explicit package kind,</li>
  <li>widget class law is not owned by one runtime,</li>
  <li>widget realization is not the same thing as widget class law,</li>
  <li>visual assets such as SVG are not executable truth.</li>
</ul>

<p>
This means that widget semantics, class legality, and host realization are related but distinct layers.
</p>

<h2 id="what-wfrog-is">5. What <code>.wfrog</code> Is</h2>

<p>
A <code>.wfrog</code> file is a structured widget-oriented package serialized in JSON form and stored with the <code>.wfrog</code> extension.
</p>

<p>
A <code>.wfrog</code> package is not a second canonical program file. It does not replace the program-owned role of <code>.frog</code>. It carries widget-oriented definitions that are referenced by the canonical program source and interpreted by runtimes and hosts according to standardized ownership rules.
</p>

<h2 id="package-kinds">6. Package Kinds</h2>

<p>
A <code>.wfrog</code> package MUST declare its package kind explicitly.
</p>

<p>
The baseline package kinds are:
</p>

<ul>
  <li><code>widget_class_package</code></li>
  <li><code>widget_realization_package</code></li>
  <li><code>widget_bundle_package</code></li>
</ul>

<p>
These package kinds have distinct roles.
</p>

<h3>6.1 <code>widget_class_package</code></h3>

<p>
A widget class package defines one or more widget classes, including:
</p>

<ul>
  <li>class identity,</li>
  <li>legal roles,</li>
  <li>value model,</li>
  <li>properties,</li>
  <li>methods,</li>
  <li>events,</li>
  <li>parts,</li>
  <li>mutability boundaries,</li>
  <li>addressing rules,</li>
  <li>and other class-level constraints.</li>
</ul>

<h3>6.2 <code>widget_realization_package</code></h3>

<p>
A widget realization package defines how one or more widget classes may be realized by a host, including:
</p>

<ul>
  <li>visual assets,</li>
  <li>SVG templates,</li>
  <li>anchor mappings,</li>
  <li>part-to-visual bindings,</li>
  <li>property-to-visual bindings,</li>
  <li>method-to-host bindings,</li>
  <li>event-to-host bindings,</li>
  <li>and bounded host-specific hints.</li>
</ul>

<h3>6.3 <code>widget_bundle_package</code></h3>

<p>
A widget bundle package combines both class and realization content. This is allowed for packaging convenience, but it SHOULD NOT be treated as the only or default long-term architectural form.
</p>

<p>
The baseline architectural preference remains explicit separation between class law and realization.
</p>

<h2 id="relation-between-frog-and-wfrog">7. Relation Between <code>.frog</code> and <code>.wfrog</code></h2>

<p>
A canonical <code>.frog</code> source file may reference one or more <code>.wfrog</code> packages.
</p>

<p>
The <code>.frog</code> file owns:
</p>

<ul>
  <li>widget instances used by the program,</li>
  <li>widget identity,</li>
  <li>widget role,</li>
  <li>class reference,</li>
  <li>value type,</li>
  <li>instance-level persisted values and instance-level settings where allowed,</li>
  <li>front-panel composition and placement,</li>
  <li>diagram-side participation through <code>widget_value</code> and <code>widget_reference</code>.</li>
</ul>

<p>
The <code>.frog</code> file does not own the full class definition of the widget and does not own the full host realization definition of the widget.
</p>

<h2 id="ownership-boundary">8. Ownership Boundary</h2>

<p>
The ownership boundary is mandatory.
</p>

<ul>
  <li><strong><code>.frog</code></strong> owns program instances and program-side usage.</li>
  <li><strong>Widget class contract</strong> owns class-level legality and normative member surfaces.</li>
  <li><strong><code>widget_class_package</code></strong> owns the serializable machine-readable form of that class-level law.</li>
  <li><strong><code>widget_realization_package</code></strong> owns host realization mappings and visual integration definitions.</li>
  <li><strong>Runtime</strong> owns interpretation and live object instantiation.</li>
  <li><strong>Host</strong> owns actual rendering, input dispatch, focus, redraw, and native visual behavior.</li>
  <li><strong>SVG</strong> owns visual description only, not executable or semantic truth.</li>
</ul>

<h2 id="minimal-top-level-shape">9. Minimal Top-Level Shape</h2>

<p>
A <code>.wfrog</code> package MUST be a JSON object with a stable top-level shape.
</p>

<pre><code>{
  "wfrog_version": "0.1",
  "kind": "widget_class_package",
  "package": {
    "name": "frog.ui.standard.numeric",
    "version": "0.1.0",
    "namespace": "frog.ui.standard"
  }
}</code></pre>

<p>
The package MAY additionally contain:
</p>

<ul>
  <li><code>imports</code>,</li>
  <li><code>classes</code>,</li>
  <li><code>targets</code>,</li>
  <li><code>assets</code>,</li>
  <li><code>extensions</code>,</li>
  <li><code>notes</code>.</li>
</ul>

<h2 id="widget-class-package">10. Widget Class Package</h2>

<p>
A widget class package SHOULD contain one or more class definitions. A class definition SHOULD include:
</p>

<ul>
  <li><code>class_id</code>,</li>
  <li><code>display_name</code>,</li>
  <li><code>roles</code>,</li>
  <li><code>value_model</code>,</li>
  <li><code>properties</code>,</li>
  <li><code>methods</code>,</li>
  <li><code>events</code>,</li>
  <li><code>parts</code>,</li>
  <li><code>behavior</code>,</li>
  <li><code>host_requirements</code>,</li>
  <li><code>extensions</code>.</li>
</ul>

<p>
A class package defines what the runtime is allowed to expose and what the program is allowed to address.
</p>

<h2 id="widget-realization-package">11. Widget Realization Package</h2>

<p>
A widget realization package SHOULD define one or more realization targets for one or more classes.
</p>

<p>
A realization target SHOULD include:
</p>

<ul>
  <li>the target <code>class_id</code>,</li>
  <li>the intended <code>host_family</code>,</li>
  <li>a <code>visual</code> section,</li>
  <li><code>part_bindings</code>,</li>
  <li><code>property_bindings</code>,</li>
  <li><code>method_bindings</code>,</li>
  <li><code>event_bindings</code>,</li>
  <li>bounded <code>host_private</code> realization hints where needed.</li>
</ul>

<p>
Realization packages define how a host may realize a widget class. They do not redefine the class law itself.
</p>

<h2 id="widget-bundle-package">12. Widget Bundle Package</h2>

<p>
A widget bundle package is a convenience form that contains both class and realization content.
</p>

<p>
A bundle package MAY be useful for examples, reference implementations, or tightly-scoped standard widget families. However, bundle packages SHOULD preserve the internal distinction between class content and realization content.
</p>

<h2 id="versioning-posture">13. Versioning Posture</h2>

<p>
The <code>wfrog_version</code> field identifies the version of the <code>.wfrog</code> package format being used.
</p>

<p>
The package version inside <code>package.version</code> identifies the version of the package contents themselves.
</p>

<p>
These two version lines are related but distinct:
</p>

<ul>
  <li><code>wfrog_version</code> = format version,</li>
  <li><code>package.version</code> = package content version.</li>
</ul>

<p>
A future FROG versioning document may govern the exact compatibility and evolution policy in more detail.
</p>

<h2 id="portability-and-conformance">14. Portability and Conformance</h2>

<p>
A conforming runtime is not required to support every realization package or every host-private hint.
</p>

<p>
However, a conforming runtime that claims support for a widget class package MUST interpret the normative class-level content consistently enough to preserve:
</p>

<ul>
  <li>class identity,</li>
  <li>legal member exposure,</li>
  <li>addressing legality,</li>
  <li>value participation,</li>
  <li>property read and write semantics,</li>
  <li>method invocation semantics,</li>
  <li>event identity and event payload shape.</li>
</ul>

<p>
Host-private realization conveniences do not become normative widget law merely because one runtime uses them.
</p>

<h2 id="example-minimal-class-package">15. Example: Minimal Class Package</h2>

<pre><code>{
  "wfrog_version": "0.1",
  "kind": "widget_class_package",
  "package": {
    "name": "frog.ui.standard.numeric",
    "version": "0.1.0",
    "namespace": "frog.ui.standard"
  },
  "classes": [
    {
      "class_id": "frog.ui.standard.numeric_control",
      "display_name": "Numeric Control",
      "roles": ["control"],
      "value_model": {
        "kind": "scalar",
        "value_property": "value",
        "type_constraints": ["i32", "u32", "i64", "f32", "f64"]
      },
      "properties": [
        {
          "name": "value",
          "type": "f64",
          "readable": true,
          "writable": true
        },
        {
          "name": "caption",
          "type": "string",
          "readable": true,
          "writable": true
        }
      ],
      "methods": [
        {
          "name": "focus",
          "inputs": [],
          "outputs": []
        }
      ],
      "events": [
        {
          "name": "value_changed",
          "payload": {
            "type": "record",
            "fields": {
              "value": "f64"
            }
          }
        }
      ],
      "parts": [
        {
          "name": "label",
          "kind": "visual_part"
        }
      ]
    }
  ]
}</code></pre>

<h2 id="example-minimal-realization-package">16. Example: Minimal Realization Package</h2>

<pre><code>{
  "wfrog_version": "0.1",
  "kind": "widget_realization_package",
  "package": {
    "name": "frog.ui.theme.default",
    "version": "0.1.0",
    "namespace": "frog.ui.theme.default"
  },
  "targets": [
    {
      "class_id": "frog.ui.standard.numeric_control",
      "host_family": "generic_svg_host",
      "visual": {
        "mode": "svg_template",
        "svg_asset": "./assets/numeric_control.svg",
        "anchors": {
          "root": "root",
          "label": "label_anchor"
        }
      }
    }
  ]
}</code></pre>

<h2 id="summary">17. Summary</h2>

<p>
FROG keeps <code>.frog</code> as the canonical program source and introduces <code>.wfrog</code> as a distinct widget-oriented artifact family.
</p>

<p>
That family is explicitly typed, layered, and bounded:
</p>

<ul>
  <li>class law is not the same thing as realization,</li>
  <li>realization is not the same thing as host-private convenience,</li>
  <li>visual assets are not semantic truth,</li>
  <li>and runtime interpretation does not redefine language ownership.</li>
</ul>

<p>
This is the baseline required for a portable, inspectable, and multi-runtime widget object system.
</p>
