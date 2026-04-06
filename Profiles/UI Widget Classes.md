<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">FROG UI Widget Classes Profile</h1>

<p align="center">
  <strong>Optional standardized widget-class catalog and class-contract profile for portable front-panel object ecosystems and the first executable UI slice</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#purpose">2. Purpose of this Profile</a></li>
  <li><a href="#architectural-role">3. Architectural Role</a></li>
  <li><a href="#scope">4. Scope</a></li>
  <li><a href="#non-scope">5. What this Profile Does Not Define</a></li>
  <li><a href="#relation-with-other-specifications">6. Relation with Other Specifications</a></li>
  <li><a href="#why-this-belongs-in-profiles">7. Why this Belongs in <code>Profiles/</code></a></li>
  <li><a href="#core-model">8. Core Model</a></li>
  <li><a href="#widget-class-contract">9. Widget Class Contract</a></li>
  <li><a href="#property-contract">10. Property Contract</a></li>
  <li><a href="#method-contract">11. Method Contract</a></li>
  <li><a href="#event-contract">12. Event Contract</a></li>
  <li><a href="#part-contract">13. Part Contract</a></li>
  <li><a href="#design-time-vs-runtime">14. Design-Time vs Runtime Distinction</a></li>
  <li><a href="#program-model-and-ide-consumption">15. Program Model and IDE Consumption</a></li>
  <li><a href="#interaction-node-consumption">16. Interaction-Node Consumption</a></li>
  <li><a href="#execution-facing-posture">17. Execution-Facing Posture</a></li>
  <li><a href="#profile-identification-and-claims">18. Profile Identification and Claims</a></li>
  <li><a href="#minimal-executable-widget-family">19. Minimal Executable Widget Family for the First Vertical Slice</a></li>
  <li><a href="#validation-rules">20. Validation Rules</a></li>
  <li><a href="#examples">21. Examples</a></li>
  <li><a href="#out-of-scope-for-v01">22. Out of Scope for v0.1</a></li>
  <li><a href="#summary">23. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines an optional FROG profile for standardized UI widget classes and their portable class contracts.
</p>

<p>
The profile exists to make front-panel widget ecosystems portable, inspectable, and tool-consumable without collapsing widget-class definition into:
</p>

<ul>
  <li>canonical widget-instance source representation,</li>
  <li>intrinsic <code>frog.ui.*</code> interaction primitive ownership,</li>
  <li>runtime-private widget handles,</li>
  <li>one IDE's internal object model,</li>
  <li>one rendering toolkit's private reflection system,</li>
  <li>or one host's private skinning system.</li>
</ul>

<p>
The goal is to provide a standardized class-catalog layer that lets a conforming IDE, validator, IR pipeline, lowering pipeline, backend-facing handoff, and runtime-facing host understand what a widget class exposes:
</p>

<ul>
  <li>its identity,</li>
  <li>its role constraints,</li>
  <li>its value-carrying behavior,</li>
  <li>its parts,</li>
  <li>its properties,</li>
  <li>its methods,</li>
  <li>its events,</li>
  <li>its design-time / runtime applicability boundaries,</li>
  <li>and its presentation-surface boundaries where the class supports front-panel skinning metadata.</li>
</ul>

<p>
This profile therefore closes an important architectural gap between:
</p>

<pre><code>Expression/Widget.md
        +
Expression/Widget class contract.md
        +
Expression/Widget interaction.md
        +
Expression/Front panel.md
        +
Libraries/UI.md
        +
IDE Program Model consumption
        +
execution-facing preservation / lowering / backend handoff
</code></pre>

<p>
without turning one private widget implementation into language law.
</p>

<p>
For the current repository campaign, this profile also defines the smallest portable widget-class family needed to support the first complete executable vertical slice that includes:
</p>

<ul>
  <li>one numeric control,</li>
  <li>one numeric indicator,</li>
  <li>natural <code>widget_value</code> participation,</li>
  <li>minimal object-style property access,</li>
  <li>and one optional SVG-based front-panel face template that remains non-semantic.</li>
</ul>

<hr/>

<h2 id="purpose">2. Purpose of this Profile</h2>

<p>
This profile is intended to support richer UI-object ecosystems than the minimal built-in baseline defined directly in the core widget model, while still remaining useful for the smallest serious executable corridor.
</p>

<p>
In particular, it exists so that:
</p>

<ul>
  <li>a widget class can be declared once through a durable portable contract,</li>
  <li>property nodes and method nodes can be generated and validated from class metadata rather than from ad hoc IDE rules,</li>
  <li>part addressing can be validated against the owning widget class,</li>
  <li>event surfaces can be named and typed in a portable way,</li>
  <li>design-time editors can expose class-aware authoring behavior without redefining source meaning,</li>
  <li>runtime-facing systems can consume an explicit class contract without depending on one editor-private reflection API,</li>
  <li>a portable presentation surface can be attached to a widget class without turning rendering metadata into executable semantics.</li>
</ul>

<p>
This profile does not attempt to define one universal GUI toolkit.
It defines the portable contract surface needed so that multiple toolchains can understand the same widget class family.
</p>

<hr/>

<h2 id="architectural-role">3. Architectural Role</h2>

<p>
Within the FROG repository architecture:
</p>

<pre><code>Expression/
  - canonical source representation of widget instances
  - class-side widget contract shape
  - diagram-side widget interaction shape
  - front-panel composition

Libraries/
  - intrinsic executable frog.ui interaction primitives

