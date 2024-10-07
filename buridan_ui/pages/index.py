import reflex as rx

from ..templates.shared.navbar import right_items, left_items

DOTS: dict = {
    "@keyframes dots": {
        "0%": {"background_position": "0 0"},
        "100%": {"background_position": "0px -100%"},
    },
    "animation": "dots 90s linear infinite",
}


def create_background():
    return (
        rx.box(
            background_size="30px 30px",
            background_image="radial-gradient(circle, hsl(0, 0%, 39%) 1px, transparent 1px)",
            mask="radial-gradient(100% 100% at 50% 100%, hsl(0, 0%, 0%, 0.85), hsl(0, 0%, 0%, 0))",
            width="100%",
            height="100%",
            position="absolute",
            **DOTS,
        ),
    )


def create_navigation():
    return rx.box(
        rx.hstack(
            left_items(),
            right_items(),
            align="center",
            justify="between",
            padding="12px 0px",
            border_bottom=f"1px solid {rx.color('slate', 7)}",
        ),
        width="100%",
        top="0",
        z_index="20",
        max_width="80em",
        position="absolute",
        padding="12px",
    )


@rx.page("/", "buridan-ui")
def index():
    return rx.vstack(
        create_navigation(),
        rx.vstack(
            rx.heading(
                "Buridan UI",
                weight="bold",
                size="2",
                letter_spacing="-1px",
                font_family="var(--chakra-fonts-serif)",
                color=rx.color("slate", 11),
            ),
            rx.heading(
                "A Component Library Built With ",
                rx.text.em("Reflex"),
                weight="bold",
                size="8",
                letter_spacing="-1px",
                font_family="var(--chakra-fonts-serif)",
                color=rx.color("slate", 12),
            ),
            width="100%",
            top="15%",
            max_width="80em",
            position="absolute",
            padding="12px",
            spacing="1",
            align="center",
            text_align="center",
        ),
        create_background(),
        width="100%",
        height="100vh",
        position="relative",
        align="center",
        justify="center",
        padding="0px 12px",
        background=rx.color("gray", 3),
    )
