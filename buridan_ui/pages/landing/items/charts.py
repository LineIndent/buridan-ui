import reflex as rx

from ....charts.line.v1 import linechart_v1
from ....charts.area.v4 import areachart_v4
from ....charts.bar.v1 import barchart_v1
from ....charts.pie.v2 import piechart_v2


line = linechart_v1()
area = areachart_v4()
bar = barchart_v1()
pie = piechart_v2()


def landing_page_chart_items() -> rx.tabs:
    return rx.tabs.root(
        rx.tabs.list(
            *[
                rx.tabs.trigger(name, value=str(i + 1), flex="1", cursor="pointer")
                for i, name in enumerate(
                    ["Line Chart", "Area Chart", "Bar Chart", "Pie Chart"]
                )
            ],
        ),
        *[
            rx.tabs.content(
                fn,
                value=str(i + 1),
                width="100%",
                padding="2em 0em",
            )
            for i, fn in enumerate([line, area, bar, pie])
        ],
        default_value="1",
        width="100%",
    )
