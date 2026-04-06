<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">FROG Widget Class Contract</h1>

<p align="center">
  <strong>Normative class-level contract for widget classes, members, parts, events, value behavior, and object-facing access</strong><br/>
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
  <li><a href="#minimal-v01-standardized-widget-family-for-the-first-executable-slice">27. Minimal v0.1 Standardized Widget Family for the First Executable Slice</a></li>
  <li><a href="#illustrative-example">28. Illustrative Example</a></li>
  <li><a href="#summary">29. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the class-level contract model for FROG widgets.
</p>

<p>
A widget instance in canonical source is not only a placed front-panel element.
It is an instance of a widget class whose exposed members, parts, events, value behavior, and interaction surface must be describable in a stable, inspectable, implementation-independent way.
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
For the first complete executable corridor of v0.1, this document also standardizes one deliberately small but operational widget family sufficient to support:
</p>

<ul>
  <li>one numeric control,</li>
  <li>one numeric indicator,</li>
  <li>natural value participation through <code>widget_value</code>,</li>
  <li>minimal object-style property access through <code>widget_reference</code>,</li>
  <li>and source-persisted front-face presentation metadata through <code>face_color</code> and <code>face_template</code>.</li>
</ul>

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
  <li><code>Front panel.md</code> defines widget composition, containment, serialized panel placement, and source-level front-face persistence posture.</li>
  <li><code>Widget.md</code> defines the widget object model at instance level, including value-carrying behavior, parts, properties, methods, events, and presentation metadata at source level.</li>
  <li><code>Widget interaction.md</code> defines diagram-side interaction with widget references through standardized executable forms such as property read, property write, and method invoke.</li>
  <li><code>Type.md</code> defines the type-expression system used by ordinary typed members.</li>
  <li><code>Diagram.md</code> defines the authoritative executable graph.</li>
  <li><code>Profiles/</code> may define additional widget classes, capability gates, standardized widget-class families, or host-side realization requirements.</li>
  <li><code>Versioning/Readme.md</code> defines the centralized distinction between specification corpus version, top-level <code>spec_version</code>, and program artifact versioning.</li>
</ul>

<p>
Accordingly:
</p>

<pre><code>Front panel           = widget containment, placement, and source-owned front-face persistence
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

source-owned presentation metadata
    !=
class identity
    !=
executable program meaning
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
  <li>which features are profile-gated or host-gated,</li>
  <li>which source-persisted front-face properties are legal.</li>
</ul>

<p>
This document closes that gap by defining the normative class-side contract behind widget instances.
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
  <li>profile and capability gates on widget members,</li>
  <li>the legality of class-recognized source-persisted presentation members.</li>
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
  <li>Ordinary value typing, widget-reference identity, UI sequencing, and front-face presentation metadata MUST remain distinct.</li>
  <li>The class-contract model MUST be general enough to support richer later widget families than those minimally standardized in v0.1.</li>
  <li>A source-persisted presentation property MUST NOT by itself create executable semantics.</li>
  <li>A front-face template resource MUST NOT replace the class contract as the source of widget meaning.</li>
  <li>Later cumulative source-format versions SHOULD normally extend earlier valid class-contract surfaces rather than silently redefine them, unless an explicit breaking boundary is declared centrally.</li>
</ul>

<hr/>

<h2 id="class-contract-model">7. Class Contract Model</h2>

<p>
A widget class contract is the normative description of the object surface shared by all instances of the class.
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
  <li>v0.1 standardizes only a minimal executable subset in the published corpus,</li>
  <li>future families MAY be much richer while still remaining compatible with this contract model.</li>
</ul>

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
  <li><code>properties</code>: declared properties,</li>
  <li><code>methods</code>: declared methods,</li>
  <li><code>events</code>: declared events,</li>
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

<hr/>

<h2 id="member-model">10. Member Model</h2>

<p>
A widget class member is any named exposed object-surface element owned by the widget or one of its declared parts.
</p>

<p>
The standardized member categories are:
</p>

<ul>
  <li>property,</li>
  <li>method,</li>
  <li>event.</li>
</ul>

<p>
A member contract MUST define at least:
</p>

