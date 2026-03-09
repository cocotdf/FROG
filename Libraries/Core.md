<h1 align="center">🐸 FROG Core Library Specification</h1>

<p align="center">
Definition of the minimal standard <strong>frog.core</strong> library for FROG v0.1<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Goals</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#role-of-frog-core">4. Role of <code>frog.core</code></a></li>
  <li><a href="#naming-and-namespace">5. Naming and Namespace</a></li>
  <li><a href="#scope-for-v01">6. Scope for v0.1</a></li>
  <li><a href="#library-categories">7. Library Categories</a></li>
  <li><a href="#typing-model">8. Typing Model</a></li>
  <li><a href="#arithmetic-functions">9. Arithmetic Functions</a></li>
  <li><a href="#comparison-functions">10. Comparison Functions</a></li>
  <li><a href="#logical-functions">11. Logical Functions</a></li>
  <li><a href="#selection-function">12. Selection Function</a></li>
  <li><a href="#local-state-function">13. Local-State Function</a></li>
  <li><a href="#diagram-representation">14. Diagram Representation</a></li>
  <li><a href="#validation-rules">15. Validation Rules</a></li>
  <li><a href="#examples">16. Examples</a></li>
  <li><a href="#out-of-scope">17. Out of Scope for v0.1</a></li>
  <li><a href="#summary">18. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the minimal standard <strong>frog.core</strong> library for FROG v0.1.
</p>

<p>
The <code>frog.core</code> library contains the smallest set of built-in language functions required to express:
</p>

<ul>
  <li>basic arithmetic,</li>
  <li>basic comparison,</li>
  <li>basic boolean logic,</li>
  <li>simple dataflow selection,</li>
  <li>explicit local memory through delayed feedback.</li>
</ul>

<p>
These functions form the foundational built-in vocabulary of the language.
They are intended to be stable, portable, and always available in conforming FROG implementations.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Minimality</strong> — define a small but usable built-in core.</li>
  <li><strong>Stability</strong> — keep the first standard library surface compact and durable.</li>
  <li><strong>Clarity</strong> — give every function a clear role, stable name, and stable port model.</li>
  <li><strong>Portability</strong> — ensure these functions are expected to exist in every conforming implementation.</li>
  <li><strong>Composability</strong> — provide a solid foundation for higher-level libraries such as <code>frog.math</code>, <code>frog.tensor</code>, <code>frog.signal</code>, or <code>frog.onnx</code>.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This document complements the following specifications:
</p>

<ul>
  <li><strong>Expression/Diagram.md</strong> — defines how built-in functions are serialized as diagram nodes.</li>
  <li><strong>Expression/Type.md</strong> — defines built-in types, type compatibility, and implicit coercion rules.</li>
  <li><strong>Language/State and cycles.md</strong> — defines the semantics of local state and the validity of cycles, including the role of <code>frog.core.delay</code>.</li>
</ul>

<p>
This document defines the standard built-in core function set.
It does not redefine the graph structure or the type system.
</p>

<hr/>

<h2 id="role-of-frog-core">4. Role of <code>frog.core</code></h2>

<p>
The <code>frog.core</code> library is the minimal standard library of the language.
It contains fundamental built-in functions that do not require user-defined dependencies.
</p>

<p>
In language terms, these are called <strong>functions</strong>.
In the serialized diagram representation defined by <code>Expression/Diagram.md</code>, calls to these built-in functions are represented as <code>primitive</code> nodes.
</p>

<p>
Therefore:
</p>

<ul>
  <li><code>frog.core.add</code> is a language-level core function,</li>
  <li>in a diagram, that function call appears as a <code>primitive</code> node with <code>type = "frog.core.add"</code>.</li>
</ul>

<hr/>

<h2 id="naming-and-namespace">5. Naming and Namespace</h2>

<p>
FROG uses the following general namespace pattern for built-in and library-defined functions:
</p>

<pre>
frog.&lt;library&gt;.&lt;function&gt;
</pre>

<p>
For this document:
</p>

<ul>
  <li><code>frog</code> identifies the language namespace,</li>
  <li><code>core</code> identifies the minimal standard core library,</li>
  <li>the final segment identifies the function name.</li>
</ul>

<p>
Examples:
</p>

<pre>
frog.core.add
frog.core.equal
frog.core.select
frog.core.delay
</pre>

<p>
Function names in <code>frog.core</code> SHOULD use lowercase snake_case where multiple words are needed.
</p>

<hr/>

<h2 id="scope-for-v01">6. Scope for v0.1</h2>

<p>
FROG v0.1 standardizes the following minimal core functions:
</p>

<ul>
  <li>arithmetic functions,</li>
  <li>comparison functions,</li>
  <li>boolean logic functions,</li>
  <li>a simple selection function,</li>
  <li>a single explicit local-state function: <code>frog.core.delay</code>.</li>
</ul>

<p>
FROG v0.1 does <strong>not</strong> attempt to define a full mathematical library, tensor library, signal-processing library, control-flow structure catalog, or ONNX operator mapping in this document.
</p>

