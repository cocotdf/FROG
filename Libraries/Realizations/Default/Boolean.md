<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization — Boolean Widgets</h1>

<p align="center">
  <strong>Normative default realization posture for standardized boolean widgets</strong><br/>
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
This document defines the default official realization posture for the standardized boolean widget family.
</p>

<hr/>

<h2 id="target-classes">2. Target Classes</h2>

<ul>
  <li><code>frog.widgets.boolean_control</code></li>
  <li><code>frog.widgets.boolean_indicator</code></li>
</ul>

<hr/>

<h2 id="realized-parts">3. Realized Parts</h2>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>state_face</code></li>
  <li><code>frame</code></li>
</ul>

<hr/>

<h2 id="standard-visual-states">4. Standard Visual States</h2>

<p>
The default boolean family defines at least:
</p>

<ul>
  <li><code>normal_false</code></li>
  <li><code>normal_true</code></li>
  <li><code>disabled_false</code></li>
  <li><code>disabled_true</code></li>
</ul>

<p>
For boolean controls, the family MAY also define:
</p>

<ul>
  <li><code>focused_false</code></li>
  <li><code>focused_true</code></li>
  <li><code>pressed_false</code></li>
  <li><code>pressed_true</code></li>
</ul>

<hr/>

<h2 id="part-state-mapping">5. Part-State Mapping</h2>

<p>
The default family expects:
</p>

<ul>
  <li><code>state_face</code> to distinguish true and false posture clearly,</li>
  <li><code>label</code> to remain readable across states,</li>
  <li><code>frame</code> to support focused posture where applicable.</li>
</ul>

<hr/>

<h2 id="resource-posture">6. Resource Posture</h2>

<p>
A typical resource posture may follow:
</p>

<pre><code>boolean_control/
  state_face/
    normal_false
    normal_true
    disabled_false
    disabled_true
    focused_false
    focused_true
    pressed_false
    pressed_true

boolean_indicator/
  state_face/
    normal_false
    normal_true
    disabled_false
    disabled_true
</code></pre>

<hr/>

<h2 id="host-expectations">7. Host Expectations</h2>

<p>
A host interpreting this realization SHOULD provide:
</p>

<ul>
  <li>clear visible distinction between true and false,</li>
  <li>clear visible distinction between enabled and disabled,</li>
  <li>reasonable focus indication for controls,</li>
  <li>reasonable activation feedback for controls.</li>
</ul>

<hr/>

<h2 id="fallback-posture">8. Fallback Posture</h2>

<p>
If state-specific resources are unavailable, a runtime MAY use host-native boolean widgets or generic state rendering, provided the true/false and enabled/disabled distinctions remain preserved.
</p>

<hr/>

<h2 id="summary">9. Summary</h2>

<p>
The default boolean realization defines one official state-structured embodiment for boolean controls and boolean indicators, centered on the public <code>state_face</code> part.
</p>
