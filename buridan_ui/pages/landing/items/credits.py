import reflex as rx
from dataclasses import dataclass, field
from typing import Callable, Dict, List


@dataclass
class CreditBannerStyle:
    base: Dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "justify": "center",
            "wrap": "wrap",
            "bg": rx.color("blue", 3),
            "padding": "14px",
            "border": f"1.5px solid {rx.color('blue')}",
        }
    )


CreditBannerStyle: CreditBannerStyle = CreditBannerStyle()

link: Callable[[str, str], rx.Component] = lambda name, url: rx.link(
    name,
    href=url,
    weight="bold",
    text_decoration="none",
    color="inherit",
    is_external=True,
)

credit_banner: Callable[[], rx.Component] = lambda: rx.hstack(
    rx.text(
        "Special thanks to ",
        link("@Reflex", "https://reflex.dev"),
        ", ",
        link("@unDraw", "https://undraw.co"),
        ", ",
        link("@shadcn/ui", "https://ui.shadcn.com/"),
        " and other amazing open-source projects for the inspiration!",
        color_scheme="blue",
        size="1",
        align="center",
    ),
    **CreditBannerStyle.base,
)
