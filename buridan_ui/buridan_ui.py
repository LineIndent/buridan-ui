import reflex as rx
from .pages import *

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap",
    ],
    style={
        rx.heading: {"font_family": "Inter"},
        rx.text: {"font_family": "Inter"},
    },
)
