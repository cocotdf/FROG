<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 Example 01 — Pure Addition</h1>

<p align="center">
  Minimal public-interface arithmetic example for the first executable FROG slice<br/>
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
  <li><a href="#lowering-and-contract-expectation">7. Lowering and Backend Contract Expectation</a></li>
  <li><a href="#reference-implementation-path">8. Reference Implementation Path</a></li>
  <li><a href="#why-this-example-matters">9. Why this Example Matters</a></li>
  <li><a href="#summary">10. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This example is the smallest useful executable FROG program for the first vertical slice of the repository.
It receives two public floating-point inputs, applies one core arithmetic primitive, and exposes the result through one public floating-point output.
</p>

<p>
It is intentionally minimal.
There is no front panel participation,
no widget participation,
no structure,
and no explicit local memory.
</p>

<p>
This example is the recommended entry point for the first executable reference slice because it exercises the full architectural chain without introducing early UI or state complexity.
</p>

<hr/>

<h2 id="purpose">2. Purpose of this Example</h2>

<p>
The purpose of this example is to provide a clean baseline case for:
</p>

<ul>
  <li>canonical source loading,</li>
  <li>basic interface validation,</li>
  <li>basic diagram validation,</li>
  <li>Execution IR derivation of public-boundary participation and primitive execution,</li>
  <li>controlled lowering for a first backend family,</li>
  <li>backend contract emission for a minimal execution unit,</li>
  <li>first reference-runtime consumption of that contract.</li>
</ul>

<p>
This is the smallest published example that still exercises the complete source-to-execution path without bringing in UI object interaction, structured control, explicit memory, or profile-dependent capabilities.
</p>

<hr/>

<h2 id="constructs-used">3. Constructs Used</h2>

<p>
This example uses only the following constructs:
</p>

<ul>
  <li>two public input ports in <code>interface.inputs</code>,</li>
  <li>one public output port in <code>interface.outputs</code>,</li>
  <li>two <code>interface_input</code> nodes in the diagram,</li>
  <li>one <code>primitive</code> node of type <code>frog.core.add</code>,</li>
  <li>one <code>interface_output</code> node in the diagram,</li>
  <li>three directed edges.</li>
</ul>

<p>
No widget participation is involved.
No structure is involved.
No explicit local-memory construct is involved.
</p>

<hr/>

<h2 id="source-shape">4. Source Shape</h2>

<p>
The canonical source shape is intentionally small.
At minimum, this example requires:
</p>

<pre><code>{
  "spec_version": "0.1",
  "metadata": { ... },
  "interface": { ... },
  "diagram": { ... }
}
</code></pre>

<p>
The public interface declares:
</p>

<ul>
  <li>input <code>a : f64</code>,</li>
  <li>input <code>b : f64</code>,</li>
  <li>output <code>result : f64</code>.</li>
</ul>

<p>
The executable diagram expresses:
</p>

<pre><code>interface_input(a) ---\
                       &gt; frog.core.add ---&gt; interface_output(result)
interface_input(b) ---/
</code></pre>

<p>
The published source file may contain richer metadata fields, but the executable meaning of this example comes from the public interface, the primitive identity, and the validated edge wiring.
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
  <li>the required top-level sections are present,</li>
  <li>the source structure is well-formed,</li>
  <li>interface port identifiers are valid and unique,</li>
  <li>declared value types are valid for the accepted subset,</li>
  <li>the primitive reference <code>frog.core.add</code> is valid,</li>
  <li>all edge endpoints are valid,</li>
  <li>the primitive input ports <code>a</code> and <code>b</code> are each driven exactly once,</li>
  <li>the primitive output port <code>result</code> is routed to the public output boundary,</li>
  <li>no UI or memory semantics are inferred from this source.</li>
</ul>

<p>
For the first executable slice, this example should remain a straightforward success case rather than an ambiguous edge case.
</p>

<hr/>

<h2 id="derivation-expectation">6. Derivation Expectation</h2>

