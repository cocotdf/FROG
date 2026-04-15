<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">FROG Default Realization Family</h1>

<p align="center">
  <strong>Normative default official realization family for the intrinsic standardized widget baseline and authorized anticipatory realization publication</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#purpose">2. Purpose</a></li>
  <li><a href="#target-classes">3. Target Classes</a></li>
  <li><a href="#family-goals">4. Family Goals</a></li>
  <li><a href="#shared-architectural-posture">5. Shared Architectural Posture</a></li>
  <li><a href="#realization-variant-posture">6. Realization Variant Posture</a></li>
  <li><a href="#shared-state-posture">7. Shared State Posture</a></li>
  <li><a href="#shared-resource-and-binding-posture">8. Shared Resource and Binding Posture</a></li>
  <li><a href="#shared-fallback-posture">9. Shared Fallback Posture</a></li>
  <li><a href="#shared-host-expectations">10. Shared Host Expectations</a></li>
  <li><a href="#documents-in-this-family">11. Documents in this Family</a></li>
  <li><a href="#summary">12. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the default official realization family for the intrinsic standardized widget baseline of FROG.
</p>

<p>
Its role is to provide one coherent, inspectable, portable, standard realization posture for the baseline widget classes already defined in <code>Libraries/Widgets/</code>.
</p>

<p>
The <code>Default</code> family is realization-side only.
It does not redefine widget class law, does not replace the standardized widget baseline, and does not make realization assets the semantic owner of public widget meaning.
</p>

<p>
The <code>Default</code> family should be understood as a full publication corridor rather than as a loose collection of skins.
It includes:
</p>

<ul>
  <li>family-level realization doctrine,</li>
  <li>per-widget realization posture,</li>
  <li>machine-readable publication posture,</li>
  <li>resource and state-mapping posture,</li>
  <li>asset-tree and asset-naming posture,</li>
  <li>example-corridor posture.</li>
</ul>

<p>
The family may also publish anticipatory realization material for classes that are not yet intrinsically standardized, provided that such material remains explicitly realization-side, subordinate to future intrinsic standardization, and non-authoritative for class law.
</p>

<hr/>

<h2 id="purpose">2. Purpose</h2>

<p>
The <code>Default</code> family exists to provide:
</p>

<ul>
  <li>a first serious standard visual embodiment of the baseline widget classes,</li>
  <li>a reference family for examples and runtime interpretation,</li>
  <li>a stable place for state-sensitive embodiment, structural part correspondence, and realization-side placement metadata,</li>
  <li>a clean separation between class law and realization detail,</li>
  <li>a repository-visible realization publication corridor that may prepare future class families without silently standardizing them intrinsically.</li>
</ul>

<p>
The family is therefore not just a collection of skins.
It is the first official realization corridor through which baseline widgets can be embodied, published, validated, and interpreted portably.
</p>

<p>
Its publication posture is intended to be strong enough that no single runtime implementation becomes the hidden semantic source of truth for the UI system.
</p>

<hr/>

<h2 id="target-classes">3. Target Classes</h2>

<p>
The default family targets the following intrinsic standardized classes:
</p>

<ul>
  <li><code>frog.widgets.numeric_control</code></li>
  <li><code>frog.widgets.numeric_indicator</code></li>
  <li><code>frog.widgets.boolean_control</code></li>
  <li><code>frog.widgets.boolean_indicator</code></li>
  <li><code>frog.widgets.string_control</code></li>
  <li><code>frog.widgets.string_indicator</code></li>
  <li><code>frog.widgets.button</code></li>
  <li><code>frog.widgets.waveform_chart</code></li>
</ul>

<p>
Those classes remain defined by the standardized widget baseline.
The <code>Default</code> family only defines one official realization posture for them.
</p>

<p>
The family MAY also publish realization-side preparation for additional classes such as <code>array</code>, <code>cluster</code>, <code>enum</code>, <code>path</code>, <code>tab</code>, <code>tree</code>, <code>table</code>, <code>picture</code>, <code>listbox</code>, and other future-facing widget families.
When such publication exists, it must be interpreted as anticipatory realization material rather than as proof that the corresponding intrinsic class law has already been standardized in <code>Libraries/Widgets/</code>.
</p>

