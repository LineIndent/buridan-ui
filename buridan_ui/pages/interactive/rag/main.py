import reflex as rx

from .shared.profile import app_profile_panel
from .shared.chat import chat_area

from .style import Style

from ....wrappers.base import base


@base(
    "/interactive/retrieval-augmented-generation",
    "Get Fit AI Application",
    title="RAG - buridan/ui",
)
def rag_ai_app() -> list[rx.Component]:
    return [
        rx.vstack(
            # ... main content area
            rx.hstack(
                app_profile_panel(),
                chat_area(),
                **Style.content,
            ),
            # ... base component style props
            # ... ... imported from main style page
            **Style.base,
        )
    ]
