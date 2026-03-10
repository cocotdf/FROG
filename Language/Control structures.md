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
  <li><a href="#scope-for-v01">5. Scope for v0.1</a></li>
  <li><a href="#standard-control-structures-for-v01">6. Standard Control Structures for v0.1</a></li>
  <li><a href="#canonical-structure-node-model">7. Canonical Structure Node Model</a></li>
  <li><a href="#boundary-model">8. Boundary Model</a></li>
  <li><a href="#structure-terminals">9. Structure Terminals</a></li>
  <li><a href="#regions">10. Regions</a></li>
  <li><a href="#case-structure">11. Case Structure</a></li>
  <li><a href="#for-loop-structure">12. For Loop Structure</a></li>
  <li><a href="#while-loop-structure">13. While Loop Structure</a></li>
  <li><a href="#execution-model">14. Execution Model</a></li>
  <li><a href="#interaction-with-local-state-and-cycles">15. Interaction with Local State and Cycles</a></li>
  <li><a href="#diagram-representation">16. Diagram Representation</a></li>
  <li><a href="#validation-rules">17. Validation Rules</a></li>
  <li><a href="#examples">18. Examples</a></li>
  <li><a href="#out-of-scope-for-v01">19. Out of Scope for v0.1</a></li>
  <li><a href="#summary">20. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
FROG is a graphical dataflow language, but not every program behavior should be represented as an ordinary function call.
Some behaviors are inherently structural: they select one executable region among several, or they repeat execution according to explicit structural rules.
These behaviors are represented by <strong>control structures</strong>.
</p>

<p>
A control structure is not merely a function with inputs and outputs.
It is a structural region of the diagram with:
</p>

<ul>
  <li>an explicit structure kind,</li>
  <li>an explicit boundary,</li>
  <li>explicit structure terminals when required,</li>
  <li>one or more owned executable regions,</li>
  <li>standardized execution semantics.</li>
</ul>

<p>
FROG v0.1 keeps concrete loop forms explicit.
Therefore, the language standardizes <code>case</code>, <code>for_loop</code>, and <code>while_loop</code> as distinct visible structures rather than collapsing them into one generic hidden form.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Clarity</strong> — distinguish ordinary computation from language-level structural control.</li>
  <li><strong>Determinism</strong> — define structural execution without weakening the dataflow model.</li>
  <li><strong>Canonical source stability</strong> — provide one durable source shape for structure nodes.</li>
  <li><strong>Readability</strong> — keep case selection and loop intent visually explicit.</li>
  <li><strong>Extensibility</strong> — allow future structure families without redefining the foundations.</li>
  <li><strong>Compatibility with graphical practice</strong> — remain understandable to users familiar with established graphical dataflow environments.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This document complements the following specifications:
</p>

<ul>
  <li><code>Expression/Diagram.md</code> — defines the executable graph, diagram scopes, node kinds, and structure-node placement in diagrams.</li>
  <li><code>Expression/Type.md</code> — defines type syntax and compatibility.</li>
  <li><code>Language/State and cycles.md</code> — defines local memory and the validity rule for cyclic graphs.</li>
  <li><code>Libraries/Core.md</code> — defines ordinary built-in functions such as <code>frog.core.add</code> and <code>frog.core.delay</code>.</li>
</ul>

<p>
This document defines the semantics of control structures.
It does not redefine ordinary function libraries, and it does not redefine the general diagram node model already defined in <code>Diagram.md</code>.
</p>

<p>
In v0.1, the canonical source form of control structures is standardized here normatively.
It is not merely illustrative.
</p>

<hr/>

<h2 id="functions-vs-control-structures">4. Functions vs Control Structures</h2>

<p>
FROG distinguishes between:
</p>

<ul>
  <li><strong>functions</strong> — callable operations such as <code>frog.core.add</code> or <code>frog.core.delay</code>,</li>
  <li><strong>control structures</strong> — structural regions such as <code>case</code>, <code>for_loop</code>, and <code>while_loop</code>.</li>
