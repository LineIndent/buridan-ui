from dataclasses import dataclass, field

import reflex as rx


@dataclass
class AppProfileWrapperStyle:
    blip: dict[str, str] = field(
        default_factory=lambda: {
            "width": "24px",
            "height": "24px",
            "border_radius": "24px",
            "background": rx.color("gray", 3),
            "border": f"1.25px solid {rx.color('gray', 6)}",
            "position": "absolute",
            "left": "-12px",
            "align_items": "center",
            "justify_content": "center",
            "display": "flex",
        },
    )

    wrapper: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "align": "start",
            "justify": "start",
            "padding_left": "5px",
            "border_radius": "0px 5px 5px 0px",
        },
    )


AppProfileWrapperStyle: AppProfileWrapperStyle = AppProfileWrapperStyle()
