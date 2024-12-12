import reflex as rx


def text_wrapper(title: str, description: str):
    return rx.vstack(
        rx.hstack(
            rx.text(
                title,
                size="3",
                weight="medium",
                color=rx.color("slate", 12),
            ),
            align="center",
        ),
        rx.text(description, size="2", color=rx.color("slate", 11), weight="regular"),
        spacing="2",
        line_height="2px",
    )


def introduction():
    return rx.box(
        rx.vstack(
            text_wrapper(
                "Introduction",
                "Welcome to a collection of beautifully designed components that you can seamlessly integrate into your applications. Accessible, customizable, and completely open source.",
            ),
            text_wrapper(
                "What makes this different?",
                "This isn’t just another component library. Rather than installing a package or adding a dependency through pip, you’ll find a curated selection of reusable components that you can easily copy and paste directly into your projects.",
            ),
            text_wrapper(
                "How does it work?",
                "Simply choose the components you need, copy the code, and customize it to suit your unique requirements. The code is yours to modify and enhance as you see fit.",
            ),
            text_wrapper(
                "",
                "Check out the installation section for more details.",
            ),
            text_wrapper(
                "",
                "Think of this as a valuable reference to inspire and guide you in building your own component libraries. Happy coding!",
            ),
            max_width="40em",
            width="100%",
            spacing="6",
        ),
        width="100%",
        display="flex",
        justify_content="center",
    )
