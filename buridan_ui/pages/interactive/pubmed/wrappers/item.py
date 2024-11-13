from typing import Callable

import reflex as rx


title: Callable[[str], rx.Component] = lambda txt: rx.text(
    txt, size="2", weight="bold", color=rx.color("slate", 11)
)


wrapper: Callable[[str, list[rx.Component]], rx.Component] = (
    lambda txt, components: rx.vstack(
        title(txt), *components, spacing="2", width="100%"
    )
)
