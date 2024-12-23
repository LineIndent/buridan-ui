from typing import Callable, Any

import reflex as rx
from reflex.components.radix.themes.components.badge import Badge
from reflex.components.radix.themes.layout.stack import VStack

data = [
    {"month": "January", "users": 600},
    {"month": "February", "users": 850},
    {"month": "March", "users": 1260},
    {"month": "April", "users": 1710},
    {"month": "May", "users": 1200},
    {"month": "June", "users": 3400},
    {"month": "July", "users": 1600},
    {"month": "August", "users": 2100},
    {"month": "September", "users": 1100},
    {"month": "October", "users": 1900},
    {"month": "November", "users": 2800},
    {"month": "December", "users": 2200},
]

titles: Callable[[str, str], VStack] = lambda title, number: rx.vstack(
    rx.text(title, size="1", color=rx.color("slate", 11)),
    rx.heading(number, size="6", color=rx.color("slate", 12)),
    width="100%",
    spacing="1",
)

stat: Callable[[str], Badge] = lambda percent: rx.badge(percent)


def infographic_v2():
    return rx.vstack(
        rx.hstack(
            titles("Subscribers", "4,245"),
            stat("+7.28%"),
            align="center",
            width="100%",
            justify="between",
        ),
        rx.recharts.line_chart(
            rx.recharts.line(data_key="users", type_="linear", dot=False),
            data=data,
            width="100%",
        ),
        width="100%",
        padding="0.5em",
    )
