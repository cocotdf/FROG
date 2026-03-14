<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="150" />
</p>

<h1 align="center">🐸 FROG Core Library Specification</h1>

<p align="center">
Definition of the minimal standard <code>frog.core</code> library for FROG v0.1<br/>
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
  <li><a href="#local-memory-primitive">13. Local-Memory Primitive</a></li>
  <li><a href="#diagram-representation">14. Diagram Representation</a></li>
  <li><a href="#validation-rules">15. Validation Rules</a></li>
  <li><a href="#examples">16. Examples</a></li>
  <li><a href="#out-of-scope-for-v01">17. Out of Scope for v0.1</a></li>
  <li><a href="#summary">18. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the minimal standard <code>frog.core</code> library for FROG v0.1.
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
  <li><code>Libraries/Readme.md</code> — defines the role of <code>Libraries/</code> as the standard primitive-library layer.</li>
  <li><code>Expression/Diagram.md</code> — defines how built-in functions are serialized as diagram nodes.</li>
  <li><code>Expression/Type.md</code> — defines built-in types, type compatibility, and implicit coercion rules.</li>
  <li><code>Expression/Control structures.md</code> — defines standardized source-facing language structures, which remain distinct from ordinary primitive functions.</li>
  <li><code>Expression/State and cycles.md</code> — defines the source-facing representation of explicit local memory and feedback-cycle construction.</li>
  <li><code>Language/State and cycles.md</code> — defines the normative semantics of local memory and the validity rule for directed cycles.</li>
  <li><code>IDE/Palette.md</code> — defines how core primitives may be exposed in authoring tools.</li>
</ul>

<p>
This document defines the standard built-in core function set.
It does not redefine the graph structure, the type system, the canonical source model, or the cross-cutting semantic rules for valid cycles.
</p>

<table>
  <tr>
    <th align="left">Layer</th>
    <th align="left">Primary ownership for this topic</th>
  </tr>
  <tr>
    <td><code>Expression/</code></td>
    <td>Canonical source representation of primitive nodes and local-memory source form</td>
  </tr>
  <tr>
    <td><code>Language/</code></td>
    <td>Normative execution semantics for local memory and valid cycles</td>
  </tr>
  <tr>
    <td><code>Libraries/</code></td>
    <td>Standardized primitive identities, ports, metadata, and primitive-local semantics</td>
  </tr>
  <tr>
    <td><code>IDE/</code></td>
    <td>Palette, authoring, observability, and debugging exposure</td>
  </tr>
</table>

<p>
Accordingly:
</p>

<ul>
  <li><code>Libraries/Core.md</code> owns the standardized identity and primitive surface of <code>frog.core.*</code> functions,</li>
  <li><code>Language/State and cycles.md</code> owns the normative cross-cutting rules that make cyclic graphs valid or invalid,</li>
  <li><code>Expression/State and cycles.md</code> owns the source-facing representation of that explicit memory in canonical program form.</li>
</ul>

<hr/>

<h2 id="role-of-frog-core">4. Role of <code>frog.core</code></h2>

<p>
The <code>frog.core</code> library is the minimal standard library of the language.
It contains fundamental built-in functions that do not require user-defined dependencies.
</p>

<p>
In language terms, these are called functions.
In the serialized diagram representation defined by <code>Expression/Diagram.md</code>, calls to these built-in functions are represented as <code>primitive</code> nodes.
</p>

<p>
Therefore:
</p>

<ul>
  <li><code>frog.core.add</code> is a language-level core function,</li>
  <li>in a diagram, that function call appears as a <code>primitive</code> node with <code>type = "frog.core.add"</code>.</li>
</ul>

<p>
The role of <code>frog.core</code> is to define the minimal standardized primitive vocabulary required by essentially all FROG programs.
It is not the place where structural control, widget object modeling, or IDE interaction models are defined.
</p>

<hr/>

<h2 id="naming-and-namespace">5. Naming and Namespace</h2>

