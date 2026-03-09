<h1 align="center">🐸 FROG State and Cycles Specification</h1>

<p align="center">
Definition of local state and cycle validity in FROG programs<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Goals</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#local-state-concept">4. Local State Concept</a></li>
  <li><a href="#stateless-vs-local-state-functions">5. Stateless vs Local-State Functions</a></li>
  <li><a href="#state-ownership-and-lifetime">6. State Ownership and Lifetime</a></li>
  <li><a href="#cycles-in-the-diagram">7. Cycles in the Diagram</a></li>
  <li><a href="#cycle-validity-rule">8. Cycle Validity Rule</a></li>
  <li><a href="#standard-local-state-function-for-v01">9. Standard Local-State Function for v0.1</a></li>
  <li><a href="#initial-state-semantics">10. Initial State Semantics</a></li>
  <li><a href="#execution-semantics">11. Execution Semantics</a></li>
  <li><a href="#determinism-and-validation">12. Determinism and Validation</a></li>
  <li><a href="#examples">13. Examples</a></li>
  <li><a href="#out-of-scope">14. Out of Scope for v0.1</a></li>
  <li><a href="#summary">15. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
FROG is a graphical dataflow language.
In a pure acyclic dataflow graph, execution order can be derived directly from data dependencies.
However, many useful programs require feedback, accumulation, filtering, integration, or other forms of memory.
</p>

<p>
This document defines how FROG represents and validates such behavior through the notion of <strong>local state</strong>.
</p>

<p>
In FROG, a directed cycle in the executable graph is allowed only when the cycle is broken semantically by at least one function that stores a value between activations.
Such a function is called a <strong>local-state function</strong>.
</p>

<p>
This document does not define the full standard library of FROG.
It defines the language-level rules that make cyclic dataflow valid and deterministic.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Clarity</strong> — define precisely what local state means in FROG.</li>
  <li><strong>Safety</strong> — prevent invalid combinational cycles that have no memory.</li>
  <li><strong>Determinism</strong> — ensure that valid feedback paths have explicit and inspectable semantics.</li>
  <li><strong>Modularity</strong> — keep local state distinct from global state, shared state, and runtime services.</li>
  <li><strong>Compatibility with dataflow</strong> — allow feedback while preserving a clear dataflow execution model.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This document complements the following specifications:
</p>

<ul>
  <li><strong>Expression/Diagram.md</strong> — defines the graph structure, node kinds, edges, and validation of diagram references.</li>
  <li><strong>Expression/Type.md</strong> — defines type compatibility for values carried through local-state functions.</li>
  <li><strong>Libraries/Core.md</strong> — may define the standard library functions that implement local state, such as <code>frog.core.delay</code>.</li>
</ul>

<p>
This document defines language semantics.
It does not redefine the JSON graph structure already described by <code>Diagram.md</code>.
</p>

<hr/>

<h2 id="local-state-concept">4. Local State Concept</h2>

<p>
A <strong>local-state function</strong> is a function whose node instance stores an internal value across activations of the same live FROG instance.
</p>

<p>
Conceptually, a local-state function has:
</p>

<ul>
  <li>a current internal state value,</li>
  <li>a rule for producing outputs from that current state and the current inputs,</li>
  <li>a rule for updating the state for a later activation.</li>
</ul>

<p>
In informal terms, a local-state function is a function with <strong>local memory</strong>.
</p>

<p>
That local memory is:
</p>

<ul>
  <li>attached to the node instance,</li>
  <li>not a global variable,</li>
  <li>not shared implicitly with other nodes,</li>
  <li>not a general-purpose shared reference mechanism.</li>
</ul>

<hr/>

<h2 id="stateless-vs-local-state-functions">5. Stateless vs Local-State Functions</h2>

<h3>5.1 Stateless function</h3>

<p>
A <strong>stateless function</strong> has no memory across activations.
Its outputs depend only on its current inputs and its fixed configuration.
</p>

<p>
Examples:
</p>

<ul>
  <li><code>frog.core.add</code></li>
  <li><code>frog.core.mul</code></li>
  <li><code>frog.core.equal</code></li>
  <li><code>frog.math.sin</code></li>
</ul>

<h3>5.2 Local-state function</h3>

<p>
A <strong>local-state function</strong> stores an internal value across activations.
Its outputs may depend on that stored value in addition to the current inputs.
</p>

<p>
Examples:
</p>

<ul>
  <li><code>frog.core.delay</code></li>
  <li>future register-style functions</li>
  <li>future integrator-style functions</li>
  <li>future stateful signal-processing functions</li>
</ul>

<hr/>

<h2 id="state-ownership-and-lifetime">6. State Ownership and Lifetime</h2>

