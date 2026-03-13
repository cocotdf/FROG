<h1 align="center">🐸 FROG Connectivity Library Specification</h1>

<p align="center">
Definition of the minimal standard <strong>frog.connectivity</strong> library for FROG v0.1<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Goals</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#role-of-frogconnectivity">4. Role of <code>frog.connectivity</code></a></li>
  <li><a href="#naming-and-namespace">5. Naming and Namespace</a></li>
  <li><a href="#scope-for-v01">6. Scope for v0.1</a></li>
  <li><a href="#connectivity-model">7. Connectivity Model</a></li>
  <li><a href="#payload-model">8. Payload Model</a></li>
  <li><a href="#python-primitives">9. Python Primitives</a></li>
  <li><a href="#native-primitives">10. Native and Shared Library Primitives</a></li>
  <li><a href="#dotnet-primitives">11. .NET Primitives</a></li>
  <li><a href="#sql-primitives">12. SQL Primitives</a></li>
  <li><a href="#diagram-representation">13. Diagram Representation</a></li>
  <li><a href="#validation-rules">14. Validation Rules</a></li>
  <li><a href="#examples">15. Examples</a></li>
  <li><a href="#out-of-scope-for-v01">16. Out of Scope for v0.1</a></li>
  <li><a href="#summary">17. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the minimal standard <code>frog.connectivity</code> library for FROG v0.1.
</p>

<p>
The <code>frog.connectivity</code> library contains a first standard set of primitives for interoperating with external runtimes, native or shared libraries, managed platforms, and SQL-capable data sources.
</p>

<p>
The goal of this first version is to standardize a practical, portable, and conservative connectivity surface that fits cleanly within the current FROG source and type model.
</p>

<p>
In v0.1, the standardized connectivity model is intentionally limited to synchronous request/response primitives with explicit textual or byte payloads.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Usefulness</strong> — provide an immediately useful standard interop surface for common engineering workflows.</li>
  <li><strong>Portability</strong> — keep primitive identity and purpose stable across conforming implementations.</li>
  <li><strong>Conservatism</strong> — standardize only the connectivity primitives that fit within the current FROG source and type model.</li>
  <li><strong>Clarity</strong> — define stable names, stable port models, and explicit success signaling.</li>
  <li><strong>Separation of concerns</strong> — keep foreign-runtime interoperability distinct from file/path/resource I/O and distinct from widget interaction.</li>
  <li><strong>Extensibility</strong> — leave room for later revisions covering sessions, handles, callbacks, transactions, richer marshaling, and asynchronous integration.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This document complements the following specifications:
</p>

<ul>
  <li><code>Expression/Diagram.md</code> — defines how connectivity primitives are serialized as diagram nodes.</li>
  <li><code>Expression/Type.md</code> — defines the built-in scalar and array types used by connectivity primitives.</li>
  <li><code>Expression/Control structures.md</code> — defines structures that MAY be used to branch on success or failure results from connectivity primitives.</li>
  <li><code>Libraries/Core.md</code> — defines the minimal core primitive library, which remains distinct from connectivity functionality.</li>
  <li><code>Libraries/IO.md</code> — defines file/path/resource I/O primitives, which remain distinct from foreign-runtime, managed-platform, native-library, and SQL interoperability.</li>
  <li><code>Libraries/UI.md</code> — defines widget interaction primitives, which remain distinct from connectivity primitives.</li>
</ul>

<p>
This document defines the standardized primitive catalog for <code>frog.connectivity</code>.
It does not redefine the graph model, the type system, general execution semantics, or the widget interaction model.
</p>

<hr/>

<h2 id="role-of-frogconnectivity">4. Role of <code>frog.connectivity</code></h2>

<p>
The <code>frog.connectivity</code> library provides standardized primitives for invoking foreign capabilities that are not modeled as ordinary FROG functions.
</p>

<p>
In serialized diagrams, calls to these primitives are represented as <code>primitive</code> nodes whose <code>type</code> field uses the <code>frog.connectivity.*</code> namespace.
</p>

<p>
Examples:
</p>

