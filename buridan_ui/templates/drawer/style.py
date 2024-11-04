from dataclasses import dataclass, field
import reflex as rx


@dataclass
class DrawerStyle:
    content: dict[str, str] = field(
        default_factory=lambda: {
            "top": "auto",
            "right": "auto",
            "height": "100%",
            "overflow": "scroll",
            "width": "20em",
            "background": rx.color("gray", 2),
        }
    )

    title: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "60px",
            "align": "center",
            "justify": "between",
            "padding": "0.75em 1em",
        }
    )

    header: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "40px",
            "color_scheme": "gray",
        }
    )

    header_components: dict[str, str] = field(
        default_factory=lambda: {
            "align": "center",
            "justify": "between",
            "width": "100%",
            "padding": "0.75em 1em",
        }
    )

    logo: dict[str, str] = field(
        default_factory=lambda: {
            "width": "22px",
            "height": "22px",
            "border_radius": "15%",
            "object_fit": "fit",
            "border": f"1px solid {rx.color('slate', 12)}",
        }
    )

    stack_content: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "100vh",
            "overflow": "auto",
            "spacing": "0",
            "padding_bottom": "2em",
        }
    )

    drawer_menu_link: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "align": "center",
            "justify": "between",
            "padding": "0.75em 1em",
        }
    )


DrawerStyle: DrawerStyle = DrawerStyle()
