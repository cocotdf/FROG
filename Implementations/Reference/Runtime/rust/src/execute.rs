
use crate::contract::{BackendContract, ExecutionResult};
use crate::diagnostics::RuntimeError;
use crate::runtime::RuntimeContext;

pub fn execute_contract(
    contract: &BackendContract,
    control_value_override: Option<u16>,
) -> Result<ExecutionResult, RuntimeError> {
    if contract.contract_family != "reference_host_runtime_ui_binding" {
        return Err(RuntimeError::UnsupportedContractFamily(
            contract.contract_family.clone(),
        ));
    }

    let iterations = contract
        .bounded_loop_iterations
        .ok_or(RuntimeError::MissingField("bounded_loop_iterations"))?;

    if iterations != 5 {
        return Err(RuntimeError::Execution(format!(
            "this minimal runtime only supports 5 iterations for slice 05, got {iterations}"
        )));
    }

    let control_value = control_value_override.unwrap_or(0);
    let initial_state = contract.initial_state.unwrap_or(0);

    let mut ctx = RuntimeContext::new(initial_state);

    for _ in 0..iterations {
        ctx.state_next = ctx
            .state_current
            .checked_add(control_value)
            .ok_or_else(|| RuntimeError::Execution("u16 overflow during accumulation".into()))?;
        ctx.commit();
    }

    Ok(ExecutionResult {
        control_value,
        iterations,
        final_state: ctx.state_current,
        output_value: ctx.state_current,
        indicator_value: ctx.state_current,
    })
}
