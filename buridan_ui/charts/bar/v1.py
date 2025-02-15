import reflex as rx

from ...wrappers.state import ComponentWrapperState
from ..style import info, tooltip_styles


def barchart_v1():

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
                "Bar Chart - Multiple",
                "3",
                "Showing total visitors for the last 6 months",
                "start",
            ),
            rx.recharts.bar_chart(
                rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-25"
                ),
                *[
                    rx.recharts.bar(
                        data_key=name,
                        fill=ComponentWrapperState.default_theme[index],
                        radius=6,
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
                bar_size=25,
                bar_category_gap="30%",
            ),
            info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
            width="100%",
            class_name=tooltip_styles.general_style,
        ),
        width="100%",
        padding="0.5em",
    )


def _bar_chart():
    data = [
        {"month": "Jan", "desktop": 186, "mobile": 80, "tablet": 50},
        {"month": "Feb", "desktop": 305, "mobile": 200, "tablet": 120},
        {"month": "Mar", "desktop": 237, "mobile": 120, "tablet": 70},
        {"month": "Apr", "desktop": 73, "mobile": 190, "tablet": 30},
        # {"month": "May", "desktop": 209, "mobile": 130, "tablet": 80},
        # {"month": "Jun", "desktop": 214, "mobile": 140, "tablet": 100},
    ]

    return rx.fragment(
        rx.hstack(
            rx.foreach(
                [["Desktop", "red"], ["Mobile", "sky"], ["Tablet", "orange"]],
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
        rx.recharts.bar_chart(
            rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
            rx.recharts.bar(
                data_key="desktop",
                fill=rx.color("red", 7),
                radius=4,
            ),
            rx.recharts.bar(
                data_key="mobile",
                fill=rx.color("sky", 7),
                radius=4,
            ),
            rx.recharts.bar(
                data_key="tablet",
                fill=rx.color("orange", 7),
                radius=4,
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
            height=350,
            bar_size=18,
            bar_category_gap="30%",
        ),
    )
