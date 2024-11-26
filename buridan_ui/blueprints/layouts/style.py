from dataclasses import dataclass, field
from typing import Dict

import reflex as rx


@dataclass
class LayoutStyleSheet:

    navigation: Dict[str, str] = field(
        default_factory=lambda: {
            "top": "0",
            "left": "0",
            "width": "100%",
            "align": "center",
            "justify": "between",
            "position": "sticky",
            "padding": "1.25em 2em",
            "background": rx.color("gray", 3),
        }
    )

    singleColumn: Dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "100vh",
            "position": "relative",
            "overflow": "scroll",
        }
    )

    doubleColumn: Dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "100vh",
            "overscroll_behavior": "none",
            "position": "relative",
        }
    )

    doubleColumnContentArea: Dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "100%",
            "position": "relative",
            "overflow": "scroll",
            "spacing": "2",
            "background": rx.color("gray", 1),
        }
    )

    doubleColumnLeft: Dict[str, str] = field(
        default_factory=lambda: {
            "top": "0",
            "left": "0",
            "spacing": "5",
            "width": "320px",
            "max_width": "320px",
            "height": "100vh",
            "position": "sticky",
            "padding": "2em 1.5em",
            "background": rx.color("gray", 3),
            "border_right": f"1px solid {rx.color('gray', 4)}",
            "display": ["none" if i <= 4 else "flex" for i in range(6)],
        }
    )


LayoutStyleSheet: LayoutStyleSheet = LayoutStyleSheet()
