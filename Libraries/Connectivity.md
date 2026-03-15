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
  <li><a href="#status-of-this-document">2. Status of this Document</a></li>
  <li><a href="#normative-home">3. Normative Home of <code>frog.connectivity</code></a></li>
  <li><a href="#namespace-continuity">4. Namespace Continuity</a></li>
  <li><a href="#transition-guidance">5. Transition Guidance</a></li>
  <li><a href="#summary">6. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document is a transition note for the <code>frog.connectivity</code> namespace.
</p>

<p>
The <code>frog.connectivity.*</code> primitive family remains part of the FROG specification, but its
normative architectural home is no longer the intrinsic <code>Libraries/</code> layer.
</p>

<p>
The detailed normative specification for this namespace is defined in:
</p>

<ul>
  <li><code>Profiles/Interop.md</code> — for the Interop profile primitive catalog, and</li>
  <li><code>Profiles/Readme.md</code> — for the architectural role of optional standardized capability families.</li>
</ul>

<hr/>

<h2 id="status-of-this-document">2. Status of this Document</h2>

<p>
This file is retained temporarily for repository continuity, navigation stability, and inbound links.
</p>

<p>
This document is <strong>not</strong> the primary normative specification for <code>frog.connectivity.*</code>.
</p>

<p>
Implementations, tooling, and future repository work MUST treat <code>Profiles/Interop.md</code> as the
authoritative normative source for the standardized <code>frog.connectivity.*</code> primitive family.
</p>

<hr/>

<h2 id="normative-home">3. Normative Home of <code>frog.connectivity</code></h2>

<p>
Within the FROG repository architecture:
</p>

<ul>
  <li><code>Libraries/</code> owns intrinsic standard primitive vocabularies,</li>
  <li><code>Profiles/</code> owns optional standardized capability families.</li>
</ul>

<p>
The <code>frog.connectivity.*</code> namespace defines an optional interoperability capability surface
for interaction with foreign runtimes, native or shared libraries, managed platforms, and SQL-capable
data sources.
</p>

<p>
Accordingly, <code>frog.connectivity.*</code> belongs to the <strong>Interop profile</strong> and is
normatively specified in <code>Profiles/Interop.md</code>.
</p>

<hr/>

<h2 id="namespace-continuity">4. Namespace Continuity</h2>

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
Only the architectural ownership changes.
The primitive identifiers themselves remain stable.
</p>

<hr/>

<h2 id="transition-guidance">5. Transition Guidance</h2>

<p>
Readers looking for the actual primitive definitions, ports, typing rules, validation rules, and
scope of standardized interop support MUST use <code>Profiles/Interop.md</code>.
</p>

<p>
This file SHOULD remain short and SHOULD NOT duplicate the detailed primitive catalog, behavioral
rules, examples, or future-scope discussion already owned by the Interop profile specification.
</p>

<p>
If future updates modify the standardized interop surface, those updates MUST be made in
<code>Profiles/Interop.md</code> rather than here.
</p>

<hr/>

<h2 id="summary">6. Summary</h2>

<p>
The <code>frog.connectivity.*</code> namespace remains part of the FROG specification, but it is now
owned by the <strong>Interop profile</strong> rather than by the intrinsic library layer.
</p>

<p>
In short:
</p>

<ul>
  <li><code>Libraries/</code> owns intrinsic standard primitive vocabularies,</li>
  <li><code>Profiles/</code> owns optional standardized capability families,</li>
  <li><code>frog.connectivity.*</code> remains stable as a namespace,</li>
  <li><code>Profiles/Interop.md</code> is the authoritative normative specification.</li>
</ul>
