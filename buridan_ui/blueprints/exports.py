import os

from buridan_ui.wrappers.blueprints.main import blueprint_app_wrapper

from .anon.main import sandboxAuth
from .dashboards.dashboard_app.main import dashboardApp
from .layouts.main import layoutDoubleColumn, layoutSingleColumn

BASE_PATH: str = (
    "https://github.com/LineIndent/buridan-ui/blob/main/buridan_ui/blueprints/"
)


def get_source(directory: str, filename: str):
    with open(
        os.path.join("buridan_ui", "blueprints", directory, filename),
    ) as file:
        return file.read()


def create_export(func, directory):

    @blueprint_app_wrapper(f"{BASE_PATH}{directory}")
    def export():
        return [func()]

    return export


blueprint_export_config = {
    "anon": [create_export(sandboxAuth, "anon")],
    "dashboards": [create_export(dashboardApp, "dashboards")],
    "layouts": [
        create_export(layoutSingleColumn, "layouts"),
        create_export(layoutDoubleColumn, "layouts"),
    ],
}
