import reflex as rx

from ...wrappers.state import ComponentWrapperState
from ..style import info, tooltip_styles


def linechart_v1():

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
                "Line Chart",
                "3",
                "Showing total visitors for the last 6 months",
                "start",
            ),
            rx.recharts.line_chart(
                rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-25"
                ),
                rx.recharts.line(
                    data_key="desktop",
                    stroke=ComponentWrapperState.default_theme[1],
                    type_="natural",
                    dot=False,
                ),
                rx.recharts.x_axis(
                    data_key="month",
                    axis_line=False,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                    interval="preserveStartEnd",
                ),
                data=data,
                width="100%",
                height=250,
            ),
            info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
            width="100%",
            class_name=tooltip_styles.general_style,
        ),
        width="100%",
        padding="0.5em",
    )


def _line_chart():
    data = [
        {"month": " ", "desktop": 186, "mobile": 80},
        {"month": "Feb", "desktop": 305, "mobile": 200},
        {"month": "Mar", "desktop": 237, "mobile": 120},
        {"month": "Apr", "desktop": 73, "mobile": 190},
        {"month": "May", "desktop": 209, "mobile": 130},
        {"month": " ", "desktop": 214, "mobile": 140},
    ]
    return rx.fragment(
        rx.hstack(
            rx.foreach(
                [["Desktop", "red"], ["Mobile", "blue"]],
                lambda key: rx.hstack(
                    rx.box(class_name="w-3 h-3 rounded-sm", bg=rx.color(key[1])),
                    rx.text(
                        key[0],
                        class_name="text-sm font-semibold",
                        color=rx.color("slate", 11),
                    ),
                    align="center",
                    spacing="2",
                ),
            ),
            class_name="py-4 px-4 flex w-full flex justify-center gap-8",
        ),
        rx.recharts.line_chart(
            rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
            rx.recharts.line(
                data_key="desktop",
                stroke=rx.color("red"),
                type_="linear",
                dot=False,
                stroke_width=2,
            ),
            rx.recharts.line(
                data_key="mobile",
                stroke=rx.color("blue"),
                type_="linear",
                dot=False,
                stroke_width=2,
            ),
            rx.recharts.x_axis(
                data_key="month",
                axis_line=False,
                tick_size=10,
                tick_line=False,
                custom_attrs={"fontSize": "12px"},
                interval="preserveStartEnd",
            ),
            data=data,
            width="100%",
            height=350,
        ),
    )
