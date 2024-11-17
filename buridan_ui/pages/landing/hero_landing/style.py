from dataclasses import dataclass, field


@dataclass
class HeroStyle:
    root: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "min_height": ["180vh", "170vh", "140vh", "120vh", "115vh", "110vh"],
            "justify": "center",
            "overflow": "hidden",
        }
    )

    body: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "inherit",
            "wrap": "wrap",
            "padding_top": "6em",
            "spacing": "8",
        }
    )

    header: dict[str, str] = field(
        default_factory=lambda: {
            "flex": ["100%" if i <= 2 else "45%" for i in range(6)],
            "position": "relative",
            "min_width": "350px",
        }
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "position": "relative",
            "flex": ["100%" if i <= 2 else "40%" for i in range(6)],
            "height": "inherit",
            "align": "end",
        }
    )

    components: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "inherit",
            "position": "absolute",
            "top": "0",
            "right": "0",
            "align": "end",
            "transform": [
                "translateX(30px)" if i <= 3 else "translateX(0px)" for i in range(6)
            ],
            "transition": "all 550ms ease",
        }
    )


HeroStyle: HeroStyle = HeroStyle()
