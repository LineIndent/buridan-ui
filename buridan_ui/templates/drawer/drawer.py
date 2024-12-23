import reflex as rx

from buridan_ui.states.routing import SiteRoutingState
from buridan_ui.templates.sidemenu.sidemenu import create_sidebar_menu_items

from .state import DrawerState
from .style import DrawerStyle

active = rx.color("slate", 12)


def drawer_menu_header(title: str):
    return rx.text(title, size="1", color=active, weight="bold", padding="0em 1.25em")


def drawer_menu_link(stack: rx.vstack):
    return rx.vstack(stack, **DrawerStyle.drawer_menu_link)


def drawer():
    return rx.drawer.root(
        rx.drawer.overlay(z_index="50"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.hstack(
                        rx.heading(
                            "buridan/ui",
                            size="4",
                            font_weight="900",
                            cursor="pointer",
                            on_click=rx.redirect("/"),
                        ),
                        rx.image(src="/logo.jpg", **DrawerStyle.logo),
                        **DrawerStyle.title,
                    ),
                    drawer_menu_header("Getting Started"),
                    drawer_menu_link(
                        create_sidebar_menu_items(
                            SiteRoutingState.GettingStartedRoutes,
                        ),
                    ),
                    drawer_menu_header("Interactive Apps"),
                    drawer_menu_link(
                        create_sidebar_menu_items(SiteRoutingState.InteractiveRoutes),
                    ),
                    drawer_menu_header("Blueprint Templates"),
                    drawer_menu_link(
                        create_sidebar_menu_items(SiteRoutingState.BlueprintRoutes),
                    ),
                    drawer_menu_header("Analytics"),
                    drawer_menu_link(
                        create_sidebar_menu_items(SiteRoutingState.AnalyticsRoutes),
                    ),
                    drawer_menu_header("Charts"),
                    drawer_menu_link(
                        create_sidebar_menu_items(SiteRoutingState.ChartRoutes),
                    ),
                    drawer_menu_header("Pantry"),
                    drawer_menu_link(
                        create_sidebar_menu_items(SiteRoutingState.PantryRoutes),
                    ),
                    **DrawerStyle.stack_content,
                ),
                on_interact_outside=DrawerState.toggle_drawer(),
                **DrawerStyle.content,
            ),
            z_index="50",
        ),
        direction="left",
        open=DrawerState.is_open,
    )
