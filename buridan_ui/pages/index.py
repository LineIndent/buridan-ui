import asyncio

import reflex as rx
from reflex import color

from ..templates.shared.navbar import right_items, left_items
from .thumbnail_items.exports import export_thumbnail


def wrapper(title: str, instructions: str, tag: str):

    return rx.hstack(
        rx.vstack(
            rx.text(title, size="2", weight="bold", color=rx.color("slate", 12)),
            rx.text(instructions, size="2", weight="bold", color=rx.color("slate", 11)),
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
            tag=tag,
            size=26,
            position="absolute",
            bottom="16px",
            right="16px",
        ),
        align="start",
        justify="start",
        position="relative",
        flex="1 1 300px",
        height="220px",
        border=f"1px solid {rx.color('gray', 6)}",
        bg=rx.color("gray", 3),
        border_radius="12px",
        padding="16px",
        overflow="hidden",
        z_index="30",
        box_shadow="0px 6px 12px 0px rgba(0, 0, 0, 0.05)",
    )


DOTS: dict = {
    "@keyframes dots": {
        "0%": {"background_position": "0 0"},
        "100%": {"background_position": "0px 100%"},
    },
    "animation": "dots 90s linear infinite",
}


def create_background(pos_x: str, pos_y: str):
    return rx.box(
        background_size="90px 90px",
        background_image=(
            "linear-gradient(hsl(0, 0%, 39%) 1px, transparent 1px), "
            "linear-gradient(to right, transparent 99%, hsl(0, 0%, 39%) 100%)"
        ),
        mask=(
            "radial-gradient(25% 25% at 75% 75%, hsl(0, 0%, 0%, 0.75), hsl(0, 0%, 0%, 0)), "  # Original mask
            "radial-gradient(45% 45% at 50% 50%, hsl(0, 0%, 0%, 0.60), hsl(0, 0%, 0%, 0)), "
            "radial-gradient(30% 50% at 50% 50%, hsl(0, 0%, 0%, 0.5), hsl(0, 0%, 0%, 0)), "  # Inner gradient for depth
            "radial-gradient(60% 70% at 50% 50%, hsl(0, 0%, 0%, 0.35), hsl(0, 0%, 0%, 0))"
            # Outer gradient for a subtle fade
        ),
        width="100%",
        height="100%",
        position="absolute",
        z_index="1",
    )


def create_navigation():
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.image(
                    src="/logo.jpg",
                    width="28px",
                    height="28px",
                    border_radius="15%",
                    object_fit="fit",
                    border=f"1px solid {rx.color('slate', 12)}",
                ),
                left_items(),
                align="center",
                padding="0px 14px",
            ),
            right_items(),
            align="center",
            justify="between",
            padding="18px 0px",
            backdrop_filter="blur(4px)",
            max_width="75em",
            width="100%",
        ),
        width="100%",
        z_index="20",
        max_width="75em",
        position="relative",  # Change to relative
        justify_content="center",
        padding="12px 0",  # Optional: add some padding for breathing space
    )


