import reflex as rx

from ..style import tooltip_styles, info
from ...wrappers.state import ComponentWrapperState


def areachart_v5():

    data = [
        {"date": "Apr 01", "desktop": 222, "mobile": 150},
        {"date": "Apr 02", "desktop": 97, "mobile": 180},
        {"date": "Apr 03", "desktop": 167, "mobile": 120},
        {"date": "Apr 04", "desktop": 242, "mobile": 260},
        {"date": "Apr 05", "desktop": 373, "mobile": 290},
        {"date": "Apr 06", "desktop": 301, "mobile": 340},
        {"date": "Apr 07", "desktop": 245, "mobile": 180},
        {"date": "Apr 08", "desktop": 409, "mobile": 320},
        {"date": "Apr 09", "desktop": 59, "mobile": 110},
        {"date": "Apr 10", "desktop": 261, "mobile": 190},
        {"date": "Apr 11", "desktop": 327, "mobile": 350},
        {"date": "Apr 12", "desktop": 292, "mobile": 210},
        {"date": "Apr 13", "desktop": 342, "mobile": 380},
        {"date": "Apr 14", "desktop": 137, "mobile": 220},
        {"date": "Apr 15", "desktop": 120, "mobile": 170},
        {"date": "Apr 16", "desktop": 138, "mobile": 190},
        {"date": "Apr 17", "desktop": 446, "mobile": 360},
        {"date": "Apr 18", "desktop": 364, "mobile": 410},
        {"date": "Apr 19", "desktop": 243, "mobile": 180},
        {"date": "Apr 20", "desktop": 89, "mobile": 150},
        {"date": "Apr 21", "desktop": 137, "mobile": 200},
        {"date": "Apr 22", "desktop": 224, "mobile": 170},
        {"date": "Apr 23", "desktop": 138, "mobile": 230},
        {"date": "Apr 24", "desktop": 387, "mobile": 290},
        {"date": "Apr 25", "desktop": 215, "mobile": 250},
        {"date": "Apr 26", "desktop": 75, "mobile": 130},
        {"date": "Apr 27", "desktop": 383, "mobile": 420},
        {"date": "Apr 28", "desktop": 122, "mobile": 180},
        {"date": "Apr 29", "desktop": 315, "mobile": 240},
        {"date": "Apr 30", "desktop": 454, "mobile": 380},
        {"date": "May 01", "desktop": 165, "mobile": 220},
        {"date": "May 02", "desktop": 293, "mobile": 310},
        {"date": "May 03", "desktop": 247, "mobile": 190},
        {"date": "May 04", "desktop": 385, "mobile": 420},
        {"date": "May 05", "desktop": 481, "mobile": 390},
        {"date": "May 06", "desktop": 498, "mobile": 520},
        {"date": "May 07", "desktop": 388, "mobile": 300},
        {"date": "May 08", "desktop": 149, "mobile": 210},
        {"date": "May 09", "desktop": 227, "mobile": 180},
        {"date": "May 10", "desktop": 293, "mobile": 330},
        {"date": "May 11", "desktop": 335, "mobile": 270},
        {"date": "May 12", "desktop": 197, "mobile": 240},
        {"date": "May 13", "desktop": 197, "mobile": 160},
        {"date": "May 14", "desktop": 448, "mobile": 490},
        {"date": "May 15", "desktop": 473, "mobile": 380},
        {"date": "May 16", "desktop": 338, "mobile": 400},
        {"date": "May 17", "desktop": 499, "mobile": 420},
        {"date": "May 18", "desktop": 315, "mobile": 350},
        {"date": "May 19", "desktop": 235, "mobile": 180},
        {"date": "May 20", "desktop": 177, "mobile": 230},
        {"date": "May 21", "desktop": 82, "mobile": 140},
        {"date": "May 22", "desktop": 81, "mobile": 120},
        {"date": "May 23", "desktop": 252, "mobile": 290},
        {"date": "May 24", "desktop": 294, "mobile": 220},
        {"date": "May 25", "desktop": 201, "mobile": 250},
        {"date": "May 26", "desktop": 213, "mobile": 170},
        {"date": "May 27", "desktop": 420, "mobile": 460},
        {"date": "May 28", "desktop": 233, "mobile": 190},
        {"date": "May 29", "desktop": 78, "mobile": 130},
        {"date": "May 30", "desktop": 340, "mobile": 280},
        {"date": "May 31", "desktop": 178, "mobile": 230},
        {"date": "Jun 01", "desktop": 178, "mobile": 200},
        {"date": "Jun 02", "desktop": 470, "mobile": 410},
        {"date": "Jun 03", "desktop": 103, "mobile": 160},
        {"date": "Jun 04", "desktop": 439, "mobile": 380},
        {"date": "Jun 05", "desktop": 88, "mobile": 140},
        {"date": "Jun 06", "desktop": 294, "mobile": 250},
        {"date": "Jun 07", "desktop": 323, "mobile": 370},
        {"date": "Jun 08", "desktop": 385, "mobile": 320},
        {"date": "Jun 09", "desktop": 438, "mobile": 480},
        {"date": "Jun 10", "desktop": 155, "mobile": 200},
        {"date": "Jun 11", "desktop": 92, "mobile": 150},
        {"date": "Jun 12", "desktop": 492, "mobile": 420},
        {"date": "Jun 13", "desktop": 81, "mobile": 130},
        {"date": "Jun 14", "desktop": 426, "mobile": 380},
        {"date": "Jun 15", "desktop": 307, "mobile": 350},
        {"date": "Jun 16", "desktop": 371, "mobile": 310},
        {"date": "Jun 17", "desktop": 475, "mobile": 520},
        {"date": "Jun 18", "desktop": 107, "mobile": 170},
        {"date": "Jun 19", "desktop": 341, "mobile": 290},
        {"date": "Jun 20", "desktop": 408, "mobile": 450},
        {"date": "Jun 21", "desktop": 169, "mobile": 210},
        {"date": "Jun 22", "desktop": 317, "mobile": 270},
        {"date": "Jun 23", "desktop": 480, "mobile": 530},
        {"date": "Jun 24", "desktop": 132, "mobile": 180},
        {"date": "Jun 25", "desktop": 141, "mobile": 190},
        {"date": "Jun 26", "desktop": 434, "mobile": 380},
        {"date": "Jun 27", "desktop": 448, "mobile": 490},
        {"date": "Jun 28", "desktop": 149, "mobile": 200},
        {"date": "Jun 29", "desktop": 103, "mobile": 160},
        {"date": "Jun 30", "desktop": 446, "mobile": 400},
    ]

    class AreaChart(rx.State):
        dataMap: dict[str, list[dict[str, str]]] = {
            "Last 3 months": data,
            "Last 30 days": data[-30:],
            "Last 7 days": data[-7:],
        }

        current_selection: list[dict[str, str]] = data

        @rx.event
        def change_data_time(self, value: str):
            self.current_selection = self.dataMap[value]

    return rx.center(
        rx.vstack(
            rx.hstack(
                info(
                    "Area Chart - Dynamic",
                    "3",
                    "Showing total visitors for the last 6 months",
                    "start",
                ),
                rx.select(
                    ["Last 3 months", "Last 30 days", "Last 7 days"],
                    default_value="Last 3 months",
                    on_change=AreaChart.change_data_time,
                ),
                align="center",
                justify="between",
                width="100%",
                wrap="wrap",
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
                        stack_id="a",
                        stroke=ComponentWrapperState.default_theme[index + 1],
                    )
                    for index, name in enumerate(["desktop", "mobile"])
                ],
                rx.recharts.x_axis(
                    data_key="date",
                    axis_line=False,
                    min_tick_gap=32,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                ),
                data=AreaChart.current_selection,
                width="100%",
                height=280,
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
