from dataclasses import dataclass, field
import reflex as rx


@dataclass
class ChangelogStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "min_height": "100vh",
            "background": rx.color("gray", 2),
            "align": "center",
        }
    )

    header: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "30vh",
            "max_width": "35em",
            "align": "start",
            "justify": "center",
            "padding": ["0px 24px" if i <= 2 else "0px 0px" for i in range(6)],
        },
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "max_width": "35em",
            "height": "100%",
            "justify": "end",
            "position": "relative",
            "padding": "1em 1em",
            "spacing": "8",
            "border_left": f"1px solid {rx.color('gray', 6)}",
        },
    )

    blip: dict[str, str] = field(
        default_factory=lambda: {
            "width": "24px",
            "height": "24px",
            "border_radius": "24px",
            "background": rx.color("gray", 3),
            "border": f"1.25px solid {rx.color('gray', 6)}",
            "position": "absolute",
            "left": "-11.5px",
            "align_items": "center",
            "justify_content": "center",
            "display": "flex",
        }
    )

    wrapper: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "align": "start",
            "justify": "start",
            "padding_left": "24px",
            "border_radius": "0px 5px 5px 0px",
        }
    )


ChangelogStyle: ChangelogStyle = ChangelogStyle()
