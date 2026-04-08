<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Widget Class Contract</h1>

<p align="center">
  <strong>Normative class-level contract for widget classes, members, parts, events, and object-surface legality</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#scope">2. Scope</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#why-this-document-exists">4. Why This Document Exists</a></li>
  <li><a href="#ownership-boundary">5. Ownership Boundary</a></li>
  <li><a href="#core-principles">6. Core Principles</a></li>
  <li><a href="#class-contract-model">7. Class Contract Model</a></li>
  <li><a href="#extensibility-posture">8. Extensibility Posture</a></li>
  <li><a href="#class-descriptor">9. Class Descriptor</a></li>
  <li><a href="#member-model">10. Member Model</a></li>
  <li><a href="#property-contract">11. Property Contract</a></li>
  <li><a href="#method-contract">12. Method Contract</a></li>
  <li><a href="#event-contract">13. Event Contract</a></li>
  <li><a href="#part-contract">14. Part Contract</a></li>
  <li><a href="#member-addressing">15. Member Addressing</a></li>
  <li><a href="#value-model">16. Value Model</a></li>
  <li><a href="#design-time-and-runtime-boundaries">17. Design-Time and Runtime Boundaries</a></li>
  <li><a href="#capability-and-profile-gating">18. Capability and Profile Gating</a></li>
  <li><a href="#host-requirements">19. Host Requirements</a></li>
  <li><a href="#source-shape-and-serialization-posture">20. Source Shape and Serialization Posture</a></li>
  <li><a href="#validation-rules">21. Validation Rules</a></li>
  <li><a href="#diagnostics">22. Diagnostics</a></li>
  <li><a href="#conformance-implications">23. Conformance Implications</a></li>
  <li><a href="#non-goals">24. Non-Goals</a></li>
  <li><a href="#minimal-v01-posture">25. Minimal v0.1 Posture</a></li>
  <li><a href="#illustrative-example">26. Illustrative Example</a></li>
  <li><a href="#summary">27. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the normative class-level contract model for FROG widgets.
</p>

<p>
A widget instance in canonical source is not merely a placed front-panel element. It is an instance of a widget class whose object surface must be describable in a stable, inspectable, implementation-independent way.
</p>

<p>
That class-level surface includes:
</p>

<ul>
  <li>class identity,</li>
  <li>role compatibility,</li>
  <li>value behavior where applicable,</li>
  <li>properties,</li>
  <li>methods,</li>
  <li>events,</li>
  <li>parts,</li>
  <li>member addressing legality,</li>
  <li>design-time and runtime access boundaries,</li>
  <li>host realization requirements where relevant.</li>
</ul>

<p>
The purpose of this document is to ensure that widget classes are explicit enough that:
</p>

<ul>
  <li>a validator can determine whether a widget instance or member access is legal,</li>
  <li>an IDE can expose coherent property and method authoring surfaces,</li>
  <li>a runtime can interpret widget object surfaces without becoming the hidden source of widget law,</li>
  <li>a host can realize widgets without redefining their semantics,</li>
  <li>independent implementations can converge on the same class-level interpretation.</li>
</ul>

<p>
This document defines the class-contract model itself. It does not claim that every possible widget family is already standardized in v0.1.
</p>

<hr/>

<h2 id="scope">2. Scope</h2>

<p>
This document standardizes the normative class-side contract shape of a widget class.
</p>

<p>
It defines:
</p>

<ul>
  <li>how a widget class is described,</li>
  <li>how members are categorized and declared,</li>
  <li>how parts participate in ownership and addressing,</li>
  <li>how property, method, and event surfaces are defined,</li>
  <li>how access legality is derived from the class contract,</li>
  <li>how design-time and runtime boundaries remain explicit,</li>
  <li>how profile and capability gates constrain class and member availability,</li>
  <li>how host realization requirements are declared.</li>
</ul>

<p>
This document does not define:
</p>

