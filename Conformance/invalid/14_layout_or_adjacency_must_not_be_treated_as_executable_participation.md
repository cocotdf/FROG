<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1>Conformance Case — Invalid: Public Interface Declaration Must Not Require Front-Panel Widget Existence</h1>

<p><strong>Invalid conformance case for requiring front-panel widget existence as a condition for public interface validity in FROG v0.1</strong><br>
FROG — Free Open Graphical Language</p>

<hr>

<h2>Contents</h2>
<ul>
  <li><a href="#case-overview">1. Case Overview</a></li>
  <li><a href="#expected-status">2. Expected Status</a></li>
  <li><a href="#intended-anti-pattern">3. Intended Anti-Pattern</a></li>
  <li><a href="#boundaries-exercised">4. Boundaries Exercised</a></li>
  <li><a href="#why-this-case-is-invalid">5. Why this Case Is Invalid</a></li>
  <li><a href="#expected-validation-outcome">6. Expected Validation Outcome</a></li>
  <li><a href="#why-derivation-is-forbidden">7. Why Derivation Is Forbidden</a></li>
  <li><a href="#why-silent-repair-is-wrong">8. Why Silent Repair Is Wrong</a></li>
  <li><a href="#summary">9. Summary</a></li>
</ul>

<hr>

<h2 id="case-overview">1. Case Overview</h2>

<p>This invalid case covers a source shape or tool behavior that treats front-panel widget existence as a required condition for public interface validity.</p>

<p>Typical anti-patterns include:</p>

<ul>
  <li>rejecting a public interface input because no matching front-panel control exists,</li>
  <li>rejecting a public interface output because no matching front-panel indicator exists,</li>
  <li>requiring every callable public port to have a UI counterpart,</li>
  <li>treating front-panel widget inventory as the authority that determines whether a public interface is legitimate.</li>
</ul>

<p>Conceptually, the forbidden collapse is:</p>

<pre><code>public interface declaration
              ==
required front-panel widget existence
</code></pre>

<p>Base FROG v0.1 does not allow that equivalence.</p>

<hr>

<h2 id="expected-status">2. Expected Status</h2>

<p><strong>Expected:</strong> invalid</p>

<hr>

<h2 id="intended-anti-pattern">3. Intended Anti-Pattern</h2>

<p>The invalid intent is any source shape, validator behavior, derivation behavior, or lowering behavior that requires a public interface declaration to be backed by corresponding front-panel widget existence in order to be accepted.</p>

<p>A minimal conceptual anti-pattern is:</p>

<pre><code>public interface:
  input  x
  output result

front panel:
  no widget for x
  no widget for result

diagram:
  interface_input(x) ----&gt; frog.core.add ----&gt; interface_output(result)

tool interpretation:
  "the interface is incomplete because no UI widgets exist for x and result"
</code></pre>

<p>Another invalid interpretation is:</p>

<pre><code>public port exists
    therefore
matching front-panel widget must exist
</code></pre>

<p>without any published rule establishing such a requirement.</p>

<hr>

<h2 id="boundaries-exercised">4. Boundaries Exercised</h2>

<ul>
  <li>public interface ownership,</li>
  <li>front-panel composition ownership,</li>
  <li>public callable contract versus UI realization,</li>
  <li>interface declaration versus widget inventory,</li>
  <li>rejection of semantic collapse across public contract and UI surface.</li>
</ul>

<hr>

<h2 id="why-this-case-is-invalid">5. Why this Case Is Invalid</h2>

<p>This case is invalid because base FROG v0.1 publishes these roles as distinct:</p>

<ul>
  <li>public interface declaration establishes the public callable boundary of the program,</li>
  <li>front-panel composition belongs to the UI surface and remains optional or separate unless explicit published participation says otherwise,</li>
  <li>public interface existence does not depend on widget existence,</li>
  <li>UI presence may support interaction, projection, or recoverability, but it does not determine whether the public contract exists.</li>
</ul>

<p>Requiring widgets in order for the public interface to be valid therefore contradicts the published architecture.</p>

<p>The required separation is:</p>

<pre><code>public interface law
          !=
front-panel widget inventory
</code></pre>

<hr>

<h2 id="expected-validation-outcome">6. Expected Validation Outcome</h2>

<p>A conforming validator should reject the case when the source or tool behavior requires front-panel widget existence as a condition for accepting an otherwise valid public interface declaration.</p>

<p>It should report that at least one of the following boundaries has been violated:</p>

<ul>
  <li>public interface declaration versus front-panel composition,</li>
  <li>callable program contract versus UI realization,</li>
  <li>interface validity versus widget inventory.</li>
</ul>

<p>If the case attempts to justify the requirement through editor convention, UX preference, implementation convenience, or backend expectation, that should still be rejected. None of those creates language law.</p>

<hr>

<h2 id="why-derivation-is-forbidden">7. Why Derivation Is Forbidden</h2>

<p>Execution IR derivation is forbidden for this invalid case because validation has not established a legitimate program meaning under the tool’s rewritten requirement.</p>

<p>There is no conforming basis for deriving:</p>

<ul>
  <li>a failure of the public callable boundary solely because no widgets exist,</li>
  <li>an execution model in which interface validity depends on UI inventory,</li>
  <li>or a backend-facing contract that pretends the interface was incomplete until widgets were added.</li>
</ul>

<p>Derivation would first require an unpublished semantic reinterpretation. That is not allowed.</p>

<hr>

<h2 id="why-silent-repair-is-wrong">8. Why Silent Repair Is Wrong</h2>

<p>A conforming toolchain must not silently “repair” this case by:</p>

<ul>
  <li>creating synthetic front-panel widgets in order to justify the public interface,</li>
  <li>downgrading public interface declaration into a UI-dependent concept,</li>
  <li>treating missing widgets as though they were missing interface declarations,</li>
  <li>making interface acceptance contingent on UI projection conventions while still claiming conformance.</li>
</ul>

<p>Such behavior would erase distinctions that the published source-to-meaning boundary requires to remain explicit and recoverable.</p>

<p>The forbidden repair pattern is:</p>

<pre><code>public interface exists
    -/-> required widget exists

missing widget
    -/-> invalid public contract
</code></pre>

<hr>

<h2 id="summary">9. Summary</h2>

<p>This case must be rejected because FROG v0.1 treats public interface declaration and front-panel widget existence as distinct published categories.</p>

<p>A conforming implementation must reject any source or tool behavior that depends on requiring front-panel widget existence in order to accept a public interface declaration.</p>

<p>The essential rule is:</p>

<pre><code>public interface declaration
    does not require
front-panel widget existence
</code></pre>
