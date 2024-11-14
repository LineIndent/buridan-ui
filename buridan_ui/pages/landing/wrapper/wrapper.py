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
            rx.badge(badge, variant="surface", size="3"),
            rx.heading(title, font_weight="900", size="8"),
            rx.text(subtitle),
            rx.link(link, href=path),
            **LandingPageSectionWrapperStyle.titles_secondary,
        ),
        *components,
        # ... wrapper style
        **LandingPageSectionWrapperStyle.wrapper_secondary,
    )


def landing_page_section_wrapper_main(
    badge: str, title: str, subtitle: str
) -> rx.vstack:
    return rx.vstack(
        # ... badge, title, subtitle, and link
        rx.vstack(
            rx.badge(badge, variant="surface", size="3"),
            rx.heading(title, font_weight="900", size="9"),
            rx.text(subtitle),
            rx.hstack(
                button(
                    "component",
                    "Explore Pantry",
                    "solid",
                    SiteRoutingState.toggle_page_change(
                        {"name": "Animations", "path": "/pantry/animations"}
                    ),
                ),
                button_with_key(
                    "github",
                    "C",
                    "View Source",
                    "surface",
                    rx.redirect("https://github.com/LineIndent/buridan-ui"),
                ),
                width="100%",
                max_width="30em",
                display="grid",
                grid_template_columns=[
                    f"repeat({i}, minmax(0, 1fr))" for i in [1, 1, 2, 2, 2, 2]
                ],
            ),
            **LandingPageSectionWrapperStyle.titles,
        ),
        # ... wrapper style
        min_height="60vh",
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
                rx.text(
                    subtitle,
                    size="4",
                ),
                spacing="1",
            ),
            *components,
        ),
        **LandingPageSectionWrapperStyle.features,
    )
