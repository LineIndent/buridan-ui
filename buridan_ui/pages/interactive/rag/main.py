import reflex as rx

from .shared.navigation import app_navigation_bar, title
from .shared.profile import app_profile_panel
from .shared.chat import chat_area

from .style import Style

from ....wrappers.base import base


@base(
    "/interactive/retrieval-augmented-generation",
    "Get Fit.ai",
    title="RAG - buridan/ui",
)
def rag_ai_app():
    return [
        rx.vstack(
            # ... navigation bar
            app_navigation_bar(),
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
