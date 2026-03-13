<h1 align="center">🐸 FROG Control Structures Specification</h1>

<p align="center">
  Source-facing representation of control structures in FROG programs<br/>
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
  <li><a href="#interaction-with-local-memory-and-cycles">15. Interaction with Local Memory and Cycles</a></li>
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
These behaviors are represented by control structures.
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
  <li>a canonical source representation that maps to standardized execution semantics.</li>
</ul>

<p>
FROG v0.1 keeps concrete loop forms explicit.
Therefore, the language standardizes <code>case</code>, <code>for_loop</code>, and <code>while_loop</code> as distinct visible structures rather than collapsing them into one generic hidden form.
</p>

<p>
In FROG, boolean conditional branching and multi-branch textual selection are both represented canonically by the same <code>case</code> structure family.
A boolean <code>case</code> is the canonical source-level equivalent of a traditional <code>if / else</code>.
There is no separate canonical <code>if</code> structure in base v0.1.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Clarity</strong> — distinguish ordinary computation from language-level structural control.</li>
  <li><strong>Canonical source stability</strong> — provide one durable source shape for structure nodes.</li>
  <li><strong>Readability</strong> — keep branch selection and loop intent visually explicit.</li>
  <li><strong>Structural explicitness</strong> — make structure boundaries, terminals, and regions first-class in canonical source.</li>
  <li><strong>Extensibility</strong> — allow future structure families without redefining the foundations.</li>
  <li><strong>Compatibility with graphical practice</strong> — remain understandable to users familiar with established graphical dataflow environments.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This document complements the following specifications:
</p>

<ul>
  <li><code>Expression/Readme.md</code> — defines the role of <code>Expression/</code> as the canonical source-specification layer.</li>
  <li><code>Language/Readme.md</code> — defines the role of <code>Language/</code> as the normative execution-semantics layer.</li>
  <li><code>Language/Control structures.md</code> — defines the normative execution semantics of control structures.</li>
  <li><code>Expression/Diagram.md</code> — defines the executable graph, diagram scopes, node kinds, and structure-node placement in diagrams.</li>
  <li><code>Expression/Type.md</code> — defines type syntax and compatibility.</li>
  <li><code>Expression/State and cycles.md</code> — defines the source-facing representation of explicit local memory and feedback-cycle formation constraints.</li>
  <li><code>Language/State and cycles.md</code> — defines the normative validity rule for cyclic graphs and local memory.</li>
  <li><code>Libraries/Core.md</code> — defines ordinary built-in functions such as <code>frog.core.add</code> and <code>frog.core.delay</code>.</li>
</ul>

<p>
This document defines the canonical source-level representation of control structures.
It does not redefine ordinary function libraries, and it does not redefine the general diagram node model already defined in <code>Expression/Diagram.md</code>.
</p>

<p>
Accordingly:
</p>

<ul>
  <li><code>Expression/Control structures.md</code> owns the canonical source representation of structure nodes,</li>
  <li><code>Language/Control structures.md</code> owns the normative execution meaning of those structures.</li>
</ul>

<p>
When both documents discuss the same structure family, they MUST remain aligned.
However, ownership remains separated between source representation and execution semantics.
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
A control structure is part of the language model itself and has a dedicated canonical source representation.
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

<p>
For usability, tools MAY present a boolean <code>case</code> as <em>If / Else</em> in the UI.
However, the canonical source structure kind remains <code>case</code>.
</p>

<hr/>

<h2 id="canonical-structure-node-model">7. Canonical Structure Node Model</h2>

<p>
Every control structure in canonical source MUST use the following general model:
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

<pre><code>"boundary": {
  "inputs": [
    { "id": "x", "type": "f64" }
  ],
  "outputs": [
    { "id": "y", "type": "f64" }
  ]
}</code></pre>

<h3>8.1 Boundary inputs</h3>

<p>
A boundary input carries a value from the outer graph into the active internal region of the structure.
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

<pre><code>{ "id": "sum_out", "type": "f64", "mode": "last_value", "zero_iteration_value": 0.0 }</code></pre>

<p>
Rules for <code>mode: "last_value"</code>:
</p>

<ul>
  <li>the output represents the value produced for that output by the last completed iteration,</li>
  <li>if zero iterations are possible, the output MUST define a type-compatible <code>zero_iteration_value</code>,</li>
  <li>if zero iterations are impossible under the active validated profile, <code>zero_iteration_value</code> MAY be omitted.</li>
</ul>

<p>
More advanced loop-output modes such as collection, reduction, or profile-defined accumulation are out of scope for base v0.1.
</p>

<h3>8.4 Boundary semantics are explicit</h3>

