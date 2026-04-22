use std::fs;
use std::path::{Path, PathBuf};

use serde::{Deserialize, Serialize};

use crate::diagnostics::{ensure, Result, RuntimeError};

pub const REFERENCE_BACKEND_FAMILY: &str = "reference_host_runtime_ui_binding";
pub const EXPECTED_OVERFLOW_BEHAVIOR: &str = "reject_execution_on_u16_overflow";

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct ArtifactReference {
    pub path: String,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct SourceRef {
    pub example_id: String,
    pub path: String,
    pub entry_unit: String,
}

#[derive(Debug, Clone, Deserialize, Serialize, Default)]
pub struct UiBindingAssumptions {
    #[serde(default)]
    pub widget_value_binding: bool,
    #[serde(default)]
    pub widget_reference_binding: bool,
}

#[derive(Debug, Clone, Deserialize, Serialize, Default)]
pub struct RuntimeFamilyAssumptions {
    #[serde(default)]
    pub name: String,
    #[serde(default)]
    pub host_model: String,
    #[serde(default)]
    pub ui_binding: UiBindingAssumptions,
}

#[derive(Debug, Clone, Deserialize, Serialize, Default)]
pub struct NumericBehaviorAssumptions {
    #[serde(default)]
    pub value_domain: String,
    #[serde(default)]
    pub overflow_behavior: String,
}

#[derive(Debug, Clone, Deserialize, Serialize, Default)]
pub struct ContractAssumptions {
    #[serde(default)]
    pub runtime_family: RuntimeFamilyAssumptions,
    #[serde(default)]
    pub numeric_behavior: NumericBehaviorAssumptions,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct BackendContract {
    pub artifact_kind: String,
    #[serde(default)]
    pub artifact_governance_ref: Option<ArtifactReference>,
    pub backend_family: String,
    pub source_ref: SourceRef,
    #[serde(default)]
    pub assumptions: ContractAssumptions,
    pub units: Vec<ContractUnit>,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct ContractUnit {
    pub unit_id: String,
    pub kind: String,
    pub public_interface: PublicInterface,
    pub ui_binding: UiBinding,
    pub state_model: StateModel,
    pub execution_model: ExecutionModel,
    #[serde(default)]
    pub property_writes: Vec<PropertyWrite>,
    pub public_output_publication: PublicOutputPublication,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct PublicInterface {
    pub inputs: Vec<InterfacePort>,
    pub outputs: Vec<InterfacePort>,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct InterfacePort {
    pub id: String,
    #[serde(rename = "type")]
    pub port_type: String,
    #[serde(default)]
    pub binding_origin: Option<String>,
    #[serde(default)]
    pub binding_target: Option<String>,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct UiBinding {
    #[serde(default)]
    pub package_refs: Vec<String>,
    pub widgets: Vec<WidgetBinding>,
    pub widget_reference_support: Vec<WidgetReferenceSupport>,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct WidgetBinding {
    pub widget_id: String,
    pub widget_class: String,
    pub value_type: String,
    pub role: String,
    pub binding: WidgetBindingMode,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct WidgetBindingMode {
    pub mode: String,
    #[serde(default)]
    pub public_input_id: Option<String>,
    #[serde(default)]
    pub public_output_id: Option<String>,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct WidgetReferenceSupport {
    pub widget_id: String,
    pub supported_members: Vec<String>,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct StateModel {
    pub explicit_state: bool,
    pub carrier: StateCarrier,
    pub commit_rule: String,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct StateCarrier {
    pub primitive: String,
    pub state_id: String,
    #[serde(rename = "type")]
    pub state_type: String,
    pub initial_value: u16,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct ExecutionModel {
    pub structure: String,
    pub iteration_count: u32,
    #[serde(default)]
    pub iteration_variable: Option<String>,
    pub body_rule: BodyRule,
    pub final_result_rule: String,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct BodyRule {
    pub kind: String,
    pub expression: String,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct PropertyWrite {
    pub operation: String,
    pub widget_id: String,
    pub member: String,
    pub value: PropertyWriteValue,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct PropertyWriteValue {
    #[serde(rename = "type")]
    pub value_type: String,
    pub value: String,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct PublicOutputPublication {
    pub output_id: String,
    pub source: String,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct WfrogPackage {
    pub format: String,
    pub kind: String,
    #[serde(default)]
    pub widget_classes: Vec<WidgetClass>,
    #[serde(default)]
    pub svg_assets: Vec<SvgAsset>,
    #[serde(default)]
    pub host_bindings: Vec<HostBinding>,
    pub front_panels: Vec<FrontPanel>,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct WidgetClass {
    pub class_id: String,
    #[serde(default)]
    pub properties: Vec<WidgetProperty>,
    #[serde(default)]
    pub methods: Vec<WidgetMethod>,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct WidgetProperty {
    pub name: String,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct WidgetMethod {
    pub name: String,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct SvgAsset {
    pub asset_id: String,
    pub path: String,
    pub kind: String,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct HostBinding {
    pub binding_id: String,
    pub target: String,
    #[serde(default)]
    pub required_capabilities: Vec<String>,
    #[serde(default)]
    pub optional_capabilities: Vec<String>,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct FrontPanel {
    pub panel_id: String,
    pub title: String,
    pub class_ref: String,
    pub layout: serde_json::Value,
    pub widgets: Vec<PanelWidget>,
    pub host_binding_ref: String,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct PanelWidget {
    pub instance_id: String,
    pub class_ref: String,
    pub layout: serde_json::Value,
    #[serde(default)]
    pub props: serde_json::Map<String, serde_json::Value>,
    #[serde(default)]
    pub visual: serde_json::Map<String, serde_json::Value>,
}

pub fn find_repo_root(start: &Path) -> Result<PathBuf> {
    for candidate in start.ancestors() {
        if candidate.join("Examples").is_dir() && candidate.join("Implementations").is_dir() {
            return Ok(candidate.to_path_buf());
        }
    }
    Err(RuntimeError::Message(
        "Unable to locate the repository root from the current path.".to_string(),
    ))
}

pub fn default_contract_path() -> Result<PathBuf> {
    let manifest_dir = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    let repo_root = find_repo_root(&manifest_dir)?;
    Ok(repo_root
        .join("Implementations")
        .join("Reference")
        .join("ContractEmitter")
        .join("examples")
        .join("05_bounded_ui_accumulator.reference_host_runtime_ui_binding.contract.json"))
}

pub fn default_wfrog_path() -> Result<PathBuf> {
    let manifest_dir = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    let repo_root = find_repo_root(&manifest_dir)?;
    Ok(repo_root
        .join("Examples")
        .join("05_bounded_ui_accumulator")
        .join("ui")
        .join("accumulator_panel.wfrog"))
}

pub fn load_contract_from_path(path: &Path) -> Result<BackendContract> {
    let text = fs::read_to_string(path)?;
    let contract: BackendContract = serde_json::from_str(&text)?;
    ensure(contract.artifact_kind == "frog_backend_contract", "Expected frog_backend_contract.")?;
    ensure(
        contract.backend_family == REFERENCE_BACKEND_FAMILY,
        format!("Unsupported backend family: {}", contract.backend_family),
    )?;
    Ok(contract)
}

pub fn load_wfrog_from_path(path: &Path) -> Result<WfrogPackage> {
    let text = fs::read_to_string(path)?;
    let package: WfrogPackage = serde_json::from_str(&text)?;
    ensure(package.format == "frog.wfrog", "Unsupported .wfrog format.")?;
    ensure(package.kind == "front_panel_package", "Only front_panel_package is supported.")?;
    Ok(package)
}
