#[derive(Debug, Clone)]
pub struct NumericControl {
    pub widget_id: String,
    pub value: u16,
}

#[derive(Debug, Clone)]
pub struct NumericIndicator {
    pub widget_id: String,
    pub value: u16,
    pub face_color: Option<String>,
}

impl NumericIndicator {
    pub fn write_face_color(&mut self, color: String) {
        self.face_color = Some(color);
    }
}
