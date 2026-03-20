<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 Example 03 — UI Property Write</h1>

<p align="center">
  Minimal object-style widget interaction example for FROG v0.1<br/>
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
This example is the first minimal FROG program that uses the <strong>object-style UI interaction path</strong>.
It receives one public string input,
creates one diagram-side widget reference,
and writes that string into the <code>text</code> property of the widget's <code>label</code> part through the standardized primitive <code>frog.ui.property_write</code>.
</p>

<p>
This example intentionally does <strong>not</strong> use:
</p>

<ul>
  <li><code>widget_value</code>,</li>
  <li><code>frog.ui.property_read</code>,</li>
  <li><code>frog.ui.method_invoke</code>,</li>
  <li>structured control,</li>
  <li>explicit local memory.</li>
</ul>

<hr/>

<h2 id="purpose">2. Purpose of this Example</h2>

<p>
The purpose of this example is to provide the smallest useful slice that demonstrates:
</p>

<ul>
  <li>diagram-side <code>widget_reference</code> participation,</li>
  <li>use of a standardized UI primitive as an ordinary <code>primitive</code> node,</li>
  <li>member addressing through <code>widget_member</code>,</li>
  <li>clear separation between public interface input and UI-object interaction,</li>
  <li>a backend handoff that still preserves UI-object interaction meaning without collapsing it into generic valueflow.</li>
</ul>

<p>
This is the baseline case for object-style widget access in the first backend family and reference runtime.
</p>

<hr/>

<h2 id="constructs-used">3. Constructs Used</h2>

<p>
This example uses the following constructs:
</p>

<ul>
  <li>one public input port in <code>interface.inputs</code>,</li>
  <li>one optional <code>front_panel</code> section,</li>
  <li>one standard widget instance declared in the front panel,</li>
  <li>one diagram-side <code>interface_input</code> node,</li>
  <li>one diagram-side <code>widget_reference</code> node,</li>
  <li>one <code>primitive</code> node of type <code>frog.ui.property_write</code>,</li>
  <li>two directed edges.</li>
</ul>

<p>
The property being written is:
</p>

<pre><code>ctrl_gain.label.text
</code></pre>

<hr/>

<h2 id="source-shape">4. Source Shape</h2>

<p>
The source contains:
</p>

<ul>
  <li>a canonical metadata section,</li>
  <li>a one-input public interface,</li>
  <li>a diagram with one public input, one widget reference, and one property-write primitive,</li>
  <li>a front panel declaring the target widget instance.</li>
</ul>

<p>
Conceptually:
</p>

<pre><code>interface_input(status_text) ----&gt; frog.ui.property_write(label.text)
                                   ^
                                   |
                         widget_reference(ctrl_gain)
</code></pre>

<p>
This example deliberately separates:
</p>

<ul>
  <li>the front-panel widget declaration,</li>
  <li>the diagram-side widget reference anchor,</li>
  <li>the primitive that performs the side-effecting UI write.</li>
</ul>

<hr/>

<h2 id="validation-expectation">5. Validation Expectation</h2>

<p>
This example is expected to validate successfully in base v0.1.
</p>

<p>
A conforming validator should confirm at least that:
</p>

<ul>
  <li>the public interface input is structurally valid,</li>
  <li>the front-panel widget exists and is structurally valid,</li>
  <li>the <code>widget_reference</code> node references an existing widget,</li>
  <li>the primitive reference <code>frog.ui.property_write</code> is valid,</li>
  <li>the node declares a valid <code>widget_member</code> descriptor,</li>
  <li>the addressed widget part <code>label</code> exists,</li>
  <li>the addressed property <code>text</code> exists and is writable,</li>
  <li>the public string input is type-compatible with the addressed property type,</li>
  <li>the primitive <code>ref</code> and <code>value</code> ports are connected correctly.</li>
</ul>

<hr/>

<h2 id="derivation-expectation">6. Derivation Expectation</h2>

<p>
Execution IR derivation should preserve the following distinctions explicitly:
</p>

<ul>
  <li>public interface entry participation for <code>status</code>,</li>
  <li>widget-reference participation for <code>ctrl_gain</code>,</li>
  <li>primitive execution identity for <code>frog.ui.property_write</code>,</li>
  <li>the member-addressing role <code>{ "part": "label", "member": "text" }</code>,</li>
  <li>the two validated edges that feed the primitive.</li>
</ul>

<p>
Nothing in this example should be reinterpreted as:
</p>

<ul>
  <li>natural <code>widget_value</code> participation,</li>
  <li>property access to widget member <code>value</code>,</li>
  <li>public interface output,</li>
  <li>structured control,</li>
  <li>explicit local memory.</li>
</ul>

<hr/>

<h2 id="backend-contract-expectation">7. Backend Contract Expectation</h2>

<p>
After lowering,
a backend contract for this example should still make clear:
</p>

<ul>
  <li>that one consumable execution unit is being offered,</li>
  <li>that the unit requires object-style UI interaction support,</li>
  <li>that the contract carries one widget-reference participation,</li>
  <li>that the contract carries one UI-object property-write operation,</li>
  <li>that the property write is not the same thing as ordinary widget-value flow,</li>
  <li>that no first-class event execution model is implied by this program.</li>
</ul>

<p>
A backend family may lower widget references to runtime handles
and property writes to family-specific operation descriptors,
but it should not collapse the reference object and the primitive operation into one untyped generic concept.
</p>

<hr/>

<h2 id="reference-runtime-expectation">8. Reference Runtime Expectation</h2>

<p>
A first reference implementation should be able to:
</p>

<ul>
  <li>load this file,</li>
  <li>validate the front panel, interface, and diagram together,</li>
  <li>derive an Execution IR that preserves widget-reference participation and primitive UI operation distinctly,</li>
  <li>lower it for the first host-oriented backend family,</li>
  <li>emit a backend contract that still states UI-object interaction clearly,</li>
  <li>run it by resolving a runtime widget handle and applying the property write.</li>
</ul>

<p>
A simple runtime-facing interpretation is:
</p>

<pre><code>ctrl_gain.label.text = status
</code></pre>

<hr/>

<h2 id="why-this-example-matters">9. Why this Example Matters</h2>

<p>
This example matters because it is the first clean proof that FROG can express object-style UI interaction without confusing:
</p>

<ul>
  <li>front-panel widget declaration,</li>
  <li>diagram-side widget reference participation,</li>
  <li>the primitive that performs a UI side effect,</li>
  <li>natural widget primary-value flow.</li>
</ul>

<p>
If a toolchain cannot handle this example coherently,
it is not ready for richer UI interaction,
method invocation,
or more advanced runtime-side UI binding.
</p>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
This example is the minimal object-style UI interaction program for the first FROG execution slice.
It uses one public input,
one front-panel widget declaration,
one diagram-side <code>widget_reference</code>,
one standardized UI primitive,
and two directed edges.
It should validate cleanly,
derive cleanly,
and remain easy to lower and consume in a first reference runtime with explicit widget-handle and property-write support.
</p>
