import reflex as rx

from ...wrappers.state import ComponentWrapperState
from ..style import info, tooltip_styles


def areachart_v4():

    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80},
        {"month": "Feb", "desktop": 305, "mobile": 200},
        {"month": "Mar", "desktop": 237, "mobile": 120},
        {"month": "Apr", "desktop": 73, "mobile": 190},
        {"month": "May", "desktop": 209, "mobile": 130},
        {"month": "Jun", "desktop": 214, "mobile": 140},
    ]

    return rx.center(
        rx.vstack(
            info(
                "Area Chart - Stacked",
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
                *[
                    rx.recharts.area(
                        data_key=name,
                        fill=ComponentWrapperState.default_theme[index],
                        stroke="none",
                    )
                    for index, name in enumerate(["desktop", "mobile"])
                ],
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
            ),
            info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
            width="100%",
            class_name=tooltip_styles.general_style,
        ),
        width="100%",
        padding="0.5em",
    )


def _area_chart():
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
        rx.recharts.area_chart(
            rx.el.svg.defs(
                rx.el.svg.linear_gradient(
                    rx.el.svg.stop(
                        stop_color=rx.color("red", 7), offset="0%", stop_opacity=0.3
                    ),
                    rx.el.svg.stop(
                        stop_color=rx.color("red", 7), offset="75%", stop_opacity=0
                    ),
                    x1=0,
                    x2=0,
                    y1=0,
                    y2=1,
                    id=f"red",
                ),
            ),
            rx.el.svg.defs(
                rx.el.svg.linear_gradient(
                    rx.el.svg.stop(
                        stop_color=rx.color("blue", 7), offset="0%", stop_opacity=0.3
                    ),
                    rx.el.svg.stop(
                        stop_color=rx.color("blue", 7), offset="75%", stop_opacity=0
                    ),
                    x1=0,
                    x2=0,
                    y1=0,
                    y2=1,
                    id=f"blue",
                ),
            ),
            rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
            rx.recharts.area(
                data_key="desktop",
                fill="url(#red)",
                stroke=rx.color("red", 8),
                stack_id="1",
            ),
            rx.recharts.area(
                data_key="mobile",
                fill="url(#blue)",
                stroke=rx.color("blue", 8),
                stack_id="1",
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
