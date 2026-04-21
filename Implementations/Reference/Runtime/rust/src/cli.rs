use std::path::PathBuf;

use serde_json::to_string_pretty;

use crate::contract::{default_contract_path, default_wfrog_path};
use crate::diagnostics::{Result, RuntimeError};
use crate::execute::execute_contract;
use crate::ui::BrowserUiRuntime;

pub fn run_cli() -> Result<()> {
    let mut args = std::env::args().skip(1).collect::<Vec<String>>();
    if args.first().map(|value| value.as_str()) == Some("ui") {
        args.remove(0);
        let mut contract_path: Option<PathBuf> = None;
        let mut wfrog_path: Option<PathBuf> = None;
        let mut host = "127.0.0.1".to_string();
        let mut port: u16 = 0;
        let mut open_browser = true;

        let mut index = 0usize;
        while index < args.len() {
            match args[index].as_str() {
                "--contract" => {
                    index += 1;
                    contract_path = Some(PathBuf::from(args.get(index).ok_or_else(|| RuntimeError::Message("Missing --contract value.".to_string()))?));
                }
                "--wfrog" => {
                    index += 1;
                    wfrog_path = Some(PathBuf::from(args.get(index).ok_or_else(|| RuntimeError::Message("Missing --wfrog value.".to_string()))?));
                }
                "--host" => {
                    index += 1;
                    host = args.get(index).cloned().ok_or_else(|| RuntimeError::Message("Missing --host value.".to_string()))?;
                }
                "--port" => {
                    index += 1;
                    port = args
                        .get(index)
                        .ok_or_else(|| RuntimeError::Message("Missing --port value.".to_string()))?
                        .parse::<u16>()?;
                }
                "--no-open-browser" => open_browser = false,
                value => return Err(RuntimeError::Message(format!("Unknown ui argument: {value}"))),
            }
            index += 1;
        }

        let runtime = BrowserUiRuntime::new(contract_path, wfrog_path)?;
        return runtime.serve(&host, port, open_browser);
    }

    let input_value = if args.is_empty() || args[0] == "run" {
        if !args.is_empty() && args[0] == "run" {
            args.remove(0);
        }
        if args.is_empty() {
            3u16
        } else {
            args.remove(0).parse::<u16>()?
        }
    } else {
        args.remove(0).parse::<u16>()?
    };

    let mut contract_path = default_contract_path()?;
    let mut wfrog_path = default_wfrog_path()?;
    let mut index = 0usize;
    while index < args.len() {
        match args[index].as_str() {
            "--contract" => {
                index += 1;
                contract_path = PathBuf::from(args.get(index).ok_or_else(|| RuntimeError::Message("Missing --contract value.".to_string()))?);
            }
            "--wfrog" => {
                index += 1;
                wfrog_path = PathBuf::from(args.get(index).ok_or_else(|| RuntimeError::Message("Missing --wfrog value.".to_string()))?);
            }
            value => return Err(RuntimeError::Message(format!("Unknown argument: {value}"))),
        }
        index += 1;
    }

    let artifact = execute_contract(input_value, Some(contract_path), Some(wfrog_path))?;
    println!("{}", to_string_pretty(&artifact).unwrap());
    Ok(())
}
