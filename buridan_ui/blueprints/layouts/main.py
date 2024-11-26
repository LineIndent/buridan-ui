import reflex as rx

from typing import Callable

from .style import LayoutStyleSheet

from .components.navigation import layoutNavigation
from .components.blocks import blockTypeOne


layoutDoubleColumn: Callable[[], rx.Component] = lambda: rx.hstack(
    rx.vstack(**LayoutStyleSheet.doubleColumnLeft),
    rx.vstack(
        layoutNavigation(), blockTypeOne(), **LayoutStyleSheet.doubleColumnContentArea
    ),
    **LayoutStyleSheet.doubleColumn,
)

layoutSingleColumn: Callable[[], rx.Component] = lambda: rx.vstack(
    layoutNavigation(),
    rx.divider(height="5em", opacity="0"),
    blockTypeOne(),
    **LayoutStyleSheet.singleColumn,
)
