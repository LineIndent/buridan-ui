import reflex as rx

from .components.blocks import blockTypeOne
from .components.navigation import layoutNavigation
from .style import LayoutStyleSheet


def layoutDoubleColumn() -> rx.Component:
    return rx.hstack(
        rx.vstack(**LayoutStyleSheet.doubleColumnLeft),
        rx.vstack(
            layoutNavigation(),
            blockTypeOne(),
            **LayoutStyleSheet.doubleColumnContentArea,
        ),
        **LayoutStyleSheet.doubleColumn,
    )


def layoutSingleColumn() -> rx.Component:
    return rx.vstack(
        layoutNavigation(),
        rx.divider(height="5em", opacity="0"),
        blockTypeOne(),
        **LayoutStyleSheet.singleColumn,
    )
