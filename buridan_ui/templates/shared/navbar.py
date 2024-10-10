from ...styles.base import *
from ..navlinks import navlinks
from ...routes.pantry_routes import PANTRY_ROUTES
from ...routes.started_routes import GETTING_STARTED_ROUTES

from .drawbar import drawbar

import reflex as rx

NAVLINKS = [
    {"name": "Home", "path": "/"},
    {"name": "Pantry", "path": PANTRY_ROUTES[0]["path"]},
    {"name": "Getting Started", "path": GETTING_STARTED_ROUTES[0]["path"]},
    {"name": "Interactive Table", "path": "/interactive-table/dashboard"},
]

NAVBAR = dict(
    top="0",
    width="100%",
    z_index="20",
    align="center",
    position="fixed",
    justify="between",
    padding="14px 18px",
    backdrop_filter="blur(10px)",
    background=rx.color("gray", 3),
    border_bottom=f"1px solid {rx.color('gray', 5)}",
)


def left_items():
    return rx.hstack(
        rx.image(
            src="/logo.jpg",
            width="22px",
            height="22px",
            border_radius="15%",
            object_fit="fit",
            border=f"1px solid {rx.color('slate', 12)}",
        ),
        rx.heading("buridan/ui", size="5", font_weight="900", color=ACTIVE),
        align="center",
    )


def right_items():
    return rx.hstack(
        rx.hstack(
            *[navlinks(i["name"], i["path"]) for i in NAVLINKS],
            display=["none", "none", "none", "none", "flex", "flex"],
        ),
        rx.hstack(
            drawbar(),
            display=["flex", "flex", "flex", "flex", "none", "none"],
        ),
        rx.divider(orientation="vertical", height="20px", color=rx.color("slate", 12)),
        rx.icon(tag="github", size=16),
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
            padding="12px 0px",
            border_bottom=f"1px solid {rx.color('slate', 7)}",
        ),
        width="100%",
        top="0",
        z_index="20",
        max_width="80em",
        position="absolute",
        padding="12px",
    )
