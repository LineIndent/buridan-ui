import reflex as rx
from typing import List, Dict, Any

# Type hints for better code clarity
DataPoint = Dict[str, Any]
ChartData = List[DataPoint]

# Sample data
data = [
    {"time": "00:00", "exercise": 1},
    {"time": "00:30", "exercise": 1},
    {"time": "01:00", "exercise": 1},
    {"time": "01:30", "exercise": 1},
    {"time": "02:00", "exercise": 1},
    {"time": "02:30", "exercise": 1},
    {"time": "03:00", "exercise": 1},
    {"time": "03:30", "exercise": 1},
    {"time": "04:00", "exercise": 1},
    {"time": "04:30", "exercise": 1},
    {"time": "05:00", "exercise": 1},
    {"time": "05:30", "exercise": 1},
    {"time": "06:00", "exercise": 20},
    {"time": "06:30", "exercise": 1},
    {"time": "07:00", "exercise": 1},
    {"time": "07:30", "exercise": 1},
    {"time": "08:00", "exercise": 1},
    {"time": "08:30", "exercise": 1},
    {"time": "09:00", "exercise": 1},
    {"time": "09:30", "exercise": 1},
    {"time": "10:00", "exercise": 1},
    {"time": "10:30", "exercise": 1},
    {"time": "11:00", "exercise": 20},
    {"time": "11:30", "exercise": 5},
    {"time": "12:00", "exercise": 20},
    {"time": "12:30", "exercise": 1},
    {"time": "13:00", "exercise": 1},
    {"time": "13:30", "exercise": 1},
    {"time": "14:00", "exercise": 1},
    {"time": "14:30", "exercise": 1},
    {"time": "15:00", "exercise": 1},
    {"time": "15:30", "exercise": 1},
    {"time": "16:00", "exercise": 1},
    {"time": "16:30", "exercise": 1},
    {"time": "17:00", "exercise": 1},
    {"time": "17:30", "exercise": 1},
    {"time": "18:00", "exercise": 1},
    {"time": "18:30", "exercise": 1},
    {"time": "19:00", "exercise": 1},
    {"time": "19:30", "exercise": 1},
    {"time": "20:00", "exercise": 1},
    {"time": "20:30", "exercise": 1},
    {"time": "21:00", "exercise": 1},
    {"time": "21:30", "exercise": 1},
    {"time": "22:00", "exercise": 1},
    {"time": "22:30", "exercise": 1},
    {"time": "23:00", "exercise": 1},
    {"time": "23:30", "exercise": 1},
]


def get_data_average(data: ChartData):
    all_heart_rates = [hr for day in data for hr in day["respiratory_rate"]]
    return sum(all_heart_rates) / len(all_heart_rates)


def get_x_axis_config(data_key: str = "day") -> rx.Component:
    """Shared X-axis configuration."""
    return rx.recharts.x_axis(
        data_key=data_key,
        type_="category",
        axis_line=False,
        tick_size=10,
        tick_line=False,
        custom_attrs={"fontSize": "12px"},
    )


def info(title: str, size: str, subtitle: str, align: str) -> rx.Component:
    return rx.vstack(
        rx.text(title, size="1", color=rx.color("slate", 11), weight="medium"),
        rx.badge(
            rx.heading(subtitle, size=size, weight="bold"),
            color_scheme="yellow",
            variant="surface",
        ),
        spacing="1",
        align=align,
    )


def create_chart_layer(
    data: ChartData,
    data_key: str,
) -> rx.Component:
    """Create a single chart layer with consistent styling."""

    return rx.recharts.bar_chart(
        rx.recharts.cartesian_grid(
            vertical=False,
            stroke_dasharray="4,4",
            horizontal_points=[0, 50, 100, 150, 200],
            custom_attrs={"opacity": 0.5},
        ),
        rx.recharts.bar(data_key=data_key, radius=5, fill=rx.color("yellow")),
        data=data,
        width="100%",
        height=250,
        bar_size=5,
        bar_gap=0,
        bar_category_gap="0%",
    )


def stats_v8():

    return rx.vstack(
        info("", "5", "5/30 MIN", "start"),
        rx.divider(height="0.5em", opacity="0"),
        rx.box(
            rx.text(
                "10 MIN",
                size="1",
                weight="bold",
                color=rx.color("slate", 11),
                top="0",
                left="0",
                position="absolute",
            ),
            create_chart_layer(data, "exercise"),
            width="100%",
            position="relative",
        ),
        width="100%",
        padding="0.5em",
        position="relative",
    )
