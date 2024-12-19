from __future__ import annotations

import reflex as rx
from reflex.constants.colors import Color

from buridan_ui.states.routing import SiteRoutingState
from buridan_ui.templates.wrapper.wrapper import menu_wrapper

from .style import SideMenuStyle


def create_sidebar_menu_items(routes: list[dict[str, str | Color]]):

    def item(data):
        return rx.hstack(
            rx.link(
                rx.text(
                    data["name"],
                    size="1",
                    weight="medium",
                    color=rx.color("slate", 12),
                ),
                href=data["path"],
                text_decoration="none",
                on_click=lambda: SiteRoutingState.toggle_page_change(data),
            ),
            rx.cond(
                data["is_beta"],
                rx.badge("In Progress", color_scheme="orange"),
                rx.cond(
                    data["is_new"],
                    rx.badge("New", color_scheme="grass"),
                    rx.spacer(),
                ),
            ),
            border_left=data["border_left"],
            background=data["background"],
            width="100%",
            align="center",
            height="26px",
            padding_left="20px",
            border_radius="0px 6px 6px 0px",
        )

    return rx.vstack(
        rx.foreach(routes, item),
        spacing="0",
        width="100%",
    )


def top_scroll_fade_out():
    return rx.box(
        top="0",
        left="0",
        position="fixed",
        width="100%",
        height="10%",
        z_index="20",
        background=rx.color("gray", 2),
        mask="linear-gradient(to bottom, hsl(0, 0%, 0%, 1) 55%, hsl(0, 0%, 0%, 0) 100%)",
    )


def sidemenu() -> rx.vstack:
    return rx.vstack(
        top_scroll_fade_out(),
        rx.vstack(
            menu_wrapper(
                "Getting Started",
                [create_sidebar_menu_items(SiteRoutingState.GettingStartedRoutes)],
            ),
            menu_wrapper(
                "Interactive Applications",
                [create_sidebar_menu_items(SiteRoutingState.InteractiveRoutes)],
            ),
            menu_wrapper(
                "Blueprint Templates",
                [create_sidebar_menu_items(SiteRoutingState.BlueprintRoutes)],
            ),
            menu_wrapper(
                "Data Analytics",
                [create_sidebar_menu_items(SiteRoutingState.AnalyticsRoutes)],
            ),
            menu_wrapper(
                "Chart Components",
                [create_sidebar_menu_items(SiteRoutingState.ChartRoutes)],
            ),
            menu_wrapper(
                "Pantry Components",
                [create_sidebar_menu_items(SiteRoutingState.PantryRoutes)],
            ),
            **SideMenuStyle.content,
        ),
        **SideMenuStyle.base,
    )
