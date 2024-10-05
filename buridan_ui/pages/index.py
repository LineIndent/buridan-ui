import reflex as rx

from ..templates.shared.navbar import navbar

css_dict = {
    "background-image": [
        "linear-gradient(45deg, #f9fafb 25%, transparent 0)",
        "linear-gradient(-45deg, #f9fafb 25%, transparent 0)",
        "linear-gradient(45deg, transparent 75%, #f9fafb 0)",
        "linear-gradient(-45deg, transparent 75%, #f9fafb 0)",
    ],
    "background-size": "20px 20px",
}


@rx.page("/", "Home")
def index():
    return rx.vstack(
        navbar(),
        width="100%",
        height="100vh",
        **css_dict,
    )