<p>
FROG uses the following general namespace pattern for built-in and library-defined functions:
</p>

<pre><code>frog.&lt;library&gt;.&lt;function&gt;</code></pre>

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

<pre><code>frog.core.add
frog.core.equal
frog.core.select
frog.core.delay</code></pre>

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
  <li>a single explicit local-memory function: <code>frog.core.delay</code>.</li>
</ul>

<p>
FROG v0.1 does not attempt to define a full mathematical library, tensor library, signal-processing library, control-flow structure catalog, or ONNX operator mapping in this document.
</p>

<hr/>

<h2 id="library-categories">7. Library Categories</h2>

<p>
The minimal <code>frog.core</code> library is organized into the following categories:
</p>

<ul>
  <li>Arithmetic</li>
  <li>Comparison</li>
  <li>Logic</li>
  <li>Selection</li>
  <li>Local Memory</li>
</ul>

<p>
This categorization is semantic.
It does not impose a mandatory palette layout, but it provides a stable foundation for IDE organization.
</p>

<hr/>

<h2 id="typing-model">8. Typing Model</h2>

<p>
All <code>frog.core</code> functions are typed according to <code>Expression/Type.md</code>.
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
  <li><code>frog.core.delay</code> is stateful and MUST be treated as a local-memory primitive,</li>
  <li>the primitive-local delayed-value behavior of <code>frog.core.delay</code> is standardized here,</li>
  <li>the general validity of cycles containing <code>frog.core.delay</code> is governed normatively by <code>Language/State and cycles.md</code>.</li>
</ul>

<hr/>

<h2 id="arithmetic-functions">9. Arithmetic Functions</h2>

<h3>9.1 <code>frog.core.add</code></h3>

<p>Adds two numeric values.</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
The operands MUST be numeric and type-compatible under the FROG type rules.
The output type is the resolved numeric result type.
</p>

<h3>9.2 <code>frog.core.sub</code></h3>

<p>Subtracts <code>b</code> from <code>a</code>.</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>9.3 <code>frog.core.mul</code></h3>

<p>Multiplies two numeric values.</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>9.4 <code>frog.core.div</code></h3>

<p>Divides <code>a</code> by <code>b</code>.</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
Division by zero behavior MUST be defined by the active execution profile for each supported numeric type family.
The standardized primitive identity and primitive meaning of the function remain the same.
</p>

<h3>9.5 <code>frog.core.neg</code></h3>

<p>Arithmetic negation of a numeric value.</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>9.6 <code>frog.core.abs</code></h3>

<p>Absolute value of a numeric input.</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<hr/>

<h2 id="comparison-functions">10. Comparison Functions</h2>

<h3>10.1 <code>frog.core.equal</code></h3>

<p>Returns whether two values are equal.</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
The output type is <code>bool</code>.
In v0.1, equality MUST be supported for built-in scalar types and any other value categories explicitly supported by the active profile.
</p>

<h3>10.2 <code>frog.core.not_equal</code></h3>

<p>Returns whether two values are not equal.</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>The output type is <code>bool</code>.</p>

<h3>10.3 <code>frog.core.less</code></h3>

<p>Returns whether <code>a &lt; b</code>.</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
The output type is <code>bool</code>.
In v0.1, this function is defined for numeric operands.
</p>

<h3>10.4 <code>frog.core.less_or_equal</code></h3>

<p>Returns whether <code>a &lt;= b</code>.</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>10.5 <code>frog.core.greater</code></h3>

<p>Returns whether <code>a &gt; b</code>.</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>10.6 <code>frog.core.greater_or_equal</code></h3>

<p>Returns whether <code>a &gt;= b</code>.</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<hr/>

<h2 id="logical-functions">11. Logical Functions</h2>

<h3>11.1 <code>frog.core.and</code></h3>

<p>Boolean conjunction.</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>Both inputs MUST be <code>bool</code>. The output type is <code>bool</code>.</p>

<h3>11.2 <code>frog.core.or</code></h3>