<ul>
  <li>pixel rendering behavior,</li>
  <li>theme systems,</li>
  <li>private runtime memory layouts,</li>
  <li>one mandatory GUI toolkit,</li>
  <li>one mandatory event loop implementation,</li>
  <li>diagram-side execution semantics of UI interaction primitives,</li>
  <li>runtime-private transport layouts for widget references,</li>
  <li>repository-wide version-governance policy.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<ul>
  <li><code>Front panel.md</code> defines source-level widget composition, containment, and placement.</li>
  <li><code>Widget.md</code> defines the source-level widget instance model.</li>
  <li><code>Widget interaction.md</code> defines diagram-side widget interaction through executable forms such as property read, property write, and method invoke.</li>
  <li><code>Widget package.md</code> defines the <code>.wfrog</code> package family used to serialize widget-oriented artifacts.</li>
  <li><code>Widget realization.md</code> defines host-side realization boundaries, visual bindings, and SVG integration.</li>
  <li><code>Widget behavior.md</code> defines declarative behavior, controlled expressions, and optional hooks where applicable.</li>
  <li><code>Type.md</code> defines the type-expression system used by ordinary typed members.</li>
  <li><code>Diagram.md</code> defines the authoritative executable graph.</li>
  <li><code>IR/</code> defines execution-facing derived representation.</li>
  <li><code>Profiles/</code> may define additional widget families, capability families, or realization requirements.</li>
  <li><code>IDE/</code> may define authoring and inspection behavior that consumes class contracts without owning them.</li>
</ul>

<p>
Accordingly:
</p>

<pre><code>Front panel           = widget instance placement and composition
Widget                = instance-side widget declaration
Widget class contract = class-side object-surface legality
Widget interaction    = executable access from the diagram
Widget package        = widget-oriented serialization family
Widget realization    = host-facing realization boundary
Widget behavior       = bounded widget behavior model
Diagram               = authoritative executable graph
IR                    = execution-facing derived representation
Profiles              = optional capability and target families
IDE                   = authoring and inspection consumption
</code></pre>

<p>
The following distinctions MUST remain explicit:
</p>

<pre><code>widget instance
    !=
widget class

widget class law
    !=
host realization

ordinary typed value
    !=
widget reference
    !=
UI sequencing token
</code></pre>

<hr/>

<h2 id="why-this-document-exists">4. Why This Document Exists</h2>

<p>
A durable widget system requires more than instance serialization.
</p>

<p>
If widget classes are underspecified, the following become implementation-private and therefore non-convergent:
</p>

<ul>
  <li>which properties exist,</li>
  <li>which properties are readable or writable,</li>
  <li>which methods exist,</li>
  <li>which events may be observed,</li>
  <li>which parts exist and how they are addressed,</li>
  <li>which accesses are legal at design time versus runtime,</li>
  <li>which classes or members are profile-gated or host-gated,</li>
  <li>how IDEs expose object-style authoring surfaces,</li>
  <li>how runtimes know what object surface they are required to interpret.</li>
</ul>

<p>
This document closes that gap by defining the normative class-side contract behind widget instances.
</p>

<p>
It also ensures that FROG can grow toward richer widget families over time without requiring each new family to reinvent the class-contract model.
</p>

<hr/>

<h2 id="ownership-boundary">5. Ownership Boundary</h2>

<p>
This document owns:
</p>

<ul>
  <li>widget class descriptors,</li>
  <li>member categories and member metadata,</li>
  <li>part-level contract structure,</li>
  <li>class-level event exposure,</li>
  <li>member addressing rules,</li>
  <li>design-time and runtime access boundaries,</li>
  <li>capability and profile gating of classes and members,</li>
  <li>host-requirement declarations for class realization.</li>
</ul>

<p>
This document does not own:
</p>

<ul>
  <li>widget instance placement on the panel,</li>
  <li>authoritative executable graph semantics,</li>
  <li>the execution semantics of <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, or <code>frog.ui.method_invoke</code>,</li>
  <li>runtime-private live object structures,</li>
  <li>host-private rendering internals,</li>
  <li>one required runtime strategy,</li>
  <li>one required IDE product behavior beyond the normative object surface implied by the contract.</li>
