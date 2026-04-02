<p align="center">
  <img src="../../FROG logo.svg" alt="FROG logo" width="200" />
</p>

<h1 align="center">🐸 Reference Internal Artifacts</h1>

<p align="center">
  Minimal internal JSON artifact shapes for the non-normative FROG reference pipeline<br/>
  <em>FROG — Free Open Graphical Language</em>
</p>

<hr/>

<h2>Contents</h2>

<ul>
  <li><a href="#overview">1. Overview</a></li>
  <li><a href="#status-and-boundary">2. Status and Boundary</a></li>
  <li><a href="#design-rules">3. Design Rules</a></li>
  <li><a href="#artifact-sequence">4. Artifact Sequence</a></li>
  <li><a href="#loaded-source-artifact">5. Loaded Source Artifact</a></li>
  <li><a href="#validation-result-artifact">6. Validation Result Artifact</a></li>
  <li><a href="#derived-execution-ir-artifact">7. Derived Execution IR Artifact</a></li>
  <li><a href="#lowered-form-artifact">8. Lowered Form Artifact</a></li>
  <li><a href="#backend-contract-artifact">9. Backend Contract Artifact</a></li>
  <li><a href="#runtime-result-artifact">10. Runtime Result Artifact</a></li>
  <li><a href="#artifact-linking-rules">11. Artifact Linking Rules</a></li>
  <li><a href="#first-slice-expectations">12. First-Slice Expectations</a></li>
  <li><a href="#summary">13. Summary</a></li>
</ul>

<hr/>

<h2 id="overview">1. Overview</h2>

<p>
This document defines <strong>minimal internal JSON artifact shapes</strong> for the first FROG reference pipeline.
These artifacts are intended to make the reference implementation directly codable while preserving the already-published stage boundaries:
</p>

<pre><code>canonical source
  -&gt; loaded source
  -&gt; validation result
  -&gt; derived Execution IR
  -&gt; lowered form
  -&gt; backend contract
  -&gt; runtime result
</code></pre>

<p>
The goal is not to standardize a universal transport for all future implementations.
The goal is to define one compact, disciplined internal shape for the first non-normative reference implementation.
</p>

<hr/>

<h2 id="status-and-boundary">2. Status and Boundary</h2>

<p>
All artifact shapes in this document are <strong>non-normative</strong>.
They do not redefine:
</p>

<ul>
  <li>canonical source structure,</li>
  <li>validated semantic truth,</li>
  <li>the normative open Execution IR model,</li>
  <li>the normative backend contract boundary.</li>
</ul>

<p>
Instead, they provide one implementation-local materialization for the first reference pipeline.
If an artifact shape becomes inconvenient or incomplete, the implementation may revise it.
What must remain stable is the published architectural separation between source, validation, open IR, lowering, backend handoff, and private realization.
</p>

<hr/>

<h2 id="design-rules">3. Design Rules</h2>

<ul>
  <li>Each artifact should have a clear stage owner.</li>
  <li>Each artifact should record its stage and version explicitly.</li>
  <li>Each artifact should carry source identity where useful.</li>
  <li>Validation failure should stop derivation.</li>
  <li>Invalid source must not produce a “successful” later artifact.</li>
  <li>Artifacts should remain simple enough to inspect by hand.</li>
  <li>The first slice should prefer explicit structure over premature compression.</li>
</ul>

<hr/>

<h2 id="artifact-sequence">4. Artifact Sequence</h2>

<p>
The reference pipeline should materialize artifacts conceptually equivalent to:
</p>

<pre><code>LoadedSource
ValidationResult
DerivedExecutionIR
LoweredForm
BackendContractArtifact
RuntimeResult
</code></pre>

<p>
Those names are implementation-facing and may be changed in code,
but their stage meaning should remain stable.
</p>

<hr/>

<h2 id="loaded-source-artifact">5. Loaded Source Artifact</h2>

<p>
The loaded-source artifact is the output of the loader.
It should remain close to canonical source while adding just enough wrapper structure for diagnostics and stage chaining.
</p>

