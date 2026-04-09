<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG UI Library</h1>

<p align="center">
  <strong>Normative specification of the intrinsic <code>frog.ui</code> primitive library for object-style and event-oriented widget interaction</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-document-exists">2. Why This Document Exists</a></li>
  <li><a href="#design-goals">3. Design Goals</a></li>
  <li><a href="#architectural-position">4. Architectural Position</a></li>
  <li><a href="#scope">5. Scope</a></li>
  <li><a href="#relation-with-other-specifications">6. Relation with Other Specifications</a></li>
  <li><a href="#namespace">7. Namespace</a></li>
  <li><a href="#standard-primitives">8. Standard Primitives</a></li>
  <li><a href="#froguiproperty_read">9. <code>frog.ui.property_read</code></a></li>
  <li><a href="#froguiproperty_write">10. <code>frog.ui.property_write</code></a></li>
  <li><a href="#froguimethod_invoke">11. <code>frog.ui.method_invoke</code></a></li>
  <li><a href="#froguievent_observe">12. <code>frog.ui.event_observe</code></a></li>
  <li><a href="#typing-and-sequencing">13. Typing and Sequencing</a></li>
  <li><a href="#validation-rules">14. Validation Rules</a></li>
  <li><a href="#execution-facing-posture">15. Execution-Facing Posture</a></li>
  <li><a href="#examples">16. Examples</a></li>
  <li><a href="#out-of-scope">17. Out of Scope</a></li>
  <li><a href="#summary">18. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the intrinsic <code>frog.ui</code> primitive library.
</p>

<p>
The <code>frog.ui</code> library standardizes the executable primitive vocabulary used for object-style
and event-oriented widget interaction in diagrams.
These primitives operate on widget objects exposed through <code>widget_reference</code> participation
and provide a stable, implementation-independent interaction surface for property access,
method invocation, and event observation.
</p>

<p>
FROG intentionally separates:
</p>

<ul>
  <li>natural primary widget-value participation,</li>
  <li>object-style widget interaction,</li>
  <li>event-oriented widget observation,</li>
  <li>widget class law,</li>
  <li>widget-oriented package content,</li>
  <li>host-side widget realization.</li>
</ul>

<p>
Accordingly:
</p>

<pre><code>widget_value
    -&gt; natural primary-value path

widget_reference
    -&gt; object-style and event-oriented widget access path

frog.ui.*
    -&gt; intrinsic executable primitive vocabulary
       for object-style and event-oriented widget interaction
</code></pre>

<p>
This document defines the intrinsic primitive catalog for that interaction layer.
It does not define the widget class catalog, front-panel serialization, widget realization packages,
general diagram graph structure, open execution-facing representations, lowering families,
backend contracts, or runtime-private widget-handle architectures.
</p>

<hr/>

<h2 id="why-this-document-exists">2. Why This Document Exists</h2>

<p>
A widget system needs more than widget declarations and class contracts.
It also needs a stable executable vocabulary for interacting with widgets as objects and as event sources inside diagrams.
</p>

<p>
Without such a library, widget interaction tends to collapse into:
</p>

<ul>
  <li>runtime-private conventions,</li>
  <li>editor-private shortcuts,</li>
  <li>backend-specific helper nodes,</li>
  <li>or implicit rewrites that are difficult to validate and difficult to preserve across runtimes.</li>
</ul>

<p>
This document therefore gives <code>frog.ui</code> a narrow but explicit role:
</p>

<ul>
  <li>provide stable primitive identities,</li>
  <li>define primitive-local contracts,</li>
  <li>preserve the distinction between natural value participation and object-style interaction,</li>
  <li>preserve the distinction between property access, method invocation, and event observation,</li>
  <li>allow several runtimes to recognize the same UI-interaction intent without turning one runtime implementation into the definition of the language.</li>
</ul>

<p>
The goal is not to make <code>frog.ui</code> the owner of the whole widget architecture.
The goal is to give the widget interaction corridor a standardized executable primitive surface that remains stable across authoring tools, validators, execution-facing representations, and runtimes.
</p>

