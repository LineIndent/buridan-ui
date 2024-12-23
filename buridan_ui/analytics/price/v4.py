from reflex.components.radix.themes.components.badge import Badge
from reflex.components.radix.themes.layout.stack import VStack
from reflex.components.radix.themes.typography.text import Text
from reflex.components.recharts.recharts import RechartsCharts
from typing import Callable

import reflex as rx

data = [
    {"price": 0.92},
    {"price": 0.87},
    {"price": 1.05},
    {"price": 0.94},
    {"price": 0.98},
    {"price": 1.02},
    {"price": 0.91},
    {"price": 1.04},
    {"price": 0.89},
    {"price": 0.96},
    {"price": 1.07},
    {"price": 0.94},
    {"price": 1.02},
]

token: Callable[[str, str], VStack] = lambda token, symbol: rx.vstack(
    rx.heading(token, size="4", color=rx.color("slate", 12)),
    rx.text(symbol, size="1", color=rx.color("slate", 10)),
    spacing="1",
)

chart: Callable[[list[dict[str, int]], str], RechartsCharts] = (
    lambda data, key: rx.recharts.line_chart(
        rx.recharts.line(
            data_key=key, dot=False, type_="natural", stroke=rx.color("ruby")
        ),
        data=data,
        width="55%",
    )
)

price: Callable[[str], Text] = lambda price: rx.text(price, size="2", weight="bold")

badge: Callable[[str], Badge] = lambda percent: rx.badge(
    percent, variant="soft", color_scheme="ruby", size="1"
)


def price_v4():
    return rx.hstack(
        token("Cardano", "ADA"),
        rx.hstack(
            chart(data, "price"),
            width="100%",
            height="100%",
            justify="center",
        ),
        rx.vstack(
            price("$0.94"),
            badge("-2.35"),
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
