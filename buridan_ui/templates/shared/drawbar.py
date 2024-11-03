import reflex as rx

from ...routes.chart_routes import CHART_ROUTES
from ...routes.started_routes import GETTING_STARTED_ROUTES
from ...routes.pantry_routes import PANTRY_ROUTES
from ...routes.interactive import INTERACTIVE

from ...styles.base import ACTIVE

from ..sidemenu.state import SideMenuState


class Drawbar(rx.State):
    is_open: bool = False

    def toggle_drawer(self):
        self.is_open = not self.is_open


ITEM = dict(
    width="100%",
    height="40px",
    align="center",
    justify="between",
    padding="0.75em 1em",
    border_top=f"1px solid {rx.color('gray', 5)}",
)


def title(name: str, icon: str):
    return rx.badge(
        rx.hstack(
            rx.text(name, size="1", color=ACTIVE, weight="bold"),
            rx.icon(tag=icon, size=15, color=ACTIVE),
            align="center",
            justify="between",
            width="100%",
        ),
        width="100%",
        height="36px",
        padding="0px 10px",
        border_radius="0px 5px 5px 0px",
        variant="soft",
        border_left=f"1px solid {rx.color('gray')}",
        color_scheme="gray",
    )


def item(data: dict[str, str]):

    return rx.hstack(
        rx.link(
            rx.text(
                data["name"],
                size="2",
                color=rx.color("slate", 11),
                weight="medium",
                on_click=[
                    Drawbar.toggle_drawer,
                    SideMenuState.toggle_page_change(data),
                ],
                _hover={"color": rx.color("slate", 12)},
            ),
            href=data["path"],
            text_decoration="none",
        ),
        rx.cond(
            data.get("is_beta", ""),
            rx.badge("In Progress", color_scheme="orange"),
            rx.cond(
                data.get("is_new", ""),
                rx.badge("New", color_scheme="grass"),
                rx.spacer(),
            ),
        ),
        **ITEM,
    )


def drawbar() -> rx.drawer:
    return rx.drawer.root(
        rx.drawer.overlay(z_index="999"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.box(
                        rx.hstack(
                            rx.heading(
                                rx.link(
                                    rx.text(
                                        "buridan/ui",
                                        color=ACTIVE,
                                    ),
                                    href="/",
                                    text_decoration="none",
                                    _hover={"color": ACTIVE},
                                    on_click=Drawbar.toggle_drawer,
                                ),
                                size="5",
                                font_weight="900",
                                color=ACTIVE,
                            ),
                            rx.image(
                                src="/logo.jpg",
                                width="22px",
                                height="22px",
                                border_radius="15%",
                                object_fit="fit",
                                border=f"1px solid {rx.color('slate', 12)}",
                            ),
                            justify="between",
                            align="end",
                            width="100%",
                            padding="0.75em 1em",
                            height="100px",
                            bg=rx.color("gray", 1),
                        ),
                        width="100%",
                    ),
                    rx.badge(
                        rx.hstack(
                            rx.text(
                                "Getting started", size="1", color=ACTIVE, weight="bold"
                            ),
                            rx.icon(tag="play", size=15, color=ACTIVE),
                            align="center",
                            justify="between",
                            width="100%",
                            padding="0.75em 1em",
                        ),
                        width="100%",
                        height="40px",
                        color_scheme="gray",
                    ),
                    *[item(data) for data in GETTING_STARTED_ROUTES],
                    rx.badge(
                        rx.hstack(
                            rx.text(
                                "Interactive Tables",
                                size="1",
                                color=ACTIVE,
                                weight="bold",
                            ),
                            rx.icon(tag="play", size=15, color=ACTIVE),
                            align="center",
                            justify="between",
                            width="100%",
                            padding="0.75em 1em",
                        ),
                        width="100%",
                        height="40px",
                        color_scheme="gray",
                    ),
                    *[item(data) for data in INTERACTIVE],
                    rx.badge(
                        rx.hstack(
                            rx.text("Charts", size="1", color=ACTIVE, weight="bold"),
                            rx.icon(tag="table-columns-split", size=15, color=ACTIVE),
                            align="center",
                            justify="between",
                            width="100%",
                            padding="0.75em 1em",
                        ),
                        width="100%",
                        height="40px",
                        color_scheme="gray",
                    ),
                    *[item(data) for data in CHART_ROUTES],
                    rx.badge(
                        rx.hstack(
                            rx.text("Pantry", size="1", color=ACTIVE, weight="bold"),
                            rx.icon(tag="component", size=15, color=ACTIVE),
                            align="center",
                            justify="between",
                            width="100%",
                            padding="0.75em 1em",
                        ),
                        width="100%",
                        height="40px",
                        color_scheme="gray",
                    ),
                    *[item(data) for data in PANTRY_ROUTES],
                    width="100%",
                    height="100%",
                    spacing="0",
                    padding_bottom="2em",
                ),
                top="auto",
                right="auto",
                height="100%",
                overflow="scroll",
                width="15em",
                background=rx.color("gray", 2),
                on_interact_outside=Drawbar.toggle_drawer(),
            ),
            z_index="999",
        ),
        direction="left",
        open=Drawbar.is_open,
    )
