import reflex as rx

from buridan_ui.pages.landing.wrapper.wrapper import landing_page_section_wrapper_main
from buridan_ui.wrappers.shared.responsive import component_wrapper_responsive_menu_hero
from buridan_ui.wrappers.shared.scheme import component_wrapper_color_scheme_hero
from buridan_ui.wrappers.shared.source import component_wrapper_source_code

from .components.h1 import payments_v1
from .components.h2 import hero_login_01, logins_v2
from .components.h3 import hero_inputs
from .style import HeroStyle

active_component = {"filter": "blur(0px)", "transform": "scale(1)", "opacity": "1"}


def set_intro_animation():
    return {
        "position": "relative",
        f"@keyframes intro": {
            "0%": {"filter": "blur(10px)", "transform": "scale(1.5)", "opacity": "0"},
            "100%": {"filter": "blur(0px)", "transform": "scale(1)", "opacity": "1"},
        },
        "animation": "intro 300ms ease",
        "transition": "filter 300ms ease 1000ms, transform 300ms ease 1000ms, opacity 300ms ease 1000ms",
    }


def hero():
    return rx.hstack(
        rx.hstack(
            rx.vstack(
                # ... hero_landing header goes here ...
                landing_page_section_wrapper_main(
                    "Build your next web app, faster than ever",
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
                                **set_intro_animation(),
                            ),
                            rx.hstack(
                                rx.box(
                                    component_wrapper_color_scheme_hero(),
                                    **set_intro_animation(),
                                ),
                                rx.button(
                                    "Button",
                                    variant="surface",
                                    color_scheme="gray",
                                    size="2",
                                    **set_intro_animation(),
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
                            **set_intro_animation(),
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
