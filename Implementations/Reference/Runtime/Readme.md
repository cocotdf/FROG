<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 Reference Runtime</h1>

<p align="center">
  First consumer/runtime family for the non-normative FROG reference implementation<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Overview</h2>

<p>
This directory contains the first runtime-side consumer of backend contracts in the reference implementation.
Its role is to accept a contract for the selected backend family and realize execution privately while staying faithful to the declared contract obligations.
</p>

<hr/>

<h2>Non-Normative Status</h2>

<p>
This runtime is not the universal FROG runtime.
It is one reference-family realization used to prove that the published boundaries can support an executable slice.
</p>

<hr/>

<h2>First Runtime Family</h2>

<p>
The recommended first family is:
</p>

<pre><code>reference_host_runtime_ui_binding</code></pre>

<p>
A useful initial shape is:
</p>

<ul>
  <li>single process,</li>
  <li>host runtime,</li>
  <li>deterministic step-oriented execution,</li>
  <li>explicit handling of state and commit points,</li>
  <li>basic UI value and UI reference support where declared by the contract.</li>
</ul>

<hr/>

<h2>What this Directory Owns</h2>

<ul>
  <li>private execution realization of accepted backend contracts,</li>
  <li>state management for the reference family,</li>
  <li>family-specific runtime objects,</li>
  <li>family-specific scheduling mechanics.</li>
</ul>

<hr/>

<h2>What this Directory Does Not Own</h2>

<ul>
  <li>the language,</li>
  <li>the open Execution IR,</li>
  <li>the backend contract boundary,</li>
  <li>the normative meaning of UI constructs.</li>
</ul>

<hr/>

<h2>Design Rules</h2>

<ul>
  <li>Accept or reject contracts explicitly.</li>
  <li>Do not silently reinterpret undeclared assumptions.</li>
  <li>Preserve explicit local-memory meaning where required.</li>
  <li>Preserve source-aligned attribution where the contract claims support for it.</li>
</ul>

<hr/>

<h2>Summary</h2>

<p>
The reference runtime is the first private consumer-side realization of the reference backend family.
It proves executability,
but it does not become the language definition.
</p>