</ul>

<hr/>

<h2 id="core-principles">6. Core Principles</h2>

<ul>
  <li>A widget class MUST expose a stable contract independent from one private implementation.</li>
  <li>A widget instance MUST be interpretable against its declared widget class.</li>
  <li>Object-style member access MUST be validated against the widget class contract.</li>
  <li>Part access MUST remain explicit and MUST NOT rely on hidden runtime reflection.</li>
  <li>Widget class law MUST remain distinct from host realization.</li>
  <li>Design-time metadata and runtime-owned state MUST remain distinct.</li>
  <li>IDE convenience MUST NOT become hidden semantic law.</li>
  <li>Runtime enrichment MAY exist, but non-standard enrichment MUST NOT become required for canonical validity.</li>
  <li>Ordinary value typing, widget-reference identity, and UI sequencing MUST remain distinct categories.</li>
  <li>The class-contract model MUST be general enough to support richer future widget families than the minimal v0.1 subset.</li>
</ul>

<hr/>

<h2 id="class-contract-model">7. Class Contract Model</h2>

<p>
A widget class contract is the normative description of the object surface shared by all instances of a class.
</p>

<p>
Conceptually:
</p>

<pre><code>widget class contract
  ├── class identity
  ├── role compatibility
  ├── value model
  ├── properties
  ├── methods
  ├── events
  ├── parts
  ├── access boundaries
  ├── capability gates
  ├── host requirements
  └── revision metadata
</code></pre>

<p>
A widget instance then binds:
</p>

<ul>
  <li>an instance identifier,</li>
  <li>a class identity,</li>
  <li>a role-compatible instance declaration,</li>
  <li>instance-level values and settings where permitted,</li>
  <li>optional instance-side part data where permitted.</li>
</ul>

<p>
The class contract defines the legal object surface. It does not serialize one live runtime object, one transport handle, or one host-specific rendering strategy.
</p>

<hr/>

<h2 id="extensibility-posture">8. Extensibility Posture</h2>

<p>
The class-contract model defined by this document is intentionally general.
</p>

<p>
It is designed so that FROG can support over time:
</p>

<ul>
  <li>additional standardized widget classes,</li>
  <li>richer standardized widget families,</li>
  <li>profile-owned capability families,</li>
  <li>recognized external widget-class packages,</li>
  <li>multiple runtime families that interpret the same class-level law,</li>
  <li>multiple host families that realize the same class-level law differently but compatibly.</li>
</ul>

<p>
The key rule is:
</p>

<pre><code>general class-contract capability
    !=
full widget-family standardization in v0.1
</code></pre>

<p>
This document therefore defines the contract model that minimal v0.1 classes use and that richer future families may also use.
</p>

<hr/>

<h2 id="class-descriptor">9. Class Descriptor</h2>

<p>
Every widget class contract MUST provide a stable class descriptor.
</p>

<p>
A class descriptor MUST include:
</p>

<ul>
  <li><code>class_id</code>: canonical class identifier,</li>
  <li><code>contract_version</code>: class-contract revision identifier,</li>
  <li><code>roles</code>: allowed widget roles for the class,</li>
  <li><code>value_model</code>: whether and how the class participates in primary value flow,</li>
  <li><code>properties</code>,</li>
  <li><code>methods</code>,</li>
  <li><code>events</code>,</li>
  <li><code>parts</code>,</li>
  <li><code>profile_requirements</code> where applicable,</li>
  <li><code>host_requirements</code> where applicable.</li>
</ul>

<p>
A class descriptor MAY additionally include:
</p>

<ul>
  <li><code>display_name</code>,</li>
  <li><code>description</code>,</li>
  <li><code>categories</code>,</li>
  <li><code>deprecated_members</code>,</li>
  <li><code>compatibility_notes</code>.</li>
</ul>

<p>
A standardized widget class identifier MUST be stable across implementations for the same class.
</p>

<hr/>

<h2 id="member-model">10. Member Model</h2>

