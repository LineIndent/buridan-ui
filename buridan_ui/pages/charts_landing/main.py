import reflex as rx

from buridan_ui.charts.exports import *
from buridan_ui.pages.landing.wrapper.wrapper import landing_page_section_wrapper
from buridan_ui.templates.drawer.drawer import drawer
from buridan_ui.templates.footer.footer import footer
from buridan_ui.templates.navigation.navigation import landing_page_navigation
from buridan_ui.wrappers.shared.scheme import component_wrapper_color_scheme

GridStyleSheet = {
    "width": "100%",
    "display": "grid",
    "column_gap": "1rem",
    "row_gap": "1rem",
    "grid_template_columns": [
        f"repeat({i}, minmax(0, 1fr))" for i in [1, 1, 1, 2, 2, 3]
    ],
}


def chartsWrapper(chart: rx.Component) -> rx.Component:
    return rx.vstack(
        chart,
        width="100%",
        padding="0.75em",
        border_radius="8px",
        border=f"3px solid {rx.color('gray', 3)}",
    )


def chartTheme() -> rx.Component:
    return rx.hstack(
        component_wrapper_color_scheme(),
        bottom="0",
        left="0",
        width="100%",
        position="sticky",
        justify="center",
        padding="1em",
        backdrop_filter="blur(5px)",
    )


def charts_landing_page():
    return rx.vstack(
        drawer(),
        rx.vstack(
            landing_page_navigation(),
            rx.divider(height="1em", opacity="0"),
            landing_page_section_wrapper(
                "Buridan Charts",
                "Powerful Chart Components Built with Reflex and Recharts",
                "High-level Reflex chart components, built on top of Recharts. Easily integrate your own data for beautiful data visualizations.",
                "Check out the Charts docs →",
                "/charts/area-charts",
                [],
            ),
            rx.divider(height="5em", opacity="0"),
            rx.vstack(
                rx.hstack(
                    chartsWrapper(areachart_v1()),
                    chartsWrapper(areachart_v6()),
                    chartsWrapper(areachart_v2()),
                    chartsWrapper(areachart_v4()),
                    chartsWrapper(areachart_v7()),
                    chartsWrapper(areachart_v3()),
                    **GridStyleSheet,
                ),
                rx.divider(height="0.25em", opacity="0"),
                chartsWrapper(rx.hstack(areachart_v5(), width="100%")),
                rx.divider(height="0.25em", opacity="0"),
                rx.hstack(
                    chartsWrapper(barchart_v1()),
                    chartsWrapper(barchart_v2()),
                    chartsWrapper(barchart_v3()),
                    chartsWrapper(barchart_v4()),
                    chartsWrapper(barchart_v6()),
                    chartsWrapper(barchart_v7()),
                    **GridStyleSheet,
                ),
                rx.divider(height="0.25em", opacity="0"),
                chartsWrapper(rx.hstack(barchart_v5(), width="100%")),
                rx.divider(height="0.25em", opacity="0"),
                rx.hstack(
                    chartsWrapper(linechart_v1()),
                    chartsWrapper(linechart_v2()),
                    chartsWrapper(linechart_v3()),
                    chartsWrapper(linechart_v4()),
                    chartsWrapper(linechart_v5()),
                    chartsWrapper(linechart_v6()),
                    **GridStyleSheet,
                ),
                rx.divider(height="0.25em", opacity="0"),
                chartsWrapper(rx.hstack(linechart_v7(), width="100%")),
                rx.divider(height="0.25em", opacity="0"),
                rx.hstack(
                    chartsWrapper(piechart_v1()),
                    chartsWrapper(piechart_v2()),
                    chartsWrapper(piechart_v3()),
                    chartsWrapper(piechart_v4()),
                    chartsWrapper(piechart_v5()),
                    chartsWrapper(piechart_v6()),
                    **GridStyleSheet,
                ),
                rx.hstack(
                    chartsWrapper(radar_v1()),
                    chartsWrapper(radar_v2()),
                    chartsWrapper(radar_v3()),
                    chartsWrapper(radar_v4()),
                    chartsWrapper(radar_v5()),
                    chartsWrapper(radar_v6()),
                    **GridStyleSheet,
                ),
                chartTheme(),
                rx.divider(height="8em", opacity="0"),
                width="100%",
                position="relative",
            ),
            footer(),
            rx.divider(height="2em", opacity="0"),
            width="100%",
            max_width="80em",
            position="relative",
            padding=["0em 1em" if i <= 5 else "0em 0em" for i in range(6)],
        ),
        width="100%",
        align="center",
        min_height="100vh",
        padding_bottom="1em",
        background=rx.color("slate", 2),
    )