Language/
  - cross-cutting validated meaning

IR/
  - execution-facing representation, lowering, backend handoff

IDE/
  - Program Model, editors, palettes, guided authoring, inspection

Profiles/
  - optional standardized capability families
</code></pre>

<p>
This profile lives in <code>Profiles/</code> because it standardizes an optional capability family:
</p>

<ul>
  <li>portable widget-class catalogs,</li>
  <li>portable class contracts,</li>
  <li>tool-consumable event / property / method metadata,</li>
  <li>part-aware object surfaces,</li>
  <li>portable presentation-surface declarations,</li>
  <li>and profile-specific UI object ecosystems.</li>
</ul>

<p>
It does not replace the core widget model.
It extends what classes may be standardized and how tools may consume them.
</p>

<hr/>

<h2 id="scope">4. Scope</h2>

<p>
For FROG v0.1, this profile defines:
</p>

<ul>
  <li>the purpose and boundaries of a portable widget-class catalog,</li>
  <li>the required shape of a widget class contract,</li>
  <li>the required shape of property, method, event, and part contracts,</li>
  <li>the distinction between semantic value members and non-semantic presentation members,</li>
  <li>the distinction between design-time, source-persisted, runtime-readable, and runtime-writable members,</li>
  <li>the minimum information a conforming IDE needs to expose class-aware authoring,</li>
  <li>the minimum information a validator needs to check widget interaction against a class catalog,</li>
  <li>the minimum information that may flow into execution-facing systems without forcing one runtime-private representation,</li>
  <li>and the first minimal standardized widget-class family needed by the first executable UI-bearing vertical slice.</li>
</ul>

<hr/>

<h2 id="non-scope">5. What this Profile Does Not Define</h2>

<p>
This profile does not define:
</p>

<ul>
  <li>the canonical source serialization of widget instances beyond what <code>Expression/</code> already owns,</li>
  <li>the intrinsic primitive catalog of <code>frog.ui.*</code>,</li>
  <li>general diagram structure,</li>
  <li>one mandatory rendering engine,</li>
  <li>pixel-perfect cross-runtime UI equivalence,</li>
  <li>one mandatory event-loop implementation,</li>
  <li>one runtime-private object-handle representation,</li>
  <li>one mandatory backend payload syntax,</li>
  <li>one mandatory commercial widget toolkit,</li>
  <li>one mandatory SVG renderer or one mandatory skin-resource packaging format.</li>
</ul>

<p>
This profile also does not redefine:
</p>

<ul>
  <li>front-panel composition ownership,</li>
  <li>the authoritative executable graph,</li>
  <li>the generic backend handoff,</li>
  <li>one universal runtime-side widget ABI,</li>
  <li>or the semantic meaning of programs outside widget-class surface definition.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">6. Relation with Other Specifications</h2>

<p>
This profile must be read together with:
</p>

<ul>
  <li><code>Expression/Widget.md</code> for the source-level widget object model,</li>
  <li><code>Expression/Widget class contract.md</code> for the normative class-side contract model already present in canonical source architecture,</li>
  <li><code>Expression/Front panel.md</code> for widget instance declaration and composition,</li>
  <li><code>Expression/Widget interaction.md</code> for canonical source-facing property-read, property-write, and method-invoke representation,</li>
  <li><code>Libraries/UI.md</code> for the intrinsic executable <code>frog.ui.*</code> primitive contracts,</li>
  <li><code>IDE/Readme.md</code> for Program Model ownership and IDE consumption boundaries,</li>
  <li><code>IR/</code> for execution-facing preservation, lowering posture, and backend handoff.</li>
</ul>

<p>
The key architectural rule is:
</p>

<pre><code>widget instance declaration
    !=
widget class contract

widget class contract
    !=
frog.ui primitive contract

widget class contract
    !=
runtime-private widget implementation

widget class contract
    !=
one IDE's private authoring model

presentation template
    !=
widget semantic identity

presentation template
    !=
widget value model
</code></pre>

<p>
This profile therefore standardizes one optional catalog and capability surface around those existing boundaries.
It does not erase them.
</p>

<hr/>

<h2 id="why-this-belongs-in-profiles">7. Why this Belongs in <code>Profiles/</code></h2>

<p>
The minimal standard widget vocabulary belongs in the core widget model because FROG needs a small common baseline.
</p>

<p>
A richer widget ecosystem does not belong in the minimal mandatory core because:
</p>

<ul>
  <li>different execution environments may support different UI capability families,</li>
  <li>different IDEs may surface different authoring ergonomics,</li>
  <li>different runtimes may support different event, theme, and host-bridge capabilities,</li>
  <li>third-party class families should be standardizable without redefining the whole language core,</li>
  <li>presentation systems may vary substantially even when class contracts remain portable.</li>
</ul>

<p>
Accordingly, richer widget-class families and their portable class-catalog rules are profile-owned.
</p>

<p>
This document also uses that profile-owned space to publish the smallest executable widget family needed by the first end-to-end UI-bearing vertical slice, while still keeping that family outside the irreducible language core.
</p>

<hr/>

<h2 id="core-model">8. Core Model</h2>

<p>
A widget class contract is a standardized declaration that describes what a widget class exposes and how tools may consume that class.
</p>

<p>
A class contract MUST define enough information for all of the following:
</p>

