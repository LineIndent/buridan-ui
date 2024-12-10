import reflex as rx

from .style import DashboardTrafficBarStyle

trafficDataSet = {
    0: {"color": "blue", "title": "github.com", "qty": 132},
    1: {"color": "purple", "title": " accounts.google.com ", "qty": 32},
    2: {"color": "teal", "title": "discord.app", "qty": 54},
    3: {"color": "orange", "title": "twitter.com", "qty": 23},
    4: {"color": "gray", "title": "Others", "qty": 16},
}

trafficQuantitySum = sum(entry["qty"] for entry in trafficDataSet.values())
trafficDataSet = {
    key: {**entry, "percent": (entry["qty"] / trafficQuantitySum) * 100}
    for key, entry in trafficDataSet.items()
}


def trafficMenuTitle() -> rx.heading:
    return rx.heading(
        "Referral Traffic",
        size="2",
        color=rx.color("slate", 12),
        weight="bold",
    )


def trafficMenuQuantity() -> rx.hstack:
    return rx.hstack(
        *[
            rx.box(
                width=f"{entry['percent']}%",
                height="10px",
                bg=rx.color(entry["color"]),
                border_radius=(
                    "10px 0 0 10px"
                    if idx == 0
                    else "0 10px 10px 0" if idx == len(trafficDataSet) - 1 else "0"
                ),
            )
            for idx, entry in enumerate(trafficDataSet.values())
        ],
        spacing="1",
        align="center",
        width="100%",
    )


def trafficMenuItem(color: str, title: str, qty: str) -> rx.hstack:
    return rx.hstack(
        rx.hstack(
            rx.box(
                width="8px",
                height="8px",
                border_radius="8px",
                background=rx.color(color),
            ),
            rx.text(title, size="1", weight="bold", color=rx.color("slate", 12)),
            align="center",
            spacing="2",
        ),
        rx.text(f"{qty}k", size="1", weight="bold", color=rx.color("slate", 11)),
        align="center",
        justify="between",
        width="100%",
    )


def dashboardTrafficbar() -> rx.vstack:
    return rx.vstack(
        rx.hstack(
            trafficMenuTitle(),
            rx.icon(tag="download", size=14),
            width="100%",
            align="center",
            justify="between",
        ),
        rx.divider(height="0.5em", opacity="0"),
        trafficMenuQuantity(),
        rx.divider(height="0.5em", opacity="0"),
        rx.vstack(
            *[
                trafficMenuItem(item["color"], item["title"], item["qty"])
                for item in trafficDataSet.values()
            ],
            width="100%",
        ),
        rx.spacer(),
        rx.button(
            "See More Analytics",
            width="100%",
            variant="surface",
            cursor="pointer",
        ),
        **DashboardTrafficBarStyle.base,
    )
