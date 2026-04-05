<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Examples</h1>

<p align="center">
  <strong>Illustrative named slices of the published FROG specification</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-directory-exists">2. Why This Directory Exists</a></li>
  <li><a href="#what-examples-are">3. What Examples Are</a></li>
  <li><a href="#what-examples-are-not">4. What Examples Are Not</a></li>
  <li><a href="#relation-with-conformance">5. Relation with Conformance</a></li>
  <li><a href="#relation-with-ir-profiles-and-reference-implementation">6. Relation with IR, Profiles, and Reference Implementation</a></li>
  <li><a href="#published-example-families">7. Published Example Families</a></li>
  <li><a href="#compiler-corridor-positive-mirror">8. Compiler-Corridor Positive Mirror</a></li>
  <li><a href="#reading-discipline">9. Reading Discipline</a></li>
  <li><a href="#growth-discipline">10. Growth Discipline</a></li>
  <li><a href="#summary">11. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory provides illustrative named slices of the published FROG specification.
</p>

<p>
Examples exist to make the repository easier to read across layers.
They give readers compact, recognizable cases that can be followed across canonical source structure, semantic interpretation, IR consequences, profile relevance, and bounded implementation consumption where such a corridor is already published.
</p>

<p>
Examples are therefore part of the repository-visible reading corridor,
but they are not independent semantic owners.
They remain subordinate to the published ownership boundaries of the specification.
</p>

<hr/>

<h2 id="why-this-directory-exists">2. Why This Directory Exists</h2>

<p>
A specification stack becomes easier to understand when readers can inspect small named slices that correspond to recognizable architectural situations.
</p>

<p>
Examples therefore exist to:
</p>

<ul>
  <li>illustrate published source structures,</li>
  <li>illustrate published semantic boundaries,</li>
  <li>illustrate published IR consequences,</li>
  <li>illustrate declared profile corridors where relevant,</li>
  <li>make repository-visible vertical slices easier to discuss across documents,</li>
  <li>support comparison between specification, conformance, and implementation-facing prototype corridors.</li>
</ul>

<p>
Their role is explanatory and alignment-oriented.
They help readers see how the specification is intended to be read in practice without turning prose documents into the only usable surface.
</p>

<hr/>

<h2 id="what-examples-are">3. What Examples Are</h2>

<p>
Examples are illustrative repository-visible slices.
They are intentionally small, focused, named, and architecture-oriented.
</p>

<p>
An example may illustrate:
</p>

<ul>
  <li>a canonical source shape,</li>
  <li>a semantic pattern,</li>
  <li>a control pattern,</li>
  <li>a state pattern,</li>
  <li>an IR-relevant derivation situation,</li>
  <li>a declared profile corridor,</li>
  <li>a bounded execution-facing reference path where such a path is already published.</li>
</ul>

<p>
A good example does not try to demonstrate everything at once.
It isolates one coherent architectural situation clearly enough that the reader can follow it across the neighboring published layers.
</p>

<hr/>

<h2 id="what-examples-are-not">4. What Examples Are Not</h2>

<p>
Examples do not become hidden semantic law.
</p>

<p>
The rule remains:
</p>

<pre><code>Specification defines
Conformance exposes public expectations
Examples illustrate</code></pre>

<p>
An example therefore does not replace the owning documents in:
</p>

<ul>
  <li><code>Expression/</code>,</li>
  <li><code>Language/</code>,</li>
  <li><code>Libraries/</code>,</li>
  <li><code>IR/</code>,</li>
  <li><code>Profiles/</code>,</li>
  <li><code>IDE/</code> where IDE-facing behavior is concerned.</li>
</ul>

<p>
Likewise:
</p>

<ul>
  <li>an example is not a substitute for conformance,</li>
  <li>an example is not a substitute for version-governance policy,</li>
  <li>an example is not a substitute for a reference implementation,</li>
  <li>an example does not authorize unstated semantic assumptions.</li>
</ul>

<p>
Examples may be useful teaching surfaces, but they must remain subordinate to the published specification owners.
</p>

<hr/>

<h2 id="relation-with-conformance">5. Relation with Conformance</h2>

<p>
Examples and conformance are related but distinct.
</p>

<ul>
  <li><strong>Examples</strong> illustrate named slices.</li>
  <li><strong>Conformance</strong> exposes accept / reject / preserve truth.</li>
</ul>

<p>
A useful reading model is:
</p>

<pre><code>example slice
   -&gt;
conformance expectation
   -&gt;
IR / profile reading where relevant
   -&gt;
reference consumption where published</code></pre>

<p>
This distinction matters because a readable example and a conforming acceptance boundary are not the same thing.
An example may help a reader understand a corridor,
but conformance is the public surface that states what must be accepted, rejected, preserved, or reported explicitly.
</p>

<p>
Examples should therefore stay synchronized with published conformance material where a named corridor is intentionally mirrored,
without allowing the example itself to become the hidden owner of the rule.
</p>

<hr/>

<h2 id="relation-with-ir-profiles-and-reference-implementation">6. Relation with IR, Profiles, and Reference Implementation</h2>

<p>
Examples may mirror:
</p>

<ul>
  <li>core source / semantic slices,</li>
  <li>IR-relevant slices,</li>
  <li>profile-relevant slices,</li>
  <li>bounded implementation-facing corridors that consume the published layers without owning them.</li>
