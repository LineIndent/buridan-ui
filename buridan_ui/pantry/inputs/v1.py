import reflex as rx
from dataclasses import dataclass, field
from typing import Callable


@dataclass
class InputsV1Style:
    root: dict[str, str] = field(
        default_factory=lambda: {"width": "100%", "height": "100%", "align": "center"}
    )

    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "max_width": "30em",
            "border_radius": "5px",
            "padding": "2.5px 10px",
            "spacing": "0",
            "transition": "all 350ms ease",
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
    ["Shipping Address", "1234 Street, New York City"],
    ["Card Number", "1234 5678 1243 4332"],
]


class InputV1State(rx.State):

    data: list[list[str]] = [
        [*item, InputsV1Style.passive_border["border"]] for item in data
    ]

    def on_entry_select(self, strings: list[str]):
        self.data = [
            (
                [*strings[:2], InputsV1Style.active_border["border"]]
                if strings[0] == item[0]
                else [*item[:2], InputsV1Style.passive_border["border"]]
            )
            for item in self.get_value(self.data)
        ]

    def on_entry_blur(self, e=None):
        self.data = [
            [*item[:2], InputsV1Style.passive_border["border"]] for item in data
        ]


title: Callable[[str], rx.Component] = lambda txt: rx.text(txt, **InputsV1Style.text)

entry: Callable[[str, list[str]], rx.Component] = lambda placeholder, strings: rx.input(
    placeholder=placeholder,
    on_focus=InputV1State.on_entry_select(strings),
    on_blur=InputV1State.on_entry_blur,
    **InputsV1Style.entry,
)

stack: Callable[[list[str]], rx.Component] = lambda strings: rx.vstack(
    title(strings[0]),
    entry(strings[1], strings),
    border=strings[2],
    **InputsV1Style.base,
)


def inputs_v1():
    return rx.vstack(rx.foreach(InputV1State.data, stack), **InputsV1Style.root)