<ul>
  <li>its name,</li>
  <li>its category,</li>
  <li>its owner scope,</li>
  <li>its type or signature where applicable,</li>
  <li>its accessibility constraints,</li>
  <li>its design-time and runtime posture,</li>
  <li>its persistence posture where applicable.</li>
</ul>

<p>
For presentation-oriented properties, the contract SHOULD also define whether the property is:
</p>

<ul>
  <li>source-persisted,</li>
  <li>host-interpreted,</li>
  <li>runtime-writable,</li>
  <li>and semantically non-executable.</li>
</ul>

<hr/>

<h2 id="property-contract">11. Property Contract</h2>

<p>
A property contract defines one named readable and/or writable member.
</p>

<p>
A property contract MUST define:
</p>

<ul>
  <li><code>type</code>,</li>
  <li><code>readable</code>,</li>
  <li><code>writable</code>,</li>
  <li><code>design_time_writable</code>,</li>
  <li><code>runtime_writable</code>,</li>
  <li><code>persistence</code>.</li>
</ul>

<p>
A property contract MAY also define:
</p>

<ul>
  <li><code>default</code>,</li>
  <li><code>semantic_role</code>,</li>
  <li><code>design_time_visible</code>,</li>
  <li><code>runtime_visible</code>,</li>
  <li><code>host_capabilities</code>,</li>
  <li><code>notes</code>.</li>
</ul>

<p>
Standard persistence categories are:
</p>

<ul>
  <li><code>source_owned</code> — persisted in canonical source,</li>
  <li><code>runtime_owned</code> — not required in canonical source and owned by runtime realization,</li>
  <li><code>mixed_boundary</code> — may be source-persisted but also participates in runtime behavior.</li>
</ul>

<p>
A source-persisted presentation property MUST NOT by itself create executable semantics.
</p>

<p>
A property contract MAY be readable and writable without being executable program state.
This is the standard posture for presentation properties such as <code>face_color</code>.
</p>

<hr/>

<h2 id="method-contract">12. Method Contract</h2>

<p>
A method contract defines one named invocable object member.
</p>

<p>
A method contract MUST define:
</p>

<ul>
  <li>its parameter list,</li>
  <li>its return values if any,</li>
  <li>whether invocation is allowed at runtime,</li>
  <li>whether invocation is allowed at design time,</li>
  <li>required host capabilities if any.</li>
</ul>

<p>
Methods MAY be standardized for richer families, but the first executable slice of v0.1 does not require method invocation.
</p>

<hr/>

<h2 id="event-contract">13. Event Contract</h2>

<p>
An event contract defines one named observable event surface.
</p>

<p>
Event publication MAY be standardized for richer widget families.
The first executable slice of v0.1 does not require event observation.
</p>

<hr/>

<h2 id="part-contract">14. Part Contract</h2>

<p>
A part contract defines one named sub-object or addressable sub-surface owned by a widget class.
</p>

<p>
Parts MAY become important for richer designer and object-access scenarios.
The first executable slice does not require standardized addressable parts.
</p>

<hr/>

<h2 id="member-addressing">15. Member Addressing</h2>

<p>
Object-style member addressing MUST remain explicit and stable.
A member address MAY target:
</p>

<ul>
  <li>the widget root object,</li>
  <li>or one declared part of the widget.</li>
</ul>

<p>
The first executable slice standardizes only root-level member access.
</p>

<hr/>

<h2 id="property-and-method-node-synthesis">16. Property and Method Node Synthesis</h2>

<p>
A conforming IDE MAY synthesize property-node and method-node authoring surfaces from the widget class contract.
</p>

<p>
That synthesis MUST preserve the following distinction:
</p>

<pre><code>natural widget_value access
    !=
object-style property access
</code></pre>

<p>
The existence of a property called <code>value</code> does not collapse the natural value path into generic object-style access.
</p>

<p>
Likewise:
</p>

<pre><code>source-owned face_template persistence
    !=
object-style value access
    !=
executable dataflow behavior
</code></pre>

<hr/>

<h2 id="value-member-model">17. Value Member Model</h2>

<p>
A value-carrying widget class MUST declare a primary value semantic.
</p>

<p>
Its class descriptor MUST therefore define:
</p>

