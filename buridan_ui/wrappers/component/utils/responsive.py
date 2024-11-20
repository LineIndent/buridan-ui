import reflex as rx

from ..state import ComponentWrapperState
from .style import ComponentWrapperUtilStyle

IconMap = {"100%": "monitor", "60%": "tablet", "30%": "smartphone"}
PaddingMap = {0: "6px 0px 0px 6px", 1: "0px", 2: "0px 6px 6px 0px"}


def _(index: int, icon: str, resize: str, idd: int):
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.button(
                rx.icon(
                    tag=icon,
                    size=20,
                    color=rx.color("slate", 11),
                    transform="scale(1.3)",
                ),
                border_radius=PaddingMap[index],
                on_click=ComponentWrapperState.resize(idd, resize),
                **ComponentWrapperUtilStyle.buttons,
            ),
        ),
        rx.hover_card.content(
            rx.text(
                icon if icon != "smartphone" else "mobile",
                size="1",
                color=rx.color("slate", 12),
                weight="bold",
            ),
            padding="10px",
            border_radius="6px",
        ),
    )


def component_wrapper_responsive_menu(idd: int) -> rx.hstack:
    return rx.hstack(
        *[
            _(index, IconMap[resize], resize, idd)
            for index, resize in enumerate(["30%", "60%", "100%"])
        ],
        spacing="0",
        align="center",
        display=["none" if i <= 3 else "flex" for i in range(6)],
    )


def component_wrapper_responsive_menu_hero(idd: int) -> rx.hstack:
    return rx.hstack(
        *[
            _(index, IconMap[resize], resize, idd)
            for index, resize in enumerate(["30%", "60%", "100%"])
        ],
        spacing="0",
        align="center",
    )
