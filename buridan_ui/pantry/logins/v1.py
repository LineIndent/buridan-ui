from dataclasses import dataclass, field

import reflex as rx


@dataclass
class LoginStyle:
    base: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "max_width": "21em",
            "height": "100%",
            "justify": "center",
            "align": "center",
            "padding": "3em 0em",
        },
    )

    LoginButton: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "cursor": "pointer",
            "variant": "surface",
            "color_scheme": "gray",
        },
    )


LoginStyle: LoginStyle = LoginStyle()


def login_button(name: str, *args) -> rx.button:
    return rx.button(*args, name, **LoginStyle.LoginButton)


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
        login_button("Sign In with Email"),
        rx.hstack(
            rx.divider(width="30%"),
            rx.text("OR CONTINUE WITH", font_size="10px", color_scheme="gray"),
            rx.divider(width="30%"),
            width="100%",
            align="center",
            justify="center",
            padding="5px 0px",
        ),
        login_button("Sign In with Email", rx.icon(tag="github", size=15)),
        rx.text(
            "By clicking continue, you agree to our ",
            rx.text("Terms of Service", as_="u"),
            " and ",
            rx.text("Privacy Policy", as_="u"),
            ".",
            font_size="11px",
            color_scheme="gray",
            text_align="center",
            padding="5px 0px",
        ),
        **LoginStyle.base,
    )
