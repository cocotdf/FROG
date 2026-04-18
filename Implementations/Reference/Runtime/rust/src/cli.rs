use std::fs;
use std::path::PathBuf;

use crate::contract::BackendContract;
use crate::diagnostics::RuntimeError;
use crate::execute::execute_contract;

fn default_contract_path() -> PathBuf {
    PathBuf::from(env!("CARGO_MANIFEST_DIR"))
        .join("../../ContractEmitter/examples/05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json")
}

pub fn run_cli() -> Result<(), RuntimeError> {
    let mut args = std::env::args().skip(1);
    let control_value = match args.next() {
        Some(v) => v
            .parse::<u16>()
            .map(Some)
            .map_err(|_| RuntimeError::Usage("control_value must be a valid u16".into()))?,
        None => Some(3),
    };

    let contract_path = args.next().map(PathBuf::from).unwrap_or_else(default_contract_path);

    let raw = fs::read_to_string(&contract_path)?;
    let contract: BackendContract = serde_json::from_str(&raw)?;
    let result = execute_contract(&contract, control_value)?;
    println!("{}", serde_json::to_string_pretty(&result)?);
    Ok(())
}
