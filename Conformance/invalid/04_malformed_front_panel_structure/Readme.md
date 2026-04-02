<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">Invalid Case — Malformed Front Panel Structure</h1>

<p align="center">
  <strong>Structurally invalid canonical source due to a malformed <code>front_panel</code> section</strong><br/>
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
  <li><a href="#why-this-case-must-fail">7. Why this Case Must Fail</a></li>
  <li><a href="#what-this-case-is-not-testing">8. What this Case Is Not Testing</a></li>
  <li><a href="#preservation-and-boundary-notes">9. Preservation and Boundary Notes</a></li>
  <li><a href="#implementation-requirements">10. Implementation Requirements</a></li>
  <li><a href="#summary">11. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This case defines a canonical-source rejection expectation for a FROG file in which the optional <code>front_panel</code> section is present but malformed at the source-structure level.
</p>

<p>
The section is optional.
However, once present, it MUST satisfy the canonical source-shape rules that apply to front-panel composition and widget containment.
If the section has the wrong source form, the file is not a structurally valid canonical <code>.frog</code> source file.
</p>

<hr/>

<h2 id="case-purpose">2. Case Purpose</h2>

<p>
This case exists to verify that a conforming implementation does not collapse:
</p>

<pre><code>optional section
      !=
structurally unconstrained section
</code></pre>

<p>
An optional section may be absent.
But if it is present, it must still satisfy the source-structure rules owned by <code>Expression/</code>.
</p>

<hr/>

<h2 id="case-classification">3. Case Classification</h2>

<ul>
  <li><strong>Case family:</strong> invalid</li>
  <li><strong>Primary owner:</strong> <code>Expression/</code></li>
  <li><strong>Case kind:</strong> source-shape / structural-validity rejection</li>
  <li><strong>Expected loadability:</strong> loadable</li>
  <li><strong>Expected structural validity:</strong> invalid</li>
  <li><strong>Expected meaning:</strong> not established</li>
  <li><strong>Expected IR derivation:</strong> must not proceed as if validated meaning existed</li>
</ul>

<hr/>

<h2 id="normative-basis">4. Normative Basis</h2>

<p>
This case is grounded in the published canonical-source requirements of <code>Expression/</code>.
</p>

<p>
In FROG v0.1:
</p>

<ul>
  <li><code>front_panel</code> is an optional top-level source section,</li>
  <li>when present, it defines front-panel composition and widget-side source content,</li>
  <li>its presence does not make it free-form or implementation-private,</li>
  <li>all executable linkage related to front-panel widgets must still pass through the <code>diagram</code>.</li>
</ul>

<p>
Therefore, a malformed <code>front_panel</code> section is a structural-source failure.
</p>

<pre><code>optional front_panel absent
    -> allowed

optional front_panel present and well-formed
    -> allowed

optional front_panel present but malformed
    -> structural invalidity
</code></pre>

<hr/>

<h2 id="input-shape">5. Input Shape</h2>

<p>
The associated invalid source artifact for this case SHOULD be a JSON-loadable <code>.frog</code> file in which <code>front_panel</code> exists but is malformed as source.
</p>

<p>
Typical invalid patterns include:
</p>

<ul>
  <li><code>front_panel</code> represented with the wrong top-level shape,</li>
  <li>widget collections represented with the wrong container type,</li>
  <li>widget entries missing required structural identity fields,</li>
  <li>widget containment encoded in a shape not permitted by the source model,</li>
  <li>mixing executable linkage directly into <code>front_panel</code> instead of expressing it through the <code>diagram</code>.</li>
</ul>

<p>
A representative invalid intention is:
</p>

<pre><code>front_panel
  -> present as a source section
  -> contains widget data in a malformed source structure
  -> cannot be interpreted as valid front-panel composition
</code></pre>

<p>
This is not merely a UI-runtime issue.
It is a canonical-source failure.
</p>

<hr/>

<h2 id="expected-outcome">6. Expected Outcome</h2>

