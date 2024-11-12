from typing import Callable

import reflex as rx


title: Callable[[str], rx.Component] = lambda name: rx.text(
    name, size="1", weight="bold", color=rx.color("slate", 11)
)


tip: Callable[[], rx.Component] = lambda: rx.icon(
    tag="info",
    size=20,
    color=rx.color("gray", 10),
    right="10px",
    position="absolute",
    cursor="help",
)

entry: Callable[[str], rx.Component] = lambda placeholder: rx.input(
    rx.tooltip(tip(), content="We store your data securely."),
    placeholder=placeholder,
    outline="none",
    variant="soft",
    width="100%",
    overflow="hidden",
    position="relative",
    display="flex",
    align_items="center",
    height="40px",
    background=rx.color("gray", 4),
)


def inputs_v3():
    return rx.vstack(
        title("Show tooltip on hover"),
        entry("Enter your email ..."),
        width="100%",
        max_width="25em",
        spacing="1",
    )
