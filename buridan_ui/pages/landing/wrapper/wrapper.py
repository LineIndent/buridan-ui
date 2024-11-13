from typing import Literal

import reflex as rx
from ....states.routing import SiteRoutingState
from .style import LandingPageSectionWrapperStyle

ButtonStyle = Literal["classic", "ghost", "outline", "soft", "solid", "surface"]


def landing_page_main_button(
    tag: str, cmd: str, name: str, style: ButtonStyle, **kwargs
) -> rx.button:
    return rx.button(
        rx.icon(tag=tag, size=18),
        rx.text(
            name,
            size="2",
            weight="bold",
        ),
        (
            rx.badge(rx.text(cmd), width="21px", height="21px", variant="soft")
            if cmd
            else rx.text()
        ),
        variant=style,
        cursor="pointer",
        size="3",
        box_shadow=f"inset 0 -3px 1.5px hsla(0, 0%, 0%, 0.1)",
        transition="all 300ms ease",
        _hover={"box_shadow": "none"},
        radius="small",
        height="42px",
        color_scheme="gray",
        **kwargs,
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
            **LandingPageSectionWrapperStyle.titles,
        ),
        *components,
        # ... wrapper style
        **LandingPageSectionWrapperStyle.wrapper,
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
                landing_page_main_button(
                    "component",
                    "",
                    "Explore Pantry",
                    "soft",
                    on_click=SiteRoutingState.toggle_page_change(
                        {"name": "Animations", "path": "/pantry/animations"}
                    ),
                ),
                landing_page_main_button(
                    "github",
                    "C",
                    "Clone Source",
                    "surface",
                    on_click=rx.redirect("https://github.com/LineIndent/buridan-ui"),
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
    return rx.box(
        rx.icon(tag=tag, size=12),
        **LandingPageSectionWrapperStyle.blip,
    )


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
