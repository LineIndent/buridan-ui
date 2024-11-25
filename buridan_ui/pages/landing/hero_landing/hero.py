import reflex as rx

from .state import HeroLandingState
from .style import HeroStyle

from .components.h2 import hero_login_01, logins_v2
from .components.h3 import hero_inputs
from .components.h1 import payments_v1

from ..wrapper.wrapper import landing_page_section_wrapper_main

from buridan_ui.wrappers.shared.scheme import component_wrapper_color_scheme_hero
from buridan_ui.wrappers.shared.responsive import (
    component_wrapper_responsive_menu_hero,
)
from buridan_ui.wrappers.shared.source import component_wrapper_source_code


def hero():
    return rx.hstack(
        rx.hstack(
            rx.vstack(
                # ... hero_landing header goes here ...
                landing_page_section_wrapper_main(
                    "Build your next web app, faster than ever.",
                    "Beautifully designed, expertly crafted components and templates built for the Reflex framework, empowering you to develop web apps in pure Python.",
                ),
                **HeroStyle.header,
            ),
            rx.vstack(
                rx.vstack(
                    # ... components go here ...
                    rx.hstack(
                        rx.vstack(
                            rx.switch(
                                size="2",
                                style=HeroLandingState.component,
                                transition="filter 300ms ease 1000ms, transform 300ms ease 1000ms, opacity 300ms ease 1000ms",
                            ),
                            rx.hstack(
                                rx.box(
                                    component_wrapper_color_scheme_hero(),
                                    style=HeroLandingState.component,
                                    transition="filter 300ms ease 1150ms, transform 300ms ease 1150ms, opacity 300ms ease 1150ms",
                                ),
                                rx.button(
                                    "Button",
                                    variant="surface",
                                    color_scheme="gray",
                                    size="2",
                                    style=HeroLandingState.component,
                                    transition="filter 300ms ease 900ms, transform 300ms ease 900ms, opacity 300ms ease 900ms",
                                ),
                                align="end",
                            ),
                            spacing="4",
                            align="end",
                        ),
                        hero_login_01(),
                        align="end",
                        spacing="5",
                    ),
                    rx.hstack(
                        rx.vstack(
                            component_wrapper_source_code("#"),
                            component_wrapper_responsive_menu_hero(0),
                            align="end",
                            style=HeroLandingState.component,
                            transition="filter 300ms ease 650ms, transform 300ms ease 650ms, opacity 300ms ease 650ms",
                        ),
                        hero_inputs,
                        width="600px",
                        align="center",
                    ),
                    rx.hstack(
                        logins_v2(),
                        payments_v1(),
                        width="900px",
                        justify="end",
                    ),
                    **HeroStyle.components,
                ),
                **HeroStyle.content,
            ),
            **HeroStyle.body,
        ),
        **HeroStyle.root,
    )