<p>
A widget member is a named object-surface element exposed by a widget class.
</p>

<p>
Standard member categories are:
</p>

<ul>
  <li><strong>property</strong>: readable and/or writable stateful member,</li>
  <li><strong>method</strong>: invocable operation,</li>
  <li><strong>event</strong>: observable occurrence emitted by the widget or one of its parts.</li>
</ul>

<p>
Each member descriptor MUST declare:
</p>

<ul>
  <li><code>name</code>,</li>
  <li><code>kind</code>,</li>
  <li><code>owner_scope</code>: widget or part,</li>
  <li><code>availability</code>: always, role-gated, profile-gated, host-gated, state-gated, or a combination thereof,</li>
  <li><code>design_time_access</code>,</li>
  <li><code>runtime_access</code>.</li>
</ul>

<p>
A member descriptor MUST NOT rely on runtime-only discovery for normative validity.
</p>

<p>
If a member uses ordinary values, its types MUST follow <code>Type.md</code>. Widget references and UI sequencing tokens MUST remain distinct from ordinary value types.
</p>

<hr/>

<h2 id="property-contract">11. Property Contract</h2>

<p>
A property descriptor defines a named readable and/or writable member exposed by a widget class or part.
</p>

<p>
A property descriptor MUST include:
</p>

<ul>
  <li><code>name</code>,</li>
  <li><code>type</code>,</li>
  <li><code>readable</code>,</li>
  <li><code>writable</code>,</li>
  <li><code>design_time_writable</code>,</li>
  <li><code>runtime_writable</code>,</li>
  <li><code>persistence</code>: source-owned, runtime-owned, or mixed-boundary,</li>
  <li><code>effects</code>: none, UI-side-effect, layout-side-effect, host-side-effect, or profile-defined,</li>
  <li><code>default_value_policy</code>.</li>
</ul>

<p>
A property descriptor MAY include:
</p>

<ul>
  <li><code>allowed_values</code>,</li>
  <li><code>range</code>,</li>
  <li><code>unit</code>,</li>
  <li><code>deprecated</code>,</li>
  <li><code>requires_ui_thread</code>,</li>
  <li><code>notes</code>.</li>
</ul>

<p>
A property MUST NOT be assumed readable or writable unless the contract declares it.
</p>

<p>
Examples:
</p>

<ul>
  <li><code>value</code> on a numeric control may be readable and writable at runtime,</li>
  <li><code>visible</code> may be readable and writable,</li>
  <li><code>bounds</code> may be design-time writable and runtime readable only,</li>
  <li><code>render_handle</code> may be runtime-owned and not source-owned,</li>
  <li><code>face_color</code> may be mixed-boundary if source declaration and runtime property writes are both allowed.</li>
</ul>

<hr/>

<h2 id="method-contract">12. Method Contract</h2>

<p>
A method descriptor defines a named invocable operation exposed by a widget class or part.
</p>

<p>
A method descriptor MUST include:
</p>

<ul>
  <li><code>name</code>,</li>
  <li><code>parameters</code>,</li>
  <li><code>results</code>,</li>
  <li><code>runtime_invocable</code>,</li>
  <li><code>design_time_invocable</code>,</li>
  <li><code>effects</code>,</li>
  <li><code>ordering_requirements</code> where explicit UI ordering matters,</li>
  <li><code>failure_surface</code>.</li>
</ul>

<p>
A method descriptor MAY include:
</p>

<ul>
  <li><code>idempotence</code>,</li>
  <li><code>requires_focus</code>,</li>
  <li><code>requires_ui_thread</code>,</li>
  <li><code>availability_state</code>,</li>
  <li><code>deprecated</code>.</li>
</ul>

<p>
A method MUST NOT be treated as a property-write shortcut.
</p>

<p>
Examples:
</p>

<ul>
  <li><code>reset_to_default()</code>,</li>
  <li><code>focus()</code>,</li>
  <li><code>scroll_into_view()</code>,</li>
  <li><code>append_series_point(value)</code> for a richer graph widget family.</li>