<hr/>

<h2 id="design-goals">3. Design Goals</h2>

<ul>
  <li><strong>Clarity</strong> — define a small, explicit, stable primitive vocabulary for object-style and event-oriented UI interaction.</li>
  <li><strong>Architectural discipline</strong> — keep executable UI primitives distinct from widget instance declarations, widget class law, front-panel source, widget-package ownership, IR ownership, and host realization.</li>
  <li><strong>Portability</strong> — provide primitive identities and primitive-local contracts that can be recognized across multiple conforming runtimes.</li>
  <li><strong>Recoverability</strong> — preserve the semantic distinction between natural <code>widget_value</code> participation and <code>widget_reference</code>-driven interaction.</li>
  <li><strong>Execution usefulness</strong> — support explicit property reads, property writes, method invocation, and event observation without forcing a complete asynchronous UI framework into the current library surface.</li>
  <li><strong>Contract alignment</strong> — ensure that intrinsic primitives remain usable only within the member and event surfaces declared legal by widget class contracts.</li>
  <li><strong>Token separation</strong> — preserve explicit separation between ordinary value flow, widget-reference participation, event payload flow, and UI sequencing flow.</li>
</ul>

<hr/>

<h2 id="architectural-position">4. Architectural Position</h2>

<p>
The architectural position of <code>frog.ui</code> is intentionally narrow and explicit:
</p>

<pre><code>Expression/   -&gt; canonical source representation
Language/     -&gt; validated-program meaning
Libraries/    -&gt; intrinsic primitive identities and primitive-local contracts
Profiles/     -&gt; optional standardized capability families
IR/           -&gt; execution-facing representation, lowering, and backend-facing boundaries
IDE/          -&gt; authoring, observability, debugging, inspection
</code></pre>

<p>
Within that architecture:
</p>

<ul>
  <li><code>Expression/Widget.md</code> owns source-level widget instances and their source-facing presence,</li>
  <li><code>Expression/Widget class contract.md</code> owns class-level widget legality,</li>
  <li><code>Expression/Widget interaction.md</code> owns the source-facing interaction model, including <code>widget_value</code> and <code>widget_reference</code>,</li>
  <li><code>Expression/Widget package (.wfrog).md</code> owns the <code>.wfrog</code> artifact family,</li>
  <li><code>Libraries/UI.md</code> owns intrinsic primitive identities, primitive-local signatures, metadata requirements, primitive typing, sequencing posture, and primitive-local execution contracts for <code>frog.ui.*</code>,</li>
  <li><code>Language/</code> owns the cross-cutting validated-program meaning of UI participation and UI interaction,</li>
  <li><code>IR/</code> may later preserve these primitives in execution-facing form and then specialize them through lowering,</li>
  <li><code>IDE/</code> may surface these primitives in authoring workflows without redefining them.</li>
</ul>

<p>
The key ownership rule is:
</p>

<pre><code>widget class law
    !=
widget interaction primitive library

front-panel widget declaration
    !=
executable widget interaction primitive

execution-facing representation
    !=
primitive catalog ownership

runtime-private widget handle
    !=
intrinsic frog.ui primitive identity
</code></pre>

<p>
This positioning matters because the primitive library must remain intrinsic even when later layers enrich, specialize, or realize it differently.
</p>

<hr/>

<h2 id="scope">5. Scope</h2>

<p>
For the current library surface, this document standardizes the following intrinsic primitive identifiers:
</p>

<ul>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
  <li><code>frog.ui.event_observe</code></li>
</ul>

<p>
This specification defines:
</p>

<ul>
  <li>primitive identifiers,</li>
  <li>required primitive-local metadata,</li>
  <li>canonical port signatures,</li>
  <li>primitive-local typing constraints,</li>
  <li>primitive-local sequencing posture,</li>
  <li>primitive-level validation rules,</li>
  <li>primitive-local execution-facing semantics.</li>
</ul>

<p>
This specification does not define:
</p>

