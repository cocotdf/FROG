<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG IR Lowering</h1>

<p align="center">
  <strong>Normative lowering boundary and transformation rules for execution-facing IR in FROG v0.1</strong><br/>
  FROG — Free Open Graphical Language
</p>

<hr/>

<h2>Contents</h2>
<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#boundary-contract">2. Boundary Contract</a></li>
  <li><a href="#position-in-the-pipeline">3. Position in the Pipeline</a></li>
  <li><a href="#scope">4. Scope</a></li>
  <li><a href="#non-goals">5. Non-Goals</a></li>
  <li><a href="#what-lowering-means-in-frog">6. What Lowering Means</a></li>
  <li><a href="#lowering-boundary">7. Lowering Boundary</a></li>
  <li><a href="#minimum-preconditions">8. Preconditions</a></li>
  <li><a href="#lowering-stages">9. Lowering Stages</a></li>
  <li><a href="#core-invariants">10. Core Invariants</a></li>
  <li><a href="#preservation-obligations">11. Preservation Obligations</a></li>
  <li><a href="#allowed-transformations">12. Allowed Transformations</a></li>
  <li><a href="#forbidden-transformations">13. Forbidden Transformations</a></li>
  <li><a href="#key-domains">14. Key Transformation Domains</a></li>
  <li><a href="#mapping-and-attribution">15. Mapping and Attribution</a></li>
  <li><a href="#observability">16. Observability and Diagnostics</a></li>
  <li><a href="#conceptual-products">17. Conceptual Lowered Products</a></li>
  <li><a href="#minimal-shape">18. Minimal Conceptual Shape</a></li>
  <li><a href="#out-of-scope">19. Out of Scope</a></li>
  <li><a href="#summary">20. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the normative architectural boundary called <strong>lowering</strong> in FROG v0.1.
</p>

<p>
Lowering begins <strong>after</strong> the construction of an open Execution IR from validated program meaning.
It transforms that IR into more target-oriented forms while preserving semantic truth and recoverability.
</p>

<pre><code>validated program meaning
        |
        v
open Execution IR
        |
        v
lowering
        |
        v
specialized forms
        |
        v
backend contract / private realization
</code></pre>

<p>
Lowering is therefore a <strong>specialization space</strong>, not a redefinition of the language or IR.
</p>

<hr/>

<h2 id="boundary-contract">2. Boundary Contract</h2>

<p>
Lowering introduces specialization but MUST preserve:
</p>

<ul>
  <li>validated semantic meaning,</li>
  <li>recoverable attribution,</li>
  <li>explicit state semantics,</li>
  <li>boundary distinctions,</li>
  <li>execution dependency meaning.</li>
</ul>

<p>
Lowering MUST NOT:
</p>

<ul>
  <li>redefine language semantics,</li>
  <li>repair invalid programs silently,</li>
  <li>collapse required distinctions irreversibly,</li>
  <li>present backend-private forms as normative FROG meaning.</li>
</ul>

<hr/>

<h2 id="position-in-the-pipeline">3. Position in the Pipeline</h2>

<pre><code>Expression/
        |
        v
validated program meaning
        |
        v
Execution IR
        |
        v
Lowering
        |
        +-- backend-oriented forms
        |
        +-- backend contract
        |
        +-- runtime-private realization
</code></pre>

<p>
Key rule:
</p>

<ul>
  <li>Execution IR = open, inspectable</li>
  <li>Lowering = specialization</li>
  <li>Backend contract = explicit handoff</li>
  <li>Runtime = private realization</li>
</ul>

<hr/>

<h2 id="scope">4. Scope</h2>

<p>
This document defines:
</p>

<ul>
  <li>the lowering boundary,</li>
  <li>allowed transformation categories,</li>
  <li>mandatory preservation rules,</li>
  <li>forbidden transformations.</li>
</ul>

<hr/>

<h2 id="non-goals">5. Non-Goals</h2>

<p>
This document does NOT define:
</p>

<ul>
  <li>one compiler architecture,</li>
  <li>one IR format after lowering,</li>
  <li>one scheduler model,</li>
  <li>one ABI,</li>
  <li>one runtime representation.</li>
</ul>

<hr/>

<h2 id="what-lowering-means-in-frog">6. What Lowering Means</h2>

<p>
Lowering is the transformation of open IR into forms closer to execution realization.
</p>

<p>
Typical goals:
</p>

<ul>
  <li>data layout concretization,</li>
  <li>control flattening or specialization,</li>
  <li>memory materialization,</li>
  <li>interface binding,</li>
  <li>execution planning.</li>
</ul>

<hr/>

<h2 id="lowering-boundary">7. Lowering Boundary</h2>

<pre><code>OPEN ZONE
---------
Execution IR
  - structured
  - attributable
  - portable

