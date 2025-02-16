import inspect

from buridan_ui.wrappers.component.wrapper import component_wrapper, chart_wrapper

from .area.v1 import areachart_v1
from .area.v2 import areachart_v2
from .area.v3 import areachart_v3
from .area.v4 import areachart_v4
from .area.v5 import areachart_v5
from .area.v6 import areachart_v6
from .area.v7 import areachart_v7
from .area.v8 import areachart_v8
from .bar.v1 import barchart_v1
from .bar.v10 import barchart_v10
from .bar.v2 import barchart_v2
from .bar.v3 import barchart_v3
from .bar.v4 import barchart_v4
from .bar.v5 import barchart_v5
from .bar.v6 import barchart_v6
from .bar.v7 import barchart_v7
from .bar.v8 import barchart_v8
from .bar.v9 import barchart_v9
from .line.v1 import linechart_v1
from .line.v2 import linechart_v2
from .line.v3 import linechart_v3
from .line.v4 import linechart_v4
from .line.v5 import linechart_v5
from .line.v6 import linechart_v6
from .line.v7 import linechart_v7
from .line.v8 import linechart_v8
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
from ..pages.landing.hero_grid_layout import responsive_grid
from ..wrappers.base.main import base

BASE_PATH: str = "https://github.com/LineIndent/buridan-ui/blob/main/buridan_ui/charts/"


def get_source(func) -> str:
    source: str = ""
    with open("buridan_ui/charts/style.py") as file:
        source += file.read()
        source += "\n"
        source += inspect.getsource(func)

    return source


def create_export(func, directory, version, has_theme=True):

    icon_map = {
        "line": "chart-line",
        "bar": "chart-bar",
        "area": "chart-area",
        "pie": "chart-pie",
        "radar": "radar",
    }

    @chart_wrapper(f"{BASE_PATH}{directory}/v{version}.py")
    def export():
        return [func(), get_source(func), icon_map.get(directory, "chart-line")]

    return export


charts_exports_config = {
    "bar": [
        create_export(barchart_v1, "bar", 1),
        create_export(barchart_v2, "bar", 2),
        create_export(barchart_v3, "bar", 3),
        create_export(barchart_v4, "bar", 4),
        create_export(barchart_v6, "bar", 6),
        create_export(barchart_v7, "bar", 7),
        create_export(barchart_v5, "bar", 5),
    ],
    "area": [
        create_export(areachart_v1, "area", 1),
        create_export(areachart_v2, "area", 2),
        create_export(areachart_v3, "area", 3),
        create_export(areachart_v4, "area", 4),
        create_export(areachart_v5, "area", 5),
        create_export(areachart_v6, "area", 6),
        create_export(areachart_v7, "area", 7),
    ],
    "line": [
        create_export(linechart_v1, "line", 1),
        create_export(linechart_v2, "line", 2),
        create_export(linechart_v3, "line", 3),
        create_export(linechart_v4, "line", 4),
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


def get_exports(directory: str, config_file: dict[str, list[callable]]):
    return [export() for export in config_file[directory]]


@base("/charts/area-charts", "Area Charts")
def area_chart_page():
    import reflex as rx

    return [
        responsive_grid(
            rx.box(
                create_export(areachart_v1, "area", 1)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(areachart_v2, "area", 2)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(areachart_v3, "area", 3)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(areachart_v4, "area", 4)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(areachart_v8, "area", 8)(),
                class_name="lg:col-span-2",
            ),
            rx.box(
                create_export(areachart_v6, "area", 6)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(areachart_v7, "area", 7)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(areachart_v5, "area", 5)(),
                class_name="lg:col-span-2",
            ),
            lg=2,
            md=2,
            gap=8,
        ),
    ]


@base("/charts/bar-charts", "Bar Charts")
def bar_chart_page():
    import reflex as rx

    return [
        responsive_grid(
            rx.box(
                create_export(barchart_v1, "bar", 1)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(barchart_v2, "bar", 2)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(barchart_v8, "bar", 1)(),
                class_name="lg:col-span-2",
            ),
            rx.box(
                create_export(barchart_v3, "bar", 3)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(barchart_v4, "bar", 4)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(barchart_v5, "bar", 5)(),
                class_name="lg:col-span-2 md:col-span-2",
            ),
            rx.box(
                create_export(barchart_v6, "bar", 6)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(barchart_v7, "bar", 7)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(barchart_v9, "bar", 7)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(barchart_v10, "bar", 7)(),
                class_name="lg:col-span-1",
            ),
            lg=2,
            md=2,
            gap=8,
        ),
    ]


@base("/charts/line-charts", "Line Charts")
def line_chart_page():
    import reflex as rx

    return [
        responsive_grid(
            rx.box(
                create_export(linechart_v1, "line", 1)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(linechart_v2, "line", 2)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(linechart_v8, "line", 8)(),
                class_name="lg:col-span-2",
            ),
            rx.box(
                create_export(linechart_v3, "line", 3)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(linechart_v4, "line", 4)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(linechart_v7, "line", 7)(),
                class_name="lg:col-span-2",
            ),
            rx.box(
                create_export(linechart_v5, "line", 5)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(linechart_v6, "line", 6)(),
                class_name="lg:col-span-1",
            ),
            lg=2,
            md=2,
            gap=8,
        ),
    ]


@base("/charts/pie-charts", "Pie Charts")
def pie_chart_page():
    import reflex as rx

    return [
        responsive_grid(
            rx.box(
                create_export(piechart_v1, "pie", 1)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(piechart_v2, "pie", 2)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(piechart_v3, "pie", 3)(),
                class_name="lg:col-span-2",
            ),
            rx.box(
                create_export(piechart_v4, "pie", 4)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(piechart_v5, "pie", 5)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(piechart_v6, "line", 6)(),
                class_name="lg:col-span-2",
            ),
            lg=2,
            md=2,
            gap=8,
        ),
    ]


@base("/charts/radar-charts", "Radar Charts")
def radar_chart_page():
    import reflex as rx

    return [
        responsive_grid(
            rx.box(
                create_export(radar_v1, "radar", 1)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(radar_v2, "radar", 2)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(radar_v3, "radar", 3)(),
                class_name="lg:col-span-2",
            ),
            rx.box(
                create_export(radar_v4, "radar", 4)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(radar_v5, "radar", 5)(),
                class_name="lg:col-span-1",
            ),
            rx.box(
                create_export(radar_v6, "radar", 6)(),
                class_name="lg:col-span-2",
            ),
            lg=2,
            md=2,
            gap=8,
        ),
    ]
