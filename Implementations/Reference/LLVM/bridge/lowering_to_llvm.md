<p align="center">
  <img src="../../../FROG logo.svg" alt="FROG logo" width="140" />
</p>

<h1 align="center">Lowering to LLVM Bridge</h1>

<p align="center">
  <strong>First lowering-to-LLVM mapping notes for the native example slice</strong><br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Overview</h2>
<p>
This document records the first direct mapping from the example-specific lowering artifact to a repository-visible LLVM IR module.
</p>

<h2>Mapping Posture</h2>
<ul>
  <li>The lowering entry becomes the LLVM function <code>@frog_example05_accumulate</code>.</li>
  <li>The scalar input becomes one LLVM integer parameter.</li>
  <li>The repeated bounded accumulation is represented in this first closure as a direct multiply-by-five equivalent.</li>
  <li>The returned accumulator value becomes the native observable result.</li>
</ul>

<h2>Why Direct Multiplication Is Acceptable Here</h2>
<p>
For this first example-specific closure, replacing five repeated additions with a multiply-by-five instruction preserves the observable arithmetic meaning of the slice while keeping the module intentionally small.
</p>
<p>
The reading rule remains:
</p>
<pre><code>first native proof equivalence
    !=
final generalized lowering policy
</code></pre>

<h2>Out of Scope</h2>
<ul>
  <li>general loop lowering policy,</li>
  <li>branching and phi-node posture for the full language,</li>
  <li>host UI rendering,</li>
  <li>native widget event execution.</li>
</ul>

<h2>Summary</h2>
<p>
This bridge captures the smallest correct arithmetic equivalence needed to make the first LLVM-native corridor executable and repository-visible.
</p>
