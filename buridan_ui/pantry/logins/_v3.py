import reflex as rx

data = [
    {"title": "Email Address", "name": "email", "placeholder": "Email Address"},
    {"title": "Password", "name": "password", "placeholder": "Password"},
]

_ = {
    "@keyframes text_sequence_author": {
        "0%": {
            "transform": "translateY(-30px)",
            "opacity": "0",
            "padding": "0",
        },
        "100%": {
            "transform": f"translateY(0px)",
            "opacity": "1",
            "padding": "1em",
        },
    },
    "animation": f"text_sequence_author 850ms ease",
}


def _login_v3(
    form_data: list[dict[str, str]] = data,
    avatar: str = None,
    title: str = None,
    subtitle: str = None,
    submit_event: rx.EventHandler = None,  # eventhandler??
):
    return rx.vstack(
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    rx.avatar(
                        src="https://avatars.githubusercontent.com/u/104714959?s=200&v=4",
                        size="3",
                    ),
                    width="100%",
                    justify="center",
                    padding="1em 0em",
                ),
                rx.vstack(
                    rx.text("Login to your Account", class_name="text-xl font-bold"),
                    rx.text(
                        "Welcome back! Please sign in to continue",
                        class_name="text-sm font-regular",
                    ),
                    width="100%",
                    spacing="1",
                    align="center",
                ),
                rx.hstack(
                    rx.button(
                        rx.icon(tag="mail", size=13),
                        rx.text("Google", class_name="text-sm font-semibold"),
                        class_name="flex-1 shadow-sm border-2",
                        variant="surface",
                        color_scheme="gray",
                        border=f"0.75px solid {rx.color('gray', 4)}",
                    ),
                    rx.button(
                        rx.icon(tag="github", size=13),
                        rx.text("GitHub", class_name="text-sm font-semibold"),
                        class_name="flex-1 shadow-sm border-2",
                        variant="surface",
                        color_scheme="gray",
                        border=f"0.75px solid {rx.color('gray', 4)}",
                    ),
                    width="100%",
                    padding="1em 0em 0em 0em",
                ),
                rx.hstack(
                    rx.divider(width="30%"),
                    rx.text("OR CONTINUE WITH", font_size="10px", color_scheme="gray"),
                    rx.divider(width="30%"),
                    width="100%",
                    align="center",
                    justify="center",
                    padding="1em 0em",
                ),
                rx.form(
                    rx.vstack(
                        rx.foreach(
                            form_data,
                            lambda item: rx.vstack(
                                rx.text(
                                    item["title"], class_name="text-sm font-regular"
                                ),
                                rx.input(
                                    # placeholder=item["placeholder"],
                                    name=item["name"],
                                    width="100%",
                                    type=rx.cond(
                                        item["name"] == "password", "password", "text"
                                    ),
                                ),
                                width="100%",
                                spacing="2",
                            ),
                        ),
                        rx.button(
                            "Continue",
                            class_name="bg-gradient-to-r from-purple-500 to-purple-600 hover:from-purple-600 hover:to-purple-700 text-white font-semibold py-2 px-4 rounded-lg shadow-md hover:shadow-lg transition-all duration-200 ease-in-out w-full",
                        ),
                        width="100%",
                        spacing="5",
                        height="100%",
                    ),
                    height="100%",
                ),
                width="100%",
                height="100%",
                padding="2em",
            ),
            width="100%",
            height="100%",
            border_radius="10px 10px 20px 20px",
            bg=rx.color("gray", 1),
            border_bottom=f"1.5px solid {rx.color('gray', 5)}",
        ),
        rx.hstack(
            rx.text("Don't have an account?", class_name="text-sm"),
            rx.text("Sign Up", class_name="text-sm font-semibold"),
            width="100%",
            justify="center",
            padding="1em",
            bg=rx.color("mauve", 2),
            border_bottom=f"1px solid {rx.color('gray', 5)}",
            spacing="1",
            height="100%",
        ),
        # rx.hstack(
        #     rx.text("Built for ", class_name="text-sm opacity-50"),
        #     rx.image(
        #         src=rx.color_mode_cond(
        #             "https://reflex.dev/logos/light/reflex.svg",
        #             "https://reflex.dev/logos/dark/reflex.svg",
        #         ),
        #         transform="scale(0.7) translateX(-4px)",
        #     ),
        #     width="100%",
        #     height="100%",
        #     justify="center",
        #     padding="1em",
        #     bg=rx.color("mauve", 2),
        #     spacing="0",
        #     overflow="hidden",
        #     **_,
        # ),
        spacing="0",
        width="100%",
        # max_width="25em",
        border_radius="20px",
        bg=rx.color("mauve", 2),
        class_name="shadow-md",
        border=f"1px solid {rx.color('gray', 5)}",
        overflow="hidden",
        height="100%",
    )
