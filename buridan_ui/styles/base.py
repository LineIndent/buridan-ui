import reflex as rx
from reflex.constants.colors import Color

ACTIVE: Color = rx.color("slate", 12)
PASSIVE: Color = rx.color("slate", 11)
BORDER: Color = rx.color("gray")


DOTS: dict = {
    "@keyframes dots": {
        "0%": {"background_position": "0 0"},
        "100%": {"background_position": "0px 100%"},
    },
    "animation": "dots 90s linear infinite",
}
