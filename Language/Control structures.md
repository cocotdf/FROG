<h1 align="center">🐸 FROG Control Structures Specification</h1>

<p align="center">
Definition of control structures in FROG programs<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Goals</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#functions-vs-structures">4. Functions vs Control Structures</a></li>
  <li><a href="#role-of-control-structures">5. Role of Control Structures</a></li>
  <li><a href="#scope-for-v01">6. Scope for v0.1</a></li>
  <li><a href="#standard-control-structures-for-v01">7. Standard Control Structures for v0.1</a></li>
  <li><a href="#case-structure">8. Case Structure</a></li>
  <li><a href="#loop-structure">9. Loop Structure</a></li>
  <li><a href="#counted-loop-profile">10. Counted Loop Profile</a></li>
  <li><a href="#conditional-loop-profile">11. Conditional Loop Profile</a></li>
  <li><a href="#tunnels-and-boundary-semantics">12. Tunnels and Boundary Semantics</a></li>
  <li><a href="#iteration-and-local-state">13. Iteration and Local State</a></li>
  <li><a href="#execution-model">14. Execution Model</a></li>
  <li><a href="#diagram-representation">15. Diagram Representation</a></li>
  <li><a href="#validation-rules">16. Validation Rules</a></li>
  <li><a href="#examples">17. Examples</a></li>
  <li><a href="#out-of-scope">18. Out of Scope for v0.1</a></li>
  <li><a href="#summary">19. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
FROG is a graphical dataflow language, but not every program behavior should be expressed as an ordinary function call.
Some language constructs exist to organize execution regions, select subgraphs, or repeat execution under explicit structural rules.
These constructs are called <strong>control structures</strong>.
</p>

<p>
A control structure is not merely a function with inputs and outputs.
It is a structural region of the diagram with its own internal graph, boundary semantics, and execution rules.
</p>

<p>
This document defines the role of control structures in FROG and standardizes the minimal structure set for v0.1.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Separation of concerns</strong> — distinguish ordinary functions from structural language constructs.</li>
  <li><strong>Clarity</strong> — give control structures explicit graphical and semantic meaning.</li>
  <li><strong>Determinism</strong> — define how structural control affects execution without weakening the dataflow model.</li>
  <li><strong>Extensibility</strong> — provide a stable base for richer structures in future revisions.</li>
  <li><strong>Usability</strong> — keep the model compatible with graphical programming expectations, including the intuition familiar from LabVIEW-style structures.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This document complements the following specifications:
</p>

<ul>
  <li><strong>Expression/Diagram.md</strong> — defines the executable graph and node model.</li>
  <li><strong>Expression/Type.md</strong> — defines type compatibility and port typing.</li>
  <li><strong>Language/State and cycles.md</strong> — defines local state and cycle validity inside graphs.</li>
  <li><strong>Libraries/Core.md</strong> — defines ordinary built-in functions such as <code>frog.core.add</code>, <code>frog.core.select</code>, and <code>frog.core.delay</code>.</li>
</ul>

<p>
This document defines control structures as language constructs.
It does not redefine the general notion of function libraries.
</p>

<hr/>

<h2 id="functions-vs-structures">4. Functions vs Control Structures</h2>

<p>
FROG distinguishes between:
</p>

<ul>
  <li><strong>functions</strong> — callable operations such as <code>frog.core.add</code> or <code>frog.core.delay</code>,</li>
  <li><strong>control structures</strong> — structural regions of the diagram such as a case structure or a loop structure.</li>
</ul>

<p>
A function is represented as a node and is evaluated according to its port signature and semantics.
A control structure contains an internal subgraph and defines how that subgraph is selected, repeated, or otherwise structurally governed.
</p>

<p>
Examples:
</p>

<ul>
  <li><code>frog.core.select</code> is a function that chooses between two values,</li>
  <li>a <strong>case structure</strong> is a control structure that selects one executable subgraph among multiple branches.</li>
</ul>

<p>
This distinction is intentional and important.
A control structure is not just a large function.
It is part of the execution structure of the language.
</p>

<hr/>

<h2 id="role-of-control-structures">5. Role of Control Structures</h2>

<p>
Control structures exist to express behaviors that are naturally structural rather than purely functional.
</p>

<p>
Typical examples include:
</p>

<ul>
  <li>choosing one branch among several executable subgraphs,</li>
  <li>executing a region repeatedly,</li>
  <li>introducing explicit iteration boundaries,</li>
  <li>organizing graph regions with semantics that cannot be reduced cleanly to a single ordinary function call.</li>
