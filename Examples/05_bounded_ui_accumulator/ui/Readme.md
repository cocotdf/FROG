<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Example 05 UI Package</h1>

<p align="center">
  <strong>Widget-oriented front-panel package assets for the bounded UI accumulator example</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Overview</h2>

<p>
This directory contains proposed widget-oriented UI package artifacts for the
<code>Examples/05_bounded_ui_accumulator/</code> vertical slice.
</p>

<p>
These files illustrate the intended separation between:
</p>

<ul>
  <li>canonical program source in <code>.frog</code>,</li>
  <li>front-panel package content in <code>.wfrog</code>,</li>
  <li>visual assets in SVG,</li>
  <li>runtime interpretation and host realization.</li>
</ul>

<h2>Files</h2>

<ul>
  <li><code>accumulator_panel.wfrog</code> — proposed front-panel package for the example.</li>
  <li><code>assets/numeric_indicator.svg</code> — proposed visual asset for the numeric indicator.</li>
</ul>

<h2>Purpose</h2>

<p>
This directory is not the definition of FROG itself.
It is a repository-visible example package surface that helps demonstrate how a runtime
could consume widget-oriented artifacts separately from the canonical <code>.frog</code> program source.
</p>
