use frog_reference_runtime_rust::contract::BackendContract;
use frog_reference_runtime_rust::execute::execute_contract;

#[test]
fn slice05_published_contract_accumulates_five_times() {
    let raw = include_str!(
        "../../../ContractEmitter/examples/05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json"
    );

    let contract: BackendContract =
        serde_json::from_str(raw).expect("published slice 05 contract must deserialize");

    let result = execute_contract(&contract, Some(3)).expect("runtime must execute published contract");

    assert_eq!(result.status, "ok");
    assert_eq!(result.contract_ref.backend_family, "reference_host_runtime_ui_binding");
    assert_eq!(result.contract_ref.source_ref.example_id, "05_bounded_ui_accumulator");
    assert_eq!(result.execution_summary.iterations, 5);
    assert_eq!(result.execution_summary.initial_state, 0);
    assert_eq!(result.execution_summary.final_state, 15);

    assert_eq!(result.outputs.public["result"], serde_json::json!(15));
    assert_eq!(result.outputs.ui["ctrl_input"], serde_json::json!(3));
    assert_eq!(result.outputs.ui["ind_result"], serde_json::json!(15));

    assert_eq!(result.ui_runtime.widgets.len(), 2);
    assert_eq!(result.ui_runtime.applied_widget_references.len(), 2);

    let ctrl_widget = result
        .ui_runtime
        .widgets
        .iter()
        .find(|w| w.widget_id == "ctrl_input")
        .expect("ctrl_input widget state must exist");
    assert_eq!(ctrl_widget.runtime.value, serde_json::json!(3));
    assert_eq!(ctrl_widget.runtime.face_color.as_deref(), Some("#D8E6FF"));

    let ind_widget = result
        .ui_runtime
        .widgets
        .iter()
        .find(|w| w.widget_id == "ind_result")
        .expect("ind_result widget state must exist");
    assert_eq!(ind_widget.runtime.value, serde_json::json!(15));
    assert_eq!(ind_widget.runtime.face_color.as_deref(), Some("#D8E6FF"));
}
