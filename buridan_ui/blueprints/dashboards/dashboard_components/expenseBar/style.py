from dataclasses import dataclass, field

import reflex as rx


@dataclass
class DashboardExpenseBarStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "height": "100%",
            "padding": "1em",
            "grid_column": "span 3",
            "border_radius": "8px",
            "background": rx.color("gray", 2),
            "border": f"1px solid {rx.color('gray', 4)}",
        },
    )


DashboardExpenseBarStyle: DashboardExpenseBarStyle = DashboardExpenseBarStyle()
