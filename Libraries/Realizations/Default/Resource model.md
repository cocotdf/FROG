<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization Resource Model</h1>

<p align="center">
  <strong>Normative resource model for the official <code>Default</code> widget realization family</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#resource-purpose">2. Resource Purpose</a></li>
  <li><a href="#relationship-with-realization-records">3. Relationship with Realization Records</a></li>
  <li><a href="#resource-kinds">4. Resource Kinds</a></li>
  <li><a href="#resource-identifiers">5. Resource Identifiers</a></li>
  <li><a href="#resource-record-shape">6. Resource Record Shape</a></li>
  <li><a href="#path-posture">7. Path Posture</a></li>
  <li><a href="#class-part-and-region-scoping">8. Class, Part, and Region Scoping</a></li>
  <li><a href="#state-scoping">9. State Scoping</a></li>
  <li><a href="#anchor-and-text-region-resources">10. Anchor and Text-Region Resources</a></li>
  <li><a href="#resource-examples">11. Resource Examples</a></li>
  <li><a href="#validation-posture">12. Validation Posture</a></li>
  <li><a href="#summary">13. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the resource model used by the official <code>Default</code> realization family.
</p>

<p>
The resource model provides the machine-readable posture for realization resources such as SVG assets, anchor maps, text-region maps, layer maps, and related support artifacts used by realization records.
</p>

<p>
Its purpose is to define what realization resources are, how they are identified, how they are scoped, and how they remain subordinate to the realization and class layers above them.
</p>

<p>
The central architectural principle is simple:
resources support embodiment, placement, composition, and styling,
but they do not become the semantic owner of public widget meaning.
</p>

<hr/>

<h2 id="resource-purpose">2. Resource Purpose</h2>

<p>
A realization resource exists to support visual embodiment and host-facing realization.
</p>

<p>
A resource does not own:
</p>

<ul>
  <li>widget class identity,</li>
  <li>public property legality,</li>
  <li>public method legality,</li>
  <li>public event legality,</li>
  <li>public part legality,</li>
  <li>bounded behavior law,</li>
  <li>semantic ownership of dynamic user-facing widget data.</li>
</ul>

<p>
A realization resource may help define:
</p>

<ul>
  <li>which visual geometry is available,</li>
  <li>which layer structure is available,</li>
  <li>which anchor or placement surfaces are available,</li>
  <li>which state-specific asset variants are available,</li>
  <li>which styling tokens or host-facing realization hints are available.</li>
</ul>

<p>
Resources remain downstream from widget class law and downstream from realization doctrine.
They support embodiment.
They do not become semantic truth.
</p>

<hr/>

<h2 id="relationship-with-realization-records">3. Relationship with Realization Records</h2>

<p>
The resource model is subordinate to realization records.
</p>

<p>
In the default family, the preferred publication split is:
</p>

<ul>
  <li><code>part_bindings</code> define stable structural correspondence between widget parts and realization surfaces,</li>
  <li><code>state_maps</code> define state-sensitive visual embodiment,</li>
  <li><code>resources</code> define the concrete machine-readable inventory of available realization artifacts,</li>
  <li><code>anchors</code> and <code>text_regions</code> define inspectable placement surfaces when dynamic host rendering is required.</li>
</ul>

<p>
Accordingly, a resource record does not by itself decide how a part is realized.
That decision emerges from the combination of:
</p>

<ul>
  <li>the realization record,</li>
  <li>the relevant <code>part_bindings</code>,</li>
  <li>the relevant <code>state_maps</code>,</li>
  <li>the resource inventory,</li>
  <li>the published anchors or text regions when applicable.</li>
</ul>

<hr/>

<h2 id="resource-kinds">4. Resource Kinds</h2>

<p>
The default family MAY use the following resource kinds:
</p>

<ul>
  <li><code>svg</code></li>
  <li><code>vector_template</code></li>
  <li><code>anchor_map</code></li>
  <li><code>text_region_map</code></li>
  <li><code>layer_map</code></li>
  <li><code>style_token_map</code></li>
</ul>

<p>
The smallest useful baseline is usually <code>svg</code> plus, when dynamic placement is needed, either <code>anchor_map</code> or <code>text_region_map</code>.
The other resource kinds are optional support artifacts.
</p>

<p>
A rough interpretation posture is:
</p>

