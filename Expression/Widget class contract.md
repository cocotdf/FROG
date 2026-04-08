<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Widget Class Contract</h1>

<p align="center">
  <strong>Normative class-level contract for widget classes, properties, methods, events, parts, and object addressing</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-document-exists">2. Why This Document Exists</a></li>
  <li><a href="#scope">3. Scope</a></li>
  <li><a href="#ownership-boundary">4. Ownership Boundary</a></li>
  <li><a href="#class-contract-purpose">5. Class Contract Purpose</a></li>
  <li><a href="#required-class-surfaces">6. Required Class Surfaces</a></li>
  <li><a href="#primary-value-model">7. Primary Value Model</a></li>
  <li><a href="#property-model">8. Property Model</a></li>
  <li><a href="#method-model">9. Method Model</a></li>
  <li><a href="#event-model">10. Event Model</a></li>
  <li><a href="#part-model">11. Part Model</a></li>
  <li><a href="#object-addressing">12. Object Addressing</a></li>
  <li><a href="#mutability-and-persistence">13. Mutability and Persistence</a></li>
  <li><a href="#design-time-vs-runtime">14. Design-Time vs Runtime</a></li>
  <li><a href="#conformance">15. Conformance</a></li>
  <li><a href="#example-class-outline">16. Example Class Outline</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
A widget class contract defines the normative class-level law of a widget family in FROG.
It specifies what a widget class is allowed to expose and how runtimes may interpret that class.
</p>

<p>
A widget class contract exists above any one runtime implementation and above any one host toolkit.
It is the stable class-level semantic surface that allows multiple runtimes to interpret the same widget class family.
</p>

<h2 id="why-this-document-exists">2. Why This Document Exists</h2>

<p>
FROG needs a widget object system that is:
</p>

<ul>
  <li>portable across runtimes,</li>
  <li>extensible beyond a tiny fixed widget inventory,</li>
  <li>inspectable and auditable,</li>
  <li>bounded by published rules rather than runtime-private conventions.</li>
</ul>

<p>
The widget class contract is the layer that prevents widget law from being hidden inside one runtime or one rendering toolkit.
</p>

<h2 id="scope">3. Scope</h2>

<p>
This document defines the normative class-level contract for:
</p>

<ul>
  <li>properties,</li>
  <li>methods,</li>
  <li>events,</li>
  <li>parts,</li>
  <li>primary value surfaces,</li>
  <li>object addressing rules,</li>
  <li>mutability and persistence boundaries.</li>
</ul>

<h2 id="ownership-boundary">4. Ownership Boundary</h2>

<ul>
  <li><strong>This contract owns:</strong> class-level widget law.</li>
  <li><strong><code>.wfrog</code> owns:</strong> machine-readable packaging of class and front-panel content.</li>
  <li><strong><code>.frog</code> owns:</strong> canonical program source and explicit graph interaction.</li>
  <li><strong>Runtime owns:</strong> interpretation of the published class law.</li>
  <li><strong>Host owns:</strong> concrete realization.</li>
</ul>

<h2 id="class-contract-purpose">5. Class Contract Purpose</h2>

<p>
A widget class contract answers the following questions:
</p>

<ul>
  <li>What is this class called?</li>
  <li>What is its primary value surface, if any?</li>
  <li>Which properties are legal?</li>
  <li>Which methods are legal?</li>
  <li>Which events are legal?</li>
  <li>Which parts are stable and addressable?</li>
  <li>Which members are readable, writable, persistent, or runtime-only?</li>
</ul>

<h2 id="required-class-surfaces">6. Required Class Surfaces</h2>

<p>
A widget class contract MUST define:
</p>

<ul>
  <li>a stable <code>class_id</code>,</li>
  <li>a category,</li>
  <li>a primary value posture,</li>
  <li>a property set,</li>
  <li>a method set,</li>
  <li>an event set,</li>
  <li>a part hierarchy or part inventory,</li>
  <li>conformance expectations.</li>
</ul>

<h2 id="primary-value-model">7. Primary Value Model</h2>

<p>
A widget class MAY define a primary value surface.
That value surface is the natural-value participation path used by <code>widget_value</code>.
</p>

<p>
If a class defines a primary value surface, the contract MUST state:
</p>

<ul>
  <li>the value type,</li>
  <li>read/write posture,</li>
  <li>whether user interaction may change it,</li>
  <li>whether runtime interaction may change it,</li>
  <li>whether it is persistent or ephemeral.</li>
