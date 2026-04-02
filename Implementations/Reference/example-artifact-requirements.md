<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">🐸 Reference Example Artifact Requirements</h1>

<p align="center">
  Minimal per-example artifact requirements for the first FROG reference pipeline<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#status-and-boundary">2. Status and Boundary</a></li>
  <li><a href="#global-stage-rules">3. Global Stage Rules</a></li>
  <li><a href="#example-01-pure-addition">4. Example 01 — Pure Addition</a></li>
  <li><a href="#example-02-ui-value-roundtrip">5. Example 02 — UI Value Roundtrip</a></li>
  <li><a href="#example-03-ui-property-write">6. Example 03 — UI Property Write</a></li>
  <li><a href="#example-04-stateful-feedback-delay">7. Example 04 — Stateful Feedback with Explicit Delay</a></li>
  <li><a href="#cross-example-rejection-rules">8. Cross-Example Rejection Rules</a></li>
  <li><a href="#implementation-note">9. Implementation Note</a></li>
  <li><a href="#summary">10. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines the <strong>minimum required fields</strong> that the first reference implementation should produce for each MVP example at each pipeline stage:
</p>

<ul>
  <li><code>validate</code></li>
  <li><code>derive-ir</code></li>
  <li><code>lower</code></li>
  <li><code>emit-contract</code></li>
  <li><code>run</code></li>
</ul>

<p>
The goal is not to freeze one universal transport.
The goal is to make the first implementation slice directly codable and testable.
</p>

<hr/>

<h2 id="status-and-boundary">2. Status and Boundary</h2>

<p>
All requirements in this document are <strong>non-normative reference-implementation requirements</strong>.
They do not replace:
</p>

<ul>
  <li>canonical source ownership,</li>
  <li>validated semantic ownership,</li>
  <li>open Execution IR ownership,</li>
  <li>backend contract ownership.</li>
</ul>

<p>
They only define what the first reference implementation should minimally materialize to prove that the published architecture is executable.
</p>

<hr/>

<h2 id="global-stage-rules">3. Global Stage Rules</h2>

<p>
For every valid MVP example, the following stage rules apply:
</p>

<ul>
  <li><strong>validate</strong> MUST produce <code>status</code>, <code>source_ref</code>, <code>validated_subset</code>, and at least one stable <code>program_id</code>.</li>
  <li><strong>derive-ir</strong> MUST produce one <code>execution_unit</code> with attributable objects and attributable connections.</li>
  <li><strong>lower</strong> MUST produce one <code>backend_family</code>, one lowered unit, and explicit <code>assumptions</code>.</li>
  <li><strong>emit-contract</strong> MUST produce one backend contract with explicit <code>units</code>, <code>assumptions</code>, and <code>unsupported</code>.</li>
  <li><strong>run</strong> MUST produce <code>status</code>, <code>contract_ref</code>, and an execution summary or an explicit rejection reason.</li>
</ul>

<p>
For every invalid conformance case:
</p>

<ul>
  <li><strong>validate</strong> MUST fail explicitly,</li>
  <li><strong>derive-ir</strong>, <strong>lower</strong>, <strong>emit-contract</strong>, and <strong>run</strong> MUST NOT claim success.</li>
</ul>

<hr/>

<h2 id="example-01-pure-addition">4. Example 01 — Pure Addition</h2>

<p>
Target source:
</p>

<pre><code>Examples/01_pure_addition/main.frog</code></pre>

<h3>4.1 validate — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_validation_result",
  "status": "ok",
  "source_ref": {
    "path": "Examples/01_pure_addition/main.frog"
  },
  "validated_subset": {
    "core_primitives": true,
    "public_interface": true,
    "widget_value": false,
    "widget_reference": false,
    "ui_object_primitives": false,
    "explicit_local_memory": false
  },
  "validated_program": {
    "program_id": "prog:01_pure_addition",
    "entry_kind": "single_frog_program"
  }
}</code></pre>

<p>
Minimum semantic facts that must be known after validation:
</p>

<ul>
  <li>two public inputs exist,</li>
  <li>one public output exists,</li>
  <li>one valid <code>frog.core.add</code> primitive exists,</li>
  <li>the graph is acyclic.</li>
</ul>

<h3>4.2 derive-ir — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_derived_execution_ir",
  "execution_unit": {
    "id": "unit:main",
    "objects": [
      { "kind": "public_input_boundary" },
      { "kind": "public_input_boundary" },
      { "kind": "primitive", "primitive_ref": "frog.core.add" },
      { "kind": "public_output_boundary" }
    ],
    "connections": [
      {},
      {},
      {}
    ]
  }
}</code></pre>

<p>
Minimum distinctions that must remain explicit:
</p>

