import reflex as rx

from .style import MenuWrapperStyle


def blip(tag: str):
    return rx.box(
        rx.icon(tag=tag, size=12, color=rx.color("slate", 12)),
        **MenuWrapperStyle.blip,
    )


def menu_wrapper(title: str, date: str, tag: str, components: list[rx.Component] = []):
    return rx.hstack(
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    blip(tag),
                    rx.text(
                        title, size="4", weight="bold", color=rx.color("slate", 11)
                    ),
                    align="center",
                ),
                # ... can switch the date with the title to show last update
                # rx.text(date, size="1", weight="bold", color=rx.color("slate", 10)),
                spacing="1",
            ),
            *components,
        ),
        **MenuWrapperStyle.wrapper,
    )
