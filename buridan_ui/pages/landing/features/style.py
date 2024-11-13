from dataclasses import dataclass, field
import reflex as rx


@dataclass
class FeaturesStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "display": "grid",
            "grid_template_columns": [
                f"repeat({i}, minmax(0, 1fr))" for i in [1, 1, 2, 2, 2, 4]
            ],
            "gap": "2rem",
            "overflow": "hidden",
        }
    )

    base_item: dict[str, str | dict] = field(
        default_factory=lambda: {
            "spacing": "1",
            "position": "relative",
            "padding": "0.5rem",
            "::before": {
                "content": "''",
                "position": "absolute",
                "z-index": "1",
                "inline-size": "1px",
                "block-size": "100vh",
                "inset-inline-start": "-1rem",
                "background-color": rx.color("gray", 5),
            },
            "::after": {
                "content": "''",
                "position": "absolute",
                "background-color": rx.color("gray", 5),
                "z-index": "1",
                "inline-size": "100vw",
                "block-size": "1px",
                "inset-block-start": "-1rem",
            },
        },
    )


FeaturesStyle: FeaturesStyle = FeaturesStyle()
