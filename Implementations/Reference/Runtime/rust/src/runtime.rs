#[derive(Debug, Clone)]
pub struct RuntimeContext {
    pub state_current: u16,
    pub state_next: u16,
}

impl RuntimeContext {
    pub fn new(initial_state: u16) -> Self {
        Self {
            state_current: initial_state,
            state_next: initial_state,
        }
    }

    pub fn commit(&mut self) {
        self.state_current = self.state_next;
    }
}
