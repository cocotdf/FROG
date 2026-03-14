<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="150" />
</p>

<h1 align="center">🐸 FROG State and Cycles Specification</h1>

<p align="center">
Normative execution semantics for local memory and cycle validity in FROG programs<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Goals</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#local-memory">4. Local Memory</a></li>
  <li><a href="#stateless-vs-local-memory-primitives">5. Stateless vs Local-Memory Primitives</a></li>
  <li><a href="#state-ownership-and-scope">6. State Ownership and Scope</a></li>
  <li><a href="#cycles-in-dataflow-graphs">7. Cycles in Dataflow Graphs</a></li>
  <li><a href="#cycle-validity-rule">8. Cycle Validity Rule</a></li>
  <li><a href="#frog-core-delay">9. <code>frog.core.delay</code></a></li>
  <li><a href="#initial-state">10. Initial State</a></li>
  <li><a href="#execution-semantics">11. Execution Semantics</a></li>
  <li><a href="#scheduler-independence">12. Scheduler Independence</a></li>
  <li><a href="#interaction-with-control-structures">13. Interaction with Control Structures</a></li>
  <li><a href="#validation-rules">14. Validation Rules</a></li>
  <li><a href="#examples">15. Examples</a></li>
  <li><a href="#out-of-scope-for-v01">16. Out of Scope for v0.1</a></li>
  <li><a href="#summary">17. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
FROG is a graphical dataflow programming language. In an acyclic graph, execution order can be derived directly from data
dependencies. However, many useful programs require feedback paths, accumulation, filtering, integration, delayed reuse of
values, or other forms of memory.
</p>

<p>
This document defines the normative execution semantics of local memory in FROG and the language-level rule that governs
the validity of directed cycles in executable diagrams. In FROG, a directed cycle is valid only when its meaning is made
explicit through at least one primitive whose node instance stores a value between activations. Such a primitive is called
a local-memory primitive.
</p>

<p>
In informal terms, a local-memory primitive is a primitive with local state. The preferred normative wording in this
specification is <strong>local memory</strong>.
</p>

<p>
This document defines the language-level semantics required for explicit local memory and cyclic dataflow.
It does not redefine the canonical source serialization already owned by <code>Expression/</code>, and it does not redefine
the standardized primitive identity of <code>frog.core.delay</code> already owned by <code>Libraries/</code>.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Clarity</strong> — define what local memory means in FROG.</li>
  <li><strong>Safety</strong> — reject invalid cycles that contain no explicit memory.</li>
  <li><strong>Determinism</strong> — require explicit and deterministic initialization of local memory.</li>
  <li><strong>Separation of concerns</strong> — keep local memory distinct from global state, shared state, and runtime services.</li>
  <li><strong>Compatibility with dataflow</strong> — allow feedback while preserving an explicit and verifiable execution model.</li>
  <li><strong>Architectural cleanliness</strong> — keep semantic ownership in <code>Language/</code> while preserving source ownership in <code>Expression/</code>.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This document complements the following specifications:
</p>

<ul>
  <li><code>Language/Readme.md</code> — defines the role of <code>Language/</code> as the normative execution-semantics layer.</li>
  <li><code>Expression/State and cycles.md</code> — defines the source-facing representation of explicit local memory and cycle-facing source constraints.</li>
  <li><code>Expression/Diagram.md</code> — defines the executable graph structure, node kinds, edges, and graph-level source representation.</li>
  <li><code>Expression/Type.md</code> — defines type compatibility for values carried through local-memory primitives.</li>
  <li><code>Language/Control structures.md</code> — defines structure semantics for nested executable regions, which remain subject to the same cycle-validity rule.</li>
  <li><code>Libraries/Core.md</code> — defines standard primitive identity, ports, required metadata, and primitive-local definition of <code>frog.core.delay</code>.</li>
</ul>

<p>
This document defines semantic rules for local memory and cycle validity.
It does not redefine the serialized graph structure already specified by <code>Expression/Diagram.md</code>.
</p>

