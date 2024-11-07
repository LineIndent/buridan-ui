import os
from random import randint

from .bar.v1 import barchart_v1
from .bar.v2 import barchart_v2
from .bar.v3 import barchart_v3
from .bar.v4 import barchart_v4

from .area.v1 import areachart_v1
from .area.v2 import areachart_v2
from .area.v3 import areachart_v3
from .area.v4 import areachart_v4

from .line.v1 import linechart_v1
from .line.v2 import linechart_v2

from ..wrappers.component.wrapper import component_wrapper

BASE_PATH: str = "https://github.com/LineIndent/buridan-ui/blob/main/buridan_ui/charts/"


def get_source(directory: str, filename: str) -> str:
    with open(os.path.join("buridan_ui", "charts", directory, filename), "r") as file:
        return file.read()


def create_export(func, directory, version):
    @component_wrapper(f"{BASE_PATH}{directory}/v{version}.py", True)
    def export():
        return [func(), get_source(directory, f"v{version}.py"), randint(0, 100000)]

    return export


charts_exports_config = {
    "bar": [
        create_export(barchart_v1, "bar", 1),
        create_export(barchart_v2, "bar", 2),
        create_export(barchart_v3, "bar", 3),
        create_export(barchart_v4, "bar", 4),
    ],
    "area": [
        create_export(areachart_v1, "area", 1),
        create_export(areachart_v2, "area", 2),
        create_export(areachart_v3, "area", 3),
        create_export(areachart_v4, "area", 4),
    ],
    "line": [
        create_export(linechart_v1, "line", 1),
        create_export(linechart_v2, "line", 2),
    ],
}