<hr/>

<h2 id="family-goals">4. Family Goals</h2>

<p>
The default family is designed to be:
</p>

<ul>
  <li>clear,</li>
  <li>minimal,</li>
  <li>portable,</li>
  <li>state-structured,</li>
  <li>part-aware,</li>
  <li>inspectable at the publication level,</li>
  <li>suitable for SVG-backed or host-native realization,</li>
  <li>usable as the first official embodiment interpreted by runtimes,</li>
  <li>capable of hosting anticipatory realization work without introducing semantic drift.</li>
</ul>

<p>
It is not intended to define the only future visual family.
It is the first official one.
</p>

<p>
Its architectural goal is to remain inspectable enough that a Python, Rust, or C/C++ runtime can interpret it without becoming the hidden owner of widget law or realization law.
</p>

<hr/>

<h2 id="shared-architectural-posture">5. Shared Architectural Posture</h2>

<p>
Across the default family, the following separation is fundamental:
</p>

<ul>
  <li>standard widget classes own public widget meaning,</li>
  <li>the realization family owns structured visual embodiment,</li>
  <li>the realization package owns machine-readable publication of that embodiment,</li>
  <li>resources own geometry, layers, anchors, regions, and visual support artifacts,</li>
  <li>host runtimes interpret or approximate the family while preserving public class meaning.</li>
</ul>

<p>
This means the default family is expected to distinguish clearly between:
</p>

<ul>
  <li>semantic widget data,</li>
  <li>widget-visible style surfaces when supported,</li>
  <li>realization-side placement metadata,</li>
  <li>decorative or state-specific assets.</li>
</ul>

<p>
The preferred realization-publication split across the family is:
</p>

<ul>
  <li><strong><code>state_maps</code></strong> for state-sensitive visual embodiment,</li>
  <li><strong><code>part_bindings</code></strong> for stable structural correspondence between public parts and realization surfaces,</li>
  <li><strong>anchors</strong> and <strong>text regions</strong> for dynamic public surfaces rendered by the host.</li>
</ul>

<p>
The button corridor is an important example of this rule:
the semantic label text belongs to the standardized button class,
while the default family owns where and how that label is visually placed and embodied.
</p>

<p>
More generally, the same architectural distinction matters for numeric value surfaces, string value surfaces, chart titles, axis labels, and other future dynamic public surfaces.
</p>

<p>
The same distinction also governs anticipatory realization material:
visual publication may be prepared ahead of intrinsic class standardization, but such publication must not be mistaken for intrinsic ownership of public semantics.
</p>

<hr/>

<h2 id="realization-variant-posture">6. Realization Variant Posture</h2>

<p>
The default family standardizes one realization corridor per published class family, but it does not require one single visible shape for each class.
</p>

<p>
Accordingly, a conforming default realization MAY publish more than one compatible embodiment posture for the same standardized class, provided that:
</p>

<ul>
  <li>the public class meaning remains unchanged,</li>
  <li>the published public parts remain interpretable,</li>
  <li>the realization contract remains inspectable,</li>
  <li>no implicit class split is introduced by realization choice alone.</li>
</ul>

<p>
This rule is especially important when several mature host traditions use visibly different but semantically equivalent embodiments for the same widget family.
</p>

<p>
For example, in the boolean corridor:
</p>

<ul>
  <li>checkbox-like embodiment,</li>
  <li>switch-like embodiment,</li>
  <li>toggle-like embodiment,</li>
  <li>LED-like embodiment</li>
</ul>

<p>
may all remain realization variants of the same standardized boolean classes, as long as they preserve the published boolean class contract.
</p>

<p>
The same general rule may later apply to other families when a visible difference is only an embodiment choice rather than a true semantic difference.
</p>

<p>
This distinction is normative:
</p>

<ul>
  <li>realization variants MAY differ in geometry, motion, emphasis, decorative layering, or host-native control style,</li>
  <li>realization variants MUST NOT silently introduce new public semantics, new mandatory public members, or a new implicit standard class.</li>
</ul>

<p>
A future specification may still introduce a distinct widget class if a later design demonstrates a genuinely distinct public contract.
Until then, embodiment diversity remains a realization concern rather than a class-law concern.
</p>

