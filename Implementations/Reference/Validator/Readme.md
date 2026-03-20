<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 Reference Validator</h1>

<p align="center">
  MVP validation stage for the non-normative FROG reference implementation<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Overview</h2>

<p>
This directory contains validation logic for the first reference implementation slice.
Its role is to check whether loaded canonical source satisfies the published rules needed to establish valid program meaning for the selected MVP subset.
</p>

<hr/>

<h2>Scope of the First Slice</h2>

<p>
The first reference validator should concentrate on the MVP subset exercised by the initial example and conformance cases, including:
</p>

<ul>
  <li>public interface participation,</li>
  <li>ordinary core primitives,</li>
  <li><code>widget_value</code>,</li>
  <li><code>widget_reference</code>,</li>
  <li>standardized UI primitives,</li>
  <li>explicit local memory through <code>frog.core.delay</code>,</li>
  <li>basic cycle legality.</li>
</ul>

<hr/>

<h2>What this Directory Owns</h2>

<ul>
  <li>implementation-side checking of published validation rules for the chosen slice,</li>
  <li>explicit acceptance or rejection of source cases,</li>
  <li>source-aligned validation diagnostics.</li>
</ul>

<hr/>

<h2>What this Directory Does Not Own</h2>

<ul>
  <li>the normative validation rules themselves,</li>
  <li>language semantics ownership,</li>
  <li>primitive-catalog ownership,</li>
  <li>Execution IR design ownership.</li>
</ul>

<p>
If the validator exposes a missing or ambiguous rule,
the fix belongs in the specification owner,
not in hidden validator folklore.
</p>

<hr/>

<h2>Design Rules</h2>

<ul>
  <li>Reject invalid source explicitly.</li>
  <li>Do not silently reinterpret invalid source.</li>
  <li>Preserve enough source identity for later attribution.</li>
  <li>Keep the first slice narrow and coherent.</li>
</ul>

<hr/>

<h2>Summary</h2>

<p>
The validator is the stage that decides whether a source case is a legitimate candidate for Execution IR derivation.
Without successful validation,
the reference implementation must not claim a conforming derived execution form.
</p>