</ul>

<p>
A function is evaluated according to its port signature and function semantics.
A control structure owns one or more internal executable regions and defines how those regions are selected, repeated, or otherwise governed.
</p>

<p>
Example:
</p>

<ul>
  <li><code>frog.core.select</code> is a function that selects one value among inputs,</li>
  <li>a <code>case</code> structure selects one executable region among multiple branches.</li>
</ul>

<p>
This distinction is fundamental.
A control structure is part of the language execution model itself.
</p>

<hr/>

<h2 id="scope-for-v01">5. Scope for v0.1</h2>

<p>
FROG v0.1 standardizes the following control structures:
</p>

<ul>
  <li><code>case</code></li>
  <li><code>for_loop</code></li>
  <li><code>while_loop</code></li>
</ul>

<p>
FROG v0.1 does not standardize event structures, timed structures, parallel-region structures, pattern-match structures, or exception-handling structures.
Those MAY be introduced later as their own structure families.
</p>

<hr/>

<h2 id="standard-control-structures-for-v01">6. Standard Control Structures for v0.1</h2>

<p>
The standard structure kinds for FROG v0.1 are:
</p>

<ul>
  <li><code>case</code></li>
  <li><code>for_loop</code></li>
  <li><code>while_loop</code></li>
</ul>

<p>
These are language structures, not library functions.
Tools SHOULD present them as dedicated structural elements in the diagram editor rather than as ordinary primitive nodes.
</p>

<hr/>

<h2 id="canonical-structure-node-model">7. Canonical Structure Node Model</h2>

<p>
Every control structure in canonical source MUST use the following general model:
</p>

<pre>
{
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
}
</pre>

<p>
Field meaning:
</p>

<ul>
  <li><code>id</code> — unique structure node identifier within the owning diagram scope,</li>
  <li><code>kind</code> — MUST be <code>"structure"</code>,</li>
  <li><code>structure_type</code> — MUST be a valid structure family such as <code>case</code>, <code>for_loop</code>, or <code>while_loop</code>,</li>
  <li><code>boundary</code> — explicit structure inputs and outputs crossing the structure wall,</li>
  <li><code>structure_terminals</code> — structure-specific terminals such as selector, count, condition, or index,</li>
  <li><code>regions</code> — owned executable regions,</li>
  <li><code>layout</code> — optional editor geometry,</li>
  <li><code>doc</code> — optional structured documentation,</li>
  <li><code>tags</code> — optional structured tags.</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li><code>id</code> MUST exist.</li>
  <li><code>kind</code> MUST exist and MUST equal <code>"structure"</code>.</li>
  <li><code>structure_type</code> MUST exist.</li>
  <li><code>boundary</code> MUST exist and MUST be valid for the selected structure type.</li>
  <li><code>structure_terminals</code> MUST exist and MUST be valid for the selected structure type.</li>
  <li><code>regions</code> MUST exist and MUST be valid for the selected structure type.</li>
</ul>

<hr/>

<h2 id="boundary-model">8. Boundary Model</h2>

<p>
The <code>boundary</code> object defines the values that cross the structure wall.
Conceptually, these crossings behave like explicit tunnels.
</p>

<pre>
"boundary": {
  "inputs": [
    { "id": "x", "type": "f64" }
  ],
  "outputs": [
    { "id": "y", "type": "f64" }
  ]
}
</pre>

<h3>8.1 Boundary inputs</h3>

<p>
A boundary input carries a value from the outer graph into the active internal region of the structure.
</p>

<p>
Rules:
</p>

<ul>
  <li><code>boundary.inputs</code> MUST exist and MUST be an array.</li>
  <li>Each input entry MUST define <code>id</code> and <code>type</code>.</li>
  <li>Boundary input identifiers MUST be unique within the structure boundary.</li>
</ul>

<h3>8.2 Boundary outputs</h3>

