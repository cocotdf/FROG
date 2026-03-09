<h1 align="center">🐸 FROG Type Specification</h1>

<p align="center">
Definition of the FROG type system for <strong>.frog</strong> files<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Goals of the Type System</a></li>
  <li><a href="#scope">3. Scope for v0.1</a></li>
  <li><a href="#location">4. Location in a .frog file</a></li>
  <li><a href="#canonical-type-expressions">5. Canonical Type Expressions</a></li>
  <li><a href="#primitive-types">6. Built-in Primitive Types</a></li>
  <li><a href="#array-types">7. Built-in Array Types</a></li>
  <li><a href="#type-identity">8. Type Identity</a></li>
  <li><a href="#type-compatibility">9. Type Compatibility</a></li>
  <li><a href="#implicit-numeric-coercions">10. Implicit Numeric Coercions</a></li>
  <li><a href="#array-coercions">11. Array Coercions</a></li>
  <li><a href="#explicit-conversion-nodes">12. Explicit Conversion Nodes</a></li>
  <li><a href="#validation-rules">13. Validation Rules</a></li>
  <li><a href="#out-of-scope">14. Out of Scope for v0.1</a></li>
  <li><a href="#examples">15. Examples</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
The FROG type system defines how values are described, validated, connected, and converted inside a <code>.frog</code> program.
</p>

<p>
For v0.1, the type system is intentionally small and explicit. It provides:
</p>

<ul>
  <li>a fixed set of built-in primitive types,</li>
  <li>a minimal set of built-in composite types,</li>
  <li>a canonical textual type syntax for use in <code>.frog</code> files,</li>
  <li>deterministic compatibility and coercion rules.</li>
</ul>

<p>
The type system applies to interface ports, diagram nodes, wires, front panel bindings, constants, and any other value-carrying element defined by the FROG expression format.
</p>

<hr/>

<h2 id="goals">2. Goals of the Type System</h2>

<p>
The FROG type system is designed to satisfy the following goals:
</p>

<ul>
  <li><strong>Clarity</strong> — types must be readable and unambiguous in source form.</li>
  <li><strong>Determinism</strong> — type compatibility and coercion behavior must be fully specified.</li>
  <li><strong>Portability</strong> — type meaning must not depend on platform-specific C compiler behavior.</li>
  <li><strong>Efficiency</strong> — types must map cleanly to compiled and runtime representations.</li>
  <li><strong>Graph usability</strong> — the system must support practical graphical programming with limited but useful implicit coercions.</li>
</ul>

<hr/>

<h2 id="scope">3. Scope for v0.1</h2>

<p>
FROG v0.1 specifies a minimal built-in type system consisting of:
</p>

<ul>
  <li>primitive scalar types,</li>
  <li>array types,</li>
  <li>type identity and compatibility rules,</li>
  <li>implicit numeric coercion rules.</li>
</ul>

<p>
FROG v0.1 does <strong>not</strong> yet standardize user-defined types, library-defined custom types, records, enums, classes, or generic type declarations beyond arrays.
</p>

<hr/>

<h2 id="location">4. Location in a .frog file</h2>

<p>
Types are represented directly where values are declared or constrained.
For example, interface ports and other typed elements use canonical textual type expressions such as:
</p>

<pre><code>{
  "name": "input_signal",
  "type": "f64"
}
</code></pre>

<p>
The top-level <code>.frog</code> file does not require a separate mandatory <code>types</code> section in v0.1.
Type definitions are embedded by reference through canonical type expressions.
</p>

<hr/>

<h2 id="canonical-type-expressions">5. Canonical Type Expressions</h2>

<p>
FROG v0.1 uses a canonical textual syntax to represent types in source files.
This syntax is normative.
</p>

<h3>5.1 Primitive type syntax</h3>

<p>
Primitive types are written as a single identifier:
</p>

<pre><code>bool
i8
i16
i32
i64
u8
u16
u32
u64
f32
f64
string
</code></pre>

<h3>5.2 Array type syntax</h3>

<p>
Dynamic-size arrays are written as:
</p>

<pre><code>array&lt;T&gt;
</code></pre>

<p>
Fixed-size arrays are written as:
</p>

<pre><code>array&lt;T, N&gt;
</code></pre>

<p>
Where:
</p>

<ul>
  <li><code>T</code> is any valid FROG v0.1 type expression,</li>
  <li><code>N</code> is a positive integer literal.</li>
</ul>

<h3>5.3 Canonical formatting rules</h3>

