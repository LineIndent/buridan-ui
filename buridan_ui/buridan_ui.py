import reflex as rx

from .wrappers.base import base

from .routes.routes import Routes

from .pantry.exports import pantry_exports_config
from .charts.exports import charts_exports_config
from .pages.started_items.exports import getting_started_config
from .pages.interactive.exports import interactive_config
from .pages.landing.hero import landing_page


AppFontURL: str = (
    "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap"
)

app = rx.App(
    stylesheets=[AppFontURL],
    style={
        "background": "transparent",
        rx.heading: {"font_family": "inter"},
        rx.text: {"font_family": "inter"},
    },
    theme=rx.theme(scaling="95%", accent_color="blue"),
)


def get_exports(directory: str, config_file: dict[str, list[callable]]):
    return [export() for export in config_file[directory]]


def add_routes(
    routes: list[dict[str, str]],
    export_config: dict[str, list[callable]],
):
    for route in routes:

        @base(route["path"], route["name"])
        def export_page() -> callable:
            if route["name"] == "Standard Tables":
                return get_exports(route["dir"], export_config)[1:]
            elif route["name"] == "Table Pagination":
                return get_exports(route["dir"], export_config)[:1]
            return get_exports(route["dir"], export_config)

        app.add_page(
            export_page(), route=route["path"], title=f"{route['name']} - Buridan UI"
        )


# ... set the DEV var to True for faster hot reload
# ... ... change the ENV to match the page in progress
DEV: bool = True

if DEV:
    # ... ex: working with X item Y -> set the ENV data as such:
    ENV = {
        "path": "/pantry/featured",
        "name": "Featured",
        "dir": "featured",
        "config": pantry_exports_config,
    }

    @base(ENV["path"], ENV["name"])
    def __() -> callable:
        return [export() for export in ENV["config"][ENV["dir"]]]

    app.add_page(landing_page(), route="/", title="Buridan UI")
    app.add_page(__(), route=ENV["path"], title=f"{ENV['name']} - Buridan UI")

else:
    app.add_page(landing_page(), route="/", title="Buridan UI")
    add_routes(Routes.interactive, interactive_config)
    add_routes(Routes.pantries, pantry_exports_config)
    add_routes(Routes.charts, charts_exports_config)
    add_routes(Routes.started, getting_started_config)
