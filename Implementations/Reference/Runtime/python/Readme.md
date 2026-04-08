<p align="center">
  <img src="../../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Reference Runtime (Python)</h1>

<p align="center">
  <strong>Bounded Python consumer for the reference runtime family in the non-normative FROG reference implementation</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-directory-should-exist">2. Why This Directory Should Exist</a></li>
  <li><a href="#directory-shape">3. Directory Shape</a></li>
  <li><a href="#role-of-each-file">4. Role of Each File</a></li>
  <li><a href="#primary-slice-target">5. Primary Slice Target</a></li>
  <li><a href="#relation-with-runtime-boundary">6. Relation to the Runtime Boundary</a></li>
  <li><a href="#what-this-runtime-consumes">7. What This Runtime Consumes</a></li>
  <li><a href="#what-this-runtime-produces">8. What This Runtime Produces</a></li>
  <li><a href="#published-pipes">9. Published Pipes for Example 05</a></li>
  <li><a href="#bounded-widget-surface">10. Bounded Widget Surface</a></li>
  <li><a href="#design-rules">11. Design Rules</a></li>
  <li><a href="#relationship-with-rust-and-cpp">12. Relationship with Rust and C/C++ Consumers</a></li>
  <li><a href="#closure-status">13. Python Closure Status</a></li>
  <li><a href="#future-growth">14. Future Growth</a></li>
  <li><a href="#summary">15. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the bounded Python realization of the published reference runtime family for the FROG reference implementation.
It is a downstream runtime consumer.
It exists to demonstrate the clearest direct execution posture for the current bounded example corridor and the first concrete rendered widget slice.
</p>

<p>
The Python runtime now serves two distinct but aligned purposes:
</p>

<ul>
  <li>consume the already-published contract-driven runtime corridor,</li>
  <li>provide one concrete host-rendered widget runtime for the bounded Example 05 widget subset.</li>
</ul>

<p>
Accordingly, this directory is not just a convenience folder for incidental Python code.
It is the first explicit language realization of a runtime family that is intended to remain parallel to Rust and future C/C++ consumers.
</p>

<hr/>

<h2 id="why-this-directory-should-exist">2. Why This Directory Should Exist</h2>

<p>
The parent runtime directory already exposes Python execution material, but a dedicated <code>python/</code> documentation surface is useful because the long-term target is not “one runtime with incidental Python code”.
The long-term target is “one runtime family with several language realizations consuming the same canonical corridor”.
</p>

<p>
This directory therefore exists to make the Python side explicit and symmetric with:
</p>

<ul>
  <li><code>Runtime/rust/</code>,</li>
  <li><code>Runtime/cpp/</code>,</li>
  <li>and later any other runtime-language consumer.</li>
</ul>

<p>
It also now provides a natural home for the first concrete widget-rendering runtime files:
</p>

<ul>
  <li><code>ui_runtime.py</code>,</li>
  <li><code>run_slice05_ui.py</code>.</li>
</ul>

<hr/>

<h2 id="directory-shape">3. Directory Shape</h2>

<pre><code>Implementations/Reference/Runtime/python/
├── Readme.md
├── ui_runtime.py
└── run_slice05_ui.py
</code></pre>

<p>
The parent runtime directory still carries contract-oriented Python files such as:
</p>

<ul>
  <li><code>Implementations/Reference/Runtime/reference_runtime.py</code>,</li>
  <li><code>Implementations/Reference/Runtime/run_slice05_contract.py</code>.</li>
</ul>

<p>
That current split is acceptable for the bounded slice, but the longer-term useful shape is:
</p>

<pre><code>Implementations/Reference/Runtime/python/
├── Readme.md
├── runtime_core.py
├── execute_contract.py
├── ui_runtime.py
├── run_slice05_ui.py
├── cli.py
└── tests/
    ├── test_slice05_contract.py
    └── test_slice05_ui_runtime.py
</code></pre>

<p>
The important point is not the exact future filenames.
The important point is that Python-side responsibilities become explicit instead of remaining mixed invisibly at parent level.
</p>

