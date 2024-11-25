from typing import Callable, List
from functools import wraps

import reflex as rx

from .style import BaseWrapperStyle

from .utils.routes import base_content_path_ui
from .utils.navigation import (
    pantry_in_page_navigation,
    charts_in_page_navigation,
    getting_started_in_page_navigation,
    blueprints_in_page_navigation,
)

from ...templates.sidemenu.sidemenu import sidemenu
from ...templates.footer.footer import footer, desktop_footer
from ...templates.wrapper.wrapper import baseWrapperHeader
from ...templates.navigation.navigation import docs_navigation
from ...templates.drawer.drawer import drawer


def base_footer_responsive(component: rx.Component, start: str, end: str):
    return rx.box(
        component,
        display=[start if i <= 3 else end for i in range(6)],
        width="100%",
    )


def base(url: str, page_name: str):

    def decorator(content: Callable[[], List[rx.Component]]):
        @wraps(content)
        def template():
            contents = content()
            return rx.hstack(
                *[drawer(), sidemenu(), docs_navigation()],
                rx.vstack(
                    rx.vstack(
                        rx.box(**BaseWrapperStyle.background),
                        rx.divider(height="2em", opacity="0"),
                        baseWrapperHeader(base_content_path_ui(url), page_name),
                        *contents,
                        rx.divider(height="4em", opacity="0"),
                        max_width="95%",
                        align="center",
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
                    ),
                    rx.divider(height="2em", opacity="0"),
                    width="100%",
                    align="center",
                    position="relative",
                ),
                **BaseWrapperStyle.parent,
            )

        return template

    return decorator
