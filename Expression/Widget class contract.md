<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">FROG Widget Class Contract</h1>

<p align="center">
  <strong>Normative class-level contract for widget classes, members, parts, events, and IDE/runtime-facing object exposure</strong><br/>
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
  <li><a href="#general-extensibility-posture">8. General Extensibility Posture</a></li>
  <li><a href="#widget-class-descriptor">9. Widget Class Descriptor</a></li>
  <li><a href="#member-model">10. Member Model</a></li>
  <li><a href="#property-contract">11. Property Contract</a></li>
  <li><a href="#method-contract">12. Method Contract</a></li>
  <li><a href="#event-contract">13. Event Contract</a></li>
  <li><a href="#part-contract">14. Part Contract</a></li>
  <li><a href="#member-addressing">15. Member Addressing</a></li>
  <li><a href="#property-and-method-node-synthesis">16. Property and Method Node Synthesis</a></li>
  <li><a href="#value-member-model">17. Value Member Model</a></li>
  <li><a href="#capability-and-profile-gating">18. Capability and Profile Gating</a></li>
  <li><a href="#lifecycle-and-state-boundary">19. Lifecycle and State Boundary</a></li>
  <li><a href="#design-time-vs-runtime-owned-members">20. Design-Time vs Runtime-Owned Members</a></li>
  <li><a href="#host-requirements">21. Host Requirements</a></li>
  <li><a href="#canonical-source-shape">22. Canonical Source Shape</a></li>
  <li><a href="#validation-rules">23. Validation Rules</a></li>
  <li><a href="#diagnostics">24. Diagnostics</a></li>
  <li><a href="#conformance-implications">25. Conformance Implications</a></li>
  <li><a href="#non-goals">26. Non-Goals</a></li>
  <li><a href="#minimal-v01-standardization-posture">27. Minimal v0.1 Standardization Posture</a></li>
  <li><a href="#illustrative-example">28. Illustrative Example</a></li>
  <li><a href="#summary">29. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the class-level contract model for FROG widgets.
</p>

<p>
A widget instance in canonical source is not only a placed front-panel element. It is an instance of a widget class whose exposed members, parts, events, and interaction surface must be describable in a stable, inspectable, implementation-independent way.
</p>

<p>
The purpose of this document is to make widget classes sufficiently explicit that:
</p>

<ul>
  <li>an IDE can expose coherent property and method access for widget objects,</li>
  <li>a validator can verify whether member access is legal,</li>
  <li>a derivation pipeline can preserve object-level intent into execution-facing representation where applicable,</li>
  <li>a runtime or UI host can realize the widget without becoming the hidden source of semantic truth,</li>
  <li>independent implementations can converge on the same object-surface interpretation.</li>
</ul>

<p>
This document defines a general class-contract model capable of supporting a wide range of widget families over time.
It does not claim that every possible widget family is already standardized in v0.1.
</p>

<p>
This document does not define repository-wide version policy.
Top-level <code>spec_version</code> identifies the source-format compatibility target of the containing <code>.frog</code> file, while the published specification corpus version and cumulative version-transition posture remain governed centrally in <code>Versioning/Readme.md</code>.
</p>

<hr/>

<h2 id="scope">2. Scope</h2>

<p>
This document standardizes the normative contract shape of a widget class.
</p>

<p>
It defines:
</p>

<ul>
  <li>how a widget class is described,</li>
  <li>how members are categorized and declared,</li>
  <li>how parts participate in member ownership and addressing,</li>
  <li>how property, method, and event surfaces are described at class level,</li>
  <li>how a class contract constrains legal object-style access,</li>
  <li>how IDEs may synthesize property-node and method-node surfaces from the class contract,</li>
  <li>how profile and capability gating constrain widget availability,</li>
  <li>and how the contract model remains open to richer future widget families without forcing them all into v0.1.</li>
</ul>

<p>
This document does not define:
</p>

<ul>
  <li>pixel rendering behavior,</li>
  <li>theme systems,</li>
  <li>private runtime memory layouts,</li>
  <li>one mandatory UI toolkit,</li>
  <li>one mandatory event loop implementation,</li>
  <li>diagram-side executable node semantics for widget interaction primitives,</li>
  <li>repository-wide version-transition doctrine.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<ul>
  <li><code>Front panel.md</code> defines widget composition, containment, and serialized panel placement.</li>
  <li><code>Widget.md</code> defines the widget object model at instance level, including value-carrying behavior, parts, properties, methods, and events.</li>
  <li><code>Widget interaction.md</code> defines diagram-side interaction with widget references through standardized executable forms such as property read, property write, and method invoke.</li>
  <li><code>Type.md</code> defines the type-expression system used by ordinary typed members.</li>
  <li><code>Diagram.md</code> defines the authoritative executable graph.</li>
  <li><code>Profiles/</code> may define additional widget classes, capability gates, standardized widget-class families, or host-side realization requirements.</li>
  <li><code>Versioning/Readme.md</code> defines the centralized distinction between specification corpus version, top-level <code>spec_version</code>, and program artifact versioning.</li>