<ul>
  <li>Type names are case-sensitive.</li>
  <li>No alternative aliases are defined in v0.1.</li>
  <li><code>float64</code>, <code>int32</code>, <code>double</code>, and similar aliases are not canonical type names.</li>
  <li>Whitespace inside a type expression is not significant for parsing, but canonical serialized form should omit unnecessary spaces.</li>
</ul>

<p>
Examples of canonical form:
</p>

<pre><code>i32
f64
array&lt;u8&gt;
array&lt;f32, 256&gt;
array&lt;array&lt;i16, 8&gt;, 4&gt;
</code></pre>

<hr/>

<h2 id="primitive-types">6. Built-in Primitive Types</h2>

<h3>6.1 Boolean</h3>

<ul>
  <li><code>bool</code> — logical true/false value.</li>
</ul>

<h3>6.2 Signed integers</h3>

<ul>
  <li><code>i8</code> — 8-bit signed integer</li>
  <li><code>i16</code> — 16-bit signed integer</li>
  <li><code>i32</code> — 32-bit signed integer</li>
  <li><code>i64</code> — 64-bit signed integer</li>
</ul>

<h3>6.3 Unsigned integers</h3>

<ul>
  <li><code>u8</code> — 8-bit unsigned integer</li>
  <li><code>u16</code> — 16-bit unsigned integer</li>
  <li><code>u32</code> — 32-bit unsigned integer</li>
  <li><code>u64</code> — 64-bit unsigned integer</li>
</ul>

<h3>6.4 Floating-point numbers</h3>

<ul>
  <li><code>f32</code> — 32-bit IEEE 754 floating-point value</li>
  <li><code>f64</code> — 64-bit IEEE 754 floating-point value</li>
</ul>

<h3>6.5 String</h3>

<ul>
  <li><code>string</code> — textual value</li>
</ul>

<p>
The exact internal encoding of <code>string</code> is not further standardized in v0.1.
Only its identity as a distinct built-in type is specified here.
</p>

<hr/>

<h2 id="array-types">7. Built-in Array Types</h2>

<p>
FROG v0.1 defines two built-in array forms:
</p>

<ul>
  <li><code>array&lt;T&gt;</code> — array of element type <code>T</code> with dynamic size,</li>
  <li><code>array&lt;T, N&gt;</code> — array of element type <code>T</code> with fixed size <code>N</code>.</li>
</ul>

<h3>7.1 Dynamic arrays</h3>

<p>
A dynamic array has a known element type but no compile-time fixed length in the type expression itself.
</p>

<p>
Example:
</p>

<pre><code>array&lt;f64&gt;
</code></pre>

<h3>7.2 Fixed-size arrays</h3>

<p>
A fixed-size array includes both its element type and its size in the type identity.
</p>

<p>
Example:
</p>

<pre><code>array&lt;u8, 1024&gt;
</code></pre>

<h3>7.3 Nested arrays</h3>

<p>
Arrays may be nested.
</p>

<p>
Example:
</p>

<pre><code>array&lt;array&lt;f32, 16&gt;, 8&gt;
</code></pre>

<hr/>

<h2 id="type-identity">8. Type Identity</h2>

<p>
Two types are identical if and only if their canonical meaning is exactly the same.
</p>

<h3>8.1 Primitive identity</h3>

<ul>
  <li><code>i32</code> is identical to <code>i32</code></li>
  <li><code>i32</code> is not identical to <code>u32</code></li>
  <li><code>f32</code> is not identical to <code>f64</code></li>
  <li><code>string</code> is not identical to <code>array&lt;u8&gt;</code></li>
</ul>

<h3>8.2 Array identity</h3>

<ul>
  <li><code>array&lt;f64&gt;</code> is identical to <code>array&lt;f64&gt;</code></li>
  <li><code>array&lt;f64, 16&gt;</code> is identical to <code>array&lt;f64, 16&gt;</code></li>
  <li><code>array&lt;f64, 16&gt;</code> is not identical to <code>array&lt;f64, 32&gt;</code></li>
  <li><code>array&lt;f64&gt;</code> is not identical to <code>array&lt;f64, 16&gt;</code></li>
  <li><code>array&lt;i32&gt;</code> is not identical to <code>array&lt;u32&gt;</code></li>
</ul>

<hr/>

<h2 id="type-compatibility">9. Type Compatibility</h2>

<p>
Type compatibility in FROG v0.1 is defined by the following categories:
</p>

