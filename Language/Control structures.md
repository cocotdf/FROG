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
  <li><a href="#functions-vs-control-structures">4. Functions vs Control Structures</a></li>
  <li><a href="#role-of-control-structures">5. Role of Control Structures</a></li>
  <li><a href="#scope-for-v01">6. Scope for v0.1</a></li>
  <li><a href="#standard-control-structures-for-v01">7. Standard Control Structures for v0.1</a></li>
  <li><a href="#canonical-structure-model">8. Canonical Structure Model</a></li>
  <li><a href="#case-structure">9. Case Structure</a></li>
  <li><a href="#for-loop-structure">10. For Loop Structure</a></li>
  <li><a href="#while-loop-structure">11. While Loop Structure</a></li>
  <li><a href="#structural-boundaries-and-tunnels">12. Structural Boundaries and Tunnels</a></li>
  <li><a href="#iteration-semantics-and-local-state">13. Iteration Semantics and Local State</a></li>
  <li><a href="#execution-model">14. Execution Model</a></li>
  <li><a href="#diagram-representation">15. Diagram Representation</a></li>
  <li><a href="#validation-rules">16. Validation Rules</a></li>
  <li><a href="#examples">17. Examples</a></li>
  <li><a href="#out-of-scope-for-v01">18. Out of Scope for v0.1</a></li>
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

<p>
For clarity and graphical readability, FROG v0.1 distinguishes concrete loop forms directly.
Therefore, the language standardizes <strong>case</strong>, <strong>for_loop</strong>, and <strong>while_loop</strong> as explicit control structures rather than exposing only a generic loop form at the language surface.
</p>

<p>
At the same time, FROG defines a common canonical structural envelope so that all present and future structures can be represented consistently in source form.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Separation of concerns</strong> — distinguish ordinary functions from structural language constructs.</li>
  <li><strong>Clarity</strong> — give control structures explicit graphical and semantic meaning.</li>
  <li><strong>Determinism</strong> — define how structural control affects execution without weakening the dataflow model.</li>
  <li><strong>Readability</strong> — make the intent of a structure immediately visible in the diagram.</li>
  <li><strong>Canonical consistency</strong> — define a shared structural source model usable across present and future structure families.</li>
  <li><strong>Extensibility</strong> — provide a stable base for richer structures in future revisions.</li>
  <li><strong>Usability</strong> — remain compatible with graphical programming expectations, including the intuition familiar from LabVIEW-style structures and the semantic distinction commonly found in textual languages such as C, C++, Python, or Rust.</li>
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

<p>
This document defines structure semantics independently from any final low-level JSON encoding.
In other words, the semantic meaning of <code>case</code>, <code>for_loop</code>, and <code>while_loop</code> is standardized here even if the exact serialized internal representation is only partially frozen in v0.1.
</p>

<hr/>

<h2 id="functions-vs-control-structures">4. Functions vs Control Structures</h2>

<p>
FROG distinguishes between:
</p>

<ul>
  <li><strong>functions</strong> — callable operations such as <code>frog.core.add</code> or <code>frog.core.delay</code>,</li>
  <li><strong>control structures</strong> — structural regions of the diagram such as a case structure, a for loop, or a while loop.</li>
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

<p>
This is especially important for loop constructs.
A counted loop and a conditional loop may both belong to the broader conceptual family of iterative structures, but they do not communicate the same intent to the programmer.
For that reason, the canonical language surface keeps them distinct.
</p>

<hr/>

<h2 id="scope-for-v01">6. Scope for v0.1</h2>

<p>
FROG v0.1 standardizes the following minimal control structures:
</p>

<ul>
  <li><strong>case</strong></li>
  <li><strong>for_loop</strong></li>
  <li><strong>while_loop</strong></li>
</ul>

<p>
FROG v0.1 does not yet attempt to standardize the full catalog of future structures such as event structures, parallel region structures, timed structures, pattern-match structures, or exception-handling structures.
</p>

<p>
The notion of a broader <strong>loop family</strong> remains conceptually useful, but canonical source and IDE-facing structure kinds in v0.1 use the explicit concrete forms <code>for_loop</code> and <code>while_loop</code>.
</p>

