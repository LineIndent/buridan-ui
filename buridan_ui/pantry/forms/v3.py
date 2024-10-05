import reflex as rx


data = [
    {
        "title": "Messages",
        "description": "Direct messages you have received from other users",
    },
    {
        "title": "Review requests",
        "description": "Code review requests from your team members",
    },
    {
        "title": "Comments",
        "description": "Daily digest with comments on your posts",
    },
    {
        "title": "Recommendations",
        "description": "Digest with best community posts from previous week",
    },
]


def forms_v3():
    return rx.vstack(
        rx.vstack(
            rx.heading("Configure notifications", size="2", color="hsl(0 0% 75%)"),
            rx.text(
                "Choose what notifications you want to receive",
                font_size="10px",
                color="hsl(0 0% 60%)",
            ),
            spacing="1",
        ),
        *list(
            map(
                lambda item: rx.hstack(
                    rx.vstack(
                        rx.heading(
                            item["title"],
                            size="1",
                            color="hsl(0 0% 80%)",
                            weight="medium",
                        ),
                        rx.text(
                            item["description"],
                            font_size="10px",
                            color="hsl(0 0% 60%)",
                        ),
                        spacing="1",
                    ),
                    rx.switch(),
                    width="100%",
                    align="center",
                    justify="between",
                    padding="5px 0px",
                ),
                data,
            )
        ),
        max_width="26em",
        width="100%",
        padding="1em",
        bg="hsla(0, 0%, 15%, 0.81)",
        border_radius="10px",
        border="1px solid hsla(0, 0%, 45%, 0.5)",
    )
