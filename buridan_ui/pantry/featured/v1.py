from typing import Callable
from dataclasses import dataclass, field
import reflex as rx


data = {
    0: {
        "image": "auditors",
        "title": "Pharmacists",
        "description": "Azurill can be seen bouncing and playing on its big, rubbery tail",
    },
    1: {
        "image": "lawyers",
        "title": "Lawyers",
        "description": "Fans obsess over the particular length and angle of its arms",
    },
    2: {
        "image": "accountants",
        "title": "Bank owners",
        "description": "They divvy up their prey evenly among the members of their pack",
    },
    3: {
        "image": "others",
        "title": "Others",
        "description": "Phanpy uses its long nose to shower itself",
    },
}


@dataclass
class FeaturesV1Style:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "max_width": "45em",
            "align": "start",
            "justify": "center",
        }
    )


FeaturesV1Style: FeaturesV1Style = FeaturesV1Style()

txt: Callable[[str, str, str, int], rx.text] = (
    lambda name, weight, size, shade: rx.text(
        name, weight=weight, size=size, color=rx.color("slate", shade)
    )
)

feature_item: Callable[[str, str], rx.vstack] = lambda title, description: rx.vstack(
    txt(title, "bold", "2", 11), txt(description, "medium", "3", 12), spacing="1"
)


def featured_v1():
    return rx.vstack(
        rx.heading(
            "PharmLand is not just for Doctors",
            color=rx.color("slate", 12),
            size="4",
        ),
        rx.text(
            "Its lungs contain an organ that creates electricity. The crackling sound of electricity can be heard when it exhales. Azurill’s tail is large and bouncy. It is packed full of the nutrients this Pokémon needs to grow.",
            color=rx.color("slate", 11),
            size="2",
        ),
        rx.divider(height="0.5em", opacity="0"),
        rx.hstack(
            *[
                feature_item(item["title"], item["description"])
                for item in data.values()
            ],
            width="100%",
            wrap="wrap",
        ),
        **FeaturesV1Style.base,
    )
