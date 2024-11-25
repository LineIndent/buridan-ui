import reflex as rx
from .style import ComponentWrapperUtilStyle


def component_wrapper_source_code(path: str):
    return rx.button(
        rx.link(
            rx.icon(tag="github", size=14, color=rx.color("slate", 11)),
            href=path,
            is_external=True,
        ),
        border_radius="6px",
        display=["none" if i <= 1 else "flex" for i in range(6)],
        **ComponentWrapperUtilStyle.buttons,
    )
