import reflex as rx

from ...routes.pantry_routes import PANTRY_ROUTES
from .navbar import left_items

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
        rx.text(title, weight="bold", size="2", color=rx.color("slate", 11)),
        rx.hstack(
            *[
                rx.text(
                    item["name"],
                    weight="bold",
                    size="1",
                    text_align="start",
                    color=rx.color("slate", 12),
                )
                for item in item_list
            ],
            display="grid",
            grid_template_columns=[
                f"repeat({i}, minmax(0, 1fr))" for i in [2, 2, 3, 4, 4]
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
                    left_items(),
                    rx.hstack(
                        rx.link(
                            rx.icon(
                                tag="github",
                                size=18,
                                color=rx.color("slate", 11),
                            ),
                            href="#",
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
                            href="#",
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
                rx.spacer(flex_grow="1"),
                rx.text(
                    "Copyright © 2024 Ahmad Hakim.",
                    size="1",
                    color=rx.color("slate", 11),
                    weight="bold",
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
                        {"name": "Installation"},
                        {"name": "Who is Buridan?"},
                        {"name": "Interactive Tables"},
                    ],
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
                        {"name": "Reflex Framework"},
                        {"name": "Source Code"},
                        {"name": "GitHub"},
                        {"name": "@LineIndent"},
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
            height="100%",
        ),
        position="sticky",
        left="0",
        bottom="0",
        height="100%",
        width="100%",
        align="stretch",
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