<ul>
  <li><code>kind: "value_carrying"</code>,</li>
  <li>the supported value types,</li>
  <li>the object member that corresponds to the primary value, when object access is allowed.</li>
</ul>

<p>
The following distinction MUST remain explicit:
</p>

<pre><code>widget_value(value path)
    !=
property_read/property_write(value member path)
</code></pre>

<p>
The first complete executable slice standardizes support for <code>u16</code> as the required value type of the minimal numeric control and indicator classes.
Other value types MAY be standardized later without changing the contract model.
</p>

<hr/>

<h2 id="capability-and-profile-gating">18. Capability and Profile Gating</h2>

<p>
A widget class MAY require:
</p>

<ul>
  <li>one or more published profile capabilities,</li>
  <li>one or more host-side realization capabilities,</li>
  <li>one or more implementation support claims.</li>
</ul>

<p>
For the first executable slice, the minimal standardized widgets are intentionally host-light.
They require only a host capable of:
</p>

<ul>
  <li>holding one control value,</li>
  <li>holding one indicator value,</li>
  <li>accepting one object-style property write to a presentation property,</li>
  <li>and optionally interpreting a face-template resource.</li>
</ul>

<hr/>

<h2 id="lifecycle-and-state-boundary">19. Lifecycle and State Boundary</h2>

<p>
Widget classes may expose properties whose runtime realization has stateful behavior.
That does not transfer program execution state ownership from the diagram to the widget class.
</p>

<p>
In the first executable slice:
</p>

<ul>
  <li>loop state remains owned by the executable graph,</li>
  <li>front-panel widget state remains presentation-side host realization,</li>
  <li>and the widget class contract does not authorize hidden persistence that would replace explicit program memory.</li>
</ul>

<hr/>

<h2 id="design-time-vs-runtime-owned-members">20. Design-Time vs Runtime-Owned Members</h2>

<p>
Members MUST clearly distinguish:
</p>

<ul>
  <li>design-time visible,</li>
  <li>design-time writable,</li>
  <li>runtime readable,</li>
  <li>runtime writable,</li>
  <li>source persistence posture.</li>
</ul>

<p>
A source-persisted design-time presentation property such as <code>face_template</code>:
</p>

<ul>
  <li>MAY be visible to the designer,</li>
  <li>MAY be used by a host or IDE as a rendering hint or preview asset,</li>
  <li>MUST NOT define executable semantics,</li>
  <li>MUST NOT replace class identity,</li>
  <li>MUST NOT replace value behavior,</li>
  <li>MUST NOT create hidden methods, hidden events, or hidden dataflow behavior.</li>
</ul>

<p>
A source-persisted presentation property such as <code>face_color</code>:
</p>

<ul>
  <li>MAY participate in runtime property writes if the class contract explicitly allows it,</li>
  <li>MAY influence realized appearance,</li>
  <li>MUST remain distinct from the primary value,</li>
  <li>MUST NOT be treated as executable program state.</li>
</ul>

<hr/>

<h2 id="host-requirements">21. Host Requirements</h2>

<p>
A conforming host that claims support for the minimal first executable slice MUST be able to:
</p>

<ul>
  <li>materialize a control widget instance for class <code>frog.ui.standard.numeric_control</code>,</li>
  <li>materialize an indicator widget instance for class <code>frog.ui.standard.numeric_indicator</code>,</li>
  <li>store and expose a primary numeric value of the declared supported type,</li>
  <li>apply a property write to <code>face_color</code>,</li>
  <li>and tolerate a persisted <code>face_template</code> member even if the host does not interpret that template family.</li>
</ul>

<p>
If a host does not support the template family referenced by <code>face_template</code>, it MAY ignore the template while still preserving widget class behavior.
</p>

<p>
If a host does support the template family, that support remains a realization concern.
It MUST NOT redefine the source-level class contract.
</p>

<hr/>

<h2 id="canonical-source-shape">22. Canonical Source Shape</h2>

<p>
This document does not own widget instance serialization.
However, a class contract conceptually has the following shape:
</p>