</ul>

<p>
Where a declared compiler corridor is involved, examples should remain bounded and conservative.
They should illustrate only a corridor that the repository already exposes clearly enough across specification, conformance, and implementation-facing support material.
</p>

<p>
This means an example may be read alongside:
</p>

<ul>
  <li><code>IR/</code> when execution-facing derivation matters,</li>
  <li><code>Profiles/</code> when an optional corridor is being bounded,</li>
  <li><code>Implementations/Reference/</code> when the published repository already contains a non-normative consumer path for the same slice.</li>
</ul>

<p>
The ownership model still remains explicit:
</p>

<pre><code>Examples
   -&gt; illustrate

Conformance
   -&gt; expose public expectations

IR
   -&gt; define canonical execution-facing law

Profiles
   -&gt; bound optional downstream corridors

Implementations/Reference
   -&gt; consume the published layers without owning them</code></pre>

<hr/>

<h2 id="published-example-families">7. Published Example Families</h2>

<p>
Published example growth should remain small, architecture-first, and repository-coherent.
</p>

<p>
At the current published state, the first coherent family is the positive compiler-corridor mirror for the conservative <code>native_cpu_llvm</code> route.
</p>

<p>
That choice is deliberate.
It opens a bounded vertical slice where readers can follow:
</p>

<ul>
  <li>canonical source intent,</li>
  <li>semantic acceptance,</li>
  <li>IR relevance,</li>
  <li>profile corridor relevance,</li>
  <li>reference implementation consumption.</li>
</ul>

<p>
The goal is not to maximize example count immediately.
The goal is to expose one disciplined and inspectable corridor clearly before broadening the example surface.
</p>

<hr/>

<h2 id="compiler-corridor-positive-mirror">8. Compiler-Corridor Positive Mirror</h2>

<p>
The initial positive mirror is:
</p>

<pre><code>Examples/compiler/
├── 01_pure_arithmetic.md
├── 02_structured_control.md
└── 03_explicit_state.md</code></pre>

<p>
These examples correspond to the first named positive corridor:
</p>

<ul>
  <li><strong>pure computation</strong>,</li>
  <li><strong>structured control</strong>,</li>
  <li><strong>explicit state</strong>.</li>
</ul>

<p>
Together, they form a conservative first mirror of a bounded compiler-oriented path.
They are intentionally modest in scope:
</p>

<ul>
  <li><code>01_pure_arithmetic.md</code> keeps the corridor centered on direct computation,</li>
  <li><code>02_structured_control.md</code> introduces control-structure relevance without opening unrelated complexity,</li>
  <li><code>03_explicit_state.md</code> introduces explicit state and valid feedback discipline as a distinct step.</li>
</ul>

<p>
This progression is architecture-first.
It does not attempt to open every front at once.
It opens one coherent corridor that can be mirrored by conformance and consumed by a reference path.
</p>

<hr/>

<h2 id="reading-discipline">9. Reading Discipline</h2>

<p>
Examples should normally be read together with their neighboring ownership and support layers.
</p>

<p>
A practical reading order is:
</p>

<pre><code>example
   -&gt;
owning Expression / Language documents
   -&gt;
IR documents where execution-facing consequences matter
   -&gt;
Profiles documents where an optional corridor is involved
   -&gt;
Conformance expectations
   -&gt;
Reference implementation workspace where published</code></pre>

<p>
This prevents two common mistakes:
</p>

<ul>
  <li>treating examples as if they defined the language,</li>
  <li>reading examples in isolation and inferring unstated closure that the repository has not published.</li>
</ul>

<hr/>

<h2 id="growth-discipline">10. Growth Discipline</h2>

<p>
Future example growth should remain disciplined.
New example families should be added when they close a meaningful repository-visible corridor rather than merely increasing surface area.
</p>

<p>
In practice, new examples should preferably:
</p>

<ul>
  <li>illustrate one coherent architectural situation,</li>
  <li>map cleanly to neighboring conformance material where relevant,</li>
  <li>remain compatible with published IR and profile boundaries,</li>
  <li>avoid silently introducing new semantic law,</li>
  <li>avoid broad mixed-purpose scenarios when a smaller slice would communicate the corridor more clearly.</li>
</ul>

<p>
The preferred direction is therefore:
</p>

<pre><code>close one coherent mirror
   -&gt;
align conformance and reference consumption
   -&gt;
only then broaden the next example family</code></pre>

<hr/>

<h2 id="summary">11. Summary</h2>

<p>
Examples are illustrative named slices of the specification.
They remain subordinate to the owning specification documents and complementary to conformance, IR, profiles, and the non-normative reference implementation workspace.
</p>

<p>
The first coherent published mirror is the positive compiler corridor for the conservative <code>native_cpu_llvm</code> route.
That mirror currently consists of:
</p>

<ul>
  <li><code>01_pure_arithmetic.md</code>,</li>
  <li><code>02_structured_control.md</code>,</li>
  <li><code>03_explicit_state.md</code>.</li>
</ul>

<p>
Examples help make the specification readable across layers,
but they do not replace the documents that own source law, semantic law, execution-facing law, profile law, or public conformance expectations.
</p>