<hr/>

<h2 id="role-of-each-file">4. Role of Each File</h2>

<ul>
  <li><code>Readme.md</code><br/>
      Explains the Python-side runtime posture and the role of this directory.</li>

  <li><code>ui_runtime.py</code><br/>
      Concrete bounded host-rendered Python widget runtime for the current Example 05 widget subset. It loads one <code>.wfrog</code> front-panel package, constructs live widget objects, interprets a bounded property/method surface, opens a real window, and updates the visible widget state.</li>

  <li><code>run_slice05_ui.py</code><br/>
      Python runner for the rendered Example 05 slice. It loads the example-local <code>.wfrog</code> package, optionally injects an initial input value, optionally autoruns the bounded accumulator, and starts the host UI loop.</li>
</ul>

<p>
The current published contract-oriented Python responsibilities still live partly at parent runtime level:
</p>

<ul>
  <li><code>Runtime/reference_runtime.py</code>,</li>
  <li><code>Runtime/run_slice05_contract.py</code>.</li>
</ul>

<p>
That means the Python family currently has two visible corridors:
</p>

<ul>
  <li>a contract-driven corridor,</li>
  <li>a rendered widget corridor.</li>
</ul>

<hr/>

<h2 id="primary-slice-target">5. Primary Slice Target</h2>

<p>
The first target for this runtime is the published example:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/</code></pre>

<p>
That example establishes a bounded executable corridor with:
</p>

<ul>
  <li>one numeric front-panel control,</li>
  <li>one numeric front-panel indicator,</li>
  <li>one bounded loop of exactly five iterations,</li>
  <li>one explicit local-memory path,</li>
  <li>one final public output,</li>
  <li>and a minimal object-style UI write surface through <code>frog.ui.property_write</code>.</li>
</ul>

<p>
The bounded rendered widget subset currently exercised by the Python runtime is:
</p>

<ul>
  <li><code>frog.widgets.panel</code>,</li>
  <li><code>frog.widgets.numeric_control</code>,</li>
  <li><code>frog.widgets.numeric_indicator</code>,</li>
  <li><code>frog.widgets.label</code>.</li>
</ul>

<hr/>

<h2 id="relation-with-runtime-boundary">6. Relation to the Runtime Boundary</h2>

<p>
The published runtime family is:
</p>

<pre><code>reference_host_runtime_ui_binding</code></pre>

<p>
This Python runtime is one consumer of that family posture.
It follows the same runtime-side assumptions as the parallel Rust and future C/C++ consumers.
</p>

<p>
At the same time, the rendered widget runner is a bounded host-realization extension that helps make the widget model concrete.
It must therefore remain downstream from the canonical corridor rather than becoming the definition of FROG itself.
</p>

<p>
The architectural rule remains:
</p>

<pre><code>.frog source
    !=
.wfrog package
    !=
runtime-private Python objects
    !=
host-rendered toolkit widgets
</code></pre>

<hr/>

<h2 id="what-this-runtime-consumes">7. What This Runtime Consumes</h2>

<p>
For the contract-oriented corridor, the Python runtime starts after source loading, structural validation, semantic validation, FIR-target derivation, and lowering have already produced an acceptable backend contract.
</p>

<p>
For the current bounded published slice, the Python family consumes:
</p>

<ul>
  <li>one backend contract artifact from the reference contract emitter,</li>
  <li>one declared backend family equal to <code>reference_host_runtime_ui_binding</code>,</li>
  <li>one explicit bounded loop model,</li>
  <li>one explicit delay-backed state carrier,</li>
  <li>one control-input binding,</li>
  <li>one indicator/public-output publication rule,</li>
  <li>and one minimal property-write surface.</li>
</ul>

<p>
For the rendered widget corridor, the Python runtime additionally consumes:
</p>

<ul>
  <li>one example-local <code>.wfrog</code> front-panel package,</li>
  <li>one bounded set of widget classes,</li>
  <li>one bounded set of source-owned widget properties,</li>
  <li>one bounded set of widget methods,</li>
  <li>optional SVG visual asset references used as skins and anchors only.</li>
