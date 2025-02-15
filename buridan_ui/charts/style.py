from dataclasses import dataclass, field

import reflex as rx


@dataclass
class TooltipStyles:
    is_animation_active: bool = False
    separator: str = ""
    cursor: bool = False
    item_style: dict = field(
        default_factory=lambda: {
            "color": "currentColor",
            "display": "flex",
            "paddingBottom": "0px",
            "justifyContent": "space-between",
            "textTransform": "capitalize",
        },
    )
    label_style: dict = field(
        default_factory=lambda: {
            "color": rx.color("slate", 9),
            "fontWeight": "500",
        },
    )
    content_style: dict = field(
        default_factory=lambda: {
            "background": rx.color("slate", 1),
            "borderColor": rx.color("slate", 5),
            "borderRadius": "5px",
            "boxShadow": "0px 24px 12px 0px light-dark(rgba(28, 32, 36, 0.02), rgba(0, 0, 0, 0.00)), 0px 8px 8px 0px light-dark(rgba(28, 32, 36, 0.02), rgba(0, 0, 0, 0.00)), 0px 2px 6px 0px light-dark(rgba(28, 32, 36, 0.02), rgba(0, 0, 0, 0.00))",
            "fontFamily": "var(--font-instrument-sans)",
            "fontSize": "0.875rem",
            "lineHeight": "1.25rem",
            "fontWeight": "500",
            "letterSpacing": "-0.01rem",
            "minWidth": "8rem",
            "width": "175px",
            "padding": "0.375rem 0.625rem ",
            "position": "relative",
        }
    )
    general_style: str = "[&_.recharts-tooltip-item-separator]:w-full"


tooltip_styles = TooltipStyles()


def info(title: str, size: str, subtitle: str, align: str) -> rx.Component:
    return rx.vstack(
        rx.heading(title, size=size, weight="bold"),
        rx.text(subtitle, size="1", color=rx.color("slate", 11), weight="medium"),
        spacing="1",
        align=align,
    )
