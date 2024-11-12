import reflex as rx

from ...routes.routes import PantryRoutes, ChartRoutes
from ...states.routing import SiteRoutingState


def create_button(route, direction):
    if len(route) > 1:
        return rx.hstack(
            (
                rx.icon(tag=f"arrow-{direction}", size=15, color=rx.color("slate", 12))
                if direction == "left"
                else rx.spacer()
            ),
            rx.link(
                rx.text(
                    route["name"],
                    weight="bold",
                    size="1",
                    on_click=SiteRoutingState.toggle_page_change(route),
                    color=rx.color("slate", 12),
                ),
                href=route["path"],
                underline="none",
            ),
            (
                rx.icon(tag=f"arrow-{direction}", size=15, color=rx.color("slate", 12))
                if direction == "right"
                else rx.spacer()
            ),
            align="center",
            spacing="2",
        )

    return rx.spacer()


def render_prev_and_next_ui(routes: list[dict[str, str]]):
    _prev, _next = routes

    prev_button = create_button(_prev, "left")
    next_button = create_button(_next, "right")

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
        z_index="20",
    )


def page_navigation(path: str, routes: list[dict]) -> rx.Component:
    for i, route in enumerate(routes):
        if route["path"] == path:
            prev_page = routes[i - 1] if i > 0 else [""]
            next_page = routes[i + 1] if i < len(routes) - 1 else [""]

            return render_prev_and_next_ui([prev_page, next_page])

    return rx.spacer()


def pantry_in_page_navigation(path: str) -> rx.Component:
    return page_navigation(path, PantryRoutes)


def charts_in_page_navigation(path: str) -> rx.Component:
    return page_navigation(path, ChartRoutes)