</ul>

<p>
In FROG, control structures remain part of the graphical language itself.
They are not hidden compiler transformations.
</p>

<hr/>

<h2 id="scope-for-v01">6. Scope for v0.1</h2>

<p>
FROG v0.1 standardizes the following minimal control structure families:
</p>

<ul>
  <li><strong>case structure</strong></li>
  <li><strong>loop structure</strong></li>
</ul>

<p>
FROG v0.1 does not yet attempt to standardize the full catalog of future structures such as event structures, parallel region structures, timed structures, pattern-match structures, or exception-handling structures.
</p>

<hr/>

<h2 id="standard-control-structures-for-v01">7. Standard Control Structures for v0.1</h2>

<p>
The minimal standard control structures for FROG v0.1 are:
</p>

<ul>
  <li><code>case</code></li>
  <li><code>loop</code></li>
</ul>

<p>
These are language structures, not library functions.
They SHOULD appear in the IDE as structural diagram elements rather than as ordinary function nodes.
</p>

<hr/>

<h2 id="case-structure">8. Case Structure</h2>

<p>
A <strong>case structure</strong> selects exactly one executable branch among several internal subgraphs.
</p>

<h3>8.1 Purpose</h3>

<p>
A case structure is used when different executable regions must be selected depending on a control value.
</p>

<p>
Typical uses:
</p>

<ul>
  <li>boolean conditional execution,</li>
  <li>enumerated branch selection,</li>
  <li>multi-case behavior with explicit diagram branches.</li>
</ul>

<h3>8.2 Conceptual model</h3>

<p>
A case structure has:
</p>

<ul>
  <li>a <strong>selector input</strong>,</li>
  <li>one or more named or indexed <strong>cases</strong>,</li>
  <li>an internal subgraph for each case,</li>
  <li>boundary inputs and outputs crossing the structure wall.</li>
</ul>

<h3>8.3 Boolean case</h3>

<p>
The simplest form is a two-branch boolean case:
</p>

<pre>
selector = true  → execute true case
selector = false → execute false case
</pre>

<h3>8.4 Multi-case form</h3>

<p>
Future stricter profiles MAY allow richer selectors such as integers or enums.
The base v0.1 model permits the concept of multiple cases, but boolean case selection is the minimal required form.
</p>

<h3>8.5 Branch exclusivity</h3>

<p>
At a given activation, exactly one case body is executed.
Other case bodies are not executed for that activation.
</p>

<hr/>

<h2 id="loop-structure">9. Loop Structure</h2>

<p>
A <strong>loop structure</strong> executes an internal subgraph repeatedly according to explicit iteration rules.
</p>

<h3>9.1 Purpose</h3>

<p>
A loop structure is used when repeated execution must be expressed structurally rather than through a single feedback cycle alone.
</p>

<p>
Typical uses:
</p>

<ul>
  <li>counted repetition,</li>
  <li>conditional repetition,</li>
  <li>iterative algorithms,</li>
  <li>explicit iteration spaces.</li>
</ul>

<h3>9.2 Conceptual model</h3>

<p>
A loop structure has:
</p>

<ul>
  <li>an internal body graph,</li>
  <li>boundary inputs and outputs,</li>
  <li>iteration semantics,</li>
  <li>optional iteration index exposure,</li>
  <li>optional local-state usage inside the loop body.</li>
</ul>

<p>
A loop structure is not equivalent to a single <code>frog.core.delay</code>.
The delay function provides local memory.
The loop structure provides repeated structural execution.
</p>

<hr/>

<h2 id="counted-loop-profile">10. Counted Loop Profile</h2>

<p>
One important loop form is a <strong>counted loop</strong>.
In this form, the structure executes its body a specified number of times.
</p>

<h3>10.1 Conceptual inputs</h3>

<p>
A counted loop conceptually uses:
</p>

<ul>
  <li>a <strong>count</strong> value indicating how many iterations must occur,</li>
  <li>optional boundary values entering the loop body,</li>
  <li>optional iteration index visibility inside the body.</li>
</ul>

<h3>10.2 Iteration index</h3>

<p>
A counted loop MAY expose a zero-based iteration index inside the body.
If exposed, that index is read-only for the body logic.
</p>

<h3>10.3 Zero iterations</h3>

