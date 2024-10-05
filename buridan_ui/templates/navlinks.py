from ..styles.base import *
import reflex as rx


def navlinks(name: str, path: str) -> rx.link:
    return rx.link(
        rx.text(name, size="2", color=ACTIVE, _hover={"color": ""}, weight="bold"),
        href=path,
        underline="none",
    )