<p>
A boundary output carries a value from an executed internal region back to the outer graph.
</p>

<p>
Rules:
</p>

<ul>
  <li><code>boundary.outputs</code> MUST exist and MUST be an array.</li>
  <li>Each output entry MUST define <code>id</code> and <code>type</code>.</li>
  <li>Boundary output identifiers MUST be unique within the structure boundary.</li>
</ul>

<h3>8.3 Loop-output metadata</h3>

<p>
For <code>for_loop</code> and <code>while_loop</code>, an output MAY define structure-specific output metadata.
The only standardized loop-output mode in v0.1 is:
</p>

<ul>
  <li><code>mode: "last_value"</code></li>
</ul>

<p>
Example:
</p>

<pre>
{ "id": "sum_out", "type": "f64", "mode": "last_value", "zero_iteration_value": 0.0 }
</pre>

<p>
Rules for <code>mode: "last_value"</code>:
</p>

<ul>
  <li>the output represents the value produced for that output by the last completed iteration,</li>
  <li>if zero iterations are possible, the output MUST define a type-compatible <code>zero_iteration_value</code>,</li>
  <li>if zero iterations are impossible under the active validated profile, <code>zero_iteration_value</code> MAY be omitted.</li>
</ul>

<p>
More advanced loop-output modes such as collection, reduction, or profile-specific accumulation are out of scope for base v0.1.
</p>

<h3>8.4 Boundary semantics are explicit</h3>

<p>
A structure boundary is part of the executable meaning of the program.
The structure wall MUST NOT be treated as a purely visual editor artifact.
</p>

<hr/>

<h2 id="structure-terminals">9. Structure Terminals</h2>

<p>
The <code>structure_terminals</code> object contains terminals that are intrinsic to the structure family rather than ordinary boundary tunnels.
</p>

<p>
Examples include:
</p>

<ul>
  <li>a case selector,</li>
  <li>a for-loop count terminal,</li>
  <li>a while-loop continuation terminal,</li>
  <li>an iteration index exposed inside a loop body.</li>
</ul>

<p>
A canonical terminal object SHOULD use the following fields when relevant:
</p>

<pre>
{
  "type": "bool",
  "outer_visible": true,
  "exposed_in_body": false,
  "read_only": true,
  "role": "selector"
}
</pre>

<p>
Field meaning:
</p>

<ul>
  <li><code>type</code> — terminal type, required,</li>
  <li><code>outer_visible</code> — whether the terminal appears as an external structure port,</li>
  <li><code>exposed_in_body</code> — whether the terminal is visible inside the owned region body,</li>
  <li><code>read_only</code> — whether body logic may only read the terminal value,</li>
  <li><code>role</code> — optional semantic role label.</li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>every standardized terminal MUST define <code>type</code>,</li>
  <li>terminal semantics MUST be determined by the structure family,</li>
  <li>terminals MUST NOT be confused with ordinary boundary values.</li>
</ul>

<p>
This document standardizes terminal availability and semantics.
It does not require v0.1 to freeze one universal low-level nested-region reference encoding for consuming those terminals inside region-local diagrams.
</p>

<hr/>

<h2 id="regions">10. Regions</h2>

<p>
The <code>regions</code> array contains the executable regions owned by the structure.
Each region contains a local diagram scope.
</p>

<p>
General region shape:
</p>

<pre>
{
  "id": "body",
  "diagram": {
    "nodes": [],
    "edges": []
  }
}
</pre>

<p>
Rules:
</p>

<ul>
  <li><code>regions</code> MUST be an array.</li>
  <li>Each region MUST define <code>id</code>.</li>
  <li>Each region MUST define <code>diagram</code>.</li>
  <li>Each region identifier MUST be unique within the owning structure.</li>
  <li>Each region-local diagram MUST itself be a valid FROG diagram scope.</li>
</ul>

<p>
A structure MAY own one region or multiple regions depending on its family:
</p>