</ul>

<hr/>

<h2 id="event-contract">13. Event Contract</h2>

<p>
An event descriptor defines an observable occurrence emitted by a widget class or part.
</p>

<p>
An event descriptor MUST include:
</p>

<ul>
  <li><code>name</code>,</li>
  <li><code>payload</code>,</li>
  <li><code>emission_scope</code>: widget or part,</li>
  <li><code>emission_conditions</code>,</li>
  <li><code>ordering_notes</code> where observable ordering matters,</li>
  <li><code>availability</code>.</li>
</ul>

<p>
An event descriptor MAY define:
</p>

<ul>
  <li><code>bubbling</code> or containment propagation,</li>
  <li><code>coalescing</code> behavior,</li>
  <li><code>rate_limit</code> expectations,</li>
  <li><code>host_dependency</code>.</li>
</ul>

<p>
This document defines the event contract as part of the object surface. It does not define one mandatory event-runtime processing model.
</p>

<hr/>

<h2 id="part-contract">14. Part Contract</h2>

<p>
A part is a named object-owned sub-surface exposed by a widget class.
</p>

<p>
Examples of parts include:
</p>

<ul>
  <li>label,</li>
  <li>plot_area,</li>
  <li>cursor,</li>
  <li>legend,</li>
  <li>axis,</li>
  <li>increment_button,</li>
  <li>decrement_button.</li>
</ul>

<p>
A part descriptor MUST include:
</p>

<ul>
  <li><code>name</code>,</li>
  <li><code>part_class</code> or equivalent part-contract identity,</li>
  <li><code>cardinality</code>: single, indexed, keyed, or profile-defined,</li>
  <li><code>members</code>,</li>
  <li><code>presence_rule</code>: always present, optional, or configuration-dependent.</li>
</ul>

<p>
A part MUST NOT be treated as an independent top-level widget unless another specification explicitly defines such a transformation.
</p>

<p>
Part surfaces MUST remain attributable to the owning widget class contract rather than to hidden runtime reflection behavior.
</p>

<hr/>

<h2 id="member-addressing">15. Member Addressing</h2>

<p>
Object-style access MUST be addressable against the class contract.
</p>

<p>
The standard addressing levels are:
</p>

<ul>
  <li>widget member,</li>
  <li>named part member,</li>
  <li>indexed part member,</li>
  <li>keyed part member.</li>
</ul>

<p>
Conceptual addressing forms:
</p>

<pre><code>widget.member
widget.part.member
widget.part[index].member
widget.part[key].member
</code></pre>

<p>
A member access is valid only if:
</p>

<ul>
  <li>the widget class exists,</li>
  <li>the targeted part exists for that class,</li>
  <li>the targeted member exists on the targeted owner scope,</li>
  <li>the requested access mode is allowed,</li>
  <li>profile and host requirements are satisfied.</li>
</ul>

<p>
The class contract defines the legal target surface. The executable transport of widget references and any sequencing requirements remain owned elsewhere.
</p>

<hr/>

<h2 id="value-model">16. Value Model</h2>

<p>
For value-carrying widget classes, the relation between the main widget value and the object model MUST remain explicit.
</p>

<p>
A value-carrying widget class MUST define:
</p>

<ul>
  <li>whether a primary value exists,</li>
  <li>the value type,</li>
  <li>whether an object-style <code>value</code> property exists,</li>
  <li>whether the primary value is readable, writable, or both,</li>
  <li>how natural <code>widget_value</code> participation relates to object-style access.</li>
</ul>

<p>
The following distinction MUST remain explicit:
</p>

<pre><code>widget_value access
  !=
object-style property access to value
</code></pre>

<p>
They may be related, but they are not the same abstraction layer.
</p>

<p>
The following distinction MUST also remain explicit:
</p>

<pre><code>ordinary value typing
  !=
widget reference transport
  !=
UI sequencing transport
</code></pre>

<hr/>

<h2 id="design-time-and-runtime-boundaries">17. Design-Time and Runtime Boundaries</h2>