<ul>
  <li>source validation of widget instances,</li>
  <li>source validation of widget interaction nodes,</li>
  <li>IDE palette and inspector population,</li>
  <li>IDE property-node and method-node generation,</li>
  <li>part-aware addressing validation,</li>
  <li>type-safe executable interaction,</li>
  <li>execution-facing preservation, lowering, and backend handoff preparation.</li>
</ul>

<p>
A class contract MAY be provided by:
</p>

<ul>
  <li>this profile itself,</li>
  <li>another published compatible profile,</li>
  <li>or an external standardized class-family package recognized by a conforming implementation.</li>
</ul>

<p>
However, whenever a tool claims conformance to this profile, the class contract MUST remain inspectable and machine-consumable in an open form.
</p>

<p>
The core rule for this profile is:
</p>

<pre><code>primary value contract
    !=
object-style property contract
    !=
presentation template contract
</code></pre>

<p>
A value-carrying widget class therefore has at least three potentially distinct surfaces:
</p>

<ul>
  <li>its primary value surface, typically consumed through <code>widget_value</code>,</li>
  <li>its object-style member surface, consumed through <code>widget_reference</code> and <code>frog.ui.*</code> interaction primitives,</li>
  <li>its optional presentation-template surface, consumed by design-time tools or runtime-capable hosts without changing executable semantics.</li>
</ul>

<hr/>

<h2 id="widget-class-contract">9. Widget Class Contract</h2>

<p>
A widget class contract MUST define at least the following fields conceptually:
</p>

<ul>
  <li><strong>class_id</strong> — stable fully qualified class identifier,</li>
  <li><strong>version</strong> — class-contract version,</li>
  <li><strong>display_name</strong> — human-readable class name,</li>
  <li><strong>description</strong> — concise class purpose,</li>
  <li><strong>allowed_roles</strong> — valid widget roles for the class,</li>
  <li><strong>value_model</strong> — whether the class carries a primary value, under what type constraints, and through which primary member,</li>
  <li><strong>container_capability</strong> — whether the class may own child widgets,</li>
  <li><strong>parts</strong> — declared part contracts,</li>
  <li><strong>properties</strong> — declared property contracts,</li>
  <li><strong>methods</strong> — declared method contracts,</li>
  <li><strong>events</strong> — declared event contracts,</li>
  <li><strong>capabilities</strong> — optional host / UI capability requirements,</li>
  <li><strong>design_time_rules</strong> — authoring-side availability and editing constraints,</li>
  <li><strong>runtime_rules</strong> — execution-facing applicability constraints,</li>
  <li><strong>presentation_rules</strong> — optional rules governing non-semantic presentation members and templates.</li>
</ul>

<p>
A class contract SHOULD also define:
</p>

<ul>
  <li>default layout hints,</li>
  <li>common inspector grouping metadata,</li>
  <li>default property values where meaningful,</li>
  <li>part inheritance or reuse rules where applicable,</li>
  <li>deprecation markers for members that remain recognized for compatibility.</li>
</ul>

<p>
A class contract MUST NOT require one IDE-private binary metadata format in order to be understood.
</p>

<p>
A class contract MUST keep the following distinctions explicit where relevant:
</p>

<ul>
  <li>primary value member vs ordinary property member,</li>
  <li>semantic member vs non-semantic presentation member,</li>
  <li>source-persisted member vs runtime-transient member,</li>
  <li>class-owned member vs part-owned member.</li>
</ul>

<hr/>

<h2 id="property-contract">10. Property Contract</h2>

<p>
Each declared property MUST expose a portable property contract.
</p>

<p>
A property contract MUST define at least:
</p>

<ul>
  <li><strong>name</strong>,</li>
  <li><strong>value_type</strong>,</li>
  <li><strong>access</strong> — <code>read_only</code>, <code>write_only</code>, or <code>read_write</code>,</li>
  <li><strong>owner</strong> — class-level member or part-level member,</li>
  <li><strong>semantic_role</strong> — primary_value, semantic_property, presentation_property, or profile-defined equivalent,</li>
  <li><strong>design_time_visibility</strong>,</li>
  <li><strong>runtime_visibility</strong>,</li>
  <li><strong>source_persisted</strong> — whether it may appear in canonical source,</li>
  <li><strong>runtime_observable</strong> — whether it may be read at runtime,</li>
  <li><strong>runtime_mutable</strong> — whether it may be written at runtime,</li>
  <li><strong>default_value</strong> when meaningful and statically expressible.</li>
</ul>

<p>
A property contract MAY also define:
</p>

<ul>
  <li>validation ranges,</li>
  <li>enumerated allowed values,</li>
  <li>editor grouping,</li>
  <li>reset behavior,</li>
  <li>whether writes are immediate, deferred, or host-scheduled,</li>
  <li>whether changes may emit one or more named events,</li>
  <li>whether the property is host-ignored when unsupported.</li>
</ul>

<p>
Property contracts MUST be sufficient for:
</p>

<ul>
  <li>property-inspector population,</li>
  <li>property-node generation,</li>
  <li>read/write validation,</li>
  <li>type checking of <code>frog.ui.property_read</code> and <code>frog.ui.property_write</code>,</li>
  <li>execution-facing member resolution,</li>
  <li>and separation of semantic state from presentation-only metadata.</li>
</ul>

<p>
A property declared as a non-semantic presentation property MUST NOT change:
</p>

<ul>
  <li>the widget role contract,</li>
  <li>the primary value type contract,</li>
  <li>the executable meaning of the program,</li>
  <li>or the validity of the surrounding dataflow graph.</li>
</ul>

