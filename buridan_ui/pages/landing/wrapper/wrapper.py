from typing import Literal, Callable

import reflex as rx
from ....states.routing import SiteRoutingState
from .style import LandingPageSectionWrapperStyle, LandingPageButtons

ButtonStyle = Literal["classic", "ghost", "outline", "soft", "solid", "surface"]
KeyDisplay = ["none" if i <= 2 else "flex" for i in range(6)]

button: Callable[[str, str, ButtonStyle, callable], rx.Component] = (
    lambda tag, name, style, func: rx.button(
        rx.icon(tag=tag, size=18),
        rx.text(name, size="2", weight="bold"),
        on_click=func,
        variant=style,
        **LandingPageButtons.base,
    )
)

button_with_key: Callable[[str, str, str, ButtonStyle, callable], rx.Component] = (
    lambda tag, cmd, name, style, func: rx.button(
        rx.icon(tag=tag, size=18),
        rx.text(name, size="2", weight="bold"),
        rx.badge(
            rx.text(cmd),
            width="20px",
            height="20px",
            variant="soft",
            box_shadow="0px 2px 8px 0px rgba(0, 0, 0, 0.25)",
            display=KeyDisplay,
        ),
        on_click=func,
        variant=style,
        **LandingPageButtons.base,
    )
)


def landing_page_section_wrapper(
    badge: str,
    title: str,
    subtitle: str,
    link: str,
    path: str,
    components: list[rx.Component] = [],
) -> rx.vstack:
    return rx.vstack(
        # ... badge, title, subtitle, and link
        rx.vstack(
            rx.badge(badge, variant="surface", size="1"),
            rx.heading(title, font_weight="900", size="8"),
            rx.text(subtitle, weight="medium", size="2"),
            rx.link(link, href=path, size="1"),
            **LandingPageSectionWrapperStyle.titles_secondary,
        ),
        *components,
        # ... wrapper style
        **LandingPageSectionWrapperStyle.wrapper_secondary,
    )


def landing_page_section_wrapper_main(title: str, subtitle: str) -> rx.vstack:
    return rx.vstack(
        # ... badge, title, subtitle, and link
        rx.vstack(
            rx.heading(
                title,
                font_weight="900",
                line_height="1em",
                font_size=["2.85em", "2.85em", "3em", "3em", "3.5em", "3.75em"],
            ),
            rx.text(subtitle, weight="medium", size="3"),
            rx.hstack(
                button(
                    "component",
                    "Explore Pantry",
                    "solid",
                    SiteRoutingState.toggle_page_change(
                        {"name": "Animations", "path": "/pantry/animations"}
                    ),
                ),
                button(
                    "github",
                    "View Source",
                    "surface",
                    rx.redirect("https://github.com/LineIndent/buridan-ui"),
                ),
                width="100%",
                max_width="25em",
                display="grid",
                grid_template_columns=[
                    f"repeat({i}, minmax(0, 1fr))" for i in [1, 1, 2, 2, 2, 2]
                ],
            ),
            **LandingPageSectionWrapperStyle.titles,
        ),
        # ... wrapper style
        **LandingPageSectionWrapperStyle.wrapper,
    )


def blip(tag: str) -> rx.box:
    return rx.box(rx.icon(tag=tag, size=12), **LandingPageSectionWrapperStyle.blip)


def landing_page_features_wrapper(
    subtitle: str, title: str, tag: str, components: list[rx.Component] = []
) -> rx.hstack:
    return rx.hstack(
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    blip(tag),
                    rx.text(title, size="3", font_weight="900"),
                ),
                rx.text(subtitle, size="4", weight="medium"),
                spacing="1",
            ),
            *components,
        ),
        **LandingPageSectionWrapperStyle.features,
    )
