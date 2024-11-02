import reflex as rx

from .state import SideMenuState
from .style import SideMenuStyle

from ..wrapper.wrapper import menu_wrapper


def create_sidebar_menu_items(routes: list[dict[str, str]]):

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
                on_click=SideMenuState.toggle_page_change(data),
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
            justify="between",
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
                "Nov 01, 2024",
                "play",
                [create_sidebar_menu_items(SideMenuState.GettingStartedRoutes)],
            ),
            menu_wrapper(
                "Interactive Apps",
                "Nov 01, 2024",
                "table",
                [create_sidebar_menu_items(SideMenuState.InteractiveRoutes)],
            ),
            menu_wrapper(
                "Charts",
                "Nov 01, 2024",
                "table-columns-split",
                [create_sidebar_menu_items(SideMenuState.ChartRoutes)],
            ),
            menu_wrapper(
                "Pantry",
                "Nov 01, 2024",
                "component",
                [create_sidebar_menu_items(SideMenuState.PantryRoutes)],
            ),
            **SideMenuStyle.content,
        ),
        **SideMenuStyle.base,
    )
