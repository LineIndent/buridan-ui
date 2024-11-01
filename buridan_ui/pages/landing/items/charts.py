import reflex as rx

from ....charts.line.v1 import linechart_v1
from ....charts.area.v4 import areachart_v4
from ....charts.bar.v1 import barchart_v1


# ... Create the charts
line = linechart_v1()
area = areachart_v4()
bar = barchart_v1()


# ... Create a new line chart without max_width
def remove_max_width(line_chart) -> rx.center:
    return rx.center(
        rx.vstack(
            *[
                child
                for child in line_chart.children[0].children
                if "max_width" not in child.__dict__
            ],
            width="100%",
            margin_right="10px",
        ),
        width="100%",
        padding="12px",
    )


def landing_page_chart_items() -> rx.tabs:
    return rx.tabs.root(
        rx.tabs.list(
            *[
                rx.tabs.trigger(name, value=str(i + 1), flex="1", cursor="pointer")
                for i, name in enumerate(["Line Chart", "Area Chart", "Bar Chart"])
            ],
        ),
        *[
            rx.tabs.content(
                remove_max_width(fn),
                value=str(i + 1),
                width="100%",
                padding="2em 0em",
            )
            for i, fn in enumerate([line, area, bar])
        ],
        default_value="1",
        width="100%",
    )
