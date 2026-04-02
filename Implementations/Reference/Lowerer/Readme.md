<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">🐸 Reference Lowerer</h1>

<p align="center">
  Controlled specialization stage for the non-normative FROG reference implementation<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Overview</h2>

<p>
This directory contains the first lowering stage of the reference implementation.
Its role is to specialize open Execution IR toward one selected backend family without claiming that this specialization is the language itself.
</p>

<hr/>

<h2>Architectural Position</h2>

<pre><code>open Execution IR
      |
      v
lowering   &lt;-- this directory
      |
      v
backend-facing consumable form
</code></pre>

<hr/>

<h2>What this Directory Owns</h2>

<ul>
  <li>family-oriented specialization of the open IR,</li>
  <li>making backend-relevant assumptions explicit,</li>
  <li>preparing the form that will later be described through the backend contract.</li>
</ul>

<hr/>

<h2>What this Directory Does Not Own</h2>

<ul>
  <li>the open IR architecture,</li>
  <li>the backend contract itself,</li>
  <li>runtime-private realization,</li>
  <li>vendor-specific deployment packaging.</li>
</ul>

<hr/>

<h2>First Target Family</h2>

<p>
The first reference lowering target should remain deliberately small,
for example:
</p>

<pre><code>reference_host_runtime_ui_binding
</code></pre>

<p>
This allows the reference implementation to exercise:
</p>

<ul>
  <li>ordinary primitive execution,</li>
  <li>public boundaries,</li>
  <li>explicit memory,</li>
  <li>natural UI value participation,</li>
  <li>object-style widget interaction.</li>
</ul>

<hr/>

<h2>Design Rules</h2>

<ul>
  <li>Lowering may specialize, but must not drift semantically.</li>
  <li>Lowering may make scheduling or placement more explicit, but must not pretend that one runtime-private architecture is normative FROG truth.</li>
  <li>Lowering must preserve enough attribution for backend-contract emission and later diagnostics.</li>
</ul>

<hr/>

<h2>Summary</h2>

<p>
The lowerer specializes open Execution IR toward the first reference backend family.
It is downstream from the open IR boundary and upstream from the standardized backend handoff.
</p>
