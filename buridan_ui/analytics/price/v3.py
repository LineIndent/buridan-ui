from reflex.components.radix.themes.components.badge import Badge
from reflex.components.radix.themes.layout.stack import VStack
from reflex.components.radix.themes.typography.text import Text
from reflex.components.recharts.recharts import RechartsCharts
from typing import Callable

import reflex as rx

data = [
    {"price": 195.82},
    {"price": 222.14},
    {"price": 210.77},
    {"price": 250.33},
    {"price": 182.65},
    {"price": 187.23},
    {"price": 174.89},
    {"price": 212.45},
    {"price": 205.12},
    {"price": 195.36},
    {"price": 230.51},
    {"price": 218.89},
    {"price": 200.22},
]

token: Callable[[str, str], VStack] = lambda token, symbol: rx.vstack(
    rx.heading(token, size="4", color=rx.color("slate", 12)),
    rx.text(symbol, size="1", color=rx.color("slate", 10)),
    spacing="1",
)

chart: Callable[[list[dict[str, int]], str], RechartsCharts] = (
    lambda data, key: rx.recharts.line_chart(
        rx.recharts.line(data_key=key, dot=False, type_="natural"),
        data=data,
        width="55%",
    )
)

price: Callable[[str], Text] = lambda price: rx.text(price, size="2", weight="bold")

badge: Callable[[str], Badge] = lambda percent: rx.badge(
    percent, variant="soft", color_scheme="green", size="1"
)


def price_v3():
    return rx.hstack(
        token("Litecoin", "LTC"),
        rx.hstack(
            chart(data, "price"),
            width="100%",
            height="100%",
            justify="center",
        ),
        rx.vstack(
            price("$187.23"),
            badge("+5.35"),
            spacing="1",
            align="center",
            justify="end",
        ),
        width="100%",
        align="center",
        justify="between",
        padding="0.5em",
        height="65px",
    )