</ul>

<p>
Accordingly:
</p>

<pre><code>Front panel           = widget containment and placement
Widget                = instance-side widget object model
Widget class contract = class-level object contract
Widget interaction    = executable object access from the diagram
Diagram               = authoritative executable behavior
Profiles              = optional capability and target gating
Versioning            = centralized cross-version governance
</code></pre>

<p>
The following distinctions MUST remain explicit:
</p>

<pre><code>ordinary typed value
    !=
widget reference token
    !=
UI sequencing token

instance-side widget declaration
    !=
class-side member legality
    !=
primitive-local interaction semantics
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
  <li>which parts may be targeted,</li>
  <li>how IDEs expose property-node and method-node surfaces,</li>
  <li>which accesses are valid at design time versus runtime,</li>
  <li>which features are profile-gated or host-gated.</li>
</ul>

<p>
This document closes that gap by defining the normative class-side contract behind widget instances.
</p>

<p>
It also exists so that FROG can remain open to richer widget-class families over time without having to redefine the contract model each time a new class family is introduced.
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
  <li>class-driven IDE exposure rules for object-style access,</li>
  <li>profile and capability gates on widget members.</li>
</ul>

<p>
This document does not own:
</p>

<ul>
  <li>actual widget instance placement on the panel,</li>
  <li>authoritative executable graph semantics,</li>
  <li>the semantics of <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, or <code>frog.ui.method_invoke</code>,</li>
  <li>one required runtime realization strategy,</li>
  <li>one required IDE product behavior beyond the normative exposure surface implied by the class contract,</li>
  <li>repository-wide version-transition doctrine.</li>
</ul>

<p>
This document therefore defines the general contract model itself, while richer families and family-specific standardizations may be published elsewhere without changing these ownership boundaries.
</p>

<hr/>

<h2 id="core-principles">6. Core Principles</h2>

<ul>
  <li>A widget class MUST expose a stable contract independent from one private implementation.</li>
  <li>A widget instance MUST be interpretable against its declared widget class.</li>
  <li>Object-style member access MUST be validated against the widget class contract.</li>
  <li>Part access MUST remain explicit and MUST NOT rely on hidden runtime reflection.</li>
  <li>Profile-gated members and classes MUST remain explicit.</li>
  <li>Design-time metadata and runtime-owned state MUST remain distinct.</li>
  <li>IDE convenience MUST NOT become hidden semantic law.</li>
  <li>Runtime realization MAY be richer than the standard contract, but non-standard richness MUST NOT be required for canonical source validity.</li>
  <li>Ordinary value typing, widget-reference identity, and UI sequencing MUST remain distinct.</li>
  <li>The class-contract model MUST be general enough to support richer later widget families than those minimally standardized in v0.1.</li>
  <li>Later cumulative source-format versions SHOULD normally extend earlier valid class-contract surfaces rather than silently redefine them, unless an explicit breaking boundary is declared centrally.</li>
</ul>

<hr/>

<h2 id="class-contract-model">7. Class Contract Model</h2>

<p>
A widget class contract is the normative description of the object surface shared by all instances of the class.
</p>

<p>
Conceptually:
</p>

<pre><code>widget class contract
  ├── class identity
  ├── role compatibility
  ├── value behavior
  ├── properties
  ├── methods
  ├── events
  ├── parts
  ├── capability gates
  ├── design-time constraints
  └── host realization requirements
</code></pre>

<p>
A widget instance then binds:
</p>

<ul>
  <li>an instance identifier,</li>
  <li>a class identity,</li>
  <li>role-specific instance data,</li>
  <li>instance property values where permitted,</li>
  <li>optional part-instance data where permitted.</li>
</ul>

<p>
The class contract defines the legal object surface.
It does not itself serialize one runtime object instance, one runtime handle, or one runtime scheduling policy.
</p>

<hr/>

<h2 id="general-extensibility-posture">8. General Extensibility Posture</h2>

