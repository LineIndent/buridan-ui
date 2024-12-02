import reflex as rx

from ..style import tooltip_styles, info
from ...wrappers.state import ComponentWrapperState

from datetime import datetime


def linechart_v7():
    data = [
        {"date": "2024-04-01", "desktop": 222, "mobile": 150},
        {"date": "2024-04-02", "desktop": 97, "mobile": 180},
        {"date": "2024-04-03", "desktop": 167, "mobile": 120},
        {"date": "2024-04-04", "desktop": 242, "mobile": 260},
        {"date": "2024-04-05", "desktop": 373, "mobile": 290},
        {"date": "2024-04-06", "desktop": 301, "mobile": 340},
        {"date": "2024-04-07", "desktop": 245, "mobile": 180},
        {"date": "2024-04-08", "desktop": 409, "mobile": 320},
        {"date": "2024-04-09", "desktop": 59, "mobile": 110},
        {"date": "2024-04-10", "desktop": 261, "mobile": 190},
        {"date": "2024-04-11", "desktop": 327, "mobile": 350},
        {"date": "2024-04-12", "desktop": 292, "mobile": 210},
        {"date": "2024-04-13", "desktop": 342, "mobile": 380},
        {"date": "2024-04-14", "desktop": 137, "mobile": 220},
        {"date": "2024-04-15", "desktop": 120, "mobile": 170},
        {"date": "2024-04-16", "desktop": 138, "mobile": 190},
        {"date": "2024-04-17", "desktop": 446, "mobile": 360},
        {"date": "2024-04-18", "desktop": 364, "mobile": 410},
        {"date": "2024-04-19", "desktop": 243, "mobile": 180},
        {"date": "2024-04-20", "desktop": 89, "mobile": 150},
        {"date": "2024-04-21", "desktop": 137, "mobile": 200},
        {"date": "2024-04-22", "desktop": 224, "mobile": 170},
        {"date": "2024-04-23", "desktop": 138, "mobile": 230},
        {"date": "2024-04-24", "desktop": 387, "mobile": 290},
        {"date": "2024-04-25", "desktop": 215, "mobile": 250},
        {"date": "2024-04-26", "desktop": 75, "mobile": 130},
        {"date": "2024-04-27", "desktop": 383, "mobile": 420},
        {"date": "2024-04-28", "desktop": 122, "mobile": 180},
        {"date": "2024-04-29", "desktop": 315, "mobile": 240},
        {"date": "2024-04-30", "desktop": 454, "mobile": 380},
        {"date": "2024-05-01", "desktop": 165, "mobile": 220},
        {"date": "2024-05-02", "desktop": 293, "mobile": 310},
        {"date": "2024-05-03", "desktop": 247, "mobile": 190},
        {"date": "2024-05-04", "desktop": 385, "mobile": 420},
        {"date": "2024-05-05", "desktop": 481, "mobile": 390},
        {"date": "2024-05-06", "desktop": 498, "mobile": 520},
        {"date": "2024-05-07", "desktop": 388, "mobile": 300},
        {"date": "2024-05-08", "desktop": 149, "mobile": 210},
        {"date": "2024-05-09", "desktop": 227, "mobile": 180},
        {"date": "2024-05-10", "desktop": 293, "mobile": 330},
        {"date": "2024-05-11", "desktop": 335, "mobile": 270},
        {"date": "2024-05-12", "desktop": 197, "mobile": 240},
        {"date": "2024-05-13", "desktop": 197, "mobile": 160},
        {"date": "2024-05-14", "desktop": 448, "mobile": 490},
        {"date": "2024-05-15", "desktop": 473, "mobile": 380},
        {"date": "2024-05-16", "desktop": 338, "mobile": 400},
        {"date": "2024-05-17", "desktop": 499, "mobile": 420},
        {"date": "2024-05-18", "desktop": 315, "mobile": 350},
        {"date": "2024-05-19", "desktop": 235, "mobile": 180},
        {"date": "2024-05-20", "desktop": 177, "mobile": 230},
        {"date": "2024-05-21", "desktop": 82, "mobile": 140},
        {"date": "2024-05-22", "desktop": 81, "mobile": 120},
        {"date": "2024-05-23", "desktop": 252, "mobile": 290},
        {"date": "2024-05-24", "desktop": 294, "mobile": 220},
        {"date": "2024-05-25", "desktop": 201, "mobile": 250},
        {"date": "2024-05-26", "desktop": 213, "mobile": 170},
        {"date": "2024-05-27", "desktop": 420, "mobile": 460},
        {"date": "2024-05-28", "desktop": 233, "mobile": 190},
        {"date": "2024-05-29", "desktop": 78, "mobile": 130},
        {"date": "2024-05-30", "desktop": 340, "mobile": 280},
        {"date": "2024-05-31", "desktop": 178, "mobile": 230},
        {"date": "2024-06-01", "desktop": 178, "mobile": 200},
        {"date": "2024-06-02", "desktop": 470, "mobile": 410},
        {"date": "2024-06-03", "desktop": 103, "mobile": 160},
        {"date": "2024-06-04", "desktop": 439, "mobile": 380},
        {"date": "2024-06-05", "desktop": 88, "mobile": 140},
        {"date": "2024-06-06", "desktop": 294, "mobile": 250},
        {"date": "2024-06-07", "desktop": 323, "mobile": 370},
        {"date": "2024-06-08", "desktop": 385, "mobile": 320},
        {"date": "2024-06-09", "desktop": 438, "mobile": 480},
        {"date": "2024-06-10", "desktop": 155, "mobile": 200},
        {"date": "2024-06-11", "desktop": 92, "mobile": 150},
        {"date": "2024-06-12", "desktop": 492, "mobile": 420},
        {"date": "2024-06-13", "desktop": 81, "mobile": 130},
        {"date": "2024-06-14", "desktop": 426, "mobile": 380},
        {"date": "2024-06-15", "desktop": 307, "mobile": 350},
        {"date": "2024-06-16", "desktop": 371, "mobile": 310},
    ]

    formatted_data = [
        {
            "date": datetime.strptime(item["date"], "%Y-%m-%d").strftime("%b %d"),
            "desktop": item["desktop"],
            "mobile": item["mobile"],
        }
        for item in data
    ]

    class Chart(rx.State):
        current_data: str = "mobile"
        with_dots: bool = False

        def toggle_with_dots(self, state: bool):
            self.with_dots = not self.with_dots

        def toggle_chart_data(self, name: str):
            self.current_data = name

    return rx.center(
        rx.vstack(
            rx.hstack(
                info(
                    "Line Chart - Dynamic",
                    "3",
                    "Showing total visitors for the last 6 months",
                    "start",
                ),
                rx.hstack(
                    rx.checkbox("Show Dots", on_change=Chart.toggle_with_dots),
                    rx.select(
                        ["mobile", "desktop"],
                        default_value="mobile",
                        on_change=Chart.toggle_chart_data,
                    ),
                    align="center",
                ),
                align="center",
                justify="between",
                width="100%",
                wrap="wrap",
            ),
            rx.recharts.line_chart(
                rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
                rx.recharts.cartesian_grid(
                    horizontal=True,
                    vertical=False,
                    fill_opacity=0.0,
                    stroke=rx.color("slate", 5),
                ),
                rx.recharts.line(
                    data_key=Chart.current_data,
                    stroke=ComponentWrapperState.default_theme[1],
                    type_="natural",
                    dot=Chart.with_dots,
                ),
                rx.recharts.y_axis(type_="number", hide=True),
                rx.recharts.x_axis(
                    data_key="date",
                    type_="category",
                    axis_line=False,
                    min_tick_gap=32,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                ),
                data=formatted_data,
                width="100%",
                height=280,
            ),
            info("Trending up by 5.2% this month", "2", "January - June 2024", "start"),
            width="100%",
            margin_right="20px",
        ),
        width="100%",
        padding="0.5em",
    )
