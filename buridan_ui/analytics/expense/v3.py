import reflex as rx
from typing import List, Dict, Any

# Type hints for better code clarity
DataPoint = Dict[str, Any]
ChartData = List[DataPoint]

# Sample data
data = [
    {"day": "2024-11-01", "spent": 50, "limit": 100},
    {"day": "2024-11-02", "spent": 60, "limit": 100},
    {"day": "2024-11-03", "spent": 45, "limit": 100},
    {"day": "2024-11-04", "spent": 75, "limit": 100},
    {"day": "2024-11-05", "spent": 85, "limit": 100},
    {"day": "2024-11-06", "spent": 40, "limit": 100},
    {"day": "2024-11-07", "spent": 95, "limit": 100},
    {"day": "2024-11-08", "spent": 110, "limit": 100},
    {"day": "2024-11-09", "spent": 65, "limit": 100},
    {"day": "2024-11-10", "spent": 80, "limit": 100},
    {"day": "2024-11-11", "spent": 55, "limit": 100},
    {"day": "2024-11-12", "spent": 120, "limit": 100},
    {"day": "2024-11-13", "spent": 70, "limit": 100},
    {"day": "2024-11-14", "spent": 90, "limit": 100},
    {"day": "2024-11-15", "spent": 60, "limit": 100},
    {"day": "2024-11-16", "spent": 50, "limit": 100},
    {"day": "2024-11-17", "spent": 85, "limit": 100},
    {"day": "2024-11-18", "spent": 55, "limit": 100},
    {"day": "2024-11-19", "spent": 70, "limit": 100},
    {"day": "2024-11-20", "spent": 95, "limit": 100},
    {"day": "2024-11-21", "spent": 120, "limit": 100},
    {"day": "2024-11-22", "spent": 40, "limit": 100},
    {"day": "2024-11-23", "spent": 75, "limit": 100},
    {"day": "2024-11-24", "spent": 100, "limit": 100},
    {"day": "2024-11-25", "spent": 90, "limit": 100},
    {"day": "2024-11-26", "spent": 80, "limit": 100},
    {"day": "2024-11-27", "spent": 60, "limit": 100},
    {"day": "2024-11-28", "spent": 115, "limit": 100},
    {"day": "2024-11-29", "spent": 50, "limit": 100},
    {"day": "2024-11-30", "spent": 105, "limit": 100},
]


def sum_data_key(data: List[dict[str, str | int]], key: str) -> int:
    return sum(item[key] for item in data)


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
        hide=True,
    )


def create_chart_layer(
    data: ChartData, data_key: str, fill_color: str, max_limit: int
) -> rx.Component:
    """Create a single chart layer with consistent styling."""
    return rx.box(
        rx.recharts.bar_chart(
            rx.recharts.bar(
                data_key=data_key,
                fill=rx.color(fill_color),
                radius=10,
            ),
            get_x_axis_config(max_limit),
            get_y_axis_config(),
            data=data,
            layout="vertical",
            class_name="w-full h-full",
            bar_size=10,
        ),
        class_name="absolute top-0 left-0 w-full h-full",
    )


def info(title: str, size: str, subtitle: str, align: str) -> rx.Component:
    return rx.vstack(
        rx.heading(title, size=size, weight="bold"),
        rx.text(subtitle, size="1", color=rx.color("slate", 11), weight="medium"),
        spacing="1",
        align=align,
    )


def expense_v3():
    # Calculate data sums: limit, spent
    sum_spent = sum_data_key(data, "spent")
    sum_limit = sum_data_key(data, "limit")

    # Modify the data
    modified_data = [{"datetime": "November", "spent": sum_spent, "limit": sum_limit}]

    # Define chart layers
    chart_layers = [
        # Limit layer
        create_chart_layer(modified_data, "limit", "gray", sum_limit),
        # Spent layer
        create_chart_layer(modified_data, "spent", "blue", sum_limit),
    ]

    return rx.vstack(
        rx.vstack(
            info("Spending Limit", "5", "Showing Data for November 2024", "start"),
            rx.button(
                "View Report", color_scheme="gray", variant="surface", cursor="pointer"
            ),
            align="start",
            width="100%",
        ),
        rx.container(*chart_layers, class_name="relative w-full"),
        rx.hstack(
            rx.text(f"$ {sum_spent}/{sum_limit}", size="2", color=rx.color("gray", 10)),
            width="100%",
            justify="end",
        ),
        width="100%",
        padding="0.5em",
        height="210px",
    )
