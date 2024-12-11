import reflex as rx

from ...wrappers.state import ComponentWrapperState
from ..style import info, tooltip_styles


def barchart_v6():

    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 340},
        {"month": "Mar", "desktop": 237, "active": True},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]

    modified_data = [
        {
            **item,
            "stroke": (
                rx.color(ComponentWrapperState.selected_theme, 11)
                if item.get("active", False)
                else "none"
            ),
        }
        for item in data
    ]

    return rx.center(
        rx.vstack(
            info(
                "Bar Chart - Active",
                "3",
                "Showing total visitors for the last 6 months",
                "start",
            ),
            rx.recharts.bar_chart(
                rx.recharts.cartesian_grid(horizontal=True, vertical=False),
                rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
                rx.recharts.bar(
                    data_key="desktop",
                    fill=ComponentWrapperState.default_theme[0],
                    stack_id="a",
                    radius=6,
                    stroke="stroke",
                    stroke_width=3,
                ),
                rx.recharts.y_axis(type_="number", hide=True),
                rx.recharts.x_axis(
                    data_key="month",
                    type_="category",
                    axis_line=False,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                ),
                data=modified_data,
                width="100%",
                height=250,
                margin={"top": 25},
                bar_size=25,
            ),
            info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
            width="100%",
            margin_right="20px",
        ),
        width="100%",
        padding="0.5em",
    )
