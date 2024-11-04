from dataclasses import dataclass, field
import reflex as rx


@dataclass
class ComponentWrapperUtilStyle:
    buttons: dict[str, str] = field(
        default_factory=lambda: {
            "size": "1",
            "color": rx.color("slate", 11),
            "width": "32px",
            "height": "32px",
            "outline": "none",
            "cursor": "pointer",
            "variant": "soft",
            "color_scheme": "gray",
        }
    )


ComponentWrapperUtilStyle: ComponentWrapperUtilStyle = ComponentWrapperUtilStyle()
