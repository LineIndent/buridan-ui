from ...styles.base import *
from ..navlinks import navlinks
from ...routes.pantry_routes import PANTRY_ROUTES
from ...routes.started_routes import GETTING_STARTED_ROUTES

from .drawbar import Drawbar

import reflex as rx

NAVLINKS = [
    {"name": "Home", "path": "/"},
    {"name": "Getting Started", "path": GETTING_STARTED_ROUTES[0]["path"]},
    {"name": "Pantry", "path": PANTRY_ROUTES[0]["path"]},
    {"name": "Interactive Table", "path": "/interactive-table/dashboard"},
]

NAVBAR = dict(
    top="0",
    width="100%",
    z_index="20",
    align="center",
    position="fixed",
    justify="between",
    padding="13px 18px",
    backdrop_filter="blur(10px)",
    background=rx.color("gray", 3),
    border_bottom=f"1px solid {rx.color('gray', 5)}",
)


def left_items():
    return rx.hstack(
        rx.hstack(
            rx.button(
                rx.icon(tag="align-justify", size=15),
                on_click=Drawbar.toggle_drawer,
                size="1",
                variant="soft",
                color_scheme="gray",
                cursor="pointer",
            ),
            display=["flex", "flex", "flex", "flex", "flex", "none"],
        ),
        rx.hstack(
            rx.image(
                src="/logo.jpg",
                width="22px",
                height="22px",
                border_radius="15%",
                object_fit="fit",
                border=f"1px solid {rx.color('slate', 12)}",
                display=["none", "none", "none", "none", "none", "flex"],
            ),
            rx.heading(
                rx.link(
                    "buridan/ui",
                    href="/",
                    text_decoration="none",
                    _hover={"color": ACTIVE},
                    color=ACTIVE,
                ),
                size="5",
                font_weight="900",
                color=ACTIVE,
            ),
            align="center",
            width="100%",
        ),
        width="320px",
        align="center",
        justify="between",
    )


def right_items():
    return rx.hstack(
        rx.hstack(
            *[navlinks(i["name"], i["path"]) for i in NAVLINKS],
            display=["none", "none", "none", "none", "none", "flex"],
            spacing="4",
        ),
        rx.divider(
            orientation="vertical",
            height="20px",
            color=rx.color("slate", 12),
            display=["none", "none", "none", "none", "none", "flex"],
        ),
        rx.link(
            rx.icon(tag="github", size=16, color=rx.color("slate", 12)),
            href="https://github.com/LineIndent/buridan-ui",
            display=["none", "none", "none", "none", "none", "flex"],
        ),
        rx.color_mode.switch(),
        align="center",
        spacing="4",
        padding="0px 14px",
    )


def navbar_type_v1():
    return rx.hstack(left_items(), right_items(), **NAVBAR)


def navbar_type_v2():
    return rx.box(
        rx.hstack(
            left_items(),
            right_items(),
            align="center",
            justify="between",
            padding="8px 0px",
            border_bottom=f"1px solid {rx.color('slate', 7)}",
        ),
        width="100%",
        padding="6px",
        top="0",
        z_index="20",
        max_width="80em",
        position="absolute",
    )
