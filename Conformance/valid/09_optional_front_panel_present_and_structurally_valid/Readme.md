<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Valid Case — Optional Front Panel Present and Structurally Valid</h1>

<p align="center">
  <strong>Structurally valid canonical source with a present <code>front_panel</code> section that remains within source ownership boundaries</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#case-purpose">2. Case Purpose</a></li>
  <li><a href="#case-classification">3. Case Classification</a></li>
  <li><a href="#normative-basis">4. Normative Basis</a></li>
  <li><a href="#input-shape">5. Input Shape</a></li>
  <li><a href="#expected-outcome">6. Expected Outcome</a></li>
  <li><a href="#why-this-case-must-pass">7. Why this Case Must Pass</a></li>
  <li><a href="#what-this-case-is-not-testing">8. What this Case Is Not Testing</a></li>
  <li><a href="#preservation-and-boundary-notes">9. Preservation and Boundary Notes</a></li>
  <li><a href="#implementation-requirements">10. Implementation Requirements</a></li>
  <li><a href="#summary">11. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This case defines a structurally valid canonical <code>.frog</code> source file in which the optional <code>front_panel</code> section is present and structurally well-formed.
</p>

<p>
The case exists to show the positive structural rule for front-panel presence:
a <code>front_panel</code> is valid when it remains a source-level UI composition surface and does not attempt to replace the executable authority of the <code>diagram</code>.
</p>

<hr/>

<h2 id="case-purpose">2. Case Purpose</h2>

<p>
This case exists to verify that a conforming implementation accepts a source file where:
</p>

<ul>
  <li><code>front_panel</code> is present,</li>
  <li>its top-level shape is structurally valid,</li>
  <li>its widget-side content remains inside the front-panel source family,</li>
  <li>it does not encode executable graph ownership that belongs to <code>diagram</code>.</li>
</ul>

<p>
It makes the following truth explicit:
</p>

<pre><code>front_panel present
+
front_panel structurally valid
      -&gt;
canonical source valid
</code></pre>

<hr/>

<h2 id="case-classification">3. Case Classification</h2>

<ul>
  <li><strong>Case family:</strong> valid</li>
  <li><strong>Primary owner:</strong> <code>Expression/</code></li>
  <li><strong>Case kind:</strong> canonical source acceptance with present structurally valid <code>front_panel</code></li>
  <li><strong>Expected loadability:</strong> loadable</li>
  <li><strong>Expected structural validity:</strong> valid</li>
  <li><strong>Expected meaning:</strong> established</li>
  <li><strong>Expected IR derivation:</strong> permitted to proceed according to the published downstream rules</li>
</ul>

<hr/>

<h2 id="normative-basis">4. Normative Basis</h2>

<p>
This case is grounded in the published canonical-source rules of <code>Expression/</code>.
</p>

<p>
For FROG v0.1:
</p>

<ul>
  <li><code>front_panel</code> is optional,</li>
  <li>when present, it defines the user-facing interaction layer through widget instances, layout, style, and related UI composition data,</li>
  <li><code>front_panel</code> does not define the public API,</li>
  <li><code>front_panel</code> does not replace the executable graph,</li>
  <li>any executable relationship involving front-panel behavior must still pass through <code>diagram</code>.</li>
</ul>

<p>
Therefore, a front panel is structurally valid when it remains within those source ownership boundaries.
</p>

<pre><code>front_panel
    -> optional UI composition source

diagram
    -> authoritative executable source

front_panel present and well-formed
    -> canonical source valid
</code></pre>

<hr/>

<h2 id="input-shape">5. Input Shape</h2>

<p>
The associated valid source artifact for this case SHOULD be a JSON-loadable <code>.frog</code> file with:
</p>

<ul>
  <li>a valid top-level object root,</li>
  <li>all required sections present,</li>
  <li>a present <code>front_panel</code> section,</li>
  <li>a structurally valid front-panel widget collection,</li>
  <li>no executable edge ownership misplaced into <code>front_panel</code>,</li>
  <li>a valid minimal <code>diagram</code>.</li>
