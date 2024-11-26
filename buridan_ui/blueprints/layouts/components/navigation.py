import reflex as rx

from typing import Callable
from ..style import LayoutStyleSheet


layoutNavigation: Callable[[], rx.Component] = lambda: rx.hstack(
    rx.heading("Site Name", size="2"),
    rx.hstack(
        *[
            rx.text(name, size="1", color=rx.color("slate", 12))
            for name in ["Home", "Services", "About Us", "Contact"]
        ]
    ),
    **LayoutStyleSheet.navigation,
)