<p>
If the loop count is zero, the body is not executed.
In that case, outputs must still be well-defined according to the structure output rules and the active profile.
</p>

<hr/>

<h2 id="conditional-loop-profile">11. Conditional Loop Profile</h2>

<p>
Another important loop form is a <strong>conditional loop</strong>.
In this form, the structure executes repeatedly until a condition indicates termination.
</p>

<h3>11.1 Conceptual behavior</h3>

<p>
A conditional loop MAY be viewed as:
</p>

<ul>
  <li>execute body,</li>
  <li>evaluate loop continuation or stop condition,</li>
  <li>repeat or terminate.</li>
</ul>

<h3>11.2 Stop rule</h3>

<p>
The exact condition convention used by a conditional loop MUST be explicit in the structure definition or active profile.
For example:
</p>

<ul>
  <li>stop if condition becomes true,</li>
  <li>continue while condition remains true.</li>
</ul>

<p>
FROG v0.1 acknowledges both conceptual models, but a stricter active profile SHOULD choose one canonical convention for editor consistency.
</p>

<hr/>

<h2 id="tunnels-and-boundary-semantics">12. Tunnels and Boundary Semantics</h2>

<p>
Control structures define a graph region boundary.
Values cross this boundary through explicit structure inputs and outputs.
</p>

<p>
Conceptually, these boundary crossings behave like <strong>tunnels</strong>.
</p>

<h3>12.1 Input tunnels</h3>

<p>
An input tunnel carries a value from outside the structure into the active internal subgraph region.
</p>

<h3>12.2 Output tunnels</h3>

<p>
An output tunnel carries a value from the executed internal region back to the outer graph.
</p>

<h3>12.3 Case output completeness</h3>

<p>
For a case structure, every required output tunnel MUST be defined for every executable branch.
Otherwise validation MUST fail unless a stricter profile defines an explicit fallback rule.
</p>

<h3>12.4 Loop output meaning</h3>

<p>
For a loop structure, output tunnels conceptually expose values derived from loop completion.
The exact mapping may depend on whether the output represents:
</p>

<ul>
  <li>the last produced value,</li>
  <li>a collected sequence,</li>
  <li>a state-carried value.</li>
</ul>

<p>
The base v0.1 model standardizes only the notion that loop outputs are explicit structural outputs and must have deterministic meaning.
More advanced output tunnel modes may be standardized later.
</p>

<hr/>

<h2 id="iteration-and-local-state">13. Iteration and Local State</h2>

<p>
Local-state functions such as <code>frog.core.delay</code> MAY appear inside loop bodies.
</p>

<p>
When they do, their state is local to the node instance inside that loop body instance.
</p>

<p>
This means:
</p>

<ul>
  <li>the loop structure provides repeated execution,</li>
  <li>the local-state function provides memory across those executions.</li>
</ul>

<p>
The two concepts are related but distinct:
</p>

<ul>
  <li><strong>loop</strong> = repeated execution structure,</li>
  <li><strong>delay</strong> = explicit local memory function.</li>
</ul>

<p>
A loop does not automatically imply hidden memory for arbitrary values unless the structure semantics explicitly define such behavior.
</p>

<hr/>

<h2 id="execution-model">14. Execution Model</h2>

<p>
Control structures participate in execution as structural regions of the dataflow graph.
</p>

<h3>14.1 Case execution</h3>

<p>
For a case structure:
</p>

<ul>
  <li>the selector value is resolved,</li>
  <li>exactly one branch is chosen,</li>
  <li>only the chosen branch body is executed for that activation,</li>
  <li>its outputs define the structure outputs.</li>
</ul>

<h3>14.2 Loop execution</h3>

<p>
For a loop structure:
</p>

<ul>
  <li>the body is executed according to the loop iteration rule,</li>
  <li>iteration continues until the loop termination semantics are satisfied,</li>
  <li>the structure outputs are produced according to the loop output semantics.</li>
</ul>

<h3>14.3 Determinism</h3>

<p>
A control structure MUST have deterministic execution meaning under a given validated program and runtime profile.
The structure wall, case selection rule, and loop termination rule MUST remain explicit and inspectable.
</p>

<hr/>

<h2 id="diagram-representation">15. Diagram Representation</h2>

<p>
Control structures are language structures, not ordinary <code>frog.core</code> functions.
</p>

<p>
Therefore, they SHOULD be represented in the program model and IDE as dedicated structural diagram elements rather than as ordinary primitive nodes.
</p>

