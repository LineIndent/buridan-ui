from .anon.main import sandboxAuth
from .dashboards.dashboard_app.main import dashboardApp

from ..wrappers.blueprints.main import blueprint_app_wrapper

import os


BASE_PATH: str = (
    "https://github.com/LineIndent/buridan-ui/blob/main/buridan_ui/blueprints/"
)


def get_source(directory: str, filename: str):
    with open(
        os.path.join("buridan_ui", "blueprints", directory, filename), "r"
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
}
