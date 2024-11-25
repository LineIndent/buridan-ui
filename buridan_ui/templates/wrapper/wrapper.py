import reflex as rx

from typing import Callable
from .style import MenuWrapperStyle, BaseHeaderWrapper


def menu_wrapper(title: str, components: list[rx.Component] = []):
    return rx.hstack(
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    rx.text(
                        title, size="1", weight="bold", color=rx.color("slate", 11)
                    ),
                    align="center",
                ),
                spacing="1",
            ),
            *components,
            width="100%",
        ),
        **MenuWrapperStyle.wrapper,
    )


baseWrapperHeader: Callable[[rx.Component, str], rx.Component] = (
    lambda path_name, title: rx.vstack(
        rx.vstack(
            path_name,
            rx.heading(title, font_weight="900", size="9"),
            rx.link(
                "See source code on GitHub →",
                href="https://github.com/LineIndent/buridan-ui",
                size="1",
            ),
            **BaseHeaderWrapper.titles,
        ),
        min_height="35vh",
        **BaseHeaderWrapper.wrapper,
    )
)