<hr/>

<h2 id="method-contract">11. Method Contract</h2>

<p>
Each declared method MUST expose a portable method contract.
</p>

<p>
A method contract MUST define at least:
</p>

<ul>
  <li><strong>name</strong>,</li>
  <li><strong>owner</strong> — class-level member or part-level member,</li>
  <li><strong>parameters</strong> — ordered parameter list with names, types, and direction,</li>
  <li><strong>results</strong> — ordered result list with names and types,</li>
  <li><strong>sequencing_kind</strong> — whether explicit <code>ui_in</code>/<code>ui_out</code> sequencing is required, optional, or meaningless,</li>
  <li><strong>runtime_visibility</strong>,</li>
  <li><strong>side_effect_kind</strong> — none, state mutation, host action, visual action, or mixed,</li>
  <li><strong>availability_constraints</strong> where host or role restrictions apply.</li>
</ul>

<p>
A method contract MAY also define:
</p>

<ul>
  <li>idempotence hints,</li>
  <li>failure categories,</li>
  <li>whether invocation may emit one or more named events,</li>
  <li>whether invocation requires the widget to be attached to a live host surface,</li>
  <li>whether invocation is design-time only, runtime only, or both.</li>
</ul>

<p>
Method contracts MUST be sufficient for:
</p>

<ul>
  <li>method-node generation,</li>
  <li>diagram typing,</li>
  <li>execution-facing lowering,</li>
  <li>backend handoff member resolution.</li>
</ul>

<hr/>

<h2 id="event-contract">12. Event Contract</h2>

<p>
This profile recognizes events as named runtime-originated interaction surfaces of widget classes and widget parts.
</p>

<p>
For v0.1, event contracts are standardized as class-catalog declarations even though full first-class executable event-structure semantics may remain profile-bounded or future-extended.
</p>

<p>
An event contract MUST define at least:
</p>

<ul>
  <li><strong>name</strong>,</li>
  <li><strong>owner</strong> — class-level member or part-level member,</li>
  <li><strong>payload</strong> — ordered named fields with FROG types,</li>
  <li><strong>trigger_kind</strong> — user action, value change, focus change, lifecycle, host signal, or profile-defined category,</li>
  <li><strong>delivery_constraints</strong> — synchronous observation, queued observation, or profile-defined delivery posture,</li>
  <li><strong>availability_constraints</strong>.</li>
</ul>

<p>
An event contract MAY also define:
</p>

<ul>
  <li>coalescing hints,</li>
  <li>whether repeated changes may be merged,</li>
  <li>whether the event is design-time visible, runtime visible, or both,</li>
  <li>whether the event is generated only by user action, only by programmatic mutation, or by both.</li>
</ul>

<p>
For v0.1, the presence of an event contract does not by itself require one mandatory event-loop execution structure in the language core.
</p>

<hr/>

<h2 id="part-contract">13. Part Contract</h2>

<p>
A widget part contract standardizes named sub-objects of a widget class that may expose their own properties, methods, and events.
</p>

<p>
A part contract MUST define at least:
</p>

<ul>
  <li><strong>part_name</strong>,</li>
  <li><strong>part_class</strong> or equivalent part category,</li>
  <li><strong>required</strong> or optional status,</li>
  <li><strong>multiplicity</strong> — single or collection-like when supported,</li>
  <li><strong>own_properties</strong>,</li>
  <li><strong>own_methods</strong>,</li>
  <li><strong>own_events</strong>,</li>
  <li><strong>addressability</strong> — whether diagram-side object access is allowed to target the part directly.</li>
</ul>

<p>
Part contracts MUST be sufficient to validate source paths such as:
</p>

<pre><code>widget.part
widget.part.property
widget.part.method
widget.part.event
</code></pre>

<p>
A part MUST NOT exist independently from its owning widget instance in canonical meaning.
</p>

<p>
When a widget class supports presentation templates, parts MAY be used as the portable named anchoring surface between:
</p>

<ul>
  <li>the class contract,</li>
  <li>design-time face-template authoring,</li>
  <li>and host-side presentation binding.</li>
</ul>

<p>
However, a presentation-facing part contract MUST NOT by itself create executable semantics.
</p>

<hr/>

<h2 id="design-time-vs-runtime">14. Design-Time vs Runtime Distinction</h2>

<p>
A conforming class contract MUST keep design-time and runtime distinctions explicit.
</p>

<p>
At minimum, class members SHOULD distinguish:
</p>

<ul>
  <li><strong>source-persisted configuration</strong> — canonical source-relevant values,</li>
  <li><strong>design-time-only metadata</strong> — editor-facing configuration not required for executable meaning,</li>
  <li><strong>runtime-readable state</strong> — state that may be read through object-style interaction,</li>
  <li><strong>runtime-writable state</strong> — state that may be mutated through object-style interaction,</li>
  <li><strong>runtime-transient state</strong> — host-private or ephemeral state that is not canonical source and not required to be portable.</li>
</ul>

<p>
The key rule is:
</p>

<pre><code>source-persisted
    !=
runtime-observable

design-time-visible
    !=
runtime-readable

editor-private convenience
    !=
portable class contract

presentation metadata
    !=
executable semantics
</code></pre>

<p>
If a class supports a presentation template reference such as an SVG-based face template, that member SHOULD normally be classified as:
</p>

<ul>
  <li>source-persisted,</li>
  <li>design-time-visible,</li>
  <li>non-semantic,</li>
  <li>and host-optional at runtime.</li>
