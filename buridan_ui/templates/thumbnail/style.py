from dataclasses import dataclass, field
import reflex as rx


@dataclass
class ThumbnailStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "align": "center",
            "justify": "center",
            "position": "relative",
            "flex": "1 1 300px",
            "height": "220px",
            "border": f"1px solid {rx.color('gray', 6)}",
            "bg": rx.color("slate", 2),
            "border_radius": "12px",
            "z_index": "25",
            "overflow": "hidden",
            "spacing": "0",
            "transition": "all 250ms linear",
        }
    )

    image: dict[str, str] = field(
        default_factory=lambda: {
            "max_width": "66%",
            "max_height": "60%",
            "object_fit": "fill",
            "transition": "all 550ms ease",
            "_hover": {"transform": "scale(1.1)"},
            "mask": "linear-gradient(to bottom, hsl(0, 0%, 0%, 0.95) 45%, hsl(0, 0%, 0%, 0))",
        }
    )

    container: dict[str, str] = field(
        default_factory=lambda: {
            "position": "absolute",
            "bottom": "0",
            "left": "0",
            "bg": rx.color("gray", 3),
            "width": "100%",
            "padding": "12px 18px",
            "spacing": "0",
            "justify": "between",
        }
    )


ThumbnailStyle: ThumbnailStyle = ThumbnailStyle()
