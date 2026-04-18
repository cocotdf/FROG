use serde_json::{json, Map, Value};

use crate::contract::{
    AppliedWidgetReference, ArtifactReference, BackendContract, ContractRef, ExecutionOutputs,
    ExecutionResult, ExecutionSummary, RuntimeDiagnostic, RuntimeWidget, RuntimeWidgetState,
    UiRuntimeState,
};
use crate::diagnostics::RuntimeError;
use crate::runtime::RuntimeContext;

const SUPPORTED_WIDGET_MEMBER: &str = "foreground_color";
const SUPPORTED_COLOR_TYPE: &str = "frog.color.rgba8";

pub fn execute_contract(
    contract: &BackendContract,
    control_value_override: Option<u16>,
) -> Result<ExecutionResult, RuntimeError> {
    if contract.artifact_kind != "frog_backend_contract" {
        return Err(RuntimeError::Execution(
            "runtime expected artifact_kind = frog_backend_contract".into(),
        ));
    }

    if contract.backend_family != "reference_host_runtime_ui_binding" {
        return Err(RuntimeError::Execution(format!(
            "unsupported backend family: {}",
            contract.backend_family
        )));
    }

    if contract.assumptions.runtime_family.name != "reference_host_runtime_ui_binding" {
        return Err(RuntimeError::Execution(
            "runtime_family.name must match reference_host_runtime_ui_binding".into(),
        ));
    }

    if contract.assumptions.scheduling.family_rule != "deterministic_step_execution" {
        return Err(RuntimeError::Execution(format!(
            "unsupported scheduling rule: {}",
            contract.assumptions.scheduling.family_rule
        )));
    }

    if contract.units.len() != 1 {
        return Err(RuntimeError::Execution(format!(
            "this minimal runtime expects exactly one unit, got {}",
            contract.units.len()
        )));
    }

    let unit = &contract.units[0];

    if unit.kind != "bounded_executable_ui_unit" {
        return Err(RuntimeError::Execution(format!(
            "unsupported unit kind: {}",
            unit.kind
        )));
    }

    if unit.execution_model.structure != "for_loop" {
        return Err(RuntimeError::Execution(format!(
            "unsupported execution structure: {}",
            unit.execution_model.structure
        )));
    }

    let iterations = unit.execution_model.iteration_count;
    if iterations != 5 {
        return Err(RuntimeError::Execution(format!(
            "this minimal runtime only supports 5 iterations for slice 05, got {iterations}"
        )));
    }

    if !unit.state_model.explicit_state {
        return Err(RuntimeError::Execution(
            "explicit_state must be true for slice 05".into(),
        ));
    }

    if unit.state_model.carrier.primitive != "frog.core.delay" {
        return Err(RuntimeError::Execution(format!(
            "unsupported state carrier primitive: {}",
            unit.state_model.carrier.primitive
        )));
    }

    if unit.public_interface.inputs.len() != 1 || unit.public_interface.inputs[0].id != "input_value" {
        return Err(RuntimeError::Execution(
            "runtime expects one public input named input_value".into(),
        ));
    }

    if unit.public_interface.outputs.len() != 1 || unit.public_interface.outputs[0].id != "result" {
        return Err(RuntimeError::Execution(
            "runtime expects one public output named result".into(),
        ));
    }

    let initial_state = unit.state_model.carrier.initial_value;
    let control_value = control_value_override.unwrap_or(0);

    let control_widget = unit
        .ui_binding
        .widgets
        .iter()
        .find(|w| w.widget_id == "ctrl_input")
        .ok_or(RuntimeError::MissingField("ctrl_input widget"))?;

    let indicator_widget = unit
        .ui_binding
        .widgets
        .iter()
        .find(|w| w.widget_id == "ind_result")
        .ok_or(RuntimeError::MissingField("ind_result widget"))?;

    if control_widget.widget_class != "frog.widgets.numeric_control" {
        return Err(RuntimeError::Execution(
            "ctrl_input must use frog.widgets.numeric_control".into(),
        ));
    }
    if indicator_widget.widget_class != "frog.widgets.numeric_indicator" {
        return Err(RuntimeError::Execution(
            "ind_result must use frog.widgets.numeric_indicator".into(),
        ));
    }

    if control_widget.binding.mode != "widget_value"
        || control_widget.binding.public_input_id.as_deref() != Some("input_value")
    {
        return Err(RuntimeError::Execution(
            "ctrl_input must be bound as widget_value to public input input_value".into(),
        ));
    }

    if indicator_widget.binding.mode != "widget_value"
        || indicator_widget.binding.public_output_id.as_deref() != Some("result")
    {
        return Err(RuntimeError::Execution(
            "ind_result must be bound as widget_value to public output result".into(),
        ));
    }

    for support in &unit.ui_binding.widget_reference_support {
        if (support.widget_id == "ctrl_input" || support.widget_id == "ind_result")
            && !support.supported_members.iter().any(|member| member == SUPPORTED_WIDGET_MEMBER)
        {
            return Err(RuntimeError::Execution(format!(
                "widget {} must support {}",
                support.widget_id, SUPPORTED_WIDGET_MEMBER
            )));
        }
    }

    let mut ctrl_foreground_color: Option<String> = None;
    let mut ind_foreground_color: Option<String> = None;
    let mut applied_widget_references: Vec<AppliedWidgetReference> = Vec::new();

    for write in &unit.property_writes {
        if write.operation != "frog.ui.property_write" {
            return Err(RuntimeError::Execution(format!(
                "unsupported property write operation: {}",
                write.operation
            )));
        }

        if write.member != SUPPORTED_WIDGET_MEMBER {
            return Err(RuntimeError::Execution(format!(
                "unsupported property write member: {}",
                write.member
            )));
        }

        if write.value.value_type != SUPPORTED_COLOR_TYPE {
            return Err(RuntimeError::Execution(format!(
                "unsupported property write value type: {}",
                write.value.value_type
            )));
        }

        match write.widget_id.as_str() {
            "ctrl_input" => ctrl_foreground_color = Some(write.value.value.clone()),
            "ind_result" => ind_foreground_color = Some(write.value.value.clone()),
            other => {
                return Err(RuntimeError::Execution(format!(
                    "unsupported property write widget id: {other}"
                )))
            }
        }

        applied_widget_references.push(AppliedWidgetReference {
            widget_id: write.widget_id.clone(),
            member: write.member.clone(),
            value: json!({
                "type": write.value.value_type,
                "value": write.value.value
            }),
        });
    }

    let mut ctx = RuntimeContext::new(initial_state);

    for _ in 0..iterations {
        ctx.state_next = ctx
            .state_current
            .checked_add(control_value)
            .ok_or_else(|| RuntimeError::Execution("u16 overflow during accumulation".into()))?;
        ctx.commit();
    }

    let final_value = ctx.state_current;

    let mut public_outputs = Map::new();
    public_outputs.insert(
        unit.public_output_publication.output_id.clone(),
        Value::from(final_value),
    );

    let mut ui_outputs = Map::new();
    ui_outputs.insert("ctrl_input".into(), Value::from(control_value));
    ui_outputs.insert("ind_result".into(), Value::from(final_value));

    Ok(ExecutionResult {
        artifact_kind: "frog_runtime_result".into(),
        artifact_governance_ref: ArtifactReference {
            path: "Versioning/Readme.md".into(),
        },
        status: "ok".into(),
        contract_ref: ContractRef {
            unit_ids: vec![unit.unit_id.clone()],
            backend_family: contract.backend_family.clone(),
            source_ref: contract.source_ref.clone(),
        },
        execution_summary: ExecutionSummary {
            mode: "deterministic_step_execution".into(),
            executed_unit: unit.unit_id.clone(),
            iterations,
            state_initialized: true,
            initial_state,
            final_state: final_value,
        },
        outputs: ExecutionOutputs {
            public: public_outputs,
            ui: ui_outputs,
        },
        ui_runtime: UiRuntimeState {
            widgets: vec![
                RuntimeWidget {
                    widget_id: "ctrl_input".into(),
                    runtime: RuntimeWidgetState {
                        value: Value::from(control_value),
                        foreground_color: ctrl_foreground_color,
                    },
                },
                RuntimeWidget {
                    widget_id: "ind_result".into(),
                    runtime: RuntimeWidgetState {
                        value: Value::from(final_value),
                        foreground_color: ind_foreground_color,
                    },
                },
            ],
            applied_widget_references,
        },
        diagnostics: vec![RuntimeDiagnostic {
            severity: Some("info".into()),
            kind: Some("execution_completed".into()),
            message: "The reference Rust runtime completed deterministic execution.".into(),
        }],
    })
}
