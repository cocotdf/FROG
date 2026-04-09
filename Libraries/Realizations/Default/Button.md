<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — Button</h1>

<p align="center">
  <strong>Normative default realization posture for <code>frog.widgets.button</code></strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#target-class">2. Target Class</a></li>
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
This document defines the default official realization posture for <code>frog.widgets.button</code>.
</p>

<p>
Its role is to provide a clean, state-structured embodiment of the standard button without making the visual assets the owner of button semantics.
</p>

<hr/>

<h2 id="target-class">2. Target Class</h2>

<ul>
  <li><strong>target class:</strong> <code>frog.widgets.button</code></li>
</ul>

<hr/>

<h2 id="realized-parts">3. Realized Parts</h2>

<p>
The default button realization targets the following public parts:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>face</code></li>
  <li><code>label</code></li>
  <li><code>frame</code> when present</li>
</ul>

<hr/>

<h2 id="standard-visual-states">4. Standard Visual States</h2>

<p>
The default button realization defines the following standard visual states:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code></li>
  <li><code>focused</code></li>
  <li><code>pressed</code></li>
</ul>

<p>
The host MAY also support <code>hovered</code>, but it is not required in the minimal default realization posture.
</p>

<hr/>

<h2 id="part-state-mapping">5. Part-State Mapping</h2>

<p>
The default family expects at least:
</p>

<ul>
  <li><code>face</code> to vary across <code>normal</code>, <code>disabled</code>, <code>focused</code>, and <code>pressed</code>,</li>
  <li><code>label</code> to remain readable in all supported states,</li>
  <li><code>frame</code>, when present, to remain visually consistent with the current state.</li>
</ul>

<hr/>

<h2 id="resource-posture">6. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>button/
  face/
    normal
    disabled
    focused
    pressed
  label/
    normal
    disabled
</code></pre>

<p>
Resources MAY be SVG-backed, host-native, or toolkit-driven.
The default family only standardizes the state and part posture, not the file format itself.
</p>

<hr/>

<h2 id="host-expectations">7. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a clearly actionable face,</li>
  <li>a visible pressed posture during activation,</li>
  <li>a visible disabled posture when interaction is suppressed,</li>
  <li>a visible focus posture where host focus is supported.</li>
</ul>

<hr/>

<h2 id="fallback-posture">8. Fallback Posture</h2>

<p>
If a specialized resource is unavailable:
</p>

<ul>
  <li><code>pressed</code> MAY fall back to a host-native pressed embodiment,</li>
  <li><code>focused</code> MAY fall back to a host-native focus ring or equivalent indicator,</li>
  <li><code>disabled</code> MUST remain visually distinguishable from <code>normal</code>.</li>
</ul>

<hr/>

<h2 id="summary">9. Summary</h2>

<p>
The default button realization defines one official state-structured embodiment of <code>frog.widgets.button</code> with stable parts and stable visual states.
</p>
