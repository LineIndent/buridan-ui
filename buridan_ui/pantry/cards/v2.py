from typing import Callable
from dataclasses import dataclass, field
import reflex as rx
from reflex.constants.colors import Color

info = [
    {
        "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-1.png",
        "name": "Robert Wolfkisser",
        "job": "Engineer",
    },
    {
        "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-2.png",
        "name": "Henry Silkeater",
        "job": "Designer",
    },
    {
        "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-10.png",
        "name": "Jeremy Footviewer",
        "job": "Manager",
    },
    {
        "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-7.png",
        "name": "Jill Jailbreaker",
        "job": "Engineer",
    },
]

color: Callable[[int], Color] = lambda shade: rx.color("slate", shade)

TextShared: dict[str, str] = {"size": "2", "weight": "bold"}


@dataclass
class CardV2Style:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "height": "220px",
            "border": f"1px solid {rx.color('gray', 6)}",
            "bg": rx.color("gray", 2),
            "border_radius": "12px",
            "overflow": "hidden",
            "spacing": "0",
            "transition": "all 250ms linear",
            "flex": "1 1 auto 1",
            "align": "center",
            "justify": "center",
            "position": "relative",
        }
    )

    image: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "100%",
            "object_fit": "fit",
            "transition": "all 550ms ease",
            "mask": "linear-gradient(to bottom, hsl(0, 0%, 0%, 0.95) 45%, hsl(0, 0%, 0%, 0))",
        }
    )

    text_container: dict[str, str] = field(
        default_factory=lambda: {
            "position": "absolute",
            "bottom": "0",
            "left": "0",
            "bg": rx.color("gray", 3),
            "width": "100%",
            "padding": "12px 18px",
            "spacing": "0",
            "justify": "between",
        }
    )

    name: dict[str, str] = field(
        default_factory=lambda: {"color": color(12), **TextShared}
    )

    job: dict[str, str] = field(
        default_factory=lambda: {"color": color(10), **TextShared}
    )


CardV2Style: CardV2Style = CardV2Style()


def item(image: str, name: str, job: str):
    return rx.vstack(
        rx.image(src=image, **CardV2Style.image),
        rx.vstack(
            rx.text(name, **CardV2Style.name),
            rx.text(job, **CardV2Style.job),
            **CardV2Style.text_container,
        ),
        **CardV2Style.base,
    )


def card_v2():
    return rx.hstack(
        *[item(data["avatar"], data["name"], data["job"]) for data in info],
        width="100%",
        flex_wrap="wrap",
        justify="center",
    )
