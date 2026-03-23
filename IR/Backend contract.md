<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG IR Backend Contract</h1>

<p align="center">
  <strong>Normative consumption contract for lowered execution forms in FROG v0.1</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#role">2. Role of the Backend Contract</a></li>
  <li><a href="#position">3. Position in the Pipeline</a></li>
  <li><a href="#scope">4. Scope</a></li>
  <li><a href="#non-goals">5. Non-Goals</a></li>
  <li><a href="#definition">6. Core Definition</a></li>
  <li><a href="#boundary">7. Contract Boundary</a></li>
  <li><a href="#preconditions">8. Preconditions</a></li>
  <li><a href="#identity">9. Contract Identity and Backend Family</a></li>
  <li><a href="#structure">10. Required Contract Structure</a></li>
  <li><a href="#producer">11. Producer Obligations</a></li>
  <li><a href="#consumer">12. Consumer Obligations</a></li>
  <li><a href="#invariants">13. Preservation Invariants</a></li>
  <li><a href="#semantics">14. Control, State, and Boundaries</a></li>
  <li><a href="#ui">15. UI Participation</a></li>
  <li><a href="#diagnostics">16. Diagnostics and Observability</a></li>
  <li><a href="#profiles">17. Relation with Profiles and Libraries</a></li>
  <li><a href="#shape">18. Minimal Conceptual Shape</a></li>
  <li><a href="#lifecycle">19. Contract Lifecycle</a></li>
  <li><a href="#out-of-scope">20. Out of Scope</a></li>
  <li><a href="#summary">21. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the <strong>backend contract</strong> for FROG v0.1.
</p>

<p>
It is the first standardized <strong>consumer-facing boundary</strong> after lowering.
It defines what a backend may rely on when consuming a lowered execution form.
</p>

<pre><code>Execution IR
      |
      v
Lowering
      |
      v
Backend Contract
      |
      v
Private realization
</code></pre>

<hr/>

<h2 id="role">2. Role of the Backend Contract</h2>

<p>
The backend contract provides a stable handoff between:
</p>

<ul>
  <li>specialized lowered representations,</li>
  <li>backend or runtime consumers.</li>
</ul>

<p>
It ensures:
</p>

<ul>
  <li>explicit assumptions,</li>
  <li>explicit obligations,</li>
  <li>explicit preserved semantics.</li>
</ul>

<p>
It prevents:
</p>

<ul>
  <li>implicit backend assumptions,</li>
  <li>semantic drift,</li>
  <li>loss of diagnosability.</li>
</ul>

<hr/>

<h2 id="position">3. Position in the Pipeline</h2>

<pre><code>canonical source
      |
      v
validated meaning
      |
      v
Execution IR
      |
      v
Lowering
      |
      v
Backend Contract
      |
      v
backend / runtime
</code></pre>

<p>
The backend contract is:
</p>

<ul>
  <li>downstream from lowering,</li>
  <li>upstream from private realization.</li>
</ul>

<hr/>

<h2 id="scope">4. Scope</h2>

<p>
This document defines:
</p>

<ul>
  <li>the contract boundary,</li>
  <li>required information for consumption,</li>
  <li>producer and consumer obligations,</li>
  <li>preserved execution semantics.</li>
</ul>

<hr/>

<h2 id="non-goals">5. Non-Goals</h2>

<p>
This document does NOT define:
</p>

<ul>
  <li>one ABI,</li>
  <li>one scheduler model,</li>
  <li>one runtime architecture,</li>
  <li>one binary or transport format.</li>
</ul>

<hr/>

<h2 id="definition">6. Core Definition</h2>

<p>
A backend contract is a <strong>declarative consumption boundary</strong>.
</p>

<p>
It specifies:
</p>

<ul>
  <li>what is executable,</li>
  <li>what assumptions are fixed,</li>
  <li>what must be preserved,</li>
  <li>what must be rejected.</li>
</ul>

<p>
It is not the execution itself.
It is the <strong>agreement before execution</strong>.
</p>

<hr/>

<h2 id="boundary">7. Contract Boundary</h2>

<pre><code>Execution IR  → open, structured
Lowering      → specialization
Backend Contract → explicit assumptions
Runtime       → private realization
</code></pre>

<p>
At this boundary:
</p>

<ul>
  <li>assumptions become explicit,</li>
  <li>consumer expectations become defined.</li>
</ul>

<hr/>

<h2 id="preconditions">8. Preconditions</h2>

<p>
A backend contract requires:
</p>

<ul>
  <li>validated program,</li>
  <li>semantically correct IR,</li>
  <li>valid lowering.</li>
</ul>

<p>
It MUST NOT hide:
</p>

