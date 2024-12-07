from dataclasses import dataclass, field
import reflex as rx


@dataclass
class LandingPageStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "min_height": "100vh",
            "align": "center",
            "spacing": "0",
            "background": rx.color("slate", 2),
        }
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "100%",
            "max_width": "75em",
            "position": "relative",
            "padding": ["0em 0.5em" if i <= 5 else "0em 0em" for i in range(6)],
        }
    )


LandingPageStyle: LandingPageStyle = LandingPageStyle()
