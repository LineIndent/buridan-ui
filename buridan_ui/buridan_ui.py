import reflex as rx

from .charts.exports import (
    charts_exports_config,
    bar_chart_page,
    area_chart_page,
    line_chart_page,
    pie_chart_page,
    radar_chart_page,
)
from .pages.charts_landing.main import charts_landing_page
from .pages.landing.hero import landing_page
from .pages.started_items.exports import getting_started_config
from .pantry.exports import pantry_exports_config
from .analytics.exports import analytics_config_file
from .analytics.landing import analytics_landing_page

from .routes.routes import Routes
from .wrappers.base.main import base

AppFontURL: str = (
    "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap"
)

meta_tags = [
    # HTML Meta Tags
    {"name": "application-name", "content": "Buridan UI"},
    {
        "name": "keywords",
        "content": "buridan, ui, web apps, framework, open source, frontend, backend, full stack",
    },
    {
        "name": "description",
        "content": "Beautifully designed Reflex components to build your web apps faster. Open source.",
    },
    # Facebook Meta Tags
    {
        "property": "og:url",
        "content": "https://buridan-ui.reflex.run/",
    },  # Replace with your actual URL
    {"property": "og:type", "content": "website"},
    {"property": "og:title", "content": "Buridan UI"},
    {
        "property": "og:description",
        "content": "Beautifully designed Reflex components to build your web apps faster. Open source.",
    },
    {
        "property": "og:image",
        "content": "https://raw.githubusercontent.com/buridan-ui/ui/refs/heads/main/assets/new_logo.PNG",
    },
    {
        "property": "og:image:width",
        "content": "1200",
    },  # Ensure the image is 1200x630 pixels
    {"property": "og:image:height", "content": "630"},
    # Twitter Meta Tags
    {"name": "twitter:card", "content": "summary_large_image"},
    {
        "property": "twitter:domain",
        "content": "https://buridan-ui.reflex.run/",
    },  # Replace with your actual domain
    {
        "property": "twitter:url",
        "content": "https://buridan-ui.reflex.run/",
    },  # Replace with your actual URL
    {"name": "twitter:title", "content": "Buridan UI"},
    {
        "name": "twitter:description",
        "content": "Beautifully designed Reflex components to build your web apps faster. Open source.",
    },
    {
        "name": "twitter:image",
        "content": "https://raw.githubusercontent.com/buridan-ui/ui/refs/heads/main/assets/new_logo.PNG",
    },
]

app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=[AppFontURL],
    style={
        "background": "transparent",
        rx.heading: {"font_family": "inter"},
        rx.text: {"font_family": "inter"},
    },
)


def get_exports(directory: str, config_file: dict[str, list[callable]]):
    return [export() for export in config_file[directory]]


def add_routes(
    routes: list[dict[str, str]],
    export_config: dict[str, list[callable]],
) -> None:
    for route in routes:

        @base(route["path"], route["name"])
        def export_page() -> callable:
            if route["name"] == "Standard Tables":
                return get_exports(route["dir"], export_config)[1:]
            if route["name"] == "Table Pagination":
                return get_exports(route["dir"], export_config)[:1]
            return get_exports(route["dir"], export_config)

        app.add_page(
            export_page(),
            route=route["path"],
            title=f"{route['name']} - Buridan UI",
            image="https://raw.githubusercontent.com/buridan-ui/ui/refs/heads/main/assets/new_logo.PNG",
            meta=meta_tags,
        )


# ... set the DEV var to True for faster hot reload
# ... ... change the ENV to match the page in progress
DEV: bool = False

if DEV:
    # ... ex: working with X item Y -> set the ENV data as such:
    ENV = {
        "path": "/charts/bar-charts",
        "name": "DEV MODE",
        "dir": "bar",
        "config": pantry_exports_config,
    }

    @base(ENV["path"], ENV["name"])
    def __() -> callable:
        return [export() for export in ENV["config"][ENV["dir"]]]

    # app.add_page(__(), "/")
    # app.add_page(landing_page(), route="/", title="Buridan UI")

else:
    app.add_page(
        landing_page(),
        route="/",
        title="Buridan UI",
        image="https://raw.githubusercontent.com/buridan-ui/ui/refs/heads/main/assets/new_logo.PNG",
        meta=meta_tags,
    )
    app.add_page(
        charts_landing_page(),
        route="/charts/ui",
        title="Charts UI",
        image="https://raw.githubusercontent.com/buridan-ui/ui/refs/heads/main/assets/new_logo.PNG",
        meta=meta_tags,
    )
    app.add_page(
        analytics_landing_page(),
        route="/analytics/ui",
        title="Analytics UI",
        image="https://raw.githubusercontent.com/buridan-ui/ui/refs/heads/main/assets/new_logo.PNG",
        meta=meta_tags,
    )
    app.add_page(
        bar_chart_page(),
        "/charts/bar-charts",
        "Bar Charts - Buridan UI",
        image="https://raw.githubusercontent.com/buridan-ui/ui/refs/heads/main/assets/new_logo.PNG",
        meta=meta_tags,
    )
    app.add_page(
        area_chart_page(),
        "/charts/area-charts",
        "Area Charts - Buridan UI",
        image="https://raw.githubusercontent.com/buridan-ui/ui/refs/heads/main/assets/new_logo.PNG",
        meta=meta_tags,
    )
    app.add_page(
        line_chart_page(),
        "/charts/line-charts",
        "Line Charts - Buridan UI",
        image="https://raw.githubusercontent.com/buridan-ui/ui/refs/heads/main/assets/new_logo.PNG",
        meta=meta_tags,
    )
    app.add_page(
        pie_chart_page(),
        "/charts/pie-charts",
        "Pie Charts - Buridan UI",
        image="https://raw.githubusercontent.com/buridan-ui/ui/refs/heads/main/assets/new_logo.PNG",
        meta=meta_tags,
    )
    app.add_page(
        radar_chart_page(),
        "/charts/radar-charts",
        "Radar Charts - Buridan UI",
        image="https://raw.githubusercontent.com/buridan-ui/ui/refs/heads/main/assets/new_logo.PNG",
        meta=meta_tags,
    )

    # add_routes(Routes.charts, charts_exports_config)
    add_routes(Routes.pantries, pantry_exports_config)
    add_routes(Routes.started, getting_started_config)
    add_routes(Routes.analytics, analytics_config_file)
