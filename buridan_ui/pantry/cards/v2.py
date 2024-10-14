import reflex as rx

info = [
    {
        "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-1.png",
        "name": "Robert Wolfkisser",
        "job": "Engineer",
    },
    {
        "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-2.png",
        "name": "Henry Silkeater",
        "job": "Designer",
    },
    {
        "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-10.png",
        "name": "Jeremy Footviewer",
        "job": "Manager",
    },
    {
        "avatar": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-7.png",
        "name": "Jill Jailbreaker",
        "job": "Engineer",
    },
]


def item(image: str, name: str, job: str):

    return rx.vstack(
        rx.image(
            src=image,
            width="100%",
            height="100%",
            object_fit="fit",
            transition="all 550ms ease",
            _hover={"transform": "scale(1.1)"},
            mask="linear-gradient(to bottom, hsl(0, 0%, 0%, 0.95) 45%, hsl(0, 0%, 0%, 0))",
        ),
        rx.vstack(
            rx.text(name, size="2", weight="bold", color=rx.color("slate", 12)),
            rx.text(
                job,
                size="2",
                weight="bold",
                color=rx.color("slate", 10),
            ),
            position="absolute",
            bottom="0",
            left="0",
            bg=rx.color("gray", 3),
            width="100%",
            padding="12px 18px",
            spacing="0",
            justify="between",
        ),
        align="center",
        justify="center",
        position="relative",
        flex="1 1 auto 1",
        height="220px",
        border=f"1px solid {rx.color('gray', 6)}",
        bg=rx.color("gray", 2),
        border_radius="12px",
        overflow="hidden",
        spacing="0",
        transition="all 250ms linear",
    )


def card_v2():
    return rx.hstack(
        *[item(data["avatar"], data["name"], data["job"]) for data in info],
        width="100%",
        flex_wrap="wrap",
        justify="center",
    )
