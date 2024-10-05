from ..templates.shared.navbar import navbar
from ..templates.shared.sidebar import sidebar
from ..templates.shared.footer import footer

from typing import Callable, List
from functools import wraps

import reflex as rx

PADDING = [
    "108px 12px 72px 12px",
    "108px 12px 72px 12px",
    "108px 12px 72px 12px",
    "108px 48px 72px 48px",
    "108px 64px 72px 64px",
    "108px 128px 72px 128px",
]

GRANDPARENT = dict(
    spacing="0",
    width="100%",
    height="100vh",
    overflow="hidden",
    scrollbar_width="thin",
)

PARENT = dict(
    spacing="0",
    width="100%",
    overflow="auto",
    scrollbar_width="thin",
)

CONTENT = dict(
    z_index="5",
    width="100%",
    spacing="9",
    padding="54px 0px",
    overflow_y="auto",
    min_height="100vh",
    overflow_x="hidden",
    transition="all 350ms ease",
    background=rx.color("gray", 3),
)

HEADER = dict(
    top="0",
    left="0",
    right="0",
    spacing="2",
    width="100%",
    align="center",
    padding=PADDING,
    justify="center",
    position="sticky",
    background_size="21px 21px",
    background=rx.color("gray", 2),
    border_left=f"1px solid {rx.color('gray', 4)}",
)


def title(name: str):
    return rx.heading(name, size="8", weight="bold")


def base(url: str, page_name: str):
    def decorator(content: Callable[[], List[rx.Component]]):
        @wraps(content)
        @rx.page(route=url, title=page_name)
        def template(*args, **kwargs):
            contents = content(*args, **kwargs)
            return rx.vstack(
                navbar(),
                rx.hstack(
                    sidebar(),
                    rx.vstack(
                        rx.vstack(
                            # create_route_ui(route),
                            title(page_name),
                            **HEADER,
                        ),
                        rx.vstack(
                            *contents,
                            # create_page_prev_and_next_navigation(route),
                            **CONTENT,
                        ),
                        footer(),
                        width="100%",
                        spacing="0",
                    ),
                    **PARENT,
                ),
                **GRANDPARENT,
            )

        return template

    return decorator