</ul>

<hr/>

<h2 id="program-model-and-ide-consumption">15. Program Model and IDE Consumption</h2>

<p>
A conforming IDE MAY use widget class contracts to provide:
</p>

<ul>
  <li>palette entries for widget insertion,</li>
  <li>property inspectors,</li>
  <li>method pickers,</li>
  <li>event pickers,</li>
  <li>part-aware navigation,</li>
  <li>typed generation of property-read, property-write, and method-invoke nodes,</li>
  <li>context-aware validation while editing,</li>
  <li>presentation-template-aware designer tooling.</li>
</ul>

<p>
However, the IDE MUST NOT treat its own private Program Model as the normative owner of the class contract.
</p>

<p>
The portable class catalog remains external to one IDE-private object model even when the IDE caches, augments, or indexes it internally for authoring.
</p>

<p>
An IDE SHOULD be able to regenerate a property node or method node directly from the published class contract without requiring hidden reflection metadata.
</p>

<p>
An IDE MAY also use:
</p>

<ul>
  <li>presentation parts,</li>
  <li>presentation properties,</li>
  <li>and template references</li>
</ul>

<p>
to support visual editing or previewing of the front panel, but such support MUST NOT redefine executable meaning.
</p>

<hr/>

<h2 id="interaction-node-consumption">16. Interaction-Node Consumption</h2>

<p>
When validating object-style widget interaction:
</p>

<ul>
  <li><code>frog.ui.property_read</code> MUST resolve the addressed member against the active widget class contract,</li>
  <li><code>frog.ui.property_write</code> MUST resolve the addressed member against the active widget class contract,</li>
  <li><code>frog.ui.method_invoke</code> MUST resolve the addressed member against the active widget class contract.</li>
</ul>

<p>
Accordingly, the class contract MUST provide enough information to determine:
</p>

<ul>
  <li>whether the member exists,</li>
  <li>whether the member belongs to the widget itself or to a named part,</li>
  <li>whether the member is readable, writable, or invokable,</li>
  <li>the member type or signature,</li>
  <li>whether explicit sequencing is required or allowed,</li>
  <li>whether access is valid under the active profile and host-capability set.</li>
</ul>

<p>
This profile therefore strengthens resolution and validation of object-style interaction without moving ownership of the interaction primitives out of <code>Libraries/UI.md</code>.
</p>

<p>
The intended default rule for value-carrying widgets remains:
</p>

<pre><code>natural value participation
    -&gt; widget_value

object-style property or method interaction
    -&gt; widget_reference + frog.ui.property_* / frog.ui.method_invoke
</code></pre>

<p>
Accordingly, even if a primary value member is also declared as a property, a class SHOULD still document which interaction path is:
</p>

<ul>
  <li>the natural value path,</li>
  <li>the object-style path,</li>
  <li>and any restrictions on mixing them.</li>
</ul>

<hr/>

<h2 id="execution-facing-posture">17. Execution-Facing Posture</h2>

<p>
This profile does not require one mandatory runtime-private object representation.
</p>

<p>
Instead, it requires that execution-facing systems be able to consume a stable class contract and derive at least:
</p>

<ul>
  <li>resolved member identity,</li>
  <li>type-correct property access,</li>
  <li>type-correct method invocation,</li>
  <li>declared event payload shape,</li>
  <li>member-level applicability constraints,</li>
  <li>and the distinction between semantic members and presentation-only members.</li>
</ul>

<p>
A lowering pipeline MAY map this information to:
</p>

<ul>
  <li>native UI host calls,</li>
  <li>retained-mode toolkit bindings,</li>
  <li>immediate-mode toolkit bridges,</li>
  <li>remote UI adapters,</li>
  <li>headless testing shims,</li>
  <li>backend-family-specific UI contracts.</li>
</ul>

<p>
Those mappings remain downstream from the class catalog itself.
</p>

<p>
This profile therefore standardizes enough class-side truth for preservation, lowering preparation, and backend handoff preparation, without pretending to standardize one private widget runtime.
</p>

<p>
Where a class supports a presentation template reference, lowering and backend handoff MAY preserve that reference as host-consumable presentation metadata.
However:
</p>

<ul>
  <li>the reference MAY be ignored by a host that does not support that presentation family,</li>
  <li>a host MAY substitute a standard rendering of the same class,</li>
  <li>and such fallback MUST NOT change the program's executable meaning.</li>
</ul>

<hr/>

<h2 id="profile-identification-and-claims">18. Profile Identification and Claims</h2>

<p>
An implementation claiming support for this profile MUST state:
</p>

<ul>
  <li>which widget class families it supports,</li>
  <li>which version of each class family it supports,</li>
  <li>whether it supports property reads, property writes, methods, and events for those classes,</li>
  <li>whether support is design-time only, runtime only, or both,</li>
  <li>which host-capability restrictions apply,</li>
  <li>whether presentation-template members are supported, ignored, or partially supported.</li>
</ul>

<p>
An implementation MUST NOT claim generic support for this profile while only supporting one editor-private undocumented class surface.
</p>

<hr/>

<h2 id="minimal-executable-widget-family">19. Minimal Executable Widget Family for the First Vertical Slice</h2>

<p>
For v0.1, this document defines not only the profile boundary and generic class-contract shape, but also the smallest standardized widget family needed by the first executable UI-bearing vertical slice.
</p>