<p>
The class-contract model defined by this document is intentionally general.
</p>

<p>
It is designed so that FROG can support over time:
</p>

<ul>
  <li>additional standardized widget classes,</li>
  <li>richer standardized widget-class families,</li>
  <li>profile-owned capability families,</li>
  <li>recognized external class-family packages,</li>
  <li>and implementation support claims that remain explicit and inspectable.</li>
</ul>

<p>
The key rule is:
</p>

<pre><code>general contract capability
    !=
full family standardization in v0.1
</code></pre>

<p>
Accordingly:
</p>

<ul>
  <li>this document defines a contract model that is open-ended by construction,</li>
  <li>v0.1 standardizes only a minimal executable subset elsewhere in the published corpus,</li>
  <li>future families MAY be much richer while still remaining compatible with this contract model.</li>
</ul>

<p>
This document therefore SHOULD NOT be interpreted as limiting FROG to only the widget classes explicitly standardized in the minimal v0.1 subset.
It defines the class-contract model that those classes use and that richer families may also use.
</p>

<hr/>

<h2 id="widget-class-descriptor">9. Widget Class Descriptor</h2>

<p>
Every widget class contract MUST provide a stable class descriptor.
</p>

<p>
A class descriptor MUST include:
</p>

<ul>
  <li><code>class</code>: canonical class identifier,</li>
  <li><code>version</code>: contract version identifier,</li>
  <li><code>roles</code>: allowed widget roles for the class,</li>
  <li><code>value_behavior</code>: whether the class is value-carrying, reference-only, event-producing, or mixed,</li>
  <li><code>members</code>: declared properties, methods, and events,</li>
  <li><code>parts</code>: declared parts exposed by the class, if any,</li>
  <li><code>profile_requirements</code>: required profile capabilities, if any,</li>
  <li><code>host_requirements</code>: realization requirements that a conforming host must satisfy for supported execution modes.</li>
</ul>

<p>
A class descriptor MAY include:
</p>

<ul>
  <li><code>display_name</code>,</li>
  <li><code>description</code>,</li>
  <li><code>categories</code>,</li>
  <li><code>deprecated_members</code>,</li>
  <li><code>compatibility_notes</code>.</li>
</ul>

<p>
A widget class identifier MUST be stable across implementations for the same standardized class.
</p>

<p>
A class-contract <code>version</code> identifies the contract revision of that widget class surface. It MUST NOT be confused with the repository-wide specification corpus version, the file-level <code>spec_version</code> carried by a <code>.frog</code> program, or the program artifact version carried in metadata.
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
  <li><strong>property</strong>: stateful readable and/or writable member,</li>
  <li><strong>method</strong>: invocable operation,</li>
  <li><strong>event</strong>: observable occurrence emitted by the widget or part.</li>
</ul>

<p>
Each member descriptor MUST declare:
</p>

<ul>
  <li><code>name</code>,</li>
  <li><code>kind</code>,</li>
  <li><code>owner_scope</code>: widget or part,</li>
  <li><code>availability</code>: always, role-gated, profile-gated, host-gated, or state-gated,</li>
  <li><code>design_time_access</code>,</li>
  <li><code>runtime_access</code>,</li>
  <li><code>diagnostic_name</code> when a more user-facing label is needed.</li>
</ul>

<p>
A member descriptor MUST NOT rely on runtime-only discovery for normative validity.
</p>

<p>
If a member exposes ordinary values, its type information MUST follow <code>Type.md</code>.
If a member consumes or emits interaction tokens, those token categories MUST remain explicit and MUST NOT be silently treated as ordinary value types.
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
  <li><code>effects</code>: pure-read, UI-side-effect, layout-side-effect, host-side-effect, or implementation-defined-extended,</li>
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
  <li><code>requires_idle_state</code>,</li>
  <li><code>notes</code>.</li>
</ul>

<p>
A property MUST NOT be assumed readable or writable unless the contract declares it.
</p>

<p>
Examples:
</p>

<ul>
  <li><code>value</code> on a control class may be readable and writable at runtime,</li>
  <li><code>visible</code> may be readable and writable,</li>
  <li><code>bounds</code> may be design-time writable and runtime readable only,</li>
  <li><code>render_handle</code> may be runtime-owned and not source-owned.</li>
</ul>

