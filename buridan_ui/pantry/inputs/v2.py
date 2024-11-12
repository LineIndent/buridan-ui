from typing import Callable

import reflex as rx


data = ["🇪🇺 EUR", "🇺🇸 USD", "🇨🇦 CAD", "🇬🇧 GBP", "🇦🇺 AUD"]

title: Callable[[str], rx.Component] = lambda name: rx.text(
    name, size="1", weight="bold", color=rx.color("slate", 11)
)


select: Callable[[], rx.Component] = lambda: rx.select(
    data,
    default_value=data[0],
    top="0",
    right="0",
    position="popper",
    width="120px",
    variant="soft",
    radius="none",
    cursor="pointer",
    size="3",
)

entry: Callable[[str], rx.Component] = lambda placeholder: rx.input(
    select(),
    placeholder=placeholder,
    outline="none",
    variant="soft",
    width="100%",
    overflow="hidden",
    background=rx.color("gray", 4),
    height="40px",
)


def inputs_v2():
    return rx.vstack(
        title("Transfer Amount"),
        entry("1000"),
        width="100%",
        max_width="25em",
        spacing="1",
    )