<p>
Ownership is intentionally split as follows:
</p>

<ul>
  <li><code>Expression/</code> owns the canonical source representation of explicit local-memory constructs,</li>
  <li><code>Language/</code> owns the normative execution meaning of local memory and valid cycles,</li>
  <li><code>Libraries/</code> owns the standardized primitive identity of <code>frog.core.delay</code>.</li>
</ul>

<hr/>

<h2 id="local-memory">4. Local Memory</h2>

<p>
A local-memory primitive is a primitive whose node instance stores an internal value across activations of the same live
FROG instance.
</p>

<p>
Conceptually, a local-memory primitive has:
</p>

<ul>
  <li>a current internal state value,</li>
  <li>a rule for producing outputs from that current state and the current inputs,</li>
  <li>a rule for updating the stored state for a later activation.</li>
</ul>

<p>
That local memory is:
</p>

<ul>
  <li>attached to the node instance,</li>
  <li>local to that primitive instance,</li>
  <li>not a global variable,</li>
  <li>not implicitly shared with other nodes,</li>
  <li>not a general-purpose shared reference mechanism.</li>
</ul>

<p>
A local-memory primitive therefore introduces persistent behavior across activations without changing the fact that FROG
remains a dataflow language.
</p>

<hr/>

<h2 id="stateless-vs-local-memory-primitives">5. Stateless vs Local-Memory Primitives</h2>

<h3>5.1 Stateless primitive</h3>

<p>
A stateless primitive does not preserve any value between activations.
Its outputs depend only on its current inputs and its fixed configuration.
</p>

<p>Examples:</p>

<ul>
  <li><code>frog.core.add</code></li>
  <li><code>frog.core.mul</code></li>
  <li><code>frog.core.equal</code></li>
  <li><code>frog.math.sin</code></li>
</ul>

<h3>5.2 Local-memory primitive</h3>

<p>
A local-memory primitive preserves an internal value between activations.
Its outputs may depend on that preserved value in addition to its current inputs.
</p>

<p>Examples:</p>

<ul>
  <li><code>frog.core.delay</code></li>
  <li>future register-style primitives</li>
  <li>future integrator-style primitives</li>
  <li>future stateful signal-processing primitives</li>
</ul>

<p>
This distinction is semantic, not merely visual or editorial.
Two primitives with identical port shapes are not semantically equivalent if one preserves state and the other does not.
</p>

<hr/>

<h2 id="state-ownership-and-scope">6. State Ownership and Scope</h2>

<p>
Local memory belongs to a specific node instance inside a specific live FROG instance.
</p>

<p>
Therefore:
</p>

<ul>
  <li>two different local-memory nodes do not share state implicitly,</li>
  <li>two different sub-FROG instances do not share local memory implicitly,</li>
  <li>duplicating a node duplicates its local memory,</li>
  <li>instantiating the same sub-FROG multiple times creates distinct local memory for each instantiated graph.</li>
</ul>

<p>
The exact lifetime of a live FROG instance may depend on the active runtime profile.
However, within one live instance, the meaning of local memory MUST remain stable and deterministic.
</p>

<p>
This means that implementation choices such as allocation strategy, storage layout, or backend representation MAY vary,
but they MUST NOT change the observable semantic identity of local memory as node-instance-scoped stored value.
</p>

<hr/>

<h2 id="cycles-in-dataflow-graphs">7. Cycles in Dataflow Graphs</h2>

<p>
A directed cycle exists when a path of directed edges leads from a node back to itself.
</p>

<p>Examples:</p>

<pre><code>A → B → C → A</code></pre>

<p>or:</p>

<pre><code>A → A</code></pre>

<p>
In a pure dataflow graph, a cycle with no memory creates an unresolved dependency loop.
Such a graph does not define valid executable behavior by itself.
</p>

<p>
Therefore, FROG distinguishes between:
</p>

