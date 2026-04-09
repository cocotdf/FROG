<p align="center">
  <img src="../../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization Assets</h1>

<p align="center">
  <strong>Normative asset-tree posture for the official <code>Default</code> widget realization family</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-directory-exists">2. Why this Directory Exists</a></li>
  <li><a href="#scope">3. Scope</a></li>
  <li><a href="#asset-tree-principles">4. Asset Tree Principles</a></li>
  <li><a href="#top-level-organization">5. Top-Level Organization</a></li>
  <li><a href="#widget-level-vs-part-level-assets">6. Widget-Level vs Part-Level Assets</a></li>
  <li><a href="#state-organization">7. State Organization</a></li>
  <li><a href="#supported-asset-kinds">8. Supported Asset Kinds</a></li>
  <li><a href="#recommended-tree-shape">9. Recommended Tree Shape</a></li>
  <li><a href="#examples">10. Examples</a></li>
  <li><a href="#fallback-posture">11. Fallback Posture</a></li>
  <li><a href="#validation-posture">12. Validation Posture</a></li>
  <li><a href="#summary">13. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the normative asset-tree posture for the official <code>Default</code> realization family.
</p>

<p>
Its purpose is to keep realization resources organized, explicit, and machine-readable-friendly without forcing the asset layer to become the owner of widget semantics.
</p>

<p>
The asset tree is the correct place for:
</p>

<ul>
  <li>state-specific SVG resources,</li>
  <li>part-specific SVG resources,</li>
  <li>optional anchor maps,</li>
  <li>optional layer maps,</li>
  <li>optional style-token maps.</li>
</ul>

<hr/>

<h2 id="why-this-directory-exists">2. Why this Directory Exists</h2>

<p>
Once the default realization family is published and machine-readable realization packages exist, the next source of drift is almost always the asset tree itself.
</p>

<p>
Without a normalized asset tree:
</p>

<ul>
  <li>different realizations use incompatible folder shapes,</li>
  <li>part names drift from class-law names,</li>
  <li>state resources become ambiguous,</li>
  <li>runtime loaders end up depending on private filename guesses,</li>
  <li>machine-readable publication becomes harder to validate.</li>
</ul>

<p>
This document prevents that drift by defining one official organization posture.
</p>

<hr/>

<h2 id="scope">3. Scope</h2>

<p>
This document defines:
</p>

<ul>
  <li>the official asset-tree organization of the <code>Default</code> realization family,</li>
  <li>how widget-class assets are grouped,</li>
  <li>how part-specific assets are grouped,</li>
  <li>how state-specific assets are grouped,</li>
  <li>which auxiliary asset-support files may appear.</li>
</ul>

<p>
This document does not define:
</p>

<ul>
  <li>widget class law,</li>
  <li>generic realization doctrine,</li>
  <li>machine-readable package structure in full,</li>
  <li>the content of any specific SVG file,</li>
  <li>one mandatory runtime asset-loading algorithm.</li>
</ul>

<hr/>

<h2 id="asset-tree-principles">4. Asset Tree Principles</h2>

<p>
The asset tree for the default family follows the following principles:
</p>

<ul>
  <li><strong>Class-first organization</strong> — assets are grouped first by target widget class.</li>
  <li><strong>Part-explicit organization</strong> — assets for public parts are grouped under their published part names.</li>
  <li><strong>State-explicit organization</strong> — state-specific assets are grouped under explicit state names.</li>
  <li><strong>No semantic guessing</strong> — runtime loaders SHOULD NOT need to infer widget law from the asset tree.</li>
  <li><strong>Machine-readable friendliness</strong> — paths should align naturally with realization package resource records.</li>
</ul>

<hr/>

<h2 id="top-level-organization">5. Top-Level Organization</h2>

<p>
The default family asset tree SHOULD be organized first by standardized widget class family.
</p>

<p>
Recommended top-level shape:
</p>

<pre><code>assets/
  button/
  numeric_control/
  numeric_indicator/
  boolean_control/
  boolean_indicator/
  string_control/
  string_indicator/
  waveform_chart/
</code></pre>

<p>
The folder names SHOULD correspond to the terminal class identifier rather than the fully qualified class name.
</p>

<hr/>

<h2 id="widget-level-vs-part-level-assets">6. Widget-Level vs Part-Level Assets</h2>

<p>
The default family distinguishes two main asset scopes:
</p>