<ul>
  <li>input boundary versus output boundary,</li>
  <li>primitive identity for <code>frog.core.add</code>,</li>
  <li>connection attribution.</li>
</ul>

<h3>4.3 lower — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_lowered_form",
  "backend_family": "reference_host_runtime_ui_binding",
  "assumptions": {
    "deterministic_step_execution": true,
    "ui_binding_enabled": false
  },
  "units": [
    {
      "id": "lowered:main",
      "role": "entry_unit",
      "operations": [
        { "kind": "public_input" },
        { "kind": "public_input" },
        { "kind": "core_primitive_add" },
        { "kind": "public_output" }
      ]
    }
  ]
}</code></pre>

<h3>4.4 emit-contract — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_backend_contract",
  "backend_family": "reference_host_runtime_ui_binding",
  "assumptions": {
    "state_model": "none",
    "ui_binding": { "enabled": false }
  },
  "units": [
    {
      "id": "main",
      "role": "entry_unit",
      "boundaries": [
        { "kind": "public_input", "value_type": "f64" },
        { "kind": "public_input", "value_type": "f64" },
        { "kind": "public_output", "value_type": "f64" }
      ]
    }
  ],
  "unsupported": []
}</code></pre>

<h3>4.5 run — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_runtime_result",
  "status": "ok",
  "contract_ref": {
    "unit_ids": ["main"]
  },
  "execution_summary": {
    "mode": "deterministic_step_execution"
  },
  "outputs": {
    "public": {
      "result": "&lt;value&gt;"
    }
  }
}</code></pre>

<hr/>

<h2 id="example-02-ui-value-roundtrip">5. Example 02 — UI Value Roundtrip</h2>

<p>
Target source:
</p>

<pre><code>Examples/02_ui_value_roundtrip/main.frog</code></pre>

<h3>5.1 validate — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_validation_result",
  "status": "ok",
  "source_ref": {
    "path": "Examples/02_ui_value_roundtrip/main.frog"
  },
  "validated_subset": {
    "core_primitives": true,
    "public_interface": false,
    "widget_value": true,
    "widget_reference": false,
    "ui_object_primitives": false,
    "explicit_local_memory": false
  },
  "validated_program": {
    "program_id": "prog:02_ui_value_roundtrip",
    "entry_kind": "single_frog_program"
  }
}</code></pre>

<p>
Minimum semantic facts that must be known after validation:
</p>

<ul>
  <li>the front panel is structurally valid,</li>
  <li>the referenced widgets exist,</li>
  <li>the <code>widget_value</code> nodes refer to value-carrying widgets,</li>
  <li>the arithmetic primitive is type-compatible with the widget value types.</li>
</ul>

<h3>5.2 derive-ir — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_derived_execution_ir",
  "execution_unit": {
    "id": "unit:main",
    "objects": [
      { "kind": "widget_value_participation", "widget_id": "ctrl_a" },
      { "kind": "widget_value_participation", "widget_id": "ctrl_b" },
      { "kind": "primitive", "primitive_ref": "frog.core.add" },
      { "kind": "widget_value_participation", "widget_id": "ind_result" }
    ],
    "connections": [
      {},
      {},
      {}
    ]
  }
}</code></pre>

<p>
Minimum distinctions that must remain explicit:
</p>

<ul>
  <li>front-panel declaration versus diagram-side participation,</li>
  <li>control-side <code>widget_value</code> versus indicator-side <code>widget_value</code>,</li>
  <li>no accidental conversion to <code>widget_reference</code>,</li>
  <li>no accidental conversion to property access on member <code>value</code>.</li>
</ul>

<h3>5.3 lower — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_lowered_form",
  "backend_family": "reference_host_runtime_ui_binding",
  "assumptions": {
    "deterministic_step_execution": true,
    "ui_binding_enabled": true,
    "ui_event_model": "not_standardized"
  },
  "units": [
    {
      "id": "lowered:main",
      "role": "entry_unit",
      "operations": [
        { "kind": "ui_value_in", "widget_id": "ctrl_a" },
        { "kind": "ui_value_in", "widget_id": "ctrl_b" },
        { "kind": "core_primitive_add" },
        { "kind": "ui_value_out", "widget_id": "ind_result" }
      ]
    }
  ]
}</code></pre>

<h3>5.4 emit-contract — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_backend_contract",
  "backend_family": "reference_host_runtime_ui_binding",
  "assumptions": {
    "state_model": "none",
    "ui_binding": {
      "enabled": true,
      "event_model": "not_standardized",
      "value_binding": "supported",
      "reference_binding": "not_required"
    }
  },
  "units": [
    {
      "id": "main",
      "role": "entry_unit",
      "boundaries": [
        { "kind": "ui_value_input", "widget_id": "ctrl_a", "value_type": "f64" },
        { "kind": "ui_value_input", "widget_id": "ctrl_b", "value_type": "f64" },
        { "kind": "ui_value_output", "widget_id": "ind_result", "value_type": "f64" }
      ]
    }
  ],
  "unsupported": []
}</code></pre>