<hr/>

<h2 id="standard-control-structures-for-v01">7. Standard Control Structures for v0.1</h2>

<p>
The standard control structures for FROG v0.1 are:
</p>

<ul>
  <li><code>case</code></li>
  <li><code>for_loop</code></li>
  <li><code>while_loop</code></li>
</ul>

<p>
These are language structures, not library functions.
They SHOULD appear in the IDE as structural diagram elements rather than as ordinary function nodes.
</p>

<p>
They SHOULD also be presented in the IDE with their own graphical identity, because their role is structural and not merely computational.
</p>

<hr/>

<h2 id="canonical-structure-model">8. Canonical Structure Model</h2>

<p>
All control structures in FROG share a common canonical source model.
This common model is intended to provide long-term consistency across present and future structure families.
</p>

<p>
Recommended canonical shape:
</p>

<pre><code>{
  "id": "struct_1",
  "kind": "structure",
  "structure_type": "case",
  "boundary": {
    "inputs": [],
    "outputs": []
  },
  "structure_terminals": {},
  "regions": [],
  "layout": {},
  "doc": {},
  "tags": []
}</code></pre>

<p>
Common fields:
</p>

<ul>
  <li><code>id</code> — unique structure identifier,</li>
  <li><code>kind</code> — fixed value <code>structure</code>,</li>
  <li><code>structure_type</code> — concrete structure kind such as <code>case</code>, <code>for_loop</code>, or <code>while_loop</code>,</li>
  <li><code>boundary</code> — explicit structure inputs and outputs crossing the wall,</li>
  <li><code>structure_terminals</code> — structure-specific terminals such as selector, count, condition, or index,</li>
  <li><code>regions</code> — internal executable regions owned by the structure,</li>
  <li><code>layout</code> — graphical editor placement and geometry,</li>
  <li><code>doc</code> — optional structured documentation,</li>
  <li><code>tags</code> — optional structured tags.</li>
</ul>

<h3>8.1 Boundary</h3>

<p>
The <code>boundary</code> object describes the explicit values crossing the structure wall.
</p>

<p>
Recommended shape:
</p>

<pre><code>"boundary": {
  "inputs": [
    { "id": "x", "type": "f64" }
  ],
  "outputs": [
    { "id": "y", "type": "f64" }
  ]
}</code></pre>

<h3>8.2 Structure terminals</h3>

<p>
The <code>structure_terminals</code> object contains terminals that are intrinsic to the structure itself rather than ordinary boundary tunnels.
</p>

<p>
Examples:
</p>

<ul>
  <li>a case selector,</li>
  <li>a for-loop count terminal,</li>
  <li>a while-loop condition terminal,</li>
  <li>an iteration index exposed to the body.</li>
</ul>

<h3>8.3 Regions</h3>

<p>
The <code>regions</code> array contains the internal executable regions of the structure.
</p>

<p>
A structure may own:
</p>

<ul>
  <li>multiple regions, such as several case branches, or</li>
  <li>a single body region, such as a for loop or a while loop.</li>
</ul>

<p>
Each region contains its own internal diagram.
</p>

<h3>8.4 Canonical visibility vs semantic extensibility</h3>

<p>
In v0.1, the common structural envelope is standardized conceptually and recommended strongly as the canonical direction.
Stricter profiles MAY refine the precise low-level JSON field set, but they MUST preserve equivalent semantics.
</p>

<hr/>

<h2 id="case-structure">9. Case Structure</h2>

<p>
A <strong>case structure</strong> selects exactly one executable branch among several internal subgraphs.
</p>

<h3>9.1 Purpose</h3>

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

<h3>9.2 Conceptual model</h3>

<p>
A case structure has:
</p>

<ul>
  <li>a <strong>selector terminal</strong>,</li>
  <li>one or more named or indexed <strong>cases</strong>,</li>
  <li>an internal subgraph for each case,</li>
  <li>boundary inputs and outputs crossing the structure wall.</li>
