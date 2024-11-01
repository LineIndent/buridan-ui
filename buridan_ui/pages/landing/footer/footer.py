import reflex as rx

from .style import LandingPageFooterStyle

from ....templates.shared.sidebar import Sidebar

from ....routes.pantry_routes import PANTRY_ROUTES
from ....routes.started_routes import GETTING_STARTED_ROUTES
from ....routes.interactive import INTERACTIVE
from ....routes.chart_routes import CHART_ROUTES
from ....routes.resources_routes import RESOURCES


def create_footer_item(title: str, item_list: list[dict[str, str]]):
    return rx.vstack(
        rx.text(title, weight="bold", size="3"),
        rx.hstack(
            *[
                rx.hstack(
                    rx.link(
                        rx.text(
                            item["name"],
                            weight="medium",
                            size="3",
                            text_align="start",
                            color=rx.color("slate", 11),
                            on_click=Sidebar.delta_page(item),
                        ),
                        href=item["path"],
                    ),
                    rx.cond(
                        item.get("is_beta", ""),
                        rx.badge("Beta", color_scheme="orange"),
                        rx.spacer(),
                    ),
                    align="center",
                )
                for item in item_list
            ],
            **LandingPageFooterStyle.footer_item,
        ),
        width="100%",
        padding="0.5em 0em",
    )


def landing_page_footer():
    return rx.vstack(
        create_footer_item("Home", GETTING_STARTED_ROUTES),
        create_footer_item("Interactive Applications", INTERACTIVE),
        create_footer_item("Charts UI", CHART_ROUTES),
        create_footer_item("Pantry UI", PANTRY_ROUTES),
        create_footer_item("Resources", RESOURCES),
        rx.divider(height="2em", opacity="0"),
        rx.vstack(
            rx.heading("buridan/ui", size="5", font_weight="900"),
            rx.text(
                "© 2024 Ahmad Hakim. All rights reserved.", size="2", weight="bold"
            ),
            width="100%",
        ),
        **LandingPageFooterStyle.base,
    )
