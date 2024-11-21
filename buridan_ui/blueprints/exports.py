from .anon.main import sandboxAuth
from .dashboard.dashboardApp.main import dashboardApp

from ..wrappers.component.wrapper import blueprint_no_code_wrapper

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

    @blueprint_no_code_wrapper(f"{BASE_PATH}{directory}")
    def export():
        return [func()]

    return export


blueprint_export_config = {
    "anon": [create_export(sandboxAuth, "anon")],
    "dashboard": [create_export(dashboardApp, "dashboard")],
}
