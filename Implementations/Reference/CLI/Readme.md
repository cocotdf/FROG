<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 Reference CLI</h1>

<p align="center">
  Command-line entry points for the non-normative FROG reference implementation<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Overview</h2>

<p>
This directory contains the command-line surface of the reference implementation.
Its role is to expose a small, explicit, stage-aware toolchain for the first executable vertical slice of FROG.
</p>

<p>
The CLI is <strong>not</strong> a language specification layer.
It is a practical consumer-facing shell around the reference pipeline.
</p>

<hr/>

<h2>Why this Directory Exists</h2>

<p>
A reference implementation becomes much easier to test and reason about when each major stage can be invoked explicitly.
The CLI therefore exists to provide stable entry points such as:
</p>

<ul>
  <li><code>validate</code></li>
  <li><code>derive-ir</code></li>
  <li><code>lower</code></li>
  <li><code>emit-contract</code></li>
  <li><code>run</code></li>
</ul>

<p>
These commands are intended to mirror the published architectural boundaries rather than skipping over them.
</p>

<hr/>

<h2>Non-Normative Status</h2>

<p>
This directory is non-normative.
It does not define the language,
the canonical source format,
the validated program meaning,
or the open Execution IR.
Those remain owned by the published specification.
</p>

<hr/>

<h2>Initial Command Intent</h2>

<pre><code>frogc validate &lt;file.frog&gt;
frogc derive-ir &lt;file.frog&gt;
frogc lower &lt;file.frog&gt;
frogc emit-contract &lt;file.frog&gt;
frogc run &lt;file.frog&gt;
</code></pre>

<p>
The exact command surface may evolve,
but the stage separation should remain explicit.
</p>

<hr/>

<h2>Design Rules</h2>

<ul>
  <li>Commands should reflect published architectural boundaries.</li>
  <li>Commands should fail explicitly rather than silently skipping invalid stages.</li>
  <li>Commands should remain implementation-oriented, not normative.</li>
  <li>Human-readable diagnostics should remain source-aligned where possible.</li>
</ul>

<hr/>

<h2>Summary</h2>

<p>
The CLI is the operational shell of the reference implementation.
It exists to expose the first FROG reference pipeline clearly and explicitly,
without collapsing the repository's published architecture into one opaque tool command.
</p>