class Animate(rx.State):
    can_show: str = "0"
    width: str = "0px"

    icon: str = (
        "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLWNsaXBib2FyZC1saXN0Ij48cmVjdCB3aWR0aD0iOCIgaGVpZ2h0PSI0IiB4PSI4IiB5PSIyIiByeD0iMSIgcnk9IjEiLz48cGF0aCBkPSJNMTYgNGgyYTIgMiAwIDAgMSAyIDJ2MTRhMiAyIDAgMCAxLTIgMkg2YTIgMiAwIDAgMS0yLTJWNmEyIDIgMCAwIDEgMi0yaDIiLz48cGF0aCBkPSJNMTIgMTFoNCIvPjxwYXRoIGQ9Ik0xMiAxNmg0Ii8+PHBhdGggZD0iTTggMTFoLjAxIi8+PHBhdGggZD0iTTggMTZoLjAxIi8+PC9zdmc+"
    )

    async def toggle_preview(self):
        self.icon = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLWNoZWNrIj48cGF0aCBkPSJNMjAgNiA5IDE3bC01LTUiLz48L3N2Zz4="
        yield
        await asyncio.sleep(1)
        self.icon = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLWNsaXBib2FyZC1saXN0Ij48cmVjdCB3aWR0aD0iOCIgaGVpZ2h0PSI0IiB4PSI4IiB5PSIyIiByeD0iMSIgcnk9IjEiLz48cGF0aCBkPSJNMTYgNGgyYTIgMiAwIDAgMSAyIDJ2MTRhMiAyIDAgMCAxLTIgMkg2YTIgMiAwIDAgMS0yLTJWNmEyIDIgMCAwIDEgMi0yaDIiLz48cGF0aCBkPSJNMTIgMTFoNCIvPjxwYXRoIGQ9Ik0xMiAxNmg0Ii8+PHBhdGggZD0iTTggMTFoLjAxIi8+PHBhdGggZD0iTTggMTZoLjAxIi8+PC9zdmc+"


