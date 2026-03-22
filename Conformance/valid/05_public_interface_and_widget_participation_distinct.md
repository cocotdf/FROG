<h1>Conformance Case — 05 Public Interface and Widget Participation Distinct</h1>

<p><strong>Valid conformance case for preserving the distinction between public interface participation and natural widget participation in FROG v0.1</strong><br>
FROG — Free Open Graphical Language</p>

<hr>

<h2>Contents</h2>
<ul>
  <li><a href="#case-overview">1. Case Overview</a></li>
  <li><a href="#expected-status">2. Expected Status</a></li>
  <li><a href="#source-target">3. Source Target</a></li>
  <li><a href="#boundaries-exercised">4. Boundaries Exercised</a></li>
  <li><a href="#why-this-case-is-valid">5. Why this Case Is Valid</a></li>
  <li><a href="#expected-validation-outcome">6. Expected Validation Outcome</a></li>
  <li><a href="#expected-derivation-preservation">7. Expected Derivation Preservation</a></li>
  <li><a href="#expected-backend-contract-preservation">8. Expected Backend Contract Preservation</a></li>
  <li><a href="#what-must-not-happen">9. What Must Not Happen</a></li>
  <li><a href="#summary">10. Summary</a></li>
</ul>

<hr>

<h2 id="case-overview">1. Case Overview</h2>

<p>This case covers a minimal valid program shape in which both of the following coexist without semantic collapse:</p>

<ul>
  <li>one public interface input,</li>
  <li>one front-panel numeric control participating through <code>widget_value</code>,</li>
  <li>one ordinary arithmetic primitive,</li>
  <li>one public interface output.</li>
</ul>

<p>The case is intentionally small. Its purpose is not to introduce a new UI object model or a richer event model. Its purpose is to prove that a conforming toolchain can accept a program where:</p>

<ul>
  <li>a public interface boundary exists,</li>
  <li>a widget contributes a value,</li>
  <li>both values participate in the same executable graph,</li>
  <li>the two participation categories remain distinct.</li>
</ul>

<p>A useful conceptual shape is:</p>

<pre><code>public input      widget value
     x                 gain
      \               /
       \             /
        \           /
         +-- add --+
              |
              v
        public output
            result
</code></pre>

<p>This is a valid case only if the implementation preserves that:</p>

<pre><code>interface_input(x) != widget_value(gain)
</code></pre>

<hr>

<h2 id="expected-status">2. Expected Status</h2>

<p>Expected: valid</p>

<p>A conforming toolchain should accept this case as a valid program shape for the published v0.1 architecture.</p>

<hr>

<h2 id="source-target">3. Source Target</h2>

<p>This case is currently defined as a specification-level conformance case.</p>

<p>It is <strong>not yet tied to a required published example slice</strong> in <code>Examples/</code>.</p>

<p>An illustrative source shape would include:</p>

<ul>
  <li>one interface input named <code>x</code>,</li>
  <li>one front-panel numeric control named <code>gain</code>,</li>
  <li>one diagram-side <code>interface_input</code> node for <code>x</code>,</li>
  <li>one diagram-side <code>widget_value</code> node for <code>gain</code>,</li>
  <li>one <code>frog.core.add</code> primitive,</li>
  <li>one diagram-side <code>interface_output</code> node for <code>result</code>.</li>
</ul>

<p>The minimal semantic intent is:</p>

<pre><code>result = x + gain
</code></pre>

<hr>

<h2 id="boundaries-exercised">4. Boundaries Exercised</h2>

<ul>
  <li>public interface declaration,</li>
  <li>front-panel widget declaration,</li>
  <li>diagram-side <code>interface_input</code> participation,</li>
  <li>diagram-side <code>widget_value</code> participation,</li>
  <li>diagram-side <code>interface_output</code> participation,</li>
  <li>ordinary arithmetic primitive execution through <code>frog.core.add</code>,</li>
  <li>clear separation between public contract and widget-owned value participation,</li>
  <li>clear rejection of any attempt to normalize widget participation into interface participation or the reverse.</li>
</ul>

<hr>

<h2 id="why-this-case-is-valid">5. Why this Case Is Valid</h2>

<p>This case is valid because:</p>

<ul>
  <li>the public interface input is well formed and remains part of the public program contract,</li>
  <li>the front-panel widget declaration is well formed and remains widget-owned UI state,</li>
  <li>the diagram-side <code>widget_value</code> references an existing value-carrying widget,</li>
  <li>the arithmetic primitive is used over type-compatible values,</li>
  <li>the graph is acyclic,</li>
  <li>no explicit local memory is required,</li>
  <li>no object-style widget interaction is required,</li>
  <li>no semantic collapse is required to make the program meaningful.</li>
