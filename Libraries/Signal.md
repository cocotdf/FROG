<h1 align="center">🐸 FROG Signal Library Specification</h1>

<p align="center">
Definition of the standard <strong>frog.signal</strong> primitive library for FROG v0.1<br/>
<em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#goals">2. Goals</a></li>
  <li><a href="#relation-with-other-specifications">3. Relation with Other Specifications</a></li>
  <li><a href="#role-of-frog-signal">4. Role of <code>frog.signal</code></a></li>
  <li><a href="#naming-and-namespace">5. Naming and Namespace</a></li>
  <li><a href="#scope-for-v01">6. Scope for v0.1</a></li>
  <li><a href="#signal-model-for-v01">7. Signal Model for v0.1</a></li>
  <li><a href="#typing-model">8. Typing Model</a></li>
  <li><a href="#analysis-functions">9. Analysis Functions</a></li>
  <li><a href="#filtering-functions">10. Filtering Functions</a></li>
  <li><a href="#resampling-functions">11. Resampling Functions</a></li>
  <li><a href="#diagram-representation">12. Diagram Representation</a></li>
  <li><a href="#validation-rules">13. Validation Rules</a></li>
  <li><a href="#examples">14. Examples</a></li>
  <li><a href="#out-of-scope">15. Out of Scope for v0.1</a></li>
  <li><a href="#summary">16. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the standard <strong>frog.signal</strong> primitive library for FROG v0.1.
</p>

<p>
The <code>frog.signal</code> library provides a first standard set of signal-oriented primitives for common 1D sampled-signal processing tasks such as:
</p>

<ul>
  <li>basic signal analysis,</li>
  <li>simple deterministic filtering,</li>
  <li>basic resampling and rate reduction.</li>
</ul>

<p>
These primitives extend the language beyond the minimal built-in vocabulary of <code>frog.core</code> without changing the canonical graph structure of FROG programs.
</p>

<hr/>

<h2 id="goals">2. Goals</h2>

<ul>
  <li><strong>Practicality</strong> — provide a useful first signal-processing surface for real programs.</li>
  <li><strong>Minimality</strong> — keep the first standard signal library compact and durable.</li>
  <li><strong>Determinism</strong> — define clear, reproducible semantics for every primitive.</li>
  <li><strong>Portability</strong> — avoid assumptions tied to one runtime, device, or platform.</li>
  <li><strong>Composability</strong> — support larger signal-processing workflows built from explicit primitives.</li>
</ul>

<hr/>

<h2 id="relation-with-other-specifications">3. Relation with Other Specifications</h2>

<p>
This document complements the following specifications:
</p>

<ul>
  <li><strong>Expression/Diagram.md</strong> — defines how primitive function calls are serialized as executable graph nodes.</li>
  <li><strong>Expression/Type.md</strong> — defines array types, scalar numeric types, type compatibility, and coercion rules used by signal primitives.</li>
  <li><strong>Libraries/Core.md</strong> — defines the minimal built-in primitive library on top of which richer libraries such as <code>frog.signal</code> may be added.</li>
  <li><strong>IDE/Palette.md</strong> — defines how namespaces such as <code>frog.signal.*</code> may be surfaced to users in an IDE palette.</li>
</ul>

<p>
This document defines signal-library primitive semantics only.
It does not redefine the graph model, the type system, control structures, widget interaction, or IDE behavior.
</p>

<hr/>

<h2 id="role-of-frog-signal">4. Role of <code>frog.signal</code></h2>

<p>
The <code>frog.signal</code> library defines standardized signal-oriented primitives used by executable diagram nodes of kind <code>primitive</code>.
</p>

<p>
In language terms, these are signal-processing functions.
In serialized diagrams, calls to these functions appear as <code>primitive</code> nodes with namespace-qualified identifiers such as <code>frog.signal.rms</code> or <code>frog.signal.fir</code>.
</p>

<p>
The role of <code>frog.signal</code> is to provide reusable signal-processing vocabulary without making signal semantics implicit or editor-specific.
</p>

<hr/>

<h2 id="naming-and-namespace">5. Naming and Namespace</h2>

<p>
FROG library primitives use stable namespace-qualified identifiers of the form:
</p>

<pre>
frog.&lt;library&gt;.&lt;primitive&gt;
</pre>

<p>
For this document:
</p>

<ul>
  <li><code>frog</code> identifies the language namespace,</li>
  <li><code>signal</code> identifies the standard signal-processing library,</li>
  <li>the final segment identifies the primitive name.</li>
</ul>

<p>
Examples:
</p>

