from dataclasses import dataclass, field

import reflex as rx


@dataclass
class CreditBannerStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "justify": "center",
            "wrap": "wrap",
            "padding": "0.5em",
            "bg": rx.color("blue", 3),
            "border_top": f"1.5px solid {rx.color('blue')}",
            "border_bottom": f"1.5px solid {rx.color('blue')}",
        },
    )


CreditBannerStyle: CreditBannerStyle = CreditBannerStyle()


def link(name: str, url: str) -> rx.Component:
    return rx.link(
        name,
        href=url,
        weight="bold",
        text_decoration="none",
        color="inherit",
        is_external=True,
    )


def credit_banner() -> rx.Component:
    return rx.hstack(
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
