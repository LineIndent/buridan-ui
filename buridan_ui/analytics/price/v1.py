from reflex.components.radix.themes.components.badge import Badge
from reflex.components.radix.themes.layout.stack import VStack
from reflex.components.radix.themes.typography.text import Text
from reflex.components.recharts.recharts import RechartsCharts
from typing import Callable

import reflex as rx

data = [
    {"price": 16191.57},
    {"price": 21224.33},
    {"price": 32143.82},
    {"price": 30701.94},
    {"price": 26835.53},
    {"price": 25929.99},
    {"price": 36663.37},
    {"price": 48775.2},
    {"price": 17747.53},
    {"price": 15953.76},
    {"price": 18708.3},
    {"price": 13846.6},
    {"price": 15435.7},
]


token: Callable[[str, str], VStack] = lambda token, symbol: rx.vstack(
    rx.heading(token, size="4", color=rx.color("slate", 12)),
    rx.text(symbol, size="1", color=rx.color("slate", 10)),
    spacing="1",
)

chart: Callable[[list[dict[str, int]], str], RechartsCharts] = (
    lambda data, key: rx.recharts.line_chart(
        rx.recharts.line(data_key=key, dot=False),
        data=data,
        width="35%",
    )
)


price: Callable[[str], Text] = lambda price: rx.text(price, size="2", weight="bold")

badge: Callable[[str], Badge] = lambda percent: rx.badge(
    percent, variant="soft", color_scheme="green", size="1"
)


def price_v1():
    return rx.hstack(
        token("Bitcoin", "BTC"),
        chart(data, "price"),
        rx.vstack(
            price("$91,367"),
            badge("+26.66"),
            spacing="1",
            align="center",
            justify="end",
        ),
        width="100%",
        align="center",
        justify="between",
        padding="0.5em",
    )
