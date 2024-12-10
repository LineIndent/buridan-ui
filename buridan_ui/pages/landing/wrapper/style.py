from __future__ import annotations

from dataclasses import dataclass, field

import reflex as rx


def padding() -> list[str]:
    return ["12px 0px" if i >= 5 else "12px 12px" for i in range(6)]


WrapperShared: dict[str, str | list[str]] = {
    "width": "100%",
    "spacing": "5",
    "padding": padding(),
}
TitlesShared: dict[str, str] = {"width": "100%", "spacing": "5"}


@dataclass
class LandingPageSectionWrapperStyle:
    wrapper: dict[str, str] = field(
        default_factory=lambda: {"align": "start", **WrapperShared},
    )

    wrapper_secondary: dict[str, str] = field(
        default_factory=lambda: {"align": "start", **WrapperShared},
    )

    titles: dict[str, str] = field(
        default_factory=lambda: {
            "align": "start",
            "text_align": "start",
            "max_width": "48em",
            **TitlesShared,
        },
    )

    titles_secondary: dict[str, str] = field(
        default_factory=lambda: {
            "align": "start",
            "text_align": "start",
            "max_width": "38em",
            **TitlesShared,
        },
    )

    blip: dict[str, str] = field(
        default_factory=lambda: {
            "width": "24px",
            "height": "24px",
            "border_radius": "24px",
            "background": rx.color("blue", 3),
            "border": f"1.25px solid {rx.color('blue', 6)}",
            "position": "absolute",
            "left": "-11.5px",
            "align_items": "center",
            "justify_content": "center",
            "display": "flex",
        },
    )

    features: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "align": "start",
            "justify": "start",
            "padding_left": "24px",
            "border_radius": "0px 5px 5px 0px",
            "position": "relative",
            "border_left": f"1px solid {rx.color('blue', 6)}",
        },
    )


@dataclass
class LandingPageButtons:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "radius": "small",
            "cursor": "pointer",
            "size": "3",
        },
    )


LandingPageButtons: LandingPageButtons = LandingPageButtons()

LandingPageSectionWrapperStyle: LandingPageSectionWrapperStyle = (
    LandingPageSectionWrapperStyle()
)
