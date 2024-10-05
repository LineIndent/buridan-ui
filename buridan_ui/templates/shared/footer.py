import reflex as rx


def footer():
    return rx.hstack(
        rx.text(
            "Built by ",
            rx.chakra.span("Ahmad Hakim", as_="u"),
            " . More details is available on ",
            rx.chakra.span("GitHub", as_="u"),
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
        height="150px",
        background=rx.color("gray", 2),
        border_left=f"1px solid {rx.color('gray', 4)}",
    )