<ul>
  <li>a <code>case</code> structure owns multiple branch regions,</li>
  <li>a <code>for_loop</code> owns one body region,</li>
  <li>a <code>while_loop</code> owns one body region.</li>
</ul>

<hr/>

<h2 id="case-structure">11. Case Structure</h2>

<p>
A <code>case</code> structure selects exactly one executable branch among multiple internal regions.
</p>

<h3>11.1 Purpose</h3>

<p>
A case structure is used when different executable regions must be selected according to a selector value.
</p>

<h3>11.2 v0.1 minimal canonical form</h3>

<p>
The minimal required canonical case form in v0.1 is a boolean two-branch case.
</p>

<p>
Therefore, a canonical v0.1 <code>case</code> MUST define:
</p>

<ul>
  <li>one selector terminal named <code>selector</code>,</li>
  <li>exactly two regions,</li>
  <li>one region matching <code>true</code>,</li>
  <li>one region matching <code>false</code>.</li>
</ul>

<h3>11.3 Selector terminal</h3>

<pre>
"structure_terminals": {
  "selector": {
    "type": "bool",
    "outer_visible": true,
    "exposed_in_body": false,
    "read_only": true,
    "role": "selector"
  }
}
</pre>

<p>
Rules:
</p>

<ul>
  <li><code>selector</code> MUST exist.</li>
  <li><code>selector.type</code> MUST be <code>bool</code> in base v0.1.</li>
  <li><code>selector.outer_visible</code> MUST be <code>true</code>.</li>
</ul>

<h3>11.4 Regions</h3>

<p>
Each case region MUST define a <code>match</code> value.
</p>

<p>
Canonical shape:
</p>

<pre>
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
</pre>

<p>
Rules:
</p>

<ul>
  <li>exactly one region MUST have <code>match: true</code>,</li>
  <li>exactly one region MUST have <code>match: false</code>,</li>
  <li>at a given activation, exactly one case region executes.</li>
</ul>

<h3>11.5 Output completeness</h3>

<p>
Every required case output MUST be defined for every executable branch.
If a required boundary output is missing from any reachable branch, validation MUST fail.
</p>

<h3>11.6 Future extensibility</h3>

<p>
Future revisions or stricter profiles MAY add integer, enum, or pattern-like selectors.
Such extensions MUST preserve the principle that one activation executes exactly one selected region.
</p>

<hr/>

<h2 id="for-loop-structure">12. For Loop Structure</h2>

<p>
A <code>for_loop</code> executes one body region a predetermined number of times.
</p>

<h3>12.1 Purpose</h3>

<p>
A for loop is used when the iteration count is explicit and bounded by a count value.
</p>

<h3>12.2 Canonical terminals</h3>

<pre>
"structure_terminals": {
  "count": {
    "type": "i64",
    "outer_visible": true,
    "exposed_in_body": false,
    "read_only": true,
    "role": "count"
  },
  "index": {
    "type": "i64",
    "outer_visible": false,
    "exposed_in_body": true,
    "read_only": true,
    "role": "index"
  }
}
</pre>

<p>
Rules:
</p>

<ul>
  <li><code>count</code> MUST exist.</li>
  <li><code>count.type</code> MUST be <code>i64</code> in base v0.1.</li>
  <li><code>count.outer_visible</code> MUST be <code>true</code>.</li>
  <li><code>index</code> MAY exist.</li>
  <li>if <code>index</code> exists, it MUST be read-only and body-visible.</li>
</ul>

<h3>12.3 Count semantics</h3>

<p>
If the resolved count value is <code>N</code>, the body executes exactly <code>N</code> times.
</p>

<p>
Rules:
</p>

<ul>
  <li><code>N</code> MUST be interpreted as a non-negative iteration count,</li>
  <li>a negative resolved count is invalid at execution time,</li>
  <li>if the count is statically known to be negative, validation MUST fail.</li>
</ul>

<h3>12.4 Iteration index</h3>

