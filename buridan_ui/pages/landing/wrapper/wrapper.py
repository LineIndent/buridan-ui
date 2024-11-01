from typing import Literal

import reflex as rx

from .style import LandingPageSectionWrapperStyle

ButtonStyle = Literal["classic", "ghost", "outline", "soft", "solid", "surface"]


def landing_page_main_button(name: str, style: ButtonStyle, **kwargs) -> rx.button:
    return rx.button(name, variant=style, cursor="pointer", **kwargs)


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
                    "Getting Started",
                    "solid",
                    on_click=rx.redirect("/getting-started/introduction"),
                ),
                landing_page_main_button(
                    "Explore Pantry Items",
                    "outline",
                    on_click=rx.redirect("/pantry/animation"),
                ),
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