<pre>
frog.signal.mean
frog.signal.rms
frog.signal.peak
frog.signal.moving_average
frog.signal.fir
frog.signal.decimate
frog.signal.resample_linear
</pre>

<p>
Primitive names in <code>frog.signal</code> SHOULD use lowercase snake_case where multiple words are needed.
</p>

<hr/>

<h2 id="scope-for-v01">6. Scope for v0.1</h2>

<p>
FROG v0.1 standardizes the following initial <code>frog.signal</code> primitive families:
</p>

<ul>
  <li>signal analysis primitives,</li>
  <li>simple deterministic filtering primitives,</li>
  <li>basic resampling and rate-reduction primitives.</li>
</ul>

<p>
In v0.1, this document intentionally remains limited to uniformly ordered one-dimensional sampled signals represented as numeric arrays.
</p>

<p>
FROG v0.1 does <strong>not</strong> attempt to define:
</p>

<ul>
  <li>frequency-domain transforms,</li>
  <li>complex-valued signal types,</li>
  <li>waveform record types with timestamps and metadata,</li>
  <li>multi-channel signal containers,</li>
  <li>adaptive filtering,</li>
  <li>spectral estimation,</li>
  <li>hardware acquisition or streaming I/O semantics.</li>
</ul>

<hr/>

<h2 id="signal-model-for-v01">7. Signal Model for v0.1</h2>

<p>
In this document, a signal is modeled as an ordered one-dimensional array of numeric samples.
</p>

<p>
For v0.1:
</p>

<ul>
  <li>signal arrays MUST use element type <code>f32</code> or <code>f64</code>,</li>
  <li>sample order is significant,</li>
  <li>sample spacing is implicit unless an explicit scalar configuration input such as <code>dt</code> is provided by the primitive,</li>
  <li>no waveform metadata object is standardized in this document.</li>
</ul>

<p>
This means that <code>frog.signal</code> operates on value arrays, not on a separate waveform object model.
</p>

<hr/>

<h2 id="typing-model">8. Typing Model</h2>

<p>
All <code>frog.signal</code> primitives are typed according to <strong>Expression/Type.md</strong>.
</p>

<p>
Unless stated otherwise:
</p>

<ul>
  <li>signal inputs MUST be <code>array&lt;f32&gt;</code> or <code>array&lt;f64&gt;</code>,</li>
  <li>scalar numeric configuration inputs MUST be valid FROG numeric scalar types,</li>
  <li>all type compatibility checks MUST follow the standard FROG type rules,</li>
  <li>all implicit coercions MUST follow the standard FROG coercion rules,</li>
  <li>all primitives in this document are stateless and side-effect-free.</li>
</ul>

<p>
Unless stated otherwise, when a primitive consumes an <code>array&lt;f32&gt;</code>, its signal-array output and scalar floating-point result outputs are of type <code>f32</code>; when it consumes an <code>array&lt;f64&gt;</code>, those outputs are of type <code>f64</code>.
</p>

<hr/>

<h2 id="analysis-functions">9. Analysis Functions</h2>

<h3>9.1 <code>frog.signal.mean</code></h3>

<p>
Returns the arithmetic mean of a signal.
</p>

<ul>
  <li>input port: <code>signal</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li><code>signal</code> MUST be non-empty,</li>
  <li>the result is the arithmetic mean of all samples,</li>
  <li>the result type matches the floating-point element type of <code>signal</code>.</li>
</ul>

<h3>9.2 <code>frog.signal.rms</code></h3>

<p>
Returns the root-mean-square value of a signal.
</p>

<ul>
  <li>input port: <code>signal</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li><code>signal</code> MUST be non-empty,</li>
  <li>the result is <code>sqrt(mean(signal[i]^2))</code>,</li>
  <li>the result type matches the floating-point element type of <code>signal</code>.</li>
</ul>

<h3>9.3 <code>frog.signal.peak</code></h3>

<p>
Returns the maximum sample value in a signal and the index of its first occurrence.
</p>

<ul>
  <li>input port: <code>signal</code></li>
  <li>output ports: <code>value</code>, <code>index</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li><code>signal</code> MUST be non-empty,</li>
  <li><code>value</code> is the maximum sample value in the array,</li>
  <li><code>index</code> is the zero-based index of the first sample whose value equals <code>value</code>,</li>
  <li><code>value</code> has the same floating-point type as the signal element type,</li>
  <li><code>index</code> is of type <code>u64</code>.</li>
</ul>

<h3>9.4 <code>frog.signal.peak_to_peak</code></h3>

<p>
Returns the peak-to-peak amplitude of a signal.
</p>