<ul>
  <li><code>svg</code> — visual geometry, skin, decorative content, and state-specific embodiment,</li>
  <li><code>vector_template</code> — parameterizable vector realization resource when the family supports template-driven generation,</li>
  <li><code>anchor_map</code> — named anchors or placement points used to bind public parts to realization surfaces,</li>
  <li><code>text_region_map</code> — named text-bearing regions used for host-rendered dynamic text placement,</li>
  <li><code>layer_map</code> — named layer correspondence or composition metadata for visual resources,</li>
  <li><code>style_token_map</code> — realization-side token mapping for style defaults or theme buckets.</li>
</ul>

<p>
These resource kinds describe realization support.
They do not authorize a resource file to invent new public widget semantics.
</p>

<hr/>

<h2 id="resource-identifiers">5. Resource Identifiers</h2>

<p>
A resource SHOULD have a stable identifier.
</p>

<p>
A recommended identifier posture is:
</p>

<pre><code>&lt;widget-surface&gt;.&lt;part-or-region&gt;.&lt;state-when-applicable&gt;.&lt;kind&gt;</code></pre>

<p>
Examples:
</p>

<ul>
  <li><code>button.face.pressed.svg</code></li>
  <li><code>button.frame.focused.svg</code></li>
  <li><code>button.label.anchor_map</code></li>
  <li><code>button.label.text_region_map</code></li>
  <li><code>numeric_control.increment_button.pressed.svg</code></li>
  <li><code>boolean_control.state_face.normal_true.svg</code></li>
</ul>

<p>
The identifier should remain stable even if the physical file path changes.
This helps preserve durable package references and stable realization bindings.
</p>

<p>
Resource identifiers SHOULD align naturally with the published asset naming posture, but they do not need to mirror the filesystem path character-for-character.
</p>

<hr/>

<h2 id="resource-record-shape">6. Resource Record Shape</h2>

<p>
A resource record SHOULD contain:
</p>

<ul>
  <li><code>id</code>,</li>
  <li><code>kind</code>,</li>
  <li><code>path</code>,</li>
  <li><code>target_class</code> when applicable,</li>
  <li><code>target_part</code> when applicable,</li>
  <li><code>target_state</code> when applicable.</li>
</ul>

<p>
A resource record MAY also contain:
</p>

<ul>
  <li><code>target_region</code> when the resource is region-oriented rather than part-oriented,</li>
  <li><code>target_layer</code> when the resource is layer-oriented,</li>
  <li><code>format</code> when further format disambiguation is useful,</li>
  <li><code>role</code> when the resource has a specialized realization-side purpose such as <code>text_anchor</code>, <code>text_region</code>, or <code>fallback_region</code>.</li>
</ul>

<p>
Conceptually:
</p>

<pre><code>{
  "id": "button.face.pressed.svg",
  "kind": "svg",
  "path": "./assets/button/face/pressed.svg",
  "target_class": "frog.widgets.button",
  "target_part": "face",
  "target_state": "pressed"
}</code></pre>

<p>
Another example:
</p>

<pre><code>{
  "id": "button.label.anchor_map",
  "kind": "anchor_map",
  "path": "./assets/button/anchors/label.json",
  "target_class": "frog.widgets.button",
  "target_part": "label",
  "role": "text_anchor"
}</code></pre>

<p>
A resource record should remain descriptive of the resource itself.
It should not duplicate the full meaning of the realization record that consumes it.
</p>

<hr/>

<h2 id="path-posture">7. Path Posture</h2>

<p>
Paths SHOULD remain explicit and relative to the publishing package root where practical.
</p>

<p>
The package SHOULD NOT depend on implicit filename guessing alone to resolve state-specific resources.
</p>

<p>
Likewise, the package SHOULD NOT depend on path naming alone to determine whether a resource is:
</p>

<ul>
  <li>state-sensitive,</li>
  <li>part-sensitive,</li>
  <li>region-sensitive,</li>
  <li>anchor-oriented,</li>
  <li>text-region-oriented,</li>
  <li>shared across multiple realizations.</li>
</ul>

<p>
Those relationships should remain inspectable through the resource record and the referencing realization structures.
</p>

<p>
Filesystem clarity is strongly preferred, but filesystem layout is not the sole carrier of realization meaning.
</p>

<hr/>

<h2 id="class-part-and-region-scoping">8. Class, Part, and Region Scoping</h2>

<p>
Resources SHOULD be scoped to the narrowest meaningful realization surface:
</p>

