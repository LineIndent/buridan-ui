import reflex as rx


def card_v1():
    return rx.hstack(
        rx.vstack(
            rx.text(
                "Interactive User Logins",
                size="2",
                weight="bold",
                color=rx.color("slate", 12),
            ),
            rx.text(
                "Explore our intuitive and secure user login system, designed to streamline the authentication process.",
                size="2",
                weight="bold",
                color=rx.color("slate", 11),
            ),
            width="100%",
            spacing="1",
            align="start",
            justify="start",
            text_align="start",
        ),
        rx.box(
            background_size="16px 16px",
            background_image=f"radial-gradient(circle, {rx.color('gray', 12)} 1px, transparent 1px)",
            mask=f"radial-gradient(100% 100% at 100% 100%, hsl(0, 0%, 0%, 0.81), hsl(0, 0%, 0%, 0))",
            width="100%",
            height="100%",
            position="absolute",
        ),
        rx.icon(
            tag="puzzle",
            size=21,
            position="absolute",
            bottom="16px",
            right="16px",
        ),
        align="start",
        justify="start",
        position="relative",
        width="100%",
        max_width="320px",
        height="200px",
        border=f"1px solid {rx.color('gray', 6)}",
        bg=rx.color("gray", 3),
        border_radius="12px",
        padding="16px",
        overflow="hidden",
        z_index="30",
        box_shadow="0px 6px 12px 0px rgba(0, 0, 0, 0.05)",
    )
