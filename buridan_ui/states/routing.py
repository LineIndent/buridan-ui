import asyncio

import reflex as rx

from buridan_ui.routes.routes import (
    BlueprintRoutes,
    ChartRoutes,
    GettingStartedRoutes,
    InteractiveRoutes,
    NavigationRoutes,
    PantryRoutes,
)

active: dict[str, str] = {
    "border_left": f"2px solid {rx.color('blue')}",
    "background": rx.color("blue", 3),
}
passive: dict[str, str] = {
    "border_left": f"1px solid {rx.color('gray', 6)}",
    "background": "none",
}


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
    BlueprintRoutes: list[dict[str, str]] = [
        {**route, **passive} for route in BlueprintRoutes
    ]
    ChartRoutes: list[dict[str, str]] = [{**route, **passive} for route in ChartRoutes]
    PantryRoutes: list[dict[str, str]] = [
        {**route, **passive} for route in PantryRoutes
    ]

    current_page: str

    on_page: str
    on_page_item: str

    @rx.event
    async def toggle_page_change(self, data: dict[str, str]) -> rx.event.redirect:
        if data is not None:
            # Special handling for Home path
            if data["path"] == "/":
                self.current_page = "home"  # Set a special identifier for the home page
            else:
                # Otherwise, extract the first part of the path for other routes
                self.current_page = data["path"].strip("/").split("/")[0]

                self.on_page = self.current_page.capitalize()
                self.on_page_item = data["path"].strip("/").split("/")[1].capitalize()

            # Update the menu for all routes
            results = await asyncio.gather(
                self.update_menu_link(self.GettingStartedRoutes, data),
                self.update_menu_link(self.InteractiveRoutes, data),
                self.update_menu_link(self.ChartRoutes, data),
                self.update_menu_link(self.PantryRoutes, data),
                self.update_menu_link(self.BlueprintRoutes, data),
            )

            # If no result matches, update the NavigationRoutes
            if all(result is None for result in results):
                await self.update_navigation_route()

        return rx.redirect(data["path"])

    async def update_menu_link(
        self,
        menu: list[dict[str, str]],
        item: dict[str, str],
    ) -> None:
        # Loop through each route and update its color
        for index in menu:
            if index["path"] == item["path"]:
                if item["path"] == "/":  # Special case for the Home route
                    self.current_page = "home"
                index["border_left"] = active["border_left"]
                index["background"] = active["background"]
            else:
                index["border_left"] = passive["border_left"]
                index["background"] = passive["background"]

    async def update_navigation_route(self) -> None:
        # Loop through the navigation routes to highlight the active page
        for index in self.NavigationRoutes:
            # Check if the current page is part of the route path
            if index["path"] == "/" and self.current_page == "home":
                index["border_left"] = active["border_left"]
                index["background"] = active["background"]
            elif index["path"].startswith(f"/{self.current_page}"):
                index["border_left"] = active["border_left"]
                index["background"] = active["background"]
            else:
                index["border_left"] = passive["border_left"]
                index["background"] = passive["background"]
