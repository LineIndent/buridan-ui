import reflex as rx

from .style import BaseHeaderWrapper, MenuWrapperStyle


def menu_wrapper(title: str, components: list[rx.Component] = []):
    return rx.hstack(
        rx.vstack(
            rx.text(
                title,
                size="1",
                weight="bold",
                color=rx.color("slate", 11),
            ),
            *components,
            width="100%",
        ),
        **MenuWrapperStyle.wrapper,
    )


def baseWrapperHeader(path_name: rx.Component, title: str) -> rx.Component:
    return rx.vstack(
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
        **BaseHeaderWrapper.wrapper,
    )