<ul>
  <li><strong>invalid combinational cycles</strong> — cycles containing no local memory,</li>
  <li><strong>valid stateful cycles</strong> — cycles containing at least one explicit local-memory primitive.</li>
</ul>

<p>
This rule applies both to the top-level diagram and to region-local diagrams owned by language structures.
</p>

<hr/>

<h2 id="cycle-validity-rule">8. Cycle Validity Rule</h2>

<p>
The base rule of FROG v0.1 is:
</p>

<pre><code>A diagram MAY contain directed cycles.

Every directed cycle MUST contain at least one local-memory primitive.</code></pre>

<p>
Equivalent interpretation:
</p>

<ul>
  <li>a cycle without local memory is invalid,</li>
  <li>a cycle containing at least one local-memory primitive is valid in principle, subject to ordinary graph and type validation.</li>
</ul>

<p>
This rule applies to:
</p>

<ul>
  <li>multi-node cycles,</li>
  <li>self-feedback cycles,</li>
  <li>feedback paths through nested diagram regions.</li>
</ul>

<p>
A validator MAY enforce this rule using strongly connected component analysis or any equivalent graph-theoretic method.
</p>

<p>
This rule is semantic, not merely structural:
</p>

<ul>
  <li>layout alone cannot make a cycle valid,</li>
  <li>documentation alone cannot make a cycle valid,</li>
  <li>tool intention alone cannot make a cycle valid,</li>
  <li>only explicit local memory can make the feedback meaning well-defined.</li>
</ul>

<hr/>

<h2 id="frog-core-delay">9. <code>frog.core.delay</code></h2>

<p>
The minimal standard local-memory primitive for FROG v0.1 is:
</p>

<pre><code>frog.core.delay</code></pre>

<p>
Its purpose is to make delayed feedback explicit.
It stores one value and exposes that stored value on the next activation.
</p>

<h3>9.1 Ports</h3>

<p>
The canonical ports of <code>frog.core.delay</code> are:
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>out</code></li>
</ul>

<h3>9.2 Semantic role</h3>

<p>
The semantic role of <code>frog.core.delay</code> is not to introduce arbitrary statefulness into the language.
Its role is narrower and more precise:
</p>

<ul>
  <li>to provide explicit local memory,</li>
  <li>to make delayed feedback visible in the graph,</li>
  <li>to permit stateful cycles without hidden scheduler-dependent interpretation.</li>
</ul>

<h3>9.3 Relation to ownership</h3>

<p>
For <code>frog.core.delay</code>, ownership remains intentionally split:
</p>

<ul>
  <li><code>Libraries/Core.md</code> owns the primitive name, ports, and required metadata,</li>
  <li><code>Expression/State and cycles.md</code> owns its canonical source representation,</li>
  <li>this document owns the normative execution meaning that makes it a local-memory primitive.</li>
</ul>

<hr/>

<h2 id="initial-state">10. Initial State</h2>

<p>
Every local-memory primitive MUST have a deterministic initial state.
</p>

<p>
For <code>frog.core.delay</code> in v0.1, the <code>initial</code> field is mandatory.
</p>

<p>
Illustrative node shape:
</p>