<pre>
frog.connectivity.python.call_text
frog.connectivity.native.call_bytes
frog.connectivity.dotnet.call_text
frog.connectivity.sql.query_text
frog.connectivity.sql.execute
</pre>

<p>
The <code>frog.connectivity</code> library is distinct from:
</p>

<ul>
  <li><code>frog.core</code>, which contains the minimal always-available computational primitives,</li>
  <li><code>frog.io</code>, which covers file, path, and resource I/O only,</li>
  <li><code>frog.ui</code>, which covers widget interaction only,</li>
  <li>future libraries for networking, hardware access, runtime coordination, or richer serialization systems.</li>
</ul>

<p>
The <code>frog.connectivity</code> namespace also owns future standardized bindings for external runtimes and external services.
However, those broader binding families are not standardized in v0.1 unless explicitly defined by this document.
</p>

<hr/>

<h2 id="naming-and-namespace">5. Naming and Namespace</h2>

<p>
FROG library primitives use namespace-qualified identifiers:
</p>

<pre>
frog.&lt;library&gt;.&lt;family&gt;.&lt;primitive&gt;
</pre>

<p>
For this document:
</p>

<ul>
  <li><code>frog</code> identifies the language namespace,</li>
  <li><code>connectivity</code> identifies the standard connectivity library namespace,</li>
  <li>the third segment identifies a standardized connectivity family,</li>
  <li>the final segment identifies the primitive name.</li>
</ul>

<p>
Examples:
</p>

<pre>
frog.connectivity.python.call_text
frog.connectivity.python.call_bytes
frog.connectivity.native.call_bytes
frog.connectivity.dotnet.call_text
frog.connectivity.sql.query_text
frog.connectivity.sql.execute
</pre>

<p>
Primitive and family names in <code>frog.connectivity</code> SHOULD use lowercase snake_case where multiple words are needed.
</p>

<hr/>

<h2 id="scope-for-v01">6. Scope for v0.1</h2>

<p>
FROG v0.1 standardizes the following minimal <code>frog.connectivity</code> primitive families:
</p>

<ul>
  <li>Python request/response invocation primitives,</li>
  <li>native or shared library request/response invocation primitives,</li>
  <li>.NET request/response invocation primitives,</li>
  <li>SQL query and statement execution primitives.</li>
</ul>

<p>
These primitives provide a first portable interoperability layer for:
</p>

<ul>
  <li>Python modules and functions,</li>
  <li>native/shared library entry points, including C or C++ compatible host-call surfaces exposed through the active execution profile,</li>
  <li>.NET assemblies, types, and methods,</li>
  <li>SQL-capable data sources addressed through the active execution profile.</li>
</ul>

<p>
FROG v0.1 does not attempt to define:
</p>

<ul>
  <li>persistent source-level handles or sessions,</li>
  <li>callbacks, event subscriptions, or bidirectional host integration,</li>
  <li>async or streaming connectivity,</li>
  <li>object-graph reflection as a standard source-level mechanism,</li>
  <li>prepared statements, transactions, cursors, or connection pooling as source-level standard objects,</li>
  <li>automatic marshaling of arbitrary FROG values into foreign object systems,</li>
  <li>COM, ActiveX, Java, gRPC, REST, message-bus, or general network transport primitives,</li>
  <li>generic external-runtime or external-service bindings beyond the explicit primitive families standardized here.</li>
</ul>

<hr/>

<h2 id="connectivity-model">7. Connectivity Model</h2>

<p>
In v0.1, standardized connectivity primitives are synchronous request/response operations.
</p>

<p>
A connectivity primitive consumes explicit inputs, performs one external interaction, and then produces ordinary FROG outputs.
</p>

<p>
The standardized source-level model does not expose persistent foreign references, runtime sessions, or connection handles as first-class FROG values.
</p>

<p>
Accordingly:
</p>

<ul>
  <li>each standardized call in this document is self-contained at source level,</li>
  <li>implementations MAY internally reuse connections, runtimes, processes, or pools,</li>
  <li>such reuse remains implementation-defined or profile-defined and is not part of the canonical source contract.</li>
</ul>

<p>
Binding resolution, host process model, security policy, timeout policy, execution environment, foreign runtime availability, and foreign platform availability are defined by the active execution profile.
</p>

