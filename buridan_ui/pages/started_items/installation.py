import reflex as rx
from ...wrappers.base import base
from ...pantry.timeline.v1 import blip


def wrapper(title: str, instructions: str, components=None, **kwargs):
    if components is None:
        components = []
    return rx.hstack(
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    blip(),
                    rx.text(
                        title, size="2", weight="medium", color=rx.color("slate", 11)
                    ),
                    align="center",
                ),
                rx.text(
                    instructions, size="3", weight="bold", color=rx.color("slate", 12)
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
            font_size="13px",
            language="markup",
            wrap_long_lines=True,
            scrollbar_width="none",
            code_tag_props={"pre": "transparent"},
            custom_style={"color": rx.color("gray", 12)},
        ),
        rx.button(
            rx.icon(tag="file", size=15),
            color_scheme="gray",
            variant="ghost",
            size="2",
            on_click=[
                rx.toast.success("Code copied!"),
                rx.set_clipboard(code_string),
            ],
            cursor="pointer",
            position="absolute",
            right="2%",
        ),
        width="100%",
        align="center",
        position="relative",
    )


@base(
    "/getting-started/installation",
    "Installation Setup",
    title="Installation - buridan/ui",
)
def installation():
    return [
        rx.box(
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
                            size="3",
                            weight="bold",
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
                max_width="50em",
                width="100%",
                spacing="9",
                position="relative",
                border_left=f"1px solid {rx.color('gray')}",
            ),
            width="100%",
            display="flex",
            justify_content="center",
            padding="0px 14px",
        )
    ]