</ul>

<h3>9.3 Boolean case</h3>

<p>
The simplest form is a two-branch boolean case:
</p>

<pre><code>selector = true  → execute true case
selector = false → execute false case</code></pre>

<h3>9.4 Multi-case form</h3>

<p>
Future stricter profiles MAY allow richer selectors such as integers or enums.
The base v0.1 model permits the concept of multiple cases, but boolean case selection is the minimal required form.
</p>

<h3>9.5 Branch exclusivity</h3>

<p>
At a given activation, exactly one case body is executed.
Other case bodies are not executed for that activation.
</p>

<h3>9.6 Canonical structure terminals</h3>

<p>
Recommended structure terminals for a case structure:
</p>

<pre><code>"structure_terminals": {
  "selector": {
    "type": "bool"
  }
}</code></pre>

<h3>9.7 Canonical regions</h3>

<p>
Recommended shape:
</p>

<pre><code>"regions": [
  {
    "id": "true_case",
    "match": true,
    "diagram": {
      "nodes": [],
      "edges": []
    }
  },
  {
    "id": "false_case",
    "match": false,
    "diagram": {
      "nodes": [],
      "edges": []
    }
  }
]</code></pre>

<hr/>

<h2 id="for-loop-structure">10. For Loop Structure</h2>

<p>
A <strong>for loop</strong> executes an internal body graph a predetermined number of times.
</p>

<h3>10.1 Purpose</h3>

<p>
A for loop is used when iteration count is explicit and bounded by a count value.
</p>

<p>
Typical uses:
</p>

<ul>
  <li>counted repetition,</li>
  <li>index-based algorithms,</li>
  <li>fixed iteration spaces,</li>
  <li>collection traversal profiles standardized later by stricter specifications.</li>
</ul>

<h3>10.2 Conceptual model</h3>

<p>
A for loop has:
</p>

<ul>
  <li>a required <strong>count</strong> terminal or equivalent structural count definition,</li>
  <li>an internal body graph,</li>
  <li>boundary inputs and outputs,</li>
  <li>an optional zero-based iteration index exposed inside the body.</li>
</ul>

<h3>10.3 Iteration count</h3>

<p>
The body executes exactly <code>N</code> times when the count is <code>N</code>, subject to successful validation of the structure and its body.
</p>

<h3>10.4 Iteration index</h3>

<p>
A for loop MAY expose a zero-based iteration index inside the body.
If exposed, that index is read-only for the body logic.
</p>

<h3>10.5 Zero iterations</h3>

<p>
If the count is zero, the body is not executed.
In that case, outputs must still be well-defined according to the output rules of the structure and the active profile.
</p>

<h3>10.6 Distinction from ordinary functions</h3>

<p>
A for loop is not reducible to an ordinary function call because it governs repeated execution of a whole structural region, not just the evaluation of a single node.
</p>

<h3>10.7 Canonical structure terminals</h3>

<p>
Recommended structure terminals for a for loop:
</p>

<pre><code>"structure_terminals": {
  "count": {
    "type": "i64"
  },
  "index": {
    "type": "i64",
    "exposed_in_body": true
  }
}</code></pre>

<h3>10.8 Canonical regions</h3>

<p>
Recommended shape:
</p>

<pre><code>"regions": [
  {
    "id": "body",
    "diagram": {
      "nodes": [],
      "edges": []
    }
  }
]</code></pre>

<hr/>

<h2 id="while-loop-structure">11. While Loop Structure</h2>

<p>
A <strong>while loop</strong> executes an internal body graph repeatedly according to an explicit loop condition.
</p>

<h3>11.1 Purpose</h3>

<p>
A while loop is used when repetition is condition-driven rather than count-driven.
</p>

<p>
Typical uses:
</p>

<ul>
  <li>condition-based repetition,</li>
  <li>iterative convergence algorithms,</li>
  <li>polling or wait-until-ready logic under a runtime profile,</li>
  <li>repetition whose final number of iterations is not known in advance.</li>
</ul>

<h3>11.2 Canonical condition rule</h3>