<p>
Execution IR derivation should preserve the following distinctions explicitly:
</p>

<ul>
  <li>the execution-unit identity of the whole FROG program,</li>
  <li>public interface entry participation for <code>a</code>,</li>
  <li>public interface entry participation for <code>b</code>,</li>
  <li>primitive execution identity for <code>frog.core.add</code>,</li>
  <li>public interface exit participation for <code>result</code>,</li>
  <li>the validated dependency edges between those objects.</li>
</ul>

<p>
Nothing in this example should be reinterpreted as:
</p>

<ul>
  <li>UI participation,</li>
  <li>object-style widget access,</li>
  <li>structured control,</li>
  <li>explicit local memory,</li>
  <li>hidden scheduler-private semantics.</li>
</ul>

<hr/>

<h2 id="lowering-and-contract-expectation">7. Lowering and Backend Contract Expectation</h2>

<p>
After lowering, a backend contract for this example should still make clear:
</p>

<ul>
  <li>that one consumable execution unit is being offered,</li>
  <li>that the unit has two public inputs and one public output,</li>
  <li>that the computation is ordinary arithmetic addition,</li>
  <li>that no explicit local-memory semantics are involved,</li>
  <li>that no UI participation is required for this example.</li>
</ul>

<p>
A backend family may specialize argument passing, evaluation order realization, or contract details, but it should not erase the public-boundary origin of the values and should not silently reinterpret this example as a UI or stateful program.
</p>

<hr/>

<h2 id="reference-implementation-path">8. Reference Implementation Path</h2>

<p>
This example is the recommended first target for the non-normative reference implementation workspace under:
</p>

<pre><code>Implementations/Reference/</code></pre>

<p>
A first demonstration pipeline should be able to:
</p>

<ul>
  <li>load this file,</li>
  <li>validate it,</li>
  <li>derive a corresponding Execution IR,</li>
  <li>lower it for the first backend family,</li>
  <li>emit a backend contract,</li>
  <li>run it as a callable computation or testable execution unit.</li>
</ul>

<p>
A simple runtime-facing interpretation is:
</p>

<pre><code>result = a + b</code></pre>

<p>
A compact demonstration flow may therefore look like:
</p>

<pre><code>python Implementations/Reference/CLI/frog_demo_pipeline.py validate Examples/01_pure_addition/main.frog
python Implementations/Reference/CLI/frog_demo_pipeline.py derive-ir Examples/01_pure_addition/main.frog
python Implementations/Reference/CLI/frog_demo_pipeline.py lower Examples/01_pure_addition/main.frog
python Implementations/Reference/CLI/frog_demo_pipeline.py emit-contract Examples/01_pure_addition/main.frog
python Implementations/Reference/CLI/frog_demo_pipeline.py run Examples/01_pure_addition/main.frog --inputs "{\"a\": 2.25, \"b\": 3.75}"</code></pre>

<p>
These commands are implementation-side demonstration commands.
They do not define the language.
They demonstrate that the published boundaries are executable for the first slice.
</p>

<hr/>

<h2 id="why-this-example-matters">9. Why this Example Matters</h2>

<p>
This example matters because it is the first clean “nothing extra” slice.
If a toolchain cannot handle this example coherently, it is not ready to move on to UI participation, widget references, structured control, or explicit local memory.
</p>

<p>
It is therefore a baseline case for:
</p>

<ul>
  <li>basic correctness,</li>
  <li>basic source-to-IR continuity,</li>
  <li>basic lowering discipline,</li>
  <li>basic backend-hand-off clarity,</li>
  <li>basic runtime-consumption correctness.</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
This example is the minimal public-interface arithmetic program for the first FROG execution slice.
It uses only public interface participation,
one core arithmetic primitive,
and directed connections.
It should validate cleanly,
derive cleanly,
lower cleanly,
and remain easy to consume in an early backend contract and reference runtime.
</p>

<p>
That is why it is the correct first executable target for the reference implementation.
</p>