<h3>5.5 run — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_runtime_result",
  "status": "ok",
  "contract_ref": {
    "unit_ids": ["main"]
  },
  "execution_summary": {
    "mode": "deterministic_step_execution",
    "ui_bound": true
  },
  "outputs": {
    "ui": {
      "ind_result": "&lt;value&gt;"
    }
  }
}</code></pre>

<hr/>

<h2 id="example-03-ui-property-write">6. Example 03 — UI Property Write</h2>

<p>
Target source:
</p>

<pre><code>Examples/03_ui_property_write/main.frog</code></pre>

<h3>6.1 validate — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_validation_result",
  "status": "ok",
  "source_ref": {
    "path": "Examples/03_ui_property_write/main.frog"
  },
  "validated_subset": {
    "core_primitives": false,
    "public_interface": true,
    "widget_value": false,
    "widget_reference": true,
    "ui_object_primitives": true,
    "explicit_local_memory": false
  },
  "validated_program": {
    "program_id": "prog:03_ui_property_write",
    "entry_kind": "single_frog_program"
  }
}</code></pre>

<p>
Minimum semantic facts that must be known after validation:
</p>

<ul>
  <li>the referenced widget exists,</li>
  <li>the <code>widget_reference</code> participation is valid,</li>
  <li>the primitive <code>frog.ui.property_write</code> is valid,</li>
  <li>the addressed member path is valid and writable,</li>
  <li>the input string is type-compatible with the addressed property.</li>
</ul>

<h3>6.2 derive-ir — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_derived_execution_ir",
  "execution_unit": {
    "id": "unit:main",
    "objects": [
      { "kind": "public_input_boundary", "interface_port": "status" },
      { "kind": "widget_reference_participation", "widget_id": "ctrl_gain" },
      {
        "kind": "primitive",
        "primitive_ref": "frog.ui.property_write",
        "member": { "part": "label", "member": "text" }
      }
    ],
    "connections": [
      {},
      {}
    ]
  }
}</code></pre>

<p>
Minimum distinctions that must remain explicit:
</p>

<ul>
  <li>public interface input versus widget reference,</li>
  <li>widget reference versus primitive UI operation,</li>
  <li>object-style UI interaction versus natural <code>widget_value</code> participation.</li>
</ul>

<h3>6.3 lower — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_lowered_form",
  "backend_family": "reference_host_runtime_ui_binding",
  "assumptions": {
    "deterministic_step_execution": true,
    "ui_binding_enabled": true,
    "ui_event_model": "not_standardized"
  },
  "units": [
    {
      "id": "lowered:main",
      "role": "entry_unit",
      "operations": [
        { "kind": "public_input", "name": "status" },
        { "kind": "ui_reference_handle", "widget_id": "ctrl_gain" },
        {
          "kind": "ui_property_write",
          "member": { "part": "label", "member": "text" }
        }
      ]
    }
  ]
}</code></pre>

<h3>6.4 emit-contract — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_backend_contract",
  "backend_family": "reference_host_runtime_ui_binding",
  "assumptions": {
    "state_model": "none",
    "ui_binding": {
      "enabled": true,
      "event_model": "not_standardized",
      "value_binding": "not_required",
      "reference_binding": "supported"
    }
  },
  "units": [
    {
      "id": "main",
      "role": "entry_unit",
      "boundaries": [
        { "kind": "public_input", "name": "status", "value_type": "string" },
        { "kind": "ui_reference", "widget_id": "ctrl_gain" },
        {
          "kind": "ui_operation",
          "operation": "property_write",
          "member": { "part": "label", "member": "text" }
        }
      ]
    }
  ],
  "unsupported": []
}</code></pre>

<h3>6.5 run — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_runtime_result",
  "status": "ok",
  "contract_ref": {
    "unit_ids": ["main"]
  },
  "execution_summary": {
    "mode": "deterministic_step_execution",
    "ui_bound": true,
    "ui_reference_resolution": true
  },
  "outputs": {
    "ui": {
      "ctrl_gain.label.text": "&lt;value&gt;"
    }
  }
}</code></pre>

<hr/>

<h2 id="example-04-stateful-feedback-delay">7. Example 04 — Stateful Feedback with Explicit Delay</h2>

<p>
Target source:
</p>

<pre><code>Examples/04_stateful_feedback_delay/main.frog</code></pre>