<hr/>

<h2 id="payload-model">8. Payload Model</h2>

<p>
All <code>frog.connectivity</code> primitives are typed according to <code>Expression/Type.md</code>.
</p>

<p>
Because FROG v0.1 does not yet standardize records, structs, enums, class types, or variant types, the minimal standardized connectivity payload model uses only built-in scalar and array types.
</p>

<p>
In v0.1, the following built-in types are especially relevant to this library:
</p>

<ul>
  <li><code>string</code> — used for identifiers, textual requests, textual responses, SQL text, and serialized parameter documents,</li>
  <li><code>bool</code> — used for success signaling,</li>
  <li><code>i64</code> — used for affected-row counts,</li>
  <li><code>array&lt;u8&gt;</code> — used for raw binary requests and responses.</li>
</ul>

<p>
Unless stated otherwise:
</p>

<ul>
  <li>all required inputs MUST exist and be type-compatible,</li>
  <li>all outputs MUST always be present,</li>
  <li>primitives that can fail MUST expose a <code>success</code> output of type <code>bool</code>,</li>
  <li>when <code>success = false</code>, any data output MUST still be well-typed and MUST take its defined fallback value.</li>
</ul>

<p>
Fallback values in this document are standardized as follows:
</p>

<ul>
  <li>empty string: <code>""</code>,</li>
  <li>zero affected rows: <code>0</code>,</li>
  <li>empty dynamic byte array: <code>array&lt;u8&gt;</code> with zero elements.</li>
</ul>

<p>
When a primitive uses a textual request or textual response payload, the semantic meaning of that payload is profile-defined.
For example, a profile MAY define JSON text, SQL parameter text, or another stable textual interchange form.
</p>

<p>
When a primitive uses a byte payload, the semantic meaning of that payload is likewise profile-defined.
</p>

<hr/>

<h2 id="python-primitives">9. Python Primitives</h2>

<h3>9.1 <code>frog.connectivity.python.call_text</code></h3>

<p>
Invokes a Python function using a textual request payload and returns a textual response payload.
</p>

<ul>
  <li>input ports: <code>module</code>, <code>function</code>, <code>request</code></li>
  <li>output ports: <code>response</code>, <code>success</code></li>
</ul>

<p>
Types:
</p>

<ul>
  <li><code>module: string</code></li>
  <li><code>function: string</code></li>
  <li><code>request: string</code></li>
  <li><code>response: string</code></li>
  <li><code>success: bool</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>if <code>success = true</code>, <code>response</code> contains the textual result produced by the addressed Python function under the active execution profile,</li>
  <li>if <code>success = false</code>, <code>response</code> MUST be the empty string,</li>
  <li>Python environment resolution, import rules, and function dispatch are profile-defined.</li>
</ul>

<h3>9.2 <code>frog.connectivity.python.call_bytes</code></h3>

<p>
Invokes a Python function using a byte request payload and returns a byte response payload.
</p>

<ul>
  <li>input ports: <code>module</code>, <code>function</code>, <code>request</code></li>
  <li>output ports: <code>response</code>, <code>success</code></li>
</ul>

<p>
Types:
</p>

<ul>
  <li><code>module: string</code></li>
  <li><code>function: string</code></li>
  <li><code>request: array&lt;u8&gt;</code></li>
  <li><code>response: array&lt;u8&gt;</code></li>
  <li><code>success: bool</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>if <code>success = true</code>, <code>response</code> contains the byte result produced by the addressed Python function under the active execution profile,</li>
  <li>if <code>success = false</code>, <code>response</code> MUST be the empty byte array.</li>
</ul>

<hr/>

<h2 id="native-primitives">10. Native and Shared Library Primitives</h2>

<h3>10.1 <code>frog.connectivity.native.call_bytes</code></h3>

<p>
Invokes an entry point from a native or shared library using a byte request payload and returns a byte response payload.
</p>

<ul>
  <li>input ports: <code>library</code>, <code>symbol</code>, <code>request</code></li>
  <li>output ports: <code>response</code>, <code>success</code></li>
</ul>

<p>
Types:
</p>

