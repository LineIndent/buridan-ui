from dataclasses import dataclass, field
import reflex as rx


@dataclass
class NavigationStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "top": "0",
            "left": "0",
            "z_index": "30",
            "width": "100%",
            "align": "center",
            "position": "absolute",
            "justify": "between",
            "padding": "14px 2em",
            "backdrop_filter": "blur(10px)",
            "border_bottom": "solid",
            "border_image": f"linear-gradient(to right, transparent, {rx.color('gray', 6)},  transparent) 2 / 4px",
            "border_image_width": "0px 0px 1px 0px",
        }
    )

    logo: dict[str, str] = field(
        default_factory=lambda: {
            "width": "22px",
            "height": "22px",
            "border_radius": "15%",
            "object_fit": "fit",
            "border": f"1px solid {rx.color('slate', 12)}",
            "display": ["none", "none", "none", "none", "none", "flex"],
        }
    )

    landing_page_nav: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "align": "center",
            "justify": "between",
            "backdrop_filter": "blur(10px)",
            "padding": ["14px 0.5em" if i <= 5 else "14px 0em" for i in range(6)],
        }
    )


NavigationStyle: NavigationStyle = NavigationStyle()
