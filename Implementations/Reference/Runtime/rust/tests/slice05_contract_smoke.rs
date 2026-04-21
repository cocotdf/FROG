use frog_reference_runtime_rust::execute::execute_contract;

#[test]
fn slice05_contract_smoke() {
    let artifact = execute_contract(3, None, None).unwrap();
    assert_eq!(artifact["status"], "ok");
    assert_eq!(artifact["execution_summary"]["iterations"], 5);
    assert_eq!(artifact["execution_summary"]["final_state"], 15);
    assert_eq!(artifact["outputs"]["public"]["result"], 15);
}
