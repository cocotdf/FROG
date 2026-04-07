use serde::{Deserialize, Serialize};
use serde_json::Value;

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct BackendContract {
    pub artifact_kind: String,
    pub artifact_version: String,
    pub backend_family: String,
    pub producer: ProducerInfo,
    pub compatibility: String,
    pub source_ref: SourceRef,
    pub assumptions: ContractAssumptions,
    pub units: Vec<ContractUnit>,
    pub unsupported: Vec<Value>,
    pub diagnostics: Vec<RuntimeDiagnostic>,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct ProducerInfo {
    pub implementation: String,
    pub implementation_kind: String,
    pub version: String,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct SourceRef {
    pub example_id: String,
    pub path: String,
    pub entry_unit: String,
    pub spec_version: String,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct ContractAssumptions {
    pub runtime_family: RuntimeFamilyAssumptions,
    pub scheduling: SchedulingAssumptions,
    pub execution_start: ExecutionStartAssumptions,
    pub numeric_behavior: NumericBehaviorAssumptions,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct RuntimeFamilyAssumptions {
    pub name: String,
    pub host_model: String,
    pub ui_binding: UiBindingAssumptions,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct UiBindingAssumptions {
    pub widget_value_binding: bool,
    pub widget_reference_binding: bool,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct SchedulingAssumptions {
    pub family_rule: String,
    pub parallelism_claim: String,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct ExecutionStartAssumptions {
    pub input_binding_complete: bool,
    pub ui_host_available: bool,
    pub initial_state_materialized: bool,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct NumericBehaviorAssumptions {
    pub value_domain: String,
    pub overflow_behavior: String,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct ContractUnit {
    pub unit_id: String,
    pub kind: String,
    pub public_interface: PublicInterface,
    pub ui_binding: UnitUiBinding,
    pub state_model: StateModel,
    pub execution_model: ExecutionModel,
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
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct UnitUiBinding {
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
    pub public_input_id: Option<String>,
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
    pub iteration_variable: String,
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
pub struct RuntimeDiagnostic {
    pub severity: String,
    pub kind: String,
    pub message: String,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct ExecutionResult {
    pub artifact_kind: String,
    pub artifact_version: String,
    pub status: String,
    pub contract_ref: ContractRef,
    pub execution_summary: ExecutionSummary,
    pub outputs: ExecutionOutputs,
    pub ui_runtime: UiRuntimeState,
    pub diagnostics: Vec<RuntimeDiagnostic>,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct ContractRef {
    pub unit_ids: Vec<String>,
    pub backend_family: String,
    pub source_ref: SourceRef,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct ExecutionSummary {
    pub mode: String,
    pub executed_unit: String,
    pub iterations: u32,
    pub state_initialized: bool,
    pub initial_state: u16,
    pub final_state: u16,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct ExecutionOutputs {
    pub public: serde_json::Map<String, Value>,
    pub ui: serde_json::Map<String, Value>,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct UiRuntimeState {
    pub widgets: Vec<RuntimeWidget>,
    pub applied_widget_references: Vec<AppliedWidgetReference>,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct RuntimeWidget {
    pub widget_id: String,
    pub runtime: RuntimeWidgetState,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct RuntimeWidgetState {
    pub value: Value,
    pub face_color: Option<String>,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct AppliedWidgetReference {
    pub widget_id: String,
    pub member: String,
    pub value: Value,
}
