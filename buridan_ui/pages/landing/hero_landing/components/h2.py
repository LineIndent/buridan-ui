import reflex as rx
from dataclasses import dataclass, field


@dataclass
class LoginStyle:
    base: dict[str, str] = field(default_factory=lambda: {"width": "100%"})

    LoginButton: dict[str, str] = field(
        default_factory=lambda: {
            "width": "100%",
            "cursor": "pointer",
            "variant": "surface",
            "color_scheme": "gray",
        }
    )


LoginStyle: LoginStyle = LoginStyle()


def login_button(name: str, *args) -> rx.button:
    return rx.button(*args, name, **LoginStyle.LoginButton)


def hero_login_01():

    return rx.badge(
        rx.vstack(
            rx.vstack(
                rx.heading("Create an account", size="3", weight="bold"),
                rx.text(
                    "Enter your email below.",
                    size="2",
                    weight="medium",
                    color_scheme="gray",
                    align="center",
                ),
                width="100%",
                spacing="1",
                align="center",
            ),
            rx.input(width="100%", placeholder="email@me.com"),
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
            login_button("Sign In with Email", rx.icon(tag="github", size=14)),
            **LoginStyle.base,
        ),
        variant="surface",
        color_scheme="gray",
        padding="2em",
        border_radius="15px",
        max_width="25em",
        **{
            "position": "relative",
            f"@keyframes intro": {
                "0%": {
                    "filter": "blur(10px)",
                    "transform": "scale(1.5)",
                    "opacity": "0",
                },
                "100%": {
                    "filter": "blur(0px)",
                    "transform": "scale(1)",
                    "opacity": "1",
                },
            },
            "animation": "intro 300ms ease",
            # "transition": "filter 300ms ease 2s, transform 300ms ease 2s, opacity 300ms ease 2s",
        },
    )


def logins_v2():

    return rx.badge(
        rx.vstack(
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
            rx.hstack(
                login_button("GitHub", rx.icon(tag="github", size=15)),
                width="100%",
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
            rx.input(width="100%", placeholder="something@example.com"),
            rx.input(width="100%", placeholder="password", type="password"),
            rx.button(
                "Create Account",
                width="100%",
                cursor="pointer",
                variant="surface",
                color_scheme="gray",
            ),
            **LoginStyle.base,
        ),
        width="100%",
        max_width="25em",
        variant="surface",
        color_scheme="gray",
        padding="2em",
        border_radius="15px",
        **{
            "position": "relative",
            f"@keyframes intro": {
                "0%": {
                    "filter": "blur(10px)",
                    "transform": "scale(1.5)",
                    "opacity": "0",
                },
                "100%": {
                    "filter": "blur(0px)",
                    "transform": "scale(1)",
                    "opacity": "1",
                },
            },
            "animation": "intro 300ms ease",
            # "transition": "filter 300ms ease, transform 300ms ease, opacity 300ms ease",
        },
    )