<p>
To avoid ambiguity, the canonical v0.1 meaning of <code>while_loop</code> is:
</p>

<pre><code>continue while condition is true</code></pre>

<p>
This means that the structure repeats as long as the loop condition remains true according to the validated body and boundary semantics.
</p>

<h3>11.3 Conceptual model</h3>

<p>
A while loop has:
</p>

<ul>
  <li>an internal body graph,</li>
  <li>a loop condition defined by the body or by an explicit structure condition terminal,</li>
  <li>boundary inputs and outputs,</li>
  <li>optional iteration index exposure inside the body.</li>
</ul>

<h3>11.4 Termination semantics</h3>

<p>
A while loop MUST have explicit and deterministic termination meaning.
The condition that governs repetition MUST be inspectable and unambiguous in the validated program model.
</p>

<h3>11.5 Initial evaluation model</h3>

<p>
The base v0.1 model does not require this document to freeze every possible low-level scheduler detail, but the observable structure meaning MUST remain equivalent to repeated body execution under the canonical continue-while-true rule.
</p>

<h3>11.6 Distinction from for loop</h3>

<p>
A while loop is semantically distinct from a for loop.
A for loop communicates bounded counted iteration.
A while loop communicates condition-governed iteration.
Both belong to the broader conceptual family of iterative structures, but they remain distinct language structures in FROG v0.1.
</p>

<h3>11.7 Canonical structure terminals</h3>

<p>
Recommended structure terminals for a while loop:
</p>

<pre><code>"structure_terminals": {
  "condition": {
    "type": "bool",
    "role": "continue_while_true"
  },
  "index": {
    "type": "i64",
    "exposed_in_body": true
  }
}</code></pre>

<h3>11.8 Canonical regions</h3>

<p>
Recommended shape:
</p>

<pre><code>"regions": [
  {
    "id": "body",
    "diagram": {
      "nodes": [],
      "edges": []
    }
  }
]</code></pre>

<hr/>

<h2 id="structural-boundaries-and-tunnels">12. Structural Boundaries and Tunnels</h2>

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
For loop structures, output tunnels conceptually expose values derived from loop completion.
The exact mapping may depend on whether the output represents:
</p>

<ul>
  <li>the last produced value,</li>
  <li>a collected sequence,</li>
  <li>a state-carried value,</li>
  <li>another explicitly standardized loop output mode.</li>
</ul>

<p>
The base v0.1 model standardizes only the notion that loop outputs are explicit structural outputs and must have deterministic meaning.
More advanced output tunnel modes may be standardized later.
</p>

<hr/>

<h2 id="iteration-semantics-and-local-state">13. Iteration Semantics and Local State</h2>

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
  <li><strong>for_loop</strong> or <strong>while_loop</strong> = repeated execution structure,</li>
  <li><strong>frog.core.delay</strong> = explicit local memory function.</li>
</ul>

<p>
A loop does not automatically imply hidden memory for arbitrary values unless the structure semantics explicitly define such behavior.
</p>

<p>
Any cycles inside a loop body remain subject to the rules defined by <strong>Language/State and cycles.md</strong>.
A loop body does not relax the validity rule for cyclic graphs.
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

<h3>14.2 For loop execution</h3>

<p>
For a for loop:
</p>

<ul>
  <li>the iteration count is resolved,</li>
  <li>the body executes the required number of times,</li>
  <li>the optional iteration index, if present, changes deterministically from <code>0</code> to <code>N-1</code>,</li>
  <li>the structure outputs are produced according to the loop output semantics.</li>
</ul>

<h3>14.3 While loop execution</h3>

<p>
For a while loop:
</p>

<ul>
  <li>the body executes under the canonical continue-while-true rule,</li>
  <li>repetition continues until termination semantics are satisfied,</li>
  <li>the structure outputs are produced according to the loop output semantics.</li>
</ul>

<h3>14.4 Determinism</h3>

<p>
A control structure MUST have deterministic execution meaning under a given validated program and runtime profile.
The structure wall, case selection rule, loop condition rule, and loop output meaning MUST remain explicit and inspectable.
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
The recommended canonical source direction in v0.1 is:
</p>

