<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Default Realization Family</h1>

<p align="center">
  <strong>Normative default official realization family for the intrinsic standardized widget baseline</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#purpose">2. Purpose</a></li>
  <li><a href="#target-classes">3. Target Classes</a></li>
  <li><a href="#family-goals">4. Family Goals</a></li>
  <li><a href="#shared-state-posture">5. Shared State Posture</a></li>
  <li><a href="#shared-resource-posture">6. Shared Resource Posture</a></li>
  <li><a href="#shared-fallback-posture">7. Shared Fallback Posture</a></li>
  <li><a href="#shared-host-expectations">8. Shared Host Expectations</a></li>
  <li><a href="#documents-in-this-family">9. Documents in this Family</a></li>
  <li><a href="#summary">10. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the default official realization family for the intrinsic standardized widget baseline of FROG.
</p>

<p>
Its role is to provide one coherent, inspectable, portable, standard realization posture for the baseline widget classes already defined in <code>Libraries/Widgets/</code>.
</p>

<hr/>

<h2 id="purpose">2. Purpose</h2>

<p>
The <code>Default</code> family exists to provide:
</p>

<ul>
  <li>a first serious standard visual embodiment of the baseline widget classes,</li>
  <li>a reference family for examples and runtime interpretation,</li>
  <li>a stable place for state-driven skins and part-driven visual mappings,</li>
  <li>a clean separation between class law and realization detail.</li>
</ul>

<hr/>

<h2 id="target-classes">3. Target Classes</h2>

<p>
The default family targets the following intrinsic standardized classes:
</p>

<ul>
  <li><code>frog.widgets.numeric_control</code></li>
  <li><code>frog.widgets.numeric_indicator</code></li>
  <li><code>frog.widgets.boolean_control</code></li>
  <li><code>frog.widgets.boolean_indicator</code></li>
  <li><code>frog.widgets.string_control</code></li>
  <li><code>frog.widgets.string_indicator</code></li>
  <li><code>frog.widgets.button</code></li>
  <li><code>frog.widgets.waveform_chart</code></li>
</ul>

<hr/>

<h2 id="family-goals">4. Family Goals</h2>

<p>
The default family is designed to be:
</p>

<ul>
  <li>clear,</li>
  <li>minimal,</li>
  <li>portable,</li>
  <li>state-structured,</li>
  <li>suitable for SVG-backed or host-native realization,</li>
  <li>usable as the first official embodiment interpreted by runtimes.</li>
</ul>

<p>
It is not intended to define the only future visual family.
It is the first official one.
</p>

<hr/>

<h2 id="shared-state-posture">5. Shared State Posture</h2>

<p>
Across the default realization family, widgets and parts MAY use a shared standard state vocabulary such as:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code></li>
  <li><code>focused</code></li>
  <li><code>pressed</code> where applicable</li>
  <li><code>hovered</code> where supported by the active host posture</li>
</ul>

<p>
Not every widget or part needs every state.
Each family-specific document defines the relevant subset.
</p>

<hr/>

<h2 id="shared-resource-posture">6. Shared Resource Posture</h2>

<p>
The default family assumes that realization resources MAY be organized by:
</p>

<ul>
  <li>widget class,</li>
  <li>widget part,</li>
  <li>interaction state,</li>
  <li>optional size or density variant.</li>
</ul>

<p>
For example:
</p>

<pre><code>button/
  face/
    normal
    pressed
    disabled
    focused

numeric_control/
  increment_button/
    normal
    pressed
  decrement_button/
    normal
    pressed
</code></pre>

<p>
This is a posture definition, not yet a mandatory asset tree.
</p>

<hr/>

<h2 id="shared-fallback-posture">7. Shared Fallback Posture</h2>

<p>
If a specialized state resource is unavailable, a conforming realization MAY fall back to:
</p>

<ul>
  <li>the nearest less-specialized state resource,</li>
  <li>a host-native compatible rendering,</li>
  <li>a generic default visual posture preserving the published part structure.</li>
</ul>

<p>
Fallback is allowed only if public interaction meaning and part meaning remain preserved.
</p>

<hr/>

<h2 id="shared-host-expectations">8. Shared Host Expectations</h2>

<p>
A host interpreting the default family SHOULD preserve at least:
</p>

<ul>
  <li>published widget parts,</li>
  <li>published state transitions,</li>
  <li>visible distinction between enabled and disabled posture,</li>
  <li>visible distinction between normal and pressed posture where applicable,</li>
  <li>reasonable focus indication where supported by the host.</li>
</ul>

<hr/>

<h2 id="documents-in-this-family">9. Documents in this Family</h2>

<ul>
  <li><code>Button.md</code> — default realization posture for the standard button</li>
  <li><code>Numeric.md</code> — default realization posture for standard numeric widgets</li>
  <li><code>Boolean.md</code> — default realization posture for standard boolean widgets</li>
  <li><code>String.md</code> — default realization posture for standard string widgets</li>
  <li><code>Chart.md</code> — default realization posture for the standard waveform chart</li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The <code>Default</code> family is the first official realization family for the intrinsic standardized widget baseline.
</p>

<p>
It defines one coherent state-structured official embodiment that runtimes may interpret faithfully or approximate compatibly while preserving class meaning and part meaning.
</p>
