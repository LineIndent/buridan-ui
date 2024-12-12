from reflex.components.radix.themes.layout.stack import VStack
from dataclasses import dataclass, field
import reflex as rx


@dataclass
class Style:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "20em",
            "align": "center",
            "justify": "center",
            "position": "relative",
        }
    )

    fade: dict[str, str] = field(
        default_factory=lambda: {
            "position": "relative",
            "animation": "shakeEffect 0.5s ease-in-out infinite",
            "@keyframes shakeEffect": {
                "0%": {"transform": "translateX(0)"},
                "25%": {"transform": "translateX(-10px)"},
                "50%": {"transform": "translateX(10px)"},
                "75%": {"transform": "translateX(-10px)"},
                "100%": {"transform": "translateX(0)"},
            },
        }
    )


Style: Style = Style()


def animation_v6() -> VStack:
    return rx.vstack(
        rx.heading(
            "buridan/ui",
            size="5",
            font_weight="900",
            **Style.fade,
        ),
        **Style.base,
    )
