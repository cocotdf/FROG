(function () {
  "use strict";

  var diagramReplacements = [
  {
    "path": "/Readme.md",
    "sectionId": "positioning",
    "kind": "image",
    "occurrence": 1,
    "count": 1,
    "image": "./assets/readme-positioning-map.png",
    "alt": "FROG positioning map: accessibility versus system-grade execution",
    "width": "760"
  },
  {
    "path": "/Readme.md",
    "sectionId": "dataflow-programming",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "./assets/readme-dataflow-execution.png",
    "alt": "Traditional execution compared with dataflow execution",
    "width": "760"
  },
  {
    "path": "/Readme.md",
    "sectionId": "repository-runtime-and-native-execution-direction",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "./assets/readme-runtime-native-execution-direction.png",
    "alt": "Runtime and native execution direction from canonical source to runtimes and optional LLVM-oriented native path",
    "width": "760"
  },
  {
    "path": "/Readme.md",
    "sectionId": "specification-architecture",
    "kind": "pre",
    "occurrence": 1,
    "count": 2,
    "image": "./assets/readme-specification-architecture.png",
    "alt": "FROG specification architecture layers",
    "width": "760"
  },
  {
    "path": "/Readme.md",
    "sectionId": "program-representation",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "./assets/readme-program-representation-pipeline.png",
    "alt": "FROG program representation pipeline from source to FIR and lowering",
    "width": "760"
  },
  {
    "path": "/Readme.md",
    "sectionId": "execution-architecture",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "./assets/readme-execution-architecture.png",
    "alt": "FROG execution architecture from IDE authoring to target execution and observability",
    "width": "760"
  },
  {
    "path": "/Readme.md",
    "sectionId": "recommended-reading-path",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "assets/ascii-flow-diagrams/ascii-flow-23-readme.png",
    "alt": "ASCII flow diagram replacement for Readme.md section Recommended reading path",
    "width": "760"
  },
  {
    "path": "/Examples/Readme.md",
    "sectionId": "applicative-vertical-slice-anchor",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-08-examples-readme.png",
    "alt": "ASCII flow diagram replacement for Examples/Readme.md section 12. Applicative Vertical-Slice Anchor",
    "width": "760"
  },
  {
    "path": "/Expression/Cache.md",
    "sectionId": "cache-model",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-09-expression-cache.png",
    "alt": "ASCII flow diagram replacement for Expression/Cache.md section 8. Cache Model",
    "width": "760"
  },
  {
    "path": "/Expression/Icon.md",
    "sectionId": "coordinate-system-and-sizing",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-10-expression-icon.png",
    "alt": "ASCII flow diagram replacement for Expression/Icon.md section 9. Coordinate System and Sizing",
    "width": "760"
  },
  {
    "path": "/Expression/Type.md",
    "sectionId": "type-compatibility-model",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-11-expression-type.png",
    "alt": "ASCII flow diagram replacement for Expression/Type.md section 10. Type Compatibility Model",
    "width": "760"
  },
  {
    "path": "/Expression/Widget interaction.md",
    "sectionId": "diagram-representation",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-12-expression-widget-interaction.png",
    "alt": "ASCII flow diagram replacement for Expression/Widget interaction.md section 15. Diagram Representation",
    "width": "760"
  },
  {
    "path": "/IDE/Debugging.md",
    "sectionId": "relationship-with-probes-and-watches",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-13-ide-debugging.png",
    "alt": "ASCII flow diagram replacement for IDE/Debugging.md section 15. Relationship with Probes and Watches",
    "width": "760"
  },
  {
    "path": "/IDE/Observability.md",
    "sectionId": "high-level-observability-model",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-14-ide-observability.png",
    "alt": "ASCII flow diagram replacement for IDE/Observability.md section 6. High-Level Observability Model",
    "width": "760"
  },
  {
    "path": "/IDE/Probes.md",
    "sectionId": "overview",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-15-ide-probes.png",
    "alt": "ASCII flow diagram replacement for IDE/Probes.md section 1. Overview",
    "width": "760"
  },
  {
    "path": "/IDE/Readme.md",
    "sectionId": "high-level-architecture",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-16-ide-readme.png",
    "alt": "ASCII flow diagram replacement for IDE/Readme.md section 7. High-Level Architecture",
    "width": "760"
  },
  {
    "path": "/IDE/Snippet.md",
    "sectionId": "illustrative-examples",
    "kind": "pre",
    "occurrence": 5,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-17-ide-snippet.png",
    "alt": "ASCII flow diagram replacement for IDE/Snippet.md section 20.5 Drag-and-drop behavior",
    "width": "760"
  },
  {
    "path": "/IR/Construction rules.md",
    "sectionId": "construction-result",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-20-ir-construction-rules.png",
    "alt": "ASCII flow diagram replacement for IR/Construction rules.md section 6. Construction Result",
    "width": "760"
  },
  {
    "path": "/IR/Readme.md",
    "sectionId": "position-in-the-representation-pipeline",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-21-ir-readme.png",
    "alt": "ASCII flow diagram replacement for IR/Readme.md section 5. Position in the Representation Pipeline",
    "width": "760"
  },
  {
    "path": "/Libraries/Readme.md",
    "sectionId": "libraries-vs-profiles",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-22-libraries-readme.png",
    "alt": "ASCII flow diagram replacement for Libraries/Readme.md section 8. Libraries vs Profiles",
    "width": "760"
  },
  {
    "path": "/Versioning/Readme.md",
    "sectionId": "repository-wide-versioning-diagram",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-25-versioning-readme.png",
    "alt": "ASCII flow diagram replacement for Versioning/Readme.md section 29. Repository-Wide Versioning Diagram",
    "width": "760"
  },
  {
    "path": "/Strategy/Heilmeier/Readme.md",
    "sectionId": "future-end-to-end-poc-direction",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-24-strategy-heilmeier-readme.png",
    "alt": "ASCII flow diagram replacement for Strategy/Heilmeier/Readme.md section 14. Future End-to-End POC Direction",
    "width": "760"
  },
  {
    "path": "/Implementations/Reference/Readme.md",
    "sectionId": "architectural-position",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-18-implementations-reference-readme.png",
    "alt": "ASCII flow diagram replacement for Implementations/Reference/Readme.md section 4. Architectural Position",
    "width": "760"
  },
  {
    "path": "/Implementations/Reference/Readme.md",
    "sectionId": "example-contract-runtime-reading",
    "kind": "pre",
    "occurrence": 3,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-19-implementations-reference-readme.png",
    "alt": "ASCII flow diagram replacement for Implementations/Reference/Readme.md section 8. Example -> Contract -> Runtime Reading",
    "width": "760"
  },
  {
    "path": "/Examples/04_stateful_feedback_delay/Readme.md",
    "sectionId": "source-shape",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-07-examples-04-stateful-feedback-delay-readme.png",
    "alt": "ASCII flow diagram replacement for Examples/04_stateful_feedback_delay/Readme.md section 4. Source Shape",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/50_identity_loss_must_not_be_disguised_as_intentional_non_primary_correspondence.md",
    "sectionId": "intended-anti-pattern",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-01-conformance-invalid-50-identity-loss-must-not-be-disguised-as-intentional-non-primary-corr.png",
    "alt": "ASCII flow diagram replacement for Conformance/invalid/50_identity_loss_must_not_be_disguised_as_intentional_non_primary_correspondence.md section 3. Intended Anti-Pattern",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/52_primary_execution_object_without_recoverable_source_anchor_is_invalid.md",
    "sectionId": "intended-anti-pattern",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-02-conformance-invalid-52-primary-execution-object-without-recoverable-source-anchor-is-inval.png",
    "alt": "ASCII flow diagram replacement for Conformance/invalid/52_primary_execution_object_without_recoverable_source_anchor_is_invalid.md section 3. Intended Anti-Pattern",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/05_public_interface_and_widget_participation_distinct.md",
    "sectionId": "overview",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-03-conformance-valid-05-public-interface-and-widget-participation-distinct.png",
    "alt": "ASCII flow diagram replacement for Conformance/valid/05_public_interface_and_widget_participation_distinct.md section 1. Overview",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/15_explicit_connectivity_remains_distinct_from_inferred_evaluation_order.md",
    "sectionId": "overview",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-04-conformance-valid-15-explicit-connectivity-remains-distinct-from-inferred-evaluation-order.png",
    "alt": "ASCII flow diagram replacement for Conformance/valid/15_explicit_connectivity_remains_distinct_from_inferred_evaluation_order.md section 1. Overview",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/21_explicit_structure_owned_state_remains_distinct_from_inferred_persistent_value_by_feedback_shape.md",
    "sectionId": "overview",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-05-conformance-valid-21-explicit-structure-owned-state-remains-distinct-from-inferred-persist.png",
    "alt": "ASCII flow diagram replacement for Conformance/valid/21_explicit_structure_owned_state_remains_distinct_from_inferred_persistent_value_by_feedback_shape.md section 1. Overview",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/53_schema_valid_canonical_ir_must_still_preserve_ir_architectural_distinctions.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-06-conformance-valid-53-schema-valid-canonical-ir-must-still-preserve-ir-architectural-distin.png",
    "alt": "ASCII flow diagram replacement for Conformance/valid/53_schema_valid_canonical_ir_must_still_preserve_ir_architectural_distinctions.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/07_invalid_section_placement/Readme.md",
    "sectionId": "",
    "kind": "pre",
    "occurrence": 6,
    "count": 1,
    "image": "../../../assets/ascii-flow-diagrams/ascii-flow-026-chaine-flechee-repository-role-readme.png",
    "alt": "Generated diagram for Conformance/invalid/07_invalid_section_placement/Readme.md section Repository role",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/08_connector_references_unknown_interface_port/Readme.md",
    "sectionId": "",
    "kind": "pre",
    "occurrence": 7,
    "count": 1,
    "image": "../../../assets/ascii-flow-diagrams/ascii-flow-027-chaine-flechee-repository-role-readme.png",
    "alt": "Generated diagram for Conformance/invalid/08_connector_references_unknown_interface_port/Readme.md section Repository role",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/12_public_interface_declaration_must_not_require_front_panel_widget_existence.md",
    "sectionId": "overview",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-028-flux-vertical-1-overview-12-public-interface-declaration-must-not-require-front-pane.png",
    "alt": "Generated diagram for Conformance/invalid/12_public_interface_declaration_must_not_require_front_panel_widget_existence.md section 1. Overview",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/12_public_interface_declaration_must_not_require_front_panel_widget_existence.md",
    "sectionId": "relation-with-specification-ownership",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-029-flux-vertical-5-relation-with-specification-ownership-12-public-interface-declaratio.png",
    "alt": "Generated diagram for Conformance/invalid/12_public_interface_declaration_must_not_require_front_panel_widget_existence.md section 5. Relation with Specification Ownership",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/12_public_interface_declaration_must_not_require_front_panel_widget_existence.md",
    "sectionId": "relation-with-the-expression-to-meaning-boundary",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-030-flux-vertical-6-relation-with-the-expression-to-meaning-boundary-12-public-interface.png",
    "alt": "Generated diagram for Conformance/invalid/12_public_interface_declaration_must_not_require_front_panel_widget_existence.md section 6. Relation with the Expression-to-Meaning Boundary",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/12_public_interface_declaration_must_not_require_front_panel_widget_existence.md",
    "sectionId": "current-published-cases",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-031-chaine-flechee-8-2-invalid-cases-12-public-interface-declaration-must-not-require-fr.png",
    "alt": "Generated diagram for Conformance/invalid/12_public_interface_declaration_must_not_require_front_panel_widget_existence.md section 8.2 Invalid cases",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/12_public_interface_declaration_must_not_require_front_panel_widget_existence.md",
    "sectionId": "relation-with-examples-and-reference-implementation",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-032-chaine-flechee-11-relation-with-examples-and-reference-implementation-12-public-inte.png",
    "alt": "Generated diagram for Conformance/invalid/12_public_interface_declaration_must_not_require_front_panel_widget_existence.md section 11. Relation with Examples and Reference Implementation",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/24_inferred_default_initial_value_must_not_be_treated_as_explicit_state_initialization.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-030-flux-vertical-6-relation-with-the-expression-to-meaning-boundary-12-public-interface.png",
    "alt": "Generated diagram for Conformance/invalid/24_inferred_default_initial_value_must_not_be_treated_as_explicit_state_initialization.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/26_inferred_scheduler_order_must_not_be_treated_as_explicit_state_read_timing.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-030-flux-vertical-6-relation-with-the-expression-to-meaning-boundary-12-public-interface.png",
    "alt": "Generated diagram for Conformance/invalid/26_inferred_scheduler_order_must_not_be_treated_as_explicit_state_read_timing.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/28_inferred_runtime_flush_order_must_not_be_treated_as_explicit_state_write_visibility.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-030-flux-vertical-6-relation-with-the-expression-to-meaning-boundary-12-public-interface.png",
    "alt": "Generated diagram for Conformance/invalid/28_inferred_runtime_flush_order_must_not_be_treated_as_explicit_state_write_visibility.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/30_inferred_runtime_observation_point_must_not_be_treated_as_explicit_state_snapshot_boundary.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-030-flux-vertical-6-relation-with-the-expression-to-meaning-boundary-12-public-interface.png",
    "alt": "Generated diagram for Conformance/invalid/30_inferred_runtime_observation_point_must_not_be_treated_as_explicit_state_snapshot_boundary.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/32_inferred_runtime_update_epoch_must_not_be_treated_as_explicit_state_version_boundary.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-030-flux-vertical-6-relation-with-the-expression-to-meaning-boundary-12-public-interface.png",
    "alt": "Generated diagram for Conformance/invalid/32_inferred_runtime_update_epoch_must_not_be_treated_as_explicit_state_version_boundary.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/34_inferred_runtime_reconciliation_pass_must_not_be_treated_as_explicit_state_merge_boundary.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-030-flux-vertical-6-relation-with-the-expression-to-meaning-boundary-12-public-interface.png",
    "alt": "Generated diagram for Conformance/invalid/34_inferred_runtime_reconciliation_pass_must_not_be_treated_as_explicit_state_merge_boundary.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/executable/01_backend_consumable_but_execution_contract_invalid/Readme.md",
    "sectionId": "corridor-covered",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../../../assets/ascii-flow-diagrams/ascii-flow-033-chaine-flechee-4-corridor-covered-readme.png",
    "alt": "Generated diagram for Conformance/invalid/executable/01_backend_consumable_but_execution_contract_invalid/Readme.md section 4. Corridor Covered",
    "width": "760"
  },
  {
    "path": "/Conformance/invalid/executable/02_execution_contract_valid_but_required_host_service_missing/Readme.md",
    "sectionId": "corridor-covered",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../../../assets/ascii-flow-diagrams/ascii-flow-034-chaine-flechee-4-corridor-covered-readme.png",
    "alt": "Generated diagram for Conformance/invalid/executable/02_execution_contract_valid_but_required_host_service_missing/Readme.md section 4. Corridor Covered",
    "width": "760"
  },
  {
    "path": "/Conformance/Readme.md",
    "sectionId": "critical-boundaries",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-035-flux-vertical-7-critical-boundaries-readme.png",
    "alt": "Generated diagram for Conformance/Readme.md section 7. Critical Boundaries",
    "width": "760"
  },
  {
    "path": "/Conformance/Readme.md",
    "sectionId": "critical-boundaries",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-036-flux-vertical-7-critical-boundaries-readme.png",
    "alt": "Generated diagram for Conformance/Readme.md section 7. Critical Boundaries",
    "width": "760"
  },
  {
    "path": "/Conformance/Readme.md",
    "sectionId": "critical-boundaries",
    "kind": "pre",
    "occurrence": 3,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-037-flux-vertical-7-critical-boundaries-readme.png",
    "alt": "Generated diagram for Conformance/Readme.md section 7. Critical Boundaries",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/11_public_interface_declaration_does_not_require_front_panel_widget_existence.md",
    "sectionId": "forbidden-reinterpretations",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-038-chaine-flechee-10-forbidden-reinterpretations-11-public-interface-declaration-does-n.png",
    "alt": "Generated diagram for Conformance/valid/11_public_interface_declaration_does_not_require_front_panel_widget_existence.md section 10. Forbidden Reinterpretations",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/23_explicit_state_initialization_remains_distinct_from_inferred_default_initial_value.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-030-flux-vertical-6-relation-with-the-expression-to-meaning-boundary-12-public-interface.png",
    "alt": "Generated diagram for Conformance/valid/23_explicit_state_initialization_remains_distinct_from_inferred_default_initial_value.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/25_explicit_state_read_timing_remains_distinct_from_inferred_scheduler_order.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-030-flux-vertical-6-relation-with-the-expression-to-meaning-boundary-12-public-interface.png",
    "alt": "Generated diagram for Conformance/valid/25_explicit_state_read_timing_remains_distinct_from_inferred_scheduler_order.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/25_explicit_state_read_timing_remains_distinct_from_inferred_scheduler_order.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-039-flux-vertical-4-boundary-being-exercised-25-explicit-state-read-timing-remains-disti.png",
    "alt": "Generated diagram for Conformance/valid/25_explicit_state_read_timing_remains_distinct_from_inferred_scheduler_order.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/27_explicit_state_write_visibility_remains_distinct_from_inferred_runtime_flush_order.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-030-flux-vertical-6-relation-with-the-expression-to-meaning-boundary-12-public-interface.png",
    "alt": "Generated diagram for Conformance/valid/27_explicit_state_write_visibility_remains_distinct_from_inferred_runtime_flush_order.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/27_explicit_state_write_visibility_remains_distinct_from_inferred_runtime_flush_order.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-039-flux-vertical-4-boundary-being-exercised-25-explicit-state-read-timing-remains-disti.png",
    "alt": "Generated diagram for Conformance/valid/27_explicit_state_write_visibility_remains_distinct_from_inferred_runtime_flush_order.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/29_explicit_state_snapshot_boundary_remains_distinct_from_inferred_runtime_observation_point.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-030-flux-vertical-6-relation-with-the-expression-to-meaning-boundary-12-public-interface.png",
    "alt": "Generated diagram for Conformance/valid/29_explicit_state_snapshot_boundary_remains_distinct_from_inferred_runtime_observation_point.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/29_explicit_state_snapshot_boundary_remains_distinct_from_inferred_runtime_observation_point.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-039-flux-vertical-4-boundary-being-exercised-25-explicit-state-read-timing-remains-disti.png",
    "alt": "Generated diagram for Conformance/valid/29_explicit_state_snapshot_boundary_remains_distinct_from_inferred_runtime_observation_point.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/31_explicit_state_version_boundary_remains_distinct_from_inferred_runtime_update_epoch.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-030-flux-vertical-6-relation-with-the-expression-to-meaning-boundary-12-public-interface.png",
    "alt": "Generated diagram for Conformance/valid/31_explicit_state_version_boundary_remains_distinct_from_inferred_runtime_update_epoch.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/31_explicit_state_version_boundary_remains_distinct_from_inferred_runtime_update_epoch.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-039-flux-vertical-4-boundary-being-exercised-25-explicit-state-read-timing-remains-disti.png",
    "alt": "Generated diagram for Conformance/valid/31_explicit_state_version_boundary_remains_distinct_from_inferred_runtime_update_epoch.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/33_explicit_state_merge_boundary_remains_distinct_from_inferred_runtime_reconciliation_pass.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-030-flux-vertical-6-relation-with-the-expression-to-meaning-boundary-12-public-interface.png",
    "alt": "Generated diagram for Conformance/valid/33_explicit_state_merge_boundary_remains_distinct_from_inferred_runtime_reconciliation_pass.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/33_explicit_state_merge_boundary_remains_distinct_from_inferred_runtime_reconciliation_pass.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-039-flux-vertical-4-boundary-being-exercised-25-explicit-state-read-timing-remains-disti.png",
    "alt": "Generated diagram for Conformance/valid/33_explicit_state_merge_boundary_remains_distinct_from_inferred_runtime_reconciliation_pass.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/35_explicit_state_commit_boundary_remains_distinct_from_inferred_runtime_stabilization_phase.md",
    "sectionId": "4-boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-030-flux-vertical-6-relation-with-the-expression-to-meaning-boundary-12-public-interface.png",
    "alt": "Generated diagram for Conformance/valid/35_explicit_state_commit_boundary_remains_distinct_from_inferred_runtime_stabilization_phase.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/35_explicit_state_commit_boundary_remains_distinct_from_inferred_runtime_stabilization_phase.md",
    "sectionId": "4-boundary-being-exercised",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-039-flux-vertical-4-boundary-being-exercised-25-explicit-state-read-timing-remains-disti.png",
    "alt": "Generated diagram for Conformance/valid/35_explicit_state_commit_boundary_remains_distinct_from_inferred_runtime_stabilization_phase.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/37_explicit_source_attribution_must_remain_recoverable_across_derivation.md",
    "sectionId": "4-boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-040-flux-vertical-4-boundary-being-exercised-37-explicit-source-attribution-must-remain.png",
    "alt": "Generated diagram for Conformance/valid/37_explicit_source_attribution_must_remain_recoverable_across_derivation.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/39_open_execution_ir_identity_must_remain_distinct_from_private_runtime_identity.md",
    "sectionId": "4-boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-041-flux-vertical-4-boundary-being-exercised-39-open-execution-ir-identity-must-remain-d.png",
    "alt": "Generated diagram for Conformance/valid/39_open_execution_ir_identity_must_remain_distinct_from_private_runtime_identity.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/41_backend_contract_identity_must_remain_distinct_from_private_runtime_identity.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-042-flux-vertical-4-boundary-being-exercised-41-backend-contract-identity-must-remain-di.png",
    "alt": "Generated diagram for Conformance/valid/41_backend_contract_identity_must_remain_distinct_from_private_runtime_identity.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/43_open_execution_ir_structure_must_remain_distinct_from_private_runtime_schedule.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-043-flux-vertical-4-boundary-being-exercised-43-open-execution-ir-structure-must-remain.png",
    "alt": "Generated diagram for Conformance/valid/43_open_execution_ir_structure_must_remain_distinct_from_private_runtime_schedule.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/45_backend_contract_structure_must_remain_distinct_from_private_runtime_schedule.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-044-flux-vertical-4-boundary-being-exercised-45-backend-contract-structure-must-remain-d.png",
    "alt": "Generated diagram for Conformance/valid/45_backend_contract_structure_must_remain_distinct_from_private_runtime_schedule.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/47_open_execution_ir_observation_surface_must_remain_distinct_from_private_runtime_debug_state.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-045-flux-vertical-4-boundary-being-exercised-47-open-execution-ir-observation-surface-mu.png",
    "alt": "Generated diagram for Conformance/valid/47_open_execution_ir_observation_surface_must_remain_distinct_from_private_runtime_debug_state.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/49_intentional_non_primary_correspondence_must_remain_explicit_in_canonical_execution_ir.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-046-flux-vertical-4-boundary-being-exercised-49-intentional-non-primary-correspondence-m.png",
    "alt": "Generated diagram for Conformance/valid/49_intentional_non_primary_correspondence_must_remain_explicit_in_canonical_execution_ir.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/51_primary_execution_object_must_keep_explicit_source_attribution_in_canonical_execution_ir.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-047-flux-vertical-4-boundary-being-exercised-51-primary-execution-object-must-keep-expli.png",
    "alt": "Generated diagram for Conformance/valid/51_primary_execution_object_must_keep_explicit_source_attribution_in_canonical_execution_ir.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/57_region_ownership_must_remain_recoverable_in_canonical_execution_ir.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-048-flux-vertical-4-boundary-being-exercised-57-region-ownership-must-remain-recoverable.png",
    "alt": "Generated diagram for Conformance/valid/57_region_ownership_must_remain_recoverable_in_canonical_execution_ir.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/59_structure_boundary_terminals_must_remain_recoverable_in_canonical_execution_ir.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-049-flux-vertical-4-boundary-being-exercised-59-structure-boundary-terminals-must-remain.png",
    "alt": "Generated diagram for Conformance/valid/59_structure_boundary_terminals_must_remain_recoverable_in_canonical_execution_ir.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/61_structure_terminal_roles_must_remain_recoverable_in_canonical_execution_ir.md",
    "sectionId": "boundary-being-exercised",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-050-flux-vertical-4-boundary-being-exercised-61-structure-terminal-roles-must-remain-rec.png",
    "alt": "Generated diagram for Conformance/valid/61_structure_terminal_roles_must_remain_recoverable_in_canonical_execution_ir.md section 4. Boundary Being Exercised",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/compiler/02_structured_control_is_consumable.md",
    "sectionId": "",
    "kind": "pre",
    "occurrence": 3,
    "count": 1,
    "image": "../../../assets/ascii-flow-diagrams/ascii-flow-051-flux-vertical-source-scenario-02-structured-control-is-consumable.png",
    "alt": "Generated diagram for Conformance/valid/compiler/02_structured_control_is_consumable.md section Source Scenario",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/executable/01_one_shot_pure_core_starts_and_terminates/Readme.md",
    "sectionId": "corridor-covered",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../../../assets/ascii-flow-diagrams/ascii-flow-052-chaine-flechee-4-corridor-covered-readme.png",
    "alt": "Generated diagram for Conformance/valid/executable/01_one_shot_pure_core_starts_and_terminates/Readme.md section 4. Corridor Covered",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/executable/02_structured_control_one_shot_executes_correctly/Readme.md",
    "sectionId": "corridor-covered",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../../../assets/ascii-flow-diagrams/ascii-flow-053-chaine-flechee-4-corridor-covered-readme.png",
    "alt": "Generated diagram for Conformance/valid/executable/02_structured_control_one_shot_executes_correctly/Readme.md section 4. Corridor Covered",
    "width": "760"
  },
  {
    "path": "/Conformance/valid/executable/03_explicit_state_step_mode_initializes_and_advances/Readme.md",
    "sectionId": "corridor-covered",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../../../assets/ascii-flow-diagrams/ascii-flow-054-chaine-flechee-4-corridor-covered-readme.png",
    "alt": "Generated diagram for Conformance/valid/executable/03_explicit_state_step_mode_initializes_and_advances/Readme.md section 4. Corridor Covered",
    "width": "760"
  },
  {
    "path": "/Examples/compiler/02_structured_control.md",
    "sectionId": "",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-051-flux-vertical-source-scenario-02-structured-control-is-consumable.png",
    "alt": "Generated diagram for Examples/compiler/02_structured_control.md section Illustrative Shape",
    "width": "760"
  },
  {
    "path": "/Expression/Diagram.md",
    "sectionId": "interface-widget-and-structure-boundaries",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-055-chaine-flechee-17-1-public-interface-boundary-diagram.png",
    "alt": "Generated diagram for Expression/Diagram.md section 17.1 Public interface boundary",
    "width": "760"
  },
  {
    "path": "/Expression/Icon.md",
    "sectionId": "location",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-056-chaine-flechee-5-location-in-a-frog-file-icon.png",
    "alt": "Generated diagram for Expression/Icon.md section 5. Location in a .frog File",
    "width": "760"
  },
  {
    "path": "/Expression/IDE preferences.md",
    "sectionId": "location",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-057-chaine-flechee-5-location-in-a-frog-file-ide-preferences.png",
    "alt": "Generated diagram for Expression/IDE preferences.md section 5. Location in a .frog File",
    "width": "760"
  },
  {
    "path": "/Expression/IDE preferences.md",
    "sectionId": "recoverability-metadata",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-058-flux-vertical-13-recoverability-metadata-ide-preferences.png",
    "alt": "Generated diagram for Expression/IDE preferences.md section 13. Recoverability Metadata",
    "width": "760"
  },
  {
    "path": "/Expression/Interface.md",
    "sectionId": "relation-with-the-diagram",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-055-chaine-flechee-17-1-public-interface-boundary-diagram.png",
    "alt": "Generated diagram for Expression/Interface.md section 12. Relation with the Diagram",
    "width": "760"
  },
  {
    "path": "/Expression/Metadata.md",
    "sectionId": "location",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-059-chaine-flechee-5-location-in-a-frog-file-metadata.png",
    "alt": "Generated diagram for Expression/Metadata.md section 5. Location in a .frog File",
    "width": "760"
  },
  {
    "path": "/Expression/Metadata.md",
    "sectionId": "structure",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-060-chaine-flechee-6-metadata-structure-metadata.png",
    "alt": "Generated diagram for Expression/Metadata.md section 6. Metadata Structure",
    "width": "760"
  },
  {
    "path": "/Expression/Metadata.md",
    "sectionId": "field-definitions",
    "kind": "pre",
    "occurrence": 6,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-061-chaine-flechee-7-5-program-version-metadata.png",
    "alt": "Generated diagram for Expression/Metadata.md section 7.5 program_version",
    "width": "760"
  },
  {
    "path": "/Expression/Readme.md",
    "sectionId": "sections-overview",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-062-chaine-flechee-12-8-cache-readme.png",
    "alt": "Generated diagram for Expression/Readme.md section 12.8 Cache",
    "width": "760"
  },
  {
    "path": "/Expression/Readme.md",
    "sectionId": "cross-cutting-subsystems",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-063-chaine-flechee-13-6-control-structure-and-local-memory-source-dependencies-readme.png",
    "alt": "Generated diagram for Expression/Readme.md section 13.6 Control-Structure and Local-Memory Source Dependencies",
    "width": "760"
  },
  {
    "path": "/Expression/Schema.md",
    "sectionId": "relation-with-conformance",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-064-chaine-flechee-15-relation-with-conformance-schema.png",
    "alt": "Generated diagram for Expression/Schema.md section 15. Relation with Conformance",
    "width": "760"
  },
  {
    "path": "/GOVERNANCE.md",
    "sectionId": "repository-layers-and-governance-boundaries",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "assets/ascii-flow-diagrams/ascii-flow-065-chaine-flechee-4-repository-layers-and-governance-boundaries-governance.png",
    "alt": "Generated diagram for GOVERNANCE.md section 4. Repository Layers and Governance Boundaries",
    "width": "760"
  },
  {
    "path": "/IDE/Debugging.md",
    "sectionId": "architectural-position-and-dependencies",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-066-flux-vertical-4-3-dependency-diagram-debugging.png",
    "alt": "Generated diagram for IDE/Debugging.md section 4.3 Dependency diagram",
    "width": "760"
  },
  {
    "path": "/IDE/Debugging.md",
    "sectionId": "stepping-model",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-067-flux-vertical-10-2-eligible-safe-debug-stop-debugging.png",
    "alt": "Generated diagram for IDE/Debugging.md section 10.2 Eligible safe debug stop",
    "width": "760"
  },
  {
    "path": "/IDE/Observability.md",
    "sectionId": "repository-position-and-dependencies",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-068-flux-vertical-3-3-dependency-diagram-observability.png",
    "alt": "Generated diagram for IDE/Observability.md section 3.3 Dependency diagram",
    "width": "760"
  },
  {
    "path": "/IDE/Observability.md",
    "sectionId": "high-level-observability-model",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-069-flux-vertical-6-high-level-observability-model-observability.png",
    "alt": "Generated diagram for IDE/Observability.md section 6. High-Level Observability Model",
    "width": "760"
  },
  {
    "path": "/IDE/Probes.md",
    "sectionId": "architectural-position-and-dependencies",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-070-flux-vertical-4-3-dependency-diagram-probes.png",
    "alt": "Generated diagram for IDE/Probes.md section 4.3 Dependency diagram",
    "width": "760"
  },
  {
    "path": "/IDE/Probes.md",
    "sectionId": "live-paused-and-retained-views",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-071-flux-vertical-13-live-paused-and-retained-views-probes.png",
    "alt": "Generated diagram for IDE/Probes.md section 13. Live, Paused, and Retained Views",
    "width": "760"
  },
  {
    "path": "/IDE/Readme.md",
    "sectionId": "overview",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-072-flux-vertical-1-overview-readme.png",
    "alt": "Generated diagram for IDE/Readme.md section 1. Overview",
    "width": "760"
  },
  {
    "path": "/IDE/Readme.md",
    "sectionId": "high-level-architecture",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-073-flux-vertical-7-high-level-architecture-readme.png",
    "alt": "Generated diagram for IDE/Readme.md section 7. High-Level Architecture",
    "width": "760"
  },
  {
    "path": "/IDE/Readme.md",
    "sectionId": "frog-program-model",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-074-flux-vertical-13-frog-program-model-readme.png",
    "alt": "Generated diagram for IDE/Readme.md section 13. FROG Program Model",
    "width": "760"
  },
  {
    "path": "/IDE/Readme.md",
    "sectionId": "execution-integration-boundary",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-075-flux-vertical-15-execution-integration-boundary-readme.png",
    "alt": "Generated diagram for IDE/Readme.md section 15. Execution Integration Boundary",
    "width": "760"
  },
  {
    "path": "/IDE/Readme.md",
    "sectionId": "execution-observability",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-076-flux-vertical-18-execution-observability-readme.png",
    "alt": "Generated diagram for IDE/Readme.md section 18. Execution Observability",
    "width": "760"
  },
  {
    "path": "/IDE/Readme.md",
    "sectionId": "probes",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-077-flux-vertical-20-probes-readme.png",
    "alt": "Generated diagram for IDE/Readme.md section 20. Probes",
    "width": "760"
  },
  {
    "path": "/IDE/Watch.md",
    "sectionId": "architectural-position-and-dependencies",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-078-flux-vertical-4-3-dependency-diagram-watch.png",
    "alt": "Generated diagram for IDE/Watch.md section 4.3 Dependency diagram",
    "width": "760"
  },
  {
    "path": "/IDE/Watch.md",
    "sectionId": "live-paused-and-retained-behavior",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-079-flux-vertical-13-live-paused-and-retained-behavior-watch.png",
    "alt": "Generated diagram for IDE/Watch.md section 13. Live, Paused, and Retained Behavior",
    "width": "760"
  },
  {
    "path": "/Implementations/Reference/Deriver/Readme.md",
    "sectionId": "",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../../assets/ascii-flow-diagrams/ascii-flow-080-flux-vertical-architectural-position-readme.png",
    "alt": "Generated diagram for Implementations/Reference/Deriver/Readme.md section Architectural Position",
    "width": "760"
  },
  {
    "path": "/Implementations/Reference/frogc.md",
    "sectionId": "architectural-position",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-081-flux-vertical-5-architectural-position-frogc.png",
    "alt": "Generated diagram for Implementations/Reference/frogc.md section 5. Architectural Position",
    "width": "760"
  },
  {
    "path": "/Implementations/Reference/frogc.md",
    "sectionId": "published-corridor-anchor",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-082-flux-vertical-7-published-corridor-anchor-frogc.png",
    "alt": "Generated diagram for Implementations/Reference/frogc.md section 7. Published Corridor Anchor",
    "width": "760"
  },
  {
    "path": "/Implementations/Reference/internal-artifacts.md",
    "sectionId": "artifact-family-map",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-083-flux-vertical-4-artifact-family-map-internal-artifacts.png",
    "alt": "Generated diagram for Implementations/Reference/internal-artifacts.md section 4. Artifact Family Map",
    "width": "760"
  },
  {
    "path": "/Implementations/Reference/LLVM/Readme.md",
    "sectionId": "architectural-boundary",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../../assets/ascii-flow-diagrams/ascii-flow-084-flux-vertical-3-architectural-boundary-readme.png",
    "alt": "Generated diagram for Implementations/Reference/LLVM/Readme.md section 3. Architectural Boundary",
    "width": "760"
  },
  {
    "path": "/Implementations/Reference/LLVM/Readme.md",
    "sectionId": "target-corridor",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../../assets/ascii-flow-diagrams/ascii-flow-085-flux-vertical-6-target-corridor-readme.png",
    "alt": "Generated diagram for Implementations/Reference/LLVM/Readme.md section 6. Target Corridor",
    "width": "760"
  },
  {
    "path": "/Implementations/Reference/Lowerer/Readme.md",
    "sectionId": "",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../../assets/ascii-flow-diagrams/ascii-flow-086-flux-vertical-architectural-position-readme.png",
    "alt": "Generated diagram for Implementations/Reference/Lowerer/Readme.md section Architectural Position",
    "width": "760"
  },
  {
    "path": "/Implementations/Reference/pipeline.md",
    "sectionId": "published-corridor-artifacts",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-082-flux-vertical-7-published-corridor-anchor-frogc.png",
    "alt": "Generated diagram for Implementations/Reference/pipeline.md section 7. Published Corridor Artifacts",
    "width": "760"
  },
  {
    "path": "/Implementations/Reference/Readme.md",
    "sectionId": "example-contract-compiler-reading",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-087-flux-vertical-9-example-fir-lowering-compiler-reading-readme.png",
    "alt": "Generated diagram for Implementations/Reference/Readme.md section 9. Example -> FIR -> Lowering -> Compiler Reading",
    "width": "760"
  },
  {
    "path": "/IR/Backend contract.md",
    "sectionId": "overview",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-088-flux-vertical-1-overview-backend-contract.png",
    "alt": "Generated diagram for IR/Backend contract.md section 1. Overview",
    "width": "760"
  },
  {
    "path": "/IR/Backend contract.md",
    "sectionId": "position-in-the-pipeline",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-089-flux-vertical-3-position-in-the-pipeline-backend-contract.png",
    "alt": "Generated diagram for IR/Backend contract.md section 3. Position in the Pipeline",
    "width": "760"
  },
  {
    "path": "/IR/Construction rules.md",
    "sectionId": "overview",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-090-flux-vertical-1-overview-construction-rules.png",
    "alt": "Generated diagram for IR/Construction rules.md section 1. Overview",
    "width": "760"
  },
  {
    "path": "/IR/Construction rules.md",
    "sectionId": "relation-with-other-specifications",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-091-chaine-flechee-4-relation-with-other-specifications-construction-rules.png",
    "alt": "Generated diagram for IR/Construction rules.md section 4. Relation with Other Specifications",
    "width": "760"
  },
  {
    "path": "/IR/Construction rules.md",
    "sectionId": "construction-pipeline",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-092-chaine-flechee-8-construction-pipeline-construction-rules.png",
    "alt": "Generated diagram for IR/Construction rules.md section 8. Construction Pipeline",
    "width": "760"
  },
  {
    "path": "/IR/Derivation rules.md",
    "sectionId": "overview",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-093-flux-vertical-1-overview-derivation-rules.png",
    "alt": "Generated diagram for IR/Derivation rules.md section 1. Overview",
    "width": "760"
  },
  {
    "path": "/IR/Derivation rules.md",
    "sectionId": "scope-of-this-document",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-094-chaine-flechee-3-scope-of-this-document-derivation-rules.png",
    "alt": "Generated diagram for IR/Derivation rules.md section 3. Scope of This Document",
    "width": "760"
  },
  {
    "path": "/IR/Derivation rules.md",
    "sectionId": "relation-with-other-specifications",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-095-chaine-flechee-4-relation-with-other-specifications-derivation-rules.png",
    "alt": "Generated diagram for IR/Derivation rules.md section 4. Relation with Other Specifications",
    "width": "760"
  },
  {
    "path": "/IR/Derivation rules.md",
    "sectionId": "inputs-and-preconditions",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-096-chaine-flechee-6-inputs-and-preconditions-derivation-rules.png",
    "alt": "Generated diagram for IR/Derivation rules.md section 6. Inputs and Preconditions",
    "width": "760"
  },
  {
    "path": "/IR/Derivation rules.md",
    "sectionId": "derivation-result",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-097-flux-vertical-7-derivation-result-derivation-rules.png",
    "alt": "Generated diagram for IR/Derivation rules.md section 7. Derivation Result",
    "width": "760"
  },
  {
    "path": "/IR/Execution IR.md",
    "sectionId": "position-in-the-pipeline",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-098-flux-vertical-5-position-in-the-pipeline-execution-ir.png",
    "alt": "Generated diagram for IR/Execution IR.md section 5. Position in the Pipeline",
    "width": "760"
  },
  {
    "path": "/IR/Execution IR.md",
    "sectionId": "position-in-the-pipeline",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-099-flux-vertical-5-position-in-the-pipeline-execution-ir.png",
    "alt": "Generated diagram for IR/Execution IR.md section 5. Position in the Pipeline",
    "width": "760"
  },
  {
    "path": "/IR/Execution IR.md",
    "sectionId": "position-in-the-pipeline",
    "kind": "pre",
    "occurrence": 3,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-100-flux-vertical-5-position-in-the-pipeline-execution-ir.png",
    "alt": "Generated diagram for IR/Execution IR.md section 5. Position in the Pipeline",
    "width": "760"
  },
  {
    "path": "/IR/Execution IR.md",
    "sectionId": "canonical-serialization",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-101-flux-vertical-9-canonical-serialization-execution-ir.png",
    "alt": "Generated diagram for IR/Execution IR.md section 9. Canonical Serialization",
    "width": "760"
  },
  {
    "path": "/IR/Execution IR.md",
    "sectionId": "primary-object-families",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-102-flux-vertical-11-primary-object-families-execution-ir.png",
    "alt": "Generated diagram for IR/Execution IR.md section 11. Primary Object Families",
    "width": "760"
  },
  {
    "path": "/IR/Execution IR.md",
    "sectionId": "primary-object-families",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-103-flux-vertical-11-primary-object-families-execution-ir.png",
    "alt": "Generated diagram for IR/Execution IR.md section 11. Primary Object Families",
    "width": "760"
  },
  {
    "path": "/IR/Execution IR.md",
    "sectionId": "regions-and-structured-control",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-104-flux-vertical-14-regions-and-structured-control-execution-ir.png",
    "alt": "Generated diagram for IR/Execution IR.md section 14. Regions and Structured Control",
    "width": "760"
  },
  {
    "path": "/IR/Lowering.md",
    "sectionId": "overview",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-105-flux-vertical-1-overview-lowering.png",
    "alt": "Generated diagram for IR/Lowering.md section 1. Overview",
    "width": "760"
  },
  {
    "path": "/IR/Lowering.md",
    "sectionId": "position-in-the-pipeline",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-106-flux-vertical-4-position-in-the-pipeline-lowering.png",
    "alt": "Generated diagram for IR/Lowering.md section 4. Position in the Pipeline",
    "width": "760"
  },
  {
    "path": "/IR/Readme.md",
    "sectionId": "architectural-boundary",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-107-flux-vertical-4-architectural-boundary-readme.png",
    "alt": "Generated diagram for IR/Readme.md section 4. Architectural Boundary",
    "width": "760"
  },
  {
    "path": "/IR/Readme.md",
    "sectionId": "position-in-the-representation-pipeline",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-108-flux-vertical-5-position-in-the-representation-pipeline-readme.png",
    "alt": "Generated diagram for IR/Readme.md section 5. Position in the Representation Pipeline",
    "width": "760"
  },
  {
    "path": "/IR/schema/README.md",
    "sectionId": "relation-with-the-rest-of-ir",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../../assets/ascii-flow-diagrams/ascii-flow-109-chaine-flechee-3-relation-with-the-rest-of-ir-readme.png",
    "alt": "Generated diagram for IR/schema/README.md section 3. Relation with the Rest of IR/",
    "width": "760"
  },
  {
    "path": "/IR/Schema.md",
    "sectionId": "relation-with-other-ir-documents",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-110-chaine-flechee-4-relation-with-other-ir-documents-schema.png",
    "alt": "Generated diagram for IR/Schema.md section 4. Relation with Other IR Documents",
    "width": "760"
  },
  {
    "path": "/Language/Expression to validated meaning.md",
    "sectionId": "position-in-the-architecture",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-111-flux-vertical-3-position-in-the-architecture-expression-to-validated-meaning.png",
    "alt": "Generated diagram for Language/Expression to validated meaning.md section 3. Position in the Architecture",
    "width": "760"
  },
  {
    "path": "/Language/Expression to validated meaning.md",
    "sectionId": "position-in-the-architecture",
    "kind": "pre",
    "occurrence": 2,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-112-flux-vertical-3-position-in-the-architecture-expression-to-validated-meaning.png",
    "alt": "Generated diagram for Language/Expression to validated meaning.md section 3. Position in the Architecture",
    "width": "760"
  },
  {
    "path": "/Language/Expression to validated meaning.md",
    "sectionId": "relation-with-other-specifications",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-113-chaine-flechee-5-relation-with-other-specifications-expression-to-validated-meaning.png",
    "alt": "Generated diagram for Language/Expression to validated meaning.md section 5. Relation with Other Specifications",
    "width": "760"
  },
  {
    "path": "/Language/Expression to validated meaning.md",
    "sectionId": "forbidden-boundary-collapses",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-114-chaine-flechee-17-forbidden-boundary-collapses-expression-to-validated-meaning.png",
    "alt": "Generated diagram for Language/Expression to validated meaning.md section 17. Forbidden Boundary Collapses",
    "width": "760"
  },
  {
    "path": "/Language/Expression to validated meaning.md",
    "sectionId": "summary",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-115-chaine-flechee-20-summary-expression-to-validated-meaning.png",
    "alt": "Generated diagram for Language/Expression to validated meaning.md section 20. Summary",
    "width": "760"
  },
  {
    "path": "/Language/Readme.md",
    "sectionId": "overview",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-116-chaine-flechee-1-overview-readme.png",
    "alt": "Generated diagram for Language/Readme.md section 1. Overview",
    "width": "760"
  },
  {
    "path": "/Language/Readme.md",
    "sectionId": "architectural-position",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-117-flux-vertical-2-architectural-position-readme.png",
    "alt": "Generated diagram for Language/Readme.md section 2. Architectural Position",
    "width": "760"
  },
  {
    "path": "/Language/Readme.md",
    "sectionId": "document-map",
    "kind": "pre",
    "occurrence": 3,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-118-flux-vertical-4-document-map-readme.png",
    "alt": "Generated diagram for Language/Readme.md section 4. Document Map",
    "width": "760"
  },
  {
    "path": "/Language/Readme.md",
    "sectionId": "expression-to-meaning-boundary",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-112-flux-vertical-3-position-in-the-architecture-expression-to-validated-meaning.png",
    "alt": "Generated diagram for Language/Readme.md section 6. Expression to Meaning Boundary",
    "width": "760"
  },
  {
    "path": "/Language/Readme.md",
    "sectionId": "relation-with-ir",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-119-flux-vertical-8-relation-with-ir-readme.png",
    "alt": "Generated diagram for Language/Readme.md section 8. Relation with IR",
    "width": "760"
  },
  {
    "path": "/Language/Readme.md",
    "sectionId": "relation-with-libraries-and-profiles",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-120-chaine-flechee-9-relation-with-libraries-and-profiles-readme.png",
    "alt": "Generated diagram for Language/Readme.md section 9. Relation with Libraries and Profiles",
    "width": "760"
  },
  {
    "path": "/Language/Readme.md",
    "sectionId": "relation-with-implementations",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-121-flux-vertical-10-relation-with-implementations-readme.png",
    "alt": "Generated diagram for Language/Readme.md section 10. Relation with Implementations",
    "width": "760"
  },
  {
    "path": "/Language/Readme.md",
    "sectionId": "summary",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-122-chaine-flechee-12-summary-readme.png",
    "alt": "Generated diagram for Language/Readme.md section 12. Summary",
    "width": "760"
  },
  {
    "path": "/Libraries/Connectivity.md",
    "sectionId": "summary",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-123-flux-vertical-7-summary-connectivity.png",
    "alt": "Generated diagram for Libraries/Connectivity.md section 7. Summary",
    "width": "760"
  },
  {
    "path": "/Libraries/Readme.md",
    "sectionId": "how-a-primitive-gets-its-meaning",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-124-flux-vertical-5-how-a-primitive-gets-its-meaning-readme.png",
    "alt": "Generated diagram for Libraries/Readme.md section 5. How a Primitive Gets its Meaning",
    "width": "760"
  },
  {
    "path": "/Libraries/Readme.md",
    "sectionId": "relation-with-other-specification-layers",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-125-flux-vertical-11-relation-with-other-specification-layers-readme.png",
    "alt": "Generated diagram for Libraries/Readme.md section 11. Relation with Other Specification Layers",
    "width": "760"
  },
  {
    "path": "/Readme.md",
    "sectionId": "internal-documentation-map",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "assets/ascii-flow-diagrams/ascii-flow-126-flux-vertical-recommended-reading-path-readme.png",
    "alt": "Generated diagram for Readme.md section Recommended reading path",
    "width": "760"
  },
  {
    "path": "/Roadmap/Readme.md",
    "sectionId": "project-map-at-a-glance",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-127-flux-vertical-1-project-map-at-a-glance-readme.png",
    "alt": "Generated diagram for Roadmap/Readme.md section 1. Project map at a glance",
    "width": "760"
  },
  {
    "path": "/Roadmap/Readme.md",
    "sectionId": "guiding-principles",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-128-chaine-flechee-6-guiding-principles-readme.png",
    "alt": "Generated diagram for Roadmap/Readme.md section 6. Guiding principles",
    "width": "760"
  },
  {
    "path": "/Strategy/Readme.md",
    "sectionId": "what-strategy-does-not-own",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-129-chaine-flechee-3-what-strategy-does-not-own-readme.png",
    "alt": "Generated diagram for Strategy/Readme.md section 3. What Strategy Does Not Own",
    "width": "760"
  },
  {
    "path": "/Strategy/Readme.md",
    "sectionId": "relation-with-the-rest-of-the-repository",
    "kind": "pre",
    "occurrence": 1,
    "count": 1,
    "image": "../assets/ascii-flow-diagrams/ascii-flow-130-chaine-flechee-7-relation-with-the-rest-of-the-repository-readme.png",
    "alt": "Generated diagram for Strategy/Readme.md section 7. Relation with the Rest of the Repository",
    "width": "760"
  }
];

  function normalizePath(path) {
    var normalized = String(path || "/Readme.md");
    if (normalized.charAt(0) !== "/") {
      normalized = "/" + normalized;
    }
    return normalized.replace(/\/+/g, "/").toLowerCase();
  }

  function escapeRegExp(value) {
    return String(value).replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  function escapeHtml(value) {
    return String(value || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function imageHtml(entry) {
    return [
      '<p align="center" class="frog-pages-diagram">',
      '  <img src="' + escapeHtml(entry.image) + '" alt="' + escapeHtml(entry.alt || "Generated diagram") + '" width="' + escapeHtml(entry.width || "760") + '" />',
      '</p>'
    ].join("\n");
  }

  function sectionRange(markdown, sectionId) {
    if (!sectionId) {
      return { start: 0, end: markdown.length };
    }

    var headingPattern = new RegExp("<h2\\s+id=[\"']" + escapeRegExp(sectionId) + "[\"'][^>]*>[\\s\\S]*?<\\/h2>", "i");
    var headingMatch = headingPattern.exec(markdown);
    if (!headingMatch) {
      return null;
    }

    var start = headingMatch.index + headingMatch[0].length;
    var remainder = markdown.slice(start);
    var nextHeadingIndex = remainder.search(/<h2\s+id=["'][^"']+["'][^>]*>/i);
    return {
      start: start,
      end: nextHeadingIndex === -1 ? markdown.length : start + nextHeadingIndex
    };
  }

  function replaceBlock(markdown, entry) {
    var range = sectionRange(markdown, entry.sectionId);
    if (!range) {
      return markdown;
    }

    var section = markdown.slice(range.start, range.end);
    var pattern = entry.kind === "image"
      ? /<p\s+align=["']center["']>\s*<img\b[\s\S]*?<\/p>/gi
      : /<pre\b[\s\S]*?<\/pre>/gi;
    var matches = [];
    var match;

    while ((match = pattern.exec(section)) !== null) {
      matches.push({ index: match.index, value: match[0] });
    }

    var occurrence = Math.max(1, Number(entry.occurrence || 1));
    var count = Math.max(1, Number(entry.count || 1));
    var first = matches[occurrence - 1];
    var last = matches[occurrence + count - 2];

    if (!first || !last) {
      return markdown;
    }

    var absoluteStart = range.start + first.index;
    var absoluteEnd = range.start + last.index + last.value.length;
    return markdown.slice(0, absoluteStart) + imageHtml(entry) + markdown.slice(absoluteEnd);
  }

  window.applyPagesDiagramReplacements = function (markdown, currentFile) {
    var normalizedCurrentFile = normalizePath(currentFile);
    return diagramReplacements
      .filter(function (entry) {
        return normalizePath(entry.path) === normalizedCurrentFile;
      })
      .sort(function (left, right) {
        if (left.sectionId === right.sectionId) {
          return Number(right.occurrence || 1) - Number(left.occurrence || 1);
        }
        return String(right.sectionId || "").localeCompare(String(left.sectionId || ""));
      })
      .reduce(function (nextMarkdown, entry) {
        return replaceBlock(nextMarkdown, entry);
      }, String(markdown || ""));
  };
}());