<p>
Local state belongs to a <strong>specific node instance</strong> inside a specific live FROG instance.
</p>

<p>
Therefore:
</p>

<ul>
  <li>two different local-state nodes do not share state implicitly,</li>
  <li>two different sub-FROG instances do not share local state implicitly,</li>
  <li>duplicating a node duplicates its local state,</li>
  <li>reusing the same FROG as a sub-FROG in multiple places creates distinct state per instantiated node graph.</li>
</ul>

<p>
The exact lifetime of a live FROG instance may depend on the active runtime profile.
However, within one live instance, the meaning of local state MUST remain stable and deterministic.
</p>

<hr/>

<h2 id="cycles-in-the-diagram">7. Cycles in the Diagram</h2>

<p>
A directed cycle exists when a path of directed edges leads from a node back to itself.
</p>

<p>
Examples:
</p>

<pre>
A → B → C → A
</pre>

<p>
or:
</p>

<pre>
A → A
</pre>

<p>
In a pure dataflow system, a cycle with no memory creates an unresolved dependency loop.
Such a loop does not define valid executable behavior by itself.
</p>

<p>
Therefore, FROG must distinguish between:
</p>

<ul>
  <li><strong>invalid combinational cycles</strong> — cycles containing no local state,</li>
  <li><strong>valid stateful cycles</strong> — cycles containing explicit local state.</li>
</ul>

<hr/>

<h2 id="cycle-validity-rule">8. Cycle Validity Rule</h2>

<p>
The base rule of FROG v0.1 is:
</p>

<pre>
A diagram MAY contain directed cycles.

Every directed cycle MUST contain at least one local-state function.
</pre>

<p>
Equivalent interpretation:
</p>

<ul>
  <li>a cycle without local state is invalid,</li>
  <li>a cycle containing at least one local-state function is valid in principle, subject to ordinary type and graph validation.</li>
</ul>

<p>
This rule applies both to:
</p>

<ul>
  <li>multi-node cycles,</li>
  <li>self-feedback cycles.</li>
</ul>

<p>
A validator MAY implement this rule through strongly connected component analysis or any equivalent graph-theoretic method.
</p>

<hr/>

<h2 id="standard-local-state-function-for-v01">9. Standard Local-State Function for v0.1</h2>

<p>
The minimal standard local-state function recommended for FROG v0.1 is:
</p>

<pre>
frog.core.delay
</pre>

<p>
Its conceptual purpose is:
</p>

<pre>
output current stored value
then store current input for the next activation
</pre>

<p>
Recommended conceptual signature:
</p>

<ul>
  <li>input port: <code>next</code></li>
  <li>output port: <code>previous</code></li>
</ul>

<p>
Recommended state equation:
</p>

<pre>
previous(t) = state(t)
state(t + 1) = next(t)
</pre>

<p>
This function is sufficient to make feedback paths explicit and valid.
</p>

<hr/>

<h2 id="initial-state-semantics">10. Initial State Semantics</h2>

<p>
A local-state function MUST have a deterministic initial state.
</p>

<p>
For <code>frog.core.delay</code>, the recommended source form is an explicit serialized initial value.
</p>

<p>
Illustrative node shape:
</p>

