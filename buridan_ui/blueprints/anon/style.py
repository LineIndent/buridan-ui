from dataclasses import dataclass, field

import reflex as rx


@dataclass
class SandboxAuthStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "60vh",
            "overflow": "hidden",
        },
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "max_width": "22em",
            "align": "center",
            "justify": "center",
            "text_align": "center",
            "spacing": "2",
            "padding": "1.5em",
            "border_radius": "10px",
            "position": "relative",
            "margin": "10px",
            "background": rx.color("gray", 3),
        },
    )


@dataclass
class AuthDynamicStyle:
    passive: dict[str, bool] = field(
        default_factory=lambda: {"loading": False, "disabled": False},
    )
    active: dict[str, bool] = field(
        default_factory=lambda: {"loading": True, "disabled": True},
    )
    finished: dict[str, bool] = field(
        default_factory=lambda: {"loading": False, "disabled": True},
    )

    alert_passive: dict[str, str] = field(
        default_factory=lambda: {
            "height": "0vh",
            "filter": "blur(10px)",
            "transform": "scale(1.5)",
            "opacity": "0",
        },
    )

    alert_active: dict[str, str] = field(
        default_factory=lambda: {
            "height": "100%",
            "filter": "blur(0px)",
            "transform": "scale(1)",
            "opacity": "1",
        },
    )


SandboxAuthStyle: SandboxAuthStyle = SandboxAuthStyle()
AuthDynamicStyle: AuthDynamicStyle = AuthDynamicStyle()
