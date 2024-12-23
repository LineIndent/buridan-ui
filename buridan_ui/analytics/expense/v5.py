import reflex as rx
from typing import List, Dict, Any

# Type hints for better code clarity
DataPoint = Dict[str, Any]
ChartData = List[DataPoint]

# Sample data
data = [
    {"day": "Mon", "last_week": 20, "present": 25},
    {"day": "Tue", "last_week": 15, "present": 45},
    {"day": "Wed", "last_week": 35, "present": 73},
    {"day": "Thu", "last_week": 80, "present": 10},
    {"day": "Fri", "last_week": 100, "present": 45},
    {"day": "Sat", "last_week": 65, "present": 100},
    {"day": "Sun", "last_week": 25, "present": 45},
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
        custom_attrs={"fontSize": "12px"},
    )


def get_y_axis_config(max_value: int) -> rx.Component:
    """Shared Y-axis configuration."""
    return rx.recharts.y_axis(
        domain=[0, max_value],
        hide=True,
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
                radius=6,
            ),
            get_x_axis_config(),
            get_y_axis_config(max_value),
            data=data,
            class_name="w-full h-full",
            bar_size=30,
            bar_category_gap=20,
        ),
        class_name="absolute top-0 left-0 w-full h-full",
    )


def expense_v5():
    # Calculate max value
    max_value = calculate_max_value(data, ["present", "last_week"])

    # Create background data
    data_with_bg = create_background_data(data, max_value)

    # Define chart layers
    chart_layers = [
        # Background layer
        create_chart_layer(data_with_bg, "bg", "gray", 3, max_value),
        # Present data layer
        create_chart_layer(data, "present", "ruby", 7, max_value),
        # Last week data layer
        create_chart_layer(data, "last_week", "ruby", 10, max_value),
    ]

    return rx.vstack(
        info(
            "Transactions - Expenses",
            "5",
            "Tracking Weekly Transaction Changes for Expenses.",
            "start",
        ),
        rx.divider(height="0.25em", opacity="0"),
        rx.container(
            *chart_layers,
            class_name="relative w-full h-[250px]",
            align_items="start",
            display="flex"
        ),
        rx.divider(height="0.25em", opacity="0"),
        rx.hstack(
            rx.badge("Current", variant="solid", size="1", color_scheme="ruby"),
            rx.badge("Last Week", variant="soft", color_scheme="ruby"),
            width="100%",
            justify="center",
        ),
        width="100%",
        padding="0.5em",
        position="relative",
    )
