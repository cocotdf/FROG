<p align="center">
  <img src="../../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Default Realization Examples</h1>

<p align="center">
  <strong>Normative example-corridor posture for the official <code>Default</code> widget realization family</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#why-this-directory-exists">2. Why this Directory Exists</a></li>
  <li><a href="#scope">3. Scope</a></li>
  <li><a href="#what-an-example-must-prove">4. What an Example Must Prove</a></li>
  <li><a href="#relationship-with-other-default-family-documents">5. Relationship with Other Default-Family Documents</a></li>
  <li><a href="#required-example-layers">6. Required Example Layers</a></li>
  <li><a href="#example-directory-posture">7. Example Directory Posture</a></li>
  <li><a href="#button-example-posture">8. Button Example Posture</a></li>
  <li><a href="#portability-posture">9. Portability Posture</a></li>
  <li><a href="#validation-posture">10. Validation Posture</a></li>
  <li><a href="#anti-patterns">11. Anti-Patterns</a></li>
  <li><a href="#summary">12. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This directory defines the normative example-corridor posture for the official <code>Default</code> realization family.
</p>

<p>
Its purpose is to ensure that published examples reinforce the realization architecture rather than quietly replacing it with undocumented conventions.
</p>

<p>
An example in this directory is not merely illustrative prose.
It is part of the inspectable publication corridor that links:
</p>

<ul>
  <li>realization doctrine,</li>
  <li>machine-readable realization publication,</li>
  <li>concrete asset-tree organization,</li>
  <li>portable runtime interpretation.</li>
</ul>

<hr/>

<h2 id="why-this-directory-exists">2. Why this Directory Exists</h2>

<p>
A realization family may look coherent at the doctrinal level while still remaining ambiguous at the publication level.
That ambiguity usually appears in the examples first.
</p>

<p>
Without a normalized example corridor:
</p>

<ul>
  <li>machine-readable packages drift away from the doctrinal wording,</li>
  <li>asset trees become private conventions instead of inspectable publication artifacts,</li>
  <li>dynamic public text may accidentally collapse into SVG ownership,</li>
  <li>runtime implementations begin to define the real behavior of the system by convention,</li>
  <li>future contributors cannot tell whether a pattern is normative, optional, or accidental.</li>
</ul>

<p>
This directory exists to prevent that drift.
</p>

<hr/>

<h2 id="scope">3. Scope</h2>

<p>
This document defines:
</p>

<ul>
  <li>the role of examples in the <code>Default</code> realization family,</li>
  <li>the minimum publication layers that a realization example should show,</li>
  <li>how example prose, machine-readable JSON, and asset trees should align,</li>
  <li>the portability posture expected from example material.</li>
</ul>

<p>
This document does not define:
</p>

<ul>
  <li>widget class law,</li>
  <li>generic realization doctrine,</li>
  <li>the full generic <code>.wfrog</code> specification,</li>
  <li>one mandatory runtime implementation,</li>
  <li>the visual design details of every shipped SVG resource.</li>
</ul>

<hr/>

<h2 id="what-an-example-must-prove">4. What an Example Must Prove</h2>

<p>
A published example in this directory SHOULD prove at least the following:
</p>

<ul>
  <li>which standardized widget class is being targeted,</li>
  <li>which official realization family is being published,</li>
  <li>which parts are realized as visual resource layers,</li>
  <li>which parts are realized through placement-support resources such as anchors or text regions,</li>
  <li>which states are published explicitly,</li>
  <li>which fallbacks are published explicitly,</li>
  <li>how the asset tree corresponds to the machine-readable resource records,</li>
  <li>how a runtime can implement the realization without becoming the semantic owner of the widget.</li>
</ul>

<p>
An example that does not make these boundaries legible is incomplete even if its JSON is syntactically valid.
</p>

<hr/>

<h2 id="relationship-with-other-default-family-documents">5. Relationship with Other Default-Family Documents</h2>

<p>
The example corridor is subordinate to the architectural and doctrinal layers above it.
</p>

<p>
In particular:
</p>

<ul>
  <li><code>Libraries/Realizations/Default/Readme.md</code> defines the family-level posture,</li>
  <li><code>Libraries/Realizations/Default/Package.md</code> defines the machine-readable publication posture,</li>
  <li><code>Libraries/Realizations/Default/Resource model.md</code> defines how realization resources are described,</li>
  <li><code>Libraries/Realizations/Default/State mapping.md</code> defines how state-sensitive realization resources are mapped,</li>
  <li><code>Libraries/Realizations/Default/Assets/Readme.md</code> defines the asset-tree posture,</li>
  <li><code>Libraries/Realizations/Default/Assets/Naming.md</code> defines the naming posture.</li>
</ul>

<p>
Examples in this directory must align with those documents.
They must not silently introduce a second architecture.
</p>

