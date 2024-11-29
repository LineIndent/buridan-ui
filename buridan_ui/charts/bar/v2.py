import reflex as rx
from ...wrappers.state import ComponentWrapperState

data = [
    {"month": "Jan", "desktop": 186},
    {"month": "Feb", "desktop": 305},
    {"month": "Mar", "desktop": 237},
    {"month": "Apr", "desktop": 73},
    {"month": "May", "desktop": 209},
    {"month": "Jun", "desktop": 214},
]


def barchart_v2():
    return rx.center(
        rx.vstack(
            rx.vstack(
                rx.heading("Bar Chart - Horizontal", size="4", weight="bold"),
                rx.text("January - June 2024", size="1", color=rx.color("slate", 11)),
                spacing="1",
            ),
            rx.divider(height="1rem", opacity="0"),
            rx.recharts.bar_chart(
                rx.recharts.graphing_tooltip(
                    label_style={"fontWeight": "700"},
                    item_style={"padding": "0px"},
                    separator=":",
                ),
                rx.recharts.bar(
                    data_key="desktop",
                    fill=ComponentWrapperState.default_theme[0],
                    radius=6,
                ),
                rx.recharts.x_axis(type_="number", hide=True, tick_size=0),
                rx.recharts.y_axis(
                    data_key="month", type_="category", axis_line=False, tick_size=0
                ),
                data=data,
                layout="vertical",
                width="100%",
                height=250,
                bar_size=25,
                bar_gap=2,
                bar_category_gap=0,
                margin={"left": -20},
            ),
            rx.vstack(
                rx.heading("Trending up by 5.2% this month", size="2", weight="bold"),
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
