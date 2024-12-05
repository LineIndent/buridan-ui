import reflex as rx
import re

from reflex.constants.colors import Color

PATTERN: str = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


class Animation(rx.State):
    value: str = ""

    position: str = "0"
    opacity: str = "0"
    background: str | Color = "none"

    async def run_animation(self, new_value: str):
        self.value = new_value

    async def run_validation(self, _):
        if re.match(PATTERN, self.value):
            self.position, self.opacity, self.background = (
                "10px",
                "1",
                rx.color("grass"),
            )
        else:
            self.position, self.opacity, self.background = ("-10px", "0", "none")
            yield
            self.position, self.opacity, self.background = (
                "10px",
                "1",
                rx.color("ruby"),
            )

        yield


def animation_v4():
    return rx.center(
        rx.hstack(
            rx.input(
                value=Animation.value,
                placeholder="Email Address",
                variant="surface",
                color_scheme="gray",
                width="100%",
                on_change=Animation.run_animation,
                on_blur=Animation.run_validation,
            ),
            rx.box(
                width="15px",
                height="15px",
                border_radius="15px",
                position="absolute",
                transition="all 150ms ease",
                right=Animation.position,
                bg=Animation.background,
                opacity=Animation.opacity,
            ),
            position="relative",
            max_width="15em",
            width="100%",
            align="center",
        ),
        rx.badge(
            "Validates email on blur.",
            variant="surface",
            position="absolute",
            top="0",
            left="0",
            size="1",
            padding="5px 10px",
            color_scheme="sky",
            border_radius="0px 0px 8px 0px",
        ),
        width="100%",
        height="20em",
    )
