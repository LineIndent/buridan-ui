from functools import wraps
from typing import Callable

import reflex as rx

from buridan_ui.templates.drawer.drawer import drawer
from buridan_ui.templates.footer.footer import desktop_footer, footer
from buridan_ui.templates.navigation.navigation import docs_navigation
from buridan_ui.templates.sidemenu.sidemenu import sidemenu
from buridan_ui.templates.wrapper.wrapper import baseWrapperHeader

from .style import BaseWrapperStyle
from .utils.navigation import (
    blueprints_in_page_navigation,
    charts_in_page_navigation,
    getting_started_in_page_navigation,
    pantry_in_page_navigation,
)
from .utils.routes import base_content_path_ui


def base_footer_responsive(component: rx.Component, start: str, end: str):
    return rx.box(
        component,
        display=[start if i <= 3 else end for i in range(6)],
        width="100%",
    )


def base(url: str, page_name: str):

    def decorator(content: Callable[[], list[rx.Component]]):
        @wraps(content)
        def template():
            contents = content()
            return rx.hstack(
                *[drawer(), sidemenu(), docs_navigation()],
                rx.vstack(
                    rx.vstack(
                        rx.divider(height="1em", opacity="0"),
                        baseWrapperHeader(base_content_path_ui(url), page_name),
                        rx.divider(height="1em", opacity="0"),
                        *contents,
                        rx.divider(height="2em", opacity="0"),
                        max_width="95%",
                        **BaseWrapperStyle.content,
                    ),
                    pantry_in_page_navigation(url),
                    charts_in_page_navigation(url),
                    getting_started_in_page_navigation(url),
                    blueprints_in_page_navigation(url),
                    rx.vstack(
                        base_footer_responsive(desktop_footer(), "none", "flex"),
                        base_footer_responsive(footer(), "flex", "none"),
                        width="100%",
                        max_width="95%",
                        align="center",
                        padding="0.75em 0em",
                    ),
                    position="relative",
                    width="100%",
                    align="center",
                    height=["100%" if i == 0 else "100vh" for i in range(6)],
                    overflow=["" if i == 0 else "scroll" for i in range(6)],
                ),
                **BaseWrapperStyle.parent,
            )

        return template

    return decorator
