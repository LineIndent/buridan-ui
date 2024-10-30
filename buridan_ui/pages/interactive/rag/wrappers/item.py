import reflex as rx

from .style import AppProfileWrapperStyle


def blip():
    return rx.box(
        rx.icon(tag="info", size=11, color=rx.color("slate", 10)),
        **AppProfileWrapperStyle.blip,
    )


def app_profile_item_wrapper(
    title: str, date: str, components: list[rx.Component] = []
):
    return rx.hstack(
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    blip(),
                    rx.text(date, size="1", weight="bold", color=rx.color("slate", 10)),
                    align="center",
                ),
                rx.text(title, size="3", weight="bold", color=rx.color("slate", 11)),
                spacing="1",
            ),
            *components,
            width="100%",
        ),
        **AppProfileWrapperStyle.wrapper,
    )
