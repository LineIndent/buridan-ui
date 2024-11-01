from dataclasses import dataclass, field

import reflex as rx


@dataclass
class BaseWrapperStyle:
    grandparent: dict[str, str] = field(
        default_factory=lambda: {
            "spacing": "0",
            "width": "100%",
            "height": "100vh",
            "overflow": "scroll",
            "scrollbar_width": "thin",
            "background": rx.color("gray", 2),
            "overscroll_behavior_y": "contain",
        }
    )

    parent: dict[str, str] = field(
        default_factory=lambda: {
            "spacing": "0",
            "width": "100%",
            "height": "100vh",
            "overflow": "auto",
            "scrollbar_width": "thin",
            "background": rx.color("gray", 2),
        }
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "z_index": "5",
            "width": "100%",
            "spacing": "9",
            "padding": "54px 0px 0px 0px",
            "position": "relative",
            "transition": "all 350ms ease",
            "background": rx.color("gray", 3),
        }
    )

    header: dict[str, str] = field(
        default_factory=lambda: {
            "top": "0",
            "left": "0",
            "spacing": "2",
            "width": "100%",
            "align": "center",
            "min_height": "25vh",
            "justify": "center",
            "background": rx.color("gray", 2),
            "border_left": f"1px solid {rx.color('gray', 4)}",
        }
    )


BaseWrapperStyle: BaseWrapperStyle = BaseWrapperStyle()
