import reflex as rx

from ..style import Style, Typography

title: rx.Component = rx.text("getFit.", weight="bold", size="1", **Typography.active)
theme: rx.Component = rx.color_mode.button(size="1", **Typography.active)


def app_navigation_bar() -> rx.hstack:
    return rx.badge(
        rx.hstack(title, theme, **Style.navigation_child),
        **Style.navigation_parent,
    )
