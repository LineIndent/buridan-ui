import reflex as rx

from buridan_ui.charts.bar._bar_test import scatter_example
from buridan_ui.charts.area.v4 import _area_chart
from buridan_ui.charts.bar.v1 import barchart_v1, _bar_chart
from buridan_ui.charts.line.v1 import linechart_v1, _line_chart
from buridan_ui.charts.pie.v2 import _pie_chart
from buridan_ui.pages.landing.hero_grid_layout import (
    responsive_grid,
    create_grid_item_chart_section,
)

line = _line_chart()
area = _area_chart()
bar = _bar_chart()
pie = _pie_chart()
bar_2 = scatter_example()


line_info = rx.el.span(
    rx.icon(tag="chart-line", size=18, class_name="inline-block pr-1"),
    rx.el.span("Line Chart - ", class_name="text-sm font-bold"),
    "Visualize data trends over time, adjust line styles, axis scaling, and include data point markers for clarity.",
    class_name="text-sm text-slate-9 font-medium block align-center pt-5 px-2",
)

bar_info = rx.el.span(
    rx.icon(tag="chart-bar", size=18, class_name="inline-block pr-1"),
    rx.el.span("Bar Chart - ", class_name="text-sm font-bold"),
    "Display categorical data with bars. Customize bar width, spacing, radius, and axis labels to highlight comparisons.",
    class_name="text-sm text-slate-9 font-medium block align-center pt-5 px-2",
)

area_info = rx.el.span(
    rx.icon(tag="chart-area", size=18, class_name="inline-block pr-1"),
    rx.el.span("Area Chart - ", class_name="text-sm font-bold"),
    "Show the magnitude of change over time with shaded regions beneath the line, perfect for representing cumulative data.",
    class_name="text-sm text-slate-9 font-medium block align-center pt-5 px-2",
)

pie_info = rx.el.span(
    rx.icon(tag="chart-pie", size=18, class_name="inline-block pr-1"),
    rx.el.span("Pie Chart - ", class_name="text-sm font-bold"),
    "Illustrate proportional data with segments representing parts of a whole. Customize colors and labels for clarity.",
    class_name="text-sm text-slate-9 font-medium block align-center pt-5 px-2",
)

scat_info = rx.el.span(
    rx.icon(tag="chart-scatter", size=18, class_name="inline-block pr-1"),
    rx.el.span("Scatter Chart - ", class_name="text-sm font-bold"),
    "Plot data points on a grid to identify relationships and correlations between two variables. Customize axis scales and point sizes.",
    class_name="text-sm text-slate-9 font-medium block align-center pt-5 px-2",
)


def landing_page_chart_items():
    return responsive_grid(
        create_grid_item_chart_section(
            line,
            line_info,
            1,
            1,
            1,
        ),
        create_grid_item_chart_section(
            bar,
            bar_info,
            1,
            1,
            1,
        ),
        create_grid_item_chart_section(
            area,
            area_info,
            1,
            1,
            1,
        ),
        create_grid_item_chart_section(
            pie,
            pie_info,
            1,
            1,
            1,
        ),
        create_grid_item_chart_section(
            bar_2,
            scat_info,
            1,
            1,
            1,
        ),
        rx.vstack(
            rx.text("37+", class_name="text-7xl text-slate-10 font-bold"),
            rx.text(
                "Charts & Graphs in Stock!",
                class_name="text-xl text-slate-9 font-semibold",
            ),
            width="100%",
            height="100%",
            align="center",
            justify="center",
        ),
        lg=3,
        md=2,
        gap=2,
        padding=0,
    )