<p>
The class contract MUST distinguish at least the following ownership and access classes:
</p>

<ul>
  <li><strong>source-owned</strong>: serializable in canonical source,</li>
  <li><strong>runtime-owned</strong>: not authoritative in canonical source,</li>
  <li><strong>mixed-boundary</strong>: source-declared but runtime-updatable under explicit rules.</li>
</ul>

<p>
Examples:
</p>

<ul>
  <li>caption text may be source-owned,</li>
  <li>current focus state may be runtime-owned,</li>
  <li>visible may be mixed-boundary,</li>
  <li><code>face_color</code> may be mixed-boundary if the active class contract allows both source declaration and runtime writes.</li>
</ul>

<p>
This distinction is necessary so that canonical source validity does not depend on opaque runtime reflection data.
</p>

<p>
Runtime-owned members MAY still be readable or observable at runtime, but they MUST NOT become hidden mandatory serialized state for canonical source validity.
</p>

<hr/>

<h2 id="capability-and-profile-gating">18. Capability and Profile Gating</h2>

<p>
A widget class or member MAY be gated by a profile, a host capability, or both.
</p>

<p>
Examples:
</p>

<ul>
  <li>a basic boolean button may belong to the core widget vocabulary,</li>
  <li>a waveform graph may require a richer UI capability family,</li>
  <li>a drag-and-drop method may require host support not guaranteed by every runtime,</li>
  <li>a hardware-backed display widget may require a profile-specific host family.</li>
</ul>

<p>
Such gates MUST be explicit in the class contract.
</p>

<p>
A conforming validator MUST be able to diagnose when:
</p>

<ul>
  <li>the class itself is unavailable,</li>
  <li>a specific member is unavailable,</li>
  <li>a part exists only under a profile or capability not currently active.</li>
</ul>

<hr/>

<h2 id="host-requirements">19. Host Requirements</h2>

<p>
A widget class contract MAY impose host requirements for realization.
</p>

<p>
Examples:
</p>

<ul>
  <li>text input support,</li>
  <li>pointer interaction support,</li>
  <li>animation support,</li>
  <li>high-frequency repaint support,</li>
  <li>event dispatch support,</li>
  <li>accessibility metadata support.</li>
</ul>

<p>
A host requirement declaration MUST NOT redefine program semantics. It only constrains whether a host can realize the class or member as declared.
</p>

<p>
Host requirements MUST remain explicit rather than being inferred from one private renderer or runtime stack.
</p>

<hr/>

<h2 id="source-shape-and-serialization-posture">20. Source Shape and Serialization Posture</h2>

<p>
Canonical <code>.frog</code> source does not need to embed full widget class descriptors inline.
</p>

<p>
Widget class law may instead be serialized through widget-oriented packages such as <code>.wfrog</code> class packages.
</p>

<p>
However, when a widget class contract is serialized in a machine-readable form, its conceptual structure SHOULD follow a shape like the following:
</p>

<pre><code>{
  "class_id": "frog.ui.standard.numeric_control",
  "contract_version": "0.1",
  "roles": ["control"],
  "value_model": {
    "kind": "value_carrying",
    "value_type": "f64",
    "object_value_member": "value"
  },
  "properties": {
    "value": {
      "type": "f64",
      "readable": true,
      "writable": true,
      "design_time_writable": true,
      "runtime_writable": true,
      "persistence": "mixed_boundary",
      "effects": "none"
    },
    "visible": {
      "type": "bool",
      "readable": true,
      "writable": true,
      "design_time_writable": true,
      "runtime_writable": true,
      "persistence": "mixed_boundary",
      "effects": "ui_side_effect"
    },
    "face_color": {
      "type": "frog.ui.color",
      "readable": true,
      "writable": true,
      "design_time_writable": true,
      "runtime_writable": true,
      "persistence": "mixed_boundary",
      "effects": "ui_side_effect"
    }
  },
  "methods": {
    "reset_to_default": {
      "parameters": [],
      "results": [],
      "runtime_invocable": true,
      "design_time_invocable": false,
      "effects": "ui_side_effect"
    }
  },
  "events": {
    "value_changed": {
      "payload": {
        "old_value": "f64",
        "new_value": "f64"
      },
      "availability": "runtime"
    }
  },
  "parts": {
    "label": {
      "part_class": "frog.ui.standard.label_part",
      "cardinality": "single"
    }
  }
}
</code></pre>