<p>Boolean disjunction.</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>11.3 <code>frog.core.not</code></h3>

<p>Boolean negation.</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>11.4 <code>frog.core.xor</code></h3>

<p>Boolean exclusive OR.</p>

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

<p>Rules:</p>

<ul>
  <li><code>condition</code> MUST be of type <code>bool</code>,</li>
  <li><code>true_value</code> and <code>false_value</code> MUST be type-compatible,</li>
  <li>the output type is the resolved common result type of the two value inputs.</li>
</ul>

<p>
This function is a data-selection function.
It is not a general control-flow structure.
Structural branching remains owned by the standardized <code>case</code> structure family.
</p>

<hr/>

<h2 id="local-memory-primitive">13. Local-Memory Primitive</h2>

<h3>13.1 <code>frog.core.delay</code></h3>

<p>
<code>frog.core.delay</code> is the minimal standard local-memory function for FROG v0.1.
</p>

<p>
It is the only stateful function defined in this document.
This document defines its standardized primitive identity, port model, required configuration surface, and primitive-local delayed-value behavior.
The normative semantics of local memory as a language concept, and the rule that determines whether a directed cycle is valid, are defined by <code>Language/State and cycles.md</code>.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>out</code></li>
</ul>

<p>Required metadata:</p>

<ul>
  <li><code>initial</code></li>
</ul>

<p>Rules:</p>

<ul>
  <li><code>in</code> and <code>out</code> MUST have the same type,</li>
  <li>every <code>frog.core.delay</code> node MUST define an explicit <code>initial</code> value in v0.1,</li>
  <li><code>initial</code> MUST be compatible with the carried value type.</li>
</ul>

<p>
Primitive-local delayed-value model:
</p>

<pre><code>out(t) = state(t)
state(t + 1) = in(t)
state(0) = initial</code></pre>

<p>
This primitive enables deterministic and explicit delayed feedback in dataflow graphs.
However, the presence of a <code>frog.core.delay</code> node inside a graph does not, by itself, redefine the general language rule for cycles.
Whether a specific cycle is valid remains governed by <code>Language/State and cycles.md</code>.
</p>

<h3>13.2 Role of <code>initial</code></h3>

<p>
The <code>initial</code> field defines the primitive's initial stored value for the first activation.
In v0.1, this field is mandatory to ensure deterministic initialization of explicit local memory.
</p>

<h3>13.3 Scope of ownership</h3>

<p>
For <code>frog.core.delay</code>, ownership is intentionally split as follows:
</p>

<ul>
  <li><code>Libraries/Core.md</code> owns the primitive name, required ports, required metadata, and primitive-local delayed-value behavior,</li>
  <li><code>Expression/State and cycles.md</code> owns the source-facing representation of explicit local memory in canonical graph form,</li>
  <li><code>Language/State and cycles.md</code> owns the cross-cutting semantic rule that makes a directed cycle valid only when explicit local memory is present.</li>
</ul>

<hr/>

<h2 id="diagram-representation">14. Diagram Representation</h2>

<p>
Calls to <code>frog.core</code> functions are serialized as <code>primitive</code> nodes in the diagram.
</p>

<p>Example:</p>

<pre><code class="language-json">{
  "id": "add_1",
  "kind": "primitive",
  "type": "frog.core.add"
}</code></pre>

<p>Stateful example:</p>

<pre><code class="language-json">{
  "id": "delay_1",
  "kind": "primitive",
  "type": "frog.core.delay",
  "initial": 0.0
}</code></pre>

<p>
The exact port existence, direction, and typing of these nodes are resolved from this specification together with the type system and the graph rules.
</p>

<p>
Conceptually:
</p>

<pre><code>primitive node
   │
   ├── type = frog.core.&lt;function&gt;
   ├── standardized ports
   ├── optional or required metadata
   └── library-defined primitive meaning</code></pre>

<hr/>

<h2 id="validation-rules">15. Validation Rules</h2>