<p>
Minimal conceptual shape:
</p>

<pre><code>{
  "artifact_kind": "frog_loaded_source",
  "artifact_version": "0.1-dev",
  "source": {
    "path": "Examples/01_pure_addition/main.frog",
    "content_hash": "sha256:...",
    "spec_version": "0.1"
  },
  "document": {
    "...": "verbatim decoded canonical source object"
  },
  "diagnostics": []
}</code></pre>

<p>
Notes:
</p>

<ul>
  <li><code>document</code> should remain as close as possible to the canonical source object.</li>
  <li>No semantic truth should be claimed yet.</li>
  <li>Loader diagnostics may exist here, but a successful loaded-source artifact is still only a source-intake artifact.</li>
</ul>

<hr/>

<h2 id="validation-result-artifact">6. Validation Result Artifact</h2>

<p>
The validation-result artifact is the first stage that may claim success or failure against the selected published rules for the MVP slice.
</p>

<p>
Minimal conceptual shape:
</p>

<pre><code>{
  "artifact_kind": "frog_validation_result",
  "artifact_version": "0.1-dev",
  "source_ref": {
    "path": "Examples/01_pure_addition/main.frog",
    "content_hash": "sha256:..."
  },
  "status": "ok",
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
    "entry_kind": "single_frog_program",
    "type_facts": [],
    "resolved_entities": {
      "interface_inputs": [],
      "interface_outputs": [],
      "widgets": [],
      "primitive_refs": []
    }
  },
  "diagnostics": []
}</code></pre>

<p>
For a failed validation:
</p>

