import reflex as rx

from ..templates.shared.navbar import navbar


@rx.page("/", "Home")
def index():
    return rx.vstack(navbar(), width="100%", height="100vh")
