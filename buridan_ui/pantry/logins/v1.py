import reflex as rx


def logins_v1():

    return rx.vstack(
        rx.vstack(
            rx.heading("Create an account", size="5", weight="bold"),
            rx.text(
                "Enter your email below to create your account",
                font_size="12px",
                weight="medium",
                color_scheme="gray",
            ),
            width="100%",
            spacing="1",
            align="center",
        ),
        rx.input(width="100%", placeholder="something@example.com"),
        rx.button(
            "Sign In with Email",
            width="100%",
            cursor="pointer",
            variant="surface",
            color_scheme="gray",
        ),
        rx.hstack(
            rx.divider(width="30%"),
            rx.text("OR CONTINUE WITH", font_size="10px", color_scheme="gray"),
            rx.divider(width="30%"),
            width="100%",
            align="center",
            justify="center",
            padding="5px 0px",
        ),
        rx.button(
            rx.icon(tag="github", size=15),
            "GitHub",
            width="100%",
            variant="surface",
            cursor="pointer",
            color_scheme="gray",
        ),
        rx.text(
            "By clicking continue, you agree to our ",
            rx.chakra.span("Terms of Service", as_="u"),
            " and ",
            rx.chakra.span("Privacy Policy", as_="u"),
            ".",
            font_size="11px",
            color_scheme="gray",
            text_align="center",
            padding="5px 0px",
        ),
        max_width="21em",
        height="100%",
        justify="center",
        align="center",
        padding="3em 0em",
    )
