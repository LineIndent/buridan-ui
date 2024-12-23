import reflex as rx
from typing import List, Dict, Any

# Type hints for better code clarity
DataPoint = Dict[str, Any]
ChartData = List[DataPoint]

# Sample data
data = [
    {"day": "Mon", "blood_pressure": [120, 80]},
    {"day": "Tue", "blood_pressure": [125, 82]},
    {"day": "Wed", "blood_pressure": [118, 76]},
    {"day": "Thu", "blood_pressure": [122, 78]},
    {"day": "Fri", "blood_pressure": [130, 85]},
    {"day": "Sat", "blood_pressure": [128, 80]},
    {"day": "Sun", "blood_pressure": [115, 75]},
]


def get_data_average(data: ChartData):
    all_heart_rates = [hr for day in data for hr in day["blood_pressure"]]
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


def get_y_axis_config() -> rx.Component:
    """Shared Y-axis configuration."""
    return rx.recharts.y_axis(
        hide=True,
    )


def info(title: str, size: str, subtitle: str, align: str) -> rx.Component:
    return rx.vstack(
        rx.text(title, size="1", color=rx.color("ruby", 11), weight="medium"),
        rx.heading(subtitle, size=size, weight="bold"),
        spacing="1",
        align=align,
    )


def create_chart_layer(
    data: ChartData,
    data_key: str,
) -> rx.Component:
    """Create a single chart layer with consistent styling."""

    return rx.recharts.bar_chart(
        rx.recharts.bar(data_key=data_key, radius=10, fill=rx.color("ruby")),
        get_x_axis_config(),
        data=data,
        width="100%",
        height=250,
        bar_size=25,
    )


def stats_v4():

    return rx.vstack(
        info("Blood Pressure", "5", "75 - 130 mmHg", "start"),
        rx.divider(height="0.5em", opacity="0"),
        create_chart_layer(data, "blood_pressure"),
        width="100%",
        padding="0.5em",
        position="relative",
    )
