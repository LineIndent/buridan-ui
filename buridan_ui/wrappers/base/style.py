from dataclasses import dataclass, field

import reflex as rx


@dataclass
class BaseWrapperStyle:
    parent: dict[str, str] = field(
        default_factory=lambda: {
            "spacing": "0",
            "width": "100%",
            "scrollbar_width": "thin",
            "background": rx.color("gray", 2),
            "height": ["100%" if i == 0 else "100vh" for i in range(6)],
        }
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "z_index": "5",
            "width": "100%",
            "spacing": "9",
            "padding": "54px 0px 0px 0px",
            "position": "relative",
            "transition": "all 350ms ease",
        }
    )

    header: dict[str, str] = field(
        default_factory=lambda: {
            "top": "0",
            "left": "0",
            "spacing": "2",
            "width": "100%",
            "align": "center",
            "min_height": "25vh",
            "justify": "center",
        }
    )

    background: dict[str, str] = field(
        default_factory=lambda: {
            "background_size": "28px 28px",
            "background_image": f"radial-gradient(circle, {rx.color('slate', 12)} 0.75px, transparent 1px)",
            "mask": (
                "radial-gradient(45% 45% at 50% 50%, hsl(0, 0%, 0%, 0.60), hsl(0, 0%, 0%, 0)), "
                "radial-gradient(60% 70% at 50% 50%, hsl(0, 0%, 0%, 0.35), hsl(0, 0%, 0%, 0))"
            ),
            "width": "100%",
            "height": "50vh",
            "position": "absolute",
            "top": "0",
            "left": "0",
            "z_index": "-2",
        }
    )


BaseWrapperStyle: BaseWrapperStyle = BaseWrapperStyle()
