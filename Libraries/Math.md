<h1 align="center">🐸 FROG Math Library Specification</h1>

<p align="center">
Definition of the standard <strong>frog.math</strong> library for FROG v0.1<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Goals</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#role-of-frog-math">4. Role of <code>frog.math</code></a></li>
  <li><a href="#naming-and-namespace">5. Naming and Namespace</a></li>
  <li><a href="#scope-for-v01">6. Scope for v0.1</a></li>
  <li><a href="#library-categories">7. Library Categories</a></li>
  <li><a href="#typing-model">8. Typing Model</a></li>
  <li><a href="#numeric-utility-functions">9. Numeric Utility Functions</a></li>
  <li><a href="#rounding-functions">10. Rounding Functions</a></li>
  <li><a href="#power-root-and-logarithmic-functions">11. Power, Root, and Logarithmic Functions</a></li>
  <li><a href="#trigonometric-functions">12. Trigonometric Functions</a></li>
  <li><a href="#hyperbolic-functions">13. Hyperbolic Functions</a></li>
  <li><a href="#diagram-representation">14. Diagram Representation</a></li>
  <li><a href="#validation-rules">15. Validation Rules</a></li>
  <li><a href="#examples">16. Examples</a></li>
  <li><a href="#out-of-scope">17. Out of Scope for v0.1</a></li>
  <li><a href="#summary">18. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the standard <strong>frog.math</strong> library for FROG v0.1.
</p>

<p>
The <code>frog.math</code> library complements the minimal <code>frog.core</code> library by defining a first standard set of scalar mathematical primitives beyond the built-in core vocabulary.
</p>

<p>
In v0.1, this library focuses on portable and commonly expected scalar mathematics, including:
</p>

<ul>
  <li>numeric utility functions,</li>
  <li>rounding functions,</li>
  <li>power, root, exponential, and logarithmic functions,</li>
  <li>trigonometric functions,</li>
  <li>hyperbolic functions.</li>
</ul>

<p>
This document does not attempt to define full linear algebra, statistics, optimization, signal processing, tensor computation, or symbolic mathematics.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Usefulness</strong> — provide a first standard mathematical library that is broadly useful in practical programs.</li>
  <li><strong>Separation of concerns</strong> — keep minimal language primitives in <code>frog.core</code> while placing broader scalar mathematics in a dedicated library.</li>
  <li><strong>Portability</strong> — ensure that the defined function names and port models remain stable across conforming implementations.</li>
  <li><strong>Clarity</strong> — define each primitive with an explicit name, role, and expected typing model.</li>
  <li><strong>Extensibility</strong> — leave room for future sibling libraries such as <code>frog.linalg</code>, <code>frog.stats</code>, <code>frog.signal</code>, or <code>frog.tensor</code>.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This document complements the following specifications:
</p>

<ul>
  <li><strong>Libraries/Core.md</strong> — defines the minimal standard primitive core, including basic arithmetic and comparison primitives.</li>
  <li><strong>Expression/Diagram.md</strong> — defines how library functions are serialized as diagram nodes.</li>
  <li><strong>Expression/Type.md</strong> — defines built-in types, type compatibility, and implicit coercion rules.</li>
  <li><strong>Expression/Control structures.md</strong> — defines standardized language structures, which remain distinct from ordinary primitive functions.</li>
</ul>

<p>
This document defines the standard mathematical primitive vocabulary of <code>frog.math</code>.
It does not redefine the graph model, the type system, or language structures.
</p>

<hr/>

<h2 id="role-of-frog-math">4. Role of <code>frog.math</code></h2>

<p>
The <code>frog.math</code> library provides standardized mathematical primitives that go beyond the minimal built-in core vocabulary.
</p>

<p>
In language terms, these are library functions.
In the serialized diagram representation defined by <code>Expression/Diagram.md</code>, calls to these functions appear as <code>primitive</code> nodes.
</p>

<p>
Therefore:
</p>

<ul>
  <li><code>frog.math.sqrt</code> is a standard mathematical function,</li>
  <li>in a diagram, that function call appears as a <code>primitive</code> node with <code>type = "frog.math.sqrt"</code>.</li>
</ul>

<hr/>

