import reflex as rx
from reflex.constants.colors import Color

from .style import NavigationStyle
from .state import NavigationState

from ...templates.shared.drawbar import Drawbar


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
        on_click=lambda: NavigationState.toggle_page_change(data),
    )


def navigation_right_side_items():
    return rx.hstack(
        rx.hstack(
            rx.foreach(NavigationState.NavigationRoutes, navigation_links),
            display=["none", "none", "none", "none", "none", "flex"],
            align="center",
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
        rx.button(
            rx.icon(tag="align-justify", size=15),
            on_click=Drawbar.toggle_drawer,
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
            on_click=rx.redirect("/"),
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