<p>
That minimal family is intentionally conservative.
Its purpose is not to standardize a broad industrial widget catalog first.
Its purpose is to support one small but complete corridor that can go from canonical <code>.frog</code> source to validation, Execution IR, lowering, backend handoff, and first runtime execution while carrying:
</p>

<ul>
  <li>one numeric control,</li>
  <li>one numeric indicator,</li>
  <li>one primary numeric value path,</li>
  <li>one minimal object-style presentation property path,</li>
  <li>and one optional face template for front-panel rendering.</li>
</ul>

<h3>19.1 Standard Classes</h3>

<p>
The following classes are standardized by this document for that first minimal family:
</p>

<ul>
  <li><code>frog.ui.standard.numeric_control</code>,</li>
  <li><code>frog.ui.standard.numeric_indicator</code>.</li>
</ul>

<p>
These classes define the minimum portable surface needed by the first vertical slice.
Richer standardized classes MAY be added later under this same profile or under compatible extensions.
</p>

<h3>19.2 Numeric Control Contract</h3>

<p>
The conceptual contract of <code>frog.ui.standard.numeric_control</code> is:
</p>

<pre><code>{
  "class_id": "frog.ui.standard.numeric_control",
  "version": "0.1",
  "display_name": "Numeric Control",
  "description": "Minimal value-carrying numeric front-panel control for the first executable UI slice.",
  "allowed_roles": ["control"],
  "value_model": {
    "kind": "value_carrying",
    "primary_member": "value",
    "type_constraints": ["u16"]
  },
  "container_capability": false,
  "parts": [
    {
      "part_name": "face",
      "part_class": "frog.ui.standard.numeric_control.face",
      "required": true,
      "multiplicity": "single",
      "addressability": "direct"
    },
    {
      "part_name": "caption",
      "part_class": "frog.ui.standard.numeric_control.caption",
      "required": false,
      "multiplicity": "single",
      "addressability": "direct"
    },
    {
      "part_name": "value_window",
      "part_class": "frog.ui.standard.numeric_control.value_window",
      "required": false,
      "multiplicity": "single",
      "addressability": "direct"
    }
  ],
  "properties": [
    {
      "name": "value",
      "value_type": "u16",
      "access": "read_write",
      "owner": "class",
      "semantic_role": "primary_value",
      "design_time_visibility": true,
      "runtime_visibility": true,
      "source_persisted": true,
      "runtime_observable": true,
      "runtime_mutable": true,
      "default_value": 0
    },
    {
      "name": "face_color",
      "value_type": "frog.ui.color",
      "access": "read_write",
      "owner": "class",
      "semantic_role": "presentation_property",
      "design_time_visibility": true,
      "runtime_visibility": true,
      "source_persisted": true,
      "runtime_observable": true,
      "runtime_mutable": true
    },
    {
      "name": "face_template",
      "value_type": "frog.ui.svg_template_ref",
      "access": "read_write",
      "owner": "class",
      "semantic_role": "presentation_property",
      "design_time_visibility": true,
      "runtime_visibility": false,
      "source_persisted": true,
      "runtime_observable": false,
      "runtime_mutable": false
    }
  ],
  "methods": [],
  "events": [],
  "capabilities": [],
  "design_time_rules": {
    "palette_visible": true,
    "designer_surface_supported": true
  },
  "runtime_rules": {
    "widget_value_supported": true,
    "widget_reference_supported": true
  },
  "presentation_rules": {
    "face_template_kind": "svg",
    "face_template_optional": true,
    "template_is_non_semantic": true,
    "host_may_fallback_to_standard_rendering": true
  }
}</code></pre>

<h3>19.3 Numeric Indicator Contract</h3>

<p>
The conceptual contract of <code>frog.ui.standard.numeric_indicator</code> is:
</p>

<pre><code>{
  "class_id": "frog.ui.standard.numeric_indicator",
  "version": "0.1",
  "display_name": "Numeric Indicator",
  "description": "Minimal value-carrying numeric front-panel indicator for the first executable UI slice.",
  "allowed_roles": ["indicator"],
  "value_model": {
    "kind": "value_carrying",
    "primary_member": "value",
    "type_constraints": ["u16"]
  },
  "container_capability": false,
  "parts": [
    {
      "part_name": "face",
      "part_class": "frog.ui.standard.numeric_indicator.face",
      "required": true,
      "multiplicity": "single",
      "addressability": "direct"
    },
    {
      "part_name": "caption",
      "part_class": "frog.ui.standard.numeric_indicator.caption",
      "required": false,
      "multiplicity": "single",
      "addressability": "direct"
    },
    {
      "part_name": "value_window",
      "part_class": "frog.ui.standard.numeric_indicator.value_window",
      "required": false,
      "multiplicity": "single",
      "addressability": "direct"
    }
  ],
  "properties": [
    {
      "name": "value",
      "value_type": "u16",
      "access": "read_write",
      "owner": "class",
      "semantic_role": "primary_value",
      "design_time_visibility": true,
      "runtime_visibility": true,
      "source_persisted": true,
      "runtime_observable": true,
      "runtime_mutable": true,
      "default_value": 0
    },
    {
      "name": "face_color",
      "value_type": "frog.ui.color",
      "access": "read_write",
      "owner": "class",
      "semantic_role": "presentation_property",
      "design_time_visibility": true,
      "runtime_visibility": true,
      "source_persisted": true,
      "runtime_observable": true,
      "runtime_mutable": true
    },
    {
      "name": "face_template",
      "value_type": "frog.ui.svg_template_ref",
      "access": "read_write",
      "owner": "class",
      "semantic_role": "presentation_property",
      "design_time_visibility": true,
      "runtime_visibility": false,
      "source_persisted": true,
      "runtime_observable": false,
      "runtime_mutable": false
    }
  ],
  "methods": [],
  "events": [],
  "capabilities": [],
  "design_time_rules": {
    "palette_visible": true,
    "designer_surface_supported": true
  },
  "runtime_rules": {
    "widget_value_supported": true,
    "widget_reference_supported": true
  },
  "presentation_rules": {
    "face_template_kind": "svg",
    "face_template_optional": true,
    "template_is_non_semantic": true,
    "host_may_fallback_to_standard_rendering": true
  }
}</code></pre>