<pre><code>{
  "artifact_kind": "frog_validation_result",
  "artifact_version": "0.1-dev",
  "source_ref": {
    "path": "Conformance/invalid/illegal_feedback_without_explicit_memory.case"
  },
  "status": "error",
  "error_code": "illegal_feedback_without_explicit_memory",
  "diagnostics": [
    {
      "severity": "error",
      "message": "Directed cycle without explicit local-memory primitive.",
      "source_anchor": {
        "node_ids": ["add_1"],
        "edge_ids": ["e3", "e4"]
      }
    }
  ]
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li><code>status = ok</code> is required before derivation may begin.</li>
  <li><code>validated_program</code> is an implementation-facing validated basis, not a new normative layer.</li>
  <li>The first slice may keep <code>type_facts</code> and <code>resolved_entities</code> simple.</li>
</ul>

<hr/>

<h2 id="derived-execution-ir-artifact">7. Derived Execution IR Artifact</h2>

<p>
The derived Execution IR artifact is the output of the deriver.
It must preserve attribution and the distinctions required by the published derivation rules,
but it remains implementation-local in transport shape.
</p>

<p>
Minimal conceptual shape:
</p>

<pre><code>{
  "artifact_kind": "frog_derived_execution_ir",
  "artifact_version": "0.1-dev",
  "source_ref": {
    "path": "Examples/02_ui_value_roundtrip/main.frog",
    "content_hash": "sha256:..."
  },
  "validation_ref": {
    "status": "ok",
    "program_id": "prog:02_ui_value_roundtrip"
  },
  "execution_unit": {
    "id": "unit:main",
    "family": "execution_unit",
    "objects": [
      {
        "id": "obj:ctrl_a_value",
        "kind": "widget_value_participation",
        "widget_id": "ctrl_a",
        "direction": "out",
        "value_type": "f64",
        "sources": ["diagram.node:ctrl_a_value"]
      },
      {
        "id": "obj:add_1",
        "kind": "primitive",
        "primitive_ref": "frog.core.add",
        "ports": [
          { "id": "a", "direction": "in", "value_type": "f64" },
          { "id": "b", "direction": "in", "value_type": "f64" },
          { "id": "result", "direction": "out", "value_type": "f64" }
        ],
        "sources": ["diagram.node:add_1"]
      },
      {
        "id": "obj:ind_result_value",
        "kind": "widget_value_participation",
        "widget_id": "ind_result",
        "direction": "in",
        "value_type": "f64",
        "sources": ["diagram.node:ind_result_value"]
      }
    ],
    "connections": [
      {
        "id": "conn:e1",
        "from": { "object": "obj:ctrl_a_value", "port": "value" },
        "to": { "object": "obj:add_1", "port": "a" },
        "sources": ["diagram.edge:e1"]
      }
    ],
    "support_objects": []
  },
  "diagnostics": []
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li>The first slice may use simple string IDs.</li>
  <li><code>sources</code> should keep source attribution explicit.</li>
  <li>The artifact must preserve distinctions such as:
    <ul>
      <li><code>interface_input</code> versus <code>interface_output</code>,</li>
      <li><code>widget_value</code> versus <code>widget_reference</code>,</li>
      <li>widget-reference participation versus UI-object primitive operation,</li>
      <li>explicit local memory versus ordinary primitive execution.</li>
    </ul>
  </li>
</ul>

<hr/>

<h2 id="lowered-form-artifact">8. Lowered Form Artifact</h2>

<p>
The lowered-form artifact is the output of the lowerer for one chosen backend family.
It is more specialized than the open Execution IR,
but it is still not yet the standardized backend contract.
</p>

<p>
Minimal conceptual shape:
</p>

<pre><code>{
  "artifact_kind": "frog_lowered_form",
  "artifact_version": "0.1-dev",
  "backend_family": "reference_host_runtime_ui_binding",
  "source_ref": {
    "path": "Examples/03_ui_property_write/main.frog",
    "content_hash": "sha256:..."
  },
  "ir_ref": {
    "execution_unit_id": "unit:main"
  },
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
        {
          "id": "op:status_in",
          "kind": "public_input"
        },
        {
          "id": "op:ctrl_gain_ref",
          "kind": "ui_reference_handle",
          "widget_id": "ctrl_gain"
        },
        {
          "id": "op:write_label_text",
          "kind": "ui_property_write",
          "member": {
            "part": "label",
            "member": "text"
          }
        }
      ],
      "wires": [
        {
          "id": "w:e1",
          "from": "op:status_in",
          "to": "op:write_label_text",
          "input": "value"
        },
        {
          "id": "w:e2",
          "from": "op:ctrl_gain_ref",
          "to": "op:write_label_text",
          "input": "ref"
        }
      ]
    }
  ],
  "diagnostics": []
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li>The lowered form may introduce backend-family-specialized operation kinds.</li>
  <li>It must not erase attribution or semantic distinctions that still matter to the backend contract.</li>
  <li>The first slice should keep the lowered form readable rather than aggressively flattened.</li>
</ul>

<hr/>

<h2 id="backend-contract-artifact">9. Backend Contract Artifact</h2>

<p>
The backend-contract artifact is the output of the contract emitter.
It should match the published backend-contract boundary closely enough to be consumed by the reference runtime.
</p>

<p>
Minimal conceptual shape:
</p>

