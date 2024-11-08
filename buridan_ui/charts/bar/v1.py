import reflex as rx
from ...wrappers.component.state import ComponentWrapperState

data = [
    {"month": "Jan", "desktop": 186, "mobile": 80},
    {"month": "Feb", "desktop": 305, "mobile": 200},
    {"month": "Mar", "desktop": 237, "mobile": 120},
    {"month": "Apr", "desktop": 73, "mobile": 190},
    {"month": "May", "desktop": 209, "mobile": 130},
    {"month": "Jun", "desktop": 214, "mobile": 140},
]


def barchart_v1():
    return rx.center(
        rx.vstack(
            rx.vstack(
                rx.heading("Bar Chart - Multiple", size="5", weight="bold"),
                rx.text("January - June 2024", size="1", color=rx.color("slate", 11)),
                spacing="1",
            ),
            rx.divider(height="1rem", opacity="0"),
            rx.recharts.bar_chart(
                rx.recharts.graphing_tooltip(
                    label_style={"fontWeight": "700"}, item_style={"padding": "0px"}
                ),
                rx.recharts.cartesian_grid(horizontal=True, vertical=False),
                *[
                    rx.recharts.bar(
                        data_key=name,
                        fill=ComponentWrapperState.default_theme[index],
                    )
                    for index, name in enumerate(["desktop", "mobile"])
                ],
                rx.recharts.x_axis(data_key="month", axis_line=False),
                data=data,
                width="100%",
                height=250,
                bar_size=25,
                bar_gap=2,
                bar_category_gap="0%",
            ),
            rx.vstack(
                rx.heading("Trending up by 5.2% this month", size="3", weight="bold"),
                rx.text(
                    "Showing total visitors for the last 6 months",
                    size="1",
                    color=rx.color("slate", 11),
                ),
                spacing="1",
            ),
            width="100%",
        ),
        width="100%",
        padding="12px",
    )
