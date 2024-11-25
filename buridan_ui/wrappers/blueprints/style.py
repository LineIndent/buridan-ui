from dataclasses import dataclass, field
import reflex as rx


@dataclass
class BlueprintWrapperStyle:
    root: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "padding": "2px",
            "overflow": "hidden",
            "default_value": "1",
            "border_radius": "10px",
            "background": rx.color("gray", 3),
        }
    )

    preview: dict[str, str] = field(
        default_factory=lambda: {
            "overflow": "hidden",
            "padding": "24px 12px",
            "align_items": "center",
            "border_radius": "10px",
            "justify_content": "center",
            "background": rx.color("gray", 2),
        }
    )


BlueprintWrapperStyle: BlueprintWrapperStyle = BlueprintWrapperStyle()
