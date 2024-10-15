from ..templates.shared.drawbar import drawbar
from ..templates.shared.navbar import navbar_type_v1
from ..templates.shared.sidebar import sidebar, Sidebar
from ..templates.shared.footer import footer, footer_v1

from ..routes.pantry_routes import PANTRY_ROUTES

from typing import Callable, List
from functools import wraps

import reflex as rx

GRANDPARENT = dict(
    spacing="0",
    width="100%",
    height="100vh",
    overflow="scroll",
    scrollbar_width="thin",
    background=rx.color("gray", 2),
    overscroll_behavior_y="contain",
)

PARENT = dict(
    spacing="0",
    width="100%",
    height="100vh",
    overflow="auto",
    scrollbar_width="thin",
    background=rx.color("gray", 2),
)

CONTENT = dict(
    z_index="5",
    width="100%",
    spacing="9",
    padding="54px 0px 0px 0px",
    position="relative",
    transition="all 350ms ease",
    background=rx.color("gray", 3),
)

HEADER = dict(
    top="0",
    left="0",
    spacing="2",
    width="100%",
    align="center",
    min_height="25vh",
    justify="center",
    background=rx.color("gray", 2),
    border_left=f"1px solid {rx.color('gray', 4)}",
)


def title(name: str):
    return rx.heading(name, size="8", weight="bold")


def create_route_ui(route: str):
    segments = route.strip("/").split("/")
    path_names = [
        item for segment in segments[:-1] for item in [capitalize_words(segment), "/"]
    ] + [capitalize_words(segments[-1])]

    return rx.hstack(
        *[
            (
                rx.text(name, font_size="11px", color_scheme="gray", weight="medium")
                if index != len(path_names) - 1
                else rx.text(name, font_size="11px", weight="medium")
            )
            for index, name in enumerate(path_names)
        ],
        spacing="1",
    )


def capitalize_words(segment: str) -> str:
    return " ".join(word.capitalize() for word in segment.replace("-", " ").split())


def render_prev_and_next_ui(routes: list[dict[str, str]]):
    _prev, _next = routes

    prev_button = (
        rx.hstack(
            rx.icon(tag="arrow-left", size=15, color=rx.color("slate", 12)),
            rx.link(
                rx.text(
                    _prev["name"],
                    weight="bold",
                    size="1",
                    on_click=Sidebar.delta_page(_prev),
                    color=rx.color("slate", 12),
                ),
                href=_prev["path"],
                underline="none",
            ),
            align="center",
            spacing="2",
        )
        if len(_prev) > 1
        else rx.spacer()
    )
    next_button = (
        rx.hstack(
            rx.link(
                rx.text(
                    _next["name"],
                    weight="bold",
                    size="1",
                    on_click=Sidebar.delta_page(_next),
                    color=rx.color("slate", 12),
                ),
                href=_next["path"],
                underline="none",
            ),
            rx.icon(tag="arrow-right", size=15, color=rx.color("slate", 12)),
            align="center",
            spacing="2",
        )
        if len(_next) > 1
        else rx.spacer()
    )

    return rx.badge(
        rx.hstack(
            prev_button,
            next_button,
            justify="between",
            width="100%",
        ),
        position="sticky",
        bottom="0",
        width="100%",
        padding="14px 24px",
        radius="none",
        bg=rx.color("blue", 5),
    )


def create_page_prev_and_next_navigation(path: str) -> rx.Component:
    for i, route in enumerate(PANTRY_ROUTES):
        if route["path"] == path:
            prev_page = PANTRY_ROUTES[i - 1] if i > 0 else [""]
            next_page = PANTRY_ROUTES[i + 1] if i < len(PANTRY_ROUTES) - 1 else [""]

            return render_prev_and_next_ui([prev_page, next_page])

    return rx.spacer()


def base(url: str, page_name: str, **kwargs):
    def decorator(content: Callable[[], List[rx.Component]]):
        @wraps(content)
        @rx.page(route=url, **kwargs)
        def template(*args, **kwargs):
            contents = content(*args, **kwargs)
            return rx.vstack(
                drawbar(),
                navbar_type_v1(),
                rx.hstack(
                    sidebar(),
                    rx.vstack(
                        rx.vstack(
                            rx.vstack(
                                rx.vstack(
                                    create_route_ui(url),
                                    title(page_name),
                                    **HEADER,
                                ),
                                *contents,
                                rx.divider(height="4em", opacity="0"),
                                create_page_prev_and_next_navigation(url),
                                **CONTENT,
                            ),
                            width="100%",
                            position="relative",
                        ),
                        footer_v1(),
                        width="100%",
                        spacing="0",
                    ),
                    **PARENT,
                ),
                **GRANDPARENT,
            )

        return template

    return decorator
