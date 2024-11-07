from typing import Callable, List
from functools import wraps

import reflex as rx

from .style import BaseWrapperStyle

from .utils.routes import base_content_path_ui
from .utils.navigation import pantry_in_page_navigation

from ..templates.sidemenu.sidemenu import sidemenu
from ..templates.footer.footer import footer, desktop_footer
from ..templates.wrapper.wrapper import base_header_wrapper
from ..templates.navigation.navigation import navigation
from ..templates.drawer.drawer import drawer


def base_footer_responsive(component: rx.Component, start: str, end: str):
    return rx.box(
        component,
        display=[start if i <= 4 else end for i in range(6)],
        width="100%",
    )


def base(url: str, page_name: str, **kwargs):

    def decorator(content: Callable[[], List[rx.Component]]):
        @wraps(content)
        def template(*args, **kwargs):
            contents = content(*args, **kwargs)
            return rx.vstack(
                drawer(),
                navigation(),
                rx.hstack(
                    sidemenu(),
                    rx.vstack(
                        rx.vstack(
                            rx.box(**BaseWrapperStyle.background),
                            rx.divider(height="2em", opacity="0"),
                            base_header_wrapper(
                                base_content_path_ui(url),
                                page_name,
                                "See source code on GitHub →",
                                "https://github.com/LineIndent/buridan-ui",
                            ),
                            *contents,
                            rx.divider(height="4em", opacity="0"),
                            max_width="95%",
                            align="center",
                            **BaseWrapperStyle.content,
                        ),
                        pantry_in_page_navigation(url),
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
                ),
                **BaseWrapperStyle.grandparent,
            )

        return template

    return decorator
