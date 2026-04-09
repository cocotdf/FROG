<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — Numeric Widgets</h1>

<p align="center">
  <strong>Normative default realization posture for standardized numeric widgets</strong><br/>
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
This document defines the default official realization posture for the standardized numeric widget family.
</p>

<hr/>

<h2 id="target-classes">2. Target Classes</h2>

<ul>
  <li><code>frog.widgets.numeric_control</code></li>
  <li><code>frog.widgets.numeric_indicator</code></li>
</ul>

<hr/>

<h2 id="realized-parts">3. Realized Parts</h2>

<p>
The default numeric realization targets the following parts:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>value_display</code></li>
  <li><code>increment_button</code> when the control realization exposes it</li>
  <li><code>decrement_button</code> when the control realization exposes it</li>
  <li><code>frame</code></li>
</ul>

<hr/>

<h2 id="standard-visual-states">4. Standard Visual States</h2>

<p>
The default numeric family defines at least:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code></li>
  <li><code>focused</code></li>
</ul>

<p>
For increment and decrement button parts, the default family additionally defines:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>pressed</code></li>
</ul>

<hr/>

<h2 id="part-state-mapping">5. Part-State Mapping</h2>

<p>
The default family expects:
</p>

<ul>
  <li><code>value_display</code> to remain readable across states,</li>
  <li><code>increment_button</code> to support state distinction between <code>normal</code> and <code>pressed</code>,</li>
  <li><code>decrement_button</code> to support state distinction between <code>normal</code> and <code>pressed</code>,</li>
  <li><code>frame</code> to support focused posture where applicable.</li>
</ul>

<hr/>

<h2 id="resource-posture">6. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>numeric_control/
  value_display/
    normal
    disabled
    focused
  increment_button/
    normal
    pressed
  decrement_button/
    normal
    pressed

numeric_indicator/
  value_display/
    normal
    focused
</code></pre>

<hr/>

<h2 id="host-expectations">7. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>a clearly readable numeric display,</li>
  <li>a visible disabled posture when interaction is suppressed,</li>
  <li>a visible focus posture where host focus is supported,</li>
  <li>visible step-button feedback when increment and decrement parts are realized.</li>
</ul>

<hr/>

<h2 id="fallback-posture">8. Fallback Posture</h2>

<p>
If step-button-specific resources are unavailable, a runtime MAY:
</p>

<ul>
  <li>use host-native increment and decrement controls,</li>
  <li>omit visible step buttons while preserving numeric editing capability,</li>
  <li>reuse generic button-state posture for increment and decrement parts.</li>
</ul>

<p>
Any fallback MUST preserve the published numeric class law and the meaning of the public parts when those parts are exposed.
</p>

<hr/>

<h2 id="summary">9. Summary</h2>

<p>
The default numeric realization defines one official embodiment of the numeric widget family, including optional stateful increment and decrement part realization.
</p>
