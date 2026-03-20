<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 Reference Contract Emitter</h1>

<p align="center">
  Backend contract emission stage for the non-normative FROG reference implementation<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Overview</h2>

<p>
This directory contains the stage that emits backend contracts from lowered execution forms.
Its role is to produce a standardized consumer-facing handoff aligned with the published backend-contract boundary.
</p>

<hr/>

<h2>Architectural Position</h2>

<pre><code>lowered form
      |
      v
backend contract emission   &lt;-- this directory
      |
      v
backend contract
      |
      v
consumer-side realization
</code></pre>

<hr/>

<h2>What this Directory Owns</h2>

<ul>
  <li>material emission of backend-contract artifacts for the selected family,</li>
  <li>declaration of family assumptions,</li>
  <li>declaration of consumable execution units,</li>
  <li>declaration of preserved attribution and unsupported features.</li>
</ul>

<hr/>

<h2>What this Directory Does Not Own</h2>

<ul>
  <li>the normative backend-contract rules themselves,</li>
  <li>runtime-private realization,</li>
  <li>deployment packaging,</li>
  <li>debugger protocol definition.</li>
</ul>

<hr/>

<h2>First-Slice Responsibilities</h2>

<p>
For the first slice, the emitter should produce artifacts rich enough to make explicit:
</p>

<ul>
  <li>contract identity,</li>
  <li>backend family orientation,</li>
  <li>declared assumptions,</li>
  <li>consumable executable units,</li>
  <li>state semantics where present,</li>
  <li>UI participation or UI-object interaction support where relevant,</li>
  <li>diagnostic and attribution support.</li>
</ul>

<hr/>

<h2>Design Rules</h2>

<ul>
  <li>Do not hide undeclared assumptions.</li>
  <li>Do not erase state semantics.</li>
  <li>Do not erase UI participation distinctions when the family claims support for them.</li>
  <li>Make rejection conditions explicit.</li>
</ul>

<hr/>

<h2>Summary</h2>

<p>
The contract emitter is the stage that turns lowered implementation-facing forms into declared consumer-facing backend contracts for the reference family.
</p>