<pre><code class="language-json">{
  "id": "delay_1",
  "kind": "primitive",
  "type": "frog.core.delay",
  "initial": 0.0
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>initial</code> MUST be present for every <code>frog.core.delay</code> node in v0.1,</li>
  <li>the value of <code>initial</code> MUST be compatible with the value type carried by the node,</li>
  <li>the initial state MUST be fully defined by source or by a stricter profile that preserves deterministic equivalence.</li>
</ul>

<p>
FROG v0.1 does not permit undefined initial state for <code>frog.core.delay</code>.
</p>

<p>
This requirement is not a cosmetic convenience.
It is part of the semantic determinism of the language.
A local-memory primitive whose first observable value is undefined would not provide a stable portable meaning for feedback.
</p>

<hr/>

<h2 id="execution-semantics">11. Execution Semantics</h2>

<p>
A local-memory primitive participates in the diagram as an ordinary executable node, but with additional state-update semantics.
</p>

<p>
For <code>frog.core.delay</code>, the conceptual execution model is:
</p>

<ol>
  <li>read the current stored state,</li>
  <li>expose that value on <code>out</code>,</li>
  <li>capture the current value on <code>in</code> as the next stored state.</li>
</ol>

<p>
The intended observable meaning is:
</p>

<pre><code>the value observed on out at activation t
is the value that was stored before the update of activation t</code></pre>

<p>
Equivalently:
</p>

<pre><code>out(t) = state(t)
state(t + 1) = in(t)
state(0) = initial</code></pre>

<p>
This preserves the expected semantics for feedback, accumulation, filtering, and iterative processes.
</p>

<p>
The semantic consequence is important:
a feedback path containing <code>frog.core.delay</code> is not interpreted as an instantaneous combinational loop.
It is interpreted as a stateful recurrence across activations.
</p>

<hr/>

<h2 id="scheduler-independence">12. Scheduler Independence</h2>

<p>
The exact internal scheduler implementation may vary across runtimes, but the observable semantics MUST remain equivalent.
</p>

<p>
Therefore, runtimes MAY differ in:
</p>

<ul>
  <li>internal event scheduling strategy,</li>
  <li>queueing mechanisms,</li>
  <li>buffer layouts,</li>
  <li>memory allocation strategies,</li>
  <li>backend execution order details that do not change meaning.</li>
</ul>

<p>
However, runtimes MUST NOT differ in:
</p>

<ul>
  <li>whether a cycle without explicit local memory is valid,</li>
  <li>whether <code>frog.core.delay</code> exposes the stored pre-update value on <code>out</code>,</li>
  <li>whether <code>initial</code> determines the first stored value,</li>
  <li>whether local memory is scoped to the primitive instance.</li>
</ul>

<p>
This separation allows backend freedom without semantic fragmentation of the language.
</p>

<hr/>

<h2 id="interaction-with-control-structures">13. Interaction with Control Structures</h2>

<p>
The cycle-validity rule applies equally inside structure-owned regions.
A control structure does not implicitly create valid local memory for a feedback path.
</p>

<p>
Therefore:
</p>

<ul>
  <li>a cycle inside a <code>case</code> branch remains invalid unless it contains explicit local memory,</li>
  <li>a cycle inside a <code>for_loop</code> body remains invalid unless it contains explicit local memory,</li>
  <li>a cycle inside a <code>while_loop</code> body remains invalid unless it contains explicit local memory.</li>
</ul>

<p>
Loop repetition is not itself a substitute for explicit local memory in a graph cycle.
Iteration and stored state are related concepts, but they are not the same semantic mechanism.
</p>

<hr/>

<h2 id="validation-rules">14. Validation Rules</h2>

<p>
Implementations MUST enforce the following rules:
</p>

<ul>
  <li>every directed cycle MUST contain at least one local-memory primitive,</li>
  <li>all value connections through local-memory primitives MUST remain type-compatible according to <code>Expression/Type.md</code>,</li>
  <li>local memory MUST be scoped to the node instance,</li>
  <li>local memory MUST NOT be implicitly shared across unrelated nodes or sub-FROG instances,</li>
  <li>the initial state of every local-memory primitive MUST be deterministic.</li>
</ul>

<p>
For <code>frog.core.delay</code> specifically:
</p>

<ul>
  <li>the node MUST define an <code>initial</code> field,</li>
  <li><code>in</code> and <code>out</code> MUST have the same value type,</li>
  <li><code>initial</code> MUST be compatible with that type.</li>
</ul>

<p>
Tools SHOULD additionally warn when:
</p>

<ul>
  <li>a cycle contains more local-memory primitives than necessary and becomes difficult to understand,</li>
  <li>feedback is valid but visually unclear,</li>
  <li>multiple feedback paths make execution hard to inspect even though validation succeeds.</li>
</ul>

<hr/>

<h2 id="examples">15. Examples</h2>

<h3>15.1 Invalid cycle without local memory</h3>

<pre><code class="language-json">{
  "diagram": {
    "nodes": [
      { "id": "a", "kind": "primitive", "type": "frog.core.add" },
      { "id": "b", "kind": "primitive", "type": "frog.core.mul" }
    ],
    "edges": [
      { "id": "e1", "from": { "node": "a", "port": "result" }, "to": { "node": "b", "port": "a" } },
      { "id": "e2", "from": { "node": "b", "port": "result" }, "to": { "node": "a", "port": "a" } }
    ]
  }
}</code></pre>

<p>
This graph is invalid because the cycle contains no local-memory primitive.
</p>

<h3>15.2 Valid cycle with <code>frog.core.delay</code></h3>

<pre><code class="language-json">{
  "diagram": {
    "nodes": [
      { "id": "input_x", "kind": "interface_input", "interface_port": "x" },
      { "id": "add_1", "kind": "primitive", "type": "frog.core.add" },
      { "id": "delay_1", "kind": "primitive", "type": "frog.core.delay", "initial": 0.0 },
      { "id": "output_y", "kind": "interface_output", "interface_port": "y" }
    ],
    "edges": [
      { "id": "e1", "from": { "node": "input_x", "port": "value" }, "to": { "node": "add_1", "port": "a" } },
      { "id": "e2", "from": { "node": "delay_1", "port": "out" }, "to": { "node": "add_1", "port": "b" } },
      { "id": "e3", "from": { "node": "add_1", "port": "result" }, "to": { "node": "delay_1", "port": "in" } },
      { "id": "e4", "from": { "node": "add_1", "port": "result" }, "to": { "node": "output_y", "port": "value" } }
    ]
  }
}</code></pre>

<p>
This graph is valid because the feedback cycle is broken by explicit local memory provided by <code>frog.core.delay</code>.
</p>

<h3>15.3 Accumulator intuition</h3>

<p>
Conceptually:
</p>

<pre><code>sum(t) = x(t) + sum(t - 1)</code></pre>

<p>
One valid graphical realization is:
</p>

<pre><code>x → add → y
     ^    |
     |    v
   delay ←</code></pre>

<h3>15.4 Delay behavior over time</h3>

<p>
If:
</p>

<ul>
  <li><code>initial = 0</code></li>
  <li><code>in</code> receives <code>10, 20, 30, 40</code></li>
</ul>

<p>
then <code>out</code> produces:
</p>

<pre><code>0, 10, 20, 30</code></pre>

<p>
This illustrates the defining semantic property of delayed state:
the output at one activation reflects the stored value from the previous activation state.
</p>

<hr/>

<h2 id="out-of-scope-for-v01">16. Out of Scope for v0.1</h2>

<ul>
  <li>implicit feedback state,</li>
  <li>automatic insertion of hidden memory to repair invalid cycles,</li>
  <li>shared mutable state between unrelated nodes,</li>
  <li>distributed state semantics,</li>
  <li>transactional state models,</li>
  <li>event-specific memory semantics,</li>
  <li>alternative standardized local-memory primitives beyond the minimal base definition.</li>
</ul>

<hr/>

<h2 id="summary">17. Summary</h2>

<p>
FROG allows feedback in executable diagrams, but only when memory is made explicit.
</p>

<ul>
  <li>a directed cycle MAY exist in a valid FROG graph,</li>
  <li>it is valid only when at least one explicit local-memory primitive appears in that cycle,</li>
  <li><code>frog.core.delay</code> is the minimal standard local-memory primitive for v0.1,</li>
  <li><code>initial</code> is mandatory for <code>frog.core.delay</code> in v0.1,</li>
  <li>local memory is scoped to the primitive instance and is not implicitly shared,</li>
  <li>scheduler freedom is allowed only when observable semantics remain equivalent.</li>
</ul>

<p>
This gives FROG a clear, explicit, and durable semantic foundation for stateful feedback in a dataflow language.
</p>