<ul>
  <li>the widget class catalog,</li>
  <li>front-panel widget serialization,</li>
  <li>the <code>widget_value</code> node kind,</li>
  <li>the <code>widget_reference</code> node kind,</li>
  <li>general diagram edge or port-resolution rules,</li>
  <li>the full source-to-validated-meaning semantic corridor,</li>
  <li>the full validated-meaning-to-IR derivation mapping,</li>
  <li>a complete asynchronous event lifecycle model,</li>
  <li>a generalized widget-reference value type for arbitrary storage or transport,</li>
  <li>one mandatory runtime UI object model,</li>
  <li>one mandatory host realization architecture.</li>
</ul>

<p>
The library therefore standardizes executable primitive truth at the primitive level, not the full surrounding architecture of widget declaration, class legality, source composition, or runtime realization.
</p>

<hr/>

<h2 id="relation-with-other-specifications">6. Relation with Other Specifications</h2>

<p>
This document is used together with the rest of the FROG specification.
</p>

<ul>
  <li><code>Libraries/Readme.md</code> defines the role of <code>Libraries/</code> as the intrinsic primitive-library layer.</li>
  <li><code>Expression/Diagram.md</code> defines how primitive nodes appear in executable diagrams and how general node and edge structure is represented.</li>
  <li><code>Expression/Type.md</code> defines ordinary FROG type expressions and compatibility rules.</li>
  <li><code>Expression/Widget.md</code> defines source-level widget instances.</li>
  <li><code>Expression/Widget class contract.md</code> defines class-level widget legality.</li>
  <li><code>Expression/Widget interaction.md</code> defines the canonical source-facing interaction model used by these primitives.</li>
  <li><code>Expression/Front panel.md</code> defines front-panel widget declaration and composition.</li>
  <li><code>Expression/Widget package (.wfrog).md</code> defines the architectural role of <code>.wfrog</code> packages.</li>
  <li><code>Language/Readme.md</code> defines semantic ownership for validated FROG programs.</li>
  <li><code>IR/</code> documents define execution-facing representation, recoverable mapping, lowering, and backend-facing handoff corridors that may later preserve and specialize these primitives.</li>
</ul>

<p>
Ownership remains intentionally split:
</p>

<ul>
  <li><code>Libraries/UI.md</code> owns primitive identities and primitive-local contracts,</li>
  <li><code>Expression/Widget interaction.md</code> owns the source-facing interaction model,</li>
  <li><code>Expression/Diagram.md</code> owns the general graph representation model,</li>
  <li><code>Expression/Widget class contract.md</code> owns widget property, method, and event availability,</li>
  <li><code>Language/</code> owns the cross-cutting semantic distinction between UI participation roles and UI interaction operations,</li>
  <li><code>IR/</code> owns execution-facing derivation, mapping, lowering, and backend-facing handoff boundaries.</li>
</ul>

<p>
In particular:
</p>

<pre><code>Libraries/UI.md
    does not own
widget class law

Libraries/UI.md
    does not own
front-panel source model

Libraries/UI.md
    does not own
.wfrog package structure

Libraries/UI.md
    does not own
execution-facing object schemas

Libraries/UI.md
    does not own
host-side realization rules

Libraries/UI.md
    owns
intrinsic executable UI-interaction primitive contracts
</code></pre>

<hr/>

<h2 id="namespace">7. Namespace</h2>

<p>
The intrinsic primitive namespace defined by this library is:
</p>

<pre><code>frog.ui.*</code></pre>

<p>
This namespace is reserved for intrinsic executable UI-interaction primitives.
</p>

<p>
It MUST be distinguished from widget-class namespaces such as:
</p>

<pre><code>frog.widgets.*</code></pre>

<p>
Accordingly:
</p>

<ul>
  <li><code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, <code>frog.ui.method_invoke</code>, and <code>frog.ui.event_observe</code> are intrinsic primitive identifiers,</li>
  <li><code>frog.widgets.numeric_control</code> and similar identifiers are widget-class identifiers,</li>
  <li>namespace prefix similarity does not collapse primitive-library ownership and widget-class ownership into one concept.</li>
</ul>

<p>
The <code>frog.ui</code> namespace is therefore about executable interaction vocabulary, not about widget taxonomy.
</p>