LOWERING
---------
specialization begins

SPECIALIZED ZONE
----------------
lowered forms
  - target-oriented
  - less source-shaped
  - possibly backend-specific
</code></pre>

<hr/>

<h2 id="minimum-preconditions">8. Preconditions</h2>

<p>
Lowering requires a fully validated program.
</p>

<p>
Lowering MUST NOT:
</p>

<ul>
  <li>fix invalid graphs,</li>
  <li>inject hidden semantics,</li>
  <li>legalize invalid cycles.</li>
</ul>

<hr/>

<h2 id="lowering-stages">9. Lowering Stages</h2>

<h3>Stage A — IR-conservative</h3>
<ul>
  <li>still close to IR</li>
  <li>adds explicit execution details</li>
</ul>

<h3>Stage B — backend-oriented</h3>
<ul>
  <li>target specialization</li>
  <li>layout, scheduling, ABI</li>
</ul>

<h3>Stage C — runtime-private</h3>
<ul>
  <li>scheduler graph</li>
  <li>compiled artifacts</li>
</ul>

<hr/>

<h2 id="core-invariants">10. Core Invariants</h2>

<ul>
  <li>semantic equivalence MUST hold</li>
  <li>attribution MUST remain recoverable</li>
  <li>explicit memory MUST remain explicit</li>
  <li>boundaries MUST remain distinguishable</li>
</ul>

<hr/>

<h2 id="preservation-obligations">11. Preservation Obligations</h2>

<p>
Lowering MUST preserve:
</p>

<ul>
  <li>dependency semantics,</li>
  <li>control semantics,</li>
  <li>state semantics,</li>
  <li>boundary roles,</li>
  <li>source attribution.</li>
</ul>

<p>
No semantic laundering is allowed.
</p>

<hr/>

<h2 id="allowed-transformations">12. Allowed Transformations</h2>

<ul>
  <li>structure → lower control (branch, loop machine)</li>
  <li>interface → ABI binding</li>
  <li>memory → buffers / registers</li>
  <li>partitioning → threads / devices</li>
  <li>scheduling → ordering / clustering</li>
</ul>

<hr/>

<h2 id="forbidden-transformations">13. Forbidden Transformations</h2>

<ul>
  <li>semantic change</li>
  <li>hidden state insertion</li>
  <li>boundary collapse</li>
  <li>loss of attribution</li>
  <li>invalid program repair</li>
</ul>

<hr/>

<h2 id="key-domains">14. Key Transformation Domains</h2>

<ul>
  <li>control structures</li>
  <li>state and memory</li>
  <li>interfaces and UI</li>
  <li>data layout</li>
  <li>scheduling and placement</li>
</ul>

<hr/>

<h2 id="mapping-and-attribution">15. Mapping and Attribution</h2>

<p>
Lowering expands objects:
</p>

<pre><code>IR object
   -&gt; multiple lowered objects
</code></pre>

<p>
Must preserve:
</p>

<ul>
  <li>origin IR object</li>
  <li>semantic origin</li>
  <li>transformation type (split, merge, generated)</li>
</ul>

<hr/>

<h2 id="observability">16. Observability and Diagnostics</h2>

<p>
Lowering MUST remain compatible with:
</p>

<ul>
  <li>source-level debugging</li>
  <li>traceability</li>
  <li>fault attribution</li>
</ul>

<p>
Rule:
</p>

<pre><code>internal complexity allowed
loss of diagnosability forbidden
</code></pre>

<hr/>

<h2 id="conceptual-products">17. Conceptual Lowered Products</h2>

<ul>
  <li>control form</li>
  <li>state form</li>
  <li>interface form</li>
  <li>storage form</li>
  <li>placement form</li>
  <li>schedule form</li>
</ul>

<hr/>

<h2 id="minimal-shape">18. Minimal Conceptual Shape</h2>

<pre><code>{
  "kind": "lowered_form",
  "target_family": "...",
  "objects": [],
  "connections": [],
  "mapping": {}
}
</code></pre>

<hr/>

<h2 id="out-of-scope">19. Out of Scope</h2>

<ul>
  <li>one universal IR after lowering</li>
  <li>one runtime model</li>
  <li>one scheduler</li>
  <li>one ABI</li>
</ul>

<hr/>

<h2 id="summary">20. Summary</h2>

<p>
Lowering is the specialization boundary after open Execution IR.
</p>

<p>
It:
</p>

<ul>
  <li>adapts IR for execution,</li>
  <li>preserves semantic truth,</li>
  <li>preserves attribution,</li>
  <li>does not redefine the language.</li>
</ul>

<pre><code>open Execution IR
        |
        v
lowering
        |
        v
specialized execution forms
</code></pre>
