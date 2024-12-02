import reflex as rx

from ..style import tooltip_styles, info
from ...wrappers.state import ComponentWrapperState


def linechart_v6():

    data = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    return rx.center(
        rx.vstack(
            info(
                "Line Chart - Minimal",
                "3",
                "Showing total visitors for the last 6 months",
                "start",
            ),
            rx.recharts.line_chart(
                rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
                rx.recharts.cartesian_grid(
                    horizontal=True,
                    vertical=False,
                    fill_opacity=0.35,
                    stroke=rx.color("slate", 5),
                ),
                rx.recharts.line(
                    data_key="visitors",
                    type_="natural",
                    dot=False,
                    stroke=ComponentWrapperState.default_theme[1],
                ),
                data=data,
                width="100%",
                height=250,
                margin={"left": 20, "right": 20, "top": 25},
            ),
            info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
            width="100%",
            margin_right="20px",
        ),
        width="100%",
        padding="0.5em",
    )