<p>
If exposed, the iteration index is zero-based.
Therefore, successive iterations observe:
</p>

<pre>
0, 1, 2, ..., N - 1
</pre>

<h3>12.5 Zero iterations</h3>

<p>
If <code>N = 0</code>, the body region is not executed.
In that case, every loop output MUST still have deterministic meaning.
If a loop output uses <code>mode: "last_value"</code> and zero iterations are possible, it MUST define a valid <code>zero_iteration_value</code>.
</p>

<h3>12.6 Regions</h3>

<p>
A canonical <code>for_loop</code> MUST define exactly one region with <code>id: "body"</code>.
</p>

<pre>
"regions": [
  {
    "id": "body",
    "diagram": {
      "nodes": [],
      "edges": []
    }
  }
]
</pre>

<h3>12.7 Distinction from ordinary functions</h3>

<p>
A for loop is not reducible to one ordinary function call.
It governs repeated execution of a structural region.
</p>

<hr/>

<h2 id="while-loop-structure">13. While Loop Structure</h2>

<p>
A <code>while_loop</code> executes one body region repeatedly according to an explicit continuation condition.
</p>

<h3>13.1 Purpose</h3>

<p>
A while loop is used when repetition is condition-driven rather than count-driven.
</p>

<h3>13.2 Canonical continuation rule</h3>

<p>
The canonical v0.1 meaning of <code>while_loop</code> is:
</p>

<pre>
execute body once
continue while condition is true
</pre>

<p>
Therefore, the base v0.1 <code>while_loop</code> is a <strong>post-test loop</strong>.
The body executes, then the continuation condition determines whether another iteration occurs.
</p>

<h3>13.3 Canonical terminals</h3>

<pre>
"structure_terminals": {
  "condition": {
    "type": "bool",
    "outer_visible": false,
    "exposed_in_body": true,
    "read_only": false,
    "role": "continue_while_true"
  },
  "index": {
    "type": "i64",
    "outer_visible": false,
    "exposed_in_body": true,
    "read_only": true,
    "role": "index"
  }
}
</pre>

<p>
Rules:
</p>

<ul>
  <li><code>condition</code> MUST exist.</li>
  <li><code>condition.type</code> MUST be <code>bool</code>.</li>
  <li><code>condition.outer_visible</code> MUST be <code>false</code> in base v0.1.</li>
  <li><code>condition.exposed_in_body</code> MUST be <code>true</code>.</li>
  <li><code>index</code> MAY exist.</li>
</ul>

<h3>13.4 Condition semantics</h3>

<p>
The loop body MUST define the continuation condition in a visible and deterministic way according to the active validated program model.
</p>

<p>
The meaning of the condition role in base v0.1 is:
</p>

<ul>
  <li><code>true</code> — another iteration MUST occur,</li>
  <li><code>false</code> — the loop MUST terminate after the current iteration.</li>
</ul>

<h3>13.5 Regions</h3>

<p>
A canonical <code>while_loop</code> MUST define exactly one region with <code>id: "body"</code>.
</p>

<pre>
"regions": [
  {
    "id": "body",
    "diagram": {
      "nodes": [],
      "edges": []
    }
  }
]
</pre>

<h3>13.6 Loop outputs</h3>

<p>
Loop outputs MUST have deterministic meaning after termination.
If a standardized output mode such as <code>last_value</code> is used, its rules MUST be satisfied.
</p>

<h3>13.7 Distinction from for loop</h3>

<p>
A while loop is semantically distinct from a for loop.
A for loop communicates counted iteration.
A while loop communicates condition-governed iteration.
Both remain distinct structure families in v0.1.
</p>

<hr/>

<h2 id="execution-model">14. Execution Model</h2>

<h3>14.1 Case execution</h3>

<p>
For a <code>case</code> structure:
</p>

<ul>
  <li>the selector value is resolved,</li>
  <li>exactly one matching region is chosen,</li>
  <li>only that chosen region executes for the activation,</li>
  <li>the structure outputs are derived from the chosen region.</li>