<p>
When a property carries an ordinary value, its <code>type</code> MUST be a valid ordinary value type expression or another explicitly standardized member-type form allowed by the active profile.
When a property is runtime-owned, that runtime ownership MUST NOT make canonical source validity depend on hidden runtime reflection data.
</p>

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
  <li><code>ordering_requirements</code> when invocation must participate in explicit UI sequencing,</li>
  <li><code>failure_surface</code>: none, standard-error-output, raised-diagnostic, or profile-defined.</li>
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
A method MUST NOT be treated as a property write shortcut.
</p>

<p>
Examples:
</p>

<ul>
  <li><code>reset_to_default()</code>,</li>
  <li><code>focus()</code>,</li>
  <li><code>scroll_into_view()</code>,</li>
  <li><code>append_series_point(value)</code> for a profile-defined graph widget class.</li>
</ul>

<p>
When a method parameter or result carries an ordinary value, its type MUST follow <code>Type.md</code>.
When a method requires explicit UI ordering, that requirement MUST remain explicit rather than being inferred from one private host implementation.
</p>

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
  <li><code>ordering_notes</code> when observable ordering matters,</li>
  <li><code>runtime_only</code> or mixed availability.</li>
</ul>

<p>
Event descriptors MAY define:
</p>

<ul>
  <li><code>bubbling</code> or containment propagation,</li>
  <li><code>coalescing</code> behavior,</li>
  <li><code>rate_limit</code> expectations,</li>
  <li><code>host_dependency</code>.</li>
</ul>

<p>
This document defines the object-surface event contract only. It does not define one mandatory event-processing runtime model.
</p>

<p>
If an event payload carries ordinary values, those payload value types MUST remain attributable and explicit.
This document does not standardize one mandatory event-runtime transport representation.
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
  <li>plot area,</li>
  <li>cursor,</li>
  <li>legend,</li>
  <li>axis,</li>
  <li>increment button,</li>
  <li>decrement button.</li>
</ul>

<p>
A part descriptor MUST include:
</p>

<ul>
  <li><code>name</code>,</li>
  <li><code>class</code> or part contract identity,</li>
  <li><code>cardinality</code>: single, indexed, keyed, or profile-defined,</li>
  <li><code>members</code>: properties, methods, and events exposed by the part,</li>
  <li><code>presence_rule</code>: always present, optional, or configuration-dependent.</li>
</ul>

<p>
A part MUST NOT be treated as an independent top-level widget unless another specification explicitly says so.
</p>

<p>
Part surfaces MUST remain explicitly attributable to the owning widget class contract rather than to hidden runtime reflection behavior.
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
widget.part(member_scope).member
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
The class contract defines the legal target surface.
The executable transport of a widget reference and any explicit sequencing requirements remain owned elsewhere.
</p>

<hr/>

<h2 id="property-and-method-node-synthesis">16. Property and Method Node Synthesis</h2>

<p>
A conforming IDE MAY synthesize property-node and method-node authoring surfaces from the widget class contract.
</p>

<p>
When it does so, the synthesis MUST respect the normative contract.
</p>

<p>
The following rules apply:
</p>

<ul>
  <li>a property marked non-readable MUST NOT appear as a readable property target,</li>
  <li>a property marked non-writable MUST NOT appear as a writable property target,</li>
  <li>a method marked non-invocable in the current context MUST NOT appear as invocable in that context,</li>
  <li>role-gated, profile-gated, or host-gated members MUST be hidden or diagnosed when unavailable,</li>
  <li>deprecated members SHOULD be distinguishable,</li>
  <li>part-level members MUST remain visibly attributable to the owning part,</li>
  <li>mixed-boundary members SHOULD distinguish design-time from runtime access.</li>
</ul>

<p>
An IDE MAY offer richer authoring affordances, but those affordances MUST NOT contradict the class contract.
</p>

<p>
IDE synthesis MUST NOT silently collapse:
</p>

<ul>
  <li>natural <code>widget_value</code> access into generic object-style property access,</li>
  <li>ordinary value typing into widget-reference transport,</li>
  <li>host-specific convenience behavior into normative member legality.</li>
</ul>

<hr/>

<h2 id="value-member-model">17. Value Member Model</h2>

<p>
For value-carrying widget classes, the relation between the main widget value and the object model MUST remain explicit.
</p>

<p>
A value-carrying widget class MUST define:
</p>

<ul>
  <li>whether <code>value</code> exists as a named property in the object model,</li>
  <li>the value type,</li>
  <li>whether the value is readable, writable, or both,</li>
  <li>whether value access is equivalent to or distinct from diagram-side <code>widget_value</code> access.</li>
</ul>

<p>
The following distinction MUST remain explicit:
</p>

<pre><code>widget_value access
  !=