<hr/>

<h2 id="library-categories">7. Library Categories</h2>

<p>
The minimal <code>frog.core</code> library is organized into the following categories:
</p>

<ul>
  <li><strong>Arithmetic</strong></li>
  <li><strong>Comparison</strong></li>
  <li><strong>Logic</strong></li>
  <li><strong>Selection</strong></li>
  <li><strong>State</strong></li>
</ul>

<p>
This categorization is semantic.
It does not impose a mandatory palette layout, but it provides a stable foundation for IDE organization.
</p>

<hr/>

<h2 id="typing-model">8. Typing Model</h2>

<p>
All <code>frog.core</code> functions are typed according to <strong>Expression/Type.md</strong>.
</p>

<p>
Unless stated otherwise:
</p>

<ul>
  <li>port types MUST be valid FROG types,</li>
  <li>all type compatibility checks MUST follow the standard FROG type rules,</li>
  <li>all implicit coercions MUST follow the standard FROG coercion rules,</li>
  <li>function outputs MUST be deterministic for a given valid input and configuration.</li>
</ul>

<p>
In v0.1:
</p>

<ul>
  <li>all functions in this document are stateless and side-effect-free, except <code>frog.core.delay</code>,</li>
  <li><code>frog.core.delay</code> is stateful and follows <strong>Language/State and cycles.md</strong>.</li>
</ul>

<hr/>

<h2 id="arithmetic-functions">9. Arithmetic Functions</h2>

<h3>9.1 <code>frog.core.add</code></h3>

<p>
Adds two numeric values.
</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
The operands MUST be numeric and type-compatible under the FROG type rules.
The output type is the resolved numeric result type.
</p>

<h3>9.2 <code>frog.core.sub</code></h3>

<p>
Subtracts <code>b</code> from <code>a</code>.
</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>9.3 <code>frog.core.mul</code></h3>

<p>
Multiplies two numeric values.
</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>9.4 <code>frog.core.div</code></h3>

<p>
Divides <code>a</code> by <code>b</code>.
</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
Division by zero behavior MUST be defined by the active execution profile for each supported numeric type family.
The serialized source meaning of the function remains the same.
</p>

<h3>9.5 <code>frog.core.neg</code></h3>

<p>
Arithmetic negation of a numeric value.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>9.6 <code>frog.core.abs</code></h3>

<p>
Absolute value of a numeric input.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<hr/>

<h2 id="comparison-functions">10. Comparison Functions</h2>

<h3>10.1 <code>frog.core.equal</code></h3>

<p>
Returns whether two values are equal.
</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
The output type is <code>bool</code>.
</p>

<p>
In v0.1, equality MUST be supported for built-in scalar types and any other value categories explicitly supported by the active profile.
</p>

<h3>10.2 <code>frog.core.not_equal</code></h3>

<p>
Returns whether two values are not equal.
</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
The output type is <code>bool</code>.
</p>

<h3>10.3 <code>frog.core.less</code></h3>

<p>
Returns whether <code>a &lt; b</code>.
</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
The output type is <code>bool</code>.
In v0.1, this function is defined for numeric operands.
</p>

<h3>10.4 <code>frog.core.less_or_equal</code></h3>

<p>
Returns whether <code>a &lt;= b</code>.
</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>10.5 <code>frog.core.greater</code></h3>

<p>
Returns whether <code>a &gt; b</code>.
</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>10.6 <code>frog.core.greater_or_equal</code></h3>

<p>
Returns whether <code>a &gt;= b</code>.
</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<hr/>

<h2 id="logical-functions">11. Logical Functions</h2>

<h3>11.1 <code>frog.core.and</code></h3>

<p>
Boolean conjunction.
</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
Both inputs MUST be <code>bool</code>.
The output type is <code>bool</code>.
</p>

<h3>11.2 <code>frog.core.or</code></h3>

<p>
Boolean disjunction.
</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>11.3 <code>frog.core.not</code></h3>

<p>
Boolean negation.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>11.4 <code>frog.core.xor</code></h3>

<p>
Boolean exclusive OR.
</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<hr/>

<h2 id="selection-function">12. Selection Function</h2>

<h3>12.1 <code>frog.core.select</code></h3>

<p>
Selects one of two input values based on a boolean condition.
</p>

<ul>
  <li>input ports: <code>condition</code>, <code>true_value</code>, <code>false_value</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li><code>condition</code> MUST be of type <code>bool</code>,</li>
  <li><code>true_value</code> and <code>false_value</code> MUST be type-compatible,</li>
  <li>the output type is the resolved common result type of the two value inputs.</li>
</ul>

<p>
This function is a data selection function.
It is not a general control-flow structure.
</p>

<hr/>

<h2 id="local-state-function">13. Local-State Function</h2>

<h3>13.1 <code>frog.core.delay</code></h3>

<p>
<code>frog.core.delay</code> is the minimal standard local-state function for FROG v0.1.
</p>

