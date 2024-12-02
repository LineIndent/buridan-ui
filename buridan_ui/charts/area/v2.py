import reflex as rx

from ..style import tooltip_styles, info
from ...wrappers.state import ComponentWrapperState


def areachart_v2():

    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 305},
        {"month": "Mar", "desktop": 237},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]

    return rx.center(
        rx.vstack(
            info(
                "Area Chart - Linear",
                "3",
                "Showing total visitors for the last 6 months",
                "start",
            ),
            rx.recharts.area_chart(
                rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
                rx.recharts.cartesian_grid(
                    horizontal=True,
                    vertical=False,
                    fill_opacity=0.5,
                    stroke=rx.color("slate", 5),
                ),
                rx.recharts.area(
                    data_key="desktop",
                    fill=ComponentWrapperState.default_theme[1],
                    stroke=ComponentWrapperState.default_theme[2],
                    type_="linear",
                ),
                rx.recharts.x_axis(
                    data_key="month",
                    axis_line=False,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                ),
                data=data,
                width="100%",
                height=250,
                margin={"left": 20},
            ),
            info(
                "Trending up by 5.2% this month",
                "2",
                "January - June 2024",
                "start",
            ),
            width="100%",
            margin_right="20px",
        ),
        width="100%",
        padding="0.5em",
    )