<pre><code>{
  "artifact_kind": "frog_backend_contract",
  "artifact_version": "0.1",
  "backend_family": "reference_host_runtime_ui_binding",
  "producer": "reference_contract_emitter",
  "compatibility": "family_specific",
  "source_ref": {
    "path": "Examples/04_stateful_feedback_delay/main.frog",
    "content_hash": "sha256:..."
  },
  "assumptions": {
    "profiles_required": [],
    "state_model": "explicit_local_memory_preserved",
    "scheduling": {
      "fixed": true,
      "family_rule": "deterministic_step_execution"
    },
    "ui_binding": {
      "enabled": false
    }
  },
  "units": [
    {
      "id": "main",
      "role": "entry_unit",
      "boundaries": [
        {
          "id": "b:x",
          "kind": "public_input",
          "value_type": "f64"
        },
        {
          "id": "b:y",
          "kind": "public_output",
          "value_type": "f64"
        }
      ],
      "state": [
        {
          "id": "state:delay_1",
          "kind": "explicit_local_memory",
          "initial": 0.0,
          "source_origin": ["diagram.node:delay_1"]
        }
      ],
      "operations": [],
      "attribution": {
        "source_mapping_available": true,
        "fault_anchor_support": true,
        "debug_anchor_support": true
      }
    }
  ],
  "unsupported": [],
  "diagnostics": []
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li>The contract should be directly consumable by the reference runtime.</li>
  <li>It must carry declared assumptions, not hidden ones.</li>
  <li>The first slice should preserve state and UI distinctions where relevant to the selected family.</li>
</ul>

<hr/>

<h2 id="runtime-result-artifact">10. Runtime Result Artifact</h2>

<p>
The runtime-result artifact is the output of the runtime stage.
It is not a normative layer.
It is an execution summary for the reference implementation.
</p>

<p>
Minimal conceptual shape:
</p>

<pre><code>{
  "artifact_kind": "frog_runtime_result",
  "artifact_version": "0.1-dev",
  "backend_family": "reference_host_runtime_ui_binding",
  "contract_ref": {
    "unit_ids": ["main"]
  },
  "status": "ok",
  "execution_summary": {
    "mode": "deterministic_step_execution",
    "state_initialized": true,
    "ui_bound": true
  },
  "outputs": {
    "public": {},
    "ui": {}
  },
  "diagnostics": []
}</code></pre>

<p>
For a rejected contract:
</p>

<pre><code>{
  "artifact_kind": "frog_runtime_result",
  "artifact_version": "0.1-dev",
  "backend_family": "reference_host_runtime_ui_binding",
  "status": "error",
  "error_code": "unsupported_ui_event_model",
  "diagnostics": [
    {
      "severity": "error",
      "message": "Contract requires a UI event model not supported by the reference family."
    }
  ]
}</code></pre>

<p>
Rules:
</p>

<ul>
  <li>The runtime must distinguish contract rejection from runtime execution failure.</li>
  <li>The artifact may expose implementation-local execution summary fields.</li>
  <li>The first slice should keep this artifact simple and diagnostic-oriented.</li>
</ul>

<hr/>

<h2 id="artifact-linking-rules">11. Artifact Linking Rules</h2>

<p>
The first reference pipeline should maintain explicit links between artifacts:
</p>

<ul>
  <li><code>LoadedSource</code> links to canonical file identity,</li>
  <li><code>ValidationResult</code> links back to source identity,</li>
  <li><code>DerivedExecutionIR</code> links back to validation and source anchors,</li>
  <li><code>LoweredForm</code> links back to the derived IR and backend family,</li>
  <li><code>BackendContractArtifact</code> links back to the lowered form and source identity,</li>
  <li><code>RuntimeResult</code> links back to the accepted backend contract.</li>
</ul>

<p>
The goal is not to freeze one global identity architecture.
The goal is to keep the first reference pipeline debuggable and auditable.
</p>

<hr/>

<h2 id="first-slice-expectations">12. First-Slice Expectations</h2>

<p>
For the first slice:
</p>

<ul>
  <li>the loaded source artifact should remain close to the file,</li>
  <li>the validation artifact should clearly distinguish success and failure,</li>
  <li>the derived IR artifact should preserve attribution and core distinctions,</li>
  <li>the lowered form should remain family-oriented but still readable,</li>
  <li>the backend contract should be directly consumable by the reference runtime,</li>
  <li>the runtime result should clearly distinguish success, rejection, and failure.</li>
</ul>

<p>
The first slice should optimize for clarity and codability,
not for compression or long-term transport standardization.
</p>

<hr/>

<h2 id="summary">13. Summary</h2>

<p>
This document defines one minimal set of internal JSON artifacts for the first FROG reference pipeline.
They are intentionally non-normative and implementation-local,
but they provide a concrete coding target for the first reference toolchain:
load,
validate,
derive open Execution IR,
lower,
emit a backend contract,
and run.
</p>