</ul>

<p>
The rendered runtime currently interprets the following property surface:
</p>

<ul>
  <li><code>value</code>,</li>
  <li><code>label</code>,</li>
  <li><code>visible</code>,</li>
  <li><code>enabled</code>,</li>
  <li><code>face_color</code>.</li>
</ul>

<p>
The rendered runtime currently interprets the following method surface:
</p>

<ul>
  <li><code>focus</code>,</li>
  <li><code>reset_to_default_style</code>.</li>
</ul>

<hr/>

<h2 id="what-this-runtime-produces">8. What This Runtime Produces</h2>

<p>
For the current bounded corridor, the Python family produces runtime-visible evidence that:
</p>

<ul>
  <li>the contract was accepted,</li>
  <li>the loop ran exactly five iterations,</li>
  <li>the state started at zero,</li>
  <li>the final state for input <code>3</code> is <code>15</code>,</li>
  <li>the public output is correct,</li>
  <li>the indicator value is correct,</li>
  <li>the bounded widget runtime state is preserved for the supported widgets.</li>
</ul>

<p>
For the rendered UI corridor, the Python runtime also produces:
</p>

<ul>
  <li>one real host window,</li>
  <li>one concrete rendered control widget,</li>
  <li>one concrete rendered indicator widget,</li>
  <li>one bounded host-side property-write effect on visible widget state,</li>
  <li>one concrete proof that the widget system is being interpreted rather than merely described.</li>
</ul>

<hr/>

<h2 id="published-pipes">9. Published Pipes for Example 05</h2>

<p>
The Python family currently exposes two useful execution pipes for Example 05.
</p>

<h3>9.1 Contract-driven pipe</h3>

<pre><code>python -m Implementations.Reference.Runtime.run_slice05_contract 3
</code></pre>

<p>
Equivalent direct invocation:
</p>

<pre><code>python Implementations/Reference/Runtime/run_slice05_contract.py 3
</code></pre>

<p>
This path exercises the already-published contract-driven reference runtime corridor.
</p>

<h3>9.2 Rendered UI pipe</h3>

<pre><code>python Implementations/Reference/Runtime/python/run_slice05_ui.py
</code></pre>

<p>
Optional initial value:
</p>

<pre><code>python Implementations/Reference/Runtime/python/run_slice05_ui.py 3
</code></pre>

<p>
Optional autorun:
</p>

<pre><code>python Implementations/Reference/Runtime/python/run_slice05_ui.py 3 --autorun
</code></pre>

<p>
This path exercises the bounded host-rendered widget runtime corridor through the example-local <code>.wfrog</code> package.
</p>

<hr/>

<h2 id="bounded-widget-surface">10. Bounded Widget Surface</h2>

<p>
The rendered Python UI runtime is intentionally bounded.
It is not yet a general industrial widget toolkit.
It is the first concrete executable widget slice for the current example family.
</p>

<p>
The currently supported widget classes are:
</p>

<ul>
  <li><code>frog.widgets.panel</code></li>
  <li><code>frog.widgets.numeric_control</code></li>
  <li><code>frog.widgets.numeric_indicator</code></li>
  <li><code>frog.widgets.label</code></li>
</ul>

<p>
The currently supported property surface is:
</p>

<ul>
  <li><code>value</code></li>
  <li><code>label</code></li>
  <li><code>visible</code></li>
  <li><code>enabled</code></li>
  <li><code>face_color</code></li>
</ul>

<p>
The currently supported method surface is:
</p>

<ul>
  <li><code>focus</code></li>
  <li><code>reset_to_default_style</code></li>
</ul>

<p>
The currently supported part names are:
</p>

<ul>
  <li><code>root</code></li>
  <li><code>label</code></li>
  <li><code>value_display</code></li>
</ul>

<p>
This bounded surface is enough to make the first widget corridor concrete without pretending that the full future widget system is already closed.
</p>