<p>
This document defines the contract model itself. The exact long-term serialization home of standardized widget class contracts may be defined elsewhere in the specification corpus.
</p>

<hr/>

<h2 id="validation-rules">21. Validation Rules</h2>

<p>
Validators MUST enforce at least the following rules when class contracts are used normatively:
</p>

<ul>
  <li>a class identifier MUST be present,</li>
  <li>a class-contract version MUST be present,</li>
  <li>member names MUST be unique within their owner scope where ambiguity would arise,</li>
  <li>a property MUST declare a type,</li>
  <li>a method parameter list and result list MUST be structurally valid,</li>
  <li>a part contract MUST declare its cardinality,</li>
  <li>a member MUST NOT be simultaneously available and forbidden in the same access context,</li>
  <li>profile-gated or host-gated members MUST carry explicit gating metadata,</li>
  <li>a value-carrying class MUST define its value model coherently,</li>
  <li>a class MUST NOT require private runtime-only reflection metadata for canonical validity.</li>
</ul>

<p>
Validators SHOULD additionally preserve the following distinctions explicitly:
</p>

<ul>
  <li>ordinary typed value member versus widget-reference token,</li>
  <li>ordinary typed value member versus sequencing token,</li>
  <li>source-owned member versus runtime-owned member,</li>
  <li>design-time legality versus runtime legality,</li>
  <li>natural <code>widget_value</code> participation versus object-style property access.</li>
</ul>

<hr/>

<h2 id="diagnostics">22. Diagnostics</h2>

<p>
Validators SHOULD diagnose at least the following classes of errors:
</p>

<ul>
  <li>unknown widget class,</li>
  <li>unsupported class-contract version,</li>
  <li>unknown member,</li>
  <li>unknown part,</li>
  <li>invalid owner scope,</li>
  <li>invalid access mode,</li>
  <li>attempted write to read-only property,</li>
  <li>attempted read from write-only property,</li>
  <li>invocation of unavailable method,</li>
  <li>use of a profile-gated member outside the required profile,</li>
  <li>use of a host-gated member without the required host capability,</li>
  <li>ambiguous or invalid part addressing,</li>
  <li>illegal dependence on a runtime-only member for source validity,</li>
  <li>confusion between ordinary value typing and interaction-token categories.</li>
</ul>

<p>
Where an implementation distinguishes backend or runtime-family support from class-level legality, diagnostics SHOULD distinguish between:
</p>

<ul>
  <li>member access illegal by class contract,</li>
  <li>member access legal in principle but unavailable for the selected profile,</li>
  <li>member access legal in principle but unsupported by the selected backend or runtime family.</li>
</ul>

<hr/>

<h2 id="conformance-implications">23. Conformance Implications</h2>

<p>
When widget class contracts participate in conformance material, positive and negative cases SHOULD verify at least:
</p>

<ul>
  <li>known versus unknown classes,</li>
  <li>valid versus invalid property access,</li>
  <li>valid versus invalid method invocation,</li>
  <li>part-member addressing legality,</li>
  <li>profile-gated availability,</li>
  <li>host-gated availability,</li>
  <li>design-time versus runtime access constraints,</li>
  <li>value-model consistency for value-carrying widgets.</li>
</ul>

<p>
Conformance cases SHOULD also verify that implementations do not silently collapse:
</p>

<ul>
  <li>natural value access into generic object-style access,</li>
  <li>runtime-owned members into required serialized source members,</li>
  <li>host-specific richness into normative class-contract requirements.</li>
</ul>

<hr/>

<h2 id="non-goals">24. Non-Goals</h2>

<p>
This document is not:
</p>

