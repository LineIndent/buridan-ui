import reflex as rx

from .style import MenuWrapperStyle, BaseHeaderWrapper


def blip(tag: str):
    return rx.box(
        rx.icon(tag=tag, size=12, color=rx.color("slate", 12)),
        **MenuWrapperStyle.blip,
    )


def menu_wrapper(title: str, tag: str, components: list[rx.Component] = []):
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
                spacing="1",
            ),
            *components,
        ),
        **MenuWrapperStyle.wrapper,
    )


def base_header_wrapper(
    path_name: rx.hstack,
    title: str,
    link: str,
    path: str,
) -> rx.vstack:
    return rx.vstack(
        # ... badge, title, subtitle, and link
        rx.vstack(
            path_name,
            rx.heading(title, font_weight="900", size="9"),
            rx.link(link, href=path),
            **BaseHeaderWrapper.titles,
        ),
        # ... wrapper style
        min_height="35vh",
        **BaseHeaderWrapper.wrapper,
    )
