import reflex as rx
from reflex.components.datadisplay.code import Theme

from buridan_ui.pantry.timeline.v1 import blip


def wrapper(title: str, instructions: str, components=None, **kwargs):
    if components is None:
        components = []
    return rx.hstack(
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    blip(),
                    rx.text(
                        title,
                        size="1",
                        weight="bold",
                        color=rx.color("slate", 11),
                    ),
                    align="center",
                ),
                rx.text(
                    instructions,
                    size="2",
                    weight="regular",
                    color=rx.color("slate", 12),
                ),
                width="100%",
                spacing="1",
            ),
            *components,
            width="100%",
        ),
        width="100%",
        align="start",
        justify="start",
        padding_left="15px",
        border_radius="0px 5px 5px 0px",
        **kwargs,
    )


def create_code_line(code_string: str):
    return rx.hstack(
        rx.code_block(
            code_string,
            width="100%",
            font_size="12px",
            language="markdown",
            theme=Theme.one_dark,
            wrap_long_lines=True,
            scrollbar_width="none",
        ),
        rx.button(
            rx.icon(tag="file", size=13),
            color="white",
            variant="ghost",
            size="1",
            on_click=[rx.set_clipboard(code_string)],
            cursor="pointer",
            position="absolute",
            right="2%",
        ),
        width="100%",
        align="center",
        position="relative",
    )


def installation():
    return rx.box(
        rx.vstack(
            wrapper(
                "Step 1: Check your Python version",
                "To use Reflex you need to have Python version 3.9 or above installed on your system.",
                [create_code_line("python3 --version")],
            ),
            wrapper(
                "Step 2: PIP install the Reflex framework",
                "Use the following command to install Reflex:",
                [
                    create_code_line("pip3 install reflex"),
                    rx.text(
                        "Male sure the latest version of Reflex is installed",
                        size="2",
                        weight="regular",
                        color=rx.color("slate", 12),
                    ),
                    create_code_line("reflex --version"),
                ],
            ),
            wrapper(
                "Step 3: Create a new Reflex Web Application",
                "Inside your root directory, run the following command to create a new app:",
                [create_code_line("reflex init")],
            ),
            wrapper(
                "Step 4: Copy & paste a pantry item directly into your app",
                "You can now easily integrate pantry pantry within your app and personalize them.",
            ),
            max_width="40em",
            width="100%",
            spacing="9",
            position="relative",
            border_left=f"0.75px solid {rx.color('gray', 5)}",
        ),
        width="100%",
        display="flex",
        justify_content="center",
    )
