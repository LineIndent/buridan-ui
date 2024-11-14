from typing import Callable
from dataclasses import dataclass, field
from reflex.constants.colors import Color

import reflex as rx

color: Callable[[int], Color] = lambda shade: rx.color("slate", shade)
TextShared: dict[str, str] = {"size": "2", "weight": "bold"}


@dataclass
class CardV1Style:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "align": "start",
            "justify": "start",
            "position": "relative",
            "width": "100%",
            "max_width": "320px",
            "height": "200px",
            "border": f"1px solid {rx.color('gray', 6)}",
            "bg": rx.color("gray", 3),
            "border_radius": "12px",
            "padding": "16px",
            "overflow": "hidden",
            "z_index": "30",
            "box_shadow": "0px 6px 12px 0px rgba(0, 0, 0, 0.05)",
        }
    )

    icon: dict[str, str] = field(
        default_factory=lambda: {
            "size": 21,
            "position": "absolute",
            "bottom": "16px",
            "right": "16px",
        }
    )

    stack: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "spacing": "1",
            "align": "start",
            "justify": "start",
            "text_align": "start",
        }
    )

    background: dict[str, str] = field(
        default_factory=lambda: {
            "background_size": "16px 16px",
            "background_image": f"radial-gradient(circle, {rx.color('gray', 12)} 1px, transparent 1px)",
            "mask": f"radial-gradient(100% 100% at 100% 100%, hsl(0, 0%, 0%, 0.81), hsl(0, 0%, 0%, 0))",
            "width": "100%",
            "height": "100%",
            "position": "absolute",
        }
    )

    title: dict[str, str] = field(
        default_factory=lambda: {"color": color(12), **TextShared}
    )

    description: dict[str, str] = field(
        default_factory=lambda: {"color": color(11), **TextShared}
    )


CardV1Style: CardV1Style = CardV1Style()


def card_v1():
    return rx.hstack(
        rx.vstack(
            rx.text("Interactive User Logins", **CardV1Style.title),
            rx.text(
                "Explore our intuitive and secure user login system, designed to streamline the authentication process.",
                **CardV1Style.description,
            ),
            **CardV1Style.stack,
        ),
        rx.box(**CardV1Style.background),
        rx.icon(tag="puzzle", **CardV1Style.icon),
        **CardV1Style.base,
    )