<hr/>

<h2 id="required-example-layers">6. Required Example Layers</h2>

<p>
A coherent realization example SHOULD include, either directly or through clearly paired files:
</p>

<ul>
  <li>a prose explanation of the example and its architectural intent,</li>
  <li>a machine-readable <code>.wfrog</code> realization package example,</li>
  <li>a simulated or concrete asset tree,</li>
  <li>enough resource naming and placement information to show how dynamic public surfaces are realized portably.</li>
</ul>

<p>
For small examples, these layers may be split across multiple files in the same example corridor.
The important point is that the files reinforce one another rather than contradicting one another.
</p>

<hr/>

<h2 id="example-directory-posture">7. Example Directory Posture</h2>

<p>
The recommended posture for this directory is:
</p>

<pre><code>Libraries/Realizations/Default/Examples/
  Readme.md
  Button default realization.wfrog.md
  Button package and assets example.md
  ButtonPackage/
    default_button_realization.wfrog.json
    assets/
      ...
</code></pre>

<p>
In this posture:
</p>

<ul>
  <li>the example prose explains what is being demonstrated,</li>
  <li>the JSON file shows the machine-readable publication,</li>
  <li>the asset subtree shows how the resources are concretely organized,</li>
  <li>the three layers remain inspectable as one coherent publication unit.</li>
</ul>

<hr/>

<h2 id="button-example-posture">8. Button Example Posture</h2>

<p>
The button example is the first normative reference pattern for this directory.
It is intentionally small, but it must already show the most important separation in the realization corridor.
</p>

<p>
For the standard default button example:
</p>

<ul>
  <li><code>face</code> is a state-sensitive visual part and therefore uses state-mapped visual resources,</li>
  <li><code>frame</code> may be published as an optional visual layer when the realization family exposes it,</li>
  <li><code>label</code> is a dynamic semantic public surface and is therefore preferably published through a placement-support resource such as <code>anchors/label.json</code> rather than through baked final label SVG files,</li>
  <li>the runtime renders live <code>label.text</code> into the published placement surface.</li>
</ul>

<p>
This is the key example posture that prevents dynamic public text from being redefined by asset ownership.
</p>

<hr/>

<h2 id="portability-posture">9. Portability Posture</h2>

<p>
Examples in this directory must remain portable across runtime families.
That portability requirement applies especially to:
</p>

<ul>
  <li>Python runtimes,</li>
  <li>Rust runtimes,</li>
  <li>C and C++ runtimes.</li>
</ul>

<p>
Portability does not require those runtimes to use identical host UI toolkits or identical rendering pipelines.
It requires them to be able to consume the same published realization contract without one implementation becoming the hidden semantic source of truth.
</p>

<p>
Accordingly, examples SHOULD publish:
</p>

<ul>
  <li>inspectable resource identities,</li>
  <li>inspectable placement resources,</li>
  <li>explicit state mappings,</li>
  <li>explicit fallbacks,</li>
  <li>clear separation between semantic public surfaces and visual assets.</li>
</ul>

<hr/>

<h2 id="validation-posture">10. Validation Posture</h2>

<p>
Reviewers and validators SHOULD be able to check at least the following from the example corridor:
</p>

<ul>
  <li>the prose example does not contradict the machine-readable package,</li>
  <li>the machine-readable package does not contradict the asset-tree shape,</li>
  <li>resource paths correspond to the published resource records,</li>
  <li>dynamic public text is not silently reassigned to state-specific SVG ownership when the realization contract publishes a placement surface instead,</li>
  <li>fallback posture remains explicit rather than hidden in one runtime loader.</li>
</ul>

<hr/>

<h2 id="anti-patterns">11. Anti-Patterns</h2>

<p>
The following example-corridor anti-patterns SHOULD be avoided:
</p>

<ul>
  <li>an example JSON package that contradicts the example asset tree,</li>
  <li>an example asset tree that reintroduces runtime-private assumptions not present in the published realization,</li>
  <li>publishing prose that says a public text surface is dynamic while the example assets still imply that final text is owned by state-specific SVG files,</li>
  <li>treating examples as disposable illustrations rather than as inspectable publication guidance,</li>
  <li>letting one runtime sample implementation become the only place where the actual realization logic can be understood.</li>
</ul>

<hr/>

<h2 id="summary">12. Summary</h2>

<p>
The <code>Examples/</code> corridor of the default realization family exists to keep the publication chain explicit from doctrine to machine-readable package to concrete assets.
</p>

<p>
A correct example in this directory:
</p>

<ul>
  <li>aligns with the doctrinal documents above it,</li>
  <li>aligns with the machine-readable realization package it accompanies,</li>
  <li>aligns with the concrete asset-tree posture,</li>
  <li>helps future runtimes implement the realization portably without becoming the owner of widget semantics.</li>
</ul>
