import reflex as rx

from typing import Callable
from dataclasses import dataclass, field


@dataclass
class TooltipStyles:
    separator: str = ""
    cursor: bool = False
    wrapper_style: dict = field(
        default_factory=lambda: {"padding": 0, "margin": 0, "width": "150px"}
    )
    view_box: dict = field(
        default_factory=lambda: {"padding": 0, "margin": 0, "width": "150px"}
    )
    item_style: dict = field(
        default_factory=lambda: {
            "color": rx.color("slate", 11),
            "fontSize": 11,
            "padding": 0,
            "margin": 0,
            "justify-content": "space-between",
            "display": "flex",
            "textTransform": "capitalize",
            "width": "175px",
        }
    )
    label_style: dict = field(
        default_factory=lambda: {
            "fontSize": 11,
            "padding": 0,
            "fontWeight": "bold",
            "color": rx.color("slate", 12),
        }
    )
    content_style: dict = field(
        default_factory=lambda: {
            "background": rx.color("gray", 2),
            "borderColor": rx.color("gray", 4),
            "borderRadius": "6px",
            "width": "150px",
            "padding": 6,
            "margin": 0,
        }
    )


tooltip_styles = TooltipStyles()


info: Callable[[str, str, str, str], rx.Component] = (
    lambda title, size, subtitle, align: rx.vstack(
        rx.heading(title, size=size, weight="bold"),
        rx.text(subtitle, size="1", color=rx.color("slate", 11), weight="medium"),
        spacing="1",
        align=align,
    )
)
