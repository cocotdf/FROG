use std::fs;
use std::path::PathBuf;

use crate::contract::BackendContract;
use crate::diagnostics::RuntimeError;
use crate::execute::execute_contract;

pub fn run_cli() -> Result<(), RuntimeError> {
    let mut args = std::env::args().skip(1);
    let contract_path = args
        .next()
        .map(PathBuf::from)
        .ok_or(RuntimeError::Usage(
            "usage: frog-reference-runtime-rust <contract.json> [control_value]".into(),
        ))?;

    let control_value = match args.next() {
        Some(v) => Some(v.parse::<u16>().map_err(|_| {
            RuntimeError::Usage("control_value must be a valid u16".into())
        })?),
        None => None,
    };

    let raw = fs::read_to_string(&contract_path)?;
    let contract: BackendContract = serde_json::from_str(&raw)?;
    let result = execute_contract(&contract, control_value)?;

    println!("{}", serde_json::to_string_pretty(&result)?);
    Ok(())
}