<pre><code>{
  "class": "frog.ui.standard.numeric_control",
  "version": "0.1",
  "roles": ["control"],
  "value_behavior": {
    "kind": "value_carrying",
    "supported_value_types": ["u16"],
    "object_value_member": "value"
  },
  "properties": {},
  "methods": {},
  "events": {},
  "parts": {},
  "profile_requirements": [],
  "host_requirements": []
}
</code></pre>

<hr/>

<h2 id="validation-rules">23. Validation Rules</h2>

<p>
Validators MUST reject at least the following:
</p>

<ul>
  <li>unknown widget class,</li>
  <li>unknown member,</li>
  <li>member access forbidden by access mode,</li>
  <li>part addressing to undeclared parts,</li>
  <li>declared widget value type unsupported by the widget class,</li>
  <li>attempt to persist source-owned presentation members not recognized by the widget class contract,</li>
  <li>attempt to infer object access legality solely from value-carrying status.</li>
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
  <li>confusion between ordinary value typing and interaction-token categories,</li>
  <li>attempt to treat a front-face template resource as though it were a method, event, or executable semantic surface.</li>
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
  <li>value-member consistency for value-carrying widgets,</li>
  <li>legality of persisted presentation members such as <code>face_color</code> and <code>face_template</code>.</li>
</ul>

<p>
Conformance cases SHOULD also verify that implementations do not silently collapse:
</p>

<ul>
  <li>natural value access into generic object-style access,</li>
  <li>runtime-owned members into required serialized source members,</li>
  <li>host-specific richness into normative class-contract requirements,</li>
  <li>front-face template interpretation into executable semantic law.</li>
</ul>

<hr/>

<h2 id="non-goals">26. Non-Goals</h2>

<p>
This document does not:
</p>

<ul>
  <li>standardize one final universal widget family,</li>
  <li>standardize one mandatory UI toolkit,</li>
  <li>define pixel-perfect rendering of widgets,</li>
  <li>define one event-loop architecture,</li>
  <li>replace the front panel as owner of widget placement,</li>
  <li>replace the diagram as owner of executable behavior.</li>
</ul>

<hr/>

<h2 id="minimal-v01-standardized-widget-family-for-the-first-executable-slice">27. Minimal v0.1 Standardized Widget Family for the First Executable Slice</h2>

<p>
For the first complete executable vertical slice, FROG v0.1 standardizes the following minimal widget classes:
</p>

<ul>
  <li><code>frog.ui.standard.numeric_control</code>,</li>
  <li><code>frog.ui.standard.numeric_indicator</code>.</li>
</ul>

<p>
These classes are standardized conservatively.
They are intended to support one real source-to-execution corridor, not to freeze the final long-term richness of the full widget ecosystem.
</p>

<h3>27.1 Standard class: <code>frog.ui.standard.numeric_control</code></h3>

<pre><code>{
  "class": "frog.ui.standard.numeric_control",
  "version": "0.1",
  "roles": ["control"],
  "value_behavior": {
    "kind": "value_carrying",
    "supported_value_types": ["u16"],
    "object_value_member": "value"
  },
  "properties": {
    "value": {
      "type": "u16",
      "readable": true,
      "writable": true,
      "design_time_writable": true,
      "runtime_writable": true,
      "persistence": "mixed_boundary",
      "default": 0,
      "semantic_role": "primary_value",
      "design_time_visible": true,
      "runtime_visible": true
    },
    "caption": {
      "type": "string",
      "readable": true,
      "writable": true,
      "design_time_writable": true,
      "runtime_writable": false,
      "persistence": "source_owned",
      "default": "",
      "semantic_role": "presentation_label",
      "design_time_visible": true,
      "runtime_visible": true
    },
    "face_color": {
      "type": "frog.ui.color",
      "readable": true,
      "writable": true,
      "design_time_writable": true,
      "runtime_writable": true,
      "persistence": "source_owned",
      "default": "#D0D0D0",
      "semantic_role": "visual_face_fill",
      "design_time_visible": true,
      "runtime_visible": true
    },
    "face_template": {
      "type": "frog.ui.face_template_ref",
      "readable": true,
      "writable": true,
      "design_time_writable": true,
      "runtime_writable": false,
      "persistence": "source_owned",
      "semantic_role": "presentation_template",
      "design_time_visible": true,
      "runtime_visible": true
    }
  },
  "methods": {},
  "events": {},
  "parts": {},
  "profile_requirements": [],
  "host_requirements": [
    "ui_basic_numeric_control",
    "ui_property_write_face_color",
    "ui_optional_face_template_support"
  ]
}
</code></pre>

