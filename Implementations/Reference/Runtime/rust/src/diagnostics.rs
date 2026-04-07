use thiserror::Error;

#[derive(Debug, Error)]
pub enum RuntimeError {
    #[error("{0}")]
    Usage(String),

    #[error("I/O error: {0}")]
    Io(#[from] std::io::Error),

    #[error("JSON error: {0}")]
    Json(#[from] serde_json::Error),

    #[error("unsupported contract family: {0}")]
    UnsupportedContractFamily(String),

    #[error("missing required field: {0}")]
    MissingField(&'static str),

    #[error("type mismatch: {0}")]
    TypeMismatch(String),

    #[error("execution error: {0}")]
    Execution(String),
}
