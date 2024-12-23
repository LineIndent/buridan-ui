import reflex as rx
from typing import List, Dict, Any

# Type hints for better code clarity
DataPoint = Dict[str, Any]
ChartData = List[DataPoint]

# Sample data
data = [
    {"day": "M", "likes": 160},
    {"day": "T", "likes": 135},
    {"day": "W", "likes": 185},
    {"day": "T", "likes": 290},
    {"day": "F", "likes": 240},
    {"day": "S", "likes": 175},
    {"day": "S", "likes": 200},
]


def calculate_max_value(data: ChartData, keys: List[str]) -> int:
    """Calculate the maximum value across multiple keys in the dataset."""
    max_value = max(max(item[key] for item in data) for key in keys)
    return int(max_value * 1.1)  # Add 10% padding


def create_background_data(data: ChartData, max_value: int) -> ChartData:
    """Create background data with constant max value."""
    return [{**item, "bg": max_value} for item in data]


def get_x_axis_config(data_key: str = "day") -> rx.Component:
    """Shared X-axis configuration."""
    return rx.recharts.x_axis(
        data_key=data_key,
        type_="category",
        axis_line=False,
        tick_size=10,
        tick_line=False,
        custom_attrs={"fontSize": "12px", "fontWeight": "600"},
    )


def get_y_axis_config(max_value: int) -> rx.Component:
    """Shared Y-axis configuration."""
    return rx.recharts.y_axis(
        domain=[0, max_value],
        hide=True,
    )


def info(title: str, size: str, subtitle: str, align: str) -> rx.Component:
    return rx.vstack(
        rx.text(subtitle, size="1", color=rx.color("blue", 11), weight="medium"),
        rx.heading(title, size=size, weight="bold"),
        spacing="1",
        align=align,
    )


def create_chart_layer(
    data: ChartData,
    data_key: str,
    fill_color: str,
    fill_shade: int,
    max_value: int,
) -> rx.Component:
    """Create a single chart layer with consistent styling."""
    return rx.box(
        rx.recharts.bar_chart(
            rx.recharts.bar(
                data_key=data_key,
                fill=rx.color(fill_color, fill_shade) if fill_shade else fill_color,
                radius=10,
            ),
            get_x_axis_config(),
            get_y_axis_config(max_value),
            data=data,
            class_name="w-full h-full",
            bar_size=10,
        ),
        class_name="absolute top-0 left-0 w-full h-full",
    )


def stats_v1():
    # Calculate max value
    max_value = calculate_max_value(data, ["likes"])

    # Create background data
    data_with_bg = create_background_data(data, max_value)

    # Define chart layers
    chart_layers = [
        # Background layer
        create_chart_layer(data_with_bg, "bg", "gray", 3, max_value),
        # Present data layer
        create_chart_layer(data, "likes", "blue", 7, max_value),
    ]

    return rx.vstack(
        rx.hstack(
            info("33,230", "7", "Likes", "center"), width="100%", justify="center"
        ),
        rx.divider(height="0.5em", opacity="0"),
        rx.container(
            *chart_layers,
            class_name="relative w-full h-[200px]",
            align_items="start",
            display="flex"
        ),
        width="100%",
        padding="0.5em",
        position="relative",
    )