<ul>
  <li><code>kind = "structure"</code></li>
  <li><code>structure_type = "case" | "for_loop" | "while_loop"</code></li>
  <li>explicit <code>boundary</code></li>
  <li>explicit <code>structure_terminals</code></li>
  <li>explicit <code>regions</code></li>
</ul>

<p>
Illustrative example:
</p>

<pre><code>{
  "id": "for_1",
  "kind": "structure",
  "structure_type": "for_loop",
  "boundary": {
    "inputs": [
      { "id": "acc_in", "type": "f64" }
    ],
    "outputs": [
      { "id": "acc_out", "type": "f64", "mode": "last_value" }
    ]
  },
  "structure_terminals": {
    "count": {
      "type": "i64"
    },
    "index": {
      "type": "i64",
      "exposed_in_body": true
    }
  },
  "regions": [
    {
      "id": "body",
      "diagram": {
        "nodes": [],
        "edges": []
      }
    }
  ]
}</code></pre>

<p>
FROG v0.1 still leaves room for profile-level refinement of the low-level encoding details, but implementations SHOULD move toward this common structural envelope.
</p>

<p>
A future event structure, if standardized, SHOULD also appear as its own dedicated structural kind rather than being treated as a mere alias or profile of a case or loop structure.
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
  <li>a for loop MUST define deterministic iteration count meaning and deterministic output meaning,</li>
  <li>a while loop MUST define deterministic condition semantics and deterministic output meaning,</li>
  <li>any cycles inside structure bodies MUST still obey <strong>Language/State and cycles.md</strong>.</li>
</ul>

<p>
Additionally:
</p>

<ul>
  <li>a case structure MUST execute exactly one branch per activation,</li>
  <li>a for loop MUST NOT have undefined count semantics,</li>
  <li>a while loop MUST NOT have undefined termination semantics,</li>
  <li>structure-local ports, indices, selectors, or region-level names MUST NOT conflict ambiguously with outer graph ports.</li>
</ul>

<p>
For the canonical structural model:
</p>

<ul>
  <li><code>kind</code> MUST be <code>structure</code> for standardized control structures,</li>
  <li><code>structure_type</code> MUST be one of the standardized structure types supported by the active profile,</li>
  <li><code>boundary.inputs</code> and <code>boundary.outputs</code> MUST be objects or arrays consistent with the active structural encoding profile,</li>
  <li><code>regions</code> MUST exist and MUST contain the executable region definitions required by the structure type,</li>
  <li><code>structure_terminals</code> MUST contain the required structure-specific terminals for the chosen <code>structure_type</code>.</li>
</ul>

<hr/>

<h2 id="examples">17. Examples</h2>

<h3>17.1 Boolean case structure</h3>

<p>
Conceptually:
</p>

<pre><code>if enabled
  execute true branch
else
  execute false branch</code></pre>

<p>
Graphically, this is a structure with:
</p>

<ul>
  <li>a boolean selector,</li>
  <li>a <code>true</code> case body,</li>
  <li>a <code>false</code> case body,</li>
  <li>shared output tunnels.</li>
</ul>

<h3>17.2 Canonical case structure sketch</h3>

<pre><code>{
  "id": "case_1",
  "kind": "structure",
  "structure_type": "case",
  "boundary": {
    "inputs": [
      { "id": "x", "type": "f64" }
    ],
    "outputs": [
      { "id": "y", "type": "f64" }
    ]
  },
  "structure_terminals": {
    "selector": {
      "type": "bool"
    }
  },
  "regions": [
    {
      "id": "true_case",
      "match": true,
      "diagram": {
        "nodes": [],
        "edges": []
      }
    },
    {
      "id": "false_case",
      "match": false,
      "diagram": {
        "nodes": [],
        "edges": []
      }
    }
  ]
}</code></pre>

<h3>17.3 For loop</h3>

<p>
Conceptually:
</p>

<pre><code>repeat body N times</code></pre>

<p>
Optionally, the body may see an iteration index:
</p>