</ul>

<h3>14.2 For-loop execution</h3>

<p>
For a <code>for_loop</code>:
</p>

<ul>
  <li>the count is resolved,</li>
  <li>the body executes exactly the required number of times,</li>
  <li>the index, if exposed, progresses deterministically from <code>0</code> to <code>N - 1</code>,</li>
  <li>the structure outputs are produced according to their declared output mode.</li>
</ul>

<h3>14.3 While-loop execution</h3>

<p>
For a <code>while_loop</code>:
</p>

<ul>
  <li>the body executes once,</li>
  <li>the continuation condition is resolved from the body-visible condition terminal,</li>
  <li>another iteration occurs only if that condition is <code>true</code>,</li>
  <li>the structure outputs are produced according to their declared output mode after termination.</li>
</ul>

<h3>14.4 Determinism</h3>

<p>
A control structure MUST have deterministic observable meaning under a validated program and active runtime profile.
The structure wall, branch selection rule, iteration rule, and output meaning MUST remain inspectable and unambiguous.
</p>

<hr/>

<h2 id="interaction-with-local-state-and-cycles">15. Interaction with Local State and Cycles</h2>

<p>
Loops provide repeated execution.
They do not automatically provide hidden memory.
</p>

<p>
Local memory across activations remains the responsibility of local-state primitives such as <code>frog.core.delay</code>.
</p>

<p>
Therefore:
</p>

<ul>
  <li><code>for_loop</code> and <code>while_loop</code> define repetition,</li>
  <li><code>frog.core.delay</code> defines explicit local memory,</li>
  <li>a loop body does not relax the cycle-validity rule of FROG.</li>
</ul>

<p>
Any directed cycle inside a loop body remains subject to the same rule as any other diagram:
every directed cycle MUST contain at least one explicit local-state function.
</p>

<hr/>

<h2 id="diagram-representation">16. Diagram Representation</h2>

<p>
Control structures are represented in the diagram as nodes of:
</p>

<pre>
kind = "structure"
</pre>

<p>
with a valid:
</p>

<pre>
structure_type = "case" | "for_loop" | "while_loop"
</pre>

<p>
Their external ports are resolved from:
</p>

<ul>
  <li><code>boundary.inputs</code>,</li>
  <li><code>boundary.outputs</code>,</li>
  <li>any terminal whose <code>outer_visible</code> value is <code>true</code>.</li>
</ul>

<p>
Their internal region-local semantics are resolved from:
</p>

<ul>
  <li>their owned regions,</li>
  <li>their structure-terminal definitions,</li>
  <li>their family-specific execution rules.</li>
</ul>

<p>
Tools SHOULD present these structures as dedicated visible structural elements rather than disguising them as ordinary primitive functions.
</p>

<hr/>

<h2 id="validation-rules">17. Validation Rules</h2>

<p>
Implementations MUST enforce the following rules:
</p>

<ul>
  <li>every structure node MUST define a valid <code>structure_type</code>,</li>
  <li>every structure node MUST define valid <code>boundary</code>, <code>structure_terminals</code>, and <code>regions</code>,</li>
  <li>all structure boundary crossings MUST be type-compatible,</li>
  <li>every region-local diagram MUST be valid as a local diagram scope,</li>
  <li>a <code>case</code> structure MUST define exactly one <code>true</code> region and exactly one <code>false</code> region in base v0.1,</li>
  <li>a <code>case</code> structure MUST define every required output for every executable branch,</li>
  <li>a <code>for_loop</code> MUST define a valid count terminal,</li>
  <li>a <code>for_loop</code> count MUST not resolve to a negative iteration count,</li>
  <li>a <code>while_loop</code> MUST define a valid boolean continuation terminal,</li>
  <li>a <code>while_loop</code> MUST use the standardized continue-while-true rule,</li>
  <li>every loop output MUST have deterministic meaning,</li>
  <li>if <code>mode: "last_value"</code> is used and zero iterations are possible, <code>zero_iteration_value</code> MUST be present and type-compatible,</li>
  <li>cycles inside structure regions MUST obey the global local-state validity rule.</li>
