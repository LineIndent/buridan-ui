from dataclasses import dataclass, field

import reflex as rx


@dataclass
class ProfileComponentStyle:
    profile_item_input_parent: dict[str, str] = field(
        default_factory=lambda: {
            "align": "center",
            "border_bottom": f"1px solid {rx.color('slate')}",
            "width": "100%",
            "justify": "between",
        },
    )

    profile_item_input_unit: dict[str, str] = field(
        default_factory=lambda: {
            "size": "1",
            "weight": "bold",
            "width": "30px",
            "align": "center",
        },
    )

    profile_item_input: dict[str, str] = field(
        default_factory=lambda: {
            "radius": "none",
            "variant": "soft",
            "outline": "none",
            "background": "none",
            "width": "100%",
        },
    )

    profile_item_activity: dict[str, str] = field(
        default_factory=lambda: {
            "size": "2",
            "variant": "soft",
            "width": "100%",
            "color_scheme": "gray",
        },
    )


@dataclass
class ChatAreaStyle:
    chat_box: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "100%",
            "border_radius": "8px",
            "overflow": "hidden",
            "position": "relative",
        },
    )

    model_tag: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "30px",
            "radius": "none",
            "padding": "0em 2em",
            "top": "0",
            "left": "0",
            "position": "absolute",
            "color_scheme": "gray",
            "background": rx.color("blue", 3),
            "z_index": "20",
        },
    )

    chat_session_style: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "padding": "3em 2em 4em 2em",
            "height": "85vh",
            "overflow": "auto",
            "mask": "linear-gradient(to bottom, hsl(0, 0%, 0%, 1) 85%, hsl(0, 0%, 0%, 0) 100%)",
        },
    )


ProfileComponentStyle: ProfileComponentStyle = ProfileComponentStyle()
ChatAreaStyle: ChatAreaStyle = ChatAreaStyle()
