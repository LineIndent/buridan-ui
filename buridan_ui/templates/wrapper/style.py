from dataclasses import dataclass, field
import reflex as rx


@dataclass
class MenuWrapperStyle:
    blip: dict[str, str] = field(
        default_factory=lambda: {
            "width": "24px",
            "height": "24px",
            "border_radius": "24px",
            "background": rx.color("gray", 3),
            "border": f"1.25px solid {rx.color('gray', 6)}",
            "position": "absolute",
            "left": "-11.5px",
            "align_items": "center",
            "justify_content": "center",
            "display": "flex",
        }
    )

    wrapper: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "align": "start",
            "justify": "start",
            "padding_left": "24px",
            "border_radius": "0px 5px 5px 0px",
            "border_left": f"1px solid {rx.color('gray', 6)}",
        }
    )


@dataclass
class BaseHeaderWrapper:
    wrapper: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "align": "start",
            "padding": ["12px 0px" if i >= 5 else "12px 24px" for i in range(6)],
        }
    )

    titles: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "max_width": "45em",
            "align": "start",
            "spacing": "4",
        }
    )


MenuWrapperStyle: MenuWrapperStyle = MenuWrapperStyle()
BaseHeaderWrapper: BaseHeaderWrapper = BaseHeaderWrapper()