</ul>

<p>
A representative valid shape is:
</p>

<pre><code>{
  "spec_version": "0.1",
  "metadata": {},
  "interface": {
    "inputs": [],
    "outputs": []
  },
  "diagram": {
    "nodes": [],
    "edges": []
  },
  "front_panel": {
    "widgets": [
      {
        "id": "widget_1",
        "class": "frog.ui.numeric_control"
      }
    ]
  }
}</code></pre>

<p>
In this shape, the front panel stays in its source role as UI composition.
It does not attempt to own executable graph content.
</p>

<hr/>

<h2 id="expected-outcome">6. Expected Outcome</h2>

<p>
The expected outcome is:
</p>

<pre><code>Expected loadability: loadable
Expected structural validity: valid
Expected meaning: established
Expected preservation: front_panel remains distinct from diagram and interface ownership
</code></pre>

<p>
A conforming implementation MUST accept the case as canonical source.
It MUST preserve the distinction between:
</p>

<ul>
  <li><code>front_panel</code> as optional UI composition source,</li>
  <li><code>diagram</code> as authoritative executable source,</li>
  <li><code>interface</code> as public logical boundary.</li>
</ul>

<hr/>

<h2 id="why-this-case-must-pass">7. Why this Case Must Pass</h2>

<p>
The published source model does not forbid front-panel presence.
It defines how front-panel presence remains valid.
</p>

<p>
This case must therefore pass because:
</p>

<ul>
  <li>the required canonical sections are present,</li>
  <li><code>front_panel</code> is allowed to be present,</li>
  <li>the front panel remains structurally well-formed,</li>
  <li>the front panel does not attempt to take ownership of executable graph content or public interface ownership.</li>
</ul>

<pre><code>front_panel present
+
front_panel structurally valid
+
diagram ownership preserved
    ->
acceptance required
</code></pre>

<hr/>

<h2 id="what-this-case-is-not-testing">8. What this Case Is Not Testing</h2>

<p>
This case is intentionally narrow.
It is not testing:
</p>

<ul>
  <li>full widget semantics,</li>
  <li><code>widget_value</code> versus <code>widget_reference</code> semantic behavior,</li>
  <li>diagram-side widget interaction,</li>
  <li>runtime UI realization,</li>
  <li>backend-family handling of UI participation.</li>
</ul>

<p>
It only tests one boundary:
</p>

<pre><code>front_panel present
      ->
must remain structurally valid
      ->
must remain in its source ownership role
</code></pre>

<hr/>

<h2 id="preservation-and-boundary-notes">9. Preservation and Boundary Notes</h2>

<p>
This case helps preserve the architectural distinction between:
</p>

<ul>
  <li>front-panel composition,</li>
  <li>public interface definition,</li>
  <li>diagram execution content,</li>
  <li>valid UI-source presence,</li>
  <li>ownership collapse.</li>
</ul>

<p>
It therefore protects the rule:
</p>

<pre><code>front_panel present
      -/-> executable authority

UI composition source
      -/-> second diagram
</code></pre>

<hr/>

<h2 id="implementation-requirements">10. Implementation Requirements</h2>

<p>
A conforming implementation handling this case SHOULD:
</p>

<ul>
  <li>load the source as JSON,</li>
  <li>validate required section presence,</li>
  <li>validate the structural shape of <code>front_panel</code>,</li>
  <li>accept the source as structurally valid canonical source,</li>
  <li>allow later semantic and derivation stages to proceed according to the published architecture.</li>
</ul>

<p>
A conforming implementation MUST NOT:
</p>

<ul>
  <li>reject the file merely because <code>front_panel</code> is present,</li>
  <li>reinterpret <code>front_panel</code> as executable graph ownership,</li>
  <li>collapse front-panel composition into public-interface ownership.</li>
</ul>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
This case establishes a focused positive truth:
</p>

<pre><code>front_panel present and structurally valid
    ->
canonical source still valid
    ->
acceptance required
</code></pre>

<p>
It anchors the positive side of the front-panel structural boundary in the FROG canonical source model.
</p>