<pre><code>i = 0, 1, 2, ..., N-1</code></pre>

<h3>17.4 Canonical for-loop sketch</h3>

<pre><code>{
  "id": "for_1",
  "kind": "structure",
  "structure_type": "for_loop",
  "boundary": {
    "inputs": [
      { "id": "acc_in", "type": "f64" }
    ],
    "outputs": [
      { "id": "acc_out", "type": "f64", "mode": "last_value" }
    ]
  },
  "structure_terminals": {
    "count": {
      "type": "i64"
    },
    "index": {
      "type": "i64",
      "exposed_in_body": true
    }
  },
  "regions": [
    {
      "id": "body",
      "diagram": {
        "nodes": [],
        "edges": []
      }
    }
  ]
}</code></pre>

<h3>17.5 While loop</h3>

<p>
Conceptually:
</p>

<pre><code>while condition is true
  execute body</code></pre>

<p>
This is the canonical v0.1 semantic rule for <code>while_loop</code>.
</p>

<h3>17.6 Canonical while-loop sketch</h3>

<pre><code>{
  "id": "while_1",
  "kind": "structure",
  "structure_type": "while_loop",
  "boundary": {
    "inputs": [
      { "id": "state_in", "type": "f64" }
    ],
    "outputs": [
      { "id": "state_out", "type": "f64", "mode": "last_value" }
    ]
  },
  "structure_terminals": {
    "condition": {
      "type": "bool",
      "role": "continue_while_true"
    },
    "index": {
      "type": "i64",
      "exposed_in_body": true
    }
  },
  "regions": [
    {
      "id": "body",
      "diagram": {
        "nodes": [],
        "edges": []
      }
    }
  ]
}</code></pre>

<h3>17.7 Loop with explicit local memory</h3>

<p>
A loop body may contain <code>frog.core.delay</code>:
</p>

<pre><code>Loop body:
  input → add → delay → add</code></pre>

<p>
In this case:
</p>

<ul>
  <li>the loop provides repeated execution,</li>
  <li>the delay provides local memory across iterations.</li>
</ul>

<h3>17.8 Function vs structure</h3>

<p>
The following are not equivalent:
</p>

<pre><code>frog.core.select</code></pre>

<p>
and:
</p>

<pre><code>case structure</code></pre>

<p>
The first selects one of two values.
The second selects one executable subgraph region.
</p>

<hr/>

<h2 id="out-of-scope-for-v01">18. Out of Scope for v0.1</h2>

<p>
The following topics are outside the strict scope of this document in v0.1:
</p>

<ul>
  <li><code>event_structure</code>,</li>
  <li>parallel for structures,</li>
  <li>timed loop structures,</li>
  <li>exception-handling structures,</li>
  <li>pattern-matching structures beyond minimal case selection,</li>
  <li>fully frozen canonical JSON serialization of all structure internals,</li>
  <li>advanced tunnel modes such as auto-indexing, reduction tunnels, or collected-output policies.</li>
</ul>

<p>
If an event structure is standardized later, it SHOULD be defined as a dedicated control structure with its own semantics rather than being reduced to a mere combination of more primitive visible structures.
</p>

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
  <li><strong>control structures</strong> are structural execution regions such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>,</li>
  <li>all standardized control structures share a common canonical envelope based on <code>kind</code>, <code>structure_type</code>, <code>boundary</code>, <code>structure_terminals</code>, and <code>regions</code>,</li>
  <li>a case structure selects one executable branch,</li>
  <li>a for loop repeats an executable region according to explicit counted iteration semantics,</li>
  <li>a while loop repeats an executable region according to explicit conditional iteration semantics,</li>
  <li>structure boundaries and outputs must remain explicit and type-safe,</li>
  <li>local-state functions may appear inside structures but do not replace them.</li>
</ul>

<p>
This provides the semantic foundation needed to model conditional execution and iterative execution in a way that remains graphical, explicit, readable, extensible, and compatible with the FROG dataflow model.
</p>

<hr/>

<p align="center">
End of FROG Control Structures Specification
</p>
