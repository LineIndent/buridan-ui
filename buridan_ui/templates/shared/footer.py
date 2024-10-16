import reflex as rx

from .sidebar import Sidebar
from ...routes.chart_routes import CHART_ROUTES
from ...routes.pantry_routes import PANTRY_ROUTES
from ...styles.base import ACTIVE

personal: str = "https://github.com/lineindent"
library: str = "https://github.com/LineIndent/buridan-ui"


def footer():
    return rx.hstack(
        rx.text(
            "Built by ",
            rx.link(
                "Ahmad Hakim",
                color_scheme="gray",
                href=personal,
                is_external=True,
                underline="always",
            ),
            " . More details is available on ",
            rx.link(
                "GitHub",
                color_scheme="gray",
                href=library,
                is_external=True,
                underline="always",
            ),
            " .",
            color_scheme="gray",
            font_size="11px",
            weight="medium",
        ),
        width="100%",
        padding=[
            "32px 32px",
            "32px 32px",
            "32px 32px",
            "32px 32px",
            "32px 48px",
            "32px 64px",
        ],
        position="sticky",
        right="0",
        left="0",
        bottom="0",
        height="150px",
        background=rx.color("gray", 2),
        border_left=f"1px solid {rx.color('gray', 4)}",
    )


def create_footer_item(title: str, item_list: list[dict[str, str]]):
    return rx.vstack(
        rx.text(title, weight="bold", size="2", color=rx.color("slate", 12)),
        rx.hstack(
            *[
                rx.hstack(
                    rx.link(
                        rx.text(
                            item["name"],
                            weight="bold",
                            size="1",
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
            display="grid",
            grid_template_columns=[
                f"repeat({i}, minmax(0, 1fr))" for i in [2, 2, 3, 3, 3, 4]
            ],
            justify="start",
            width="100%",
            gap="1rem 3rem",
        ),
        width="100%",
    )


def footer_v1():
    return rx.vstack(
        rx.spacer(),
        rx.hstack(
            rx.vstack(
                rx.vstack(
                    rx.heading("buridan/ui", size="5", font_weight="900", color=ACTIVE),
                    rx.hstack(
                        rx.link(
                            rx.icon(
                                tag="github",
                                size=18,
                                color=rx.color("slate", 11),
                            ),
                            href="https://github.com/LineIndent/buridan-ui",
                            color_scheme="gray",
                            bg=rx.color("gray", 4),
                            border_radius="20%",
                            padding="3.5px",
                        ),
                        rx.link(
                            rx.icon(
                                tag="youtube",
                                size=18,
                                color=rx.color("slate", 11),
                            ),
                            href="https://www.youtube.com/@lineindent",
                            color_scheme="gray",
                            bg=rx.color("gray", 4),
                            border_radius="20%",
                            padding="3.5px",
                        ),
                        align="center",
                    ),
                    width="100%",
                    flex_grow="1",
                    align="stretch",
                ),
                rx.text(
                    "Copyright © 2024 Ahmad Hakim.",
                    size="1",
                    color=rx.color("slate", 11),
                    weight="bold",
                    height="100%",
                ),
                justify="between",
                flex=["100%", "100%", "100%", "20%", "20%"],
                align="stretch",
                min_height="inherit",
                flex_grow="1",
            ),
            rx.vstack(
                create_footer_item(
                    "Home",
                    [
                        {
                            "name": "Introduction",
                            "path": "/getting-started/introduction",
                        },
                        {
                            "name": "Installation",
                            "path": "/getting-started/installation",
                        },
                        {
                            "name": "Who is Buridan?",
                            "path": "/getting-started/who-is-buridan",
                        },
                        {
                            "name": "Interactive Tables",
                            "path": "/interactive-table/dashboard",
                            "is_beta": True,
                        },
                    ],
                ),
                rx.divider(height="1em", opacity="0"),
                create_footer_item(
                    "Charts",
                    CHART_ROUTES,
                ),
                rx.divider(height="1em", opacity="0"),
                create_footer_item(
                    "Pantry",
                    PANTRY_ROUTES,
                ),
                rx.divider(height="1em", opacity="0"),
                create_footer_item(
                    "Resources",
                    [
                        {"name": "Reflex Framework", "path": "https://reflex.dev/"},
                        {
                            "name": "Source Code",
                            "path": "https://github.com/LineIndent/buridan-ui",
                        },
                        {"name": "GitHub", "path": "https://github.com/LineIndent"},
                        {
                            "name": "@LineIndent",
                            "path": "https://www.youtube.com/@lineindent",
                        },
                    ],
                ),
                rx.divider(height="1em", opacity="0"),
                width="100%",
                flex=["100%", "100%", "100%", "50%", "65%"],
            ),
            width="100%",
            align="start",
            flex_wrap=[
                "wrap-reverse",
                "wrap-reverse",
                "wrap-reverse",
                "wrap",
                "wrap",
            ],
        ),
        width="100%",
        background=rx.color("gray", 2),
        border_left=f"1px solid {rx.color('gray', 4)}",
        padding=[
            "32px 32px",
            "32px 32px",
            "32px 32px",
            "32px 32px",
            "32px 48px",
            "32px 64px",
        ],
    )