<ul>
  <li><code>library: string</code></li>
  <li><code>symbol: string</code></li>
  <li><code>request: array&lt;u8&gt;</code></li>
  <li><code>response: array&lt;u8&gt;</code></li>
  <li><code>success: bool</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>if <code>success = true</code>, <code>response</code> contains the byte result produced by the addressed native/shared-library entry point under the active execution profile,</li>
  <li>if <code>success = false</code>, <code>response</code> MUST be the empty byte array,</li>
  <li>library resolution, calling convention, symbol visibility, ABI compatibility, and memory ownership rules are profile-defined.</li>
</ul>

<hr/>

<h2 id="dotnet-primitives">11. .NET Primitives</h2>

<h3>11.1 <code>frog.connectivity.dotnet.call_text</code></h3>

<p>
Invokes a .NET method using a textual request payload and returns a textual response payload.
</p>

<ul>
  <li>input ports: <code>assembly</code>, <code>type_name</code>, <code>method</code>, <code>request</code></li>
  <li>output ports: <code>response</code>, <code>success</code></li>
</ul>

<p>
Types:
</p>

<ul>
  <li><code>assembly: string</code></li>
  <li><code>type_name: string</code></li>
  <li><code>method: string</code></li>
  <li><code>request: string</code></li>
  <li><code>response: string</code></li>
  <li><code>success: bool</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>if <code>success = true</code>, <code>response</code> contains the textual result produced by the addressed .NET method under the active execution profile,</li>
  <li>if <code>success = false</code>, <code>response</code> MUST be the empty string,</li>
  <li>assembly resolution, type lookup, method binding, runtime loading, and instance/static dispatch policy are profile-defined.</li>
</ul>

<hr/>

<h2 id="sql-primitives">12. SQL Primitives</h2>

<h3>12.1 <code>frog.connectivity.sql.query_text</code></h3>

<p>
Executes a SQL query and returns a textual result document.
</p>

<ul>
  <li>input ports: <code>connection</code>, <code>query</code>, <code>parameters</code></li>
  <li>output ports: <code>rows</code>, <code>success</code></li>
</ul>

<p>
Types:
</p>

<ul>
  <li><code>connection: string</code></li>
  <li><code>query: string</code></li>
  <li><code>parameters: string</code></li>
  <li><code>rows: string</code></li>
  <li><code>success: bool</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>if <code>success = true</code>, <code>rows</code> contains the query result encoded as a profile-defined textual result document,</li>
  <li>if <code>success = false</code>, <code>rows</code> MUST be the empty string,</li>
  <li>the textual form of <code>parameters</code> is profile-defined,</li>
  <li>connection-string interpretation, driver selection, dialect behavior, and result encoding are profile-defined.</li>
</ul>

<h3>12.2 <code>frog.connectivity.sql.execute</code></h3>

<p>
Executes a non-query SQL statement and returns an affected-row count.
</p>

<ul>
  <li>input ports: <code>connection</code>, <code>query</code>, <code>parameters</code></li>
  <li>output ports: <code>affected_rows</code>, <code>success</code></li>
</ul>

<p>
Types:
</p>

<ul>
  <li><code>connection: string</code></li>
  <li><code>query: string</code></li>
  <li><code>parameters: string</code></li>
  <li><code>affected_rows: i64</code></li>
  <li><code>success: bool</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li>if <code>success = true</code>, <code>affected_rows</code> contains the affected-row count produced by the active execution profile,</li>
  <li>if <code>success = false</code>, <code>affected_rows</code> MUST be <code>0</code>,</li>
  <li>the textual form of <code>parameters</code> is profile-defined.</li>
</ul>

<p>
In v0.1, SQL primitives do not standardize source-level transactions, prepared-statement handles, cursor iteration, or connection lifetime control.
</p>

<hr/>

<h2 id="diagram-representation">13. Diagram Representation</h2>

<p>
Calls to <code>frog.connectivity</code> primitives are serialized as <code>primitive</code> nodes in the diagram.
</p>

<p>
Examples:
</p>

<pre>
{
  "id": "py_eval_1",
  "kind": "primitive",
  "type": "frog.connectivity.python.call_text"
}
</pre>