@rx.page("/", "buridan-ui")
def index():
    return rx.vstack(
        create_navigation(),
        rx.vstack(
            rx.divider(height="4em", opacity="0"),
            rx.hstack(
                rx.heading(
                    "Buridan UI",
                    weight="bold",
                    size="2",
                    letter_spacing="-1px",
                    font_family="var(--chakra-fonts-serif)",
                    color=rx.color("slate", 11),
                ),
                rx.separator(orientation="vertical", width="1.25px", height="30px"),
                *[
                    rx.badge(
                        rx.heading(
                            name,
                            size="2",
                            letter_spacing="-1px",
                            font_family="var(--chakra-fonts-serif)",
                            color=rx.color("slate", 11),
                        ),
                        variant="surface",
                        color_scheme="gray",
                    )
                    for name in ["Accessible", "Modern", "Open Source"]
                ],
                align="center",
                backdrop_filter="blur(24px)",
                z_index="20",
            ),
            rx.heading(
                "A Component Library Built With ",
                rx.text.em("Reflex"),
                weight="bold",
                size="9",
                font_family="var(--chakra-fonts-serif)",
                color=rx.color("slate", 12),
            ),
            rx.text(
                "Speed up your development with ready-made components designed for seamless integration. Create stunning applications effortlessly!",
                size="5",
                weight="medium",
                color=rx.color("slate", 11),
                max_width="45em",
                align="center",
            ),
            rx.hstack(
                rx.button(
                    "Getting Started",
                    variant="surface",
                    color_scheme="gray",
                    flex="4",
                    size="3",
                    z_index="20",
                ),
                rx.button(
                    "Pantry",
                    variant="soft",
                    color_scheme="gray",
                    flex="2",
                    size="3",
                    z_index="20",
                ),
                width="100%",
                max_width="20em",
                justify="center",
                padding="24px 0px",
            ),
            rx.divider(height="12em", opacity="0"),
            rx.vstack(
                rx.heading(
                    "Components Entirely Built With Reflex",
                    weight="bold",
                    size="8",
                    font_family="var(--chakra-fonts-serif)",
                    color=rx.color("slate", 12),
                ),
                rx.text(
                    "A full-stack framework complete with built-in features, including a comprehensive theming system, ready-to-use UI components, and customizable elements.",
                    size="4",
                    weight="medium",
                    color=rx.color("slate", 11),
                    max_width="60em",
                ),
                width="100%",
                text_align="start",
                padding="14px 0px",
            ),
            rx.hstack(
                wrapper(
                    "Fully Customizable Components",
                    "Easily adjust colors, fonts, and styles to create a unique look that enhances your application's user experience.",
                    "component",
                ),
                wrapper(
                    "Light & Dark Mode",
                    "Component Theming offers ready-to-use light and dark modes, allowing you to switch seamlessly between styles.",
                    "sun-moon",
                ),
                wrapper(
                    "Open Source License",
                    "Our components are available under an open source license, empowering you to use, modify, and share them freely.",
                    "code",
                ),
                width="100%",
                display="grid",
                gap="2rem",
                grid_template_columns=[
                    "repeat(1, minmax(0, 1fr))",
                    "repeat(1, minmax(0, 1fr))",
                    "repeat(2, minmax(0, 1fr))",
                    "repeat(3, minmax(0, 1fr))",
                    "repeat(3, minmax(0, 1fr))",
                ],
                padding="18px 0px",
            ),
            rx.divider(height="10em", opacity="0"),
            rx.vstack(
                rx.heading(
                    "Reflex Components",
                    weight="bold",
                    size="8",
                    font_family="var(--chakra-fonts-serif)",
                    color=rx.color("slate", 12),
                ),
                rx.text(
                    "Built on the Reflex framework, our components provide a set of prebuilt UI elements that streamline the development of responsive, web-based applications. Easily customize and adapt them to fit your unique design needs.",
                    size="4",
                    weight="medium",
                    color=rx.color("slate", 11),
                    max_width="60em",
                ),
                width="100%",
                text_align="start",
                padding="14px 0px",
            ),
            rx.hstack(
                *export_thumbnail,
                width="100%",
                display="grid",
                gap="1rem",
                grid_template_columns=[
                    "repeat(2, minmax(0, 1fr))",
                    "repeat(2, minmax(0, 1fr))",
                    "repeat(3, minmax(0, 1fr))",
                    "repeat(4, minmax(0, 1fr))",
                    "repeat(4, minmax(0, 1fr))",
                ],
                min_height="100vh",
                padding="18px 0px",
            ),
            rx.divider(height="10em", opacity="0"),
            rx.vstack(
                rx.heading(
                    "You're One Step Away From Shipping Your Web Application",
                    weight="bold",
                    size="8",
                    font_family="var(--chakra-fonts-serif)",
                    color=rx.color("slate", 12),
                ),
                rx.text(
                    "Download and install Reflex to start building out your idea, or check our the get started pages for more information.",
                    size="4",
                    weight="medium",
                    color=rx.color("slate", 11),
                    max_width="60em",
                ),
                width="100%",
                text_align="start",
                padding="14px 0px",
            ),
            rx.box(
                rx.hstack(
                    rx.button(
                        "Get Started",
                        variant="surface",
                        color_scheme="gray",
                        flex="3",
                        size="4",
                        z_index="20",
                    ),
                    rx.button(
                        "pip install reflex",
                        rx.separator(
                            orientation="vertical", width="1.25px", height="25px"
                        ),
                        rx.image(
                            src=Animate.icon,
                            size=14,
                            color=rx.color("slate", 12),
                            filter="invert(0.81)",
                        ),
                        variant="soft",
                        color_scheme="gray",
                        flex="5",
                        size="4",
                        z_index="20",
                        display="flex",
                        justify_content="space-between",
                        cursor="pointer",
                        on_click=Animate.toggle_preview,
                    ),
                    max_width="25em",
                    justify="start",
                    padding="24px 0px",
                ),
                width="100%",
            ),
            rx.divider(height="10em", opacity="0"),
            rx.vstack(
                rx.text(),
                width="100%",
                height="30em",
                bg=rx.color("gray", 1, True),
            ),
            width="100%",
            padding="12px",
            spacing="1",
            align="center",
            justify="start",
            text_align="center",
            z_index="50",
            max_width="75em",
        ),
        create_background("100%", "100%"),
        width="100%",
        min_height="100vh",  # Change this to allow it to grow
        overflow="scroll",  # Keep this to allow for internal scrolling
        align="center",
        justify="start",
        padding="0px 12px",
        background=rx.color("gray", 3),
    )
