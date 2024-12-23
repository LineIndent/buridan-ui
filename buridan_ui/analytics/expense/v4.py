import random
import reflex as rx
from typing import List, Dict, Any

# Type hints for better code clarity
DataPoint = Dict[str, Any]
ChartData = List[DataPoint]

# Generate income and expense data for 30 days with random variability
income = [
    {"day": f"Day {i+1}", "range": [0, random.randint(20, 230)]} for i in range(30)
]
expense = [
    {"day": f"Day {i+1}", "range": [0, -random.randint(50, 180)]} for i in range(30)
]


def info(title: str, size: str, subtitle: str, align: str) -> rx.Component:
    return rx.vstack(
        rx.heading(title, size=size, weight="bold"),
        rx.text(subtitle, size="1", color=rx.color("slate", 11), weight="medium"),
        spacing="1",
        align=align,
    )


def create_chart_layer(data: ChartData, data_key: str, color: str) -> rx.Component:
    """Create a single chart layer with consistent styling."""
    return rx.box(
        rx.recharts.bar_chart(
            rx.recharts.bar(
                data_key=data_key,
                fill=rx.color(color, 8),
                radius=[6, 6, 0, 0],
            ),
            data=data,
            width="100%",
            height=200,
            bar_size=12,
        ),
    )


def expense_v4():

    # Define chart layers
    chart_layers = [
        create_chart_layer(income, "range", "grass"),
        create_chart_layer(expense, "range", "ruby"),
    ]

    return rx.vstack(
        info("Cash Flow", "5", "Cash flow over a period of 30 days", "start"),
        rx.divider(height="0.5em", opacity="0"),
        rx.box(*chart_layers, width="100%"),
        width="100%",
        padding="0.5em",
        position="relative",
    )
