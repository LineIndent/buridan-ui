import reflex as rx

from .style import FooterStyle
from ..sidemenu.state import SideMenuState


def create_footer_item(title: str, routes: list[dict[str, str]]):
    def item(data):
        return rx.hstack(
            rx.link(
                rx.text(
                    data["name"],
                    size="2",
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
        rx.text(title, weight="bold", size="3"),
        rx.hstack(rx.foreach(routes, item), **FooterStyle.footer_item),
        width="100%",
        padding="0.5em 0em",
    )


def footer():
    return rx.vstack(
        create_footer_item("Home", SideMenuState.GettingStartedRoutes),
        create_footer_item("Interactive Applications", SideMenuState.InteractiveRoutes),
        create_footer_item("Charts UI", SideMenuState.ChartRoutes),
        create_footer_item("Pantry UI", SideMenuState.PantryRoutes),
        create_footer_item("Resources", SideMenuState.ResourcesRoutes),
        rx.divider(height="2em", opacity="0"),
        rx.vstack(
            rx.heading("buridan/ui", size="5", font_weight="900"),
            rx.text(
                "© 2024 Ahmad Hakim. All rights reserved.", size="2", weight="bold"
            ),
            width="100%",
        ),
        **FooterStyle.base,
    )


def desktop_footer():
    return rx.vstack(
        rx.vstack(
            rx.heading("buridan/ui", size="5", font_weight="900"),
            rx.text(
                "© 2024 Ahmad Hakim. All rights reserved.", size="2", weight="bold"
            ),
            width="100%",
        ),
        **FooterStyle.base,
    )