<ul>
  <li>invalid programs,</li>
  <li>invalid cycles,</li>
  <li>broken semantics.</li>
</ul>

<hr/>

<h2 id="identity">9. Contract Identity and Backend Family</h2>

<p>
Each contract MUST declare:
</p>

<ul>
  <li>contract kind,</li>
  <li>version,</li>
  <li>backend family.</li>
</ul>

<p>
Backend family defines:
</p>

<ul>
  <li>execution assumptions,</li>
  <li>target class,</li>
  <li>consumption expectations.</li>
</ul>

<hr/>

<h2 id="structure">10. Required Contract Structure</h2>

<p>
A contract MUST contain:
</p>

<ul>
  <li>header (identity),</li>
  <li>assumptions,</li>
  <li>executable units,</li>
  <li>boundaries,</li>
  <li>state representation,</li>
  <li>placement/scheduling if fixed,</li>
  <li>attribution metadata,</li>
  <li>unsupported features.</li>
</ul>

<hr/>

<h2 id="producer">11. Producer Obligations</h2>

<p>
The producer MUST:
</p>

<ul>
  <li>preserve semantics,</li>
  <li>declare assumptions,</li>
  <li>preserve attribution,</li>
  <li>explicitly declare unsupported features.</li>
</ul>

<p>
The producer MUST NOT:
</p>

<ul>
  <li>hide semantic changes,</li>
  <li>erase memory semantics,</li>
  <li>collapse boundaries improperly.</li>
</ul>

<hr/>

<h2 id="consumer">12. Consumer Obligations</h2>

<p>
The consumer MUST:
</p>

<ul>
  <li>either accept or reject the contract,</li>
  <li>respect declared assumptions,</li>
  <li>preserve semantics.</li>
</ul>

<p>
The consumer MUST NOT:
</p>

<ul>
  <li>reinterpret assumptions,</li>
  <li>erase attribution,</li>
  <li>change execution meaning.</li>
</ul>

<hr/>

<h2 id="invariants">13. Preservation Invariants</h2>

<ul>
  <li>semantic equivalence MUST hold</li>
  <li>state MUST remain explicit</li>
  <li>boundaries MUST remain identifiable</li>
  <li>diagnostics MUST remain possible</li>
</ul>

<hr/>

<h2 id="semantics">14. Control, State, and Boundaries</h2>

<p>
Lowering may transform representation, but MUST preserve:
</p>

<ul>
  <li>control semantics,</li>
  <li>state semantics,</li>
  <li>boundary meaning.</li>
</ul>

<p>
Explicit memory MUST remain explicit.
</p>

<hr/>

<h2 id="ui">15. UI Participation</h2>

<p>
If UI is supported:
</p>

<ul>
  <li>widget_value and widget_reference MUST remain distinct,</li>
  <li>UI interaction MUST remain attributable.</li>
</ul>

<p>
No universal UI execution model is defined.
</p>

<hr/>

<h2 id="diagnostics">16. Diagnostics and Observability</h2>

<p>
The contract MUST allow:
</p>

<ul>
  <li>source mapping,</li>
  <li>fault attribution,</li>
  <li>debug support.</li>
</ul>

<p>
Rule:
</p>

<pre><code>internal complexity allowed
loss of diagnosability forbidden
</code></pre>

<hr/>

<h2 id="profiles">17. Relation with Profiles and Libraries</h2>

<ul>
  <li>Libraries define primitives</li>
  <li>Profiles define capabilities</li>
</ul>

<p>
The contract MAY require them but MUST NOT redefine them.
</p>

<hr/>

<h2 id="shape">18. Minimal Conceptual Shape</h2>

<pre><code>{
  "kind": "frog_backend_contract",
  "version": "0.1",
  "backend_family": "...",
  "assumptions": {},
  "units": [],
  "mapping": {},
  "unsupported": []
}
</code></pre>

<hr/>

<h2 id="lifecycle">19. Contract Lifecycle</h2>

<pre><code>lowering
   → backend contract
       → accepted → execution
       → rejected → incompatibility
</code></pre>

<hr/>

<h2 id="out-of-scope">20. Out of Scope</h2>

<ul>
  <li>universal ABI</li>
  <li>runtime model</li>
  <li>binary format</li>
  <li>event system</li>
</ul>

<hr/>

<h2 id="summary">21. Summary</h2>

<p>
The backend contract is the standardized consumption boundary of FROG.
</p>

<p>
It:
</p>

<ul>
  <li>declares assumptions,</li>
  <li>preserves semantics,</li>
  <li>enables safe execution.</li>
</ul>

<pre><code>Execution IR
      |
      v
Lowering
      |
      v
Backend Contract
      |
      v
Runtime
</code></pre>
