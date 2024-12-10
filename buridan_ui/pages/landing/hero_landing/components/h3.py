import reflex as rx

from dataclasses import dataclass, field

from typing import Callable

data: list[list[str]] = [
    ["Shipping Address", "1234 Street, New York City"],
    ["Card Number", "1234 5678 1243 4332"],
]


@dataclass
class InputsV1Style:

    root: dict[str, str] = field(default_factory=lambda: {"width": "100%"})

    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "max_width": "30em",
            "border_radius": "5px",
            "padding": "2.5px 10px",
            "spacing": "0",
            "transition": "filter 300ms ease 700ms, transform 300ms ease 700ms, opacity 300ms ease 700ms",
        }
    )

    text: dict[str, str] = field(
        default_factory=lambda: {
            "size": "1",
            "weight": "bold",
            "padding": "8px 8px 0px 8px",
            "color": rx.color("slate", 11),
        }
    )

    entry: dict[str, str] = field(
        default_factory=lambda: {
            "outline": "none",
            "variant": "soft",
            "width": "100%",
            "background": "transparent",
        }
    )

    active_border: dict[str, str] = field(
        default_factory=lambda: {
            "border": f"2px solid {rx.color('blue', 7)}",
        }
    )

    passive_border: dict[str, str] = field(
        default_factory=lambda: {
            "border": f"2px solid {rx.color('gray', 5)}",
        }
    )


InputsV1Style: InputsV1Style = InputsV1Style()
data: list[list[str]] = [
    [*item, InputsV1Style.passive_border["border"]] for item in data
]

title: Callable[[str], rx.Component] = lambda txt: rx.text(txt, **InputsV1Style.text)

entry: Callable[[str, list[str]], rx.Component] = lambda placeholder, strings: rx.input(
    placeholder=placeholder,
    **InputsV1Style.entry,
)

stack: Callable[[list[str]], rx.Component] = lambda strings: rx.vstack(
    title(strings[0]),
    entry(strings[1], strings),
    border=strings[2],
    **InputsV1Style.base,
    **{
        "position": "relative",
        f"@keyframes intro": {
            "0%": {"filter": "blur(10px)", "transform": "scale(1.5)", "opacity": "0"},
            "100%": {"filter": "blur(0px)", "transform": "scale(1)", "opacity": "1"},
        },
        "animation": "intro 300ms ease",
    },
)

hero_inputs = rx.hstack(*[stack(item) for item in data], **InputsV1Style.root)
