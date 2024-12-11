import reflex as rx


def title(txt: str) -> rx.Component:
    return rx.text(txt, size="2", weight="bold", color=rx.color("slate", 11))


def wrapper(txt: str, components: list[rx.Component]) -> rx.Component:
    return rx.vstack(title(txt), *components, spacing="2", width="100%")
