from buridan_ui.analytics.exports import *
from buridan_ui.templates.drawer.drawer import drawer
from buridan_ui.templates.footer.footer import footer
from buridan_ui.templates.navigation.navigation import landing_page_navigation
from buridan_ui.pages.landing.wrapper.wrapper import landing_page_section_wrapper


SharedGridStyle = {
    "width": "100%",
    "display": "grid",
    "column_gap": "1rem",
    "row_gap": "1rem",
}

InfographicGrid = {
    **SharedGridStyle,
    "grid_template_columns": [
        f"repeat({i}, minmax(0, 1fr))" for i in [1, 2, 2, 3, 3, 3]
    ],
}

PriceGrid = {
    **SharedGridStyle,
    "grid_template_columns": [
        f"repeat({i}, minmax(0, 1fr))" for i in [1, 1, 2, 2, 4, 4]
    ],
}

ExpenseGrid = {
    **SharedGridStyle,
    "grid_template_columns": [
        f"repeat({i}, minmax(0, 1fr))" for i in [1, 1, 1, 2, 2, 2]
    ],
}


StatsGrid = {
    **SharedGridStyle,
    "grid_template_columns": [
        f"repeat({i}, minmax(0, 1fr))" for i in [1, 1, 1, 3, 3, 3]
    ],
}


def chartsWrapper(chart: rx.Component) -> rx.Component:
    return rx.vstack(
        chart,
        width="100%",
        padding="0.5em",
        border_radius="8px",
        border=f"3px solid {rx.color('gray', 3)}",
    )


def analytics_landing_page():
    return rx.vstack(
        drawer(),
        rx.vstack(
            landing_page_navigation(),
            rx.divider(height="1em", opacity="0"),
            landing_page_section_wrapper(
                "Buridan Analytics",
                "Powerful Analytics Components Built with Reflex",
                "High-level Reflex chart components, built on top of Recharts. Easily integrate your own data for beautiful data visualizations.",
                "Check out the Charts docs →",
                "/analytics/infographics",
                [],
            ),
            rx.divider(height="5em", opacity="0"),
            rx.vstack(
                rx.hstack(
                    chartsWrapper(infographic_v1()),
                    chartsWrapper(infographic_v4()),
                    chartsWrapper(infographic_v2()),
                    chartsWrapper(infographic_v5()),
                    chartsWrapper(infographic_v6()),
                    chartsWrapper(infographic_v3()),
                    **InfographicGrid,
                ),
                chartsWrapper(expense_v3()),
                rx.hstack(
                    chartsWrapper(price_v1()),
                    chartsWrapper(price_v2()),
                    chartsWrapper(price_v3()),
                    chartsWrapper(price_v4()),
                    **PriceGrid,
                ),
                rx.hstack(
                    chartsWrapper(expense_v1()),
                    chartsWrapper(expense_v5()),
                    **ExpenseGrid,
                ),
                rx.hstack(
                    chartsWrapper(stats_v1()),
                    chartsWrapper(stats_v2()),
                    chartsWrapper(stats_v6()),
                    **StatsGrid,
                ),
                chartsWrapper(expense_v4()),
                rx.hstack(
                    chartsWrapper(stats_v3()),
                    chartsWrapper(stats_v4()),
                    chartsWrapper(stats_v5()),
                    **StatsGrid,
                ),
                chartsWrapper(stats_v7()),
                chartsWrapper(stats_v8()),
                rx.divider(height="8em", opacity="0"),
                width="100%",
                position="relative",
            ),
            # footer(),
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
