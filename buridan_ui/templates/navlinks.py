from ..styles.base import *
from ..templates.shared.sidebar import Sidebar
from ..routes.pantry_routes import PANTRY_ROUTES
import reflex as rx


def navlinks(name: str, path: str) -> rx.link:
    data = next(
        (route for route in PANTRY_ROUTES if route["path"] == path),
        None,
    )

    return rx.link(
        rx.text(
            name,
            size="2",
            color=ACTIVE,
            _hover={"color": ""},
            weight="bold",
            on_click=Sidebar.delta_page(data),
        ),
        href=path,
        underline="none",
    )
