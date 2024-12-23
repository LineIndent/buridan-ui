import reflex as rx
from typing import List, Dict, Any

# Type hints for better code clarity
DataPoint = Dict[str, Any]
ChartData = List[DataPoint]

# Sample data
data = [
    {"day": "Mon", "last_week": 120, "present": 160},
    {"day": "Tue", "last_week": 110, "present": 135},
    {"day": "Wed", "last_week": 150, "present": 185},
    {"day": "Thu", "last_week": 180, "present": 290},
    {"day": "Fri", "last_week": 200, "present": 240},
    {"day": "Sat", "last_week": 145, "present": 175},
    {"day": "Sun", "last_week": 185, "present": 200},
]


def calculate_max_value(data: ChartData, keys: List[str]) -> int:
    """Calculate the maximum value across multiple keys in the dataset."""
    max_value = max(max(item[key] for item in data) for key in keys)
    return int(max_value * 1.1)  # Add 10% padding


def create_background_data(data: ChartData, max_value: int) -> ChartData:
    """Create background data with constant max value."""
    return [{**item, "bg": max_value} for item in data]


def get_x_axis_config(max_value: int) -> rx.Component:
    """Shared X-axis configuration."""
    return rx.recharts.x_axis(domain=[0, max_value], hide=True, type_="number")


def get_y_axis_config() -> rx.Component:
    """Shared Y-axis configuration."""
    return rx.recharts.y_axis(
        data_key="day",
        axis_line=False,
        type_="category",
        tick_size=10,
        tick_line=False,
        custom_attrs={"fontSize": "12px"},
    )


def info(title: str, size: str, subtitle: str, align: str) -> rx.Component:
    return rx.vstack(
        rx.heading(title, size=size, weight="bold"),
        rx.text(subtitle, size="1", color=rx.color("slate", 11), weight="medium"),
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
            get_x_axis_config(max_value),
            get_y_axis_config(),
            data=data,
            layout="vertical",
            class_name="w-full h-full",
        ),
        class_name="absolute top-0 left-0 w-full h-full ml-[-30px]",
    )


def expense_v2():
    # Calculate max value
    max_value = calculate_max_value(data, ["present", "last_week"])

    # Create background data
    data_with_bg = create_background_data(data, max_value)

    # Define chart layers
    chart_layers = [
        # Background layer
        create_chart_layer(data_with_bg, "bg", "gray", 3, max_value),
        # Present data layer
        create_chart_layer(data, "present", "blue", 3, max_value),
        # Last week data layer
        create_chart_layer(data, "last_week", "blue", 7, max_value),
    ]

    return rx.vstack(
        rx.container(
            *chart_layers,
            class_name="relative w-full h-[250px]",
            align_items="start",
            display="flex"
        ),
        rx.divider(height="0.5em", opacity="0"),
        info("Transactions", "5", "Tracking Weekly Transaction Changes.", "start"),
        rx.hstack(
            rx.badge("Current", variant="solid", size="1"),
            rx.badge("Last Week", variant="soft"),
        ),
        width="100%",
        padding="0.5em",
        position="relative",
    )
