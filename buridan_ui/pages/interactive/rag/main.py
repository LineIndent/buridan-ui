import reflex as rx

from .shared.profile import app_profile_panel
from .shared.chat import chat_area


def rag_ai_app() -> rx.tabs:
    return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger("User Profile Data", value="1", flex="1"),
            rx.tabs.trigger("gemini-1.5-flash", value="2", flex="1"),
        ),
        rx.tabs.content(app_profile_panel(), value="1", bg=rx.color("gray", 2)),
        rx.tabs.content(chat_area(), value="2", bg=rx.color("gray", 2)),
        default_value="1",
        width="100%",
    )
