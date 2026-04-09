<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — String Widgets</h1>

<p align="center">
  <strong>Normative default realization posture for standardized string widgets</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#target-classes">2. Target Classes</a></li>
  <li><a href="#realized-parts">3. Realized Parts</a></li>
  <li><a href="#standard-visual-states">4. Standard Visual States</a></li>
  <li><a href="#part-state-mapping">5. Part-State Mapping</a></li>
  <li><a href="#resource-posture">6. Resource Posture</a></li>
  <li><a href="#host-expectations">7. Host Expectations</a></li>
  <li><a href="#fallback-posture">8. Fallback Posture</a></li>
  <li><a href="#summary">9. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the default official realization posture for the standardized string widget family.
</p>

<hr/>

<h2 id="target-classes">2. Target Classes</h2>

<ul>
  <li><code>frog.widgets.string_control</code></li>
  <li><code>frog.widgets.string_indicator</code></li>
</ul>

<hr/>

<h2 id="realized-parts">3. Realized Parts</h2>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>text_display</code></li>
  <li><code>frame</code></li>
</ul>

<hr/>

<h2 id="standard-visual-states">4. Standard Visual States</h2>

<p>
The default string family defines at least:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code></li>
  <li><code>focused</code></li>
</ul>

<hr/>

<h2 id="part-state-mapping">5. Part-State Mapping</h2>

<p>
The default family expects:
</p>

<ul>
  <li><code>text_display</code> to remain readable in all supported states,</li>
  <li><code>frame</code> to support a focused posture where applicable,</li>
  <li><code>label</code> to remain visually consistent with the widget state.</li>
</ul>

<hr/>

<h2 id="resource-posture">6. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>string_control/
  text_display/
    normal
    disabled
    focused

string_indicator/
  text_display/
    normal
    focused
</code></pre>

<hr/>

<h2 id="host-expectations">7. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a clearly readable text value surface,</li>
  <li>a visible disabled posture when interaction is suppressed,</li>
  <li>a visible focus posture for controls where supported by the host.</li>
</ul>

<hr/>

<h2 id="fallback-posture">8. Fallback Posture</h2>

<p>
If specialized text-display resources are unavailable, a runtime MAY use host-native text entry or text display surfaces provided the published part structure and interaction meaning remain preserved.
</p>

<hr/>

<h2 id="summary">9. Summary</h2>

<p>
The default string realization defines one official embodiment for string controls and string indicators centered on the public <code>text_display</code> part.
</p>
