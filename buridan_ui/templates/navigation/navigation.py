import reflex as rx
from reflex.constants.colors import Color

from .style import NavigationStyle
from ...templates.drawer.state import DrawerState
from ...states.routing import SiteRoutingState


def navigation_links(data: dict[str, str | Color]):
    return rx.link(
        rx.text(
            data["name"],
            size="2",
            weight="bold",
            color=data["color"],
            _hover={"color": rx.color("slate", 12)},
            transition="color 350ms ease",
        ),
        href=data["path"],
        text_decoration="none",
        on_click=SiteRoutingState.toggle_page_change(data),
    )


def navigation_right_side_items():
    return rx.hstack(
        rx.hstack(
            rx.foreach(SiteRoutingState.NavigationRoutes, navigation_links),
            display=["none", "none", "none", "none", "none", "flex"],
            align="center",
        ),
        rx.divider(
            orientation="vertical",
            height="30px",
            width="0.75px",
            color_scheme="gray",
            display=["none", "none", "none", "none", "none", "flex"],
            margin="0em 0.5em",
        ),
        rx.hstack(
            rx.link(
                rx.icon(
                    tag="github",
                    size=16,
                    color=rx.color("slate", 12),
                    fill=rx.color("slate", 12),
                ),
                href="https://github.com/LineIndent/buridan-ui",
                display=["none", "none", "none", "none", "none", "flex"],
            ),
            rx.color_mode.switch(size="1"),
            align="center",
        ),
        rx.button(
            rx.icon(tag="align-justify", size=15),
            on_click=DrawerState.toggle_drawer,
            size="1",
            variant="soft",
            color_scheme="gray",
            cursor="pointer",
            display=["flex", "flex", "flex", "flex", "flex", "none"],
        ),
        align="center",
    )


def navigation_left_side_items():
    return rx.hstack(
        rx.image(src="/logo.jpg", **NavigationStyle.logo),
        rx.heading(
            "buridan/ui",
            size="5",
            font_weight="900",
            cursor="pointer",
            on_click=[
                SiteRoutingState.toggle_page_change({"name": "Home", "path": "/"}),
                rx.redirect("/"),
            ],
        ),
        align="center",
    )


def navigation():
    return rx.hstack(
        navigation_left_side_items(),
        navigation_right_side_items(),
        **NavigationStyle.base,
    )


def landing_page_navigation():
    return rx.hstack(
        navigation_left_side_items(),
        navigation_right_side_items(),
        **NavigationStyle.landing_page_nav,
    )
