from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Optional

import tkinter as tk
from tkinter import ttk


SUPPORTED_WIDGET_CLASSES = {
    "frog.widgets.panel",
    "frog.widgets.numeric_control",
    "frog.widgets.numeric_indicator",
    "frog.widgets.label",
}


@dataclass
class WidgetInstance:
    instance_id: str
    class_ref: str
    role: str
    layout: Dict[str, Any]
    properties: Dict[str, Any] = field(default_factory=dict)
    parts: Dict[str, Any] = field(default_factory=dict)
    visual: Dict[str, Any] = field(default_factory=dict)
    default_properties: Dict[str, Any] = field(default_factory=dict)

    frame: Optional[tk.Frame] = None
    label_widget: Optional[tk.Label] = None
    value_widget: Optional[tk.Widget] = None
    tk_variable: Optional[tk.StringVar] = None

    def get_property(self, name: str) -> Any:
        return self.properties.get(name)

    def set_property(self, name: str, value: Any) -> None:
        self.properties[name] = value

    def reset_to_default_style(self) -> None:
        self.properties["face_color"] = self.default_properties.get("face_color", "#DDDDDD")
        self.properties["visible"] = self.default_properties.get("visible", True)
        self.properties["enabled"] = self.default_properties.get("enabled", True)
        self.properties["label"] = self.default_properties.get("label", "")
        self.sync_to_view()

    def sync_to_view(self) -> None:
        if self.frame is None:
            return

        visible = bool(self.properties.get("visible", True))
        enabled = bool(self.properties.get("enabled", True))
        face_color = str(self.properties.get("face_color", "#DDDDDD"))
        label_text = str(self.properties.get("label", ""))

        if visible:
            self.frame.place(
                x=int(self.layout.get("x", 0)),
                y=int(self.layout.get("y", 0)),
                width=int(self.layout.get("width", 100)),
                height=int(self.layout.get("height", 60)),
            )
        else:
            self.frame.place_forget()

        self.frame.configure(bg=face_color)

        if self.label_widget is not None:
            self.label_widget.configure(text=label_text, bg=face_color)

        if self.class_ref == "frog.widgets.label":
            if self.value_widget is not None:
                self.value_widget.configure(text=label_text, bg=face_color)
            return

        state = "normal" if enabled else "disabled"

        if self.class_ref == "frog.widgets.numeric_control":
            if self.value_widget is not None:
                try:
                    self.value_widget.configure(state=state)
                except tk.TclError:
                    pass

                if self.tk_variable is not None:
                    self.tk_variable.set(str(self.properties.get("value", 0)))

        elif self.class_ref == "frog.widgets.numeric_indicator":
            if self.value_widget is not None:
                self.value_widget.configure(text=str(self.properties.get("value", 0)), bg="#F8FFF0")


