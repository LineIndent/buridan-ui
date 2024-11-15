import reflex as rx

from ..state import ComponentWrapperState
from .style import ComponentWrapperUtilStyle

IconMap = {"100%": "monitor", "60%": "tablet", "30%": "smartphone"}
PaddingMap = {0: "10px 0px 0px 10px", 1: "0px", 2: "0px 10px 10px 0px"}


def _(index: int, icon: str, resize: str, idd: int):
    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.button(
                rx.icon(
                    tag=icon,
                    size=14,
                    color=rx.color("slate", 11),
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
        padding_right=["0px" if i <= 1 else "24px" for i in range(6)],
        display=["none" if i <= 4 else "flex" for i in range(6)],
    )
