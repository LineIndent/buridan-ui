import reflex as rx

from ..shared.sidebar import Sidebar

from ...routes.started_routes import GETTING_STARTED_ROUTES
from ...routes.pantry_routes import PANTRY_ROUTES


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
                # rx.text(),
                width="100%",
                align="center",
            )
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
            rx.menu.item(
                rx.hstack(
                    rx.text("Home", color_scheme="gray", weight="bold", size="1"),
                    rx.icon(tag="home", size=13),
                    width="100%",
                    justify="between",
                    align="center",
                ),
                _hover={"bg": "none"},
                padding_top="20px",
                padding_bottom="15px",
            ),
            rx.menu.item(
                rx.hstack(
                    rx.text(
                        "Getting Started", color_scheme="gray", weight="bold", size="1"
                    ),
                    rx.icon(tag="play", size=13),
                    width="100%",
                    justify="between",
                    align="center",
                ),
                _hover={"bg": "none"},
                padding_top="20px",
                padding_bottom="15px",
            ),
            *create_menu_items(GETTING_STARTED_ROUTES),
            rx.menu.item(
                rx.hstack(
                    rx.text("Pantry", color_scheme="gray", weight="bold", size="1"),
                    rx.icon(tag="component", size=13),
                    width="100%",
                    justify="between",
                    align="center",
                ),
                _hover={"bg": "none"},
                padding_top="20px",
                padding_bottom="15px",
            ),
            *create_menu_items(PANTRY_ROUTES),
            size="1",
            width="200px",
        ),
    )