</ul>

<p>
Tools SHOULD additionally warn when:
</p>

<ul>
  <li>loop output meaning is technically valid but visually unclear,</li>
  <li>the use of local state inside a loop is valid but hard to inspect,</li>
  <li>structure behavior becomes unnecessarily difficult to understand.</li>
</ul>

<hr/>

<h2 id="examples">18. Examples</h2>

<h3>18.1 Canonical boolean case</h3>

<pre>
{
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
      "type": "bool",
      "outer_visible": true,
      "exposed_in_body": false,
      "read_only": true,
      "role": "selector"
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
}
</pre>

<h3>18.2 Canonical for loop</h3>

<pre>
{
  "id": "for_1",
  "kind": "structure",
  "structure_type": "for_loop",
  "boundary": {
    "inputs": [],
    "outputs": [
      { "id": "sum_out", "type": "f64", "mode": "last_value", "zero_iteration_value": 0.0 }
    ]
  },
  "structure_terminals": {
    "count": {
      "type": "i64",
      "outer_visible": true,
      "exposed_in_body": false,
      "read_only": true,
      "role": "count"
    },
    "index": {
      "type": "i64",
      "outer_visible": false,
      "exposed_in_body": true,
      "read_only": true,
      "role": "index"
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
}
</pre>

<h3>18.3 Canonical while loop</h3>

<pre>
{
  "id": "while_1",
  "kind": "structure",
  "structure_type": "while_loop",
  "boundary": {
    "inputs": [],
    "outputs": [
      { "id": "state_out", "type": "f64", "mode": "last_value" }
    ]
  },
  "structure_terminals": {
    "condition": {
      "type": "bool",
      "outer_visible": false,
      "exposed_in_body": true,
      "read_only": false,
      "role": "continue_while_true"
    },
    "index": {
      "type": "i64",
      "outer_visible": false,
      "exposed_in_body": true,
      "read_only": true,
      "role": "index"
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
}
</pre>

<h3>18.4 Conceptual while-loop meaning</h3>

<pre>
execute body
if condition == true:
  repeat
else:
  stop
</pre>

<hr/>

<h2 id="out-of-scope-for-v01">19. Out of Scope for v0.1</h2>

<ul>
  <li>event structures,</li>
  <li>timed structures,</li>
  <li>parallel-region structures,</li>
  <li>exception-handling structures,</li>
  <li>collection and reduction loop-output modes beyond <code>last_value</code>,</li>
  <li>one universal low-level nested-region terminal encoding,</li>
  <li>hidden or implicit memory semantics attached to loops,</li>
  <li>pre-test loop forms distinct from the canonical v0.1 <code>while_loop</code>.</li>
</ul>

<hr/>

<h2 id="summary">20. Summary</h2>

<p>
FROG v0.1 standardizes control structures as explicit language-level structural nodes.
</p>

<ul>
  <li><code>case</code>, <code>for_loop</code>, and <code>while_loop</code> are standardized structure families.</li>
  <li>The canonical structure source form uses <code>kind</code>, <code>structure_type</code>, <code>boundary</code>, <code>structure_terminals</code>, and <code>regions</code>.</li>
  <li>A <code>case</code> selects one executable region.</li>
  <li>A <code>for_loop</code> repeats a body region according to an explicit count.</li>
  <li>A <code>while_loop</code> repeats a body region according to the canonical continue-while-true post-test rule.</li>
  <li>Looping does not introduce hidden memory.</li>
  <li>Any memory across activations remains explicit through local-state primitives such as <code>frog.core.delay</code>.</li>
</ul>

<p>
This provides a clear, durable, and extensible structural foundation for FROG execution graphs.
</p>
