<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Example 05 UI Package</h1>

<p align="center">
  <strong>Published front-panel package and SVG realization assets for the bounded UI accumulator example</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#directory-shape">2. Directory Shape</a></li>
  <li><a href="#role-of-each-file">3. Role of Each File</a></li>
  <li><a href="#package-role">4. Package Role</a></li>
  <li><a href="#asset-role">5. Asset Role</a></li>
  <li><a href="#boundary">6. Boundary</a></li>
  <li><a href="#summary">7. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>
<p>
This directory contains the published UI package artifacts for the
<code>Examples/05_bounded_ui_accumulator/</code> bounded vertical slice.
</p>

<p>
These files make the front-panel package layer visible separately from:
</p>

<ul>
  <li>canonical program source in <code>.frog</code>,</li>
  <li>execution-facing FIR and lowering artifacts,</li>
  <li>downstream backend-family contract emission,</li>
  <li>runtime-family and host-specific realization consumption.</li>
</ul>

<p>
The important architectural rule is that this directory participates in the example publication corridor, but it does not redefine executable semantics.
</p>

<h2 id="directory-shape">2. Directory Shape</h2>
<pre><code>Examples/05_bounded_ui_accumulator/ui/
├── Readme.md
├── accumulator_panel.wfrog
└── assets/
    ├── numeric_control.svg
    └── numeric_indicator.svg
</code></pre>

<h2 id="role-of-each-file">3. Role of Each File</h2>
<ul>
  <li><code>accumulator_panel.wfrog</code><br/>
      Published front-panel package for the bounded example.</li>

  <li><code>assets/numeric_control.svg</code><br/>
      SVG realization asset used for the numeric control publication path.</li>

  <li><code>assets/numeric_indicator.svg</code><br/>
      SVG realization asset used for the numeric indicator publication path.</li>
</ul>

<h2 id="package-role">4. Package Role</h2>
<p>
The <code>.wfrog</code> file in this directory is the example-local published front-panel package artifact.
It gives the bounded slice a repository-visible widget realization layer that remains separate from the canonical <code>.frog</code> program source.
</p>

<p>
Its purpose is to support a repository-visible corridor such as:
</p>

<pre><code>canonical source
  -&gt; front-panel package
  -&gt; FIR
  -&gt; lowering
  -&gt; backend-family contract
  -&gt; runtime-family and host consumption
</code></pre>

<p>
This package layer therefore helps demonstrate how widget-oriented publication can remain peripheral to source-owned program meaning.
</p>

<h2 id="asset-role">5. Asset Role</h2>
<p>
The SVG files in <code>assets/</code> are minimal realization assets for the two widgets used by Example 05:
</p>

<ul>
  <li>one numeric control,</li>
  <li>one numeric indicator.</li>
</ul>

<p>
These assets support the example-local realization corridor, but they do not define widget semantics.
Widget class meaning remains governed by canonical source, published widget contracts, and downstream execution-facing artifacts.
</p>

<h2 id="boundary">6. Boundary</h2>
<p>
This directory does not define FROG itself.
It does not define the language.
It does not define FIR.
It does not define lowering.
It does not own backend-family runtime contracts.
</p>

<pre><code>published UI package
    !=
semantic authority
</code></pre>

<pre><code>SVG realization asset
    !=
widget class definition
</code></pre>

<p>
The correct reading posture is:
</p>

<ul>
  <li><code>main.frog</code> owns example-local executable meaning,</li>
  <li><code>accumulator_panel.wfrog</code> owns example-local package publication,</li>
  <li>the SVG files support realization,</li>
  <li>downstream hosts and runtimes may consume these artifacts privately without acquiring semantic authority.</li>
</ul>

<h2 id="summary">7. Summary</h2>
<p>
This directory contains the published front-panel package and the minimal SVG realization assets for Example 05.
It exists to make the widget-oriented package layer visible in the repository while preserving strict separation from canonical source-owned program meaning.
</p>
