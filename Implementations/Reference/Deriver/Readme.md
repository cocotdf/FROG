<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">🐸 Reference Deriver</h1>

<p align="center">
  Execution IR derivation stage for the non-normative FROG reference implementation<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Overview</h2>

<p>
This directory contains the reference implementation stage that derives open Execution IR from validated program meaning.
Its role is to consume validated source-side truth and emit an execution-facing representation aligned with the published IR derivation boundary.
</p>

<hr/>

<h2>Architectural Position</h2>

<pre><code>canonical source
      |
      v
validated program meaning
      |
      v
Execution IR derivation   &lt;-- this directory
      |
      v
open Execution IR
</code></pre>

<p>
This stage begins only after validation has succeeded.
</p>

<hr/>

<h2>What this Directory Owns</h2>

<ul>
  <li>implementation-side derivation of Execution IR objects,</li>
  <li>preservation of source attribution and recoverability required by the published IR boundary,</li>
  <li>introduction of support objects where derivation is allowed to make already-validated execution structure explicit.</li>
</ul>

<hr/>

<h2>What this Directory Does Not Own</h2>

<ul>
  <li>the normative definition of Execution IR,</li>
  <li>the derivation rules themselves,</li>
  <li>lowering,</li>
  <li>backend contract emission,</li>
  <li>runtime-private realization.</li>
</ul>

<hr/>

<h2>First-Slice Focus</h2>

<p>
The first reference deriver should cover:
</p>

<ul>
  <li><code>primitive</code>,</li>
  <li><code>subfrog</code> where needed later,</li>
  <li><code>interface_input</code>,</li>
  <li><code>interface_output</code>,</li>
  <li><code>widget_value</code>,</li>
  <li><code>widget_reference</code>,</li>
  <li>explicit local memory through <code>frog.core.delay</code>,</li>
  <li>basic edge and connectivity derivation.</li>
</ul>

<hr/>

<h2>Design Rules</h2>

<ul>
  <li>Preserve validated meaning.</li>
  <li>Preserve attribution.</li>
  <li>Preserve explicit memory as explicit memory.</li>
  <li>Preserve the distinction between public interface, widget-value participation, widget-reference participation, and standardized UI-object primitives.</li>
  <li>Do not smuggle runtime-private assumptions into the open IR.</li>
</ul>

<hr/>

<h2>Summary</h2>

<p>
The deriver is the stage that turns validated meaning into open Execution IR.
It is the first execution-facing stage of the reference implementation,
but it remains upstream from lowering,
backend handoff,
and runtime realization.
</p>
