<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">🐸 frogc Command Sketch</h1>

<p align="center">
  Initial command sketch for the FROG reference implementation CLI<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Overview</h2>

<p>
This file records the first intended command surface for the reference implementation CLI.
It is an implementation sketch,
not a normative language document.
</p>

<hr/>

<h2>Initial Commands</h2>

<pre><code>frogc validate &lt;file.frog&gt;
frogc derive-ir &lt;file.frog&gt;
frogc lower &lt;file.frog&gt;
frogc emit-contract &lt;file.frog&gt;
frogc run &lt;file.frog&gt;
</code></pre>

<hr/>

<h2>Intent</h2>

<ul>
  <li><code>validate</code> checks whether canonical source satisfies the selected published rules.</li>
  <li><code>derive-ir</code> emits an open execution-facing derived form.</li>
  <li><code>lower</code> specializes that form for the selected backend family.</li>
  <li><code>emit-contract</code> emits a backend contract artifact for that family.</li>
  <li><code>run</code> executes the program through the first reference runtime family.</li>
</ul>

<hr/>

<h2>Summary</h2>

<p>
The CLI sketch is intentionally small.
Its purpose is to mirror the published architecture rather than bypass it.
</p>