<ul>
  <li>widget-level resource when the whole widget surface is state-specific,</li>
  <li>part-level resource when a specific realized part is state-specific,</li>
  <li>region-level resource when a public or realized surface is expressed through a named placement region,</li>
  <li>family-level shared resource only when multiple realizations intentionally reuse it.</li>
</ul>

<p>
Part-oriented scoping is generally preferred when the realization family exposes stable parts and binds those parts independently.
Region-oriented scoping is generally preferred when a part is consumed through a placement surface rather than a distinct visual layer.
</p>

<p>
For example:
</p>

<ul>
  <li>a button <code>face</code> pressed asset is naturally part-scoped,</li>
  <li>a button <code>label</code> anchor map is naturally part-scoped, because it binds the <code>label</code> part through a placement surface,</li>
  <li>a string indicator value region may be region-scoped when the realization publishes a distinct value region,</li>
  <li>a shared focus-ring style token map may be family-scoped.</li>
</ul>

<p>
This distinction is important because a placement resource may target a semantic public surface without becoming the semantic owner of that surface.
</p>

<hr/>

<h2 id="state-scoping">9. State Scoping</h2>

<p>
State scoping SHOULD be explicit in the resource record or in the state map that references the resource.
</p>

<p>
The default family avoids making state inference depend only on filenames.
</p>

<p>
State scoping is most natural for resources such as:
</p>

<ul>
  <li>button face assets,</li>
  <li>button frame variants,</li>
  <li>boolean state-face assets,</li>
  <li>focused or disabled frame variants,</li>
  <li>pressed increment or decrement button assets.</li>
</ul>

<p>
State scoping is usually less important for:
</p>

<ul>
  <li>anchor maps,</li>
  <li>text-region maps,</li>
  <li>style token maps that apply across multiple states.</li>
</ul>

<p>
However, the model MAY still permit state-sensitive anchor or region resources when a realization intentionally changes text placement, clipping, or layout posture across states.
</p>

<p>
When that happens, the preferred posture remains explicit publication through the realization record rather than hidden filename conventions alone.
</p>

<hr/>

<h2 id="anchor-and-text-region-resources">10. Anchor and Text-Region Resources</h2>

<h3>10.1 Purpose</h3>

<p>
Anchor and text-region resources exist to make realization-side placement explicit and inspectable when a host dynamically renders a public part rather than consuming a single asset that already contains its final user-visible content.
</p>

<p>
This is especially important for dynamic text-bearing parts such as:
</p>

<ul>
  <li><code>button.label</code>,</li>
  <li>numeric display text regions,</li>
  <li>string display regions,</li>
  <li>other standardized parts whose final visible content is supplied at runtime.</li>
</ul>

<h3>10.2 Anchor maps</h3>

<p>
An <code>anchor_map</code> resource SHOULD allow a realization family to publish named anchors or placement surfaces that a host can target.
</p>

<p>
Typical anchor-oriented metadata may include:
</p>

<ul>
  <li>anchor identifier,</li>
  <li>anchor kind,</li>
  <li>alignment posture,</li>
  <li>reference box or bounds,</li>
  <li>padding or insets,</li>
  <li>clipping posture when needed.</li>
</ul>

<p>
Anchor maps are generally appropriate when the realization wants to publish a point, boxed anchor, or alignment-focused placement surface.
</p>

<h3>10.3 Text-region maps</h3>

<p>
A <code>text_region_map</code> resource SHOULD allow a realization family to publish named text-bearing regions with enough metadata for a host to render text consistently.
</p>

<p>
Typical text-region metadata may include:
</p>

<ul>
  <li>region identifier,</li>
  <li>bounding box or region path,</li>
  <li>horizontal alignment,</li>
  <li>vertical alignment,</li>
  <li>clipping rule,</li>
  <li>padding or inset metadata.</li>
</ul>

<p>
Text-region maps are generally appropriate when the realization wants to publish a bounded text surface rather than a point-like or anchor-like placement target.
</p>

<h3>10.4 Relationship with bindings</h3>

<p>
Anchor and text-region resources are usually consumed through realization-side <code>part_bindings</code>.
</p>

<p>
Typical posture:
</p>

<ul>
  <li>the resource record publishes the underlying placement-support file,</li>
  <li>an <code>anchors</code> or <code>text_regions</code> entry publishes an inspectable placement surface identifier,</li>
  <li>the realization record binds the target part to that placement surface,</li>
  <li>the host renders live content into that surface.</li>