<hr/>

<h2 id="shared-state-posture">7. Shared State Posture</h2>

<p>
Across the default realization family, widgets and parts MAY use a shared standard state vocabulary such as:
</p>

<ul>
  <li><code>normal</code></li>
  <li><code>disabled</code></li>
  <li><code>focused</code></li>
  <li><code>pressed</code> where applicable</li>
  <li><code>hovered</code> where supported by the active host posture</li>
</ul>

<p>
Not every widget or part needs every state.
Each family-specific document defines the relevant subset.
</p>

<p>
These are realization-side visual states.
They do not automatically create new source-owned persistent widget state.
</p>

<p>
The family prefers explicit state publication over filename guessing or host-private conventions.
Where state-sensitive embodiment exists, it should remain inspectable through published <code>state_maps</code> and explicit resource inventories.
</p>

<hr/>

<h2 id="shared-resource-and-binding-posture">8. Shared Resource and Binding Posture</h2>

<p>
The default family assumes that realization resources MAY be organized by:
</p>

<ul>
  <li>widget class,</li>
  <li>realized visual part,</li>
  <li>interaction state,</li>
  <li>optional size or density variant,</li>
  <li>placement-support role such as anchors or text regions.</li>
</ul>

<p>
For example:
</p>

<pre><code>button/
  face/
    normal
    pressed
    disabled
    focused
  frame/
    normal
    focused
  anchors/
    label

numeric_control/
  increment_button/
    normal
    pressed
  decrement_button/
    normal
    pressed
  anchors/
    label
    value
</code></pre>

<p>
This is a posture definition, not one mandatory concrete asset tree.
However, the family expects concrete publication to remain aligned with the documented asset and naming posture of this corridor.
</p>

<p>
Across the family, realization publication is expected to distinguish at least:
</p>

<ul>
  <li><strong>state maps</strong> for state-sensitive embodiment,</li>
  <li><strong>part bindings</strong> for stable structural correspondence between public parts and realization surfaces,</li>
  <li><strong>anchor or text-region publication</strong> when a host dynamically renders a public part into a realization-defined placement surface.</li>
</ul>

<p>
This distinction is especially important for dynamic text-bearing parts.
A public part such as a button <code>label</code> should preferably bind to an anchor, text region, or equivalent placement surface rather than rely on asset-baked text as the only embodiment path.
</p>

<p>
Likewise, the existence of a visual asset near a dynamic public surface must not be interpreted as semantic ownership of that surface by the asset layer.
</p>

<p>
When multiple compatible embodiment variants exist for the same class, their resource inventories may differ, but the published part meaning and the family-level publication rules must remain stable.
</p>

<p>
When anticipatory realization material is published for classes that are not yet intrinsically standardized, the same resource and binding posture still applies, but that publication remains realization-side preparation only.
</p>

<hr/>

<h2 id="shared-fallback-posture">9. Shared Fallback Posture</h2>

<p>
If a specialized state resource is unavailable, a conforming realization MAY fall back to:
</p>

<ul>
  <li>the nearest less-specialized state resource,</li>
  <li>a host-native compatible rendering,</li>
  <li>a generic default visual posture preserving the published part structure.</li>
</ul>

<p>
If a specialized placement surface is unavailable, a conforming realization MAY also fall back to:
</p>

<ul>
  <li>a host-native compatible region,</li>
  <li>a documented generic placement rule,</li>
  <li>another explicitly published compatible anchor or region.</li>
</ul>

<p>
Fallback is allowed only if public interaction meaning and part meaning remain preserved.
Fallback must remain inspectable rather than disappearing into runtime-private heuristics.
</p>

<p>
The family-level expectation is:
</p>

<ul>
  <li>visual-state fallback should remain visible in <code>state_maps</code>,</li>
  <li>structural or placement fallback should remain visible in <code>part_bindings</code> or equivalent placement publication.</li>
</ul>

<p>
If one embodiment variant cannot be realized exactly, a host MAY fall back to another compatible embodiment variant of the same class, provided that:
</p>