<hr/>

<h2 id="standard-primitives">8. Standard Primitives</h2>

<p>
This library standardizes the following intrinsic <code>frog.ui</code> primitives:
</p>

<ul>
  <li><code>frog.ui.property_read</code> — read a property from a widget or widget part,</li>
  <li><code>frog.ui.property_write</code> — write a property of a widget or widget part,</li>
  <li><code>frog.ui.method_invoke</code> — invoke a method on a widget or widget part,</li>
  <li><code>frog.ui.event_observe</code> — observe a declared event on a widget or widget part.</li>
</ul>

<p>
All four primitives:
</p>

<ul>
  <li>MUST be valid intrinsic primitive identifiers in the active library catalog,</li>
  <li>MUST consume a widget reference through a required input port <code>ref</code>,</li>
  <li>MAY expose optional sequencing ports <code>ui_in</code> and <code>ui_out</code>,</li>
  <li>MUST use <code>widget_member</code>, <code>widget_method</code>, or <code>widget_event</code> metadata as appropriate.</li>
</ul>

<p>
These primitives are object-style or event-oriented interaction primitives.
They do not replace the natural primary-value path represented by <code>widget_value</code>.
</p>

<p>
The semantic distinction MUST remain recoverable:
</p>

<pre><code>widget_value
    !=
widget_reference

widget_reference
    !=
frog.ui.property_read / property_write / method_invoke / event_observe

property access to member "value"
    !=
natural widget_value participation

event payload observation
    !=
natural widget_value participation
</code></pre>

<p>
This primitive set is intentionally small.
Its role is to close the standard interaction corridor, not to enumerate every possible future UI operation.
</p>

<hr/>

<h2 id="froguiproperty_read">9. <code>frog.ui.property_read</code></h2>

<p>
Primitive identifier:
</p>

<pre><code>frog.ui.property_read</code></pre>

<p>
A property-read primitive reads a property value from a widget root or widget part and exposes that value to the diagram.
</p>

<p>
Required primitive-local metadata:
</p>

<pre><code>{
  "widget_member": {
    "member": "visible"
  }
}</code></pre>

<p>
Canonical port signature:
</p>

<ul>
  <li>required input port <code>ref</code>,</li>
  <li>optional input port <code>ui_in</code>,</li>
  <li>required output port <code>value</code>,</li>
  <li>optional output port <code>ui_out</code>.</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>the primitive MUST declare <code>widget_member</code>,</li>
  <li>the addressed property MUST be readable for the addressed widget member under the active widget class law,</li>
  <li>the output port <code>value</code> MUST have the declared type of the addressed property.</li>
</ul>

<p>
Reading <code>{ "member": "value" }</code> is valid when the widget class exposes <code>value</code> as a readable property.
However, when the intent is ordinary primary-value dataflow, tools SHOULD prefer the natural <code>widget_value</code> representation.
</p>

<p>
Primitive-local semantics:
</p>

<ul>
  <li>the read observes the current property value at execution time,</li>
  <li>if <code>ui_in</code> is connected, the read MUST occur only after the incoming sequencing token becomes available,</li>
  <li>if <code>ui_out</code> is connected, it MUST become available only after the read has completed,</li>
  <li>the primitive remains an object-style UI-interaction primitive even when the addressed member is named <code>value</code>.</li>
</ul>

<hr/>

<h2 id="froguiproperty_write">10. <code>frog.ui.property_write</code></h2>

<p>
Primitive identifier:
</p>

<pre><code>frog.ui.property_write</code></pre>

<p>
A property-write primitive writes a diagram value into a writable property of a widget root or widget part.
</p>

<p>
Required primitive-local metadata:
</p>

<pre><code>{
  "widget_member": {
    "part": "label",
    "member": "text"
  }
}</code></pre>

<p>
Canonical port signature:
</p>

