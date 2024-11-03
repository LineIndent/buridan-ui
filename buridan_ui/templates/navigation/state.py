import reflex as rx
from reflex.constants.colors import Color

from ...routes.routes import NavigationRoutes

active: dict[str, Color] = {"color": rx.color("slate", 12)}
passive: dict[str, Color] = {"color": rx.color("slate", 10)}


class NavigationState(rx.State):
    NavigationRoutes: list[dict[str, str]] = [
        {**route, **passive} for route in NavigationRoutes
    ]

    async def toggle_page_change(self, route: dict[str, str]):
        if route is not None:
            for index in self.NavigationRoutes:
                index["color"] = (
                    active["color"]
                    if index["name"] == route["name"]
                    else passive["color"]
                )