<h2 id="naming-and-namespace">5. Naming and Namespace</h2>

<p>
FROG uses the following general namespace pattern for built-in and library-defined primitives:
</p>

<pre>
frog.&lt;library&gt;.&lt;primitive&gt;
</pre>

<p>
For this document:
</p>

<ul>
  <li><code>frog</code> identifies the language namespace,</li>
  <li><code>math</code> identifies the standard scalar mathematics library,</li>
  <li>the final segment identifies the primitive name.</li>
</ul>

<p>
Examples:
</p>

<pre>
frog.math.sqrt
frog.math.pow
frog.math.sin
frog.math.round
</pre>

<p>
Primitive names in <code>frog.math</code> SHOULD use lowercase snake_case where multiple words are needed.
</p>

<hr/>

<h2 id="scope-for-v01">6. Scope for v0.1</h2>

<p>
FROG v0.1 standardizes the following mathematical families in <code>frog.math</code>:
</p>

<ul>
  <li>numeric utility functions,</li>
  <li>rounding functions,</li>
  <li>power and root functions,</li>
  <li>exponential and logarithmic functions,</li>
  <li>trigonometric functions,</li>
  <li>hyperbolic functions.</li>
</ul>

<p>
In v0.1, <code>frog.math</code> is intentionally limited to scalar mathematics.
Array-wide, matrix-wide, tensor-wide, and domain-specific mathematical libraries are outside the strict scope of this document.
</p>

<hr/>

<h2 id="library-categories">7. Library Categories</h2>

<p>
The standard <code>frog.math</code> library is organized into the following categories:
</p>

<ul>
  <li><strong>Numeric Utility</strong></li>
  <li><strong>Rounding</strong></li>
  <li><strong>Powers, Roots, and Logarithms</strong></li>
  <li><strong>Trigonometric</strong></li>
  <li><strong>Hyperbolic</strong></li>
</ul>

<p>
This categorization is semantic.
It does not impose a mandatory palette layout, but it provides a stable foundation for IDE organization.
</p>

<hr/>

<h2 id="typing-model">8. Typing Model</h2>

<p>
All <code>frog.math</code> functions are typed according to <strong>Expression/Type.md</strong>.
</p>

<p>
Unless stated otherwise:
</p>

<ul>
  <li>all input and output ports MUST use valid FROG types,</li>
  <li>all compatibility checks MUST follow the standard FROG type rules,</li>
  <li>all implicit coercions MUST follow the standard FROG coercion rules,</li>
  <li>all functions in this document are stateless and side-effect-free,</li>
  <li>all functions in this document operate on scalar values in v0.1.</li>
</ul>

<p>
Required support for v0.1:
</p>

<ul>
  <li>every conforming implementation that supports <code>frog.math</code> MUST support <code>float32</code> and <code>float64</code> for all primitives in this document,</li>
  <li>support for additional numeric scalar types MAY be defined by the active execution profile,</li>
  <li>behavior for domain errors, infinities, NaNs, overflow, underflow, and implementation-defined numeric edge cases MUST be defined by the active execution profile for each supported numeric family.</li>
</ul>

<p>
This document standardizes primitive identity, port models, and source-level meaning.
It does not require a single universal floating-point exception model across all runtimes.
</p>

<hr/>

<h2 id="numeric-utility-functions">9. Numeric Utility Functions</h2>

<h3>9.1 <code>frog.math.min</code></h3>

<p>
Returns the smaller of two numeric scalar inputs.
</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
The two inputs MUST be type-compatible under the FROG type rules.
The output type is the resolved common result type.
</p>

<h3>9.2 <code>frog.math.max</code></h3>

<p>
Returns the larger of two numeric scalar inputs.
</p>

<ul>
  <li>input ports: <code>a</code>, <code>b</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>9.3 <code>frog.math.clamp</code></h3>

<p>
Constrains a numeric scalar input to a closed interval.
</p>

<ul>
  <li>input ports: <code>value</code>, <code>min_value</code>, <code>max_value</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>all three inputs MUST be type-compatible,</li>
  <li><code>min_value</code> SHOULD be less than or equal to <code>max_value</code>,</li>
  <li>the output type is the resolved common result type.</li>
</ul>