object-style property access to value
</code></pre>

<p>
They may target related semantics, but they are not the same abstraction layer.
</p>

<p>
The following distinction MUST also remain explicit:
</p>

<pre><code>ordinary value member typing
  !=
widget reference transport
  !=
UI sequencing transport
</code></pre>

<p>
A value-carrying class MUST therefore not be interpreted as making widget references or sequencing ports ordinary user-declared value types.
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
  <li>a base boolean button class may belong to the core widget vocabulary,</li>
  <li>a waveform graph class may require a richer UI capability family,</li>
  <li>a drag-and-drop method may require host support not guaranteed by every runtime,</li>
  <li>a hardware-backed display widget may require a profile-specific UI host.</li>
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

<p>
Later cumulative source-format versions MAY add new classes, parts, members, or gates, but repository-wide compatibility posture for such growth remains centralized in <code>Versioning/Readme.md</code>.
</p>

<hr/>

<h2 id="lifecycle-and-state-boundary">19. Lifecycle and State Boundary</h2>

<p>
A widget class contract MAY declare lifecycle-related requirements for its members.
</p>

<p>
These may include:
</p>

<ul>
  <li>creation-time only members,</li>
  <li>design-time only members,</li>
  <li>runtime-only readable members,</li>
  <li>members available only after initialization,</li>
  <li>members invalid after disposal or detachment.</li>
</ul>

<p>
The class contract MUST NOT require one hidden runtime lifecycle implementation. It only standardizes which member availability constraints exist.
</p>

<hr/>

<h2 id="design-time-vs-runtime-owned-members">20. Design-Time vs Runtime-Owned Members</h2>

<p>
The class contract MUST distinguish at least the following ownership classes:
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
  <li>visible may be mixed-boundary if source-defaulted but runtime-writable.</li>
</ul>

<p>
This distinction is necessary so that canonical source validity does not depend on opaque runtime reflection data.
</p>

<p>
Runtime-owned members MAY still be readable or observable at runtime, but they MUST NOT become hidden mandatory serialized state for canonical source validity.
</p>

<hr/>

<h2 id="host-requirements">21. Host Requirements</h2>

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

<h2 id="canonical-source-shape">22. Canonical Source Shape</h2>

<p>
Canonical v0.1 source does not require every FROG file to embed full widget class descriptors inline.
</p>

<p>
However, when a widget class contract is serialized or referenced in canonical source or repository-visible support material, the conceptual shape SHOULD follow this structure:
</p>

<pre><code>{
  "class": "frog.ui.standard.numeric_control",
  "version": "0.1",
  "roles": ["control"],
  "value_behavior": {
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
      "runtime_only": true
    }
  },
  "parts": {
    "label": {
      "class": "frog.ui.standard.label_part",
      "cardinality": "single"
    }
  }
}
</code></pre>

<p>
The exact serialization home of standardized widget class contracts may be defined by future specification work. This document defines the contract model itself.
</p>

<p>
The example above uses canonical ordinary value type expressions such as <code>f64</code> and <code>bool</code>. It does not imply that widget references or sequencing tokens are declared through the same ordinary source type-expression vocabulary.
</p>

<hr/>

<h2 id="validation-rules">23. Validation Rules</h2>

<p>
Validators MUST enforce at least the following rules when class contracts are used normatively:
</p>

<ul>
  <li>a class identifier MUST be present,</li>
  <li>a class contract version MUST be present,</li>
  <li>member names MUST be unique within their owner scope and member kind where ambiguity would arise,</li>
  <li>a property MUST declare a type,</li>
  <li>a method parameter list and result list MUST be structurally valid,</li>
  <li>a part contract MUST declare its cardinality,</li>
  <li>a member MUST NOT be both available and forbidden in the same access context,</li>
  <li>profile-gated or host-gated members MUST carry explicit gating metadata,</li>
  <li>a value-carrying class MUST define its value behavior coherently,</li>
  <li>a class MUST NOT require private runtime-only reflection metadata for canonical validity.</li>
</ul>

<p>
Validators SHOULD additionally preserve the following distinctions explicitly:
</p>

<ul>
  <li>ordinary typed value member versus widget-reference token,</li>
  <li>ordinary typed value member versus sequencing token,</li>
  <li>source-owned member versus runtime-owned member,</li>
  <li>design-time legality versus runtime legality.</li>
</ul>

<p>
Validators SHOULD also diagnose when an implementation-specific rich class surface is presented as though it were already part of the standardized minimal v0.1 subset without an explicit published contract.
</p>

