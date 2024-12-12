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
            rx.heading(
                title,
                font_weight="900",
                font_size=["2.85em", "2.85em", "3em", "3em", "3.5em", "3.75em"],
                line_height="1",
            ),
            rx.link(
                "See source code on GitHub →",
                href="https://github.com/LineIndent/buridan-ui",
                size="1",
            ),
            **BaseHeaderWrapper.titles,
        ),
        **BaseHeaderWrapper.wrapper,
    )
