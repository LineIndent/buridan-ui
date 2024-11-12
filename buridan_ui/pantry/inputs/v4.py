from typing import Callable

import reflex as rx


class InputsV4State(rx.State):
    is_open: bool = False
    string: str
    tip: str = "Password must include at least 6 characters"

    def on_entry_focus(self, event=None):
        self.is_open = not self.is_open

    def on_entry_blur(self, event=None):
        self.is_open = False

    def entry_value_update(self, value: str):
        self.string = value

        self.tip = (
            "All good!"
            if len(self.string) >= 6
            else "Password must include at least 6 characters"
        )


title: Callable[[str], rx.Component] = lambda name: rx.text(
    name, size="1", weight="bold", color=rx.color("slate", 11)
)


tip: Callable[[], rx.Component] = lambda: rx.tooltip(
    rx.icon(
        tag="info",
        position="absolute",
        bottom="0",
        left="0",
        opacity="0",
    ),
    content=InputsV4State.tip,
    side="bottom",
    align="start",
    padding="0.5em",
    open=InputsV4State.is_open,
)

entry: Callable[[str], rx.Component] = lambda placeholder: rx.input(
    tip(),
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
    type="password",
    on_focus=InputsV4State.on_entry_focus,
    on_blur=InputsV4State.on_entry_blur,
    on_change=InputsV4State.entry_value_update,
)


def inputs_v4():
    return rx.vstack(
        title("Show tooltip on focus"),
        entry("Your password"),
        width="100%",
        max_width="25em",
        spacing="1",
    )
