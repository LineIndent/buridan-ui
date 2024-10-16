from ..routes.chart_routes import CHART_ROUTES
from ..styles.base import *
from ..templates.shared.sidebar import Sidebar
from ..routes.pantry_routes import PANTRY_ROUTES
from ..routes.started_routes import GETTING_STARTED_ROUTES
import reflex as rx

normalized_links = {
    "Home": {"name": "Home", "path": "/"},
    "Getting Started": {
        "name": GETTING_STARTED_ROUTES[0]["name"],
        "path": GETTING_STARTED_ROUTES[0]["path"],
    },
    "Pantry": {"name": PANTRY_ROUTES[0]["name"], "path": PANTRY_ROUTES[0]["path"]},
    "Interactive Table": {
        "name": "Interactive Table",
        "path": "/interactive-table/dashboard",
    },
    "Charts": {"name": CHART_ROUTES[0]["name"], "path": CHART_ROUTES[0]["path"]},
}


def navlinks(name: str, path: str) -> rx.link:
    data = normalized_links.get(name)

    return rx.link(
        rx.text(
            name,
            size="2",
            color=ACTIVE,
            _hover={"color": ""},
            weight="bold",
            on_click=Sidebar.delta_page(data),
        ),
        href=data["path"],
        underline="none",
    )
