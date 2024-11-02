from dataclasses import dataclass, field
import reflex as rx


@dataclass
class SideMenuStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "top": "0",
            "left": "0",
            "bottom": "0",
            "width": "350px",
            "height": "100vh",
            "overflow": "auto",
            "position": "sticky",
            "padding": "90px 28px",
            "scrollbar_width": "none",
            "background": rx.color("gray", 2),
            "display": ["none" if i <= 4 else "flex" for i in range(6)],
            "mask": "linear-gradient(to bottom, hsl(0, 0%, 0%, 1) 94%, hsl(0, 0%, 0%, 0) 100%)",
        }
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "position": "relative",
            "spacing": "8",
        }
    )


SideMenuStyle: SideMenuStyle = SideMenuStyle()