<hr/>

<h2 id="diagnostics">24. Diagnostics</h2>

<p>
Validators SHOULD diagnose at least the following classes of errors:
</p>

<ul>
  <li>unknown widget class,</li>
  <li>unsupported class version,</li>
  <li>unknown member,</li>
  <li>unknown part,</li>
  <li>invalid owner scope,</li>
  <li>invalid access mode,</li>
  <li>attempted write to read-only property,</li>
  <li>attempted read from write-only property,</li>
  <li>invocation of unavailable method,</li>
  <li>use of profile-gated member outside the required profile,</li>
  <li>use of host-gated member without required host capability,</li>
  <li>ambiguous or invalid part addressing,</li>
  <li>illegal dependence on runtime-only property for source validity,</li>
  <li>confusion between ordinary value typing and interaction-token categories.</li>
</ul>

<hr/>

<h2 id="conformance-implications">25. Conformance Implications</h2>

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
  <li>value-member consistency for value-carrying widgets.</li>
</ul>

<p>
Conformance cases SHOULD also verify that implementations do not silently collapse:
</p>

<ul>
  <li>natural value access into generic object-style access,</li>
  <li>runtime-owned members into required serialized source members,</li>
  <li>host-specific richness into normative class-contract requirements.</li>
</ul>

<p>
Conformance SHOULD also distinguish clearly between:
</p>

<ul>
  <li>what belongs to the minimal standardized v0.1 subset,</li>
  <li>what belongs to richer but explicitly published class families,</li>
  <li>and what is implementation-private only.</li>
</ul>

<hr/>

<h2 id="non-goals">26. Non-Goals</h2>

<p>
This document is not:
</p>

<ul>
  <li>a complete GUI toolkit specification,</li>
  <li>a rendering engine specification,</li>
  <li>a theme or styling guide,</li>
  <li>a complete event-loop specification,</li>
  <li>a private runtime object layout specification,</li>
  <li>a mandate that every implementation expose identical authoring ergonomics,</li>
  <li>a repository-wide versioning policy.</li>
</ul>

<hr/>

<h2 id="minimal-v01-standardization-posture">27. Minimal v0.1 Standardization Posture</h2>

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
This posture defines the minimum coherent contract surface, not the maximum future richness of the FROG widget ecosystem.
</p>

<p>
Future versions MAY extend this contract model with:
</p>

<ul>
  <li>inheritance or interface-style class factoring,</li>
  <li>richer event routing,</li>
  <li>collection-like parts,</li>
  <li>stronger host accessibility contracts,</li>
  <li>richer capability taxonomies,</li>
  <li>more formal IDE exposure recommendations,</li>
  <li>and richer standardized widget families published through compatible profile surfaces.</li>
</ul>

<p>
Such growth SHOULD normally remain cumulative and centrally governed through the published versioning surface rather than being redefined independently by local widget documents.
</p>

<hr/>

<h2 id="illustrative-example">28. Illustrative Example</h2>

<p>
Conceptually:
</p>

<pre><code>Widget class: frog.ui.standard.numeric_control

  Widget-level properties
    - value        : f64      read/write
    - visible      : bool     read/write
    - enabled      : bool     read/write

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
  <li><code>value</code>, <code>visible</code>, and <code>enabled</code> in a property-node surface,</li>
  <li><code>reset_to_default()</code> and <code>focus()</code> in a method-node surface,</li>
  <li><code>label.text</code> as a part-scoped property target,</li>
  <li>diagnostics when a forbidden access mode is attempted.</li>
</ul>

<p>
The same general contract model may later support richer families than this illustrative example without changing the architectural ownership boundaries defined by this document.
</p>

<hr/>

<h2 id="summary">29. Summary</h2>

<p>
The widget class contract is the normative class-side object surface that makes widget interaction explicit, inspectable, and implementation-independent.
</p>

<p>
It closes the gap between:
</p>

<ul>
  <li>instance-side front-panel serialization,</li>
  <li>diagram-side widget interaction primitives,</li>
  <li>IDE-side property and method exposure,</li>
  <li>runtime-side realization constraints.</li>
</ul>

<p>
By keeping widget classes explicit, FROG can support rich widget-object interaction without turning one private IDE or runtime into the hidden source of truth.
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
  <li>local class-contract revision,</li>
  <li>centralized repository-wide version governance.</li>
</ul>

<p>
The contract model is intentionally general enough to support open-ended widget-class families over time, while the minimal v0.1 standardized subset remains deliberately conservative.
</p>