<h3>27.2 Standard class: <code>frog.ui.standard.numeric_indicator</code></h3>

<pre><code>{
  "class": "frog.ui.standard.numeric_indicator",
  "version": "0.1",
  "roles": ["indicator"],
  "value_behavior": {
    "kind": "value_carrying",
    "supported_value_types": ["u16"],
    "object_value_member": "value"
  },
  "properties": {
    "value": {
      "type": "u16",
      "readable": true,
      "writable": true,
      "design_time_writable": true,
      "runtime_writable": true,
      "persistence": "mixed_boundary",
      "default": 0,
      "semantic_role": "primary_value",
      "design_time_visible": true,
      "runtime_visible": true
    },
    "caption": {
      "type": "string",
      "readable": true,
      "writable": true,
      "design_time_writable": true,
      "runtime_writable": false,
      "persistence": "source_owned",
      "default": "",
      "semantic_role": "presentation_label",
      "design_time_visible": true,
      "runtime_visible": true
    },
    "face_color": {
      "type": "frog.ui.color",
      "readable": true,
      "writable": true,
      "design_time_writable": true,
      "runtime_writable": true,
      "persistence": "source_owned",
      "default": "#D8E6FF",
      "semantic_role": "visual_face_fill",
      "design_time_visible": true,
      "runtime_visible": true
    },
    "face_template": {
      "type": "frog.ui.face_template_ref",
      "readable": true,
      "writable": true,
      "design_time_writable": true,
      "runtime_writable": false,
      "persistence": "source_owned",
      "semantic_role": "presentation_template",
      "design_time_visible": true,
      "runtime_visible": true
    }
  },
  "methods": {},
  "events": {},
  "parts": {},
  "profile_requirements": [],
  "host_requirements": [
    "ui_basic_numeric_indicator",
    "ui_property_write_face_color",
    "ui_optional_face_template_support"
  ]
}
</code></pre>

<h3>27.3 Face-template posture</h3>

<p>
The standardized type <code>frog.ui.face_template_ref</code> is a source-owned presentation reference.
For the first executable slice, the only recommended resource family is an SVG template resource reference.
</p>

<p>
That template:
</p>

<ul>
  <li>MAY be used by an IDE designer for preview,</li>
  <li>MAY be used by a host as a skin resource,</li>
  <li>MUST NOT define executable semantics,</li>
  <li>MUST NOT create methods, events, state, or value behavior,</li>
  <li>MUST NOT replace the class contract as the source of object meaning.</li>
</ul>

<hr/>

<h2 id="illustrative-example">28. Illustrative Example</h2>

<p>
Conceptually:
</p>

<pre><code>Widget class: frog.ui.standard.numeric_control

  Widget-level properties
    - value         : u16                         read/write
    - caption       : string                      read/write (design-time source-owned)
    - face_color    : frog.ui.color               read/write
    - face_template : frog.ui.face_template_ref   read/write (design-time source-owned)

  Widget-level methods
    - none required for the first executable slice

  Widget-level events
    - none required for the first executable slice
</code></pre>

<p>
The matching indicator class exposes the same minimal primary value and presentation surface, with role compatibility restricted to <code>indicator</code>.
</p>

<hr/>

<h2 id="summary">29. Summary</h2>

<p>
This document defines the stable class-level contract model behind FROG widget instances.
</p>

<p>
For the first complete executable slice of v0.1, it standardizes two minimal but serious widget classes:
</p>

<ul>
  <li>one numeric control class,</li>
  <li>one numeric indicator class.</li>
</ul>

<p>
Those classes support:
</p>

<ul>
  <li>an explicit primary value of type <code>u16</code>,</li>
  <li>a natural <code>widget_value</code> path,</li>
  <li>object-style property access to <code>value</code> when applicable,</li>
  <li>source-persisted presentation properties such as <code>face_color</code> and <code>face_template</code>,</li>
  <li>and a presentation-template posture that remains clearly distinct from executable semantics.</li>
</ul>