<ul>
  <li>input port: <code>signal</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li><code>signal</code> MUST be non-empty,</li>
  <li>the result is <code>max(signal) - min(signal)</code>,</li>
  <li>the result type matches the floating-point element type of <code>signal</code>.</li>
</ul>

<hr/>

<h2 id="filtering-functions">10. Filtering Functions</h2>

<h3>10.1 <code>frog.signal.moving_average</code></h3>

<p>
Applies a causal trailing moving-average filter to a signal.
</p>

<ul>
  <li>input ports: <code>signal</code>, <code>window_size</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li><code>signal</code> MAY be empty,</li>
  <li><code>window_size</code> MUST be a positive integer value,</li>
  <li>the output length MUST equal the input signal length,</li>
  <li>for sample index <code>i</code>, the output is the mean of samples from <code>max(0, i - window_size + 1)</code> through <code>i</code>,</li>
  <li>the result signal element type matches the input signal element type.</li>
</ul>

<h3>10.2 <code>frog.signal.fir</code></h3>

<p>
Applies a causal finite impulse response filter to a signal.
</p>

<ul>
  <li>input ports: <code>signal</code>, <code>coefficients</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li><code>signal</code> MAY be empty,</li>
  <li><code>coefficients</code> MUST be non-empty,</li>
  <li><code>signal</code> and <code>coefficients</code> MUST have the same floating-point element type,</li>
  <li>the output length MUST equal the input signal length,</li>
  <li>the filter is defined as <code>y[i] = Σ(k = 0..M-1) h[k] * x[i-k]</code>,</li>
  <li>for indices below zero, <code>x[j]</code> MUST be treated as <code>0</code>,</li>
  <li>the result signal element type matches the input signal element type.</li>
</ul>

<hr/>

<h2 id="resampling-functions">11. Resampling Functions</h2>

<h3>11.1 <code>frog.signal.decimate</code></h3>

<p>
Reduces signal sample count by keeping every <code>factor</code>-th sample.
</p>

<ul>
  <li>input ports: <code>signal</code>, <code>factor</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li><code>factor</code> MUST be a positive integer value greater than or equal to <code>1</code>,</li>
  <li>the result contains input samples at indices <code>0</code>, <code>factor</code>, <code>2 * factor</code>, and so on,</li>
  <li>no implicit anti-alias filtering is performed by this primitive,</li>
  <li>the result signal element type matches the input signal element type.</li>
</ul>

<p>
This primitive performs deterministic sample dropping only.
If anti-alias filtering is required, it MUST be expressed explicitly in the diagram, for example by applying <code>frog.signal.fir</code> before decimation.
</p>

<h3>11.2 <code>frog.signal.resample_linear</code></h3>

<p>
Resamples a signal to a target output length using piecewise-linear interpolation.
</p>

<ul>
  <li>input ports: <code>signal</code>, <code>output_length</code></li>
  <li>output port: <code>result</code></li>
</ul>

<p>
Rules:
</p>

<ul>
  <li><code>signal</code> MUST be non-empty,</li>
  <li><code>output_length</code> MUST be a positive integer value,</li>
  <li>if <code>output_length = 1</code>, the result contains the first input sample only,</li>
  <li>if the input signal length is <code>1</code>, the single input value MUST be replicated to fill the output length,</li>
  <li>otherwise, the result samples are obtained by linear interpolation over the normalized input index range from <code>0</code> to <code>input_length - 1</code>,</li>
  <li>the result signal element type matches the input signal element type.</li>
</ul>

<hr/>

<h2 id="diagram-representation">12. Diagram Representation</h2>

<p>
Calls to <code>frog.signal</code> primitives are serialized as <code>primitive</code> nodes in the diagram.
</p>

<p>
Examples:
</p>

<pre><code>{
  "id": "rms_1",
  "kind": "primitive",
  "type": "frog.signal.rms"
}</code></pre>

<pre><code>{
  "id": "fir_1",
  "kind": "primitive",
  "type": "frog.signal.fir"
}</code></pre>

<p>
The exact port existence, direction, and typing of these nodes are resolved from this specification together with the type system and the graph rules.
</p>

<hr/>

<h2 id="validation-rules">13. Validation Rules</h2>

<p>
Implementations MUST enforce the following rules:
</p>

<ul>
  <li>every <code>frog.signal</code> function reference MUST identify a valid standardized signal primitive name,</li>
  <li>all required input ports for the referenced primitive MUST exist and be type-compatible,</li>
  <li>all produced output ports MUST match the primitive definition,</li>
  <li>all implicit coercions MUST follow <strong>Expression/Type.md</strong>,</li>
  <li>all primitives in this document MUST be treated as stateless and side-effect-free.</li>
