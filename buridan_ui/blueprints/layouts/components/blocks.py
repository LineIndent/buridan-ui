import reflex as rx


def blockTypeOne() -> rx.Component:
    return rx.hstack(
        *[
            rx.box(
                flex="1 1 200px",
                border_radius="8px",
                height="30vh",
                border=f"1px solid {rx.color('gray', 5)}",
                background=rx.color("gray", 3),
            )
            for _ in range(4)
        ],
        *[
            rx.box(
                flex="1 1 400px",
                border_radius="8px",
                height="30vh",
                border=f"1px solid {rx.color('gray', 5)}",
                background=rx.color("gray", 3),
            )
            for _ in range(4)
        ],
        *[
            rx.box(
                flex="1 1 200px",
                border_radius="8px",
                height="30vh",
                border=f"1px solid {rx.color('gray', 5)}",
                background=rx.color("gray", 3),
            )
            for _ in range(4)
        ],
        wrap="wrap",
        width="100%",
    )
