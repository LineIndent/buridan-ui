import reflex as rx

from .style import ThumbnailStyle


def pantry_thumbnail(path: str, image: str, title: str, quantity: str, **kwargs):

    return rx.link(
        rx.vstack(
            rx.image(src=image, **ThumbnailStyle.image, **kwargs),
            rx.vstack(
                rx.text(title, size="2", weight="Medium", color=rx.color("slate", 12)),
                rx.text(
                    (
                        f"{quantity} component"
                        if quantity == "1"
                        else f"{quantity} components"
                    ),
                    size="1",
                    weight="regular",
                    color=rx.color("slate", 10),
                ),
                **ThumbnailStyle.container,
            ),
            **ThumbnailStyle.base,
        ),
        href=path,
    )