<p>
It is the only stateful function defined in this document.
Its semantics are defined jointly by this document and <strong>Language/State and cycles.md</strong>.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>out</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li><code>in</code> and <code>out</code> MUST have the same type,</li>
  <li>every <code>frog.core.delay</code> node MUST define an explicit <code>initial</code> value in v0.1,</li>
  <li><code>initial</code> MUST be compatible with the carried value type.</li>
</ul>

<p>
Conceptual semantics:
</p>

<pre>
out(t) = state(t)
state(t + 1) = in(t)
state(0) = initial
</pre>

<p>
This function enables deterministic and explicit feedback in dataflow graphs.
</p>

<hr/>

<h2 id="diagram-representation">14. Diagram Representation</h2>

<p>
Calls to <code>frog.core</code> functions are serialized as <code>primitive</code> nodes in the diagram.
</p>

<p>
Example:
</p>

<pre><code>{
  "id": "add_1",
  "kind": "primitive",
  "type": "frog.core.add"
}</code></pre>

<p>
Stateful example:
</p>

<pre><code>{
  "id": "delay_1",
  "kind": "primitive",
  "type": "frog.core.delay",
  "initial": 0.0
}</code></pre>

<p>
The exact port existence, direction, and typing of these nodes are resolved from this specification together with the type system and the graph rules.
</p>

<hr/>

<h2 id="validation-rules">15. Validation Rules</h2>

<p>
Implementations MUST enforce the following rules:
</p>

<ul>
  <li>every <code>frog.core</code> function reference MUST identify a valid standardized core function name,</li>
  <li>all required input ports for the referenced function MUST exist and be type-compatible,</li>
  <li>all produced output ports MUST match the function definition,</li>
  <li>all implicit coercions MUST follow <strong>Expression/Type.md</strong>,</li>
  <li>all functions in this document MUST be treated as stateless unless explicitly defined as stateful.</li>
</ul>

<p>
For <code>frog.core.delay</code> specifically:
</p>

<ul>
  <li>the node MUST define <code>initial</code>,</li>
  <li><code>initial</code> MUST be type-compatible with the delay state type,</li>
  <li>the function MUST be treated as a local-state function for cycle validation.</li>
</ul>

<p>
For boolean logic functions:
</p>

<ul>
  <li><code>and</code>, <code>or</code>, <code>not</code>, and <code>xor</code> MUST operate on <code>bool</code> values in v0.1.</li>
</ul>

<p>
For comparison functions:
</p>

<ul>
  <li><code>less</code>, <code>less_or_equal</code>, <code>greater</code>, and <code>greater_or_equal</code> MUST operate on supported ordered types,</li>
  <li>in v0.1, numeric support is required.</li>
</ul>

<hr/>

<h2 id="examples">16. Examples</h2>

<h3>16.1 Addition</h3>

<pre><code>{
  "id": "add_1",
  "kind": "primitive",
  "type": "frog.core.add"
}</code></pre>

<p>
Conceptual ports:
</p>

<pre>
a, b → result
</pre>

<h3>16.2 Boolean selection</h3>

<pre><code>{
  "id": "select_1",
  "kind": "primitive",
  "type": "frog.core.select"
}</code></pre>

<p>
Conceptual ports:
</p>

<pre>
condition, true_value, false_value → result
</pre>

<h3>16.3 Delay</h3>

<pre><code>{
  "id": "delay_1",
  "kind": "primitive",
  "type": "frog.core.delay",
  "initial": 0
}</code></pre>

<p>
Conceptual ports:
</p>

<pre>
in → out
</pre>

<h3>16.4 Feedback with delay</h3>

<pre><code>"diagram": {
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
}</code></pre>

<hr/>

<h2 id="out-of-scope">17. Out of Scope for v0.1</h2>

<p>
The following are outside the strict scope of <code>frog.core</code> in v0.1:
</p>

<ul>
  <li>advanced mathematics such as trigonometry, exponentials, logarithms, or special functions,</li>
  <li>tensor-oriented operators,</li>
  <li>signal-processing operators,</li>
  <li>ONNX operator compatibility catalogs,</li>
  <li>bitwise operators,</li>
  <li>string manipulation functions,</li>
  <li>array, map, or collection transformation libraries,</li>
  <li>control-flow structures such as <code>if</code>, <code>for</code>, <code>while</code>, or <code>loop</code>,</li>
  <li>shared mutable reference models or global-state mechanisms.</li>
</ul>

<hr/>

<h2 id="summary">18. Summary</h2>

<p>
The <code>frog.core</code> library defines the minimal standard built-in function set of FROG v0.1.
</p>

<p>
It provides:
</p>

<ul>
  <li>basic arithmetic,</li>
  <li>basic comparison,</li>
  <li>basic boolean logic,</li>
  <li>simple value selection,</li>
  <li>explicit local-state feedback through <code>frog.core.delay</code>.</li>
</ul>

<p>
This library is intentionally small.
Its purpose is to provide a durable and universal foundation for the language, on top of which richer libraries and higher-level structures may be defined.
</p>

<hr/>

<p align="center">
End of FROG Core Library Specification
</p>