</ul>

<p>
This keeps the placement resource, the placement surface, and the part binding distinct and inspectable.
</p>

<h3>10.5 Button-specific posture</h3>

<p>
For <code>frog.widgets.button</code>, the preferred default posture is:
</p>

<ul>
  <li><code>face</code> uses state-sensitive visual resources such as <code>svg</code>,</li>
  <li><code>label</code> uses an <code>anchor_map</code> or <code>text_region_map</code>,</li>
  <li>the host dynamically renders the semantic <code>label.text</code> into that published placement surface.</li>
</ul>

<p>
That distinction helps preserve the architectural split between:
</p>

<ul>
  <li>semantic text owned by widget class law,</li>
  <li>placement owned by realization publication,</li>
  <li>decorative geometry owned by visual assets.</li>
</ul>

<h3>10.6 Asset limitation rule</h3>

<p>
A resource file MAY contain placeholder text, decorative preview text, or design-time guide content.
However, a conforming realization family must not require that asset-baked text become the only path by which the public semantic text is shown.
</p>

<hr/>

<h2 id="resource-examples">11. Resource Examples</h2>

<pre><code>{
  "resources": [
    {
      "id": "button.face.normal.svg",
      "kind": "svg",
      "path": "./assets/button/face/normal.svg",
      "target_class": "frog.widgets.button",
      "target_part": "face",
      "target_state": "normal"
    },
    {
      "id": "button.face.pressed.svg",
      "kind": "svg",
      "path": "./assets/button/face/pressed.svg",
      "target_class": "frog.widgets.button",
      "target_part": "face",
      "target_state": "pressed"
    },
    {
      "id": "button.frame.focused.svg",
      "kind": "svg",
      "path": "./assets/button/frame/focused.svg",
      "target_class": "frog.widgets.button",
      "target_part": "frame",
      "target_state": "focused"
    },
    {
      "id": "button.label.anchor_map",
      "kind": "anchor_map",
      "path": "./assets/button/anchors/label.json",
      "target_class": "frog.widgets.button",
      "target_part": "label",
      "role": "text_anchor"
    },
    {
      "id": "numeric_control.increment_button.pressed.svg",
      "kind": "svg",
      "path": "./assets/numeric_control/increment_button/pressed.svg",
      "target_class": "frog.widgets.numeric_control",
      "target_part": "increment_button",
      "target_state": "pressed"
    },
    {
      "id": "string_indicator.value.text_region_map",
      "kind": "text_region_map",
      "path": "./assets/string_indicator/text_regions/value.json",
      "target_class": "frog.widgets.string_indicator",
      "target_region": "value",
      "role": "text_region"
    }
  ]
}</code></pre>

<hr/>

<h2 id="validation-posture">12. Validation Posture</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>duplicate resource identifiers,</li>
  <li>unknown resource kinds,</li>
  <li>missing resource paths,</li>
  <li>target part names not declared by the target class or not justified by the relevant realization publication,</li>
  <li>target states not declared by the associated realization record,</li>
  <li>anchor or text-region resources that are referenced but not published,</li>
  <li>resources whose declared role contradicts their declared kind,</li>
  <li>resource usage that implies asset-baked semantic text as the only embodiment path for a dynamic public text-bearing part.</li>
</ul>

<p>
Validators MAY also diagnose:
</p>

<ul>
  <li>needlessly coarse widget-level scoping when a stable part-level or region-level scope is available,</li>
  <li>ambiguous overlap between multiple anchor or text-region resources targeting the same part without explicit precedence posture,</li>
  <li>resource records whose scoping does not match the published asset naming posture closely enough to remain inspectable.</li>
</ul>

<hr/>

<h2 id="summary">13. Summary</h2>

<p>
The default realization resource model defines how official realization resources are identified, scoped, and published.
</p>

<p>
It covers visual assets, anchors, text regions, layer maps, and related support artifacts while keeping those resources explicit, structured, and subordinate to the realization and class layers above them.
</p>

<p>
Its preferred architecture is:
</p>

<ul>
  <li>visual resources for visual embodiment,</li>
  <li>state maps for state-sensitive realization posture,</li>
  <li>placement resources for dynamic public surfaces rendered by the host,</li>
  <li>clear separation between resource inventory, part bindings, and semantic widget meaning.</li>
</ul>
