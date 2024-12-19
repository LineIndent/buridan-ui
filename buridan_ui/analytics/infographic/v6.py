from typing import Callable, Any

import reflex as rx
from reflex.components.radix.themes.components.badge import Badge
from reflex.components.radix.themes.layout.stack import VStack

data = [
    {"month": "January", "users": 1000},
    {"month": "February", "users": 1150},
    {"month": "March", "users": 1200},
    {"month": "April", "users": 1700},
    {"month": "May", "users": 2200},
    {"month": "June", "users": 1900},
    {"month": "July", "users": 1600},
    {"month": "August", "users": 1700},
    {"month": "September", "users": 1500},
    {"month": "October", "users": 1420},
    {"month": "November", "users": 1360},
    {"month": "December", "users": 1190},
]

titles: Callable[[str, str], VStack] = lambda title, number: rx.vstack(
    rx.text(title, size="1", color=rx.color("slate", 11)),
    rx.heading(number, size="6", color=rx.color("slate", 12)),
    width="100%",
    spacing="1",
)

stat: Callable[[str], Badge] = lambda percent: rx.badge(percent)


def infographic_v6():
    return rx.vstack(
        rx.hstack(
            titles("Users", "9,655"),
            stat("+3.53%"),
            align="center",
            width="100%",
            justify="between",
        ),
        rx.recharts.area_chart(
            rx.recharts.area(
                data_key="users", fill=rx.color("ruby"), type_="linear", stroke="none"
            ),
            data=data,
            width="100%",
        ),
        width="100%",
        padding="0.5em",
    )