<pre>
{
  "id": "native_call_1",
  "kind": "primitive",
  "type": "frog.connectivity.native.call_bytes"
}
</pre>

<pre>
{
  "id": "sql_query_1",
  "kind": "primitive",
  "type": "frog.connectivity.sql.query_text"
}
</pre>

<p>
The exact port existence, direction, and typing of these nodes are resolved from this specification together with the type system and the graph rules.
</p>

<hr/>

<h2 id="validation-rules">14. Validation Rules</h2>

<p>
Implementations MUST enforce the following rules:
</p>

<ul>
  <li>every <code>frog.connectivity</code> primitive reference MUST identify a valid standardized connectivity primitive name,</li>
  <li>all required input ports MUST exist and be type-compatible,</li>
  <li>all produced output ports MUST match the primitive definition,</li>
  <li>all identifier-like selector ports in this document MUST use type <code>string</code> in v0.1,</li>
  <li>all byte payload ports in this document MUST use type <code>array&lt;u8&gt;</code>,</li>
  <li>all success outputs MUST use type <code>bool</code>.</li>
</ul>

<p>
For result-bearing primitives:
</p>

<ul>
  <li>a <code>success</code> output MUST exist,</li>
  <li>fallback values for unsuccessful results MUST match the definitions in this specification.</li>
</ul>

<p>
For <code>frog.connectivity.sql.execute</code>:
</p>

<ul>
  <li><code>affected_rows</code> MUST use type <code>i64</code>.</li>
</ul>

<hr/>

<h2 id="examples">15. Examples</h2>

<h3>15.1 Call a Python function with a textual payload</h3>

<pre>
{
  "id": "py_eval_1",
  "kind": "primitive",
  "type": "frog.connectivity.python.call_text"
}
</pre>

<p>
Conceptual ports:
</p>

<pre>
module, function, request → response, success
</pre>

<h3>15.2 Call a native/shared library entry point with a byte payload</h3>

<pre>
{
  "id": "native_call_1",
  "kind": "primitive",
  "type": "frog.connectivity.native.call_bytes"
}
</pre>

<p>
Conceptual ports:
</p>

<pre>
library, symbol, request → response, success
</pre>

<h3>15.3 Execute a SQL query</h3>

<pre>
{
  "id": "sql_query_1",
  "kind": "primitive",
  "type": "frog.connectivity.sql.query_text"
}
</pre>

<p>
Conceptual ports:
</p>

<pre>
connection, query, parameters → rows, success
</pre>

<hr/>

<h2 id="out-of-scope-for-v01">16. Out of Scope for v0.1</h2>

<ul>
  <li>persistent foreign handles or object references as source-level standardized values,</li>
  <li>standardized reflection over Python objects, .NET objects, or native ABI structures,</li>
  <li>automatic bidirectional mapping between arbitrary FROG values and foreign structured types,</li>
  <li>callbacks and re-entrant invocation into FROG graphs,</li>
  <li>transaction control primitives such as begin, commit, and rollback,</li>
  <li>prepared statements, cursors, and row-by-row iteration,</li>
  <li>network protocols such as HTTP, TCP, UDP, WebSocket, MQTT, or gRPC,</li>
  <li>COM, ActiveX, Java, or other non-listed foreign platforms,</li>
  <li>generic external-runtime or external-service primitives beyond the explicit families standardized here,</li>
  <li>async execution, futures, promises, channels, or runtime scheduling primitives.</li>
</ul>

<hr/>

<h2 id="summary">17. Summary</h2>

<p>
The <code>frog.connectivity</code> library defines a minimal standard interoperability surface for FROG v0.1.
</p>

<p>
It standardizes conservative request/response primitives for Python, native/shared libraries, .NET, and SQL while remaining compatible with the current FROG source and type model.
</p>

<p>
In short:
</p>

<ul>
  <li><code>frog.io</code> covers file, path, and resource I/O,</li>
  <li><code>frog.ui</code> covers widget interaction,</li>
  <li><code>frog.connectivity</code> covers foreign-runtime, native/shared-library, managed-platform, and SQL interoperability,</li>
  <li>richer sessions, handles, callbacks, broader service bindings, and async coordination remain for later revisions.</li>
</ul>
