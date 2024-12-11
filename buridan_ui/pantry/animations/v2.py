import asyncio
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
        },
    )

    button: dict[str, str] = field(
        default_factory=lambda: {
            "top": "-24px",
            "right": "-12px",
            "cursor": "pointer",
            "position": "absolute",
            "border_radius": "0px 0px 0px 8px",
        },
    )

    right: dict[str, str] = field(
        default_factory=lambda: {
            "position": "relative",
            "animation": "rightSlide 0.6s",
            "@keyframes rightSlide": {
                "from": {"right": "-300px", "opacity": "0"},
                "to": {"right": "0px", "opacity": "1"},
            },
        },
    )


Style: Style = Style()


class Animation(rx.State):
    animate: dict[str, str] = {}
    is_disabled: bool = False

    async def run_animation(self):
        if self.is_disabled:  # Prevent running if already animating
            return

        self.is_disabled = True
        self.animate = Style.right
        yield  # Allow the animation to apply

        await asyncio.sleep(1)  # Wait for the animation to finish
        self.is_disabled = False
        self.animate = {}  # Reset animation after completion


def animation_v2():
    return rx.vstack(
        rx.heading("buridan/ui", size="5", font_weight="900", style=Animation.animate),
        rx.button(
            "Run",
            loading=Animation.is_disabled,
            on_click=Animation.run_animation,
            **Style.button,
        ),
        **Style.base,
    )
