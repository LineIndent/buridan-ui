import reflex as rx


def subscribe_v1():
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.hstack(
                    rx.icon(tag="mail", size=13, color=rx.color("slate", 11)),
                    rx.input(
                        variant="soft",
                        background="transparent",
                        outline="none",
                        placeholder="Enter your email",
                        width="100%",
                    ),
                    align="center",
                    spacing="0",
                ),
                rx.button(
                    "Join",
                    variant="surface",
                ),
                border=f"1px solid {rx.color('gray', 6)}",
                align="center",
                border_radius="8px",
                padding="5px 5px 5px 10px",
                width="100%",
                justify="between",
            ),
            rx.text(
                "No spam, unsubscribe at any time.",
                size="1",
                color=rx.color("slate", 11),
            ),
            max_width="30em",
            width="100%",
            align="start",
        ),
        width="100%",
        height="25vh",
    )