<hr/>

<h2 id="design-rules">11. Design Rules</h2>

<ul>
  <li>Accept or reject contracts explicitly.</li>
  <li>Accept or reject widget packages explicitly.</li>
  <li>Do not silently reinterpret undeclared assumptions.</li>
  <li>Keep explicit local-memory meaning visible in runtime execution.</li>
  <li>Keep loop iteration count explicit where the contract declares it.</li>
  <li>Keep runtime-private helper structures downstream from the published backend contract and widget package surfaces.</li>
  <li>Reject unsupported widget classes, widget parts, properties, or methods explicitly.</li>
  <li>Do not let Python implementation convenience become semantic law.</li>
  <li>Do not let visual assets become the owner of widget semantics, dynamic values, or dynamic text.</li>
</ul>

<hr/>

<h2 id="relationship-with-rust-and-cpp">12. Relationship with Rust and C/C++ Consumers</h2>

<p>
The Python runtime is not “the FROG runtime”.
It is one runtime-language realization of the same runtime family.
It must remain aligned with:
</p>

<ul>
  <li>the Rust consumer,</li>
  <li>the future C/C++ consumer,</li>
  <li>and the same canonical example corridor.</li>
</ul>

<p>
The rendered Python widget path is useful because it makes the widget system visible now, but it must not become an excuse to leave Rust and C/C++ permanently behind.
The long-term goal remains one shared corridor consumed by several runtime-language realizations.
</p>

<hr/>

<h2 id="closure-status">13. Python Closure Status</h2>

<table>
  <thead>
    <tr>
      <th>Python-side surface</th>
      <th>Status</th>
      <th>Posture</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Contract loading</td>
      <td>Closed</td>
      <td>Published contract artifact is consumed successfully.</td>
    </tr>
    <tr>
      <td>Direct contract example runner</td>
      <td>Closed</td>
      <td>A direct command exists for Example 05.</td>
    </tr>
    <tr>
      <td>Rendered UI runner</td>
      <td>Closed for bounded slice</td>
      <td>A concrete command exists for the bounded widget subset of Example 05.</td>
    </tr>
    <tr>
      <td>Bounded widget interpretation</td>
      <td>Closed for current subset</td>
      <td>Panel, numeric control, numeric indicator, and label are interpreted concretely.</td>
    </tr>
    <tr>
      <td>Parity with Rust</td>
      <td>Partial</td>
      <td>Both consume the same corridor family, but rendered UI parity is not yet closed.</td>
    </tr>
    <tr>
      <td>Parity with C/C++</td>
      <td>Missing</td>
      <td>No C/C++ peer consumer is published yet.</td>
    </tr>
    <tr>
      <td>General widget-system closure</td>
      <td>Missing</td>
      <td>The current runtime is intentionally bounded and example-driven.</td>
    </tr>
    <tr>
      <td>Contract-driven rendered UI unification</td>
      <td>Partial</td>
      <td>The two Python corridors exist, but they are not yet fully merged into one rendered contract-driven path.</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2 id="future-growth">14. Future Growth</h2>

<ol>
  <li>factor parent-level contract Python files into a clearer Python-side structure,</li>
  <li>connect the rendered UI path more directly to the contract-driven corridor,</li>
  <li>add Python-side tests for widget-package loading and rendered Example 05 behavior,</li>
  <li>align Python, Rust, and future C/C++ pipes around the same example-local artifact set,</li>
  <li>extend the bounded widget subset carefully instead of growing an unstructured UI surface.</li>
</ol>

<hr/>

<h2 id="summary">15. Summary</h2>

<p>
This directory makes the Python runtime posture explicit as one consumer of the reference runtime family.
Its role is now twofold:
</p>

<ul>
  <li>provide the clearest direct contract-driven execution corridor,</li>
  <li>provide the first bounded rendered widget corridor for Example 05.</li>
</ul>

<p>
It remains only one downstream realization of the same shared corridor.
It must not become the owner of widget semantics, language truth, or long-term runtime exclusivity.
</p>
