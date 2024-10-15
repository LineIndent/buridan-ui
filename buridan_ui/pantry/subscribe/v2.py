import reflex as rx


def subscribe_v2():

    return rx.center(
        rx.vstack(
            rx.text(
                "Sign up to our newsletter",
                size="4",
                weight="bold",
                color=rx.color("slate", 12),
            ),
            rx.hstack(
                rx.hstack(
                    rx.input(
                        variant="soft",
                        background="transparent",
                        outline="none",
                        placeholder="Enter your email",
                        width="100%",
                    ),
                    align="center",
                    spacing="0",
                    border=f"1px solid {rx.color('gray', 6)}",
                    border_radius="8px",
                    padding="5px 5px 5px 10px",
                    flex=["100%" if i <= 3 else "80%" for i in range(6)],
                ),
                rx.button(
                    "Subscribe",
                    variant="solid",
                    flex=["100%" if i <= 3 else "15%" for i in range(6)],
                    size="3",
                ),
                align="center",
                width="100%",
                justify="start",
                flex_wrap="wrap",
            ),
            max_width="30em",
            width="100%",
            align="center",
            spacing="5",
        ),
        width="100%",
        height="25vh",
    )