</ul>

<p>
For signal-array inputs in this document:
</p>

<ul>
  <li>the input type MUST be <code>array&lt;f32&gt;</code> or <code>array&lt;f64&gt;</code>,</li>
  <li>nested arrays are not valid signal inputs for these primitives in v0.1,</li>
  <li>mixed floating-point element types within the same primitive call are not permitted unless made valid through standard FROG coercion rules before the primitive boundary.</li>
</ul>

<p>
For integer configuration inputs:
</p>

<ul>
  <li><code>window_size</code>, <code>factor</code>, and <code>output_length</code> MUST evaluate to strictly positive integer values in valid executions,</li>
  <li>supplying zero or a negative effective value is invalid.</li>
</ul>

<p>
For primitives that require non-empty input signals:
</p>

<ul>
  <li><code>frog.signal.mean</code>, <code>frog.signal.rms</code>, <code>frog.signal.peak</code>, <code>frog.signal.peak_to_peak</code>, and <code>frog.signal.resample_linear</code> MUST reject empty input arrays in v0.1.</li>
</ul>

<hr/>

<h2 id="examples">14. Examples</h2>

<h3>14.1 RMS of a signal</h3>

<pre><code>{
  "id": "rms_1",
  "kind": "primitive",
  "type": "frog.signal.rms"
}</code></pre>

<p>
Conceptual ports:
</p>

<pre>
signal → result
</pre>

<h3>14.2 Causal moving average</h3>

<pre><code>{
  "id": "avg_1",
  "kind": "primitive",
  "type": "frog.signal.moving_average"
}</code></pre>

<p>
Conceptual ports:
</p>

<pre>
signal, window_size → result
</pre>

<h3>14.3 FIR followed by decimation</h3>

<pre><code>"diagram": {
  "nodes": [
    { "id": "input_signal", "kind": "interface_input", "interface_port": "signal" },
    { "id": "coeffs", "kind": "interface_input", "interface_port": "coefficients" },
    { "id": "fir_1", "kind": "primitive", "type": "frog.signal.fir" },
    { "id": "decimate_1", "kind": "primitive", "type": "frog.signal.decimate" },
    { "id": "factor_in", "kind": "interface_input", "interface_port": "factor" },
    { "id": "output_signal", "kind": "interface_output", "interface_port": "result" }
  ],
  "edges": [
    { "id": "e1", "from": { "node": "input_signal", "port": "value" }, "to": { "node": "fir_1", "port": "signal" } },
    { "id": "e2", "from": { "node": "coeffs", "port": "value" }, "to": { "node": "fir_1", "port": "coefficients" } },
    { "id": "e3", "from": { "node": "fir_1", "port": "result" }, "to": { "node": "decimate_1", "port": "signal" } },
    { "id": "e4", "from": { "node": "factor_in", "port": "value" }, "to": { "node": "decimate_1", "port": "factor" } },
    { "id": "e5", "from": { "node": "decimate_1", "port": "result" }, "to": { "node": "output_signal", "port": "value" } }
  ]
}</code></pre>

<hr/>

<h2 id="out-of-scope">15. Out of Scope for v0.1</h2>

<p>
The following are outside the strict scope of <code>frog.signal</code> in v0.1:
</p>

<ul>
  <li>FFT, DFT, STFT, and other frequency-domain transforms,</li>
  <li>complex-valued signal primitives,</li>
  <li>window-function catalogs such as Hann, Hamming, Blackman, or Kaiser,</li>
  <li>IIR filters and adaptive filters,</li>
  <li>multi-rate filter-bank design,</li>
  <li>spectral density estimation,</li>
  <li>correlation and convolution families beyond the specific causal FIR primitive standardized here,</li>
  <li>multi-channel waveform containers,</li>
  <li>timestamped waveform records,</li>
  <li>hardware acquisition, streaming buffers, and device-driven sampling semantics.</li>
</ul>

<hr/>

<h2 id="summary">16. Summary</h2>

<p>
The <code>frog.signal</code> library defines a first standard signal-processing primitive set for FROG v0.1.
</p>

<p>
It provides:
</p>

<ul>
  <li>basic signal analysis,</li>
  <li>simple deterministic filtering,</li>
  <li>basic resampling and rate reduction.</li>
</ul>

<p>
This library is intentionally limited in v0.1.
Its purpose is to provide a durable first signal-processing foundation while preserving clear separation from the core language, the graph model, the type system, and future domain-specific expansion.
</p>

<hr/>

<p align="center">
End of FROG Signal Library Specification
</p>
