<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Examples</h1>

<p align="center">
  <strong>Minimal example programs for the published FROG specification</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-directory-exists">2. Why this Directory Exists</a></li>
  <li><a href="#what-examples-are-for">3. What Examples Are For</a></li>
  <li><a href="#what-examples-are-not">4. What Examples Are Not</a></li>
  <li><a href="#relation-with-the-specification">5. Relation with the Specification</a></li>
  <li><a href="#example-design-rules">6. Example Design Rules</a></li>
  <li><a href="#recommended-example-shape">7. Recommended Example Shape</a></li>
  <li><a href="#first-example-slices">8. First Example Slices</a></li>
  <li><a href="#how-to-read-an-example">9. How to Read an Example</a></li>
  <li><a href="#relation-with-conformance-and-reference-implementation">10. Relation with Conformance and Reference Implementation</a></li>
  <li><a href="#status-in-v01">11. Status in v0.1</a></li>
  <li><a href="#summary">12. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory contains <strong>minimal example FROG programs</strong> used to illustrate and exercise the published specification.
Each example is intended to be small, readable, architecturally meaningful, and directly tied to one or more boundaries already defined elsewhere in the repository.
</p>

<p>
Examples exist to make the specification easier to read, easier to discuss, easier to implement, and easier to inspect through early toolchains.
They are deliberately practical, but they are <strong>not</strong> the normative source of language truth.
</p>

<pre><code>Examples/
   |
   +-- small published programs
   +-- readable slices of the specification
   +-- early implementation targets
   +-- support material for conformance
</code></pre>

<hr/>

<h2 id="why-this-directory-exists">2. Why this Directory Exists</h2>

<p>
The FROG repository defines a layered architecture:
</p>

<ul>
  <li>canonical source,</li>
  <li>validated program meaning,</li>
  <li>open execution-facing IR,</li>
  <li>lowering and backend-facing handoff,</li>
  <li>private realization by implementations.</li>
</ul>

<p>
That architecture is intentionally explicit.
However, architectural precision alone is not enough to support early validators, early execution experiments, or a future reference implementation.
A dedicated examples directory is therefore needed to provide:
</p>

<ul>
  <li>small canonical source programs,</li>
  <li>clear coverage of important distinctions,</li>
  <li>testable slices of the specification pipeline,</li>
  <li>shared named programs for future implementations.</li>
</ul>

<p>
Without examples, the repository would remain readable in principle but harder to approach in practice.
Examples are the smallest public bridge between specification text and executable experimentation.
</p>

<hr/>

<h2 id="what-examples-are-for">3. What Examples Are For</h2>

<p>
Examples in this directory are intended to serve several purposes at once:
</p>

<ul>
  <li><strong>reading support</strong> — they make specification boundaries easier to understand,</li>
  <li><strong>implementation support</strong> — they provide small targets for loaders, validators, derivation stages, lowerers, contract emitters, and runtimes,</li>
  <li><strong>discussion support</strong> — they make architectural distinctions visible in concrete form,</li>
  <li><strong>regression support</strong> — they help reveal accidental architectural drift.</li>
</ul>

<p>
A useful early pipeline is:
</p>

<pre><code>example .frog
      |
      v
validation
      |
      v
Execution IR derivation
      |
      v
lowering
      |
      v
backend contract emission
      |
      v
reference runtime experimentation
</code></pre>

<p>
Examples therefore help turn repository architecture into something inspectable and runnable without claiming that the example itself owns the meaning of the language.
</p>

<hr/>

<h2 id="what-examples-are-not">4. What Examples Are Not</h2>

<p>
Examples in this directory are <strong>not</strong>:
</p>

<ul>
  <li>a replacement for the normative specification,</li>
  <li>a conformance decision surface,</li>
  <li>a complete tutorial curriculum,</li>
  <li>a frozen implementation test suite,</li>
  <li>a hidden source of semantics that should have lived in <code>Expression/</code>, <code>Language/</code>, or <code>IR/</code>.</li>
</ul>

<p>
If an example appears to define language truth by itself, the owning specification layer should be clarified instead.
</p>

<p>
The core distinction is:
</p>

<pre><code>Examples
    illustrate

Conformance
    declares expected accept / reject / preserve outcomes

Specification
    owns the rules
</code></pre>

<hr/>

<h2 id="relation-with-the-specification">5. Relation with the Specification</h2>

<p>
This directory must be read as <strong>downstream support material</strong> for the published specification.
It does not own semantic or architectural law.
</p>

<p>
Ownership remains:
</p>

<ul>
  <li><code>Expression/</code> — canonical source shape,</li>
  <li><code>Language/</code> — validated semantic truth,</li>
  <li><code>Libraries/</code> — intrinsic primitive catalogs,</li>
  <li><code>Profiles/</code> — optional standardized capability families,</li>
  <li><code>IR/</code> — open execution-facing representation and its derivation, construction, mapping, lowering, and backend handoff boundaries,</li>
  <li><code>IDE/</code> — authoring-facing and observability-facing tooling concerns.</li>
</ul>

<p>
Examples may illustrate those layers.
They must not silently replace them.
</p>

<p>
The reading rule is:
</p>

<pre><code>specification defines
examples illustrate
implementations consume
</code></pre>

<hr/>

<h2 id="example-design-rules">6. Example Design Rules</h2>

<p>
Examples in this directory should follow the rules below:
</p>

