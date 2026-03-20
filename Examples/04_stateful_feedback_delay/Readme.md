<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 Example 04 — Stateful Feedback with Explicit Delay</h1>

<p align="center">
  Minimal explicit local-memory feedback example for FROG v0.1<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#purpose">2. Purpose of this Example</a></li>
  <li><a href="#constructs-used">3. Constructs Used</a></li>
  <li><a href="#source-shape">4. Source Shape</a></li>
  <li><a href="#validation-expectation">5. Validation Expectation</a></li>
  <li><a href="#derivation-expectation">6. Derivation Expectation</a></li>
  <li><a href="#backend-contract-expectation">7. Backend Contract Expectation</a></li>
  <li><a href="#reference-runtime-expectation">8. Reference Runtime Expectation</a></li>
  <li><a href="#why-this-example-matters">9. Why this Example Matters</a></li>
  <li><a href="#summary">10. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This example is the first minimal FROG program that contains a <strong>valid feedback cycle</strong>.
The cycle is valid only because it contains one explicit local-memory primitive:
<code>frog.core.delay</code>.
</p>

<p>
The program receives one public floating-point input,
adds it to the delayed previous value,
feeds the result back through the delay,
and also exposes that result through one public floating-point output.
</p>

<p>
This example intentionally does <strong>not</strong> use:
</p>

<ul>
  <li>front-panel widgets,</li>
  <li><code>widget_value</code>,</li>
  <li><code>widget_reference</code>,</li>
  <li>standardized UI-object primitives,</li>
  <li>structured control.</li>
</ul>

<hr/>

<h2 id="purpose">2. Purpose of this Example</h2>

<p>
The purpose of this example is to provide the smallest useful slice that demonstrates:
</p>

<ul>
  <li>a directed feedback path,</li>
  <li>cycle validity through explicit local memory,</li>
  <li>required deterministic initialization through <code>initial</code>,</li>
  <li>preservation of explicit state through Execution IR derivation,</li>
  <li>a backend handoff that still carries explicit state semantics rather than hiding them inside runtime-private machinery.</li>
</ul>

<p>
This is the baseline example for stateful recurrence in the first executable vertical slice of FROG.
</p>

<hr/>

<h2 id="constructs-used">3. Constructs Used</h2>

<p>
This example uses the following constructs:
</p>

<ul>
  <li>one public input port in <code>interface.inputs</code>,</li>
  <li>one public output port in <code>interface.outputs</code>,</li>
  <li>one diagram-side <code>interface_input</code> node,</li>
  <li>one <code>primitive</code> node of type <code>frog.core.add</code>,</li>
  <li>one <code>primitive</code> node of type <code>frog.core.delay</code>,</li>
  <li>one required <code>initial</code> value on the delay node,</li>
  <li>one diagram-side <code>interface_output</code> node,</li>
  <li>four directed edges.</li>
</ul>

<p>
All carried values in this example use the canonical FROG value type <code>f64</code>.
</p>

<hr/>

<h2 id="source-shape">4. Source Shape</h2>

<p>
The public interface declares:
</p>

<ul>
  <li>input <code>x : f64</code>,</li>
  <li>output <code>y : f64</code>.</li>
</ul>

<p>
The executable diagram expresses:
</p>

<pre><code>interface_input(x) ------&gt; frog.core.add(a)
                             ^
                             |
                     frog.core.delay(out)
                             ^
                             |
                 frog.core.add(result)
                             |
                             +------&gt; interface_output(y)
                             |
                             +------&gt; frog.core.delay(in)
</code></pre>

<p>
The delay node carries:
</p>

<pre><code>{
  "kind": "primitive",
  "type": "frog.core.delay",
  "initial": 0.0
}
</code></pre>

<p>
This makes the feedback explicit,
deterministic,
and valid in principle.
</p>

<hr/>

<h2 id="validation-expectation">5. Validation Expectation</h2>

<p>
This example is expected to validate successfully in base v0.1.
</p>

