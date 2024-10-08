import reflex as rx


def thumbnail(path: str, image: str, title: str, quantity: str, **kwargs):

    return rx.link(
        rx.vstack(
            rx.image(
                src=image,
                max_width="66%",
                max_height="60%",
                object_fit="fill",
                mask="linear-gradient(to bottom, hsl(0, 0%, 0%, 0.95) 45%, hsl(0, 0%, 0%, 0))",
                _hover={"transform": "scale(1.1)"},
                transition="all 550ms ease",
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
            border=f"1px solid {rx.color('gray', 6)}",
            position="relative",
            # width="300px",
            flex="1 1 300px",
            height="220px",
            bg=rx.color("gray", 2),
            z_index="25",
            overflow="hidden",
            spacing="0",
            border_radius="12px",
            transition="all 250ms linear",
            # _hover={
            #     "border": f"3px solid {rx.color('blue', 6)}",
            # },
        ),
        href=path,
    )
