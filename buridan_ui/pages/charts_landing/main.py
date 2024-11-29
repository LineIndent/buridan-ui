import reflex as rx
from typing import Callable

from ..landing.wrapper.wrapper import landing_page_section_wrapper
from ...templates.navigation.navigation import landing_page_navigation
from ...charts.exports import *


GridStyleSheet = {
    "width": "100%",
    "display": "grid",
    "column_gap": "1.5rem",
    "row_gap": "1.5rem",
    "grid_template_columns": [
        f"repeat({i}, minmax(0, 1fr))" for i in [1, 1, 1, 2, 2, 3]
    ],
}


chartsWrapper: Callable[[rx.Component], rx.Component] = lambda chart: rx.vstack(
    chart,
    width="100%",
    padding="0.75em",
    border_radius="8px",
    border=f"1px solid {rx.color('gray', 5)}",
)


def charts_landing_page():
    return rx.vstack(
        rx.vstack(
            landing_page_navigation(),
            rx.divider(height="1em", opacity="0"),
            landing_page_section_wrapper(
                "Buridan Charts",
                "Chart Components",
                "High-level Reflex chart components, built on top of Recharts. Easily integrate your own data for beautiful data visualizations.",
                "Check out charts doc →",
                "/charts/area-charts",
                [],
            ),
            rx.divider(height="5em", opacity="0"),
            rx.hstack(
                chartsWrapper(areachart_v1()),
                chartsWrapper(areachart_v2()),
                chartsWrapper(areachart_v3()),
                chartsWrapper(areachart_v4()),
                chartsWrapper(areachart_v6()),
                chartsWrapper(areachart_v7()),
                **GridStyleSheet,
            ),
            chartsWrapper(rx.hstack(areachart_v5(), width="100%")),
            rx.hstack(
                chartsWrapper(barchart_v1()),
                chartsWrapper(barchart_v2()),
                chartsWrapper(barchart_v3()),
                chartsWrapper(barchart_v4()),
                chartsWrapper(barchart_v6()),
                **GridStyleSheet,
            ),
            width="100%",
            max_width="85em",
            padding=["0em 1em" if i <= 5 else "0em 0em" for i in range(6)],
        ),
        width="100%",
        align="center",
        min_height="100vh",
        padding_bottom="1em",
    )
