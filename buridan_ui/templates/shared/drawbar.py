import reflex as rx
from docutils.parsers.rst.directives.tables import align
from reflex import color

from ..shared.sidebar import Sidebar

from ...routes.started_routes import GETTING_STARTED_ROUTES
from ...routes.pantry_routes import PANTRY_ROUTES
from ...routes.interactive_tables import INTERACTIVE_TABLES


def create_menu_title(title: str, icon_name: str):
    return rx.menu.item(
        rx.hstack(
            rx.text(title, color=rx.color("slate", 11), weight="bold", size="1"),
            rx.icon(tag=icon_name, size=13, color=rx.color("slate", 11)),
            width="100%",
            justify="between",
            align="center",
        ),
        padding_top="15px",
        padding_bottom="15px",
        margin_top="10px",
        margin_bottom="10px",
        _hover={
            "bg": rx.color("gray", 3),
        },
        bg=rx.color("gray", 3),
    )


def create_menu_items(data: list[dict[str, str]]):
    return [
        rx.menu.item(
            rx.hstack(
                rx.link(
                    rx.text(
                        item["name"],
                        color=rx.color("slate", 12),
                        weight="medium",
                        on_click=Sidebar.delta_page(item),
                    ),
                    href=item["path"],
                ),
                (
                    rx.badge("BETA - DEMO", color_scheme="orange")
                    if item.get("is_beta", False)
                    else rx.spacer()
                ),
                width="100%",
                align="center",
            ),
            padding_top="2px",
            padding_bottom="2px",
            _hover={
                "bg": rx.color("gray", 4),
            },
        )
        for item in data
    ]


def drawbar():
    return rx.menu.root(
        rx.menu.trigger(
            rx.button(
                "Menu", variant="soft", size="1", color_scheme="gray", cursor="pointer"
            ),
        ),
        rx.menu.content(
            create_menu_title("Home", "home"),
            create_menu_title("Getting Started", "play"),
            *create_menu_items(GETTING_STARTED_ROUTES),
            create_menu_title("Interactive Tables", "table"),
            *create_menu_items(INTERACTIVE_TABLES),
            create_menu_title("Pantry", "component"),
            *create_menu_items(PANTRY_ROUTES),
            size="1",
            width="200px",
        ),
    )
