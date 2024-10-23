from dataclasses import dataclass, field

from ..templates.shared.footer import footer_v1
from ..templates.shared.navbar import navbar_type_v2

from ..routes.pantry_routes import PANTRY_ROUTES
from ..routes.chart_routes import CHART_ROUTES

import reflex as rx


@dataclass
class ChangelogStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "min_height": "100vh",
            "background": rx.color("gray", 2),
            "align": "center",
        }
    )

    header: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "30vh",
            "max_width": "35em",
            "align": "start",
            "justify": "center",
            "padding": ["0px 24px" if i <= 2 else "0px 0px" for i in range(6)],
        },
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "max_width": "35em",
            "height": "100%",
            "justify": "end",
            "position": "relative",
            "padding": "1em 1em",
            "spacing": "8",
            "border_left": f"1px solid {rx.color('gray', 6)}",
        },
    )

    blip: dict[str, str] = field(
        default_factory=lambda: {
            "width": "24px",
            "height": "24px",
            "border_radius": "24px",
            "background": rx.color("gray", 3),
            "border": f"1.25px solid {rx.color('gray', 6)}",
            "position": "absolute",
            "left": "-11.5px",
            "align_items": "center",
            "justify_content": "center",
            "display": "flex",
        }
    )

    wrapper: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "align": "start",
            "justify": "start",
            "padding_left": "24px",
            "border_radius": "0px 5px 5px 0px",
        }
    )


ChangelogStyle: ChangelogStyle = ChangelogStyle()


def changelog_back_trigger():
    return rx.badge(
        rx.link(
            rx.text("<- home", size="1", weight="bold", color="inherit"),
            text_decoration="none",
            href="/",
        ),
        width="100%",
        height="30px",
        radius="none",
        top="0",
        left="0",
        position="absolute",
        padding="0em 24px",
    )


def changelog_header():
    return rx.vstack(
        rx.heading("Changelog", color=rx.color("slate", 12)),
        rx.text("See what's new added, changed, fixed, improved or updated."),
        **ChangelogStyle.header,
    )


def blip():
    return rx.box(
        rx.icon(tag="calendar-days", size=11, color=rx.color("gray")),
        **ChangelogStyle.blip,
    )


def wrapper(title: str, date: str, components: list[rx.Component] = []):
    return rx.hstack(
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    blip(),
                    rx.text(date, size="1", weight="bold", color=rx.color("slate", 10)),
                    align="center",
                ),
                rx.text(title, size="3", weight="bold", color=rx.color("slate", 11)),
                spacing="1",
            ),
            *components,
        ),
        **ChangelogStyle.wrapper,
    )


def changelog_badge(tag: str, text: str):
    return rx.hstack(
        rx.box(
            rx.icon(tag=tag, size=14),
            background=rx.color("gray", 2),
            border_radius="100%",
            padding="8px",
            align_items="center",
            justify_content="center",
            display="flex",
        ),
        rx.text(text, size="2", weight="medium"),
        height="35px",
        border_radius="35px",
        background=rx.color("gray", 3),
        align="center",
        justify="start",
        padding="0em 1em 0em 0.25em",
        spacing="2",
    )


def create_pantry_links(item_list: list[dict[str, str]]):
    return rx.vstack(
        *[
            rx.link(
                rx.text(
                    data["name"],
                    size="2",
                    weight="medium",
                    color=rx.color("slate", 10),
                    _hover={"color": rx.color("slate", 12)},
                    transition="color 350ms ease",
                ),
                href=data["path"],
                text_decoration="none",
            )
            for data in item_list
        ],
        spacing="1",
    )


@rx.page("/pro/changelog", title="Changelog - buridan/ui")
def changelog():
    return rx.vstack(
        changelog_back_trigger(),
        changelog_header(),
        rx.box(
            rx.vstack(
                wrapper(
                    "New Components and Improvements to Pantry Items",
                    "October 21, 2024",
                    [create_pantry_links(PANTRY_ROUTES)],
                ),
                wrapper(
                    "New Library Component: Charts",
                    "October 18, 2024",
                    [create_pantry_links(CHART_ROUTES)],
                ),
                wrapper(
                    "buridan/ui v0.0.1 Deployed to Reflex",
                    "October 16, 2024",
                    [
                        changelog_badge("party-popper", "buridan/ui v0.0.1"),
                    ],
                ),
                wrapper("Initial Release", "October 5, 2024"),
                **ChangelogStyle.content,
            ),
            width="100%",
            align_items="center",
            justify_content="center",
            display="flex",
            padding="0px 24px",
        ),
        rx.divider(height="4em", opacity="0"),
        footer_v1(),
        **ChangelogStyle.base,
    )
