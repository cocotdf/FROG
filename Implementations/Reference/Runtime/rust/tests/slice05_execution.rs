use frog_reference_runtime_rust::contract::BackendContract;
use frog_reference_runtime_rust::execute::execute_contract;

#[test]
fn slice05_accumulates_five_times() {
    let contract = BackendContract {
        contract_family: "reference_host_runtime_ui_binding".into(),
        example_id: Some("05_bounded_ui_accumulator".into()),
        bounded_loop_iterations: Some(5),
        control_widget_id: Some("input_value".into()),
        indicator_widget_id: Some("result_indicator".into()),
        output_id: Some("result".into()),
        supports_face_color_write: Some(true),
        initial_state: Some(0),
    };

    let result = execute_contract(&contract, Some(3)).unwrap();
    assert_eq!(result.final_state, 15);
    assert_eq!(result.output_value, 15);
    assert_eq!(result.indicator_value, 15);
}
