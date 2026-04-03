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
  <li><a href="#relation-with-ir-and-profiles">6. Relation with IR and Profiles</a></li>
  <li><a href="#published-example-families">7. Published Example Families</a></li>
  <li><a href="#compiler-corridor-positive-mirror">8. Compiler-Corridor Positive Mirror</a></li>
  <li><a href="#summary">9. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory provides illustrative named slices of the published FROG specification.
</p>

<p>
Examples are intended to make the specification easier to read, easier to compare, and easier to discuss across layers without turning prose alone into the only reading surface.
</p>

<hr/>

<h2 id="why-this-directory-exists">2. Why This Directory Exists</h2>

<p>
A specification stack becomes easier to understand when readers can see small named slices that correspond to recognizable architectural situations.
</p>

<p>
Examples therefore exist to:
</p>

<ul>
  <li>illustrate published structures,</li>
  <li>illustrate published semantic boundaries,</li>
  <li>illustrate published IR consequences,</li>
  <li>illustrate declared profile corridors where relevant.</li>
</ul>

<hr/>

<h2 id="what-examples-are">3. What Examples Are</h2>

<p>
Examples are illustrative repository-visible slices.
They may be small, focused, named, and architecture-oriented.
</p>

<p>
An example may illustrate:
</p>

<ul>
  <li>a source shape,</li>
  <li>a semantic pattern,</li>
  <li>a control pattern,</li>
  <li>a state pattern,</li>
  <li>a declared profile corridor.</li>
</ul>

<hr/>

<h2 id="what-examples-are-not">4. What Examples Are Not</h2>

<p>
Examples do not become hidden semantic law.
</p>

<p>
The rule remains:
</p>

<pre><code>Specification defines
Conformance tests
Examples illustrate</code></pre>

<p>
An example therefore does not replace the owning documents in:
</p>

<ul>
  <li><code>Expression/</code>,</li>
  <li><code>Language/</code>,</li>
  <li><code>Libraries/</code>,</li>
  <li><code>IR/</code>,</li>
  <li><code>Profiles/</code>.</li>
</ul>

<hr/>

<h2 id="relation-with-conformance">5. Relation with Conformance</h2>

<p>
Examples and conformance are related but distinct.
</p>

<ul>
  <li>Examples illustrate named slices.</li>
  <li>Conformance exposes accept / reject / preserve truth.</li>
</ul>

<p>
A useful reading model is:
</p>

<pre><code>example slice
   -&gt;
conformance case
   -&gt;
IR / profile reading where relevant</code></pre>

<hr/>

<h2 id="relation-with-ir-and-profiles">6. Relation with IR and Profiles</h2>

<p>
Examples may mirror:
</p>

<ul>
  <li>core source / semantic slices,</li>
  <li>IR-relevant slices,</li>
  <li>profile-relevant slices.</li>
</ul>

<p>
Where a declared compiler corridor is involved, examples should remain bounded and conservative.
</p>

<hr/>

<h2 id="published-example-families">7. Published Example Families</h2>

<p>
The first coherent example growth should remain small and architecture-first.
</p>

<p>
A suitable first family is the positive compiler-corridor mirror for the conservative <code>native_cpu_llvm</code> route.
</p>

<hr/>

<h2 id="compiler-corridor-positive-mirror">8. Compiler-Corridor Positive Mirror</h2>

<p>
The initial positive mirror is:
</p>

<pre><code>Examples/compiler/
01_pure_arithmetic.md
02_structured_control.md
03_explicit_state.md</code></pre>

<p>
These examples correspond to the first named positive conformance corridor:
</p>

<ul>
  <li>pure computation,</li>
  <li>structured control,</li>
  <li>explicit state.</li>
</ul>

<hr/>

<h2 id="summary">9. Summary</h2>

<p>
Examples are illustrative named slices of the specification.
They remain subordinate to the owning spec documents and complementary to conformance.
</p>

<p>
The first coherent mirror to open is the positive compiler corridor for the conservative <code>native_cpu_llvm</code> route.
</p>
