use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct BackendContract {
    pub contract_family: String,
    pub example_id: Option<String>,
    pub bounded_loop_iterations: Option<u32>,
    pub control_widget_id: Option<String>,
    pub indicator_widget_id: Option<String>,
    pub output_id: Option<String>,
    pub supports_face_color_write: Option<bool>,
    pub initial_state: Option<u16>,
}

#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct ExecutionResult {
    pub control_value: u16,
    pub iterations: u32,
    pub final_state: u16,
    pub output_value: u16,
    pub indicator_value: u16,
}
