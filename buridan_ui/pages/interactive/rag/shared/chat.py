import reflex as rx

from ..style import Style
from ..style import Typography
from .style import ChatAreaStyle
from ..state import State


def chat_message(data: dict[str, str]):
    return rx.vstack(
        rx.text(data["role"], size="1", weight="bold", **Typography.passive),
        rx.text(
            data["message"],
            size="2",
            weight="medium",
            line_height="1.75em",
            **Typography.active,
        ),
        spacing="2",
        width="100%",
    )


def chat_box():
    return rx.vstack(
        # ... rx.vstack => chat history and chat session
        rx.vstack(
            #
            rx.foreach(State.chat_history, chat_message),
            **ChatAreaStyle.chat_session_style,
        ),
        chat_prompt(),
        **ChatAreaStyle.chat_box,
    )


def chat_prompt():
    return rx.hstack(
        rx.box(
            rx.input(value=State.prompt, on_change=State.set_prompt, width="100%"),
            width="100%",
        ),
        rx.button("send", on_click=State.send_prompt, loading=State.is_generating),
        width="100%",
        bottom="0",
        left="0",
        position="absolute",
        padding="1em 2em",
    )


def chat_area() -> rx.vstack:
    return rx.vstack(
        rx.badge(
            rx.text("Using Google's gemini-1.5-flash model.", size="1", weight="bold"),
            **ChatAreaStyle.model_tag,
        ),
        chat_box(),
        **Style.chat_area_base,
    )
