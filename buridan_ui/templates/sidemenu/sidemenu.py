import reflex as rx
from typing import List, Dict

from .style import SideMenuStyle
from ..wrapper.wrapper import menu_wrapper
from ...states.routing import SiteRoutingState


def create_sidebar_menu_items(routes: List[Dict[str, str]]):

    def item(data):
        return rx.hstack(
            rx.link(
                rx.text(
                    data["name"],
                    size="3",
                    weight="medium",
                    color=data["color"],
                    _hover={"color": rx.color("slate", 12)},
                    transition="color 350ms ease",
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
            width="100%",
            align="center",
        )

    return rx.vstack(
        rx.foreach(routes, item),
        spacing="2",
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
        mask="linear-gradient(to bottom, hsl(0, 0%, 0%, 1) 45%, hsl(0, 0%, 0%, 0) 100%)",
    )


def sidemenu() -> rx.vstack:
    return rx.vstack(
        top_scroll_fade_out(),
        rx.vstack(
            menu_wrapper(
                "Getting Started",
                "play",
                [create_sidebar_menu_items(SiteRoutingState.GettingStartedRoutes)],
            ),
            menu_wrapper(
                "Interactive Apps",
                "table",
                [create_sidebar_menu_items(SiteRoutingState.InteractiveRoutes)],
            ),
            menu_wrapper(
                "Charts",
                "table-columns-split",
                [create_sidebar_menu_items(SiteRoutingState.ChartRoutes)],
            ),
            menu_wrapper(
                "Pantry",
                "component",
                [create_sidebar_menu_items(SiteRoutingState.PantryRoutes)],
            ),
            **SideMenuStyle.content,
        ),
        **SideMenuStyle.base,
    )