<h3>19.4 Required Semantic Distinction for the Minimal Family</h3>

<p>
For the minimal family standardized here:
</p>

<ul>
  <li><code>value</code> is the primary value member,</li>
  <li><code>face_color</code> is a non-semantic presentation property,</li>
  <li><code>face_template</code> is a non-semantic presentation-template reference.</li>
</ul>

<p>
Accordingly:
</p>

<pre><code>value
    !=
face_color
    !=
face_template
</code></pre>

<p>
Changing <code>face_color</code> or <code>face_template</code> MUST NOT:
</p>

<ul>
  <li>change the widget role,</li>
  <li>change the widget type constraints,</li>
  <li>change the primary value contract,</li>
  <li>change the executable meaning of the program.</li>
</ul>

<h3>19.5 SVG Face Template Boundary</h3>

<p>
This profile allows the minimal family to reference an SVG-based face template through <code>face_template</code>.
</p>

<p>
That template reference MUST be treated as:
</p>

<ul>
  <li>source-persisted,</li>
  <li>design-time-visible,</li>
  <li>presentation-only,</li>
  <li>non-semantic,</li>
  <li>and host-optional at runtime.</li>
</ul>

<p>
An SVG face template MAY provide:
</p>

<ul>
  <li>a previewable front-panel face,</li>
  <li>a visual skin for a compatible host,</li>
  <li>part anchoring for named presentation parts such as <code>face</code>, <code>caption</code>, or <code>value_window</code>.</li>
</ul>

<p>
An SVG face template MUST NOT:
</p>

<ul>
  <li>redefine the widget class identity,</li>
  <li>redefine the primary value type,</li>
  <li>introduce executable behavior,</li>
  <li>introduce hidden methods or events,</li>
  <li>or become the normative owner of widget semantics.</li>
</ul>

<p>
A host that does not support SVG face templates MAY ignore <code>face_template</code> and render the same widget class through a standard fallback surface.
Such fallback MUST preserve the widget class contract and the program's executable meaning.
</p>

<h3>19.6 Design Tokens and Presentation Properties</h3>

<p>
For the minimal family, <code>face_color</code> acts as the first standardized presentation token.
Later compatible extensions MAY add additional presentation tokens such as:
</p>

<ul>
  <li><code>border_color</code>,</li>
  <li><code>text_color</code>,</li>
  <li><code>accent_color</code>.</li>
</ul>

<p>
Those later additions MUST remain presentation-only unless another specification explicitly states otherwise.
</p>

<h3>19.7 Why this Minimal Family Exists</h3>

<p>
This minimal family exists so that the first executable vertical slice can carry:
</p>

<ul>
  <li>a real numeric control,</li>
  <li>a real numeric indicator,</li>
  <li>a natural value path via <code>widget_value</code>,</li>
  <li>a minimal object-style property path via <code>widget_reference</code> and <code>frog.ui.property_write</code>,</li>
  <li>and one serious but bounded front-panel presentation story.</li>
</ul>

<p>
It is intentionally small.
It is not intended to standardize the full future UI ecosystem in v0.1.
</p>

<hr/>

<h2 id="validation-rules">20. Validation Rules</h2>

<p>
For a program to be valid under this profile:
</p>

<ul>
  <li>every widget instance using a profile-owned class MUST reference a recognized class identifier,</li>
  <li>every addressed property MUST exist in the resolved class or part contract,</li>
  <li>every property read MUST target a readable member,</li>
  <li>every property write MUST target a writable member,</li>
  <li>every method invocation MUST target an invokable member,</li>
  <li>every supplied argument MUST match the declared parameter type,</li>
  <li>every expected result MUST match the declared result type,</li>
  <li>every part name MUST be valid for the owning class,</li>
  <li>every event reference MUST target a declared event surface when event-aware interaction is used by a future compatible mechanism,</li>
  <li>design-time-only members MUST NOT be treated as runtime-valid executable interaction surfaces.</li>
</ul>

<p>
A validator SHOULD also reject contradictory contracts such as:
</p>

<ul>
  <li>a property declared both non-runtime-visible and runtime-readable,</li>
  <li>a method declared invokable but with no parameter / result contract,</li>
  <li>a part declared addressable but exposing no member surface definition,</li>
  <li>an event declared with payload fields lacking FROG type definitions,</li>
  <li>a presentation-only property declared as executable semantic state,</li>
  <li>a template reference declared as changing value-model meaning.</li>
</ul>

<p>
For the minimal executable widget family defined in this document, a validator MUST also confirm at least:
</p>

