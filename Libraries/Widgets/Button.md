<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Standard Button Widget</h1>

<p align="center">
  <strong>Normative baseline for the standardized push button widget class</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#class-defined-here">2. Class Defined Here</a></li>
  <li><a href="#frogwidgetsbutton">3. <code>frog.widgets.button</code></a></li>
  <li><a href="#standard-parts">4. Standard Parts</a></li>
  <li><a href="#behavior-expectations">5. Behavior Expectations</a></li>
  <li><a href="#realization-expectations">6. Realization Expectations</a></li>
  <li><a href="#diagram-interaction-posture">7. Diagram Interaction Posture</a></li>
  <li><a href="#validation-expectations">8. Validation Expectations</a></li>
  <li><a href="#summary">9. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the intrinsic standardized baseline for the push button widget of FROG.
</p>

<p>
The button is a command-oriented widget.
Its primary role is not to expose a user-edited scalar value in the same way as numeric, boolean, or string controls.
Its primary role is to expose an explicit interaction surface that may trigger methods, event observation, or command-style logic.
</p>

<hr/>

<h2 id="class-defined-here">2. Class Defined Here</h2>

<p>
This document defines the following standardized widget class:
</p>

<ul>
  <li><code>frog.widgets.button</code></li>
</ul>

<hr/>

<h2 id="frogwidgetsbutton">3. <code>frog.widgets.button</code></h2>

<h3>3.1 Class identity</h3>

<ul>
  <li><strong>class_id:</strong> <code>frog.widgets.button</code></li>
  <li><strong>category:</strong> <code>control</code></li>
  <li><strong>compatible role:</strong> <code>control</code></li>
</ul>

<h3>3.2 Primary value posture</h3>

<p>
The intrinsic button baseline does not define a standard persistent primary value surface.
</p>

<p>
Instead, the standard button is primarily event- and method-oriented.
It may expose transient interaction state through properties, but it is not standardized here as a value-carrying scalar control.
</p>

<h3>3.3 Standard properties</h3>

<ul>
  <li><code>label.text</code></li>
  <li><code>interaction.enabled</code></li>
  <li><code>interaction.visible</code></li>
  <li><code>interaction.pressed</code> — readable runtime interaction state when exposed</li>
</ul>

<h3>3.4 Standard methods</h3>

<ul>
  <li><code>focus()</code></li>
  <li><code>press()</code> when allowed by the active interaction posture</li>
  <li><code>release()</code> when allowed by the active interaction posture</li>
</ul>

<h3>3.5 Standard events</h3>

<ul>
  <li><code>pressed</code></li>
  <li><code>released</code></li>
  <li><code>clicked</code></li>
  <li><code>focus_gained</code></li>
  <li><code>focus_lost</code></li>
</ul>

<h3>3.6 Standard parts</h3>

<ul>
  <li><code>root</code></li>
  <li><code>face</code></li>
  <li><code>label</code></li>
  <li><code>frame</code> when present</li>
</ul>

<hr/>

<h2 id="standard-parts">4. Standard Parts</h2>

<p>
The button family uses the following common stable parts:
</p>

<ul>
  <li><code>root</code> — root widget surface</li>
  <li><code>face</code> — the main clickable visual face of the button</li>
  <li><code>label</code> — the text or content-bearing visible label surface</li>
  <li><code>frame</code> — optional outer frame surface</li>
</ul>

<hr/>

<h2 id="behavior-expectations">5. Behavior Expectations</h2>

<p>
The intrinsic behavior baseline of the button includes at least:
</p>

<ul>
  <li>user-originated activation is suppressed when the button is disabled,</li>
  <li>press interaction may emit <code>pressed</code>,</li>
  <li>release interaction may emit <code>released</code>,</li>
  <li>a completed button activation may emit <code>clicked</code>,</li>
  <li>runtime interaction state such as pressed posture, when exposed, remains transient rather than canonical program state.</li>
</ul>

<hr/>

<h2 id="realization-expectations">6. Realization Expectations</h2>

<p>
A conforming realization of the button SHOULD provide:
</p>

<ul>
  <li>a clearly perceivable actionable face surface,</li>
  <li>standard visual states such as enabled, disabled, pressed, and focused where supported by the host,</li>
  <li>stable part-to-visual mapping for <code>face</code> and <code>label</code>,</li>
  <li>reasonable visible feedback on user activation.</li>
</ul>

<p>
The button is a particularly important example of the realization split:
multiple SVG resources or other realization assets MAY exist for different interaction states,
but those assets do not define the semantics of the button.
They only realize already-published class surfaces and interaction states.
</p>

<hr/>

<h2 id="diagram-interaction-posture">7. Diagram Interaction Posture</h2>

<p>
The button supports:
</p>

<ul>
  <li>object-style property access where legal,</li>
  <li>method invocation where legal,</li>
  <li>event observation through <code>frog.ui.event_observe</code>,</li>
  <li>widget reference targeting through <code>widget_reference</code>.</li>
</ul>

<p>
The intrinsic button baseline is primarily event-oriented and command-oriented.
It is not standardized here as a natural value-path widget.
</p>

<hr/>

<h2 id="validation-expectations">8. Validation Expectations</h2>

<p>
Validators SHOULD diagnose at least:
</p>

<ul>
  <li>attempts to treat the button as a required scalar value-carrying widget in the intrinsic baseline,</li>
  <li>access to unknown members or parts,</li>
  <li>use of role/class combinations incompatible with <code>frog.widgets.button</code>,</li>
  <li>attempts to interpret transient pressed state as canonical persistent source-owned state by default.</li>
</ul>

<hr/>

<h2 id="summary">9. Summary</h2>

<p>
The standardized button defines the intrinsic command-oriented action widget of the FROG baseline:
</p>

<ul>
  <li><code>frog.widgets.button</code></li>
</ul>

<p>
It is primarily an event- and method-oriented control surface with stable parts, stable interaction states, and portable executable observation through the widget interaction corridor.
</p>
