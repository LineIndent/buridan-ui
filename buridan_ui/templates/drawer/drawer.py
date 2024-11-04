import reflex as rx

from .style import DrawerStyle
from .state import DrawerState

from ..sidemenu.sidemenu import create_sidebar_menu_items
from ..sidemenu.state import SideMenuState

active = rx.color("slate", 12)


def drawer_menu_header(title: str, icon: str):
    return rx.badge(
        rx.hstack(
            rx.text(title, size="1", color=active, weight="bold"),
            rx.icon(tag=icon, size=15, color=active),
            **DrawerStyle.header_components,
        ),
        **DrawerStyle.header,
    )


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
                            size="5",
                            font_weight="900",
                            cursor="pointer",
                            on_click=rx.redirect("/"),
                        ),
                        rx.image(src="/logo.jpg", **DrawerStyle.logo),
                        **DrawerStyle.title,
                    ),
                    drawer_menu_header("Getting Started", "play"),
                    drawer_menu_link(
                        create_sidebar_menu_items(SideMenuState.GettingStartedRoutes)
                    ),
                    drawer_menu_header("Interactive Apps", "puzzle"),
                    drawer_menu_link(
                        create_sidebar_menu_items(SideMenuState.InteractiveRoutes)
                    ),
                    drawer_menu_header("Charts", "table-columns-split"),
                    drawer_menu_link(
                        create_sidebar_menu_items(SideMenuState.ChartRoutes)
                    ),
                    drawer_menu_header("Pantry", "component"),
                    drawer_menu_link(
                        create_sidebar_menu_items(SideMenuState.PantryRoutes)
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