<h3>9.4 <code>frog.math.sign</code></h3>

<p>
Returns the sign classification of a numeric scalar input.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
In v0.1, the output value MUST be negative, zero, or positive according to the active execution profile for the supported numeric family.
The output type is the same as the resolved input type unless the active execution profile defines a stricter standard result type.
</p>

<h3>9.5 <code>frog.math.square</code></h3>

<p>
Returns the square of a numeric scalar input.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>9.6 <code>frog.math.reciprocal</code></h3>

<p>
Returns the reciprocal of a numeric scalar input.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
Division-by-zero and non-finite behavior MUST be defined by the active execution profile.
</p>

<hr/>

<h2 id="rounding-functions">10. Rounding Functions</h2>

<h3>10.1 <code>frog.math.floor</code></h3>

<p>
Returns the greatest integral value not greater than the input.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>10.2 <code>frog.math.ceil</code></h3>

<p>
Returns the smallest integral value not less than the input.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>10.3 <code>frog.math.trunc</code></h3>

<p>
Returns the integral value obtained by truncation toward zero.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>10.4 <code>frog.math.round</code></h3>

<p>
Returns the rounded integral value nearest to the input according to the active execution profile.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
Tie-breaking behavior MUST be defined by the active execution profile.
</p>

<hr/>

<h2 id="power-root-and-logarithmic-functions">11. Power, Root, and Logarithmic Functions</h2>

<h3>11.1 <code>frog.math.pow</code></h3>

<p>
Raises a base value to a power.
</p>

<ul>
  <li>input ports: <code>base</code>, <code>exponent</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
The input operands MUST be numeric scalar values.
The output type is the resolved result type under the active execution profile.
</p>

<h3>11.2 <code>frog.math.sqrt</code></h3>

<p>
Returns the square root of a numeric scalar input.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>11.3 <code>frog.math.exp</code></h3>

<p>
Returns the natural exponential of a numeric scalar input.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>11.4 <code>frog.math.ln</code></h3>

<p>
Returns the natural logarithm of a numeric scalar input.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>11.5 <code>frog.math.log10</code></h3>

<p>
Returns the base-10 logarithm of a numeric scalar input.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
Domain constraints, NaN handling, and behavior on unsupported values MUST be defined by the active execution profile.
</p>

<hr/>

<h2 id="trigonometric-functions">12. Trigonometric Functions</h2>

<h3>12.1 <code>frog.math.sin</code></h3>

<p>
Returns the sine of an angle input.
</p>

<ul>
  <li>input port: <code>angle</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>12.2 <code>frog.math.cos</code></h3>

<p>
Returns the cosine of an angle input.
</p>

<ul>
  <li>input port: <code>angle</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>12.3 <code>frog.math.tan</code></h3>

<p>
Returns the tangent of an angle input.
</p>

<ul>
  <li>input port: <code>angle</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>12.4 <code>frog.math.asin</code></h3>

<p>
Returns the inverse sine of a numeric scalar input.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>12.5 <code>frog.math.acos</code></h3>

<p>
Returns the inverse cosine of a numeric scalar input.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>12.6 <code>frog.math.atan</code></h3>

<p>
Returns the inverse tangent of a numeric scalar input.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>12.7 <code>frog.math.atan2</code></h3>

<p>
Returns the two-argument inverse tangent.
</p>

<ul>
  <li>input ports: <code>y</code>, <code>x</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
In v0.1, angle units are profile-defined.
A conforming execution profile that supports <code>frog.math</code> SHOULD make the angle convention explicit, and radians SHOULD be the default unless another convention is stated.
</p>

<hr/>

<h2 id="hyperbolic-functions">13. Hyperbolic Functions</h2>

<h3>13.1 <code>frog.math.sinh</code></h3>

<p>
Returns the hyperbolic sine of a numeric scalar input.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>13.2 <code>frog.math.cosh</code></h3>

<p>
Returns the hyperbolic cosine of a numeric scalar input.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<h3>13.3 <code>frog.math.tanh</code></h3>

<p>
Returns the hyperbolic tangent of a numeric scalar input.
</p>

<ul>
  <li>input port: <code>in</code></li>
  <li>output port: <code>result</code></li>
</ul>

<hr/>

