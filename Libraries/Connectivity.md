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
  <li><a href="#architectural-reclassification">3. Architectural Reclassification</a></li>
  <li><a href="#normative-home">4. Normative Home of <code>frog.connectivity</code></a></li>
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
The <code>frog.connectivity.*</code> primitive family remains part of the FROG specification, but its
normative architectural home is no longer the intrinsic <code>Libraries/</code> layer.
</p>

<p>
The authoritative normative specification for this namespace is now defined in:
</p>

<ul>
  <li><code>Profiles/Interop.md</code> — authoritative normative specification for the Interop profile primitive surface,</li>
  <li><code>Profiles/Readme.md</code> — architectural definition of optional standardized capability families.</li>
</ul>

<p>
This file exists to make that transition explicit and easy to understand.
It is intentionally short.
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
In other words, this file remains here so that readers can quickly understand that:
</p>

<pre>
Libraries/Connectivity.md   -> transition note
Profiles/Interop.md        -> normative specification
</pre>

<p>
This document is therefore <strong>not</strong> a second full specification.
It is a redirection document with explicit architectural meaning.
</p>

<hr/>

<h2 id="architectural-reclassification">3. Architectural Reclassification</h2>

<p>
The change is not a removal of <code>frog.connectivity.*</code> from FROG.
It is an <strong>architectural reclassification</strong>.
</p>

<p>
The repository now distinguishes more clearly between:
</p>

<ul>
  <li><strong>intrinsic standard primitive vocabularies</strong> in <code>Libraries/</code>, and</li>
  <li><strong>optional standardized capability families</strong> in <code>Profiles/</code>.</li>
</ul>

<p>
That distinction can be summarized as follows:
</p>

<pre>
Intrinsic, portable, always-language-facing surface
    -> Libraries/

Optional, environment-dependent, ecosystem-facing capability surface
    -> Profiles/
</pre>

<p>
The <code>frog.connectivity.*</code> namespace defines an interoperability capability surface for interaction with:
</p>

<ul>
  <li>foreign runtimes,</li>
  <li>native or shared libraries,</li>
  <li>managed platforms,</li>
  <li>SQL-capable data systems.</li>
</ul>

<p>
Because this capability surface depends on broader environment assumptions, it is now owned by the
<strong>Interop profile</strong> rather than by the intrinsic library core.
</p>

<p>
This keeps <code>Libraries/</code> focused on intrinsic, portable primitive vocabularies and avoids turning
the intrinsic library layer into a catch-all container for external ecosystem integration.
</p>

<hr/>

<h2 id="normative-home">4. Normative Home of <code>frog.connectivity</code></h2>

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
Accordingly:
</p>

<ul>
  <li><code>Libraries/</code> owns intrinsic standard primitive vocabularies,</li>
  <li><code>Profiles/</code> owns optional standardized capability families,</li>
  <li><code>frog.connectivity.*</code> is normatively owned by the <strong>Interop profile</strong>.</li>
</ul>

<p>
The authoritative normative home of <code>frog.connectivity.*</code> is therefore:
</p>

<pre><code>Profiles/Interop.md</code></pre>

<p>
It MUST be treated as the primary normative specification for:
</p>

<ul>
  <li>primitive catalog definition,</li>
  <li>primitive ports,</li>
  <li>typing rules,</li>
  <li>validation rules,</li>
  <li>capability claims,</li>
  <li>scope boundaries for standardized interop support.</li>
</ul>

<p>
<code>frog.connectivity.*</code> MUST NOT be treated as part of the minimal intrinsic standard library core.
</p>

<hr/>

<h2 id="what-did-not-change">5. What Did Not Change</h2>

<p>
This architectural reclassification does <strong>not</strong> rename the standardized primitive identifiers.
</p>

<p>
The namespace remains:
</p>

<pre><code>frog.connectivity.*</code></pre>

<p>
Examples:
</p>

<ul>
  <li><code>frog.connectivity.python.call_text</code></li>
  <li><code>frog.connectivity.python.call_bytes</code></li>
  <li><code>frog.connectivity.native.call_bytes</code></li>
  <li><code>frog.connectivity.dotnet.call_text</code></li>
  <li><code>frog.connectivity.sql.query_text</code></li>
  <li><code>frog.connectivity.sql.execute</code></li>
</ul>

<p>
Only the <strong>architectural ownership</strong> changes.
The namespace identity itself remains stable.
</p>

<p>
This can be summarized simply:
</p>

<pre>
What changed:
- normative ownership
- architectural classification

What did not change:
- namespace prefix
- primitive identifiers
- FROG-level existence of the capability family
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
  <li>what their ports are,</li>
  <li>how they are typed,</li>
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
  <li>the detailed primitive catalog,</li>
  <li>behavioral rules,</li>
  <li>validation details,</li>
  <li>examples already owned by the Interop profile specification,</li>
  <li>profile support or capability-claim rules already defined there.</li>
</ul>

<p>
If future updates modify the standardized interop surface, those updates MUST be made in
<code>Profiles/Interop.md</code> rather than here.
</p>

<p>
If a later repository phase makes this transition note unnecessary, it MAY be reduced further or removed
once continuity and navigation concerns are no longer relevant.
</p>

<hr/>

<h2 id="summary">7. Summary</h2>

<p>
The <code>frog.connectivity.*</code> namespace remains part of the FROG specification, but it is now owned by the
<strong>Interop profile</strong> rather than by the intrinsic library layer.
</p>

<p>
In short:
</p>

<ul>
  <li><code>Libraries/</code> owns intrinsic standard primitive vocabularies,</li>
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

Need to understand why Connectivity is still listed under Libraries/?
        |
        v
Read this transition note
</pre>
