from typing import Callable, Any

import reflex as rx
from reflex.components.radix.themes.components.badge import Badge
from reflex.components.radix.themes.layout.stack import VStack

data = [
    {"month": "January", "users": 800},
    {"month": "February", "users": 950},
    {"month": "March", "users": 1200},
    {"month": "April", "users": 1700},
    {"month": "May", "users": 2200},
    {"month": "June", "users": 2400},
    {"month": "July", "users": 1200},
    {"month": "August", "users": 1600},
    {"month": "September", "users": 1100},
    {"month": "October", "users": 1900},
    {"month": "November", "users": 1700},
    {"month": "December", "users": 2500},
]

titles: Callable[[str, str], VStack] = lambda title, number: rx.vstack(
    rx.text(title, size="1", color=rx.color("slate", 11)),
    rx.heading(number, size="6", color=rx.color("slate", 12)),
    width="100%",
    spacing="1",
)

stat: Callable[[str], Badge] = lambda percent: rx.badge(percent)


def infographic_v1():
    return rx.vstack(
        rx.hstack(
            titles("Users", "14,245"),
            stat("+3.53%"),
            align="center",
            width="100%",
            justify="between",
        ),
        rx.recharts.line_chart(
            rx.recharts.line(data_key="users", type_="natural", dot=False),
            data=data,
            width="100%",
        ),
        width="100%",
        padding="0.5em",
    )
