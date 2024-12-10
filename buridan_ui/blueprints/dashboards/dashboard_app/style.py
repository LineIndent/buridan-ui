from dataclasses import dataclass, field


@dataclass
class DashboardAppStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "100vh",
            "spacing": "0",
            "overscroll_behavior": "none",
        },
    )

    contentArea: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "100%",
            "position": "relative",
            "overflow": "scroll",
            "spacing": "2",
        },
    )

    trafficAndExpenses: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "100%",
            "display": "grid",
            "grid_template_columns": [
                f"repeat({i}, minmax(0, 1fr))" for i in [1, 1, 1, 1, 3, 3]
            ],
            "padding": "1em",
            "row_gap": "1em",
            "column_gap": "1em",
        },
    )


DashboardAppStyle: DashboardAppStyle = DashboardAppStyle()
