use frog_reference_runtime_rust::ui::BrowserUiRuntime;

#[test]
fn slice05_runtime_renders_html_and_snapshot() {
    let runtime = BrowserUiRuntime::new(None, None).unwrap();
    let html = runtime.render_html();
    assert!(html.contains("Input"));
    assert!(html.contains("Accumulated result"));
    assert!(html.contains("/asset/numeric_control_svg"));
    assert!(html.contains("/asset/numeric_indicator_svg"));
}
