from dataclasses import dataclass, field

import reflex as rx


@dataclass
class DashboardNavBarStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "top": "0",
            "left": "0",
            "width": "100%",
            "spacing": "4",
            "z_index": "2",
            "justify": "end",
            "align": "center",
            "position": "sticky",
            "padding": "0.75em 2em",
            "background": rx.color("gray", 2),
            "border_bottom": f"1px solid {rx.color('gray', 4)}",
        },
    )


DashboardNavBarStyle: DashboardNavBarStyle = DashboardNavBarStyle()
