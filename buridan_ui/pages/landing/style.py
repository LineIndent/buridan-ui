from dataclasses import dataclass, field


@dataclass
class LandingPageStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "min_height": "100vh",
            "align": "center",
            "position": "relative",
        }
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "max_width": "90em",
        }
    )


LandingPageStyle: LandingPageStyle = LandingPageStyle()
