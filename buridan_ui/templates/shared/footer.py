import reflex as rx


personal: str = "https://github.com/lineindent"
library: str = "https://github.com/LineIndent/buridan-ui"


def footer():
    return rx.hstack(
        rx.text(
            "Built by ",
            rx.link(
                "Ahmad Hakim", color_scheme="gray", href=personal, is_external=True
            ),
            " . More details is available on ",
            rx.link("GitHub", color_scheme="gray", href=library, is_external=True),
            " .",
            color_scheme="gray",
            font_size="11px",
            weight="medium",
        ),
        width="100%",
        padding=[
            "32px 32px",
            "32px 32px",
            "32px 32px",
            "32px 32px",
            "32px 48px",
            "32px 64px",
        ],
        position="sticky",
        right="0",
        left="0",
        bottom="0",
        height="120px",
        background=rx.color("gray", 2),
        border_left=f"1px solid {rx.color('gray', 4)}",
    )
