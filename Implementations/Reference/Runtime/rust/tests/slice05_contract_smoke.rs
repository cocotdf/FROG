use frog_reference_runtime_rust::contract::BackendContract;

#[test]
fn contract_payload_can_be_deserialized() {
    let raw = r#"
    {
      "artifact_kind": "frog_backend_contract",
      "artifact_version": "0.1",
      "backend_family": "reference_host_runtime_ui_binding",
      "source_ref": {
        "example_id": "05_bounded_ui_accumulator"
      },
      "assumptions": {
        "scheduling": {
          "family_rule": "deterministic_step_execution"
        }
      },
      "units": [
        {
          "unit_id": "main",
          "iteration_count": 5,
          "initial_state": 0,
          "control_widget_id": "ctrl_input",
          "indicator_widget_id": "ind_result",
          "output_id": "result",
          "property_writes": [
            {
              "widget_id": "ctrl_input",
              "member": "face_color",
              "value": { "value": "#D8E6FF" }
            },
            {
              "widget_id": "ind_result",
              "member": "face_color",
              "value": { "value": "#D8E6FF" }
            }
          ]
        }
      ],
      "unsupported": [],
      "diagnostics": []
    }
    "#;

    let contract: BackendContract = serde_json::from_str(raw).unwrap();

    assert_eq!(contract.backend_family, "reference_host_runtime_ui_binding");
    assert_eq!(
        contract.assumptions.scheduling.family_rule,
        "deterministic_step_execution"
    );
    assert_eq!(contract.units.len(), 1);
    assert_eq!(contract.units[0].iteration_count, Some(5));
}
