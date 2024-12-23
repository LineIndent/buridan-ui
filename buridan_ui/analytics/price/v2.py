from reflex.components.radix.themes.components.badge import Badge
from reflex.components.radix.themes.layout.stack import VStack
from reflex.components.radix.themes.typography.text import Text
from reflex.components.recharts.recharts import RechartsCharts
from typing import Callable

import reflex as rx

data = [
    {"price": 3191.57},
    {"price": 2224.33},
    {"price": 1143.82},
    {"price": 4701.94},
    {"price": 2835.53},
    {"price": 2929.99},
    {"price": 6663.37},
    {"price": 4775.2},
    {"price": 1747.53},
    {"price": 1553.76},
    {"price": 1878.3},
    {"price": 1384.6},
    {"price": 1545.7},
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
        height="100%",  # add height to prevent overflow if data is large values
    )
)


price: Callable[[str], Text] = lambda price: rx.text(price, size="2", weight="bold")

badge: Callable[[str], Badge] = lambda percent: rx.badge(
    percent, variant="soft", color_scheme="green", size="1"
)


def price_v2():
    return rx.hstack(
        token("Ethereum", "ETH"),
        rx.hstack(chart(data, "price"), width="100%", height="100%", justify="center"),
        rx.vstack(
            price("$3,797"),
            badge("+16.96"),
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
