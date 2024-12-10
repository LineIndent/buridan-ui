from dataclasses import dataclass, field

import reflex as rx


@dataclass
class ComponentWrapperStyle:
    root: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "padding": "2px",
            "overflow": "hidden",
            "default_value": "1",
            "border_radius": "10px",
            "background": rx.color("gray", 3),
        },
    )

    shared: dict[str, str] = field(
        default_factory=lambda: {
            "margin_top": "5px",
            "display": "flex",
            "background": rx.color("gray", 2),
            "border_radius": "0px 0px 10px 10px",
        },
    )

    preview: dict[str, str] = field(
        default_factory=lambda: {
            "margin_top": "5px",
            "padding": "24px 12px",
            "align_items": "center",
            "justify_content": "center",
            "overflow": "hidden",
            "background": rx.color("gray", 2),
            "border_radius": "0px 0px 10px 10px",
        },
    )

    code: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "font_size": "12px",
            "language": "python",
            "wrap_long_lines": True,
            "scrollbar_width": "none",
            "code_tag_props": {"pre": "transparent"},
            "custom_style": {"backgroundColor": "transparent"},
        },
    )

    copy_button: dict[str, str] = field(
        default_factory=lambda: {
            "color_scheme": "gray",
            "variant": "ghost",
            "size": "1",
            "cursor": "pointer",
            "position": "absolute",
            "top": "24px",
            "right": "24px",
        },
    )


ComponentWrapperStyle: ComponentWrapperStyle = ComponentWrapperStyle()

InnerCode: dict[str, str] = {
    "align_items": "start",
    "position": "relative",
    "padding_right": "12px",
    "padding_top": "12px",
    "width": "100%",
    **ComponentWrapperStyle.shared,
}

PreviewNoCOde = {
    **ComponentWrapperStyle.preview,
    "border_radius": "10px",
    "margin": "0",
}
