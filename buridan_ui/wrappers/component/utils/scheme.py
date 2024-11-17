import reflex as rx

from ..state import ComponentWrapperState


def color_scheme_boxes(color: str):
    common_box_props = {
        "width": "15px",
        "height": "15px",
    }

    name_map = {
        "blue": "Fayrouz فَيْرُوز",
        "ruby": "Yaqout يَاقُوت",
        "jade": "Zumurud زُمُرُّد",
        "gray": "Hematite هَيْمَاتِيت",
    }

    return rx.hover_card.root(
        rx.hover_card.trigger(
            rx.vstack(
                rx.hstack(
                    rx.box(
                        **common_box_props,
                        bg=rx.color(color, 5),
                        border_radius="7.5px 0 0 0",
                    ),
                    rx.box(
                        **common_box_props,
                        bg=rx.color(color, 6),
                        border_radius="0 7.5px 0 0",
                    ),
                    spacing="0",
                ),
                rx.hstack(
                    rx.box(
                        **common_box_props,
                        bg=rx.color(color, 7),
                        border_radius="0 0 0 7.5px",
                    ),
                    rx.box(
                        **common_box_props,
                        bg=rx.color(color, 8),
                        border_radius="0 0 7.5px 0",
                    ),
                    spacing="0",
                ),
                spacing="0",
                padding="2.5px",
                width="32px",
                height="32px",
                cursor="pointer",
                opacity="0.71",
                _hover={
                    "opacity": "1",
                    "filter": rx.color_mode_cond(
                        "brightness(0.95)", "brightness(1.25)"
                    ),
                },
                on_click=lambda: ComponentWrapperState.toggle_theme(color),
            )
        ),
        rx.hover_card.content(
            rx.text(
                f"{name_map[color]}",
                size="1",
                color=rx.color("slate", 12),
                weight="bold",
            ),
            padding="10px",
            border_radius="6px",
        ),
    )


def component_wrapper_color_scheme():
    return rx.hstack(
        *[color_scheme_boxes(color) for color in ["blue", "ruby", "jade", "gray"]],
        spacing="1",
        align="center",
        padding=["0px 0px" if i <= 1 else "0px 24px" for i in range(6)],
    )


def component_wrapper_color_scheme_hero():
    return rx.hstack(
        *[color_scheme_boxes(color) for color in ["blue", "ruby", "jade", "gray"]],
        spacing="1",
        align="center",
    )