<h3>7.1 validate — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_validation_result",
  "status": "ok",
  "source_ref": {
    "path": "Examples/04_stateful_feedback_delay/main.frog"
  },
  "validated_subset": {
    "core_primitives": true,
    "public_interface": true,
    "widget_value": false,
    "widget_reference": false,
    "ui_object_primitives": false,
    "explicit_local_memory": true
  },
  "validated_program": {
    "program_id": "prog:04_stateful_feedback_delay",
    "entry_kind": "single_frog_program"
  }
}</code></pre>

<p>
Minimum semantic facts that must be known after validation:
</p>

<ul>
  <li>a directed feedback cycle exists,</li>
  <li>the cycle is legal because it contains <code>frog.core.delay</code>,</li>
  <li>the delay node has the required <code>initial</code> field,</li>
  <li>the initial value is type-compatible,</li>
  <li>the graph therefore has explicit local memory rather than illegal combinational feedback.</li>
</ul>

<h3>7.2 derive-ir — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_derived_execution_ir",
  "execution_unit": {
    "id": "unit:main",
    "objects": [
      { "kind": "public_input_boundary", "interface_port": "x" },
      { "kind": "primitive", "primitive_ref": "frog.core.add" },
      {
        "kind": "explicit_local_memory",
        "primitive_ref": "frog.core.delay",
        "initial": 0.0
      },
      { "kind": "public_output_boundary", "interface_port": "y" }
    ],
    "connections": [
      {},
      {},
      {},
      {}
    ]
  }
}</code></pre>

<p>
Minimum distinctions that must remain explicit:
</p>

<ul>
  <li>ordinary primitive execution versus explicit local memory,</li>
  <li>the initial state value,</li>
  <li>feedback connectivity,</li>
  <li>public input and public output boundaries.</li>
</ul>

<h3>7.3 lower — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_lowered_form",
  "backend_family": "reference_host_runtime_ui_binding",
  "assumptions": {
    "deterministic_step_execution": true,
    "ui_binding_enabled": false
  },
  "units": [
    {
      "id": "lowered:main",
      "role": "entry_unit",
      "operations": [
        { "kind": "public_input", "name": "x" },
        { "kind": "state_read", "state_id": "delay_1" },
        { "kind": "core_primitive_add" },
        { "kind": "state_commit", "state_id": "delay_1" },
        { "kind": "public_output", "name": "y" }
      ]
    }
  ]
}</code></pre>

<h3>7.4 emit-contract — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_backend_contract",
  "backend_family": "reference_host_runtime_ui_binding",
  "assumptions": {
    "state_model": "explicit_local_memory_preserved",
    "ui_binding": { "enabled": false }
  },
  "units": [
    {
      "id": "main",
      "role": "entry_unit",
      "boundaries": [
        { "kind": "public_input", "name": "x", "value_type": "f64" },
        { "kind": "public_output", "name": "y", "value_type": "f64" }
      ],
      "state": [
        {
          "id": "state:delay_1",
          "kind": "explicit_local_memory",
          "initial": 0.0
        }
      ]
    }
  ],
  "unsupported": []
}</code></pre>

<h3>7.5 run — minimum required fields</h3>

<pre><code>{
  "artifact_kind": "frog_runtime_result",
  "status": "ok",
  "contract_ref": {
    "unit_ids": ["main"]
  },
  "execution_summary": {
    "mode": "deterministic_step_execution",
    "state_initialized": true,
    "state_updated": true
  },
  "outputs": {
    "public": {
      "y": "&lt;value&gt;"
    }
  }
}</code></pre>

<hr/>

<h2 id="cross-example-rejection-rules">8. Cross-Example Rejection Rules</h2>

<p>
The first prototype should also enforce the following rejection rules:
</p>

<ul>
  <li>If validation returns <code>status = error</code>, no later stage may claim success.</li>
  <li>If a case requires <code>widget_reference</code> semantics but the backend family does not support reference binding, <code>emit-contract</code> or <code>run</code> must reject explicitly.</li>
  <li>If a case requires explicit local memory and the lowering stage attempts to erase it, that is a lowering failure, not an acceptable specialization.</li>
  <li>If a case depends on a distinction that the runtime family cannot preserve while claiming support, the runtime must reject the contract explicitly.</li>
</ul>

<hr/>

<h2 id="implementation-note">9. Implementation Note</h2>

<p>
The first prototype should prefer <strong>over-explicit artifacts</strong> over aggressively minimized ones.
The point of the first slice is to make the pipeline easy to debug and easy to inspect.
Compression can come later.
</p>

<hr/>

<h2 id="summary">10. Summary</h2>

<p>
This document fixes the minimum internal artifact content that the first reference pipeline should produce for each of the four MVP examples.
That gives the prototype an immediate coding target:
each stage knows what it must minimally emit,
and each example knows what distinctions must still be visible downstream.
</p>
