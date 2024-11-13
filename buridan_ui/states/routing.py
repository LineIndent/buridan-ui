import asyncio
import reflex as rx
from reflex.constants.colors import Color

from ..routes.routes import (
    GettingStartedRoutes,
    InteractiveRoutes,
    PantryRoutes,
    ChartRoutes,
    ResourcesRoutes,
    NavigationRoutes,
)


active: dict[str, Color] = {"color": rx.color("blue", 9)}
passive: dict[str, Color] = {"color": rx.color("slate", 11)}


class SiteRoutingState(rx.State):
    NavigationRoutes: list[dict[str, str]] = [
        {**route, **passive} for route in NavigationRoutes
    ]
    GettingStartedRoutes: list[dict[str, str]] = [
        {**route, **passive} for route in GettingStartedRoutes
    ]
    InteractiveRoutes: list[dict[str, str]] = [
        {**route, **passive} for route in InteractiveRoutes
    ]
    ChartRoutes: list[dict[str, str]] = [{**route, **passive} for route in ChartRoutes]
    PantryRoutes: list[dict[str, str]] = [
        {**route, **passive} for route in PantryRoutes
    ]
    ResourcesRoutes: list[dict[str, str]] = [
        {**route, **passive} for route in ResourcesRoutes
    ]

    current_page: str

    async def toggle_page_change(self, data: dict[str, str]):
        if data is not None:
            # Special handling for Home path
            if data["path"] == "/":
                self.current_page = "home"  # Set a special identifier for the home page
            else:
                # Otherwise, extract the first part of the path for other routes
                self.current_page = data["path"].strip("/").split("/")[0]

            # Update the menu for all routes
            results = await asyncio.gather(
                self.update_menu_link(self.GettingStartedRoutes, data),
                self.update_menu_link(self.InteractiveRoutes, data),
                self.update_menu_link(self.ChartRoutes, data),
                self.update_menu_link(self.PantryRoutes, data),
            )

            # If no result matches, update the NavigationRoutes
            if all(result is None for result in results):
                await self.update_navigation_route()

        return rx.redirect(data["path"])

    async def update_menu_link(
        self,
        menu: list[dict[str, str]],
        item: dict[str, str],
    ):
        # Loop through each route and update its color
        for index in menu:
            if index["path"] == item["path"]:
                if item["path"] == "/":  # Special case for the Home route
                    self.current_page = "home"
                index["color"] = active["color"]
            else:
                index["color"] = passive["color"]

    async def update_navigation_route(self):
        # Loop through the navigation routes to highlight the active page
        for index in self.NavigationRoutes:
            # Check if the current page is part of the route path
            if index["path"] == "/" and self.current_page == "home":
                index["color"] = active["color"]
            elif index["path"].startswith(f"/{self.current_page}"):
                index["color"] = active["color"]
            else:
                index["color"] = passive["color"]
