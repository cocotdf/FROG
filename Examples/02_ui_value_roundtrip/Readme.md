<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">🐸 Example 02 — UI Value Roundtrip</h1>

<p align="center">
  Minimal front-panel value participation example for FROG v0.1<br/>
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
This example is the first minimal FROG program that includes a serialized <code>front_panel</code> and natural widget-value participation in the executable diagram.
It reads two numeric control values from the front panel,
adds them through one core primitive,
and writes the computed result to one numeric indicator.
</p>

<p>
It intentionally uses the natural primary-value path only.
It does not use:
</p>

<ul>
  <li>public interface participation,</li>
  <li><code>widget_reference</code>,</li>
  <li><code>frog.ui.property_read</code>,</li>
  <li><code>frog.ui.property_write</code>,</li>
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
  <li>front-panel widget declaration,</li>
  <li>natural <code>widget_value</code> participation in the diagram,</li>
  <li>directional use of controls and indicators,</li>
  <li>ordinary primitive computation over widget-driven values,</li>
  <li>a backend handoff that still carries UI-value participation without introducing object-style widget access.</li>
</ul>

<p>
This is the baseline case for the first reference runtime family that supports value binding between the front panel and executable behavior.
</p>

<hr/>

<h2 id="constructs-used">3. Constructs Used</h2>

<p>
This example uses only the following constructs:
</p>

<ul>
  <li>an optional <code>front_panel</code> section,</li>
  <li>two value-carrying widgets of class <code>frog.ui.standard.numeric_control</code>,</li>
  <li>one value-carrying widget of class <code>frog.ui.standard.numeric_indicator</code>,</li>
  <li>three diagram-side <code>widget_value</code> nodes,</li>
  <li>one <code>primitive</code> node of type <code>frog.core.add</code>,</li>
  <li>three directed edges.</li>
</ul>

<p>
All value-carrying widgets in this example use the canonical FROG value type <code>f64</code>.
</p>

<hr/>

<h2 id="source-shape">4. Source Shape</h2>

<p>
The source contains:
</p>

<ul>
  <li>a canonical metadata section,</li>
  <li>an empty public interface,</li>
  <li>a diagram with widget-value participation and one arithmetic primitive,</li>
  <li>a front panel declaring the widget instances used by the diagram.</li>
</ul>

<p>
Conceptually:
</p>

<pre><code>front_panel widgets:
  ctrl_a      : numeric_control(f64)
  ctrl_b      : numeric_control(f64)
  ind_result  : numeric_indicator(f64)

diagram:
  widget_value(ctrl_a) ---\
                           &gt; frog.core.add ---&gt; widget_value(ind_result)
  widget_value(ctrl_b) ---/
</code></pre>

<p>
The front panel owns widget declaration and composition.
The diagram owns executable participation.
This example relies on that separation explicitly.
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
  <li>the <code>front_panel</code> section is structurally valid,</li>
  <li>widget identifiers are unique,</li>
  <li>the widget classes are valid standard widget classes,</li>
  <li>the value type <code>f64</code> is valid for standard numeric controls and numeric indicators,</li>
  <li>every <code>widget_value</code> node references an existing value-carrying widget,</li>
  <li>the output of each control-side <code>widget_value</code> participation is routed correctly to the primitive inputs,</li>
  <li>the primitive output is routed correctly to the indicator-side <code>widget_value</code> participation.</li>
</ul>

<hr/>

<h2 id="derivation-expectation">6. Derivation Expectation</h2>

<p>
Execution IR derivation should preserve the following distinctions explicitly:
</p>

<ul>
  <li>the execution unit identity of the whole FROG,</li>
  <li>widget-value participation for <code>ctrl_a</code>,</li>
  <li>widget-value participation for <code>ctrl_b</code>,</li>
  <li>primitive execution identity for <code>frog.core.add</code>,</li>
  <li>widget-value participation for <code>ind_result</code>,</li>
  <li>the validated dependency edges between these objects.</li>
</ul>

<p>
Nothing in this example should be reinterpreted as:
</p>

<ul>
  <li>public interface participation,</li>
  <li>object-style widget access,</li>
  <li>property-based access to a widget member named <code>value</code>,</li>
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
  <li>that the computation depends on UI value participation,</li>
  <li>that the UI participation is of the natural <code>widget_value</code> kind,</li>
  <li>that no object-style widget-reference operations are required,</li>
  <li>that no first-class event execution model is implied by this program,</li>
  <li>that no explicit local-memory semantics are involved.</li>
</ul>

<p>
A backend family may lower these value participations to runtime value channels,
binding cells,
or other family-specific mechanisms,
but it should not collapse them into object-style reference interaction.
</p>

<hr/>

<h2 id="reference-runtime-expectation">8. Reference Runtime Expectation</h2>

<p>
A first reference implementation should be able to:
</p>

<ul>
  <li>load this file,</li>
  <li>validate the front panel and the diagram together,</li>
  <li>derive an Execution IR that preserves widget-value participation explicitly,</li>
  <li>lower it for the first host-oriented backend family,</li>
  <li>emit a backend contract that still states UI value participation clearly,</li>
  <li>run it with a simple value-binding runtime strategy.</li>
</ul>

<p>
A simple runtime-facing interpretation is:
</p>

<pre><code>ind_result.value = ctrl_a.value + ctrl_b.value
</code></pre>

<hr/>

<h2 id="why-this-example-matters">9. Why this Example Matters</h2>

<p>
This example is the first clean proof that FROG can carry user-facing values through the published architecture without confusing:
</p>

<ul>
  <li>front-panel declaration,</li>
  <li>diagram-side value participation,</li>
  <li>object-style widget interaction.</li>
</ul>

<p>
If a toolchain cannot handle this example coherently,
it is not ready to move on to:
</p>

<ul>
  <li><code>widget_reference</code>,</li>
  <li><code>frog.ui.property_read</code> or <code>frog.ui.property_write</code>,</li>
  <li>UI-aware backend contracts,</li>
  <li>reference runtime UI binding.</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
This example is the minimal natural UI-value program for the first FROG execution slice.
It uses only front-panel widget declaration,
diagram-side <code>widget_value</code> participation,
one arithmetic primitive,
and directed connections.
It should validate cleanly,
derive cleanly,
and remain easy to lower and run in a first reference host runtime with value binding.
</p>