<ul>
  <li>required input port <code>ref</code>,</li>
  <li>required input port <code>value</code>,</li>
  <li>optional input port <code>ui_in</code>,</li>
  <li>optional output port <code>ui_out</code>.</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>the primitive MUST declare <code>widget_member</code>,</li>
  <li>the addressed property MUST be writable for the addressed widget member under the active widget class law,</li>
  <li>the input port <code>value</code> MUST be type-compatible with the declared type of the addressed property.</li>
</ul>

<p>
Writing <code>{ "member": "value" }</code> is valid when the widget class exposes <code>value</code> as a writable property.
This object-style write MUST remain semantically distinct from the natural primary-value path represented by <code>widget_value</code>.
For ordinary widget-value participation in dataflow, tools SHOULD prefer the natural <code>widget_value</code> representation.
</p>

<p>
Primitive-local semantics:
</p>

<ul>
  <li>a property write applies a UI side effect to the addressed widget member,</li>
  <li>if <code>ui_in</code> is connected, the write MUST occur only after the incoming sequencing token becomes available,</li>
  <li>if <code>ui_out</code> is connected, it MUST become available only after the write has completed according to the active implementation behavior,</li>
  <li>the primitive remains an object-style UI-interaction primitive even when the addressed member is named <code>value</code>.</li>
</ul>

<p>
A presentation-property write such as <code>{ "member": "foreground_color" }</code> MAY affect host-visible appearance.
It MUST NOT by itself redefine the executable meaning of the program.
</p>

<hr/>

<h2 id="froguimethod_invoke">11. <code>frog.ui.method_invoke</code></h2>

<p>
Primitive identifier:
</p>

<pre><code>frog.ui.method_invoke</code></pre>

<p>
A method-invoke primitive calls a method on a widget root or widget part.
</p>

<p>
Required primitive-local metadata:
</p>

<pre><code>{
  "widget_method": {
    "name": "reset_to_default_style"
  }
}</code></pre>

<p>
Canonical port signature:
</p>

<ul>
  <li>required input port <code>ref</code>,</li>
  <li>zero or more method-argument input ports in canonical method order,</li>
  <li>optional input port <code>ui_in</code>,</li>
  <li>zero or more method-result output ports in canonical method order,</li>
  <li>optional output port <code>ui_out</code>.</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>the primitive MUST declare <code>widget_method</code>,</li>
  <li>the addressed method MUST exist for the addressed widget member under the active widget class law,</li>
  <li>argument input ports MUST match the canonical method signature,</li>
  <li>result output ports MUST match the canonical method signature,</li>
  <li>each argument input MUST be type-compatible with the declared parameter type,</li>
  <li>each result output MUST have the declared result type.</li>
</ul>

<p>
Primitive-local semantics:
</p>

<ul>
  <li>a method invocation MAY produce UI side effects, ordinary return values, or both,</li>
  <li>if <code>ui_in</code> is connected, the invocation MUST occur only after the incoming sequencing token becomes available,</li>
  <li>if <code>ui_out</code> is connected, it MUST become available only after invocation has completed according to the active implementation behavior,</li>
  <li>the primitive remains distinct from both widget declaration identity and widget-reference participation identity.</li>
</ul>

<p>
Method invocation remains a primitive-level UI operation.
It does not redefine class law and does not redefine source-side widget declaration.
</p>

<hr/>

<h2 id="froguievent_observe">12. <code>frog.ui.event_observe</code></h2>

<p>
Primitive identifier:
</p>

<pre><code>frog.ui.event_observe</code></pre>

<p>
An event-observe primitive observes a declared event on a widget root or widget part and exposes the event payload, when any, to the diagram according to the primitive contract.
</p>

<p>
Required primitive-local metadata:
</p>

<pre><code>{
  "widget_event": {
    "name": "value_rendered"
  }
}</code></pre>

<p>
Canonical port signature:
</p>

<ul>
  <li>required input port <code>ref</code>,</li>
  <li>optional input port <code>ui_in</code>,</li>
  <li>optional output port <code>payload</code>,</li>
  <li>required output port <code>observed</code>,</li>
  <li>optional output port <code>ui_out</code>.</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>the primitive MUST declare <code>widget_event</code>,</li>
  <li>the addressed event MUST be observable for the addressed widget member under the active widget class law,</li>
  <li>if the event declares a payload, the output port <code>payload</code> MUST have that declared payload type,</li>
  <li>the output port <code>observed</code> MUST indicate whether the event occurrence has been observed according to the primitive contract.</li>
