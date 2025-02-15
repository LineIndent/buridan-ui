from typing import Literal

import reflex as rx

# from ....states.routing import SiteRoutingState
from .style import LandingPageButtons, LandingPageSectionWrapperStyle

ButtonStyle = Literal["classic", "ghost", "outline", "soft", "solid", "surface"]
KeyDisplay = ["none" if i <= 2 else "flex" for i in range(6)]


def button(name: str, class_name: str, text_color: rx.Color, **props) -> rx.Component:
    return rx.button(
        rx.text(name, size="1", color=text_color),
        class_name=class_name,
        **LandingPageButtons.base,
        **props,
    )


def button_with_key(
    tag: str,
    cmd: str,
    name: str,
    style: ButtonStyle,
    func: callable,
) -> rx.Component:
    return rx.button(
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
            # rx.badge(badge, variant="surface", size="1"),
            rx.heading(title, font_weight="900", size="8"),
            rx.text(subtitle, weight="medium", size="2"),
            rx.divider(height="1em", opacity="0"),
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
                font_weight="800",
                line_height="1em",
                font_size=["2.5em", "2.5em", "3em", "3em", "3em", "3em"],
            ),
            rx.text(
                subtitle,
                weight="medium",
                size="2",
                max_width="40em",
                color=rx.color("slate", 11),
            ),
            rx.divider(height="1em", opacity="0"),
            rx.hstack(
                button(
                    "Get Started",
                    "bg-blue-500 border border-solid border-blue-500 hover:brightness-110 font-semibold py-5 px-4 rounded-lg shadow-md text-white",
                    rx.color("white"),
                    on_click=rx.redirect("/getting-started/introduction/"),
                ),
                button(
                    "Pantry & Charts",
                    "bg-inherit hover:brightness-110 font-semibold py-5 px-4 rounded-lg shadow-md",
                    rx.color("slate", 12),
                    border=f"1px solid {rx.color('gray', 4)}",
                    on_click=rx.redirect("/pantry/animations/"),
                ),
                width="100%",
                max_width=["22em" if i >= 2 else "100%" for i in range(6)],
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
    subtitle: str,
    title: str,
    tag: str,
    components: list[rx.Component] = [],
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