<ul>
  <li><strong>widget-level assets</strong> — assets for whole-widget visual posture,</li>
  <li><strong>part-level assets</strong> — assets for one published public part.</li>
</ul>

<p>
The default family prefers part-level organization whenever a public part is explicitly realized.
</p>

<p>
Recommended posture:
</p>

<pre><code>assets/
  button/
    face/
    label/
    frame/
</code></pre>

<p>
Widget-level assets MAY still exist when:
</p>

<ul>
  <li>the realization changes as one indivisible surface,</li>
  <li>the target class has a very small public part model,</li>
  <li>a fallback whole-widget embodiment is needed.</li>
</ul>

<hr/>

<h2 id="state-organization">7. State Organization</h2>

<p>
Within a part directory, resources SHOULD be grouped by explicit state.
</p>

<p>
Recommended posture:
</p>

<pre><code>assets/
  button/
    face/
      normal.svg
      disabled.svg
      focused.svg
      pressed.svg
</code></pre>

<p>
For families that encode value posture in the state itself, the state name MAY be compound:
</p>

<pre><code>assets/
  boolean_control/
    state_face/
      normal_false.svg
      normal_true.svg
      disabled_false.svg
      disabled_true.svg
</code></pre>

<hr/>

<h2 id="supported-asset-kinds">8. Supported Asset Kinds</h2>

<p>
The default family asset tree MAY contain the following file kinds:
</p>

<ul>
  <li><code>.svg</code> — primary scalable visual resources</li>
  <li><code>.json</code> — auxiliary maps such as anchors, layers, or style tokens</li>
</ul>

<p>
Recommended auxiliary support files include:
</p>

<ul>
  <li><code>anchor_map.json</code></li>
  <li><code>layer_map.json</code></li>
  <li><code>style_token_map.json</code></li>
</ul>

<p>
These files remain realization support artifacts.
They do not become semantic truth.
</p>

<hr/>

<h2 id="recommended-tree-shape">9. Recommended Tree Shape</h2>

<p>
The recommended official asset-tree shape is:
</p>

<pre><code>assets/
  button/
    face/
      normal.svg
      disabled.svg
      focused.svg
      pressed.svg
      anchor_map.json
      layer_map.json
    label/
      normal.svg
      disabled.svg

  numeric_control/
    value_display/
      normal.svg
      disabled.svg
      focused.svg
    increment_button/
      normal.svg
      pressed.svg
    decrement_button/
      normal.svg
      pressed.svg
    frame/
      normal.svg
      focused.svg

  boolean_control/
    state_face/
      normal_false.svg
      normal_true.svg
      disabled_false.svg
      disabled_true.svg

  string_control/
    text_display/
      normal.svg
      disabled.svg
      focused.svg

  waveform_chart/
    plot_area/
      normal.svg
      focused.svg
    x_axis/
      normal.svg
    y_axis/
      normal.svg
    frame/
      normal.svg
      focused.svg
</code></pre>

<hr/>

<h2 id="examples">10. Examples</h2>

<p>
Example resource paths:
</p>

<ul>
  <li><code>./assets/button/face/pressed.svg</code></li>
  <li><code>./assets/numeric_control/increment_button/pressed.svg</code></li>
  <li><code>./assets/boolean_control/state_face/normal_true.svg</code></li>
  <li><code>./assets/string_control/text_display/focused.svg</code></li>
  <li><code>./assets/waveform_chart/plot_area/normal.svg</code></li>
</ul>

<hr/>

<h2 id="fallback-posture">11. Fallback Posture</h2>

<p>
When a state-specific resource is missing, runtimes MAY apply published fallback rules.
</p>

<p>
However, the asset tree itself SHOULD remain complete enough that default-family realizations do not rely primarily on hidden fallback heuristics.
</p>

<hr/>

<h2 id="validation-posture">12. Validation Posture</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>asset paths that do not match declared realization resources,</li>
  <li>directories named with non-published part identifiers,</li>
  <li>state resource filenames that do not correspond to declared realization states,</li>
  <li>auxiliary map files attached to unknown parts.</li>
</ul>

<hr/>

<h2 id="summary">13. Summary</h2>

<p>
The default-family asset tree is organized by:
</p>

<ul>
  <li>widget class,</li>
  <li>then public part,</li>
  <li>then explicit state.</li>
</ul>

<p>
This keeps resources inspectable, stable, and aligned with machine-readable realization publication.
</p>