<ul>
  <li><strong>Exact match</strong> — source and target types are identical.</li>
  <li><strong>Implicit coercion allowed</strong> — source and target types are different, but FROG allows deterministic automatic conversion.</li>
  <li><strong>Explicit conversion required</strong> — no implicit coercion is allowed, but an explicit conversion node may make the connection legal.</li>
  <li><strong>Incompatible</strong> — the types are not compatible under v0.1 rules.</li>
</ul>

<p>
Unless otherwise defined, a connection is valid when:
</p>

<ul>
  <li>the source and target types are identical, or</li>
  <li>an implicit coercion is defined by this specification, or</li>
  <li>an explicit conversion node is inserted by the author.</li>
</ul>

<hr/>

<h2 id="implicit-numeric-coercions">10. Implicit Numeric Coercions</h2>

<p>
FROG v0.1 allows implicit coercions between numeric types.
These coercions are part of the language semantics.
They are <strong>not</strong> user-authored diagram nodes in source form.
</p>

<p>
An IDE may visually indicate an implicit coercion, for example by displaying a coercion marker on the target terminal.
Such visualization is an IDE concern and does not require an explicit source node.
</p>

<h3>10.1 Numeric types</h3>

<p>
For the purpose of implicit coercion, the numeric built-in types are:
</p>

<ul>
  <li><code>i8</code>, <code>i16</code>, <code>i32</code>, <code>i64</code></li>
  <li><code>u8</code>, <code>u16</code>, <code>u32</code>, <code>u64</code></li>
  <li><code>f32</code>, <code>f64</code></li>
</ul>

<p>
The following built-in types are <strong>not</strong> numeric:
</p>

<ul>
  <li><code>bool</code></li>
  <li><code>string</code></li>
</ul>

<h3>10.2 General rule</h3>

<p>
Any numeric scalar type may be implicitly coerced to any other numeric scalar type.
The conversion result must follow the rules below.
</p>

<h3>10.3 Integer to integer</h3>

<p>
When converting from one integer type to another:
</p>

<ul>
  <li>if the source value is representable in the target type, the result is the exact converted value,</li>
  <li>if the source value is below the minimum representable target value, the result is the minimum target value,</li>
  <li>if the source value is above the maximum representable target value, the result is the maximum target value.</li>
</ul>

<p>
This is a saturating conversion.
</p>

<h3>10.4 Integer to float</h3>

<p>
When converting from an integer type to a floating-point type:
</p>

<ul>
  <li>the conversion follows IEEE 754 numeric semantics for the target floating-point representation,</li>
  <li>if the integer magnitude exceeds the representable range of the target floating-point type, the result is <code>+Inf</code> or <code>-Inf</code> as appropriate.</li>
</ul>

<h3>10.5 Float to float</h3>

<p>
When converting from one floating-point type to another:
</p>

<ul>
  <li>the conversion follows IEEE 754 semantics for the target type,</li>
  <li>finite values are converted to the nearest representable value according to the target representation,</li>
  <li><code>NaN</code> remains <code>NaN</code>,</li>
  <li><code>+Inf</code> remains <code>+Inf</code>,</li>
  <li><code>-Inf</code> remains <code>-Inf</code>.</li>
</ul>

<h3>10.6 Float to integer</h3>

<p>
When converting from a floating-point type to an integer type:
</p>

<ul>
  <li>finite values are first truncated toward zero,</li>
  <li>the truncated value is then saturated to the representable range of the target integer type,</li>
  <li><code>NaN</code> converts to <code>0</code>,</li>
  <li><code>+Inf</code> converts to the maximum representable target value,</li>
  <li><code>-Inf</code> converts to the minimum representable target value.</li>
</ul>

<h3>10.7 Non-numeric built-in types</h3>

<p>
No implicit coercion is defined in v0.1 for:
</p>

<ul>
  <li><code>bool</code> ↔ numeric</li>
  <li><code>string</code> ↔ numeric</li>
  <li><code>bool</code> ↔ <code>string</code></li>
</ul>

<hr/>

<h2 id="array-coercions">11. Array Coercions</h2>

<p>
FROG v0.1 allows implicit coercion between array types when coercion is valid for the array element type and the array shape remains compatible.
</p>

<h3>11.1 Element-wise coercion</h3>

<p>
If <code>T</code> may be implicitly coerced to <code>U</code>, then:
</p>

<ul>
  <li><code>array&lt;T&gt;</code> may be implicitly coerced to <code>array&lt;U&gt;</code>,</li>
  <li><code>array&lt;T, N&gt;</code> may be implicitly coerced to <code>array&lt;U, N&gt;</code>.</li>
</ul>

