import asyncio

from ...styles.base import *
from ...routes.pantry_routes import PANTRY_ROUTES
from ...routes.started_routes import GETTING_STARTED_ROUTES

import reflex as rx

SELECTED: dict[str, str] = {
    "color": ACTIVE,
    "border": f"1px solid {rx.color('indigo', 10)}",
    "bg": rx.color("indigo", 5, True),
}

DESELECTED: dict[str, str] = {
    "color": PASSIVE,
    "border": f"1px solid {rx.color('gray')}",
    "bg": "",
}


class Sidebar(rx.State):
    pantry: list[dict[str, str]] = [{**item, **DESELECTED} for item in PANTRY_ROUTES]
    getting_started: list[dict[str, str]] = [
        {**item, **DESELECTED} for item in GETTING_STARTED_ROUTES
    ]

    async def delta_page(self, data: dict[str, str]):
        await asyncio.gather(
            self.refresh_sidebar(self.pantry, data),
            self.refresh_sidebar(self.getting_started, data),
        )

    async def refresh_sidebar(self, menu: list[dict[str, str]], item: dict[str, str]):
        for index in menu:
            if index["name"] == item["name"]:
                index["border"], index["bg"] = SELECTED["border"], SELECTED["bg"]
                index["color"] = SELECTED["color"]

            else:
                index["border"], index["bg"] = DESELECTED["border"], DESELECTED["bg"]
                index["color"] = DESELECTED["color"]


MAP = {"Pantry": "component", "Getting Started": "play"}


SIDEBAR = dict(
    top="0",
    left="0",
    bottom="0",
    spacing="5",
    width="320px",
    height="100vh",
    overflow="auto",
    position="sticky",
    padding="80px 18px",
    scrollbar_width="none",
    background=rx.color("gray", 2),
    display=["none" if i <= 3 else "flex" for i in range(6)],
    mask="linear-gradient(to bottom, hsl(0, 0%, 0%, 1) 90%, hsl(0, 0%, 0%, 0) 100%)",
)

TITLE = dict(
    width="100%",
    height="36px",
    align="center",
    justify="between",
    padding="0px 10px",
    border_radius="0px 5px 5px 0px",
    border_left=f"1px solid {BORDER}",
    background=rx.color("gray", 4),
)

ITEM = dict(
    width="100%",
    height="36px",
    align="center",
    justify="start",
    padding_left="10px",
    border_radius="0px 5px 5px 0px",
)


def title(name: str, icon: str):
    return rx.hstack(
        rx.text(name, size="1", color=ACTIVE, weight="bold"),
        rx.icon(tag=icon, size=15, color=ACTIVE),
        **TITLE,
    )


def item(data: dict[str, str]):
    return rx.hstack(
        rx.link(
            rx.text(
                data["name"],
                size="2",
                color=data["color"],
                weight="medium",
                on_click=Sidebar.delta_page(data),
            ),
            href=data["path"],
            text_decoration="none",
        ),
        **ITEM,
        border_left=data["border"],
        background=data["bg"],
    )


def sidebar_menu(name: str, routes: list[dict[str, str]]):
    return rx.vstack(
        title(name, MAP[name]),
        rx.foreach(routes, item),
        width="100%",
        spacing="0",
    )


def sidebar() -> rx.vstack:
    return rx.vstack(
        sidebar_menu("Getting Started", Sidebar.getting_started),
        sidebar_menu("Pantry", Sidebar.pantry),
        **SIDEBAR,
    )
