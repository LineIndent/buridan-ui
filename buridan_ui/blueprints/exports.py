from .anon.main import sandboxAuth

from ..wrappers.component.wrapper import blueprint_wrapper

from random import randint
import os


def get_source(directory: str, filename: str):
    with open(
        os.path.join("buridan_ui", "blueprints", directory, filename), "r"
    ) as file:
        return file.read()


def create_export(func, directory, filenamePreview, filenameStyle, filenameState):

    preview = get_source(directory, filenamePreview)
    style_code = get_source(directory, filenameStyle)
    state_code = get_source(directory, filenameState)

    @blueprint_wrapper()
    def export():
        return [func(), preview, style_code, state_code, randint(0, 100000)]

    return export


blueprint_export_config = {
    "anon": [
        create_export(
            sandboxAuth,
            "anon",
            "main.py",
            "style.py",
            "state.py",
        ),
    ],
}