<ul>
  <li>that <code>frog.ui.standard.numeric_control</code> and <code>frog.ui.standard.numeric_indicator</code> are used only with their allowed roles,</li>
  <li>that their primary value type is <code>u16</code>,</li>
  <li>that <code>face_color</code> writes use a value compatible with <code>frog.ui.color</code>,</li>
  <li>that <code>face_template</code>, when present, is treated as non-semantic presentation metadata,</li>
  <li>that natural value participation uses <code>widget_value</code> rather than requiring object-style property access for ordinary dataflow.</li>
</ul>

<hr/>

<h2 id="examples">21. Examples</h2>

<h3>21.1 Minimal Numeric Control Class Contract</h3>

<pre><code>{
  "class_id": "frog.ui.standard.numeric_control",
  "version": "0.1",
  "display_name": "Numeric Control",
  "allowed_roles": ["control"],
  "value_model": {
    "kind": "value_carrying",
    "primary_member": "value",
    "type_constraints": ["u16"]
  },
  "properties": [
    {
      "name": "value",
      "value_type": "u16",
      "access": "read_write",
      "semantic_role": "primary_value",
      "source_persisted": true,
      "runtime_observable": true,
      "runtime_mutable": true
    },
    {
      "name": "face_color",
      "value_type": "frog.ui.color",
      "access": "read_write",
      "semantic_role": "presentation_property",
      "source_persisted": true,
      "runtime_observable": true,
      "runtime_mutable": true
    },
    {
      "name": "face_template",
      "value_type": "frog.ui.svg_template_ref",
      "access": "read_write",
      "semantic_role": "presentation_property",
      "source_persisted": true,
      "runtime_observable": false,
      "runtime_mutable": false
    }
  ]
}</code></pre>

<h3>21.2 Natural Value Participation Example</h3>

<pre><code>widget_value(ctrl_count)
    -&gt; u16
</code></pre>

<p>
This is the natural value path of the widget class.
It is the preferred path for ordinary dataflow participation.
</p>

<h3>21.3 Presentation Property Write Example</h3>

<pre><code>widget_reference(ctrl_count)
    -&gt; frog.ui.property_write {
         "member": "face_color"
       }
</code></pre>

<p>
This is valid only if the active class contract declares <code>face_color</code> as writable and class-owned.
</p>

<h3>21.4 Face Template Source Example</h3>

<pre><code>{
  "id": "ctrl_count",
  "role": "control",
  "widget": "frog.ui.standard.numeric_control",
  "value_type": "u16",
  "props": {
    "caption": "Count",
    "face_color": "#D0D0D0",
    "face_template": {
      "kind": "resource",
      "path": "./assets/widgets/u16_numeric_control_face.svg"
    }
  }
}</code></pre>

<p>
The presence of <code>face_template</code> does not change the executable meaning of the widget instance.
It only contributes presentation metadata for design-time tools or compatible hosts.
</p>

<h3>21.5 Part-Aware Presentation Anchoring Example</h3>

<pre><code>{
  "class_id": "frog.ui.standard.numeric_indicator",
  "parts": [
    {
      "part_name": "face",
      "part_class": "frog.ui.standard.numeric_indicator.face",
      "required": true,
      "addressability": "direct"
    },
    {
      "part_name": "value_window",
      "part_class": "frog.ui.standard.numeric_indicator.value_window",
      "required": false,
      "addressability": "direct"
    }
  ]
}</code></pre>

<p>
A compatible designer or host MAY use those named parts as a stable anchoring surface between the class contract and an SVG face template.
That anchoring remains presentation-facing only unless another specification states otherwise.
</p>

<hr/>

<h2 id="out-of-scope-for-v01">22. Out of Scope for v0.1</h2>

<ul>
  <li>a universal industrial widget catalog,</li>
  <li>pixel-perfect rendering equivalence across hosts,</li>
  <li>mandatory cross-platform theme fidelity,</li>
  <li>a mandatory first-class language-level event-structure execution model,</li>
  <li>one universal accessibility contract for every future host family,</li>
  <li>one mandatory serialization syntax for external class-catalog packages,</li>
  <li>one mandatory runtime-private widget-handle ABI,</li>
  <li>a large rich-widget family such as tables, graphs, trees, or industrial panels,</li>
  <li>a mandatory event-heavy designer surface,</li>
  <li>one universal SVG authoring package format.</li>
</ul>

<hr/>

<h2 id="summary">23. Summary</h2>

<p>
This profile defines the missing portable layer between source-declared widget instances and portable executable widget-object ecosystems.
</p>

<p>
In this architecture:
</p>

<ul>
  <li><code>Expression/</code> continues to own canonical widget-instance source,</li>
  <li><code>Expression/Widget class contract.md</code> continues to own the normative class-side contract model in the core source architecture,</li>
  <li><code>Libraries/UI.md</code> continues to own intrinsic <code>frog.ui.*</code> executable primitive identities,</li>
  <li><code>IDE/</code> continues to own Program Model and authoring behavior,</li>
  <li><code>IR/</code> continues to own execution-facing preservation and lowering,</li>
  <li>this profile owns the optional standardized widget-class catalog and class-contract surface for richer UI object families and for the first minimal executable UI-bearing widget family.</li>
</ul>

<p>
That separation makes it possible to support:
</p>

<ul>
  <li>portable widget class families,</li>
  <li>typed property and method node generation,</li>
  <li>part-aware validation,</li>
  <li>future event-surface standardization,</li>
  <li>presentation metadata without semantic confusion,</li>
  <li>and backend-facing handoff without one IDE-private reflection model becoming normative truth.</li>
</ul>
