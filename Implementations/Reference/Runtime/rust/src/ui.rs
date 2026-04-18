#[derive(Debug, Clone)]
pub struct NumericControl {
    pub widget_id: String,
    pub value: u16,
}

#[derive(Debug, Clone)]
pub struct NumericIndicator {
    pub widget_id: String,
    pub value: u16,
    pub foreground_color: Option<String>,
}

impl NumericIndicator {
    pub fn write_foreground_color(&mut self, color: String) {
        self.foreground_color = Some(color);
    }
}
