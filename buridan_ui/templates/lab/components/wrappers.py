import reflex as rx
from typing import Callable


header: Callable[[str], rx.text] = lambda title: rx.text(
    title, size="1", weight="bold", color=rx.color("slate", 11)
)

data_wrapper: Callable[[str, list[rx.Component]], rx.Component] = (
    lambda title, components: rx.vstack(
        header(title), *components, spacing="2", width="100%"
    )
)
