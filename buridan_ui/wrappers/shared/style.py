from dataclasses import dataclass, field

import reflex as rx


@dataclass
class ComponentWrapperUtilStyle:
    buttons: dict[str, str] = field(
        default_factory=lambda: {
            "size": "1",
            "color": rx.color("slate", 11),
            "outline": "none",
            "cursor": "pointer",
            "variant": "soft",
            "color_scheme": "gray",
            "width": "25px",
            "height": "25px",
        },
    )


ComponentWrapperUtilStyle: ComponentWrapperUtilStyle = ComponentWrapperUtilStyle()