<ul>
  <li>Each example should be small enough to understand quickly.</li>
  <li>Each example should highlight one architectural point or one compact cluster of related points.</li>
  <li>Each example should remain close to canonical source rather than to one implementation-private form.</li>
  <li>Each example should avoid unnecessary decorative complexity.</li>
  <li>Each example should state clearly which constructs it is exercising.</li>
  <li>Each example should remain useful to future conformance and implementation work.</li>
</ul>

<p>
Preferred style:
</p>

<pre><code>small
explicit
single-purpose
architecturally meaningful
easy to validate
easy to derive
easy to run in a reference pipeline
</code></pre>

<p>
The goal is not to show everything.
The goal is to show one thing clearly enough that later layers can exercise it without ambiguity.
</p>

<hr/>

<h2 id="recommended-example-shape">7. Recommended Example Shape</h2>

<p>
Each example directory should usually contain:
</p>

<ul>
  <li><code>Readme.md</code> — human-readable explanation of the example,</li>
  <li><code>main.frog</code> — canonical source artifact for the example.</li>
</ul>

<p>
The example README should normally explain:
</p>

<ul>
  <li>the purpose of the example,</li>
  <li>the constructs used,</li>
  <li>which specification documents own those constructs,</li>
  <li>what a validator is expected to accept,</li>
  <li>what derivation should preserve,</li>
  <li>what a lowering or backend handoff may later specialize,</li>
  <li>what a reference implementation is expected to do with the example.</li>
</ul>

<p>
A compact example shape is usually better than a broad one.
An example should be easy to inspect as source first, then easy to carry through later stages.
</p>

<hr/>

<h2 id="first-example-slices">8. First Example Slices</h2>

<p>
For the first executable vertical slices of FROG v0.1, the recommended initial examples are:
</p>

<ul>
  <li><strong>pure addition</strong> — public interface input to primitive to public interface output,</li>
  <li><strong>UI value roundtrip</strong> — <code>widget_value</code> participation through ordinary execution,</li>
  <li><strong>UI property write</strong> — <code>widget_reference</code> plus standardized UI-object primitive operation,</li>
  <li><strong>stateful feedback with explicit delay</strong> — legal feedback requiring explicit local memory.</li>
</ul>

<p>
Together, these examples provide a compact first coverage set for:
</p>

<ul>
  <li>interface boundaries,</li>
  <li>primitive execution,</li>
  <li>IR derivation,</li>
  <li>UI value participation,</li>
  <li>UI object-style interaction,</li>
  <li>explicit local memory.</li>
</ul>

<p>
These examples are intentionally small but architecturally dense.
They are not chosen for breadth.
They are chosen because they expose critical distinctions early.
</p>

<hr/>

<h2 id="how-to-read-an-example">9. How to Read an Example</h2>

<p>
A reader should normally approach each example in the following order:
</p>

<ol>
  <li>read the example README,</li>
  <li>inspect the canonical <code>.frog</code> source,</li>
  <li>check which specification documents own the constructs being used,</li>
  <li>check the corresponding conformance material when available,</li>
  <li>run the example through validation, derivation, lowering, and execution tooling when available.</li>
</ol>

<p>
Examples are therefore intended to be both readable documents and early execution targets.
</p>

<p>
The main reading discipline is:
</p>

<pre><code>read the example
then read the owning specification
not the reverse
</code></pre>

<p>
An example helps the reader enter the specification.
It does not replace the need to read the owning layer.
</p>

<hr/>

<h2 id="relation-with-conformance-and-reference-implementation">10. Relation with Conformance and Reference Implementation</h2>

<p>
This directory is meant to work together with:
</p>

<ul>
  <li><code>Conformance/</code> — which states what should be accepted, rejected, or preserved,</li>
  <li><code>Implementations/Reference/</code> — which may use these examples as the first runnable targets of a reference toolchain.</li>
</ul>

<p>
The distinction must remain explicit:
</p>

<pre><code>Examples/
   provides small named programs

Conformance/
   states expected accept / reject / preserve outcomes

Implementations/Reference/
   attempts to load, validate, derive, lower, emit contracts,
   and eventually run those programs
</code></pre>

<p>
An example may be illustrative without being a full conformance statement.
A conformance case may reference an example but still owns the explicit expectation.
A reference implementation may execute an example correctly, but it does not become language law by doing so.
</p>

<hr/>

<h2 id="status-in-v01">11. Status in v0.1</h2>

<p>
In base v0.1, this directory is intentionally small.
The goal is not breadth.
The goal is to establish a <strong>clean, durable, implementation-useful starting set</strong>.
</p>

<p>
More examples may be added later,
but the first examples should remain carefully chosen and architecturally dense.
</p>

<p>
A good v0.1 example set should be:
</p>

<ul>
  <li>small enough to inspect manually,</li>
  <li>strong enough to drive early implementations,</li>
  <li>clear enough to support future conformance work,</li>
  <li>stable enough to remain useful as the repository grows.</li>
</ul>

<hr/>

<h2 id="summary">12. Summary</h2>

<p>
This directory provides minimal example programs for the published FROG specification.
Its role is to support reading, early execution experiments, future conformance, and a future reference implementation.
</p>

<p>
Examples are intentionally practical,
but they remain downstream from the normative specification layers.
They illustrate the language.
They do not redefine it.
</p>

<p>
The essential distinction is:
</p>

<pre><code>Specification
    owns truth

Examples
    make that truth easier to read

Conformance
    makes that truth testable

Implementations
    must follow accordingly
</code></pre>
