from dataclasses import dataclass, field
from typing import Callable

import reflex as rx


@dataclass
class FeaturesStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "overflow": "hidden",
            "gap": "2rem",
            "wrap": "wrap",
        }
    )

    base_item: dict[str, str | dict] = field(
        default_factory=lambda: {
            "spacing": "1",
            "flex": "1 1 300px",
            "padding": "0.5rem",
        },
    )


FeaturesStyle: FeaturesStyle = FeaturesStyle()


features = {
    0: {
        "tag": "sun-moon",
        "title": "Light & Dark Mode",
        "description": "Easily switch between themes.",
    },
    1: {
        "tag": "copyright",
        "title": "Open Source License",
        "description": "Free, flexible, and open usage.",
    },
    2: {
        "tag": "component",
        "title": "Pre-designed Components",
        "description": "Simple copy-and-paste components.",
    },
    4: {
        "tag": "code",
        "title": "Pure Python",
        "description": "Single stack, single language solution.",
    },
    5: {
        "tag": "bot-message-square",
        "title": "A.I. Applications",
        "description": "Seamlessly integrate A.I. functionality.",
    },
    7: {
        "tag": "frame",
        "title": "Minimalistic Design",
        "description": "Clean, simple, and sleek UI designs.",
    },
}


feature_item_title: Callable[[str, str], rx.Component] = lambda tag, title: rx.hstack(
    rx.badge(
        rx.icon(tag=tag, size=20),
        variant="surface",
        width="21px",
        height="21px",
        padding="5px",
    ),
    rx.text(title, weight="bold", size="1", color=rx.color("slate", 12)),
    align="center",
    spacing="2",
)

feature_item_description: Callable[[str], rx.Component] = lambda description: rx.hstack(
    rx.text(description, weight="medium", size="1", color=rx.color("slate", 11))
)


feature_item: Callable[[str, str, str], rx.Component] = lambda _, __, ___: rx.vstack(
    feature_item_title(_, __),
    feature_item_description(___),
    **FeaturesStyle.base_item,
)


def featured_v2():
    return rx.hstack(
        *[
            feature_item(item["tag"], item["title"], item["description"])
            for item in features.values()
        ],
        **FeaturesStyle.base,
    )