<p>
The coercion is applied element by element.
</p>

<h3>11.2 Shape preservation</h3>

<p>
Implicit array coercion never changes array shape.
</p>

<ul>
  <li><code>array&lt;i32, 16&gt;</code> to <code>array&lt;f64, 16&gt;</code> is allowed.</li>
  <li><code>array&lt;i32, 16&gt;</code> to <code>array&lt;f64, 32&gt;</code> is not allowed.</li>
  <li><code>array&lt;i32&gt;</code> to <code>array&lt;f64&gt;</code> is allowed.</li>
  <li><code>array&lt;i32&gt;</code> to <code>i32</code> is not allowed.</li>
</ul>

<h3>11.3 Nested arrays</h3>

<p>
Nested arrays follow the same rule recursively.
If the inner element type coercion is valid and shape is preserved at each fixed-size level, the nested array coercion is valid.
</p>

<hr/>

<h2 id="explicit-conversion-nodes">12. Explicit Conversion Nodes</h2>

<p>
FROG implementations may define explicit conversion nodes such as numeric conversion, cast, or type adaptation nodes.
These nodes are distinct from implicit coercions.
</p>

<p>
An explicit conversion node:
</p>

<ul>
  <li>is authored intentionally in the diagram,</li>
  <li>is represented as a real node in source form,</li>
  <li>may be used when no implicit coercion is defined,</li>
  <li>may also be used to make intent explicit even when an implicit coercion would be legal.</li>
</ul>

<p>
The exact standard library of explicit conversion nodes is outside the scope of this document, but the distinction between implicit coercion and explicit conversion is normative.
</p>

<hr/>

<h2 id="validation-rules">13. Validation Rules</h2>

<p>
A FROG validator must apply the following rules:
</p>

<ul>
  <li>every type expression must parse successfully according to this specification,</li>
  <li>every referenced built-in type name must be valid,</li>
  <li>every fixed array size <code>N</code> must be a positive integer literal,</li>
  <li>connections between typed ports must be accepted only if they are exact matches, implicitly coercible, or explicitly converted through a node,</li>
  <li>implicit coercions must follow the deterministic rules defined in this document,</li>
  <li>shape-changing implicit array coercions must be rejected.</li>
</ul>

<p>
A validator may report warnings or informational diagnostics for implicit coercions, but if a coercion is defined by this specification, the connection is valid.
</p>

<hr/>

<h2 id="out-of-scope">14. Out of Scope for v0.1</h2>

<p>
The following are not standardized by FROG v0.1:
</p>

<ul>
  <li>user-defined named types,</li>
  <li>library-defined custom types,</li>
  <li>records / structs / clusters,</li>
  <li>enums,</li>
  <li>classes and objects,</li>
  <li>unions or variants,</li>
  <li>maps, dictionaries, and sets,</li>
  <li>path, timestamp, waveform, or domain-specific built-in types,</li>
  <li>generic polymorphism beyond array element typing,</li>
  <li>subtyping and inheritance.</li>
</ul>

<p>
Future versions of FROG may extend the type system in a backward-compatible way.
</p>

<hr/>

<h2 id="examples">15. Examples</h2>

<h3>15.1 Valid primitive declarations</h3>

<pre><code>{ "type": "bool" }
{ "type": "i32" }
{ "type": "f64" }
{ "type": "string" }
</code></pre>

<h3>15.2 Valid array declarations</h3>

<pre><code>{ "type": "array&lt;u8&gt;" }
{ "type": "array&lt;f64, 1024&gt;" }
{ "type": "array&lt;array&lt;i16, 8&gt;, 4&gt;" }
</code></pre>

<h3>15.3 Valid implicit numeric coercions</h3>

<ul>
  <li><code>i32 → f64</code></li>
  <li><code>u32 → i32</code> (saturating if needed)</li>
  <li><code>f64 → i32</code> (truncate toward zero, then saturate)</li>
  <li><code>array&lt;i32&gt; → array&lt;f64&gt;</code> (element-wise)</li>
  <li><code>array&lt;u32, 16&gt; → array&lt;i32, 16&gt;</code> (element-wise, saturating if needed)</li>
</ul>

<h3>15.4 Invalid implicit coercions</h3>

<ul>
  <li><code>bool → i32</code></li>
  <li><code>string → f64</code></li>
  <li><code>array&lt;i32, 16&gt; → array&lt;i32, 32&gt;</code></li>
  <li><code>array&lt;i32&gt; → i32</code></li>
</ul>

<hr/>

<p align="center">
End of FROG Type Specification
</p>
