<p align="center">
  <img src="../../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization Asset Naming</h1>

<p align="center">
  <strong>Normative naming posture for assets of the official <code>Default</code> widget realization family</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#naming-goals">2. Naming Goals</a></li>
  <li><a href="#directory-naming">3. Directory Naming</a></li>
  <li><a href="#part-directory-naming">4. Part Directory Naming</a></li>
  <li><a href="#state-file-naming">5. State File Naming</a></li>
  <li><a href="#compound-state-naming">6. Compound State Naming</a></li>
  <li><a href="#auxiliary-file-naming">7. Auxiliary File Naming</a></li>
  <li><a href="#prohibited-drift">8. Prohibited Drift</a></li>
  <li><a href="#examples">9. Examples</a></li>
  <li><a href="#summary">10. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the naming posture for assets in the official <code>Default</code> realization family.
</p>

<p>
Its purpose is to ensure that paths, filenames, part names, and state names remain stable and predictable across:
</p>

<ul>
  <li>documentation,</li>
  <li>machine-readable realization packages,</li>
  <li>runtime loaders,</li>
  <li>future asset generation workflows.</li>
</ul>

<hr/>

<h2 id="naming-goals">2. Naming Goals</h2>

<p>
The naming posture is designed to be:
</p>

<ul>
  <li>simple,</li>
  <li>stable,</li>
  <li>machine-friendly,</li>
  <li>human-readable,</li>
  <li>aligned with published class and part names.</li>
</ul>

<hr/>

<h2 id="directory-naming">3. Directory Naming</h2>

<p>
Widget-class directories SHOULD use the terminal class identifier in lowercase snake_case.
</p>

<p>
Examples:
</p>

<ul>
  <li><code>button</code></li>
  <li><code>numeric_control</code></li>
  <li><code>numeric_indicator</code></li>
  <li><code>boolean_control</code></li>
  <li><code>boolean_indicator</code></li>
  <li><code>string_control</code></li>
  <li><code>string_indicator</code></li>
  <li><code>waveform_chart</code></li>
</ul>

<hr/>

<h2 id="part-directory-naming">4. Part Directory Naming</h2>

<p>
Part directories MUST use the published public part identifier exactly, in lowercase snake_case when that is the part identifier.
</p>

<p>
Examples:
</p>

<ul>
  <li><code>face</code></li>
  <li><code>label</code></li>
  <li><code>value_display</code></li>
  <li><code>increment_button</code></li>
  <li><code>decrement_button</code></li>
  <li><code>state_face</code></li>
  <li><code>text_display</code></li>
  <li><code>plot_area</code></li>
</ul>

<p>
The asset tree MUST NOT silently rename parts away from the published part model.
</p>

<hr/>

<h2 id="state-file-naming">5. State File Naming</h2>

<p>
A state-specific primary SVG asset SHOULD use:
</p>

<pre><code>&lt;state&gt;.svg</code></pre>

<p>
Examples:
</p>

<ul>
  <li><code>normal.svg</code></li>
  <li><code>disabled.svg</code></li>
  <li><code>focused.svg</code></li>
  <li><code>pressed.svg</code></li>
</ul>

<p>
The state name MUST match a published realization state.
</p>

<hr/>

<h2 id="compound-state-naming">6. Compound State Naming</h2>

<p>
When the state expresses more than one realization dimension, the filename MAY use a compound state name:
</p>

<pre><code>&lt;state_a&gt;_&lt;state_b&gt;.svg</code></pre>

<p>
Examples:
</p>

<ul>
  <li><code>normal_true.svg</code></li>
  <li><code>normal_false.svg</code></li>
  <li><code>disabled_true.svg</code></li>
  <li><code>disabled_false.svg</code></li>
</ul>

<p>
Compound state names SHOULD remain explicit and finite.
They SHOULD NOT become a hidden multi-axis combinatorial system without published realization support.
</p>

<hr/>

<h2 id="auxiliary-file-naming">7. Auxiliary File Naming</h2>

<p>
Recommended auxiliary support filenames are:
</p>

<ul>
  <li><code>anchor_map.json</code></li>
  <li><code>layer_map.json</code></li>
  <li><code>style_token_map.json</code></li>
</ul>

<p>
These filenames SHOULD be used consistently when such support files exist.
</p>

<hr/>

<h2 id="prohibited-drift">8. Prohibited Drift</h2>

<p>
The following drift patterns SHOULD be avoided:
</p>

<ul>
  <li>renaming published parts only in the asset tree,</li>
  <li>using host-toolkit terminology instead of published part terminology,</li>
  <li>encoding unpublished semantic meaning into filenames,</li>
  <li>using multiple competing spellings for the same state,</li>
  <li>using mixed casing without an explicit convention.</li>
</ul>

<hr/>

<h2 id="examples">9. Examples</h2>

<p>
Valid examples:
</p>

<ul>
  <li><code>assets/button/face/pressed.svg</code></li>
  <li><code>assets/numeric_control/increment_button/pressed.svg</code></li>
  <li><code>assets/boolean_control/state_face/disabled_true.svg</code></li>
  <li><code>assets/string_control/text_display/focused.svg</code></li>
  <li><code>assets/button/face/anchor_map.json</code></li>
</ul>

<p>
Invalid drift examples:
</p>

<ul>
  <li><code>assets/button/mainSurface/down.svg</code></li>
  <li><code>assets/numeric_control/upArrow/pushed.svg</code></li>
  <li><code>assets/boolean_control/stateFace/onDisabled.svg</code></li>
</ul>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
The default-family naming posture is simple:
</p>

<ul>
  <li>widget directory = terminal class identifier,</li>
  <li>part directory = published part identifier,</li>
  <li>state file = published realization state,</li>
  <li>auxiliary files = normalized support names.</li>
</ul>

<p>
This keeps the asset layer aligned with the published realization and class layers above it.
</p>