</ul>

<p>
Event observation remains semantically distinct from both property access and natural primary-value participation.
An event payload MUST NOT be silently normalized into <code>widget_value</code> participation.
</p>

<p>
Primitive-local semantics:
</p>

<ul>
  <li>the primitive observes occurrences of the declared event at execution time,</li>
  <li>if <code>ui_in</code> is connected, observation MUST respect the incoming sequencing token,</li>
  <li>if <code>ui_out</code> is connected, it MUST become available only after the observation step has completed according to the active implementation behavior,</li>
  <li>the primitive remains an event-oriented UI-interaction primitive and does not redefine the event as a property or as the widget primary value.</li>
</ul>

<hr/>

<h2 id="typing-and-sequencing">13. Typing and Sequencing</h2>

<h3>13.1 Widget-reference typing</h3>

<p>
The required input port <code>ref</code> carries an opaque widget-reference token.
This token is interaction-oriented and diagram-internal.
It is not standardized here as a general-purpose first-class value type for arbitrary storage, transport, comparison, or computation.
</p>

<h3>13.2 Property typing</h3>

<p>
Property-read and property-write primitives MUST use the declared property type of the addressed widget member.
Compatibility checks and implicit coercions MUST follow the ordinary FROG type rules.
</p>

<h3>13.3 Method typing</h3>

<p>
Method-invoke primitives MUST use the declared method signature of the addressed widget member.
Argument and result ports MUST follow the canonical method signature defined by the active widget class law.
</p>

<h3>13.4 Event typing</h3>

<p>
Event-observe primitives MUST use the declared event payload type of the addressed widget event.
If the event declares no payload, the <code>payload</code> port MAY be omitted.
</p>

<h3>13.5 UI sequencing ports</h3>

<p>
The optional ports <code>ui_in</code> and <code>ui_out</code> define explicit ordering between UI interactions.
These ports:
</p>

<ul>
  <li>MUST NOT be interpreted as ordinary data values,</li>
  <li>MUST NOT redefine ordinary data-dependency typing,</li>
  <li>MAY be omitted when no explicit UI ordering is required,</li>
  <li>SHOULD be used when deterministic ordering of UI side effects or event observation matters.</li>
</ul>

<p>
The sequencing token carried by <code>ui_in</code> and <code>ui_out</code> is opaque.
Its runtime representation is implementation-defined, but its ordering meaning between standardized UI-interaction primitives is defined by this specification.
</p>

<h3>13.6 Boundary rule</h3>

<p>
The presence of sequencing ports does not convert these primitives into a general callback model,
full asynchronous orchestration model, or general message-bus model.
They remain explicit widget interaction primitives with optional ordering support.
</p>

<p>
The following distinction MUST remain explicit:
</p>

<pre><code>ordinary typed value ports
    !=
widget reference ports
    !=
event payload ports
    !=
UI sequencing ports
</code></pre>

<p>
Likewise:
</p>

<pre><code>property value
    !=
event payload
    !=
widget reference token
    !=
sequencing token
</code></pre>

<hr/>

<h2 id="validation-rules">14. Validation Rules</h2>

<p>
Implementations MUST enforce at least the following primitive-level rules:
</p>

<ul>
  <li>the primitive identifier MUST be one of the standardized identifiers defined by this document,</li>
  <li>the required input port <code>ref</code> MUST be present,</li>
  <li>a property primitive MUST declare <code>widget_member</code>,</li>
  <li>a method primitive MUST declare <code>widget_method</code>,</li>
  <li>an event primitive MUST declare <code>widget_event</code>,</li>
  <li>required and optional ports MUST match the standardized signature of the primitive,</li>
  <li>primitive-local typing MUST remain valid under the ordinary FROG type rules.</li>
</ul>

<p>
Additionally:
</p>

