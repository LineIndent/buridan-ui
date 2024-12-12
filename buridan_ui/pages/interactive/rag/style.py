from dataclasses import dataclass, field

import reflex as rx


@dataclass
class Typography:
    active: dict[str, str] = field(
        default_factory=lambda: {"color": rx.color("slate", 12)},
    )

    passive: dict[str, str] = field(
        default_factory=lambda: {"color": rx.color("slate", 10)},
    )


@dataclass
class Style:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "min_height": "100vh",
        },
    )

    navigation_parent: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "30px",
            "radius": "none",
            "padding": "0em 5em",
            "top": "0",
            "left": "0",
            "position": "absolute",
        },
    )

    navigation_child: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "justify": "between",
            "align": "center",
        },
    )

    content: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "100%",
            "align": "center",
            "display": "grid",
            "grid_template_columns": [
                f"repeat({i}, minmax(0, 1fr))" for i in [1, 1, 1, 1, 2, 2]
            ],
        },
    )

    profile_base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "100%",
            "align": "center",
        },
    )

    profile_inner_content: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "100%",
            "position": "relative",
            "padding": "0em 24px",
            "spacing": "8",
            "border_left": f"1px solid {rx.color('gray', 6)}",
        },
    )

    profile_activity_stat_hstack: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "display": "grid",
            "grid_template_columns": [
                f"repeat({i}, minmax(0, 1fr))" for i in [1, 1, 2, 2, 2, 2]
            ],
            "gap": ["12px" if i <= 3 else "32px" for i in range(6)],
        },
    )

    chat_area_base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "height": "50vh",
            "align": "center",
            "padding": "0em 24px",
        },
    )


Typography: Typography = Typography()

Style: Style = Style()