<p>
A structure boundary is part of canonical executable-graph representation.
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

<pre><code>{
  "type": "bool",
  "outer_visible": true,
  "exposed_in_body": false,
  "read_only": true,
  "role": "selector"
}</code></pre>

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
This document standardizes terminal availability and source representation.
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

<pre><code>{
  "id": "body",
  "diagram": {
    "nodes": [],
    "edges": []
  }
}</code></pre>

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
A <code>case</code> structure selects exactly one executable branch among several internal regions.
</p>

<h3>11.1 Purpose</h3>

<p>
A case structure is used when different executable regions must be selected according to a selector value.
</p>

<p>
In base v0.1, the standardized selector categories are:
</p>

<ul>
  <li><code>bool</code></li>
  <li><code>string</code></li>
</ul>

<p>
This means that a <code>case</code> structure in v0.1 supports:
</p>

<ul>
  <li>boolean conditional execution,</li>
  <li>string-based branch selection.</li>
</ul>

<h3>11.2 Canonical selector terminal</h3>

<p>
A canonical <code>case</code> MUST define one selector terminal named <code>selector</code>.
</p>

<pre><code>"structure_terminals": {
  "selector": {
    "type": "bool",
    "outer_visible": true,
    "exposed_in_body": false,
    "read_only": true,
    "role": "selector"
  }
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>selector</code> MUST exist.</li>
  <li><code>selector.type</code> MUST be either <code>bool</code> or <code>string</code> in base v0.1.</li>
  <li><code>selector.outer_visible</code> MUST be <code>true</code>.</li>
  <li><code>selector.exposed_in_body</code> SHOULD be <code>false</code>.</li>
  <li><code>selector.read_only</code> SHOULD be <code>true</code>.</li>
</ul>

<h3>11.3 Boolean case</h3>

<p>
A boolean case is the canonical source-level equivalent of a classic <code>if / else</code>.
</p>

<p>
If <code>selector.type</code> is <code>bool</code>:
</p>

<ul>
  <li>the structure MUST define exactly two executable regions,</li>
  <li>exactly one region MUST have <code>match: true</code>,</li>
  <li>exactly one region MUST have <code>match: false</code>,</li>
  <li>no default region is required or expected.</li>
</ul>

<p>
Conceptually:
</p>

<pre><code>selector = true  → execute true branch
selector = false → execute false branch</code></pre>

<p>
Tools MAY present this form as an If / Else structure in the UI.
The canonical source remains <code>case</code>.
</p>

<h3>11.4 String case</h3>

<p>
If <code>selector.type</code> is <code>string</code>, the structure performs multi-branch selection using string literals.
</p>

<p>
Rules:
</p>

<ul>
  <li>one or more regions MAY define a string <code>match</code> value,</li>
  <li>every explicit string <code>match</code> value MUST be unique within the structure,</li>
  <li>a string case MUST define exactly one default region,</li>
  <li>if the selector value matches one explicit string literal, the corresponding region executes,</li>
  <li>otherwise the default region executes.</li>
</ul>

<p>
Canonical shape:
</p>

<pre><code>"regions": [
  {
    "id": "case_start",
    "match": "start",
    "diagram": {
      "nodes": [],
      "edges": []
    }
  },
  {
    "id": "case_stop",
    "match": "stop",
    "diagram": {
      "nodes": [],
      "edges": []
    }
  },
  {
    "id": "default_case",
    "default": true,
    "diagram": {
      "nodes": [],
      "edges": []
    }
  }
]</code></pre>

<h3>11.5 Outputs</h3>

<p>
Every executable branch of a <code>case</code> structure MUST define the source representation of every required boundary output.
Normative branch-selection and output-production semantics are defined by <code>Language/Control structures.md</code>.
</p>

<h3>11.6 Region count</h3>

<p>
A <code>case</code> MUST own at least one region, and in practice MUST own:
</p>

<ul>
  <li>exactly two regions for a boolean case,</li>
  <li>one or more matched regions plus exactly one default region for a string case.</li>
</ul>

<h3>11.7 Future extensibility</h3>

<p>
Future revisions or stricter profiles MAY add selector categories such as integers, enums, or pattern-oriented matching.
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

<pre><code>"structure_terminals": {
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
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>count</code> MUST exist.</li>
  <li><code>count.type</code> MUST be <code>i64</code> in base v0.1.</li>
  <li><code>count.outer_visible</code> MUST be <code>true</code>.</li>
  <li><code>index</code> MUST exist.</li>
  <li><code>index.type</code> MUST be <code>i64</code> in base v0.1.</li>
  <li><code>index.exposed_in_body</code> MUST be <code>true</code>.</li>
  <li><code>index.read_only</code> SHOULD be <code>true</code>.</li>
</ul>

<h3>12.3 Count meaning</h3>

<p>
The canonical source representation of <code>for_loop</code> includes an explicit count terminal whose validated value governs iteration count under the normative execution semantics defined in <code>Language/Control structures.md</code>.
</p>

<p>
The canonical iteration index values are:
</p>

<pre><code>0, 1, 2, ..., N - 1</code></pre>

<h3>12.4 Negative counts</h3>

<p>
A negative iteration count is invalid in base v0.1.
Validation MUST reject a <code>for_loop</code> whose resolved count is negative.
</p>

<h3>12.5 Zero iterations</h3>

<p>
If <code>N = 0</code>, the body region is not executed.
In that case, every loop output MUST still have deterministic meaning under the normative loop semantics.
If a loop output uses <code>mode: "last_value"</code> and zero iterations are possible, it MUST define a valid <code>zero_iteration_value</code>.
</p>

<h3>12.6 Regions</h3>

<p>
A canonical <code>for_loop</code> MUST define exactly one region with <code>id: "body"</code>.
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
The canonical v0.1 source model of <code>while_loop</code> assumes the standardized continue-while-true semantics defined by <code>Language/Control structures.md</code>.
</p>

<pre><code>execute body once
continue while condition is true</code></pre>

<p>
Therefore, the base v0.1 <code>while_loop</code> is a post-test loop.
The body executes, then the continuation condition determines whether another iteration occurs.
</p>

<h3>13.3 Canonical terminals</h3>

<pre><code>"structure_terminals": {
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
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>condition</code> MUST exist.</li>
  <li><code>condition.type</code> MUST be <code>bool</code>.</li>
  <li><code>condition.exposed_in_body</code> MUST be <code>true</code>.</li>
  <li><code>condition.outer_visible</code> SHOULD be <code>false</code> in base v0.1.</li>
  <li><code>index</code> MUST exist.</li>
  <li><code>index.type</code> MUST be <code>i64</code> in base v0.1.</li>
  <li><code>index.exposed_in_body</code> MUST be <code>true</code>.</li>
</ul>

<h3>13.4 Continuation meaning</h3>

<p>
After each completed body activation, the continuation condition is resolved from terminal <code>condition</code>.
If it is <code>true</code>, another iteration occurs.
If it is <code>false</code>, the loop terminates.
</p>

<h3>13.5 Regions</h3>

<p>
A canonical <code>while_loop</code> MUST define exactly one region with <code>id: "body"</code>.
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

<p>
The normative execution semantics of control structures are defined by <code>Language/Control structures.md</code>.
This section summarizes the execution interpretation assumed by the canonical source representation defined here.
</p>

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

<p>
For a boolean case, matching is exact on <code>true</code> or <code>false</code>.
For a string case, matching is exact on the string literal values declared by branch regions; otherwise the default region executes.
</p>

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

<h3>14.4 Dataflow and structure interaction</h3>

<p>
A structure remains part of the dataflow graph.
Its external activations and observable outputs remain constrained by the graph and by the structure family semantics.
A structure does not introduce arbitrary instruction ordering outside the standardized rules defined for the language.
</p>

<hr/>

<h2 id="interaction-with-local-memory-and-cycles">15. Interaction with Local Memory and Cycles</h2>

<p>
Control structures do not weaken the general cycle-validity rule of FROG.
A directed cycle is valid only when explicit local memory exists in that cycle.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>a cycle in the outer graph remains subject to the normal explicit-local-memory rule,</li>
  <li>a cycle inside a structure region remains subject to the same explicit-local-memory rule,</li>
  <li>loop repetition by itself is not equivalent to a valid dataflow cycle,</li>
  <li>control structures do not implicitly create hidden memory for graph cycles.</li>
</ul>

<p>
Any directed cycle inside a loop body remains subject to the same rule as any other diagram:
every directed cycle MUST contain at least one explicit local-memory primitive.
In base v0.1, <code>frog.core.delay</code> is the minimal standard primitive used to make such feedback explicit and deterministic.
</p>

<p>
The canonical source-facing representation of such constructs is defined here and in <code>Expression/State and cycles.md</code>.
Their normative execution meaning is defined by <code>Language/State and cycles.md</code>.
</p>

<hr/>

<h2 id="diagram-representation">16. Diagram Representation</h2>

<p>
Control structures are represented in the diagram as nodes of:
</p>

<pre><code>kind = "structure"</code></pre>

<p>
with a valid:
</p>

<pre><code>structure_type = "case" | "for_loop" | "while_loop"</code></pre>

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
  <li>their family-specific structure model.</li>
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
  <li>a <code>case</code> selector MUST use <code>bool</code> or <code>string</code> in base v0.1,</li>
  <li>if a <code>case</code> selector uses <code>bool</code>, exactly one region MUST match <code>true</code> and exactly one region MUST match <code>false</code>,</li>
  <li>if a <code>case</code> selector uses <code>string</code>, each explicit string <code>match</code> value MUST be unique,</li>
  <li>if a <code>case</code> selector uses <code>string</code>, exactly one region MUST define <code>default: true</code>,</li>
  <li>a <code>case</code> structure MUST define every required output for every executable branch,</li>
  <li>a <code>for_loop</code> MUST define a valid count terminal,</li>
  <li>a <code>for_loop</code> count MUST not resolve to a negative iteration count,</li>
  <li>a <code>while_loop</code> MUST define a valid boolean continuation terminal,</li>
  <li>a <code>while_loop</code> MUST use the standardized continue-while-true rule,</li>
  <li>every loop output MUST have deterministic meaning,</li>
  <li>if <code>mode: "last_value"</code> is used and zero iterations are possible, <code>zero_iteration_value</code> MUST be present and type-compatible,</li>
  <li>cycles inside structure regions MUST obey the global local-memory validity rule.</li>
</ul>

<p>
Tools SHOULD additionally warn when:
</p>

<ul>
  <li>loop output meaning is technically valid but visually unclear,</li>
  <li>the use of local memory inside a loop is valid but hard to inspect,</li>
  <li>structure behavior becomes unnecessarily difficult to understand.</li>
</ul>

<hr/>

<h2 id="examples">18. Examples</h2>

<h3>18.1 Boolean case (canonical if / else)</h3>

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
}</code></pre>

<h3>18.2 String case</h3>

<pre><code>{
  "id": "case_2",
  "kind": "structure",
  "structure_type": "case",
  "boundary": {
    "inputs": [],
    "outputs": []
  },
  "structure_terminals": {
    "selector": {
      "type": "string",
      "outer_visible": true,
      "exposed_in_body": false,
      "read_only": true,
      "role": "selector"
    }
  },
  "regions": [
    {
      "id": "case_start",
      "match": "start",
      "diagram": {
        "nodes": [],
        "edges": []
      }
    },
    {
      "id": "case_stop",
      "match": "stop",
      "diagram": {
        "nodes": [],
        "edges": []
      }
    },
    {
      "id": "default_case",
      "default": true,
      "diagram": {
        "nodes": [],
        "edges": []
      }
    }
  ]
}</code></pre>

<h3>18.3 For loop</h3>

<pre><code>{
  "id": "loop_1",
  "kind": "structure",
  "structure_type": "for_loop",
  "boundary": {
    "inputs": [
      { "id": "x", "type": "f64" }
    ],
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
}</code></pre>

<h3>18.4 While loop</h3>

<pre><code>{
  "id": "loop_2",
  "kind": "structure",
  "structure_type": "while_loop",
  "boundary": {
    "inputs": [
      { "id": "x", "type": "f64" }
    ],
    "outputs": [
      { "id": "y", "type": "f64", "mode": "last_value" }
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
}</code></pre>

<hr/>

<h2 id="out-of-scope-for-v01">19. Out of Scope for v0.1</h2>

<ul>
  <li>event structures,</li>
  <li>timed or clock-driven structures,</li>
  <li>parallel-region control structures,</li>
  <li>pattern-matching structures beyond the standardized boolean and string case forms,</li>
  <li>exception-handling structures,</li>
  <li>advanced loop output modes such as implicit collection or generalized reduction,</li>
  <li>hidden automatic memory insertion inside structures.</li>
</ul>

<hr/>

<h2 id="summary">20. Summary</h2>

<p>
FROG treats structural control as an explicit language-level concept, not as a disguised library call.
</p>

<ul>
  <li><code>case</code>, <code>for_loop</code>, and <code>while_loop</code> are the standardized control structures of base v0.1.</li>
  <li>A boolean <code>case</code> is the canonical source-level equivalent of <code>if / else</code>.</li>
  <li>A string <code>case</code> provides canonical multi-branch selection with an explicit required default region.</li>
  <li>Loop structures remain semantically distinct from ordinary functions.</li>
  <li>Structure boundaries, structure terminals, and owned regions are explicit parts of canonical source meaning.</li>
  <li>Control structures do not weaken the explicit-local-memory rule for cycles.</li>
</ul>

<p>
This gives FROG a clear, durable, and visually explicit foundation for structural program control at the source-representation level.
</p>