<ul>
  <li><code>frog.ui.property_read</code> MUST address a readable property,</li>
  <li><code>frog.ui.property_write</code> MUST address a writable property,</li>
  <li><code>frog.ui.method_invoke</code> MUST address a valid method,</li>
  <li><code>frog.ui.event_observe</code> MUST address a valid observable event,</li>
  <li>part names, member names, method names, and event names MUST be valid for the addressed widget class,</li>
  <li>the distinction between object-style interaction, event observation, and natural <code>widget_value</code> participation MUST remain semantically recoverable,</li>
  <li>use of a property named <code>value</code> through <code>frog.ui.property_read</code> or <code>frog.ui.property_write</code> MUST NOT be silently normalized into <code>widget_value</code> participation,</li>
  <li>natural <code>widget_value</code> participation MUST NOT be silently reclassified as property-based access to member <code>value</code>,</li>
  <li>event payload observation MUST NOT be silently normalized into property access or natural primary-value participation.</li>
</ul>

<p>
Invalid UI-interaction primitives MUST trigger validation errors.
</p>

<p>
Source-level graph-shape constraints remain owned by <code>Expression/Widget interaction.md</code> and <code>Expression/Diagram.md</code>.
Cross-cutting semantic acceptance remains owned by <code>Language/</code>.
Execution-facing derivation, mapping, lowering, and backend-facing handoff remain owned by <code>IR/</code>.
</p>

<hr/>

<h2 id="execution-facing-posture">15. Execution-Facing Posture</h2>

<p>
This document defines intrinsic primitive-local truth, not one execution-facing representation.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>execution-facing representations MAY preserve recognizable primitive execution objects corresponding to <code>frog.ui.property_read</code>, <code>frog.ui.property_write</code>, <code>frog.ui.method_invoke</code>, and <code>frog.ui.event_observe</code>,</li>
  <li>derivation MAY add execution-facing explicitness such as resolved member descriptors, method descriptors, event descriptors, classification records, or source-attribution records,</li>
  <li>identity and mapping rules MAY require these primitives to remain distinguishable from widget-reference participation and from natural widget-value participation,</li>
  <li>lowering MAY later specialize these primitives into backend-oriented UI-binding operations, callable descriptors, event observation adapters, handle-oriented operations, or equivalent lower forms,</li>
  <li>backend contracts MAY later declare consumer-facing assumptions about UI capability support or UI-interaction transport,</li>
  <li>runtime-private realization MAY choose private widget handles, tokens, dispatch tables, event bridges, or host-binding objects,</li>
  <li>but none of those later stages redefines the intrinsic primitive identities or primitive-local contracts owned here.</li>
</ul>

<p>
This corridor matters:
</p>

<pre><code>intrinsic primitive truth
    -&gt; frog.ui.* primitive-local contract

validated meaning
    -&gt; preserves semantic distinction between participation roles and UI-operation roles

execution-facing representation
    -&gt; may preserve recognizable UI-operation execution objects

lowered form
    -&gt; may specialize them for a backend family

backend contract
    -&gt; may declare what a consumer may rely on

private runtime
    -&gt; may realize them through private widget-handle and host-binding machinery
</code></pre>

<p>
The primitive stays the same intrinsic primitive across that corridor.
Only the later representation and realization change.
</p>

<hr/>

<h2 id="examples">16. Examples</h2>

<h3>16.1 Property read</h3>

<pre><code>{
  "id": "read_label_text",
  "kind": "primitive",
  "type": "frog.ui.property_read",
  "widget_member": {
    "part": "label",
    "member": "text"
  }
}</code></pre>

<h3>16.2 Property write</h3>

<pre><code>{
  "id": "write_visible",
  "kind": "primitive",
  "type": "frog.ui.property_write",
  "widget_member": {
    "member": "visible"
  }
}</code></pre>

<h3>16.3 Method invoke</h3>

<pre><code>{
  "id": "invoke_focus",
  "kind": "primitive",
  "type": "frog.ui.method_invoke",
  "widget_method": {
    "name": "focus"
  }
}</code></pre>