<pre><code>{
  "id": "delay_1",
  "kind": "primitive",
  "type": "frog.core.delay",
  "initial": 0.0
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li>if an <code>initial</code> value is serialized, it MUST be compatible with the function state type,</li>
  <li>if an <code>initial</code> value is omitted, the active library definition or active profile MUST define a deterministic default,</li>
  <li>if neither an explicit initial value nor a deterministic profile-defined default exists, validation MUST fail.</li>
</ul>

<p>
FROG v0.1 does not permit undefined initial state.
</p>

<hr/>

<h2 id="execution-semantics">11. Execution Semantics</h2>

<p>
A local-state function participates in the diagram as an ordinary executable node, but with additional state-update semantics.
</p>

<p>
For <code>frog.core.delay</code>, the conceptual execution model is:
</p>

<ol>
  <li>read the current stored state,</li>
  <li>expose that value on the output,</li>
  <li>capture the current input as the next stored state.</li>
</ol>

<p>
The intended observable meaning is:
</p>

<pre>
the output seen at activation t is the state that existed before the update of activation t
</pre>

<p>
This preserves the expected feedback behavior used in control systems, filtering, accumulation, and iterative processes.
</p>

<p>
The exact internal scheduler implementation may vary between runtimes, but the observable semantics MUST remain equivalent.
</p>

<hr/>

<h2 id="determinism-and-validation">12. Determinism and Validation</h2>

<p>
Implementations MUST enforce the following rules:
</p>

<ul>
  <li>every directed cycle MUST contain at least one local-state function,</li>
  <li>all ordinary value connections through local-state functions MUST remain type-compatible according to <code>Expression/Type.md</code>,</li>
  <li>the initial state of every local-state function MUST be deterministic,</li>
  <li>local state MUST be scoped to the node instance, not implicitly shared across unrelated nodes or sub-FROG instances.</li>
</ul>

<p>
For <code>frog.core.delay</code> specifically:
</p>

<ul>
  <li><code>next</code> and <code>previous</code> MUST have the same type,</li>
  <li>the serialized <code>initial</code> value, when present, MUST be compatible with that type.</li>
</ul>

<p>
Tools SHOULD additionally warn when:
</p>

<ul>
  <li>a cycle contains more local-state functions than necessary and may be difficult to understand,</li>
  <li>feedback is valid but visually unclear,</li>
  <li>a local-state function is used with a profile-dependent implicit initial state rather than an explicit serialized one.</li>
</ul>

<hr/>

<h2 id="examples">13. Examples</h2>

<h3>13.1 Invalid cycle without local state</h3>

<pre><code>"diagram": {
  "nodes": [
    { "id": "a", "kind": "primitive", "type": "frog.core.add" },
    { "id": "b", "kind": "primitive", "type": "frog.core.mul" }
  ],
  "edges": [
    { "id": "e1", "from": { "node": "a", "port": "result" }, "to": { "node": "b", "port": "x" } },
    { "id": "e2", "from": { "node": "b", "port": "result" }, "to": { "node": "a", "port": "x" } }
  ]
}</code></pre>

<p>
This graph is invalid because the cycle contains no local-state function.
</p>

<h3>13.2 Valid cycle with <code>frog.core.delay</code></h3>

<pre><code>"diagram": {
  "nodes": [
    { "id": "input_x", "kind": "interface_input", "interface_port": "x" },
    { "id": "add_1", "kind": "primitive", "type": "frog.core.add" },
    { "id": "delay_1", "kind": "primitive", "type": "frog.core.delay", "initial": 0.0 },
    { "id": "output_y", "kind": "interface_output", "interface_port": "y" }
  ],
  "edges": [
    { "id": "e1", "from": { "node": "input_x", "port": "value" }, "to": { "node": "add_1", "port": "a" } },
    { "id": "e2", "from": { "node": "delay_1", "port": "previous" }, "to": { "node": "add_1", "port": "b" } },
    { "id": "e3", "from": { "node": "add_1", "port": "result" }, "to": { "node": "delay_1", "port": "next" } },
    { "id": "e4", "from": { "node": "add_1", "port": "result" }, "to": { "node": "output_y", "port": "value" } }
  ]
}</code></pre>

<p>
This graph is valid because the feedback cycle is broken by <code>frog.core.delay</code>.
</p>

<h3>13.3 Accumulator intuition</h3>

<p>
Conceptually:
</p>

<pre>
sum(t) = x(t) + sum(t - 1)
</pre>

<p>
One valid graphical realization is:
</p>

<pre>
x → add → y
     ^    |
     |    v
   delay ←
</pre>

<h3>13.4 Self-feedback with local state</h3>

<p>
A self-loop may be valid only if the looped node is itself a local-state function or if the self-loop path contains one.
</p>

<p>
Example intuition:
</p>

<pre>
delay.previous → delay.next
</pre>

<p>
This remains meaningful only because <code>delay</code> defines explicit local-state semantics.
</p>

<hr/>

<h2 id="out-of-scope">14. Out of Scope for v0.1</h2>

<p>
The following topics are outside the strict scope of this document in v0.1:
</p>

<ul>
  <li>global shared state mechanisms,</li>
  <li>distributed shared memory,</li>
  <li>multi-writer shared mutable references,</li>
  <li>full actor-style state models,</li>
  <li>persistent state serialization across process restarts,</li>
  <li>advanced state rollback, checkpointing, or transactional semantics,</li>
  <li>automatic inference of hidden memory inside otherwise stateless functions.</li>
</ul>

<hr/>

<h2 id="summary">15. Summary</h2>

<p>
FROG allows feedback in executable graphs, but only through explicit local state.
</p>

<p>
This specification establishes that:
</p>

<ul>
  <li>some functions are <strong>local-state functions</strong>,</li>
  <li>local state belongs to a node instance,</li>
  <li>cycles are valid only when they include explicit local state,</li>
  <li><code>frog.core.delay</code> is the minimal standard local-state function recommended for v0.1,</li>
  <li>local-state initialization and behavior must remain deterministic.</li>
</ul>

<p>
This provides the semantic foundation needed for feedback paths, accumulation, filtering, control systems, and future stateful language features while keeping the FROG dataflow model explicit, verifiable, and predictable.
</p>

<hr/>

<p align="center">
End of FROG State and Cycles Specification
</p>
