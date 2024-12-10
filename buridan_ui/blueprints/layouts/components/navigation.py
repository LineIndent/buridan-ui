import reflex as rx

from buridan_ui.blueprints.layouts.style import LayoutStyleSheet


def layoutNavigation() -> rx.Component:
    return rx.hstack(
        rx.heading("Site Name", size="2"),
        rx.hstack(
            *[
                rx.text(name, size="1", color=rx.color("slate", 12))
                for name in ["Home", "Services", "About Us", "Contact"]
            ],
        ),
        **LayoutStyleSheet.navigation,
    )