</ul>

<h2 id="property-model">8. Property Model</h2>

<p>
Each property declaration SHOULD include:
</p>

<ul>
  <li><code>name</code></li>
  <li><code>type</code></li>
  <li><code>access</code> — <code>read_only</code>, <code>write_only</code>, or <code>read_write</code></li>
  <li><code>mutability</code></li>
  <li><code>persistent</code></li>
  <li><code>default</code></li>
  <li><code>nullable</code></li>
  <li><code>constraints</code></li>
  <li><code>applies_to_part</code> when applicable</li>
</ul>

<p>
A property is legal only if published by the class contract or by an allowed extension model.
</p>

<h2 id="method-model">9. Method Model</h2>

<p>
Each method declaration SHOULD include:
</p>

<ul>
  <li><code>name</code></li>
  <li>typed parameters</li>
  <li>return type</li>
  <li>availability boundary</li>
  <li>declared side-effect posture</li>
</ul>

<p>
A runtime MUST NOT expose undeclared methods as portable class law.
</p>

<h2 id="event-model">10. Event Model</h2>

<p>
Each event declaration SHOULD include:
</p>

<ul>
  <li><code>name</code></li>
  <li>payload type</li>
  <li>origin surface</li>
  <li>delivery posture</li>
</ul>

<p>
Events MAY be emitted by the widget root or by a declared part.
Event names and payload shapes form part of the portable contract.
</p>

<h2 id="part-model">11. Part Model</h2>

<p>
A part is a stable addressable sub-surface of a widget object.
Parts allow a widget to expose internal structure without collapsing into one opaque box.
</p>

<p>
A part declaration SHOULD include:
</p>

<ul>
  <li><code>part_id</code></li>
  <li><code>kind</code></li>
  <li>optional parent part</li>
  <li>optional local properties</li>
  <li>optional local events</li>
</ul>

<h2 id="object-addressing">12. Object Addressing</h2>

<p>
FROG object-style widget access requires stable object addressing.
The contract therefore supports addressing of:
</p>

<ul>
  <li>the widget root object,</li>
  <li>named properties,</li>
  <li>named methods,</li>
  <li>named parts,</li>
  <li>part-local properties where allowed.</li>
</ul>

<p>
Portable addressing MUST be string-stable and contract-based.
</p>

<h2 id="mutability-and-persistence">13. Mutability and Persistence</h2>

<p>
The contract MUST distinguish:
</p>

<ul>
  <li>construction-only values,</li>
  <li>design-time mutable values,</li>
  <li>runtime mutable values,</li>
  <li>persistent values,</li>
  <li>ephemeral values.</li>
</ul>

<p>
This distinction is required so that runtimes and IDEs do not guess property law differently.
</p>

<h2 id="design-time-vs-runtime">14. Design-Time vs Runtime</h2>

<p>
A widget class contract MAY distinguish:
</p>

<ul>
  <li>design-time surface,</li>
  <li>runtime surface,</li>
  <li>shared surface.</li>
</ul>

<p>
For example, a label text may be design-time and runtime mutable, while one geometry property may be
design-time only.
</p>

<h2 id="conformance">15. Conformance</h2>

<p>
A runtime is conforming for a widget class only if it preserves the class contract for all portable members
it claims to implement.
</p>

<p>
A host-specific extension is allowed only if:
</p>

<ul>
  <li>it is clearly marked as non-portable,</li>
  <li>it does not redefine published class law,</li>
  <li>it does not change primary value semantics.</li>
</ul>

<h2 id="example-class-outline">16. Example Class Outline</h2>

<pre><code>{
  "class_id": "frog.widgets.numeric_indicator",
  "category": "indicator",
  "primary_value": {
    "type": "float64",
    "access": "read_write"
  },
  "properties": [
    { "name": "value", "type": "float64", "access": "read_write" },
    { "name": "format", "type": "string", "access": "read_write" },
    { "name": "foreground_color", "type": "frog.color.rgba8", "access": "read_write" }
  ],
  "methods": [
    { "name": "reset_to_default_style", "parameters": [], "returns": { "type": "void" } }
  ],
  "events": [
    { "name": "value_rendered", "payload": { "type": "string" } }
  ],
  "parts": [
    { "part_id": "root", "kind": "container" },
    { "part_id": "value_text", "kind": "text" }
  ]
}</code></pre>
