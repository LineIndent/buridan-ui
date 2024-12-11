import reflex as rx
from reflex.components.datadisplay.code import Theme

code: dict[str, str] = {
    "width": "100%",
    "font_size": "12px",
    "language": "python",
    "wrap_long_lines": True,
    "scrollbar_width": "none",
    "code_tag_props": {"pre": "transparent"},
    "custom_style": {"backgroundColor": "transparent"},
}

root = {
    "width": "100%",
    "padding": "2px",
    "overflow": "hidden",
    "default_value": "1",
    "border_radius": "10px",
    "margin": "1em 0em",
    "background": rx.color("gray", 3),
}

ComponentMapping = {
    "h2": lambda string: rx.heading(
        string,
        color=rx.color("slate", 11),
        margin="1em 0em 0.5em 0em",
    ),
    "h3": lambda string: rx.heading(
        string,
        margin="2em 0em 0.5em 0em",
        color=rx.color("slate", 11),
        size="5",
    ),
    "h4": lambda string: rx.heading(
        string,
        margin="2em 0em 0.5em 0em",
        color=rx.color("gray", 11),
        size="3",
    ),
    "p": lambda string: rx.text(
        string,
        color=rx.color("gray", 11),
        size="2",
        line_height=1.85,
    ),
    "codeblock": lambda string, **props: rx.vstack(
        rx.code_block(
            string,
            **code,
            theme=Theme.darcula,
        ),
        **root,
    ),
}