<p>
A conforming validator should confirm at least that:
</p>

<ul>
  <li>the public interface is structurally valid,</li>
  <li>the primitive reference <code>frog.core.add</code> is valid,</li>
  <li>the primitive reference <code>frog.core.delay</code> is valid,</li>
  <li>the delay node defines the required <code>initial</code> field,</li>
  <li><code>initial</code> is type-compatible with the carried value type,</li>
  <li>the delay ports <code>in</code> and <code>out</code> are used correctly,</li>
  <li>the directed cycle is valid because it contains an explicit local-memory primitive,</li>
  <li>the graph does not rely on implicit memory or hidden scheduler repair.</li>
</ul>

<hr/>

<h2 id="derivation-expectation">6. Derivation Expectation</h2>

<p>
Execution IR derivation should preserve the following distinctions explicitly:
</p>

<ul>
  <li>public interface entry participation for <code>x</code>,</li>
  <li>primitive execution identity for <code>frog.core.add</code>,</li>
  <li>explicit local-memory execution identity for <code>frog.core.delay</code>,</li>
  <li>the required explicit initial-state value,</li>
  <li>public interface exit participation for <code>y</code>,</li>
  <li>the feedback connectivity that makes the recurrence explicit.</li>
</ul>

<p>
The derived IR must not reinterpret this program as:
</p>

<ul>
  <li>a pure combinational graph,</li>
  <li>a valid cycle repaired by hidden memory insertion,</li>
  <li>a scheduler-private recurrence with no attributable state object.</li>
</ul>

<hr/>

<h2 id="backend-contract-expectation">7. Backend Contract Expectation</h2>

<p>
After lowering,
a backend contract for this example should still make clear:
</p>

<ul>
  <li>that one consumable execution unit is being offered,</li>
  <li>that explicit local memory is required for correct meaning,</li>
  <li>that the delay state has a deterministic initial value,</li>
  <li>that the feedback is stateful rather than combinational,</li>
  <li>that the consumer must preserve state semantics rather than silently reinterpreting them.</li>
</ul>

<p>
A backend family may lower the stateful behavior into reads,
writes,
commits,
buffers,
or family-specific state cells,
but it should not erase the fact that the program meaning depends on one explicit local-memory primitive.
</p>

<hr/>

<h2 id="reference-runtime-expectation">8. Reference Runtime Expectation</h2>

<p>
A first reference implementation should be able to:
</p>

<ul>
  <li>load this file,</li>
  <li>validate the cycle and the delay node,</li>
  <li>derive an Execution IR that preserves explicit local memory as explicit local memory,</li>
  <li>lower it for the first backend family,</li>
  <li>emit a backend contract that still states explicit state semantics clearly,</li>
  <li>run it with deterministic state initialization and deterministic state update across activations.</li>
</ul>

<p>
A simple runtime-facing interpretation is:
</p>

<pre><code>y(t) = x(t) + state(t)
state(t + 1) = y(t)
state(0) = 0.0
</code></pre>

<hr/>

<h2 id="why-this-example-matters">9. Why this Example Matters</h2>

<p>
This example matters because it is the first clean proof that FROG can express recurrence without hidden scheduler magic.
It closes the minimal language-core slice for:
</p>

<ul>
  <li>feedback legality,</li>
  <li>explicit memory,</li>
  <li>deterministic initialization,</li>
  <li>state-preserving derivation,</li>
  <li>state-preserving backend handoff.</li>
</ul>

<p>
If a toolchain cannot handle this example coherently,
it is not yet ready for richer stateful behavior,
loop-carried recurrence,
or more advanced runtime families.
</p>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
This example is the minimal explicit-memory feedback program for the first FROG execution slice.
It uses one public input,
one public output,
one arithmetic primitive,
one explicit local-memory primitive,
and one valid feedback cycle.
It should validate cleanly,
derive cleanly,
and remain easy to lower and consume in a first reference runtime that preserves state semantics explicitly.
</p>
