import asyncio
from dataclasses import dataclass, field

import reflex as rx


@dataclass
class AnimationStyle:

    dash: dict[str, str] = field(
        default_factory=lambda: {
            "position": "absolute",
            "width": "2px",
            "height": "100%",
            "top": "20px",
            "background": rx.color("gray", 5),
            "overflow": "hidden",
            "border_radius": "50%",
            "::after": {
                "content": "''",
                "display": "block",
                "position": "absolute",
                "height": "10vh",
                "width": "100%",
                "top": "-50%",
                "left": 0,
                "border": f"2px dashed {rx.color('red')}",
                "animation": "drop 1.5s 0s infinite",
                "animation-fill-mode": "forwards",
            },
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

    dash_animation: dict[str, str] = field(
        default_factory=lambda: {
            "@keyframes drop": {"0%": {"top": "-50%"}, "100%": {"top": "100%"}},
        },
    )

    text: dict[str, str] = field(
        default_factory=lambda: {"size": "1", "weight": "bold"},
    )


AnimationStyle: AnimationStyle = AnimationStyle()

active_blip = {"opacity": "1"}
passive_blip = {"opacity": "0.71"}

active_text = {"filter": "blur(0px)", "transform": "scale(1)", "opacity": "1"}
passive_text = {"filter": "blur(10px)", "transform": "scale(1.15)", "opacity": "0"}


class AnimationState(rx.State):
    is_disabled: bool = False

    blip: dict[str, str] = passive_blip
    blip_color: str = "gray"
    blip_type: str = "surface"

    text: dict[str, str] = passive_text

    runner: dict[str, str] = {}

    async def run_animation(self):
        self.is_disabled = True
        yield

        self.blip, self.text, self.blip_color, self.blip_type = (
            active_blip,
            active_text,
            "red",
            "solid",
        )
        self.runner = AnimationStyle.dash_animation
        yield
        await asyncio.sleep(5)
        await self.stop_animation()
        self.is_disabled = False

    async def stop_animation(self) -> None:
        self.reset()
        self.runner = {}


dash = rx.box(**AnimationStyle.dash, style=AnimationState.runner)


def blip(delay: int):

    return rx.badge(
        "-",
        width="21px",
        height="21px",
        position="absolute",
        border_radius="21px",
        left="-9.5px",
        display="flex",
        align_items="center",
        justify_content="center",
        transition=f"all 300ms ease {delay}ms",
        variant=AnimationState.blip_type,
        color_scheme=AnimationState.blip_color,
        style=AnimationState.blip,
    )


def wrapper(issue: str, response: str, posY: str, delay: int) -> rx.box:
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.vstack(
                    rx.hstack(
                        blip(delay),
                        rx.text(
                            issue,
                            color=rx.color("slate", 12),
                            style=AnimationState.text,
                            transition=f"all 300ms ease {delay}ms",
                            **AnimationStyle.text,
                        ),
                        align="center",
                    ),
                    spacing="1",
                    wrap="wrap",
                ),
                rx.text(
                    response,
                    color=rx.color("slate", 11),
                    style=AnimationState.text,
                    transition=f"all 300ms ease {delay}ms",
                    **AnimationStyle.text,
                ),
                rx.divider(height="2em", opacity="0"),
            ),
            width="100%",
            align="start",
            justify="start",
            padding_left="2em",
            top=posY,
        ),
        position="relative",
    )


def animation_v6():
    return rx.vstack(
        rx.vstack(
            dash,
            wrapper(
                "Build and Test",
                "Runs tests after building the project to ensure code quality.",
                "20%",
                350,
            ),
            wrapper(
                "Deploy to Staging",
                "Deploys the application to the staging environment for QA.",
                "40%",
                550,
            ),
            wrapper(
                "Release Production",
                "Builds and deploys the latest version to production.",
                "60%",
                750,
            ),
            wrapper(
                "Run Unit Tests",
                "Executes unit tests for individual components of the project.",
                "80%",
                950,
            ),
            max_width="40em",
            padding="1em 0em",
        ),
        rx.button(
            "Run",
            loading=AnimationState.is_disabled,
            on_click=AnimationState.run_animation,
            **AnimationStyle.button,
        ),
        position="relative",
        width="100%",
        height="50vh",
        align="center",
        justify="center",
        padding="1em",
    )