<ul>
  <li>no class-level semantic drift occurs,</li>
  <li>the published part meaning remains preserved,</li>
  <li>the fallback does not imply a new implicit class contract.</li>
</ul>

<hr/>

<h2 id="shared-host-expectations">10. Shared Host Expectations</h2>

<p>
A host interpreting the default family SHOULD preserve at least:
</p>

<ul>
  <li>published widget parts,</li>
  <li>published realization-state distinctions,</li>
  <li>visible distinction between enabled and disabled posture,</li>
  <li>visible distinction between normal and pressed posture where applicable,</li>
  <li>reasonable focus indication where supported by the host,</li>
  <li>dynamic rendering of public parts that the family publishes as host-rendered rather than asset-baked.</li>
</ul>

<p>
A host MAY approximate the family when exact resources are unavailable, but it should preserve:
</p>

<ul>
  <li>the stable meaning of public parts,</li>
  <li>the separation between semantic widget data and decorative assets,</li>
  <li>the machine-readable realization posture published by the family.</li>
</ul>

<p>
In particular, hosts should remain able to consume the same published realization contract across Python, Rust, and C/C++ runtime families without one host implementation becoming the only place where the real realization logic can be understood.
</p>

<p>
Hosts MAY choose among compatible family-supported embodiment variants when the relevant per-widget realization posture allows it.
That choice remains valid only if published class meaning and realization inspectability remain preserved.
</p>

<p>
Hosts MAY also consume anticipatory realization material for example, prototype, or experimental runtime purposes, but such use must not be presented as evidence that intrinsic class standardization has already been closed.
</p>

<hr/>

<h2 id="documents-in-this-family">11. Documents in this Family</h2>

<ul>
  <li><code>Readme.md</code> — family-level posture for the official <code>Default</code> realization family</li>
  <li><code>Button.md</code> — default realization posture for the standard button</li>
  <li><code>Numeric.md</code> — default realization posture for standard numeric widgets</li>
  <li><code>Boolean.md</code> — default realization posture for standard boolean widgets</li>
  <li><code>String.md</code> — default realization posture for standard string widgets</li>
  <li><code>Chart.md</code> — default realization posture for the standard waveform chart</li>
  <li><code>Package.md</code> — machine-readable publication posture for the family</li>
  <li><code>Resource model.md</code> — resource identification, scoping, and publication posture</li>
  <li><code>State mapping.md</code> — state-sensitive embodiment and structural binding posture</li>
  <li><code>Assets/Readme.md</code> — concrete asset-tree posture for the family</li>
  <li><code>Assets/Naming.md</code> — asset naming posture for the family</li>
  <li><code>Examples/Readme.md</code> — example-corridor posture for the family</li>
</ul>

<p>
Additional per-class or future-facing realization documents MAY be published in this family before the corresponding intrinsic class standardization is closed, but such publication remains realization-side preparation unless and until <code>Libraries/Widgets/</code> standardizes the class intrinsically.
</p>

<hr/>

<h2 id="summary">12. Summary</h2>

<p>
The <code>Default</code> family is the first official realization family for the intrinsic standardized widget baseline.
</p>

<p>
It defines one coherent, state-structured, part-aware official embodiment that runtimes may interpret faithfully or approximate compatibly while preserving class meaning and part meaning.
</p>

<p>
Its architectural value is that it keeps realization explicit:
state-sensitive embodiment remains inspectable,
structural part bindings remain inspectable,
dynamic placement surfaces remain inspectable,
and assets remain subordinate to the widget and realization layers above them.
</p>

<p>
Its preferred family-wide architecture is:
</p>

<ul>
  <li>class law for public widget meaning,</li>
  <li>realization doctrine for structured embodiment,</li>
  <li>machine-readable package publication for inspectable realization contracts,</li>
  <li>resource and asset publication for concrete embodiment support,</li>
  <li>portable runtime interpretation without semantic ownership drift.</li>
</ul>

<p>
Within that architecture, compatible visible embodiment variants may coexist inside the same realization family as long as they remain realization choices rather than hidden class splits.
</p>

<p>
The same architecture also allows anticipatory realization publication for future-facing widget families, provided that such publication remains subordinate to intrinsic class law and is never mistaken for intrinsic standardization itself.
</p>
