import reflex as rx

import asyncio

fade: dict[str, str] = {
    "position": "relative",
    f"@keyframes opacity": {
        "0%": {"opacity": "0"},
        "100%": {"opacity": "1"},
    },
    "animation": "opacity 1s",
}


class Animation(rx.State):
    animate: dict[str, str] = {}
    is_disabled: bool = False

    async def run_animation(self):
        if self.is_disabled:  # Prevent running if already animating
            return

        self.is_disabled = True
        self.animate = fade
        yield  # Allow the animation to apply

        await asyncio.sleep(1.1)  # Wait for the animation to finish
        self.is_disabled = False
        self.animate = {}  # Reset animation after completion


def animation_v1():
    return rx.vstack(
        rx.heading("buridan/ui", size="5", font_weight="900", style=Animation.animate),
        rx.button(
            "Run",
            top="-24px",
            right="-12px",
            cursor="pointer",
            position="absolute",
            loading=Animation.is_disabled,
            border_radius="0px 0px 0px 8px",
            on_click=Animation.run_animation,
        ),
        width="100%",
        height="20em",
        align="center",
        justify="center",
        position="relative",
    )
