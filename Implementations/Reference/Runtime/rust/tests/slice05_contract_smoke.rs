use frog_reference_runtime_rust::contract::BackendContract;

#[test]
fn published_slice05_contract_deserializes_and_exposes_expected_shape() {
    let raw = include_str!(
        "../../../ContractEmitter/examples/05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json"
    );

    let contract: BackendContract =
        serde_json::from_str(raw).expect("published slice 05 contract must deserialize");

    assert_eq!(contract.artifact_kind, "frog_backend_contract");
    assert_eq!(contract.backend_family, "reference_host_runtime_ui_binding");
    assert_eq!(contract.source_ref.example_id, "05_bounded_ui_accumulator");
    assert_eq!(
        contract.source_ref.path,
        "Examples/05_bounded_ui_accumulator/main.frog"
    );
    assert_eq!(contract.source_ref.entry_unit, "main");
    assert_eq!(
        contract.assumptions.runtime_family.name,
        "reference_host_runtime_ui_binding"
    );
    assert_eq!(
        contract.assumptions.scheduling.family_rule,
        "deterministic_step_execution"
    );
    assert_eq!(contract.assumptions.numeric_behavior.value_domain, "u16");
    assert_eq!(contract.units.len(), 1);

    let unit = &contract.units[0];
    assert_eq!(unit.unit_id, "main");
    assert_eq!(unit.kind, "bounded_executable_ui_unit");
    assert_eq!(unit.public_interface.inputs.len(), 1);
    assert_eq!(unit.public_interface.inputs[0].id, "input_value");
    assert_eq!(unit.public_interface.inputs[0].port_type, "u16");
    assert_eq!(
        unit.public_interface.inputs[0].binding_origin.as_deref(),
        Some("widget.ctrl_input.value")
    );
    assert_eq!(unit.public_interface.outputs.len(), 1);
    assert_eq!(unit.public_interface.outputs[0].id, "result");
    assert_eq!(unit.public_interface.outputs[0].port_type, "u16");
    assert_eq!(
        unit.public_interface.outputs[0].binding_target.as_deref(),
        Some("interface.result")
    );
    assert_eq!(unit.execution_model.structure, "for_loop");
    assert_eq!(unit.execution_model.iteration_count, 5);
    assert_eq!(unit.state_model.explicit_state, true);
    assert_eq!(unit.state_model.carrier.primitive, "frog.core.delay");
    assert_eq!(unit.state_model.carrier.state_type, "u16");
    assert_eq!(unit.state_model.carrier.initial_value, 0);
    assert_eq!(unit.ui_binding.widgets.len(), 2);
    assert!(unit.ui_binding.package_refs.iter().any(|p| {
        p == "Examples/05_bounded_ui_accumulator/ui/accumulator_panel.wfrog"
    }));
    assert!(unit.ui_binding.widgets.iter().any(|w| {
        w.widget_id == "ctrl_input"
            && w.widget_class == "frog.widgets.numeric_control"
            && w.binding.public_input_id.as_deref() == Some("input_value")
    }));
    assert!(unit.ui_binding.widgets.iter().any(|w| {
        w.widget_id == "ind_result"
            && w.widget_class == "frog.widgets.numeric_indicator"
            && w.binding.public_output_id.as_deref() == Some("result")
    }));
    assert_eq!(unit.property_writes.len(), 2);
    assert!(unit
        .property_writes
        .iter()
        .all(|w| w.operation == "frog.ui.property_write" && w.member == "foreground_color"));
    assert!(unit
        .property_writes
        .iter()
        .any(|w| w.widget_id == "ctrl_input" && w.value.value == "#5B9BD5"));
    assert!(unit
        .property_writes
        .iter()
        .any(|w| w.widget_id == "ind_result" && w.value.value == "#70AD47"));
}
