import reflex as rx


def thumbnail(path: str, image: str, title: str, quantity: str, **kwargs):

    return rx.link(
        rx.vstack(
            rx.image(
                src=image,
                max_width="66%",
                max_height="60%",
                object_fit="fill",
                transition="all 550ms ease",
                _hover={"transform": "scale(1.1)"},
                mask="linear-gradient(to bottom, hsl(0, 0%, 0%, 0.95) 45%, hsl(0, 0%, 0%, 0))",
                **kwargs,
            ),
            rx.vstack(
                rx.text(title, size="2", weight="bold", color=rx.color("slate", 12)),
                rx.text(
                    # quantity,
                    (
                        f"{quantity} component"
                        if quantity == "1"
                        else f"{quantity} components"
                    ),
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
            flex="1 1 300px",
            height="220px",
            border=f"1px solid {rx.color('gray', 6)}",
            bg=rx.color("slate", 2),
            border_radius="12px",
            z_index="25",
            overflow="hidden",
            spacing="0",
            transition="all 250ms linear",
        ),
        href=path,
    )