<h2 id="diagram-representation">14. Diagram Representation</h2>

<p>
Calls to <code>frog.math</code> functions are serialized as <code>primitive</code> nodes in the diagram.
</p>

<p>
Example:
</p>

<pre><code>{
  "id": "sqrt_1",
  "kind": "primitive",
  "type": "frog.math.sqrt"
}</code></pre>

<p>
Another example:
</p>

<pre><code>{
  "id": "sin_1",
  "kind": "primitive",
  "type": "frog.math.sin"
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
  <li>every <code>frog.math</code> function reference MUST identify a valid standardized <code>frog.math</code> function name,</li>
  <li>all required input ports for the referenced function MUST exist and be type-compatible,</li>
  <li>all produced output ports MUST match the function definition,</li>
  <li>all implicit coercions MUST follow <strong>Expression/Type.md</strong>,</li>
  <li>all functions in this document MUST be treated as stateless and side-effect-free.</li>
</ul>

<p>
For v0.1 scalar support:
</p>

<ul>
  <li>all functions in this document MUST operate on scalar inputs only,</li>
  <li>array, matrix, tensor, map, set, and cluster-wide lifting semantics are not defined by this document,</li>
  <li>conforming implementations that claim support for <code>frog.math</code> MUST support <code>float32</code> and <code>float64</code> for every primitive in this document.</li>
</ul>

<p>
For numeric edge cases:
</p>

<ul>
  <li>domain violations, overflow, underflow, NaN propagation, and infinity handling MUST be defined by the active execution profile,</li>
  <li>these profile-defined runtime details MUST NOT change primitive identity or source-level meaning.</li>
</ul>

<hr/>

<h2 id="examples">16. Examples</h2>

<h3>16.1 Square root</h3>

<pre><code>{
  "id": "sqrt_1",
  "kind": "primitive",
  "type": "frog.math.sqrt"
}</code></pre>

<p>
Conceptual ports:
</p>

<pre>
in → result
</pre>

<h3>16.2 Power</h3>

<pre><code>{
  "id": "pow_1",
  "kind": "primitive",
  "type": "frog.math.pow"
}</code></pre>

<p>
Conceptual ports:
</p>

<pre>
base, exponent → result
</pre>

<h3>16.3 Clamp</h3>

<pre><code>{
  "id": "clamp_1",
  "kind": "primitive",
  "type": "frog.math.clamp"
}</code></pre>

<p>
Conceptual ports:
</p>

<pre>
value, min_value, max_value → result
</pre>

<h3>16.4 Two-argument arctangent</h3>

<pre><code>{
  "id": "atan2_1",
  "kind": "primitive",
  "type": "frog.math.atan2"
}</code></pre>

<p>
Conceptual ports:
</p>

<pre>
y, x → result
</pre>

<hr/>

<h2 id="out-of-scope">17. Out of Scope for v0.1</h2>

<p>
The following are outside the strict scope of <code>frog.math</code> in v0.1:
</p>

<ul>
  <li>vectorized or broadcast semantics over arrays, matrices, or tensors,</li>
  <li>linear algebra primitives,</li>
  <li>probability and statistics primitives,</li>
  <li>curve fitting, optimization, and numerical solvers,</li>
  <li>signal-processing primitives,</li>
  <li>symbolic or algebraic manipulation,</li>
  <li>units-of-measure systems,</li>
  <li>special-function catalogs beyond the functions explicitly standardized here.</li>
</ul>

<hr/>

<h2 id="summary">18. Summary</h2>

<p>
The <code>frog.math</code> library defines a first standard scalar mathematics library for FROG v0.1.
</p>

<p>
It provides:
</p>

<ul>
  <li>numeric utility functions,</li>
  <li>rounding functions,</li>
  <li>power, root, exponential, and logarithmic functions,</li>
  <li>trigonometric functions,</li>
  <li>hyperbolic functions.</li>
</ul>

<p>
This library is intentionally broader than <code>frog.core</code> but still bounded.
Its purpose is to provide a durable and useful standard foundation for scalar mathematical programming in FROG while leaving richer numerical domains to future sibling libraries.
</p>

<hr/>

<p align="center">
End of FROG Math Library Specification
</p>
