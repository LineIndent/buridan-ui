from typing import Callable, Any

import reflex as rx
from reflex.components.radix.themes.components.badge import Badge
from reflex.components.radix.themes.layout.stack import VStack

data = [
    {"month": "January", "users": 820},
    {"month": "February", "users": 950},
    {"month": "March", "users": 1700},
    {"month": "April", "users": 1400},
    {"month": "May", "users": 1800},
    {"month": "June", "users": 1410},
    {"month": "July", "users": 1200},
    {"month": "August", "users": 1600},
    {"month": "September", "users": 1100},
    {"month": "October", "users": 1950},
    {"month": "November", "users": 1900},
    {"month": "December", "users": 2100},
]

titles: Callable[[str, str], VStack] = lambda title, number: rx.vstack(
    rx.text(title, size="1", color=rx.color("slate", 11)),
    rx.heading(number, size="6", color=rx.color("slate", 12)),
    width="100%",
    spacing="1",
)

stat: Callable[[str], Badge] = lambda percent: rx.badge(percent)


def infographic_v3():
    return rx.vstack(
        rx.hstack(
            titles("Followers", "8,129"),
            stat("+13.53%"),
            align="center",
            width="100%",
            justify="between",
        ),
        rx.recharts.line_chart(
            rx.recharts.line(data_key="users", type_="step", dot=False),
            data=data,
            width="100%",
        ),
        width="100%",
        padding="0.5em",
    )