<ul>
  <li>a complete GUI toolkit specification,</li>
  <li>a rendering engine specification,</li>
  <li>a theme or styling guide,</li>
  <li>a complete event-loop specification,</li>
  <li>a private runtime object-layout specification,</li>
  <li>a mandate that every implementation expose identical authoring ergonomics.</li>
</ul>

<hr/>

<h2 id="minimal-v01-posture">25. Minimal v0.1 Posture</h2>

<p>
For v0.1, the minimum required standardization posture is:
</p>

<ul>
  <li>a widget class MUST expose a stable identifier,</li>
  <li>roles MUST be explicit,</li>
  <li>value-carrying behavior MUST be explicit when applicable,</li>
  <li>properties and methods that participate in standardized object-style interaction MUST be explicitly contractable,</li>
  <li>part-member access MUST be explicit when supported,</li>
  <li>profile and host gates MUST be explicit where relevant.</li>
</ul>

<p>
For the first bounded executable corridor, the minimum useful class-side surface SHOULD also be strong enough that a validator and a reference consumer can agree on the legality of at least:
</p>

<ul>
  <li>one value-carrying numeric control class,</li>
  <li>one value-carrying numeric indicator class,</li>
  <li>their natural value path,</li>
  <li>and a minimal writable property surface such as <code>face_color</code>.</li>
</ul>

<p>
This posture defines the minimum coherent class-contract surface, not the maximum future richness of the FROG widget ecosystem.
</p>

<hr/>

<h2 id="illustrative-example">26. Illustrative Example</h2>

<p>
Conceptually:
</p>

<pre><code>Widget class: frog.ui.standard.numeric_control

  Widget-level properties
    - value        : f64      read/write
    - visible      : bool     read/write
    - enabled      : bool     read/write
    - face_color   : color    read/write

  Widget-level methods
    - reset_to_default()
    - focus()

  Widget-level events
    - value_changed(old_value, new_value)

  Parts
    - label
        properties:
          text : string read/write
    - increment_button
        methods:
          flash()
    - decrement_button
        methods:
          flash()
</code></pre>

<p>
An IDE may then expose:
</p>

<ul>
  <li><code>value</code>, <code>visible</code>, <code>enabled</code>, and <code>face_color</code> in a property-authoring surface,</li>
  <li><code>reset_to_default()</code> and <code>focus()</code> in a method-authoring surface,</li>
  <li><code>label.text</code> as a part-scoped property target,</li>
  <li>diagnostics when a forbidden access mode is attempted.</li>
</ul>

<p>
A bounded executable slice may then use:
</p>

<ul>
  <li>natural <code>widget_value</code> participation for the main numeric value,</li>
  <li><code>widget_reference</code> plus <code>frog.ui.property_write</code> for <code>face_color</code>,</li>
  <li>while keeping those two interaction surfaces distinct.</li>
</ul>

<hr/>

<h2 id="summary">27. Summary</h2>

<p>
The widget class contract is the normative class-side object surface that makes widget interaction explicit, inspectable, and implementation-independent.
</p>

<p>
It closes the gap between:
</p>

<ul>
  <li>instance-side front-panel declaration,</li>
  <li>diagram-side widget interaction primitives,</li>
  <li>IDE-side property and method exposure,</li>
  <li>runtime-side interpretation obligations,</li>
  <li>host-side realization constraints.</li>
</ul>

<p>
By keeping widget classes explicit, FROG can support rich widget-object interaction without turning one private IDE, runtime, or host stack into the hidden source of truth.
</p>

<p>
The document also keeps explicit the distinctions between:
</p>

<ul>
  <li>ordinary value typing,</li>
  <li>widget-reference transport,</li>
  <li>UI sequencing transport,</li>
  <li>source-owned members,</li>
  <li>runtime-owned members,</li>
  <li>class-side law,</li>
  <li>host-side realization.</li>
</ul>

<p>
The model is intentionally general enough to support open-ended widget-class families over time, while the minimal v0.1 standardized subset remains deliberately conservative.
</p>
