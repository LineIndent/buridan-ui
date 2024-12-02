from typing import Callable

import reflex as rx

from .style import ChangelogStyle

from ...routes.routes import PantryRoutes, ChartRoutes

info: Callable[[str, any], rx.Component] = lambda txt, *args: rx.text(
    txt, size="2", color=rx.color("slate", 11), *args
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
                    color=rx.color("slate", 11),
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


def create_link(name: str, path: str):
    return rx.link(
        rx.text(
            name,
            size="2",
            weight="medium",
            color=rx.color("slate", 11),
            _hover={"color": rx.color("slate", 12)},
            transition="color 350ms ease",
        ),
        href=path,
        text_decoration="none",
    )


def changelog():
    return rx.vstack(
        rx.box(
            rx.vstack(
                wrapper(
                    "Buridan Charts",
                    "December 02, 2024",
                    [
                        info("New charts landing page."),
                        info("New chart item: Radar Charts."),
                        info("New chart theme color: purple."),
                        info("New chart tooltip style sheet."),
                        info("Updated responsive logic for mobile view."),
                        info("Significant UI update to entire chart codebase."),
                        info("New dynamic charting for area, bar, and line charts."),
                        changelog_badge("party-popper", "buridan/ui v0.4.0"),
                    ],
                ),
                wrapper(
                    "Site patches and New Blueprint Items",
                    "November 26, 2024",
                    [
                        info("New blueprint items: Dashboards & Layouts."),
                        info(
                            "Major code refactoring for pantry, charts, and blueprint wrappers."
                        ),
                        changelog_badge("party-popper", "buridan/ui v0.3.4"),
                    ],
                ),
                wrapper(
                    "New library feature: Blueprint Templates",
                    "November 20, 2024",
                    [
                        info(
                            "Blueprints templates consist of in-depth, more well-rounded apps that can be used out of the box with minor changes."
                        ),
                        rx.link(
                            "Authentication",
                            href="/blueprints/anonymous-authentication",
                            color=rx.color("slate", 11),
                            text_decoration="none",
                            is_external=True,
                        ),
                        changelog_badge("party-popper", "buridan/ui v0.3.3"),
                    ],
                ),
                wrapper(
                    "New Site Landing Page and UI Changes",
                    "November 17, 2024",
                    [
                        info("New site landing page with animation!"),
                        info("Fixed UI scaling issue for site: functional."),
                        info("Updated many site components (nav, side menu, etc...)"),
                        changelog_badge("party-popper", "buridan/ui v0.3.2"),
                    ],
                ),
                wrapper(
                    "Small Patch for Site Scaling UI",
                    "November 15, 2024",
                    [
                        info("Fixed UI scaling issue for site: operational."),
                        changelog_badge("party-popper", "buridan/ui v0.3.1"),
                    ],
                ),
                wrapper(
                    "New Apps and Site UI Changes",
                    "November 13, 2024",
                    [
                        info("New pantry: Footers!"),
                        info("New chart item: Pie Charts!"),
                        info("New interactive app: PubMed A.I."),
                        info("UI changes to site landing page."),
                        changelog_badge("party-popper", "buridan/ui v0.3.0"),
                    ],
                ),
                wrapper(
                    "Site Refinement and UI Updates",
                    "November 08, 2024",
                    [
                        info("Changes to Charts component wrapper."),
                        info("Codebase refactor and state changes."),
                        info("Changes to code block theme and font size."),
                        info("Major changes to @component_wrapper menu items."),
                        changelog_badge("party-popper", "buridan/ui v0.2.0"),
                    ],
                ),
                wrapper(
                    "New Interactive App: RAG AI Application",
                    "October 30, 2024",
                    [
                        create_link(
                            "RAG Application",
                            "/intractive/retrieval-augmented-generation",
                        ),
                        changelog_badge("party-popper", "buridan/ui v0.1.0"),
                    ],
                ),
                wrapper(
                    "New Components and Improvements to Pantry Items",
                    "October 21, 2024",
                    [create_pantry_links(PantryRoutes)],
                ),
                wrapper(
                    "New Library Component: Charts",
                    "October 18, 2024",
                    [create_pantry_links(ChartRoutes)],
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
        **ChangelogStyle.base,
    )