</ul>

<p>The key point is that the case does <strong>not</strong> require the toolchain to pretend that the widget is a public port or that the public port is a widget.</p>

<hr>

<h2 id="expected-validation-outcome">6. Expected Validation Outcome</h2>

<p>A conforming validator should accept the case. It should confirm at minimum that:</p>

<ul>
  <li>the source is structurally valid canonical FROG source,</li>
  <li>the public interface input declaration is valid,</li>
  <li>the public interface output declaration is valid,</li>
  <li>the front-panel widget declaration is valid,</li>
  <li>the selected widget class is value-carrying,</li>
  <li>the declared <code>value_type</code> for the widget is valid,</li>
  <li>the diagram-side <code>interface_input</code> participation refers to an actual public input,</li>
  <li>the diagram-side <code>widget_value</code> participation refers to an actual widget,</li>
  <li>the primitive reference <code>frog.core.add</code> is valid,</li>
  <li>the connected values are type-compatible,</li>
  <li>the public output participation is well formed,</li>
  <li>the case does not require <code>widget_reference</code>,</li>
  <li>the case does not require property-based UI interaction,</li>
  <li>the case does not require explicit local-memory semantics.</li>
</ul>

<p>The validator should therefore establish valid language-level meaning for a program that contains both:</p>

<pre><code>public contract participation
and
widget-owned value participation
</code></pre>

<p>without merging them.</p>

<hr>

<h2 id="expected-derivation-preservation">7. Expected Derivation Preservation</h2>

<p>Execution IR derivation should preserve explicitly:</p>

<ul>
  <li>public entry participation for input <code>x</code>,</li>
  <li>widget-value participation for widget <code>gain</code>,</li>
  <li>primitive execution identity for <code>frog.core.add</code>,</li>
  <li>public exit participation for output <code>result</code>,</li>
  <li>the validated dependency edges between those elements,</li>
  <li>recoverable attribution showing that the two incoming values come from different source-side ownership categories.</li>
</ul>

<p>The derivation must <strong>not</strong> reinterpret this case as:</p>

<ul>
  <li>two public interface inputs,</li>
  <li>two widget-driven inputs,</li>
  <li>object-style UI interaction through <code>widget_reference</code>,</li>
  <li>property access to widget member <code>value</code>,</li>
  <li>an event-driven program,</li>
  <li>a stateful program.</li>
</ul>

<p>The preserved distinction should remain conceptually equivalent to:</p>

<pre><code>source-side role A: interface_input(x)
source-side role B: widget_value(gain)

A != B
both may feed the same computation
</code></pre>

<hr>

<h2 id="expected-backend-contract-preservation">8. Expected Backend Contract Preservation</h2>

<p>If this case is lowered and emitted as a backend contract, the contract should still make clear that:</p>

<ul>
  <li>one input comes from the public callable program boundary,</li>
  <li>one input comes from widget-owned value participation,</li>
  <li>the computation is ordinary arithmetic addition,</li>
  <li>the result is exposed through a public output boundary,</li>
  <li>no object-style widget reference handling is required,</li>
  <li>no hidden event model is required,</li>
  <li>no explicit local-memory semantics are required.</li>
</ul>

<p>A backend family may specialize how UI value binding is realized, but it must not erase the distinction between:</p>

<pre><code>public interface argument
and
widget-sourced value contribution
</code></pre>

<p>If that distinction disappears, the lowered form is no longer preserving the published architecture.</p>

<hr>

<h2 id="what-must-not-happen">9. What Must Not Happen</h2>

<ul>
  <li>The case must not be rewritten as if the widget declaration automatically created a public interface port.</li>
  <li>The case must not be rewritten as if the public input were just another widget.</li>
  <li>The case must not be normalized into object-style UI interaction through <code>widget_reference</code>.</li>
  <li>The case must not be normalized into property access to widget member <code>value</code>.</li>
  <li>The case must not be rejected merely because public interface participation and widget participation coexist in the same graph.</li>
  <li>The case must not gain implicit state.</li>
  <li>The case must not gain hidden event semantics.</li>
  <li>The implementation must not silently merge distinct source-side ownership categories into one generic endpoint class while still claiming conformance.</li>
</ul>

<hr>

<h2 id="summary">10. Summary</h2>

<p>This is the baseline valid conformance case for coexistence without collapse between:</p>

<ul>
  <li>public interface participation, and</li>
  <li>natural widget-value participation.</li>
</ul>

<p>A conforming toolchain should accept it, validate it as a meaningful program, derive it without losing ownership distinctions, and preserve through backend handoff that:</p>

<pre><code>interface boundary participation
and
widget-owned value participation
</code></pre>

<p>may coexist in one executable graph while remaining semantically distinct.</p>