<p>
The expected outcome is:
</p>

<pre><code>Expected loadability: loadable
Expected structural validity: invalid
Expected meaning: not established
Expected rejection: malformed front_panel structure
</code></pre>

<p>
A conforming implementation MUST reject the case explicitly.
It MUST NOT silently normalize malformed front-panel source into validity.
It MUST NOT treat malformed UI source as harmless decoration.
It MUST NOT continue as if validated meaning had been established.
</p>

<hr/>

<h2 id="why-this-case-must-fail">7. Why this Case Must Fail</h2>

<p>
The FROG source model allows optional sections, but optionality does not remove structural discipline.
</p>

<p>
If a malformed <code>front_panel</code> were tolerated as canonical source, then:
</p>

<ul>
  <li>source-level UI composition would become implementation-defined,</li>
  <li>tooling could silently reinterpret broken source in incompatible ways,</li>
  <li>canonical source validity would no longer be publicly checkable.</li>
</ul>

<p>
This case must therefore fail because:
</p>

<ul>
  <li><code>front_panel</code> remains part of canonical source when present,</li>
  <li>canonical source must stay structurally checkable,</li>
  <li>runtime or IDE repair must not replace source validity.</li>
</ul>

<pre><code>optional section present
    +
malformed source shape
    ->
canonical source contract not satisfied
    ->
rejection required
</code></pre>

<hr/>

<h2 id="what-this-case-is-not-testing">8. What this Case Is Not Testing</h2>

<p>
This case is intentionally narrow.
It is not testing:
</p>

<ul>
  <li>whether a front panel is required,</li>
  <li>whether a given widget class is semantically useful,</li>
  <li>diagram legality for widget participation,</li>
  <li>widget_value versus widget_reference semantics,</li>
  <li>state semantics,</li>
  <li>IR preservation details,</li>
  <li>runtime UI realization.</li>
</ul>

<p>
It only tests one architectural boundary:
</p>

<pre><code>optional front_panel
      ->
still source-structured
      ->
still subject to structural validation
</code></pre>

<hr/>

<h2 id="preservation-and-boundary-notes">9. Preservation and Boundary Notes</h2>

<p>
This case helps preserve the following source-layer distinctions:
</p>

<ul>
  <li>optional presence versus arbitrary structure,</li>
  <li>UI composition source versus runtime UI realization,</li>
  <li>front-panel composition versus executable linkage.</li>
</ul>

<p>
It therefore protects the rule:
</p>

<pre><code>front_panel present
      -/-> source-valid by default

UI composition source
      -/-> implementation-private blob
</code></pre>

<p>
This boundary matters before semantic validation and far before runtime realization.
It must not be repaired implicitly by tools.
</p>

<hr/>

<h2 id="implementation-requirements">10. Implementation Requirements</h2>

<p>
A conforming implementation handling this case SHOULD:
</p>

<ul>
  <li>load the source if it is syntactically readable,</li>
  <li>validate the structural shape of <code>front_panel</code> when present,</li>
  <li>detect malformed front-panel source content,</li>
  <li>reject the file before claiming validated meaning exists,</li>
  <li>report the rejection as a structural-source failure.</li>
</ul>

<p>
A conforming implementation MUST NOT:
</p>

<ul>
  <li>treat malformed <code>front_panel</code> content as acceptable implementation-private UI data,</li>
  <li>auto-repair malformed widget composition silently,</li>
  <li>reinterpret malformed front-panel source as valid canonical source,</li>
  <li>derive execution-facing artifacts as if the source were structurally valid.</li>
</ul>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
This case establishes a clear public truth:
</p>

<pre><code>malformed front_panel structure
    ->
structurally invalid canonical source
    ->
rejection required
</code></pre>

<p>
It protects a key principle of the FROG source layer:
</p>

<pre><code>optional source section
   -&gt;
still canonical source
   -&gt;
still structurally checkable
</code></pre>

<p>
That principle must remain explicit across all conforming implementations.
</p>