<p>
FROG v0.1 leaves the exact serialized JSON representation of control structures open, provided that:
</p>

<ul>
  <li>the structural meaning is explicit,</li>
  <li>the internal subgraph is representable,</li>
  <li>boundary inputs and outputs are representable,</li>
  <li>validation and execution semantics remain equivalent to this document.</li>
</ul>

<p>
This deliberate flexibility allows the language to stabilize control structure semantics before freezing a final low-level source encoding.
</p>

<hr/>

<h2 id="validation-rules">16. Validation Rules</h2>

<p>
Implementations MUST enforce the following rules:
</p>

<ul>
  <li>every control structure MUST have a well-defined selector or iteration rule appropriate to its kind,</li>
  <li>every structure boundary input and output MUST be explicitly defined,</li>
  <li>all values crossing structure boundaries MUST be type-compatible,</li>
  <li>a case structure MUST define all required outputs for every executable branch,</li>
  <li>a loop structure MUST define deterministic completion and deterministic output meaning,</li>
  <li>any cycles inside structure bodies MUST still obey <strong>Language/State and cycles.md</strong>.</li>
</ul>

<p>
Additionally:
</p>

<ul>
  <li>a case structure MUST execute exactly one branch per activation,</li>
  <li>a loop structure MUST NOT have undefined termination semantics,</li>
  <li>structure-local ports, indices, or selectors MUST NOT conflict ambiguously with outer graph ports.</li>
</ul>

<hr/>

<h2 id="examples">17. Examples</h2>

<h3>17.1 Boolean case structure</h3>

<p>
Conceptually:
</p>

<pre>
if enabled
  execute true branch
else
  execute false branch
</pre>

<p>
Graphically, this is a structure with:
</p>

<ul>
  <li>a boolean selector,</li>
  <li>a <code>true</code> case body,</li>
  <li>a <code>false</code> case body,</li>
  <li>shared output tunnels.</li>
</ul>

<h3>17.2 Counted loop</h3>

<p>
Conceptually:
</p>

<pre>
repeat body N times
</pre>

<p>
Optionally, the body may see an iteration index:
</p>

<pre>
i = 0, 1, 2, ..., N-1
</pre>

<h3>17.3 Loop with explicit local memory</h3>

<p>
A loop body may contain <code>frog.core.delay</code>:
</p>

<pre>
Loop body:
  input → add → delay → add
</pre>

<p>
In this case:
</p>

<ul>
  <li>the loop provides repeated execution,</li>
  <li>the delay provides local memory across iterations.</li>
</ul>

<h3>17.4 Function vs structure</h3>

<p>
The following are not equivalent:
</p>

<pre>
frog.core.select
</pre>

<p>
and:
</p>

<pre>
case structure
</pre>

<p>
The first selects one of two values.
The second selects one executable subgraph region.
</p>

<hr/>

<h2 id="out-of-scope">18. Out of Scope for v0.1</h2>

<p>
The following topics are outside the strict scope of this document in v0.1:
</p>

<ul>
  <li>event structures,</li>
  <li>parallel for structures,</li>
  <li>timed loop structures,</li>
  <li>exception-handling structures,</li>
  <li>pattern-matching structures beyond minimal case selection,</li>
  <li>fully frozen canonical JSON serialization of all structure internals,</li>
  <li>advanced tunnel modes such as auto-indexing, reduction tunnels, or collected-output policies.</li>
</ul>

<hr/>

<h2 id="summary">19. Summary</h2>

<p>
FROG distinguishes ordinary functions from control structures.
</p>

<p>
This specification establishes that:
</p>

<ul>
  <li><strong>functions</strong> are callable operations such as <code>frog.core.add</code> or <code>frog.core.delay</code>,</li>
  <li><strong>control structures</strong> are structural execution regions such as <code>case</code> and <code>loop</code>,</li>
  <li>a case structure selects one executable branch,</li>
  <li>a loop structure repeats an executable region according to explicit iteration semantics,</li>
  <li>structure boundaries and outputs must remain explicit and type-safe,</li>
  <li>local-state functions may appear inside structures but do not replace them.</li>
</ul>

<p>
This provides the semantic foundation needed to model conditional execution and iterative execution in a way that remains graphical, explicit, and compatible with the FROG dataflow model.
</p>

<hr/>

<p align="center">
End of FROG Control Structures Specification
</p>
