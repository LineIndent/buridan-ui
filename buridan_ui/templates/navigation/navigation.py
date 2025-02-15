from __future__ import annotations

import reflex as rx
from reflex.constants.colors import Color

from buridan_ui.states.routing import SiteRoutingState
from buridan_ui.templates.drawer.state import DrawerState

from .style import NavigationStyle


def nav_icon(component: rx.Component) -> rx.badge:
    return rx.badge(
        component,
        color_scheme="gray",
        variant="soft",
        width="21px",
        height="21px",
        display="flex",
        align_items="center",
        justify_content="center",
        background="none",
    )


theme = nav_icon(
    rx.el.button(
        rx.color_mode.icon(
            light_component=rx.icon(
                "moon",
                size=14,
                color=rx.color("slate", 12),
            ),
            dark_component=rx.icon(
                "sun",
                size=14,
                color=rx.color("slate", 12),
            ),
        ),
        on_click=rx.toggle_color_mode,
    ),
)

github = nav_icon(
    rx.link(
        rx.icon(
            tag="github",
            size=14,
            color=rx.color("slate", 12),
        ),
        href="https://github.com/LineIndent/buridan-ui",
        display=["none", "none", "none", "none", "flex", "flex"],
    ),
)


def navigation_links(data: dict[str, str | Color]):
    return rx.link(
        rx.text(data["name"], size="1", weight="medium", color=rx.color("slate", 12)),
        href=data["path"],
        text_decoration="none",
        on_click=SiteRoutingState.toggle_page_change(data),
    )


def navigation_right_side_items():
    return rx.hstack(
        rx.hstack(github, theme, align="center", spacing="2"),
        rx.el.button(
            rx.icon(tag="align-right", size=15),
            on_click=DrawerState.toggle_drawer,
            size="1",
            variant="ghost",
            color_scheme="gray",
            cursor="pointer",
            display=["flex", "flex", "flex", "flex", "none", "none"],
        ),
        align="center",
    )


def navigation_left_side_items():
    return rx.hstack(
        # rx.image(src="/new_logo.png", **NavigationStyle.logo),
        rx.heading(
            "buridan/ui",
            font_size="0.9em",
            font_weight="800",
            cursor="pointer",
            on_click=[
                SiteRoutingState.toggle_page_change({"name": "Home", "path": "/"}),
                rx.redirect("/"),
            ],
        ),
        rx.divider(width="0.75em", opacity="0"),
        rx.hstack(
            rx.foreach(SiteRoutingState.NavigationRoutes, navigation_links),
            display=["none", "none", "none", "none", "flex", "flex"],
            align="center",
        ),
        align="center",
        spacing="2",
    )


def navigation():
    return rx.hstack(
        navigation_left_side_items(),
        navigation_right_side_items(),
        **NavigationStyle.base,
    )


def docs_navigation():
    return rx.hstack(
        rx.hstack(
            # rx.image(src="/logo.jpg", **NavigationStyle.logo),
            rx.heading(
                "buridan/ui",
                font_size="0.9em",
                font_weight="800",
                cursor="pointer",
                on_click=[
                    SiteRoutingState.toggle_page_change({"name": "Home", "path": "/"}),
                    rx.redirect("/"),
                ],
            ),
            align="center",
        ),
        rx.hstack(
            rx.hstack(github, theme, align="center", spacing="2"),
            rx.el.button(
                rx.icon(
                    tag="align-right",
                    size=15,
                    cursor="pointer",
                ),
                on_click=DrawerState.toggle_drawer,
                size="1",
                variant="soft",
                color_scheme="gray",
                cursor="pointer",
                display=["flex", "flex", "flex", "flex", "none", "none"],
            ),
            align="center",
        ),
        **NavigationStyle.base,
    )


def landing_page_navigation():
    return rx.hstack(
        navigation_left_side_items(),
        navigation_right_side_items(),
        **NavigationStyle.landing_page_nav,
    )