<h3>16.4 Event observe</h3>

<pre><code>{
  "id": "observe_rendered",
  "kind": "primitive",
  "type": "frog.ui.event_observe",
  "widget_event": {
    "name": "value_rendered"
  }
}</code></pre>

<h3>16.5 Example diagram fragment</h3>

<pre><code>{
  "nodes": [
    {
      "id": "ctrl_gain_ref",
      "kind": "widget_reference",
      "widget": "ctrl_gain"
    },
    {
      "id": "read_gain_value_property",
      "kind": "primitive",
      "type": "frog.ui.property_read",
      "widget_member": {
        "member": "value"
      }
    },
    {
      "id": "write_visible",
      "kind": "primitive",
      "type": "frog.ui.property_write",
      "widget_member": {
        "member": "visible"
      }
    },
    {
      "id": "observe_rendered",
      "kind": "primitive",
      "type": "frog.ui.event_observe",
      "widget_event": {
        "name": "value_rendered"
      }
    }
  ],
  "edges": [
    {
      "id": "e1",
      "from": { "node": "ctrl_gain_ref", "port": "ref" },
      "to":   { "node": "read_gain_value_property", "port": "ref" }
    },
    {
      "id": "e2",
      "from": { "node": "ctrl_gain_ref", "port": "ref" },
      "to":   { "node": "write_visible", "port": "ref" }
    },
    {
      "id": "e3",
      "from": { "node": "ctrl_gain_ref", "port": "ref" },
      "to":   { "node": "observe_rendered", "port": "ref" }
    }
  ]
}</code></pre>

<p>
In this example, reading member <code>value</code> through <code>frog.ui.property_read</code> remains object-style property access.
It is not the same thing as natural <code>widget_value</code> participation.
Likewise, observing <code>value_rendered</code> remains event-oriented interaction and is not the same thing as either property access or natural value participation.
</p>

<hr/>

<h2 id="out-of-scope">17. Out of Scope</h2>

<ul>
  <li>a full standardized widget catalog,</li>
  <li>pixel-perfect cross-runtime rendering equivalence,</li>
  <li>a complete standardized event subscription lifecycle,</li>
  <li>general-purpose asynchronous callback delivery,</li>
  <li>a generalized widget-reference value type for arbitrary storage or transport,</li>
  <li>complete theme and style systems,</li>
  <li>automatic inference of UI sequencing in all cases,</li>
  <li>full standardization of all possible widget member sets,</li>
  <li>one mandatory execution-facing UI-object schema,</li>
  <li>one mandatory lowering family for UI interaction,</li>
  <li>one mandatory backend-family UI contract model,</li>
  <li>one mandatory runtime-private widget-handle architecture.</li>
</ul>

<hr/>

<h2 id="summary">18. Summary</h2>

<p>
The <code>frog.ui</code> library defines the intrinsic executable UI-interaction primitives of FROG:
</p>

<ul>
  <li><code>frog.ui.property_read</code></li>
  <li><code>frog.ui.property_write</code></li>
  <li><code>frog.ui.method_invoke</code></li>
  <li><code>frog.ui.event_observe</code></li>
</ul>

<p>
These primitives:
</p>

<ul>
  <li>consume widget references,</li>
  <li>use <code>widget_member</code>, <code>widget_method</code>, or <code>widget_event</code> metadata,</li>
  <li>support optional explicit UI sequencing through <code>ui_in</code> and <code>ui_out</code>,</li>
  <li>complement, but do not replace, the natural <code>widget_value</code> path,</li>
  <li>remain distinct from widget class law, widget declarations, front-panel source, <code>.wfrog</code> package ownership, execution-facing representation ownership, backend-contract ownership, and runtime-private realization.</li>
</ul>

<p>
In short:
</p>

<ul>
  <li><strong><code>widget_value</code></strong> is the natural primary-value path,</li>
  <li><strong><code>widget_reference</code></strong> is the object-style and event-oriented reference path,</li>
  <li><strong><code>frog.ui.*</code></strong> is the intrinsic executable interaction vocabulary that consumes those references.</li>
</ul>
