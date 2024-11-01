from dataclasses import dataclass, field


@dataclass
class LandingPageNavigationStyle:
    style: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "align": "center",
            "justify": "between",
            "padding": ["24px 0px" if i >= 4 else "24px 24px" for i in range(6)],
            "backdrop_filter": "blur(2.5px)",
        }
    )


LandingPageNavigationStyle: LandingPageNavigationStyle = LandingPageNavigationStyle()
