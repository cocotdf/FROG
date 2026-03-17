<p align="center">
  <img src="../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">🐸 FROG Connectivity Transition</h1>

<p align="center">
  Transition note for <strong>frog.connectivity</strong> in FROG v0.1<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-file-still-exists">2. Why this File Still Exists</a></li>
  <li><a href="#architectural-status">3. Architectural Status</a></li>
  <li><a href="#normative-home">4. Normative Home</a></li>
  <li><a href="#what-did-not-change">5. What Did Not Change</a></li>
  <li><a href="#how-to-use-this-document">6. How to Use this Document</a></li>
  <li><a href="#summary">7. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document is a <strong>transition note</strong> for the <code>frog.connectivity.*</code> namespace.
</p>

<p>
The <code>frog.connectivity.*</code> capability family remains part of the <strong>standardized FROG specification surface</strong>,
but it no longer belongs to the minimal intrinsic <code>Libraries/</code> core.
</p>

<p>
Its authoritative normative home is now the <strong>Interop profile</strong>.
</p>

<p>
Accordingly:
</p>

<ul>
  <li><code>Profiles/Interop.md</code> is the primary normative specification for <code>frog.connectivity.*</code>,</li>
  <li><code>Profiles/Readme.md</code> defines the architectural role of optional standardized capability families,</li>
  <li>this file exists only to explain why <code>Connectivity.md</code> still appears under <code>Libraries/</code>.</li>
</ul>

<p>
This document is intentionally narrow.
It is a routing and continuity note, not a second full specification.
</p>

<hr/>

<h2 id="why-this-file-still-exists">2. Why this File Still Exists</h2>

<p>
This file is retained for:
</p>

<ul>
  <li>repository continuity,</li>
  <li>navigation stability,</li>
  <li>inbound-link compatibility,</li>
  <li>architectural clarity for readers who still look for connectivity under <code>Libraries/</code>.</li>
</ul>

<p>
Its purpose is simple:
</p>

<pre>
Libraries/Connectivity.md   -> transition note
Profiles/Interop.md         -> authoritative normative specification
</pre>

<p>
This file MUST NOT be treated as a competing normative source.
</p>

<hr/>

<h2 id="architectural-status">3. Architectural Status</h2>

<p>
The move of <code>frog.connectivity.*</code> out of the intrinsic library layer is an
<strong>architectural reclassification</strong>, not a removal from FROG.
</p>

<p>
The repository now distinguishes more clearly between:
</p>

<ul>
  <li><strong>intrinsic standardized primitive vocabularies</strong> in <code>Libraries/</code>, and</li>
  <li><strong>optional standardized capability families</strong> in <code>Profiles/</code>.</li>
</ul>

<p>
That distinction can be summarized as follows:
</p>

<pre>
Intrinsic, portable, core language-facing surface
    -> Libraries/

Optional, environment-dependent, ecosystem-facing surface
    -> Profiles/
</pre>

<p>
The <code>frog.connectivity.*</code> namespace belongs to the second category.
It standardizes an interoperability capability surface that may depend on host environments,
external runtimes, shared libraries, managed platforms, or data-system assumptions.
</p>

<p>
Because of that architectural character, normative ownership now belongs to the
<strong>Interop profile</strong> rather than to the intrinsic library core.
</p>

<hr/>

<h2 id="normative-home">4. Normative Home</h2>

<p>
Within the current FROG repository architecture:
</p>

<pre>
Expression/   -> canonical source form
Language/     -> cross-cutting execution semantics
Libraries/    -> intrinsic primitive vocabularies
Profiles/     -> optional standardized capability families
IDE/          -> authoring and tooling responsibilities
</pre>

<p>
Within that architecture:
</p>

<ul>
  <li><code>Libraries/</code> owns intrinsic standardized primitive vocabularies,</li>
  <li><code>Profiles/</code> owns optional standardized capability families,</li>
  <li><code>frog.connectivity.*</code> is normatively owned by the <strong>Interop profile</strong>.</li>
</ul>

<p>
The authoritative normative home of <code>frog.connectivity.*</code> is therefore:
</p>

<pre><code>Profiles/Interop.md</code></pre>

<p>
That document MUST be treated as the primary normative source for:
</p>

<ul>
  <li>the standardized primitive catalog,</li>
  <li>primitive ports and types,</li>
  <li>validation rules,</li>
  <li>profile support and capability claims,</li>
  <li>scope boundaries for standardized interop support.</li>
</ul>

<p>
<code>frog.connectivity.*</code> MUST NOT be treated as part of the minimal intrinsic standard library core.
</p>

<hr/>

<h2 id="what-did-not-change">5. What Did Not Change</h2>

<p>
This reclassification does <strong>not</strong> rename the namespace.
</p>

<p>
The standardized namespace remains:
</p>

<pre><code>frog.connectivity.*</code></pre>

<p>
Only the <strong>architectural ownership</strong> changes.
The namespace identity remains stable.
</p>

<p>
In simple terms:
</p>

<pre>
What changed:
- normative ownership
- architectural classification

What did not change:
- namespace prefix
- primitive identifiers
- standardized existence of the capability family
</pre>

<hr/>

<h2 id="how-to-use-this-document">6. How to Use this Document</h2>

<p>
Use this file as a <strong>routing document</strong>, not as a detailed specification.
</p>

<p>
If you need to know:
</p>

<ul>
  <li>which standardized interop primitives exist,</li>
  <li>what ports and types they define,</li>
  <li>how they validate,</li>
  <li>what support claims an implementation may make,</li>
  <li>what belongs in scope or out of scope for standardized interop,</li>
</ul>

<p>
then you MUST read:
</p>

<pre><code>Profiles/Interop.md</code></pre>

<p>
This file SHOULD remain short and SHOULD NOT duplicate:
</p>

<ul>
  <li>the primitive catalog,</li>
  <li>primitive-local behavioral details,</li>
  <li>validation rules,</li>
  <li>examples already owned by the Interop profile specification,</li>
  <li>profile-support or capability-claim rules defined there.</li>
</ul>

<p>
If future revisions modify the standardized interop surface, those changes MUST be made in
<code>Profiles/Interop.md</code>, not here.
</p>

<p>
If a later repository phase makes this transition note unnecessary, it MAY be reduced further or removed,
once continuity and navigation concerns are no longer relevant.
</p>

<hr/>

<h2 id="summary">7. Summary</h2>

<p>
The <code>frog.connectivity.*</code> namespace remains part of the standardized FROG specification surface,
but it is now owned by the <strong>Interop profile</strong> rather than by the intrinsic library layer.
</p>

<p>
In short:
</p>

<ul>
  <li><code>Libraries/</code> owns intrinsic standardized primitive vocabularies,</li>
  <li><code>Profiles/</code> owns optional standardized capability families,</li>
  <li><code>frog.connectivity.*</code> remains stable as a namespace,</li>
  <li><code>Profiles/Interop.md</code> is the authoritative normative specification,</li>
  <li>this file remains only as a transition and continuity note.</li>
</ul>

<p>
Decision sketch:
</p>

<pre>
Need the detailed interop specification?
        |
        v
Go to Profiles/Interop.md

Need to understand why Connectivity still appears under Libraries/?
        |
        v
Read this transition note
</pre>
