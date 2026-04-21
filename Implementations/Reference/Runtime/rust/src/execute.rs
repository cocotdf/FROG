use std::path::{Path, PathBuf};

use serde_json::Value;

use crate::contract::{default_contract_path, default_wfrog_path};
use crate::diagnostics::Result;
use crate::runtime::RuntimeCore;

pub fn execute_contract(
    input_value: u16,
    contract_path: Option<PathBuf>,
    wfrog_path: Option<PathBuf>,
) -> Result<Value> {
    let contract = contract_path.unwrap_or(default_contract_path()?);
    let wfrog = wfrog_path.unwrap_or(default_wfrog_path()?);
    let mut runtime = RuntimeCore::from_paths(contract, wfrog)?;
    runtime.execute(Some(input_value))
}
