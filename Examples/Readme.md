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
  <li><a href="#core-language-example-slices">8. Core Language Example Slices</a></li>
  <li><a href="#applicative-vertical-slice">9. Applicative Vertical Slice</a></li>
  <li><a href="#compiler-corridor-positive-mirror">10. Compiler-Corridor Positive Mirror</a></li>
  <li><a href="#reading-discipline">11. Reading Discipline</a></li>
  <li><a href="#growth-discipline">12. Growth Discipline</a></li>
  <li><a href="#summary">13. Summary</a></li>
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
Where an applicative vertical slice is involved, examples should still remain bounded enough that the repository-visible ownership chain can be followed clearly.
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
At the current published state, this directory contains two complementary public reading surfaces:
</p>

<ul>
  <li>a sequence of core named slices under <code>Examples/01_*</code> through <code>Examples/05_*</code>,</li>
  <li>and a conservative compiler-corridor positive mirror under <code>Examples/compiler/</code>.</li>
</ul>

<p>
That split is intentional.
The numbered example slices help the repository expose progressively richer source-to-semantics and source-to-execution situations,
while the compiler mirror keeps a deliberately narrower and more conservative corridor visible for compiler-facing reading.
</p>

<p>
The goal is not to maximize example count immediately.
The goal is to expose disciplined and inspectable corridors clearly before broadening the example surface further.
</p>

<hr/>

<h2 id="core-language-example-slices">8. Core Language Example Slices</h2>

<p>
The currently published numbered slices are:
</p>

<pre><code>Examples/
├── 01_pure_addition/
├── 02_ui_value_roundtrip/
├── 03_ui_property_write/
├── 04_stateful_feedback_delay/
└── 05_bounded_ui_accumulator/</code></pre>

<p>
Taken together, these slices expose a useful progression:
</p>

<ul>
  <li><strong>01_pure_addition</strong> keeps the first reading corridor centered on simple dataflow computation,</li>
  <li><strong>02_ui_value_roundtrip</strong> introduces front-panel value participation without opening object-style UI access yet,</li>
  <li><strong>03_ui_property_write</strong> introduces bounded object-style property-write participation,</li>
  <li><strong>04_stateful_feedback_delay</strong> introduces explicit state through a bounded feedback / delay pattern,</li>
  <li><strong>05_bounded_ui_accumulator</strong> combines front-panel participation, bounded iteration, explicit state, public output, and minimal UI object-style access in one coherent applicative slice.</li>
</ul>

<p>
This progression should be read as architectural layering, not as hidden semantic law.
Each slice remains illustrative and subordinate to the documents that own source, semantic, IR, profile, and runtime-boundary meaning.
</p>

<hr/>

<h2 id="applicative-vertical-slice">9. Applicative Vertical Slice</h2>

<p>
The first repository-visible applicative vertical slice is:
</p>

<pre><code>Examples/05_bounded_ui_accumulator/</code></pre>

<p>
This slice matters because it is the first published example in this directory that intentionally touches multiple major layers in one bounded corridor, including:
</p>

<ul>
  <li>canonical source structure,</li>
  <li>public interface participation,</li>
  <li>front-panel participation,</li>
  <li>simple widget-value use,</li>
  <li>minimal widget-reference use,</li>
  <li>bounded loop behavior,</li>
  <li>explicit state,</li>
  <li>observable final output,</li>
  <li>and a published non-normative runtime-consumption posture in <code>Implementations/Reference/Runtime/</code>.</li>
</ul>

<p>
This does not make the example the owner of the corridor.
It means the repository now contains a more complete applicative reading anchor than the earlier narrower mirrors alone.
</p>

<p>
Accordingly, readers interested in the first published end-to-end executable posture should treat <code>05_bounded_ui_accumulator</code> as the primary named example anchor for that bounded corridor.
</p>

<hr/>

<h2 id="compiler-corridor-positive-mirror">10. Compiler-Corridor Positive Mirror</h2>

<p>
The conservative compiler-oriented mirror remains:
</p>

<pre><code>Examples/compiler/
├── 01_pure_arithmetic.md
├── 02_structured_control.md
└── 03_explicit_state.md</code></pre>

<p>
These examples correspond to a narrower positive corridor centered on:
</p>

<ul>
  <li><strong>pure computation</strong>,</li>
  <li><strong>structured control</strong>,</li>
  <li><strong>explicit state</strong>.</li>
</ul>

<p>
Together, they still form a useful conservative mirror of a bounded compiler-facing path.
They remain intentionally modest in scope:
</p>

<ul>
  <li><code>01_pure_arithmetic.md</code> keeps the corridor centered on direct computation,</li>
  <li><code>02_structured_control.md</code> introduces control-structure relevance without opening unrelated complexity,</li>
  <li><code>03_explicit_state.md</code> introduces explicit state and valid feedback discipline as a distinct step.</li>
</ul>

<p>
This mirror remains valuable.
However, it should no longer be read as the only coherent published example family in the repository.
It now coexists with the numbered example slices and with the first applicative vertical slice under <code>05_bounded_ui_accumulator</code>.
</p>

<hr/>

<h2 id="reading-discipline">11. Reading Discipline</h2>

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
For the first applicative executable corridor, a practical entry point is:
</p>

<pre><code>Examples/05_bounded_ui_accumulator
   -&gt;
Expression/Front panel.md
Expression/Widget.md
Expression/Widget interaction.md
Language/Control structures.md
Language/State and cycles.md
   -&gt;
IR/
   -&gt;
Profiles/ where relevant
   -&gt;
Conformance/
   -&gt;
Implementations/Reference/Runtime/</code></pre>

<p>
This prevents two common mistakes:
</p>

<ul>
  <li>treating examples as if they defined the language,</li>
  <li>reading examples in isolation and inferring unstated closure that the repository has not published.</li>
</ul>

<hr/>

<h2 id="growth-discipline">12. Growth Discipline</h2>

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
close one applicative vertical slice
   -&gt;
align conformance and reference consumption
   -&gt;
only then broaden the next example family</code></pre>

<p>
This directory should therefore grow by strengthening repository-visible corridor closure,
not by accumulating disconnected demonstrations.
</p>

<hr/>

<h2 id="summary">13. Summary</h2>

<p>
Examples are illustrative named slices of the specification.
They remain subordinate to the owning specification documents and complementary to conformance, IR, profiles, and the non-normative reference implementation workspace.
</p>

<p>
The published example surface now has two complementary forms:
</p>

<ul>
  <li>a numbered slice progression from <code>01_pure_addition</code> through <code>05_bounded_ui_accumulator</code>,</li>
  <li>and a conservative compiler-oriented positive mirror under <code>Examples/compiler/</code>.</li>
</ul>

<p>
Among these, <code>05_bounded_ui_accumulator</code> is currently the primary applicative vertical-slice anchor because it is the first bounded example that visibly combines front-panel participation, bounded iteration, explicit state, public output, and reference-runtime consumption posture in one named corridor.
</p>

<p>
Examples help make the specification readable across layers,
but they do not replace the documents that own source law, semantic law, execution-facing law, profile law, runtime-boundary law, or public conformance expectations.
</p>