<p>
Implementations MUST enforce the following rules:
</p>

<ul>
  <li>every <code>frog.core</code> function reference MUST identify a valid standardized core function name,</li>
  <li>all required input ports for the referenced function MUST exist and be type-compatible,</li>
  <li>all produced output ports MUST match the function definition,</li>
  <li>all implicit coercions MUST follow <code>Expression/Type.md</code>,</li>
  <li>all functions in this document MUST be treated as stateless unless explicitly defined as stateful.</li>
</ul>

<p>For <code>frog.core.delay</code> specifically:</p>

<ul>
  <li>the node MUST define <code>initial</code>,</li>
  <li><code>initial</code> MUST be type-compatible with the delay state type,</li>
  <li><code>in</code> and <code>out</code> MUST have the same type,</li>
  <li>the primitive MUST be treated as a local-memory primitive,</li>
  <li>the graph-level validity of any cycle using that primitive MUST be evaluated according to <code>Language/State and cycles.md</code>.</li>
</ul>

<p>For boolean logic functions:</p>

<ul>
  <li><code>and</code>, <code>or</code>, <code>not</code>, and <code>xor</code> MUST operate on <code>bool</code> values in v0.1.</li>
</ul>

<p>For comparison functions:</p>

<ul>
  <li><code>less</code>, <code>less_or_equal</code>, <code>greater</code>, and <code>greater_or_equal</code> MUST operate on supported comparable operands, and in base v0.1 they are defined for numeric operands.</li>
</ul>

<hr/>

<h2 id="examples">16. Examples</h2>

<h3>16.1 Arithmetic primitive</h3>

<pre><code class="language-json">{
  "id": "add_1",
  "kind": "primitive",
  "type": "frog.core.add"
}</code></pre>

<h3>16.2 Selection primitive</h3>

<pre><code class="language-json">{
  "id": "select_1",
  "kind": "primitive",
  "type": "frog.core.select"
}</code></pre>

<h3>16.3 Local-memory primitive</h3>

<pre><code class="language-json">{
  "id": "delay_1",
  "kind": "primitive",
  "type": "frog.core.delay",
  "initial": 0.0
}</code></pre>

<h3>16.4 Delay used in explicit feedback</h3>

<pre><code>value ───────┐
             ▼
        [ frog.core.add ] ───► next_value
             ▲
             │
   [ frog.core.delay ]
             ▲
             │
          feedback</code></pre>

<p>
The exact validity of the feedback cycle is not determined by this sketch alone.
It depends on the language-level cycle-validity rule defined in <code>Language/State and cycles.md</code>.
</p>

<hr/>

<h2 id="out-of-scope-for-v01">17. Out of Scope for v0.1</h2>

<ul>
  <li>a full mathematical standard library,</li>
  <li>tensor operators,</li>
  <li>signal-processing operators,</li>
  <li>domain-specific operator packs,</li>
  <li>implicit memory insertion,</li>
  <li>hidden stateful primitives beyond the standardized <code>frog.core.delay</code>,</li>
  <li>redefinition of structural control through primitive functions.</li>
</ul>

<hr/>

<h2 id="summary">18. Summary</h2>

<p>
The <code>frog.core</code> library defines the minimal standard built-in primitive vocabulary of FROG.
</p>

<ul>
  <li>it provides arithmetic, comparison, logical, and simple selection primitives,</li>
  <li>it also defines the minimal explicit local-memory primitive <code>frog.core.delay</code>,</li>
  <li>all primitives in this document are standardized as <code>primitive</code> nodes in diagrams,</li>
  <li><code>frog.core.delay</code> is the only stateful core primitive in base v0.1,</li>
  <li>primitive identity and required configuration are owned here,</li>
  <li>graph-wide local-memory and cycle-validity semantics remain owned by <code>Language/State and cycles.md</code>.</li>
</ul>

<p>
This gives FROG a compact, durable, and implementation-portable built-in primitive foundation for v0.1.
</p>