class FrogUIRuntime:
    def __init__(self, wfrog_path: str | Path) -> None:
        self.wfrog_path = Path(wfrog_path).resolve()
        self.package_dir = self.wfrog_path.parent

        self.root: Optional[tk.Tk] = None
        self.widgets: Dict[str, WidgetInstance] = {}
        self.panel_spec: Dict[str, Any] = {}

    def load_package(self) -> None:
        with self.wfrog_path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        if data.get("format") != "frog.wfrog":
            raise ValueError("Unsupported widget package format")

        if data.get("kind") != "front_panel_package":
            raise ValueError("Only front_panel_package is supported by this runtime")

        panels = data.get("front_panels", [])
        if not panels:
            raise ValueError("No front_panels section found in package")

        self.panel_spec = panels[0]
        self.widgets.clear()

        for widget_data in self.panel_spec.get("widgets", []):
            class_ref = widget_data.get("class_ref", "")
            if class_ref not in SUPPORTED_WIDGET_CLASSES:
                raise ValueError(f"Unsupported widget class: {class_ref}")

            instance_id = str(widget_data["instance_id"])
            initial_properties = dict(widget_data.get("initial_properties", {}))

            widget = WidgetInstance(
                instance_id=instance_id,
                class_ref=class_ref,
                role=str(widget_data.get("role", "")),
                layout=dict(widget_data.get("layout", {})),
                properties=dict(initial_properties),
                parts=dict(widget_data.get("parts", {})),
                visual=dict(widget_data.get("visual", {})),
                default_properties=dict(initial_properties),
            )
            self.widgets[instance_id] = widget

    def build_window(self) -> None:
        if not self.panel_spec:
            raise RuntimeError("Package must be loaded before building the window")

        self.root = tk.Tk()
        self.root.title(str(self.panel_spec.get("title", "FROG UI Runtime")))

        size = self.panel_spec.get("size", {})
        width = int(size.get("width", 640))
        height = int(size.get("height", 240))
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)
        self.root.configure(bg="#F4F6F8")

        for widget in self.widgets.values():
            self._create_widget_view(widget)

        run_button = ttk.Button(self.root, text="Run Example 05", command=self.run_example_05)
        run_button.place(x=528, y=40, width=96, height=36)

        reset_button = ttk.Button(self.root, text="Reset Style", command=self.reset_all_styles)
        reset_button.place(x=528, y=84, width=96, height=36)

    def _create_widget_view(self, widget: WidgetInstance) -> None:
        assert self.root is not None

        face_color = str(widget.properties.get("face_color", "#DDDDDD"))

        frame = tk.Frame(self.root, bg=face_color, bd=1, relief="solid", highlightthickness=0)
        widget.frame = frame

        layout = widget.layout
        frame.place(
            x=int(layout.get("x", 0)),
            y=int(layout.get("y", 0)),
            width=int(layout.get("width", 100)),
            height=int(layout.get("height", 60)),
        )

        label = tk.Label(
            frame,
            text=str(widget.properties.get("label", "")),
            anchor="w",
            bg=face_color,
            fg="#FFFFFF" if widget.class_ref != "frog.widgets.label" else "#202020",
            font=("Segoe UI", 10, "bold"),
        )
        label.place(x=10, y=8, width=max(int(layout.get("width", 100)) - 20, 40), height=20)
        widget.label_widget = label

        if widget.class_ref == "frog.widgets.numeric_control":
            var = tk.StringVar(value=str(widget.properties.get("value", 0)))
            entry = tk.Entry(frame, textvariable=var, font=("Consolas", 14))
            entry.place(x=10, y=40, width=max(int(layout.get("width", 100)) - 20, 40), height=28)
            widget.value_widget = entry
            widget.tk_variable = var

        elif widget.class_ref == "frog.widgets.numeric_indicator":
            value_label = tk.Label(
                frame,
                text=str(widget.properties.get("value", 0)),
                anchor="w",
                bg="#F8FFF0",
                fg="#1E1E1E",
                font=("Consolas", 14, "bold"),
                relief="solid",
                bd=1,
            )
            value_label.place(x=10, y=40, width=max(int(layout.get("width", 100)) - 20, 40), height=28)
            widget.value_widget = value_label

        elif widget.class_ref == "frog.widgets.label":
            value_label = tk.Label(
                frame,
                text=str(widget.properties.get("label", "")),
                anchor="w",
                bg=face_color,
                fg="#202020",
                font=("Segoe UI", 10),
            )
            value_label.place(x=0, y=0, width=int(layout.get("width", 100)), height=int(layout.get("height", 24)))
            widget.value_widget = value_label
            if widget.label_widget is not None:
                widget.label_widget.place_forget()
                widget.label_widget = None

        elif widget.class_ref == "frog.widgets.panel":
            panel_title = tk.Label(
                frame,
                text=str(widget.properties.get("label", "")),
                anchor="w",
                bg=face_color,
                fg="#1E1E1E",
                font=("Segoe UI", 10, "bold"),
            )
            panel_title.place(x=8, y=6, width=max(int(layout.get("width", 100)) - 16, 40), height=20)
            widget.value_widget = panel_title
            if widget.label_widget is not None:
                widget.label_widget.place_forget()
                widget.label_widget = None
            frame.lower()

        widget.sync_to_view()

    def property_read(self, widget_id: str, member: str, part: Optional[str] = None) -> Any:
        widget = self._get_widget(widget_id)
        self._validate_property(member, part)
        return widget.get_property(member)

    def property_write(self, widget_id: str, member: str, value: Any, part: Optional[str] = None) -> None:
        widget = self._get_widget(widget_id)
        self._validate_property(member, part)

        if member == "value":
            if widget.class_ref == "frog.widgets.numeric_indicator":
                widget.set_property("value", int(value))
            elif widget.class_ref == "frog.widgets.numeric_control":
                widget.set_property("value", int(value))
            else:
                raise ValueError(f"'value' is not supported on class {widget.class_ref}")
        elif member in {"label", "visible", "enabled", "face_color"}:
            widget.set_property(member, value)
        else:
            raise ValueError(f"Unsupported property: {member}")

        widget.sync_to_view()

    def method_invoke(self, widget_id: str, method_name: str, part: Optional[str] = None) -> None:
        widget = self._get_widget(widget_id)

        if part is not None and part not in widget.parts:
            raise ValueError(f"Unknown widget part '{part}' for widget '{widget_id}'")

        if method_name == "focus":
            if widget.value_widget is not None:
                try:
                    widget.value_widget.focus_set()
                except tk.TclError:
                    pass
        elif method_name == "reset_to_default_style":
            widget.reset_to_default_style()
        else:
            raise ValueError(f"Unsupported method: {method_name}")

    def run_example_05(self) -> int:
        input_widget = self._get_widget("ctrl_input")
        result_widget = self._get_widget("ind_result")
        status_widget = self._get_widget("lbl_status")

        input_value = self._read_control_value(input_widget)

        state = 0
        iterations = 5
        for _ in range(iterations):
            state = state + input_value

        self.property_write("ind_result", "value", state)
        self.property_write("ind_result", "face_color", "#70AD47")
        self.property_write("ctrl_input", "face_color", "#5B9BD5")
        self.property_write("lbl_status", "label", f"Status: executed with input={input_value}, result={state}")

        return state

    def reset_all_styles(self) -> None:
        for widget in self.widgets.values():
            widget.reset_to_default_style()
        self.property_write("lbl_status", "label", "Status: ready")

    def mainloop(self) -> None:
        if self.root is None:
            raise RuntimeError("Window has not been built")
        self.root.mainloop()

    def _get_widget(self, widget_id: str) -> WidgetInstance:
        if widget_id not in self.widgets:
            raise ValueError(f"Unknown widget instance: {widget_id}")
        return self.widgets[widget_id]

    def _validate_property(self, member: str, part: Optional[str]) -> None:
        supported_properties = {"value", "label", "visible", "enabled", "face_color"}
        if member not in supported_properties:
            raise ValueError(f"Unsupported property '{member}'")

        if part is not None and part not in {"root", "label", "value_display"}:
            raise ValueError(f"Unsupported widget part '{part}'")

    def _read_control_value(self, widget: WidgetInstance) -> int:
        if widget.class_ref != "frog.widgets.numeric_control":
            raise ValueError(f"Widget '{widget.instance_id}' is not a numeric_control")

        raw = widget.properties.get("value", 0)
        if widget.tk_variable is not None:
            raw = widget.tk_variable.get()

        try:
            value = int(raw)
        except (TypeError, ValueError):
            value = 0

        if value < 0:
            value = 0
        if value > 65535:
            value = 65535

        widget.set_property("value", value)
        widget.sync_to_view()
        return value


def build_runtime(wfrog_path: str | Path) -> FrogUIRuntime:
    runtime = FrogUIRuntime(wfrog_path)
    runtime.load_package()
    runtime.build_window()
    return runtime
