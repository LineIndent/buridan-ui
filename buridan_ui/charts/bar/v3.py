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


def barchart_v3():
    return rx.center(
        rx.vstack(
            rx.vstack(
                rx.heading("Bar Chart - Stacked + Legend", size="4", weight="bold"),
                rx.text("January - June 2024", size="1", color=rx.color("slate", 11)),
                spacing="1",
            ),
            rx.divider(height="1rem", opacity="0"),
            rx.recharts.bar_chart(
                rx.recharts.cartesian_grid(horizontal=True, vertical=False),
                rx.recharts.graphing_tooltip(
                    label_style={"fontWeight": "700"},
                    item_style={"padding": "0px"},
                    separator=":",
                ),
                rx.recharts.bar(
                    data_key="desktop",
                    fill=ComponentWrapperState.default_theme[0],
                    stack_id="a",
                ),
                rx.recharts.bar(
                    data_key="mobile",
                    fill=ComponentWrapperState.default_theme[1],
                    stack_id="a",
                ),
                rx.recharts.y_axis(type_="number", hide=True),
                rx.recharts.x_axis(data_key="month", type_="category", axis_line=False),
                rx.recharts.legend(),
                data=data,
                width="100%",
                height=300,
                bar_size=50,
                bar_gap=0,
                bar_category_gap=-10,
            ),
            rx.vstack(
                rx.heading("Trending up by 5.2% this month", size="2", weight="bold"),
                rx.text(
                    "Showing total visitors for the last 6 months",
                    size="1",
                    color=rx.color("slate", 11),
                ),
                spacing="1",
                padding="10px",
            ),
            width="100%",
        ),
        width="100%",
        padding="12px",
    )
