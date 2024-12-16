import inspect
import reflex as rx

from random import randint
from buridan_ui.wrappers.component.wrapper import component_wrapper

from .area.v1 import areachart_v1
from .area.v2 import areachart_v2
from .area.v3 import areachart_v3
from .area.v4 import areachart_v4
from .area.v5 import areachart_v5
from .area.v6 import areachart_v6
from .area.v7 import areachart_v7
from .bar.v1 import barchart_v1
from .bar.v2 import barchart_v2
from .bar.v3 import barchart_v3
from .bar.v4 import barchart_v4
from .bar.v5 import barchart_v5
from .bar.v6 import barchart_v6
from .bar.v7 import barchart_v7
from .line.v1 import linechart_v1
from .line.v2 import linechart_v2
from .line.v3 import linechart_v3
from .line.v4 import linechart_v4
from .line.v5 import linechart_v5
from .line.v6 import linechart_v6
from .line.v7 import linechart_v7
from .pie.v1 import piechart_v1
from .pie.v2 import piechart_v2
from .pie.v3 import piechart_v3
from .pie.v4 import piechart_v4
from .pie.v5 import piechart_v5
from .pie.v6 import piechart_v6
from .radar.v1 import radar_v1
from .radar.v2 import radar_v2
from .radar.v3 import radar_v3
from .radar.v4 import radar_v4
from .radar.v5 import radar_v5
from .radar.v6 import radar_v6

BASE_PATH: str = "https://github.com/LineIndent/buridan-ui/blob/main/buridan_ui/charts/"


def get_source(func) -> str:
    source: str = ""
    with open("buridan_ui/charts/style.py") as file:
        source += file.read()
        source += "\n"
        source += inspect.getsource(func)

    return source


def create_export(
    func, directory, version, has_theme=True, lab: rx.Component = rx.spacer()
):
    @component_wrapper(f"{BASE_PATH}{directory}/v{version}.py", has_theme)
    def export():
        return [func(), get_source(func), randint(0, 100000), lab]

    return export


from ..templates.lab.main import ChartLab

charts_exports_config = {
    "bar": [
        create_export(
            barchart_v1,
            "bar",
            1,
            True,
            ChartLab(chart_type="bar-v1"),
        ),
        create_export(barchart_v2, "bar", 2),
        create_export(
            barchart_v3,
            "bar",
            3,
            True,
            ChartLab(chart_type="bar-v3"),
        ),
        create_export(barchart_v4, "bar", 4),
        create_export(barchart_v5, "bar", 5),
        create_export(barchart_v6, "bar", 6),
        create_export(barchart_v7, "bar", 7),
    ],
    "area": [
        create_export(
            areachart_v1,
            "area",
            1,
            True,
            ChartLab(chart_type="area-v1"),
        ),
        create_export(
            areachart_v2,
            "area",
            2,
            True,
            ChartLab(chart_type="area-v2"),
        ),
        create_export(
            areachart_v3,
            "area",
            3,
            True,
            ChartLab(chart_type="area-v3"),
        ),
        create_export(
            areachart_v4,
            "area",
            4,
            True,
            ChartLab(chart_type="area-v4"),
        ),
        create_export(areachart_v5, "area", 5),
        create_export(
            areachart_v6,
            "area",
            6,
            True,
            ChartLab(chart_type="area-v6"),
        ),
        create_export(
            areachart_v7,
            "area",
            7,
            True,
            ChartLab(chart_type="area-v7"),
        ),
    ],
    "line": [
        create_export(
            linechart_v1,
            "line",
            1,
            True,
            ChartLab(chart_type="line-v1"),
        ),
        create_export(
            linechart_v2,
            "line",
            2,
            True,
            ChartLab(chart_type="line-v2"),
        ),
        create_export(
            linechart_v3,
            "line",
            3,
            True,
            ChartLab(chart_type="line-v3"),
        ),
        create_export(
            linechart_v4,
            "line",
            4,
            True,
            ChartLab(chart_type="line-v4"),
        ),
        create_export(linechart_v5, "line", 5),
        create_export(linechart_v6, "line", 6),
        create_export(linechart_v7, "line", 7),
    ],
    "pie": [
        create_export(piechart_v1, "pie", 1),
        create_export(piechart_v2, "pie", 2),
        create_export(piechart_v3, "pie", 3),
        create_export(piechart_v4, "pie", 4),
        create_export(piechart_v5, "pie", 5),
        create_export(piechart_v6, "pie", 6),
    ],
    "radar": [
        create_export(radar_v1, "radar", 1),
        create_export(radar_v2, "radar", 2),
        create_export(radar_v3, "radar", 3),
        create_export(radar_v4, "radar", 4),
        create_export(radar_v5, "radar", 5),
        create_export(radar_v6, "radar", 6),
    ],
}
